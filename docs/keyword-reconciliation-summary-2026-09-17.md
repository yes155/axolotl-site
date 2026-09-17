# MyAxolotl keyword reconciliation — 2026-09-17

## Scope

- Reconciles all 923 rows in `axoltol_all-keywords_us_2026-02-28 (1).xlsx` against the current MyAxolotl semantic architecture and page ownership.
- Applies the saved semantic SEO methodology: a missing keyword string is not itself a content gap. A gap requires a missing entity, attribute, value/state, relationship, intent, contextual bridge, or prerequisite.
- Architecture checkpoint used for the audit: `aa2d4085f3ff2a3c68942b35a292719cf1270ebe` plus current repository spot checks.
- Search-volume totals below are raw sums of Semrush keyword rows. Variants overlap, so these totals are demand signals rather than unique traffic estimates.

## Reconciliation result

| Coverage | Keyword rows | Raw volume |
|---|---:|---:|
| DIRECT | 773 | 211,010 |
| SUPPORTED | 24 | 4,530 |
| WEAK | 48 | 9,140 |
| MISSING | 32 | 6,040 |
| EXCLUDE | 41 | 4,410 |
| MISSING_LOW_PRIORITY | 5 | 400 |
| **Total** | **923** | **235,530** |

`DIRECT` means a dedicated page or direct semantic section clearly answers the intent. `SUPPORTED` means the meaning is answered but is not the primary section or ideal owner placement. `WEAK` means coverage is incidental or partial and the existing owner page should be strengthened. `MISSING` means no meaningful direct answer was found. `EXCLUDE` protects topical borders from generic, ambiguous, irrelevant, or volatile navigation queries.

## Highest-priority action gaps

| Semantic gap | Keyword rows | Raw volume | Existing owner | Decision |
|---|---:|---:|---|---|
| Teeth / oral anatomy | 6 | 3,640 | `/biology-and-science/anatomy-gills-and-lungs/` | Expand existing anatomy owner; do not create a standalone teeth page. |
| Freshwater vs saltwater | 15 | 2,310 | `/biology-and-science/wild-habitat-xochimilco/` | Add a direct freshwater/saltwater section to the habitat owner. |
| Spelling | 7 | 2,030 | `/care-basics/how-to-pronounce-axolotl/` | Add a direct “How do you spell axolotl?” section and common misspellings. |
| Discovery / history | 5 | 1,330 | `/care-basics/axolotl-facts/` | Add a sourced discovery/history section first; only split later if scope warrants it. |
| Wild predators | 6 | 1,230 | `/biology-and-science/conservation-status/` | Add a direct predators section with native vs introduced context. |
| Poisonous / venomous safety | 3 | 770 | `/care-basics/axolotls-and-children/` | Add a direct safety answer; no separate page. |

## Medium-priority expansions

- Other anatomy (ears, scales, nose, tongue, eyelids): broaden the existing anatomy page rather than fragmenting anatomy into multiple URLs.
- Adaptations: add a compact section to the appropriate biology/habitat owner; no new page yet.
- Sleep/rest and hibernation: strengthen `/care-basics/behavior/` with evidence-cautious distinctions.
- Cannibalism: add life-stage, nipping, and cannibalism context to `/care-basics/keeping-multiple-axolotls/`.
- Collective noun: verify reliable terminology before adding anything; do not manufacture an answer merely to target a keyword.

## Deliberate non-page decisions

- Retailer-specific Petco/PetSmart queries remain under the existing breeder-vs-pet-store decision page. Availability and pricing are volatile, so dedicated retailer pages are not justified.
- Mudpuppy/olm comparison variants have low demand and do not currently justify standalone pages.
- Generic salamander queries and other ambiguous/non-axolotl rows are excluded where targeting them would weaken the topical border.

## Important false alarms resolved by semantic checking

- “Are axolotls nocturnal?” is already answered by the behavior page’s section on when axolotls are most active.
- “What does axolotl mean?” is already directly answered by the pronunciation page.
- Vision/sight intent is already addressed by the intelligence-and-senses content.
- Minecraft feeding, breeding, taming, spawning, blue rarity, survival, despawning, combat, and command intent is now consolidated on the existing Minecraft guide rather than split into duplicate pages.

## Execution rule

Fix one semantic owner at a time. For each gap: verify the current final HTML, research the missing attribute where needed, update the existing owner page unless the Entity + Attribute + Intent + Page Role test proves a new URL is necessary, rebuild, verify generated `public/`, and then commit. Re-run the reconciliation after the priority expansions rather than chasing individual keyword strings.