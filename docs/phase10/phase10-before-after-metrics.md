# Phase 10 — BEFORE → AFTER Metrics

Baseline numbers are the Phase 8/9 audit outputs (`docs/phase8-semantic-mesh-report.md`,
`docs/phase9/phase9-page-audit.csv`). PPR numbers are an internal operational approximation
(methodology §10) — **not** an official Google metric.

## Graph metrics

`python build/phase10_qa.py` after build (see `qa-report.json`).

| Metric | BEFORE | AFTER (measured) | Target Δ | Status |
|---|---|---|---|---|
| Content pages | 124 | **126** (+2) | +2 (water-change, emergency) | ✅ |
| Internal content edges | 414 | **482** | +~26 (link-changes table) | ✅ +68 |
| Cross-cluster edges | 81 (19.6%) | **118 (24.5%)** | +5, all typed real relations | ✅ +37 |
| Avg out-links/content page | 3.34 | **3.83** | ~3.5, no link spam | ✅ |
| Zero-inbound content pages | 18 (13 hubs + 5 tools) | 18 (same set) | 16 (-2) | ⚠️ see note |
| Zero-outbound pages | 1 (`/tools`) | **0** | 1 | ✅ tools gateway links out |

*Hub/tool "zero inbound" note:* hubs and all five tools are reachable from
every page via the site-wide nav/footer (127 of 132 pages), which the Phase-7B
methodology excludes via its ≥90% template rule — so the 18-count set is a
<strong>measurement artifact, not true islands</strong>, and is unchanged from
baseline. Article-bodied links into hubs/tools remain a Phase-12 suggestion.

## Coverage & completeness (E-A-V / intent)

| Metric | BEFORE | AFTER (plan) |
|---|---|---|
| 3 weak tier-1 anchors (leucistic 611w, wild-type 881w, punnett 852w) | `partial` | ~1,100–1,400w each with E-A-V chains (rarity, price, variants, worked examples, limitations) |
| Canonical impaction (537w) | `thin` | ~900w + cause-routing |
| Morphs comparison chart (466w) | `thin` | ~900w full comparison table |
| Neoteny (495w) | `partial` | ~750w + owner metamorphosis section |
| Water-params + cost page | `solid` | + testing procedure / first-year table |
| New procedural + decision pages | - | 2 new complete pages |

## Cannibalization / ownership

| Metric | BEFORE | AFTER (plan) |
|---|---|---|
| HIGH cannibalizations | 3 (C1, C2, C10) | 0 — each family has a clear canonical owner + role labels |
| MEDIUM cannibalizations | 6 (C3–C8) | 0 — role-differentiated pairs, no silent duplicates |
| LOW cannibalizations | 1 (C9) | 0 — chart = consolidator |
| Pages with duplicated dramatic passage (fast-duration) | 3 | 1 canonical table |

## Redirect / URL hygiene

| Metric | BEFORE | AFTER (plan) |
|---|---|---|
| Redirects introduced | 0 | **0 (zero)** |
| Redirect chains / broken links | 0 | 0 (verified) |
| Duplicate canonicals | 0 | 0 |

## Search

| Metric | BEFORE | AFTER (measured) | Status |
|---|---|---|---|
| Result families deduped | none | 20/20 smoke assertions pass (families, trouble routes, calculators, vet/emergency, typo salvage) | ✅ |
| Action buttons | tools (Phase 6) | 7 indexed actions: 5 tool chips + finding-an-exotic-vet + emergency-first-aid | ✅ |
| Role labels in search | none | 18 pages carry `role-note` (family/role disambiguation) | ✅ |
| Empty-result fallback / typo salvage | partial | implemented (`fixTypos`, `clusterFallback`) | ✅ |

## Content volume

| Metric | BEFORE | AFTER (plan) |
|---|---|---|
| Total words (corpus) | ~380k | ~384k |

BEFORE->AFTER numbers are re-computed after build in `docs/phase10-semantic-seo-report.md`.