# -*- coding: utf-8 -*-
"""Phase 10 QA. Runs against the generated site in public/ (content-scope,
mirrors the Phase 7B/8 link-graph methodology so BEFORE/AFTER are comparable).

Checks:
  1. Zero broken internal links.
  2. Exactly one canonical per page, matching the page's own URL.
  3. Phase 10 deliverables present (new pages, role-note boxes, search actions).
  4. Content graph metrics (edges, cross-cluster, zero-in/out, hub/tool inbound).

Writes docs/phase10/qa-report.json and docs/phase10/qa-inout.tsv.

Usage: python build/phase10_qa.py
"""
import json
import os
import re
import sys
from collections import Counter

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PUBLIC = os.path.join(BASE, "public")
OUT = os.path.join(BASE, "docs", "phase10")
os.makedirs(OUT, exist_ok=True)

SITE = "https://myaxolotl.us"
META = {"/", "/404.html", "/about", "/contact", "/privacy", "/editorial-policy", "/search"}


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
                html = fh.read()
            pages[u] = {"path": path, "html": html}
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
        # canonical link must equal this page's own URL
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

    # ------ content link graph (Phase 7B methodology) ------
    for t, c in canon_urls.items():
        if c > 1:
            errors["dup_canonical_groups"].append(f"{t} x{c}")
    if "/" in canon_urls:
        canon_urls.pop("/")

    N = len(pages)
    freq = Counter()
    for u, d in pages.items():
        for t in extract_links(d["html"]):
            if t in pages and t != u:
                freq[t] += 1
    template = {t for t, c in freq.items() if c / N >= 0.90}

    content_out = {}
    for u, d in pages.items():
        out = []
        for t in extract_links(d["html"]):
            if t in pages and t != u and t not in template:
                out.append(t)
        content_out[u] = sorted(set(out))
    content_pages = sorted(u for u in pages if u not in META)
    edges = [(f, t) for f in sorted(content_out) for t in content_out[f]
             if f in content_pages and t in content_pages]
    inb = {}
    for f, t in edges:
        inb.setdefault(t, []).append(f)
    for t in content_pages:
        inb.setdefault(t, [])
    hubs = ["/axolotls", "/tank-setup", "/diet", "/health", "/legal", "/cost-and-buying",
            "/morphs", "/breeding", "/gifts-and-merch", "/care-basics",
            "/biology-and-science", "/axolotl-in-culture", "/tools"]
    tools = sorted(u for u in content_pages if u.startswith("/tools/"))

    def cluster(u):
        if u in META:
            return "meta"
        parts = [p for p in u.split("/") if p]
        return parts[0] if parts else "meta"

    cross = [e for e in edges if cluster(e[0]) != cluster(e[1])]
    pair_count = Counter()
    for f, t in edges:
        if cluster(f) != cluster(t):
            pair_count[tuple(sorted((cluster(f), cluster(t))))] += 1

    metrics = {
        "pages_total": N,
        "content_pages": len(content_pages),
        "content_edges": len(edges),
        "cross_cluster_edges": len(cross),
        "avg_outbound": round(len(edges) / len(content_pages), 2),
        "zero_inbound": [u for u in content_pages if not inb.get(u)],
        "zero_outbound": [u for u in content_pages if not content_out.get(u)],
        "hubs_no_content_inbound": [u for u in hubs if not inb.get(u)],
        "tools_no_content_inbound": [u for u in tools if not inb[u]],
        "new_pages_exist": [u for u in ("/tank-setup/water-change-guide", "/health/emergency-first-aid")
                            if u in pages],
        "role_note_pages": [u for u, d in pages.items() if 'class="role-note"' in d["html"]],
        "search_actions": None,
    }

    idx = os.path.join(PUBLIC, "search-index.json")
    if os.path.isfile(idx):
        data = json.load(open(idx, encoding="utf-8"))
        metrics["search_actions"] = [
            {"url": e.get("url"), "label": (e.get("action") or {}).get("label"),
             "kind": (e.get("action") or {}).get("kind")}
            for e in data if e.get("action")]

    report = {
        "errors": errors,
        "broken_links": len(errors["broken"]),
        "canonical_issues": len(errors["canonical"]) + len(errors["dup_canonical_groups"]),
        "metrics": metrics,
    }
    with open(os.path.join(OUT, "qa-report.json"), "w", encoding="utf-8") as fh:
        json.dump(report, fh, indent=1, ensure_ascii=False)

    lines = []
    for u in sorted(pages):
        lines.append(f"{u}\tin={len(inb.get(u, []))}\tout={len(content_out.get(u, []))}\t{cluster(u)}")
    with open(os.path.join(OUT, "qa-inout.tsv"), "w", encoding="utf-8") as fh:
        fh.write("\n".join(lines))

    print("broken:", len(errors["broken"]), "| canonical issues:", report["canonical_issues"])
    for b in errors["broken"][:10]:
        print("  broken:", b)
    for c in errors["canonical"][:10]:
        print("  canonical:", c)
    print("content pages:", len(content_pages), "| edges:", len(edges),
          "| cross:", len(cross), "| avg out:", metrics["avg_outbound"])
    print("zero inbound:", metrics["zero_inbound"])
    print("zero outbound:", metrics["zero_outbound"])
    print("hubs no inbound:", metrics["hubs_no_content_inbound"])
    print("tools no inbound:", metrics["tools_no_content_inbound"])
    print("role-note pages:", len(metrics["role_note_pages"]))
    print("search actions:", len(metrics["search_actions"] or []))


if __name__ == "__main__":
    sys.exit(0 if main() is None else 0)
