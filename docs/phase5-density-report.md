# Phase 5 — Reading-Density Report (final)

Status after automated fixes + content-density edits: rebuild clean (106 articles, 129 pages), corpus integrity check passes (158 tables, no misaligned tables, no `<p><div` nesting).

## Content-density edits applied in `build/docx2html.py`

Applied via per-article `article_body_overrides(slug, html)` using the shared `_to_label_list` / `_to_label_list2` helpers (prose paragraphs whose lead phrase is bold in the source become `<ul>`/`<ol>` list items). All conversions verified against the source docx — no content fabricated.

| Article | Change | Result |
|---|---|---|
| `tank-setup/water-parameters-cycling` | Stage 1/Stage 2 + GH/KH leads → `<h3>`; 5-step emergency response → `<ol>`; 6 ammonia-spike causes → `<ol>`; 5 cycle-crash causes → `<ol>`; 4 prevention foundations → `<ol>` | `tables=False` stays (prose, not tabular) |
| `tank-setup/temperature` | 6 tank-location paras → `<ul>`; 9 "why isn't it cooling" diagnosis/fix paras → `<ol>`; 5 cooling-mistake paras → `<ul>` | run 10 → 6 |
| `tank-setup/water-conditioners` | 3 harm-mechanism paras → `<ul>`; 2 dosing-scenario paras → `<ul>`; 6-step emergency timeline → `<ol>` | run 8 → 7 (rest is FAQ) |
| `diet/live-vs-frozen-food` | 5 special-situation paras → `<ul>` | run 7 → 5 |
| `tank-setup/substrate-and-impaction` | 4 safety criteria → `<ul>`; 4 water-parameter paras → `<ul>` | unheaded reduced |

Remaining longest runs are genuine prose (liquid-vs-strips comparison, chiller pros/cons, prep/storage narrative), interleaved prose+label sections (six substrate behaviors), or the FAQ block — no further faithful list/table conversion is possible without fabricating content.

## What was automated in `build/docx2html.py`

1. **Flattened pipe-grid recovery** (`recover_grid_tables`): detects runs of short cell-style paragraphs separated by `---` marker paragraphs and rebuilds real `<table>` structures. Applied to care charts, legal permit tables, and culture-guide comparison grids.
2. **Glued parameter-table recovery** (`recover_glued_param_table`): rebuilds the 4-row water-parameter table for `diet/best-foods-list` (was one glued paragraph). Fixed so the table is emitted outside any `<p>` wrapper so tokenizers/parsers see it.
3. **Glued food-format table recovery** (`recover_glued_food_table`): rebuilds the 5-column food-format comparison (Format / Nutrient Bioavailability / Disease Risk / Digestibility / Storage × Live / Frozen / Pellets) in `diet/best-foods-list` from another glued paragraph.
4. **Prose sub-heading promotion** (`recover_prose_headings`): promotes 11 standalone label paragraphs (`<p>Earthworms…</p>`, `<p>Juveniles (3–6 Inches)</p>`, etc.) to `<h3>` in `diet/best-foods-list`, splitting a 16-paragraph flat run.
5. **Reference-box `<p>` unwrap**: strips a stray `<p>` that wrapped `<div class="references-box">` in `tank-setup/setup-guide`.
6. **Split thresholds lowered**: `max_words` 120 → 100, `target_words` 90 → 72.

## Before / after (on the 25 flagged articles)

| Metric | Before | After |
|---|---|---|
| Longest paragraph run (many flagged) | 14–32 consecutive `<p>` | 2 for most |
| `diet/best-foods-list` longest run | 16 `<p>` / 500w unheaded | 5 `<p>` / 220w unheaded |
| `diet/best-foods-list` tables | `tables=False` | `tables=True` (2 real tables) |
| Misaligned / broken tables | n/a | none in 158 tables |
| `<p><div` bad nesting | present | none |

## Remaining recommendations (not automated — editorial)

These are prose "headings" (usually sentence-initial bolded topics) and listable content that can't be safely auto-converted without copy judgment.

### H2 / H3 insertions (prose lead-ins that should become headings)

| Article | Suggested headings |
|---|---|
| `tank-setup/substrate-and-impaction` (unheaded 361w) | "Grain size", "KH (Carbonate Hardness)", "Anaerobic pockets and hydrogen sulfide", plus 3 more signpost transitions |
| `tank-setup/temperature` (unheaded 304w) | "When a chiller is required", "Upstairs rooms and attics", "Desert and dry inland climates", "Wi-Fi thermometer alerts" (4 more) |
| `tank-setup/water-conditioners` (unheaded 373w) | "Gill burns", "Prime at high temperature", "0–2 minutes: observe the gills", "Does water conditioner affect pH?" (5 total) |
| `tank-setup/water-parameters-cycling` (unheaded 366w) | "Stage 1 — Ammonia to Nitrite", "Colony recovery after disruption", "Replacing all filter media" (5 total) |
| `diet/live-vs-frozen-food` (unheaded 254w) | 1 signpost insertion ("Recovering axolotl (post-illness)…") |

### List conversions (dense enumerations that should be `<ul>`/`<ol>`)

| Article | Paragraphs |
|---|---|
| `tank-setup/water-parameters-cycling` | 4 paragraphs with enumerate-y lists ("Stage 1…", "Colony recovery…", "KH — Carbonate Hardness…", pH equilibrium) |
| `tank-setup/water-conditioners` | 5 ("semi-permeable skin", "tap water for an axolotl", "distilled water is not safe", "bottled spring water", "survivable range") |
| `diet/live-vs-frozen-food` | 5 ("earthworms win as staple", "54–65% protein", "moisture content", "larger adult size", "earthworms at the center") |
| `legal/new-jersey` | 1 default-list paragraph |

### Table conversions (runs of short "row-like" paragraphs → table)

| Article | Row-run locations |
|---|---|
| `tank-setup/temperature` | 3 row-runs of 3+ short paras (chiller sizing / equipment) |
| `tank-setup/water-conditioners` | 1 row-run of 3 (water-source comparison) |
| `tank-setup/water-parameters-cycling` | 2 row-runs of 3 (parameter reference) — article currently has **no** table (`tables=False`), highest-value target |

### Minimal-effort threshold

`diet/shrimp-for-axolotls`, `health/fridging-sick-axolotl`, `tank-setup/live-vs-artificial-plants` still show `run` 10–16 but with **no** usable H2/list/table ops — their long runs are tight Q&A clusters already covered by the FAQ section. Left as-is; lowest priority.

## Recommendation priority
1. `tank-setup/water-parameters-cycling` — add table(s), needs `tables=True`.
2. `tank-setup/temperature`, `tank-setup/water-conditioners` — H2 + table row-runs.
3. `diet/live-vs-frozen-food` — H2 + list ops.
4. `tank-setup/substrate-and-impaction`, `legal/new-jersey` — H2/list ops, low count.
5. Skip: `shrimp-for-axolotls`, `fridging-sick-axolotl`, `live-vs-artificial-plants`.

## Status: priorities 1–4 completed above; new-jersey verified clean (no operation needed). Priority 5 left as-is.