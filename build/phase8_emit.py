# -*- coding: utf-8 -*-
"""Phase 8 deliverable emitter: builds docs/phase8-semantic-graph.json and
docs/phase8-link-changes.csv from the current build + the Phase 8 edge table."""
import json, os, io, csv, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DOCS = os.path.join(BASE, "docs")
CLG = json.load(open(os.path.join(DOCS, "phase7b", "content-linkgraph.json"), encoding="utf-8"))
pages = json.load(open(os.path.join(DOCS, "phase7", "pages.json"), encoding="utf-8"))

META = {"/", "/404.html", "/about", "/contact", "/privacy", "/search"}

def cluster(u):
    if u in META:
        return "meta"
    parts = [p for p in u.split("/") if p]
    return parts[0] if parts else "meta"

# Phase 8 edge table: (source_slug, target_slug_or_url, relationship, priority, mechanism, anchor, reason)
EDGES = [
    ("biology-and-science/anatomy-gills-and-lungs", "health/shrinking-gills",
     "biology -> practical application | gills change shape with health/water issues", "P0",
     "related-rail", "(destination title)", "Anatomy page states gills 'change shape with stress and water quality'; shrinking-gills is the care application."),
    ("health/shrinking-gills", "biology-and-science/anatomy-gills-and-lungs",
     "symptom -> underlying anatomy", "P0", "related-rail", "(destination title)", "Shrinking/curling gills are the same organ the anatomy page explains; connects care symptom to biology."),
    ("biology-and-science/anatomy-gills-and-lungs", "health/stress-signs",
     "biology -> practical application | gills as health indicator", "P0", "inline",
     "health indicator", "The exact phrase 'health indicator' already exists; stress-signs is the operational checklist."),
    ("biology-and-science/anatomy-gills-and-lungs", "health/why-axolotl-floating",
     "natural physiology -> captive-care implication", "P1", "inline",
     "Surface gulping", "'Surface gulping ... is normal behavior' directly connects to the floating page's swallowed-air section."),
    ("health/limb-regeneration", "biology-and-science/regeneration-and-limb-regrowth",
     "healing experience -> underlying science", "P0", "related-rail", "(destination title)", "Limb-regeneration page describes the mechanism; the biology page explains why it happens. Reciprocates the existing biology->health edge."),
    ("biology-and-science/regeneration-and-limb-regrowth", "health/minor-scrapes-and-wounds",
     "science -> practical wound care", "P0", "related-rail", "(destination title)", "Regeneration page explains wound closure; minor-scrapes is the everyday application for the same mechanism."),
    ("health/curled-gills-stress-signal", "biology-and-science/anatomy-gills-and-lungs",
     "symptom -> causal organ", "P1", "related-rail", "(destination title)", "Curled gills are a gill-structure symptom; the anatomy page explains why gills respond to stress."),
    ("health/malnutrition-signs", "biology-and-science/regeneration-and-limb-regrowth",
     "biology rationale -> recovery caveat", "P1", "related-rail", "(destination title)", "Malnutrition page itself notes 'how much their biology depends on regeneration'; links the cited biology."),
    ("health/fungal-infections-saprolegnia", "biology-and-science/anatomy-gills-and-lungs",
     "anatomy -> treatment sensitivity", "P1", "related-rail", "(destination title)", "Fungal page explains skin/external-gill permeability; anatomy page is the underlying physiology."),
    ("breeding/egg-and-larvae-care", "diet/shrimp-for-axolotls",
     "procedure -> food item | first food is baby brine shrimp", "P0", "related-rail", "(destination title)", "Larvae care directs feeding live baby brine shrimp; the shrimp page covers that food in detail."),
    ("breeding/egg-and-larvae-care", "diet/feeding-schedule-by-age",
     "life stage -> feeding frequency", "P0", "related-rail", "(destination title)", "Hatchlings feeding 2-3x/day is covered by the age-based schedule page."),
    ("breeding/raising-juveniles", "diet/feeding-schedule-by-age",
     "procedure -> schedule", "P0", "related-rail", "(destination title)", "Raising page has a 'How Often Do You Feed Baby Axolotls' section; the schedule page is its reference."),
    ("breeding/raising-juveniles", "diet/blackworms-for-juveniles",
     "procedure -> staple food", "P0", "related-rail", "(destination title)", "Juvenile staple food is blackworms; the dedicated diet page covers preparation and feeding."),
    ("diet/shrimp-for-axolotls", "breeding/egg-and-larvae-care",
     "food item -> life stage that needs it", "P1", "related-rail", "(destination title)", "Shrimp page mentions baby brine shrimp for hatchlings; the breeding page explains that stage. Reciprocal of egg->shrimp."),
    ("diet/blackworms-for-juveniles", "breeding/raising-juveniles",
     "feeding -> post-breeding husbandry", "P1", "related-rail", "(destination title)", "Juveniles come from the breeding process; reciprocal of raising->blackworms."),
    ("diet/feeding-schedule-by-age", "breeding/raising-juveniles",
     "schedule -> lifecycle context", "P1", "related-rail", "(destination title)", "Juvenile stage is the breeding outcome; reciprocal of raising->feeding-schedule."),
    ("axolotls/care-guide", "legal",
     "ownership decision -> legal status -> jurisdiction", "P0", "inline(2)+related-rail",
     "Check your specific state and city before you buy / before buying", "Care-guide's legal section is a dead-letter reference; the exact gate the audit identified."),
    ("axolotl-in-culture/adopt-me-axolotl-guide", "legal",
     "virtual ownership -> real-world legality", "P1", "inline",
     "check your local laws first", "Adopt-Me page already says 'check your local laws first'; links the legal hub that answers it."),
    ("tools", "tank-setup/setup-guide",
     "tool -> prerequisite knowledge", "P1", "tools-index", "(destination title)", "Grounds the tool hub: the setup guide is the baseline all tools assume."),
    ("tools", "tank-setup/water-parameters-cycling",
     "tool -> referenced science", "P1", "tools-index", "(destination title)", "Nitrogen-cycle tracker and dosage calculator depend on the cycling science."),
    ("tools", "diet/feeding-schedule-by-age",
     "tool -> referenced schedule", "P1", "tools-index", "(destination title)", "Feeding-schedule generator operationalizes this article; fixes the /tools dead end."),
    ("tools", "health/refusing-to-eat",
     "tool -> action pathway", "P1", "tools-index", "(destination title)", "Symptom checker funnels to refusing-to-eat as the first next step; fixes the /tools dead end."),
]

REL = {(a, b): r for a, b, r, *_ in EDGES}
NEW = {("/" + a if a != "tools" else "/tools", "/" + b) for a, b, *_ in EDGES}

# ---- semantic-graph.json ----
nodes = []
for u in sorted(pages):
    nodes.append({"url": u, "cluster": cluster(u), "type": pages[u].get("type", "")})

edges_out = []
seen = set()
for e in CLG["edges"]:
    f, t = e["from"], e["to"]
    if f in META or t in META:
        continue
    key = (f, t)
    if key in seen:
        continue
    seen.add(key)
    edges_out.append({
        "source": f, "target": t,
        "source_cluster": cluster(f), "target_cluster": cluster(t),
        "phase8": (f, t) in NEW,
        "relationship": REL.get((f, t), "contextual (existing)"),
    })

# phase8-only edges that resolve to hubs/tools not in the content graph (legal hub is template-filtered)
for a, b, r, p, mech, anchor, reason in EDGES:
    su = ("/" + a) if a != "tools" else "/tools"
    tu = "/" + b
    if (su, tu) not in seen and (su, tu) in NEW:
        seen.add((su, tu))
        edges_out.append({
            "source": su, "target": tu,
            "source_cluster": cluster(su), "target_cluster": cluster(tu),
            "phase8": True,
            "relationship": r,
            "note": "rendered; excluded from content-linkgraph because target is template-filtered (site-wide footer/nav)",
        })

with open(os.path.join(DOCS, "phase8-semantic-graph.json"), "w", encoding="utf-8") as fh:
    json.dump({"generated_for": "phase8", "nodes": nodes, "edges": edges_out},
              fh, ensure_ascii=False, indent=1)
print("wrote phase8-semantic-graph.json: nodes=", len(nodes), "edges=", len(edges_out))

# ---- link-changes.csv ----
with open(os.path.join(DOCS, "phase8-link-changes.csv"), "w", newline="", encoding="utf-8") as fh:
    w = csv.writer(fh, lineterminator="\n")
    w.writerow(["source_url", "target_url", "relationship", "priority", "mechanism", "anchor_text", "status", "reason"])
    for a, b, r, p, mech, anchor, reason in EDGES:
        su = "/" + a + "/" if a != "tools" else "/tools"
        tu = "/" + b + "/"
        w.writerow([su, tu, r, p, mech, anchor, "implemented", reason])
print("wrote phase8-link-changes.csv:", len(EDGES), "rows")