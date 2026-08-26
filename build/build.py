# -*- coding: utf-8 -*-
"""
Static site generator for the axolotl care website.

Pipeline:
  1. Convert every .docx article to HTML (docx2html)
  2. Optimize images (PNG -> WebP), extract embedded docx images
  3. Render pages: home, hubs, articles, tools, simple pages, 404
  4. Copy standalone tool HTML pages into /tools/
  5. Emit sitemap.xml, robots.txt, ads.txt, security.txt, build-report.json

The templates below use plain, class-based markup and NO inline styles;
all presentation lives in /css/style.css.
"""
import os
import re
import io
import json
import html
from datetime import date
from urllib.parse import quote
from pathlib import Path

from PIL import Image

import config
from docx2html import convert_docx, words_from

# ---------------------------------------------------------------------------
# Paths / constants
# ---------------------------------------------------------------------------
ROOT = Path(__file__).resolve().parent.parent
BUILD_DIR = ROOT / "build"
SRC = config.SOURCE_DIR
PUBLIC = ROOT / "public"
IMG_DIR = PUBLIC / "images"
TOOLS_DIR = PUBLIC / "tools"
TODAY = date.today().isoformat()
YEAR = date.today().year

NAV_PRIMARY = [
    ("/axolotls/", "Care"),
    ("/tank-setup/", "Tank Setup"),
    ("/diet/", "Diet"),
    ("/health/", "Health"),
]

NAV_MORE = [
    ("/care-basics/", "Care Basics"),
    ("/morphs/", "Morphs"),
    ("/breeding/", "Breeding"),
    ("/legal/", "Legal"),
    ("/cost-and-buying/", "Cost & Buying"),
    ("/biology-and-science/", "Biology"),
    ("/gifts-and-merch/", "Gifts & Merch"),
    ("/axolotl-in-culture/", "Culture"),
]

# Verified facts shown in the homepage quick-info bar.
QUICK_FACTS = [
    ("Scientific name", "Ambystoma mexicanum"),
    ("Adult size", "9&ndash;12 in (23&ndash;30 cm)"),
    ("Lifespan", "10&ndash;15 yrs, up to 20+"),
    ("Water temp", "60&ndash;68&deg;F (16&ndash;20&deg;C)"),
    ("Diet", "Obligate carnivore"),
]

HOME = {
    "title_tag": "MyAxolotl - Everything You Need to Know About Axolotls",
    "meta": "Everything about axolotls: care, feeding, habitat, genetics, morphs, breeding, and their history in Mexico. Your trusted axolotl guide.",
    "h1": "Axolotls Are Unusual. Their Care Shouldn't Be Confusing.",
    "hero_img": "/images/axolotl-home.webp",
    "hero_alt": "Axolotl in a planted aquarium tank",
    "hero_text": "Research-led guidance on axolotl tank setup, water quality, feeding, health, behavior, morphs, breeding, and more.",
    "hero_tagline": "Care with confidence.",
    "featured": ["axolotls/care-guide", "tank-setup/setup-guide", "diet/best-foods-list", "health/refusing-to-eat"],
    "picks": ["health/refusing-to-eat", "tank-setup/water-parameters-cycling",
              "biology-and-science/regeneration-and-limb-regrowth", "diet/feeding-schedule-by-age"],
    "cta_title": "Ready to give your axolotl the best life?",
    "cta_text": "Start with the complete care guide, then set up the right tank, feed a healthy diet, and spot problems before they become serious.",
    "cta_link": "/tank-setup/setup-guide/",
    "cta_label": "Start the setup guide",
}

SIMPLE = {
    "about": {
        "title": "About",
        "meta": "About MyAxolotl and the people behind it.",
        "schema": "AboutPage",
        "body": """
<p>MyAxolotl publishes practical axolotl care guides, tools, and reference pages. The site is designed to answer the questions keepers actually ask: how to set up a safe tank, what to feed, how to spot illness, and when to seek an exotic vet.</p>
<p>Research and writing are handled by <a href="/authors/farrukh-abdullah/">Farrukh Abdullah</a>. Editorial review is handled by <a href="/editors/ananda-abidin/">Ananda Abidin</a>.</p>
<p>Start with the <a href="/axolotls/care-guide/">care guide</a>, then use the <a href="/editorial-policy/">editorial policy</a> to understand how the site is maintained.</p>
""",
    },
    "privacy": {
        "title": "Privacy Policy",
        "meta": "Privacy policy for MyAxolotl.",
        "schema": "WebPage",
        "body": """
<p>MyAxolotl does not require accounts or user profiles to read the guides.</p>
<p>The site may use standard analytics and advertising cookies to understand traffic and support the work. If you have a privacy question, contact <a href="mailto:f.abdullah79@gmail.com">Farrukh Abdullah</a>.</p>
""",
    },
    "contact": {
        "title": "Contact",
        "meta": "Contact MyAxolotl for corrections or questions.",
        "schema": "ContactPage",
        "body": """
<p>Questions, corrections, or sourcing notes should go to <a href="mailto:f.abdullah79@gmail.com">f.abdullah79@gmail.com</a>.</p>
<p>You can also reach <a href="https://www.linkedin.com/in/farrukh-abdullah-5a218424/">Farrukh Abdullah on LinkedIn</a> or review editorial workflow on the <a href="/editorial-policy/">editorial policy</a> page.</p>
""",
    },
    "editorial-policy": {
        "title": "Editorial Policy",
        "meta": "How MyAxolotl researches, reviews, and updates care guidance.",
        "schema": "WebPage",
        "body": """
<p>MyAxolotl separates research from editing so the care advice stays clear and accountable.</p>
<ol>
<li><strong>Research and drafting:</strong> Farrukh Abdullah writes the guides and keeps claims grounded in husbandry evidence.</li>
<li><strong>Editorial review:</strong> Ananda Abidin checks structure, clarity, and consistency.</li>
<li><strong>Transparency:</strong> The site does not invent credentials, awards, publications, or photos.</li>
<li><strong>Corrections:</strong> Confirmed errors are corrected and pages are updated when better husbandry guidance becomes available.</li>
</ol>
<p>If you spot an issue, use the <a href="/contact/">contact page</a> or email <a href="mailto:f.abdullah79@gmail.com">Farrukh Abdullah</a>.</p>
""",
    },
}

PROFILE_PAGES = config.PEOPLE

# One-line descriptions used for tool cards and the search index.
TOOL_DESCS = {
    "water-conditioner-dosage-calculator": "Work out exactly how many drops or ml of water conditioner you need for your tank volume.",
    "feeding-schedule-generator": "Generate a daily feeding schedule tailored to your axolotl's age and size.",
    "nitrogen-cycle-tracker": "Track ammonia, nitrite, and nitrate as your new tank cycles before adding your axolotl.",
    "symptom-checker": "Match your axolotl's symptoms to likely causes and the right first step to take.",
    "tank-size-calculator": "Find the minimum tank size for your axolotl based on its length and number of axolotls.",
}

# Popular searches shown on the empty search page (label -> query).
POPULAR_SEARCHES = [
    ("water temperature", "water temperature"),
    ("tank setup", "tank setup"),
    ("feeding", "feeding"),
    ("cycling", "cycling"),
    ("gills", "gills"),
    ("breeding", "breeding"),
    ("morphs", "morphs"),
    ("health", "health"),
]


def esc(text):
    return html.escape(str(text), quote=True)


SOCIAL_ICON_SVGS = {
    "Facebook": (
        '<svg class="footer-social-icon" aria-hidden="true" focusable="false" '
        'viewBox="0 0 24 24" width="21" height="21" fill="currentColor">'
        '<path d="M14.5 8H16V5.5h-1.8C11.8 5.5 10 7.3 10 9.7V11H8v3h2v7h3v-7h2.4l.6-3H13v-1.2c0-.9.6-1.8 1.5-1.8z"/>'
        '</svg>'
    ),
    "Instagram": (
        '<svg class="footer-social-icon" aria-hidden="true" focusable="false" '
        'viewBox="0 0 24 24" width="21" height="21" fill="none" '
        'stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">'
        '<rect x="4.5" y="4.5" width="15" height="15" rx="4"/>'
        '<circle cx="12" cy="12" r="3.5"/>'
        '<circle cx="16.7" cy="7.3" r="1" fill="currentColor" stroke="none"/>'
        '</svg>'
    ),
    "Pinterest": (
        '<svg class="footer-social-icon" aria-hidden="true" focusable="false" '
        'viewBox="0 0 24 24" width="21" height="21" fill="none" '
        'stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">'
        '<circle cx="12" cy="12" r="8.5"/>'
        '<path d="M11 17.5 12.2 13c-1.3-.1-2.4-.7-2.4-2.5 0-2 1.6-3.4 3.8-3.4 2.4 0 3.8 1.4 3.8 3.4 0 2.2-1.5 4.1-3.8 4.1-.5 0-.9-.1-1.3-.3l-.7 2.5H11z" fill="currentColor" stroke="none"/>'
        '</svg>'
    ),
    "X": (
        '<svg class="footer-social-icon" aria-hidden="true" focusable="false" '
        'viewBox="0 0 24 24" width="21" height="21" fill="none" '
        'stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">'
        '<path d="M6 5l12 14M18 5L6 19"/>'
        '</svg>'
    ),
    "Discord": (
        '<svg class="footer-social-icon" aria-hidden="true" focusable="false" '
        'viewBox="0 0 24 24" width="21" height="21" fill="none" '
        'stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">'
        '<path d="M7.4 8.3h9.2c2.4 0 4.4 2 4.4 4.4v1.1c0 2.4-2 4.4-4.4 4.4H7.4C5 18.2 3 16.2 3 13.8v-1.1c0-2.4 2-4.4 4.4-4.4z"/>'
        '<path d="M9 12.5h.01M15 12.5h.01" stroke-width="2.6"/>'
        '<path d="M8.8 10.9c.8-.4 1.7-.6 3.2-.6s2.4.2 3.2.6"/>'
        '</svg>'
    ),
}


def social_link(label, url):
    icon = SOCIAL_ICON_SVGS[label]
    return (
        f'<li><a class="footer-social-link" href="{esc(url)}" aria-label="{esc(label)}" '
        f'title="{esc(label)}">{icon}<span class="sr-only">{esc(label)}</span></a></li>'
    )


def ensure_dir(path):
    Path(path).mkdir(parents=True, exist_ok=True)


def write_page(rel_dir, filename, text):
    d = os.path.join(PUBLIC, rel_dir)
    ensure_dir(d)
    with open(os.path.join(d, filename), "w", encoding="utf-8") as fh:
        fh.write(text)


# ---------------------------------------------------------------------------
# Image helpers
# ---------------------------------------------------------------------------
def optimize_image(src_bytes, dst_path, fmt="WEBP", quality=82, max_side=1400):
    im = Image.open(io.BytesIO(src_bytes))
    if im.mode in ("RGBA", "P", "LA"):
        im = im.convert("RGBA")
    else:
        im = im.convert("RGB")
    if max(im.size) > max_side:
        ratio = max_side / float(max(im.size))
        im = im.resize((int(im.size[0] * ratio), int(im.size[1] * ratio)), Image.LANCZOS)
    dst = dst_path if dst_path.lower().endswith(".webp") else os.path.splitext(dst_path)[0] + ".webp"
    im.save(dst, "WEBP", quality=quality, method=6)
    return dst


def filename_alt(name):
    base = re.sub(r"\s*[-–—]\s*\d+\s*\.webp$", "", name)
    base = re.sub(r"\.(webp|png|jpe?g|svg)$", "", base, flags=re.I)
    base = re.sub(r"[-_]+", " ", base)
    base = re.sub(r"\s+", " ", base).strip()
    return base or "axolotl"


def clean_image_name(name):
    base = os.path.splitext(name)[0]
    base = re.sub(r"^\d+\s*[-–—]\s*", "", base)
    base = re.sub(r"\(.*?\)", "", base)
    base = re.sub(r"[-_\s]+", "-", base).strip("-").lower()
    base = re.sub(r"-{2,}", "-", base)
    return base or "axolotl"


# Deterministic order for candidate images: descriptive files first, bare
# numbers last; within a tier, alphabetically.
_IMG_PREFER = re.compile(r"(comparison|decision|tree|diagram|chart|table|best|hero)", re.I)


def _image_sort_key(name):
    base = os.path.splitext(os.path.basename(name))[0]
    rem = re.sub(r"^\s*\d+\s*[-–—]?\s*", "", base).strip()
    if not rem or re.match(r"^\d+$", rem):
        return (3, base.lower())
    if _IMG_PREFER.search(rem):
        return (0, rem.lower())
    return (1, rem.lower())


def _pick_featured_image(cands):
    if not cands:
        return None
    if len(cands) == 1:
        return cands[0]
    hero = [c for c in cands if re.search(r"\bhero\b", c.get("alt", ""), re.I)]
    if hero:
        return hero[0]
    return cands[0]


def _seo_alt_from_title(title):
    alt = title.split("|")[0].strip()
    alt = re.sub(r"\s+", " ", alt).strip()
    return alt or "Axolotl care guide"


def _generate_placeholder(title, slug):
    """Branded WebP placeholder hero for articles without a photo."""
    from PIL import ImageDraw, ImageFont
    w, h = 1200, 800
    im = Image.new("RGB", (w, h))
    px = im.load()
    c1 = (15, 57, 70)
    c2 = (135, 206, 235)
    for y in range(h):
        t = y / float(h)
        r = int(c1[0] + (c2[0] - c1[0]) * t)
        g = int(c1[1] + (c2[1] - c1[1]) * t)
        b = int(c1[2] + (c2[2] - c1[2]) * t)
        for x in range(w):
            px[x, y] = (r, g, b)
    draw = ImageDraw.Draw(im)
    cx, cy = w // 2, int(h * 0.34)
    draw.ellipse((cx - 90, cy - 70, cx + 90, cy + 90), outline=(255, 255, 255, 180), width=6)
    for gx in (-150, -110, 110, 150):
        draw.line((gx, cy - 30, gx - 40, cy - 110), fill=(255, 255, 255, 170), width=6)
        draw.line((gx, cy, gx - 55, cy + 10), fill=(255, 255, 255, 170), width=6)
    try:
        font = ImageFont.truetype("C:/Windows/Fonts/segoeuib.ttf", 44)
        font_sm = ImageFont.truetype("C:/Windows/Fonts/segoeui.ttf", 26)
    except Exception:
        font = ImageFont.load_default()
        font_sm = ImageFont.load_default()
    words = title.split()
    lines = []
    cur = ""
    for word in words:
        trial = (cur + " " + word).strip()
        if draw.textlength(trial, font=font) > w - 160 or len(lines) >= 3:
            if cur:
                lines.append(cur)
                cur = word
            else:
                lines.append(word)
        else:
            cur = trial
        if len(lines) >= 3:
            break
    if cur:
        lines.append(cur)
    lines = lines[:3]
    y = int(h * 0.58)
    for ln in lines:
        lw = draw.textlength(ln, font=font)
        draw.text(((w - lw) / 2, y), ln, fill=(255, 255, 255), font=font)
        y += 56
    brand = config.SITE_NAME
    lw = draw.textlength(brand, font=font_sm)
    draw.text(((w - lw) / 2, int(h * 0.86)), brand, fill=(220, 245, 247), font=font_sm)
    ensure_dir(IMG_DIR)
    dst = os.path.join(IMG_DIR, f"{slug.replace('/', '-')}-placeholder.webp")
    im.save(dst, "WEBP", quality=82, method=6)
    return "/images/" + os.path.basename(dst)


# ---------------------------------------------------------------------------
# Article conversion & mapping
# ---------------------------------------------------------------------------
def title_tag_for(title, cfg):
    tag = cfg.get("title_tag")
    if tag:
        return tag
    brand = " | " + config.SITE_NAME
    if len(title) + len(brand) <= 63:
        return title + brand
    return trim_title(title, 63 - len(brand)) + brand


def trim_title(title, maxlen=60):
    if len(title) <= maxlen:
        return title
    cut = title[: maxlen - 1]
    last_space = cut.rfind(" ")
    if last_space > maxlen * 0.6:
        cut = cut[:last_space]
    return cut.rstrip(" ,;:") + "…"


def first_paragraph_text(body_html, title):
    """Plain-text excerpt: first <p> that isn't empty or a duplicate of title."""
    for m in re.finditer(r"<p>(.*?)</p>", body_html, re.S):
        txt = re.sub(r"<[^>]+>", "", m.group(1))
        txt = html.unescape(txt).strip()
        if not txt:
            continue
        if title and txt.lower() == title.lower():
            continue
        if len(txt) > 180:
            txt = txt[:177].rstrip() + "..."
        return txt
    return ""


def build_articles():
    """Return {slug: article_data}."""
    articles = {}
    for fname, cfg in config.ARTICLES.items():
        path = os.path.join(config.SOURCE_DIR, fname)
        if not os.path.exists(path):
            print("  !! missing:", fname)
            continue
        r = convert_docx(path, slug=cfg["slug"])
        slug = cfg["slug"]
        hub = cfg.get("hub", "axolotls")
        title = cfg.get("title_override") or r["title"]
        meta = cfg.get("meta_override") or r["meta_description"]
        articles[slug] = {
            "slug": slug,
            "file": fname,
            "num": int(re.match(r"^\s*(\d+)", fname).group(1)),
            "hub": hub,
            "title": title,
            "title_tag": title_tag_for(title, cfg),
            "meta": meta,
            "intro": first_paragraph_text(r["body_html"], title),
            "body_html": r["body_html"],
            "headings": r["headings"],
            "faq": r["faq"],
            "embedded": r["embedded"],
            "words": words_from(r["body_html"]),
            "featured": cfg.get("featured", False),
            "date_published": cfg.get("date_published", TODAY),
            "date_modified": cfg.get("date_modified", cfg.get("date_published", TODAY)),
        }
        articles[slug]["lastmod"] = articles[slug]["date_modified"]

    # Build-level (HTML-authored) articles from config.
    for slug, cfg in config.CONFIG_ARTICLES.items():
        articles[slug] = {
            "slug": cfg["slug"],
            "file": "",
            "num": int(cfg.get("num", 900)),
            "hub": cfg.get("hub", "axolotls"),
            "title": cfg["title"],
            "title_tag": title_tag_for(cfg["title"], cfg),
            "meta": cfg.get("meta", ""),
            "intro": cfg.get("intro", ""),
            "body_html": cfg["body"],
            "headings": [(2, h) for h in cfg.get("headings", [])],
            "faq": cfg.get("faq", []),
            "embedded": {},
            "words": words_from(cfg["body"]),
            "featured": cfg.get("featured", False),
            "date_published": cfg.get("date_published", TODAY),
            "date_modified": cfg.get("date_modified", cfg.get("date_published", TODAY)),
        }
        articles[slug]["lastmod"] = articles[slug]["date_modified"]

    # Phase 10 semantic layer: standfirst overrides, role callouts, section
    # expansions (applied to all articles, docx- or config-sourced alike).
    for slug, a in articles.items():
        intro_ovr = config.INTRO_OVERRIDES.get(slug)
        if intro_ovr:
            a["intro"] = intro_ovr
        callout = config.ROLE_CALLOUTS.get(slug)
        if callout:
            fm = re.search(r"</p>", a["body_html"])
            if fm:
                pos = fm.end()
                a["body_html"] = (a["body_html"][:pos] + callout
                                  + a["body_html"][pos:])
        for heading, html in config.EXTRA_SECTIONS.get(slug, []):
            a["body_html"] += f"<h2>{heading}</h2>{html}"
            a["headings"].append((2, heading))
        a["words"] = words_from(a["body_html"])
    return articles


def build_image_map(articles):
    """Map every article -> one featured image, and save ALL embedded images."""
    ensure_dir(IMG_DIR)
    img_map = {}

    all_images = [f for f in os.listdir(SRC)
                  if f.lower().endswith((".png", ".jpg", ".jpeg"))]
    by_num = {}
    for f in all_images:
        m = re.match(r"^\s*(\d+)\s*[-–—]?\s*", f)
        if m and not re.search(r"logo|fevicon|favicon|homepage", f, re.I):
            by_num.setdefault(int(m.group(1)), []).append(f)

    special = {
        2: ["axolotl tank setup.png", "axolotl tank setup diagram.jpg"],
        7: ["Best axolotl filters.png"],
    }

    for slug, a in articles.items():
        n = a["num"]
        cands = []
        for f in sorted(by_num.get(n, []), key=_image_sort_key):
            safe = clean_image_name(f)
            cands.append({"src": os.path.join(SRC, f),
                          "url": f"/images/{n}-{safe}.webp",
                          "alt": filename_alt(f"{n}-{safe}.webp")})
        for f in special.get(n, []):
            p = os.path.join(SRC, f)
            if not os.path.exists(p):
                continue
            safe = clean_image_name(f)
            cands.append({"src": p,
                          "url": f"/images/{n}-{safe}.webp",
                          "alt": filename_alt(f"{n}-{safe}.webp")})
        for rid, blob in a["embedded"].items():
            cands.append({"src_bytes": blob,
                          "url": f"/images/{n}-embedded-{rid}.webp",
                          "alt": f"Embedded illustration {rid}"})

        featured = _pick_featured_image(cands)
        if featured:
            dst = os.path.join(IMG_DIR, os.path.basename(featured["url"]))
            try:
                if "src_bytes" in featured:
                    optimize_image(featured["src_bytes"], dst)
                else:
                    with open(featured["src"], "rb") as fh:
                        optimize_image(fh.read(), dst)
                featured["alt"] = _seo_alt_from_title(a["title"])
                if slug == "axolotls/care-guide":
                    featured["alt"] = "Dark axolotl in a properly set up aquarium with cool water, fine sand, plants and a hide"
                img_map[slug] = featured
            except Exception as e:
                print("  !! img fail", slug, e)
                img_map[slug] = {"url": _generate_placeholder(a["title"], slug),
                                 "alt": _seo_alt_from_title(a["title"]),
                                 "placeholder": True}
        else:
            img_map[slug] = {"url": _generate_placeholder(a["title"], slug),
                             "alt": _seo_alt_from_title(a["title"]),
                             "placeholder": True}
            print(f"  !! placeholder generated for: {slug}")

    # Save every remaining embedded image so inline [[EMBED_IMG:...]] markers resolve.
    for slug, a in articles.items():
        n = a["num"]
        for rid, blob in a["embedded"].items():
            url = f"/images/{n}-embedded-{rid}.webp"
            if url in (img_map.get(slug) or {}).get("url", ""):
                continue
            dst = os.path.join(IMG_DIR, os.path.basename(url))
            if not os.path.exists(dst):
                try:
                    optimize_image(blob, dst)
                except Exception as e:
                    print("  !! embedded img fail", slug, rid, e)

    return img_map


def build_site_assets():
    """Create homepage hero + logo + favicon from the provided brand files."""
    ensure_dir(IMG_DIR)

    home = os.path.join(SRC, "hero.png")
    if os.path.exists(home):
        with open(home, "rb") as fh:
            optimize_image(fh.read(), os.path.join(IMG_DIR, "axolotl-home.webp"),
                           quality=80, max_side=1600)
        print("  !! homepage hero set from 'hero.png'")

    logo = None
    for cand in ("axolotl.us -  site logo.png", "site-logo.png", "axolotl logo.jpg"):
        p = os.path.join(SRC, cand)
        if os.path.exists(p):
            logo = p
            break
    if logo:
        logo_out = os.path.join(IMG_DIR, os.path.basename(config.SITE_LOGO))
        with open(logo, "rb") as fh:
            optimize_image(fh.read(), logo_out, quality=88, max_side=400)
        print(f"  !! logo set from '{os.path.basename(logo)}'")

    fav = None
    for cand in ("axolotl.us - site fevicon.png", "site-logo.png", "axolotl fevicon.jpg", "axolotl logo.jpg"):
        p = os.path.join(SRC, cand)
        if os.path.exists(p):
            fav = p
            break
    if fav:
        with open(fav, "rb") as fh:
            data = fh.read()
        im = Image.open(io.BytesIO(data))
        if im.mode != "RGBA":
            im = im.convert("RGBA")
        side = min(im.size)
        im = im.crop(((im.width - side) // 2, (im.height - side) // 2,
                      (im.width + side) // 2, (im.height + side) // 2))
        im = im.resize((64, 64), Image.LANCZOS)
        im.save(os.path.join(IMG_DIR, "axolotl-favicon.webp"), "WEBP", quality=90)


# ---------------------------------------------------------------------------
# Shared page chrome
# ---------------------------------------------------------------------------
def nav_item(href, label, active_href):
    cls = ' class="is-active"' if href == active_href else ""
    return f'<li><a href="{href}"{cls}>{esc(label)}</a></li>'


def header(active_href=""):
    primary = "".join(nav_item(href, label, active_href) for href, label in NAV_PRIMARY)

    more_open = active_href in [h for h, _ in NAV_MORE] or active_href == "/tools/"
    more_items = "".join(nav_item(href, label, active_href) for href, label in NAV_MORE)
    more_btn = (
        '<button type="button" class="more-toggle" aria-haspopup="true" aria-expanded="false" '
        'data-more-toggle>More <svg class="chev" aria-hidden="true" viewBox="0 0 12 8" '
        'width="10" height="7"><path d="M1 1l5 5 5-5" fill="none" stroke="currentColor" '
        'stroke-width="2"/></svg></button>'
    )
    if more_open:
        more_btn = more_btn.replace('aria-expanded="false"', 'aria-expanded="true"')

    # Mobile panel: all primary + all more, grouped.
    mobile_all = "".join(nav_item(href, label, active_href) for href, label in NAV_PRIMARY + NAV_MORE)
    tools_btn = (
        f'<a class="tools-link{" is-active" if active_href == "/tools/" else ""}" href="/tools/">'
        "Tools</a>"
    )

    search_link = (
        '<a class="nav-search" href="/search/" aria-label="Search axolotl guides">'
        '<svg class="search-icon" aria-hidden="true" viewBox="0 0 24 24" width="18" height="18" '
        'fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round">'
        '<circle cx="11" cy="11" r="7"/><path d="M21 21l-4.3-4.3"/></svg>'
        '<span class="sr-only">Search</span></a>'
    )

    return (
        '<header class="site-header"><div class="header-inner">'
        f'<a class="brand" href="/"><img class="logo-img" src="{esc(config.SITE_LOGO)}" '
        f'alt="{esc(config.SITE_NAME)} logo" width="60" height="40">'
        f'<span class="brand-name">{esc(config.SITE_NAME)}</span></a>'
        '<nav class="main-nav" aria-label="Main">'
        f'<ul class="nav-primary">{primary}'
        f'<li class="has-more"><div class="more-wrap">{more_btn}<ul class="more-menu">{more_items}</ul></div></li>'
        "</ul>"
        '<ul class="nav-tools">'
        f"<li>{tools_btn}</li>"
        "</ul>"
        "</nav>"
        f'{search_link}'
        '<button type="button" class="nav-burger" aria-label="Open menu" aria-expanded="false" '
        'data-nav-burger aria-controls="mobile-nav"><span></span><span></span><span></span></button>'
        '<nav class="mobile-nav" id="mobile-nav" aria-label="Mobile">'
        f'<ul>{mobile_all}<li>{tools_btn}</li></ul>'
        "</nav>"
        "</div></header>"
    )


def footer():
    def group(label, keys):
        items = "".join(
            f'<li><a href="/{k}/">{esc(config.HUBS[k]["cat"])}</a></li>'
            for k in keys
        )
        return f'<div class="footer-col"><h2 class="footer-col-title">{label}</h2><ul>{items}</ul></div>'

    care = group("Care", ["axolotls", "care-basics", "tank-setup", "diet", "health"])
    explore = group("Explore", ["morphs", "breeding", "legal", "cost-and-buying",
                                "biology-and-science", "gifts-and-merch", "axolotl-in-culture"])
    tools = "".join(
        f'<li><a href="/{t["slug"]}/">{esc(t["title"])}</a></li>'
        for t in config.TOOLS.values()
    )
    return (
        f'<footer class="site-footer"><div class="container">'
        '<div class="footer-grid">'
        '<div class="footer-col footer-brand">'
        f'<a class="footer-logo" href="/"><img class="logo-img" src="{esc(config.SITE_LOGO)}" '
        f'alt="{esc(config.SITE_NAME)} logo" width="48" height="32">'
        f'<span>{esc(config.SITE_NAME)}</span></a>'
        f'<p class="footer-tagline">{esc(config.SITE_TAGLINE)}</p>'
        '<ul class="footer-mini">'
        '<li><a href="/about/">About</a></li>'
        '<li><a href="/editorial-policy/">Editorial policy</a></li>'
        '<li><a href="/privacy/">Privacy</a></li>'
        '<li><a href="/contact/">Contact</a></li>'
        "</ul></div>"
        f"{care}{explore}"
        f'<div class="footer-col"><h2 class="footer-col-title">Tools</h2><ul>{tools}</ul></div>'
        "</div>"
        '<ul class="footer-mini footer-social">'
        + ''.join(social_link(label, url) for label, url in (*config.SOCIAL_LINKS, ("X", config.X_PROFILE_URL)))
        + '</ul>'
        '<div class="footer-bottom">'
        f'<span>&copy; {YEAR} {esc(config.SITE_NAME)}. All rights reserved.</span>'
        '<span>Made for axolotl keepers everywhere.</span>'
        "</div>"
        "</div></footer>"
    )


def page_html(title, meta, canonical, content, active_href="",
              og_type="website", og_image=None, json_ld=""):
    og_url = canonical
    og_image = og_image or "/images/axolotl-home.webp"
    if not og_image.startswith("http"):
        og_image = config.SITE_URL + og_image
    schema = ""
    if json_ld:
        schema = f"<script type=\"application/ld+json\">{json_ld}</script>"
    return (
        "<!DOCTYPE html>\n<html lang=\"en\">\n<head>\n"
        '<meta charset="utf-8">\n'
        '<meta name="viewport" content="width=device-width, initial-scale=1">\n'
        f"<title>{esc(title)}</title>\n"
        f'<meta name="description" content="{esc(meta)}">\n'
        f'<link rel="canonical" href="{esc(og_url)}">\n'
        f'<meta property="og:type" content="{esc(og_type)}">\n'
        f'<meta property="og:site_name" content="{esc(config.SITE_NAME)}">\n'
        f'<meta property="og:title" content="{esc(title)}">\n'
        f'<meta property="og:description" content="{esc(meta)}">\n'
        f'<meta property="og:url" content="{esc(og_url)}">\n'
        f'<meta property="og:image" content="{esc(og_image)}">\n'
        '<meta name="twitter:card" content="summary_large_image">\n'
        f'<meta name="twitter:title" content="{esc(title)}">\n'
        f'<meta name="twitter:description" content="{esc(meta)}">\n'
        f'<meta name="twitter:image" content="{esc(og_image)}">\n'
        f'<meta name="twitter:site" content="{esc(config.X_HANDLE)}">\n'
        f'<meta name="twitter:creator" content="{esc(config.X_HANDLE)}">\n'
        '<link rel="icon" href="/images/axolotl-favicon.webp" type="image/webp">\n'
        '<link rel="preconnect" href="https://fonts.googleapis.com">\n'
        '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>\n'
        '<link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,500;9..144,600;9..144,700&family=Poppins:wght@400;500;600;700&display=swap" rel="stylesheet">\n'
        '<link rel="stylesheet" href="/css/style.css">\n'
        f"{schema}\n</head>\n<body>\n"
        '<a class="skip-link" href="#main">Skip to content</a>\n'
        f"{header(active_href)}\n"
        f"<main id=\"main\">\n{content}\n</main>\n"
        f"{footer()}\n"
        "<script>"
        "(function(){"
        "var b=document.querySelector('[data-nav-burger]'),m=document.querySelector('.mobile-nav');"
        "if(b&&m){b.addEventListener('click',function(){"
        "var open=m.classList.toggle('is-open');b.setAttribute('aria-expanded',open?'true':'false');"
        "b.classList.toggle('is-active',open);"
        "document.body.classList.toggle('nav-open',open);});}"
        "var t=document.querySelector('[data-more-toggle]'),mm=document.querySelector('.more-menu');"
        "if(t&&mm){t.addEventListener('click',function(e){e.stopPropagation();"
        "var open=mm.classList.toggle('is-open');t.setAttribute('aria-expanded',open?'true':'false');});"
        "document.addEventListener('click',function(e){"
        "if(!e.target.closest('.more-wrap')){mm.classList.remove('is-open');"
        "t.setAttribute('aria-expanded','false');}});}"
        "})();"
        "</script>"
        "</body>\n</html>"
    )


# ---------------------------------------------------------------------------
# Content helpers
# ---------------------------------------------------------------------------
def process_article_body(a):
    """Heading ids, embed markers, and leading-title cleanup."""
    body = a["body_html"]

    # Strip side-tab accent borders from inline-styled content blocks.
    body = re.sub(r'\s*border-left\s*:\s*[^;"\']*;?', "", body)

    # Drop stray font-size / margin inline presentation so the type scale
    # stays fully controlled by style.css (docx2html occasionally emits them).
    body = re.sub(r'\s*(?:font-size|margin-top|margin-bottom|line-height)\s*:\s*[^;"\']*;?', "", body)

    # Remove now-empty style attributes left behind by the strip above.
    body = re.sub(r'\s+style=""', "", body)

    # .references-box divs carry legacy inline background/padding — let CSS own it.
    body = re.sub(r'(<div class="references-box")\s+style="[^"]*"', r"\1", body)

    # Replace [[EMBED_IMG:rid]] markers with inline <img> tags.
    def embed_repl(m):
        rid = m.group(1)
        return (f'<img class="article-img" src="/images/{a["num"]}-embedded-{rid}.webp" '
                'alt="Illustration" loading="lazy">')
    body = re.sub(r"\[\[EMBED_IMG:([^\]]+)\]\]", embed_repl, body)

    # Drop a leading paragraph that just repeats the title.
    def strip_first(m):
        txt = re.sub(r"<[^>]+>", "", m.group(1)).strip()
        return "" if txt.lower() == a["title"].lower() else m.group(0)
    fm = re.search(r"<p>(.*?)</p>", body, re.S)
    if fm:
        body = body[:fm.start()] + strip_first(fm) + body[fm.end():]

    # Phase 8: semantic inline anchors (verified phrases -> contextual links).
    for phrase, href, anchor, replace_all in config.SEMANTIC_INLINE.get(a["slug"], []):
        if phrase not in body:
            print(f"  !! inline anchor phrase not found in {a['slug']}: {phrase!r}")
            continue
        rx = re.compile(r"(?<![A-Za-z0-9])" + re.escape(phrase) + r"(?![A-Za-z0-9])")
        link = f'<a href="{href}">{html.escape(anchor)}</a>'
        body = rx.sub(lambda _m: link, body) if replace_all else rx.sub(link, body, count=1)

    # Assign s0..sN ids to every h2/h3/h4.
    counter = {"i": 0}

    def add_id(m):
        tag, attrs = m.group(1), m.group(2)
        attrs = re.sub(r'\s+id="[^"]*"', "", attrs)
        n = counter["i"]
        counter["i"] += 1
        return f"<h{tag}{attrs} id=\"s{n}\">"

    body = re.sub(r"<h([234])([^>]*)>", add_id, body)

    return body


def render_toc(headings):
    if not headings:
        return ""
    items = ""
    for i, (lvl, text) in enumerate(headings):
        cls = ' class="toc-sub"' if lvl > 2 else ""
        items += f'<li{cls}><a href="#s{i}">{esc(text)}</a></li>'
    return (
        f'<details class="toc-details" open><summary class="toc-summary">In this guide</summary>'
        f'<nav class="toc"><ol>{items}</ol></nav></details>'
    )


def article_card(a, img):
    return (
        '<article class="card">'
        f'<img class="thumb" src="{esc(img["url"])}" alt="{esc(img["alt"])}" '
        'loading="lazy" width="640" height="360">'
        '<div class="card-body">'
        f'<div class="meta">{esc(config.HUBS[a["hub"]]["cat"])}</div>'
        f'<h3><a href="/{esc(a["slug"])}/">{esc(a["title"])}</a></h3>'
        f'<p>{esc(a["intro"])}</p>'
        f'<a class="read-more" href="/{esc(a["slug"])}/">Read guide &rarr;</a>'
        "</div></article>"
    )


def hub_card(key, hub, count):
    return (
        f'<a class="card" href="/{key}/"><div class="card-body">'
        f'<div class="meta">{esc(hub["cat"])} &middot; {count} guides</div>'
        f'<h3>{esc(hub["title"])}</h3>'
        f'<p>{esc(hub["intro"])}</p>'
        f'<span class="read-more">Explore {esc(hub["cat"])} guides &rarr;</span>'
        "</div></a>"
    )


def breadcrumbs(hub_key):
    hub = config.HUBS[hub_key]
    return (
        f'<nav class="breadcrumbs" aria-label="Breadcrumb"><a href="/">Home</a> '
        f'&rsaquo; <a href="/{hub_key}/">{esc(hub["cat"])}</a></nav>'
    )


def breadcrumb_items_for_hub(key):
    hub = config.HUBS[key]
    label = hub["cat"]
    return [("Home", "/"), (label, f"/{key}/")]


def breadcrumb_items_for_article(a):
    return breadcrumb_items_for_hub(a["hub"])


def breadcrumb_list_node(items):
    return {
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": [
            {
                "@type": "ListItem",
                "position": i,
                "name": name,
                "item": config.SITE_URL + href,
            }
            for i, (name, href) in enumerate(items, 1)
        ],
    }


def breadcrumb_list_schema(items):
    return json.dumps(breadcrumb_list_node(items), ensure_ascii=False, separators=(",", ":"))


def add_breadcrumb_list_schema(json_ld, items):
    breadcrumb_node = breadcrumb_list_node(items)
    if not json_ld:
        return json.dumps(breadcrumb_node, ensure_ascii=False, separators=(",", ":"))
    data = json.loads(json_ld)
    if "@graph" in data:
        data["@graph"].append(breadcrumb_node)
        return json.dumps(data, ensure_ascii=False, separators=(",", ":"))
    return json.dumps({"@context": "https://schema.org", "@graph": [data, breadcrumb_node]},
                      ensure_ascii=False, separators=(",", ":"))


def html_fragment_to_text(fragment):
    return re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", " ", fragment))).strip()


def tool_breadcrumb_items(text, page_href, title):
    nav = re.search(r'<nav\b[^>]*aria-label="Breadcrumb"[^>]*>(.*?)</nav>', text, re.I | re.S)
    if nav:
        nav_html = nav.group(1)
        anchors = list(re.finditer(r'<a\b[^>]*href="([^"]+)"[^>]*>(.*?)</a>', nav_html, re.I | re.S))
        if anchors:
            items = [(html_fragment_to_text(m.group(2)), m.group(1)) for m in anchors]
            tail = html_fragment_to_text(re.sub(r'<a\b[^>]*>.*?</a>', ' ', nav_html, flags=re.I | re.S))
            tail = re.sub(r'[›]+', ' ', tail)
            tail = re.sub(r'\s+', ' ', tail).strip()
            if tail:
                items.append((tail, page_href))
            return items

    context_patterns = (
        r'Companion tool to the full <a href="([^"]+)">([^<]+)</a>',
        r'Read the full dosing and safety guide: <a href="([^"]+)">([^<]+)</a>',
    )
    for pattern in context_patterns:
        m = re.search(pattern, text, re.I | re.S)
        if m:
            return [("Home", "/"), (html_fragment_to_text(m.group(2)), m.group(1)), (title, page_href)]

    return [("Home", "/"), (title, page_href)]


def related_section(slug, articles):
    hub_key = slug.split("/")[0]
    hub = config.HUBS.get(hub_key)
    picks = []
    hrefs = set()
    if hub:
        href = f"/{hub_key}/"
        picks.append((href, hub["title"]))
        hrefs.add(href)
    # Resolve LINKING targets across articles, hubs, and tools.
    title_map = {f"/{a['slug']}/": a["title"] for a in articles.values()}
    for k, h in config.HUBS.items():
        title_map.setdefault(f"/{k}/", h["title"])
    for t in config.TOOLS.values():
        title_map.setdefault(f"/{t['slug']}/", t["title"])
    for t in config.LINKING.get(slug, []):
        href = f"/{t}/"
        if t != slug and href in title_map and href not in hrefs:
            hrefs.add(href)
            picks.append((href, title_map[href]))
    # Fallback 1: siblings in the same hub, nearest in reading order first.
    if len(picks) < 3:
        siblings = sorted(
            (a for a in articles.values()
             if a["hub"] == hub_key and a["slug"] != slug),
            key=lambda a: abs(a["num"] - articles[slug]["num"]),
        )
        for a in siblings:
            if len(picks) >= 3:
                break
            href = f"/{a['slug']}/"
            if href not in hrefs:
                hrefs.add(href)
                picks.append((href, a["title"]))
    # Fallback 2: flagship guides.
    for fs in ("axolotls/care-guide", "tank-setup/setup-guide", "health/refusing-to-eat"):
        if len(picks) >= 3:
            break
        if fs in articles and fs != slug:
            href = f"/{fs}/"
            if href not in hrefs:
                hrefs.add(href)
                picks.append((href, articles[fs]["title"]))
    links = "".join(
        f'<li><a href="{esc(href)}">{esc(label)}</a></li>' for href, label in picks
    )
    return f'<section class="related"><h2>Related guides</h2><ul>{links}</ul></section>'


def share_row(url, title):
    fb = f"https://www.facebook.com/sharer/sharer.php?u={html.escape(url, quote=True)}"
    tw = ("https://twitter.com/intent/tweet?"
          f"text={html.escape(title, quote=True)}&url={html.escape(url, quote=True)}")
    return (
        f'<div class="share-row"><a class="btn" href="{fb}">Share</a>'
        f'<a class="btn" href="{tw}">Tweet</a></div>'
    )


def person_schema(person, url):
    same_as = person.get("sameAs", [])
    node = {
        "@context": "https://schema.org",
        "@graph": [
            {
                "@type": "ProfilePage",
                "name": person["name"],
                "description": person["meta"],
                "url": url,
                "mainEntity": {"@id": url + "#person"},
            },
            {
                "@type": "Person",
                "@id": url + "#person",
                "name": person["name"],
                "jobTitle": person["role"],
                "description": person["summary"],
                "url": url,
                "worksFor": {"@type": "Organization", "name": config.SITE_NAME, "url": config.SITE_URL},
            },
        ],
    }
    if same_as:
        node["@graph"][1]["sameAs"] = same_as
    if person.get("email"):
        node["@graph"][1]["email"] = f"mailto:{person['email']}"
    return json.dumps(node, ensure_ascii=False, separators=(",", ":"))


def static_page_schema(key, cfg, url):
    schema_type = cfg.get("schema", "WebPage")
    node = {
        "@context": "https://schema.org",
        "@type": schema_type,
        "name": cfg["title"],
        "description": cfg["meta"],
        "url": url,
    }
    if key == "about":
        node["about"] = {
            "@type": "Organization",
            "name": config.SITE_NAME,
            "url": config.SITE_URL,
            "sameAs": config.ORGANIZATION_SAME_AS,
        }
    return json.dumps(node, ensure_ascii=False, separators=(",", ":"))


def article_schema(a, url):
    nodes = [{
        "@context": "https://schema.org",
        "@type": "Article",
        "headline": a["title"],
        "description": a["meta"],
        "datePublished": a["date_published"],
        "dateModified": a["date_modified"],
        "author": {
            "@type": "Person",
            "name": config.AUTHOR["name"],
            "url": config.SITE_URL + "/" + config.AUTHOR["slug"] + "/",
            "jobTitle": config.AUTHOR["role"],
            "sameAs": config.AUTHOR.get("sameAs", []),
        },
        "editor": {
            "@type": "Person",
            "name": config.EDITOR["name"],
            "url": config.SITE_URL + "/" + config.EDITOR["slug"] + "/",
            "jobTitle": config.EDITOR["role"],
            "sameAs": config.EDITOR.get("sameAs", []),
        },
        "publisher": {"@type": "Organization", "name": config.SITE_NAME},
        "mainEntityOfPage": url,
        "wordCount": a["words"],
    }]
    if a["faq"]:
        nodes.append({
            "@type": "FAQPage",
            "mainEntity": [
                {"@type": "Question", "name": q,
                 "acceptedAnswer": {"@type": "Answer", "text": ans}}
                for q, ans in a["faq"]
            ],
        })
    if len(nodes) == 1:
        return json.dumps(nodes[0], ensure_ascii=False)
    return json.dumps({"@context": "https://schema.org", "@graph": nodes},
                      ensure_ascii=False)


# ---------------------------------------------------------------------------
# Page renderers
# ---------------------------------------------------------------------------
def render_home(articles, img_map):
    def feat_card(slug):
        a = articles[slug]
        img = img_map[slug]
        return (
            '<article class="card">'
            f'<img class="thumb" src="{esc(img["url"])}" alt="{esc(img["alt"])}" '
            'loading="lazy" width="640" height="360">'
            '<div class="card-body">'
            f'<div class="meta">{esc(config.HUBS[a["hub"]]["cat"])}</div>'
            f'<h3><a href="/{esc(slug)}/">{esc(a["title"])}</a></h3>'
            f'<p>{esc(a["intro"])}</p>'
            f'<a class="read-more" href="/{esc(slug)}/">Read guide &rarr;</a>'
            "</div></article>"
        )

    # 1. Hero — full-width background image with text overlay
    hero = (
        '<section class="hero hero-home" style="--hero-image:url(/images/axolotl-home.webp)">'
        '<div class="container hero-shell">'
        '<div class="hero-copy">'
        f'<h1>{HOME["h1"]}</h1>'
        f'<p class="hero-text">{HOME["hero_text"]}</p>'
        f'<p class="hero-tagline">{HOME["hero_tagline"]}</p>'
        '<div class="hero-actions">'
        f'<a class="btn" href="/{HOME["featured"][0]}/">Start with the care guide</a>'
        '<a class="btn btn-ghost" href="/tools/">Browse tools</a>'
        "</div></div>"
        "</div></section>"
    )

    # 2. Quick-info bar (real facts)
    facts = "".join(
        f'<li class="fact"><span class="fact-label">{esc(label)}</span>'
        f'<span class="fact-value">{value}</span></li>'
        for label, value in QUICK_FACTS
    )
    quick = f'<section class="quick-info"><div class="container"><ul class="fact-list">{facts}</ul></div></section>'

    # 3. Start Here — asymmetric: one primary path + secondary paths
    start = [
        HOME["featured"][0],
        HOME["featured"][1],
        HOME["featured"][2],
    ]
    primary = start[0]
    a = articles[primary]
    img = img_map[primary]
    start_primary = (
        '<a class="start-primary" href="/' + esc(primary) + '/">'
        f'<img class="thumb" src="{esc(img["url"])}" alt="{esc(img["alt"])}" '
        'loading="lazy" width="640" height="360">'
        '<div class="card-body">'
        f'<div class="meta">{esc(config.HUBS[a["hub"]]["cat"])} &middot; Start here</div>'
        f'<h3>{esc(a["title"])}</h3>'
        f'<p>{esc(a["intro"])}</p>'
        '<p>An axolotl is a salamander that never grows up &mdash; at least not on the outside. Most amphibians go through metamorphosis and move onto land; axolotls skip that step, staying aquatic and reaching full sexual maturity while still looking like a larva. Biologists call this neoteny.</p>'
        '<p>The cause is one missing hormonal signal: the pituitary never tells the thyroid to release enough thyroxine, the hormone that triggers metamorphosis in other amphibians. Labs can force the change with hormone injections or high iodine doses, but it almost never happens on its own at home &mdash; and when it does, it usually signals hybridization with a tiger salamander or serious environmental stress, not a milestone.</p>'
        '<p>That larval body also makes their skin unkeratinized and highly absorbent &mdash; useful in the wild, risky in a tank, because anything in the water gets into the animal, good or bad. Their skeleton is cartilage, not bone, which is part of why a hard substrate bump or rough handling does real damage.</p>'
        '<span class="read-more">Begin here &rarr;</span>'
        "</div></a>"
    )
    start_secondary = "".join(feat_card(s) for s in start[1:])
    start_section = (
        '<section class="section start-here" aria-labelledby="start-title">'
        '<div class="container">'
        '<div class="section-head">'
        '<h2 id="start-title" class="section-title">Start Here</h2>'
        '<p class="section-note">New to axolotls? Begin with the essentials.</p>'
        '</div>'
        '<div class="start-grid">'
        f"{start_primary}"
        f'<div class="start-secondary">{start_secondary}</div>'
        "</div></div></section>"
    )

    # 4. Featured guides — editor's picks
    picks = [s for s in HOME["picks"] if s in articles][:4]
    if picks:
        pick_cards = "".join(feat_card(s) for s in picks)
        featured = (
            '<section class="section featured" aria-labelledby="featured-title">'
            '<div class="container">'
            '<div class="section-head">'
            '<h2 id="featured-title" class="section-title">Featured Guides</h2>'
            '<p class="section-note">Editor&rsquo;s picks to read next.</p>'
            "</div>"
            f'<div class="grid-4">{pick_cards}</div>'
            "</div></section>"
        )
    else:
        featured = ""

    # 5. Browse by Topic — hub grid
    hub_cards = ""
    for key, hub in config.HUBS.items():
        count = sum(1 for art in articles.values() if art["hub"] == key)
        hub_cards += hub_card(key, hub, count)
    topics = (
        '<section class="section topics" aria-labelledby="topics-title">'
        '<div class="container">'
        '<div class="section-head">'
        '<h2 id="topics-title" class="section-title">Browse by Topic</h2>'
        '<p class="section-note">Jump straight to the area you need.</p>'
        "</div>"
        f'<div class="topic-grid">{hub_cards}</div>'
        "</div></section>"
    )

    # 6. Tools discovery
    tool_cards = "".join(
        f'<a class="tool-card" href="/{esc(t["slug"])}/">'
        f'<h3>{esc(t["title"])}</h3>'
        "<p>Free interactive tool for axolotl keepers.</p>"
        '<span class="read-more">Open tool &rarr;</span></a>'
        for t in config.TOOLS.values()
    )
    tools = (
        '<section class="section tools" aria-labelledby="tools-title">'
        '<div class="container">'
        '<div class="section-head">'
        '<h2 id="tools-title" class="section-title">Handy Tools</h2>'
        '<p class="section-note">Calculators &amp; trackers.</p>'
        "</div>"
        f'<div class="tool-grid">{tool_cards}</div>'
        "</div></section>"
    )

    # 7. Call to action
    cta = (
        '<section class="cta-band">'
        '<div class="container cta-inner">'
        f"<h2>{HOME['cta_title']}</h2>"
        f"<p>{HOME['cta_text']}</p>"
        f'<a class="btn" href="{HOME["cta_link"]}">{HOME["cta_label"]}</a>'
        "</div></section>"
    )

    body = (
        f"{hero}{quick}"
        f"{start_section}{featured}{topics}{tools}"
        f"{cta}"
    )
    return page_html(HOME["title_tag"], HOME["meta"], config.SITE_URL + "/",
                     body, "", "website", HOME["hero_img"])


def render_hub(key, hub, articles, img_map):
    if key == "axolotls":
        page_title = "Axolotl Care: Tank Setup, Diet, Health & More"
        page_meta = "Start with the complete axolotl care guide or explore specific care topics like tank setup, care basics, diet, health, cost, tools, and supporting guides."
        page_h1 = "Axolotl Care"
        page_intro = "Start with the complete care guide, or explore specific care topics below if you already know what you need."
        guide = articles["axolotls/care-guide"]
        guide_img = img_map["axolotls/care-guide"]

        def hub_tile(href, title, desc, meta):
            return (
                f'<a class="hub-card" href="{href}">'
                f'<div class="meta">{esc(meta)}</div>'
                f'<h3>{esc(title)}</h3>'
                f'<p>{esc(desc)}</p>'
                f'<span class="read-more">Explore {esc(title)} &rarr;</span>'
                "</a>"
            )

        featured = (
            '<a class="start-primary care-hub-featured" href="/axolotls/care-guide/">'
            f'<img class="thumb" src="{esc(guide_img["url"])}" alt="{esc(guide_img["alt"])}" '
            'loading="lazy" width="640" height="360">'
            '<div class="card-body">'
            '<div class="meta">Foundational guide</div>'
            f'<h3>{esc(guide["title"])}</h3>'
            f'<p>{esc(guide["intro"])}</p>'
            '<span class="read-more">Start here &rarr;</span>'
            "</div></a>"
        )

        primary_cards = [
            hub_tile(
                "/tank-setup/",
                "Tank Setup",
                "Build a cool, stable habitat with the right tank size, substrate, filtration, temperature, and water changes.",
                "Primary care topic",
            ),
            hub_tile(
                "/care-basics/",
                "Care Basics & Water",
                "Beginner axolotl knowledge, behavior, handling, and the water-quality fundamentals that shape every care decision.",
                "Primary care topic",
            ),
            hub_tile(
                "/diet/",
                "Diet & Feeding",
                "Learn what axolotls eat, how often to feed, and how to avoid overfeeding and impaction.",
                "Primary care topic",
            ),
            hub_tile(
                "/health/",
                "Health",
                "Spot warning signs early and respond to common problems like fungus, parasites, stress, and refusal to eat.",
                "Primary care topic",
            ),
            hub_tile(
                "/tools/",
                "Tools",
                "Use calculators and checkers for conditioning, feeding, tank size, and symptom triage.",
                "Support tool",
            ),
            hub_tile(
                "/cost-and-buying/",
                "Cost & Buying",
                "Plan the initial setup, monthly budget, morph prices, and safe places to buy.",
                "Primary care topic",
            ),
        ]

        secondary_cards = [
            hub_tile(
                "/biology-and-science/",
                "Biology",
                "Understand the science behind neoteny, regeneration, and the wild habitat.",
                "Supporting topic",
            ),
            hub_tile(
                "/morphs/",
                "Morphs",
                "Compare colors, patterns, and the genetics behind each morph.",
                "Supporting topic",
            ),
            hub_tile(
                "/breeding/",
                "Breeding",
                "Learn conditioning, courtship, eggs, larvae, and breeding ethics.",
                "Supporting topic",
            ),
            hub_tile(
                "/legal/",
                "Legal",
                "Check where axolotls are restricted and what the rules mean for owners.",
                "Supporting topic",
            ),
        ]

        body = (
            f'<section class="hub-hero"><div class="container">'
            f'<nav class="breadcrumbs" aria-label="Breadcrumb"><a href="/">Home</a>'
            f' &rsaquo; {esc(hub["cat"])}'
            f'</nav><h1>{esc(page_h1)}</h1>'
            f'<p class="hub-intro">{esc(page_intro)}</p>'
            f'</div></section>'
            f'<div class="container page">'
            f'{featured}'
            '<section class="section" aria-labelledby="primary-care-title">'
            '<div class="section-head">'
            '<h2 id="primary-care-title" class="section-title">Primary Care Topics</h2>'
            '<p class="section-note">Start with these six routes through care.</p>'
            '</div>'
            f'<div class="grid-3">{"".join(primary_cards)}</div>'
            '</section>'
            '<section class="section" aria-labelledby="supporting-topics-title">'
            '<div class="section-head">'
            '<h2 id="supporting-topics-title" class="section-title">Supporting Topics</h2>'
            '<p class="section-note">Context for the broader care journey.</p>'
            '</div>'
            f'<div class="grid-4">{"".join(secondary_cards)}</div>'
            '</section>'
            '</div>'
        )
        json_ld = breadcrumb_list_schema(breadcrumb_items_for_hub(key))
        return page_html(page_title, page_meta, config.SITE_URL + "/axolotls/",
                         body, "/axolotls/", "website", guide_img["url"], json_ld)

    guides = sorted(
        [a for a in articles.values() if a["hub"] == key],
        key=lambda a: a["num"],
    )
    if not guides:
        listing = ('<div class="hub-empty"><h2>Guides coming soon</h2>'
                   "<p>This section is being written. Start with the "
                   '<a href="/axolotls/">complete care guide</a> in the meantime.</p></div>')
        lead = ""
    else:
        lead = article_card(guides[0], img_map[guides[0]["slug"]])
        rest = "".join(article_card(a, img_map[a["slug"]]) for a in guides[1:])
        listing = (
            '<h2 class="section-title">All ' + esc(hub["cat"]) + ' Guides</h2>'
            f'<div class="grid-3">{lead}{rest}</div>'
        )

    # Related topics — other hubs, human-labeled
    related = "".join(
        f'<a class="topic-chip" href="/{k}/">{esc(h["cat"])}</a>'
        for k, h in config.HUBS.items() if k != key
    )
    body = (
        f'<section class="hub-hero"><div class="container">'
        f'<nav class="breadcrumbs" aria-label="Breadcrumb"><a href="/">Home</a>'
        f' &rsaquo; {esc(hub["cat"])}</nav>'
        f'<h1>{esc(hub["h1"])}</h1>'
        f'<p class="hub-intro">{esc(hub["intro"])}</p>'
        "</div></section>"
        f'<div class="container page">{listing}'
        '<div class="hub-related"><h2 class="section-title">Related Topics</h2>'
        f'<div class="chip-row">{related}</div></div>'
        "</div>"
    )
    json_ld = breadcrumb_list_schema(breadcrumb_items_for_hub(key))
    return page_html(hub["title_tag"], hub["meta"], config.SITE_URL + f"/{key}/",
                     body, f"/{key}/", "website", None, json_ld)

def render_article(slug, a, articles, img_map):
    url = config.SITE_URL + f"/{slug}/"
    img = img_map.get(slug, {"url": "/images/axolotl-home.webp", "alt": a["title"]})
    toc = render_toc(a["headings"])
    author_url = "/" + config.AUTHOR["slug"] + "/"
    editor_url = "/" + config.EDITOR["slug"] + "/"
    body = (
        f'<div class="container article-page">'
        f"{breadcrumbs(a['hub'])}"
        '<header class="article-head">'
        f'<h1>{esc(a["title"])}</h1>'
        f'<p class="standfirst">{esc(a["intro"])}</p>'
        f'<div class="article-byline">By <a href="{author_url}">{esc(config.AUTHOR["name"])}</a> &middot; '
        f'Edited by <a href="{editor_url}">{esc(config.EDITOR["name"])}</a> &middot; '
        f'Updated {a["date_modified"]} &middot; {a["words"]:,} words</div>'
        "</header>"
        f'<figure class="article-hero"><img class="hero-img" src="{esc(img["url"])}" '
        f'alt="{esc(img["alt"])}" width="1200" height="800"></figure>'
        '<div class="article-grid">'
        f'<aside class="article-toc">{toc}</aside>'
        f'<div class="article-main"><div class="article-body">{process_article_body(a)}</div>'
        f"{related_section(slug, articles)}"
        f"{share_row(url, a['title'])}"
        "</div></div></div>"
    )
    active = "/" + slug.split("/")[0] + "/"
    json_ld = add_breadcrumb_list_schema(article_schema(a, url), breadcrumb_items_for_article(a))
    return page_html(a["title_tag"], a["meta"], url, body, active,
                     "article", img["url"], json_ld)


def render_simple(key, cfg):
    url = config.SITE_URL + f"/{key}/"
    body = (
        f'<div class="container page article-layout"><h1>{esc(cfg["title"])}</h1>'
        f'<div class="article-body">{cfg["body"]}</div></div>'
    )
    return page_html(cfg["title"], cfg["meta"], url, body,
                     og_type="website",
                     json_ld=static_page_schema(key, cfg, url))


def render_profile(key, person):
    url = config.SITE_URL + f"/{person['slug']}/"
    links = "".join(
        f'<li><a href="{esc(href)}">{esc(label)}</a></li>'
        for label, href in person.get("links", [])
    )
    experience = ""
    if person.get("experience"):
        rows = "".join(
            "<li>"
            f"<strong>{esc(exp['organization'])}</strong>"
            f"<span>{esc(exp['role'])}</span>"
            f"<span>{esc(exp['dates'])}</span>"
            f"<span>{esc(exp['duration'])}</span>"
            f"<span>{esc(exp['location'])}</span>"
            "</li>"
            for exp in person["experience"]
        )
        experience = f'<h2>Experience</h2><ul>{rows}</ul>'
    extra = f'<div class="article-body">{experience}</div>' if experience else ""
    body = (
        '<div class="container page article-layout">'
        f'<h1>{esc(person["name"])}</h1>'
        f'<p class="standfirst">{esc(person["meta"])}</p>'
        f'<div class="callout"><p><strong>Role:</strong> {esc(person["role"])}</p>'
        f'<p>{esc(person["summary"])}</p>'
        f'<p><strong>Focus:</strong> {esc(person["focus"])}</p>'
        f'<ul>{links}</ul></div>'
        f"{extra}"
        '</div>'
    )
    return page_html(person["name"], person["meta"], url, body, "/about/",
                     og_type="profile", json_ld=person_schema(person, url))


def render_tools_index():
    url = config.SITE_URL + "/tools/"
    cards = "".join(
        f'<a class="tool-card" href="/{esc(t["slug"])}/">'
        f'<h3>{esc(t["title"])}</h3>'
        f"<p>{esc(TOOL_DESCS.get(t['slug'].split('/')[-1], 'Free interactive tool for axolotl keepers.'))}</p>"
        '<span class="read-more">Open tool &rarr;</span></a>'
        for t in config.TOOLS.values()
    )
    # Knowledge behind the tools — grounds each utility in the guide it comes from.
    start_here = [
        ("/tank-setup/setup-guide/", "Tank Setup Guide", "The step-by-step setup every tool assumes"),
        ("/tank-setup/water-parameters-cycling/", "Water Parameters & Cycling", "The science behind ppm, ammonia, and nitrite readings"),
        ("/diet/feeding-schedule-by-age/", "Feeding Frequency by Life Stage", "The age-and-size schedule the generator follows"),
        ("/health/refusing-to-eat/", "Why Is My Axolotl Refusing to Eat?", "What the symptom checker points you to first"),
    ]
    start_links = "".join(
        f'<li><a class="start-here-link" href="{h}">{esc(t)}</a><span class="start-here-note">{esc(n)}</span></li>'
        for h, t, n in start_here
    )
    body = (
        '<section class="hub-hero"><div class="container">'
        '<nav class="breadcrumbs" aria-label="Breadcrumb"><a href="/">Home</a> &rsaquo; Tools</nav>'
        "<h1>Axolotl Care Tools</h1>"
        "<p class=\"hub-intro\">Free calculators and trackers for axolotl keepers &mdash; no sign-up required, all in your browser.</p>"
        "</div></section>"
        f'<div class="container page">'
        '<h2 class="sr-only">All axolotl tools</h2>'
        f'<div class="tool-grid">{cards}</div>'
        '<section class="tools-starthere" aria-labelledby="tools-start-title">'
        '<h2 id="tools-start-title" class="section-title">Start with the knowledge behind these tools</h2>'
        f'<ul class="tools-starthere-list">{start_links}</ul></section></div>'
    )
    json_ld = breadcrumb_list_schema([("Home", "/"), ("Tools", "/tools/")])
    return page_html("Axolotl Tools & Calculators",
                     "Free axolotl calculators: tank size, water conditioner dose, feeding schedule, nitrogen cycle tracker, symptom checker.",
                     url, body, "/tools/", "website", None, json_ld)


def render_search():
    url = config.SITE_URL + "/search/"
    popular = "".join(
        f'<a class="topic-chip" href="/search/?q={quote(q, safe="")}">{esc(label)}</a>'
        for label, q in POPULAR_SEARCHES
    )
    topic_chips = "".join(
        f'<a class="topic-chip" href="/{esc(k)}/">{esc(h["cat"])}</a>'
        for k, h in config.HUBS.items()
    )
    body = (
        '<section class="search-hero"><div class="container">'
        '<nav class="breadcrumbs" aria-label="Breadcrumb"><a href="/">Home</a> &rsaquo; Search</nav>'
        "<h1>Search Axolotl Guides</h1>"
        '<form id="search-form" role="search" class="search-form" action="/search/" method="get">'
        '<label class="sr-only" for="search-input">Search axolotl guides</label>'
        '<div class="search-row">'
        '<input id="search-input" class="search-input" type="search" name="q" '
        'placeholder="What are you looking for?" autocomplete="off" spellcheck="false">'
        '<button type="submit" class="btn search-submit">Search</button>'
        "</div></form>"
        "</div></section>"
        '<div class="container search-body">'
        '<div id="search-status" class="search-status" role="status" aria-live="polite">'
        "</div>"
        '<section id="search-empty" class="search-empty" aria-label="Popular searches">'
        f'<h2>Popular searches</h2><div class="chip-row">{popular}</div>'
        f"<h2>Browse a topic</h2><div class=\"chip-row\">{topic_chips}</div>"
        "</section>"
        '<section id="search-results" class="search-results" aria-label="Search results" hidden>'
        "</section>"
        '<div id="search-null" class="search-null" hidden>'
        '<h2 id="search-null-title"></h2>'
        '<p>Try a broader search or browse a topic.</p>'
        f'<div class="chip-row">{topic_chips}</div>'
        "</div>"
        '<noscript><p class="search-note">Search requires JavaScript. '
        'Browse <a href="/tools/">tools</a> or use the site menu instead.</p></noscript>'
        "</div>"
        '<script src="/js/search.js" defer></script>'
    )
    json_ld = breadcrumb_list_schema([("Home", "/"), ("Search", "/search/")])
    return page_html("Search Axolotl Guides",
                     "Search every axolotl guide — care, tank setup, diet, health, breeding, morphs, and more.",
                     url, body, "/search/", "website", None, json_ld)


def strip_html_to_text(body_html):
    """Plain-text version of an article body for the search index.

    Block-level close tags become newlines so the client can pull a relevant,
    query-specific passage (paragraph) for the excerpt instead of the intro.
    """
    txt = re.sub(r"</(?:p|li|h[1-6]|tr|blockquote|div)[^>]*>", "\n", body_html)
    txt = re.sub(r"<[^>]+>", " ", txt)
    txt = html.unescape(txt)
    txt = re.sub(r"[ \t]+", " ", txt)
    txt = re.sub(r"\n\s*\n+", "\n", txt)
    return txt.strip()


def _tool_subtitle(fname):
    """Extract the one-line subtitle from a self-contained tool page source."""
    try:
        src = os.path.join(SRC, fname)
        with open(src, encoding="utf-8", errors="ignore") as fh:
            h = fh.read()
        m = re.search(r'class="subtitle"[^>]*>(.*?)</p>', h, re.S)
        if m:
            return re.sub(r"<[^>]+>", " ", m.group(1)).strip()
    except OSError:
        pass
    return ""


def build_search_index(articles):
    """Write search-index.json for client-side search (Phase 9).

    Each entry carries structured metadata so the client can rank and render
    semantically: title, description (dek), url, cluster, page type, headings,
    and the plain-text article body.  Template chrome (nav/footer/cookie text)
    is never included because the text is derived from the article body HTML
    only — header, footer, and sidebar markup live in the page shell, not here.
    """
    items = []

    def add_entry(entry):
        entry.setdefault("headings", [])
        items.append(entry)

    for slug, a in articles.items():
        entry = {
            "title": a["title"],
            "url": f"/{slug}/",
            "type": "article",
            "role": "article",
            "cluster": a["hub"],
            "category": config.HUBS[a["hub"]]["cat"],
            "dek": a["intro"],
            "headings": [text for _, text in a["headings"]],
            "text": strip_html_to_text(a["body_html"]),
        }
        act = config.SEARCH_ACTIONS.get(slug)
        if act:
            entry["action"] = {"label": act["label"], "url": f"/{slug}/",
                               "kind": act["kind"]}
        add_entry(entry)

    for key, hub in config.HUBS.items():
        kw = " ".join(hub.get("keywords", []))
        cluster_titles = [a["title"] for slug, a in articles.items()
                          if a["hub"] == key]
        add_entry({
            "title": hub["title"],
            "url": f"/{key}/",
            "type": "hub",
            "role": "hub",
            "cluster": key,
            "category": hub["cat"],
            "dek": hub["intro"],
            "headings": [],
            "text": f"{hub['intro']} {kw} {chr(10)}" +
                    chr(10).join(sorted(set(cluster_titles))).strip(),
        })

    for fname, t in config.TOOLS.items():
        stem = t["slug"].split("/")[-1]
        desc = TOOL_DESCS.get(stem, "Free interactive tool for axolotl keepers.")
        subtitle = _tool_subtitle(fname)
        text = f"{t['title']}. {desc} {subtitle}".strip()
        add_entry({
            "title": t["title"],
            "url": f"/{t['slug']}/",
            "type": "tool",
            "role": "tool",
            "cluster": "tools",
            "category": "Tools",
            "dek": desc,
            "headings": [t["title"]],
            "text": text,
            "action": {"label": "Open tool", "url": f"/{t['slug']}/", "kind": "tool"},
        })

    for key, page in SIMPLE.items():
        add_entry({
            "title": page["title"],
            "url": f"/{key}/",
            "type": "page",
            "role": "page",
            "cluster": "site",
            "category": "Site",
            "dek": page["meta"],
            "headings": [],
            "text": strip_html_to_text(page["body"]),
        })

    for person in PROFILE_PAGES.values():
        add_entry({
            "title": person["name"],
            "url": f"/{person['slug']}/",
            "type": "profile",
            "role": "profile",
            "cluster": "site",
            "category": "Site",
            "dek": person["meta"],
            "headings": [],
            "text": person["summary"],
        })

    seen = set()
    unique = []
    for item in items:
        if item["url"] in seen:
            continue
        seen.add(item["url"])
        unique.append(item)

    with open(os.path.join(PUBLIC, "search-index.json"), "w", encoding="utf-8") as fh:
        json.dump(unique, fh, ensure_ascii=False, separators=(",", ":"))
    return len(unique)


def render_404():
    url = config.SITE_URL + "/404.html"
    body = (
        '<div class="container error-page"><h1>404</h1>'
        '<p>That page doesn&rsquo;t exist. Try the <a href="/">homepage</a> or one of the guides below.</p></div>'
    )
    return page_html("Page Not Found", "The page you are looking for does not exist.",
                     url, body)


# ---------------------------------------------------------------------------
# Site files
# ---------------------------------------------------------------------------
def copy_tools():
    """Copy the self-contained tool HTML files verbatim."""
    written = []
    for fname, t in config.TOOLS.items():
        src = os.path.join(SRC, fname)
        if not os.path.exists(src):
            print("  !! missing tool:", fname)
            continue
        dst_dir = os.path.join(PUBLIC, t["slug"])
        ensure_dir(dst_dir)
        with open(src, "rb") as fh:
            data = fh.read()
        text = data.decode("utf-8", errors="ignore")
        if '<link rel="canonical"' not in text:
            tag = f'<link rel="canonical" href="{config.SITE_URL}/{t["slug"]}/">'
            text = text.replace("</head>", tag + "</head>", 1)
        if 'name="description"' not in text:
            desc = TOOL_DESCS.get(fname, TOOL_DESCS.get(t["slug"].split("/")[-1],
                                                        "Free interactive tool for axolotl keepers."))
            meta = (f'<meta name="description" content="{esc(desc)}">'
                    f'<meta property="og:description" content="{esc(desc)}">'
                    f'<meta name="twitter:description" content="{esc(desc)}">')
            text = text.replace("</head>", meta + "</head>", 1)
        page_url = config.SITE_URL + f"/{t['slug']}/"
        fallback_image = config.SITE_URL + "/images/axolotl-home.webp"
        x_handle = "@myaxolotls"

        def find_meta(attr_name, attr_kind):
            patterns = (
                rf'<meta\b[^>]*\b{attr_kind}="{re.escape(attr_name)}"[^>]*\bcontent="([^"]*)"',
                rf'<meta\b[^>]*\bcontent="([^"]*)"[^>]*\b{attr_kind}="{re.escape(attr_name)}"',
            )
            for pattern in patterns:
                m = re.search(pattern, text, re.I)
                if m:
                    return html.unescape(m.group(1))
            return None

        social_title = find_meta("og:title", "property") or find_meta("title", "name")
        if not social_title:
            m = re.search(r'<title>(.*?)</title>', text, re.I | re.S)
            social_title = html.unescape(re.sub(r'\s+', ' ', m.group(1)).strip()) if m else t["slug"].split("/")[-1]
        social_desc = (find_meta("og:description", "property") or
                       find_meta("description", "name") or
                       TOOL_DESCS.get(fname, TOOL_DESCS.get(t["slug"].split("/")[-1],
                                                           "Free interactive tool for axolotl keepers.")))
        social_image = find_meta("og:image", "property") or fallback_image
        if not social_image.startswith("http"):
            social_image = config.SITE_URL + social_image if social_image.startswith("/") else fallback_image
        social_tags = (
            r'<meta\b[^>]*(?:property="og:(?:title|description|type|url|site_name|image)"|'
            r'name="twitter:(?:card|title|description|image|site|creator)")[^>]*>'
        )
        text = re.sub(social_tags, "", text, flags=re.I)
        if 'BreadcrumbList' not in text:
            h1 = re.search(r'<h1\b[^>]*>(.*?)</h1>', text, re.I | re.S)
            tool_title = html_fragment_to_text(h1.group(1)) if h1 else t["title"]
            breadcrumb_items = tool_breadcrumb_items(text, f'/{t["slug"]}/', tool_title)
            breadcrumb_json = breadcrumb_list_schema(breadcrumb_items)
            text = text.replace("</head>", f'<script type="application/ld+json">{breadcrumb_json}</script>\n</head>', 1)
        inject = (
            f'<meta property="og:title" content="{esc(social_title)}">\n'
            f'<meta property="og:description" content="{esc(social_desc)}">\n'
            '<meta property="og:type" content="website">\n'
            f'<meta property="og:url" content="{esc(page_url)}">\n'
            f'<meta property="og:site_name" content="{esc(config.SITE_NAME)}">\n'
            f'<meta property="og:image" content="{esc(social_image)}">\n'
            '<meta name="twitter:card" content="summary_large_image">\n'
            f'<meta name="twitter:title" content="{esc(social_title)}">\n'
            f'<meta name="twitter:description" content="{esc(social_desc)}">\n'
            f'<meta name="twitter:image" content="{esc(social_image)}">\n'
            f'<meta name="twitter:site" content="{esc(x_handle)}">\n'
            f'<meta name="twitter:creator" content="{esc(x_handle)}">\n'
        )
        text = text.replace("</head>", inject + "</head>", 1)
        data = text.encode("utf-8")
        with open(os.path.join(dst_dir, "index.html"), "wb") as fh:
            fh.write(data)
        written.append(t["slug"])
    return written


def copy_downloads(articles):
    """Copy PDFs referenced as /downloads/... from the source dir."""
    wanted = set()
    for a in articles.values():
        for m in re.finditer(r"/downloads/([A-Za-z0-9._%+-]+)", a["body_html"]):
            wanted.add(m.group(1))
    if not wanted:
        return []
    dl_dir = os.path.join(PUBLIC, "downloads")
    ensure_dir(dl_dir)
    copied = []
    for name in sorted(wanted):
        src = os.path.join(SRC, name)
        if not os.path.exists(src):
            print("  !! missing download:", name)
            continue
        with open(src, "rb") as fh:
            data = fh.read()
        with open(os.path.join(dl_dir, name), "wb") as fh:
            fh.write(data)
        copied.append(name)
    return copied


def write_sitemap(articles):
    base = config.SITE_URL
    locs = [base]
    entries = [(base, 0.9)]
    entries += [(base + "/search/", 0.4)]
    for key in SIMPLE:
        prio = 0.3
        if key == "privacy":
            prio = 0.2
        elif key == "editorial-policy":
            prio = 0.25
        entries += [(base + f"/{key}/", prio)]
    for person in PROFILE_PAGES.values():
        entries += [(base + f"/{person['slug']}/", 0.3)]
    entries += [(base + "/tools/", 0.6)]
    for k in config.HUBS:
        entries += [(config.SITE_URL + f"/{k}/", 0.8)]
    for t in config.TOOLS.values():
        entries += [(config.SITE_URL + f"/{t['slug']}/", 0.5)]
    for a in articles.values():
        entries += [(config.SITE_URL + f"/{a['slug']}/", 0.8)]

    article_lastmod = {
        config.SITE_URL + f"/{a['slug']}/": a["date_modified"]
        for a in articles.values()
    }
    seen = set()
    rows = []
    for loc, prio in entries:
        if loc in seen:
            continue
        seen.add(loc)
        lastmod = article_lastmod.get(loc, TODAY)
        rows.append(
            f"  <url><loc>{loc}</loc><lastmod>{lastmod}</lastmod>"
            f"<changefreq>monthly</changefreq><priority>{prio}</priority></url>"
        )
    sitemap = (
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
        + "\n".join(rows) + "\n</urlset>\n"
    )
    with open(os.path.join(PUBLIC, "sitemap.xml"), "w", encoding="utf-8") as fh:
        fh.write(sitemap)


def write_site_files():
    with open(os.path.join(PUBLIC, "robots.txt"), "w", encoding="utf-8") as fh:
        fh.write(f"User-agent: *\nAllow: /\n\nSitemap: {config.SITE_URL}/sitemap.xml\n")
    with open(os.path.join(PUBLIC, "ads.txt"), "w", encoding="utf-8") as fh:
        fh.write("google.com, pub-0000000000000000, DIRECT, f08c47fec0942fa0\nthis-is-an-adstxt-verification-marker\n")
    sec_dir = os.path.join(PUBLIC, ".well-known")
    ensure_dir(sec_dir)
    with open(os.path.join(sec_dir, "security.txt"), "w", encoding="utf-8") as fh:
        fh.write(f"Contact: mailto:{config.AUTHOR['email']}\nPreferred-Languages: en\nExpires: 2027-01-01\n")


# ---------------------------------------------------------------------------
# main
# ---------------------------------------------------------------------------
def main():
    print("1/6  Converting articles ...")
    articles = build_articles()
    print(f"      {len(articles)} articles")

    print("2/6  Optimizing images ...")
    img_map = build_image_map(articles)
    print(f"      {len(img_map)} featured images")
    build_site_assets()

    print("3/6  Rendering home ...")
    write_page(".", "index.html", render_home(articles, img_map))

    print("4/6  Rendering hubs & articles ...")
    for key, hub in config.HUBS.items():
        write_page(key, "index.html", render_hub(key, hub, articles, img_map))
    for slug, a in articles.items():
        write_page(slug, "index.html", render_article(slug, a, articles, img_map))

    print("5/6  Rendering tools, people, simple pages, search, 404 ...")
    write_page("tools", "index.html", render_tools_index())
    copy_tools()
    copy_downloads(articles)
    write_page("search", "index.html", render_search())
    for key, cfg in SIMPLE.items():
        write_page(key, "index.html", render_simple(key, cfg))
    for key, person in PROFILE_PAGES.items():
        write_page(person["slug"], "index.html", render_profile(key, person))
    write_page(".", "404.html", render_404())

    print("6/6  Writing search index, sitemap, robots, ads, security, report ...")
    n_index = build_search_index(articles)
    print(f"      search index: {n_index} entries")
    write_sitemap(articles)
    write_site_files()

    total_words = sum(a["words"] for a in articles.values())
    hub_keyed = len([s for s in articles if s in config.HUBS])
    pages = 1 + len(config.HUBS) + (len(articles) - hub_keyed) \
        + 1 + len(config.TOOLS) + len(SIMPLE) + len(PROFILE_PAGES) + 1
    report = {
        "generated": TODAY,
        "site_url": config.SITE_URL,
        "articles": len(articles),
        "images": len(img_map),
        "words": total_words,
        "pages": pages,
    }
    with open(os.path.join(PUBLIC, "build-report.json"), "w", encoding="utf-8") as fh:
        json.dump(report, fh, indent=2)

    print(f"\nDone. {report['articles']} articles, {report['images']} images, "
          f"{report['words']:,} words, {report['pages']} pages.")


if __name__ == "__main__":
    main()
