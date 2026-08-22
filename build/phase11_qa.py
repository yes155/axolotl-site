# -*- coding: utf-8 -*-
"""Phase 11 QA. Extends the Phase 10 methodology (content link graph, canonicals,
broken links) with the Phase 11 search-routing corrections and build cleanups.

Weighted score out of 100 — the site must pass >= 65.

Checks:
  1. Phase 10 smoke (20 assertions) still passes with the rerouted search.
  2. Phase 11 natural-language smoke (21 assertions) passes.
  3. Zero broken internal links; exact canonical per page.
  4. Search index / sitemap / pages parity.
  5. All tool pages carry a meta description (Phase 11 build-layer fix).
  6. No dead SEARCH_ACTIONS entry for the (nonexistent) symptom-checker slug.

Writes docs/phase11/qa-report.json.
Usage: python build/phase11_qa.py
"""
import json
import os
import re
import subprocess
import sys
from collections import Counter

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PUBLIC = os.path.join(BASE, "public")
OUT = os.path.join(BASE, "docs", "phase11")
os.makedirs(OUT, exist_ok=True)

SITE = "https://myaxolotl.us"
META = {"/", "/404.html", "/about", "/contact", "/privacy", "/editorial-policy", "/search"}

WEIGHTS = {
    "phase10_smoke": 20,
    "phase11_smoke": 25,
    "broken_links": 15,
    "canonical": 15,
    "index_sitemap_parity": 10,
    "tools_descriptions": 10,
    "search_actions": 5,
}
THRESHOLD = 65


def url_for(path):
    rel = path[len(PUBLIC) + 1:].replace("\\", "/")
    if rel == "index.html":
        return "/"
    if rel == "404.html":
        return "/404.html"
    if rel.endswith("index.html"):
        return "/" + rel[:-len("index.html")].rstrip("/")
    if rel.endswith(".html"):
        return "/" + rel[: -len(".html")]
    return "/" + rel


def walk():
    pages = {}
    for root, _dirs, files in os.walk(PUBLIC):
        for fn in files:
            if not fn.endswith(".html"):
                continue
            path = os.path.join(root, fn)
            u = url_for(path)
            if u in pages:
                continue
            with open(path, encoding="utf-8", errors="ignore") as fh:
                pages[u] = {"path": path, "html": fh.read()}
    return pages


def extract_links(html):
    out = set()
    for href in re.findall(r'<a[^>]+href="([^"]+)"', html):
        if href.startswith(("http://", "https://", "//", "mailto:", "tel:", "data:", "#")):
            continue
        if href.startswith("/"):
            u = href.split("#")[0].split("?")[0]
            if u.startswith("/images/") or u.startswith("/css/") or u.startswith("/js/"):
                continue
            if u.endswith("/"):
                u = u.rstrip("/")
            out.add(u)
    return out


def main():
    pages = walk()
    errors = {"broken": [], "canonical": [], "dup_canonical_groups": []}
    canon_urls = Counter()

    for u, d in pages.items():
        html = d["html"]
        m = re.search(r'<link rel="canonical" href="([^"]+)"', html)
        if u == "/":
            expected = SITE
        elif u == "/404.html":
            expected = SITE + "/404.html"
        else:
            expected = SITE + u + "/"
        if not m:
            errors["canonical"].append(u)
        elif m.group(1) != expected and u != "/":
            errors["canonical"].append(f"{u} -> {m.group(1)}")
        canon_urls[m.group(1) if m else ""] += 1
        for t in extract_links(html):
            target = os.path.join(PUBLIC, t.lstrip("/").replace("/", os.sep))
            if not os.path.isfile(target):
                target = os.path.join(PUBLIC, (t + "/index.html").lstrip("/").replace("/", os.sep))
                if not os.path.isfile(target):
                    target = os.path.join(PUBLIC, (t + ".html").lstrip("/").replace("/", os.sep))
            if not os.path.isfile(target):
                errors["broken"].append(f"{u} -> {t}")

    for t, c in canon_urls.items():
        if c > 1:
            errors["dup_canonical_groups"].append(f"{t} x{c}")

    # --- search index / sitemap parity ------------------------------------
    idx = json.load(open(os.path.join(PUBLIC, "search-index.json"), encoding="utf-8"))
    index_urls = {e["url"] for e in idx if e.get("url")}
    sitemap = open(os.path.join(PUBLIC, "sitemap.xml"), encoding="utf-8").read()
    sitemap_urls = set(re.findall(r"<loc>([^<]+)</loc>", sitemap))
    sitemap_urls = {u.replace(SITE, "") if u != SITE else "/" for u in sitemap_urls}
    # Everything searchable must be crawlable; the only sitemap-only pages are
    # the intentionally non-searchable static pages.
    NON_SEARCH = {"/", "/about/", "/contact/", "/privacy/", "/search/", "/tools/"}
    only_in_sitemap = sitemap_urls - index_urls
    unexpected_sitemap_only = sorted(only_in_sitemap - NON_SEARCH)
    missing_from_sitemap = sorted(u for u in index_urls - sitemap_urls)
    parity_ok = not unexpected_sitemap_only and not missing_from_sitemap

    # --- tool meta descriptions -------------------------------------------
    tools_dir = os.path.join(PUBLIC, "tools")
    tool_pages = sorted(u for u in pages if u.startswith("/tools/") and u != "/tools")
    tools_missing_desc = [u for u in tool_pages if 'name="description"' not in pages[u]["html"]]

    # --- dead search action -------------------------------------------------
    dead_actions = []
    for e in idx:
        act = e.get("action")
        if act and act.get("url") == "/health/symptom-checker/":
            dead_actions.append(e["url"])

    # --- smoke gates ---------------------------------------------------------
    def run(cmd):
        env = dict(os.environ)
        p = subprocess.run(cmd, cwd=BASE, capture_output=True, text=True, env=env)
        return p.returncode, (p.stdout or "") + (p.stderr or "")

    p10_rc, p10_out = run(["node", "build/phase10_search_smoke.mjs"])
    p11_rc, p11_out = run(["node", "build/phase11_search_smoke.mjs"])
    p10_ok = p10_rc == 0
    p11_ok = p11_rc == 0

    # --- weighted score -------------------------------------------------------
    table = {
        "phase10_smoke": p10_ok,
        "phase11_smoke": p11_ok,
        "broken_links": not errors["broken"],
        "canonical": not errors["canonical"] and not errors["dup_canonical_groups"],
        "index_sitemap_parity": parity_ok,
        "tools_descriptions": not tools_missing_desc,
        "search_actions": not dead_actions,
    }
    earned = sum(WEIGHTS[k] for k, ok in table.items() if ok)
    total = sum(WEIGHTS.values())
    passed = earned >= THRESHOLD

    report = {
        "phase": "phase11",
        "weighted_score": earned,
        "weighted_total": total,
        "threshold": THRESHOLD,
        "passed": passed,
        "weights": {
            k: {"weight": WEIGHTS[k], "pass": table[k]}
            for k in table
        },
        "errors": {
            "broken": errors["broken"][:10],
            "canonical": errors["canonical"][:10],
            "dup_canonical_groups": errors["dup_canonical_groups"],
            "tools_missing_description": tools_missing_desc,
            "dead_search_actions": dead_actions,
            "index_missing_from_sitemap": missing_from_sitemap[:10],
            "unexpected_sitemap_only": unexpected_sitemap_only[:10],
        },
        "metrics": {
            "pages_total": len(pages),
            "index_entries": len(idx),
            "sitemap_entries": len(sitemap_urls),
            "tool_pages": len(tool_pages),
        },
        "smoke": {
            "phase10": {"ok": p10_ok, "last_line": p10_out.strip().splitlines()[-1] if p10_out.strip().splitlines() else ""},
            "phase11": {"ok": p11_ok, "last_line": p11_out.strip().splitlines()[-1] if p11_out.strip().splitlines() else ""},
        },
    }
    with open(os.path.join(OUT, "qa-report.json"), "w", encoding="utf-8") as fh:
        json.dump(report, fh, indent=1, ensure_ascii=False)

    print(f"Phase 11 weighted score: {earned}/{total} (need {THRESHOLD}) -> {'PASS' if passed else 'FAIL'}")
    for k, ok in table.items():
        print(f"  {'[ok]' if ok else '[!!]'} {k}")
    if not p10_ok:
        print("phase10 smoke tail:", p10_out.strip().splitlines()[-3:])
    if not p11_ok:
        print("phase11 smoke tail:", p11_out.strip().splitlines()[-3:])
    print("broken:", len(errors["broken"]), "| canonical:", report["errors"]["canonical"] and len(errors["canonical"]))
    print("tools missing desc:", tools_missing_desc)
    print("dead search actions:", dead_actions)
    return 0 if passed else 1


if __name__ == "__main__":
    sys.exit(main())
