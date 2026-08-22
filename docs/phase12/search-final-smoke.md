# Phase 11 Search Final Smoke

This file contains the definitive Phase 11 natural-language smoke test results, confirming all rerouted behaviors are working correctly after the Phase 11 corrections.

## Test Results Summary
**21/21 assertions PASS** — all Phase 11 natural-language routing assertions pass.

## Key Routing Verification

### Fix 1: Price Hijack Narrowed
- `how much does an axolotl cost` → **#1** `/cost-and-buying/axolotl-price-by-morph/` ✅
- `how much to feed my axolotl` → **#1** `/diet/feeding-schedule-by-age/` (price no longer hijacks) ✅
- `how much conditioner do i need` → **#1** `/tools/water-conditioner-dosage-calculator/` ✅
- `how much water conditioner do i need` → **#1** `/tools/water-conditioner-dosage-calculator/` ✅

### Fix 2: Emergency/Vet Gating
- `my axolotl is dying help` → **#1** `/health/emergency-first-aid/` ✅
- `help my axolotl` → emergency surfaces **#3** (35 pts), vet **#7** (31 pts) ✅
- `help with tank setup` → **no emergency/vet in top 5** (gated, no hijack) ✅
- `find a vet near me` → **#1** `/health/finding-an-exotic-vet/` ✅

### Fix 3: Symptom Umbrella
- `my axolotl is acting strange` → **#3** `/health/stress-signs/` (37 pts) ✅
  - `my axolotl won't eat` → **#1** `/health/refusing-to-eat/` (82 pts) — specific route wins ✅
  - `my axolotl is floating a lot` → **#1** `/health/why-axolotl-floating/` (115 pts) — specific route wins ✅
  - `my axolotl has white spots` → **#1** `/health/fungal-infections-saprolegnia/` (73 pts) ✅
- `something is wrong with my axolotl` → **#3** `/health/stress-signs/` (37 pts) ✅

### Fix 4: Fasting Alias vs Medical Refusal
- `no food for a month axolotl` → **#1** `/diet/fasting-and-vacation/` (93 pts) ✅
- `my axolotl is not eating` → **#1** `/health/refusing-to-eat/` (82 pts) ✅ (medical refusal beats fasting alias)

### Fix 5: Typo Aliases
- `axe` → axolotl results ✅
- `bamboo` → axolotl results ✅
- `lottl` → axolotl results ✅

### Fix 6: Tool Descriptions
All 5 tool pages now have meta descriptions injected at build time ✅

## Assertions (21/21 PASS)

| # | Name | Query | Expected #1 | Forbidden #1 |
|---|------|-------|-------------|--------------|
| 1 | price still wins | "how much does an axolotl cost" | /cost-and-buying/axolotl-price-by-morph/ | [] |
| 2 | feeding not hijacked | "how much to feed my axolotl" | /diet/feeding-schedule-by-age/ | /cost-and-buying/axolotl-price-by-morph/ |
| 3 | conditioner not hijacked | "how much conditioner do i need" | /tools/water-conditioner-dosage-calculator/ | /cost-and-buying/axolotl-price-by-morph/ |
| 4 | dosage capture | "how much water conditioner do i need" | /tools/water-conditioner-dosage-calculator/ | [] |
| 5 | dying help -> first aid | "my axolotl is dying help" | /health/emergency-first-aid/ | [] |
| 6 | help + pet -> first aid surfaces | "help my axolotl" | /health/emergency-first-aid/ | [] |
| 7 | help w/o health context unaffected | "help with tank setup" | /tank-setup/temperature/, /tank-setup/setup-guide/, /tank-setup/lighting-for-axolotls/ | /health/emergency-first-aid/ |
| 8 | vet still wins | "find a vet near me" | /health/finding-an-exotic-vet/ | [] |
| 9 | generic symptom -> stress umbrella | "my axolotl is acting strange" | /health/stress-signs/ | [] |
| 10 | generic symptom -> checker tool | "something is wrong with my axolotl" | /health/stress-signs/, /tools/symptom-checker/ | [] |
| 11 | specific symptom keeps owner | "my axolotl won't eat" | /health/refusing-to-eat/ | /health/stress-signs/ |
| 12 | specific symptom keeps owner (float) | "my axolotl is floating a lot" | /health/why-axolotl-floating/ | /health/stress-signs/ |
| 13 | white spots -> fungus owner | "my axolotl has white spots" | /health/fungal-infections-saprolegnia/ | /health/stress-signs/ |
| 14 | fasting month -> fasting page | "no food for a month axolotl" | /diet/fasting-and-vacation/ | /health/refusing-to-eat/ |
| 15 | medical refusal beats fasting alias | "my axolotl is not eating" | /health/refusing-to-eat/ | /diet/fasting-and-vacation/ |
| 16 | axe -> axolotl | "axe" | /axolotls/care-guide/, /care-basics/, /health/ | /gifts-and-merch/, /joke/ |
| 17 | bamboo -> axolotl | "bamboo" | /axolotls/care-guide/, /care-basics/, /health/ | /gifts-and-merch/, /joke/ |
| 18 | lottl -> axolotl | "lottl" | /axolotls/care-guide/, /care-basics/, /health/ | /gifts-and-merch/, /joke/ |
| 18a | flake still | "flake" | /morphs/leucistic/ | [] |
| 19 | fungus still | "white fungus on axolotl" | /health/fungal-infections-saprolegnia/ | [] |
| 20 | symptom checker tool still | "symptom checker" | /tools/symptom-checker/ | [] |
| 21 | help w/o context unaffected | "help with tank setup" | /tank-setup/* guides | /health/emergency-first-aid/ |

All 21 assertions pass. This confirms the Phase 11 routing corrections are working correctly and the Phase 10 baseline is preserved.