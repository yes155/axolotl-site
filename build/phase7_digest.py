# -*- coding: utf-8 -*-
"""Phase 7 digest builder — compact per-page semantic digest + metadata audit."""
import json

pages = json.load(open("docs/phase7/pages.json", encoding="utf-8"))
idx = json.load(open("public/search-index.json", encoding="utf-8"))
by_url = {i["url"].rstrip("/") or "/": i for i in idx}

out = []
meta_flags = {}
for u, p in sorted(pages.items()):
    if p["type_hint"] == "404":
        continue
    md = p["meta_desc"] or ""
    flags = []
    if not md:
        flags.append("no-meta")
    elif len(md) > 170:
        flags.append("meta-too-long")
    elif len(md) < 50:
        flags.append("meta-short")
    meta_flags[u] = flags

for u in sorted(pages):
    p = pages[u]
    line = {
        "url": u,
        "type": p["type_hint"],
        "title": p["h1"] or p["title"],
        "words": p["words"],
        "in": p["inbound_count"],
        "out": len(p["outbound_contextual"]),
        "faq": len(p["faq"]),
        "dek": (by_url.get(u, {}).get("dek") or "")[:150],
        "meta_flags": meta_flags.get(u, []),
    }
    out.append(line)

with open("docs/phase7/digest.json", "w", encoding="utf-8") as fh:
    json.dump(out, fh, ensure_ascii=False, indent=1)

# ---- metadata audit ----
issues = []
for u, p in sorted(pages.items()):
    if p["type_hint"] == "404":
        continue
    md = p["meta_desc"] or ""
    t = p["title"] or ""
    if not md:
        issues.append(("no-meta", u))
    elif len(md) > 170:
        issues.append(("meta-too-long", u, len(md)))
    elif len(md) < 50:
        issues.append(("meta-short", u, len(md)))
    if not t:
        issues.append(("no-title", u))
    if p["h1"] and p["h1"] != p["title"]:
        pass  # title!=H1 is by design (title_tag mangling); recorded separately
# duplicate-ish titles (first 45 chars)
seen = {}
dups = []
for u, p in sorted(pages.items()):
    t = (p["title"] or "").split("|")[0].strip().replace("…", "").rstrip()
    key = t[:45]
    seen.setdefault(key, []).append(u)
for k, us in seen.items():
    if len(us) > 1:
        dups.append((k, us))
print("== metadata issues ==")
for i in issues:
    print(i)
print()
print("== near-identical titles ==")
for k, us in dups:
    print(k, "->", us)