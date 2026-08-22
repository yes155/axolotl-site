# Phase 10 — Search Change Report

Companion to `docs/phase9/phase9-search-spec.md`. Part A (index metadata, synonym/alias layer,
keyboard nav, ARIA, role badges) shipped in Phase 9. This report specifies the **Phase 9-B search
refinements** implemented in Phase 10, driven by the cannibalization/care decisions above.

## 1. Intent-aware routing (dedupe at the family level)

For each dedupe family a canonical URL wins for its dominant query; the runner-up stays in results
but is clearly scoped by its role label:

| Family | Trigger tokens | Canonical winner | Runner-up behavior |
|---|---|---|---|
| care | care guide, how to care, axolotl care | `/axolotls/care-guide` (article) | `/axolotls/` hub shown only for navigation intent (exact hub words) |
| stress | stress, stressed | `/health/stress-signs` (umbrella) | curled-gills / floating shown below, labeled "specific sign" |
| fasting | fast, fasting, vacation, no food for | `/diet/fasting-and-vacation` (planned fast) | refusing-to-eat labeled "medical refusal"; feeding-schedule labeled "routine" |
| fungus | fungus, fungal, saprolegnia, cotton | `/health/fungal-infections-saprolegnia` | tea-bath / salt-bath labeled "treatment" |
| impaction | impaction, impacted, bloated belly | `/health/impaction-symptoms-treatment` | overfeeding / substrate / gravel labeled "cause: …" |
| filter | filter, filtration, canister, sponge | `/tank-setup/filtration-for-axolotls` (principles) + `/tank-setup/canister-vs-sponge-filter` (decision) | both kept, different role labels |
| cooling | chiller, cool, too warm, temperature | `/tank-setup/temperature` (info) + `/tank-setup/aquarium-chillers` (buying) | both kept, different role labels |
| morph price | price, cost, how much (morph) | `/cost-and-buying/axolotl-price-by-morph` | morph pages labeled by morph |
| budget | budget, monthly cost, first year | `/care-basics/cost-of-ownership-monthly` | none |
| regeneration | regeneration, regrow, limb | biology page (science) vs `/health/limb-regeneration` (owner) | both kept; "the science" vs "owner's guide" labels |

## 2. Troubleshooting deep-link routing

- "curl"/"curled", "floating"/"float", "not eating"/"won't eat", "gills", "fungus" all route to the
  specific diagnostic pages (not the umbrella) when the token is the dominant intent.
- Symptom-checker style queries ("my axolotl is ...") bias toward `/health/stress-signs` +
  `/tools/symptom-checker`.

## 3. Vet / emergency enrichment

- Queries containing "vet", "veterinarian", "emergency", "urgent", "dying", "help" boost
  `/health/finding-an-exotic-vet` and the new `/health/emergency-first-aid`, and surface a
  "Find a vet / Emergency" action chip.

## 4. Empty-result cluster fallback

- If no entry scores above the null threshold, fall back to the cluster of the best partial match,
  then to the hub's top guides. The `/search/` page never renders a blank state for a plausible topic.

## 5. Calculator query capture

- "dose"/"calculator"/"how much conditioner", "sizing"/"what size tank", "schedule"/"feeding
  schedule", "track"/"cycle", "symptom checker" all route to the matching tool with an **action
  button** ("Open tool") from the result card. Tool entries carry `action` metadata from the build.

## 6. Typo salvage

- Edit-distance (≤2) against a curated alias/typo list: `flake → leucistic`, `melaniod →
  melanoid`, `alby → albino`, `saprolegnia → saprolegnia/fungus`, `lucy → leucistic`,
  `bamboo/axe/lottl` variants → axolotl. Uses the existing alias layer in search.js.

## 7. Role-aware dedupe (result families)

- After scoring, collapse result families: no two results from the same dedupe family may both
  appear in the top-3 unless they carry distinct role labels (which they do per §1).

## 8. Implementation

- Build side (`build/build.py`): each index entry gains `action` metadata
  (`{"label", "url", "kind": "tool"|"guide"}`) from `config.SEARCH_ACTIONS`; new articles and hubs
  flow in automatically.
- Client side (`public/js/search.js`): keeps Phase 6/9 features (cluster-aware scoring, aliases,
  role badges, calculator actions, keyboard nav, ARIA) and adds the 6 behaviors above.

## 9. Smoke tests (Phase 10)

Maintained in `docs/phase10/_search-smoke.md` — see the QA report for results.
