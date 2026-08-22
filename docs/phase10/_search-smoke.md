# Phase 10 — Search Smoke Tests

Home of the Phase-10 search regression suite referenced in
`phase10-search-changes.md` §9. The runner is a faithful Node port of the
exact scoring / routing pipeline in `public/js/search.js`
(`scoreItem`, `phraseBoost`, `applySemantic`, `limitFamilies`,
`clusterFallback`, `fixTypos`) executed against the built
`public/search-index.json`, so no browser is needed to gate a build.

## Run

```powershell
node build/phase10_search_smoke.mjs
```

Exit code 0 = every assertion passes. Read via `docs/phase10/qa-report.json`
for link/canonical/deliverable checks (`python build/phase10_qa.py`).

## Scenarios (mapped to phase10-search-changes.md)

| # | Query | Expected winner | Spec section |
|---|---|---|---|
| 1 | `flake` (typo) | `/morphs/leucistic/` | §6 typo salvage |
| 2 | `curled gills` | `/health/curled-gills-stress-signal/` | §2 trouble deep-link |
| 3 | `my axolotl won't eat` | `/health/refusing-to-eat/` | §2 trouble deep-link |
| 4 | `not eating` | `/health/refusing-to-eat/` | §1 fasting family / §2 |
| 5 | `water conditioner dosage calculator` | `/tools/water-conditioner-dosage-calculator/` | §5 calculator capture |
| 6 | `symptom checker` | `/tools/symptom-checker/` | §5 calculator capture |
| 7 | `how much does an axolotl cost` | `/cost-and-buying/axolotl-price-by-morph/` | §1 price family |
| 8 | `monthly cost of owning an axolotl` | `/care-basics/cost-of-ownership-monthly/` | §1 budget family |
| 9 | `axolotl impaction` | `/health/impaction-symptoms-treatment/` | §1 impaction family |
| 10 | `why is my axolotl floating` | `/health/why-axolotl-floating/` | §2 trouble deep-link |
| 11 | `fasting axolotl` | `/diet/fasting-and-vacation/` | §1 fasting family |
| 12 | `white fungus on axolotl` | `/health/fungal-infections-saprolegnia/` | §1 fungus family |
| 13 | `stress signs` | `/health/stress-signs/` (hub demoted) | §1 stress family |
| 14 | `regeneration science` | `/biology-and-science/regeneration-and-limb-regrowth/` | §1 regeneration |
| 15 | `how do axolotls regrow limbs` | `/health/limb-regeneration/` | §1 regeneration |
| 16 | `water too warm` | `/tank-setup/temperature/` (hub demoted) | §1 cooling family |
| 17 | `best chiller` | `/tank-setup/aquarium-chillers/` | §1 cooling nuance |
| 18 | `best filter` | `/tank-setup/filtration-for-axolotls/` | §1 filter family |
| 19 | `emergency` | `/health/emergency-first-aid/` | §3 vet/emergency |
| 20 | `find a vet` | `/health/finding-an-exotic-vet/` | §3 vet/emergency |

## Current status

**20 / 20 passing** (2026-08-20, build of 108 articles / 126 content pages).