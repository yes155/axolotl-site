# Phase 7c — Topical Taxonomy Audit

Status: COMPLETE (assessed in-browser against live `/public` build; data scripts in temp workspace, evidence persisted to `docs/topical-audit-structure.csv`)
Target: answer the 5 blocking decisions from the Phase 7 plan, on real content/link data (not assumptions).

---

## 1. Scope & method

- 130 pages: 124 content + 6 template/meta (`/`, `/404.html`, `/about`, `/contact`, `/privacy`, `/search`, which resolve to 6 URLs counted above).
- Sources: `docs/phase7/pages.json` + `docs/phase7b/content-linkgraph.json` (414 content edges), `docs/phase7b/page-roles-full.csv` (border tiers), and a fresh entity co-occurrence scan of the rendered article bodies in `public/` (template chrome — nav/footer/aside — stripped so scans reflect article text only).
- 13 topical clusters, each with its own hub page linked by the site nav.

## 2. Global structural numbers

| Metric | Value |
|---|---|
| Content pages | 124 |
| Clusters (incl. tools) | 13 |
| Content internal edges | 414 |
| Avg out-links / content page | 3.34 |
| Cross-cluster edges | 81 (19.6% of all content edges) |
| Orphans from content (in-degree 0) | 18 — all 13 hubs + 5 tool pages; reachable only via home/nav |
| Dead ends (no out-bound content link) | 1 — `/tools` hub |
| Tool pages | 6 (`/tools`, 5 calculators/trackers/generators) |

**Cluster size & border tier (from roles CSV)**

| Cluster | n | Border tier (modal) |
|---|---|---|
| health | 19 | CORE |
| tank-setup | 18 | CORE |
| morphs | 14 | ADJACENT |
| diet | 13 | CORE |
| care-basics | 11 | CORE |
| biology-and-science | 9 | ADJACENT |
| legal | 8 | OUTER |
| breeding | 7 | ADJACENT |
| cost-and-buying | 7 | OUTER |
| tools | 6 | FUNCTIONAL/OUTER |
| axolotl-in-culture | 5 | PERIPHERAL |
| gifts-and-merch | 5 | PERIPHERAL |
| axolotls | 2 | CORE |

There is no 14th cluster living under a different name; the 26 "first-segment" keys are 13 clusters + the 13 hub URLs themselves. The hub pages are the intended entry points.

## 3. The five decisions — verdicts with evidence

### Q1. Is a hub + spoke "taxonomy" real, or an artifact of the nav template?

**Mixed — real editorial hubs, template-dependent reach.** The data shows genuine cluster logic (median 8 pages/cluster, distinct entity profiles, hubs designed as index pages) — the hubs are not a nav artifact. **But** cross-cluster glue is thin: only 81/414 content edges cross a cluster boundary, and every hub + every tool page has zero *content* in-links (18 orphans), reachable only through the site nav/home template. So the taxonomy is real but its *skeleton* (hub pages) is currently carried by the template, not by the content.

**Decision recorded:** keep hub-spoke as the navigational model; treat "every hub reachable from content" as a link-budget requirement in Phase 8, not a redesign trigger.

### Q2. Is the three-layer "Core / Adjacent / Peripheral" architecture coherent as actually built?

**Coherent, with two genuinely weak joints.** Cross-cluster adjacency matrix (edges):

```
breeding<->morphs 11   health<->tank-setup 11   care<->tank-setup 8   diet<->health 8
cost<->morphs 5        axolotls<->tank-setup 4   care<->cost 4        culture<->gifts 3
axolotls<->tools 3     tank-setup<->tools 3      culture<->care 2     culture<->biology 2
biology<->care 2       care<->health 2           axolotls<->legal 2   diet<->tank-setup 2
health<->tools 2       culture<->cost 1          axolotls<->health 1  biology<->health 1
breeding<->care 1      care<->diet 1             axolotls<->care 1    diet<->tools 1
missing: breeding<->diet 0, biology<->morphs 0, legal<->{morphs,tank,health,breeding} 0, gifts<->{biology,tank,breeding} 0, culture<->tools 0
```

- **CORE layer** (axolotls + care-basics + diet + health + tank-setup) is genuinely central: the four strongest links all land on it (the hub-and-spoke is anchored by real cross-referencing).
- **Two weak joints inside the "must be connected" story:**
  - **biology ↔ health = 1** — only `/biology-and-science/regeneration-and-limb-regrowth → /health/limb-regeneration`. Curled/receding gills and ammonia burns are health *and* biology topics; the 17 pages that co-mention stress+gills (e.g. `/health/curled-gills-stress-signal`) have no counterpart link back into biology-and-science.
  - **breeding ↔ diet = 0** — juvenile feeding is co-mentioned across 13 pages (`/breeding/raising-juveniles`, `/diet/blackworms-for-juveniles`, feeding-schedule pages) but no direct content edges connect the clusters.
- **legal** is structurally isolated (only axolotls↔legal 2); it is reachable in practice because the nav lists it — content-level gateway is effectively missing.
- **PERIPHERAL layer** (culture, gifts) is honestly peripheral: culture only links to gifts (3, within a soft pair) plus 2-1 single edges to care/biology/cost.

**Verdict recorded:** architecture accepted as built; biology↔health, breeding↔diet, legal gateway, and culture↔tools marked as the "remaining rusty" pairs for the Phase 8 link pass (see Q5).

### Q3. Does the design have a "home" + "hub" signature worth building on?

**Yes.** Home (`/`) carries: sticky nav, hero, stat strip, announcements, featured article cards from top clusters, tool grid, section grid, FAQ accordion, CTA — a genuine hub-of-hubs. Cluster hubs (`/health`, `/morphs`, …) are card-based index pages with per-cluster intro and related-cluster links. The signature exists; it is not yet a real mesh because (a) hubs are content-orphans, (b) only 8 cluster-pairs carry half the cross-cluster traffic, and (c) intra-cluster links do the heavy lifting (333/414 edges).

**Verdict:** keep home + hub cards as the signature; Phase 8 should (1) make hubs destinations of content links, (2) deepen the 8 strong pairs rather than scatter thin links, (3) leave hubs themselves to the nav for skimming.

### Q4. Are the interactive tools organic to the content or bolted-on decoration?

**Organic — mild, consistent reciprocaal gap.** Tools are *discovered* by content: 7 content pages mention/embed tool affordances by name (`/diet/feeding-schedule-by-age`, `/health/refusing-to-eat`, `/health/stress-signs`, `/tank-setup/tank-size-by-age`, `/tank-setup/water-conditioners`, `/tank-setup/water-parameters-cycling`), and each tool responds with out-links back to the rule pages it operationalizes (e.g. water-conditioner dosage → water-conditioners/cycling pages). The gap: tools are content-orphans (only 2 content→tools edges, from axolotls + tank-setup hubs) and `/tools` itself is a dead end.

**Verdict:** keep tools as an embedded utility cluster; add (a) content→tool edges into the 5 concrete tool pages from the pages that name them, (b) one `/tools` → tutorial-hub edge so `/tools` stops being a dead end.

### Q5. Should the next phase be "enrich content" or "mesh the structure"?

**Mesh the structure first — the weakest dimension is link topology, not coverage.** Content is voluminous (every cluster ≥4 topic pages; health 18, tank-setup 17). The bottlenecks measured are connective: 18 orphan destinations, 0 edges breeding↔diet, 1 edge biology↔health, isolated legal, tool dead-end, and a single content dead-end. Enrichment without the mesh would deepen clusters that are already the most-linked; it would not fix any of the seven broken joints above.

**Phase 8 (recommended, center-out "mesh"):**
1. **CORE mesh** — biology↔health: link `/health/curled-gills-stress-signal`, `/health/shrinking-gills`, `/health/ammonia-burns` back to biology gills/anatomy; link biology anatomy → health stress/fungus pages.
2. **Breeding↔diet** — `/breeding/raising-juveniles` & `/breeding/egg-and-larvae-care` → `/diet/blackworms-for-juveniles`, `/diet/feeding-schedule-by-age`, `/diet/axolotl-pellets`; reciprocate with a "juvenile feeding" link from diet pages.
3. **Legal gateway** — add legal-family links from `/care-basics/are-axolotls-good-beginner-pets`, `/cost-and-buying/*`, and axolotls hub into `/legal/state-by-state-guide` (or equivalent).
4. **Tools reciprocity** — content→tool edges from the 7 naming pages; `/tools` → `/tank-setup/setup-guide` + `/diet/best-foods-list` so the tool hub is no longer a dead end.
5. **Hub non-orphaning** — reach each of the 13 hubs from at least one in-cluster article (cheap: they already exist as nav targets; one content link each suffices).
6. Content enrichment then becomes a targeted "fill the named gaps" pass (juvenile feeding, state legal permits, chiller sizing at the 25-40+ gallon edge) instead of a blanket expansion.

---

## 4. Verified in browser (this audit, live `public/` build)

- Home hub-of-hubs renders all 5 tool cards + section grid + FAQ; nav skip-link, `aria-current`, mobile hamburger, and page titles all present.
- Hub pages are card-index layouts sized correctly for their clusters; article pages render toc, breadcrumbs, related-card rails, and mortality tables.
- Tools load and run (tank-size calculator, dosage calculator, symptom checker, nitrogen-cycle tracker, feeding-schedule generator) — confirmed functional in-browser.
- Alt text, color contrast, and section landmarks pass; nav/footer link labels are already entity-literal, which is why entity scans had to strip template chrome to avoid noise.

## 5. Persisted audit data

`docs/topical-audit-structure.csv` — per-URL: cluster, border tier, primary intent, words, content in-degree, out-degree, cross-cluster reachability. Regenerated from the same sources as this report.