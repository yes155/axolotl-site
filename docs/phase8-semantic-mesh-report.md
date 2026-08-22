# Phase 8 — Semantic Mesh / Contextual Internal-Link Pass

Status: COMPLETE — mesh implemented, site rebuilt, validated.

---

## 1. Phase 7C baseline (preserved)

Persisted before any Phase 8 edit in `docs/phase8/metrics-before.json` (rebuilt from current source, matches the Phase 7C audit).

| Metric | BEFORE |
|---|---|
| Content pages | 124 |
| Content internal edges | 414 |
| Cross-cluster edges | 81 (19.6%) |
| Avg outbound links / content page | 3.34 |
| Zero-inbound pages (content graph) | 18 — all 13 hubs + 5 tool pages (nav/footer-reachable; template-filtered) |
| Zero-outbound pages | 1 — `/tools` |
| health ↔ biology | 1 |
| breeding ↔ diet | 0 |
| legal | 0 external inbound edges (semantic) |
| tools | 0 content-graph inbound (5 inline article→tool anchors exist but are footer-template-filtered); `/tools` dead end |

## 2. Semantic problems discovered

1. **biology ↔ health = 1 edge** despite heavy conceptual overlap — gills are simultaneously the site's biology organ *and* its most-discussed health symptom organ; regeneration science is the basis for the site's wound-care advice.
2. **breeding ↔ diet = 0 edges** — the natural lifecycle arc (eggs → larvae → juveniles → feeding → growth) has no links between the two clusters.
3. **legal had 0 inbound semantic links** — the flagship care guide contains a large legality section that is a dead-letter reference (no link to the legal coverage); culture page even says "check your local laws" without linking.
4. **Tools are contextually linked but graph-invisible and one-sided** — all 5 tools already have article→tool inline anchors and tool→article links, but the `/tools` hub was a dead end (0 outbound content links), and the tool inbound metric reads 0 because every footer links to all tools (≥90% template filter).
5. **18 template-filtered "orphans" are not true orphans** — all hubs are child→hub related-rail + nav/footer reachable; the orphan metric is a measurement artifact of the ≥90% template rule (category B/D, intentional structural).

## 3. Proposed edges

22 implemented edges:

- **Health ↔ Biology (9 new):** anatomy→shrinking-gills, shrinking-gills→anatomy, anatomy→stress-signs, anatomy→floating, limb-regeneration→regeneration, regeneration→minor-scrapes, curled-gills→anatomy, malnutrition→regeneration, fungal→anatomy.
- **Breeding ↔ Diet (7 new):** egg-and-larvae→shrimp, egg-and-larvae→feeding-schedule, raising-juveniles→feeding-schedule, raising-juveniles→blackworms, shrimp→egg-and-larvae, blackworms→raising-juveniles, feeding-schedule→raising-juveniles.
- **Legal gateway (3 anchors + 1 rail):** care-guide→legal (inline ×2 + related-rail), adopt-me→legal (inline ×1).
- **Tools (4 new):** `/tools`→setup-guide, `/tools`→water-parameters-cycling, `/tools`→feeding-schedule-by-age, `/tools`→refusing-to-eat.

Full table with anchor text and reasons: `docs/phase8-link-changes.csv`.

## 4. Relationship type for every proposed edge

See `docs/phase8-link-changes.csv` (`relationship` column). Every edge is classified: `biology→practical application`, `symptom→underlying anatomy`, `healing experience→underlying science`, `science→practical wound care`, `procedure→food item`, `life stage→feeding frequency`, `procedure→schedule`, `procedure→staple food`, `food item→life stage that needs it`, `feeding→post-breeding husbandry`, `schedule→lifecycle context`, `ownership decision→legal status→jurisdiction`, `virtual ownership→real-world legality`, `tool→prerequisite knowledge/referenced science/referenced schedule/action pathway`. No edge was added without a one-sentence relationship (see `reason` column).

## 5. Implemented edges (22)

| Source | Target | Priority | Mechanism |
|---|---|---|---|
| biology/anatomy ↔ health/shrinking-gills | anatomy ↔ shrinking-gills | P0 | related-rail |
| biology/anatomy | health/stress-signs | P0 | inline |
| biology/anatomy | health/why-axolotl-floating | P1 | inline |
| health/limb-regeneration ↔ biology/regeneration | P0 | related-rail |
| biology/regeneration | health/minor-scrapes-and-wounds | P0 | related-rail |
| health/curled-gills-stress-signal | biology/anatomy | P1 | related-rail |
| health/malnutrition-signs | biology/regeneration | P1 | related-rail |
| health/fungal-infections-saprolegnia | biology/anatomy | P1 | related-rail |
| breeding/egg-and-larvae-care ↔ diet/shrimp-for-axolotls | P0 | related-rail |
| breeding/egg-and-larvae-care | diet/feeding-schedule-by-age | P0 | related-rail |
| breeding/raising-juveniles ↔ diet/feeding-schedule-by-age | P0 | related-rail |
| breeding/raising-juveniles | diet/blackworms-for-juveniles | P0 | related-rail |
| diet/shrimp-for-axolotls ↔ breeding/egg-and-larvae-care | P1 | related-rail |
| diet/blackworms-for-juveniles ↔ breeding/raising-juveniles | P1 | related-rail |
| diet/feeding-schedule-by-age ↔ breeding/raising-juveniles | P1 | related-rail |
| axolotls/care-guide | legal | P0 | inline (×2) + related-rail |
| culture/adopt-me | legal | P1 | inline |
| /tools | tank-setup/setup-guide, water-parameters-cycling, diet/feeding-schedule-by-age, health/refusing-to-eat | P1 | tools-index |

## 6. Rejected edges and why

| Candidate | Verdict | Reason |
|---|---|---|
| health/salt-bath → biology/anatomy | REJECT | Permeability mention exists but treatment context is too far from anatomy; already covered by fungal→anatomy. |
| biology/lifespan → care/age-and-size-chart | REJECT | No prose bridge (lifespan page never discusses size/age growth stages). |
| cost-and-buying/breeder-vs-pet-store → legal | REJECT | No legality prose in the page; would be a forced unrelated jump. |
| cost-and-buying/shipping-live-axolotls → legal | REJECT | No state/border/legality prose present. |
| cost-and-buying/axolotl-price-by-morph → legal | REJECT | Price page has no law content; same for cost-of-ownership, beginner page, red-flags. |
| care-basics/are-axolotls-good-beginner-pets → legal | REJECT | No legality prose on the beginner page. |
| morphs↔health cross-links | REJECT | No semantic bridge in the corpus; would be artificial. |
| diet/axolotl-pellets → breeding | REJECT | Pellets are explicitly wrong for larvae (corpus says so); would contradict content. |
| biology/wild-habitat ↔ tank-setup | P2 — not implemented | Natural-habitat replication is real but optional; left out to keep the mesh tight. |
| health/finding-an-exotic-vet ↔ care/cost-of-ownership | P2 — not implemented | Vet cost → budget relation is real but optional; left out. |

## 7. BEFORE → AFTER metrics

| Metric | BEFORE | AFTER | Δ |
|---|---|---|---|
| Content internal edges | 414 | 433 | +19 |
| Cross-cluster edges | 81 | 100 | +19 |
| Avg outbound / content page | 3.34 | 3.49 | +0.15 |
| Zero-outbound pages | 1 (`/tools`) | 0 | −1 |
| Zero-inbound pages (content graph) | 18 | 18 (unchanged — template-filtered hubs/tools, documented) | 0 |
| health ↔ biology | 1 | **10** | +9 |
| breeding ↔ diet | 0 | **7** | +7 |
| legal (semantic inbound anchors) | 0 | **3 inline anchors + 1 rail** | +3 semantic routes |
| tools: `/tools` outbound | 9 | 13 | +4 |
| tools: article→tool inline anchors | 5 (all tools, pre-existing) | 5 (unchanged) | 0 |

Transparency note: the −1 axolotls-cluster outbound is the flagship care-guide's related rail trading one generic fallback link for the targeted `/legal/` gateway link — a deliberate semantic upgrade.

## 8. Health ↔ Biology result

**1 → 10 edges.** 9 new edges, both directions:

- `anatomy-gills-and-lungs` ↔ `shrinking-gills` (gills change shape — the anatomy page literally says so)
- `anatomy` → `stress-signs` (inline "health indicator")
- `anatomy` → `floating` (inline "Surface gulping" — floating page covers swallowed air)
- `limb-regeneration` ↔ `regeneration-and-limb-regrowth` (reciprocal; was one-way)
- `regeneration-and-limb-regrowth` → `minor-scrapes-and-wounds` (wound closure science → practical wounds)
- `curled-gills-stress-signal` → `anatomy` (symptom → causal organ)
- `malnutrition-signs` → `regeneration` (citation of regeneration biology)
- `fungal-infections-saprolegnia` → `anatomy` (permeability → drug sensitivity)

Every edge improves semantic coherence: a care reader on a health page can now reach the biology that explains *why*; a biology reader can reach the practical care that applies it.

## 9. Breeding ↔ Diet result

**0 → 7 edges.** The lifecycle arc is now linked:

- `egg-and-larvae-care` → `shrimp-for-axolotls` (larvae first food) + `feeding-schedule-by-age`
- `raising-juveniles` → `feeding-schedule-by-age` + `blackworms-for-juveniles`
- Reciprocal: `shrimp` → `egg-and-larvae-care`, `blackworms` → `raising-juveniles`, `feeding-schedule` → `raising-juveniles`

BREEDING → EGGS/LARVAE → JUVENILES → FEEDING → GROWTH → CARE is now a navigable path instead of a wall.

## 10. Legal gateway result

- Conceptual gateway implemented: **OWNERSHIP → LEGAL STATUS → JURISDICTION**.
- `/axolotls/care-guide` legal section now links `/legal/` inline twice (the two "check your…" sentences) plus one related-rail item.
- `/axolotl-in-culture/adopt-me-axolotl-guide` links `/legal/` inline ("check your local laws first").
- No mass-linking: state articles stay linked from the legal hub only; jurisdiction pages already link back to care-guide (e.g. legal/california → care-guide).
- Graph metric note: `/legal/` appears in the site-wide footer/nav, so the extraction's ≥90% template rule filters it — the 3 semantic anchors + rail do not show up in the 433-edge graph count. They are included explicitly in `docs/phase8-semantic-graph.json` (edges flagged `phase8: true` + `note`) and verified in rendered HTML: care-guide now contains 2 anchors to `/legal/`, adopt-me 1.

## 11. Tool reciprocity result

| Tool | Primary intent | Required knowledge | Supporting article(s) | Article→tool | Tool→article |
|---|---|---|---|---|---|
| Tank size calculator | size tank by axolotl length/age | age-length-minimum volume | tank-size-by-age, setup-guide | inline ✓ (pre-existing) | ✓ |
| Water conditioner dosage calculator | dose conditioner | tank volume, conditioner rules | water-conditioners, water-parameters-cycling | inline ✓ (pre-existing) | ✓ |
| Feeding schedule generator | plan by age/size | life-stage frequencies, portions | feeding-schedule-by-age, best-foods-list | inline ✓ (pre-existing) | ✓ |
| Nitrogen cycle tracker | log cycling | ammonia/nitrite/nitrate readings | water-parameters-cycling | inline ✓ (pre-existing) | ✓ |
| Symptom checker | differential from symptoms | symptom→cause mapping | stress-signs, refusing-to-eat | inline ✓ (pre-existing) | ✓ |

- Fixed the one real tool defect: `/tools` was a dead end → now links to 4 grounding guides (setup-guide, water-parameters-cycling, feeding-schedule-by-age, refusing-to-eat). `/tools` content outbound: 9 → 13.
- Tool inbound reads 0 in the graph solely because the footer links to all 5 tools on every page (≥90% template filter). Verified in HTML: each tool page has 1-2 real article backlinks.

## 12. Hub reachability result

| Hub | Classification | Action |
|---|---|---|
| /health, /tank-setup, /diet, /morphs, /breeding, /care-basics, /cost-and-buying, /legal, /biology-and-science, /gifts-and-merch, /axolotl-in-culture, /axolotls | B + D — navigation-only orphan / hub intentionally structural | No change (each hub is reachable via site nav + footer + every in-cluster article's related-rail "‹Cluster›" link). |
| /tools | C — utility hub, previously also a dead end | Grounded via 4 start-here links; no longer a dead end. |
| 5 tool pages | C — tool intentionally isolated (kept under nav/footer + contextual article anchors) | No change. |

Every content hub is reachable through meaningful architecture; no structural "fix" was applied to intentional pages.

## 13. Remaining weak joints

1. **Graph-invisible reversibility**: legal hub edges and tool inbound edges stay 0 in the machine-readable graph because of the ≥90% template filter (footer/nav). The links exist in HTML; only the metric is hidden. Future phase must exempt footer-resident tool/legal links from the template rule to count them.
2. **morphs↔health = 0**: no corpus bridge (kept REJECT).
3. **culture→tools = 0**: culture pages never mention tools; left untouched.
4. **/tools individual pages** remain template-filtered for inbound — same as (1).
5. `gifts-and-merch` has only single-digit cross links (culture) — acceptable for a peripheral layer.

## 14. Pages requiring editorial changes

None. No article URL, title, H1, FAQ structure, layout, or CSS was changed. The only content-touching edits are links added via the reusable `config.LINKING`/`config.SEMANTIC_INLINE` maps (content-processing layer) and a 4-link "knowledge behind these tools" block on the `/tools` index template.

---

## Quality control

- **Broken URLs:** 0 (full internal-link scan of every rendered page against the 130-page site map).
- **Duplicate links:** 0 in-page duplicate hrefs in any article body or related rail.
- **Repeated anchors:** 0 (each inline phrase unique to its sentence; rail anchors are destination titles).
- **Unnatural anchors:** inline anchors are verbatim prose ("health indicator", "Surface gulping", "check your local laws first", "Check your specific state and city before you buy/buying"); rail anchors are destination titles.
- **Links in inappropriate contexts / unrelated pages:** none — every edge has a one-sentence relationship recorded.
- **Excessive cross-cluster linking:** none — 100/433 content edges cross clusters (23%), concentrated in high-coherence pairs.
- **Circular linking without purpose:** none — reciprocity only where the relationship genuinely runs both ways.
- **Orphaned important pages:** none — 0 zero-outbound; all zero-inbound pages are nav/footer-reachable hubs/tools (documented).

## Content gaps — NOT implemented

None required. No missing bridge needed a new article; all Phase 8 relationships were supported by existing corpus prose.

## Files

- `docs/phase8-semantic-mesh-report.md` (this file)
- `docs/phase8-link-changes.csv` (22 implemented edges + relationship + anchor + reason)
- `docs/phase8-semantic-graph.json` (130 nodes, 435 edges incl. legal/tool routes)
- `docs/phase8/metrics-before.json`, `docs/phase8/metrics-after.json`
- `build/phase8_graph.py`, `build/phase8_text.py`, `build/phase8_srch.py`, `build/phase8_emit.py` (pipeline tools)
- `build/config.py` (LINKING + SEMANTIC_INLINE additions), `build/build.py` (related-rail hub/tool resolution + /tools start-here links)