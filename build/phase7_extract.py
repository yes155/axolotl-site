# -*- coding: utf-8 -*-
"""
Phase 7 — Semantic SEO corpus extraction.

Parses the rendered site in public/ and emits:
  - docs/phase7/pages.json      (per-page structural data)
  - docs/phase7/linkgraph.json  (node + edge graph, inbound/outbound)
  - prints summary stats

No files under public/ are modified.
"""
import os
import re
import json
import html as htmlmod

ROOT = os.path.dirname(os.path.abspath(__file__))
PUBLIC = os.path.normpath(os.path.join(ROOT, "..", "public"))
OUT = os.path.normpath(os.path.join(ROOT, "..", "docs", "phase7"))
SITE = "https://myaxolotl.us"

BLOCK_STRIP = re.compile(r"<(script|style|noscript)[^>]*>.*?</\1>", re.S)
TAG_RE = re.compile(r"<[^>]+>")
H2_RE = re.compile(r"<h2[^>]*>(.*?)</h2>", re.S)
H3_RE = re.compile(r"<h3[^>]*>(.*?)</h3>", re.S)
A_RE = re.compile(r'<a\s+[^>]*href="([^"]+)"[^>]*>(.*?)</a>', re.S)
SUMMARY_RE = re.compile(r"<summary[^>]*>(.*?)</summary>", re.S)
FAQ_ITEM_RE = re.compile(r'<details class="faq-item"[^>]*>\s*<summary[^>]*>(.*?)</summary>', re.S)
IMG_ALT_RE = re.compile(r'<img[^>]*alt="([^"]*)"', re.S)
JSONLD_RE = re.compile(r'<script[^>]*type="application/ld\+json"[^>]*>(.*?)</script>', re.S)
WORDS_RE = re.compile(r"&middot; ([0-9,]+) words")

INTERNAL = ("/", SITE)


def strip(s):
    return htmlmod.unescape(TAG_RE.sub(" ", s or "")).replace("\xa0", " ").strip()


def norm_internal(href):
    href = href.split("#")[0]
    if href.startswith(SITE):
        href = href[len(SITE):]
    if not href.startswith("/") or href.startswith("//"):
        return None
    if href != "/" and href.endswith("/"):
        href = href[:-1]
    return href or "/"


def page_url(path):
    rel = os.path.relpath(path, PUBLIC).replace("\\", "/")
    if rel == "index.html":
        return "/"
    if rel.endswith("/index.html"):
        return "/" + rel[: -len("/index.html")]
    return "/" + rel


def classify(url):
    if url == "/":
        return "home"
    if url == "/404.html":
        return "404"
    if url == "/search":
        return "search"
    segs = url.strip("/").split("/")
    hub_slugs = {"axolotls", "tank-setup", "diet", "health", "legal",
                 "cost-and-buying", "morphs", "breeding", "gifts-and-merch",
                 "care-basics", "biology-and-science", "axolotl-in-culture"}
    if segs[0] == "tools" and len(segs) == 1:
        return "tools-index"
    if segs[0] == "tools":
        return "tool"
    if segs[0] in ("about", "privacy", "contact"):
        return "simple"
    if len(segs) == 1 and segs[0] in hub_slugs:
        return "hub"
    return "article"


def extract(path):
    with open(path, encoding="utf-8") as fh:
        raw = fh.read()
    body = BLOCK_STRIP.sub(" ", raw)
    url = page_url(path)
    title = htmlmod.unescape(
        re.search(r"<title>(.*?)</title>", raw, re.S).group(1).strip()
    ) if re.search(r"<title>(.*?)</title>", raw, re.S) else ""
    md = re.search(r'<meta name="description" content="([^"]*)"', raw)
    h1 = re.search(r"<h1[^>]*>(.*?)</h1>", body, re.S)
    canon = re.search(r'<link rel="canonical" href="([^"]+)"', raw)
    # breadcrumbs
    bc = re.search(r'<nav class="breadcrumbs"[^>]*>(.*?)</nav>', body, re.S)
    bc_links = [strip(l[1]) for l in A_RE.findall(bc.group(1), re.S)[:2]] if bc else []
    h3_raw = H3_RE.findall(body)
    h2_raw = H2_RE.findall(body)
    # drop related-guides / FAQ section from heading list? keep for semantics audit separately
    headings = []
    for h in h2_raw:
        t = strip(h)
        headings.append(t)
    for h in h3_raw:
        t = strip(h)
        if t:
            headings.append("  " + t)
    faq = [strip(s) for s in FAQ_ITEM_RE.findall(body)]
    alts = [a for a in IMG_ALT_RE.findall(raw)]
    wc = WORDS_RE.search(raw)
    words = int(wc.group(1).replace(",", "")) if wc else None
    # schema types
    types = []
    faq_schema = False
    for ld in JSONLD_RE.findall(raw):
        ld = ld.strip()
        for m in re.finditer(r'"@type"\s*:\s*"([A-Za-z]+)"', ld):
            if m.group(1) not in types:
                types.append(m.group(1))
        if '"FAQPage"' in ld:
            faq_schema = True
    # outbound internal links (dedupe, exclude self, exclude pure-hash)
    out = set()
    anchors = A_RE.findall(body)
    for href, _txt in anchors:
        ni = norm_internal(href)
        if ni and ni != url:
            out.add(ni)
    shorts = ["/"]  # drop header/footer nav hub links from "contextual" count later
    return {
        "url": url,
        "type_hint": classify(url),
        "title": title,
        "meta_desc": strip(md.group(1)) if md else None,
        "h1": strip(h1.group(1)) if h1 else None,
        "breadcrumbs": bc_links,
        "canonical": canon.group(1) if canon else None,
        "headings": headings,
        "faq": faq,
        "faq_schema": faq_schema,
        "schema_types": types,
        "img_alts": alts,
        "words": words,
        "raw_outbound": sorted(out),
        "_file": os.path.relpath(path, PUBLIC),
    }


def main():
    pages = {}
    for dirpath, _dirs, files in os.walk(PUBLIC):
        for fn in files:
            if fn in ("index.html", "404.html"):
                p = os.path.join(dirpath, fn)
                pages[page_url(p)] = extract(p)

    # build graph
    nodes, edges = [], []
    inbound = {u: [] for u in pages}
    for u, d in pages.items():
        for tgt in d["raw_outbound"]:
            if tgt in pages and tgt != u:
                edges.append({"from": u, "to": tgt})
                inbound[tgt].append(u)
    for u, d in pages.items():
        d["inbound"] = sorted(inbound[u])
        d["inbound_count"] = len(inbound[u])
        d["outbound_contextual"] = sorted(
            t for t in d["raw_outbound"] if t in pages
        )
    with open(os.path.join(OUT, "pages.json"), "w", encoding="utf-8") as fh:
        json.dump(pages, fh, ensure_ascii=False, indent=1)
    with open(os.path.join(OUT, "linkgraph.json"), "w", encoding="utf-8") as fh:
        json.dump({"nodes": list(pages), "edges": edges}, fh, ensure_ascii=False)

    types = {}
    for d in pages.values():
        types[d["type_hint"]] = types.get(d["type_hint"], 0) + 1
    orphans = [u for u, d in pages.items() if d["inbound_count"] == 0 and u != "/404.html"]
    zero_out = [u for u, d in pages.items() if not d["outbound_contextual"]]
    zero_in = [u for u, d in pages.items() if d["inbound_count"] == 0]
    print("pages:", len(pages), "| types:", types)
    print("edges:", len(edges))
    print("orphans (0 inbound):", orphans)
    print("zero outbound:", zero_out)
    print("zero inbound:", zero_in)
    print("total faq items:", sum(len(d['faq']) for d in pages.values()))
    print("faq_schema pages:", sum(1 for d in pages.values() if d['faq_schema']))
    print("pages without FAQPage schema but with FAQ:", sum(
        1 for d in pages.values() if d['faq'] and not d['faq_schema']))
    print("schema type coverage:", dict(
        (t, sum(1 for d in pages.values() if t in d['schema_types']))
        for t in ("Article", "WebSite", "WebPage", "FAQPage", "BreadcrumbList", "SoftwareApplication")))


if __name__ == "__main__":
    main()
