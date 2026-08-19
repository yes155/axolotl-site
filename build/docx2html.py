# -*- coding: utf-8 -*-
"""
docx -> clean HTML converter.

Handles the mixed formats found in the source articles:
  - Markdown-style articles (# headings, **bold**, | tables |, "- " lists, > blockquote)
  - Word-style articles (bold short paragraphs = headings, real tables, numbered lists)
  - SEO meta blocks (Title Tag: / H1: / Meta Description: lines)
  - Junk "AI drafting" paragraphs that must be stripped
"""
import re
import html as _html
from docx import Document
from docx.table import Table
from docx.text.paragraph import Paragraph
from docx.oxml.ns import qn

# ---------------------------------------------------------------------------
# helpers
# ---------------------------------------------------------------------------

JUNK_STARTS = (
    "perfect.", "perfect !", "perfect!",
    "i went through the gap analysis",
    "we'll rebuild it",
    "let's rebuild",
    "here's the rebuilt",
    "site audit",
)
JUNK_WORDS = ("gap analysis", "under 2,500 words", "increasing information density",
              "we'll rebuild", "rebuilt the article", "draft complete")


def looks_like_junk(text):
    t = text.lower().strip()
    if not t:
        return False
    if t.startswith(JUNK_STARTS):
        return True
    # Very short AI prompts / QA notes
    if len(t) < 25 and ("rebuild" in t or "draft" in t or "word count" in t):
        return True
    return False


def is_meta_line(text):
    return bool(re.match(r"^(title tag|h1|meta description|focus keyword|primary keyword|secondary keyword|primary entity|secondary entity|supporting entity|adjacent entity|url|slug|macro context|central entity|search volume|buyer stage|competition|search activities|representative query)\s*:", text, re.I))


def strip_markdown_inline(text):
    """Convert **bold**, *italic*, and backtick code to HTML inline."""
    text = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", text)
    text = re.sub(r"(?<!\*)\*([^*]+?)\*(?!\*)", r"<em>\1</em>", text)
    text = re.sub(r"`([^`]+)`", r"<code>\1</code>", text)
    return text


def clean_text(text):
    """Normalise spaces but keep unicode."""
    text = text.replace("\u00a0", " ")
    return text


def cell_text(cell):
    t = cell.text.strip()
    t = re.sub(r"\s*\n\s*", " ", t)
    return strip_markdown_inline(t)


# ---------------------------------------------------------------------------
# markdown (pipe) table parser
# ---------------------------------------------------------------------------

def parse_pipe_table(lines):
    """lines: list of raw paragraph strings that start with |"""
    rows = []
    for ln in lines:
        ln = ln.strip()
        if not ln.startswith("|"):
            continue
        cells = [c.strip() for c in ln.strip("|").split("|")]
        rows.append(cells)
    if not rows:
        return None
    # drop separator row |---|---|
    rows = [r for r in rows if not all(re.fullmatch(r":?-{2,}:?", c) for c in r if c)]
    if not rows:
        return None
    return rows


def render_table(rows, header=True):
    ncol = max(len(r) for r in rows)
    out = ['<div class="table-wrap"><table>']
    if header and rows:
        out.append("<thead><tr>" + "".join(f"<th>{c}</th>" for c in rows[0][:ncol]) + "</tr></thead>")
        body = rows[1:]
    else:
        body = rows
    out.append("<tbody>")
    for r in body:
        out.append("<tr>" + "".join(f"<td>{c}</td>" for c in r[:ncol]) + "</tr>")
    out.append("</tbody></table></div>")
    return "\n".join(out)


def render_docx_table(table):
    rows = []
    for r in table.rows:
        rows.append([cell_text(c) for c in r.cells])
    if not rows:
        return ""
    return render_table(rows, header=True)


# ---------------------------------------------------------------------------
# Grid recovery (reading-density): some source docs encode markdown pipe tables
# as a run of short cell paragraphs + one "---" paragraph per column, because
# the pipes were stripped in the original AI-drafted docx. Those render as a
# wall of tiny <p> blocks today; rebuild them into real <table>s.
# ---------------------------------------------------------------------------

_GRID_CELL = r"<p>([^<>]{1,100})</p>"

GRID_RE = re.compile(
    r"(?P<head>(?:%s){2,})"
    r"(?P<sep>(?:<hr>){2,})"
    r"(?P<body>(?:%s)+)" % (_GRID_CELL, _GRID_CELL),
    re.S,
)


def _grid_columns(cells, ncols):
    return [cells[i:i + ncols] for i in range(0, len(cells) - (len(cells) % ncols), ncols)]


def recover_grid_tables(html):
    """Rebuild flattened pipe-grids (header cells + N <hr> separators + row
    cells) into a real table. Only fires when the shape is unambiguous:
    every cell is a short plain paragraph, the separator count fixes the
    column count, and the body is a clean multiple of that count."""
    def repl(m):
        head = re.findall(_GRID_CELL, m.group("head"))
        ncols = m.group("sep").count("<hr>")
        body = re.findall(_GRID_CELL, m.group("body"))
        if ncols < 2 or len(head) != ncols or len(body) < ncols:
            return m.group(0)
        # Trailing body cells that don't fit the grid are left as <p>s.
        full_rows = len(body) // ncols * ncols
        rows = [head] + _grid_columns(body[:full_rows], ncols)
        trailing = body[full_rows:]
        table = render_table(rows, header=True)
        trail_html = "".join(f"<p>{c}</p>" for c in trailing)
        return table + trail_html
    return GRID_RE.sub(repl, html)


def recover_glued_param_table(html):
    """One known case (diet/best-foods-list): a pipe table whose cells were
    glued into a single paragraph with no separators. Split it back on the
    row labels and the "ParameterSafe RangeWhy It Matters" camel header."""
    glued = ("ParameterSafe RangeWhy It Matters"
             "Ammonia (NH3)0 ppmToxic above 1 ppm; produced by waste and uneaten food"
             "Nitrite (NO2)0 ppmProduced as bacteria break down ammonia; toxic at low levels"
             "Nitrate (NO3)Below 20\u201340 ppmLess toxic but still harmful at high concentrations"
             "Temperature60\u201368\u00b0F (15\u201320\u00b0C)Above 72\u201375\u00b0F (22\u201324\u00b0C) "
             "stresses metabolism and immune function")
    if glued not in html:
        return html
    header = ["Parameter", "Safe Range", "Why It Matters"]
    rows = [
        ["Ammonia (NH3)", "0 ppm", "Toxic above 1 ppm; produced by waste and uneaten food"],
        ["Nitrite (NO2)", "0 ppm", "Produced as bacteria break down ammonia; toxic at low levels"],
        ["Nitrate (NO3)", "Below 20\u201340 ppm", "Less toxic but still harmful at high concentrations"],
        ["Temperature", "60\u201368\u00b0F (15\u201320\u00b0C)",
         "Above 72\u201375\u00b0F (22\u201324\u00b0C) stresses metabolism and immune function"],
    ]
    table = render_table([header] + rows, header=True)
    return re.sub(rf"<p>{re.escape(glued)}</p>", table, html)


def recover_glued_food_table(html):
    """Known case (diet/best-foods-list): a 5-column food-format comparison
    (Format / Nutrient Bioavailability / Disease Risk / Digestibility /
    Storage) glued into a single paragraph. Rebuild the real table."""
    glued = ("FormatNutrient BioavailabilityDisease RiskDigestibilityStorage"
             "Live (earthworms, blackworms)HighestLow if sourced wellHigh"
             "Requires a worm bin or refrigeration"
             "Frozen (bloodworms, brine shrimp)MediumVery lowMedium"
             "Freezer, months-long shelf life"
             "PelletsMedium (protein-controlled)LowestMedium-high if soft"
             "Dry storage, long shelf life")
    if glued not in html:
        return html
    header = ["Format", "Nutrient Bioavailability", "Disease Risk",
              "Digestibility", "Storage"]
    rows = [
        ["Live (earthworms, blackworms)", "Highest", "Low if sourced well",
         "High", "Requires a worm bin or refrigeration"],
        ["Frozen (bloodworms, brine shrimp)", "Medium", "Very low", "Medium",
         "Freezer, months-long shelf life"],
        ["Pellets", "Medium (protein-controlled)", "Lowest",
         "Medium-high if soft", "Dry storage, long shelf life"],
    ]
    table = render_table([header] + rows, header=True)
    return re.sub(rf"<p>{re.escape(glued)}</p>", table, html)


# Standalone prose labels in the body that are clearly sub-section headings
# (e.g. food names in the diet guide) but were authored as plain short
# paragraphs. Promote them to <h3> so long flat runs split into scannable
# sections. Keyed on the exact paragraph text to stay surgical.
PROSE_H3_LABELS = [
    "What Are the Best Foods for Axolotls?",
    "Earthworms (Nightcrawlers, Red Wigglers, Dendrobaena)",
    "Blackworms",
    "Bloodworms",
    "Brine Shrimp and Daphnia",
    "Axolotl and Salmon Pellets",
    "Feeding by Life Stage",
    "Hatchlings (Under 3 Inches)",
    "Juveniles (3\u20136 Inches)",
    "Subadults (6\u20139 Inches)",
    "Adults (9+ Inches)",
]

def recover_prose_headings(html):
    """Promote known standalone sub-heading labels from <p> to <h3>."""
    for text in PROSE_H3_LABELS:
        html = re.sub(
            rf"<p>{re.escape(text)}</p>",
            f"<h3>{text}</h3>",
            html)
    return html


# Per-article editorial structure overrides, keyed by slug. These handle
# reading-density cases too surgical for a generic rule: splitting prose
# lead-ins ("Stage 1 — ...", "Step 1 — ...") into headings/lists so a long
# flat run of paragraphs becomes scannable structure.
def article_body_overrides(slug, html):
    if slug == "tank-setup/water-parameters-cycling":
        html = _wpc_overrides(html)
    elif slug == "tank-setup/temperature":
        html = _temp_overrides(html)
    elif slug == "tank-setup/water-conditioners":
        html = _wc_overrides(html)
    elif slug == "diet/live-vs-frozen-food":
        html = _lvff_overrides(html)
    elif slug == "tank-setup/substrate-and-impaction":
        html = _sub_overrides(html)
    return html


def _split_prose_leads(html, leads):
    """Turn '<p>LEAD. body</p>' into '<h3>LEAD</h3><p>body</p>' for each lead."""
    for lead in leads:
        html = re.sub(
            rf"<p>{re.escape(lead)}\. (.*?)</p>",
            f"<h3>{lead}</h3>\n<p>\\1</p>",
            html, flags=re.S)
    return html


_WPC_STAGE_LEADS = [
    "Stage 1 \u2014 Ammonia to Nitrite",
    "Stage 2 \u2014 Nitrite to Nitrate",
]

# GH/KH explainer leads -> H3 sub-headings inside the "What Do GH and KH Mean"
# section, splitting a long flat run into definition chunks.
_WPC_HARDNESS_LEADS = [
    "GH \u2014 General Hardness",
    "KH \u2014 Carbonate Hardness",
]

_WPC_STEPS = [
    "Step 1 \u2014 Tub the axolotl immediately",
    "Step 2 \u2014 Add Seachem Prime at double dose to the main tank",
    "Step 3 \u2014 Identify and remove the ammonia source",
    "Step 4 \u2014 Protect and restore the bacterial colony",
    "Step 5 \u2014 Test and decide on fridging",
]

# Ammonia-spike causes introduced as "in order of frequency" (source doc has a
# bold topic lead per cause). Rendered flat; grouped into the ordered list the
# wording calls for. Keyed on the first words of each paragraph.
_WPC_CAUSES = [
    "Overfeeding is the most common cause",
    "Axolotl waste output itself is significant",
    "Dead organic matter \u2014 waste buried",
    "Filter damage from cleaning media",
    "New tank syndrome (no established bacterial colony)",
    "KH depletion (old tank syndrome)",
]

# Nitrogen-cycle crash causes ("The five most common causes of nitrogen cycle
# crashes…"); each paragraph has a bold topic lead in the source.
_WPC_CRASHES = [
    "Replacing all filter media at once",
    "Cleaning filter media with tap water",
    "Medications and antibiotics",
    "Power outages",
    "Overstocking",
]

# Ammonia-spike prevention foundations ("The four foundations…"); bold lead
# per paragraph.
_WPC_PREVENTION = [
    "Complete fishless cycling",
    "Weekly water testing",
    "Consistent water change schedule",
    "Filter media preservation",
]


def _wpc_overrides(html):
    # 1. Stage lead-ins -> H3
    html = _split_prose_leads(html, _WPC_STAGE_LEADS)
    # 1b. GH/KH definition leads -> H3. These read "<p>GH — General Hardness
    # measures …</p>"; the em-dash lead is the sub-heading.
    for lead in _WPC_HARDNESS_LEADS:
        html = re.sub(
            rf"<p>{re.escape(lead)}( measures| is)(.*?)</p>",
            f"<h3>{lead}</h3>\n<p>\\1\\2</p>",
            html, count=1, flags=re.S)
    # 2. The 5-step emergency response -> ordered list. Each source paragraph
    # reads "<p>Step N — title. body</p>"; rebuild as one <ol>.
    parts = []
    for lead in _WPC_STEPS:
        m = re.search(rf"<p>{re.escape(lead)}\. (.*?)</p>", html, flags=re.S)
        if m:
            parts.append(f"<li><strong>{lead}.</strong> {m.group(1)}</li>")
    if len(parts) == len(_WPC_STEPS):
        for lead in _WPC_STEPS:
            html = re.sub(rf"<p>{re.escape(lead)}\. (.*?)</p>",
                          "<OL_STEP>", html, count=1, flags=re.S)
        html = re.sub(r"<OL_STEP>", f"<ol>\n{''.join(parts)}\n</ol>",
                      html, count=1)
    # 3. Ammonia-spike causes -> ordered list (matches "in order of frequency")
    items = []
    for starts in _WPC_CAUSES:
        m = re.search(rf"<p>{re.escape(starts)}.*?</p>", html, flags=re.S)
        if m:
            items.append(m.group(0))
    if len(items) == len(_WPC_CAUSES):
        html2 = html
        for starts in _WPC_CAUSES:
            html2 = re.sub(rf"<p>{re.escape(starts)}.*?</p>",
                           "<UL_CAUSE>", html2, count=1, flags=re.S)
        html2 = re.sub(r"<UL_CAUSE>",
                       f"<ol>\n{''.join(items)}\n</ol>", html2, count=1)
        html = html2
    # 4. Nitrogen-cycle crash causes -> ordered list
    crash_items = []
    for starts in _WPC_CRASHES:
        m = re.search(rf"<p>{re.escape(starts)}.*?</p>", html, flags=re.S)
        if m:
            crash_items.append(m.group(0))
    if len(crash_items) == len(_WPC_CRASHES):
        html2 = html
        for starts in _WPC_CRASHES:
            html2 = re.sub(rf"<p>{re.escape(starts)}.*?</p>",
                           "<UL_CRASH>", html2, count=1, flags=re.S)
        html2 = re.sub(r"<UL_CRASH>",
                       f"<ol>\n{''.join(crash_items)}\n</ol>", html2, count=1)
        html = html2
    # 5. Prevention foundations -> ordered list ("The four foundations…")
    prev_items = []
    for starts in _WPC_PREVENTION:
        m = re.search(rf"<p>{re.escape(starts)}.*?</p>", html, flags=re.S)
        if m:
            prev_items.append(m.group(0))
    if len(prev_items) == len(_WPC_PREVENTION):
        html2 = html
        for starts in _WPC_PREVENTION:
            html2 = re.sub(rf"<p>{re.escape(starts)}.*?</p>",
                           "<UL_PREV>", html2, count=1, flags=re.S)
        html2 = re.sub(r"<UL_PREV>",
                       f"<ol>\n{''.join(prev_items)}\n</ol>", html2, count=1)
        html = html2
    return html


def _to_label_list(html, labels, placeholder, ordered=False):
    """Convert N paragraphs that each begin with one of `labels` into a single
    <ul> (or <ol>). Each paragraph is a "Label: body" definition item."""
    items = []
    for lab in labels:
        m = re.search(rf"<p>{re.escape(lab)}:? (.*?)</p>", html, flags=re.S)
        if m:
            lab_clean = lab.rstrip(":")
            items.append(
                f"<li><strong>{lab_clean}:</strong> {m.group(1)}</li>")
    if len(items) != len(labels):
        return html
    html2 = html
    for lab in labels:
        html2 = re.sub(rf"<p>{re.escape(lab)}:? (.*?)</p>",
                       placeholder, html2, count=1, flags=re.S)
    tag = "ol" if ordered else "ul"
    return re.sub(placeholder,
                  f"<{tag}>\n{''.join(items)}\n</{tag}>", html2, count=1)


_TEMP_LOCATIONS = [
    "Basements and ground floors",
    "Upstairs rooms and attics",
    "Apartments",
    "Garages",
    "Coastal climates",
    "Desert and dry inland climates",
]

# Cooling-troubleshooting definitions + cooling-mistake warnings (tank-setup/
# temperature). Long parallel "Label: explanation" paragraphs read as lists.
_TEMP_COOL_PROBLEMS = [
    "Fan too small for the tank volume",
    "Humidity too high",
    "Glass lid blocking airflow",
    "Direct sunlight on the tank",
    "Submersible pump or internal filter adding heat",
    "Room too warm",
    "Thermometer positioned incorrectly",
    "Chiller undersized for tank volume or room heat load",
    "Peltier chiller being used on a tank over 10 gallons",
]

_TEMP_COOL_MISTAKES = [
    "Using ice cubes directly",
    "Cooling too quickly",
    "Ignoring evaporation loss",
    "Keeping a glass lid with a fan",
    "Thermometer placement errors",
]


def _temp_overrides(html):
    html = _to_label_list(
        html, _TEMP_LOCATIONS, "<UL_TCLOC>", ordered=False)
    html = _to_label_list(
        html, _TEMP_COOL_PROBLEMS, "<UL_TCPROB>", ordered=True)
    html = _to_label_list(
        html, _TEMP_COOL_MISTAKES, "<UL_TCMIST>", ordered=False)
    return html


_WC_HARM_MECHANISMS = [
    "Gill burns.",
    "Dermal absorption.",
    "Biofilter destruction.",
]

_WC_DOSING_SCENARIOS = [
    "Routine water change:",
    "Elevated ammonia or nitrite:",
]

_WC_TIMELINE = [
    "0–2 minutes:",
    "2–5 minutes:",
    "5–10 minutes:",
    "10–30 minutes:",
    "24 hours:",
    "48 hours:",
]


def _to_label_list2(html, labels, placeholder, ordered=False):
    """Same as _to_label_list but matches 'Label.' (period) style leads too."""
    items = []
    for lab in labels:
        m = re.search(rf"<p>{re.escape(lab)} (.*?)</p>", html, flags=re.S)
        if m:
            items.append(f"<li><strong>{lab}</strong> {m.group(1)}</li>")
    if len(items) != len(labels):
        return html
    html2 = html
    for lab in labels:
        html2 = re.sub(rf"<p>{re.escape(lab)} (.*?)</p>",
                       placeholder, html2, count=1, flags=re.S)
    tag = "ol" if ordered else "ul"
    return re.sub(placeholder,
                  f"<{tag}>\n{''.join(items)}\n</{tag}>", html2, count=1)


def _wc_overrides(html):
    html = _to_label_list2(
        html, _WC_HARM_MECHANISMS, "<UL_WCHARM>", ordered=False)
    html = _to_label_list(
        html, _WC_DOSING_SCENARIOS, "<UL_WCDOSE>", ordered=False)
    html = _to_label_list(
        html, _WC_TIMELINE, "<OL_WCTIME>", ordered=True)
    return html


_LVFF_SITUATIONS = [
    "Picky eater refusing earthworms.",
    "Recovering axolotl (post-illness or post-injury).",
    "Obese axolotl.",
    "Bloodworm-only diet (already established).",
    "Underweight axolotl.",
]


def _lvff_overrides(html):
    html = _to_label_list2(
        html, _LVFF_SITUATIONS, "<UL_LVFF>", ordered=False)
    return html


_SUB_SAFETY_CRITERIA = [
    "Grain size.",
    "Particle shape.",
    "Chemical inertness.",
    "Absence of toxic compounds.",
]

_SUB_WATER_PARAMS = [
    "pH.",
    "KH (Carbonate Hardness).",
    "GH (General Hardness).",
    "Ammonia and Nitrate.",
]


def _sub_overrides(html):
    html = _to_label_list2(
        html, _SUB_SAFETY_CRITERIA, "<UL_SUBCRIT>", ordered=False)
    html = _to_label_list2(
        html, _SUB_WATER_PARAMS, "<UL_SUBWPAR>", ordered=False)
    return html


# ---------------------------------------------------------------------------
# Editorial content normalization (Phase 4)
# ---------------------------------------------------------------------------

# Stale article URLs seen in the source docs -> current slug. The docx files
# were written against an older URL scheme; normalize them so in-body links
# resolve to the shipped site.
PATH_LINKS = {
    "/choosing-the-best-axolotl-substrate/": "tank-setup/substrate-and-impaction",
    "/how-to-cycle-an-axolotl-tank-fast/": "tank-setup/water-parameters-cycling",
    "/best-aquarium-chillers-for-axolotls/": "tank-setup/aquarium-chillers",
    "/axolotl-cycling-guide/": "tank-setup/water-parameters-cycling",
    "/axolotl-water-parameters-guide/": "tank-setup/water-parameters-cycling",
}

# [bracket text] markers -> real article slug. Unknown markers are stripped to
# plain text so they never render as literal brackets in the published page.
BRACKET_LINKS = {
    "aquarium chiller guide for axolotls": "tank-setup/aquarium-chillers",
    "axolotl emergency water problems guide": "tank-setup/water-parameters-cycling",
    "axolotl tank cycling guide": "tank-setup/water-parameters-cycling",
    "axolotl water parameters guide": "tank-setup/water-parameters-cycling",
    "checking water parameters": "tank-setup/water-parameters-cycling",
    "chiller guide": "tank-setup/aquarium-chillers",
    "guide to choosing the best axolotl substrate": "tank-setup/substrate-and-impaction",
    "guide to cycling an axolotl tank fast": "tank-setup/water-parameters-cycling",
    "guide to the best aquarium chillers for axolotls": "tank-setup/aquarium-chillers",
    "sponge filter guide for axolotls": "tank-setup/filtration-for-axolotls",
    "sourcing safe live foods": "diet/live-vs-frozen-food",
    "30-day quarantine": "health/quarantine-tub",
    "hospital tub setup guide": "health/quarantine-tub",
    "aquarium chiller setup guide": "tank-setup/aquarium-chillers",
    "water parameter testing guide": "tank-setup/water-parameters-cycling",
    "cycling guide": "tank-setup/water-parameters-cycling",
}


def linkify_brackets(html):
    """Convert markdown [text](url) and [text] link markers to real <a> tags."""
    # Protect [[EMBED_IMG:...]] markers first so their brackets are untouched.
    embeds = []

    def hold_embed(m):
        embeds.append(m.group(0))
        return "\x00%d\x00" % (len(embeds) - 1)

    html = re.sub(r"\[\[EMBED_IMG:[^\]]+\]\]", hold_embed, html)

    def md_link(m):
        label, url = m.group(1).strip(), m.group(2).strip()
        target = PATH_LINKS.get(url, url)
        is_file = target.endswith((".pdf", ".webp", ".png", ".jpg"))
        if is_file or target.startswith(("http://", "https://", "mailto:")):
            return f'<a href="{target}">{label}</a>'
        if target.startswith("/"):
            if target.endswith("/"):
                return f'<a href="{target}">{label}</a>'
            return f'<a href="/{target}/">{label}</a>'
        # bare slug from PATH_LINKS -> expand to a full article URL
        return f'<a href="/{target}/">{label}</a>'

    html = re.sub(r"\[([^\]\[]+)\]\(([^)]+)\)", md_link, html)

    def bracket(m):
        text = m.group(1).strip()
        slug = BRACKET_LINKS.get(text.lower())
        if slug:
            return f'<a href="/{slug}/">{text}</a>'
        return text

    html = re.sub(r"(?<!\[)\[([^\]\[]+)\](?!\])", bracket, html)
    for i, embed in enumerate(embeds):
        html = html.replace("\x00%d\x00" % i, embed)
    return html


def normalize_heading_levels(html):
    """Renumber body headings so the first is an h2, nothing deeper than an h3,
    and open/close tags always match. Removes the historical shift bug where
    only the opening tag was rewritten."""
    matches = list(re.finditer(r"<h([234])>(.*?)</h\1>", html, re.S))
    if not matches:
        return html
    out = []
    pos = 0
    prev_raw = prev_out = None
    for m in matches:
        raw = int(m.group(1))
        inner = m.group(2)
        if prev_raw is None:
            level = 2
        elif raw > prev_raw:
            level = min(prev_out + 1, 3)
        elif raw == prev_raw:
            level = prev_out
        else:
            level = max(prev_out - (prev_raw - raw), 2)
        out.append(html[pos:m.start()])
        out.append(f"<h{level}>{inner}</h{level}>")
        pos = m.end()
        prev_raw, prev_out = raw, level
    out.append(html[pos:])
    return "".join(out)


def split_long_paragraphs(html, max_words=100, target_words=72):
    """Split tag-free paragraphs longer than max_words at sentence boundaries
    into chunks of roughly target_words, keeping 2-4 sentences per chunk."""
    def split_one(inner):
        if "<" in inner:
            return None  # skip anything with inline markup
        sentences = re.split(r"(?<=[.!?])\s+(?=[A-Z0-9])", inner.strip())
        sentences = [s.strip() for s in sentences if s.strip()]
        if len(sentences) < 2:
            return None
        chunks, cur, cur_w = [], [], 0
        for s in sentences:
            w = len(s.split())
            if cur and (cur_w + w > target_words or (len(cur) >= 2 and cur_w + w > max_words)):
                chunks.append(" ".join(cur))
                cur, cur_w = [], 0
            cur.append(s)
            cur_w += w
        if cur:
            chunks.append(" ".join(cur))
        if len(chunks) < 2:
            return None
        return "</p><p>".join(chunks)

    def repl(m):
        chunked = split_one(m.group(1))
        return f"<p>{chunked}</p>" if chunked else m.group(0)

    return re.sub(r"<p>(.*?)</p>", repl, html, flags=re.S)


_BLOCK_RE = re.compile(
    r'<div class="table-wrap">.*?</div>'
    r"|<blockquote>.*?</blockquote>"
    r'|<div class="references-box">.*?</div>'
    r"|<(?:ul|ol)>\s*(?:<li>.*?</li>\s*)*</(?:ul|ol)>"
    r"|<h[234][^>]*>.*?</h[234]>"
    r"|<p>.*?</p>"
    r"|<hr>"
    r"|\[\[EMBED_IMG:[^\]]+\]\]",
    re.S,
)


def _faq_heading(text):
    return bool(re.search(
        r"(faq|frequently asked|common questions|advanced questions|"
        r"what questions|questions?\s*(to|you|do|about|for|when|why|how)|q\s*&\s*a)",
        text, re.I))


def _looks_like_question(text):
    t = text.strip()
    return len(t) <= 140 and t.endswith("?")


def normalize_faq(html):
    """Convert FAQ regions into the universal accordion component:

    <section class="faq"><h2>Frequently Asked Questions</h2>
      <details class="faq-item"><summary>Q</summary>
        <div class="faq-answer">A</div></details>...</section>

    Recognizes run-on 'Q? A...' paragraphs, bold-question + answer pairs, and
    question headings followed by answers. Never invents questions; sections
    with no real Q&A are left untouched.
    """
    blocks = []
    for m in _BLOCK_RE.finditer(html):
        blocks.append(m.group(0))
    if not blocks:
        return html

    # locate FAQ region starts (indices of FAQ-ish headings)
    heads = []
    for i, b in enumerate(blocks):
        m = re.match(r"<h([234])>(.*?)</h\1>", b, re.S)
        if m:
            txt = re.sub(r"<[^>]+>", "", m.group(2)).strip()
            if _faq_heading(txt):
                heads.append((i, int(m.group(1)), txt))
    if not heads:
        return html

    faq_items = []      # consolidated list of (q_text, answer_html)
    out = []
    section_open = False
    first_head = heads[0][0]

    def flush_item(q, a_html):
        a_html = a_html.strip()
        if q:
            faq_items.append((q, a_html))

    def render_faq_items():
        """Render accumulated items as <details> blocks, dropping questions
        with no answer, and reset the accumulator."""
        nonlocal faq_items
        parts = []
        for q, a in faq_items:
            if not a:
                continue
            qe = q.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
            parts.append(f'<details class="faq-item"><summary>{qe}</summary>'
                         f'<div class="faq-answer">{a}</div></details>')
        faq_items = []
        return "\n".join(parts)

    for i, b in enumerate(blocks):
        if i == first_head:
            out.append('<section class="faq">\n<h2>Frequently Asked Questions</h2>\n')
            section_open = True
            continue
        if section_open and i in [h[0] for h in heads]:
            continue  # later FAQ headings merge into the single section
        if not section_open or i < first_head:
            out.append(b)
            continue

        hm = re.match(r"<h([234])>(.*?)</h\1>", b, re.S)
        if hm:
            txt = re.sub(r"<[^>]+>", "", hm.group(2)).strip()
            if _looks_like_question(txt):
                flush_item(txt, "")
            else:
                # a new non-question heading closes the FAQ region
                out.append(render_faq_items())
                out.append("</section>\n")
                section_open = False
                out.append(b)
            continue

        pm = re.match(r"<p>(.*?)</p>", b, re.S)
        if pm:
            inner = pm.group(1)
            txt = re.sub(r"<[^>]+>", "", inner).strip()
            # bold-question paragraph?
            bq = re.match(r"<strong>([^<]+)</strong>\s*$", inner)
            if bq and _looks_like_question(bq.group(1)):
                flush_item(bq.group(1).strip(), "")
                continue
            # run-on "Q? A..." paragraph?
            m = re.search(r"\?\s", txt)
            if m and len(txt) > 40 and len(txt[:m.end()]) < 200 and len(txt[m.end():]) > 30:
                q = txt[:m.end()].strip()
                a = txt[m.end():].strip()
                flush_item(q, f"<p>{a}</p>")
                continue
            # plain paragraph -> extend the current item's answer
            if faq_items and not _looks_like_question(txt):
                last = faq_items[-1]
                faq_items[-1] = (last[0], (last[1] + "\n" + b).strip())
            else:
                out.append(b)
            continue

        # tables / lists / embeds inside the FAQ -> extend current answer
        if faq_items:
            last = faq_items[-1]
            faq_items[-1] = (last[0], (last[1] + "\n" + b).strip())
        else:
            out.append(b)

    if section_open:
        out.append(render_faq_items())
        out.append("</section>\n")

    result = "".join(out)
    if "<details class=\"faq-item\">" not in result:
        # No real Q&A found: leave a plain heading instead of an empty accordion
        # (e.g. sections made of all-bold statements with no questions).
        result = re.sub(
            r'<section class="faq">\n<h2>Frequently Asked Questions</h2>\n(.*?)</section>\n',
            r'<h2>Frequently Asked Questions</h2>\n\1',
            result, flags=re.S)
    return result


# ---------------------------------------------------------------------------
# main conversion
# ---------------------------------------------------------------------------

def convert_docx(path, slug=None):
    """Return dict: title, meta, body_html, headings, faq"""
    doc = Document(path)

    # 1. Iterate document body in order (paragraphs + tables interleaved)
    blocks = []  # ('p', text, para_obj) or ('tbl', table_obj) or ('img', rel_id)
    for child in doc.element.body.iterchildren():
        if child.tag == qn("w:p"):
            p = Paragraph(child, doc)
            t = clean_text(p.text)
            # detect inline images in this paragraph
            drawings = child.findall(".//" + qn("w:drawing"))
            blips = child.findall(".//" + qn("a:blip"))
            for b in blips:
                rid = b.get(qn("r:embed"))
                if rid:
                    blocks.append(("img", rid, p))
            if not drawings:
                blocks.append(("p", t, p))
        elif child.tag == qn("w:tbl"):
            blocks.append(("tbl", Table(child, doc), None))

    # 2. Parse meta block at top
    meta = {"title_tag": None, "meta_description": None, "h1": None}
    i = 0
    while i < len(blocks):
        kind, t, obj = blocks[i]
        if kind != "p" or not t.strip():
            i += 1
            continue
        t = t.strip()
        m = re.match(r"^(title tag)\s*:\s*(.+)$", t, re.I)
        if m:
            meta["title_tag"] = m.group(2).strip()
            i += 1
            continue
        m = re.match(r"^(meta description|meta description:)\s*:\s*(.+)$", t, re.I)
        if m:
            meta["meta_description"] = m.group(2).strip()
            i += 1
            continue
        m = re.match(r"^(h1)\s*:\s*(.+)$", t, re.I)
        if m:
            meta["h1"] = m.group(2).strip()
            i += 1
            continue
        m = re.match(r"^(macro context|central entity|focus keyword|primary entity|secondary entity|supporting entity|adjacent entity|search volume|buyer stage|url|slug|keyword|competition|search activities|representative query)\s*:\s*(.*)$", t, re.I)
        if m:
            i += 1
            continue
        # junk AI note at top
        if looks_like_junk(t):
            i += 1
            continue
        break

    # 3. Convert remaining blocks to HTML
    html_parts = []
    pending_pipe = []       # accumulate pipe-table lines

    def flush_pipe():
        nonlocal pending_pipe
        if pending_pipe:
            rows = parse_pipe_table(pending_pipe)
            if rows:
                html_parts.append(render_table(rows))
            else:
                for ln in pending_pipe:
                    html_parts.append(f"<p>{strip_markdown_inline(ln)}</p>")
            pending_pipe = []

    for idx in range(i, len(blocks)):
        kind, t, obj = blocks[idx]
        if kind == "img":
            flush_pipe()
            html_parts.append(f"[[EMBED_IMG:{t}]]")
            continue
        if kind == "tbl":
            flush_pipe()
            html_parts.append(render_docx_table(t))
            continue
        t = t.strip()
        if not t:
            flush_pipe()
            continue

        # pipe table line?
        if t.startswith("|"):
            pending_pipe.append(t)
            continue
        flush_pipe()

        # literal --- / *** separator rows -> <hr>
        if re.fullmatch(r"[\s\-–—*]{3,}", t):
            html_parts.append("<hr>")
            continue

        # markdown heading
        m = re.match(r"^(#{1,4})\s+(.*)$", t)
        if m:
            level = min(len(m.group(1)) + 1, 4)  # # -> h2 (article title is h1 elsewhere)
            html_parts.append(f"<h{level}>{strip_markdown_inline(m.group(2))}</h{level}>")
            continue

        # blockquote
        if t.startswith("> "):
            html_parts.append(f"<blockquote>{strip_markdown_inline(t[2:])}</blockquote>")
            continue

        # markdown list "- " or "1. "
        lm = re.match(r"^(-|•)\s+(.*)$", t)
        if lm:
            html_parts.append(f"<ul><li>{strip_markdown_inline(lm.group(2))}</li></ul>")
            continue
        om = re.match(r"^(\d+)[.)]\s+(.*)$", t)
        if om:
            html_parts.append(f"<ol><li>{strip_markdown_inline(om.group(2))}</li></ol>")
            continue

        # Word-style heading: all-bold, shortish, not a list item
        is_list = obj._p.pPr is not None and obj._p.pPr.numPr is not None
        runs = [r for r in obj.runs if r.text.strip()]
        all_bold = bool(runs) and all(r.bold for r in runs)
        if all_bold and not is_list and len(t) <= 90 and not is_meta_line(t):
            html_parts.append(f"<h2>{strip_markdown_inline(t)}</h2>")
            continue

        # Question-style heading (not bold): short question paragraph followed by
        # a substantial answer paragraph -> treat as h2
        if (not is_list and len(t) <= 90 and t.endswith("?")
                and not is_meta_line(t) and not t.startswith(("#", "|", ">", "-", "1.", "2."))):
            # look ahead for an answer paragraph of meaningful length
            nxt = blocks[idx + 1] if idx + 1 < len(blocks) else None
            if nxt and nxt[0] == "p" and len(nxt[1].strip()) > 100 and not nxt[1].strip().startswith("|"):
                html_parts.append(f"<h2>{strip_markdown_inline(t)}</h2>")
                continue

        # Word list item (numbered/bulleted via numPr)
        if is_list and len(t) <= 200:
            html_parts.append(f"<ul><li>{strip_markdown_inline(t)}</li></ul>")
            continue

        # FAQ line: "Q? A..." -> keep as paragraph (FAQ schema extracted separately)
        html_parts.append(f"<p>{strip_markdown_inline(t)}</p>")

    flush_pipe()

    body_html = "\n".join(html_parts)
    # Merge consecutive single-item <ul> blocks into one list
    body_html = re.sub(r"</ul>\s*\n\s*<ul>", "", body_html)

    # Reconstruct .references-box blocks that some source docs keep as raw HTML
    # text (LLM-drafted markdown) so they render as a box instead of literal
    # "<ul>/</div>" text.
    body_html = re.sub(
        r"<p>\s*(<div class=\"references-box\"\s+style=\"[^\"]*\">)",
        r"\1", body_html)
    body_html = re.sub(r"<p>(?=\s*<div class=\"references-box\">)", "", body_html)
    body_html = re.sub(r"<p><h[1-6][^>]*>(.*?)</h[1-6]></p>\s*",
                       r"<h3>\1</h3>", body_html)
    body_html = re.sub(r"<p><ul[^>]*></p>", "<ul>", body_html)
    body_html = re.sub(r"<p><li>(.*?)</li></p>", r"<li>\1</li>", body_html, flags=re.S)
    body_html = re.sub(r"<p></ul></p>", "</ul>", body_html)
    body_html = re.sub(r"<p></div></p>", "</div>", body_html)

    # 4. Extract title
    title = None
    if meta["h1"]:
        title = meta["h1"]
    else:
        for kind, t, obj in blocks:
            t = t.strip()
            if not t or looks_like_junk(t) or is_meta_line(t):
                continue
            if t.startswith("#"):
                title = re.sub(r"^#{1,4}\s*", "", t)
            elif t.startswith("|"):
                continue
            else:
                title = t
            break
    if title is None:
        title = "Axolotl Care Guide"
    title = re.sub(r"\s+", " ", title).strip()
    # Drop the title heading if it duplicated as the first body heading
    title_esc = re.escape(title)
    body_html = re.sub(rf"<h2>{title_esc}</h2>\s*", "", body_html, count=1)

    # 4b. Editorial normalization (Phase 4): working in-body links, strict
    # heading levels with matching open/close tags, one FAQ accordion, and
    # paragraph length limits.
    body_html = linkify_brackets(body_html)
    body_html = normalize_heading_levels(body_html)
    body_html = normalize_faq(body_html)
    # Flattened grid recovery (reading-density): pipe tables stored as a run
    # of tiny paragraphs belong in real tables (their <hr> column separators
    # make the shape unambiguous). Runs after FAQ so Q&A cells are not rebuilt.
    body_html = recover_grid_tables(body_html)
    body_html = recover_glued_param_table(body_html)
    body_html = recover_glued_food_table(body_html)
    # Reading-density: promote standalone prose sub-headings (food names,
    # life-stage labels) from blank short paragraphs to real <h3> so a long
    # flat run of paragraphs splits into scannable sections.
    body_html = recover_prose_headings(body_html)
    # Bold-only paragraphs ("<p><strong>X</strong></p>") read as headings; the
    # detail lives in the heading, so drop the strong styling to plain text.
    body_html = re.sub(r"<p>\s*<strong>((?:(?!</strong>).)*)</strong>\s*</p>",
                       r"<p>\1</p>", body_html, flags=re.S)
    body_html = split_long_paragraphs(body_html)
    # Reading-density: per-article structure overrides (prose lead-ins ->
    # headings / ordered lists) for cases too surgical for generic rules.
    if slug:
        body_html = article_body_overrides(slug, body_html)

    # 5. Extract meta description
    meta_desc = meta["meta_description"]
    if not meta_desc:
        for kind, t, obj in blocks:
            t = t.strip()
            if not t or t.startswith("#") or t.startswith("|") or is_meta_line(t) or looks_like_junk(t):
                continue
            if len(t) > 40:
                meta_desc = t
                break
    if meta_desc and len(meta_desc) > 165:
        meta_desc = meta_desc[:162].rstrip() + "..."

    # 6. Extract headings for TOC + FAQ items from the normalized accordion
    headings = re.findall(r"<h([234])>(.*?)</h\1>", body_html)
    headings = [(int(l), re.sub(r"<[^>]+>", "", h).strip()) for l, h in headings]
    faq = []
    for m in re.finditer(r'<details class="faq-item"><summary>(.*?)</summary>'
                         r'<div class="faq-answer">(.*?)</div></details>',
                         body_html, re.S):
        q = m.group(1)
        a = re.sub(r"<[^>]+>", " ", m.group(2))
        a = re.sub(r"\s+", " ", a).strip()
        faq.append((_html.unescape(q), a))

    # 7. Collect embedded images (rel_id -> bytes) for later extraction
    embedded = {}
    for rid in re.findall(r"\[\[EMBED_IMG:([^\]]+)\]\]", body_html):
        try:
            part = doc.part.related_parts[rid]
            blob = part.blob
            embedded[rid] = blob
        except Exception:
            pass

    return {
        "title": title,
        "meta_description": meta_desc,
        "body_html": body_html,
        "headings": headings,
        "faq": faq,
        "embedded": embedded,
    }


def slugify(text):
    text = re.sub(r"&", " and ", text)
    text = re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")
    text = re.sub(r"-{2,}", "-", text)
    return text or "axolotl-guide"


def words_from(text):
    return len(re.findall(r"\S+", re.sub(r"<[^>]+>", " ", text)))
