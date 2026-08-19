# Phase 7B — Semantic Content & Internal-Linking Audit

**Scope**: the whole axolotl-site corpus (130 pages: 106 articles, 12 hubs, 6 tools, 6 boilerplate).
**Inputs**: `docs/phase7b/content-linkgraph.json` (413 content edges + template nav list), `content-inout.tsv`, `page-roles.csv`, `page-roles-full.csv` (incl. `key_relationships` per page), `cluster-matrix.txt`, plus Phase 7 (`semantic-page-audit.csv`, `topical-map.md`, `semantic-priority.md`).
**Status**: analysis only — no pages were changed. Actions are registered for later phases (see §14).

**Conventions used in this report**
- `in=` = contextual (in-body) inbound links from the Phase 7B content linkgraph. Template/nav links are excluded; hubs and tools therefore show `in=0` from content even though every page renders them in the nav layer (that layer is `content_in=124/125` in `page-roles.csv`).
- Roles and border ring (CORE / ADJACENT / OUTER / PERIPHERAL / FUNCTIONAL) come from `page-roles.csv`.
- Cluster cross-link counts come from `cluster-matrix.txt` (row = source cluster, column = target cluster).

---

## 0. Method notes

Phase 7 scored individual pages (thickness, FAQs, metadata, inbound). Phase 7B operates on **relationships**: which nodes exist, what each claims (role + intent + attribute), and how the content linkgraph does or does not realize the topical map. Findings below are derived from the artifact CSVs/JSON, not from page re-reading, so every claim is reproducible from `docs/phase7b/`.

One measurement caveat carried forward: `page-roles-full.csv` `key_relationships` and `content-inout.tsv` `out=` come from the same 413-edge graph, but Phase 7's `semantic-priority.md` reported higher `out=` counts (25–29) — that report counted template+near-miss links, not only content edges. Where counts differ, the Phase 7B content-graph number is used.

---

## 1. Corpus at a glance

| Measure | Value | Source |
|---|---|---|
| Pages total | 130 | `pages.json` |
| Articles + tools (content-bearing) | 111 | Phase 7 digest |
| Content edges in linkgraph | 413 | `content-linkgraph.json` |
| Template nav targets | 23 | `content-linkgraph.json` (template[]) |
| Content-inbound median (articles) | in=3 | `content-inout.tsv` |
| Lowest content inbound (articles) | in=2 | 38 pages — **no orphans** |
| Weakest content authorities | in=2 (38 pages) | see §6 |
| Strongest content authority | `/tank-setup/water-parameters-cycling` in=15 | |
| FAQs total | 404 | Phase 7 digest |
| Thin pages (<700 w) | 42 | Phase 7 |
| Pages without FAQ block | 41 | Phase 7 |

The corpus is healthy at the *surface* level (dense FAQ coverage, zero orphan-ish pages, `in<2` count = 0 per Phase 7). The structural weaknesses live at the cluster and hub boundaries (§3, §7, §8).

---

## 2. Topical map & source-context model

`topical-map.md` (Phase 7) defines the site's knowledge domain as **axolotl ownership**: "what the animal is" (biology) through "how to keep, feed, and fix it" (care) to "acquire, breed, buy, and enjoy" (commerce + culture).

Phase 7B extends this with a **border model** — how far each cluster sits from the purchase/intent core:

- **CORE** — decision-driving, high-dwell clusters: `care-basics`, `tank-setup`, `diet`, `health`, plus the `axolotls` hub root (`care-guide` is the site's foundational node).
- **ADJACENT** — support knowledge that strengthens E-E-A-T and informs care decisions: `morphs`, `breeding`, `biology-and-science`.
- **OUTER** — legitimate but secondary demand: `cost-and-buying`, `legal`.
- **PERIPHERAL** — marketing/culture/merch demand-capture: `axolotl-in-culture`, `gifts-and-merch`; borderline articles inside biology (`axolotl-vs-tiger-salamander`) and care (`how-to-pronounce-axolotl`).
- **FUNCTIONAL** — non-topical: home, search, tools, legal boilerplate, 404.

Entity model (from `page-roles-full.csv` `primary_entity`/`primary_attribute`): the single central entity **Axolotl (species/subject)**; secondary entities `Axolotl biology`, `Axolotl (as cultural icon)`; attributes are the observable dimensions pages compete on — water, feeding, health/appetite, gill state, morph/color, breeding, cost/legality, merch. Every page claims exactly one `primary_attribute`; overlaps between attribute claims feed the cannibalization audit (§9).

---

## 3. Cluster topology (from `cluster-matrix.txt`)

Content edges by source→target cluster (row = source, target columns in map order: axolotls, care-basics, tank-setup, diet, health, morphs, breeding, biology, cost, legal, culture, gifts, tools):

| from \ to | ax | cb | ts | d | h | mo | br | bio | cost | leg | cult | gift | tools |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| axolotls | 1 | | 4 | | 1 | | | | | | | | |
| care-basics | 1 | **25** | 6 | 1 | 2 | | 1 | 2 | 3 | | | | |
| tank-setup | | 2 | **53** | 2 | 3 | | | | | | | | |
| diet | | | | **37** | 1 | | | | | | | | |
| health | | | 8 | 4 | **59** | | | | | | | | |
| morphs | | | | | | **47** | 9 | | 3 | | | | |
| breeding | | | | | | 2 | **17** | | | | | | |
| biology | | | | | 1 | | | **26** | | | 1 | | |
| cost-and-buying | | 1 | | | | 2 | | | **16** | | | | |
| legal | 2 | | | | | | | | | **30** | | | |
| axolotl-in-culture | | 2 | | | | | | 1 | 1 | | **11** | 2 | |
| gifts-and-merch | | | | | | | | | | | 1 | **12** | |
| tools | 3 | | | | | | | | | | | | |

**Within-cluster self-link rate** = diagonal / row total (share of a cluster's content links that stay inside it):

| cluster | within % | read |
|---|---|---|
| axolotls | 1/6 = 17% | tiny cluster (hub + care-guide) — fine |
| diet | 37/38 = **97%** | **silo risk**: diet barely feeds health or breeding |
| biology-and-science | 26/28 = 93% | self-contained science ring |
| legal | 30/32 = 94% | self-contained |
| gifts-and-merch | 12/13 = 92% | self-contained (ok, cultural) |
| breeding | 17/19 = 89% | light cross-link to morphs only |
| tank-setup | 53/60 = 88% | healthy |
| cost-and-buying | 16/19 = 84% | morphs + care cross-links |
| health | 59/71 = 83% | healthy |
| morphs | 47/59 = 80% | strong to breeding (9) + cost (3) |
| care-basics | 25/41 = 61% | best cross-cluster spread |
| axolotl-in-culture | 11/17 = 65% | cross-links into real care — good |
| tools | 0/3 = **0%** | no self-links; see §13 |

**Read of the map as a graph**
- The site's strongest **cross-cluster conduits** are `health → tank-setup` (8), `care-basics → tank-setup` (6), `health → diet` (4), `axolotls → tank-setup` (4), `care-basics → cost-and-buying` (3). Water/tank-setup is correctly positioned as the shared cause-layer under both healthy care and illness diagnosis — good architecture.
- `morphs → breeding` (9) and `breeding/color-genetics-punnett-squares` (in=9) make genetics a true two-way bridge — good.
- **Zero content edges target the tools cluster (tools column = 0)** and **zero content edges enter legal from any other cluster** (legal column = 0 external). Both clusters exist only because the nav template renders them everywhere (§7, §10, §13).
- `diet → health` is only 1 while `health → diet` is 4. Feeding-risk pages don't link their health consequences.
- `biology → breeding` = 0 and `breeding → biology` = 0, though `neoteny`, `lifespan-wild-vs-captivity` and `regeneration-and-limb-regrowth` are direct prerequisites for breeding/raising `juveniles`.

---

## 4. Core / outer coverage audit

Goal: confirm no cluster is overscoped (content diluting CORE) or missing (demand with no node).

| Cluster | Ring | Ring finding | Node finding |
|---|---|---|---|
| care-basics | CORE | justified | `how-to-pronounce-axolotl` (524w) is PERIPHERAL in-ring — acceptable low-cost demand capture |
| tank-setup | CORE | justified | strongest cluster (17 nodes, 88% internal) |
| diet | CORE | justified | 12 nodes, but silo risk (97% internal) |
| health | CORE | justified | 18 nodes, richest diagnostic set |
| morphs | ADJACENT | justified | comparison-chart at 466w is the thinnest hub-spoke; `pigment-cells` under-linked from morph pages |
| breeding | ADJACENT | justified | 6 nodes only; no `breeding → juveniles growth` pathway into care/diet |
| biology-and-science | ADJACENT | justified | clean ring; `axolotl-vs-tiger-salamander` is PERIPHERAL in-ring (entity disambiguation — valuable, keep) |
| cost-and-buying | OUTER | justified | price-by-morph ↔ morph pages reciprocally linked — good |
| legal | OUTER | justified | 7 jurisdiction pages, but content-inbound zero outside cluster (§7) |
| axolotl-in-culture | PERIPHERAL | justified | connects back into real care (facts, conservation) — recommended |
| gifts-and-merch | PERIPHERAL | justified | revenue-adjacent; mostly one-way into culture |
| tools | FUNCTIONAL | see §13 | strong UX value, zero semantic integration |

**Nothing sits outside the topic sphere** (`OUTSIDE` ring = 0). No page should be removed for scope reasons; several should be *connected* rather than cut. The single biggest coverage gap is not a missing page but a missing **relationship**: the tools cluster has no inbound content references (`tools` column = 0 in the matrix).
---

## 5. Semantic roles & intent model

Each page carries one role (`page-roles.csv`) for a distinct query intent. Only two roles can hold the same intent without friction: `explanatory` (reference) and `procedural` (how-to) split cleanly; `diagnostic` is the problem-solving workhorse the site's health conversation depends on.

Role distribution (content pages):

| role | count | intent | examples |
|---|---|---|---|
| explanatory | 45 | informational / definitional | neoteny, morph pages, best-foods-list |
| procedural | 16 | procedural | setup-guide, salt-bath, sexing-axolotls |
| diagnostic | 13 | problem-solving | refusing-to-eat, ammonia-burns, why-axolotl-floating |
| comparative | 8 | comparative | canister-vs-sponge, axolotl-vs-tiger-salamander |
| transactional | 9 | transactional | cost-of-ownership, axolotl-price-by-morph, squishmallow |
| location-specific | 7 | location-specific | legal jurisdiction pages |
| tool | 6 | tool/calculator | the 5 tools + search |
| hub / foundational / supporting | 26 | navigational | cluster hubs, care-guide, home |

**Quality of the intent mapping**: the site does **not** do single-intent duplication of comparable weight — there is exactly one comparative node per comparison axis (filtration, decor, food-type, species) and one procedural node per task. Where two pages look similar by title (e.g. "axolotl-pellets" vs "best-foods-list" vs "shrimp-for-axolotls"), role + attribute differ (§9). This is the correct shape for a topical-authority site: role variety per entity, not duplicate pages per query.

`diagnostic` pages also carry the widest outbound attribute spread (each points at a cause + a treatment), which is why `health` is the best-connected cluster (§3).

---

## 6. Authority structure (content inbound)

Content inbound is the graph's measure of which nodes the corpus itself treats as authoritative. Top 15 content authorities:

| page | in | role | cluster |
|---|---|---|---|
| /tank-setup/water-parameters-cycling | **15** | explanatory | tank-setup |
| /health/refusing-to-eat | 11 | diagnostic | health |
| /health/fungal-infections-saprolegnia | 10 | diagnostic | health |
| /morphs/leucistic | 10 | explanatory | morphs |
| /breeding/color-genetics-punnett-squares | 9 | explanatory | breeding |
| /morphs/wild-type | 9 | explanatory | morphs |
| /tank-setup/setup-guide | 9 | procedural | tank-setup |
| /axolotls/care-guide | 8 | foundational | axolotls |
| /diet/best-foods-list | 8 | explanatory | diet |
| /diet/feeding-schedule-by-age | 8 | procedural | diet |
| /legal/california | 7 | location-specific | legal |
| /cost-and-buying/axolotl-price-by-morph | 6 | transactional | cost-and-buying |
| /morphs/chimera | 6 | explanatory | morphs |
| /biology-and-science/neoteny | 6 | explanatory | biology-and-science |
| /diet/overfeeding-and-impaction | 6 | diagnostic | diet |

Observations
- **Water is the semantic backbone** (water-parameters-cycling in=15, setup-guide in=9). Every "why is my axolotl sick/x" question eventually routes here for causes. This is exactly right for a topical-authority hub.
- **Genetics authority is pre-built** (leucistic 10, wild-type 9, punnett 9) even though the cluster is ADJACENT — breeding/morph pages already lean on each other.
- **`diet` has only two strong nodes** (best-foods-list 8, feeding-schedule-by-age 8); 8 of 12 diet pages sit at in=2–3. Diet is the site's least-reinforced CORE cluster (matches the 97% silo score in §3).
- **Legal's single strong node** (california in=7) is fed only by other legal pages. Its authority is synthetic — nav-based, not content-based.

Cold-but-important nodes (in=2) that deserve a second donor: `diet/axolotl-pellets` (commercial, in=2), `diet/beef-heart` (in=2), `diet/shrimp-for-axolotls` (in=2), `diet/how-to-hand-feed` (in=2), `diet/fasting-and-vacation` (in=2), `health/finding-an-exotic-vet` (in=2), `health/minor-scrapes-and-wounds` (in=2), `health/shrinking-gills` (in=2), `health/parasite-treatment` (in=2), `tank-setup/canister-vs-sponge-filter` (in=2, 6117w — the site's longest page, barely reinforced), `axolotl-in-culture/*` (in=2–5, fine for PERIPHERAL).

---

## 7. Hub-spoke integrity

All 12 cluster hubs show `in=0` content inbound; every hub's reach comes from the template nav (content_in=124/125). That the **spokes never contextually link back to their hub** is normal in many architectures, but combined with two specific clusters it becomes a real defect:

1. **Legal (OUTER, column inbound = 0)**: no planning, breeding, or buying page links into `legal` or `/legal/*` from body content. The queries these pages answer ("are axolotls legal in [...]") are exactly the questions that occur *while planning purchase* — the cost-and-buying and care-basics funnel should route there contextually. Currently a reader can only discover legal via the nav.
2. **Tools (FUNCTIONAL, column inbound = 0)**: the 5 calculators are rendered on every page via nav but are never referenced in article body text where the calculation is relevant (§13).

Additionally, Phase 7's secondary-signal map promised legal cross-links from `wild-habitat-xochimilco`, `care-basics/axolotl-facts`, `are-axolotls-good-beginner-pets`, `cost-and-buying/*`, `breeding/*` — the executed linkgraph realizes **none** of these (legal column = 0). Planned-but-unimplemented links are catalogued in `link-issues.csv` (LI-02).

Conversely the hub→spoke pattern is strong: hubs `care-basics` (out=10), `diet` (out=12), `health` (out=18), `tank-setup` (out=17) fan out to full cluster coverage.

---

## 8. Content gap register (summary)

Full register: `gap-register.csv` (machine-readable). High-confidence gaps, by priority:

**P0 — concentration & conversion blocking**
- **G0-01 · Tools unanchored.** No content edge reaches any tool page (§3, §13). Readers solving feeding/size/water/sickness problems are one nav-layer away from a utility, at the exact moment of need.
- **G0-02 · Water master node lacks FAQ + tool link.** `water-parameters-cycling` is in=15 (top authority), 4924w, but has **no FAQ block** (Phase 7 flags `[no-faq]`) and never mentions the `nitrogen-cycle-tracker` or `water-conditioner-dosage-calculator`. The site's most authoritative page is the least rich in PAA-driven sub-headings and the least tool-connecting.
- **G0-03 · Diet silo.** `diet` is 97% self-contained. `overfeeding-and-impaction` (diagnostic, in=6) should reach `health/impaction-symptoms-treatment` and `health/malnutrition-signs`; `feeder-fish-risks` should reach parasite content; `feeding-schedule-by-age` should reach `breeding/raising-juveniles` and the feeding tool.

**P1 — E-E-A-T & scoping**
- **G1-01 · Vet node thin.** `finding-an-exotic-vet` 519w, in=2, no emergency-threshold content; diagnostic pages don't escalate to it. Bridge.
- **G1-02 · Behavior/stress overlap.** `care-basics/behavior`, `health/stress-signs` (576w, thin, no FAQ), `health/curled-gills-stress-signal`, `health/why-axolotl-floating`, `health/shrinking-gills` share the behavior/gill-state attribute. Needs explicit role differentiation + a cross-cluster link lattice (§9, CG-04).
- **G1-03 · Gill-state space fragmented.** Healthy-gill reference is spread over `anatomy-gills-and-lungs` + `how-to-choose-a-healthy-axolotl` + the three gill diagnostics. Recommend reciprocal linking into a gill-state cluster, not a new page.
- **G1-04 · Juvenile lifecycle unconnected.** `axolotl-age-and-size-chart` → `breeding/raising-juveniles` → `diet/blackworms-for-juveniles` → `diet/feeding-schedule-by-age` should be one explicit path; only sparse pieces exist.
- **G1-05 · Legal planning links unrealized.** Add legal cross-links at the planning moment (cost-and-buying, are-axolotls-good-beginner-pets, shipping, breeding) per Phase 7 secondary signals.
- **G1-06 · Biology→breeding bridge.** `neoteny`, `lifespan-wild-vs-captivity`, `regeneration-and-limb-regrowth` → breeding pages is 0 in content.

**P2 — polish (included for completeness)**
- **G2-01** morphs-comparison-chart 466w (thin) — promote to mini-hub inside morphs.
- **G2-02** `taxonomy`/`species` node `axolotl-vs-tiger-salamander` — fine as is; optional FAQ add.
- **G2-03** `tank-mates` (601w), `acclimating-a-new-axolotl` (639w), `tank-size-by-age` (500w) thin but adequately integrated.
- **G2-04** `pigment-cells` (588w, in=4) — morph pages don't link the mechanism page; add 1–2.

---

## 9. Cannibalization register

Full register: `gap-register.csv` row-type CANNIBALIZATION. Findings:

| pair/group | entity + attribute | role | verdict |
|---|---|---|---|
| `care-basics/behavior` ↔ `health/stress-signs` ↔ `health/curled-gills-stress-signal` ↔ `health/why-axolotl-floating` ↔ `health/shrinking-gills` | behavior / gill posture | diagnostic (care) vs diagnostic (health) | **POTENTIAL** — five nodes answer "is something wrong?" with overlapping evidence (curled gills, floating, appetite loss). Must be scoped: behavior = normal repertoire; stress-signs = first-response protocol; curled-gills = one sign deep-dive; floating = one sign deep-dive; shrinking-gills = chronic cause. Add explicit cross-links + distinct subsidiary headings. |
| `tank-setup/tank-size-by-age` ↔ `care-basics/axolotl-age-and-size-chart` ↔ `tools/tank-size-calculator` | size / growth | definitional vs definitional vs tool | **LEGITIMATE** — different roles for different intents. Keep, but add directional links: age-and-size-chart → size-by-age → calculator. |
| `diet/axolotl-pellets` ↔ `diet/best-foods-list` ↔ `diet/shrimp-for-axolotls` ↔ `diet/beef-heart` | food | comparative vs reference vs definitional | **LEGITIMATE** — food-entity pages vs reference. best-foods-list is already the hub (in=8). |
| `diet/overfeeding-and-impaction` ↔ `diet/fasting-and-vacation` | appetite | diagnostic vs procedural | **LEGITIMATE** — opposite axes; must cross-link (currently they don't — see diet silo). |
| `diet/feeder-fish-risks` ↔ `health/parasite-treatment` | nutrition/disease | explanatory vs diagnostic | **LEGITIMATE** but **missing link** — feeder-fish-risks should point to parasite-treatment. |
| morphs leucistic/wild-type/melanoid/golden-albino/copper/piebald/mosaic/chimera | morph/color | definitional | **LEGITIMATE** — distinct values of one attribute; comparison-chart already exists as disambiguator. |
| legal state pages (7) | legality | location-specific | **LEGITIMATE** — distinct jurisdiction values. |
| `/health/refusing-to-eat` ↔ `/health/malnutrition-signs` ↔ `/diet/fasting-and-vacation` | appetite/nutrition | diagnostic vs diagnostic vs procedural | **BORDERLINE** — refusing-to-eat (in=11) is the authority; malnutrition-signs should cite it explicitly (link exists one-way? see gap register). |

No true cannibalization (two near-identical pages at comparable authority for the same intent) was found. The only cluster in real risk is the behavior/stress group above.

---

## 10. Internal linking audit (content graph)

Issues from the 413-edge graph, grouped and catalogued in `link-issues.csv`.

**Missing high-value edges (link exists in intent but not in graph)** — see §8 gap register; the ten most valuable:
1. `diet/feeding-schedule-by-age` → `tools/feeding-schedule-generator`
2. `tank-setup/water-parameters-cycling` → `tools/nitrogen-cycle-tracker`
3. `health/stress-signs` → `tools/symptom-checker`
4. `health/refusing-to-eat` → `tools/symptom-checker`
5. `tank-setup/tank-size-by-age` → `tools/tank-size-calculator`
6. `tank-setup/water-conditioners` → `tools/water-conditioner-dosage-calculator`
7. `diet/overfeeding-and-impaction` → `health/impaction-symptoms-treatment`
8. `diet/feeder-fish-risks` → `health/parasite-treatment`
9. `care-basics/behavior` → `health/stress-signs` (and reverse)
10. `cost-and-buying/axolotl-price-by-morph` → `legal` (`legal/&ast;`) + `cost-and-buying/red-flags-when-buying` → `legal`

**Directionality defects**
- `health → diet` 4 vs `diet → health` 1: consequence pages (malnutrition, refusing-to-eat) point at causes in diet, but diet never points back at consequences. Add 2–3 return edges.
- `health → tank-setup` 8 vs `tank-setup → health` 3: acceptable asymmetry (disease flows downward), but `diet/salt-bath` / `black-tea-bath` (procedural treatments) should cross-link the fungal-infections diagnostic they treat.
- `tools → axolotls` 3: the only tool outbound edges point at the axolotls tab; tools should also point at their knowledge articles (§13).

**Incorrect/unreliable edges**
- No `content-linkgraph.json` edge stores anchor text — anchor quality cannot be verified from Phase 7B artifacts. **Flag**: re-run extraction anchor-aware in the next phase (LI-08). Phase 7's word-boundary secondary signals (e.g. `health → cost-and-buying`, `legal/canada → cost-and-buying`) were keyword-driven and over-predict cross-cluster links that the executed graph does not confirm.

**Generic/untyped link clusters**
- Hub "Related guides" widgets are untyped link lists (navigation-like, in template). Fine as hubs; they should not be the *only* cross-cluster carrier between `diet` and `health` cause pages.

**Reciprocity quality**
- Reciprocal pairs that are well-formed: `morphs ↔ cost-and-buying` (5 edges), `breeding ↔ morphs` (11), `care-basics ↔ cost-and-buying` (4), `culture ↔ gifts` (3).
- One-way pairs to fix: `health ↔ diet` (see above), `care-basics ↔ diet` (care-basics→diet = 1, diet→care-basics = 0 — `axolotl-intelligence-and-bonding → diet` has no return).

**Clique check**: tank-setup's `lighting ↔ hides-and-caves ↔ live-vs-artificial-plants` triangle and `water-conditioners ↔ acclimating ↔ water-parameters-cycling` triangle are legitimate decor/water workspaces, not link-cliques (external nodes exist at both ends).

---

## 11. PPR snapshot (prominence × popularity × relevance)

PPR is properly measured with query data (clicks, impressions). This snapshot uses the artifacts we have and states clearly what is unobserved:

- **Prominence P**: content inbound (`in=`) from the linkgraph — observed.
- **Popularity P'**: **NOT OBSERVED** (no search-console/keyword-volume export was available for this audit). FAQ-count per page (Phase 7) is used only as a *PAA-fit proxy*, never as traffic.
- **Relevance R**: qualitative — does the node's role/intent match the class of query its cluster serves (diagnostic↔problem-solving, tool↔calculator, location↔geo)? Qualified High/Med.

| node | P (in=) | P' proxy (FAQ) | R | PPR reading |
|---|---|---|---|---|
| water-parameters-cycling | 15 | 0 | High | the site's launcher node — but FAQ=0 caps its PAA surface near-term |
| refusing-to-eat | 11 | 17 | High | highest combined (P×PAA) — protect, don't dilute |
| fungal-infections-saprolegnia | 10 | 4 | High | strong diagnostic authority |
| leucistic | 10 | 4 | Med | morph demand is real but ADJACENT |
| setup-guide | 9 | 5 | High | procedural anchor |
| color-genetics-punnett-squares | 9 | 0 | Med | genetics gateway |
| best-foods-list | 8 | 0 | High | CORE diet reference (PAA gap!) |
| feeding-schedule-by-age | 8 | 10 | High | procedural + PAA-strong |
| canister-vs-sponge-filter | 2 | 11 | High | longest page (6117w), rich FAQs, in=2 — **under-promoted relative to content mass** |
| finding-an-exotic-vet | 2 | 4 | Med | thin, cold — raise P, keep R |
| (all 5 tools) | 0 | 0–6 | High (tool) | functional value, zero semantic P |

**PPR conclusion**: the corpus over-in-Bs toward two megafauna nodes (refusing-to-eat, water-parameters-cycling) while *content-rich, query-rich* mid pages — especially `canister-vs-sponge-filter`, `axolotl-pellets`, `beef-heart`, `squishmallow-guide` — sit at in=2. Weight-of-authority should be redistributed with ~4–6 new contextual inbound links each (§8), and the **FAQ-less authority pages** (water-parameters-cycling, best-foods-list, color-genetics, leucistic, wild-type, setup-guide) should carry micro-FAQs next phase since they are the pages most likely to earn PAA placement.

---

## 12. Border audit

Everything mapped in `page-roles.csv` lands inside CORE→PERIPHERAL; nothing is OUTSIDE the topic sphere. Verdict per cluster on whether its ring and content both justify keeping the pages as-is:

| cluster | ring | verdict | note |
|---|---|---|---|
| care-basics | CORE | keep | one PERIPHERAL node (pronounce) is justified low-cost demand |
| tank-setup | CORE | keep | exhaustive, correctly integrated |
| diet | CORE | keep | needs cross-cluster venting (§8 G0-03) |
| health | CORE | keep | richest; watch the behavior/stress overlap (§9) |
| morphs | ADJACENT | keep | pigment-cells → morph links missing |
| breeding | ADJACENT | keep | add biology→breeding bridge |
| biology-and-science | ADJACENT | keep | comparison node justified |
| cost-and-buying | OUTER | keep | good reciprocity with morphs |
| legal | OUTER | keep | must gain content inbound (LI-02) |
| axolotl-in-culture | PERIPHERAL | keep | culture→conservation links are on-strategy |
| gifts-and-merch | PERIPHERAL | keep | one-way into culture; acceptable |
| tools / search / meta | FUNCTIONAL | keep | tools need semantic integration (§13) |

No node is recommended for removal. Border hygiene is good; the audit's work is connectivity, not pruning.

---

## 13. Tools as semantic nodes

The five tools are the site's most UX-valuable FUNCTIONAL artifact and its most semantically disconnected. Facts from the artifacts: `tools` cluster has 0 content inbound (matrix column = 0), 3 outbound content edges total (to axolotls), each tool is template-linked on every page (in=124/125 by nav only), and content-inout shows tools-index in=0/out=0.

Seed-and-spoke pairing they should own (none implemented):

| tool | entity/intent it serves | knowledge article that must link it (missing) | tool should link back to |
|---|---|---|---|
| feeding-schedule-generator | feeding plan, procedural | diet/feeding-schedule-by-age | diet/feeding-schedule-by-age |
| nitrogen-cycle-tracker | nitrogen cycle, water | tank-setup/water-parameters-cycling | tank-setup/water-parameters-cycling, setup-guide |
| symptom-checker | health mystery, diagnostic | health/stress-signs, health/refusing-to-eat | health hub, health/&ast; diagnostics |
| tank-size-calculator | tank sizing, definitional | tank-setup/tank-size-by-age | tank-setup/tank-size-by-age |
| water-conditioner-dosage-calculator | water conditioning, procedural | tank-setup/water-conditioners | tank-setup/water-conditioners |

Recommendation: if a tool is rendered as a "[action] + [tool]" contextual block inside the matching article (one contextual outbound link from the article to the tool and one return link), the tools cluster becomes a *supporting hub* of the CORE clusters rather than a nav-only layer, and every CORE diagnostic/procedural page carries a completion CTA without any new template work.

---

## 14. Topological model & recommended change order

Current model (what the graph actually implements):

```
                    NAV LAYER (renders hubs + tools on every page)
  home ── axolotls ─ care-basics ─ tank-setup ─ diet ─ health
                    morphs ─ breeding ─ biology  (ADJACENT ring)
                    cost-and-buying ─ legal      (OUTER ring)
                    culture ─ gifts              (PERIPHERAL ring)
                    tools                        (FUNCTIONAL, nav-only, no content edges in)
```

Implementation order for the audit's recommendations (each is a content/link edit, no new pages required):

1. **P0 link battery** — add the 10 missing high-value edges of §10 (tools ×5, diet→health ×2, diet feathers→parasite, behavior↔stress-signs, price→legal). Low effort, immediate topology change.
2. **P0 FAQ top-up** — micro-FAQ blocks on the FAQ-less authority pages (§11) so the PPA-in-strong nodes gain PAA fit, *not* new body text.
3. **P1 vet + juvenile ladder** — depth for `finding-an-exotic-vet`, and the care→breeding→diet juvenile path (§8 G1-01/G1-04).
4. **P1 legal & biology bridles** — legal column inbound > 0; biology→breeding edges (§8 G1-05/G1-06).
5. **P2 polish** — pigment-cells, morphs-comparison-chart, misc thin pages.
6. **Re-run** `phase7_extract.py` + `phase7_digest.py` + `phase7b_links.py` after edits; then **anchor-aware** extraction and a live PPR pass with Search Console once available (LI-08).

---

## Appendix — machine-readable registers

- `docs/phase7b/gap-register.csv` — 20 rows: P0/P1/P2 content gaps + cannibalization verdicts (type, priority, cluster, nodes, evidence, action, expected_effect).
- `docs/phase7b/link-issues.csv` — 12 rows: missing-edge and directionality issues with graph evidence (severity, from, to, category in graph, evidence).

Scope note: this report is analytical output of Phase 7B only. No site files were changed to produce it.