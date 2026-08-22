/*
 * Phase 10 search smoke test — a faithful port of public/js/search.js
 * scoring/routing (scoreItem, phraseBoost, applySemantic, limitFamilies,
 * clusterFallback, fixTypos) executed against the built search-index.json.
 *
 * Usage: node build/phase10_search_smoke.mjs
 * Exit 0 = every assertion passes.
 */
import fs from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";

const here = path.dirname(fileURLToPath(import.meta.url));
const BASE = path.dirname(here);
const SITE = "https://axolotlcare.example.com";

// ---- verbatim port of search.js helpers ----
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
  var out = [word];
  if (word.length > 3 && word.slice(-1) === "s") out.push(word.slice(0, -1));
  return out;
}
function countTerms(termList, haystack) {
  var n = 0;
  termList.forEach(function (word) {
    var hit = false;
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
  var qn = normalize(query);
  var boost = 0;
  SYNONYMS.forEach(function (entry) {
    var triggered = false;
    entry.q.forEach(function (variant) {
      if (!triggered && qn.indexOf(normalize(variant)) !== -1) triggered = true;
    });
    if (!triggered) return;
    var titleN = normalize(item.title);
    var hay = function (s) { return normalize(s); };
    entry.hits.forEach(function (phrase) {
      var p = normalize(phrase);
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
  var qn = normalize(query);
  for (var i = 0; i < phrases.length; i++) {
    if (qn.indexOf(normalize(phrases[i])) !== -1) return true;
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
  for (var i = 0; i < FAMILIES.length; i++) {
    if (matchesAny(query, FAMILIES[i].triggers)) return FAMILIES[i];
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
  var m = a.length, n = b.length;
  var row = new Array(n + 1);
  for (var j = 0; j <= n; j++) row[j] = j;
  for (var i = 1; i <= m; i++) {
    var prev = row[0];
    row[0] = i;
    for (var j = 1; j <= n; j++) {
      var tmp = row[j];
      row[j] = Math.min(row[j] + 1, row[j - 1] + 1, prev + (a[i - 1] === b[j - 1] ? 0 : 1));
      prev = tmp;
    }
  }
  return row[n];
}
function fixTypos(query) {
  var terms = tokenize(query);
  if (terms.length > 1) return query;
  var word = terms[0];
  if (TYPO_MAP[word]) return TYPO_MAP[word];
  var best = null, bestD = 3;
  KNOWN_WORDS.forEach(function (k) {
    var d = editDistance(word, k);
    if (d <= 2 && d < bestD) { bestD = d; best = k; }
  });
  return best || query;
}

function applySemantic(scores, query) {
  var byUrl = {};
  scores.forEach(function (s) { byUrl[s.item.url] = s; });
  var family = familyFor(query);
  if (family) {
    var canon = byUrl[family.canonical];
    if (canon) canon.score += (family.boost || 12);
    if (family.demoteHubs) {
      scores.forEach(function (s) {
        if (s.item.role === "hub" && s.item.url !== family.canonical) s.score -= 18;
      });
    }
  }
  if (family && family.key === "cooling") {
    if (matchesAny(query, ["chiller", "buy", "which chiller", "price"])) {
      var ch = byUrl["/tank-setup/aquarium-chillers/"];
      if (ch) ch.score += 10;
    }
  }
  if (matchesAny(query, ["regeneration", "regrow"])) {
    if (matchesAny(query, ["science", "how does", "why does", "biology"])) {
      var bio = byUrl["/biology-and-science/regeneration-and-limb-regrowth/"];
      if (bio) bio.score += 8;
    }
  }
  TROUBLE_ROUTES.forEach(function (r) {
    if (matchesAny(query, r.tokens)) {
      var t = byUrl[r.url];
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
      var tool = byUrl["/tools/" + r.slug + "/"];
      if (tool) tool.score += 10;
    }
  });
}

function familyMembers(family) {
  if (family.key === "care") return ["/axolotls/care-guide/", "/axolotls/"];
  if (family.key === "stress") return ["/health/stress-signs/", "/health/curled-gills-stress-signal/", "/health/why-axolotl-floating/"];
  if (family.key === "fasting") return ["/diet/fasting-and-vacation/", "/diet/feeding-schedule-by-age/", "/health/refusing-to-eat/"];
  if (family.key === "fungus") return ["/health/fungal-infections-saprolegnia/", "/health/black-tea-bath/", "/health/salt-bath/"];
  if (family.key === "impaction") return ["/health/impaction-symptoms-treatment/", "/diet/overfeeding-and-impaction/",
    "/tank-setup/substrate-and-impaction/", "/tank-setup/gravel-risks/"];
  if (family.key === "filter") return ["/tank-setup/filtration-for-axolotls/", "/tank-setup/canister-vs-sponge-filter/"];
  if (family.key === "cooling") return ["/tank-setup/temperature/", "/tank-setup/aquarium-chillers/"];
  if (family.key === "price") return ["/cost-and-buying/axolotl-price-by-morph/"];
  if (family.key === "budget") return ["/care-basics/cost-of-ownership-monthly/"];
  if (family.key === "regeneration") return ["/health/limb-regeneration/", "/biology-and-science/regeneration-and-limb-regrowth/"];
  return [];
}
function limitFamilies(scored, query) {
  var family = familyFor(query);
  if (!family) return scored;
  var memberSet = {};
  familyMembers(family).forEach(function (u) { memberSet[u] = true; });
  var out = [], deferred = [], familySeen = 0;
  for (var i = 0; i < scored.length; i++) {
    var url = scored[i].item.url;
    if (memberSet[url]) {
      if (familySeen < 2) { familySeen += 1; out.push(scored[i]); }
      else deferred.push(scored[i]);
    } else {
      out.push(scored[i]);
    }
  }
  return out.concat(deferred);
}

function scoreItem(item, query, terms) {
  var titleNorm = normalize(item.title);
  var titleTerms = tokenize(item.title);
  var score = 0;
  if (titleNorm.indexOf(query) !== -1) score += 60;
  if (terms.length > 1 && countTerms(terms, titleNorm) === terms.length) score += 30;
  var titleHit = countTerms(terms, titleNorm);
  score += titleHit * 8;
  var catNorm = normalize(item.category || "");
  if (countTerms(terms, catNorm) > 0) score += 5 * countTerms(terms, catNorm);
  var clName = normalize((item.cluster || "").replace(/[-_]/g, " "));
  if (clName && countTerms(terms, clName) > 0) score += 3 * countTerms(terms, clName);
  var headingHit = 0;
  (item.headings || []).forEach(function (h) {
    if (countTerms(terms, normalize(h)) > 0) headingHit += 1;
  });
  score += Math.min(headingHit, 3) * 4;
  if (countTerms(terms, normalize(item.dek || "")) > 0) score += 3;
  var body = normalize(item.text || "");
  var bodyHits = 0;
  body.split("\n").filter(Boolean).forEach(function (p) {
    var c = countTerms(terms, p);
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

function clusterFallback(terms, index) {
  var hubs = index.filter(function (it) { return it.role === "hub"; });
  var bestHub = null, bestN = 0;
  hubs.forEach(function (h) {
    var n = countTerms(terms, normalize(h.title + " " + (h.category || "")));
    if (n > bestN) { bestN = n; bestHub = h; }
  });
  if (!bestHub) return [];
  var cluster = bestHub.cluster;
  return index.filter(function (it) { return it.cluster === cluster; })
    .sort(function (a, b) { return (a.title || "").localeCompare(b.title || ""); })
    .slice(0, 4);
}

// ---- run one query through the exact search.js pipeline ----
const index = JSON.parse(fs.readFileSync(path.join(BASE, "public", "search-index.json"), "utf-8"))
  .filter(it => it && it.title && it.url && it.url !== SITE + "/");

function rank(query) {
  var effectiveQuery = fixTypos(query);
  var effectiveTerms = tokenize(effectiveQuery);
  var scored = [];
  index.forEach(function (item) {
    var s = scoreItem(item, effectiveQuery, effectiveTerms);
    if (s > 0) scored.push({ item, score: s });
  });
  applySemantic(scored, effectiveQuery);
  scored.sort(function (a, b) {
    if (b.score !== a.score) return b.score - a.score;
    return a.item.title.localeCompare(b.item.title);
  });
  scored = limitFamilies(scored, effectiveQuery);
  var items = scored.slice(0, 20).map(s => s.item);
  if (!items.length) items = clusterFallback(effectiveTerms, index);
  return { urls: items.map(i => i.url.replace(SITE, "")), effective: effectiveQuery, items };
}

const checks = [
  ["flake (typo->leucistic)", "flake", "/morphs/leucistic/"],
  ["curled gills", "curled gills", "/health/curled-gills-stress-signal/"],
  ["won't eat", "my axolotl won't eat", "/health/refusing-to-eat/"],
  ["not eating", "not eating", "/health/refusing-to-eat/"],
  ["conditioner dosage", "water conditioner dosage calculator", "/tools/water-conditioner-dosage-calculator/"],
  ["symptom checker", "symptom checker", "/tools/symptom-checker/"],
  ["price", "how much does an axolotl cost", "/cost-and-buying/axolotl-price-by-morph/"],
  ["impaction", "axolotl impaction", "/health/impaction-symptoms-treatment/"],
  ["float troubleshooting", "why is my axolotl floating", "/health/why-axolotl-floating/"],
  ["budget family", "monthly cost of owning an axolotl", "/care-basics/cost-of-ownership-monthly/"],
  ["fasting", "fasting axolotl", "/diet/fasting-and-vacation/"],
  ["fungus", "white fungus on axolotl", "/health/fungal-infections-saprolegnia/"],
  ["stress pillar", "stress signs", "/health/stress-signs/", "/axolotls/care-guide/"],
  ["science regen", "regeneration science", "/biology-and-science/regeneration-and-limb-regrowth/"],
  ["limb regrow", "how do axolotls regrow limbs", "/health/limb-regeneration/"],
  ["cooling", "water too warm", "/tank-setup/temperature/", "/axolotls/care-guide/"],
  ["chiller purchase", "best chiller", "/tank-setup/aquarium-chillers/"],
  ["best filter", "best filter", "/tank-setup/filtration-for-axolotls/"],
  ["emergency", "emergency", "/health/emergency-first-aid/"],
  ["find vet", "find a vet", "/health/finding-an-exotic-vet/"],
];

let failed = 0;
for (const [name, q, first, notFirst] of checks) {
  const r = rank(q);
  const top5 = r.urls.slice(0, 5).join(", ") || "(none)";
  const okFirst = r.urls[0] === first;
  const okNot = notFirst ? r.urls[0] !== notFirst : true;
  const pass = okFirst && okNot;
  if (!pass) failed++;
  console.log(`[${pass ? "PASS" : "FAIL"}] ${name}: "${q}" (eff: ${r.effective})\n        top: ${top5}`);
}
if (failed) {
  console.log(`\n${failed}/${checks.length} assertions FAILED`);
  process.exit(1);
}
console.log(`\nall ${checks.length} smoke assertions passed`);
