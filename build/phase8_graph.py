# -*- coding: utf-8 -*-
"""Phase 8 graph metrics. Content-scope only (excludes template/meta pages).
Usage:
  python phase8_graph.py                 # measure current build -> docs/phase8/metrics-before.json
  python phase8_graph.py after           # measure current build -> docs/phase8/metrics-after.json
Reads docs/phase7b/content-linkgraph.json.
"""
import json, os, io, sys
from collections import Counter, defaultdict

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
P7 = os.path.join(BASE, "docs", "phase7")
OUT = os.path.join(BASE, "docs", "phase8")
os.makedirs(OUT, exist_ok=True)

tag = sys.argv[1] if len(sys.argv) > 1 else "before"
lgpath = os.path.join(BASE, "docs", "phase7b", "content-linkgraph.json")
lg = json.load(open(lgpath, encoding="utf-8"))
edges = lg["edges"]
pages = set(json.load(open(os.path.join(P7, "pages.json"), encoding="utf-8")))

META = {"/", "/404.html", "/about", "/contact", "/privacy", "/search"}
CONTENT = sorted(u for u in pages if u not in META)


def cluster(u):
    if u in META:
        return "meta"
    parts = [p for p in u.split("/") if p]
    return parts[0] if parts else "meta"


CLUSTERS = ["axolotls", "care-basics", "tank-setup", "diet", "health", "morphs",
            "breeding", "biology-and-science", "cost-and-buying", "legal",
            "axolotl-in-culture", "gifts-and-merch", "tools"]

content_edges = [(e["from"], e["to"]) for e in edges
                 if e["from"] in CONTENT and e["to"] in CONTENT]
out = defaultdict(list)
for f, t in content_edges:
    out[f].append(t)
inb = defaultdict(list)
for f, t in content_edges:
    inb[t].append(f)

ipages = set(f for f, t in content_edges)
zero_in = [u for u in CONTENT if not inb.get(u)]
zero_out = [u for u in CONTENT if not out.get(u)]

cross = [(f, t) for f, t in content_edges if cluster(f) != cluster(t)]
mat = Counter((cluster(f), cluster(t)) for f, t in content_edges)

hubs = ["/axolotls", "/tank-setup", "/diet", "/health", "/legal", "/cost-and-buying",
        "/morphs", "/breeding", "/gifts-and-merch", "/care-basics",
        "/biology-and-science", "/axolotl-in-culture", "/tools"]
tools = sorted(u for u in CONTENT if u.startswith("/tools/"))

def reachable(node_list):
    return [u for u in node_list if inb.get(u)]

pair_count = Counter()
for f, t in content_edges:
    if cluster(f) != cluster(t):
        pair_count[tuple(sorted((cluster(f), cluster(t))))] += 1

def specific(a, b):
    return sum(1 for f, t in content_edges
               if (cluster(f) == a and cluster(t) == b) or (cluster(f) == b and cluster(t) == a))

metrics = {
    "tag": tag,
    "total_pages": len(pages),
    "content_pages": len(CONTENT),
    "content_edges": len(content_edges),
    "cross_cluster_edges": len(cross),
    "avg_outbound": round(len(content_edges) / len(CONTENT), 2),
    "zero_inbound": zero_in,
    "zero_outbound": zero_out,
    "hubs_with_content_inbound": reachable(hubs),
    "hubs_no_content_inbound": [u for u in hubs if u not in reachable(hubs)],
    "tools_with_content_inbound": reachable(tools),
    "tools_no_content_inbound": [u for u in tools if not inb.get(u)],
    "health_biology_edges": specific("health", "biology-and-science"),
    "breeding_diet_edges": specific("breeding", "diet"),
    "legal_external_inbound": [u for u in sorted(inb) if cluster(u) == "legal"
                               and any(cluster(f) != "legal" for f in inb[u])],
    "legal_external_inbound_edges": sum(1 for t in inb if cluster(t) == "legal"
                                        for f in inb[t] if cluster(f) != "legal"),
    "tools_external_inbound_edges": sum(1 for u in tools for f in inb.get(u, [])),
    "cross_pair_counts": {f"{a}<->{b}": n for (a, b), n in sorted(pair_count.items(), key=lambda kv: -kv[1])},
    "cluster_out": {k: sum(1 for f, t in content_edges if cluster(f) == k) for k in CLUSTERS},
    "cluster_in": {k: sum(1 for f, t in content_edges if cluster(t) == k) for k in CLUSTERS},
}

with open(os.path.join(OUT, f"metrics-{tag}.json"), "w", encoding="utf-8") as fh:
    json.dump(metrics, fh, indent=1, ensure_ascii=False)

print("== metrics:", tag)
print("content pages:", len(CONTENT), "| content edges:", len(content_edges),
      "| cross-cluster:", len(cross), "| avg out:", round(len(content_edges)/len(CONTENT), 2))
print("zero inbound:", zero_in)
print("zero outbound:", zero_out)
print("hubs with content inbound:", reachable(hubs))
print("tools with content inbound:", reachable(tools))
print("health<->biology:", metrics["health_biology_edges"],
      "| breeding<->diet:", metrics["breeding_diet_edges"])
print("legal external inbound edges:", metrics["legal_external_inbound_edges"])
print("tools external inbound edges:", metrics["tools_external_inbound_edges"])
print("cross pairs:", len(pair_count))