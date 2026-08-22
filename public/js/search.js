/*
 * Axolotl Care Guide — site-wide search (Phase 6, upgraded Phase 9, Phase 10)
 *
 * Architecture: client-side search over the build-generated search-index.json.
 * No external search service, no database, no dependencies.
 *
 * Index schema (search-index.json):
 *   { title, url, type, role, cluster, category, dek, headings, text, action? }
 *   - text is the article body only (nav/footer/template never indexed)
 *   - cluster + role let ranking understand the site's content structure
 *   - action (Phase 10) carries an explicit action button (tools, emergency, vet)
 *
 * Ranking (highest first):
 *   1. exact phrase in title
 *   2. complete query terms in title
 *   3. title word matches
 *   4. category / cluster-name match (content-structure signal)
 *   5. heading (H1/H2/H3) matches
 *   6. dek / summary matches
 *   7. body text matches (paragraph level, dense hits win)
 *
 * Phase 10 (Phase 9-B) layer on top of pure scoring:
 *   - intent-aware routing (canonical owner per family: care, stress, fasting,
 *     fungus, impaction, filter, cooling, price, budget, regeneration)
 *   - troubleshooting deep-link routing (curl, floating, refusal, ...)
 *   - vet / emergency enrichment and action chips
 *   - calculator capture (tool action buttons)
 *   - empty-result cluster fallback
 *   - typo salvage (edit distance on known terms)
 *
 * Security: all query text is rendered via textContent/createElement — never
 * innerHTML with raw user input.
 */
(function () {
  "use strict";

  var INDEX_URL = "/search-index.json";
  var MAX_RESULTS = 20;

  var form = document.getElementById("search-form");
  var input = document.getElementById("search-input");
  var statusEl = document.getElementById("search-status");
  var emptyEl = document.getElementById("search-empty");
  var resultsEl = document.getElementById("search-results");
  var nullEl = document.getElementById("search-null");
  var nullTitle = document.getElementById("search-null-title");

  // ---------------------------------------------------------------------------
  // Query normalization
  // ---------------------------------------------------------------------------
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

  // Basic singular/plural handling: treat "axolotl" and "axolotls" as the
  // same term by also matching the word minus a trailing "s".
  function stems(word) {
    var out = [word];
    if (word.length > 3 && word.slice(-1) === "s") {
      out.push(word.slice(0, -1));
    }
    return out;
  }

  function tokensMatch(a, b) {
    var sa = {};
    a.forEach(function (w) { stems(w).forEach(function (s) { sa[s] = 1; }); });
    var sb = {};
    b.forEach(function (w) { stems(w).forEach(function (s) { sb[s] = 1; }); });
    for (var k in sa) { if (sb[k]) { return true; } }
    return false;
  }

  // ---------------------------------------------------------------------------
  // Index
  // ---------------------------------------------------------------------------
  var index = null;
  var indexByName = null; // normalized title -> item (for autocomplete/dedup)

  function loadIndex() {
    if (index) { return Promise.resolve(index); }
    return fetch(INDEX_URL, { headers: { Accept: "application/json" } })
      .then(function (r) {
        if (!r.ok) { throw new Error("HTTP " + r.status); }
        return r.json();
      })
      .then(function (data) {
        index = data.filter(function (it) {
          return it && it.title && it.url;
        });
        indexByName = {};
        index.forEach(function (it) {
          var key = normalize(it.title);
          if (!(key in indexByName)) { indexByName[key] = it; }
        });
        return index;
      })
      .catch(function (err) {
        statusEl.textContent = "Search is temporarily unavailable. Please try again later.";
        statusEl.hidden = false;
        if (emptyEl) { emptyEl.hidden = false; }
        return null;
      });
  }

  // ---------------------------------------------------------------------------
  // Scoring
  // ---------------------------------------------------------------------------
  function countTerms(termList, haystack) {
    var n = 0;
    termList.forEach(function (word) {
      var hit = false;
      stems(word).forEach(function (s) {
        if (haystack.indexOf(s) !== -1) { hit = true; }
      });
      if (hit) { n += 1; }
    });
    return n;
  }

  // ---------------------------------------------------------------------------
  // Alias / phrase layer — helps normal conversational queries reach the page
  // whose content actually answers them, even when the query wording differs
  // from the title (e.g. "not eating" -> "refusing to eat").
  // ---------------------------------------------------------------------------
  var SYNONYMS = [
    { q: ["not eating", "wont eat", "won't eat", "stopped eating", "refusing food", "not hungry"],
      hits: ["refusing to eat", "not eating", "refusing food"] },
    { q: ["not pooping", "not pooping", "not pooping", "constipated"],
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
        if (!triggered && qn.indexOf(normalize(variant)) !== -1) { triggered = true; }
      });
      if (!triggered) { return; }

      var titleN = normalize(item.title);
      var hay = function (s) { return normalize(s); };
      entry.hits.forEach(function (phrase) {
        var p = normalize(phrase);
        if (titleN.indexOf(p) !== -1) { boost += 22; return; }
        (item.headings || []).forEach(function (h) {
          if (hay(h).indexOf(p) !== -1) { boost += 10; }
        });
        if (hay(item.dek || "").indexOf(p) !== -1) { boost += 7; }
        if (hay(item.text || "").indexOf(p) !== -1) { boost += 3; }
      });
    });
    return Math.min(boost, 44);
  }

  // ---------------------------------------------------------------------------
  // Phase 10 / Phase 9-B — semantic routing over the scored result set
  // ---------------------------------------------------------------------------
  function matchesAny(query, phrases) {
    var qn = normalize(query);
    for (var i = 0; i < phrases.length; i++) {
      if (qn.indexOf(normalize(phrases[i])) !== -1) { return true; }
    }
    return false;
  }

  // Dedupe families: for each, `canonical` OWNS the dominant intent. When the
  // family triggers, the canonical is promoted; hubs in the family are demoted.
  var FAMILIES = [
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
      if (matchesAny(query, FAMILIES[i].triggers)) { return FAMILIES[i]; }
    }
    return null;
  }

  // Troubleshooting deep links: "which page wins" for symptom-state queries.
  var TROUBLE_ROUTES = [
    { tokens: ["curled", "curl"], url: "/health/curled-gills-stress-signal/" },
    { tokens: ["floating", "float", "buoy"], url: "/health/why-axolotl-floating/" },
    { tokens: ["not eating", "wont eat", "won't eat", "refusing"], url: "/health/refusing-to-eat/" },
    { tokens: ["red leg", "red leg syndrome"], url: "/health/red-leg-syndrome/" },
    { tokens: ["ammonia burn", "burned gills"], url: "/health/ammonia-burns/" },
  ];

  // Vet / emergency enrichment. Strong distress words boost hard; "help" is
  // gated so it only fires alongside a health/symptom/the-pet context, keeping
  // informational "help with X" queries from being hijacked.
  var URGENT_STRONG = ["emergency", "urgent", "dying"];
  var VET_STRONG = ["vet", "veterinarian"];
  var HELP_CONTEXT = ["my axolotl", "symptom", "dying", "emergency", "urgent", "vet",
    "veterinarian", "sick", "ill", "hurt", "not eating", "wont eat", "won't eat",
    "refusing", "floating", "curled", "fungus", "ammonia", "burn", "impaction",
    "stressed", "strange", "wrong"];

  // Calculator capture: tool slug -> trigger phrases (mutually exclusive).
  var TOOL_ROUTES = [
    { slug: "water-conditioner-dosage-calculator", tokens: ["dose", "how much conditioner", "calculator"] },
    { slug: "tank-size-calculator", tokens: ["sizing", "size tank", "what size", "how big"] },
    { slug: "feeding-schedule-generator", tokens: ["feeding schedule", "schedule generator"] },
    { slug: "nitrogen-cycle-tracker", tokens: ["cycle tracker", "track cycle", "tracker"] },
    { slug: "symptom-checker", tokens: ["symptom checker", "checker"] },
  ];

  var KNOWN_WORDS = ["leucistic", "melanoid", "albino", "golden", "axolotl", "saprolegnia",
    "impaction", "morph", "fungus", "chiller", "cannister", "water"];
  var TYPO_MAP = { flake: "leucistic", melaniod: "melanoid", alby: "albino", lucy: "leucistic",
    axololt: "axolotl", axolotll: "axolotl", axe: "axolotl", bamboo: "axolotl",
    lottl: "axolotl", groom: "frog", "cannister": "canister" };

  function editDistance(a, b) {
    var m = a.length, n = b.length;
    var row = new Array(n + 1);
    for (var j = 0; j <= n; j++) { row[j] = j; }
    for (var i = 1; i <= m; i++) {
      var prev = row[0];
      row[0] = i;
      for (var j = 1; j <= n; j++) {
        var tmp = row[j];
        row[j] = Math.min(row[j] + 1, row[j - 1] + 1,
          prev + (a[i - 1] === b[j - 1] ? 0 : 1));
        prev = tmp;
      }
    }
    return row[n];
  }

  function fixTypos(query) {
    var terms = tokenize(query);
    if (terms.length > 1) { return query; }
    var word = terms[0];
    if (TYPO_MAP[word]) { return TYPO_MAP[word]; }
    var best = null, bestD = 3;
    KNOWN_WORDS.forEach(function (k) {
      var d = editDistance(word, k);
      if (d <= 2 && d < bestD) { bestD = d; best = k; }
    });
    return best || query;
  }

  // Promote/demote scores by semantic intent before the final sort.
  function applySemantic(scores, query, terms) {
    var byUrl = {};
    scores.forEach(function (s) { byUrl[s.item.url] = s; });

    var family = familyFor(query);
    if (family) {
      var canon = byUrl[family.canonical];
      if (canon) { canon.score += (family.boost || 12); }
      if (family.demoteHubs) {
        scores.forEach(function (s) {
          if (s.item.role === "hub" && s.item.url !== family.canonical) { s.score -= 18; }
        });
      }
    }

    // Cooling nuance: "chiller"/"which chiller"/"buy" is a purchase query and
    // belongs to the chiller comparison, not the husbandry pillar.
    if (family && family.key === "cooling") {
      if (matchesAny(query, ["chiller", "buy", "which chiller", "price"])) {
        var ch = byUrl["/tank-setup/aquarium-chillers/"];
        if (ch) { ch.score += 10; }
      }
    }

    // Science-redirects regeneration to the biology page.
    if (matchesAny(query, ["regeneration", "regrow"])) {
      if (matchesAny(query, ["science", "how does", "why does", "biology"])) {
        var bio = byUrl["/biology-and-science/regeneration-and-limb-regrowth/"];
        if (bio) { bio.score += 8; }
      }
    }

    TROUBLE_ROUTES.forEach(function (r) {
      if (matchesAny(query, r.tokens)) {
        var t = byUrl[r.url];
        if (t) { t.score += 9; }
      }
    });

    // Emergency / vet enrichment (Phase 11): strong distress words boost the
    // first-aid and vet pages hard; "help" alone (or in a non-health context
    // like "help with tank setup") does not. Curated tools still capture above.
    var ev = byUrl["/health/emergency-first-aid/"];
    var vet = byUrl["/health/finding-an-exotic-vet/"];
    var evStrong = matchesAny(query, URGENT_STRONG);
    var vetStrong = matchesAny(query, VET_STRONG);
    if (evStrong && ev) { ev.score += 30; }
    if (vetStrong && vet) { vet.score += 30; }
    // Cross-enrichment: an emergency query also surfaces the vet page (and
    // vice-versa) as the actionable next step, but more softly than the owner.
    if (evStrong && vet) { vet.score += 10; }
    if (vetStrong && ev) { ev.score += 10; }
    if (matchesAny(query, ["help"]) && matchesAny(query, HELP_CONTEXT)) {
      if (ev) { ev.score += 14; }
      if (vet) { vet.score += 14; }
    }

    // Symptom-checker style "my axolotl is/has..." phrasing points the owner
    // at the stress umbrella and the symptom-checker tool. It deliberately
    // scores below the specific TROUBLE_ROUTES (+9) so "won't eat" still wins
    // on /health/refusing-to-eat/, etc.
    if (matchesAny(query, ["my axolotl is", "my axolotl has", "my axolotl seems",
                           "my axolotl acting", "something is wrong"])) {
      var stress = byUrl["/health/stress-signs/"];
      var checker = byUrl["/tools/symptom-checker/"];
      if (stress) { stress.score += 12; }
      if (checker) { checker.score += 12; }
    }

    TOOL_ROUTES.forEach(function (r) {
      if (matchesAny(query, r.tokens)) {
        var tool = byUrl["/tools/" + r.slug + "/"];
        if (tool) { tool.score += 10; }
      }
    });
  }

  // Cap duplicates within one family: the canonical owner plus one
  // role-differentiated runner-up stay native; further family members defer.
  function limitFamilies(scored, query) {
    var family = familyFor(query);
    if (!family) { return scored; }
    var members = familyMembers(family).map(function (u) { return u; });
    var memberSet = {};
    members.forEach(function (u) { memberSet[u] = true; });
    var out = [];
    var deferred = [];
    var familySeen = 0;
    for (var i = 0; i < scored.length; i++) {
      var url = scored[i].item.url;
      if (memberSet[url]) {
        if (familySeen < 2) { familySeen += 1; out.push(scored[i]); }
        else { deferred.push(scored[i]); }
      } else {
        out.push(scored[i]);
      }
    }
    return out.concat(deferred);
  }

  function familyMembers(family) {
    if (family.key === "care") {
      return ["/axolotls/care-guide/", "/axolotls/"];
    }
    if (family.key === "stress") {
      return ["/health/stress-signs/", "/health/curled-gills-stress-signal/", "/health/why-axolotl-floating/"];
    }
    if (family.key === "fasting") {
      return ["/diet/fasting-and-vacation/", "/diet/feeding-schedule-by-age/", "/health/refusing-to-eat/"];
    }
    if (family.key === "fungus") {
      return ["/health/fungal-infections-saprolegnia/", "/health/black-tea-bath/", "/health/salt-bath/"];
    }
    if (family.key === "impaction") {
      return ["/health/impaction-symptoms-treatment/", "/diet/overfeeding-and-impaction/",
              "/tank-setup/substrate-and-impaction/", "/tank-setup/gravel-risks/"];
    }
    if (family.key === "filter") {
      return ["/tank-setup/filtration-for-axolotls/", "/tank-setup/canister-vs-sponge-filter/"];
    }
    if (family.key === "cooling") {
      return ["/tank-setup/temperature/", "/tank-setup/aquarium-chillers/"];
    }
    if (family.key === "price") { return ["/cost-and-buying/axolotl-price-by-morph/"]; }
    if (family.key === "budget") { return ["/care-basics/cost-of-ownership-monthly/"]; }
    if (family.key === "regeneration") {
      return ["/health/limb-regeneration/", "/biology-and-science/regeneration-and-limb-regrowth/"];
    }
    return [];
  }

  function clusterFallback(terms) {
    // Best hub by term overlap, then top guides from that cluster.
    var hubs = index.filter(function (it) { return it.role === "hub"; });
    var bestHub = null, bestN = 0;
    hubs.forEach(function (h) {
      var n = countTerms(terms, normalize(h.title + " " + (h.category || "")));
      if (n > bestN) { bestN = n; bestHub = h; }
    });
    if (!bestHub) { return []; }
    var cluster = bestHub.cluster;
    return index.filter(function (it) { return it.cluster === cluster; })
      .sort(function (a, b) { return (a.title || "").localeCompare(b.title || ""); })
      .slice(0, 4);
  }

  function scoreItem(item, query, terms) {
    var titleNorm = normalize(item.title);
    var titleTerms = tokenize(item.title);
    var score = 0;

    // 1. exact phrase in title
    if (titleNorm.indexOf(query) !== -1) { score += 60; }

    // 2. all query terms in title
    if (terms.length > 1 && countTerms(terms, titleNorm) === terms.length) {
      score += 30;
    }

    // 3. title word matches (weighted by fraction)
    var titleHit = countTerms(terms, titleNorm);
    score += titleHit * 8;

    // 4. category / cluster-name match (content-structure signal)
    var catNorm = normalize(item.category || "");
    if (countTerms(terms, catNorm) > 0) { score += 5 * countTerms(terms, catNorm); }
    var clName = normalize((item.cluster || "").replace(/[-_]/g, " "));
    if (clName && countTerms(terms, clName) > 0) { score += 3 * countTerms(terms, clName); }

    // 5. heading matches
    var headingHit = 0;
    (item.headings || []).forEach(function (h) {
      if (countTerms(terms, normalize(h)) > 0) { headingHit += 1; }
    });
    score += Math.min(headingHit, 3) * 4;

    // 6. dek / summary matches
    if (countTerms(terms, normalize(item.dek || "")) > 0) { score += 3; }

    // 7. body text matches (paragraph level, prefer dense hits)
    var body = normalize(item.text || "");
    var bodyHits = 0;
    var paragraphs = body.split("\n").filter(Boolean);
    paragraphs.forEach(function (p) {
      var c = countTerms(terms, p);
      if (c > 0) {
        if (c === terms.length) { bodyHits += 3; }
        else { bodyHits += 1; }
      }
    });
    score += Math.min(bodyHits, 6) * 2;

    // Small boost for shorter/exact documents so a title match wins clearly.
    if (score > 0 && titleHit === terms.length) { score += 2; }

    // Alias layer: conversational query phrasing -> canonical content phrase.
    score += phraseBoost(item, query);
    return score;
  }

  // ---------------------------------------------------------------------------
  // Excerpt — pick the query-relevant passage, fall back to dek.
  // ---------------------------------------------------------------------------
  function buildExcerpt(item, terms) {
    var paragraphs = (item.text || "").split("\n").filter(Boolean);
    var best = null;
    for (var i = 0; i < paragraphs.length; i++) {
      var p = paragraphs[i];
      var count = countTerms(terms, normalize(p));
      if (count > 0 && (!best || count > best.count || (count === best.count && p.length < best.len))) {
        best = { text: p, count: count, len: p.length };
      }
    }
    var snippet = best ? best.text : (item.dek || "");
    return truncateSnippet(snippet);
  }

  function truncateSnippet(text) {
    text = String(text || "").replace(/\s+/g, " ").trim();
    if (text.length <= 200) { return text; }
    var cut = text.slice(0, 197);
    var last = cut.lastIndexOf(" ");
    if (last > 80) { cut = cut.slice(0, last); }
    return cut.replace(/[\s,;:]+$/, "") + "\u2026";
  }

  // ---------------------------------------------------------------------------
  // Rendering (textContent only — no innerHTML with user input)
  // ---------------------------------------------------------------------------
  function highlightTerms(node, text, terms) {
    var out = document.createDocumentFragment();
    var remaining = String(text || "");
    while (remaining.length) {
      var bestIdx = -1;
      var bestWord = null;
      for (var i = 0; i < terms.length; i++) {
        stems(terms[i]).forEach(function (s) {
          var idx = remaining.toLowerCase().indexOf(s);
          if (idx !== -1 && (bestIdx === -1 || idx < bestIdx)) {
            bestIdx = idx;
            bestWord = remaining.slice(idx, idx + s.length);
          }
        });
      }
      if (bestIdx === -1) { break; }
      if (bestIdx > 0) {
        out.appendChild(document.createTextNode(remaining.slice(0, bestIdx)));
      }
      var t = document.createElement("strong");
      t.textContent = bestWord;
      out.appendChild(t);
      remaining = remaining.slice(bestIdx + bestWord.length);
    }
    if (remaining.length) {
      out.appendChild(document.createTextNode(remaining));
    }
    node.appendChild(out);
  }

  function resultItem(item, terms) {
    var li = document.createElement("li");
    li.className = "search-result";
    li.setAttribute("role", "listitem");

    var meta = document.createElement("div");
    meta.className = "search-result-meta";
    var roleLabel = item.role === "tool" ? "Tool"
      : item.role === "hub" ? "Topic"
      : (item.category || "Guide");
    meta.textContent = roleLabel;
    li.appendChild(meta);

    var title = document.createElement("h3");
    var link = document.createElement("a");
    link.href = item.url;
    link.className = "search-result-link";
    highlightTerms(link, item.title, terms);
    title.appendChild(link);
    li.appendChild(title);

    var p = document.createElement("p");
    p.className = "search-result-snippet";
    highlightTerms(p, buildExcerpt(item, terms), terms);
    li.appendChild(p);

    var pathEl = document.createElement("div");
    pathEl.className = "search-result-path";
    pathEl.textContent = item.cluster && item.cluster !== "tools"
      ? "/" + item.cluster + (item.url !== "/" + item.cluster + "/" ? item.url.slice(item.cluster.length + 1) : "/")
      : item.url;
    li.appendChild(pathEl);

    if (item.action && item.action.label && item.action.url) {
      var actLink = document.createElement("a");
      actLink.href = item.action.url;
      actLink.className = "search-result-action btn btn-sm";
      actLink.textContent = item.action.kind === "tool" ? "Open tool \u2192" : item.action.label + " \u2192";
      li.appendChild(actLink);
    }

    return li;
  }

  function renderResults(items, terms) {
    emptyEl.hidden = true;
    nullEl.hidden = true;
    if (!items.length) {
      resultsEl.hidden = true;
      statusEl.textContent = "No results found";
      nullTitle.textContent = "No guides found for \u201c" + (input.value || "") + "\u201d";
      nullEl.hidden = false;
      return;
    }

    var q = (input.value || "").trim();
    statusEl.textContent = items.length + (items.length === 1 ? " result" : " results") +
      (q ? " for \u201c" + q + "\u201d" : "");
    statusEl.hidden = false;

    var ol = document.createElement("ol");
    ol.className = "search-results-list";
    ol.setAttribute("role", "list");
    ol.setAttribute("aria-label", "Search results" + (q ? " for " + q : ""));
    items.forEach(function (item) { ol.appendChild(resultItem(item, terms)); });
    resultsEl.innerHTML = "";
    resultsEl.appendChild(ol);
    resultsEl.hidden = false;
    attachResultNav();
  }

  // ---------------------------------------------------------------------------
  // Keyboard navigation across result links (ArrowUp/Down, Home/End)
  // ---------------------------------------------------------------------------
  function attachResultNav() {
    var links = Array.prototype.slice.call(
      document.querySelectorAll(".search-result-link:not([data-nav-bound]), .search-result-action:not([data-nav-bound])")
    );
    if (!links.length) { return; }

    var keydown = function (e) {
      var idx = links.indexOf(document.activeElement);
      var next = -1;
      if (e.key === "ArrowDown") { next = idx + 1; }
      else if (e.key === "ArrowUp") { next = idx - 1; }
      else if (e.key === "Home") { next = 0; }
      else if (e.key === "End") { next = links.length - 1; }
      else { return; }

      e.preventDefault();
      if (next >= 0 && next < links.length) {
        links[next].focus();
      }
    };

    links.forEach(function (l) {
      l.setAttribute("data-nav-bound", "1");
      l.addEventListener("keydown", keydown);
    });
  }

  // ---------------------------------------------------------------------------
  // Search driver
  // ---------------------------------------------------------------------------
  function currentQuery() {
    var sp = new URLSearchParams(window.location.search);
    return normalize(sp.get("q") || "");
  }

  function run(query, pushHistory) {
    if (pushHistory) {
      var sp = new URLSearchParams(window.location.search);
      if (query) { sp.set("q", query); }
      else { sp.delete("q"); }
      var qs = sp.toString();
      history.replaceState(null, "", qs ? "/search/?" + qs : "/search/");
    }

    var terms = tokenize(query);
    if (input && input.value !== query) { input.value = query; }

    if (!query || !terms.length) {
      emptyEl.hidden = false;
      resultsEl.hidden = true;
      nullEl.hidden = true;
      statusEl.textContent = "";
      return;
    }

    loadIndex().then(function () {
      if (!index) { return; }

      var effectiveQuery = fixTypos(query);
      var effectiveTerms = tokenize(effectiveQuery);

      var scored = [];
      index.forEach(function (item) {
        var s = scoreItem(item, effectiveQuery, effectiveTerms);
        if (s > 0) { scored.push({ item: item, score: s }); }
      });

      applySemantic(scored, effectiveQuery, effectiveTerms);

      // Deterministic sort: score desc, then title asc.
      scored.sort(function (a, b) {
        if (b.score !== a.score) { return b.score - a.score; }
        return a.item.title.localeCompare(b.item.title);
      });

      scored = limitFamilies(scored, effectiveQuery);

      var items = scored.slice(0, MAX_RESULTS).map(function (s) { return s.item; });

      // Empty-result cluster fallback: recommend the closest cluster's guides.
      if (!items.length) {
        items = clusterFallback(effectiveTerms);
        if (items.length) {
          statusEl.textContent = "No exact match \u2014 best from \u201c" +
            (items[0].category || "Taxonomy") + "\u201d:";
        }
      }

      renderResults(items, effectiveTerms);

      // Analytics preparation — future analytics can subscribe to this event.
      window.dispatchEvent(new CustomEvent("site_search", {
        detail: {
          query: query,
          effective_query: effectiveQuery,
          result_count: items.length,
        },
      }));
    });
  }

  // ---------------------------------------------------------------------------
  // Wire-up
  // ---------------------------------------------------------------------------
  function init() {
    if (!form || !input) { return; }

    form.addEventListener("submit", function (e) {
      e.preventDefault();
      run(normalize(input.value), true);
      input.blur();
    });

    // Live search as you type is intentionally NOT bound here — the spec asks
    // for a solid results page over an autocomplete app. Enter submits.

    document.addEventListener("keydown", function (e) {
      if (e.key === "Escape" && document.activeElement === input) {
        input.blur();
      }
    });

    // Restore on back/forward navigation.
    window.addEventListener("popstate", function () {
      run(currentQuery(), false);
    });

    // Initial load (refresh / share / deep link with ?q=...).
    if (document.readyState === "loading") {
      document.addEventListener("DOMContentLoaded", function () {
        run(currentQuery(), false);
      });
    } else {
      run(currentQuery(), false);
    }
  }

  init();
})();