# -*- coding: utf-8 -*-
"""Phase 7B: page-role, PPR and border assignments (judgment encoded here,
grounded in the corpus evidence dumped from docs/phase7). Writes CSVs to
docs/phase7b/. Analysis only."""

import json, os

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
P7 = os.path.join(BASE, "docs", "phase7")
OUT = os.path.join(BASE, "docs", "phase7b")
os.makedirs(OUT, exist_ok=True)

pages = json.load(open(os.path.join(P7, "pages.json"), encoding="utf-8"))

# url -> (role, border_status_letter, primary_intent, primary_attribute)
# border: C=core A=adjacent O=outer P=peripheral X=outside M=meta/functional
S = {
    "/": ("foundational", "M", "navigational", "-"),
    "/404.html": ("hub", "M", "navigational", "-"),
    "/about": ("supporting", "M", "navigational", "-"),
    "/contact": ("supporting", "M", "navigational", "-"),
    "/privacy": ("supporting", "M", "navigational", "-"),
    "/search": ("tool", "M", "tool/calculator", "search"),
    "/tools": ("tool", "M", "tool/calculator", "tools"),
    # ---- axolotls (foundational) ----
    "/axolotls": ("hub", "C", "navigational", "axolotl"),
    "/axolotls/care-guide": ("foundational", "C", "informational", "axolotl"),
    # ---- care-basics ----
    "/care-basics": ("hub", "C", "navigational", "ownership"),
    "/care-basics/are-axolotls-good-beginner-pets": ("explanatory", "C", "definitional", "suitability"),
    "/care-basics/axolotl-age-and-size-chart": ("explanatory", "C", "definitional", "growth"),
    "/care-basics/axolotl-facts": ("explanatory", "C", "informational", "species"),
    "/care-basics/axolotl-intelligence-and-bonding": ("explanatory", "C", "informational", "behavior"),
    "/care-basics/axolotls-and-children": ("explanatory", "C", "definitional", "suitability"),
    "/care-basics/behavior": ("diagnostic", "C", "problem-solving", "behavior"),
    "/care-basics/cost-of-ownership-monthly": ("transactional", "O", "transactional", "cost"),
    "/care-basics/handling": ("procedural", "C", "procedural", "handling"),
    "/care-basics/how-to-pronounce-axolotl": ("explanatory", "P", "definitional", "language"),
    "/care-basics/keeping-multiple-axolotls": ("explanatory", "C", "informational", "housing"),
    # ---- tank-setup ----
    "/tank-setup": ("hub", "C", "navigational", "tank"),
    "/tank-setup/acclimating-a-new-axolotl": ("procedural", "C", "procedural", "acclimation"),
    "/tank-setup/aquarium-chillers": ("comparative", "P", "comparative", "temperature"),
    "/tank-setup/canister-vs-sponge-filter": ("comparative", "C", "comparative", "filtration"),
    "/tank-setup/filtration-for-axolotls": ("comparative", "C", "comparative", "filtration"),
    "/tank-setup/gravel-risks": ("explanatory", "C", "problem-solving", "substrate"),
    "/tank-setup/hides-and-caves": ("comparative", "P", "comparative", "decor"),
    "/tank-setup/lighting-for-axolotls": ("explanatory", "C", "informational", "lighting"),
    "/tank-setup/live-vs-artificial-plants": ("comparative", "P", "comparative", "decor"),
    "/tank-setup/setup-guide": ("procedural", "C", "procedural", "tank"),
    "/tank-setup/substrate-and-impaction": ("explanatory", "C", "informational", "substrate"),
    "/tank-setup/tank-mates": ("explanatory", "C", "informational", "housing"),
    "/tank-setup/tank-size-by-age": ("explanatory", "C", "definitional", "size"),
    "/tank-setup/temperature": ("procedural", "C", "procedural", "temperature"),
    "/tank-setup/uneaten-food-and-ammonia": ("explanatory", "C", "problem-solving", "ammonia"),
    "/tank-setup/water-conditioners": ("procedural", "C", "procedural", "water"),
    "/tank-setup/water-parameters-cycling": ("explanatory", "C", "informational", "water"),
    "/tank-setup/why-tank-water-smells": ("diagnostic", "C", "problem-solving", "water"),
    # ---- diet ----
    "/diet": ("hub", "C", "navigational", "diet"),
    "/diet/axolotl-pellets": ("comparative", "C", "comparative", "food"),
    "/diet/beef-heart": ("explanatory", "C", "definitional", "food"),
    "/diet/best-foods-list": ("explanatory", "C", "informational", "food"),
    "/diet/blackworms-for-juveniles": ("procedural", "O", "procedural", "food"),
    "/diet/fasting-and-vacation": ("procedural", "O", "procedural", "feeding"),
    "/diet/feeder-fish-risks": ("explanatory", "C", "problem-solving", "food"),
    "/diet/feeding-schedule-by-age": ("procedural", "C", "procedural", "feeding"),
    "/diet/how-to-hand-feed": ("procedural", "C", "procedural", "feeding"),
    "/diet/live-vs-frozen-food": ("comparative", "C", "comparative", "food"),
    "/diet/overfeeding-and-impaction": ("diagnostic", "C", "problem-solving", "feeding"),
    "/diet/shrimp-for-axolotls": ("explanatory", "C", "definitional", "food"),
    "/diet/vitamin-and-supplement-needs": ("explanatory", "C", "informational", "nutrition"),
    # ---- health ----
    "/health": ("hub", "C", "navigational", "health"),
    "/health/ammonia-burns": ("diagnostic", "C", "diagnostic", "gill/skin damage"),
    "/health/black-tea-bath": ("procedural", "C", "procedural", "treatment"),
    "/health/curled-gills-stress-signal": ("diagnostic", "C", "diagnostic", "gill posture"),
    "/health/finding-an-exotic-vet": ("transactional", "O", "transactional", "veterinary"),
    "/health/fridging-sick-axolotl": ("procedural", "C", "procedural", "treatment"),
    "/health/fungal-infections-saprolegnia": ("diagnostic", "C", "diagnostic", "disease"),
    "/health/impaction-symptoms-treatment": ("diagnostic", "C", "diagnostic", "digestive"),
    "/health/limb-regeneration": ("explanatory", "A", "informational", "regeneration"),
    "/health/malnutrition-signs": ("diagnostic", "C", "diagnostic", "nutrition"),
    "/health/minor-scrapes-and-wounds": ("procedural", "C", "procedural", "treatment"),
    "/health/parasite-treatment": ("diagnostic", "C", "diagnostic", "disease"),
    "/health/quarantine-tub": ("procedural", "C", "procedural", "treatment"),
    "/health/red-leg-syndrome": ("diagnostic", "C", "diagnostic", "disease"),
    "/health/refusing-to-eat": ("diagnostic", "C", "diagnostic", "appetite"),
    "/health/salt-bath": ("procedural", "C", "procedural", "treatment"),
    "/health/shrinking-gills": ("diagnostic", "C", "diagnostic", "gill size"),
    "/health/stress-signs": ("diagnostic", "C", "diagnostic", "behavior"),
    "/health/why-axolotl-floating": ("diagnostic", "C", "diagnostic", "behavior"),
    # ---- morphs ----
    "/morphs": ("hub", "A", "navigational", "morph"),
    "/morphs/blue-and-pink-axolotl-myth": ("explanatory", "A", "definitional", "color"),
    "/morphs/chimera": ("explanatory", "A", "definitional", "morph"),
    "/morphs/copper": ("explanatory", "A", "definitional", "morph"),
    "/morphs/enigma-firefly-mac": ("explanatory", "A", "definitional", "morph"),
    "/morphs/gfp-axolotl": ("explanatory", "A", "definitional", "morph"),
    "/morphs/golden-albino": ("explanatory", "A", "definitional", "morph"),
    "/morphs/leucistic": ("explanatory", "A", "definitional", "morph"),
    "/morphs/melanoid": ("explanatory", "A", "definitional", "morph"),
    "/morphs/morphs-comparison-chart": ("comparative", "A", "comparative", "morph"),
    "/morphs/mosaic": ("explanatory", "A", "definitional", "morph"),
    "/morphs/piebald": ("explanatory", "A", "definitional", "morph"),
    "/morphs/pigment-cells": ("explanatory", "A", "informational", "pigment"),
    "/morphs/wild-type": ("explanatory", "A", "definitional", "morph"),
    # ---- breeding ----
    "/breeding": ("hub", "A", "navigational", "breeding"),
    "/breeding/breeding-triggers-temperature-cycling": ("procedural", "A", "procedural", "breeding"),
    "/breeding/color-genetics-punnett-squares": ("explanatory", "A", "informational", "genetics"),
    "/breeding/egg-and-larvae-care": ("procedural", "A", "procedural", "larvae"),
    "/breeding/genetics-and-inbreeding": ("explanatory", "A", "informational", "genetics"),
    "/breeding/raising-juveniles": ("procedural", "A", "procedural", "juveniles"),
    "/breeding/sexing-axolotls": ("procedural", "A", "procedural", "sex"),
    # ---- biology ----
    "/biology-and-science": ("hub", "A", "navigational", "biology"),
    "/biology-and-science/anatomy-gills-and-lungs": ("explanatory", "A", "definitional", "anatomy"),
    "/biology-and-science/axolotl-vs-tiger-salamander": ("comparative", "P", "comparative", "species"),
    "/biology-and-science/conservation-status": ("explanatory", "A", "informational", "conservation"),
    "/biology-and-science/is-axolotl-amphibian": ("explanatory", "A", "definitional", "taxonomy"),
    "/biology-and-science/lifespan-wild-vs-captivity": ("explanatory", "O", "informational", "longevity"),
    "/biology-and-science/neoteny": ("explanatory", "A", "definitional", "development"),
    "/biology-and-science/regeneration-and-limb-regrowth": ("explanatory", "A", "informational", "regeneration"),
    "/biology-and-science/wild-habitat-xochimilco": ("explanatory", "A", "informational", "habitat"),
    # ---- cost & buying ----
    "/cost-and-buying": ("hub", "O", "navigational", "cost"),
    "/cost-and-buying/axolotl-price-by-morph": ("transactional", "O", "transactional", "cost"),
    "/cost-and-buying/breeder-vs-pet-store": ("comparative", "O", "comparative", "source"),
    "/cost-and-buying/choosing-a-reputable-breeder": ("transactional", "O", "transactional", "source"),
    "/cost-and-buying/how-to-choose-a-healthy-axolotl": ("procedural", "O", "procedural", "source"),
    "/cost-and-buying/red-flags-when-buying": ("transactional", "O", "transactional", "source"),
    "/cost-and-buying/shipping-live-axolotls": ("procedural", "O", "procedural", "shipping"),
    # ---- legal ----
    "/legal": ("hub", "O", "navigational", "legality"),
    "/legal/california": ("location-specific", "O", "location-specific", "legality"),
    "/legal/canada": ("location-specific", "O", "location-specific", "legality"),
    "/legal/hawaii": ("location-specific", "O", "location-specific", "legality"),
    "/legal/maine": ("location-specific", "O", "location-specific", "legality"),
    "/legal/new-jersey": ("location-specific", "O", "location-specific", "legality"),
    "/legal/new-mexico": ("location-specific", "O", "location-specific", "legality"),
    "/legal/virginia": ("location-specific", "O", "location-specific", "legality"),
    # ---- culture ----
    "/axolotl-in-culture": ("hub", "P", "navigational", "culture"),
    "/axolotl-in-culture/adopt-me-axolotl-guide": ("procedural", "P", "procedural", "game"),
    "/axolotl-in-culture/axolotl-in-pop-culture-and-memes": ("explanatory", "P", "informational", "culture"),
    "/axolotl-in-culture/minecraft-axolotls-guide": ("procedural", "P", "procedural", "game"),
    "/axolotl-in-culture/why-axolotls-are-suddenly-popular": ("explanatory", "P", "informational", "culture"),
    # ---- gifts & merch ----
    "/gifts-and-merch": ("hub", "P", "navigational", "merch"),
    "/gifts-and-merch/axolotl-squishmallow-guide": ("transactional", "P", "transactional", "merch"),
    "/gifts-and-merch/best-axolotl-lego-sets": ("transactional", "P", "transactional", "merch"),
    "/gifts-and-merch/best-axolotl-toys-and-plushies": ("transactional", "P", "transactional", "merch"),
    "/gifts-and-merch/build-a-bear-axolotl-guide": ("transactional", "P", "transactional", "merch"),
    # ---- tools ----
    "/tools/feeding-schedule-generator": ("tool", "O", "tool/calculator", "feeding"),
    "/tools/nitrogen-cycle-tracker": ("tool", "O", "tool/calculator", "water"),
    "/tools/symptom-checker": ("tool", "O", "tool/calculator", "health"),
    "/tools/tank-size-calculator": ("tool", "O", "tool/calculator", "size"),
    "/tools/water-conditioner-dosage-calculator": ("tool", "O", "tool/calculator", "water"),
}

BORDERNAME = {"C": "CORE", "A": "ADJACENT", "O": "OUTER", "P": "PERIPHERAL", "X": "OUTSIDE", "M": "FUNCTIONAL"}

rows = []
flagged = []
for u in sorted(pages):
    p = pages[u]
    role, border, intent, attr = S.get(u, ("supporting", "X", "informational", "?"))
    cluster = [x for x in u.split("/") if x]
    cluster = "meta" if not cluster or cluster[0] in ("404.html", "about", "contact", "privacy", "search") else cluster[0]
    rows.append({
        "url": u, "title": p.get("title", "").strip(),
        "cluster": cluster, "role": role, "intent": intent,
        "attribute": attr, "border": BORDERNAME.get(border, border),
        "words": p.get("words"), "in": p.get("inbound_count", 0),
    })
    if u not in S:
        flagged.append(u)

with open(os.path.join(OUT, "page-roles.csv"), "w", encoding="utf-8") as fh:
    fh.write("url\ttitle\tcluster\trole\tprimary_intent\tprimary_attribute\tborder\twords\tcontent_in\n")
    for r in rows:
        fh.write("\t".join(str(r[k]) for k in
                 ("url", "title", "cluster", "role", "intent", "attribute", "border", "words", "in")) + "\n")

print("pages without assignment (should be empty):", flagged)
print("rows:", len(rows))