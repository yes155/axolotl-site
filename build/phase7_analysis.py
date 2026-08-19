# -*- coding: utf-8 -*-
"""
Phase 7 - Semantic SEO analysis.
Reads docs/phase7/digest.json + pages.json (headings/FAQ/schema) and
the hub config + topical-map keywords, then emits:

  docs/phase7/topical-map.json        machine-readable taxonomy
  docs/phase7/topical-map.md          human-readable topical map
  docs/phase7/semantic-page-audit.csv per-page semantic audit
  docs/phase7/semantic-priority.md    priority / strategy report

No source files under public/ are modified.
"""
import os
import re
import json
import csv
import sys

ROOT = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.normpath(os.path.join(ROOT, "..", "docs", "phase7"))

# ---------------------------------------------------------------- load data
def load(fn):
    with open(os.path.join(OUT, fn), encoding="utf-8") as fh:
        return json.load(fh)

digest = load("digest.json")          # list of per-page metrics
pages = load("pages.json")            # dict url -> structural details
dby = {d["url"]: d for d in digest}

# ---------------------------------------------------------------- taxonomy
# Each cluster: hub slug it owns (authoritative primary), plus discriminating
# phrase signals (word-boundary regex) used only for cross-topic relevance.
CLUSTERS = [
    {"id": "care-basics", "name": "Care basics & ownership", "stage": "TOFU",
     "hubs": ["care-basics", "axolotls"],
     "terms": ["beginner", "good pets", "for kids", "children", "pronounce",
               "fact", "behavior", "hold", "recognize", "age and size",
               "live together", "cost of ownership", "monthly cost", "age chart"]},
    {"id": "tank-setup", "name": "Tank setup & water", "stage": "MOFU",
     "hubs": ["tank-setup"],
     "terms": ["tank setup", "tank size", "filter", "chiller", "substrate",
               "gravel", "lighting", "hides", "caves", "plants", "temperature",
               "tank cool", "acclimate", "water conditioner", "water quality",
               "ammonia", "nitrate", "smell", "stink", "cycle", "nitrogen",
               "tank mates", "live with fish", "uneaten food", "aquarium"]},
    {"id": "diet", "name": "Diet & feeding", "stage": "MOFU",
     "hubs": ["diet"],
     "terms": ["eat", "diet guide", "what do axolotls eat", "feed",
               "feeding frequency", "pellets", "earthworm", "bloodworm",
               "beef heart", "shrimp", "blackworm", "feeder fish", "fast",
               "hand feed", "obesity", "overfeed", "vitamin", "supplement",
               "malnutrition", "food"]},
    {"id": "health", "name": "Health & illness", "stage": "MOFU",
     "hubs": ["health"],
     "terms": ["fungus", "fungal", "tea bath", "salt bath", "fridge",
               "fridging", "gills", "floating", "stress", "regeneration",
               "limb", "ammonia burn", "red leg", "quarantine", "parasite",
               "scrapes", "wounds", "refusing to eat", "impaction", "vet",
               "sick", "shrinking", "sap", "disease", "syndrome"]},
    {"id": "morphs", "name": "Morphs & color genetics", "stage": "MOFU",
     "hubs": ["morphs"],
     "terms": ["morph", "leucistic", "melanoid", "albino", "gfp", "copper",
               "piebald", "chimera", "mosaic", "wild type", "pigment",
               "enigma", "firefly", "mac", "blue and pink", "color",
               "genetics", "punnett", "glowing"]},
    {"id": "breeding", "name": "Breeding & genetics", "stage": "MOFU",
     "hubs": ["breeding"],
     "terms": ["breed", "egg", "larvae", "juvenile", "punnett", "inbreeding",
               "sexing", "gender", "temperature cycling", "raising baby",
               "juveniles"]},
    {"id": "cost-buying", "name": "Cost & buying", "stage": "BOFU",
     "hubs": ["cost-and-buying"],
     "terms": ["price", "cost", "buy", "breeder", "pet store", "shipped",
               "seller", "red flag", "healthy axolotl"]},
    {"id": "legal", "name": "Legality", "stage": "BOFU",
     "hubs": ["legal"],
     "terms": ["legal", "law", "permit", "california", "canada", "hawaii",
               "maine", "jersey", "virginia", "mexico"]},
    {"id": "biology", "name": "Biology & science", "stage": "TOFU",
     "hubs": ["biology-and-science"],
     "terms": ["anatomy", "lungs", "amphibian", "neoteny", "regeneration",
               "salamander", "habitat", "xochimilco", "conservation",
               "endangered", "lifespan", "biology"]},
    {"id": "culture", "name": "Pop culture, gifts & merch", "stage": "TOFU",
     "hubs": ["axolotl-in-culture", "gifts-and-merch"],
     "terms": ["minecraft", "adopt me", "meme", "popular", "culture",
               "squishmallow", "lego", "plush", "toy", "build-a-bear",
               "gifts", "merch"]},
    {"id": "tools", "name": "Interactive tools", "stage": "BOFU",
     "hubs": ["tools"],
     "terms": ["calculator", "generator", "tracker", "checker"]},
]
HUB_TO_CLUSTER = {}
for c in CLUSTERS:
    for h in c["hubs"]:
        HUB_TO_CLUSTER[h] = c["id"]
TERM_SET = {}
for c in CLUSTERS:
    for t in c["terms"]:
        TERM_SET.setdefault(t, []).append(c["id"])

# ---------------------------------------------------------------- intent
INFO = ["what is", "what s", "what's", "what do", "what does", "how to", "how do",
        "how long", "how much", "how are", "how old", "can ", "do ", "does ",
        "why ", "is ", "are ", "when", "amazing", "myth", "guide", "complete",
        "explained", "understand", "review", "vs ", "compare"]
BUY = ["price", "cost", "buy", "where to buy", "legal", "for sale", "how much",
       "shipped", "seller", "breeder vs", "budget"]
NAV = ["about", "contact", "privacy", "search", "404", "tools"]

def intent_of(title, url):
    t = (title or "").lower()
    ty = dby.get(url, {}).get("type", "")
    if ty in ("home", "simple", "search", "404", "tools-index"):
        return "nav"
    if ty == "tool":
        return "trans"
    if any(k in t for k in BUY):
        return "commercial"
    if "best " in t or " vs " in t or "top " in t or "comparison" in t:
        return "commercial-investigation"
    return "informational"

# ---------------------------------------------------------------- entities
def entities_of(url):
    text = " ".join([
        dby.get(url, {}).get("title", "") or "",
        dby.get(url, {}).get("dek", "") or "",
    ]).lower()
    found = set()
    for term, cl in TERM_SET.items():
        pat = r"(?<![a-z])" + re.escape(term) + r"(?![a-z])"
        if re.search(pat, text):
            found.add(cl[0])
    return sorted(found)

def primary_cluster(url):
    hub = url.strip("/").split("/")[0] if url != "/" else "home"
    return HUB_TO_CLUSTER.get(hub, "other")

# ---------------------------------------------------------------- content audit
def audit(url):
    d = dby.get(url, {})
    ty = d.get("type", "")
    flags = []
    words = d.get("words") or 0
    if ty == "article":
        if words < 700:
            flags.append("thin")
        if not (d.get("faq") or 0):
            flags.append("no-faq")
        if (d.get("in") or 0) < 2:
            flags.append("cold-hub")
    flags += list(d.get("meta_flags", []))
    return flags

# ------------------------------------------------------------------ build map
def main():
    articles = [d for d in digest if d["type"] in ("article", "tool")]
    rows = []
    for a in articles:
        url = a["url"]
        prim = primary_cluster(url)
        ent = entities_of(url)
        secondary = [c for c in ent if c != prim]
        rows.append({
            "url": url,
            "title": a["title"],
            "hub": url.strip("/").split("/")[0] if url != "/" else "home",
            "type": a["type"],
            "words": a["words"] or 0,
            "inbound": a["in"] or 0,
            "outbound": a["out"] or 0,
            "faqs": a["faq"] or 0,
            "intent": intent_of(a["title"], url),
            "cluster": prim,
            "secondary": secondary,
            "flags": audit(url),
        })

    cluster_members = {}
    for c in CLUSTERS:
        cluster_members[c["id"]] = [r for r in rows if r["cluster"] == c["id"]]

    # ---- topical-map.json
    mapping = {
        "site": "axolotlcare",
        "page_count": len(digest),
        "article_count": len([r for r in rows if r["type"] == "article"]),
        "clusters": [],
    }
    for c in CLUSTERS:
        mems = cluster_members[c["id"]]
        mapping["clusters"].append({
            "id": c["id"],
            "name": c["name"],
            "stage": c["stage"],
            "page_count": len(mems),
            "page_urls": [m["url"] for m in mems],
        })
    with open(os.path.join(OUT, "topical-map.json"), "w", encoding="utf-8") as fh:
        json.dump(mapping, fh, ensure_ascii=False, indent=1)

    # ---- semantic-page-audit.csv
    with open(os.path.join(OUT, "semantic-page-audit.csv"), "w", encoding="utf-8",
              newline="") as fh:
        w = csv.writer(fh)
        w.writerow(["url", "title", "type", "hub", "cluster", "secondary",
                    "words", "inbound", "outbound", "faqs", "intent", "flags"])
        for r in sorted(rows, key=lambda r: (r["cluster"], r["url"])):
            w.writerow([r["url"], r["title"], r["type"], r["hub"], r["cluster"],
                        "|".join(r["secondary"]), r["words"], r["inbound"],
                        r["outbound"], r["faqs"], r["intent"],
                        "|".join(r["flags"])])

    # ---- topical-map.md
    lines = ["# Axolotl Care Guide - Topical Map (Phase 7)", "",
             f"Built corpus: **{mapping['page_count']} pages** = "
             f"{mapping['article_count']} articles + 12 hubs + 6 tools + boilerplate.",
             "",
             "## Topic clusters", ""]
    for c in CLUSTERS:
        mems = cluster_members[c["id"]]
        lines.append(f"### {c['name']}  _({c['stage']})_  - {len(mems)} pages")
        for m in sorted(mems, key=lambda m: (m["hub"], m["url"])):
            fl = ("  [" + ",".join(m["flags"]) + "]") if m["flags"] else ""
            x = ("  -> " + ",".join(m["secondary"])) if m["secondary"] else ""
            lines.append(f"- `{m['url']}`  {m['intent']}  {m['words']}w  "
                         f"in={m['inbound']}  faq={m['faqs']}{fl}{x}")
        lines.append("")
    lines.append("## Cross-topic relevance (secondary signals only)")
    for r in sorted(rows, key=lambda r: -len(r["secondary"])):
        if r["secondary"]:
            lines.append(f"- `{r['url']}` -> " + ", ".join(r["secondary"]))
    with open(os.path.join(OUT, "topical-map.md"), "w", encoding="utf-8") as fh:
        fh.write("\n".join(lines))

    # ---- semantic-priority.md (strategy)
    flags_agg = {}
    for r in rows:
        for f in r["flags"]:
            flags_agg[f] = flags_agg.get(f, 0) + 1
    aus = sorted(rows, key=lambda r: -r["inbound"])
    thin = [r for r in rows if "thin" in r["flags"]]
    nofaq = [r for r in rows if "no-faq" in r["flags"]]
    cold = [r for r in rows if "cold-hub" in r["flags"]]

    L = ["# Phase 7 - Semantic SEO Priority Report", "",
         "## 1. Corpus summary", "",
         f"- Pages: {mapping['page_count']} | Articles+tools: {len(rows)}",
         f"- Total FAQ items: {sum(r['faqs'] for r in rows)}",
         f"- Flag counts: {json.dumps(flags_agg, indent=0)}", "",
         "## 2. Internal linking - highest inbound (authority pages)", ""]
    for r in aus[:12]:
        L.append(f"- `{r['url']}` in={r['inbound']} out={r['outbound']} (" + (r["title"] or "")[:60] + ")")
    L += ["", "## 3. Content quality gaps", "",
          f"### Thin articles (<700 words) - {len(thin)}"]
    for r in thin:
        L.append(f"- `{r['url']}` {r['words']}w")
    L += ["", f"### No FAQ block - {len(nofaq)}"]
    for r in nofaq:
        L.append(f"- `{r['url']}`")
    L += ["", f"### Cold / orphan-ish (inbound < 2) - {len(cold)}"]
    for r in cold:
        L.append(f"- `{r['url']}` in={r['inbound']}")
    L += ["", "## 4. Intent mix", ""]
    from collections import Counter
    cm = Counter(r["intent"] for r in rows)
    for k, v in cm.most_common():
        L.append(f"- {k}: {v}")
    L += ["", "## 5. Recommendations (ranked)", "",
          "1. Convert thin informative articles into hub spokes with FAQ schema.",
          "2. Add inbound links from authority pages to cold articles.",
          "3. Add FAQ blocks to articles missing them.",
          "4. Build out any cluster not yet covered by the topical map.",
          "5. Re-run `phase7_extract.py` + `phase7_digest.py` after edits."]
    with open(os.path.join(OUT, "semantic-priority.md"), "w", encoding="utf-8") as fh:
        fh.write("\n".join(L))

    print("wrote", "topical-map.json", "topical-map.md", "semantic-page-audit.csv",
          "semantic-priority.md")
    for c in CLUSTERS:
        print(f"  {c['name']:28s} {len(cluster_members[c['id']]):3d} pages")


if __name__ == "__main__":
    main()