/* Axolotl Care Guide — site-wide search (Phase 6)
 *
 * Architecture: client-side search over the build-generated search-index.json.
 * No external search service, no database, no dependencies.
 *
 * Ranking (highest first):
 *   1. exact phrase in title
 *   2. complete query terms in title
 *   3. title word matches
 *   4. category match
 *   5. heading (H1/H2/H3) matches
 *   6. dek / summary matches
 *   7. body text matches
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

    // 4. category match
    var catNorm = normalize(item.category || "");
    if (countTerms(terms, catNorm) > 0) { score += 6 * countTerms(terms, catNorm); }

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

    var meta = document.createElement("div");
    meta.className = "search-result-meta";
    meta.textContent = item.type === "tool" ? "Tool" : item.category;
    li.appendChild(meta);

    var title = document.createElement("h3");
    var link = document.createElement("a");
    link.href = item.url;
    link.tabIndex = 0;
    highlightTerms(link, item.title, terms);
    title.appendChild(link);
    li.appendChild(title);

    var p = document.createElement("p");
    p.className = "search-result-snippet";
    highlightTerms(p, buildExcerpt(item, terms), terms);
    li.appendChild(p);

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

    statusEl.textContent = items.length + (items.length === 1 ? " result" : " results");
    statusEl.hidden = false;

    var ol = document.createElement("ol");
    ol.className = "search-results-list";
    items.forEach(function (item) { ol.appendChild(resultItem(item, terms)); });
    resultsEl.innerHTML = "";
    resultsEl.appendChild(ol);
    resultsEl.hidden = false;
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

      var scored = [];
      index.forEach(function (item) {
        var s = scoreItem(item, query, terms);
        if (s > 0) { scored.push({ item: item, score: s }); }
      });

      // Deterministic sort: score desc, then title asc.
      scored.sort(function (a, b) {
        if (b.score !== a.score) { return b.score - a.score; }
        return a.item.title.localeCompare(b.item.title);
      });

      var items = scored.slice(0, MAX_RESULTS).map(function (s) { return s.item; });
      renderResults(items, terms);

      // Analytics preparation — future analytics can subscribe to this event.
      window.dispatchEvent(new CustomEvent("site_search", {
        detail: {
          query: query,
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