# Phase 11 — SEO / Search Implementation Report

Phase 11 was a **routing-correction pass** over the Phase 10 search layer. The
Phase 10 change report (`docs/phase10/phase10-search-changes.md`) documented
several behaviors that the shipped `public/js/search.js` did **not** actually
deliver under natural-language queries. This phase narrowed the gaps without
rewriting the scoring architecture: intent boost weights and the alias layer
were adjusted so the documented routing wins clean, real-world phrasings, and
previously-hijacked queries now reach the correct owner.

Scope guardrail honored: **no URL, redirect, page, or semantic-relationship
changes.** Nothing here invalidates Phase 10 assertions; the Phase 10 smoke
suite (20/20) and Phase 10 QA metrics are unchanged and still pass.

---

## 1. Changes

### 1a. Narrowed the price-family trigger (was: feeding/dosage hijack)

**Problem.** The `price` family triggered on the bare phrase `how much`
(`build/config.py` family table in `search.js`). Because `how much` is
hyper-common, informational queries were livestolen by the price page:

- `how much to feed my axolotl`
- `how much conditioner do i need`
- `how much water conditioner do i need`

**Fix.** Replaced the `how much` trigger with morph-specific cost phrasings:

| Trigger set (`price`) |
|---|
| `price`, `cost`, `expensive` |
| `how much does`, `how much is`, `how much cost` |

`how much does an axolotl cost` still routes to `/cost-and-buying/axolotl-price-by-morph/`
(Phase 10 assertion #7 unchanged), while feeding/conditioner queries fall to
their correct owners. A new synonym entry maps `how much conditioner` /
`how much water conditioner` / `how many drops` → `dosage calculator`,
so those queries surface `/tools/water-conditioner-dosage-calculator/`.

### 1b. Gated emergency / vet enrichment (was: weak + blanket `help` boost)

**Problem.** The Phase 10 report claimed `vet / veterinarian / emergency /
urgent / dying / help` *"boost finding-an-exotic-vet and the new
emergency-first-aid, and surface a 'Find a vet / Emergency' action chip."*
The shipped code applied a single `+8` to both pages whenever **any** of those
words appeared — too weak to surface emergency content for
`my axolotl is dying help`, and simultaneously too broad because bare `help`
fired for any help-seeking query.

**Fix.** Split the boost:

- **Strong distress words** — `emergency`, `urgent`, `dying` → `+30` to
  `/health/emergency-first-aid/`, `+10` cross-enrichment to
  `/health/finding-an-exotic-vet/`.
- **Strong vet intent** — `vet`, `veterinarian` → `+30` to the vet page,
  `+10` cross-enrichment to first aid.
- **Gated `help`** — `help` only boosts (`+14`) when combined with a
  health / symptom / the-pet context: `my axolotl`, `dying`, `symptom`,
  `sick`, `not eating`, `floating`, `curled`, `fungus`, `ammonia`, etc.
  Informational help queries (`help with tank setup`) are untouched.

Results (verified by `build/phase11_search_smoke.mjs`):

- `my axolotl is dying help` → **#1** `/health/emergency-first-aid/`
- `find a vet near me` → **#1** `/health/finding-an-exotic-vet/`
- `help my axolotl` → first-aid surfaces in top results (with action chip)
- `help with tank setup` → tank-setup guides only (no emergency hijack)

### 1c. Symptom-checker umbrella (documented in §2 but never implemented)

**Problem.** Phase 10 §2 promised *"Symptom-checker style queries
('my axolotl is ...') bias toward /health/stress-signs +
/tools/symptom-checker."* The shipped code had **no such route**:
`my axolotl is acting strange` returned /joke/wants-peace-and-quiet.

**Fix.** Added a low-weight umbrella boost (+12 to `/health/stress-signs/`
and `/tools/symptom-checker/`) for `my axolotl is/has/seems`,
`my axolotl acting`, and `something is wrong`. It is deliberately **weaker
than the specific TROUBLE_ROUTES (+9)**, preserving the documented precedence:

1. specific symptom owner (won't eat → refusing-to-eat, floating →
   why-axolotl-floating, white spots → fungus),
2. emergency / vet intent,
3. generic "my axolotl is …" symptom intent,
4. normal informational / how-to routing.

Verified: `my axolotl won't eat` still → refusing-to-eat; `my axolotl is
floating a lot` → why-axolotl-floating; `my axolotl has white spots` → fungus.

### 1d. Fasting phrase alias (was: family trigger present, routing too weak)

**Problem.** The fasting family already triggered on `no food`, but the
canonical page (`How Long Can Axolotls Fast?`) still lost to weight-of-content
scoring: `no food for a month axolotl` returned beginner/hub pages.

**Fix.** Added a synonym entry mapping `no food` / `without food` /
`gone without food` → `fast` / `fasting` / `vacation` so the fasting page's
title phrase wins. Medical refusal keeps precedence — `my axolotl is not
eating` still → `/health/refusing-to-eat/`.

### 1e. Typo aliases documented but missing (Phase 10 §6)

**Problem.** Phase 10 §6 listed `bamboo / axe / lottl → axolotl`, but the
`TYPO_MAP` had none. `axe` single-term returned /joke/new-jersey/.

**Fix.** Added `axe`, `bamboo`, `lottl` → `axolotl` to `TYPO_MAP`. `fixTypos`
only rewrites **single-token** queries, so these scoped aliases cannot
override strong multi-word matches. Verified: `axe`, `bamboo`, `lottl` all
salvage to axolotl-topic guides.

### 1f. Build cleanups (config / tool metadata)

- **Removed dead action** — `config.SEARCH_ACTIONS` contained
  `health/symptom-checker`, a slug that does not exist as an article (the
  symptom checker is a tool and carries its own action from `config.TOOLS`).
  The entry was inert but inaccurate; removed.
- **Injected missing tool descriptions** — 3 of 5 `public/tools/*/index.html`
  had no `<meta name="description">` (feeding-schedule-generator,
  symptom-checker, tank-size-calculator). `build.py::copy_tools()` now injects
  `meta name="description"` + `og:description` + `twitter:description` from
  `TOOL_DESCS` when absent, mirroring the existing canonical-tag injection.
  (The other 2 tools already owned description tags from their source files.)

## 2. Files changed

| File | Change |
|---|---|
| `public/js/search.js` | price trigger, gated urgent/vet boost, symptom umbrella, fasting alias, typo aliases |
| `build/phase10_search_smoke.mjs` | kept verbatim-in-sync with `search.js` (Phase 10 assertions unchanged) |
| `build/phase11_search_smoke.mjs` | **new** — 21 natural-language routing assertions |
| `build/phase11_qa.py` | **new** — weighted QA runner (writes `docs/phase11/qa-report.json`) |
| `build/config.py` | removed dead `health/symptom-checker` SEARCH_ACTION |
| `build/build.py` | `copy_tools()` injects missing tool meta descriptions |
| `docs/phase11/qa-report.json` | **new** — Phase 11 QA report |
| `docs/phase11/phase11-search-changes.md` | this report |

The smoke runner stays a faithful Node port of `public/js/search.js` so the
Phase 10 gate continues to test the exact shipped pipeline.

## 3. Verification

| Gate | Result |
|---|---|
| Build (`python build/build.py`) | clean, 125 index entries, 131 pages |
| **Phase 10 smoke** (`node build/phase10_search_smoke.mjs`) | **20/20 PASS** |
| Phase 10 QA (`python build/phase10_qa.py`) | 0 broken / 0 canonical / 482 edges (unchanged baseline) |
| **Phase 11 smoke** (`node build/phase11_search_smoke.mjs`) | **21/21 PASS** |
| **Phase 11 QA** (`python build/phase11_qa.py`) | **100/100 PASS** (threshold ≥ 65) |
| Broken links / canonical / sitemap-index parity / tool descriptions / dead actions | all clean |

No Phase 10 assertion regressed; no weights were re-tuned to force a pass.
This was a routing correction pass only.