# -*- coding: utf-8 -*-
"""Phase 7B: build a content-only link graph (excludes nav/template edges)
and cluster matrices from docs/phase7/pages.json. Analysis only; writes
analysis artifacts to docs/phase7b/."""
import json, os, io

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
P7 = os.path.join(BASE, "docs", "phase7")
OUT = os.path.join(BASE, "docs", "phase7b")
os.makedirs(OUT, exist_ok=True)

pages = json.load(open(os.path.join(P7, "pages.json"), encoding="utf-8"))

# Template/nav targets = seen on >= 90% of pages (boilerplate, header nav, footer)
from collections import Counter
freq = Counter()
for u, d in pages.items():
    for t in d["raw_outbound"]:
        if t in pages and t != u:
            freq[t] += 1
N = len(pages)
TEMPLATE = {t for t, c in freq.items() if c / N >= 0.90}

def cluster(u):
    if u in ("/", "/404.html", "/about", "/contact", "/privacy", "/search"):
        return "meta"
    parts = [p for p in u.split("/") if p]
    if not parts:
        return "meta"
    return parts[0]

CLUSTERS = ["axolotls", "care-basics", "tank-setup", "diet", "health",
            "morphs", "breeding", "biology-and-science", "cost-and-buying",
            "legal", "axolotl-in-culture", "gifts-and-merch", "tools"]

# content edges
content_out = {}
content_in = {u: [] for u in pages}
for u, d in pages.items():
    out = []
    for t in d["raw_outbound"]:
        if t in pages and t != u and t not in TEMPLATE:
            out.append(t)
    content_out[u] = sorted(set(out))
    for t in content_out[u]:
        content_in[t].append(u)
for u in content_in:
    content_in[u] = sorted(set(content_in[u]))

with open(os.path.join(OUT, "content-linkgraph.json"), "w", encoding="utf-8") as fh:
    json.dump({"template": sorted(TEMPLATE),
               "edges": [{"from": u, "to": t} for u in sorted(content_out)
                         for t in content_out[u]]}, fh, indent=1)

# cluster x cluster content edge matrix
mat = {}
for u in sorted(content_out):
    cu = cluster(u)
    for t in content_out[u]:
        ct = cluster(t)
        mat[(cu, ct)] = mat.get((cu, ct), 0) + 1

def cell(a, b):
    return mat.get((a, b), 0)

rows = []
hdr = "cluster\t" + "\t".join(CLUSTERS)
rows.append(hdr)
for a in CLUSTERS:
    rows.append(a + "\t" + "\t".join(str(cell(a, b)) for b in CLUSTERS))
open(os.path.join(OUT, "cluster-matrix.txt"), "w", encoding="utf-8").write("\n".join(rows))

# per-page content in/out summaries
lines = []
for u in sorted(pages):
    d = pages[u]
    lines.append("%s\t%s\t%s\tin=%d\tout=%d\t%s %s" % (
        u, cluster(u), d.get("type_hint"), len(content_in.get(u, [])),
        len(content_out.get(u, [])), d.get("h1", ""), d.get("title")))
open(os.path.join(OUT, "content-inout.tsv"), "w", encoding="utf-8").write("\n".join(lines))

# top content-inbound pages
top = sorted(content_in.items(), key=lambda kv: -len(kv[1]))[:25]
print("TOP CONTENT INBOUND")
for u, ins in top:
    print("%3d  %-55s <- %s" % (len(ins), u, ", ".join(ins)))
print()
print("cluster matrix (rows=source, cols=target)")
print("\n".join(rows))