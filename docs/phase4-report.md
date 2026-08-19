# Phase 4 Report — Coherent Publication Normalization

**Date:** 2026-08-17
**Scope:** all 106 articles in the axolotl-site corpus
**Result:** rebuild clean — `106 articles, 106 images, 153,512 words, 129 pages`

## What was done

- **Universal article structure** enforced across every article: breadcrumb → H1 → dek → byline → hero → body → FAQ (one component) → related guides → footer.
- **Heading normalization:** heading levels rewritten to a valid, non-skipping sequence (first → h2, deeper → capped at h3, open+close tags both rewritten).
- **FAQ normalization:** every detectable Q→A pattern split into accordion items (`<details class="faq-item"><summary>…</summary><div class="faq-answer">…</div></details>`) under a single "Frequently Asked Questions" section; empty sections collapse back to a plain heading.
- **Paragraph normalization:** split paragraphs over 120 words at sentence boundaries.
- **Bold-only paragraphs** (a `<strong>` alone inside a `<p>`) unwrapped so text isn't styled as a heading substitute.
- **Horizontal-rule artifacts** (`---`, `***`, dash rows) converted to `<hr>`.
- **Internal links:** bare slug links expanded to full `/slug/` URLs, stale bracket markers (`[text]`) cleaned, orphan-killing `LINKING` edges added in `config.py`.
- **References box** on care-guide (authored as raw HTML text) reconstructed into a real `<div class="references-box">`.
- **TOC** wrapped in a collapsible `<details>` ("In this guide") with native marker; FAQ and references headings now appear in the TOC.
- **FAQPage schema** emitted as a `@graph` node when an article has FAQ items.
- **Related guides** never empty: hub link + cross-links + same-hub siblings + flagship fallback.
- **CSS** added for TOC details/summary, FAQ section/items, and `.article-body hr` — no palette or font changes.

## BEFORE → AFTER

| Metric | Before | After |
|---|---|---|
| Long paragraphs (>120 words) | 16 in 7 articles | **0** (max 107 words) |
| Bold-only paragraphs | 138 in 40 articles | **0** pure (32 lead-sentence bolds, legit) |
| Horizontal-rule artifacts | 44 in 16 articles | **0** |
| Heading level skips | 1 | **0** |
| Invalid / unbalanced heading tags | yes | **0** |
| Literal `[text]` bracket links | many | **0** |
| Orphans (no internal links, link graph) | 13 | **0** |
| Zero-inbound articles (link graph) | 92 | **0** |
| FAQ sections / items | run-on Q&A | 65 sections / 398 items |
| TOC rendered on all articles | — | **all present** |
| TOC↔anchor (`#sN` ↔ `id="sN"`) misalignments | — | **0** |
| Related sections with <3 links | — | **0** |
| Pure bold-only / heading / bracket problems (verify gate) | — | **0 — problems: none** |

Note: the audit's source-text orphan metric counts links present in the raw docx; the authoritative final-site metric is `link_graph.py` (0 orphans, 0 zero-inbound, 831 internal edges; 2 zero-outbound are the standalone tool pages `tools/nitrogen-cycle-tracker` and `tools/water-conditioner-dosage-calculator` — expected).

## Key files

- `build/docx2html.py` — docx → HTML normalization pipeline (linkify, heading levels, FAQ accordion, bold unwrap, paragraph split, `<hr>`, references reconstruction)
- `build/build.py` — page/data assembly (TOC details wrapper, sequential `id="sN"` anchors, FAQPage schema, related-guides fallback)
- `build/config.py` — `LINKING` edges for orphan killing
- `public/css/style.css` — `.toc-details`, `.toc-summary`, `.faq`, `.faq-item`, `.faq-answer`, `.article-body hr`

## Verification

- `python build.py` → clean rebuild, 129 pages.
- `phase4_verify.py` over all 106 rendered articles → **problems: none**.
- `phase4_audit.py` → structural metrics above.
- `link_graph.py` → 0 orphans, 0 zero-inbound, 831 internal edges.
- Preview: `http://127.0.0.1:8011/`
