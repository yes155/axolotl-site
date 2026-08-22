# -*- coding: utf-8 -*-
"""Phase 8 helper: search article text for a phrase (case-insensitive).
Usage: python phase8_srch.py "phrase" [url-substring]
Prints article urls whose body contains the phrase, plus the surrounding sentence."""
import json, os, sys, re, io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
data = json.load(open(os.path.join(BASE, "docs", "phase8", "article-text.json"), encoding="utf-8"))

phrase = sys.argv[1].lower()
urllike = sys.argv[2] if len(sys.argv) > 2 else ""
rx = re.compile(re.escape(phrase), re.I)

hits = []
for u, d in data.items():
    if urllike and urllike not in u:
        continue
    if rx.search(d["lower"]):
        hits.append(u)

print(f"phrase '{phrase}' in {len(hits)} article(s):")
for u in sorted(hits)[:40]:
    txt = data[u]["text"]
    m = rx.search(txt)
    s = max(0, m.start() - 90)
    ctx = re.sub(r"\s+", " ", txt[s:m.end() + 90])
    print("  %-50s ...%s..." % (u, ctx))