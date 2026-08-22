/*
 * Phase 11 search smoke test — natural-language routing assertions.
 *
 * Reuses the exact Phase 10 porting approach (verbatim from public/js/search.js,
 * including Phase 11 rerouting: narrowed price trigger, gated help boost,
 * symptom-checker umbrella, no-food/without-food fasting alias, axe/bamboo/
 * lottl -> axolotl typo aliases).
 *
 * Usage: node build/phase11_search_smoke.mjs
 * Exit 0 = every assertion passes.
 */
import fs from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";

const here = path.dirname(fileURLToPath(import.meta.url));
const BASE = path.dirname(here);
const SITE = "https://axolotlcare.example.com";

// ---- verbatim port of search.js helpers (Phase 11 state) ----
function normalize(text) {
  return String(text || "")
    .toLowerCase()
    .replace(/\u2019/g, "'")
    .replace(/[^a-z0-9'\s-]/g, " ")
    .replace(/\s+/g, " ")
    .trim();
}
function tokenize(text) {
  return normalize(text).split(" ").filter(Boolean);
}
function stems(word) {
  const out = [word];
  if (word.length > 3 && word.slice(-1) === "s") out.push(word.slice(0, -1));
  return out;
}
function countTerms(termList, haystack) {
  let n = 0;
  termList.forEach(function (word) {
    let hit = false;
    stems(word).forEach(function (s) {
      if (haystack.indexOf(s) !== -1) hit = true;
    });
    if (hit) n += 1;
  });
  return n;
}

const SYNONYMS = [
  { q: ["not eating", "wont eat", "won't eat", "stopped eating", "refusing food", "not hungry"],
    hits: ["refusing to eat", "not eating", "refusing food"] },
  { q: ["not pooping", "constipated"],
    hits: ["constipation", "impaction", "pooping"] },
  { q: ["white fuzz", "white spots", "cotton", "fluffy"],
    hits: ["fungus", "saprolegnia", "white fuzz", "cotton"] },
  { q: ["how big", "what size tank"],
    hits: ["tank size", "minimum"] },
  { q: ["how often to feed", "how much to feed", "how much food"],
    hits: ["feeding schedule", "how often", "how much"] },
  { q: ["how much conditioner", "how much water conditioner", "how many drops"],
    hits: ["dosage calculator", "water conditioner", "dose"] },
  { q: ["no food", "without food", "gone without food"],
    hits: ["fast", "fasting", "vacation"] },
  { q: ["curled gills", "gills curled", "curled tail"],
    hits: ["curled gills", "curled tail", "stress signal"] },
  { q: ["need a filter", "do i need a filter", "best filter"],
    hits: ["filter"] },
  { q: ["can they live together", "multiple axolotls", "tank mates"],
    hits: ["keeping multiple", "tank mates", "multiple axolotls"] },
];

function phraseBoost(item, query) {
  const qn = normalize(query);
  let boost = 0;
  SYNONYMS.forEach(function (entry) {
    let triggered = false;
    entry.q.forEach(function (variant) {
      if (!triggered && qn.indexOf(normalize(variant)) !== -1) triggered = true;
    });
    if (!triggered) return;
    const titleN = normalize(item.title);
    const hay = function (s) { return normalize(s); };
    entry.hits.forEach(function (phrase) {
      const p = normalize(phrase);
      if (titleN.indexOf(p) !== -1) { boost += 22; return; }
      (item.headings || []).forEach(function (h) {
        if (hay(h).indexOf(p) !== -1) boost += 10;
      });
      if (hay(item.dek || "").indexOf(p) !== -1) boost += 7;
      if (hay(item.text || "").indexOf(p) !== -1) boost += 3;
    });
  });
  return Math.min(boost, 44);
}

function matchesAny(query, phrases) {
  const qn = normalize(query);
  for (const p of phrases) {
    if (qn.indexOf(normalize(p)) !== -1) return true;
  }
  return false;
}

const FAMILIES = [
  { key: "care", triggers: ["care guide", "how to care", "take care", "care of"],
    canonical: "/axolotls/care-guide/", demoteHubs: true },
  { key: "stress", triggers: ["stressed", "stress", "stressed out"],
    canonical: "/health/stress-signs/" },
  { key: "fasting", triggers: ["fasting", "fast", "vacation", "without food", "no food"],
    canonical: "/diet/fasting-and-vacation/" },
  { key: "fungus", triggers: ["fungus", "fungal", "saprolegnia", "cotton wool"],
    canonical: "/health/fungal-infections-saprolegnia/" },
  { key: "impaction", triggers: ["impaction", "impacted", "blocked up"],
    canonical: "/health/impaction-symptoms-treatment/" },
  { key: "filter", triggers: ["filter", "filtration", "canister", "sponge filter"],
    canonical: "/tank-setup/filtration-for-axolotls/" },
  { key: "cooling", triggers: ["chiller", "chillers", "cool", "too warm"],
    canonical: "/tank-setup/temperature/", boost: 16 },
  { key: "budget", triggers: ["budget", "monthly", "year one", "first year"],
    canonical: "/care-basics/cost-of-ownership-monthly/" },
  { key: "price", triggers: ["price", "cost", "how much does", "how much is",
    "how much cost", "expensive"],
    canonical: "/cost-and-buying/axolotl-price-by-morph/", boost: 18 },
  { key: "regeneration", triggers: ["regeneration", "regrow", "regrowing"],
    canonical: "/health/limb-regeneration/" },
];

function familyFor(query) {
  for (const f of FAMILIES) {
    if (matchesAny(query, f.triggers)) return f;
  }
  return null;
}

const TROUBLE_ROUTES = [
  { tokens: ["curled", "curl"], url: "/health/curled-gills-stress-signal/" },
  { tokens: ["floating", "float", "buoy"], url: "/health/why-axolotl-floating/" },
  { tokens: ["not eating", "wont eat", "won't eat", "refusing"], url: "/health/refusing-to-eat/" },
  { tokens: ["red leg", "red leg syndrome"], url: "/health/red-leg-syndrome/" },
  { tokens: ["ammonia burn", "burned gills"], url: "/health/ammonia-burns/" },
];
const URGENT_STRONG = ["emergency", "urgent", "dying"];
const VET_STRONG = ["vet", "veterinarian"];
const HELP_CONTEXT = ["my axolotl", "symptom", "dying", "emergency", "urgent", "vet",
  "veterinarian", "sick", "ill", "hurt", "not eating", "wont eat", "won't eat",
  "refusing", "floating", "curled", "fungus", "ammonia", "burn", "impaction",
  "stressed", "strange", "wrong"];
const TOOL_ROUTES = [
  { slug: "water-conditioner-dosage-calculator", tokens: ["dose", "how much conditioner", "calculator"] },
  { slug: "tank-size-calculator", tokens: ["sizing", "size tank", "what size", "how big"] },
  { slug: "feeding-schedule-generator", tokens: ["feeding schedule", "schedule generator"] },
  { slug: "nitrogen-cycle-tracker", tokens: ["cycle tracker", "track cycle", "tracker"] },
  { slug: "symptom-checker", tokens: ["symptom checker", "checker"] },
];
const KNOWN_WORDS = ["leucistic", "melanoid", "albino", "golden", "axolotl", "saprolegnia",
  "impaction", "morph", "fungus", "chiller", "cannister", "water"];
const TYPO_MAP = { flake: "leucistic", melaniod: "melanoid", alby: "albino", lucy: "leucistic",
  axololt: "axolotl", axolotll: "axolotl", axe: "axolotl", bamboo: "axolotl",
  lottl: "axolotl", groom: "frog", cannister: "canister" };

function editDistance(a, b) {
  const m = a.length, n = b.length;
  const row = new Array(n + 1);
  for (let j = 0; j <= n; j++) row[j] = j;
  for (let i = 1; i <= m; i++) {
    let prev = row[0];
    row[0] = i;
    for (let j = 1; j <= n; j++) {
      const tmp = row[j];
      row[j] = Math.min(row[j] + 1, row[j - 1] + 1, prev + (a[i - 1] === b[j - 1] ? 0 : 1));
      prev = tmp;
    }
  }
  return row[n];
}
function fixTypos(query) {
  const terms = tokenize(query);
  if (terms.length > 1) return query;
  const word = terms[0];
  if (TYPO_MAP[word]) return TYPO_MAP[word];
  let best = null, bestD = 3;
  KNOWN_WORDS.forEach(function (k) {
    const d = editDistance(word, k);
    if (d <= 2 && d < bestD) { bestD = d; best = k; }
  });
  return best || query;
}

function applySemantic(scores, query) {
  const byUrl = {};
  scores.forEach(function (s) { byUrl[s.item.url] = s; });
  const family = familyFor(query);
  if (family) {
    const canon = byUrl[family.canonical];
    if (canon) canon.score += (family.boost || 12);
    if (family.demoteHubs) {
      scores.forEach(function (s) {
        if (s.item.role === "hub" && s.item.url !== family.canonical) s.score -= 18;
      });
    }
  }
  if (family && family.key === "cooling") {
    if (matchesAny(query, ["chiller", "buy", "which chiller", "price"])) {
      const ch = byUrl["/tank-setup/aquarium-chillers/"];
      if (ch) ch.score += 10;
    }
  }
  if (matchesAny(query, ["regeneration", "regrow"])) {
    if (matchesAny(query, ["science", "how does", "why does", "biology"])) {
      const bio = byUrl["/biology-and-science/regeneration-and-limb-regrowth/"];
      if (bio) bio.score += 8;
    }
  }
  TROUBLE_ROUTES.forEach(function (r) {
    if (matchesAny(query, r.tokens)) {
      const t = byUrl[r.url];
      if (t) t.score += 9;
    }
  });
  const ev = byUrl["/health/emergency-first-aid/"];
  const vet = byUrl["/health/finding-an-exotic-vet/"];
  const evStrong = matchesAny(query, URGENT_STRONG);
  const vetStrong = matchesAny(query, VET_STRONG);
  if (evStrong && ev) ev.score += 30;
  if (vetStrong && vet) vet.score += 30;
  if (evStrong && vet) vet.score += 10;
  if (vetStrong && ev) ev.score += 10;
  if (matchesAny(query, ["help"]) && matchesAny(query, HELP_CONTEXT)) {
    if (ev) ev.score += 14;
    if (vet) vet.score += 14;
  }
  if (matchesAny(query, ["my axolotl is", "my axolotl has", "my axolotl seems",
                         "my axolotl acting", "something is wrong"])) {
    const stress = byUrl["/health/stress-signs/"];
    const checker = byUrl["/tools/symptom-checker/"];
    if (stress) stress.score += 12;
    if (checker) checker.score += 12;
  }
  TOOL_ROUTES.forEach(function (r) {
    if (matchesAny(query, r.tokens)) {
      const tool = byUrl["/tools/" + r.slug + "/"];
      if (tool) tool.score += 10;
    }
  });
}

function scoreItem(item, query, terms) {
  const titleNorm = normalize(item.title);
  let score = 0;
  if (titleNorm.indexOf(query) !== -1) score += 60;
  if (terms.length > 1 && countTerms(terms, titleNorm) === terms.length) score += 30;
  const titleHit = countTerms(terms, titleNorm);
  score += titleHit * 8;
  const catNorm = normalize(item.category || "");
  if (countTerms(terms, catNorm) > 0) score += 5 * countTerms(terms, catNorm);
  let headingHit = 0;
  (item.headings || []).forEach(function (h) {
    if (countTerms(terms, normalize(h)) > 0) headingHit += 1;
  });
  score += Math.min(headingHit, 3) * 4;
  if (countTerms(terms, normalize(item.dek || "")) > 0) score += 3;
  const body = normalize(item.text || "");
  let bodyHits = 0;
  body.split("\n").filter(Boolean).forEach(function (p) {
    const c = countTerms(terms, p);
    if (c > 0) {
      if (c === terms.length) bodyHits += 3;
      else bodyHits += 1;
    }
  });
  score += Math.min(bodyHits, 6) * 2;
  if (score > 0 && titleHit === terms.length) score += 2;
  score += phraseBoost(item, query);
  return score;
}

const index = JSON.parse(fs.readFileSync(path.join(BASE, "public", "search-index.json"), "utf-8"))
  .filter(it => it && it.title && it.url && it.url !== SITE + "/");

function rank(query) {
  const effectiveQuery = fixTypos(query);
  const terms = tokenize(effectiveQuery);
  const scored = [];
  index.forEach(function (item) {
    const s = scoreItem(item, effectiveQuery, terms);
    if (s > 0) scored.push({ item, score: s });
  });
  applySemantic(scored, effectiveQuery);
  scored.sort(function (a, b) {
    if (b.score !== a.score) return b.score - a.score;
    return a.item.title.localeCompare(b.item.title);
  });
  return { urls: scored.slice(0, 20).map(s => s.item.url.replace(SITE, "")), effective: effectiveQuery };
}

// name, query, expected[0] must be present in top-5, forbidden[0] must NOT be #1
const checks = [
  // Fix 1 — narrowed price trigger: feeding / conditioner / dosage no longer
  // hijacked by the price family; genuinely-cost queries still work.
  ["price still wins", "how much does an axolotl cost", ["/cost-and-buying/axolotl-price-by-morph/"], []],
  ["feeding not hijacked", "how much to feed my axolotl", ["/diet/feeding-schedule-by-age/"], ["/cost-and-buying/axolotl-price-by-morph/"]],
  ["conditioner not hijacked", "how much conditioner do i need", ["/tools/water-conditioner-dosage-calculator/", "/tank-setup/water-conditioners/"], ["/cost-and-buying/axolotl-price-by-morph/"]],
  ["dosage capture", "how much water conditioner do i need", ["/tools/water-conditioner-dosage-calculator/", "/tank-setup/water-conditioners/"], []],
  // Fix 2 — emergency gating: strong words boost; bare "help" in a
  // non-health context stays informational.
  ["dying help -> first aid", "my axolotl is dying help", ["/health/emergency-first-aid/"], []],
  ["help + pet -> first aid surfaces", "help my axolotl", ["/health/emergency-first-aid/"], []],
  ["help w/o health context unaffected", "help with tank setup", ["/tank-setup/temperature/", "/tank-setup/setup-guide/", "/tank-setup/lighting-for-axolotls/"], ["/health/emergency-first-aid/"]],
  ["vet still wins", "find a vet near me", ["/health/finding-an-exotic-vet/"], []],
  // Fix 3 — symptom-checker umbrella, below specific symptom owners.
  ["generic symptom -> stress umbrella", "my axolotl is acting strange", ["/health/stress-signs/"], []],
  ["generic symptom -> checker tool", "something is wrong with my axolotl", ["/health/stress-signs/", "/tools/symptom-checker/"], []],
  ["specific symptom keeps owner", "my axolotl won't eat", ["/health/refusing-to-eat/"], ["/health/stress-signs/"]],
  ["specific symptom keeps owner (float)", "my axolotl is floating a lot", ["/health/why-axolotl-floating/"], ["/health/stress-signs/"]],
  ["white spots -> fungus owner", "my axolotl has white spots", ["/health/fungal-infections-saprolegnia/"], ["/health/stress-signs/"]],
  // Fix 4 — fasting alias vs medical refusal precedence.
  ["fasting month -> fasting page", "no food for a month axolotl", ["/diet/fasting-and-vacation/"], ["/health/refusing-to-eat/"]],
  ["medical refusal beats fasting alias", "my axolotl is not eating", ["/health/refusing-to-eat/"], ["/diet/fasting-and-vacation/"]],
  // Fix 5 — typo aliases documented in Phase 10. "axe"/"bamboo"/"lottl"
  // should salvage to axolotl results (a topic guide), never junk/gifting.
  ["axe -> axolotl", "axe", ["/axolotls/care-guide/", "/care-basics/", "/health/"], ["/gifts-and-merch/", "/joke/"]],
  ["bamboo -> axolotl", "bamboo", ["/axolotls/care-guide/", "/care-basics/", "/health/"], ["/gifts-and-merch/", "/joke/"]],
  ["lottl -> axolotl", "lottl", ["/axolotls/care-guide/", "/care-basics/", "/health/"], ["/gifts-and-merch/", "/joke/"]],
  // Regression guards on Phase 10 core.
  ["flake still", "flake", ["/morphs/leucistic/"], []],
  ["fungus still", "white fungus on axolotl", ["/health/fungal-infections-saprolegnia/"], []],
  ["symptom checker tool still", "symptom checker", ["/tools/symptom-checker/"], []],
];

let failed = 0;
for (const [name, q, wanted, forbidden] of checks) {
  const r = rank(q);
  const top5 = r.urls.slice(0, 5);
  const has = (u) => top5.some(x => x === u || x.startsWith(u));
  const okWant = wanted.some(has);
  const okForbid = !forbidden.some(u => r.urls[0] === u);
  const pass = okWant && okForbid;
  if (!pass) failed++;
  console.log(`[${pass ? "PASS" : "FAIL"}] ${name}: "${q}" (eff: ${r.effective})\n        top: ${top5.join(", ") || "(none)"}`);
}
if (failed) {
  console.log(`\n${failed}/${checks.length} Phase 11 assertions FAILED`);
  process.exit(1);
}
console.log(`\nall ${checks.length} Phase 11 smoke assertions passed`);