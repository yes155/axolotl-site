# Phase 9 — Semantic Content Audit

Site: Axolotl Care Guide · Scope date: 2026-08-20
Companion files: `phase9-page-audit.csv`, `phase9-content-gaps.csv`, `phase9-cannibalization.csv`, `phase9-search-spec.md`
Supporting data: `_master.csv` (page inventory), `_tiers.txt` (tier assignments), `_content-digest.txt` (page text pulls)

---

## 1. Executive summary

The site is a **124-page, 13-cluster topical map** around a single broad entity (the axolotl) with strong depth on the conversion-relevant system topics (tank setup, water chemistry, diet, treatments) and a long wing of culture/game/merch content that feeds the care core.

Three structural facts drive everything that follows:

1. **Authority concentrates in a handful of anchor articles.** Only 8 tier-1 articles exist among 21 tier-1 pages; the other 13 tier-1 pages are navigation hubs with **0 internal inbound links by construction**. The hub-and-spoke design means authority flows through *internal links, not inbound links*, which makes cross-cluster linking and the search index boost the two levers that matter.
2. **Completeness is bipolar.** By word-count screen, 20 of 106 content pages are `canonical` and 14 `solid`, but **72 (68%) are `partial` or `thin`**. The deep pages are the system pages (water chemistry, diet science, treatment protocols); the thin zone is morphs, care-basics explainers, legal state pages, and culture articles. Word counts are a screen only — e.g. the rendered text counter differs from the CSV counter for some pages (setup-guide 2869 CSV vs 1199 rendered; temperature 5826 vs 1430) — so the `thin` flag is a review queue, not a verdict.
3. **Three clusters concentrate the cannibalization risk.** `health`, `tank-setup`, and `diet` each have near-duplicate intent pairs; one is high-severity (`stress-signs` fully subsumed), several are medium (fungus treatment trio, impaction four-way, filter pair, temperature/chiller pair, regeneration pair, care-guide title collision).

Recommended posture: **do not add pages to the map until the 3 high-severity cannibalizations and the 1 high-priority gap (water-change guide) are resolved.** The map already has enough surface; the work is consolidation, differentiation, and thickening thin winners.

---

## 2. Methodology & scope

- **Inventory source:** `_master.csv` built from the built site (129 HTML pages; 124 in-cluster pages plus 5 generator/page shims excluded). Fields: url, cluster, tier, title, meta description, headings, FAQ count, word count, inbound link count, outbound link count.
- **Tiering:** graph-based (inbound+mapping distance) with curation — tier 1 = hubs + anchor articles, tier 3 = exploitative long-tail. Distribution **21 / 44 / 59**.
- **Completeness rubric** (screen only): `canonical` ≥2500w, `solid` 1100–2499w, `partial` 550–1099w, `thin` <550w, `index` = hub (no content), `interactive` = tool.
- **Digest pulls:** select tier-1 and priority-tier-2 pages read in full text (`_content-digest.txt`) to ground entity–attribute–intent and E-A-V claim structure.
- **Analysis products:** per-page E-A-V table (`phase9-page-audit.csv`), cannibalization groups (`phase9-cannibalization.csv`), content gaps (`phase9-content-gaps.csv`), search spec (`phase9-search-spec.md`).

## 3. Topical architecture & cluster inventory

13 clusters, 124 pages. Page distribution and tier posture:

| Cluster | Pages | Hub | T1 arts | T2 | T3 | Posture |
|---|---|---|---|---|---|---|
| tank-setup | 18 | ✓ | 2 | 7 | 9 | Deepest + most linked cluster; anchor docs present |
| health | 19 | ✓ | 2 | 7 | 10 | Scope leader (18 children); treatment depth strong, diagnostics thin spots |
| morphs | 14 | ✓ | 2 | 2 | 10 | **Highest hub link-out (13) but thin flagship depth — key gap** |
| diet | 13 | ✓ | 1 | 4 | 8 | Strong science; 3-way fasting/impaction overlaps |
| care-basics | 10 | ✓ | 0 | 2 | 8 | Long-tail explainers; decision pages overlap moderately |
| biology-and-science | 9 | ✓ | 0 | 6 | 3 | Question-led; thin owners-facing (neoteny 495w) |
| legal | 9 | ✓ | 0 | 4 | 5 | Only 5 US states covered; high money intent per page |
| cost-and-buying | 7 | ✓ | 0 | 4 | 3 | Thin zone (4 of 7 pages <550w) |
| breeding | 7 | ✓ | 1 | 3 | 3 | Coherent procedural chain |
| tools | 6 | ✓ | 0 | 0 | 6 | 5 calculators, all 0 inbound (deep nav only) |
| axolotl-in-culture | 5 | ✓ | 0 | 2 | 3 | Growth wing that funnels to care core |
| gifts-and-merch | 5 | ✓ | 0 | 2 | 3 | Low information value; revenue/community |
| axolotls | 2 | ✓ | 0 | 1 | 0 | **Title collision between hub and care-guide (C1)** |

Total: 21 tier-1 (13 hubs + 8 articles), 44 tier-2, 59 tier-3.

## 4. Entity–attribute inventory (E-A-V model)

Nine core entities; every page maps to exactly one (see `phase9-page-audit.csv`):

| Entity | Definition | Key attributes in play |
|---|---|---|
| axolotl | the animal as pet/subject | suitability, buying-check, age-size, behavior, cost, handling, cohabitation, lifespan |
| tank-system | hardware + physical setup | tank-size, setup-process, filtration, substrate, lighting, temperature, hides, plants, tank-mates, acclimation |
| water-chemistry | water + nitrogen dynamics | cycling, readings, conditioners, ammonia sources, odor diagnostics, testing |
| diet | food + feeding practice | food-items, frequency, fasting, pellets, supplements, specific-food verdicts |
| health-condition | disease/problem + treatment | fungus, appetite-loss, stress, floating, impaction, parasites, malnutrition, burns, red-leg, fridging, tea/salt-bath |
| morph | color/genetics variant | appearance, genetics, price, rarity, care-difference, myth/ethics |
| legal-jurisdiction | law per state/country | legality, permit, import, penalties |
| breeding-system | reproduction chain | triggers, egg-care, juvenile-raising, genetics, sexing, inbreeding-ethics |
| biology-concept | science/classification | respiration, neoteny, regeneration, habitat, conservation, metamorphosis |
| culture-artifact | games/merch/memes | minecraft, adopt-me, memes, merchandise, popularity |
| tools | interactive calculators | feed-schedule, cycle-tracker, dose, tank-size, symptom-check |

**Reconciliation finding:** every cluster's hub correctly broadcasts its children, and cross-cluster bridges exist where needed (diet↔health over impaction, water↔health over ammonia). The one entity-level hole is **metamorphosis** (owner-intent) — see §8.

## 5. Intent coverage by cluster

Intent set used: `informational`, `procedural`, `troubleshooting`, `comparative`, `decision`, `reference`.

- Strong: **tank-setup/water-chemistry/diet** carry all six intents with canonical depth; **health** troubleshooting is well-served by the treatment protocol pages.
- Thin-intent gaps:
  - **decision** (buy/own): only 6 decision pages (beginner-pets, kids, monthly-cost, price-by-morph, breeder-vs-pet-store, choosing-breeder) and they under-deliver depth (4 of 6 are ≤549w). The pre-purchase decision funnel is the weakest revenue-adjacent intent on the site.
  - **reference**: morph-comparison-chart (466w) cannot serve the cross-morph reference job; tank-size-by-age (517w) is a stub of the setup-guide's tank section.
  - **comparative**: only 3 true comparison pages (breeder-vs-pet-store, live-vs-frozen-food, canister-vs-sponge-filter, plus fltration overlap C4).

## 6. Page-level audit highlights

Top inbound anchor articles (authority backbone):

| Page | Inbound | Words | Class |
|---|---|---|---|
| /tank-setup/water-parameters-cycling | 16 | 5305 | canonical |
| /diet/feeding-schedule-by-age | 11 | 1781 | solid |
| /health/refusing-to-eat | 11 | 3364 | canonical |
| /health/fungal-infections-saprolegnia | 10 | 1791 | canonical |
| /morphs/leucistic | 10 | 611 | **partial** |
| /tank-setup/setup-guide | 9 | 2869 | canonical |
| /breeding/color-genetics-punnett-squares | 9 | 852 | partial |
| /morphs/wild-type | 9 | 881 | partial |

**Tier-1 scrutiny (the 8 anchor articles):**
- Strong anchors: water-parameters-cycling, feeding-schedule-by-age, refusing-to-eat, fungal-infections-saprolegnia, setup-guide. These carry the E-A-V chains the rest of the site repeats.
- **Weak anchors: leucistic (611w) and wild-type (881w) are the two most-linked morph articles yet are `partial` — the exact pages Google samples for 'leucistic axolotl' queries.** color-genetics-punnett-squares (852w) underpins all morph genetics discussion but stays `partial`. These three are the Phase-10 expansion target with the best ROI (high retention, low depth).
- Ten thin-but-high-retention pages (review for depth or consolidation): neoteny 495w, comparison-chart 466w, price-by-morph 544w, breeder-vs-pet-store 502w, choosing-healthy-axolotl 549w, impaction-symptoms-treatment 537w, finding-vet 519w, tank-size-by-age 517w, pronunciation 524w, adoption/game pages 439–517w.
- The **5 calculators are orphaned at 0 inbound** — they are reachable only through the /tools hub despite being the site's most differentiated assets (see §11).

## 7. Cannibalization analysis

10 groups catalogued in `phase9-cannibalization.csv`. Severity:

- **HIGH (3):**
  - **C1** — `/axolotls` hub vs `/axolotls/care-guide` both bid on "axolotl care guide" in their titles.
  - **C2** — `/health/stress-signs` is fully subsumed by `curled-gills-stress-signal` + `why-axolotl-floating`.
  - **C10** — fasting-duration tables duplicated across feeding-schedule-by-age, fasting-and-vacation, and refusing-to-eat.
- **MEDIUM (6):** C3 temperature/chiller, C4 filter pair, C5 fungus treatment trio, C6 impaction four-way, C7 pre-purchase decision trio, C8 regeneration science/owner pair.
- **LOW (1):** C9 morph comparison chart vs individual morphs.

Consolidation principle applied throughout: **each unique intent keeps exactly one ranking page; overlapping content is either claimed explicitly by a deeper page or removed.** No redirects are proposed that would break the search index until the Phase-10 campaign is approved.

## 8. Content gaps along the E-A-V chains

Catalogued in `phase9-content-gaps.csv` (10 rows). Priority calls:

- **HIGH — water-change procedure.** The single most repeated operational task has no owning page; four pages reference it. Create `/tank-setup/water-change-guide` and back-anchor from water-parameters-cycling, water-conditioners, why-tank-water-smells, uneaten-food-and-ammonia.
- **MEDIUM-HIGH — metamorphosis (owner intent).** Thin neoteny (495w) cannot carry 'why is my axolotl turning into a salamander'. Either a new page or a major neoteny expansion is required.
- **MEDIUM — emergency triage.** No 'call a vet now' decision table exists despite five treatment pages that assume one.
- **MEDIUM — healthy-stool diagnostics** (long-tail that funnels to parasite/impaction treatments) and **test-kit how-to** (feeds the nitrogen-cycle-tracker tool).
- **MEDIUM — legal coverage gap.** Only 5 of 50 US states + Canada; expand strictly on verified demand (see table in gaps CSV for the demand-verification step before authoring).
- **LOW** — chiller-size calculator, first-year budget consolidation, earthworm sourcing, hatchling→pellet transition table.

## 9. Completeness assessment

`canonical 20 (19%) · solid 14 (13%) · partial 57 (54%) · thin 15 (14%)` of 106 content pages; remainder = 13 hubs (`index`) + 5 tools (`interactive`).

Thin zone by cluster: cost-and-buying (4/7 <550w), morphs (comparison-chart, blue-myth, golden-albino), biology (neoteny), health (impaction-treatment, finding-vet), care-basics (pronunciation), culture (minecraft, adopt-me, pop-culture), tank (tank-size-by-age).

The deep zone is intentionally concentrated where users act (setup, water, feeding, treatment), which is the correct prioritization. The explicit recommendation is **not to equalize word counts**; it is to (a) thicken the 3 weak tier-1 anchors and the 3 most-linked combatants, and (b) let the rest stay lean as long as they are differentiated and link upward.

## 10. Internal link / authority analysis

- Hubs have 0 inbound by design → the hub-spoke model means **the search-index cluster boost + hub link-outs are the site's only authority vectors**. This is already partly engineered in Phase-9-A search (see §11).
- Strongest in-cluster linking: health (18 outbound from hub), tank-setup (17), morphs (13), diet (12). Weakest: axolotls (hub → 1 child), gifts-and-merch (4), tools (4 link-outs; 5 calculators with 0 inbound).
- **Orphan-adjacent pages** (≤2 inbound, non-hub): lifespan, sexing, adopt-me, pop-culture, leaf-off articles like shrimp/vitamins/shipping — these rely entirely on the hub link. Acceptable for tier-3 long-tail, but two deserve a mention link from a tier-1 anchor: `shipping-live-axolotls` (from choosing-a-reputable-breeder flow) and `finding-an-exotic-vet` (from every treatment page's 'when to call a vet' — currently under-linked).

## 11. Search integration findings

Already shipped in Phase 9-A (from `search.js` + rebuilt index):

- Cluster-aware scoring: query → cluster weighting, parent-hub terms boost children (mitigates the hub-0-inbound authority asymmetry).
- Alias/synonym layer (e.g. 'food', 'feeding', 'diet' group; 'tank', 'setup', 'size' group) covering table-implicit synonyms.
- Roles from the index feed UI labels (`guide`/`calculator`/`hub`), and calculators return action links.
- Keyboard navigation + ARIA on the dropdown; results now include the destination path.

Remaining search work is specified in `phase9-search-spec.md` (`Phase-9-B`): deep-link routing for troubleshooting queries, `when to call a vet` result enrichment, empty-result fallback to a cluster's `document` page, and calculator query capture.

## 12. Prioritized remediation roadmap

**P0 (before any new content — Phase 9-B confirmations):**
1. C1: differentiate `/axolotls` hub title/H1 vs `/axolotls/care-guide`; route hub links to care-guide for the flagship query.
2. C2: consolidate `stress-signs` into `curled-gills-stress-signal` + `why-axolotl-floating`; redirect.
3. C10: single fasting-duration truth table in `fasting-and-vacation`; link other two pages by intent.
4. Thicken the 3 weak tier-1 anchors: `leucistic`, `wild-type`, `color-genetics-punnett-squares`.

**P1 (high ROI, low risk):**
5. C3–C8 medium cannibalizations: explicit role statements + cross-links (no rewrites required for several).
6. HIGH gap: `water-change-guide` + back-anchors.
7. MEDIUM-HIGH gap: metamorphosis owner page (or neoteny expansion).
8. Emergency-triage decision table page + under-linking fix for `finding-an-exotic-vet`, `shipping-live-axolotls`.

**P2 (opportunistic):**
9. Legal expansion on verified demand only; test-kit how-to; healthy-stool diagnostics; chiller calculator; first-year budget table.
10. Long-tail tier-3 depth only where a page is both thin *and* the intended sole claimant of its intent (e.g. morph-comparison-chart, tank-size-by-age).

## 13. Recommendation list

1. Fix C1, C2, C10 before adding anything.
2. Thicken the 3 tier-1 anchors (leucistic, wild-type, Punnett squares) to ≥1,200 words each with E-A-V claim chains (appearance → genetics → price → care-difference → action).
3. Build the water-change guide first among all gaps.
4. Role-split the six medium cannibalizations with explicit one-line intent statements + cross-links.
5. Do not pursue word-count equalization; keep tier-3 lean and differentiated.
6. Wire `finding-an-exotic-vet` into every tier-1 treatment page.
7. Implement the Phase-9-B search deep-link + fallback items from `phase9-search-spec.md`.
8. Re-run the audit (regenerate `_master.csv`, tiers, and the three CSVs) after Phase-10 changes to re-verify tier distribution and cannibalization.