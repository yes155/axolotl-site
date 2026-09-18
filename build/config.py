# -*- coding: utf-8 -*-
"""
Site configuration. Maps every source .docx article into the
hub-and-spoke structure defined in axolotl_topical_map.xml.
"""

from pathlib import Path

# ── Site identity ──────────────────────────────────────────────────────────
# CHANGE THIS once you buy your domain:
SITE_URL = "https://myaxolotl.us"
SITE_NAME = "MyAxolotl"
SITE_TAGLINE = "Evidence-based axolotl care, tank setup, diet, and health guides."
SITE_LOGO = "/images/myaxolotl-logo-v3.webp"
SITE_FAVICON = "/images/axolotl-favicon.webp"
X_HANDLE = "@myaxolotls"
X_PROFILE_URL = "https://x.com/myaxolotls"

SOCIAL_LINKS = [
    ("Facebook", "https://www.facebook.com/myaxolotl.us/"),
    ("Instagram", "https://www.instagram.com/myaxolotl.us/"),
    ("Pinterest", "https://www.pinterest.com/myaxolotls/"),
    ("Discord", "https://discord.gg/MXUQwDgdgJ"),
]

ORGANIZATION_SAME_AS = [url for label, url in SOCIAL_LINKS if label != "Discord"] + [X_PROFILE_URL]

PEOPLE = {
    "author": {
        "name": "Farrukh Abdullah",
        "role": "Researcher & Writer",
        "slug": "authors/farrukh-abdullah",
        "meta": "Researcher and writer for MyAxolotl.",
        "summary": "Farrukh Abdullah researches and writes the MyAxolotl guides.",
        "focus": "Practical husbandry, tank setup, diet, and health explanations.",
        "links": [
            ("LinkedIn", "https://www.linkedin.com/in/farrukh-abdullah-5a218424/"),
            ("Email", "mailto:f.abdullah79@gmail.com"),
        ],
        "email": "f.abdullah79@gmail.com",
        "sameAs": ["https://www.linkedin.com/in/farrukh-abdullah-5a218424/"],
    },
    "editor": {
        "name": "Ananda Abidin",
        "role": "Editor",
        "slug": "editors/ananda-abidin",
        "meta": "Editor for MyAxolotl.",
        "summary": "Ananda Abidin edits MyAxolotl guides for clarity and editorial consistency.",
        "focus": "Editorial review, structure, and consistency.",
        "links": [
            ("LinkedIn", "https://www.linkedin.com/in/ananda-abidin/"),
        ],
        "sameAs": ["https://www.linkedin.com/in/ananda-abidin/"],
        "experience": [
            {
                "organization": "Axohub Indonesia",
                "role": "Content Writer & Video Editor",
                "dates": "May 2025 – November 2025",
                "duration": "7 months",
                "location": "Malang, East Java, Indonesia",
            },
        ],
    },
}

# Source folder containing the .docx articles
ROOT = Path(__file__).resolve().parent.parent
SOURCE_DIR = ROOT.parent / "axolotls"

# Article-specific hero assets live in the repository so external DOCX builds
# cannot replace them with generated placeholders. Add each approved hero here
# with descriptive metadata and an HTML text anchor for any fact in the image.
HERO_IMAGE_DIR = ROOT / "build" / "hero-images"
HERO_IMAGE_OVERRIDES = {
    "tank-setup/setup-guide": {
        "file": "2-axolotl-tank-setup.webp",
        "alt": (
            "Leucistic axolotl in a planted aquarium with fine sand, a hide, "
            "gentle filtration and cool-water equipment"
        ),
        "caption": (
            "A suitable axolotl tank provides ample floor space, cool dechlorinated "
            "water, an established biofilter, low flow, safe substrate and at least "
            "one hide."
        ),
        "description": (
            "Axolotl tank-setup hero showing a leucistic axolotl in a planted, "
            "filtered aquarium with fine sand and a hide."
        ),
        "credit": "MyAxolotl original graphic",
        "width": 1600,
        "height": 900,
    },
    "diet/best-foods-list": {
        "file": "16-best-foods-for-axolotls.webp",
        "alt": (
            "Dark axolotl above suitable food options including worms, shrimp "
            "and sinking pellets"
        ),
        "caption": (
            "Earthworms or nightcrawlers and suitable sinking axolotl pellets are "
            "dependable staples, while smaller foods such as blackworms or brine "
            "shrimp are more useful for juveniles."
        ),
        "description": (
            "Best-foods guide hero showing a dark axolotl with worms, shrimp and "
            "sinking pellets arranged below it."
        ),
        "credit": "MyAxolotl original graphic",
        "width": 1600,
        "height": 900,
    },
    "diet/feeding-schedule-by-age": {
        "file": "axolotl-feeding-frequency-by-life-stage.webp",
        "alt": (
            "Hatchling, juvenile and adult axolotls shown with age-specific foods "
            "and feeding frequencies"
        ),
        "caption": (
            "Hatchlings under 3 in (7.5 cm) eat 2–3 times daily, juveniles 3–7.5 "
            "in (7.5–19 cm) eat 1–3 times daily, and adults over 7.5 in (19 cm) "
            "eat every 2–3 days; offer head-width portions and remove leftovers "
            "within 3–5 minutes."
        ),
        "description": (
            "Axolotl feeding-frequency chart comparing hatchling, juvenile and "
            "adult schedules, portions and age-appropriate foods."
        ),
        "credit": "MyAxolotl original graphic",
        "width": 1600,
        "height": 900,
    },
    "axolotls/care-guide": {
        "file": "1-axolotl-care-guide-attached.webp",
        "alt": (
            "Dark wild-type axolotl in a planted aquarium with cool water, "
            "fine sand, a hide, filtration and feeding-care symbols"
        ),
        "caption": (
            "A suitable axolotl habitat combines cool stable water, an established "
            "biofilter, safe substrate and hides, with appropriate feeding and "
            "routine health observation."
        ),
        "description": (
            "Axolotl care-guide hero showing a wild-type axolotl in a complete "
            "aquarium with water-quality, habitat, feeding and health cues."
        ),
        "credit": "MyAxolotl original graphic",
        "width": 1600,
        "height": 900,
    },
    "tank-setup/live-vs-artificial-plants": {
        "file": "live-vs-artificial-plants.webp",
        "alt": (
            "Leucistic axolotl in a split aquarium comparing live green plants "
            "with soft artificial plants"
        ),
        "caption": (
            "Live plants can absorb some nitrate and provide cover, while soft "
            "artificial plants offer low-maintenance shelter without lighting or "
            "fertilizer needs; avoid sharp plastic edges."
        ),
        "description": (
            "Split-tank comparison of live and artificial plants for an axolotl "
            "aquarium."
        ),
        "credit": "MyAxolotl original graphic",
        "width": 1600,
        "height": 900,
    },
    "tank-setup/temperature": {
        "file": "axolotl-tank-temperature.webp",
        "alt": (
            "Blue axolotl in a cooled aquarium with a fan, thermometer and "
            "aquarium chiller"
        ),
        "caption": (
            "Aim for stable water around 60–64°F (16–18°C); sustained temperatures "
            "above 68°F (20°C) increase stress, so reliably warm rooms may require "
            "a chiller."
        ),
        "description": (
            "Axolotl tank-cooling graphic showing target temperature, thermometer, "
            "fan and chiller."
        ),
        "credit": "MyAxolotl original graphic",
        "width": 1600,
        "height": 900,
    },
    "tank-setup/canister-vs-sponge-filter": {
        "file": "canister-vs-sponge-filter.webp",
        "alt": (
            "Sponge and canister filters compared beside two wild-type axolotls"
        ),
        "caption": (
            "Sponge filters offer gentle biological filtration, while canisters "
            "suit larger systems when their output is baffled or dispersed to "
            "prevent strong current."
        ),
        "description": (
            "Sponge-filter versus canister-filter comparison for axolotl tanks."
        ),
        "credit": "MyAxolotl original graphic",
        "width": 1600,
        "height": 900,
    },
    "tank-setup/gravel-risks": {
        "file": "axolotl-sharp-gravel-risks.webp",
        "alt": (
            "Leucistic axolotl on fine sand compared with a dark axolotl on "
            "sharp gravel"
        ),
        "caption": (
            "Fine sand under 1 mm is safer for suitably sized axolotls, while "
            "gravel and other swallowable stones can cause impaction; bare-bottom "
            "tanks are another safe option."
        ),
        "description": (
            "Side-by-side comparison of fine sand and sharp gravel in axolotl "
            "tanks, highlighting gravel-ingestion and impaction risk."
        ),
        "credit": "MyAxolotl original graphic",
        "width": 1600,
        "height": 900,
    },
    "tank-setup/uneaten-food-and-ammonia": {
        "file": "uneaten-food-and-ammonia.webp",
        "alt": (
            "Wild-type axolotl below a four-step diagram showing how uneaten food "
            "raises ammonia"
        ),
        "caption": (
            "Remove leftovers promptly because decaying food adds waste and can "
            "drive ammonia above the required 0 ppm."
        ),
        "description": (
            "Uneaten-food and ammonia pathway graphic for an axolotl aquarium."
        ),
        "credit": "MyAxolotl original graphic",
        "width": 1600,
        "height": 900,
    },
    "tank-setup/filtration-for-axolotls": {
        "file": "axolotl-tank-filtration.webp",
        "alt": (
            "Wild-type axolotl in a filtered aquarium with sponge, baffled "
            "hang-on-back and canister filter examples"
        ),
        "caption": (
            "Choose filtration for the tank’s volume and waste load, prioritize "
            "biological capacity, and baffle or disperse the outlet to keep flow "
            "gentle."
        ),
        "description": (
            "Axolotl filtration guide comparing sponge, hang-on-back and canister "
            "filters."
        ),
        "credit": "MyAxolotl original graphic",
        "width": 1600,
        "height": 900,
    },
    "tank-setup/hides-and-caves": {
        "file": "axolotl-hides-and-caves.webp",
        "alt": (
            "Leucistic axolotl beside terracotta pot, slate cave and smooth PVC "
            "tunnel hides"
        ),
        "caption": (
            "Provide at least one dark, enclosed hide per axolotl and choose smooth "
            "terracotta, slate or PVC without sharp edges."
        ),
        "description": (
            "Axolotl hide comparison showing a terracotta pot, slate cave and PVC "
            "tunnel."
        ),
        "credit": "MyAxolotl original graphic",
        "width": 1600,
        "height": 900,
    },
    "tank-setup/why-tank-water-smells": {
        "file": "axolotl-tank-water-smell.webp",
        "alt": (
            "Leucistic axolotl with examples of a filter, dirty substrate, waste "
            "and a water test vial"
        ),
        "caption": (
            "A healthy aquarium may smell faintly earthy; strong odors call for "
            "water testing and checks for trapped waste, uneaten food and dirty "
            "filter media."
        ),
        "description": (
            "Axolotl tank-odor troubleshooting graphic showing common sources and "
            "water testing."
        ),
        "credit": "MyAxolotl original graphic",
        "width": 1600,
        "height": 900,
    },
    "tank-setup/lighting-for-axolotls": {
        "file": "axolotl-tank-lighting.webp",
        "alt": (
            "Dark axolotl in a planted tank with day and night lux-meter readings "
            "and a timer"
        ),
        "caption": (
            "Use low, indirect light and a consistent 10–12-hour daytime "
            "photoperiod, leaving the tank dark at night and providing hides."
        ),
        "description": (
            "Axolotl lighting guide showing low daytime light, darkness at night "
            "and a timer."
        ),
        "credit": "MyAxolotl original graphic",
        "width": 1600,
        "height": 900,
    },
    "tank-setup/substrate-and-impaction": {
        "file": "axolotl-substrate-and-impaction.webp",
        "alt": (
            "Wild-type and leucistic axolotls above examples of fine sand, bare "
            "bottom, gravel and large pebbles"
        ),
        "caption": (
            "Fine sand under 1 mm is the safer loose substrate for suitably sized "
            "axolotls; bare-bottom tanks work for juveniles or quarantine, while "
            "gravel and swallowable stones pose impaction risk."
        ),
        "description": (
            "Axolotl substrate comparison showing fine sand, bare bottom, gravel "
            "and large pebbles."
        ),
        "credit": "MyAxolotl original graphic",
        "width": 1600,
        "height": 900,
    },
    "axolotl-in-culture/adopt-me-axolotl-guide": {
        "file": "adopt-me-axolotl-guide.webp",
        "alt": (
            "Pink virtual Adopt Me axolotl beside notes about legendary rarity, "
            "trading, neon forms and the care needs of real axolotls"
        ),
        "caption": (
            "The Adopt Me axolotl was introduced as a premium Pet Shop pet. "
            "Players currently obtain it mainly through trading unless the game "
            "returns it to the shop; availability and trade value can change."
        ),
        "description": (
            "Adopt Me axolotl guide graphic explaining current acquisition, "
            "virtual forms and the difference between a game pet and real care."
        ),
        "credit": "MyAxolotl original graphic",
        "width": 1600,
        "height": 900,
    },
    "axolotl-in-culture/axolotl-in-pop-culture-and-memes": {
        "file": "axolotl-pop-culture-and-memes.webp",
        "alt": (
            "Leucistic axolotl surrounded by examples of games, memes, media, "
            "merchandise and science coverage"
        ),
        "caption": (
            "Axolotls circulate between games, memes, merchandise and science "
            "coverage. Their recognizable gills and apparent smile make them easy "
            "to adapt into friendly characters and reaction images."
        ),
        "description": (
            "Axolotl pop-culture graphic connecting games, memes, merchandise, "
            "media and science attention."
        ),
        "credit": "MyAxolotl original graphic",
        "width": 1600,
        "height": 900,
    },
    "axolotl-in-culture/minecraft-axolotls-guide": {
        "file": "minecraft-axolotls-guide.webp",
        "alt": (
            "Minecraft-style axolotls in five colors with lush-cave spawning, "
            "blue-variant breeding and water-bucket guidance"
        ),
        "caption": (
            "Minecraft axolotls spawn in water in lush caves and appear in five "
            "color variants. The rare blue variant is obtained through breeding, "
            "with a 1-in-1,200 chance for each baby."
        ),
        "description": (
            "Minecraft axolotl guide graphic covering lush-cave spawning, five "
            "colors, the rare blue variant and bucket collection."
        ),
        "credit": "MyAxolotl original graphic",
        "width": 1600,
        "height": 900,
    },
    "axolotl-in-culture/why-axolotls-are-suddenly-popular": {
        "file": "why-axolotls-are-popular.webp",
        "alt": (
            "Wild-type axolotl with four popularity factors: Minecraft, internet "
            "memes, regeneration science and endangered status"
        ),
        "caption": (
            "Axolotl popularity grew through the 2021 Minecraft update, a highly "
            "recognizable face, continuing regeneration research and public concern "
            "for a species listed as Critically Endangered in the wild."
        ),
        "description": (
            "Axolotl-popularity timeline combining gaming, internet culture, "
            "regeneration science and conservation awareness."
        ),
        "credit": "MyAxolotl original graphic",
        "width": 1600,
        "height": 900,
    },
    "diet/beef-heart": {
        "file": "axolotl-beef-heart-feeding-warning.webp",
        "alt": (
            "Wild-type axolotl beside beef heart with guidance to offer it only "
            "occasionally and choose earthworms or axolotl pellets instead"
        ),
        "caption": (
            "Beef heart is not suitable as a staple axolotl food because its "
            "calcium-to-phosphorus balance is poor. Use earthworms or "
            "axolotl-formulated pellets for routine feeding."
        ),
        "description": (
            "Educational axolotl feeding graphic explaining why beef heart "
            "should be occasional rather than a staple food."
        ),
        "credit": "MyAxolotl original graphic",
        "width": 1600,
        "height": 900,
    },
    "diet/overfeeding-and-impaction": {
        "file": "axolotl-obesity-body-condition-guide.webp",
        "alt": (
            "Wild-type axolotl beside a food bowl and guidance on healthy body "
            "proportions, adult feeding frequency and occasional high-fat treats"
        ),
        "caption": (
            "Assess body condition from above after digestion: a healthy "
            "abdomen is approximately as wide as the head. Most adults maintain "
            "condition on two or three meals per week, with high-fat foods kept "
            "as occasional treats."
        ),
        "description": (
            "Educational axolotl-obesity graphic showing body-proportion, "
            "adult feeding-frequency and high-fat treat guidance."
        ),
        "credit": "MyAxolotl original graphic",
        "width": 1600,
        "height": 900,
    },
    "morphs/blue-and-pink-axolotl-myth": {
        "file": "axolotl-blue-pink-color-myth.webp",
        "alt": (
            "Pale axolotl under blue aquarium lighting beside an explanation "
            "that no true blue axolotl morph is recognized"
        ),
        "caption": (
            "No established axolotl morph is naturally bright blue. Blue-looking "
            "photos usually result from colored lighting or editing, while pink "
            "appearance is common in pale leucistic and albino morphs."
        ),
        "description": (
            "Myth-busting axolotl color graphic distinguishing lighting effects "
            "from recognized pale morphs."
        ),
        "credit": "MyAxolotl original graphic",
        "width": 1600,
        "height": 900,
    },
    "morphs/chimera": {
        "file": "chimera-axolotl-bilateral-color-split.webp",
        "alt": (
            "Split-colored chimera axolotl illustrating two genetically distinct "
            "cell populations divided along the body"
        ),
        "caption": (
            "A chimera can form when two early embryos fuse, producing genetically "
            "distinct cell populations. It is a developmental event rather than a "
            "predictably inherited morph."
        ),
        "description": (
            "Educational chimera axolotl graphic showing a bilateral color split "
            "and its developmental origin."
        ),
        "credit": "MyAxolotl original graphic",
        "width": 1600,
        "height": 900,
    },
    "morphs/copper": {
        "file": "copper-axolotl-morph.webp",
        "alt": (
            "Copper axolotl with an orange-brown body, reddish gills and pale eyes "
            "beside recessive color-genetics notes"
        ),
        "caption": (
            "Copper axolotls have a warm orange-brown appearance associated with "
            "recessive variation affecting melanin production. Their husbandry is "
            "the same as for other axolotl color morphs."
        ),
        "description": (
            "Copper axolotl morph profile showing its characteristic color, eyes "
            "and recessive inheritance."
        ),
        "credit": "MyAxolotl original graphic",
        "width": 1600,
        "height": 900,
    },
    "morphs/enigma-firefly-mac": {
        "file": "rare-axolotl-morphs-enigma-firefly-mac.webp",
        "alt": (
            "Rare axolotl appearance comparison labeled Enigma, firefly and MAC "
            "with notes on origin and inheritance"
        ),
        "caption": (
            "Names such as Enigma, firefly and MAC describe different rare "
            "appearances or breeding lines. Firefly is produced through tissue "
            "grafting and is not a standard heritable color morph."
        ),
        "description": (
            "Comparison graphic explaining three rare axolotl appearance labels "
            "and why their origins and inheritance differ."
        ),
        "credit": "MyAxolotl original graphic",
        "width": 1600,
        "height": 900,
    },
    "morphs/gfp-axolotl": {
        "file": "gfp-axolotl-uv-fluorescence.webp",
        "alt": (
            "GFP axolotl fluorescing green under blue light beside notes about "
            "the dominant transgene and normal routine care"
        ),
        "caption": (
            "The GFP transgene produces green fluorescence under suitable blue "
            "excitation light. A GFP axolotl has the same routine husbandry needs "
            "as other morphs and does not require special lighting."
        ),
        "description": (
            "GFP axolotl graphic explaining blue-light fluorescence, transgene "
            "inheritance and ordinary husbandry needs."
        ),
        "credit": "MyAxolotl original graphic",
        "width": 1600,
        "height": 900,
    },
    "morphs/golden-albino": {
        "file": "golden-albino-axolotl-morph.webp",
        "alt": (
            "Golden albino axolotl with a yellow-gold body, pink gills and pale "
            "red eyes beside pigment notes"
        ),
        "caption": (
            "Golden albinos lack dark melanin but retain yellow pigment, producing "
            "a gold body and pale red eyes. Color does not change their core "
            "husbandry requirements."
        ),
        "description": (
            "Golden albino axolotl morph profile showing its yellow pigment, pale "
            "eyes and standard care needs."
        ),
        "credit": "MyAxolotl original graphic",
        "width": 1600,
        "height": 900,
    },
    "morphs/leucistic": {
        "file": "leucistic-axolotl-morph.webp",
        "alt": (
            "Leucistic axolotl with a pale body, dark eyes and pink external gills "
            "beside identifying features"
        ),
        "caption": (
            "Leucistic axolotls have reduced body pigmentation but retain dark "
            "eyes. The dark eyes help distinguish them from albino morphs."
        ),
        "description": (
            "Leucistic axolotl morph profile highlighting its pale body, dark eyes "
            "and pink gills."
        ),
        "credit": "MyAxolotl original graphic",
        "width": 1600,
        "height": 900,
    },
    "morphs/melanoid": {
        "file": "melanoid-axolotl-morph.webp",
        "alt": (
            "Dark melanoid axolotl with an even black-brown body and no metallic "
            "eye ring beside pigment-cell notes"
        ),
        "caption": (
            "Melanoid axolotls have abundant dark pigment and lack reflective "
            "iridophores, so they do not show the metallic shine or gold eye ring "
            "typical of a wild type."
        ),
        "description": (
            "Melanoid axolotl morph profile showing uniform dark pigmentation and "
            "the absence of reflective iridophores."
        ),
        "credit": "MyAxolotl original graphic",
        "width": 1600,
        "height": 900,
    },
    "morphs/morphs-comparison-chart": {
        "file": "axolotl-morph-comparison-chart.webp",
        "alt": (
            "Comparison chart of wild type, leucistic, melanoid, golden albino, "
            "copper, GFP, piebald, mosaic and chimera axolotls"
        ),
        "caption": (
            "Compare axolotl appearances by body and eye color, reflective shine, "
            "fluorescence and pattern distribution. Rarity and individual patterns "
            "can vary between breeding populations."
        ),
        "description": (
            "Nine-panel axolotl morph comparison chart covering common colors, "
            "fluorescent GFP and uncommon patterned appearances."
        ),
        "credit": "MyAxolotl original graphic",
        "width": 1600,
        "height": 900,
    },
    "morphs/mosaic": {
        "file": "mosaic-axolotl-morph.webp",
        "alt": (
            "Mosaic axolotl with irregular dark and pale patches beside notes on "
            "cell populations and inheritance"
        ),
        "caption": (
            "Mosaic axolotls show irregular patchwork from genetically different "
            "cell populations. The pattern is not predictably inherited, and "
            "appearance alone cannot confirm its developmental mechanism."
        ),
        "description": (
            "Mosaic axolotl profile showing irregular color patches and explaining "
            "their variable developmental origin."
        ),
        "credit": "MyAxolotl original graphic",
        "width": 1600,
        "height": 900,
    },
    "morphs/piebald": {
        "file": "piebald-axolotl-morph.webp",
        "alt": (
            "Piebald axolotl with a dark base and irregular unpigmented patches "
            "beside comparison notes"
        ),
        "caption": (
            "Piebald patterning combines pigmented and unpigmented areas. It differs "
            "from a dirty leucistic's pale base with dark spots and from a chimera's "
            "often bilateral division."
        ),
        "description": (
            "Piebald axolotl profile explaining its contrasting patches and how it "
            "differs from dirty leucistic and chimera appearances."
        ),
        "credit": "MyAxolotl original graphic",
        "width": 1600,
        "height": 900,
    },
    "morphs/pigment-cells": {
        "file": "axolotl-pigment-cells-color-genetics.webp",
        "alt": (
            "Wild-type axolotl with callouts for melanophores, xanthophores and "
            "reflective iridophores"
        ),
        "caption": (
            "Axolotl color comes from three main pigment-cell groups: dark "
            "melanophores, yellow-orange xanthophores and reflective iridophores."
        ),
        "description": (
            "Axolotl pigment-cell diagram identifying the three chromatophore "
            "groups that combine to produce color and shine."
        ),
        "credit": "MyAxolotl original graphic",
        "width": 1600,
        "height": 900,
    },
    "morphs/wild-type": {
        "file": "wild-type-axolotl-natural-color.webp",
        "alt": (
            "Wild-type axolotl with olive-brown skin, dark and yellow speckles and "
            "a reflective gold eye ring"
        ),
        "caption": (
            "Wild-type axolotls combine dark melanophores, yellow xanthophores and "
            "reflective iridophores. The resulting olive-brown pattern and gold eye "
            "ring distinguish them from melanoids."
        ),
        "description": (
            "Wild-type axolotl morph profile showing natural camouflage colors, "
            "speckling and reflective eye-ring features."
        ),
        "credit": "MyAxolotl original graphic",
        "width": 1600,
        "height": 900,
    },
    "breeding/breeding-triggers-temperature-cycling": {
        "file": "axolotl-breeding-temperature-cycling.webp",
        "alt": (
            "Adult axolotls in a breeding tank beside seasonal temperature and "
            "day-length cues for courtship"
        ),
        "caption": (
            "Stable seasonal changes in water temperature and day length can "
            "coincide with axolotl courtship. Avoid abrupt thermal shocks and "
            "keep breeding animals within safe husbandry conditions."
        ),
        "description": (
            "Axolotl breeding-cue graphic showing a conditioned pair, gradual "
            "seasonal changes and temperature-safety guidance."
        ),
        "credit": "MyAxolotl original graphic",
        "width": 1600,
        "height": 900,
    },
    "breeding/color-genetics-punnett-squares": {
        "file": "axolotl-color-genetics-punnett-square.webp",
        "alt": (
            "Four axolotl color morphs beside a Punnett square explaining "
            "dominant, recessive and carrier inheritance"
        ),
        "caption": (
            "A Punnett square models one gene at a time. For a single recessive "
            "trait, two carriers predict a 25 percent homozygous-recessive chance "
            "per offspring, not a guaranteed clutch ratio."
        ),
        "description": (
            "Axolotl color-genetics graphic combining multiple morphs with a "
            "single-locus Punnett-square example."
        ),
        "credit": "MyAxolotl original graphic",
        "width": 1600,
        "height": 900,
    },
    "breeding/egg-and-larvae-care": {
        "file": "axolotl-eggs-larvae-care.webp",
        "alt": (
            "Developing axolotl embryos inside eggs beside incubation, water-care "
            "and first-food guidance"
        ),
        "caption": (
            "Axolotl embryo development speeds up as incubation temperature rises. "
            "Keep the water clean, inspect eggs daily, and prepare live food before "
            "the larvae finish absorbing their yolk."
        ),
        "description": (
            "Axolotl egg-and-larvae graphic showing developing embryos, incubation "
            "care and the transition to live baby brine shrimp."
        ),
        "credit": "MyAxolotl original graphic",
        "width": 1600,
        "height": 900,
    },
    "breeding/genetics-and-inbreeding": {
        "file": "axolotl-genetic-diversity-inbreeding-risk.webp",
        "alt": (
            "Leucistic axolotl beside a pedigree chart and genetic-diversity "
            "guidance for breeding decisions"
        ),
        "caption": (
            "The historic laboratory axolotl population began with a small founder "
            "group. Appearance cannot reveal relatedness, so pedigree records and "
            "healthy, unrelated breeding stock matter."
        ),
        "description": (
            "Axolotl genetic-diversity graphic using a pedigree to explain founder "
            "effects, inbreeding risk and responsible pair selection."
        ),
        "credit": "MyAxolotl original graphic",
        "width": 1600,
        "height": 900,
    },
    "breeding/raising-juveniles": {
        "file": "raising-baby-axolotls-growth-stages.webp",
        "alt": (
            "Several juvenile axolotls at different sizes beside feeding, size "
            "separation and growth-stage guidance"
        ),
        "caption": (
            "Newly feeding larvae need appropriately sized live food. Grade growing "
            "juveniles by size to reduce biting, maintain clean water, and rehome "
            "only after feeding and growth are stable."
        ),
        "description": (
            "Juvenile axolotl growth graphic showing multiple animals with first "
            "foods, size separation, limb development and rehoming milestones."
        ),
        "credit": "MyAxolotl original graphic",
        "width": 1600,
        "height": 900,
    },
    "breeding/sexing-axolotls": {
        "file": "male-female-axolotl-sexing-guide.webp",
        "alt": (
            "Adult male and female axolotls viewed from above with their cloacae "
            "highlighted for comparison"
        ),
        "caption": (
            "A mature male develops an enlarged, side-bulging cloaca. A small cloaca "
            "can indicate a female or an immature animal, and body shape alone is "
            "not a reliable sexing method."
        ),
        "description": (
            "Male-versus-female axolotl sexing graphic focused on the cloaca while "
            "warning against decisions based only on body shape."
        ),
        "credit": "MyAxolotl original graphic",
        "width": 1600,
        "height": 900,
    },
    "care-basics/are-axolotls-good-beginner-pets": {
        "file": "are-axolotls-good-beginner-pets.webp",
        "alt": (
            "Leucistic axolotl in a filtered aquarium beside a beginner-readiness "
            "checklist for temperature and long-term care"
        ),
        "caption": (
            "Axolotls can suit prepared beginners who can cycle the aquarium, "
            "maintain cool stable water, and commit to long-term care. They are "
            "not a low-maintenance impulse pet."
        ),
        "description": (
            "Beginner axolotl care graphic showing a leucistic animal, filter, "
            "thermometer and preparation checklist."
        ),
        "credit": "MyAxolotl original graphic",
        "width": 1600,
        "height": 900,
    },
    "care-basics/axolotl-age-and-size-chart": {
        "file": "axolotl-age-and-size-chart.webp",
        "alt": (
            "Four axolotl growth stages aligned with a ruler from larva through "
            "juvenile, subadult and adult"
        ),
        "caption": (
            "Measure from snout to tail tip. Size varies with genetics, diet, "
            "temperature, health, and individual growth, so stage labels are "
            "approximate rather than deadlines."
        ),
        "description": (
            "Axolotl age-and-size chart comparing larval, juvenile, subadult and "
            "adult growth stages against a measurement scale."
        ),
        "credit": "MyAxolotl original graphic",
        "width": 1600,
        "height": 900,
    },
    "care-basics/axolotl-facts": {
        "file": "amazing-axolotl-facts.webp",
        "alt": (
            "Wild-type axolotl in a Xochimilco collage with fact icons for "
            "amphibian identity, neoteny, regeneration and conservation"
        ),
        "caption": (
            "Axolotls are fully aquatic salamanders native to Xochimilco. They "
            "retain larval traits as adults, can regenerate complex tissues, and "
            "remain critically endangered in the wild."
        ),
        "description": (
            "Axolotl fact graphic connecting the species with Xochimilco, "
            "amphibian biology, neoteny, regeneration and wild conservation."
        ),
        "credit": "MyAxolotl original graphic",
        "width": 1600,
        "height": 900,
    },
    "care-basics/axolotl-intelligence-and-bonding": {
        "file": "axolotl-owner-recognition.webp",
        "alt": (
            "Copper axolotl approaching its keeper beside notes on associative "
            "learning, routines and owner recognition"
        ),
        "caption": (
            "Axolotls can learn feeding cues and become responsive to a familiar "
            "keeper's movement and routine. This is associative learning, not "
            "evidence of mammal-like attachment."
        ),
        "description": (
            "Axolotl owner-recognition graphic explaining learned feeding cues, "
            "familiar routines and the limits of bonding claims."
        ),
        "credit": "MyAxolotl original graphic",
        "width": 1600,
        "height": 900,
    },
    "care-basics/axolotls-and-children": {
        "file": "axolotls-as-pets-for-kids.webp",
        "alt": (
            "Child and adult observing a leucistic axolotl aquarium beside "
            "supervision and no-handling guidance"
        ),
        "caption": (
            "An axolotl can be a family pet when an adult manages water quality, "
            "feeding, and equipment. Children should observe rather than handle "
            "the animal."
        ),
        "description": (
            "Family axolotl-care graphic showing a child and adult observing the "
            "tank with supervision and handling-safety reminders."
        ),
        "credit": "MyAxolotl original graphic",
        "width": 1600,
        "height": 900,
    },
    "care-basics/behavior": {
        "file": "axolotl-behavior-guide.webp",
        "alt": (
            "Melanoid axolotls demonstrating resting, hiding, nocturnal activity "
            "and frantic-swimming behavior"
        ),
        "caption": (
            "Resting and hiding can be normal, especially during the day. Sudden "
            "frantic swimming is a reason to check water quality, temperature, "
            "flow, and other stressors."
        ),
        "description": (
            "Axolotl behavior graphic comparing normal resting and hiding with "
            "activity patterns and a possible stress response."
        ),
        "credit": "MyAxolotl original graphic",
        "width": 1600,
        "height": 900,
    },
    "care-basics/cost-of-ownership-monthly": {
        "file": "axolotl-monthly-ownership-cost.webp",
        "alt": (
            "Golden albino axolotl aquarium beside monthly expense categories for "
            "food, conditioner, supplies and emergency savings"
        ),
        "caption": (
            "Monthly costs vary by location, tank equipment, electricity rates, "
            "diet, and health needs. Plan for routine supplies plus an emergency "
            "reserve instead of treating one price as universal."
        ),
        "description": (
            "Axolotl ownership-cost graphic organizing recurring expenses into "
            "food, water care, supplies and emergency-fund categories."
        ),
        "credit": "MyAxolotl original graphic",
        "width": 1600,
        "height": 900,
    },
    "care-basics/handling": {
        "file": "how-to-handle-an-axolotl-safely.webp",
        "alt": (
            "Wild-type axolotl being transferred in water beside container, "
            "minimal-handling and bare-hand safety guidance"
        ),
        "caption": (
            "Avoid routine bare-hand handling. When movement is necessary, a "
            "water-filled container is generally the safest first choice; keep "
            "any transfer brief and protect the gills and limbs."
        ),
        "description": (
            "Axolotl transfer-safety graphic emphasizing a water-filled container, "
            "minimal handling time and protection of delicate skin and gills."
        ),
        "credit": "MyAxolotl original graphic",
        "width": 1600,
        "height": 900,
    },
    "care-basics/how-to-pronounce-axolotl": {
        "file": "how-to-pronounce-axolotl.webp",
        "alt": (
            "Leucistic axolotl beside the modern English pronunciation "
            "ACK-suh-lot-ul and notes that Nahuatl and Spanish differ"
        ),
        "caption": (
            "Modern English commonly uses ACK-suh-lot-ul. The Nahuatl source word "
            "and Spanish ajolote have different pronunciations, so they should not "
            "be presented as one universal form."
        ),
        "description": (
            "Axolotl pronunciation graphic separating the common modern English "
            "form from the related Nahuatl and Spanish forms."
        ),
        "credit": "MyAxolotl original graphic",
        "width": 1600,
        "height": 900,
    },
    "care-basics/keeping-multiple-axolotls": {
        "file": "can-axolotls-live-together.webp",
        "alt": (
            "Three similarly sized axolotls in an aquarium with multiple hides "
            "beside cohabitation safety checks"
        ),
        "caption": (
            "Cohabitation depends on comparable body size, adequate floor space, "
            "multiple hides, consistent feeding, and close monitoring. Separate "
            "animals if biting or persistent stress occurs."
        ),
        "description": (
            "Axolotl cohabitation graphic showing similarly sized animals, several "
            "hides, adequate space and monitoring for biting or stress."
        ),
        "credit": "MyAxolotl original graphic",
        "width": 1600,
        "height": 900,
    },
    "biology-and-science/anatomy-gills-and-lungs": {
        "file": "axolotl-anatomy-gills-lungs.webp",
        "alt": (
            "Leucistic axolotl with labeled external gills, lungs and "
            "skin-based oxygen absorption"
        ),
        "caption": (
            "Axolotls exchange gases through external gills, skin and simple "
            "lungs. Gill movement can increase water flow, while occasional "
            "surface gulps use the lungs."
        ),
        "description": (
            "Axolotl respiratory-anatomy graphic labeling external gills, "
            "internal lungs and oxygen-absorbing skin."
        ),
        "credit": "MyAxolotl original graphic",
        "width": 1600,
        "height": 900,
    },
    "biology-and-science/axolotl-vs-tiger-salamander": {
        "file": "axolotl-vs-tiger-salamander.webp",
        "alt": (
            "Aquatic axolotl beside a terrestrial tiger salamander with "
            "neoteny and metamorphosis differences"
        ),
        "caption": (
            "Axolotls normally remain aquatic and retain larval traits, while "
            "tiger salamanders typically metamorphose into terrestrial adults. "
            "They are related but distinct species."
        ),
        "description": (
            "Axolotl-versus-tiger-salamander comparison showing different "
            "adult forms, habitats and developmental pathways."
        ),
        "credit": "MyAxolotl original graphic",
        "width": 1600,
        "height": 900,
    },
    "biology-and-science/conservation-status": {
        "file": "axolotl-conservation-status.webp",
        "alt": (
            "Wild-type axolotl in Xochimilco beside Critically Endangered "
            "status, habitat threats and range map"
        ),
        "caption": (
            "Wild axolotls are restricted to Xochimilco and classified as "
            "Critically Endangered. Habitat degradation, pollution and "
            "invasive fish continue to threaten the remaining population."
        ),
        "description": (
            "Axolotl conservation graphic connecting the IUCN status with "
            "Xochimilco, habitat loss and invasive-species pressure."
        ),
        "credit": "MyAxolotl original graphic",
        "width": 1600,
        "height": 900,
    },
    "biology-and-science/is-axolotl-amphibian": {
        "file": "axolotl-amphibian-classification.webp",
        "alt": (
            "Golden axolotl beside an amphibian classification chart and "
            "features that distinguish it from fish"
        ),
        "caption": (
            "The axolotl is an amphibian: a salamander in the order Caudata. "
            "It remains fully aquatic and retains larval features as a "
            "reproductive adult."
        ),
        "description": (
            "Axolotl classification graphic identifying the species as a "
            "neotenic aquatic salamander rather than a fish."
        ),
        "credit": "MyAxolotl original graphic",
        "width": 1600,
        "height": 900,
    },
    "biology-and-science/lifespan-wild-vs-captivity": {
        "file": "axolotl-lifespan-wild-vs-captivity.webp",
        "alt": (
            "Captive leucistic axolotl and wild-type axolotl compared on "
            "lifespan timelines and environmental pressures"
        ),
        "caption": (
            "Lifespan estimates vary. Captive axolotls often live longer when "
            "temperature, water quality, diet and veterinary care are stable; "
            "wild animals face habitat and predation pressures."
        ),
        "description": (
            "Wild-versus-captive axolotl lifespan comparison emphasizing "
            "husbandry and environmental factors rather than guaranteed ages."
        ),
        "credit": "MyAxolotl original graphic",
        "width": 1600,
        "height": 900,
    },
    "biology-and-science/regeneration-and-limb-regrowth": {
        "file": "axolotl-regeneration-science.webp",
        "alt": (
            "Axolotl limb regeneration sequence showing wound closure, "
            "blastema formation, patterning and growth"
        ),
        "caption": (
            "Axolotl regeneration proceeds through wound closure, formation "
            "of a blastema, tissue patterning and growth. Regeneration is "
            "powerful but not unlimited, and injury prevention remains essential."
        ),
        "description": (
            "Scientific axolotl-regeneration graphic illustrating the major "
            "stages of limb regrowth and biological limits."
        ),
        "credit": "MyAxolotl original graphic",
        "width": 1600,
        "height": 900,
    },
    "biology-and-science/neoteny": {
        "file": "axolotl-neoteny-explained.webp",
        "alt": (
            "Axolotl neoteny diagram comparing retained larval traits with "
            "salamander metamorphosis"
        ),
        "caption": (
            "Neoteny allows an axolotl to reach sexual maturity while retaining "
            "larval traits such as external gills, a finned tail and an aquatic "
            "lifestyle."
        ),
        "description": (
            "Axolotl neoteny graphic comparing its lifelong larval features "
            "with the metamorphic pathway of other salamanders."
        ),
        "credit": "MyAxolotl original graphic",
        "width": 1600,
        "height": 900,
    },
    "biology-and-science/wild-habitat-xochimilco": {
        "file": "axolotl-wild-habitat-xochimilco.webp",
        "alt": (
            "Wild-type axolotl in a Xochimilco canal beside a Mexico City map "
            "and habitat features"
        ),
        "caption": (
            "Wild axolotls are native to the Xochimilco canal system south of "
            "Mexico City. Shallow vegetated water, chinampa landscapes and "
            "remaining refuges define this restricted habitat."
        ),
        "description": (
            "Axolotl habitat graphic showing Xochimilco's location, canals, "
            "vegetation and the species' narrow native range."
        ),
        "credit": "MyAxolotl original graphic",
        "width": 1600,
        "height": 900,
    },
    "legal/california": {
        "file": "axolotl-legal-california.webp",
        "alt": (
            "California axolotl ownership graphic showing restricted-species "
            "permit rules and a CDFW verification reminder"
        ),
        "caption": (
            "California treats axolotls as restricted wildlife. CDFW does not "
            "issue restricted-species permits for ordinary pet ownership; verify "
            "current state and local rules before acting."
        ),
        "description": (
            "California axolotl legality infographic summarizing restricted "
            "status, permit limits and current-rule verification."
        ),
        "credit": "MyAxolotl original graphic",
        "width": 1600,
        "height": 900,
    },
    "legal/canada": {
        "file": "axolotl-legal-canada.webp",
        "alt": (
            "Canada map beside an axolotl and guidance that ownership rules "
            "vary by province and locality"
        ),
        "caption": (
            "Axolotls are legal to own in most of Canada, but provincial, "
            "municipal, import and cross-border requirements can differ. Confirm "
            "the current rules for your location and source."
        ),
        "description": (
            "Canada axolotl ownership graphic emphasizing provincial variation, "
            "captive-bred sourcing and possible import requirements."
        ),
        "credit": "MyAxolotl original graphic",
        "width": 1600,
        "height": 900,
    },
    "legal/hawaii": {
        "file": "axolotl-legal-hawaii.webp",
        "alt": (
            "Hawaii axolotl law graphic showing prohibited ownership and import "
            "restrictions beside an axolotl"
        ),
        "caption": (
            "Hawaii prohibits ordinary private ownership and import of axolotls. "
            "Confirm current requirements with the Hawaii Department of "
            "Agriculture before any movement or acquisition."
        ),
        "description": (
            "Hawaii axolotl legality infographic explaining ownership and import "
            "restrictions and the purpose of island biosecurity."
        ),
        "credit": "MyAxolotl original graphic",
        "width": 1600,
        "height": 900,
    },
    "legal/maine": {
        "file": "axolotl-legal-maine.webp",
        "alt": (
            "Maine axolotl law graphic showing permit-based ownership and import "
            "requirements"
        ),
        "caption": (
            "Maine regulates axolotls through permit-based wildlife rules. Verify "
            "the current possession and import requirements with Maine DIFW "
            "before acquiring or moving one."
        ),
        "description": (
            "Maine axolotl legality infographic summarizing restricted-species "
            "category, possession permits and import permits."
        ),
        "credit": "MyAxolotl original graphic",
        "width": 1600,
        "height": 900,
    },
    "legal/new-jersey": {
        "file": "axolotl-legal-new-jersey.webp",
        "alt": (
            "New Jersey axolotl law graphic showing prohibited private ownership "
            "and nonnative-species concerns"
        ),
        "caption": (
            "New Jersey does not permit ordinary private ownership of axolotls. "
            "Confirm current possession and transport rules with the New Jersey "
            "Division of Fish and Wildlife before acting."
        ),
        "description": (
            "New Jersey axolotl legality infographic explaining private-ownership "
            "restrictions, ecological concerns and current-rule verification."
        ),
        "credit": "MyAxolotl original graphic",
        "width": 1600,
        "height": 900,
    },
    "legal/new-mexico": {
        "file": "axolotl-legal-new-mexico.webp",
        "alt": (
            "New Mexico axolotl law graphic showing prohibited private ownership "
            "and import restrictions"
        ),
        "caption": (
            "New Mexico prohibits ordinary private ownership and import of "
            "axolotls. Verify the current requirements with the New Mexico "
            "Department of Game and Fish before acting."
        ),
        "description": (
            "New Mexico axolotl legality infographic summarizing possession and "
            "import restrictions with a current-rule reminder."
        ),
        "credit": "MyAxolotl original graphic",
        "width": 1600,
        "height": 900,
    },
    "legal/virginia": {
        "file": "axolotl-legal-virginia.webp",
        "alt": (
            "Virginia axolotl law graphic showing ownership, import and sale "
            "allowed without a state wildlife permit"
        ),
        "caption": (
            "Virginia currently allows possession, import and sale of axolotls "
            "without a state wildlife permit, but local rules can still apply. "
            "Verify current state and local requirements."
        ),
        "description": (
            "Virginia axolotl legality infographic summarizing state permit "
            "status, allowed activities and local-rule verification."
        ),
        "credit": "MyAxolotl original graphic",
        "width": 1600,
        "height": 900,
    },
    "cost-and-buying/axolotl-price-by-morph": {
        "file": "axolotl-price-by-morph.webp",
        "alt": (
            "Six axolotl morphs displayed with example purchase-price ranges "
            "and reminders that seller, age, lineage, location and shipping affect cost"
        ),
        "caption": (
            "Advertised axolotl prices vary by seller, morph, age, lineage and "
            "location. Treat displayed ranges as market examples rather than "
            "guaranteed prices, and include shipping when comparing the total cost."
        ),
        "description": (
            "Axolotl price-by-morph comparison graphic showing common and uncommon "
            "appearances with variable-price and shipping-cost guidance."
        ),
        "credit": "MyAxolotl original graphic",
        "width": 1600,
        "height": 900,
    },
    "cost-and-buying/breeder-vs-pet-store": {
        "file": "axolotl-breeder-vs-pet-store.webp",
        "alt": (
            "Axolotl breeder and pet-store comparison with feeding records, "
            "water-quality questions and written-cost checks"
        ),
        "caption": (
            "Seller type alone does not prove quality. Compare the exact animal, "
            "feeding and hatch records, measured water conditions, delivered cost "
            "and written terms before choosing a breeder or pet store."
        ),
        "description": (
            "Breeder-versus-pet-store axolotl buying graphic focused on verifiable "
            "records, husbandry conditions and transaction terms."
        ),
        "credit": "MyAxolotl original graphic",
        "width": 1600,
        "height": 900,
    },
    "cost-and-buying/choosing-a-reputable-breeder": {
        "file": "choosing-a-reputable-axolotl-breeder.webp",
        "alt": (
            "Axolotl breeder checklist showing dated animal photos, water records, "
            "parentage details and written buyer terms"
        ),
        "caption": (
            "Choose a breeder by the evidence they can provide. Request current "
            "photos, feeding and water records, hatch and parentage information, "
            "written terms and a payment method with buyer protection."
        ),
        "description": (
            "Reputable axolotl breeder checklist illustrating the records and "
            "transaction safeguards to verify before payment."
        ),
        "credit": "MyAxolotl original graphic",
        "width": 1600,
        "height": 900,
    },
    "cost-and-buying/how-to-choose-a-healthy-axolotl": {
        "file": "choosing-a-healthy-axolotl.webp",
        "alt": (
            "Golden albino axolotl with buying checks for body condition, intact "
            "skin and gills, movement, feeding history and water readings"
        ),
        "caption": (
            "Before buying, observe body condition, skin and gill integrity, "
            "balanced movement, recent feeding history and measured water quality. "
            "A photograph can reveal warning signs but cannot diagnose an axolotl."
        ),
        "description": (
            "Healthy-axolotl buying graphic showing observable condition checks and "
            "the records a prospective owner should request."
        ),
        "credit": "MyAxolotl original graphic",
        "width": 1600,
        "height": 900,
    },
    "cost-and-buying/red-flags-when-buying": {
        "file": "axolotl-seller-red-flags.webp",
        "alt": (
            "Dark axolotl beside seller red flags including unverifiable animals, "
            "unsafe payment requests, vague care information and changed terms"
        ),
        "caption": (
            "Pause a purchase when the seller cannot verify the exact animal, "
            "explain its current care or provide consistent written terms. Avoid "
            "payment methods that remove ordinary buyer protection."
        ),
        "description": (
            "Axolotl seller-red-flags graphic covering identity, husbandry, payment "
            "and shipping warning signs."
        ),
        "credit": "MyAxolotl original graphic",
        "width": 1600,
        "height": 900,
    },
    "cost-and-buying/shipping-live-axolotls": {
        "file": "shipping-live-axolotls.webp",
        "alt": (
            "Axolotl shipping sequence with insulated packaging, delivery tracking, "
            "unboxing documentation and transfer to a prepared cycled aquarium"
        ),
        "caption": (
            "Before payment, verify the carrier's current live-animal policy, route "
            "legality and suitable weather. Arrange prompt delivery, document the "
            "unboxing, and prepare a cycled destination before the animal arrives."
        ),
        "description": (
            "Live-axolotl shipping graphic showing insulated packing, tracking, "
            "arrival documentation and transfer preparation."
        ),
        "credit": "MyAxolotl original graphic",
        "width": 1600,
        "height": 900,
    },
    "gifts-and-merch/best-axolotl-toys-and-plushies": {
        "file": "best-axolotl-toys-and-plushies.webp",
        "alt": (
            "Axolotl plush toys and activity toys arranged as gift ideas by age, "
            "play style and budget"
        ),
        "caption": (
            "Match an axolotl toy to the recipient's age and intended use, then "
            "check the current product label for age guidance. Prices and stock "
            "vary by retailer, size and design."
        ),
        "description": (
            "Axolotl toy-and-plush gift guide showing cuddly, reversible, "
            "interactive and fidget-style options."
        ),
        "credit": "MyAxolotl original graphic",
        "width": 1600,
        "height": 900,
    },
    "gifts-and-merch/axolotl-squishmallow-guide": {
        "file": "axolotl-squishmallow-guide.webp",
        "alt": (
            "Archie-style axolotl plush collection ranging from a small clip to "
            "a 24-inch jumbo size"
        ),
        "caption": (
            "Axolotl Squishmallows are sold in multiple sizes, with 8-inch and "
            "12-inch versions among the common gift formats. Character selection, "
            "sizes, retail prices and availability change between sellers."
        ),
        "description": (
            "Axolotl Squishmallow size guide comparing clip, 5-inch, 8-inch, "
            "12-inch and jumbo plush formats with buying notes."
        ),
        "credit": "MyAxolotl original graphic",
        "width": 1600,
        "height": 900,
    },
    "gifts-and-merch/build-a-bear-axolotl-guide": {
        "file": "build-a-bear-axolotl-guide.webp",
        "alt": (
            "Build-A-Bear axolotl plush beside clothing, scent, sound and gift-tag "
            "customization options"
        ),
        "caption": (
            "Build-A-Bear lists the standard pink axolotl separately from optional "
            "clothing, sounds, scents and gift sets. Prices, colors, seasonal models "
            "and availability can change, so verify the current official listing."
        ),
        "description": (
            "Build-A-Bear axolotl buying graphic showing the base plush and common "
            "customization choices with variable-price guidance."
        ),
        "credit": "MyAxolotl original graphic",
        "width": 1600,
        "height": 900,
    },
    "gifts-and-merch/best-axolotl-lego-sets": {
        "file": "lego-axolotl-house-set-21247.webp",
        "alt": (
            "LEGO Minecraft Axolotl House set 21247 with an axolotl-shaped house, "
            "underwater scenery and set specifications"
        ),
        "caption": (
            "LEGO Minecraft The Axolotl House is set 21247, rated for ages 7 and "
            "up, with 242 pieces and a 2023 release year. It is discontinued in "
            "some markets, so current availability and resale prices vary."
        ),
        "description": (
            "LEGO Axolotl House set guide showing the Minecraft model, set number, "
            "piece count, age rating and release information."
        ),
        "credit": "MyAxolotl original graphic",
        "width": 1600,
        "height": 900,
    },
    "tank-setup/aquarium-chillers": {
        "file": "axolotl-aquarium-chillers.webp",
        "alt": (
            "Golden albino axolotl tank connected to a compressor aquarium "
            "chiller with a digital thermometer and water-flow diagram"
        ),
        "caption": (
            "A compressor chiller can stabilize an axolotl tank through warm "
            "weather. Match the unit to the tank volume and required flow rate, "
            "then verify the water temperature with a separate thermometer."
        ),
        "description": (
            "Educational aquarium-chiller graphic showing a golden albino "
            "axolotl, compressor unit, circulation loop and temperature checks."
        ),
        "credit": "MyAxolotl original graphic",
        "width": 1600,
        "height": 900,
    },
    "tank-setup/water-change-guide": {
        "file": "axolotl-water-change-guide.webp",
        "alt": (
            "Golden albino axolotl beside a siphon, replacement-water tub and "
            "five-step aquarium water-change guide"
        ),
        "caption": (
            "For routine maintenance, test the water, siphon waste, condition "
            "and temperature-match the replacement water, then refill slowly. "
            "Ammonia or nitrite spikes may require larger or repeated changes."
        ),
        "description": (
            "Step-by-step axolotl water-change graphic showing preparation, "
            "siphoning, routine amounts, temperature matching and slow refilling."
        ),
        "credit": "MyAxolotl original graphic",
        "width": 1600,
        "height": 900,
    },
    "tank-setup/water-conditioners": {
        "file": "axolotl-water-conditioners.webp",
        "alt": (
            "Leucistic axolotl beside an unbranded water conditioner with "
            "chlorine, chloramine, ammonia and nitrite treatment callouts"
        ),
        "caption": (
            "Treat new tap water at the product's label dose to neutralize "
            "chlorine and chloramine. Some conditioners temporarily detoxify "
            "ammonia or nitrite, but they do not replace a cycled biofilter."
        ),
        "description": (
            "Axolotl water-conditioner graphic explaining tap-water treatment "
            "and ingredient checks for chlorine, chloramine and heavy metals."
        ),
        "credit": "MyAxolotl original graphic",
        "width": 1600,
        "height": 900,
    },
    "tank-setup/tank-size-by-age": {
        "file": "axolotl-tank-size-by-age.webp",
        "alt": (
            "Wild-type axolotl beside tank-size guidance for baby, juvenile, "
            "adult and paired axolotls"
        ),
        "caption": (
            "Tank volume should increase as an axolotl grows: 5-10 gallons for "
            "a small grow-out setup, 20 gallons for a juvenile, 20-40 gallons "
            "for one adult, and at least a 40-gallon breeder for a pair."
        ),
        "description": (
            "Life-stage tank-size comparison for baby, juvenile and adult "
            "axolotls, emphasizing long tanks and usable floor space."
        ),
        "credit": "MyAxolotl original graphic",
        "width": 1600,
        "height": 900,
    },
    "tank-setup/tank-mates": {
        "file": "axolotl-tank-mates.webp",
        "alt": (
            "Melanoid and leucistic axolotls together with tank-mate safety "
            "notes about fish, shrimp, snails and adult tank size"
        ),
        "caption": (
            "Axolotls are safest alone or with a similarly sized axolotl in "
            "adequate space. Fish may nip exposed gills, while shrimp and "
            "snails may be swallowed."
        ),
        "description": (
            "Tank-mate risk graphic comparing same-size axolotls with fish, "
            "shrimp and snails in a planted aquarium."
        ),
        "credit": "MyAxolotl original graphic",
        "width": 1600,
        "height": 900,
    },
    "tank-setup/acclimating-a-new-axolotl": {
        "file": "acclimating-a-new-axolotl.webp",
        "alt": (
            "Leucistic axolotl in a dim aquarium beside acclimation steps for "
            "temperature matching and transfer without transport water"
        ),
        "caption": (
            "For a local pickup, dim the lights, match the temperature and add "
            "tank water gradually before transferring the axolotl without the "
            "transport water. Overnight shipping requires a faster method."
        ),
        "description": (
            "Step-by-step acclimation graphic showing a floating bag, timed "
            "water additions and transfer into a prepared axolotl tank."
        ),
        "credit": "MyAxolotl original graphic",
        "width": 1600,
        "height": 900,
    },
    "tank-setup/water-parameters-cycling": {
        "file": "axolotl-water-parameters-nitrogen-cycle.webp",
        "alt": (
            "Leucistic axolotl beside aquarium test tubes and target readings "
            "for ammonia, nitrite, nitrate, pH and temperature"
        ),
        "caption": (
            "A cycled axolotl tank should test at 0 ppm ammonia and 0 ppm "
            "nitrite. Track nitrate, pH and temperature as trends because a "
            "single test does not show whether conditions are stable."
        ),
        "description": (
            "Axolotl water-parameter graphic with liquid test tubes and target "
            "readings for monitoring the aquarium nitrogen cycle."
        ),
        "credit": "MyAxolotl original graphic",
        "width": 1600,
        "height": 900,
    },
    "health/black-tea-bath": {
        "file": "axolotl-black-tea-bath.webp",
        "alt": (
            "Leucistic axolotl in a shallow black tea bath beside a timer, pure "
            "tea bag and thermometer"
        ),
        "caption": (
            "For mild irritation or early surface fungus, a short 10–15-minute "
            "bath made with cooled, pure black tea may provide supportive care; "
            "stop if the axolotl shows distress and seek veterinary help for "
            "persistent or spreading disease."
        ),
        "description": (
            "Axolotl black-tea-bath guide showing a shallow treatment tub, timer, "
            "thermometer and pure black tea."
        ),
        "credit": "MyAxolotl original graphic",
        "width": 1600,
        "height": 900,
    },
    "health/parasite-treatment": {
        "file": "axolotl-parasite-treatment.webp",
        "alt": (
            "Wild-type axolotl in a hospital tub with a magnified parasite and "
            "quarantine sign"
        ),
        "caption": (
            "Possible parasites require water-quality checks, isolation in a "
            "clean hospital tub and confirmation by an experienced exotic "
            "veterinarian before treatment."
        ),
        "description": (
            "Axolotl parasite-treatment graphic showing quarantine, water checks "
            "and veterinary confirmation."
        ),
        "credit": "MyAxolotl original graphic",
        "width": 1600,
        "height": 900,
    },
    "health/malnutrition-signs": {
        "file": "axolotl-malnutrition-signs.webp",
        "alt": (
            "Golden albino axolotl beside healthy and underweight body-condition "
            "comparisons"
        ),
        "caption": (
            "Evaluate body condition from above: a persistently narrow abdomen, "
            "reduced tail mass, poor growth or low energy can indicate "
            "undernutrition, but water quality and disease should also be "
            "investigated."
        ),
        "description": (
            "Axolotl malnutrition-signs graphic comparing healthy and underweight "
            "body condition."
        ),
        "credit": "MyAxolotl original graphic",
        "width": 1600,
        "height": 900,
    },
    "health/why-axolotl-floating": {
        "file": "why-axolotl-floating.webp",
        "alt": (
            "Dark axolotl floating near the aquarium surface beside common-cause "
            "and first-check guidance"
        ),
        "caption": (
            "Floating is a symptom rather than a diagnosis. Check water parameters "
            "and temperature first; swallowed air, constipation, impaction and "
            "illness are possible causes, especially when floating persists or "
            "worsens."
        ),
        "description": (
            "Axolotl floating guide showing a dark axolotl near the surface and "
            "the first checks owners should make."
        ),
        "credit": "MyAxolotl original graphic",
        "width": 1600,
        "height": 900,
    },
    "health/fridging-sick-axolotl": {
        "file": "fridging-sick-axolotl-risks.webp",
        "alt": (
            "Leucistic axolotl in a labeled hospital tub beside a refrigerator "
            "and thermometer"
        ),
        "caption": (
            "Fridging is not routine home treatment. Household refrigerators "
            "create temperature and water-quality risks, so controlled cooling "
            "should be used only when an experienced exotic veterinarian "
            "recommends it."
        ),
        "description": (
            "Axolotl fridging-risk graphic showing a hospital tub, refrigerator, "
            "thermometers and veterinary-guidance warning."
        ),
        "credit": "MyAxolotl original graphic",
        "width": 1600,
        "height": 900,
    },
    "health/refusing-to-eat": {
        "file": "axolotl-not-eating-first-checks.webp",
        "alt": (
            "Dark melanoid axolotl turning away from an offered earthworm beside "
            "first checks for appetite loss"
        ),
        "caption": (
            "Unexpected appetite loss is a symptom, not a diagnosis. Record water "
            "values, temperature, food, stool and body condition; seek prompt "
            "veterinary care for swelling, breathing difficulty or rapid decline."
        ),
        "description": (
            "Axolotl-not-eating guide showing a melanoid axolotl refusing a worm "
            "and the first husbandry and health checks to make."
        ),
        "credit": "MyAxolotl original graphic",
        "width": 1600,
        "height": 900,
    },
    "health/fungal-infections-saprolegnia": {
        "file": "axolotl-fungal-infection-signs.webp",
        "alt": (
            "Copper axolotl with a small cotton-like white tuft on its tail shown "
            "in a magnified inset"
        ),
        "caption": (
            "Cotton-like white or gray tufts can indicate fungal growth. Isolate "
            "the axolotl in clean, cool hospital water, test ammonia, nitrite and "
            "temperature, and seek an exotic veterinarian if growth spreads or "
            "the gills are affected."
        ),
        "description": (
            "Axolotl fungal-infection guide showing a localized cotton-like tail "
            "tuft, magnified texture and safe first-response guidance."
        ),
        "credit": "MyAxolotl original graphic",
        "width": 1600,
        "height": 900,
    },
    "health/curled-gills-stress-signal": {
        "file": "axolotl-curled-gills-posture-comparison.webp",
        "alt": (
            "Two axolotls comparing relaxed and curled gill and tail posture "
            "beside water and temperature first-check guidance"
        ),
        "caption": (
            "Compare gill and tail posture with the axolotl's normal baseline. "
            "A forward curl can occur with stress, so test water parameters and "
            "temperature before drawing conclusions."
        ),
        "description": (
            "Wild-type and leucistic axolotls demonstrate relaxed and curled "
            "posture with a water-and-temperature first-check reminder."
        ),
        "credit": "MyAxolotl; morphology references sourced from Wikimedia Commons",
        "width": 1600,
        "height": 900,
    },
    "health/minor-scrapes-and-wounds": {
        "file": "axolotl-minor-wounds-tank-safety-check.webp",
        "alt": (
            "Top-down axolotl tank safety inspection showing smooth decor, a "
            "covered filter intake and warning signs after a scrape"
        ),
        "caption": (
            "Check tank decor and filter intakes after a scrape. Spreading "
            "redness, swelling, persistent bleeding, or rapid deterioration "
            "needs veterinary assessment."
        ),
        "description": (
            "Top-down aquarium inspection showing two axolotl morphs, smooth "
            "decor, a covered intake and wound-escalation warning signs."
        ),
        "credit": "MyAxolotl; morphology references sourced from Wikimedia Commons",
        "width": 1600,
        "height": 900,
    },
    "health/shrinking-gills": {
        "file": "axolotl-shrinking-gills-photo-comparison.webp",
        "alt": (
            "Baseline, later and current photos comparing gill fullness in "
            "leucistic and axanthic axolotls"
        ),
        "caption": (
            "Use repeat photos from the same angle to track gill changes. Test "
            "ammonia, nitrite, and temperature because appearance alone does "
            "not identify the cause."
        ),
        "description": (
            "Photo-record comparison for tracking axolotl gill changes against "
            "the animal's own baseline instead of diagnosing from one image."
        ),
        "credit": "MyAxolotl; morphology references sourced from Wikimedia Commons",
        "width": 1600,
        "height": 900,
    },
    "health/limb-regeneration": {
        "file": "axolotl-limb-regeneration-stages.webp",
        "alt": (
            "Copper axolotl and four-panel limb regeneration sequence from "
            "wound epidermis through blastema and patterned outgrowth"
        ),
        "caption": (
            "Axolotl limb regeneration progresses through wound epidermis, "
            "blastema formation, and patterned outgrowth. Healing speed varies "
            "with the injury and husbandry conditions."
        ),
        "description": (
            "Scientific four-panel sequence explaining the wound epidermis, "
            "blastema and patterned-outgrowth stages of axolotl limb regeneration."
        ),
        "credit": "MyAxolotl; morphology references sourced from Wikimedia Commons",
        "width": 1600,
        "height": 900,
    },
    "health/salt-bath": {
        "file": "axolotl-salt-bath-veterinary-safety.webp",
        "alt": (
            "Axolotl salt bath safety checklist showing a treatment container, "
            "salt, timer and thermometer"
        ),
        "caption": (
            "Salt baths should be veterinarian-directed: the diagnosis, "
            "concentration, exposure time, and observation plan determine "
            "whether they are appropriate."
        ),
        "description": (
            "Veterinary-safety checklist for axolotl salt baths with treatment "
            "equipment and diagnosis, concentration and observation gates."
        ),
        "credit": "MyAxolotl; morphology reference sourced from Wikimedia Commons",
        "width": 1600,
        "height": 900,
    },
    "health/impaction-symptoms-treatment": {
        "file": "axolotl-impaction-substrate-risk-signs.webp",
        "alt": (
            "Dark and golden albino axolotls on fine sand beside a swallowable "
            "gravel warning and nonspecific impaction signs"
        ),
        "caption": (
            "Loss of appetite and swelling are nonspecific signs. Remove "
            "swallowable gravel and seek veterinary assessment for persistent "
            "or worsening symptoms."
        ),
        "description": (
            "Aquarium substrate comparison showing fine sand, swallowable "
            "gravel risk and the limits of diagnosing impaction from appearance."
        ),
        "credit": "MyAxolotl; morphology references sourced from Wikimedia Commons",
        "width": 1600,
        "height": 900,
    },
    "health/red-leg-syndrome": {
        "file": "axolotl-red-leg-symptoms-vet-triage.webp",
        "alt": (
            "Wild-type, leucistic and copper axolotls beside a leg and belly "
            "observation map for rapid redness"
        ),
        "caption": (
            "Skin color varies by morph. Rapid new redness with lethargy or "
            "other decline is a veterinary warning sign, not a diagnosis from "
            "appearance."
        ),
        "description": (
            "Three-morph comparison and anatomical observation map explaining "
            "why rapidly changing redness needs veterinary assessment."
        ),
        "credit": "MyAxolotl; morphology references sourced from Wikimedia Commons",
        "width": 1600,
        "height": 900,
    },
    "health/quarantine-tub": {
        "file": "axolotl-quarantine-hospital-tub-setup.webp",
        "alt": (
            "Top-down axolotl hospital tub setup with two tubs, thermometer, "
            "secure vented lid, hide and dedicated tools"
        ),
        "caption": (
            "A hospital tub uses clean dechlorinated, temperature-matched "
            "water, a bare bottom, a secure vented lid, a smooth hide, and "
            "dedicated tools."
        ),
        "description": (
            "Top-down checklist showing the core equipment for a controlled "
            "axolotl hospital or quarantine tub."
        ),
        "credit": "MyAxolotl; morphology reference sourced from Wikimedia Commons",
        "width": 1600,
        "height": 900,
    },
    "health/finding-an-exotic-vet": {
        "file": "find-axolotl-exotic-vet-checklist.webp",
        "alt": (
            "Desk with an axolotl veterinarian search, call questions, "
            "transport checklist and two morph reference photos"
        ),
        "caption": (
            "Locate an amphibian-experienced veterinarian before an emergency "
            "and ask whether the clinic treats axolotls, offers urgent care, "
            "and has transport instructions."
        ),
        "description": (
            "Planning desk showing an exotic-vet search, screening questions "
            "and an axolotl transport-preparation checklist."
        ),
        "credit": "MyAxolotl; morphology references sourced from Wikimedia Commons",
        "width": 1600,
        "height": 900,
    },
    "health/emergency-first-aid": {
        "file": "axolotl-emergency-first-aid-triage.webp",
        "alt": (
            "Axolotl emergency triage station with water tests, thermometer, "
            "transport tub and urgent veterinary warning signs"
        ),
        "caption": (
            "In an axolotl emergency, test water and temperature first. "
            "Breathing difficulty, uncontrolled bleeding, or inability to "
            "remain upright needs urgent veterinary care."
        ),
        "description": (
            "Urgency-first axolotl triage station combining husbandry checks, "
            "transport preparation and veterinary red flags."
        ),
        "credit": "MyAxolotl; morphology references sourced from Wikimedia Commons",
        "width": 1600,
        "height": 900,
    },
    "health/ammonia-burns": {
        "file": "axolotl-ammonia-exposure-water-test.webp",
        "alt": (
            "Ammonia and nitrite test comparison beside dechlorinated water "
            "and copper, golden albino and dark axolotl reference cards"
        ),
        "caption": (
            "Ammonia and nitrite should read 0 ppm. Move an exposed axolotl "
            "from contaminated water into clean, dechlorinated, "
            "temperature-matched water while arranging veterinary help if "
            "signs are severe."
        ),
        "description": (
            "Water-quality emergency visual showing zero-ammonia and "
            "zero-nitrite targets, clean replacement water and three morphs."
        ),
        "credit": "MyAxolotl; morphology references sourced from Wikimedia Commons",
        "width": 1600,
        "height": 900,
    },
    "health/stress-signs": {
        "file": "axolotl-stress-signs-observation-guide.webp",
        "alt": (
            "Wild-type, albino and golden albino axolotls beside observation "
            "cues for gill posture, tail posture and buoyancy"
        ),
        "caption": (
            "Compare gill posture, tail posture and buoyancy with the axolotl's "
            "normal baseline. One sign alone does not diagnose illness; check "
            "water parameters and temperature first."
        ),
        "description": (
            "Three-panel educational hero showing wild-type, albino and golden "
            "albino axolotls with neutral observation prompts for gill posture, "
            "tail posture and buoyancy."
        ),
        "credit": "MyAxolotl; real-photo morph references from Wikimedia Commons (CC0)",
        "width": 1600,
        "height": 900,
    },
}

# ── Core hubs (from topical map) ───────────────────────────────────────────
HUBS = {
    "axolotls": {
        "title": "All Axolotl Guides: Care, Tank Setup, Diet, Health & More",
        "title_tag": "Axolotl Guides Index: Care, Tank, Diet, Health & Genetics",
        "meta": "Browse every axolotl guide in one place - complete care, tank setup, diet, health, morphs, breeding, cost, legality, and the science behind them.",
        "h1": "All Axolotl Guides",
        "intro": "This is the index to every guide on the site - the complete care guide, tank setup, diet, health, morphs, breeding, cost, legality, and the science behind them. New here? Start with the full care guide.",
        "keywords": ["axolotl guides", "axolotl care", "axolotl care guide"],
        "cat": "Care",
    },
    "tank-setup": {
        "title": "Axolotl Tank Setup: The Complete Guide",
        "title_tag": "Axolotl Tank Setup Guide: Size, Filter, Substrate, Water",
        "h1": "Axolotl Tank Setup",
        "meta": "Learn how to set up an axolotl tank correctly the first time - size, temperature, filtration, substrate, lighting, and plants, explained.",
        "intro": "Building the right environment is the single biggest factor in keeping a healthy axolotl. These guides cover every component - tank size, water quality, filtration, substrate, temperature, lighting, and decor.",
        "keywords": ["axolotl tank setup", "axolotl tank", "axolotl filter", "axolotl substrate"],
        "cat": "Tank Setup",
    },
    "diet": {
        "title": "Axolotl Diet & Feeding Guide",
        "title_tag": "Axolotl Food: What to Feed & How Often",
        "meta": "A complete axolotl feeding guide covering safe foods, schedules by age, portions, and how to avoid overfeeding and impaction.",
        "h1": "Axolotl Diet & Feeding Guide",
        "intro": "Axolotls are obligate carnivores with simple but specific feeding needs. Learn exactly what to feed, how much, how often, and how to avoid the diet mistakes that cause most health problems.",
        "keywords": ["axolotl food", "what do axolotls eat", "axolotl feeding", "how often to feed axolotl"],
        "cat": "Diet",
    },
    "health": {
        "title": "Axolotl Health: Symptoms, First Checks & When to See a Vet",
        "title_tag": "Axolotl Health: Symptoms, First Checks & Vet Warning Signs",
        "meta": "Learn how to observe axolotl health signs, check water and temperature first, and recognize problems that need an exotics-experienced veterinarian.",
        "h1": "Axolotl Health & Illness Guide",
        "intro": "Use these guides to observe symptoms, check water quality and temperature first, and understand when an axolotl needs prompt veterinary care. A single sign cannot diagnose a disease, and medication or intensive supportive care should be guided by an exotics-experienced veterinarian.",
        "keywords": ["axolotl health", "sick axolotl", "axolotl fungus", "axolotl parasites"],
        "cat": "Health",
    },
    "legal": {
        "title": "Is It Legal to Own an Axolotl?",
        "title_tag": "Axolotl Laws: Ownership & Import Rules by Location (2026)",
        "meta": "Axolotl ownership and import rules vary by location. Check permits and restricted areas, then verify current rules with the relevant wildlife authority.",
        "h1": "Is It Legal to Own an Axolotl?",
        "intro": "Axolotl ownership and import rules vary by state and country. Restrictions can come from exotic-wildlife, invasive-species, disease-control, conservation, and import laws. This guide explains the main rules and how to verify the current law where you live.",
        "keywords": ["is it legal to own an axolotl", "axolotl illegal", "axolotl legal states", "axolotl permit"],
        "cat": "Legal",
    },
    "cost-and-buying": {
        "title": "Axolotl Cost & Where to Buy",
        "title_tag": "Axolotl Cost: Price, Monthly Budget & Where to Buy (2026)",
        "meta": "How much does an axolotl cost? Complete price breakdown - purchase price by morph, setup costs, monthly food and water bills, and where to buy one safely.",
        "h1": "Axolotl Cost & Where to Buy",
        "intro": "Before you buy, know what an axolotl really costs - the initial setup, the monthly upkeep, and why the price you pay for the animal is the smallest part of the bill. This guide covers purchase prices by morph and the safest places to buy.",
        "keywords": ["axolotl cost", "axolotl price", "where to buy axolotl", "axolotl for sale"],
        "cat": "Cost & Buying",
    },
    "morphs": {
        "title": "Axolotl Morphs & Color Genetics",
        "title_tag": "Axolotl Morphs: Colors, Types & Genetics Explained",
        "meta": "Every axolotl morph explained - leucistic, golden albino, melanoid, wild type, copper, GFP, and more - with photos, rarity, and the genetics behind each color.",
        "h1": "Axolotl Morphs & Color Genetics",
        "intro": "Axolotls come in a stunning range of colors and patterns, from the common leucistic to rare mosaic and copper morphs. Learn to tell every morph apart, what makes it rare, and the simple genetics behind each color.",
        "keywords": ["axolotl morphs", "axolotl colors", "leucistic axolotl", "axolotl genetics"],
        "cat": "Morphs",
    },
    "breeding": {
        "title": "Axolotl Breeding Guide",
        "title_tag": "How to Breed Axolotls: Complete Breeding Guide (2026)",
        "meta": "How to breed axolotls successfully - conditioning, courtship, egg care, raising larvae, and the genetics and ethics every breeder needs to know.",
        "h1": "Axolotl Breeding Guide",
        "intro": "Breeding axolotls starts before courtship. Confirm sex and maturity, check that the adults are healthy and not closely related, and plan how you will manage eggs, live food, grow-out space, and rehoming before attempting a spawn.",
        "keywords": ["breeding axolotls", "axolotl eggs", "axolotl larvae", "axolotl breeding"],
        "cat": "Breeding",
    },
    "gifts-and-merch": {
        "title": "Axolotl Gifts & Merchandise",
        "title_tag": "Axolotl Toy & Gifts: Plushies, Squishmallows, Apparel & More",
        "meta": "The best axolotl gifts and merchandise for axolotl lovers - axolotl toys, plushies, mugs, apparel, decor, and stocking-stuffer ideas for every budget.",
        "h1": "Axolotl Gifts & Merchandise",
        "intro": "From cuddly axolotl plushies to mugs, shirts, and room decor - the perfect axolotl gifts for every age and budget, curated for the axolotl lover in your life.",
        "keywords": ["axolotl toy", "axolotl plush", "axolotl gifts", "axolotl merch"],
        "cat": "Gifts & Merch",
    },
    "care-basics": {
        "title": "Axolotl Care Basics: Facts, Behavior & Beginner Guides",
        "title_tag": "Axolotl Care Basics: Facts, Behavior & Beginner Tips",
        "meta": "Axolotl care basics for beginners - fun facts, how to pronounce the name, behavior, handling, keeping multiple axolotls, and whether they are good pets.",
        "h1": "Axolotl Care Basics",
        "intro": "The essentials every new axolotl owner should know - what axolotls are really like as pets, their behavior, how to handle them safely, and the facts that surprise most first-time owners.",
        "keywords": ["axolotl facts", "are axolotls good pets", "axolotl behavior", "axolotl beginner"],
        "cat": "Care Basics",
    },
    "biology-and-science": {
        "title": "Axolotl Biology & Science",
        "title_tag": "Axolotl Biology: Anatomy, Neoteny & Regeneration Science",
        "meta": "The fascinating biology of axolotls - how they breathe, neoteny, regeneration, their endangered wild status in Xochimilco, and how they compare to other salamanders.",
        "h1": "Axolotl Biology & Science",
        "intro": "Axolotls are one of the most studied animals in biology for a reason: they regenerate limbs, stay in a larval form their whole lives, and hold clues to tissue repair. Here is the science, explained clearly.",
        "keywords": ["axolotl biology", "axolotl neoteny", "axolotl regeneration", "axolotl endangered"],
        "cat": "Biology",
    },
    "axolotl-in-culture": {
        "title": "Axolotls in Pop Culture: Games, Memes & Media",
        "title_tag": "Axolotls in Pop Culture: Minecraft, Memes & More",
        "meta": "Why axolotls are everywhere - Minecraft axolotls, Adopt Me pets, memes, pop culture, and why this endangered salamander became so popular.",
        "h1": "Axolotls in Pop Culture",
        "intro": "From Minecraft and Adopt Me to memes, plushies, and science headlines - find out why the axolotl became one of the most beloved animals on the internet, and how the virtual versions compare to the real thing.",
        "keywords": ["axolotl minecraft", "axolotl adopt me", "axolotl meme", "why are axolotls so popular"],
        "cat": "Culture",
    },
}

# ── Article -> hub/slug mapping ────────────────────────────────────────────
# key: exact source filename (must match file in SOURCE_DIR)
# value: {slug, hub, title_override (optional), meta_override (optional),
#         intro (optional, first paragraph fallback used if missing)}
ARTICLES = {
    "1- axolotl-care-guide (1).docx": {
        "slug": "axolotls/care-guide",
        "hub": "axolotls",
        "featured": True,
        "title_override": "Axolotl Care Guide: Tank, Water, Diet & Health",
        "meta_override": "Axolotls are cold-water amphibians that need stable tanks, clean water, the right diet, and careful health management.",
    },
    "2-How to Set Up an Axolotl Tank the Right Way.docx": {
        "slug": "tank-setup/setup-guide",
        "hub": "tank-setup",
        "featured": True,
        "meta_override": "Set up an axolotl tank correctly with the right tank size, filtration, substrate, lighting, temperature, and cycling before adding your axolotl.",
    },
    "3- Best aquarium chillers for  axolots.docx": {
        "slug": "tank-setup/aquarium-chillers",
        "hub": "tank-setup",
        "title_override": "Best Aquarium Chillers for Axolotls: Sizing & Buying Guide",
        "title_tag": "Best Aquarium Chillers for Axolotls: Sizing & Buying Guide",
        "meta_override": "Choose an aquarium chiller for an axolotl tank by water volume, room heat load, target temperature, flow requirements, installation, noise and operating cost.",
        "date_modified": "2026-09-18",
    },
    "4- Choosing best Axolotl subtrate.docx": {
        "slug": "tank-setup/substrate-and-impaction",
        "hub": "tank-setup",
        "title_override": "Choosing the Best Axolotl Substrate",
        "meta_override": "Fine sand under 1 mm is safest for adult axolotls; juveniles under 6 inches should stay on bare-bottom tanks to reduce impaction risk.",
    },
    "5- Managing Ammonia and Nitrate Spikes in Axolotl Tanks.docx": {
        "slug": "tank-setup/water-parameters-cycling",
        "hub": "tank-setup",
        "title_override": "Axolotl Water Parameters & Nitrogen Cycle",
        "title_tag": "Axolotl Water Parameters: Ammonia, Nitrite, Nitrate & pH",
        "meta_override": "Axolotl water parameters and nitrogen cycle explained: ammonia, nitrite, nitrate, pH, cycling, testing, spikes and how to interpret changing aquarium readings.",
        "date_modified": "2026-09-18",
    },
    "7 - Best axolotl filters.docx": {
        "slug": "tank-setup/filtration-for-axolotls",
        "hub": "tank-setup",
        "title_override": "Do Axolotls Need a Filter? Filtration, Flow Rate & Sizing",
        "title_tag": "Do Axolotls Need a Filter? Filtration, Flow Rate & Sizing",
        "meta_override": "Do axolotls need a filter? Learn biological filtration, low-flow requirements, filter sizing and how sponge, HOB and canister filters fit different axolotl tanks.",
        "date_modified": "2026-09-18",
    },
    "8- How to keep axolotl tank cool safe.docx": {
        "slug": "tank-setup/temperature",
        "hub": "tank-setup",
        "title_override": "How to Keep an Axolotl Tank Cool",
    },
    "9 - canister vs sponge filter.docx": {
        "slug": "tank-setup/canister-vs-sponge-filter",
        "hub": "tank-setup",
        "title_override": "Canister Filters vs. Sponge Filters for Axolotls",
    },
    "10 - Water conditioner for axolotl.docx": {
        "slug": "tank-setup/water-conditioners",
        "hub": "tank-setup",
        "title_override": "Axolotl Water Conditioner: Creating Safe Water",
        "meta_override": "Use an axolotl-safe water conditioner to remove chlorine and chloramine from tap water, with correct dosing for each water change.",
    },
    "11- axolotl lighting requirements.docx": {
        "slug": "tank-setup/lighting-for-axolotls",
        "hub": "tank-setup",
        "title_override": "Axolotl Tank Lighting Requirements",
        "meta_override": "Axolotl tanks need low-intensity, indirect light around 100–400 lux with a consistent 10–12-hour photoperiod on a timer.",
    },
    "12 - Best hides and caves for axolotls.docx": {
        "slug": "tank-setup/hides-and-caves",
        "hub": "tank-setup",
        "title_override": "Best Hides and Caves for Axolotls",
        "meta_override": "Axolotls need a dark, smooth, fully enclosed hide; terracotta, PVC pipe, and fired ceramic are practical, safe choices.",
    },
    "13 - The Dangers of Sharp Gravel for Axolotls.docx": {
        "slug": "tank-setup/gravel-risks",
        "hub": "tank-setup",
        "title_override": "The Dangers of Sharp Gravel for Axolotls",
    },
    "14- Live Plants vs artificial plants.docx": {
        "slug": "tank-setup/live-vs-artificial-plants",
        "hub": "tank-setup",
        "title_override": "Live Plants vs. Fake Plants for Axolotl Tanks",
    },
    "15 - Why my axotol tank water stink.docx": {
        "slug": "tank-setup/why-tank-water-smells",
        "hub": "tank-setup",
        "title_override": "Why Does My Axolotl Tank Water Stink?",
        "meta_override": "A healthy axolotl tank should smell faint and earthy. Strong odors can signal ammonia, a stalled cycle, dirty filtration, waste, or anaerobic pockets.",
    },
    "16 - What Do Axolotls Eat.docx": {
        "slug": "diet/best-foods-list",
        "hub": "diet",
        "featured": True,
        "meta_override": "Best axolotl foods include earthworms, quality sinking pellets, blackworms, and suitable occasional treats. Compare nutrition, safety, and feeding use.",
    },
    "17 -how often should you feed an axolotl.docx": {
        "slug": "diet/feeding-schedule-by-age",
        "hub": "diet",
        "title_override": "Axolotl Feeding Frequency by Life Stage and Size",
        "meta_override": "Find an axolotl feeding schedule by age and size, with frequency and portion guidance for hatchlings, juveniles, subadults, and adults.",
    },
    "18 - Best Axolotl Pellets and Commercial Foods.docx": {
        "slug": "diet/axolotl-pellets",
        "hub": "diet",
        "title_override": "Best Axolotl Pellets and Commercial Foods",
        "meta_override": "Compare high-protein axolotl pellets and commercial foods, including protein targets, ingredients, and how they fit alongside earthworms.",
    },
    "19 - Earthworms vs. Bloodworms Which Is Better for Axolotl.docx": {
        "slug": "diet/live-vs-frozen-food",
        "hub": "diet",
        "title_override": "Earthworms vs. Bloodworms: Best for Axolotls?",
        "meta_override": "Compare earthworms, bloodworms, and frozen foods for axolotls so you can pick the safest staple and best occasional treats.",
    },
    "20 - Why Is My Axolotl Refusing to Eat.docx": {
        "slug": "health/refusing-to-eat",
        "hub": "health",
        "featured": True,
        "title_override": "Axolotl Not Eating? Causes & When to Worry",
        "title_tag": "Axolotl Not Eating? First Checks & Vet Warning Signs",
        "meta_override": "Learn what to check when an axolotl stops eating, which warning signs need prompt veterinary care, and which risky home treatments to avoid.",
        "date_modified": "2026-08-27",
    },
    "21 - The Risks of Feeding Feeder Fish to Axolotls.docx": {
        "slug": "diet/feeder-fish-risks",
        "hub": "diet",
        "title_override": "The Risks of Feeding Feeder Fish to Axolotls",
    },
    "22 - Can Axolotls Eat Beef Heart.docx": {
        "slug": "diet/beef-heart",
        "hub": "diet",
        "meta_override": "Axolotls can eat beef heart, but its poor mineral balance and high fat make it unsuitable as a regular staple food.",
    },
    "23 - Dealing with Axolotl Obesity.docx": {
        "slug": "diet/overfeeding-and-impaction",
        "hub": "diet",
        "title_override": "Axolotl Obesity: Signs, Causes & Treatment",
    },
    "24 - Black worms for juveniles.docx": {
        "slug": "diet/blackworms-for-juveniles",
        "hub": "diet",
        "title_override": "Preparing Blackworms for Juvenile Axolotls",
        "meta_override": "Learn how to rinse, store, and prepare blackworms for juvenile axolotls, including safe size, feeding, and cleanliness checks.",
    },
    "25 - Vacation Prep.docx": {
        "slug": "diet/fasting-and-vacation",
        "hub": "diet",
        "title_override": "How Long Can Axolotls Go Without Food? Fasting & Vacation Guide",
        "title_tag": "How Long Can Axolotls Go Without Food? Fasting & Vacation Guide",
        "meta_override": "How long can an axolotl go without food? Learn planned fasting vs appetite loss, vacation feeding, life-stage differences and when not eating becomes a health concern.",
        "date_modified": "2026-09-18",
    },
    "26 - How to Hand Feed axolotls.docx": {
        "slug": "diet/how-to-hand-feed",
        "hub": "diet",
        "title_override": "How to Hand Feed Your Axolotl Safely",
        "meta_override": "Learn how to hand-feed your axolotl safely, from choosing the right food to timing, technique, and when to avoid hand-feeding.",
    },
    "27 - Shrimps for axolotls.docx": {
        "slug": "diet/shrimp-for-axolotls",
        "hub": "diet",
        "title_override": "Can Axolotls Eat Shrimp?",
        "meta_override": "Axolotls can eat shrimp as an occasional treat, but it should not replace staple foods such as earthworms and quality sinking pellets.",
    },
    "28 - Do Axolotls Need Vitamin Supplements.docx": {
        "slug": "diet/vitamin-and-supplement-needs",
        "hub": "diet",
        "title_override": "Do Axolotls Need Vitamin Supplements?",
    },
    "29 - Cleaning Uneaten Food to Prevent Ammonia.docx": {
        "slug": "tank-setup/uneaten-food-and-ammonia",
        "hub": "tank-setup",
        "title_override": "Why Uneaten Food Causes Ammonia in an Axolotl Tank",
    },
    "30 - Sign of malnutrition in axolotls.docx": {
        "slug": "health/malnutrition-signs",
        "hub": "health",
        "title_override": "Signs of Malnutrition in Axolotls",
    },
    "31 - Parasites in axolots.docx": {
        "slug": "health/parasite-treatment",
        "hub": "health",
        "title_override": "Treating Axolotl Parasites",
    },
    "32 - How to Identify and Treat Axolotl Fungus.docx": {
        "slug": "health/fungal-infections-saprolegnia",
        "hub": "health",
        "title_override": "Axolotl Fungus: Symptoms, Causes & Treatment",
        "title_tag": "Axolotl Fungus: Symptoms, Causes & Treatment",
        "meta_override": "Axolotl fungus guide: what white or cottony growth can look like, possible causes, first checks, treatment decision points and when veterinary assessment is needed.",
        "date_modified": "2026-09-18",
    },
    "33 - The Black Tea Bath Protocol for Axolotls.docx": {
        "slug": "health/black-tea-bath",
        "hub": "health",
        "title_override": "Black Tea Bath for Axolotls: When & How to Use One",
        "title_tag": "Black Tea Bath for Axolotls: When & How to Use One",
        "meta_override": "Black tea baths for axolotls: what they are, when they may be considered as supportive care, how the procedure works, limits, risks and when to seek veterinary help.",
        "date_modified": "2026-09-18",
    },
    "34 - When and how to fridge axolotl.docx": {
        "slug": "health/fridging-sick-axolotl",
        "hub": "health",
        "title_override": "Fridging an Axolotl: Risks & Veterinary Guidance",
        "title_tag": "Fridging an Axolotl: Risks & When a Vet May Use It",
        "meta_override": "Understand why fridging is not routine home treatment, what risks household refrigerators create, and what to ask if an amphibian vet recommends it.",
        "date_modified": "2026-08-27",
    },
    "35 - axolotl salt bath.docx": {
        "slug": "health/salt-bath",
        "hub": "health",
        "title_override": "Axolotl Salt Bath: When It May Be Used & How It Works",
        "title_tag": "Axolotl Salt Bath: When It May Be Used & How It Works",
        "meta_override": "Axolotl salt baths explained: when they may be discussed for selected external problems, why they can irritate amphibian skin, procedure limits and safer escalation.",
        "date_modified": "2026-09-18",
    },
    "36 - Why is My Axolotl Floating Continuously.docx": {
        "slug": "health/why-axolotl-floating",
        "hub": "health",
        "title_override": "Why Is My Axolotl Floating? Causes and Treatment",
    },
    "38 - Wild Type Axolotl.docx": {
        "slug": "morphs/wild-type",
        "hub": "morphs",
        "title_override": "Wild Type Axolotl: The Natural Color",
        "title_tag": "Wild Type Axolotl: Color, Genetics & How to Identify One",
    },
    "39 - Chimera Axolotl.docx": {
        "slug": "morphs/chimera",
        "hub": "morphs",
        "title_override": "Chimera Axolotl: The Rarest Morph of All",
        "title_tag": "Chimera Axolotl: The Rarest Morph, Explained",
    },
    "40 - Axolotl Egg and Larvae Care.docx": {
        "slug": "breeding/egg-and-larvae-care",
        "hub": "breeding",
        "title_override": "Axolotl Egg and Larvae Care: A Complete Guide",
        "title_tag": "Axolotl Egg Care: Hatching Time, Setup & Feeding Larvae",
    },
    "41 - Axolotl Genetics and Inbreeding Risk.docx": {
        "slug": "breeding/genetics-and-inbreeding",
        "hub": "breeding",
        "title_override": "Axolotl Genetics and Inbreeding Risk",
        "title_tag": "Axolotl Genetics & Inbreeding Risk: What Breeders Must Know",
    },
    "42 - Breeding Triggers Temperature Cycling.docx": {
        "slug": "breeding/breeding-triggers-temperature-cycling",
        "hub": "breeding",
        "title_override": "Breeding Triggers: Temperature Cycling for Axolotls",
        "title_tag": "How to Trigger Axolotl Breeding: Temperature & Light Cycling",
    },
    "43 - How to Tell Axolotl Gender.docx": {
        "slug": "breeding/sexing-axolotls",
        "hub": "breeding",
        "title_override": "How to Tell Axolotl Gender (Sexing Guide)",
        "title_tag": "How to Tell Axolotl Gender: Male vs Female Cloaca Guide",
    },
    "44 - Raising Baby Axolotls.docx": {
        "slug": "breeding/raising-juveniles",
        "hub": "breeding",
        "title_override": "Baby Axolotl Care: Feeding, Growth & Raising Juveniles",
        "title_tag": "Baby Axolotl Care: Feeding, Growth & Raising Juveniles",
        "meta_override": "Baby axolotl care from newly feeding larvae through juvenile grow-out: food transitions, growth, size sorting, water quality, and when young axolotls need separate housing.",
        "date_modified": "2026-09-18",
    },
    "45 - Axolotl Color Genetics Punnett Squares.docx": {
        "slug": "breeding/color-genetics-punnett-squares",
        "hub": "breeding",
        "title_override": "Axolotl Color Genetics: Punnett Squares Explained",
        "title_tag": "Axolotl Color Genetics: Punnett Squares Explained",
    },
    "46 - Leucistic Axolotl.docx": {
        "slug": "morphs/leucistic",
        "hub": "morphs",
        "title_override": "Leucistic Axolotl: The \"Lucy\" Morph",
        "title_tag": "Leucistic Axolotl: Color, Genetics & How to Spot a Dirty Lucy",
    },
    "47 - Melanoid Axolotl.docx": {
        "slug": "morphs/melanoid",
        "hub": "morphs",
        "title_override": "Melanoid Axolotl: The Dark Morph",
        "title_tag": "Melanoid Axolotl: Genetics & How to Identify One",
        "meta_override": "The melanoid axolotl is a near-black morph with no metallic shine. Learn how to distinguish it from a dark wild-type axolotl.",
    },
    "48 - Golden Albino Axolotl.docx": {
        "slug": "morphs/golden-albino",
        "hub": "morphs",
        "title_override": "Golden Albino Axolotl",
        "title_tag": "Golden Albino Axolotl: Genetics, Price & Care Guide",
    },
    "49 - GFP Axolotl.docx": {
        "slug": "morphs/gfp-axolotl",
        "hub": "morphs",
        "title_override": "GFP Axolotl: The Glowing Morph",
        "title_tag": "What Is a GFP Axolotl? Care, Setup & Why They Glow",
    },
    "50 - Copper Axolotl.docx": {
        "slug": "morphs/copper",
        "hub": "morphs",
        "title_override": "Copper Axolotl",
        "title_tag": "Copper Axolotl: Color, Genetics & How to Breed Them",
        "meta_override": "The copper axolotl is a brown-orange morph with reddish gills and light eyes caused by a recessive Tyrp1 mutation.",
    },
    "51 - Piebald Axolotl.docx": {
        "slug": "morphs/piebald",
        "hub": "morphs",
        "title_override": "Piebald Axolotl: The Patchy Morph",
        "title_tag": "Piebald Axolotl: Genetics, Price & How It's Different",
        "meta_override": "A piebald axolotl has a dark body with irregular white patches. Learn how it differs from leucistic and chimera axolotls.",
    },
    "52 - Understanding Axolotl Pigment Cells.docx": {
        "slug": "morphs/pigment-cells",
        "hub": "morphs",
        "title_override": "Axolotl Pigment Cells & Color Changes: How Their Colors Work",
        "title_tag": "Axolotl Pigment Cells & Color Changes: How Their Colors Work",
        "meta_override": "How axolotl colors work: melanophores, xanthophores and iridophores, why morphs look different, how color can appear to change, and where axanthic, melanoid and albino fit.",
        "date_modified": "2026-09-18",
    },
    "53 - Enigma MAC and Firefly Axolotls.docx": {
        "slug": "morphs/enigma-firefly-mac",
        "hub": "morphs",
        "title_override": "Enigma, MAC and Firefly Axolotls",
        "title_tag": "Enigma, MAC & Firefly Axolotls: Rare Morphs and the Ethics Debate",
        "meta_override": "Enigma, MAC, and firefly axolotls are rare, controversial morphs. Compare how they are produced, their rarity, cost, and ethical concerns.",
    },
    "54 - Axolotl Curled Gills Stress Signal.docx": {
        "slug": "health/curled-gills-stress-signal",
        "hub": "health",
        "title_override": "Axolotl Curled Gills and Tail Tips: Understanding a Stress Signal",
        "title_tag": "Curled Axolotl Gills & Tail Tip: Stress Signals & Fixes",
        "date_modified": "2026-08-29",
    },
    "55 - Understanding Axolotl Limb Regeneration.docx": {
        "slug": "health/limb-regeneration",
        "hub": "health",
        "title_override": "My Axolotl Lost a Limb: What Should I Do?",
        "title_tag": "My Axolotl Lost a Limb: Healing, Regrowth & When to Get Help",
        "date_modified": "2026-09-18",
    },
    "56 - How to Treat Axolotl Ammonia Burns.docx": {
        "slug": "health/ammonia-burns",
        "hub": "health",
        "title_override": "How to Treat Axolotl Ammonia Burns",
        "title_tag": "Axolotl Ammonia Burn: Signs, Stages & Treatment",
        "date_modified": "2026-08-29",
    },
    "57 - Recognizing Red Leg Syndrome in Axolotls.docx": {
        "slug": "health/red-leg-syndrome",
        "hub": "health",
        "title_override": "Recognizing Red Leg Syndrome in Axolotls",
        "title_tag": "Axolotl Red Leg Disease: Signs, Treatment & Prevention",
        "date_modified": "2026-08-29",
    },
    "58 - Setting Up a Hospital Quarantine Tub for Axolotls.docx": {
        "slug": "health/quarantine-tub",
        "hub": "health",
        "title_override": "Setting Up an Axolotl Hospital Quarantine Tub",
        "title_tag": "Axolotl Hospital Quarantine Tub: Setup & Care",
        "date_modified": "2026-08-29",
    },
    "59 - The Causes of Shrinking Axolotl Gills.docx": {
        "slug": "health/shrinking-gills",
        "hub": "health",
        "title_override": "The Causes of Shrinking Axolotl Gills",
        "title_tag": "Why Are My Axolotl's Gills Shrinking? Causes & Fixes",
        "date_modified": "2026-08-29",
    },
    "60 - Treating Minor Scrapes and Wounds on Axolotls.docx": {
        "slug": "health/minor-scrapes-and-wounds",
        "hub": "health",
        "title_override": "Treating Minor Scrapes and Wounds on Axolotls",
        "title_tag": "Treating Minor Axolotl Scrapes & Wounds: What to Do",
        "date_modified": "2026-08-29",
    },
    "61 - Best Axolotl Toys and Plushies.docx": {
        "slug": "gifts-and-merch/best-axolotl-toys-and-plushies",
        "hub": "gifts-and-merch",
        "title_override": "The Best Axolotl Toys and Plushies",
        "title_tag": "Best Axolotl Toys & Plushies: Stuffed Animals & More (2026)",
    },
    "62 - Axolotl Squishmallow Guide.docx": {
        "slug": "gifts-and-merch/axolotl-squishmallow-guide",
        "hub": "gifts-and-merch",
        "title_override": "The Complete Axolotl Squishmallow Guide",
        "title_tag": "Every Axolotl Squishmallow: Archie, Sizes & How to Buy",
    },
    "63 - Build-A-Bear Axolotl Guide.docx": {
        "slug": "gifts-and-merch/build-a-bear-axolotl-guide",
        "hub": "gifts-and-merch",
        "title_override": "The Build-A-Bear Axolotl Guide",
        "title_tag": "Build-A-Bear Axolotl: Every Model, Price & How to Customize",
    },
    "64 - Best Axolotl LEGO Sets.docx": {
        "slug": "gifts-and-merch/best-axolotl-lego-sets",
        "hub": "gifts-and-merch",
        "title_override": "Best LEGO Axolotl Sets",
        "title_tag": "LEGO Axolotl Sets: Minecraft The Axolotl House Explained",
    },
    "65 - Are Axolotls Legal in California.docx": {
        "slug": "legal/california",
        "hub": "legal",
        "title_override": "Are Axolotls Legal in California?",
        "title_tag": "Are Axolotls Legal in California? Laws & Permits (2026)",
    },
    "66 - Are Axolotls Legal in Canada.docx": {
        "slug": "legal/canada",
        "hub": "legal",
        "title_override": "Are Axolotls Legal in Canada?",
        "title_tag": "Are Axolotls Legal in Canada? Import Rules by Province (2026)",
    },
    "67 - Are Axolotls Legal in Hawaii.docx": {
        "slug": "legal/hawaii",
        "hub": "legal",
        "title_override": "Are Axolotls Legal in Hawaii?",
        "title_tag": "Are Axolotls Legal in Hawaii? Import Rules Explained (2026)",
    },
    "68 - Are Axolotls Legal in Maine.docx": {
        "slug": "legal/maine",
        "hub": "legal",
        "title_override": "Are Axolotls Legal in Maine?",
        "title_tag": "Are Axolotls Legal in Maine? Permit Rules Explained (2026)",
    },
    "69 - Are Axolotls Legal in New Jersey.docx": {
        "slug": "legal/new-jersey",
        "hub": "legal",
        "title_override": "Are Axolotls Legal in New Jersey?",
        "title_tag": "Are Axolotls Legal in New Jersey? Laws Explained (2026)",
    },
    "70 - Are Axolotls Legal in New Mexico.docx": {
        "slug": "legal/new-mexico",
        "hub": "legal",
        "title_override": "Are Axolotls Legal in New Mexico?",
        "title_tag": "Are Axolotls Legal in New Mexico? Import Permit (2026)",
    },
    "71 - Are Axolotls Legal in Virginia.docx": {
        "slug": "legal/virginia",
        "hub": "legal",
        "title_override": "Are Axolotls Legal in Virginia?",
        "title_tag": "Are Axolotls Legal in Virginia? Laws Explained (2026)",
    },
    "72 - Are Axolotls Good Beginner Pets.docx": {
        "slug": "care-basics/are-axolotls-good-beginner-pets",
        "hub": "care-basics",
        "title_override": "Are Axolotls Good Pets? Pros, Cons & Beginner Care Difficulty",
        "title_tag": "Are Axolotls Good Pets? Pros, Cons & Beginner Care Difficulty",
        "date_modified": "2026-09-18",
    },
    "73 - Axolotl Age and Size Chart.docx": {
        "slug": "care-basics/axolotl-age-and-size-chart",
        "hub": "care-basics",
        "title_override": "How Big Do Axolotls Get? Age, Size & Growth Chart",
        "title_tag": "How Big Do Axolotls Get? Age, Size & Growth Chart",
        "date_modified": "2026-09-18",
    },
    "74 - Amazing Axolotl Facts.docx": {
        "slug": "care-basics/axolotl-facts",
        "hub": "care-basics",
        "title_override": "What Is an Axolotl? 25 Facts About This Mexican Salamander",
        "title_tag": "What Is an Axolotl? 25 Facts About This Mexican Salamander",
        "meta_override": "What is an axolotl? Learn the core facts about this Mexican aquatic salamander: classification, neoteny, regeneration, habitat, conservation, lifespan, diet and pet biology.",
        "date_modified": "2026-09-18",
    },
    "75 - Do Axolotls Recognize Their Owners.docx": {
        "slug": "care-basics/axolotl-intelligence-and-bonding",
        "hub": "care-basics",
        "title_override": "Do Axolotls Recognize Their Owners?",
        "title_tag": "Do Axolotls Recognize Their Owners? Bonding & Intelligence",
    },
    "76 - Are Axolotls Good Pets for Kids.docx": {
        "slug": "care-basics/axolotls-and-children",
        "hub": "care-basics",
        "title_override": "Are Axolotls Good Pets for Kids?",
        "title_tag": "Are Axolotls Good Pets for Kids? What Parents Must Know",
        "meta_override": "Are axolotls suitable pets for children? Learn age and maturity considerations, adult responsibility, observation-first handling rules, equipment, feeding supervision and long-term family commitment.",
    },
    "77 - Axolotl Behavior Explained.docx": {
        "slug": "care-basics/behavior",
        "hub": "care-basics",
        "title_override": "Axolotl Behavior Explained",
        "title_tag": "Axolotl Behavior Explained: What Every Owner Should Know",
    },
    "78 - Axolotl Monthly Cost of Ownership.docx": {
        "slug": "care-basics/cost-of-ownership-monthly",
        "hub": "care-basics",
        "title_override": "Axolotl Monthly Cost of Ownership",
        "title_tag": "Axolotl Monthly Cost: Budget for Food, Water & Supplies (2026)",
    },
    "79 - How to Hold an Axolotl.docx": {
        "slug": "care-basics/handling",
        "hub": "care-basics",
        "title_override": "Can You Hold an Axolotl? Safe Handling, Petting & Transport",
        "title_tag": "Can You Hold an Axolotl? Safe Handling, Petting & Transport",
        "date_modified": "2026-09-18",
    },
    "80 - How to Pronounce Axolotl.docx": {
        "slug": "care-basics/how-to-pronounce-axolotl",
        "hub": "care-basics",
        "title_override": "How to Pronounce and Spell Axolotl: Meaning & Correct Pronunciation",
        "title_tag": "How to Pronounce and Spell Axolotl: Meaning & Correct Pronunciation",
        "meta_override": "Learn how to pronounce axolotl in English, spell A-X-O-L-O-T-L, understand the plural, and see how the English form differs from Nahuatl and Spanish ajolote.",
        "date_modified": "2026-09-18",
    },
    "81 - Can Axolotls Live Together.docx": {
        "slug": "care-basics/keeping-multiple-axolotls",
        "hub": "care-basics",
        "title_override": "Can Axolotls Live Together? One vs Two Axolotls & Cohabitation",
        "title_tag": "Can Axolotls Live Together? One vs Two Axolotls & Cohabitation",
        "meta_override": "Can two axolotls live together? Learn size matching, juvenile nipping and cannibalism risk, space and hides, introduction, monitoring and when animals should be separated.",
        "date_modified": "2026-09-18",
    },
    "82 - Axolotl Anatomy Gills and Lungs.docx": {
        "slug": "biology-and-science/anatomy-gills-and-lungs",
        "hub": "biology-and-science",
        "title_override": "Axolotl Anatomy: Gills, Lungs, Teeth & Body Parts",
        "title_tag": "Axolotl Anatomy: Gills, Lungs, Teeth & Body Parts",
        "date_modified": "2026-09-18",
    },
    "83 - Axolotl vs Tiger Salamander.docx": {
        "slug": "biology-and-science/axolotl-vs-tiger-salamander",
        "hub": "biology-and-science",
        "title_override": "Axolotl vs Tiger Salamander",
        "title_tag": "Axolotl vs Tiger Salamander: Key Differences Explained",
    },
    "84 - Axolotl Conservation Status.docx": {
        "slug": "biology-and-science/conservation-status",
        "hub": "biology-and-science",
        "title_override": "Are Axolotls Endangered? How Many Are Left in the Wild?",
        "title_tag": "Are Axolotls Endangered? How Many Are Left in the Wild?",
        "date_modified": "2026-09-18",
    },
    "85 - Is an Axolotl an Amphibian.docx": {
        "slug": "biology-and-science/is-axolotl-amphibian",
        "hub": "biology-and-science",
        "title_override": "Is an Axolotl an Amphibian?",
        "title_tag": "Is an Axolotl an Amphibian? Yes - Here's Why",
    },
    "86 - Axolotl Lifespan Wild vs Captivity.docx": {
        "slug": "biology-and-science/lifespan-wild-vs-captivity",
        "hub": "biology-and-science",
        "title_override": "Axolotl Lifespan: Wild vs Captivity",
        "title_tag": "Axolotl Lifespan: How Long Do Axolotls Live?",
    },
    "87 - Axolotl Regeneration and Limb Regrowth.docx": {
        "slug": "biology-and-science/regeneration-and-limb-regrowth",
        "hub": "biology-and-science",
        "title_override": "Axolotl Regeneration: The Science",
        "title_tag": "Axolotl Regeneration: How They Regrow Limbs & Body Parts",
    },
    "88 - What is Neoteny Axolotl.docx": {
        "slug": "biology-and-science/neoteny",
        "hub": "biology-and-science",
        "title_override": "What Is Neoteny?",
        "title_tag": "What Is Neoteny? Why Axolotls Never Grow Up",
    },
    "89 - Axolotl Wild Habitat Xochimilco.docx": {
        "slug": "biology-and-science/wild-habitat-xochimilco",
        "hub": "biology-and-science",
        "title_override": "Where Do Axolotls Live? Wild Habitat in Xochimilco, Mexico",
        "title_tag": "Where Do Axolotls Live? Wild Habitat in Xochimilco, Mexico",
        "date_modified": "2026-09-18",
    },
    "90 - Axolotl Price by Morph.docx": {
        "slug": "cost-and-buying/axolotl-price-by-morph",
        "hub": "cost-and-buying",
        "title_override": "Axolotl Price by Morph",
        "title_tag": "Axolotl Price by Morph: Cost Guide for Every Color (2026)",
        "meta_override": "August 2026 US axolotl price snapshot by morph, with current listing examples, shipping costs, and checks that matter more than the advertised color.",
        "date_modified": "2026-08-27",
    },
    "91 - Axolotl Breeder vs Pet Store.docx": {
        "slug": "cost-and-buying/breeder-vs-pet-store",
        "hub": "cost-and-buying",
        "title_override": "Axolotl Breeder vs Pet Store: Which Buying Option Is Better?",
        "title_tag": "Axolotl Breeder vs Pet Store: Which Buying Option Is Better?",
        "meta_override": "Compare buying an axolotl from a specialist breeder vs a pet store by animal records, husbandry visibility, selection, support, pickup or shipping, terms and buyer verification.",
        "date_modified": "2026-09-18",
    },
    "92 - How to Choose an Axolotl Breeder.docx": {
        "slug": "cost-and-buying/choosing-a-reputable-breeder",
        "hub": "cost-and-buying",
        "title_override": "How to Choose a Reputable Axolotl Breeder",
        "title_tag": "How to Choose an Axolotl Breeder: 12 Questions to Ask",
        "meta_override": "Use 12 practical questions to verify an axolotl breeder's husbandry, parentage records, current animal photos, shipping terms, and support.",
        "date_modified": "2026-08-27",
    },
    "93 - How to Choose a Healthy Axolotl.docx": {
        "slug": "cost-and-buying/how-to-choose-a-healthy-axolotl",
        "hub": "cost-and-buying",
        "title_override": "How to Choose a Healthy Axolotl",
        "title_tag": "How to Choose a Healthy Axolotl: Signs to Check Before Buying",
        "meta_override": "Check an axolotl's body condition, skin, gills, movement, appetite history, and water records before buying, without diagnosing disease from a photo.",
        "date_modified": "2026-08-27",
    },
    "94 - Axolotl Seller Red Flags.docx": {
        "slug": "cost-and-buying/red-flags-when-buying",
        "hub": "cost-and-buying",
        "title_override": "Axolotl Seller Red Flags",
        "title_tag": "Axolotl Seller Red Flags: How to Spot Scams and Bad Breeders",
        "meta_override": "Spot axolotl seller scams by verifying the exact animal, written terms, traceable payment, husbandry records, identity, and shipping plan.",
        "date_modified": "2026-08-27",
    },
    "95 - How Axolotls Are Shipped.docx": {
        "slug": "cost-and-buying/shipping-live-axolotls",
        "hub": "cost-and-buying",
        "title_override": "How Are Axolotls Shipped? Delivery, Unboxing & Arrival Guide",
        "title_tag": "How Are Axolotls Shipped? Delivery, Unboxing & Arrival Guide",
        "meta_override": "How live axolotl shipping works: seller and carrier checks, weather planning, packing, delivery timing, unboxing, arrival inspection, acclimation and what to do after a delay.",
        "date_modified": "2026-09-18",
    },
    "96 - Axolotl Adopt Me Guide.docx": {
        "slug": "axolotl-in-culture/adopt-me-axolotl-guide",
        "hub": "axolotl-in-culture",
        "title_override": "Axolotl in Adopt Me: How to Get One",
        "title_tag": "Axolotl in Adopt Me: How to Get One & All Colors (2026)",
        "meta_override": "How to get an axolotl in Adopt Me through current trading or a future Pet Shop return, plus its forms and how the virtual pet differs from real care.",
        "date_modified": "2026-08-30",
    },
    "97 - Axolotl in Pop Culture and Memes.docx": {
        "slug": "axolotl-in-culture/axolotl-in-pop-culture-and-memes",
        "hub": "axolotl-in-culture",
        "title_override": "Axolotl in Pop Culture: Minecraft, Gravity Falls, Literature, Memes & More",
        "title_tag": "Axolotl in Pop Culture: Minecraft, Gravity Falls, Literature & Memes",
        "meta_override": "Axolotls in pop culture: Minecraft, Gravity Falls and Bill Cipher, Julio Cortázar, memes, merchandise, science media and the cultural meanings attached to the animal.",
        "date_modified": "2026-09-18",
    },
    "98 - Minecraft Axolotls Guide.docx": {
        "slug": "axolotl-in-culture/minecraft-axolotls-guide",
        "hub": "axolotl-in-culture",
        "title_override": "Minecraft Axolotls: Complete Guide",
        "title_tag": "Minecraft Axolotls: Spawning, Colors & How to Catch Them",
    },
    "99 - Why Are Axolotls So Popular.docx": {
        "slug": "axolotl-in-culture/why-axolotls-are-suddenly-popular",
        "hub": "axolotl-in-culture",
        "title_override": "Why Are Axolotls So Popular?",
        "title_tag": "Why Are Axolotls So Popular? The Rise of a Cute Endangered Amphibian",
    },
    "100 - Blue and Pink Axolotl Myth.docx": {
        "slug": "morphs/blue-and-pink-axolotl-myth",
        "hub": "morphs",
        "title_override": "Pink, Blue, Purple & Green Axolotls: Which Colors Are Real?",
        "title_tag": "Pink, Blue, Purple & Green Axolotls: Which Colors Are Real?",
        "meta_override": "Which axolotl colors are recognized morphs, and which labels come from lighting, GFP fluorescence, editing, or seller terminology? Compare pink, blue, purple, green, yellow, and real morph names.",
        "date_modified": "2026-09-18",
    },
    "101 - Axolotl Morphs Comparison Chart.docx": {
        "slug": "morphs/morphs-comparison-chart",
        "hub": "morphs",
        "title_override": "Axolotl Colors & Morphs: Types, Rarity and Comparison Chart",
        "title_tag": "Axolotl Colors & Morphs: Types, Rarity & Comparison Chart",
        "meta_override": "Compare axolotl colors and morphs side by side, including wild type, leucistic, melanoid, albino, golden albino, copper, axanthic, GFP, piebald, mosaic, and chimera terminology.",
        "date_modified": "2026-09-18",
    },
    "102 - Mosaic Axolotl.docx": {
        "slug": "morphs/mosaic",
        "hub": "morphs",
        "title_override": "Mosaic Axolotl",
        "title_tag": "Mosaic Axolotl: The Patchy Rare Morph, Explained",
    },
    "103 - Finding an Exotic Vet for Axolotls.docx": {
        "slug": "health/finding-an-exotic-vet",
        "hub": "health",
        "title_override": "Finding an Exotic Vet for Axolotls",
        "title_tag": "How to Find an Axolotl Vet: Search & Screening Guide",
        "meta_override": "Find and screen a veterinarian with amphibian experience, prepare useful records, and understand emergency, teletriage, and cost questions.",
        "date_modified": "2026-08-29",
    },
    "104 - Axolotl Stress Signs.docx": {
        "slug": "health/stress-signs",
        "hub": "health",
        "title_override": "Axolotl Stress Signs: How to Tell If Your Axolotl Is Stressed",
        "title_tag": "Axolotl Stress Signs: How to Tell If Your Axolotl Is Stressed",
        "meta_override": "Learn common axolotl stress signs and where each symptom should lead next: curled gills, floating, appetite loss, shrinking gills, fungus-like growth, abnormal swimming and water-quality checks.",
        "date_modified": "2026-09-18",
    },
    "105 - Axolotl Impaction Symptoms and Treatment.docx": {
        "slug": "health/impaction-symptoms-treatment",
        "hub": "health",
        "title_override": "Axolotl Impaction Symptoms and Treatment",
        "title_tag": "Axolotl Impaction: Symptoms, Causes & Treatment",
        "date_modified": "2026-08-29",
    },
    "106 - Axolotl Tank Size by Age.docx": {
        "slug": "tank-setup/tank-size-by-age",
        "hub": "tank-setup",
        "title_override": "What Size Tank Does an Axolotl Need? Tank Size by Age & Number",
        "title_tag": "What Size Tank Does an Axolotl Need? By Age & Number",
        "meta_override": "Choose axolotl tank size by body length, floor space, water volume, filtration, life stage, and number of animals. Compare baby, juvenile, adult, and multi-axolotl needs.",
        "date_modified": "2026-09-18",
    },
    "107 - Can Axolotls Live with Fish.docx": {
        "slug": "tank-setup/tank-mates",
        "hub": "tank-setup",
        "title_override": "Can Axolotls Live with Fish?",
        "title_tag": "Can Axolotls Live with Fish? Tank-Mates, Explained",
    },
    "108 - How to Acclimate a New Axolotl.docx": {
        "slug": "tank-setup/acclimating-a-new-axolotl",
        "hub": "tank-setup",
        "title_override": "How to Acclimate a New Axolotl",
        "title_tag": "How to Acclimate a New Axolotl: Step-by-Step",
    },
}

# Articles that ship interactive tools (copy into /tools/ as bonus pages)
TOOLS = {
    "axolotl-calculator for water conditioner dose.html": {
        "slug": "tools/water-conditioner-dosage-calculator",
        "title": "Axolotl Water Conditioner Dosage Calculator",
        "title_override": "Axolotl Water Conditioner Dosage Calculator | MyAxolotl",
        "cat": "Tools",
    },
    "axolotl-feeding-schedule-generator.html": {
        "slug": "tools/feeding-schedule-generator",
        "title": "Axolotl Feeding Schedule Generator",
        "cat": "Tools",
    },
    "axolotl-nitrogen-cycle-tracker.html": {
        "slug": "tools/nitrogen-cycle-tracker",
        "title": "Axolotl Nitrogen Cycle Tracker",
        "cat": "Tools",
    },
    "axolotl-symptom-checker.html": {
        "slug": "tools/symptom-checker",
        "title": "Axolotl Symptom Checker",
        "cat": "Tools",
    },
    "axolotl-tank-size-calculator.html": {
        "slug": "tools/tank-size-calculator",
        "title": "Axolotl Tank Size Calculator",
        "cat": "Tools",
    },
    "axolotl-chiller-size-calculator.html": {
        "slug": "tools/chiller-size-calculator",
        "title": "Axolotl Chiller Size Calculator",
        "title_override": "Axolotl Chiller Size Calculator: Estimate HP & Flow | MyAxolotl",
        "cat": "Tools",
    },
    "aquarium-volume-calculator.html": {
        "slug": "tools/aquarium-volume-calculator",
        "title": "Aquarium Volume Calculator",
        "title_override": "Aquarium Volume Calculator: Gallons & Liters from Dimensions | MyAxolotl",
        "cat": "Tools",
    },
}

# Internal linking map (source_slug -> [target_slug, ...]) applied to article
# pages automatically. Keys/values are slugs from ARTICLES (without leading /).
LINKING = {
    # Flagship guide anchors the ownership -> legal-status gateway (phase 8).
    "axolotls/care-guide": ["legal"],
    "tank-setup/setup-guide": ["tank-setup/substrate-and-impaction", "tank-setup/filtration-for-axolotls",
                               "tank-setup/temperature", "tank-setup/water-parameters-cycling",
                               "tools/aquarium-volume-calculator"],
    "tank-setup/substrate-and-impaction": ["health/refusing-to-eat", "tank-setup/gravel-risks",
                                           "health/impaction-symptoms-treatment"],
    "tank-setup/gravel-risks": ["tank-setup/substrate-and-impaction", "tank-setup/live-vs-artificial-plants",
                                "health/impaction-symptoms-treatment"],
    "tank-setup/filtration-for-axolotls": ["tank-setup/canister-vs-sponge-filter", "tank-setup/water-parameters-cycling"],
    "tank-setup/canister-vs-sponge-filter": ["tank-setup/filtration-for-axolotls"],
    "tank-setup/water-parameters-cycling": ["tank-setup/why-tank-water-smells", "tank-setup/uneaten-food-and-ammonia"],
    "tank-setup/why-tank-water-smells": ["tank-setup/setup-guide"],
    "tank-setup/uneaten-food-and-ammonia": ["tank-setup/setup-guide"],
    "tank-setup/temperature": ["tank-setup/aquarium-chillers", "tools/chiller-size-calculator", "health/refusing-to-eat"],
    "tank-setup/aquarium-chillers": ["tools/chiller-size-calculator", "tank-setup/temperature"],
    "tank-setup/water-conditioners": ["tank-setup/acclimating-a-new-axolotl",
                                      "tank-setup/lighting-for-axolotls",
                                      "tools/aquarium-volume-calculator"],
    "tank-setup/lighting-for-axolotls": ["tank-setup/hides-and-caves"],
    "tank-setup/hides-and-caves": ["tank-setup/live-vs-artificial-plants"],
    "tank-setup/live-vs-artificial-plants": ["tank-setup/hides-and-caves", "tank-setup/lighting-for-axolotls"],
    "tank-setup/tank-size-by-age": ["tank-setup/setup-guide", "tank-setup/gravel-risks",
                                    "care-basics/axolotl-age-and-size-chart", "tank-setup/tank-mates",
                                    "tools/aquarium-volume-calculator"],
    "tank-setup/tank-mates": ["tank-setup/tank-size-by-age", "diet/feeder-fish-risks",
                              "care-basics/keeping-multiple-axolotls"],
    "tank-setup/acclimating-a-new-axolotl": ["tank-setup/setup-guide"],
    "diet": ["diet/best-foods-list", "diet/feeding-schedule-by-age", "diet/overfeeding-and-impaction"],
    "diet/best-foods-list": ["diet/feeding-schedule-by-age", "diet/live-vs-frozen-food", "diet/axolotl-pellets",
                             "diet/how-to-hand-feed"],
    "diet/feeding-schedule-by-age": ["diet/best-foods-list", "diet/overfeeding-and-impaction",
                                     "breeding/raising-juveniles"],
    "diet/axolotl-pellets": ["diet/best-foods-list", "diet/live-vs-frozen-food"],
    "diet/live-vs-frozen-food": ["diet/best-foods-list", "diet/feeder-fish-risks", "health/parasite-treatment"],
    "diet/feeder-fish-risks": ["diet/best-foods-list", "diet/live-vs-frozen-food", "health/parasite-treatment"],
    "diet/beef-heart": ["diet/best-foods-list", "diet/live-vs-frozen-food"],
    "diet/overfeeding-and-impaction": ["health/refusing-to-eat", "health/impaction-symptoms-treatment", "diet/feeding-schedule-by-age"],
    "diet/blackworms-for-juveniles": ["diet/feeding-schedule-by-age", "diet/best-foods-list",
                                      "breeding/raising-juveniles"],
    "diet/fasting-and-vacation": ["diet/feeding-schedule-by-age", "health/refusing-to-eat"],
    "diet/how-to-hand-feed": ["diet/best-foods-list", "diet/feeding-schedule-by-age"],
    "diet/shrimp-for-axolotls": ["diet/best-foods-list", "diet/feeding-schedule-by-age",
                                 "diet/live-vs-frozen-food"],
    "diet/vitamin-and-supplement-needs": ["diet/best-foods-list", "health/malnutrition-signs"],
    "health": ["health/refusing-to-eat", "health/fungal-infections-saprolegnia", "health/parasite-treatment"],
    "health/refusing-to-eat": ["diet/overfeeding-and-impaction", "health/malnutrition-signs"],
    "health/malnutrition-signs": ["health/refusing-to-eat", "diet/vitamin-and-supplement-needs",
                                  "biology-and-science/regeneration-and-limb-regrowth"],
    "health/parasite-treatment": ["health/fungal-infections-saprolegnia"],
    "health/fungal-infections-saprolegnia": ["health/black-tea-bath", "health/salt-bath", "health/fridging-sick-axolotl",
                                             "biology-and-science/anatomy-gills-and-lungs"],
    "health/black-tea-bath": ["health/fungal-infections-saprolegnia", "health/fridging-sick-axolotl"],
    "health/fridging-sick-axolotl": ["health/emergency-first-aid", "health/finding-an-exotic-vet",
                                      "health/impaction-symptoms-treatment", "tank-setup/temperature"],
    "health/salt-bath": ["health/fungal-infections-saprolegnia", "health/black-tea-bath"],
    "health/why-axolotl-floating": ["health/refusing-to-eat", "tank-setup/water-parameters-cycling"],
    "health/curled-gills-stress-signal": ["health/shrinking-gills", "health/ammonia-burns",
                                          "tank-setup/water-parameters-cycling", "health/stress-signs",
                                          "biology-and-science/anatomy-gills-and-lungs"],
    "health/limb-regeneration": ["health/minor-scrapes-and-wounds", "health/fungal-infections-saprolegnia",
                                 "biology-and-science/regeneration-and-limb-regrowth"],
    "health/ammonia-burns": ["health/curled-gills-stress-signal", "health/quarantine-tub",
                             "tank-setup/water-parameters-cycling"],
    "health/red-leg-syndrome": ["health/quarantine-tub", "health/fungal-infections-saprolegnia",
                                "health/finding-an-exotic-vet"],
    "health/quarantine-tub": ["health/red-leg-syndrome", "health/refusing-to-eat",
                              "health/fungal-infections-saprolegnia"],
    "health/shrinking-gills": ["health/curled-gills-stress-signal", "tank-setup/temperature",
                               "tank-setup/water-parameters-cycling", "biology-and-science/anatomy-gills-and-lungs"],
    "health/minor-scrapes-and-wounds": ["health/limb-regeneration", "health/fungal-infections-saprolegnia",
                                        "health/salt-bath"],
    "health/finding-an-exotic-vet": ["health/red-leg-syndrome", "health/impaction-symptoms-treatment",
                                     "health/fungal-infections-saprolegnia", "health/parasite-treatment",
                                     "health/emergency-first-aid"],
    "health/stress-signs": ["health/curled-gills-stress-signal", "health/why-axolotl-floating",
                            "health/refusing-to-eat", "tank-setup/water-parameters-cycling"],
    "health/impaction-symptoms-treatment": ["health/refusing-to-eat", "health/fridging-sick-axolotl",
                                            "diet/overfeeding-and-impaction", "tank-setup/substrate-and-impaction",
                                            "tank-setup/gravel-risks"],
    "health/emergency-first-aid": ["health/finding-an-exotic-vet", "health/refusing-to-eat",
                                   "health/red-leg-syndrome", "health/ammonia-burns",
                                   "health/why-axolotl-floating", "health/fungal-infections-saprolegnia",
                                   "health/fridging-sick-axolotl"],
    "tank-setup/water-change-guide": ["tank-setup/setup-guide"],
    "gifts-and-merch": ["gifts-and-merch/best-axolotl-toys-and-plushies",
                        "gifts-and-merch/axolotl-squishmallow-guide",
                        "gifts-and-merch/build-a-bear-axolotl-guide",
                        "gifts-and-merch/best-axolotl-lego-sets"],
    "gifts-and-merch/best-axolotl-toys-and-plushies": ["gifts-and-merch/best-axolotl-lego-sets",
                                                       "gifts-and-merch/axolotl-squishmallow-guide",
                                                       "gifts-and-merch/build-a-bear-axolotl-guide"],
    "gifts-and-merch/axolotl-squishmallow-guide": ["gifts-and-merch/best-axolotl-toys-and-plushies",
                                                   "gifts-and-merch/build-a-bear-axolotl-guide"],
    "gifts-and-merch/build-a-bear-axolotl-guide": ["gifts-and-merch/axolotl-squishmallow-guide",
                                                   "gifts-and-merch/best-axolotl-toys-and-plushies"],
    "gifts-and-merch/best-axolotl-lego-sets": ["gifts-and-merch/best-axolotl-toys-and-plushies",
                                               "axolotl-in-culture/minecraft-axolotls-guide"],
    "morphs/wild-type": ["morphs/pigment-cells", "morphs/morphs-comparison-chart",
                         "breeding/color-genetics-punnett-squares", "cost-and-buying/axolotl-price-by-morph"],
    "morphs/chimera": ["morphs/mosaic", "morphs/morphs-comparison-chart", "morphs/pigment-cells"],
    "morphs/leucistic": ["morphs/golden-albino", "morphs/pigment-cells",
                         "morphs/morphs-comparison-chart", "cost-and-buying/axolotl-price-by-morph"],
    "morphs/melanoid": ["morphs/pigment-cells", "morphs/wild-type",
                        "breeding/color-genetics-punnett-squares"],
    "morphs/golden-albino": ["morphs/leucistic", "morphs/pigment-cells",
                             "breeding/color-genetics-punnett-squares"],
    "morphs/gfp-axolotl": ["morphs/morphs-comparison-chart",
                           "breeding/color-genetics-punnett-squares",
                           "cost-and-buying/axolotl-price-by-morph"],
    "morphs/copper": ["morphs/pigment-cells", "breeding/color-genetics-punnett-squares",
                      "cost-and-buying/axolotl-price-by-morph"],
    "morphs/piebald": ["morphs/pigment-cells", "morphs/mosaic", "morphs/leucistic"],
    "morphs/pigment-cells": ["morphs/morphs-comparison-chart",
                             "breeding/color-genetics-punnett-squares", "morphs/melanoid"],
    "morphs/enigma-firefly-mac": ["morphs/pigment-cells", "morphs/copper", "morphs/melanoid"],
    "morphs/blue-and-pink-axolotl-myth": ["morphs/morphs-comparison-chart",
                                          "morphs/leucistic", "morphs/gfp-axolotl"],
    "morphs/morphs-comparison-chart": ["morphs/pigment-cells",
                                       "breeding/color-genetics-punnett-squares",
                                       "cost-and-buying/axolotl-price-by-morph"],
    "morphs/mosaic": ["morphs/chimera", "morphs/piebald", "morphs/morphs-comparison-chart"],
    "breeding/sexing-axolotls": ["breeding/genetics-and-inbreeding",
                                 "breeding/breeding-triggers-temperature-cycling"],
    "breeding/genetics-and-inbreeding": ["breeding/sexing-axolotls",
                                        "breeding/color-genetics-punnett-squares",
                                        "breeding/breeding-triggers-temperature-cycling"],
    "breeding/color-genetics-punnett-squares": ["breeding/genetics-and-inbreeding",
                                               "morphs/morphs-comparison-chart",
                                               "breeding/breeding-triggers-temperature-cycling"],
    "breeding/breeding-triggers-temperature-cycling": ["breeding/sexing-axolotls",
                                                       "breeding/genetics-and-inbreeding",
                                                       "breeding/egg-and-larvae-care"],
    "breeding/egg-and-larvae-care": ["breeding/breeding-triggers-temperature-cycling",
                                     "breeding/raising-juveniles",
                                     "diet/feeding-schedule-by-age"],
    "breeding/raising-juveniles": ["breeding/egg-and-larvae-care",
                                   "diet/feeding-schedule-by-age",
                                   "diet/blackworms-for-juveniles",
                                   "breeding/genetics-and-inbreeding"],
    "legal": ["legal/california", "legal/canada", "legal/virginia", "legal/new-jersey"],
    "legal/california": ["legal/virginia", "legal/new-jersey", "legal/canada", "axolotls/care-guide"],
    "legal/canada": ["legal/california", "legal/virginia", "legal/maine", "axolotls/care-guide"],
    "legal/hawaii": ["legal/california", "legal/canada", "legal/maine"],
    "legal/maine": ["legal/virginia", "legal/california", "legal/canada", "legal/hawaii"],
    "legal/new-jersey": ["legal/virginia", "legal/california", "legal/canada"],
    "legal/new-mexico": ["legal/california", "legal/maine", "legal/virginia"],
    "legal/virginia": ["legal/california", "legal/maine", "legal/new-jersey", "legal/new-mexico"],
    "care-basics": ["care-basics/are-axolotls-good-beginner-pets", "care-basics/axolotl-facts",
                    "care-basics/axolotl-age-and-size-chart", "care-basics/behavior"],
    "care-basics/are-axolotls-good-beginner-pets": ["care-basics/axolotls-and-children",
                                                    "care-basics/cost-of-ownership-monthly",
                                                    "tank-setup/setup-guide",
                                                    "cost-and-buying/breeder-vs-pet-store"],
    "care-basics/axolotl-age-and-size-chart": ["care-basics/are-axolotls-good-beginner-pets",
                                               "diet/feeding-schedule-by-age", "breeding/egg-and-larvae-care"],
    "care-basics/axolotl-facts": ["care-basics/how-to-pronounce-axolotl",
                                  "biology-and-science/regeneration-and-limb-regrowth",
                                  "biology-and-science/conservation-status"],
    "care-basics/axolotl-intelligence-and-bonding": ["care-basics/behavior", "care-basics/handling"],
    "care-basics/axolotls-and-children": ["care-basics/are-axolotls-good-beginner-pets",
                                          "care-basics/handling", "tank-setup/setup-guide",
                                          "cost-and-buying/how-to-choose-a-healthy-axolotl"],
    "care-basics/behavior": ["care-basics/axolotl-intelligence-and-bonding",
                             "health/curled-gills-stress-signal", "health/why-axolotl-floating"],
    "care-basics/cost-of-ownership-monthly": ["care-basics/are-axolotls-good-beginner-pets",
                                              "tank-setup/setup-guide", "tank-setup/aquarium-chillers",
                                              "cost-and-buying/axolotl-price-by-morph"],
    "care-basics/handling": ["care-basics/axolotls-and-children", "care-basics/keeping-multiple-axolotls",
                             "tank-setup/setup-guide"],
    "care-basics/how-to-pronounce-axolotl": ["care-basics/axolotl-facts", "axolotls/care-guide"],
    "care-basics/keeping-multiple-axolotls": ["care-basics/are-axolotls-good-beginner-pets",
                                              "tank-setup/tank-size-by-age", "care-basics/behavior"],
    "biology-and-science/anatomy-gills-and-lungs": ["biology-and-science/neoteny",
                                                    "biology-and-science/is-axolotl-amphibian",
                                                    "biology-and-science/wild-habitat-xochimilco",
                                                    "health/shrinking-gills"],
    "biology-and-science/axolotl-vs-tiger-salamander": ["biology-and-science/neoteny",
                                                        "biology-and-science/is-axolotl-amphibian"],
    "biology-and-science/conservation-status": ["biology-and-science/wild-habitat-xochimilco",
                                                "cost-and-buying/choosing-a-reputable-breeder",
                                                "axolotls/care-guide"],
    "biology-and-science/is-axolotl-amphibian": ["biology-and-science/anatomy-gills-and-lungs",
                                                 "biology-and-science/axolotl-vs-tiger-salamander"],
    "biology-and-science/lifespan-wild-vs-captivity": ["biology-and-science/conservation-status",
                                                       "biology-and-science/wild-habitat-xochimilco"],
    "biology-and-science/regeneration-and-limb-regrowth": ["health/limb-regeneration",
                                                           "biology-and-science/neoteny",
                                                           "biology-and-science/anatomy-gills-and-lungs",
                                                           "health/minor-scrapes-and-wounds"],
    "biology-and-science/neoteny": ["biology-and-science/axolotl-vs-tiger-salamander",
                                    "biology-and-science/is-axolotl-amphibian"],
    "biology-and-science/wild-habitat-xochimilco": ["biology-and-science/conservation-status",
                                                    "tank-setup/setup-guide",
                                                    "tank-setup/temperature"],
    "cost-and-buying": ["cost-and-buying/axolotl-price-by-morph", "cost-and-buying/breeder-vs-pet-store",
                        "cost-and-buying/how-to-choose-a-healthy-axolotl"],
    "cost-and-buying/axolotl-price-by-morph": ["morphs/wild-type", "morphs/leucistic",
                                               "care-basics/cost-of-ownership-monthly"],
    "cost-and-buying/breeder-vs-pet-store": ["cost-and-buying/choosing-a-reputable-breeder",
                                             "cost-and-buying/shipping-live-axolotls"],
    "cost-and-buying/choosing-a-reputable-breeder": ["cost-and-buying/breeder-vs-pet-store",
                                                     "cost-and-buying/red-flags-when-buying"],
    "cost-and-buying/how-to-choose-a-healthy-axolotl": ["cost-and-buying/red-flags-when-buying",
                                                        "cost-and-buying/choosing-a-reputable-breeder"],
    "cost-and-buying/red-flags-when-buying": ["cost-and-buying/choosing-a-reputable-breeder",
                                              "cost-and-buying/how-to-choose-a-healthy-axolotl"],
    "cost-and-buying/shipping-live-axolotls": ["cost-and-buying/breeder-vs-pet-store",
                                               "cost-and-buying/how-to-choose-a-healthy-axolotl",
                                               "tank-setup/acclimating-a-new-axolotl"],
    "axolotl-in-culture": ["axolotl-in-culture/minecraft-axolotls-guide",
                           "axolotl-in-culture/axolotl-in-pop-culture-and-memes",
                           "axolotl-in-culture/why-axolotls-are-suddenly-popular",
                           "axolotl-in-culture/adopt-me-axolotl-guide"],
    "axolotl-in-culture/minecraft-axolotls-guide": ["axolotl-in-culture/axolotl-in-pop-culture-and-memes",
                                                    "axolotl-in-culture/why-axolotls-are-suddenly-popular",
                                                    "morphs/blue-and-pink-axolotl-myth"],
    "axolotl-in-culture/axolotl-in-pop-culture-and-memes": ["axolotl-in-culture/why-axolotls-are-suddenly-popular",
                                                            "axolotl-in-culture/minecraft-axolotls-guide",
                                                            "gifts-and-merch/axolotl-squishmallow-guide"],
    "axolotl-in-culture/why-axolotls-are-suddenly-popular": ["axolotl-in-culture/minecraft-axolotls-guide",
                                                             "biology-and-science/conservation-status",
                                                             "care-basics/axolotl-facts",
                                                             "axolotl-in-culture/adopt-me-axolotl-guide"],
    "axolotl-in-culture/adopt-me-axolotl-guide": ["axolotl-in-culture/minecraft-axolotls-guide",
                                                  "care-basics/are-axolotls-good-beginner-pets",
                                                  "morphs/blue-and-pink-axolotl-myth"],
}

# Phase 8 semantic inline anchors: (phrase, target, anchor_label, replace_all).
# The phrase must already exist verbatim in the article body; the anchor label is
# the natural in-sentence text that becomes the link (identical to the phrase so
# no prose is rewritten). replace_all=true is used only where every occurrence of
# the phrase carries the same relationship (verified before adding).
SEMANTIC_INLINE = {
    "axolotls/care-guide": [
        ("Check your specific state and city before you buy", "/legal/",
         "Check your specific state and city before you buy", True),
        ("Check your specific state and city before buying", "/legal/",
         "Check your specific state and city before buying", True),
    ],
    "axolotl-in-culture/adopt-me-axolotl-guide": [
        ("check your local laws first", "/legal/", "check your local laws first", False),
    ],
    "biology-and-science/anatomy-gills-and-lungs": [
        ("health indicator", "/health/stress-signs/", "health indicator", False),
        ("Surface gulping", "/health/why-axolotl-floating/", "surface gulping", False),
    ],
}

# ---------------------------------------------------------------------------
# Phase 10 semantic-SEO layer
# ---------------------------------------------------------------------------

# Standfirst (intro) overrides. Used to re-scope a page's dominant intent
# without touching its docx-sourced body (cannibalization role splits).
INTRO_OVERRIDES = {
    "axolotl-in-culture/adopt-me-axolotl-guide": (
        "The Adopt Me axolotl is a legendary virtual pet originally sold through "
        "the Pet Shop. Players now usually obtain it by trading unless the game "
        "returns it to the shop."
    ),
    "cost-and-buying/axolotl-price-by-morph": (
        "As of August 27, 2026, common captive-bred axolotls in current US listings are "
        "usually advertised around $50–$100 before shipping. Morph, age, lineage, seller, "
        "and delivery cost change the total, so these figures are a market snapshot rather "
        "than guaranteed prices."
    ),
    "cost-and-buying/breeder-vs-pet-store": (
        "A specialist breeder is often the easiest source to verify, but the seller type "
        "alone does not prove quality. Compare the exact animal, water records, feeding "
        "history, written terms, and shipping or pickup plan."
    ),
    "cost-and-buying/choosing-a-reputable-breeder": (
        "Choose an axolotl breeder by the records and conditions they can show, not by "
        "follower count or a polished storefront. Ask the same 12 questions before paying "
        "for any animal."
    ),
    "cost-and-buying/how-to-choose-a-healthy-axolotl": (
        "Before buying, look for normal body condition, intact skin, balanced movement, "
        "recent feeding records, and measured water quality. Appearance can reveal warning "
        "signs, but a photo cannot diagnose an axolotl."
    ),
    "cost-and-buying/red-flags-when-buying": (
        "The strongest seller red flags are identity or animal details that cannot be "
        "verified, pressure to pay quickly, unsafe husbandry, vague written terms, and "
        "payment methods that remove buyer protection."
    ),
    "cost-and-buying/shipping-live-axolotls": (
        "A responsible shipment starts before the box is packed: the route must be legal, "
        "the carrier must accept amphibians, the weather must be suitable, and the recipient "
        "must be ready for the delivery."
    ),
    "care-basics/how-to-pronounce-axolotl": (
        "In modern English, pronounce axolotl as ACK-suh-lot-ul, with the stress "
        "on the first syllable. The Nahuatl source word and Spanish ajolote sound "
        "different, so this guide keeps the three forms separate."
    ),
    "tank-setup/filtration-for-axolotls": (
        "Before choosing a filter you need the principles: why axolotls need gentle, low-flow "
        "filtration, how waste becomes ammonia, and which filter families exist. This guides the "
        "options; the head-to-head canister-versus-sponge decision has its own dedicated guide."
    ),
    "tank-setup/aquarium-chillers": (
        "Axolotls require water between 60–68°F (15–20°C) to survive long-term, and most US homes "
        "maintain ambient temperatures of 68–78°F — which drives tank water above the safe ceiling "
        "without active cooling equipment."
    ),
    "biology-and-science/regeneration-and-limb-regrowth": (
        "This is the science page: why axolotls can regenerate limbs, organs, and even parts of "
        "the brain, at the cellular level. Owners looking for what to do when a limb is damaged "
        "should read the practical owner's guide instead."
    ),
    "health/limb-regeneration": (
        "An owner-facing guide to axolotl limb regeneration: what to expect, how to protect a "
        "healing limb, and when to worry. For the underlying biology, see the science page."
    ),
    "health/emergency-first-aid": (
        "Use this page to assess urgency and take safe first steps while arranging veterinary "
        "help. It cannot identify a disease from one sign and does not replace an "
        "exotics-experienced veterinarian."
    ),
    "health/finding-an-exotic-vet": (
        "Use this guide to locate and screen a veterinarian with amphibian experience, prepare "
        "for the visit, and understand that availability and costs vary by clinic and location."
    ),
    "health/fridging-sick-axolotl": (
        "Fridging is not routine home treatment. This page explains the risks and the questions "
        "to ask if an exotics-experienced veterinarian specifically recommends controlled "
        "refrigeration for an individual axolotl."
    ),
    "health/refusing-to-eat": (
        "Unexpected appetite loss is an observation, not a diagnosis. Check water parameters, "
        "temperature, recent feeding, stool, body condition, and other signs first; seek "
        "veterinary care promptly for severe, worsening, or persistent changes."
    ),
}

# Targeted corrections for externally stored DOCX text. Each source phrase is
# matched verbatim at build time so a future source revision cannot be silently
# overwritten by an outdated replacement.
BODY_TEXT_REPLACEMENTS = {
    "axolotl-in-culture/adopt-me-axolotl-guide": [
        (
            "Players who want one either hatch it during its event or trade for it afterward.",
            "The pet was originally sold through the Pet Shop, and players now usually obtain it by trading unless it returns to the shop.",
        ),
        (
            "There are 3 ways to get one: hatch it from a pet egg during its limited-time event, trade for it with other players, or buy it from the pet shop when it is re-released.",
            "The current route is trading with another player. The axolotl was originally sold as a premium Pet Shop pet, so it may also be available if Adopt Me returns it to the shop.",
        ),
        (
            "The axolotl appears during special events, so obtaining it is easiest while it is available.",
            "Availability changes with game updates, so check the current in-game Pet Shop before relying on an older guide.",
        ),
        (
            "Hatch it from a pet egg during its limited-time event.",
            "Check whether it has returned to the in-game Pet Shop.",
        ),
        (
            "Trade, hatch, or buy in pet shop",
            "Trade, or buy in the Pet Shop if re-released",
        ),
    ],
}


# Evidence-bounded color terminology override. The external DOCX used absolute
# claims ("no breeder has ever...") that exceed what the cited genetics sources establish.
COLOR_LABELS_BODY_OVERRIDE = r'''
<h2>Are pink axolotls real?</h2>
<p><strong>Yes. Pink-looking axolotls are common, but “pink” is an appearance label rather than one single genetic category.</strong> The Ambystoma Genetic Stock Center describes white/leucistic axolotls as having pinkish skin with dark eyes. Albino combinations can also look pale, white, yellow, or pinkish depending on which other pigment traits are present.</p>
<p>If you are trying to identify a pale animal, start with the eyes and the remaining pigment pattern. A pale body with dark eyes usually points toward the white/leucistic phenotype, while albino animals lack normal melanin production and have pinkish or reddish eyes.</p>

<h2>Is blue a recognized axolotl morph?</h2>
<p><strong>“Blue” is not one of the standard pigment mutations or stock designations documented by the Ambystoma Genetic Stock Center.</strong> That does not mean every photo described as blue is deliberately fake. Cool aquarium lighting, camera white balance, image editing, GFP fluorescence, and informal seller terminology can all make an animal appear more blue or cyan than it looks under neutral light.</p>
<p>So treat “blue axolotl” as a color claim that needs verification, not as a standardized genetic label. Ask for neutral-light photos, the animal's actual morph or lineage name, and whether GFP or colored lighting is involved.</p>

<h2>Are purple or lavender axolotls real morphs?</h2>
<p><strong>Purple and lavender are not standard AGSC pigment-mutation names.</strong> Breeders and hobbyists may use these words informally for a particular shade, line, lighting effect, or combination of recognized traits. If a listing uses only a color nickname, ask what established phenotype or genetic background the seller means.</p>

<h2>Are green axolotls real?</h2>
<p><strong>An axolotl can look green for more than one reason.</strong> Wild-type animals may have olive or greenish mottling, while GFP axolotls fluoresce green under suitable blue or ultraviolet illumination. GFP is a fluorescent trait that can occur on top of other pigment backgrounds; it is not simply a “green color morph.”</p>

<h2>What about yellow and golden axolotls?</h2>
<p><strong>Yellow or gold appearance often overlaps with albino pigment combinations.</strong> The AGSC describes an otherwise wild-type albino as yellow with reddish eyes and notes that this appearance is often called a golden albino. Other albino combinations can look paler or whiter.</p>

<h2>Color label vs recognized phenotype</h2>
<div class="table-wrap"><table>
<thead><tr><th>Common search/listing label</th><th>How to interpret it</th><th>Best next page</th></tr></thead>
<tbody>
<tr><td>Pink / white</td><td>Often leucistic/white or an albino combination; check eye color and pigment pattern.</td><td><a href="/morphs/leucistic/">Leucistic</a></td></tr>
<tr><td>Yellow / gold</td><td>Often golden-albino appearance or another albino combination.</td><td><a href="/morphs/golden-albino/">Golden albino</a></td></tr>
<tr><td>Green / glowing</td><td>May be olive wild-type appearance or GFP fluorescence under suitable light.</td><td><a href="/morphs/gfp-axolotl/">GFP</a></td></tr>
<tr><td>Blue / cyan</td><td>Not a standard AGSC pigment-mutation label; verify lighting, editing, GFP status, and lineage.</td><td><a href="/morphs/morphs-comparison-chart/">Morph comparison</a></td></tr>
<tr><td>Purple / lavender</td><td>Usually an informal shade or line name unless the seller can tie it to a defined phenotype/genetic background.</td><td><a href="/morphs/morphs-comparison-chart/">Morph comparison</a></td></tr>
</tbody></table></div>

<h2>How do you verify an axolotl color or morph?</h2>
<ol>
<li><strong>Ask for neutral-light photos</strong> of the exact animal, not a heavily processed promotional image.</li>
<li><strong>Check the eyes</strong> because eye pigment helps distinguish leucistic/white animals from albino combinations.</li>
<li><strong>Look for reflective shine, speckling, and patch pattern</strong> rather than judging only the overall hue.</li>
<li><strong>Ask whether the animal is GFP</strong> and under what light the photo was taken.</li>
<li><strong>Ask for the breeder's actual phenotype or lineage terminology</strong> if the listing uses a nickname such as blue, lavender, or neon.</li>
</ol>
<p>For side-by-side identification, use the <a href="/morphs/morphs-comparison-chart/">axolotl colors and morphs comparison</a>. For the biology behind color, see <a href="/morphs/pigment-cells/">pigment cells</a> and <a href="/breeding/color-genetics-punnett-squares/">color genetics</a>.</p>

<h2>Sources</h2>
<ul>
<li><a href="https://ambystoma.uky.edu/teachers-materials-menu/teachers-materials-books-menu?id=9">Ambystoma Genetic Stock Center: Mutant Genes</a></li>
<li><a href="https://ambystoma.uky.edu/axolotl-research2/12-educationresources/10-axolotl-strains">Ambystoma Genetic Stock Center: Axolotl Strains</a></li>
</ul>
'''


# Full render-time replacements for Health pages whose external DOCX source is
# either overly prescriptive or too absolute for safe owner-facing guidance.
# The source files remain the editorial record; these bodies define the public
# semantic role until the external source is revised.
BODY_OVERRIDES = {
    "morphs/blue-and-pink-axolotl-myth": COLOR_LABELS_BODY_OVERRIDE,
    "cost-and-buying/axolotl-price-by-morph": """
<p><strong>As of August 27, 2026, current US listings place many common captive-bred axolotls around $50&ndash;$100 before shipping.</strong> A morph name does not set a fixed price. Size, sex, lineage records, unusual patterning, seller, location, and delivery charges can move the total substantially.</p>
<h2>What Do Axolotls Cost by Morph in 2026?</h2>
<p>The ranges below are working US listing ranges observed across current breeder and marketplace pages. They describe asking prices, not completed-sale averages or guarantees.</p>
<div class="table-wrap"><table>
<thead><tr><th>Morph or listing type</th><th>Observed working range</th><th>What changes the price</th></tr></thead>
<tbody>
<tr><td>Wild type</td><td>$50&ndash;$90</td><td>Size, sex, seller, and whether shipping is included</td></tr>
<tr><td>Leucistic</td><td>$60&ndash;$110</td><td>Patterning, GFP status, size, and current stock</td></tr>
<tr><td>Melanoid or golden albino</td><td>$60&ndash;$120</td><td>Seller, age, size, and additional traits</td></tr>
<tr><td>Copper or axanthic</td><td>$65&ndash;$160</td><td>Lineage, expression, size, and combined recessive traits</td></tr>
<tr><td>GFP combinations</td><td>$75&ndash;$200+</td><td>The base morph, fluorescence status, size, and seller</td></tr>
<tr><td>Hypomelanistic or stacked-trait listings</td><td>$150&ndash;$400+</td><td>Scarcity, documented lineage, phenotype, and seller</td></tr>
<tr><td>Mosaic or chimera-labelled animals</td><td>No stable band; often several hundred dollars</td><td>Each animal is unusual, labels are sometimes disputed, and listings are sparse</td></tr>
</tbody></table></div>
<p>A current MorphMarket listing showed a juvenile copper at $65, while another adult copper was listed at $150 before shipping. Current GFP leucistic listings included examples near $65, $75, $90, $110, and $125. Mosaic-labelled examples ranged from $75 to $1,000, which is why a single “mosaic price” is misleading.</p>
<h2>How Much Does Shipping Add?</h2>
<p><strong>Current US listing examples add roughly $20&ndash;$100 for shipping and packaging.</strong> MorphMarket listings commonly show shipping bands around $20&ndash;$80. One large retailer lists $47.95 for priority overnight delivery plus a $12 packaging fee, while another advertises $20 flat-rate overnight shipping.</p>
<p>Compare the delivered total, not the animal price alone. A $65 axolotl with $75 shipping costs more than an $85 local animal, and local pickup avoids transit risk.</p>
<h2>Why Do Prices Vary So Much?</h2>
<ul>
<li><strong>Morph and combined traits:</strong> common single-trait animals usually have more supply than uncommon combinations.</li>
<li><strong>Size and confirmed sex:</strong> older animals cost more to raise, and confirmed adults may be priced differently.</li>
<li><strong>Individual appearance:</strong> unusual spotting, gill color, or symmetry can raise an asking price even within one morph.</li>
<li><strong>Documentation:</strong> clear parentage, hatch date, feeding history, and current photos make the listing easier to assess.</li>
<li><strong>Delivery:</strong> overnight service, insulated packaging, weather holds, and rural surcharges change the final total.</li>
</ul>
<h2>Does a Higher Price Mean a Healthier Axolotl?</h2>
<p><strong>No. Price reflects the listing and market, not a medical assessment.</strong> Use the <a href="/cost-and-buying/how-to-choose-a-healthy-axolotl/">healthy-axolotl buyer checklist</a> and ask for measured water parameters, a feeding history, current media of the exact animal, and written arrival terms. A cheaper common morph with good records can be a better purchase than an expensive animal with vague history.</p>
<h2>How Should You Use These Price Ranges?</h2>
<p>Use the table to build a budget and identify listings that need more questions. Do not treat the lower edge as a price a seller must match. Before paying, confirm that ownership and transport are legal at the origin and destination, then compare the delivered cost across several current listings.</p>
<div class="references-box"><h2>August 2026 Market Sources</h2><ul>
<li><a href="https://www.morphmarket.com/us/c/amphibians/axolotls">MorphMarket: current US axolotl listings</a></li>
<li><a href="https://axolotlplanet.com/collections/axolotls">Axolotl Planet: current axolotl catalog</a></li>
<li><a href="https://www.gillywateraquatics.com/shop-axolotls">Gillywater Aquatics: current axolotl listings</a></li>
<li><a href="https://axolotlsuperstore.com/">Axolotl Superstore: current prices and shipping</a></li>
<li><a href="https://www.bigappleherp.com/products/axolotl-for-sale">Big Apple Herp: current animal and shipping prices</a></li>
</ul><p>MyAxolotl sampled publicly displayed asking prices on August 27, 2026. Stock, sales, and shipping charges can change without notice.</p></div>
""",
    "cost-and-buying/breeder-vs-pet-store": """
<p><strong>A reputable specialist breeder is often easier to evaluate than a general pet store, but no seller type guarantees a healthy axolotl.</strong> Compare the exact animal, its care records, the water it is kept in, the written terms, and the handoff plan.</p>
<h2>How Do Breeders and Pet Stores Compare?</h2>
<div class="table-wrap"><table>
<thead><tr><th>Source</th><th>Main advantage</th><th>Main limitation</th><th>Best verification step</th></tr></thead>
<tbody>
<tr><td>Specialist breeder</td><td>May provide parentage, hatch date, feeding history, and support</td><td>Quality varies; online purchases may require shipping</td><td>Ask for current media and written husbandry and arrival terms</td></tr>
<tr><td>Independent exotic pet store</td><td>You can inspect the animal and holding system in person</td><td>Staff knowledge and supplier records vary</td><td>Ask who bred the animal and see measured water results</td></tr>
<tr><td>Marketplace breeder</td><td>Many sellers and prices can be compared</td><td>The platform does not replace seller verification</td><td>Review identity, history, policies, and the exact listing</td></tr>
<tr><td>Local rehome</td><td>Local pickup and a known individual animal</td><td>Records and support may be limited</td><td>Confirm current care, reason for rehoming, and equipment needs</td></tr>
</tbody></table></div>
<h2>When Is a Breeder the Better Choice?</h2>
<p>Choose a breeder when the seller can show useful records: the hatch date or age estimate, foods accepted, measured temperature and water chemistry, parentage or lineage notes where available, and current photos or video of the exact axolotl. A breeder should also explain what happens if delivery is delayed or the animal arrives in poor condition.</p>
<p>Specialization is useful only when the records support it. A large social following, a long morph list, or a claim of “health-tested” animals is not a substitute for specific evidence.</p>
<h2>When Can a Pet Store Be a Good Option?</h2>
<p>An independent exotic pet store can be a reasonable choice when its axolotl system is cool, clean, uncrowded, and managed separately from warm tropical displays. The University of Kentucky Ambystoma Genetic Stock Center keeps axolotls at 60&ndash;65°F (15&ndash;18°C), which gives buyers a useful reference for evaluating the store's temperature.</p>
<p>Ask the store who supplied the animal, how long it has been there, what it eats, and what the current ammonia and nitrite readings are. If staff cannot retrieve those details, treat the missing information as uncertainty rather than assuming the animal is healthy.</p>
<h2>Which Source Is Usually Cheaper?</h2>
<p><strong>Compare delivered cost instead of assuming one channel is cheaper.</strong> A breeder may have a lower animal price but add overnight delivery and packaging. A local store may charge more but avoid shipping. Rehomes can be inexpensive, but equipment or veterinary assessment may add cost.</p>
<h2>What Should Every Seller Provide?</h2>
<ul>
<li>Current photos or video of the exact animal</li>
<li>A recent feeding history and the food currently accepted</li>
<li>Measured temperature, ammonia, and nitrite information</li>
<li>Any available age, parentage, morph, and health-history records</li>
<li>Written payment, pickup or shipping, and live-arrival terms</li>
<li>A direct answer about whether the animal is captive-bred</li>
</ul>
<p>Use the <a href="/cost-and-buying/choosing-a-reputable-breeder/">12-question breeder checklist</a> for a seller interview and the <a href="/cost-and-buying/how-to-choose-a-healthy-axolotl/">buyer health checklist</a> for the animal itself.</p>
<div class="references-box"><h2>Sources</h2><ul><li><a href="https://ambystoma.uky.edu/education1/guide-to-axolotl-husbandry">Ambystoma Genetic Stock Center: Guide to Axolotl Husbandry</a></li></ul></div>
""",
    "cost-and-buying/choosing-a-reputable-breeder": """
<p><strong>Choose an axolotl breeder by what the breeder can document and show.</strong> A professional-looking site or popular account may help you find a seller, but current animal records, husbandry answers, identity, and written terms are stronger evidence.</p>
<h2>What 12 Questions Should You Ask an Axolotl Breeder?</h2>
<ol>
<li>Is this axolotl captive-bred, and did you breed it yourself?</li>
<li>What is its hatch date or best age estimate?</li>
<li>Can you send a current photo or short video of this exact animal?</li>
<li>What foods does it currently accept, and when did it last eat?</li>
<li>What are its current water temperature, ammonia, nitrite, nitrate, and pH readings?</li>
<li>Has it shown any recent injury, appetite, buoyancy, skin, or gill changes?</li>
<li>What parentage or lineage records are available?</li>
<li>How do you prevent accidental or poorly planned close-relative pairings?</li>
<li>How long do you observe new or returned animals separately from established stock?</li>
<li>What support do you provide after pickup or delivery?</li>
<li>What are the written live-arrival, delay, and claim terms?</li>
<li>Which carrier and service will be used, and what weather conditions trigger a hold?</li>
</ol>
<p>A useful answer includes numbers, dates, photos, or a written policy. “Perfect water,” “premium genetics,” and “guaranteed healthy” are marketing phrases unless the seller explains what they mean.</p>
<h2>What Should a Breeder's Husbandry Show?</h2>
<p>Look for cool, dechlorinated water; measured water chemistry; appropriate space; low waste accumulation; secure containers; and animals separated when size or breeding risk requires it. The University of Kentucky Ambystoma Genetic Stock Center reports keeping axolotls at 60&ndash;65°F (15&ndash;18°C). A breeder does not need to copy a laboratory system, but should be able to explain how temperature and water quality are monitored.</p>
<h2>How Should You Assess Genetics and Parentage?</h2>
<p><strong>Ask for records without expecting a promise of genetic perfection.</strong> Captive axolotl lineages can be incomplete, and a morph name does not prove health or unrelated ancestry. A responsible breeder should distinguish known parentage from assumptions and explain why a pairing was chosen.</p>
<p>Do not rely on claims that one pedigree guarantees a long lifespan or that every close-relative pairing produces visible defects. The practical buyer question is whether the breeder keeps accurate records, avoids careless repeat pairings, and states uncertainty honestly.</p>
<h2>How Do You Verify the Seller?</h2>
<ul>
<li>Confirm the seller's name, contact details, and consistent sales history.</li>
<li>Reverse-search listing photos and request new media with a date or agreed identifier.</li>
<li>Read recent reviews, including how the seller handled delays or problems.</li>
<li>Keep the listing, invoice, written policy, and messages before paying.</li>
<li>Use a payment method with applicable buyer protection.</li>
</ul>
<p>Community feedback can reveal patterns, but one anonymous complaint or endorsement should not decide the purchase by itself.</p>
<h2>Which Answers Should Stop the Purchase?</h2>
<p>Walk away if the seller cannot show the animal, refuses basic husbandry questions, uses unsafe water or substrate, misrepresents the route's legality, changes written terms after payment, or demands gift cards. The Federal Trade Commission warns that gift cards are for gifts, not payments.</p>
<section class="faq"><h2>Frequently Asked Questions</h2></section>
<div class="references-box"><h2>Sources</h2><ul>
<li><a href="https://ambystoma.uky.edu/education1/guide-to-axolotl-husbandry">Ambystoma Genetic Stock Center: Guide to Axolotl Husbandry</a></li>
<li><a href="https://consumer.ftc.gov/articles/avoiding-and-reporting-gift-card-scams">Federal Trade Commission: Avoiding and Reporting Gift Card Scams</a></li>
</ul></div>
""",
    "cost-and-buying/how-to-choose-a-healthy-axolotl": """
<p><strong>Before buying an axolotl, check body condition, skin, gills, movement, recent feeding, and the water it is living in.</strong> These observations can identify reasons to pause a purchase, but they cannot diagnose a disease from a photo or short visit.</p>
<h2>What Should You Check Before Buying?</h2>
<div class="table-wrap"><table>
<thead><tr><th>Check</th><th>Reassuring observation</th><th>Reason to pause and ask more</th></tr></thead>
<tbody>
<tr><td>Body condition</td><td>Proportionate body and tail with no marked wasting or sudden swelling</td><td>Very thin body, pronounced asymmetry, or unexplained swelling</td></tr>
<tr><td>Skin</td><td>Intact surface appropriate for the morph</td><td>Open wounds, bleeding, ulcers, heavy shedding, or attached growth</td></tr>
<tr><td>Gills</td><td>Gill tissue present with no obvious damage or attached material</td><td>Rapid change, injury, unusual discharge, or severe deterioration</td></tr>
<tr><td>Posture and movement</td><td>Balanced position and coordinated movement when the animal moves on its own</td><td>Persistent inability to stay upright, uncontrolled floating, or poor coordination</td></tr>
<tr><td>Feeding history</td><td>Seller can name the food, portion, and last accepted meal</td><td>No recent record, repeated refusal, or sudden change without explanation</td></tr>
<tr><td>Water records</td><td>Seller provides measured temperature, ammonia, and nitrite</td><td>Only says the water is “fine” or cannot provide readings</td></tr>
</tbody></table></div>
<h2>Can Gills or Skin Diagnose an Illness?</h2>
<p><strong>No single visible feature diagnoses an axolotl illness.</strong> Gill size and posture vary with anatomy, activity, flow, and environment. White material can have more than one cause. Redness, lesions, lethargy, appetite change, and abnormal position are clinical signs that require context and sometimes veterinary testing.</p>
<p>The Merck Veterinary Manual notes that amphibian infections can produce overlapping signs and may require microscopy, culture, histology, or other diagnostics. Treat a concerning sign as a reason not to complete the purchase until the seller explains it or an exotics-experienced veterinarian assesses it.</p>
<h2>Should You Tap the Glass or Demand a Feeding Demonstration?</h2>
<p><strong>Do not tap the glass to test an axolotl.</strong> Observe undisturbed movement and breathing, and ask the seller for a recent feeding video or written feeding history. An axolotl may not eat on demand during a brief visit, so one refused meal does not prove illness.</p>
<p>A repeated appetite change combined with weight loss, abnormal posture, skin damage, or poor water records is more meaningful than one moment of behavior.</p>
<h2>What Records Should You Request?</h2>
<ul>
<li>A current photo or video of the exact axolotl</li>
<li>Hatch date or age estimate and current length</li>
<li>Food type, feeding frequency, and last accepted meal</li>
<li>Current temperature, ammonia, nitrite, nitrate, and pH</li>
<li>Recent injury, treatment, appetite, buoyancy, or skin history</li>
<li>Written pickup, shipping, and live-arrival terms</li>
</ul>
<h2>What Should You Do After Choosing an Axolotl?</h2>
<p>Prepare a fully cycled, temperature-appropriate setup before pickup or delivery. If other axolotls are already present, use a separate observation or quarantine setup and discuss an appropriate plan with an exotics-experienced veterinarian. Use the <a href="/tank-setup/acclimating-a-new-axolotl/">new-axolotl acclimation guide</a> for the handoff.</p>
<section class="faq"><h2>Frequently Asked Questions</h2></section>
<div class="references-box"><h2>Sources and Scope</h2><ul>
<li><a href="https://ambystoma.uky.edu/education1/guide-to-axolotl-husbandry">Ambystoma Genetic Stock Center: Guide to Axolotl Husbandry</a></li>
<li><a href="https://www.merckvetmanual.com/exotic-and-laboratory-animals/amphibians/infectious-diseases-of-amphibians">Merck Veterinary Manual: Infectious Diseases of Amphibians</a></li>
</ul><p>This page is a pre-purchase observation checklist, not a veterinary diagnosis.</p></div>
""",
    "cost-and-buying/red-flags-when-buying": """
<p><strong>The strongest axolotl seller red flags are facts that cannot be verified, unsafe care, pressure to pay quickly, missing written terms, and payment methods that remove buyer protection.</strong> One unusual detail deserves a question; a pattern of contradictions is a reason to stop.</p>
<h2>Which Red Flags Should Stop an Axolotl Purchase?</h2>
<div class="table-wrap"><table>
<thead><tr><th>Red flag</th><th>Why it matters</th><th>What to request</th></tr></thead>
<tbody>
<tr><td>Seller cannot show the exact animal</td><td>The listing may use stolen, old, or unrelated media</td><td>A new photo or video with a date or agreed identifier</td></tr>
<tr><td>Water claims have no readings</td><td>“Perfect water” cannot be checked</td><td>Temperature, ammonia, nitrite, nitrate, and pH</td></tr>
<tr><td>Details change between messages</td><td>Age, morph, size, or history may be misrepresented</td><td>A written invoice describing the animal</td></tr>
<tr><td>Pressure to pay immediately</td><td>Urgency can prevent verification</td><td>Time to review terms and confirm identity</td></tr>
<tr><td>No written arrival or delay policy</td><td>Buyer and seller may disagree after a shipping problem</td><td>Claim window, required evidence, exclusions, and remedy</td></tr>
<tr><td>Gift-card payment demanded</td><td>Gift-card numbers transfer value with little recovery protection</td><td>A normal, traceable payment method</td></tr>
</tbody></table></div>
<h2>How Do You Verify the Exact Animal?</h2>
<p>Ask for a current photo or short video that shows the full animal and an agreed identifier, such as the date or your initials on paper beside the container. Reverse-image search the listing photo. Compare markings, size, and gill shape across the seller's media.</p>
<p>A seller does not have to accept an unscheduled video call to be legitimate. The important point is whether the seller can provide fresh, specific evidence and answer consistent questions.</p>
<h2>Is a Low Price Automatically a Scam?</h2>
<p><strong>No. A low price is a prompt to verify the listing, not proof of fraud.</strong> Rehomes, sales, local pickup, and common morphs can cost less. Compare the price with several current listings for the same morph, size, and delivery method, then verify the animal and terms.</p>
<p>Rare labels deserve extra scrutiny because “mosaic,” “chimera,” “GFP,” and stacked-trait names can be misunderstood or misused. A high price also does not prove the label or the animal's health.</p>
<h2>Which Payment Methods Are Risky?</h2>
<p>The Federal Trade Commission says gift cards are for gifts, not payments. Do not send gift-card numbers to an animal seller. Be cautious with wire transfers, cryptocurrency, and friends-and-family transfers because recovery or purchase protection may be limited.</p>
<p>Before paying, read the protection rules for the exact payment method and transaction type. Save the listing, invoice, seller identity, policy, and messages.</p>
<h2>When Should You Walk Away?</h2>
<p>End the purchase if the seller will not verify the animal, cannot describe its current care, demands an unsafe payment method, changes the deal after payment, or proposes an illegal or carrier-prohibited route. Another listing is cheaper than recovering from a scam or unsafe shipment.</p>
<section class="faq"><h2>Frequently Asked Questions</h2></section>
<div class="references-box"><h2>Consumer Source</h2><ul><li><a href="https://consumer.ftc.gov/articles/avoiding-and-reporting-gift-card-scams">Federal Trade Commission: Avoiding and Reporting Gift Card Scams</a></li></ul></div>
""",
    "cost-and-buying/shipping-live-axolotls": """
<p><strong>Axolotls are commonly sent in a sealed, leak-resistant primary container inside an insulated outer box using a carrier service that accepts amphibians.</strong> Safe shipping depends on legal routing, approved packaging, weather, service timing, and a recipient who can receive the box promptly.</p>
<h2>What Should You Confirm Before an Axolotl Ships?</h2>
<ul>
<li>Ownership and transport are legal at the origin, destination, and any relevant jurisdiction.</li>
<li>The named carrier accepts amphibians under the seller's account and packaging arrangement.</li>
<li>The service is scheduled to avoid weekends, holidays, and known delay periods.</li>
<li>The seller has checked temperatures along the route and defined weather-hold limits.</li>
<li>You will be available for delivery or approved hub pickup.</li>
<li>The live-arrival and carrier-delay terms are in writing.</li>
</ul>
<p>FedEx states that harmless amphibians can be shipped, but requires packaging approval and directs live-animal shipments to overnight services Monday through Thursday for weekday arrival. UPS lists amphibians among accepted live animals and requires next-day service, compliant packaging, and no Friday or pre-holiday tender. Carrier rules can change, so the seller must verify the current policy for the actual shipment.</p>
<h2>How Is an Axolotl Packaged?</h2>
<div class="table-wrap"><table>
<thead><tr><th>Layer</th><th>Purpose</th><th>What the buyer should verify</th></tr></thead>
<tbody>
<tr><td>Primary container</td><td>Contains the axolotl and water without leaking</td><td>Secure closure and enough room for the animal</td></tr>
<tr><td>Secondary containment</td><td>Reduces leak risk if the first layer fails</td><td>Seller can describe the bagging or container method</td></tr>
<tr><td>Insulation and cushioning</td><td>Limits temperature change and movement</td><td>Box suits the route, season, and animal size</td></tr>
<tr><td>Temperature control when needed</td><td>Offsets route conditions</td><td>Pack choice follows forecast and tested packaging, not season alone</td></tr>
<tr><td>Outer box and label</td><td>Protects the shipment and identifies live contents</td><td>Carrier-compliant box, label, and service</td></tr>
</tbody></table></div>
<p>A heat or cold pack is not automatically correct because the calendar says winter or summer. The shipper must account for the forecast, route, box insulation, pack placement, and risk of direct contact.</p>
<h2>What Should the Live-Arrival Policy Say?</h2>
<p><strong>A live-arrival policy should define the claim window, evidence, exclusions, and remedy before payment.</strong> Check whether carrier delay, missed delivery, unsafe destination weather, address errors, and hub pickup are covered. A guarantee is a contract term, not proof that the packing method is safe.</p>
<p>If the policy requires an unboxing video, prepare to film the sealed box, shipping label, opening, and animal without breaks. Contact the seller within the stated window if anything is wrong.</p>
<h2>What Should You Do When the Box Arrives?</h2>
<ol>
<li>Bring the package indoors immediately and inspect it for damage or leakage.</li>
<li>Record the opening if the written policy requires evidence.</li>
<li>Check the animal and water temperature without prolonged handling.</li>
<li>Follow the seller's written axolotl-specific arrival instructions and use a prepared, cycled observation or quarantine setup.</li>
<li>For an overnight-shipped animal, avoid leaving it in opened transport water for a long mixing process. Transfer it promptly under the applicable protocol and discard the shipping water.</li>
<li>Contact the seller and an exotics-experienced veterinarian promptly if the axolotl is injured, unresponsive, unable to remain upright, or otherwise in severe distress.</li>
</ol>
<p>The detailed handoff belongs in the <a href="/tank-setup/acclimating-a-new-axolotl/">new-axolotl acclimation guide</a>. The shipping page covers the seller, carrier, package, and arrival terms.</p>
<h2>What Temperature Should the Shipment Protect?</h2>
<p>The University of Kentucky Ambystoma Genetic Stock Center reports keeping axolotls at 60&ndash;65°F (15&ndash;18°C) and warns against temperatures above about 72°F (22°C). A shipper should use a tested packaging plan that limits unsafe exposure rather than promise that the box will hold one exact temperature for the entire route.</p>
<section class="faq"><h2>Frequently Asked Questions</h2></section>
<div class="references-box"><h2>Carrier and Husbandry Sources</h2><ul>
<li><a href="https://www.fedex.com/en-us/shipping/how-to-ship-live-animals.html">FedEx: How to Ship Live Animals</a></li>
<li><a href="https://www.ups.com/us/en/support/shipping-support/shipping-special-care-regulated-items/prohibited-items/plants-and-animals">UPS: How to Ship Plants and Live Animals</a></li>
<li><a href="https://ambystoma.uky.edu/education1/guide-to-axolotl-husbandry">Ambystoma Genetic Stock Center: Guide to Axolotl Husbandry</a></li>
</ul></div>
""",
    "care-basics/how-to-pronounce-axolotl": """
<p><strong>In modern English, pronounce axolotl as ACK-suh-lot-ul, with the stress on ACK.</strong> Cambridge gives the British pronunciation as /ˈæk.sə.lɒt.əl/ and the American pronunciation as /ˈæk.sə.lɑː.t̬əl/. Both use four syllables and first-syllable stress.</p>
<h2>What Is the English Syllable Breakdown?</h2>
<div class="table-wrap"><table>
<thead><tr><th>Part</th><th>Say it like</th><th>Note</th></tr></thead>
<tbody>
<tr><td>Ax</td><td><strong>ACK</strong></td><td>This syllable carries the stress.</td></tr>
<tr><td>o</td><td>suh</td><td>Use a short, unstressed vowel.</td></tr>
<tr><td>lot</td><td>lot</td><td>The vowel varies slightly between British and American English.</td></tr>
<tr><td>l</td><td>ul</td><td>Finish lightly rather than forcing a separate “t-l” cluster.</td></tr>
</tbody></table></div>
<p>Say the parts slowly as ACK-suh-lot-ul, then join them without adding a fifth syllable. Normal accent differences can change the vowel in “lot,” but they do not move the primary stress away from the first syllable in the cited English dictionary forms.</p>
<h2>What Are the Most Common English Mistakes?</h2>
<ul>
<li><strong>Moving the stress:</strong> ack-suh-LOT-ul does not match the cited British or American dictionary stress.</li>
<li><strong>Reading every letter separately:</strong> ax-oh-lot-oh-tul adds sounds that are not in the English dictionary form.</li>
<li><strong>Forcing the ending:</strong> English speakers can finish with a light “t-ul” sound; they do not need to reproduce the Nahuatl final consonant.</li>
</ul>
<h2>Is the English Pronunciation the Same as Nahuatl?</h2>
<p><strong>No. The English pronunciation is an established loanword pronunciation, not a reproduction of the Nahuatl source.</strong> The Online Nahuatl Dictionary records <em>axolotl</em> with the IPA spelling /ɑːʃoːloːtɬ/. In that form, the “x” represents a “sh” sound, and the final /tɬ/ is a lateral affricate that English does not normally use.</p>
<p>The spelling therefore follows two different sound systems. In English <em>axolotl</em>, the opening letters are pronounced “ack-s.” In the recorded Nahuatl form, the “x” is closer to English “sh.” Explaining the English “x” as an “ks” sound is useful only for the modern English word, not for Nahuatl pronunciation.</p>
<h2>How Do You Pronounce Axolotl in Spanish?</h2>
<p><strong>The usual Spanish word is <em>ajolote</em>, pronounced approximately ah-ho-LO-teh.</strong> The Real Academia Española traces <em>ajolote</em> to Nahuatl <em>axolotl</em>. Spanish changes the spelling as well as the sounds, so <em>ajolote</em> should not be used as the syllable guide for the English word.</p>
<h2>What Does the Word Axolotl Mean?</h2>
<p><strong><em>Axolotl</em> is a Nahuatl name for the animal.</strong> Popular literal glosses such as “water dog” and “water monster” vary by source and depend on a proposed analysis of the word. The dictionaries cited here establish the Nahuatl origin, but they do not support treating one of those English glosses as the single settled translation.</p>
<h2>How Can You Remember the English Pronunciation?</h2>
<p>Start with the stressed word “ACK,” add “suh,” and finish with “lot-ul”: ACK-suh-lot-ul. If the stress lands on the first syllable and the word has four syllables, the result matches the cited modern English pronunciation.</p>
<div class="references-box"><h2>Pronunciation Sources</h2><ul>
<li><a href="https://dictionary.cambridge.org/pronunciation/english/axolotl">Cambridge Dictionary: English pronunciation of axolotl</a></li>
<li><a href="https://nahuatl.wired-humanities.org/content/axolotl">Online Nahuatl Dictionary: axolotl</a></li>
<li><a href="https://dle.rae.es/ajolote">Real Academia Española: ajolote</a></li>
</ul><p>The respelling on this page is an English reading aid. IPA gives the more precise dictionary forms.</p></div>
""",
    "health/finding-an-exotic-vet": """
<p>An axolotl may need a veterinarian who is comfortable with aquatic amphibians. The goal is not to find a clinic with a particular label; it is to confirm that a named veterinarian can assess an axolotl, interpret husbandry records, and arrange appropriate diagnostics or referral.</p>
<h2>Where to Look for an Axolotl Veterinarian</h2>
<p>Start with the <a href="https://arav.org/find-a-vet/">Association of Reptile and Amphibian Veterinarians Find a Vet directory</a>. You can also call veterinary teaching hospitals, zoo or wildlife medicine services, and local exotic-animal clinics. A directory listing is a starting point, not proof that a clinic currently sees axolotls, so confirm by phone.</p>
<p>If the nearest suitable clinic is far away, ask a local veterinarian whether they can consult with or refer to an amphibian-experienced colleague. Some clinics may offer teletriage or remote follow-up where local rules permit it, but an examination or diagnostics may still need to happen in person.</p>
<h2>Questions to Ask Before Booking</h2>
<p>Ask the receptionist to check with the veterinarian rather than relying on the clinic name alone:</p>
<ul>
<li>Does a named veterinarian currently examine axolotls or other aquatic salamanders?</li>
<li>Can the clinic evaluate water-quality records and collect appropriate samples if needed?</li>
<li>What should you bring, and how should the axolotl be transported?</li>
<li>Does the clinic handle urgent cases, or where does it refer after hours?</li>
<li>Can it provide a written estimate for the exam and likely diagnostics?</li>
</ul>
<p>A clinic that does not see axolotls may still be able to direct you to one that does. Establishing that contact before an emergency makes escalation faster.</p>
<h2>What to Prepare for the Appointment</h2>
<p>Bring a short timeline of the problem and objective husbandry records. Useful information includes current and recent ammonia, nitrite, nitrate, pH, and water-temperature readings; tank volume; filtration and cycling history; water-change routine; substrate; tank mates; diet; last meal; last observed stool; recent additions or treatments; and clear photos or video of the change.</p>
<p>Ask the clinic how to transport the animal. Avoid unnecessary handling, sudden temperature changes, and improvised medications or baths before the appointment unless the treating veterinarian gives specific instructions.</p>
<h2>Costs and Remote Advice</h2>
<p>Exam, emergency, diagnostic, imaging, and medication costs vary by clinic and location. Ask what the initial exam includes, whether an emergency surcharge applies, and when the clinic can provide an estimate. A price quoted by another owner or an old article is not a reliable budget for an individual case.</p>
<p>Remote contact can help a clinic judge urgency or prepare for arrival, but photos and water readings cannot replace every physical examination or diagnostic test. The veterinarian should decide what is sufficient for the case and what local professional rules allow.</p>
<h2>When to Call Promptly</h2>
<p>Use the <a href="/health/emergency-first-aid/">emergency first-aid guide</a> when signs are sudden, severe, or worsening. Breathing difficulty, inability to remain upright, uncontrolled bleeding, major injury, marked swelling, rapid deterioration, or extensive skin damage warrant urgent contact. Persistent appetite loss, weight loss, abnormal buoyancy, skin or gill changes, and recurrent problems also deserve veterinary assessment even when water and temperature have been corrected.</p>
<p>A symptom is not a diagnosis. Record what you can observe and let the veterinarian determine whether the cause is environmental, infectious, traumatic, nutritional, obstructive, or something else.</p>
<section class="faq"><h2>Frequently Asked Questions</h2></section>
<div class="references-box"><h2>Sources and Scope</h2><ul>
<li><a href="https://arav.org/find-a-vet/">Association of Reptile and Amphibian Veterinarians: Find a Vet</a></li>
<li><a href="https://www.merckvetmanual.com/exotic-and-laboratory-animals/amphibians/clinical-techniques-in-amphibians">Merck Veterinary Manual: Clinical Techniques in Amphibians</a></li>
</ul><p>This guide helps owners locate care and prepare records. It does not diagnose a condition or replace a veterinarian.</p></div>
""",
    "health/fridging-sick-axolotl": """
<p>Fridging means keeping an axolotl in deliberately colder water under a controlled care plan. It is not a routine home treatment for appetite loss, floating, bloating, constipation, fungus, heat stress, or an axolotl that simply appears unwell.</p>
<h2>What Controlled Cooling Can and Cannot Do</h2>
<p>Axolotls are ectotherms, so water temperature affects their metabolism. That fact explains why a veterinarian may sometimes consider controlled cooling as supportive care. It does not show that cooling will remove a swallowed object, identify an infection, cure a skin lesion, or correct the cause of abnormal buoyancy.</p>
<p>Several unrelated problems can produce the same visible signs. Bloating, reduced stool, floating, and appetite loss can raise concern, but they do not confirm impaction or tell an owner to use a refrigerator. A veterinarian needs the animal's history, examination findings, and sometimes imaging or laboratory testing to judge the cause and the safest response.</p>
<h2>Why a Household Refrigerator Is Risky</h2>
<p>Household refrigerators are designed for food, not aquatic patients. Water can cool differently from the appliance display, and shelves may have cold spots, cycling swings, vibration, darkness, and limited space for safe observation. An unsuitable temperature, transition, duration, or water-change plan can add stress, worsen water quality, or delay needed care.</p>
<p>Freezing is never safe. Do not use ice, a freezer, or an improvised rapid-cooling method. Do not copy a generic temperature or number of days from a forum, social post, or timetable: there is no universal protocol that is safe for every cause, age, body condition, or refrigerator.</p>
<h2>What to Do Before Considering Fridging</h2>
<ol>
<li>Check measured water parameters and temperature; do not infer them from how the tank looks.</li>
<li>Record appetite, stool, belly shape, buoyancy, posture, breathing, skin and gill changes, injuries, and recent tank changes.</li>
<li>Correct a measured husbandry problem with the established <a href="/tank-setup/water-parameters-cycling/">water-quality</a> or <a href="/tank-setup/temperature/">temperature</a> guide.</li>
<li>Use the <a href="/health/emergency-first-aid/">emergency guide</a> for severe or rapidly worsening signs and contact an <a href="/health/finding-an-exotic-vet/">amphibian-experienced veterinarian</a>.</li>
</ol>
<p>A properly maintained hospital tub may sometimes provide temporary isolation, but tubbing and fridging are not interchangeable. The need for either depends on the animal, the water, the suspected cause, and the ability to maintain safe conditions.</p>
<h2>If a Veterinarian Recommends Controlled Cooling</h2>
<p>Ask for an individual written plan before starting. It should state:</p>
<ul>
<li>the purpose of cooling and what other treatment or testing is planned;</li>
<li>the exact measured water-temperature range and how quickly to transition;</li>
<li>the container, water preparation, water-change, and monitoring requirements;</li>
<li>whether food should be offered and how body condition will be tracked;</li>
<li>the review time, expected response, stop criteria, and emergency contact;</li>
<li>how to return the axolotl to normal housing without a sudden temperature change.</li>
</ul>
<p>If the plan is unclear, call the treating clinic rather than substituting an online protocol. A veterinarian's recommendation for one axolotl does not become a general rule for another.</p>
<h2>Monitoring and Escalation</h2>
<p>Follow the veterinarian's monitoring schedule and record measured water temperature, water changes, waste, posture, buoyancy, breathing, skin and gill appearance, and any treatment given. Contact the clinic if the measurements leave the prescribed range, the animal deteriorates, new signs appear, or the equipment cannot maintain the plan.</p>
<p>Do not extend controlled cooling because a generic timetable has not expired. The treating veterinarian should decide when to review, change, or stop the plan and how to transition the animal back to its normal environment.</p>
<section class="faq"><h2>Frequently Asked Questions</h2></section>
<div class="references-box"><h2>Sources and Scope</h2><ul>
<li><a href="https://pmc.ncbi.nlm.nih.gov/articles/PMC5487785/">A retrospective study of diseases in <em>Ambystoma mexicanum</em></a></li>
<li><a href="https://www.merckvetmanual.com/exotic-and-laboratory-animals/amphibians/environment-and-husbandry-for-amphibians">Merck Veterinary Manual: Environment and Husbandry for Amphibians</a></li>
</ul><p>These sources support careful temperature and husbandry management. They do not provide a universal household-refrigerator prescription; this page therefore limits fridging to an individual veterinary plan.</p></div>
""",
    "health/refusing-to-eat": """
<p>An axolotl not eating is an observation, not a diagnosis. One missed meal can occur without illness, especially in an adult, but an unusual or continuing change deserves measured water and temperature checks plus attention to body condition and other signs.</p>
<h2>Check for Urgent Warning Signs First</h2>
<p>Contact an amphibian-experienced veterinarian promptly when appetite loss appears with breathing difficulty, inability to remain upright or submerge, a firm or worsening swelling, major injury, uncontrolled bleeding, extensive skin damage, marked lethargy, rapid weight loss, or other rapid deterioration. Use the <a href="/health/emergency-first-aid/">emergency first-aid guide</a> while arranging help.</p>
<p>Duration matters, but it cannot set the same emergency threshold for every axolotl. Age, normal feeding schedule, body condition, temperature, and accompanying signs all change the level of concern. Juveniles normally feed more frequently than adults, so an unusual feeding change in a juvenile deserves quicker attention.</p>
<h2>What to Record and Check First</h2>
<ol>
<li><strong>Water:</strong> record ammonia, nitrite, nitrate, and pH from a reliable test. Check the tank, source water, and recent cycling or filter changes.</li>
<li><strong>Temperature:</strong> use a water thermometer and note recent peaks or swings, not only the reading at one moment.</li>
<li><strong>Feeding:</strong> record the last accepted meal, normal schedule, food type, portion size, freshness, and whether the axolotl refuses every food or only one item.</li>
<li><strong>Waste and exposure:</strong> note the last observed stool and any access to gravel, coarse substrate, tank-mate food, or loose objects.</li>
<li><strong>Other signs:</strong> record body condition, belly shape, buoyancy, posture, breathing, activity, injuries, and skin or gill changes. Photos and short videos can help a veterinarian compare changes over time.</li>
</ol>
<p>Normal results do not rule out illness, and one abnormal result does not prove it is the only cause. Similar signs may come from husbandry stress, food presentation, swallowed material, injury, infection, parasites, or other disease.</p>
<h2>Common Contexts to Consider</h2>
<ul>
<li><strong>Measured husbandry changes:</strong> unsafe water chemistry, excessive heat, strong flow, recent cycling disruption, or abrupt environmental change can reduce feeding.</li>
<li><strong>Food presentation:</strong> stale, oversized, tough, or unfamiliar food may be refused even when another appropriate staple is accepted.</li>
<li><strong>Stress or competition:</strong> recent transport, repeated handling, bright exposure, or a tank mate may change feeding behavior.</li>
<li><strong>Digestive or substrate concern:</strong> appetite loss with abnormal swelling, reduced stool, or buoyancy changes needs assessment; those signs do not confirm impaction by themselves.</li>
<li><strong>Illness, injury, or recovery:</strong> infection, parasites, mouth injury, systemic illness, or recent treatment may affect appetite and often require veterinary evaluation.</li>
</ul>
<p>This list is not ranked and cannot identify the cause from symptoms alone.</p>
<h2>Safe Steps While You Observe</h2>
<p>Correct a measured water or temperature problem using the <a href="/tank-setup/water-parameters-cycling/">water-quality guide</a> and <a href="/tank-setup/temperature/">temperature guide</a>. Keep conditions stable, reduce unnecessary handling, remove uneaten food, and offer a fresh, familiar staple in an appropriate size at the normal feeding time. Do not repeatedly change foods in one session.</p>
<p>Do not force-feed, raise the water temperature to speed digestion, start medication, give a bath, or fridge the axolotl based only on appetite loss or bloating. Those actions can add stress, obscure the clinical picture, or delay the care needed for the actual cause.</p>
<h2>When to Contact a Veterinarian</h2>
<p>Seek immediate help for the urgent warning signs above. For a stable axolotl, contact an <a href="/health/finding-an-exotic-vet/">exotics-experienced veterinarian</a> when refusal persists beyond the animal's normal pattern, recurs, is accompanied by weight or body-condition loss, or continues after a measured husbandry problem has been corrected.</p>
<p>Provide the clinic with the recorded water values, temperature history, feeding and stool timeline, photos, tank details, substrate exposure, and any products already used. That evidence is more useful than assigning a diagnosis at home.</p>
<h2>Planned Fasting Is a Different Question</h2>
<p>If food was deliberately withheld for travel or a planned absence and the axolotl otherwise appears normal, use the <a href="/diet/fasting-and-vacation/">planned fasting and vacation guide</a>. This page covers an unexpected change in appetite, not routine adult feeding intervals.</p>
<section class="faq"><h2>Frequently Asked Questions</h2></section>
<div class="references-box"><h2>Sources and Scope</h2><ul>
<li><a href="https://www.merckvetmanual.com/exotic-and-laboratory-animals/amphibians/environment-and-husbandry-for-amphibians">Merck Veterinary Manual: Environment and Husbandry for Amphibians</a></li>
<li><a href="https://www.merckvetmanual.com/exotic-and-laboratory-animals/amphibians/clinical-techniques-in-amphibians">Merck Veterinary Manual: Clinical Techniques in Amphibians</a></li>
<li><a href="https://pmc.ncbi.nlm.nih.gov/articles/PMC5487785/">A retrospective study of diseases in <em>Ambystoma mexicanum</em></a></li>
</ul><p>This guide supports observation and escalation. It does not diagnose the cause of appetite loss or prescribe treatment.</p></div>
""",
}

ROLE_CALLOUTS = {
    "diet/best-foods-list": (
        '<div class="role-note"><strong>Use this as the food-choice overview.</strong> '
        'Once you know the safe staples, use the <a href="/diet/feeding-schedule-by-age/">feeding schedule</a> '
        'for frequency and portions, the <a href="/diet/live-vs-frozen-food/">live vs. frozen comparison</a> '
        'for format choice, and the <a href="/diet/axolotl-pellets/">pellet guide</a> for commercial foods.</div>'
    ),
    "health/stress-signs": (
        '<div class="role-note"><strong>Which stress sign are you seeing?</strong> '
        "Stress covers many signs and each has its own deep guide. "
        '<a href="/health/curled-gills-stress-signal/">Curled or tightly curled gills</a> – gill and '
        'tail posture. <a href="/health/why-axolotl-floating/">Floating or bloating</a> – buoyancy. '
        '<a href="/health/refusing-to-eat/">Not eating</a> – appetite loss. '
        "Always test your <a href=\"/tank-setup/water-parameters-cycling/\">water quality</a> first."
        "</div>"
    ),
    "diet/feeding-schedule-by-age": (
        '<div class="role-note"><strong>Planning a fast?</strong> If you are asking how long an '
        "axolotl can go without food (vacation or planned fasting), the "
        '<a href="/diet/fasting-and-vacation/">fasting and vacation guide</a> has the single '
        "duration reference. This page covers the normal lifecycle feeding schedule.</div>"
    ),
    "health/refusing-to-eat": (
        '<div class="role-note"><strong>Unexpected appetite loss, not a diagnosis.</strong> If you '
        "deliberately let your axolotl fast, see the "
        '<a href="/diet/fasting-and-vacation/">planned fasting guide</a>. If eating has stopped '
        "unexpectedly, use this page for observations and safe first checks. Severe, worsening, "
        "or persistent changes need an <a href=\"/health/finding-an-exotic-vet/\">exotics-experienced veterinarian</a>.</div>"
    ),
    "tank-setup/temperature": (
        '<div class="role-note"><strong>Managing heat.</strong> This is the husbandry guide for '
        "keeping the tank cool. If you are deciding which chiller to buy instead, the "
        '<a href="/tank-setup/aquarium-chillers/">chiller comparison</a> covers the purchase '
        "decision.</div>"
    ),
    "tank-setup/aquarium-chillers": (
        '<div class="role-note"><strong>This is a buying decision.</strong> For non-purchase ways '
        "to cool a tank, or to check whether you need a chiller at all, "
        '<a href="/tank-setup/temperature/">the temperature guide</a> covers husbandry first.</div>'
    ),
    "tank-setup/filtration-for-axolotls": (
        '<div class="role-note"><strong>Principles and options.</strong> Read this first to '
        "understand axolotl filtration biology and the filter families. For the single "
        "canister-versus-sponge decision, use the "
        '<a href="/tank-setup/canister-vs-sponge-filter/">dedicated comparison</a>.</div>'
    ),
    "tank-setup/canister-vs-sponge-filter": (
        '<div class="role-note"><strong>Exactly the decision you came for.</strong> For the full '
        "range of filter options and the biology behind flow, start with the "
        '<a href="/tank-setup/filtration-for-axolotls/">filtration overview</a>.</div>'
    ),
    "health/fungal-infections-saprolegnia": (
        '<div class="role-note"><strong>Which treatment fits your case?</strong> Mild, early '
        "fungus &rarr; <a href=\"/health/black-tea-bath/\">black tea bath</a>. Widespread or "
        "resistant case &rarr; <a href=\"/health/salt-bath/\">salt bath</a>. Confirm the severity "
        "here before treating.</div>"
    ),
    "health/black-tea-bath": (
        '<div class="role-note"><strong>A mild, first-line treatment.</strong> Use only for mild, '
        "early fungal infections after reading the "
        '<a href="/health/fungal-infections-saprolegnia/">fungus diagnosis guide</a>.</div>'
    ),
    "health/salt-bath": (
        '<div class="role-note"><strong>Reserved for severe cases.</strong> Salt baths are '
        "stressful &mdash; confirm the case is severe with the "
        '<a href="/health/fungal-infections-saprolegnia/">fungus diagnosis guide</a> before '
        "starting.</div>"
    ),
    "diet/overfeeding-and-impaction": (
        '<div class="role-note"><strong>Worried about impaction?</strong> The canonical diagnosis '
        "and treatment guide covers every cause and what to do: "
        '<a href="/health/impaction-symptoms-treatment/">impaction symptoms and treatment</a>.</div>'
    ),
    "tank-setup/substrate-and-impaction": (
        '<div class="role-note"><strong>Substrate is one common cause of impaction.</strong> '
        "For diagnosis and treatment of impaction itself, "
        '<a href="/health/impaction-symptoms-treatment/">start with the canonical guide</a>.</div>'
    ),
    "tank-setup/gravel-risks": (
        '<div class="role-note"><strong>Gravel is a leading impaction cause.</strong> If your '
        "axolotl may have swallowed gravel, see "
        '<a href="/health/impaction-symptoms-treatment/">impaction symptoms and treatment</a>.</div>'
    ),
    "care-basics/are-axolotls-good-beginner-pets": (
        '<div class="role-note"><strong>Thinking about the true cost?</strong> The complete '
        "numbers &mdash; setup, monthly, and first year &mdash; live on the cost owner: "
        '<a href="/care-basics/cost-of-ownership-monthly/">cost of owning an axolotl per month</a>.</div>'
    ),
    "care-basics/axolotls-and-children": (
        '<div class="role-note"><strong>Budget matters for families.</strong> See the full cost '
        "picture before deciding: "
        '<a href="/care-basics/cost-of-ownership-monthly/">monthly cost of an axolotl</a>.</div>'
    ),
    "axolotl-in-culture/axolotl-in-pop-culture-and-memes": (
        '<div class="role-note"><strong>This page maps where axolotls appear in culture.</strong> '
        'Use it for games, memes, media, merchandise, and science-news examples. For the causal question of why popularity surged, read '
        '<a href="/axolotl-in-culture/why-axolotls-are-suddenly-popular/">why axolotls became so popular</a>.</div>'
    ),
    "axolotl-in-culture/why-axolotls-are-suddenly-popular": (
        '<div class="role-note"><strong>This page owns the popularity question.</strong> '
        'It explains the forces behind the surge in attention. For a catalog of where axolotls show up in games, memes, media, and merch, use '
        '<a href="/axolotl-in-culture/axolotl-in-pop-culture-and-memes/">the pop-culture guide</a>.</div>'
    ),
    "biology-and-science/conservation-status": (
        '<div class="role-note"><strong>This page owns the wild-conservation question.</strong> '
        'It covers status, population decline, threats, and recovery work. For the physical ecology of the last wild habitat, use '
        '<a href="/biology-and-science/wild-habitat-xochimilco/">the Xochimilco habitat guide</a>; '
        'for captive care, use <a href="/axolotls/care-guide/">the axolotl care guide</a>.</div>'
    ),
    "biology-and-science/wild-habitat-xochimilco": (
        '<div class="role-note"><strong>This page owns the habitat question.</strong> '
        'It explains where wild axolotls live and the conditions of Xochimilco. For population status, threats, and conservation work, use '
        '<a href="/biology-and-science/conservation-status/">the conservation-status guide</a>; '
        'for translating those conditions into a home tank, use <a href="/tank-setup/setup-guide/">the tank-setup guide</a>.</div>'
    ),
    "biology-and-science/regeneration-and-limb-regrowth": (
        '<div class="role-note"><strong>The science lane.</strong> This page explains how limb '
        "regeneration works. Owners with an injured axolotl should use the practical guide: "
        '<a href="/health/limb-regeneration/">axolotl limb regeneration for owners</a>.</div>'
    ),
    "health/limb-regeneration": (
        '<div class="role-note"><strong>The owner lane.</strong> What to do when your axolotl '
        "loses part of a limb. For how regeneration works at the cellular level, read "
        '<a href="/biology-and-science/regeneration-and-limb-regrowth/">the regeneration science</a>.</div>'
    ),
    "morphs/morphs-comparison-chart": (
        '<div class="role-note"><strong>Use this page to identify and compare a morph.</strong> '
        'For why the colors differ, read <a href="/morphs/pigment-cells/">pigment-cell biology</a>; '
        'for inheritance, use <a href="/breeding/color-genetics-punnett-squares/">color genetics</a>; '
        'and for market ranges, see <a href="/cost-and-buying/axolotl-price-by-morph/">price by morph</a>.</div>'
    ),
    "breeding/genetics-and-inbreeding": (
        '<div class="role-note"><strong>This page decides whether a pair should be bred.</strong> '
        'For predicting offspring colors rather than pair suitability, use '
        '<a href="/breeding/color-genetics-punnett-squares/">the color-genetics guide</a>.</div>'
    ),
    "breeding/color-genetics-punnett-squares": (
        '<div class="role-note"><strong>This page predicts inherited color outcomes.</strong> '
        'Before planning a cross, use <a href="/breeding/genetics-and-inbreeding/">genetics and inbreeding risk</a> '
        'to decide whether the pair is suitable to breed at all.</div>'
    ),
    "breeding/egg-and-larvae-care": (
        '<div class="role-note"><strong>This page owns the egg-to-first-feeding stage.</strong> '
        'Once larvae are feeding and growing, continue with '
        '<a href="/breeding/raising-juveniles/">juvenile grow-out and rehoming</a>.</div>'
    ),
    "breeding/raising-juveniles": (
        '<div class="role-note"><strong>This page owns post-hatch grow-out.</strong> '
        'For incubation, hatching, and the first feeding window, start with '
        '<a href="/breeding/egg-and-larvae-care/">egg and early-larval care</a>.</div>'
    ),
    "health/emergency-first-aid": (
        '<div class="role-note"><strong>Urgency guide, not a diagnosis.</strong> Use the page for '
        "safe first checks and red-flag routing. If the axolotl needs a vet now, use the "
        '<a href="/health/finding-an-exotic-vet/">exotic-vet guide</a>. Do not start medication, '
        "baths, or intensive cooling from one observed sign.</div>"
    ),
    "health/finding-an-exotic-vet": (
        '<div class="role-note"><strong>This page owns the care-escalation step.</strong> It helps '
        "you find and screen an amphibian-experienced veterinarian. For deciding how urgent the "
        'current signs are, start with the <a href="/health/emergency-first-aid/">emergency guide</a>.</div>'
    ),
    "health/fridging-sick-axolotl": (
        '<div class="role-note"><strong>Veterinarian-directed supportive care only.</strong> '
        "A household refrigerator is not a general treatment for floating, constipation, fungus, "
        "or appetite loss. Use the <a href=\"/health/emergency-first-aid/\">emergency guide</a> "
        "for safe first checks and the <a href=\"/health/finding-an-exotic-vet/\">vet guide</a> "
        "before considering fridging.</div>"
    ),
}

# Extra sections appended to the body of existing articles (surgeon-level
# content layer; the .docx source is untouched). Format: heading text + HTML.
EXTRA_SECTIONS = {
    "biology-and-science/conservation-status": [
        ("What Can Pet Axolotl Owners Do?", """
<p>Pet keeping and wild conservation are separate jobs. The most useful owner actions are to keep captive axolotls out of natural waterways, buy only captive-bred animals from reputable sources, and support habitat work in Xochimilco rather than treating hobby breeding as a substitute for conserving the wild population.</p>
<ul>
<li><strong>Never release a pet axolotl.</strong> Captive animals do not belong in local waterways.</li>
<li><strong>Choose a responsible source.</strong> Use the <a href="/cost-and-buying/choosing-a-reputable-breeder/">reputable breeder guide</a> before buying.</li>
<li><strong>Keep the conservation target clear.</strong> The wild population depends on protecting and restoring <a href="/biology-and-science/wild-habitat-xochimilco/">Xochimilco habitat</a>, not on producing more pet morphs.</li>
</ul>"""),
    ],
    "breeding/raising-juveniles": [
        ("Live Food to Juvenile Diet: Transition Milestones", """
<p>The main transition is from movement-triggered live prey to foods a growing juvenile can recognize and swallow. Use size and feeding response rather than a fixed calendar:</p>
<div class="table-wrap"><table>
<thead><tr><th>Stage</th><th>Approx. size</th><th>Main food</th><th>Feeding pattern</th><th>Next step</th></tr></thead>
<tbody>
<tr><td>Yolk-sac stage</td><td>Newly hatched</td><td>No food until the yolk is absorbed</td><td>First 24&ndash;72 hours</td><td>Prepare live food before active feeding begins</td></tr>
<tr><td>Early larva</td><td>About 1&ndash;2 cm</td><td>Live baby brine shrimp, daphnia, or moina</td><td>Once or twice daily</td><td>Keep prey small and remove dead food promptly</td></tr>
<tr><td>Food transition</td><td>About 2.5&ndash;4 cm</td><td>Continue live food while introducing finely chopped bloodworm, small pellets, or tiny earthworm pieces</td><td>Twice daily while growing</td><td>Introduce one new food at a time and confirm it is being eaten</td></tr>
<tr><td>Juvenile grow-out</td><td>Above the early transition stage</td><td>Appropriately sized worms and pellets; <a href="/diet/blackworms-for-juveniles/">prepared blackworms</a> are another juvenile option</td><td>Follow body size and growth</td><td>Use the <a href="/diet/feeding-schedule-by-age/">feeding schedule by age and size</a> as the routine-feeding reference</td></tr>
</tbody></table></div>
<p>The goal is not to stop live food on a particular birthday. Keep enough familiar live prey in the rotation until each juvenile consistently accepts the replacement food.</p>"""),
    ],
    "morphs/leucistic": [
        ("How Rare Is a Leucistic Axolotl, and What Does One Cost?", """
<p>The leucistic is one of the two most common morphs in the pet trade, so it is neither rare nor expensive. Pets start around $25&ndash;$60, rising only for specific lines or high-quality dirty-lucy patterns. Compare every morph's pricing in the <a href="/cost-and-buying/axolotl-price-by-morph/">price-by-morph guide</a>, or see all morphs side by side in the <a href="/morphs/morphs-comparison-chart/">comparison chart</a>.</p>"""),
        ("Leucistic vs Golden Albino at a Glance", """
<p>Both morphs look pale pink to white, which is why they are confused. The easy difference is the eyes: leucistic axolotls keep dark eyes, while golden albino axolotls have red or pink eyes because they cannot make melanin at all. Leucistic animals also keep their natural pigment cells everywhere except the skin, which is limited to the gills and the occasional spot. Read the full breakdown on the <a href="/morphs/golden-albino/">golden albino</a> page.</p>"""),
    ],
    "morphs/wild-type": [
        ("Wild Type Variants and Color Intensity", """
<p>"Wild type" is a range, not a single shade. Wild-type axolotls carry all three pigment-cell types &mdash; melanophores, xanthophores, and iridophores &mdash; and the balance of those cells decides whether an individual reads dark black-brown, olive, or a brighter "high-yellow" animal. This is the same three-cell mechanism covered in the <a href="/morphs/pigment-cells/">pigment-cells guide</a>, and it means no two wild types are exactly the same colour.</p>"""),
        ("Rarity, Price, and Availability", """
<p>The wild type is the baseline and one of the cheapest morphs to buy, usually from around $25. Because they are the natural form, they are widely available from reputable breeders and pet stores. Prices sit on the <a href="/cost-and-buying/axolotl-price-by-morph/">price-by-morph page</a>; for buyer advice see <a href="/cost-and-buying/breeder-vs-pet-store/">breeder vs pet store</a>.</p>"""),
        ("The Wild Population Behind the Pet", """
<p>Wild-type is the colour of the wild axolotl &mdash; but the wild population is critically endangered and survives only in the canals of Xochimilco near Mexico City. Pet wild types are captive-bred, never taken from the wild. For the animal's true situation, see <a href="/biology-and-science/wild-habitat-xochimilco/">the Xochimilco habitat</a> and <a href="/biology-and-science/conservation-status/">conservation status</a>.</p>"""),
    ],
    "breeding/color-genetics-punnett-squares": [
        ("Limitations of Punnett Squares", """
<p>Punnett squares predict outcomes at a single locus, which makes them the right tool for the classic diallelic genes (leucistic, albino, melanoid, axanthic). They cannot predict how an animal will look when genetics play out unpredictably: <a href="/morphs/chimera/">chimeras</a> arise from fused embryos (two separate animals in one), <a href="/morphs/mosaic/">mosaics</a> from a mutation in one embryonic cell line, and GFP and copper intensity vary with polygenic modifiers rather than one gene. For those cases the biology is covered in <a href="/morphs/pigment-cells/">the pigment-cells guide</a>.</p>"""),
        ("Worked Example: Leucistic x Albino (Two-Gene Cross)", """
<p>Each gene resolves independently. For the white locus, a leucistic parent (d/d) bred to a wild-color carrier (D/d) gives <strong>50% leucistic</strong> and <strong>50% wild colour</strong> for that locus. The albino locus works the same way as a separate diallelic recessive. So a single pairing reads as two independent 50/50 flips: roughly a quarter of the clutch can end up showing the albino trait, a quarter leucistic, a quarter leucistic+albino (both recessives), and a quarter visibly wild type &mdash; before considering pigment intensity, which Punnett squares do not model.</p>"""),
    ],
    "biology-and-science/neoteny": [
        ("My Axolotl Is Metamorphosing &mdash; What Should I Do?", """
<p>Healthy axolotls stay neotenic their whole lives. When an axolotl begins to metamorphose &mdash; resorbing gills, developing eyelids, losing the fin &#8212; it is almost always because something forced the thyroid hormone system to kick in, most often induced metamorphosis (iodine exposure) rather than a natural event.</p>
<p><strong>Metamorphosis is generally not reversible</strong>, so the priority is keeping the animal comfortable through the change and getting veterinary help. A metamorphosed axolotl can no longer live fully aquatic the same way: it needs a setup with both land and deeper water areas, damp cover, and careful humidity, and it eats the same carnivorous diet on land. The animal may also show behaviour changes &mdash; see <a href="/biology-and-science/axolotl-vs-tiger-salamander/">axolotl vs tiger salamander</a> for what a metamorphosed salamander is closer to.</p>
<p>Do not try to "fix" it with unproven treatments. Get guidance from an <a href="/health/finding-an-exotic-vet/">exotic veterinarian</a> promptly, and keep water quality and temperature in the safe range while the animal transitions.</p>"""),
    ],
    "tank-setup/water-parameters-cycling": [
        ("How to Test Tank Water Correctly", """
<p>Liquid test kits beat test strips for accuracy: strips are convenient for a quick ammonia check but unreliable for borderline numbers. Test at least ammonia and nitrite, and ideally nitrate and pH, and always test the same time of day relative to feeding. During cycling test daily; in a stable cycled tank, test once a week and always after a water change, illness, or a new animal. Log every reading &mdash; the <a href="/tools/nitrogen-cycle-tracker/">nitrogen cycle tracker</a> is built for exactly this and will show you your trend line.</p>"""),
    ],
    "care-basics/cost-of-ownership-monthly": [
        ("First-Year Budget: The Real Year-One Cost", """
<p>The first year costs far more than the animal itself. A rough plan, using the numbers on <a href="/cost-and-buying/axolotl-price-by-morph/">price by morph</a> and the <a href="/tank-setup/setup-guide/">setup guide</a>:</p>
<ul>
<li><strong>Purchase:</strong> $25&ndash;$150+ depending on morph (pets from roughly $25; rare morphs climb much higher).</li>
<li><strong>Tank setup:</strong> a 40-gallon breeder-style tank, stand, filter, lid, lighting, hides, and substrate &mdash; the largest single line item.</li>
<li><strong>Water care gear:</strong> test kit, buckets, and conditioner for the year.</li>
<li><strong>Food:</strong> monthly cost of worms or pellets times twelve.</li>
<li><strong>Emergency reserve:</strong> keep enough for an <a href="/health/finding-an-exotic-vet/">exotic vet visit</a> &mdash; the one cost most first-time owners forget.</li>
</ul>
<p>Expect the first-year total to land well above the monthly figure you planned on &mdash; that is normal, and after year one the recurring cost is much smaller.</p>"""),
    ],
    "morphs/morphs-comparison-chart": [
        ("Core Morphs, Pigment Types and Traits Side by Side", """
<table>
<tr><th>Name</th><th>Typical appearance</th><th>What the name describes</th><th>Read more</th></tr>
<tr><td>Wild type</td><td>Dark brown / olive with mottling</td><td>Baseline pigment phenotype</td><td><a href="/morphs/wild-type/">Wild type</a></td></tr>
<tr><td>Leucistic / white</td><td>Pale pink-white with dark eyes</td><td>White-locus phenotype</td><td><a href="/morphs/leucistic/">Leucistic</a></td></tr>
<tr><td>Albino</td><td>Reduced/no melanin; eye and body color vary by pigment combination</td><td>Recessive albino mutation</td><td><a href="/morphs/golden-albino/">Albino combinations</a></td></tr>
<tr><td>Golden albino</td><td>Yellow-gold body with pink/red eyes</td><td>Albino combined with retained yellow pigment</td><td><a href="/morphs/golden-albino/">Golden albino</a></td></tr>
<tr><td>Melanoid</td><td>Dark body with reduced reflective shine</td><td>Melanoid pigment mutation</td><td><a href="/morphs/melanoid/">Melanoid</a></td></tr>
<tr><td>Axanthic</td><td>Reduced yellow/reflective pigment; often gray-toned</td><td>Axanthic pigment mutation</td><td><a href="/morphs/pigment-cells/">Pigment cells</a></td></tr>
<tr><td>Copper</td><td>Copper / tan / reddish-brown tones</td><td>Distinct pigment phenotype used in captive lines</td><td><a href="/morphs/copper/">Copper</a></td></tr>
<tr><td>GFP</td><td>Green fluorescence under suitable blue/UV light</td><td>Fluorescent transgenic trait that can occur with other morphs</td><td><a href="/morphs/gfp-axolotl/">GFP</a></td></tr>
<tr><td>Piebald</td><td>Irregular pale and pigmented patches</td><td>Pattern description</td><td><a href="/morphs/piebald/">Piebald</a></td></tr>
<tr><td>Mosaic</td><td>Patchwork pigment pattern</td><td>Developmental/pattern category, not a simple single-gene color</td><td><a href="/morphs/mosaic/">Mosaic</a></td></tr>
<tr><td>Chimera</td><td>Two genetically distinct cell populations in one animal</td><td>Developmental chimera, not a simple color morph</td><td><a href="/morphs/chimera/">Chimera</a></td></tr>
</table>
<p><strong>There is no single authoritative fixed count of “all axolotl morphs.”</strong> Lists differ because breeders mix core pigment mutations, combinations, patterns, and traits such as GFP under the same everyday word <em>morph</em>. Availability and perceived rarity also change by breeder, region, and time, so use the <a href="/cost-and-buying/axolotl-price-by-morph/">price-by-morph page</a> for market context rather than treating rarity as a permanent biological ranking.</p>"""),
    ],
    "health/impaction-symptoms-treatment": [
        ("Impaction vs Constipation: Know the Difference", """
<p>Impaction is a physical blockage of the digestive tract &mdash; most often by swallowed substrate &mdash; and constipation is slow or stalled passage of waste. Both show as a bloated belly and reduced appetite, but impaction is the emergency: a blocked axolotl stops passing waste entirely and can go downhill fast. If you suspect impaction, do not feed, do not heat, and see the treatment steps on this page &mdash; then ask a vet.</p>"""),
        ("Which Cause Is Behind the Blockage?", """
<p>Three causes cover most impactions, and each has its own deep-dive guide:</p>
<ul>
<li><strong>Overfeeding</strong> &mdash; too much food or too-large prey. <a href="/diet/overfeeding-and-impaction/">Overfeeding and impaction</a>.</li>
<li><strong>Substrate</strong> &mdash; coarse or loose substrate swallowed with food. <a href="/tank-setup/substrate-and-impaction/">Substrate guide</a>.</li>
<li><strong>Sharp gravel</strong> &mdash; the classic danger. <a href="/tank-setup/gravel-risks/">Gravel risks</a>.</li>
</ul>"""),
    ],
}


# P0 keyword-reconciliation additions (2026-09-18).
# These sharpen existing page ownership without creating duplicate URLs.
INTRO_OVERRIDES["breeding/raising-juveniles"] = (
    "Baby axolotl care changes quickly as larvae begin feeding and grow into juveniles. "
    "Use this page for post-hatch feeding, growth, size sorting, food transitions, and "
    "juvenile grow-out; egg incubation and the first hatch window stay in the egg-care guide."
)
INTRO_OVERRIDES["tank-setup/tank-size-by-age"] = (
    "There is no single research-backed gallon number that answers every axolotl tank-size "
    "question. Use body length, usable floor area, water volume, filtration, life stage, and "
    "the number of animals together; this page is the site's canonical tank-size reference."
)
INTRO_OVERRIDES["morphs/morphs-comparison-chart"] = (
    "Use this guide to identify and compare axolotl colors and morph terminology side by side. "
    "It owns the color/type/rarity comparison; pigment-cell biology, inheritance, and pricing "
    "remain on their specialist pages."
)
INTRO_OVERRIDES["morphs/blue-and-pink-axolotl-myth"] = (
    "Pink, blue, purple, lavender, green, and yellow are common search and seller labels, but "
    "they do not all map one-to-one to recognized axolotl pigment phenotypes. This guide separates "
    "standard morph terminology from lighting, fluorescence, editing, and informal color names."
)

ROLE_CALLOUTS["tank-setup/tank-size-by-age"] = (
    '<div class="role-note"><strong>This page owns tank-size requirements.</strong> '
    'Use it for age, body size, floor space, gallon capacity, and multiple-axolotl sizing. '
    'For the full build sequence, filtration, cooling, substrate, and cycling, use the '
    '<a href="/tank-setup/setup-guide/">tank setup guide</a>.</div>'
)
ROLE_CALLOUTS["breeding/raising-juveniles"] = (
    '<div class="role-note"><strong>This page owns baby and juvenile grow-out.</strong> '
    'For eggs, hatching, and the first feeding window, use '
    '<a href="/breeding/egg-and-larvae-care/">egg and larval care</a>; for routine feeding '
    'after grow-out, use the <a href="/diet/feeding-schedule-by-age/">feeding schedule</a>.</div>'
)
ROLE_CALLOUTS["morphs/blue-and-pink-axolotl-myth"] = (
    '<div class="role-note"><strong>This page explains informal color labels.</strong> '
    'For recognized morph identification and rarity, use the '
    '<a href="/morphs/morphs-comparison-chart/">morph comparison</a>; for the underlying '
    'biology, use <a href="/morphs/pigment-cells/">pigment cells</a>.</div>'
)

EXTRA_SECTIONS.setdefault("breeding/raising-juveniles", []).append((
    "When Is an Axolotl a Larva, Baby, or Juvenile?",
    """
<p><strong>Axolotl life-stage labels overlap in everyday use, so size and feeding stage are more useful than a rigid birthday.</strong> The Ambystoma Genetic Stock Center begins feeding newly hatched larvae after the yolk is absorbed, starts supplementing brine shrimp with small pellets at about 4 cm, and reports that young axolotls around 5 cm or longer are commonly separated because size differences and nipping become important.</p>
<p>For this site, <em>baby axolotl</em> is the broad search term, while <em>larva</em> describes the early post-hatch stage and <em>juvenile</em> describes the later grow-out stage before adulthood. Use feeding response, body size, and development rather than assuming every animal reaches a milestone on the same day.</p>
<p><strong>Source:</strong> <a href="https://ambystoma.uky.edu/education1/guide-to-axolotl-husbandry">Ambystoma Genetic Stock Center: Guide to Axolotl Husbandry</a>.</p>
"""
))

EXTRA_SECTIONS.setdefault("morphs/blue-and-pink-axolotl-myth", []).append((
    "What Do Pink, Purple, Lavender, Green and Yellow Axolotl Labels Mean?",
    """
<p><strong>Color words are not always genetic morph names.</strong> The Ambystoma Genetic Stock Center separately documents established pigment mutations and strains such as white/leucistic, albino, melanoid, and axanthic. Seller or social-media labels such as purple, lavender, green, or neon may instead describe how an animal looks under a particular light, a combination of recognized traits, GFP fluorescence, image processing, or informal marketing language.</p>
<div class="table-wrap"><table>
<thead><tr><th>Search label</th><th>Best interpretation</th><th>Where to continue</th></tr></thead>
<tbody>
<tr><td>Pink / white</td><td>Often leucistic; eye color and pigment pattern help distinguish leucistic from albino combinations.</td><td><a href="/morphs/leucistic/">Leucistic axolotl</a></td></tr>
<tr><td>Yellow / gold</td><td>Often used for golden-albino appearance or other yellow-pigment expression.</td><td><a href="/morphs/golden-albino/">Golden albino</a></td></tr>
<tr><td>Green / glowing</td><td>May refer to GFP fluorescence rather than a naturally green body pigment.</td><td><a href="/morphs/gfp-axolotl/">GFP axolotl</a></td></tr>
<tr><td>Blue / purple / lavender</td><td>Do not assume the color word is a standardized genetic morph name; verify the animal's actual phenotype, lineage, and lighting conditions.</td><td><a href="/morphs/morphs-comparison-chart/">Morph comparison</a></td></tr>
</tbody></table></div>
<p><strong>Sources:</strong> <a href="https://ambystoma.uky.edu/teachers-materials-menu/teachers-materials-books-menu?id=9">Ambystoma Genetic Stock Center: Mutant Genes</a>; <a href="https://ambystoma.uky.edu/axolotl-research2/12-educationresources/10-axolotl-strains">Ambystoma Genetic Stock Center: Axolotl Strains</a>.</p>
"""
))

EXTRA_SECTIONS.setdefault("morphs/morphs-comparison-chart", []).append((
    "Morph Names vs Color Descriptions",
    """
<p>A morph is more useful than a color nickname when it points to a repeatable pigment phenotype or genetic background. The Ambystoma Genetic Stock Center documents standard pigment mutations including albino, axanthic, melanoid, and white, while hobby names also describe combinations, patterns, and transgenic traits. That is why two animals that both look “pink” can belong to different pigment categories, and why a label such as “lavender” should not automatically be treated as a separate genetic morph.</p>
<p>Use the comparison table to identify visible traits first, then continue to <a href="/morphs/pigment-cells/">pigment-cell biology</a> and <a href="/breeding/color-genetics-punnett-squares/">color genetics</a> when you need the mechanism rather than the appearance.</p>
<p><strong>Sources:</strong> <a href="https://ambystoma.uky.edu/teachers-materials-menu/teachers-materials-books-menu?id=9">Ambystoma Genetic Stock Center: Mutant Genes</a>; <a href="https://ambystoma.uky.edu/axolotl-research2/12-educationresources/10-axolotl-strains">Ambystoma Genetic Stock Center: Axolotl Strains</a>.</p>
"""
))



# Second P0 reconciliation pass (2026-09-18): entity, habitat, conservation,
# growth, suitability, handling, and owner-facing limb recovery.
INTRO_OVERRIDES["care-basics/are-axolotls-good-beginner-pets"] = (
    "Axolotls can suit an owner who wants an observation-focused aquatic pet and is willing "
    "to manage cool, clean water consistently. This page owns the decision question: benefits, "
    "drawbacks, beginner difficulty, time, equipment, handling limits, and who should reconsider."
)
INTRO_OVERRIDES["care-basics/axolotl-age-and-size-chart"] = (
    "Use this page for the animal's body size and growth: how big axolotls get, how size changes "
    "through development, and why individuals grow at different rates. Tank capacity belongs to "
    "the separate tank-size guide."
)
INTRO_OVERRIDES["care-basics/axolotl-facts"] = (
    "An axolotl is Ambystoma mexicanum, a permanently aquatic Mexican salamander best known for "
    "retaining larval traits such as external gills into adulthood. This page is the broad entity "
    "definition and routes detailed care, habitat, classification, morph, and conservation questions "
    "to their specialist guides."
)
INTRO_OVERRIDES["care-basics/handling"] = (
    "Axolotls are observation-focused aquatic pets, so routine touching and petting are not the goal. "
    "Use this guide for the limited situations when handling, netting, or transport is necessary and "
    "for safer ways to move an axolotl while minimizing skin and slime-coat disturbance."
)
INTRO_OVERRIDES["biology-and-science/wild-habitat-xochimilco"] = (
    "Wild Ambystoma mexicanum is native to the freshwater lake-and-canal system of Xochimilco in "
    "the Valley of Mexico. This page owns where axolotls live, where they come from, their freshwater "
    "habitat, ecological adaptations, and habitat threats."
)
INTRO_OVERRIDES["biology-and-science/conservation-status"] = (
    "Wild axolotls remain in a critical conservation situation in Xochimilco. The most recent published "
    "density benchmark is still the 2014 estimate of about 36 animals per square kilometre; UNAM reported "
    "in June 2026 that results from the newer census were still being processed."
)
INTRO_OVERRIDES["health/limb-regeneration"] = (
    "This is the owner-facing injury page: what to do after an axolotl loses part of a limb, how to protect "
    "the animal during healing, and when veterinary assessment is warranted. The cellular science of "
    "regeneration stays on the biology page."
)

ROLE_CALLOUTS["care-basics/axolotl-facts"] = (
    '<div class="role-note"><strong>This page answers “what is an axolotl?”</strong> '
    'For husbandry, use the <a href="/axolotls/care-guide/">care guide</a>; for fish-vs-amphibian '
    'classification, use <a href="/biology-and-science/is-axolotl-amphibian/">the classification guide</a>; '
    'for where they live, use <a href="/biology-and-science/wild-habitat-xochimilco/">wild habitat</a>.</div>'
)
ROLE_CALLOUTS["care-basics/axolotl-age-and-size-chart"] = (
    '<div class="role-note"><strong>This page owns animal size and growth.</strong> '
    'If you are choosing aquarium capacity, continue to '
    '<a href="/tank-setup/tank-size-by-age/">the axolotl tank-size guide</a>.</div>'
)
ROLE_CALLOUTS["care-basics/handling"] = (
    '<div class="role-note"><strong>This page owns touching, petting, moving, netting, and transport.</strong> '
    'For poison/venom/bite safety, use the dedicated human-safety guide when published; '
    'for normal interaction and recognition, use <a href="/care-basics/axolotl-intelligence-and-bonding/">bonding and intelligence</a>.</div>'
)

EXTRA_SECTIONS.setdefault("biology-and-science/conservation-status", []).append((
    "How Many Wild Axolotls Are Left in 2026?",
    """
<p><strong>There is not yet a published 2026 wild headcount that should replace the older benchmark.</strong> UNAM reported in June 2026 that the latest census results were still being processed. The university continues to cite the dramatic decline from roughly 6,000 axolotls per square kilometre in 1998 to about 36 per square kilometre in the 2014 census.</p>
<p>That number is a <em>density estimate</em>, not a statement that only 36 individual axolotls exist in the world or even in all of Xochimilco. Captive axolotls are numerous, while conservation status refers to the wild population and its habitat.</p>
<p>The new UNAM census uses traditional fishing surveys together with environmental-DNA methods. Until its results are formally released, this page keeps the 2014 density as the latest published benchmark and labels it by date rather than presenting it as a current 2026 count.</p>
<p><strong>Current sources:</strong> <a href="https://www.dgcs.unam.mx/boletin/bdboletin/2026_387.html">UNAM, June 28, 2026: new census results still being processed</a>; <a href="https://www.gaceta.unam.mx/levantan-nuevo-censo-del-axolote-en-xochimilco/">Gaceta UNAM: new Xochimilco census</a>; <a href="https://www.ib.unam.mx/ib/adopta-axolotl/">Instituto de Biología UNAM: Adoptaxolotl 2026</a>.</p>
"""
))


# Build-level (HTML-authored) new pages. These exist nowhere in SOURCE_DIR and
# are inserted as full articles during the build. HARD-STOP-exempt: each fills
# a genuine entity/attribute/intent cell (procedural + decision), not a keyword.
CONFIG_ARTICLES = {
    "tank-setup/water-change-guide": {
        "slug": "tank-setup/water-change-guide",
        "hub": "tank-setup",
        "title": "How to Do an Axolotl Water Change Step by Step",
        "title_tag": "Axolotl Water Change: Step-by-Step Guide",
        "meta": "Learn how to change axolotl tank water step by step, including testing, dechlorination, temperature matching, safe siphoning and common mistakes.",
        "intro": "A complete step-by-step guide to changing your axolotl's tank water - how often, how much to remove, and how to treat and match replacement water without stressing the animal.",
        "num": 210,
        "headings": [
            "How Often Should You Change the Water?",
            "What You Need Before You Start",
            "Step 1: Test the Tank Water",
            "Step 2: Prepare and Dechlorinate Replacement Water",
            "Step 3: Match the Temperature",
            "Step 4: Remove Water from the Tank",
            "Step 5: Add Fresh Water Slowly",
            "Step 6: Test Again and Log the Readings",
            "Common Mistakes to Avoid",
            "When a Water Change Is Not the Answer",
        ],
        "body": """
<p>Regular water changes are the most important routine maintenance task in an axolotl tank. Waste breaks down into ammonia and nitrates that even a cycled filter cannot fully remove, and a consistent change schedule keeps toxins low and gills healthy.</p>
<h2>How Often Should You Change the Water?</h2>
<p>The change schedule has four cases.</p>
<ul>
<li><strong>Cycling tank:</strong> daily or every other day for the first 4&ndash;6 weeks, until the cycle finishes.</li>
<li><strong>Adults in a cycled tank:</strong> a 20&ndash;25% change once a week.</li>
<li><strong>Juveniles:</strong> two to three times a week &mdash; they eat more relative to their size and add more waste.</li>
<li><strong>After a spike:</strong> ammonia or nitrite spikes call for a larger or repeated change; see <a href="/tank-setup/water-parameters-cycling/">managing ammonia and nitrate spikes</a>.</li>
</ul>
<h2>What You Need Before You Start</h2>
<p>You need four things ready before touching the tank: a siphon or bucket, water conditioner, thermometer, and an ammonia test kit. Prepare them all first so the axolotl is disturbed for the shortest possible time.</p>
<ul>
<li>A bucket or siphon reserved for axolotl use only (washed with water, never detergent).</li>
<li>Water conditioner &mdash; <a href="/tank-setup/water-conditioners/">the water-conditioner guide</a>.</li>
<li>A thermometer to match temperature.</li>
<li>A test kit for ammonia, nitrite, and nitrate.</li>
</ul>
<h2>Step 1: Test the Tank Water</h2>
<p>Test ammonia, nitrite, pH, and temperature before changing anything. The test tells you how big a change is actually needed and gives a before-reading to compare after.</p>
<h2>Step 2: Prepare and Dechlorinate Replacement Water</h2>
<p>Fill your bucket with fresh tap water and treat it with water conditioner at the label dose. The conditioner removes chlorine and chloramine instantly; untreated tap water damages gills and slime coat.</p>
<h2>Step 3: Match the Temperature</h2>
<p>Bring the replacement water to the same temperature as the tank (60&ndash;68&deg;F / 15&ndash;20&deg;C). A swing of more than 2&ndash;3&deg;F (1&ndash;2&deg;C) stresses the axolotl and can trigger floating or illness; see <a href="/tank-setup/temperature/">keeping the tank cool</a>.</p>
<h2>Step 4: Remove Water from the Tank</h2>
<p>Use a siphon or a clean cup, drawing water from the top of the tank while keeping the siphon above the substrate so you neither vacuum up the axolotl nor rearrange clean sand. Never drop the water level below about half the tank in one go.</p>
<h2>Step 5: Add Fresh Water Slowly</h2>
<p>Pour the replacement water against the glass or a baffle, never directly onto the axolotl. Slow addition keeps temperature and chemistry even and avoids frightening the animal.</p>
<h2>Step 6: Test Again and Log the Readings</h2>
<p>Retest ammonia and nitrite about an hour later. In a cycled tank the numbers stay unchanged or lower; the <a href="/tools/nitrogen-cycle-tracker/">nitrogen cycle tracker</a> logs trends between changes.</p>
<h2>Common Mistakes to Avoid</h2>
<p>Four mistakes cause most water-change harm.</p>
<ul>
<li><strong>Skipping the conditioner</strong> &mdash; tap-water chlorine is a common cause of gill damage.</li>
<li><strong>Changing the whole tank at once</strong> &mdash; massive changes destabilize chemistry.</li>
<li><strong>Ignoring the smell</strong> &mdash; an ammonia-smelling tank needs testing and more frequent changes; see <a href="/tank-setup/why-tank-water-smells/">why the tank water stinks</a>.</li>
<li><strong>Leaving uneaten food</strong> &mdash; rotting food becomes this week's ammonia spike; <a href="/tank-setup/uneaten-food-and-ammonia/">manage uneaten food</a>.</li>
</ul>
<h2>When a Water Change Is Not the Answer</h2>
<p>A water change is still the first step for every axolotl, and almost always enough. When the animal looks actively stressed &mdash; floating uncontrollably, refusing food, reddened skin, or severe gill damage &mdash; the <a href="/health/emergency-first-aid/">emergency first-aid guide</a> decides whether it needs immediate care.</p>
""",
    },
    "health/emergency-first-aid": {
        "slug": "health/emergency-first-aid",
        "hub": "health",
        "title": "Axolotl Emergency Guide: First Aid & Triage",
        "title_tag": "Axolotl Emergency & First Aid: Triage, Urgent Signs, What to Do",
        "meta": "The emergency triage guide for axolotls: which signs are urgent, what to do first, what NOT to do, and when to see a vet now.",
        "intro": "The triage guide for axolotl emergencies: how to tell urgent from not-urgent, what to do in the first minutes, what NOT to do, and when to call an exotic vet immediately.",
        "num": 211,
        "date_modified": "2026-08-29",
        "headings": [
            "Is It an Emergency? Use This Severity Ladder",
            "First Steps for Any Stressed or Sick Axolotl",
            "Red Flags That Need a Vet Now",
            "What NOT to Do in an Emergency",
            "Emergency Care by Sickness",
            "Aftercare and Prevention",
        ],
        "body": """
<p>Some axolotl problems require a vet immediately; most do not. This guide ranks how urgent each situation is, gives the first steps to take, and marks the line where you must get help. For a vet near you, start with the <a href="/health/finding-an-exotic-vet/">exotic vet guide</a>.</p>
<h2>Is It an Emergency? Use This Severity Ladder</h2>
<p>The severity ladder has three tiers.</p>
<ul>
<li><strong>Urgent (act now):</strong> heavy labored breathing at the surface, visible bleeding or a torn wound, a belly that is hard and bloated, uncontrollable floating, reddening or peeling skin, or a total refusal to eat with these signs. Do a quick water test and get help.</li>
<li><strong>Watch closely (same day):</strong> curled gills, constant hiding, clamped or receding gills, floating that comes and goes, or reduced appetite &mdash; test water and temperature, record the signs, and escalate if they persist or worsen.</li>
<li><strong>Monitor:</strong> a brief change in activity without other warning signs &mdash; verify husbandry, reduce disturbance, and keep records rather than assuming a diagnosis.</li>
</ul>
<h2>First Steps for Any Stressed or Sick Axolotl</h2>
<p>Four first steps apply to any sick or stressed axolotl.</p>
<ol>
<li>Test ammonia, nitrite, nitrate, and pH, and record the measured water temperature. Water and temperature problems are important possibilities, but they are not the only causes; see the <a href="/tank-setup/water-parameters-cycling/">water-quality guide</a>.</li>
<li>If a measured value is unsafe, follow the <a href="/tank-setup/water-change-guide/">water-change guide</a> and <a href="/tank-setup/temperature/">temperature guide</a> without creating a sudden temperature or chemistry swing.</li>
<li>Do not force-feed or start medication while the cause is unclear. Record the last meal, stool, behavior, and any recent tank changes for the veterinarian.</li>
<li>Avoid unnecessary handling. If the water is unsafe or a tank mate poses an immediate risk, move the axolotl gently to a prepared, temperature-matched tub.</li>
</ol>
<h2>Red Flags That Need a Vet Now</h2>
<p>Six signs call for a vet now.</p>
<ul>
<li>Heavy gasping at the surface combined with limp gills.</li>
<li>Blood, an open wound, or skin sloughing.</li>
<li>Extreme bloating with a rigid body.</li>
<li>A hard or rapidly enlarging swollen belly, which can have several causes &mdash; see the <a href="/health/impaction-symptoms-treatment/">impaction observation guide</a>.</li>
<li>Reddening skin that spreads quickly &mdash; <a href="/health/red-leg-syndrome/">red leg syndrome</a>.</li>
<li>Sudden appetite loss with bloating, abnormal floating, marked lethargy, injury, or rapid weight loss &mdash; <a href="/health/refusing-to-eat/">refusing to eat</a>.</li>
</ul>
<p>Find and call an <a href="/health/finding-an-exotic-vet/">exotic veterinarian</a> &mdash; call ahead so they are ready for you.</p>
<h2>What NOT to Do in an Emergency</h2>
<ul>
<li>Do not shock the animal with a huge or ultra-cold water change.</li>
<li>Do not dose "human" or unidentified medications.</li>
<li>Do not start a tea bath or salt bath from one observed sign. Use the <a href="/health/fungal-infections-saprolegnia/">fungus observation guide</a> and seek veterinary guidance for spreading growth, skin damage, or deterioration.</li>
<li>Do not move the axolotl to completely different water without acclimation &mdash; see <a href="/tank-setup/acclimating-a-new-axolotl/">acclimating a new axolotl</a>.</li>
<li>Do not raise temperature to "speed up" recovery &mdash; axolotls need cool water.</li>
</ul>
<h2>Emergency Care by Sickness</h2>
<p>Once the water is stable, use the guide that matches the sign you can observe. These pages explain possibilities and escalation points; they do not confirm a diagnosis:</p>
<ul>
<li><strong>Ammonia burns or curled gills:</strong> <a href="/health/ammonia-burns/">ammonia burns</a> and <a href="/health/curled-gills-stress-signal/">curled gills</a>.</li>
<li><strong>Severe fungus:</strong> <a href="/health/fungal-infections-saprolegnia/">fungal infections</a>.</li>
<li><strong>Floating:</strong> <a href="/health/why-axolotl-floating/">why is my axolotl floating</a>.</li>
<li><strong>Not eating:</strong> <a href="/health/refusing-to-eat/">refusing to eat</a>.</li>
<li><strong>Bleeding or injury:</strong> <a href="/health/minor-scrapes-and-wounds/">minor scrapes and wounds</a>.</li>
</ul>
<h2>Aftercare and Prevention</h2>
<p>Once stable, reduce disturbance and continue monitoring. Use a <a href="/health/quarantine-tub/">quarantine tub</a> when isolation is needed and it can be maintained with temperature-matched, dechlorinated water. Stable cool temperature, gentle filtration, and consistent water care reduce many husbandry-related health risks, but persistent or worsening signs still need veterinary assessment.</p>
""",
    },
}


# ---------------------------------------------------------------------------
# Keyword-reconciliation new pages — batch 1 (2026-09-18)
# ---------------------------------------------------------------------------
# These pages fill distinct entity / process / procedural intents. Temporary
# non-placeholder heroes reuse closely related MyAxolotl original graphics;
# each can later receive a unique hero without changing its URL or semantic role.

CONFIG_ARTICLES.update({
    "biology-and-science/metamorphosis": {
        "slug": "biology-and-science/metamorphosis",
        "hub": "biology-and-science",
        "title": "Do Axolotls Turn Into Salamanders? Metamorphosis Explained",
        "title_tag": "Do Axolotls Turn Into Salamanders? Metamorphosis Explained",
        "meta": "Learn why axolotls normally remain aquatic, what changes during rare metamorphosis and what owners should do if those changes appear.",
        "intro": "Axolotls are salamanders already, but unlike most salamanders they normally reach adulthood without transforming into a terrestrial form. This page explains paedomorphosis, the rare metamorphic pathway, the body changes involved, and why owners should never try to trigger metamorphosis at home.",
        "num": 212,
        "date_published": "2026-09-18",
        "date_modified": "2026-09-18",
        "headings": [
            "Do axolotls turn into salamanders?",
            "Why do axolotls normally stay aquatic?",
            "What changes when an axolotl metamorphoses?",
            "Can an axolotl metamorphose naturally?",
            "What role do thyroid hormones play?",
            "Can iodine make an axolotl metamorphose?",
            "Can metamorphosis be reversed?",
            "What should you do if a pet axolotl starts metamorphosing?",
            "Metamorphosis vs neoteny",
            "Sources",
        ],
        "body": r'''
<p><strong>Axolotls are salamanders from the beginning; the unusual part is that they normally become sexually mature while keeping an aquatic, larval-looking body.</strong> This lifelong retention of juvenile traits is called paedomorphosis or neoteny. A typical axolotl therefore keeps its external gills, finned tail and aquatic lifestyle instead of completing the more familiar salamander transition to a land-adapted form.</p>

<h2>Do axolotls turn into salamanders?</h2>
<p><strong>They do not need to “turn into” salamanders because <em>Ambystoma mexicanum</em> is already a salamander species.</strong> What people usually mean is: can an axolotl undergo metamorphosis and lose its larval aquatic features? The answer is yes under some circumstances, but that is not the normal developmental route for healthy captive axolotls.</p>
<p>The standard axolotl life history is paedomorphic. Adults reproduce while retaining external gills and other juvenile traits, which is why an adult axolotl still looks unlike a terrestrial tiger salamander.</p>

<h2>Why do axolotls normally stay aquatic?</h2>
<p>Research on the axolotl endocrine system shows that its paedomorphosis is associated with low activity of the hypothalamic-pituitary-thyroid pathway that drives metamorphosis in many other amphibians. The tissues can respond to thyroid-hormone signaling, but the normal hormonal cascade does not produce the same metamorphic transition seen in related salamanders.</p>
<p>This is an evolved life-history strategy, not a sign that an adult axolotl is an unfinished or unhealthy animal.</p>

<h2>What changes when an axolotl metamorphoses?</h2>
<p>A metamorphosing axolotl progressively shifts toward a more terrestrial salamander body plan. Changes can include:</p>
<ul>
<li>reduction or resorption of the external gills;</li>
<li>reduction of the tail fin;</li>
<li>changes in skin and body shape;</li>
<li>development of eyelids;</li>
<li>changes in head shape and feeding mechanics; and</li>
<li>a change from a fully aquatic lifestyle toward a form that can use terrestrial habitat.</li>
</ul>
<p>These changes happen as an integrated developmental program. They should not be confused with sick or shrinking gills caused by poor water quality, injury, infection, or stress.</p>

<h2>Can an axolotl metamorphose naturally?</h2>
<p><strong>Rare spontaneous metamorphosis has been reported, but it is not the expected pathway for ordinary pet axolotls.</strong> Laboratory research also shows that the ancestral metamorphic pathway can be activated experimentally because axolotl tissues remain responsive to thyroid-hormone signaling.</p>
<p>For an owner, the important point is that a sudden change in gills, skin, body shape, or behavior should be evaluated as a health and husbandry problem first rather than assumed to be “natural metamorphosis.”</p>

<h2>What role do thyroid hormones play?</h2>
<p>Thyroid hormones are central regulators of amphibian metamorphosis. Reviews of axolotl endocrinology describe a functional downstream thyroid-hormone response but reduced upstream stimulation of the pathway compared with metamorphosing relatives. This helps explain why axolotls normally remain paedomorphic even though the body can still respond to experimentally supplied thyroid hormone.</p>

<h2>Can iodine make an axolotl metamorphose?</h2>
<p><strong>Do not use iodine, thyroid hormone, supplements, foods, chemicals, or temperature manipulation to try to induce metamorphosis in a pet axolotl.</strong> Experimental induction belongs in controlled research settings with defined protocols and animal-care oversight. A search result or anecdote is not a safe husbandry procedure.</p>
<p>If you are concerned about iodine exposure or a product used in the aquarium, remove the suspected source only if that can be done safely, keep water conditions stable, and discuss the exposure with an amphibian-experienced veterinarian.</p>

<h2>Can metamorphosis be reversed?</h2>
<p>Once the coordinated metamorphic program is well underway, owners should not assume that returning the animal to ordinary aquarium conditions will reverse it. The practical response is veterinary assessment and preparation for the changing respiratory, skin and habitat needs of the individual rather than trying unproven “reversal” treatments.</p>

<h2>What should you do if a pet axolotl starts metamorphosing?</h2>
<ol>
<li><strong>Document the changes.</strong> Take dated photos and note changes in gills, tail fin, eyes, skin, appetite and activity.</li>
<li><strong>Test the environment.</strong> Record temperature and water-quality readings so ordinary husbandry problems are not mistaken for metamorphosis.</li>
<li><strong>Do not add hormones, iodine or home remedies.</strong></li>
<li><strong>Contact an amphibian-experienced veterinarian.</strong> A veterinarian can help distinguish true metamorphic change from disease, injury or environmental stress and advise on housing if the body plan is changing.</li>
</ol>
<p>Use the <a href="/health/finding-an-exotic-vet/">axolotl vet guide</a> if you need help finding an appropriate clinician.</p>

<h2>Metamorphosis vs neoteny</h2>
<div class="table-wrap"><table>
<thead><tr><th>Feature</th><th>Typical axolotl / neoteny</th><th>Metamorphosed form</th></tr></thead>
<tbody>
<tr><td>External gills</td><td>Retained into adulthood</td><td>Reduced or lost</td></tr>
<tr><td>Tail fin</td><td>Broad aquatic fin retained</td><td>Reduced as body plan changes</td></tr>
<tr><td>Eyelids</td><td>Absent in the typical paedomorphic form</td><td>Develop during metamorphic change</td></tr>
<tr><td>Habitat</td><td>Fully aquatic</td><td>More terrestrial / semi-terrestrial requirements</td></tr>
<tr><td>Normal for pet axolotls?</td><td>Yes</td><td>No; uncommon and warrants assessment</td></tr>
</tbody></table></div>
<p>For the evolutionary/developmental concept itself, continue to <a href="/biology-and-science/neoteny/">what neoteny means in axolotls</a>.</p>

<h2>Sources</h2>
<ul>
<li><a href="https://pubmed.ncbi.nlm.nih.gov/29777689/">Crowner et al. (2019): endocrinology of paedomorphosis in the Mexican axolotl</a></li>
<li><a href="https://pmc.ncbi.nlm.nih.gov/articles/PMC6473073/">Voss et al. (2019): thyroid-hormone-dependent development and axolotl paedomorphosis</a></li>
<li><a href="https://ambystoma.uky.edu/genetic-stock-center/documents/AGSC%20_Guide_2024.pdf">Ambystoma Genetic Stock Center: Axolotl Guide 2024</a></li>
</ul>
''',
        "featured": False,
    },

    "biology-and-science/axolotl-life-cycle": {
        "slug": "biology-and-science/axolotl-life-cycle",
        "hub": "biology-and-science",
        "title": "Axolotl Life Cycle: Egg, Larva, Juvenile & Adult Stages",
        "title_tag": "Axolotl Life Cycle: Egg, Larva, Juvenile & Adult Stages",
        "meta": "Follow the axolotl life cycle from egg and embryo through hatchling, larva, juvenile and aquatic adult, including how neoteny shapes development.",
        "intro": "The axolotl life cycle runs from fertilized egg to embryo, hatchling, feeding larva, juvenile and sexually mature adult. Unlike most salamanders, the normal adult remains aquatic and keeps larval traits such as external gills.",
        "num": 213,
        "date_published": "2026-09-18",
        "date_modified": "2026-09-18",
        "headings": [
            "What are the stages of the axolotl life cycle?",
            "Stage 1: fertilized egg and embryo",
            "Stage 2: hatching",
            "Stage 3: feeding larva",
            "Stage 4: juvenile growth",
            "Stage 5: sexually mature adult",
            "Why doesn't the normal life cycle end in a land salamander?",
            "How long does the axolotl life cycle take?",
            "Life cycle vs care stages",
            "Sources",
        ],
        "body": r'''
<p><strong>The normal axolotl life cycle is egg → embryo → hatchling → feeding larva → juvenile → sexually mature aquatic adult.</strong> Development does not stop when an axolotl keeps its gills. The species continues to grow, develop limbs, mature its organs and become reproductively mature while retaining several juvenile-looking aquatic traits.</p>

<h2>What are the stages of the axolotl life cycle?</h2>
<div class="table-wrap"><table>
<thead><tr><th>Stage</th><th>What is happening</th><th>Best site guide</th></tr></thead>
<tbody>
<tr><td>Egg / embryo</td><td>Cleavage, gastrulation, neurulation, organ formation and pre-hatch development</td><td><a href="/breeding/egg-and-larvae-care/">Egg & larval care</a></td></tr>
<tr><td>Hatchling</td><td>Newly hatched animal uses remaining yolk before active feeding</td><td><a href="/breeding/egg-and-larvae-care/">Egg & larval care</a></td></tr>
<tr><td>Feeding larva</td><td>Begins active feeding; limbs continue developing</td><td><a href="/breeding/raising-juveniles/">Baby axolotl care</a></td></tr>
<tr><td>Juvenile</td><td>Rapid growth, food transitions and increasing need for individual space</td><td><a href="/breeding/raising-juveniles/">Baby axolotl care</a></td></tr>
<tr><td>Adult</td><td>Sexual maturity while retaining the aquatic body plan</td><td><a href="/care-basics/axolotl-age-and-size-chart/">Age & size chart</a></td></tr>
</tbody></table></div>

<h2>Stage 1: fertilized egg and embryo</h2>
<p>Axolotl development begins with a fertilized egg surrounded by protective jelly layers. Classic staging systems divide embryonic development into cleavage, blastula, gastrula, neurula, tailbud and pre-hatch stages. The Ambystoma Genetic Stock Center's staging resources extend from the one-cell egg through stage 44, just after hatching.</p>
<p>Temperature affects developmental speed, so an embryo should be described by its morphological stage rather than assuming that every clutch reaches a landmark on exactly the same day.</p>

<h2>Stage 2: hatching</h2>
<p>At hatching, the animal is still using stored yolk. The AGSC husbandry guide describes transferring newly hatched larvae into clean rearing water and waiting for the onset of feeding behavior before offering newly hatched brine shrimp. This separates the hatch event from the true beginning of active feeding.</p>

<h2>Stage 3: feeding larva</h2>
<p>After yolk reserves are used, the larva becomes an active predator. During this stage the external gills are prominent, the body elongates and the limbs continue developing. Limb-development staging extends beyond hatching because forelimbs and hindlimbs appear and differentiate over time rather than being complete at the moment the animal leaves the egg.</p>
<p>Larvae also vary in growth rate. Size sorting matters because larger larvae can injure or attempt to eat smaller ones.</p>

<h2>Stage 4: juvenile growth</h2>
<p>The juvenile period is a practical husbandry stage rather than one single universally fixed age. The AGSC increases individual container size as animals grow and changes foods as body size permits. Research staging papers likewise show that post-hatch development and maturation stretch across months.</p>
<p>For owners, use the animal's length, feeding ability, body condition and development rather than a rigid “juvenile starts on day X” rule.</p>

<h2>Stage 5: sexually mature adult</h2>
<p>An adult axolotl reaches reproductive maturity without undergoing the normal terrestrial metamorphosis seen in many related salamanders. A recent developmental review notes that sexual maturity is generally around a year or older, while the time from hatchling to mature adult can vary substantially with density, temperature, nutrition and individual growth.</p>
<p>Recent gonadal research also shows that reproductive tissues mature progressively over the later larval/juvenile period rather than switching on at one exact age.</p>

<h2>Why doesn't the normal life cycle end in a land salamander?</h2>
<p><strong>Because paedomorphosis is the normal developmental strategy of <em>Ambystoma mexicanum</em>.</strong> Adults retain external gills, a finned tail and an aquatic lifestyle while becoming reproductively mature. That is why the axolotl life cycle should not be illustrated as “egg → tadpole → ordinary land salamander” unless the figure is specifically explaining experimentally induced or unusual metamorphosis.</p>
<p>Read <a href="/biology-and-science/metamorphosis/">axolotl metamorphosis</a> for the exceptional pathway and <a href="/biology-and-science/neoteny/">neoteny</a> for the underlying developmental concept.</p>

<h2>How long does the axolotl life cycle take?</h2>
<p>There is no single clock for every animal. Early embryonic stages are strongly temperature-dependent, while later growth and sexual maturation depend on husbandry, density, genetics, nutrition and sex. A modern staging review follows development from fertilization to immature adult and reports that sexually mature adulthood may take roughly a year or longer, with some animals taking substantially longer under different rearing conditions.</p>

<h2>Life cycle vs care stages</h2>
<p>This page owns the biological sequence. For day-to-day husbandry:</p>
<ul>
<li><strong>Eggs and hatchlings:</strong> <a href="/breeding/egg-and-larvae-care/">egg and larval care</a></li>
<li><strong>Baby and juvenile grow-out:</strong> <a href="/breeding/raising-juveniles/">baby axolotl care</a></li>
<li><strong>Body length and growth:</strong> <a href="/care-basics/axolotl-age-and-size-chart/">age and size chart</a></li>
<li><strong>Feeding frequency:</strong> <a href="/diet/feeding-schedule-by-age/">feeding schedule by age and size</a></li>
</ul>

<h2>Sources</h2>
<ul>
<li><a href="https://ambystoma.uky.edu/education1/embryo-staging-series">Ambystoma Genetic Stock Center: Embryo Staging Series</a></li>
<li><a href="https://pmc.ncbi.nlm.nih.gov/articles/PMC9536427/">Khattak et al. (2022): updated axolotl staging from one-cell embryo to immature adult</a></li>
<li><a href="https://ambystoma.uky.edu/genetic-stock-center/documents/AGSC%20_Guide_2024.pdf">Ambystoma Genetic Stock Center: Axolotl Guide 2024</a></li>
<li><a href="https://ambystoma.uky.edu/genetic-stock-center/documents/Nye%20et%20al%202002.pdf">Nye et al.: extension of normal staging through limb development</a></li>
</ul>
''',
        "featured": False,
    },

    "morphs/albino": {
        "slug": "morphs/albino",
        "hub": "morphs",
        "title": "Albino Axolotl: Color, Genetics, Types & Identification",
        "title_tag": "Albino Axolotl: Color, Genetics, Types & Identification",
        "meta": "Learn how albino axolotl genetics affect melanin, why albinos may appear golden, white or pale, and how to distinguish albino from leucistic animals.",
        "intro": "An albino axolotl is homozygous for a recessive mutation that disrupts melanin production. Because other pigment systems can remain, albino animals are not all the same color: golden, white-albino and axanthic-albino combinations can look different.",
        "num": 214,
        "date_published": "2026-09-18",
        "date_modified": "2026-09-18",
        "headings": [
            "What is an albino axolotl?",
            "What causes albinism in axolotls?",
            "What does an albino axolotl look like?",
            "Golden albino vs albino: what's the difference?",
            "Albino vs leucistic axolotl",
            "What is a white albino axolotl?",
            "What is an axanthic albino axolotl?",
            "Are albino axolotls rare?",
            "Do albino axolotls need different care?",
            "Sources",
        ],
        "body": r'''
<p><strong>Albino axolotls cannot make normal dark melanin because of a recessive mutation affecting the tyrosinase gene.</strong> The term <em>albino</em> describes that loss of melanin production; it does not guarantee one exact body color because yellow pigment, reflective cells and other pigment mutations can change the final appearance.</p>

<h2>What is an albino axolotl?</h2>
<p>In the laboratory axolotl lineage, the classic albino allele was introduced historically through a cross with an albino tiger salamander. Modern genetic work mapped the albino phenotype to <em>tyrosinase</em> (<em>tyr</em>), a key melanin-synthesis gene. Animals with two copies of the recessive albino allele lack normal melanin production.</p>

<h2>What causes albinism in axolotls?</h2>
<p>Research identified a disruptive change in the axolotl <em>tyr</em> allele associated with the historic albino phenotype. Because tyrosinase is required for melanin synthesis, the melanophores can be present but cannot produce normal dark melanin.</p>
<p>Other pigment systems are not automatically removed. That is why an otherwise wild-type albino can still show strong yellow coloration.</p>

<h2>What does an albino axolotl look like?</h2>
<p>An albino axolotl commonly has pale reddish or pinkish eyes because dark melanin is missing. Body color depends on the other pigment traits present:</p>
<ul>
<li><strong>Golden albino:</strong> yellow/gold body with reddish or pink eyes.</li>
<li><strong>White albino:</strong> pale white/pink body from combining the white phenotype with albinism.</li>
<li><strong>Axanthic albino:</strong> very pale animal because both melanin and normal yellow/reflective pigment systems are altered.</li>
</ul>
<p>This is why “albino = white” is too simple for axolotls.</p>

<h2>Golden albino vs albino: what's the difference?</h2>
<p><strong>Golden albino is one visible albino combination, not a separate definition of albinism.</strong> The Ambystoma Genetic Stock Center describes an otherwise wild-type albino as yellow with reddish eyes and notes that this appearance is often called a golden albino. The gold comes from retained yellow pigments rather than melanin.</p>
<p>For the specific yellow-gold phenotype, see the <a href="/morphs/golden-albino/">golden albino axolotl guide</a>.</p>

<h2>Albino vs leucistic axolotl</h2>
<div class="table-wrap"><table>
<thead><tr><th>Feature</th><th>Albino</th><th>Leucistic / white</th></tr></thead>
<tbody>
<tr><td>Main pigment mechanism</td><td>Cannot synthesize normal melanin</td><td>Reduced pigment-cell migration/distribution associated with the white phenotype</td></tr>
<tr><td>Eyes</td><td>Usually pinkish/reddish because melanin is absent</td><td>Typically dark</td></tr>
<tr><td>Body color</td><td>Can be yellow/gold, white/pink or very pale depending on other genes</td><td>Usually pale pink-white</td></tr>
<tr><td>Can combine with other mutations?</td><td>Yes</td><td>Yes</td></tr>
</tbody></table></div>
<p>See <a href="/morphs/leucistic/">leucistic axolotl</a> for the white/dark-eye phenotype.</p>

<h2>What is a white albino axolotl?</h2>
<p>A white albino combines the white phenotype with the albino mutation. It can resemble an ordinary leucistic/white axolotl at first glance, but the eyes are pale or pinkish rather than dark because melanin production is also absent.</p>

<h2>What is an axanthic albino axolotl?</h2>
<p>An axanthic albino combines albinism with the axanthic mutation. AGSC strain notes describe young animals of this genotype as nearly colorless, with older animals sometimes becoming pale yellow as dietary riboflavins accumulate.</p>

<h2>Are albino axolotls rare?</h2>
<p><strong>“Albino” is a genetic phenotype, not a permanent market-rarity category.</strong> Albino stocks are well established in captive axolotls and are maintained by the Ambystoma Genetic Stock Center. Local availability and price depend on breeder supply, lineage, additional traits and region rather than on albinism alone.</p>
<p>Use the <a href="/morphs/morphs-comparison-chart/">morph comparison</a> for appearance and the <a href="/cost-and-buying/axolotl-price-by-morph/">price-by-morph guide</a> for current market context.</p>

<h2>Do albino axolotls need different care?</h2>
<p>Core husbandry is the same: stable cool water, appropriate filtration, suitable food, safe substrate and hides. Pale animals may be visually more sensitive to bright display lighting, but color does not create a separate temperature, water-chemistry or feeding requirement.</p>

<h2>Sources</h2>
<ul>
<li><a href="https://ambystoma.uky.edu/teachers-materials-menu/teachers-materials-books-menu?id=9">Ambystoma Genetic Stock Center: Mutant Genes</a></li>
<li><a href="https://ambystoma.uky.edu/12-educationresources/10-axolotl-strains">Ambystoma Genetic Stock Center: Axolotl Strains</a></li>
<li><a href="https://pubmed.ncbi.nlm.nih.gov/28127056/">Woodcock et al. (2017): identification of the axolotl albino gene</a></li>
<li><a href="https://pubmed.ncbi.nlm.nih.gov/3723064/">Frost et al. (1986): analysis of the albino pigment phenotype</a></li>
</ul>
''',
        "featured": False,
    },

    "morphs/axanthic": {
        "slug": "morphs/axanthic",
        "hub": "morphs",
        "title": "Axanthic Axolotl: Color, Pigment Cells, Genetics & Identification",
        "title_tag": "Axanthic Axolotl: Color, Genetics & Identification",
        "meta": "Learn how axanthic genetics affect yellow pigment and iridophores, how axanthic differs from melanoid, and why genetic combinations change appearance.",
        "intro": "Axanthic axolotls have a recessive pigment phenotype in which normal yellow pteridine pigmentation is lost and iridophore development is also affected. The result is commonly a gray-toned appearance dominated by melanophores, but combinations with albino or other pigment genes can look very different.",
        "num": 215,
        "date_published": "2026-09-18",
        "date_modified": "2026-09-18",
        "headings": [
            "What is an axanthic axolotl?",
            "What causes the axanthic color?",
            "What does an axanthic axolotl look like?",
            "Axanthic vs melanoid axolotl",
            "What is an axanthic albino?",
            "Is axanthic the same as gray, silver or lavender?",
            "Are axanthic axolotls rare?",
            "Do axanthic axolotls need special care?",
            "Sources",
        ],
        "body": r'''
<p><strong>An axanthic axolotl carries a recessive pigment mutation that disrupts the normal yellow-pigment system and also affects reflective pigment cells.</strong> In the classic axanthic phenotype, melanophores remain, so an otherwise wild-type axanthic animal can look uniformly dark gray rather than yellow-green or olive.</p>

<h2>What is an axanthic axolotl?</h2>
<p>The name comes from the loss of normal xanthophore pigmentation. Xanthophores are pigment cells associated with yellow/orange coloration. Classic axolotl genetics uses the symbol <em>ax</em> for the recessive axanthic mutation.</p>

<h2>What causes the axanthic color?</h2>
<p>Microscopy and biochemical studies found unpigmented xanthophore-lineage cells but no detectable pteridine pigments in axanthic skin, suggesting disruption of the pteridine biosynthesis pathway. The same work reported failure of normal iridophore differentiation. Melanophores remained, leaving dark pigment more visually dominant.</p>

<h2>What does an axanthic axolotl look like?</h2>
<p>An otherwise wild-type axanthic may look charcoal, slate or dark gray because it lacks the usual yellow/reflective contribution that gives wild-type animals their olive or greenish mottling. Appearance still varies with age, lighting, genetic background and other pigment genes.</p>
<p>Do not identify an axanthic animal from one photo alone. Use eye appearance, reflective shine, known parentage and breeder records where available.</p>

<h2>Axanthic vs melanoid axolotl</h2>
<div class="table-wrap"><table>
<thead><tr><th>Feature</th><th>Axanthic</th><th>Melanoid</th></tr></thead>
<tbody>
<tr><td>Main pigment change</td><td>Yellow pteridine pigment is absent; iridophore development is also affected</td><td>Increased/dominant dark melanophore appearance with loss of iridophores and reduced xanthophores</td></tr>
<tr><td>Typical impression</td><td>Gray/slate or dark gray</td><td>Deep black/dark brown-gray</td></tr>
<tr><td>Same mutation?</td><td>No</td><td>No</td></tr>
<tr><td>Can occur with albino?</td><td>Yes</td><td>Yes</td></tr>
</tbody></table></div>
<p>Use the <a href="/morphs/melanoid/">melanoid guide</a> for the separate melanoid phenotype.</p>

<h2>What is an axanthic albino?</h2>
<p>Axanthic and albino are separate recessive mutations, so an animal can inherit both. In an axanthic albino, melanin is also absent, removing the dark pigment that normally dominates an axanthic animal. AGSC strain descriptions note that young axanthic albinos can be nearly colorless and may become pale yellow later as riboflavins accumulate.</p>

<h2>Is axanthic the same as gray, silver or lavender?</h2>
<p><strong>No color nickname alone proves axanthic genetics.</strong> Gray, silver and lavender are visual descriptions that may be influenced by lighting, camera processing, other pigment combinations or informal breeder terminology. “Axanthic” is useful when it refers to the actual axanthic phenotype/genetic background rather than simply a cool-toned photograph.</p>
<p>For informal color labels, see <a href="/morphs/blue-and-pink-axolotl-myth/">pink, blue, purple and green axolotl colors</a>.</p>

<h2>Are axanthic axolotls rare?</h2>
<p>Market rarity changes with breeder supply and region. The axanthic mutation is a long-described laboratory pigment phenotype, so the word itself does not mean a one-of-a-kind animal. A captive seller may still charge more for particular combinations or lines.</p>

<h2>Do axanthic axolotls need special care?</h2>
<p>Core care requirements are the same as for other axolotl pigment phenotypes. Color genetics does not create a separate target temperature, nitrogen cycle, feeding schedule or substrate requirement. Evaluate health from body condition, gills, behavior, appetite and measured water quality rather than from the morph name.</p>

<h2>Sources</h2>
<ul>
<li><a href="https://ambystoma.uky.edu/teachers-materials-menu/teachers-materials-books-menu?id=9">Ambystoma Genetic Stock Center: Mutant Genes</a></li>
<li><a href="https://pubmed.ncbi.nlm.nih.gov/3794587/">Frost, Epp & Robinson (1986): analysis of the axanthic phenotype</a></li>
<li><a href="https://ambystoma.uky.edu/12-educationresources/10-axolotl-strains">Ambystoma Genetic Stock Center: Axolotl Strains</a></li>
</ul>
''',
        "featured": False,
    },

    "tank-setup/how-to-test-water": {
        "slug": "tank-setup/how-to-test-water",
        "hub": "tank-setup",
        "title": "How to Test Axolotl Water: Ammonia, Nitrite, Nitrate & pH",
        "title_tag": "How to Test Axolotl Water: Ammonia, Nitrite, Nitrate & pH",
        "meta": "Learn how to test axolotl water for ammonia, nitrite, nitrate and pH, use liquid kits or strips correctly, read results and respond to abnormal values.",
        "intro": "Good water testing has two separate jobs: obtain a reliable reading, then interpret it. This page owns the testing procedure; the Water Parameters & Cycling guide explains what the readings mean and what aquarium process may be causing them.",
        "num": 216,
        "date_published": "2026-09-18",
        "date_modified": "2026-09-18",
        "headings": [
            "What should you test in an axolotl tank?",
            "Liquid test kit vs test strips",
            "How to take a water sample",
            "How to test ammonia",
            "How to test nitrite and nitrate",
            "How to test pH",
            "How to read a color chart accurately",
            "Common water-testing mistakes",
            "How often should you test?",
            "What should you do with the result?",
            "Sources",
        ],
        "body": r'''
<p><strong>Test the water before trying to diagnose an axolotl from appearance or behavior alone.</strong> A reliable aquarium record normally includes ammonia, nitrite, nitrate, pH and temperature, with additional source-water or hardness testing when your local water chemistry makes it relevant.</p>

<h2>What should you test in an axolotl tank?</h2>
<div class="table-wrap"><table>
<thead><tr><th>Measurement</th><th>Why it matters</th><th>Where to interpret it</th></tr></thead>
<tbody>
<tr><td>Ammonia</td><td>Waste and uneaten food enter the nitrogen cycle as ammonia</td><td><a href="/tank-setup/water-parameters-cycling/">Water Parameters & Cycling</a></td></tr>
<tr><td>Nitrite</td><td>Shows the intermediate stage of biological nitrogen processing</td><td><a href="/tank-setup/water-parameters-cycling/">Water Parameters & Cycling</a></td></tr>
<tr><td>Nitrate</td><td>Helps track the end product that accumulates between water changes</td><td><a href="/tank-setup/water-parameters-cycling/">Water Parameters & Cycling</a></td></tr>
<tr><td>pH</td><td>Changes both biological filtration and the toxicity profile of ammonia</td><td><a href="/tank-setup/water-parameters-cycling/">Water Parameters & Cycling</a></td></tr>
<tr><td>Temperature</td><td>Water temperature affects metabolism, oxygen demand and stress</td><td><a href="/tank-setup/temperature/">Temperature guide</a></td></tr>
</tbody></table></div>

<h2>Liquid test kit vs test strips</h2>
<p><strong>Use a testing method that actually measures the parameters you need and follow its instructions exactly.</strong> Multi-parameter strips are fast and convenient, but some products omit ammonia or use a narrower measurement range. Liquid colorimetric kits usually provide individual ammonia, nitrite, nitrate and pH tests but require more steps and careful timing.</p>
<p>The most important rule is consistency: do not compare readings taken with different products as though every scale and chemistry were identical. If a result is surprising, repeat the test and, when possible, confirm it with a second method or a fresh reagent before making a large correction.</p>

<h2>How to take a water sample</h2>
<ol>
<li>Wash your hands and rinse the test vial or sample cup with tank water only.</li>
<li>Take water from the aquarium itself rather than from the replacement-water bucket.</li>
<li>Avoid scooping obvious food debris or substrate into the sample unless you are specifically investigating that area.</li>
<li>Use the exact sample volume required by the test.</li>
<li>Test promptly instead of leaving an open sample sitting for a long period.</li>
</ol>

<h2>How to test ammonia</h2>
<p>Follow the exact reagent order, drop count, mixing method and development time printed for your kit. Some ammonia tests use multiple reagents that must be added in sequence. Read too early or too late and the color may not correspond to the supplied chart.</p>
<p>The AGSC emphasizes frequent ammonia monitoring in municipal-water systems and filtered/recirculating systems because ammonia interacts with pH and biological filtration. Record the number rather than writing “fine” or “bad” so you can compare trends.</p>

<h2>How to test nitrite and nitrate</h2>
<p>Nitrite and nitrate tests also depend on the manufacturer's mixing and timing steps. Nitrate tests in particular may require vigorous shaking to resuspend reagents. Skipping that step can produce a misleadingly low result on some kits.</p>
<p>Measure ammonia, nitrite and nitrate as a set when evaluating the nitrogen cycle. One number by itself cannot show the full direction of the cycle.</p>

<h2>How to test pH</h2>
<p>Use the pH range that covers your actual water. If a broad kit includes both low-range and high-range pH tests, choose the one whose scale brackets your reading rather than forcing an off-scale color match. Compare tank pH with source-water pH when investigating repeated swings.</p>

<h2>How to read a color chart accurately</h2>
<ul>
<li>Use neutral white light rather than colored aquarium LEDs.</li>
<li>Hold the vial against the background specified by the manufacturer.</li>
<li>Read at the stated development time.</li>
<li>If the color falls between two blocks, record it as an approximate range rather than inventing false precision.</li>
<li>Photographs are useful for trend records but phone cameras can change white balance, so do not rely on a photo alone to match a color chart.</li>
</ul>

<h2>Common water-testing mistakes</h2>
<ul>
<li>expired or contaminated reagents;</li>
<li>wrong sample volume;</li>
<li>incorrect drop count;</li>
<li>not shaking a reagent that requires mixing;</li>
<li>reading the result outside the specified time window;</li>
<li>testing only nitrate and assuming ammonia/nitrite must also be safe;</li>
<li>using colored tank lighting to compare the vial; and</li>
<li>making a large water-chemistry change from one questionable reading without confirming it.</li>
</ul>

<h2>How often should you test?</h2>
<p>Test more frequently during cycling, after a suspected cycle disruption, when an animal is unwell, after a major maintenance change, or when readings have been unstable. A mature stable aquarium can be monitored on a routine schedule, but the schedule should tighten whenever conditions change.</p>
<p>Use the <a href="/tools/nitrogen-cycle-tracker/">Nitrogen Cycle Tracker</a> to record results and see trends instead of relying on memory.</p>

<h2>What should you do with the result?</h2>
<p><strong>This page tells you how to obtain the reading; it does not duplicate the full corrective protocol.</strong> Take your confirmed numbers to the <a href="/tank-setup/water-parameters-cycling/">Water Parameters & Cycling guide</a>. If a water change is indicated, follow the <a href="/tank-setup/water-change-guide/">step-by-step Water Change Guide</a>.</p>
<p>If the axolotl shows severe or rapidly worsening signs as well as abnormal water readings, use the <a href="/health/emergency-first-aid/">emergency triage guide</a> and seek veterinary care when indicated.</p>

<h2>Sources</h2>
<ul>
<li><a href="https://ambystoma.uky.edu/genetic-stock-center/documents/AGSC%20_Guide_2024.pdf">Ambystoma Genetic Stock Center: Axolotl Guide 2024, water-quality section</a></li>
<li><a href="https://ambystoma.uky.edu/genetic-stock-center/">Ambystoma Genetic Stock Center</a></li>
</ul>
''',
        "featured": False,
    },
})

# Dedicated MyAxolotl hero graphics for the new pages.
HERO_IMAGE_OVERRIDES.update({
    "biology-and-science/metamorphosis": {
        "file": "axolotl-metamorphosis-explained.webp",
        "alt": "Axolotl neoteny and metamorphosis diagram comparing the normal aquatic adult with the metamorphic pathway",
        "caption": "Axolotls normally mature while retaining larval aquatic traits; metamorphosis is an unusual alternative pathway, not a routine pet-care goal.",
        "description": "Axolotl developmental diagram contrasting paedomorphosis with salamander metamorphosis.",
        "credit": "MyAxolotl original graphic",
        "width": 1600, "height": 900,
    },
    "biology-and-science/axolotl-life-cycle": {
        "file": "axolotl-life-cycle-stages.webp",
        "alt": "Axolotl growth stages from early larva through juvenile and adult",
        "caption": "Axolotl development continues from embryo and hatchling through larva, juvenile and sexually mature aquatic adult.",
        "description": "Axolotl growth-stage graphic used to illustrate the post-hatch portion of the life cycle.",
        "credit": "MyAxolotl original graphic",
        "width": 1600, "height": 900,
    },
    "morphs/albino": {
        "file": "albino-axolotl-identification.webp",
        "alt": "Albino axolotl showing pale eyes and reduced dark melanin",
        "caption": "Albinism removes normal melanin production, while other pigment systems determine whether the animal looks golden, white-pink or very pale.",
        "description": "Albino axolotl pigment graphic showing the visible effect of reduced melanin.",
        "credit": "MyAxolotl original graphic",
        "width": 1600, "height": 900,
    },
    "morphs/axanthic": {
        "file": "axanthic-axolotl-identification.webp",
        "alt": "Axolotl pigment-cell diagram used to explain the axanthic phenotype",
        "caption": "Axanthic genetics alters the normal yellow pteridine system and reflective pigment-cell development, leaving melanophores visually dominant in a typical axanthic animal.",
        "description": "Axolotl pigment-cell graphic explaining how axanthic differs from other color phenotypes.",
        "credit": "MyAxolotl original graphic",
        "width": 1600, "height": 900,
    },
    "tank-setup/how-to-test-water": {
        "file": "how-to-test-axolotl-water.webp",
        "alt": "Axolotl aquarium water testing with ammonia, nitrite, nitrate and pH test vials",
        "caption": "Reliable water testing starts with correct sampling, reagent timing and consistent recording before the numbers are interpreted.",
        "description": "Axolotl water-test graphic showing the core nitrogen-cycle and pH measurements.",
        "credit": "MyAxolotl original graphic",
        "width": 1600, "height": 900,
    },
})

LINKING.update({
    "biology-and-science/metamorphosis": [
        "biology-and-science/neoteny",
        "biology-and-science/axolotl-life-cycle",
        "biology-and-science/axolotl-vs-tiger-salamander",
        "health/finding-an-exotic-vet",
    ],
    "biology-and-science/axolotl-life-cycle": [
        "breeding/egg-and-larvae-care",
        "breeding/raising-juveniles",
        "care-basics/axolotl-age-and-size-chart",
        "biology-and-science/neoteny",
        "biology-and-science/metamorphosis",
    ],
    "morphs/albino": [
        "morphs/golden-albino",
        "morphs/leucistic",
        "morphs/axanthic",
        "morphs/morphs-comparison-chart",
        "morphs/pigment-cells",
    ],
    "morphs/axanthic": [
        "morphs/pigment-cells",
        "morphs/melanoid",
        "morphs/albino",
        "morphs/morphs-comparison-chart",
    ],
    "tank-setup/how-to-test-water": [
        "tank-setup/water-parameters-cycling",
        "tank-setup/water-change-guide",
        "tools/nitrogen-cycle-tracker",
        "health/emergency-first-aid",
    ],
})



# ---------------------------------------------------------------------------
# Keyword-reconciliation new pages — batch 2 (2026-09-18)
# ---------------------------------------------------------------------------

CONFIG_ARTICLES.update({
    "cost-and-buying/where-to-buy-axolotls": {
        "slug": "cost-and-buying/where-to-buy-axolotls",
        "hub": "cost-and-buying",
        "title": "Where to Buy an Axolotl: Breeders, Pet Stores & Online Options",
        "title_tag": "Where to Buy an Axolotl: Breeders, Pet Stores & Online Options",
        "meta": "Compare US axolotl breeders, exotic pet stores, online sellers and rehomes, with checks for legality, animal health, shipping and seller credibility.",
        "intro": "The safest place to buy an axolotl is the seller you can verify, not automatically the closest or cheapest seller. Compare specialist breeders, local exotic pet stores, online sellers and responsible rehomes by the exact animal, husbandry records, legal route, written terms and shipping or pickup plan.",
        "num": 217,
        "date_published": "2026-09-18",
        "date_modified": "2026-09-18",
        "headings": [
            "Where can you buy an axolotl?",
            "Buying from a specialist axolotl breeder",
            "Buying from a local exotic pet store",
            "Buying an axolotl online",
            "Where can you buy an axolotl near you?",
            "Does Petco sell axolotls?",
            "Does PetSmart sell axolotls?",
            "What should you verify before paying?",
            "How do you choose the individual animal?",
            "What should you know about shipping?",
            "How much should an axolotl cost?",
            "Check legality before buying",
            "Current retailer availability note",
        ],
        "body": r'''
<p><strong>Start with the seller's evidence, not the seller category.</strong> A specialist breeder can be easier to verify because they may have hatch dates, parentage, feeding history and current photos, but a good local store or rehome can also be appropriate when the animal and husbandry records are transparent.</p>

<h2>Where can you buy an axolotl?</h2>
<div class="table-wrap"><table>
<thead><tr><th>Source</th><th>Main advantage</th><th>Main thing to verify</th></tr></thead>
<tbody>
<tr><td>Specialist breeder</td><td>Often the best access to lineage, hatch and feeding records</td><td>Actual husbandry, exact-animal photos, written terms and shipping practices</td></tr>
<tr><td>Local exotic pet store</td><td>You may be able to inspect the animal and tank in person</td><td>Water quality, feeding history, source of the animal and staff knowledge</td></tr>
<tr><td>Online seller</td><td>Wider choice of morphs and locations</td><td>Identity, current photos, legal shipping route, weather plan and arrival policy</td></tr>
<tr><td>Responsible rehome / rescue</td><td>Can place an existing animal into an appropriate home</td><td>Health history, reason for rehoming, current setup and quarantine plan</td></tr>
</tbody></table></div>

<h2>Buying from a specialist axolotl breeder</h2>
<p>A specialist breeder is useful when you want clear age, lineage or morph information. Do not treat “breeder” as a quality guarantee. Ask for current photos or video of the exact animal, its feeding routine, measured water conditions, hatch or approximate age, and written arrival or pickup terms.</p>
<p>Use the <a href="/cost-and-buying/choosing-a-reputable-breeder/">12-question axolotl breeder checklist</a> before paying.</p>

<h2>Buying from a local exotic pet store</h2>
<p>Buying locally lets you inspect the animal and the display system before transport. Look beyond the animal's color. Check whether the tank has appropriate substrate, cool stable water, low-flow filtration, intact animals without obvious wounds, and staff who can answer basic husbandry questions with measured values rather than vague assurances.</p>
<p>Ask where the axolotl came from and whether the store has recent feeding and water-quality records. A store that cannot answer those questions is harder to evaluate than one that can.</p>

<h2>Buying an axolotl online</h2>
<p>Online buying adds shipping and transaction risk. Verify the seller's identity, the exact animal, written live-arrival terms, the carrier, delivery timing and the weather plan before payment. Avoid sellers who pressure you to pay immediately, refuse current photos, use only stock images or insist on payment methods with no buyer protection.</p>
<p>Use <a href="/cost-and-buying/red-flags-when-buying/">axolotl seller red flags</a> before placing an online order.</p>

<h2>Where can you buy an axolotl near you?</h2>
<p>For “axolotl for sale near me” searches, start with local exotic-aquatic stores and local breeder listings, then verify the seller rather than assuming proximity means quality. Call before driving because live-animal inventory can change quickly.</p>
<p>Local pickup has one advantage: you can reduce shipping stress and inspect the animal. It does not remove the need for quarantine, acclimation and a fully cycled home tank.</p>

<h2>Does Petco sell axolotls?</h2>
<p><strong>Petco currently says that various axolotls are available at select Petco locations and on Petco.com, with offerings varying by location.</strong> That statement appears on Petco's current axolotl care sheet. Because live inventory varies, call the specific store or check the current product/location system before planning a purchase.</p>
<p>Do not rely on the chain name alone. Apply the same health and husbandry checks you would use for any seller.</p>
<p><strong>Source checked September 18, 2026:</strong> <a href="https://www.petco.com/pet-education/caresheets/axolotl">Petco Axolotl Care Guide — Where to Buy</a>.</p>

<h2>Does PetSmart sell axolotls?</h2>
<p><strong>We did not confirm a current live-axolotl listing on PetSmart's website during our September 18, 2026 check.</strong> PetSmart's site did surface axolotl-themed merchandise, but that is not evidence of live-animal availability. A local store may have different regional inventory, so call the store directly rather than assuming either yes or no from an old search result.</p>
<p>This section is intentionally date-stamped because retailer livestock policies and regional availability change.</p>

<h2>What should you verify before paying?</h2>
<ol>
<li><strong>The exact animal.</strong> Ask for current photos or video, not only a generic morph image.</li>
<li><strong>Feeding history.</strong> What food is it eating, how often, and when did it last eat?</li>
<li><strong>Measured water conditions.</strong> Ask for actual temperature and water-test readings where available.</li>
<li><strong>Age or hatch information.</strong> Exact records are ideal; an honest approximate age is better than a made-up date.</li>
<li><strong>Current body condition and injuries.</strong> Look at gills, skin, limbs, belly and movement.</li>
<li><strong>Written terms.</strong> Know what happens if the animal arrives dead, injured or delayed.</li>
<li><strong>Legal route.</strong> Confirm that ownership, sale, pickup and any interstate shipment are legal for both ends of the transaction.</li>
</ol>

<h2>How do you choose the individual animal?</h2>
<p>Seller quality and animal condition are separate checks. A reputable seller can still have an individual animal that needs treatment or should not be moved yet. Use the <a href="/cost-and-buying/how-to-choose-a-healthy-axolotl/">healthy axolotl buyer checklist</a> to inspect the animal itself.</p>

<h2>What should you know about shipping?</h2>
<p>Live-animal shipping is highly dependent on carrier rules, origin and destination law, weather and delivery timing. Do not accept vague promises such as “we ship anywhere.” Ask what carrier will be used, whether the seller checks weather at both ends, how the animal is packed, whether a signature or hub pickup is used, and what the live-arrival terms require from you.</p>
<p>See <a href="/cost-and-buying/shipping-live-axolotls/">how axolotls are shipped</a> before ordering online.</p>

<h2>How much should an axolotl cost?</h2>
<p>Price depends on morph, size, sex, lineage, seller, region and shipping. Do not use a high price as proof of rarity or health, and do not use a low price as proof of a bargain. Compare current market examples in the <a href="/cost-and-buying/axolotl-price-by-morph/">axolotl price-by-morph guide</a>.</p>

<h2>Check legality before buying</h2>
<p><strong>Confirm ownership and transport rules before you send money.</strong> State, provincial, local and import rules can differ, and a seller's willingness to ship is not legal advice. Use the <a href="/legal/">axolotl legality hub</a> and then verify the current primary-source rules for your jurisdiction.</p>

<h2>Current retailer availability note</h2>
<p>This page separates long-term buying guidance from retailer availability because stock changes faster than husbandry principles. Petco's official care sheet was checked on September 18, 2026 and states that axolotls are offered at select locations and Petco.com. A current live-axolotl PetSmart listing was not confirmed in the same check. Recheck retailer sites and call the local store before making a trip.</p>
''',
        "featured": False,
    },

    "health/healthy-axolotl-poop": {
        "slug": "health/healthy-axolotl-poop",
        "hub": "health",
        "title": "Axolotl Poop: What's Normal, Frequency & Warning Signs",
        "title_tag": "Axolotl Poop: What's Normal, Frequency & Warning Signs",
        "meta": "Learn what can be normal for axolotl poop, how to track frequency and consistency, warning signs to watch for and when a veterinary fecal test may help.",
        "intro": "There is no well-established veterinary chart that defines one universal 'normal axolotl poop' color, shape or schedule. The useful approach is to know your animal's baseline, track fecal production with appetite and body condition, and use a fresh veterinary fecal examination when persistent changes raise concern for parasites or gastrointestinal disease.",
        "num": 218,
        "date_published": "2026-09-18",
        "date_modified": "2026-09-18",
        "headings": [
            "What does normal axolotl poop look like?",
            "How often do axolotls poop?",
            "What should you track?",
            "Does white or stringy poop mean parasites?",
            "When can poop changes point to impaction or constipation?",
            "What signs make a stool change more concerning?",
            "How does a veterinarian test axolotl poop?",
            "How do you collect a fresh fecal sample?",
            "When should you contact a vet?",
            "Sources",
        ],
        "body": r'''
<p><strong>Do not diagnose an axolotl from stool color alone.</strong> Axolotl-specific veterinary literature does not provide a validated “healthy poop chart” with one correct color, shape or number of bowel movements. Veterinary amphibian references instead emphasize observing fecal production, the animal's overall condition and husbandry, and examining a fresh fecal sample when parasites or gastrointestinal disease are suspected.</p>

<h2>What does normal axolotl poop look like?</h2>
<p><strong>Use your own healthy animal's repeated baseline rather than an internet color chart.</strong> Diet, meal size, digestion time and how long feces remains in water can change its appearance. Once a sample sits in the aquarium, it can soften, break apart and mix with substrate, food debris or biofilm, making visual interpretation less reliable.</p>
<p>The most useful question is therefore not “Is this exact shade normal?” but “Is this a persistent change from this axolotl's usual feces, and is it happening with appetite, weight, swelling, behavior or water-quality changes?”</p>

<h2>How often do axolotls poop?</h2>
<p><strong>There is no single evidence-based bowel-movement schedule for every axolotl.</strong> Frequency varies with age, feeding schedule, meal size, food type, temperature, activity and individual digestion. A juvenile eating more frequently may pass waste on a different schedule from an adult fed only a few times a week.</p>
<p>Track frequency in relation to meals rather than expecting one bowel movement every fixed number of days.</p>

<h2>What should you track?</h2>
<div class="table-wrap"><table>
<thead><tr><th>Observation</th><th>Why it helps</th></tr></thead>
<tbody>
<tr><td>Date of last meal</td><td>Connects stool timing with feeding frequency and fasting</td></tr>
<tr><td>Food type and amount</td><td>Diet changes can alter fecal output</td></tr>
<tr><td>Fecal production</td><td>Shows whether waste is still being passed</td></tr>
<tr><td>Persistent change in consistency</td><td>More useful than one isolated unusual sample</td></tr>
<tr><td>Appetite and weight trend</td><td>Helps distinguish an isolated stool change from a broader health problem</td></tr>
<tr><td>Belly shape / swelling</td><td>Persistent distension plus reduced output may require gastrointestinal assessment</td></tr>
<tr><td>Water quality and temperature</td><td>Husbandry stress can change appetite, activity and digestion</td></tr>
</tbody></table></div>

<h2>Does white or stringy poop mean parasites?</h2>
<p><strong>No single stool appearance proves parasites.</strong> Amphibian feces can contain microorganisms that are not causing disease; Merck/MSD Veterinary Manual specifically notes that gastrointestinal protozoa may be abundant without necessarily indicating illness. At the same time, parasites can be detected in feces and some infections are associated with weight loss, poor appetite or abnormal stool.</p>
<p>That is why “white/stringy = parasites” is too simplistic. If the change persists or occurs with weight loss, anorexia, weakness, bloating or other signs, a veterinarian can examine a fresh sample rather than treating from appearance alone.</p>

<h2>When can poop changes point to impaction or constipation?</h2>
<p>A period without visible feces is not enough by itself to diagnose impaction. The concern rises when reduced fecal output occurs with persistent abdominal swelling, loss of appetite, abnormal buoyancy, pain-like behavior, known ingestion of gravel or another foreign material, or progressive decline.</p>
<p>Use the <a href="/health/impaction-symptoms-treatment/">axolotl impaction guide</a> for suspected blockage and the <a href="/tank-setup/gravel-risks/">gravel-risk guide</a> if swallowable substrate may be involved.</p>

<h2>What signs make a stool change more concerning?</h2>
<p>Seek veterinary advice sooner when an abnormal fecal pattern is accompanied by:</p>
<ul>
<li>persistent loss of appetite;</li>
<li>progressive weight loss or poor body condition;</li>
<li>blood-tinged feces;</li>
<li>visible worms or repeated unusual material;</li>
<li>persistent or increasing abdominal swelling;</li>
<li>cloacal prolapse;</li>
<li>marked lethargy or abnormal swimming; or</li>
<li>multiple animals in the same collection developing similar signs.</li>
</ul>

<h2>How does a veterinarian test axolotl poop?</h2>
<p>Veterinary amphibian workups may use a direct wet mount, flotation, sedimentation or other fecal techniques depending on the suspected organism. A 2026 study of juvenile <em>Ambystoma mexicanum</em> used fecal sedimentation, Faust and modified McMaster methods to detect <em>Eimeria</em> oocysts and nematode eggs, showing why microscopic testing is more informative than visual color matching.</p>
<p>A positive organism on microscopy still has to be interpreted with the animal's clinical signs because some amphibian gastrointestinal organisms can be present without causing disease.</p>

<h2>How do you collect a fresh fecal sample?</h2>
<p><strong>If your veterinarian asks for a fecal sample, collect the freshest uncontaminated sample you can.</strong> Use a clean disposable tool and place the sample in a clean leakproof container. Keep it separate from substrate, uneaten food and dirty filter material as much as possible.</p>
<p>Ask the clinic how quickly they want it delivered and whether it should be refrigerated. Freshness matters for some parasite stages, and the exact handling method depends on the test the veterinarian plans to run.</p>

<h2>When should you contact a vet?</h2>
<p>One unusual bowel movement in an otherwise normal axolotl is less informative than a persistent change with other clinical signs. Contact an amphibian-experienced veterinarian when stool changes persist, when the animal is losing weight or refusing food, when there is blood or prolapse, or when swelling and reduced output suggest a possible obstruction.</p>
<p>Use the <a href="/health/finding-an-exotic-vet/">axolotl vet finder</a> for escalation and the <a href="/health/parasite-treatment/">parasite guide</a> for the difference between suspicion and confirmed treatment.</p>

<h2>Sources</h2>
<ul>
<li><a href="https://www.merckvetmanual.com/exotic-and-laboratory-animals/amphibians/clinical-techniques-in-amphibians">Merck Veterinary Manual: Clinical Techniques in Amphibians</a></li>
<li><a href="https://www.msdvetmanual.com/exotic-and-laboratory-animals/amphibians/infectious-diseases-of-amphibians">MSD Veterinary Manual: Infectious Diseases of Amphibians</a></li>
<li><a href="https://pubmed.ncbi.nlm.nih.gov/41608998/">2026 study: Eimeria and nematode detection in Ambystoma mexicanum fecal samples</a></li>
<li><a href="https://veterinarypartner.vin.com/default.aspx?id=8030801&amp;meta=0&amp;pId=19239">Veterinary Partner / VIN: Gastrointestinal Foreign Body or Overload in Amphibians</a></li>
</ul>
''',
        "featured": False,
    },
})

HERO_IMAGE_OVERRIDES.update({
    "cost-and-buying/where-to-buy-axolotls": {
        "file": "where-to-buy-axolotls.webp",
        "alt": "Axolotl buying-source comparison covering breeders, pet stores, online sellers and verification questions",
        "caption": "Where you buy matters less than what you can verify: the exact animal, husbandry records, written terms, legal route and shipping or pickup plan.",
        "description": "Axolotl buying guide graphic comparing breeder, pet-store and online purchase checks.",
        "credit": "MyAxolotl original graphic",
        "width": 1600, "height": 900,
    },
    "health/healthy-axolotl-poop": {
        "file": "healthy-axolotl-poop-guide.webp",
        "alt": "Axolotl health observation graphic used for fecal and parasite assessment guidance",
        "caption": "Stool appearance alone cannot diagnose parasites or impaction. Track the animal's baseline and use a fresh veterinary fecal examination when persistent changes occur with other signs.",
        "description": "Axolotl health graphic emphasizing observation, fresh fecal testing and veterinary confirmation.",
        "credit": "MyAxolotl original graphic",
        "width": 1600, "height": 900,
    },
})

LINKING.update({
    "cost-and-buying/where-to-buy-axolotls": [
        "cost-and-buying/breeder-vs-pet-store",
        "cost-and-buying/choosing-a-reputable-breeder",
        "cost-and-buying/how-to-choose-a-healthy-axolotl",
        "cost-and-buying/red-flags-when-buying",
        "cost-and-buying/shipping-live-axolotls",
        "cost-and-buying/axolotl-price-by-morph",
        "legal",
    ],
    "health/healthy-axolotl-poop": [
        "health/parasite-treatment",
        "health/impaction-symptoms-treatment",
        "health/refusing-to-eat",
        "health/finding-an-exotic-vet",
        "tank-setup/water-parameters-cycling",
    ],
})



# ---------------------------------------------------------------------------
# Keyword-reconciliation new pages — batch 3 (2026-09-18)
# ---------------------------------------------------------------------------

CONFIG_ARTICLES.update({
    "axolotl-in-culture/do-people-eat-axolotls": {
        "slug": "axolotl-in-culture/do-people-eat-axolotls",
        "hub": "axolotl-in-culture",
        "title": "Do People Eat Axolotls? History, Culture & Conservation",
        "title_tag": "Do People Eat Axolotls? History, Culture & Conservation",
        "meta": "Explore the history of axolotls as food and traditional medicine in Mexico and why critically endangered wild axolotls should never be harvested today.",
        "intro": "Yes, axolotls have a documented history as food in central Mexico, including pre-Hispanic and later Xochimilco traditions. That historical fact should not be confused with advice to eat wild axolotls today: Ambystoma mexicanum is critically endangered in the wild, and modern conservation measures protect the remaining Xochimilco population.",
        "num": 219,
        "date_published": "2026-09-18",
        "date_modified": "2026-09-18",
        "headings": [
            "Did people historically eat axolotls?",
            "How were axolotls used in pre-Hispanic Mexico?",
            "Were axolotls still eaten after the colonial period?",
            "Do people eat axolotls today?",
            "Why shouldn't wild axolotls be harvested?",
            "What does the historical food record tell us?",
            "Axolotls in traditional medicine",
            "Food history vs pet axolotls",
            "Sources",
        ],
        "body": r'''
<p><strong>Axolotls have a real food history in Mexico, especially in the lake-and-canal cultures of the Valley of Mexico.</strong> Historical sources and modern Mexican government/university summaries document axolotls as part of local diets before and after the Spanish conquest. That does not mean the remaining wild <em>Ambystoma mexicanum</em> population should be treated as food today.</p>

<h2>Did people historically eat axolotls?</h2>
<p><strong>Yes.</strong> Mexico's environmental ministry notes that the Mexican axolotl was valued as food from before the colonial period onward. UNAM historical research likewise identifies the axolotl as both a food resource and a culturally significant animal in Nahua history.</p>
<p>The historical record makes sense in context: the lakes and wetlands around the Valley of Mexico supported fish, frogs, crustaceans, insects, waterfowl and axolotls that formed part of a much broader lacustrine food system.</p>

<h2>How were axolotls used in pre-Hispanic Mexico?</h2>
<p>Nahuatl-language and colonial-era sources record axolotls among aquatic animals exchanged, presented and eaten. The UNAM Gran Diccionario Náhuatl preserves historical passages listing axolotls alongside fish, frogs, shrimp and other products of the lake environment.</p>
<p>Modern historical summaries from Xochimilco also describe axolotls among the animal foods used in pre-Hispanic regional cooking. The important point is cultural context: this was part of a living wetland economy, not a novelty food trend detached from the ecosystem.</p>

<h2>Were axolotls still eaten after the colonial period?</h2>
<p>Yes. Mexican environmental and historical sources describe continued use in soups, stews, tamal-like preparations and traditional remedies over later periods. The record is historical and ethnographic; this page does not reproduce recipes or provide instructions for harvesting or preparing wild animals.</p>

<h2>Do people eat axolotls today?</h2>
<p><strong>Historical consumption continues to appear in cultural accounts, but the wild Xochimilco axolotl is now a conservation priority rather than an ordinary food resource.</strong> The Xochimilco borough's current cultural material notes that traditional dishes involving protected species such as the axolotl have been adapted or disappeared as protection measures increased.</p>
<p>Mexico's national aquaculture information also notes that captive culture exists, but production costs make food-industry use difficult and the species is maintained primarily as an ornamental/captive animal rather than a mainstream food product.</p>

<h2>Why shouldn't wild axolotls be harvested?</h2>
<p>Wild <em>Ambystoma mexicanum</em> survives only in a highly restricted Xochimilco habitat and is critically endangered. Habitat degradation, introduced fish, water-quality pressures and fragmentation already threaten the remaining population.</p>
<p><strong>Do not collect, buy or eat a wild-caught Xochimilco axolotl.</strong> Conservation depends on protecting habitat and the wild population, not recreating historical harvest practices.</p>
<p>See <a href="/biology-and-science/conservation-status/">axolotl conservation status</a> and <a href="/biology-and-science/wild-habitat-xochimilco/">wild habitat in Xochimilco</a>.</p>

<h2>What does the historical food record tell us?</h2>
<p>The record shows that axolotls were embedded in human culture long before they became laboratory animals, internet icons or pets. Food use, traditional medicine, mythology and local ecology all form part of the species' history.</p>
<p>That matters for interpretation: “Were axolotls eaten?” is a cultural-history question, not a care or husbandry question and not evidence that modern pet axolotls should be treated as food.</p>

<h2>Axolotls in traditional medicine</h2>
<p>Mexican government sources also document historical use of axolotl preparations in traditional remedies, especially for respiratory complaints. Historical medical use does not establish modern clinical effectiveness, and this page does not recommend axolotl-derived remedies.</p>

<h2>Food history vs pet axolotls</h2>
<p>Captive pet axolotls belong to a modern husbandry context. If your interest is buying or caring for a pet, use the <a href="/cost-and-buying/where-to-buy-axolotls/">where-to-buy guide</a> and <a href="/axolotls/care-guide/">complete care guide</a>. If your interest is why the animal matters in Mexico, continue to the site's history, culture and conservation coverage.</p>

<h2>Sources</h2>
<ul>
<li><a href="https://www.gob.mx/semarnat/articulos/ajolote-mexicano-criatura-super-dotada?idiom=es">SEMARNAT: Ajolote mexicano, criatura súper dotada</a></li>
<li><a href="https://ru.historicas.unam.mx/handle/20.500.12525/9239">UNAM Instituto de Investigaciones Históricas: El axólotl</a></li>
<li><a href="https://gdn.iib.unam.mx/diccionario/axolotl/174630">UNAM Gran Diccionario Náhuatl: axolotl</a></li>
<li><a href="https://www.xochimilco.cdmx.gob.mx/que-comer/">Alcaldía Xochimilco: historical regional food traditions</a></li>
<li><a href="https://sidof.segob.gob.mx/notas/docFuente/5668529">Carta Nacional Acuícola: Ajolote</a></li>
</ul>
''',
        "featured": False,
    },

    "axolotl-in-culture/minecraft-axolotl-enclosure-builds": {
        "slug": "axolotl-in-culture/minecraft-axolotl-enclosure-builds",
        "hub": "axolotl-in-culture",
        "title": "Minecraft Axolotl Enclosure Builds: Tanks, Caves & Breeding Pools",
        "title_tag": "Minecraft Axolotl Enclosure Builds: Tanks, Caves & Breeding Pools",
        "meta": "Build a functional Minecraft axolotl enclosure with water-first tanks, lush caves, breeding pools, escape prevention and practical decoration ideas.",
        "intro": "A good Minecraft axolotl enclosure is mostly a water-design problem: keep the mob in or near water, make collection and breeding easy, and decorate around those mechanics. This page focuses on builds; spawning, food, breeding odds and commands stay in the main Minecraft axolotl guide.",
        "num": 220,
        "date_published": "2026-09-18",
        "date_modified": "2026-09-18",
        "headings": [
            "What does a Minecraft axolotl enclosure need?",
            "Build 1: simple glass aquarium",
            "Build 2: lush-cave axolotl habitat",
            "Build 3: breeding pool for a blue axolotl",
            "Build 4: underground viewing tunnel",
            "Build 5: natural pond enclosure",
            "How do you stop axolotls drying out?",
            "Will enclosure axolotls despawn?",
            "What blocks and decorations work well?",
            "How large should the enclosure be?",
            "Common Minecraft axolotl enclosure mistakes",
            "Sources and version notes",
        ],
        "body": r'''
<p><strong>Minecraft axolotl enclosures should prioritize continuous water access.</strong> Current Bedrock behavior data gives axolotls a five-minute drying timer when they are out of water, so a decorative land-heavy enclosure is less reliable than a water-first aquarium, pond or cave pool.</p>

<h2>What does a Minecraft axolotl enclosure need?</h2>
<ul>
<li><strong>Enough water for normal swimming.</strong></li>
<li><strong>Walls or landscaping that prevent long land wandering.</strong></li>
<li><strong>Easy bucket access</strong> if you collect colors or move animals.</li>
<li><strong>A breeding area</strong> if you are trying for the rare blue variant.</li>
<li><strong>Lighting and blocks that fit the theme</strong> without blocking your own access.</li>
</ul>
<p>You do not need to “tame” the axolotl first. Minecraft axolotls are not tameable in the wolf/cat sense; you keep them by bucket transport, enclosure design and breeding.</p>

<h2>Build 1: simple glass aquarium</h2>
<p>This is the easiest display build.</p>
<ol>
<li>Build a rectangular glass tank with a solid floor.</li>
<li>Fill the usable interior with water rather than leaving large dry ledges.</li>
<li>Add clay, moss, rooted dirt, stone or other natural-looking blocks for visual texture.</li>
<li>Use trapdoors, stairs or slabs outside the waterline as decoration without creating an easy path out.</li>
<li>Add the axolotl with a water bucket.</li>
</ol>
<p>A long, low aquarium is easier to view than a tall narrow column. The exact dimensions are aesthetic rather than a hidden game requirement.</p>

<h2>Build 2: lush-cave axolotl habitat</h2>
<p>For a natural look, recreate the lush-cave theme with clay, moss, dripleaf, azalea, glow berries and irregular stone. Keep the water pool broad and make the land margin steep enough that axolotls quickly return to water if they climb out.</p>
<p>This build matches the mob's current natural-spawn theme without needing to reproduce every spawn condition inside a player-made enclosure.</p>

<h2>Build 3: breeding pool for a blue axolotl</h2>
<p>A breeding pool should be functional before it is decorative:</p>
<ul>
<li>keep two adults in an easy-to-access water area;</li>
<li>store Buckets of Tropical Fish nearby;</li>
<li>leave enough room to see and bucket the baby;</li>
<li>separate or label colors if you are tracking breeding pairs.</li>
</ul>
<p>Current Bedrock behavior data uses a tropical-fish bucket as the breeding item and shows a blue mutation factor of about 1 in 1,200 for a new baby. Once a blue parent exists, inheritance also matters, so a dedicated pool helps you manage repeated breeding efficiently.</p>
<p>For breeding rules and blue-variant odds, use the <a href="/axolotl-in-culture/minecraft-axolotls-guide/">main Minecraft axolotl guide</a>.</p>

<h2>Build 4: underground viewing tunnel</h2>
<p>Build the enclosure around a glass tunnel instead of placing the player walkway above the water. Axolotls can swim on both sides while you move through a dry central corridor. This works well for large collections because the animals remain in water while the player gets a close view.</p>

<h2>Build 5: natural pond enclosure</h2>
<p>A landscaped pond works well in gardens, caves or village builds. Use a deep central water area, short shoreline and perimeter blocks that discourage long wandering. Reeds, mossy stone and clay fit the theme, but avoid designing a broad dry beach that invites the axolotl to stay out of water.</p>

<h2>How do you stop axolotls drying out?</h2>
<p><strong>Keep water close and make escape paths short.</strong> Microsoft's current Bedrock behavior data sets a drying-out timer of 300 seconds when an axolotl is on land. Rain or returning to water interrupts the drying state.</p>
<p>The safest design is therefore not an “amphibian terrarium” with a large land section; it is a water enclosure with decorative edges.</p>

<h2>Will enclosure axolotls despawn?</h2>
<p>Bucket an axolotl before moving it into a permanent collection. The main Minecraft guide covers current persistence behavior in more detail, but bucket collection is the practical way to transport and keep specific colors you care about.</p>

<h2>What blocks and decorations work well?</h2>
<div class="table-wrap"><table>
<thead><tr><th>Theme</th><th>Useful blocks</th></tr></thead>
<tbody>
<tr><td>Lush cave</td><td>Moss, clay, stone, dripleaf, azalea, glow berries</td></tr>
<tr><td>Modern aquarium</td><td>Glass, quartz, sea lanterns, smooth stone</td></tr>
<tr><td>Natural pond</td><td>Mud, mossy stone, clay, rooted dirt, leaves</td></tr>
<tr><td>Fantasy display</td><td>Prismarine, tinted glass, froglights, amethyst accents</td></tr>
</tbody></table></div>
<p>Decoration does not change breeding odds. Keep the functional water area easy to reach before adding visual complexity.</p>

<h2>How large should the enclosure be?</h2>
<p>Minecraft does not give axolotls a real-world welfare gallon requirement. Build size is therefore about pathing, visibility, number of mobs and your design goal. A compact breeding pool can be small; a display habitat can be as large as you want.</p>

<h2>Common Minecraft axolotl enclosure mistakes</h2>
<ul>
<li>large dry shorelines that let mobs stay out of water;</li>
<li>decor so dense that you cannot bucket or see babies;</li>
<li>assuming a special block increases the blue-axolotl mutation chance;</li>
<li>trying to tame the axolotl instead of using buckets and breeding;</li>
<li>mixing real axolotl husbandry rules with Minecraft mechanics.</li>
</ul>

<h2>Sources and version notes</h2>
<ul>
<li><a href="https://learn.microsoft.com/en-us/minecraft/creator/reference/source/vanillabehaviorpack_snippets/entities/axolotl?view=minecraft-bedrock-stable">Microsoft Learn: current vanilla axolotl behavior data</a></li>
<li><a href="https://learn.microsoft.com/en-us/minecraft/creator/reference/content/entityreference/examples/entitygoals/minecraftbehavior_move_to_water?view=minecraft-bedrock-stable">Microsoft Learn: move-to-water behavior</a></li>
<li><a href="/axolotl-in-culture/minecraft-axolotls-guide/">MyAxolotl: current Minecraft axolotl mechanics and version notes</a></li>
</ul>
''',
        "featured": False,
    },

    "axolotl-in-culture/axolotl-names": {
        "slug": "axolotl-in-culture/axolotl-names",
        "hub": "axolotl-in-culture",
        "title": "Axolotl Names: Cute, Funny, Color & Unique Name Ideas",
        "title_tag": "Axolotl Names: Cute, Funny, Color & Unique Name Ideas",
        "meta": "Browse cute, funny, color, food, science, nature and Minecraft-inspired axolotl names, with a simple method for choosing a memorable name.",
        "intro": "A useful axolotl name is short enough to remember, distinct from your other pets, and connected to something you actually notice about the animal—its morph, personality, favorite hide, feeding behavior or the story of how you got it.",
        "num": 221,
        "date_published": "2026-09-18",
        "date_modified": "2026-09-18",
        "headings": [
            "How do you choose a good axolotl name?",
            "Cute axolotl names",
            "Funny axolotl names",
            "Food-inspired axolotl names",
            "Pink and leucistic axolotl names",
            "Dark and melanoid axolotl names",
            "Golden and albino axolotl names",
            "Copper axolotl names",
            "Science-inspired axolotl names",
            "Water and nature names",
            "Minecraft-inspired axolotl names",
            "Gender-neutral axolotl names",
            "Unique axolotl names",
            "A quick 3-step naming method",
        ],
        "body": r'''
<p><strong>There is no “correct” axolotl name.</strong> The best names usually come from one memorable trait: color, behavior, food, water, science, a game, or a joke that still makes sense after the novelty wears off.</p>

<h2>How do you choose a good axolotl name?</h2>
<p>Use three filters:</p>
<ol>
<li><strong>Easy to say:</strong> one to three syllables is convenient.</li>
<li><strong>Easy to distinguish:</strong> avoid a name that sounds almost identical to another pet in the house.</li>
<li><strong>Connected to the animal:</strong> choose a trait, story or theme you will still recognize later.</li>
</ol>
<p>Axolotl sex is often unknown when the animal is young, so gender-neutral names are especially useful.</p>

<h2>Cute axolotl names</h2>
<p>Bean, Bubbles, Mochi, Pebble, Poppy, Pip, Noodle, Waffle, Sprout, Pudding, Button, Miso, Tofu, Pogo, Gilly, Doodle, Jellybean, Twinkle, Niblet, Pickle.</p>

<h2>Funny axolotl names</h2>
<p>Sir Gills, Gillbert, Gillian, Professor Wiggle, Water Sausage, Captain Frill, Axolittle, Lotl, Sir Swims-a-Lotl, Snack Inspector, Bubble Boss, Mud Manager, Worm Auditor, Frill Clinton, Tank Sinatra, Gill Nye, Swim Shady, The Axeman, Bucket, Soggy.</p>

<h2>Food-inspired axolotl names</h2>
<p>Mochi, Dumpling, Nori, Miso, Tofu, Udon, Ramen, Sesame, Pumpkin, Peach, Jelly, Pudding, Cocoa, Truffle, Cinnamon, Nugget, Waffle, Biscuit, Mango, Boba.</p>

<h2>Pink and leucistic axolotl names</h2>
<p>Blush, Pearl, Rose, Peony, Sakura, Marshmallow, Cloud, Quartz, Petal, Cotton, Opal, Frosting, Lychee, Milkshake, Pinky, Blossom, Moon, Snowdrop, Vanilla, Halo.</p>
<p>If you are not sure whether a pale animal is leucistic or albino, use the <a href="/morphs/morphs-comparison-chart/">morph comparison</a> rather than naming the genetics from color alone.</p>

<h2>Dark and melanoid axolotl names</h2>
<p>Onyx, Ink, Shadow, Coal, Pepper, Slate, Eclipse, Obsidian, Raven, Midnight, Smoky, Licorice, Storm, Ash, Soot, Graphite, Nova, Phantom, Noir, Cinder.</p>

<h2>Golden and albino axolotl names</h2>
<p>Sunny, Goldie, Honey, Saffron, Butter, Lemon, Sol, Amber, Marigold, Custard, Dune, Topaz, Glow, Biscotti, Cornbread, Maple, Dawn, Buttercup, Halo, Gleam.</p>

<h2>Copper axolotl names</h2>
<p>Penny, Copper, Rusty, Auburn, Maple, Ember, Terra, Cinnamon, Chestnut, Caramel, Bronze, Autumn, Paprika, Brick, Sienna, Toffee, Rooibos, Ginger, Hazel, Sepia.</p>

<h2>Science-inspired axolotl names</h2>
<p>Darwin, Curie, Tesla, Newton, Ada, Rosalind, Mendel, Neuron, Axon, Glia, Nova, Quark, Pixel, Helix, Vector, Soma, Thyroid, Blastema, Regen, Atlas.</p>
<p><strong>Blastema</strong> is especially on-theme: it is the mass of proliferating cells involved in limb regeneration. For the biology, see <a href="/biology-and-science/regeneration-and-limb-regrowth/">axolotl regeneration</a>.</p>

<h2>Water and nature names</h2>
<p>River, Ripple, Brook, Rain, Mist, Delta, Lagoon, Moss, Fern, Willow, Reed, Pebble, Cove, Tide, Dew, Lotus, Lily, Marina, Azul, Aqua.</p>

<h2>Minecraft-inspired axolotl names</h2>
<p>Lucy, Cyan, Gold, Blue, Lush, Clay, Moss, Bucket, Dripleaf, Glowberry, Azalea, Caves, Pixel, Block, Spawn, Bedrock, Java, Steve, Alex, Mojang.</p>
<p>For game mechanics rather than naming ideas, see the <a href="/axolotl-in-culture/minecraft-axolotls-guide/">Minecraft axolotl guide</a>.</p>

<h2>Gender-neutral axolotl names</h2>
<p>Bean, River, Nova, Pixel, Moss, Mochi, Sunny, Echo, Pebble, Sage, Pip, Clover, Orbit, Comet, Nori, Onyx, Indigo, Bubble, Puck, Scout.</p>

<h2>Unique axolotl names</h2>
<p>Quasar, Vesper, Lumen, Kelp, Orbit, Sumi, Nimbus, Tundra, Rune, Calyx, Zephyr, Mica, Rook, Fable, Brume, Solace, Kumo, Oriel, Nix, Vanta.</p>

<h2>A quick 3-step naming method</h2>
<ol>
<li>Choose one category: <strong>color, behavior, food, science, nature, game or joke</strong>.</li>
<li>Write five names from that category and say each one aloud twice.</li>
<li>Pick the one that still feels natural after a day rather than the most complicated option.</li>
</ol>
<p>If you have several axolotls, use a shared theme—planets, foods, scientists, weather, plants or game blocks—while keeping each individual name clearly different.</p>
''',
        "featured": False,
    },
})

HERO_IMAGE_OVERRIDES.update({
    "axolotl-in-culture/do-people-eat-axolotls": {
        "file": "axolotl-food-history-conservation.webp",
        "alt": "Wild-type axolotl in Xochimilco used to illustrate the species' food history and modern conservation context",
        "caption": "Axolotls were historically part of the Valley of Mexico's lacustrine food culture, but the remaining wild Xochimilco population is now a conservation priority.",
        "description": "Xochimilco axolotl graphic connecting historical human use with modern wild-population conservation.",
        "credit": "MyAxolotl original graphic",
        "width": 1600, "height": 900,
    },
    "axolotl-in-culture/minecraft-axolotl-enclosure-builds": {
        "file": "minecraft-axolotl-enclosure-builds.webp",
        "alt": "Minecraft axolotl habitat with water enclosure, lush-cave blocks and multiple axolotl colors",
        "caption": "Minecraft axolotl builds work best as water-first aquariums, cave pools or breeding enclosures with easy bucket access.",
        "description": "Minecraft axolotl build graphic illustrating enclosure and breeding-pool concepts.",
        "credit": "MyAxolotl original graphic",
        "width": 1600, "height": 900,
    },
    "axolotl-in-culture/axolotl-names": {
        "file": "axolotl-name-ideas.webp",
        "alt": "Axolotl surrounded by playful theme icons used for naming inspiration",
        "caption": "Choose an axolotl name from something memorable about the animal: color, behavior, food, nature, science, games or a joke.",
        "description": "Playful axolotl culture graphic used for a categorized axolotl name-ideas guide.",
        "credit": "MyAxolotl original graphic",
        "width": 1600, "height": 900,
    },
})

LINKING.update({
    "axolotl-in-culture/do-people-eat-axolotls": [
        "biology-and-science/wild-habitat-xochimilco",
        "biology-and-science/conservation-status",
        "care-basics/axolotl-facts",
        "axolotl-in-culture/axolotl-in-pop-culture-and-memes",
    ],
    "axolotl-in-culture/minecraft-axolotl-enclosure-builds": [
        "axolotl-in-culture/minecraft-axolotls-guide",
        "morphs/blue-and-pink-axolotl-myth",
        "morphs/morphs-comparison-chart",
    ],
    "axolotl-in-culture/axolotl-names": [
        "morphs/morphs-comparison-chart",
        "biology-and-science/regeneration-and-limb-regrowth",
        "axolotl-in-culture/minecraft-axolotls-guide",
        "axolotl-in-culture/axolotl-in-pop-culture-and-memes",
    ],
})



# ---------------------------------------------------------------------------
# Keyword-reconciliation new pages — batch 4 (2026-09-18)
# ---------------------------------------------------------------------------

CONFIG_ARTICLES.update({
    "care-basics/are-axolotls-poisonous": {
        "slug": "care-basics/are-axolotls-poisonous",
        "hub": "care-basics",
        "title": "Are Axolotls Poisonous or Dangerous? Venom, Bites & Human Safety",
        "title_tag": "Are Axolotls Poisonous or Dangerous? Venom, Bites & Safety",
        "meta": "Are axolotls poisonous or venomous? Learn the real human-health risks from bites, handling, tank water and Salmonella, plus safer hygiene around pet axolotls.",
        "intro": "Pet axolotls are not generally treated as poisonous or venomous animals. The practical human-health risks are ordinary bite or wound hygiene and germs associated with amphibians and aquarium water, especially Salmonella—not toxin injection.",
        "num": 222,
        "date_published": "2026-09-18",
        "date_modified": "2026-09-18",
        "headings": [
            "Are axolotls poisonous?",
            "Are axolotls venomous?",
            "Can an axolotl bite hurt you?",
            "Can you get sick from touching an axolotl?",
            "Can axolotl tank water carry germs?",
            "Who should be extra careful around amphibians?",
            "What should you do after an axolotl bite?",
            "Is it safe to pet or hold an axolotl?",
            "Axolotl danger myths vs real risks",
            "Sources",
        ],
        "body": r'''
<p><strong>Pet axolotls are not generally regarded as poisonous or venomous to people.</strong> Standard species and veterinary references focus on their delicate amphibian skin, small teeth, aquatic husbandry and infectious-disease hygiene rather than a toxin-delivery system. The main human-health issue is contact with germs carried by amphibians or their aquarium environment.</p>

<h2>Are axolotls poisonous?</h2>
<p><strong>There is no established pet-husbandry hazard in which touching an axolotl poisons a person through its skin.</strong> That does not make unnecessary handling a good idea: axolotl skin and slime coat are delicate, so frequent touching can harm the animal even when it is not a poisoning risk to the owner.</p>
<p>Use <a href="/care-basics/handling/">the axolotl handling guide</a> for situations where an animal genuinely needs to be moved.</p>

<h2>Are axolotls venomous?</h2>
<p><strong>Axolotls are not treated as venomous salamanders in standard pet or species references.</strong> Venom requires a biological system that delivers toxin into another animal, such as through specialized teeth, spines or stingers. Axolotl oral anatomy is adapted to grip and suction-feed on prey, not to inject venom.</p>
<p>For the teeth and feeding structures themselves, see <a href="/biology-and-science/anatomy-gills-and-lungs/">axolotl anatomy</a>.</p>

<h2>Can an axolotl bite hurt you?</h2>
<p>An axolotl may snap at a finger during feeding or when it mistakes movement for prey. The bite is not a venom exposure. Any animal bite can still break or irritate skin, and aquarium water can contain bacteria, so clean a wound rather than dismissing it simply because the animal is small.</p>

<h2>Can you get sick from touching an axolotl?</h2>
<p><strong>Yes, infection risk is possible through the same route that applies to other amphibians: germs on the animal or in its environment can reach your mouth, food or an open wound.</strong> The CDC states that amphibians can carry <em>Salmonella</em> even when they appear healthy and clean.</p>
<p>Wash hands with soap and running water after contact with the axolotl, its food, feces, equipment or tank water. Do not clean aquarium equipment in food-preparation areas.</p>

<h2>Can axolotl tank water carry germs?</h2>
<p>Yes. The CDC specifically includes aquarium water and habitat equipment in its amphibian-hygiene guidance. You do not have to hold the animal for exposure to occur; tank water, decorations, tools and waste can all become contaminated.</p>
<p>Keep dedicated buckets and aquarium tools separate from kitchen equipment and wash hands after maintenance.</p>

<h2>Who should be extra careful around amphibians?</h2>
<p>The CDC identifies children under 5, adults 65 and older, and people with weakened immune systems as groups at higher risk of serious illness from germs reptiles and amphibians can carry. The CDC advises that children younger than 5 should not handle or touch amphibians or their environments.</p>
<p>For family-specific ownership questions, see <a href="/care-basics/axolotls-and-children/">are axolotls good pets for kids?</a>.</p>

<h2>What should you do after an axolotl bite?</h2>
<ol>
<li>Rinse and wash the area promptly with warm soapy water.</li>
<li>Do not put aquarium water or unclean equipment on the wound.</li>
<li>Watch for increasing redness, warmth, swelling, pain or drainage.</li>
<li>Seek medical attention for a serious wound or signs of infection, and follow the CDC's bite/scratch guidance for higher-risk individuals.</li>
</ol>
<p>The goal is ordinary wound hygiene, not antivenom or “detox” treatment.</p>

<h2>Is it safe to pet or hold an axolotl?</h2>
<p><strong>Routine petting is unnecessary and can be harder on the axolotl than on the person.</strong> Axolotls are best treated as observation-focused aquatic pets. If you must move one for veterinary care, quarantine or tank safety, minimize contact and use the least stressful transfer method available.</p>

<h2>Axolotl danger myths vs real risks</h2>
<div class="table-wrap"><table>
<thead><tr><th>Claim</th><th>Better interpretation</th></tr></thead>
<tbody>
<tr><td>“Axolotls are poisonous to touch”</td><td>No established poisoning hazard from normal pet contact; handling should still be minimized for the animal.</td></tr>
<tr><td>“An axolotl bite injects venom”</td><td>Axolotls are not treated as venomous; use ordinary bite/wound hygiene.</td></tr>
<tr><td>“The tank is harmless if the animal looks healthy”</td><td>Healthy amphibians and their environments can still carry germs such as Salmonella.</td></tr>
<tr><td>“Kids can handle them if they are gentle”</td><td>CDC advises children under 5 not to touch amphibians or their environments; older children still need hygiene and supervision.</td></tr>
</tbody></table></div>

<h2>Sources</h2>
<ul>
<li><a href="https://www.cdc.gov/healthy-pets/about/reptiles-and-amphibians.html">CDC: Reptiles and Amphibians, updated January 13, 2026</a></li>
<li><a href="https://animaldiversity.org/accounts/Ambystoma_mexicanum/">Animal Diversity Web: Ambystoma mexicanum</a></li>
<li><a href="/biology-and-science/anatomy-gills-and-lungs/">MyAxolotl: Axolotl Anatomy — Gills, Lungs, Teeth & Body Parts</a></li>
</ul>
''',
        "featured": False,
    },

    "biology-and-science/axolotl-history-discovery": {
        "slug": "biology-and-science/axolotl-history-discovery",
        "hub": "biology-and-science",
        "title": "When Were Axolotls Discovered? History & Scientific Discovery",
        "title_tag": "When Were Axolotls Discovered? History & Scientific Discovery",
        "meta": "Trace axolotl history from Nahua knowledge and the 1798 scientific description to the Paris colony, neoteny research and modern laboratory populations.",
        "intro": "There is no single honest date when humans 'discovered' axolotls: people in the Valley of Mexico knew and named them long before European taxonomy. If the question means formal scientific description, Shaw and Nodder described Gyrinus mexicanus in 1798, the name on which today's Ambystoma mexicanum is based.",
        "num": 223,
        "date_published": "2026-09-18",
        "date_modified": "2026-09-18",
        "headings": [
            "When were axolotls discovered?",
            "Who knew axolotls before European science?",
            "What happened in 1798?",
            "What did Humboldt and Cuvier contribute?",
            "When did living axolotls reach Europe?",
            "How did Duméril change axolotl science?",
            "How did axolotls become laboratory animals?",
            "Why is 1863 vs 1864 sometimes confusing?",
            "Axolotl history timeline",
            "Sources",
        ],
        "body": r'''
<p><strong>No single scientist “discovered” axolotls.</strong> The animal was already known, named and used by peoples of the Valley of Mexico long before European zoologists assigned it a Latin scientific name. The clean historical distinction is between Indigenous/local knowledge and later formal scientific description.</p>

<h2>When were axolotls discovered?</h2>
<p>If <em>discovered</em> means “formally described in European zoological literature,” the key date is <strong>1798</strong>. The American Museum of Natural History's Amphibian Species of the World lists <em>Gyrinus mexicanus</em> Shaw and Nodder, 1798 as the original combination for the species now called <em>Ambystoma mexicanum</em>.</p>
<p>That date should not be rewritten as “humans first found axolotls in 1798.” It marks a taxonomic publication, not the beginning of human knowledge of the animal.</p>

<h2>Who knew axolotls before European science?</h2>
<p>Axolotls were part of the natural and cultural landscape of central Mexico long before modern taxonomy. Their name derives from Nahuatl, and historical Mexican sources document food, medicinal and cultural associations. That earlier knowledge belongs to the species' history even though it did not use the later Linnaean taxonomic system.</p>

<h2>What happened in 1798?</h2>
<p>George Shaw and Frederick Polydore Nodder published the species under the name <em>Gyrinus mexicanus</em>. Modern taxonomic databases retain Shaw and Nodder, 1798 in the author citation for <em>Ambystoma mexicanum</em>, showing the continuity between the original description and the current valid name.</p>
<p>Later authors moved the species through several genera and combinations before <em>Ambystoma mexicanum</em> became the accepted name.</p>

<h2>What did Humboldt and Cuvier contribute?</h2>
<p>At the beginning of the 19th century, Alexander von Humboldt sent preserved Mexican axolotl specimens to Georges Cuvier in Paris. With only preserved material, European anatomists debated whether the strange gilled animal was a larval salamander or an adult form.</p>
<p>That debate became much easier to investigate once living axolotls reached Paris decades later.</p>

<h2>When did living axolotls reach Europe?</h2>
<p><strong>Historical sources place the first major living shipment in Paris at the transition between late 1863 and 1864.</strong> The Muséum national d'Histoire naturelle describes the Jardin des Plantes as receiving axolotls in 1863, while modern histories of laboratory axolotls often use 1864 for the arrival and scientific study of the living animals.</p>
<p>A detailed historical review reports that 34 living Mexican axolotls were brought from Mexico to Europe, with six animals going to Auguste Duméril at the Paris museum. Those animals and their descendants transformed the axolotl from an anatomical curiosity into an experimental organism.</p>

<h2>How did Duméril change axolotl science?</h2>
<p>Auguste Duméril observed that axolotls could reproduce while retaining their gilled aquatic form. Later, some descendants underwent metamorphic change. These observations forced zoologists to rethink the simple assumption that a permanently gilled animal must be an immature larva.</p>
<p>Duméril also experimented with the animals and reported regeneration after gill removal, helping launch the long history of axolotl regeneration research.</p>

<h2>How did axolotls become laboratory animals?</h2>
<p>The Paris animals bred readily and were distributed to other laboratories, zoos and private keepers. A historical review of axolotl research describes the species as one of the oldest self-sustaining laboratory animals, with major roles in developmental biology, embryology, endocrinology and later regeneration research.</p>
<p>Modern captive research stocks have a complex history, so “all pet axolotls descend from exactly six animals” is too simplistic. The 19th-century Paris lineage is foundational, but later laboratory and breeding histories include additional stock management and crosses.</p>

<h2>Why is 1863 vs 1864 sometimes confusing?</h2>
<p>Different sources date different parts of the same transfer. Some describe the animals reaching the Paris institution in late 1863; scientific histories often mark 1864 as the point when the first living Mexican axolotls entered the museum research context. The disagreement is therefore usually about which step of the transfer is being dated, not whether living axolotls reached Paris in that period.</p>

<h2>Axolotl history timeline</h2>
<div class="table-wrap"><table>
<thead><tr><th>Period</th><th>Event</th></tr></thead>
<tbody>
<tr><td>Before European taxonomy</td><td>Axolotls were already known and named in the Valley of Mexico.</td></tr>
<tr><td>1798</td><td>Shaw and Nodder formally described <em>Gyrinus mexicanus</em>.</td></tr>
<tr><td>Early 1800s</td><td>Humboldt sent preserved specimens to Cuvier in Paris.</td></tr>
<tr><td>1863–1864</td><td>Living axolotls from Mexico reached Paris and entered sustained scientific study.</td></tr>
<tr><td>1860s onward</td><td>Duméril studied reproduction, metamorphosis and regeneration; captive colonies spread through Europe.</td></tr>
<tr><td>20th–21st centuries</td><td>Axolotls became major experimental models for development, genetics and regeneration.</td></tr>
</tbody></table></div>

<h2>Sources</h2>
<ul>
<li><a href="https://amphibiansoftheworld.amnh.org/Amphibia/Caudata/Ambystomatidae/Ambystoma/Ambystoma-mexicanum">American Museum of Natural History: Amphibian Species of the World — Ambystoma mexicanum</a></li>
<li><a href="https://pmc.ncbi.nlm.nih.gov/articles/PMC9117742/">Reiß: Cut and Paste — the long history of axolotl regeneration research</a></li>
<li><a href="https://pubmed.ncbi.nlm.nih.gov/25920413/">Reiß, Olsson & Hoßfeld: 150 years of axolotl research</a></li>
<li><a href="https://www.mnhn.fr/fr/axolotl">Muséum national d'Histoire naturelle: Axolotl</a></li>
</ul>
''',
        "featured": False,
    },

    "biology-and-science/axolotl-adaptations": {
        "slug": "biology-and-science/axolotl-adaptations",
        "hub": "biology-and-science",
        "title": "Axolotl Adaptations: How They Feed, Breathe & Survive Underwater",
        "title_tag": "Axolotl Adaptations: Feeding, Breathing & Aquatic Survival",
        "meta": "Learn how external gills, a finned tail, lateral-line sensing, suction feeding and paedomorphosis support the axolotl's permanently aquatic life.",
        "intro": "Axolotls are built for a permanently aquatic life. Their most defensible aquatic adaptations and retained traits include paedomorphosis, external gills, a finned tail, mechanosensory lateral-line organs and suction feeding.",
        "num": 224,
        "date_published": "2026-09-18",
        "date_modified": "2026-09-18",
        "headings": [
            "What adaptations do axolotls have?",
            "How does paedomorphosis support aquatic life?",
            "How do external gills help axolotls breathe?",
            "How does the tail help an axolotl swim?",
            "How does the lateral line help an axolotl sense water movement?",
            "What adaptations do axolotls have for feeding?",
            "How does suction feeding work?",
            "Is regeneration an axolotl habitat adaptation?",
            "How do these traits fit Xochimilco?",
            "Adaptation vs anatomy vs husbandry",
            "Sources",
        ],
        "body": r'''
<p><strong>The clearest axolotl adaptations for aquatic life are a permanently aquatic developmental strategy, external gills, a finned tail, specialized water-sensing organs and suction feeding.</strong> These traits work together: the animal remains in water, exchanges gases through aquatic respiratory surfaces, detects movement around its body and rapidly draws prey into the mouth.</p>

<h2>What adaptations do axolotls have?</h2>
<div class="table-wrap"><table>
<thead><tr><th>Adaptation or retained trait</th><th>Function</th></tr></thead>
<tbody>
<tr><td>Paedomorphosis / neoteny</td><td>Allows reproductive adulthood while retaining an aquatic body plan.</td></tr>
<tr><td>External gills</td><td>Provide large exposed respiratory surfaces for gas exchange in water.</td></tr>
<tr><td>Finned tail</td><td>Supports propulsion and maneuvering underwater.</td></tr>
<tr><td>Lateral-line neuromasts</td><td>Mechanoreceptors detect water movement around the head and body.</td></tr>
<tr><td>Suction feeding</td><td>Rapid expansion of the mouth/throat region pulls prey and water inward.</td></tr>
</tbody></table></div>

<h2>How does paedomorphosis support aquatic life?</h2>
<p>Axolotls become reproductively mature without completing the usual terrestrial metamorphosis of many salamanders. A 2026 review treats axolotl neoteny as an evolutionary life-history strategy rather than simply “failed development.” By retaining larval features into adulthood, the species keeps the structures associated with its aquatic mode of life.</p>
<p>For the developmental mechanism, see <a href="/biology-and-science/neoteny/">neoteny</a> and <a href="/biology-and-science/metamorphosis/">axolotl metamorphosis</a>.</p>

<h2>How do external gills help axolotls breathe?</h2>
<p>Feathery external gills expose a large respiratory surface directly to the surrounding water. Axolotls also use skin and simple lungs, so breathing is not an “external gills only” system. The retained gills are nevertheless one of the most visible features of the aquatic adult body plan.</p>
<p>For respiratory anatomy, use <a href="/biology-and-science/anatomy-gills-and-lungs/">gills, lungs and skin anatomy</a>.</p>

<h2>How does the tail help an axolotl swim?</h2>
<p>The tail retains a broad fin associated with the larval aquatic form. Side-to-side body and tail movement provides propulsion, while the limbs contribute to positioning and slow movement along the bottom. The result is a body better suited to submerged movement than to a terrestrial salamander lifestyle.</p>

<h2>How does the lateral line help an axolotl sense water movement?</h2>
<p>Axolotls possess superficial lateral-line neuromasts on the head and trunk. These are mechanoreceptive organs that respond to water movement. Anatomical studies describe multiple lines of neuromasts and specialized innervation across the head and body.</p>
<p>This sensory system matters underwater because visual information is only one source of environmental information. Water movement can help an aquatic predator detect nearby movement even in dim or complex habitat.</p>

<h2>What adaptations do axolotls have for feeding?</h2>
<p><strong>Suction feeding is the best-supported feeding adaptation in the keyword cluster.</strong> Axolotls do not need to chase and chew prey like a terrestrial mammal. Instead, rapid expansion of the oral and throat region creates water flow that draws prey into the mouth.</p>

<h2>How does suction feeding work?</h2>
<p>A 2025 kinematic study found suction feeding in axolotl larvae, juveniles and adults. The timing and speed of jaw and hyoid movement change with size, but the basic feeding mode persists across development.</p>
<p>The small teeth help grip prey once it enters the mouth; they are not the main mechanism for capturing it. See <a href="/biology-and-science/anatomy-gills-and-lungs/">axolotl teeth and oral anatomy</a> for the structures.</p>

<h2>Is regeneration an axolotl habitat adaptation?</h2>
<p><strong>Do not automatically label every famous axolotl trait a Xochimilco adaptation.</strong> Regeneration is a remarkable biological capacity, but the sources used here do not establish limb regeneration specifically as an adaptation to modern Xochimilco canal conditions. It is better covered as a regeneration trait with its own evolutionary and developmental questions.</p>
<p>See <a href="/biology-and-science/regeneration-and-limb-regrowth/">axolotl regeneration</a>.</p>

<h2>How do these traits fit Xochimilco?</h2>
<p>Wild axolotls persist in a freshwater canal-and-wetland environment with shallow vegetated water. A permanently aquatic body plan, water-breathing structures, a swimming tail, water-motion sensing and suction feeding are all coherent with life in that setting.</p>
<p>For the place itself—range, canals, water type and threats—use <a href="/biology-and-science/wild-habitat-xochimilco/">the Xochimilco habitat guide</a>.</p>

<h2>Adaptation vs anatomy vs husbandry</h2>
<p>This page owns the function question: <em>what traits help an axolotl live and feed underwater?</em></p>
<ul>
<li><strong>What body part is this?</strong> → <a href="/biology-and-science/anatomy-gills-and-lungs/">Anatomy</a></li>
<li><strong>Where do wild axolotls live?</strong> → <a href="/biology-and-science/wild-habitat-xochimilco/">Wild Habitat</a></li>
<li><strong>How should I build a pet tank?</strong> → <a href="/tank-setup/setup-guide/">Tank Setup</a></li>
<li><strong>How can they regrow limbs?</strong> → <a href="/biology-and-science/regeneration-and-limb-regrowth/">Regeneration</a></li>
</ul>

<h2>Sources</h2>
<ul>
<li><a href="https://pubmed.ncbi.nlm.nih.gov/42489940/">Mussies (2026): Neoteny and Evolutionary Strategy</a></li>
<li><a href="https://pmc.ncbi.nlm.nih.gov/articles/PMC12309904/">Toussaint-Larde et al. (2025): suction-feeding kinematics through axolotl development</a></li>
<li><a href="https://pubmed.ncbi.nlm.nih.gov/1484121/">Northcutt et al.: distribution and innervation of axolotl lateral-line organs</a></li>
<li><a href="https://pubmed.ncbi.nlm.nih.gov/29879797/">Smith, Lannoo & Armstrong: lateral-line neuromast development</a></li>
</ul>
''',
        "featured": False,
    },
})

HERO_IMAGE_OVERRIDES.update({
    "care-basics/are-axolotls-poisonous": {
        "file": "are-axolotls-poisonous-safety.webp",
        "alt": "Axolotl aquarium with not venomous, bites are uncommon and wash-hands safety guidance",
        "caption": "Axolotls are not generally treated as poisonous or venomous pets; practical human safety centers on hygiene, bite care and limiting unnecessary handling.",
        "description": "Axolotl human-safety graphic emphasizing observation, hygiene and minimal handling.",
        "credit": "MyAxolotl original graphic",
        "width": 1600, "height": 900,
    },
    "biology-and-science/axolotl-history-discovery": {
        "file": "axolotl-history-discovery.webp",
        "alt": "Axolotl in a Xochimilco and science-history collage used to illustrate its cultural and research history",
        "caption": "Axolotls were known in Mexico long before their 1798 formal scientific description; living animals reached Paris in the 1863–64 period and helped launch modern laboratory research.",
        "description": "Axolotl history graphic connecting Xochimilco, taxonomy and scientific research.",
        "credit": "MyAxolotl original graphic",
        "width": 1600, "height": 900,
    },
    "biology-and-science/axolotl-adaptations": {
        "file": "axolotl-aquatic-adaptations.webp",
        "alt": "Wild-type axolotl in Xochimilco illustrating aquatic adaptations including gills, tail, sensing and suction feeding",
        "caption": "Axolotl aquatic adaptations include paedomorphosis, external gills, a finned tail, lateral-line sensing and suction feeding.",
        "description": "Xochimilco axolotl graphic used to explain aquatic survival and feeding adaptations.",
        "credit": "MyAxolotl original graphic",
        "width": 1600, "height": 900,
    },
})

LINKING.update({
    "care-basics/are-axolotls-poisonous": [
        "care-basics/handling",
        "care-basics/axolotls-and-children",
        "biology-and-science/anatomy-gills-and-lungs",
        "health/finding-an-exotic-vet",
    ],
    "biology-and-science/axolotl-history-discovery": [
        "care-basics/axolotl-facts",
        "biology-and-science/wild-habitat-xochimilco",
        "biology-and-science/neoteny",
        "biology-and-science/regeneration-and-limb-regrowth",
    ],
    "biology-and-science/axolotl-adaptations": [
        "biology-and-science/wild-habitat-xochimilco",
        "biology-and-science/anatomy-gills-and-lungs",
        "biology-and-science/neoteny",
        "biology-and-science/regeneration-and-limb-regrowth",
    ],
})


# Persisted article dates: the 106 DOCX-backed pages first appeared in the
# launch commit, and the two config-authored pages first appeared later in the
# same public repo history.
DOCX_ARTICLE_DATE_PUBLISHED = "2026-08-22"
DOCX_ARTICLE_DATE_MODIFIED = DOCX_ARTICLE_DATE_PUBLISHED
CONFIG_ARTICLE_DATE_PUBLISHED = "2026-08-22"
CONFIG_ARTICLE_DATE_MODIFIED = CONFIG_ARTICLE_DATE_PUBLISHED


def _stamp_article_dates(entries, published, modified=None, published_source=None, modified_source=None):
    modified = modified or published
    for cfg in entries.values():
        cfg.setdefault("date_published", published)
        cfg.setdefault("date_modified", modified)
        if published_source is not None:
            cfg.setdefault("date_published_source", published_source)
        if modified_source is not None:
            cfg.setdefault("date_modified_source", modified_source)



# Move three now-distinct keyword intents out of broader parent pages.
BODY_TEXT_REPLACEMENTS.setdefault("care-basics/axolotls-and-children", []).append((
    "<h2>Are axolotls poisonous or venomous?</h2>\n<p><strong>No—pet axolotls are not generally considered poisonous or venomous to people.</strong> The practical human-health concern is not toxin injection or poisoning; it is hygiene around an amphibian and its aquarium water. The CDC notes that reptiles and amphibians can carry <em>Salmonella</em> even when they look healthy, and the germs can spread from the animal, tank water, equipment, and other habitat surfaces.</p>\n<div class=\"table-wrap\"><table>\n<thead><tr><th>Question</th><th>Practical answer</th></tr></thead>\n<tbody>\n<tr><td>Are axolotls venomous?</td><td>No known venom-delivery hazard is part of normal axolotl contact or bites.</td></tr>\n<tr><td>Are axolotls poisonous to touch?</td><td>They are not treated as a poisoning hazard in normal pet husbandry. Handling should still be minimized because it can harm the axolotl's delicate skin.</td></tr>\n<tr><td>What is the main human-health risk?</td><td>Germs associated with amphibians and aquarium water, especially <em>Salmonella</em>.</td></tr>\n<tr><td>What should families do?</td><td>Wash hands with soap and running water after tank contact, keep aquarium equipment away from food-preparation areas, and supervise children.</td></tr>\n</tbody></table></div>\n<p>The CDC advises that children younger than 5 should not handle or touch reptiles or amphibians or their environments because they are at higher risk of serious illness from germs such as <em>Salmonella</em>. For older children, observation is safer for the animal than routine handling, and adults should supervise tank maintenance and handwashing.</p>\n<p><strong>Sources:</strong> <a href=\"https://www.cdc.gov/healthy-pets/about/reptiles-and-amphibians.html\">CDC: Reptiles and Amphibians</a>; <a href=\"https://www.fda.gov/animal-veterinary/animal-health-literacy/salmonella-feeder-rodents-and-pet-reptiles-and-amphibians-tips-you-should-know-prevent-infection\">FDA: Salmonella, Reptiles and Amphibians</a>; <a href=\"https://www.worldwildlife.org/resources/explainers/should-you-keep-an-exotic-animal-as-a-pet-this-guide-can-help-you-tell/\">WWF: Responsible Exotic Pet Guide</a>.</p>",
    '<h2>Are axolotls poisonous or venomous?</h2><p><strong>Axolotls are not generally treated as poisonous or venomous pets.</strong> The more important family-safety issue is hygiene around amphibians and aquarium water. See <a href="/care-basics/are-axolotls-poisonous/">axolotl poison, venom, bite and human-safety guidance</a> for the full answer.</p>'
))
BODY_TEXT_REPLACEMENTS.setdefault("care-basics/axolotl-facts", []).append((
    "<h2>When were axolotls discovered?</h2>\n<p><strong>There is no single human \"discovery\" date for the axolotl.</strong> Nahua peoples in the Valley of Mexico knew and named the animal long before European zoological taxonomy. If the question means \"when was the axolotl formally described by science?\", the key date is <strong>1798</strong>, when George Shaw and Frederick Polydore Nodder described it as <em>Gyrinus mexicanus</em>, the name on which today's <em>Ambystoma mexicanum</em> is based.</p>\n<div class=\"table-wrap\"><table>\n<thead><tr><th>Period</th><th>What happened</th><th>Why it matters</th></tr></thead>\n<tbody>\n<tr><td>Pre-Hispanic and colonial Mexico</td><td>The axolotl was already known in Nahua culture; colonial-era natural-history accounts included descriptions of the animal.</td><td>Its human history begins well before European scientific naming.</td></tr>\n<tr><td>1798</td><td>George Shaw and Frederick Polydore Nodder formally described <em>Gyrinus mexicanus</em>.</td><td>This is the clearest date for the species' formal scientific description.</td></tr>\n<tr><td>Early 1800s</td><td>Alexander von Humboldt sent preserved Mexican axolotl specimens to Georges Cuvier in Paris.</td><td>European anatomists began debating whether the gilled animal was a larva or an adult form.</td></tr>\n<tr><td>1863–1864</td><td>Living axolotls were shipped from Mexico to Paris; historical sources date the shipment to 1863 and their arrival and early study to 1864.</td><td>Those animals helped establish the long-running laboratory lineage and research on neoteny.</td></tr>\n</tbody></table></div>\n<h3>Who discovered axolotls?</h3>\n<p><strong>No single scientist can accurately be called the discoverer of axolotls.</strong> The animal was already known in Mexico. Shaw and Nodder are credited with the 1798 formal scientific description; Humboldt later brought preserved specimens to the attention of Cuvier and European naturalists.</p>\n<h3>Where did axolotls come from?</h3>\n<p><strong>Axolotls are native to the lake system of the Valley of Mexico, especially Xochimilco and historically Lake Chalco.</strong> Their surviving wild range is now restricted to Xochimilco. See the <a href=\"/biology-and-science/wild-habitat-xochimilco/\">Xochimilco habitat guide</a> for the modern range and habitat conditions.</p>\n<p><strong>Sources:</strong> <a href=\"https://amphibiansoftheworld.amnh.org/Amphibia/Caudata/Ambystomatidae/Ambystoma/Ambystoma-mexicanum\">American Museum of Natural History: Amphibian Species of the World</a>; <a href=\"https://ru.historicas.unam.mx/handle/20.500.12525/9239\">UNAM Instituto de Investigaciones Históricas: El axólotl</a>; <a href=\"https://pubmed.ncbi.nlm.nih.gov/25920413/\">Reiß, Olsson &amp; Hoßfeld: 150 years of axolotl research</a>; <a href=\"https://ambystoma.uky.edu/genetic-stock-center/about.php\">University of Kentucky Ambystoma Genetic Stock Center</a>.</p>",
    '<h2>When were axolotls discovered?</h2><p><strong>Axolotls were known in Mexico long before European taxonomy; 1798 is the key date for their formal scientific description by Shaw and Nodder.</strong> For the full timeline from Nahua knowledge through Humboldt, Cuvier, Paris and the rise of laboratory axolotls, see <a href="/biology-and-science/axolotl-history-discovery/">axolotl history and scientific discovery</a>.</p>'
))
BODY_TEXT_REPLACEMENTS.setdefault("biology-and-science/wild-habitat-xochimilco", []).append((
    "<h2>What adaptations help axolotls survive in Xochimilco?</h2>\n<p><strong>Axolotls are adapted to a permanently aquatic life: they mature without losing larval features such as external gills and a finned tail, and they combine aquatic sensing and suction feeding with that body plan.</strong> In evolutionary biology this retention of juvenile traits into reproductive adulthood is called paedomorphosis or neoteny.</p>\n<div class=\"table-wrap\"><table>\n<thead><tr><th>Adaptation or retained trait</th><th>How it supports aquatic life</th></tr></thead>\n<tbody>\n<tr><td>Paedomorphosis / neoteny</td><td>Adults remain aquatic instead of completing the usual salamander transition to a terrestrial form.</td></tr>\n<tr><td>External gills</td><td>Large feathery respiratory surfaces support gas exchange while the animal remains submerged.</td></tr>\n<tr><td>Finned tail</td><td>The retained larval-style tail fin supports swimming through shallow canal and lake habitat.</td></tr>\n<tr><td>Lateral-line system</td><td>Mechanoreceptive neuromasts detect water movement around the body; see the <a href=\"/biology-and-science/anatomy-gills-and-lungs/\">anatomy guide</a> for the sensory structures.</td></tr>\n<tr><td>Suction feeding</td><td>Axolotls rapidly expand the mouth and throat region to draw aquatic prey and water inward; research finds this feeding mode from larvae through adults.</td></tr>\n</tbody></table></div>\n<p>These are better-supported aquatic adaptations than generic lists that label every unusual axolotl feature as a habitat adaptation. Regeneration, for example, is a remarkable biological ability, but the sources reviewed here do not establish it as a specific adaptation to Xochimilco's modern canal conditions.</p>\n<p><strong>Sources:</strong> <a href=\"https://pmc.ncbi.nlm.nih.gov/articles/PMC28454/\">Voss &amp; Shaffer (1997): paedomorphosis as an adaptation for an aquatic life cycle</a>; <a href=\"https://animaldiversity.org/accounts/Ambystoma_mexicanum/\">Animal Diversity Web: development and aquatic traits</a>; <a href=\"https://pmc.ncbi.nlm.nih.gov/articles/PMC10999947/\">Lyons &amp; Arbuckle (2024): evolution of neoteny in <em>Ambystoma</em></a>; <a href=\"https://pmc.ncbi.nlm.nih.gov/articles/PMC12309904/\">Toussaint-Larde et al. (2025): suction-feeding kinematics through axolotl development</a>.</p>",
    '<h2>What adaptations help axolotls survive in Xochimilco?</h2><p><strong>Axolotls retain a permanently aquatic body plan with external gills and a finned tail, and they use lateral-line sensing and suction feeding underwater.</strong> See <a href="/biology-and-science/axolotl-adaptations/">axolotl adaptations</a> for the full functional explanation; this page stays focused on Xochimilco habitat and range.</p>'
))

# Minecraft Culture sub-pillar: keyword-reconciled, research-verified override.
# This intentionally overrides the external DOCX article at render time so the
# comprehensive Minecraft coverage survives future builds without creating a
# duplicate URL or changing the site's core topical architecture.
CONFIG_ARTICLES['axolotl-in-culture/minecraft-axolotls-guide'] = {
    "slug": 'axolotl-in-culture/minecraft-axolotls-guide',
    "num": 98,
    "hub": "axolotl-in-culture",
    "title": 'Minecraft Axolotls: Complete Guide',
    "title_tag": 'Minecraft Axolotls: Food, Breeding, Blue Axolotl & More',
    "meta": 'What do axolotls eat in Minecraft? Learn feeding, breeding, blue-axolotl odds, lush-cave spawning, taming, despawning, combat and commands.',
    "intro": 'Minecraft axolotls live in lush caves, breed with Buckets of Tropical Fish, cannot be tamed, and come in five colors. Blue axolotls do not spawn naturally: a baby has a 1-in-1,200 mutation chance, while a blue parent can also pass on its color.',
    "body": r'''<p><strong>Minecraft axolotls live in lush caves, breed with Buckets of Tropical Fish, cannot be tamed, and come in five colors.</strong> The rare blue variant is the exception: it does not spawn naturally, so survival players obtain it through breeding.</p>

<div class="table-wrap"><table>
<thead><tr><th>Question</th><th>Quick answer</th></tr></thead>
<tbody>
<tr><td>What do axolotls eat in Minecraft?</td><td>Use a <strong>Bucket of Tropical Fish</strong> to feed, lead, and breed them. The loose Tropical Fish item does not work for breeding.</td></tr>
<tr><td>Can you tame an axolotl?</td><td>No. You can catch one in a water bucket, lead it with a Bucket of Tropical Fish, and breed it, but there is no wolf-style tame state.</td></tr>
<tr><td>Where do they spawn?</td><td>Underwater in lush caves, with clay beneath the spawning water.</td></tr>
<tr><td>How rare is blue?</td><td>A bred baby has roughly a 1-in-1,200 blue-mutation chance; blue can also be inherited from a blue parent.</td></tr>
<tr><td>Do bucketed axolotls despawn?</td><td>Axolotls caught in a water bucket and released again are persistent and do not naturally despawn.</td></tr>
</tbody></table></div>

<h2>What do axolotls eat in Minecraft?</h2>
<p><strong>For player feeding, Minecraft axolotls use a Bucket of Tropical Fish, not the ordinary Tropical Fish item.</strong> Use the bucket on an adult axolotl to feed it. Hold the same item and nearby axolotls are tempted to follow you.</p>
<p>This distinction matters because killing or otherwise obtaining a loose tropical fish gives you a different item. To get the breeding food, scoop a living tropical fish into a water bucket. After the axolotl consumes the fish, the bucket becomes a water bucket again.</p>
<p>Axolotls also hunt aquatic mobs on their own. That natural hunting behavior is separate from the item used by the player to feed or breed them.</p>

<h2>How do you breed axolotls in Minecraft?</h2>
<p><strong>Feed two adult axolotls one Bucket of Tropical Fish each.</strong> When both enter love mode, they breed and produce a baby axolotl. In Java Edition the parents have a five-minute breeding cooldown; in Bedrock Edition the cooldown is one minute.</p>
<ol>
<li>Find or capture two adult axolotls.</li>
<li>Collect at least two Buckets of Tropical Fish.</li>
<li>Use one bucket on each adult.</li>
<li>Keep the adults close enough to reach each other.</li>
<li>Wait for the baby to appear.</li>
</ol>
<p>A baby normally takes about 20 minutes to become an adult. Buckets of Tropical Fish can also accelerate baby growth.</p>

<h2>How do you get a blue axolotl in Minecraft?</h2>
<p><strong>In normal survival play, breed axolotls.</strong> Since Java 1.17.1, blue axolotls do not spawn naturally. Breeding gives a baby roughly a <strong>1-in-1,200</strong> mutation chance to become blue; otherwise the baby normally inherits a parent's color.</p>
<p>Once you have a blue parent, inheritance changes the practical odds because a non-mutated baby can inherit that parent's blue color. Breeding two blue parents therefore produces blue offspring without waiting for another 1-in-1,200 mutation.</p>
<p>If you are searching lush caves for a naturally spawned blue axolotl, you can stop: the four naturally spawning colors are the ones to look for in the wild.</p>

<h2>Where do axolotls spawn in Minecraft?</h2>
<p><strong>Axolotls spawn underwater in lush caves where the spawning water has clay beneath it.</strong> Mojang moved axolotl spawning to this lush-cave rule in Java 1.18.</p>
<p>To find them efficiently, look for an azalea tree on the surface, which can indicate a lush cave below, then explore water pools around clay inside the cave. Bringing empty water buckets lets you capture an axolotl immediately, and a Bucket of Tropical Fish can draw one toward you if it is nearby but hard to see.</p>

<h2>What are the five Minecraft axolotl colors?</h2>
<p>Minecraft has five vanilla axolotl variants:</p>
<ol>
<li><strong>Leucistic (pink/lucy)</strong></li>
<li><strong>Wild (brown)</strong></li>
<li><strong>Gold</strong></li>
<li><strong>Cyan</strong></li>
<li><strong>Blue</strong></li>
</ol>
<p>Pink, brown, gold, and cyan can spawn naturally. Blue is the breeding-only rare variant in normal survival play. Current vanilla Minecraft does <strong>not</strong> have a green axolotl variant.</p>
<p>The game colors are inspired by real axolotl appearances but are not a one-to-one guide to real morphs. In particular, <a href="/morphs/blue-and-pink-axolotl-myth/">there is no true blue axolotl morph in real life</a>.</p>

<h2>Can you tame an axolotl in Minecraft?</h2>
<p><strong>No. Minecraft axolotls cannot be tamed.</strong> They do not gain an owner state, sit on command, or behave like tamed wolves and cats. Mojang's Bedrock release notes explicitly distinguish breeding from taming.</p>
<p>You can still keep one: catch it with a water bucket, release it into a suitable water enclosure, lead it with a Bucket of Tropical Fish, breed it, and take it into aquatic combat. Searching for a special taming food will not unlock a hidden tame mechanic.</p>

<h2>How do you catch an axolotl, and will it despawn?</h2>
<p><strong>Use a water bucket directly on the axolotl.</strong> This creates a Bucket of Axolotl that preserves the animal for transport. When you place it back into water, a bucket-caught axolotl is persistent and does not naturally despawn.</p>
<p>Naturally spawned axolotls that have not been made persistent can be subject to normal despawning behavior. If you are collecting colors or building a breeding pool, bucket each axolotl before moving it home rather than simply trying to herd wild spawns over a long distance.</p>

<h2>Can Minecraft axolotls breathe air or live on land?</h2>
<p><strong>They are amphibious, but they should be kept in water.</strong> Current Bedrock behavior data marks axolotls as able to breathe both water and air, yet it also gives them a drying-out timer of 300 seconds. After about five minutes out of water, an axolotl begins taking drying damage unless rain or water interrupts the timer.</p>
<p>That means an axolotl does not die on land because it instantly “drowns in air.” The practical danger is drying out. Build transport routes and enclosures so they can stay in water instead of relying on their short land tolerance.</p>

<h2>What do axolotls attack in Minecraft?</h2>
<p><strong>Axolotls are active aquatic predators.</strong> Current Bedrock behavior data targets the fish family, squid family, and tadpoles, plus drowned, guardians, and elder guardians. Frogs are not in that target list, so the game does not treat adult frogs as a normal axolotl prey target.</p>
<p>When you kill a mob that an axolotl is fighting, the axolotl can reward you with temporary Regeneration and remove Mining Fatigue. That interaction is why axolotls are especially useful around guardians and ocean monuments.</p>
<p>Axolotls can also play dead after taking damage, temporarily causing attackers to stop targeting them while the axolotl regenerates.</p>

<h2>What are the Minecraft axolotl summon commands?</h2>
<p>Commands require cheats or suitable operator permissions. The basic commands are:</p>
<div class="table-wrap"><table>
<thead><tr><th>Edition</th><th>Command</th><th>Result</th></tr></thead>
<tbody>
<tr><td>Java</td><td><code>/summon minecraft:axolotl ~ ~ ~</code></td><td>Summons an axolotl at your position.</td></tr>
<tr><td>Java — blue</td><td><code>/summon minecraft:axolotl ~ ~ ~ {Variant:4}</code></td><td>On current Java 26.x builds, variant value 4 is the blue axolotl.</td></tr>
<tr><td>Bedrock</td><td><code>/summon axolotl ~ ~ ~</code></td><td>Summons a normally generated axolotl.</td></tr>
</tbody></table></div>
<p><strong>What about a blue-axolotl command in Bedrock?</strong> Older guides commonly recommend <code>/summon axolotl ~ ~ ~ minecraft:entity_born</code>. Current Microsoft behavior documentation defines <code>minecraft:entity_born</code> as the event used when an axolotl is produced through breeding, not as a documented stable blue-variant selector. Because Bedrock spawn-event behavior is version-sensitive, we do not present that older shortcut as a guaranteed current blue command. For a reliable blue axolotl in normal Bedrock gameplay, use breeding; for commands, use the suggestions exposed by your installed version.</p>
<p>Command data formats are more version-sensitive than survival mechanics. Java's <code>Variant:4</code> syntax remains in current 26.x command references, but recheck command syntax after major technical updates.</p>

<h2>When were axolotls added to Minecraft?</h2>
<p><strong>Axolotls arrived with Caves &amp; Cliffs: Part I (1.17) in June 2021.</strong> Java 1.17.1 then made blue axolotls breeding-only, and Java 1.18 moved natural spawning to water in lush caves above clay blocks.</p>
<p>For this guide, the core mechanics were rechecked against the current 2026 Java/Bedrock release line and the current Bedrock vanilla behavior data. That matters because older 1.17 guides still repeat the original underground-water spawning rule that Mojang replaced in 1.18.</p>

<h2>How are Minecraft axolotls different from real axolotls?</h2>
<p>Minecraft gets several recognizable traits right: axolotls are aquatic salamanders, have feathery external gills, and occur in pale, gold, and dark-looking forms. But game mechanics are fictional. Real axolotls do not grant Regeneration, fight guardians, live in buckets, or come in a true blue morph.</p>
<p>If the game is what introduced you to the animal, use the <a href="/axolotls/care-guide/">real axolotl care guide</a> for husbandry and the <a href="/morphs/morphs-comparison-chart/">morph comparison</a> for real colors.</p>

<h2>Sources and version notes</h2>
<div class="references"><ul>
<li><a href="https://feedback.minecraft.net/hc/en-us/articles/4402626897165-Minecraft-Caves-Cliffs-Part-1-1-17-Java">Minecraft Java 1.17: Caves &amp; Cliffs Part I</a></li>
<li><a href="https://feedback.minecraft.net/hc/en-us/articles/4404449719949-Minecraft-Java-Edition-1-17-1">Minecraft Java 1.17.1</a></li>
<li><a href="https://feedback.minecraft.net/hc/en-us/articles/4415128577293-Minecraft-Java-Edition-1-18">Minecraft Java 1.18</a></li>
<li><a href="https://feedback.minecraft.net/hc/en-us/articles/4402427632013-Minecraft-Caves-Cliffs-Part-I-1-17-0-Bedrock">Minecraft Bedrock 1.17.0</a></li>
<li><a href="https://feedback.minecraft.net/hc/en-us/articles/48913133328013-Minecraft-Java-Edition-26-3">Minecraft Java Edition 26.3</a></li>
<li><a href="https://feedback.minecraft.net/hc/en-us/articles/48915928859789-Minecraft-Bedrock-Edition-26-51-Hotfix-Changelog">Minecraft Bedrock Edition 26.51</a></li>
<li><a href="https://learn.microsoft.com/en-us/minecraft/creator/reference/source/vanillabehaviorpack_snippets/entities/axolotl?view=minecraft-bedrock-stable">Microsoft Learn: current vanilla axolotl behavior data</a></li>
<li><a href="https://learn.microsoft.com/en-us/minecraft/creator/commands/commands/summon?view=minecraft-bedrock-stable">Microsoft Learn: /summon command</a></li>
</ul></div>''',
    "headings": [
        'What do axolotls eat in Minecraft?',
        'How do you breed axolotls in Minecraft?',
        'How do you get a blue axolotl in Minecraft?',
        'Where do axolotls spawn in Minecraft?',
        'What are the five Minecraft axolotl colors?',
        'Can you tame an axolotl in Minecraft?',
        'How do you catch an axolotl, and will it despawn?',
        'Can Minecraft axolotls breathe air or live on land?',
        'What do axolotls attack in Minecraft?',
        'What are the Minecraft axolotl summon commands?',
        'When were axolotls added to Minecraft?',
        'How are Minecraft axolotls different from real axolotls?',
        'Sources and version notes',
    ],
    "faq": [],
    "featured": False,
    "date_published": "2026-08-22",
    "date_modified": "2026-09-17",
}

# Correct a cross-page wording conflict discovered during the Minecraft audit:
# axolotls are bucketable and breedable in Minecraft, but are not tameable.
BODY_TEXT_REPLACEMENTS.setdefault(
    "axolotl-in-culture/why-axolotls-are-suddenly-popular", []
).append((
    "added axolotls as a tame, bucketable, endlessly cute mob",
    "added axolotls as bucketable, breedable aquatic mobs",
))

_stamp_article_dates(ARTICLES, DOCX_ARTICLE_DATE_PUBLISHED, DOCX_ARTICLE_DATE_MODIFIED,
                     published_source="git:924cb99")
_stamp_article_dates(CONFIG_ARTICLES, CONFIG_ARTICLE_DATE_PUBLISHED,
                     CONFIG_ARTICLE_DATE_MODIFIED, published_source="git:924cb99")

# Search action metadata (Phase 9-B): index entries that carry an explicit
# action button / route. Tools get their action automatically in build.py.
SEARCH_ACTIONS = {
    "health/emergency-first-aid": {"label": "Emergency first aid", "kind": "guide"},
    "health/finding-an-exotic-vet": {"label": "Find an exotic vet", "kind": "guide"},
}

# Author / publisher info (shown on articles, in schema)
AUTHOR = PEOPLE["author"]
EDITOR = PEOPLE["editor"]


# ---------------------------------------------------------------------------
# Canonical body rewrites — stress diagnostics + pop culture (2026-09-18)
# ---------------------------------------------------------------------------

BODY_OVERRIDES["health/stress-signs"] = r'''
<p><strong>No single posture or behavior proves that an axolotl is “stressed.”</strong> The useful approach is to notice a change from the animal's normal pattern, check the environment, and then follow the specialist guide for the specific sign. Appetite, gill condition, buoyancy, swimming, skin, posture and water-quality measurements all matter together.</p>

<h2>What are common axolotl stress or illness warning signs?</h2>
<p>Owners commonly notice changes such as forward-curled gills, an unusually curled tail tip, persistent abnormal floating, reduced appetite, frantic or abnormal swimming, shrinking or damaged gills, skin changes, wounds, or a marked change in activity. These observations are <strong>nonspecific</strong>: several different husbandry or medical problems can produce similar signs.</p>
<p>The Ambystoma Genetic Stock Center notes that poor husbandry and adverse environmental conditions increase vulnerability to disease, and identifies loss of appetite and gill deterioration as early illness signs. Veterinary amphibian guidance likewise recommends assessing appetite, water quality, temperature, posture, behavior, respiratory effort, equilibrium and fecal production rather than diagnosing from one visible feature.</p>

<h2>Which sign should you follow next?</h2>
<div class="table-wrap"><table>
<thead><tr><th>What you observe</th><th>What it can tell you</th><th>Best next guide</th></tr></thead>
<tbody>
<tr><td>Forward-curled gills or curled tail tip</td><td>A posture change worth checking against water, temperature, flow and recent disturbance; not a diagnosis by itself</td><td><a href="/health/curled-gills-stress-signal/">Curled gills & tail tip</a></td></tr>
<tr><td>Persistent floating, inability to sink, rolling or loss of equilibrium</td><td>Buoyancy or swimming abnormality that can have multiple causes</td><td><a href="/health/why-axolotl-floating/">Why is my axolotl floating?</a></td></tr>
<tr><td>Reduced or absent appetite</td><td>Can accompany husbandry problems, illness, gastrointestinal problems or normal feeding variation</td><td><a href="/health/refusing-to-eat/">Axolotl not eating</a></td></tr>
<tr><td>Shrinking or deteriorating gills</td><td>Gill-health change requiring water, flow, oxygenation and health review</td><td><a href="/health/shrinking-gills/">Shrinking gills</a></td></tr>
<tr><td>White or cotton-like growth</td><td>Possible surface growth; appearance alone does not confirm the organism</td><td><a href="/health/fungal-infections-saprolegnia/">Axolotl fungus</a></td></tr>
<tr><td>Swelling plus reduced appetite or suspected swallowed material</td><td>Possible gastrointestinal problem; impaction is only one possibility</td><td><a href="/health/impaction-symptoms-treatment/">Impaction symptoms</a></td></tr>
<tr><td>Bleeding, open wound, severe swelling, skin sloughing or rapid decline</td><td>Potentially urgent problem</td><td><a href="/health/emergency-first-aid/">Emergency signs & first aid</a></td></tr>
</tbody></table></div>

<h2>What should you check first?</h2>
<p><strong>Start with measurements and recent changes.</strong> A veterinarian evaluating an amphibian asks about diet and appetite, temperature, lighting, recent animal introductions, medications, disinfection practices and measured water quality. That same structure is useful at home before you guess at a diagnosis.</p>
<ol>
<li><strong>Measure the water temperature.</strong> Do not rely on how the tank feels to your hand.</li>
<li><strong>Test ammonia, nitrite, nitrate and pH.</strong> Record the actual numbers. Use <a href="/tank-setup/how-to-test-water/">how to test axolotl water</a> if you need the procedure.</li>
<li><strong>Review recent changes.</strong> New tank mate, filter, cleaning, décor, food, medication, move or power outage can matter.</li>
<li><strong>Check water flow and disturbance.</strong> AGSC notes that rapid circulation can be stressful; flow should not force an axolotl to constantly brace or move.</li>
<li><strong>Look at the whole animal.</strong> Appetite, body condition, gills, skin, posture, breathing effort, swimming and fecal production provide more context than one feature alone.</li>
</ol>

<h2>Do curled gills always mean stress?</h2>
<p><strong>No single gill position is a validated diagnostic test.</strong> A persistent or new forward curl can be a useful observation, especially when it appears with other changes, but it should lead to a husbandry and health check rather than an automatic conclusion such as “ammonia burn” or “high temperature.”</p>
<p>Use the <a href="/health/curled-gills-stress-signal/">curled-gills guide</a> for the more specific differential and escalation pathway.</p>

<h2>Is floating always a stress sign?</h2>
<p><strong>No.</strong> Brief surface visits or temporary buoyancy can occur without disease. Persistent inability to control position, rolling, upside-down floating, or loss of equilibrium is more concerning. Merck's amphibian examination guidance notes that abnormal swimming or inability to maintain equilibrium can indicate neurologic impairment, but other buoyancy and gastrointestinal problems can produce abnormal position too.</p>
<p>That is why the <a href="/health/why-axolotl-floating/">floating guide</a> owns the differential instead of this general stress page.</p>

<h2>Can water quality or temperature cause stress?</h2>
<p>Yes. Water quality and temperature are foundational axolotl husbandry variables, so they should be checked whenever behavior or appearance changes. AGSC emphasizes clean water, biological control of ammonia and nitrite in filtered systems, cool temperatures, and low flow. However, <strong>normal test results do not rule out illness</strong>, and an abnormal reading does not prove it is the only cause of the animal's signs.</p>
<p>Interpret numbers on <a href="/tank-setup/water-parameters-cycling/">Water Parameters & Nitrogen Cycle</a>, and use <a href="/tank-setup/temperature/">the temperature guide</a> for thermal management.</p>

<h2>What should you do after correcting a husbandry problem?</h2>
<p>Record the correction and keep watching the animal. Do not promise yourself that a sign must disappear within a fixed number of hours or days: recovery depends on the underlying cause, severity and whether there is concurrent disease or injury.</p>
<p>If the axolotl is worsening, has severe signs, cannot maintain normal position, has an open wound, marked swelling, skin sloughing, significant respiratory difficulty, or continues to decline despite corrected husbandry, seek an amphibian-experienced veterinarian. Use the <a href="/health/finding-an-exotic-vet/">axolotl vet guide</a> if needed.</p>

<h2>Stress signs vs normal behavior</h2>
<p>Normal resting, hiding, slow walking along the bottom and periods of inactivity belong on the <a href="/care-basics/behavior/">axolotl behavior guide</a>. This page is a health-routing page for <em>changes that concern the owner</em>. Keeping that boundary prevents normal behavior from being mislabeled as disease and prevents a genuinely abnormal sign from being dismissed as “just stress.”</p>

<h2>Sources</h2>
<ul>
<li><a href="https://www.merckvetmanual.com/exotic-and-laboratory-animals/amphibians/clinical-techniques-in-amphibians">Merck Veterinary Manual: Clinical Techniques in Amphibians, updated February 2026</a></li>
<li><a href="https://www.merckvetmanual.com/exotic-and-laboratory-animals/amphibians/environment-and-husbandry-for-amphibians">Merck Veterinary Manual: Environment and Husbandry for Amphibians</a></li>
<li><a href="https://ambystoma.uky.edu/education1/guide-to-axolotl-husbandry">Ambystoma Genetic Stock Center: Guide to Axolotl Husbandry</a></li>
</ul>
'''

BODY_OVERRIDES["axolotl-in-culture/axolotl-in-pop-culture-and-memes"] = r'''
<p><strong>Axolotls appear in modern games, animation fandom, literature, memes, merchandise and science media.</strong> Minecraft is the most obvious mass-market example, but the animal also has a much older literary presence in Julio Cortázar's “Axolotl” and a recurring connection to the mythology surrounding Bill Cipher in <em>Gravity Falls</em>.</p>
<div class="role-note"><strong>This page owns cultural appearances.</strong> For the separate question of why public interest accelerated, read <a href="/axolotl-in-culture/why-axolotls-are-suddenly-popular/">why axolotls became so popular</a>. For game mechanics, use the <a href="/axolotl-in-culture/minecraft-axolotls-guide/">Minecraft axolotl guide</a>.</div>

<h2>Where do axolotls appear in pop culture?</h2>
<div class="table-wrap"><table>
<thead><tr><th>Medium</th><th>Example</th><th>Why the axolotl matters</th></tr></thead>
<tbody>
<tr><td>Video games</td><td>Minecraft</td><td>Axolotls became an interactive mob in Caves & Cliffs Part I in June 2021.</td></tr>
<tr><td>Animation / fandom</td><td>Gravity Falls</td><td>The word “AXOLOTL” and an Axolotl figure are tied to Bill Cipher lore across the finale-era puzzle/fandom material and later franchise books.</td></tr>
<tr><td>Literature</td><td>Julio Cortázar, “Axolotl”</td><td>The narrator becomes obsessively identified with axolotls at the Jardin des Plantes in Paris.</td></tr>
<tr><td>Internet culture</td><td>Memes, reaction images, short videos</td><td>The face, external gills and still posture are easy to anthropomorphize.</td></tr>
<tr><td>Merchandise</td><td>Plush toys, apparel, figures and gifts</td><td>The simplified “smiling axolotl” silhouette transfers easily to character design.</td></tr>
<tr><td>Science media</td><td>Regeneration and genome research</td><td>Scientific coverage keeps the real animal visible beyond entertainment.</td></tr>
</tbody></table></div>

<h2>When did Minecraft add axolotls?</h2>
<p><strong>Minecraft added axolotls in Caves & Cliffs Part I in June 2021.</strong> Mojang's own retrospective says Part I added axolotls, goats and glow squid to the Overworld, and its later “Taking Inventory” article confirms that axolotls entered Minecraft in the first part of Caves & Cliffs.</p>
<p>Mojang was already publishing axolotl fan art before release, which shows that the creature was part of the update's community identity before players could encounter it in the finished game. The game uses five color variants and fictional mechanics; those variants should not be treated as a guide to real axolotl morph genetics.</p>
<p>For spawning, feeding, breeding, blue-variant odds, bucket persistence and commands, use <a href="/axolotl-in-culture/minecraft-axolotls-guide/">Minecraft Axolotls: Complete Guide</a>. For build ideas, use <a href="/axolotl-in-culture/minecraft-axolotl-enclosure-builds/">Minecraft axolotl enclosure builds</a>.</p>

<h2>What is the Gravity Falls axolotl connection?</h2>
<p><strong>The axolotl is part of the Bill Cipher mythology that fans follow across <em>Gravity Falls</em> and related books.</strong> Fan reference documentation records that Bill's final reversed speech in the series includes the word “AXOLOTL,” and later franchise material develops an Axolotl figure connected with Bill's fate.</p>
<p>Disney's official publishing catalog confirms that Alex Hirsch's <em>The Book of Bill</em> continues Bill Cipher's story and lore after the television series. Because some details of the Axolotl connection come through ciphers, bonus material and later books, this page separates the basic documented connection from fan theories about what it ultimately means.</p>
<p><strong>What we should not do:</strong> present a fan theory about the Axolotl as a confirmed biological or mythological explanation for the real animal. The fictional character and the real salamander are separate subjects.</p>

<h2>What is Julio Cortázar's “Axolotl”?</h2>
<p><strong>“Axolotl” is a short story by Argentine writer Julio Cortázar, first published in 1956.</strong> Literary reference sources describe a narrator who repeatedly watches axolotls at the Jardin des Plantes in Paris until the boundary between human observer and animal becomes unstable.</p>
<p>The story made the axolotl a literary image decades before modern games and social media. It is therefore useful evidence that the animal's cultural appeal did not begin with Minecraft.</p>

<h2>Why do axolotls work so well as characters and memes?</h2>
<p>Several visible traits make the animal easy to stylize: a broad head, small eyes, prominent external gills and a mouth line that can look smile-like from a human point of view. Those features are routinely exaggerated into friendly character designs even though a real axolotl's facial expression should not be interpreted as a human emotion.</p>
<p>That distinction matters on an animal-care site: the “cute smile” is a visual impression, not evidence that an animal is happy, social or asking to be handled.</p>

<h2>How does science contribute to axolotl fame?</h2>
<p>Axolotls are not only entertainment icons. Their ability to regenerate complex tissues and their long history as laboratory animals repeatedly generate science coverage. That creates a second cultural pathway: someone may first meet the animal through a game or plush toy and then discover regeneration research, or encounter the science first and later recognize the animal in entertainment.</p>
<p>Read <a href="/biology-and-science/regeneration-and-limb-regrowth/">axolotl regeneration</a> for the biology rather than the pop-culture shorthand.</p>

<h2>Are axolotls important in Mexican culture too?</h2>
<p>Yes. The axolotl's cultural history is much older than modern fandom. Its Nahuatl name and historical role in the Valley of Mexico connect it to Indigenous and local history, while Xochimilco remains the home of the surviving wild population. Modern internet culture should not erase that geographic and historical context.</p>
<p>Continue to <a href="/biology-and-science/axolotl-history-discovery/">axolotl history and scientific discovery</a>, <a href="/biology-and-science/wild-habitat-xochimilco/">Xochimilco habitat</a>, and <a href="/axolotl-in-culture/do-people-eat-axolotls/">axolotl food and cultural history</a>.</p>

<h2>Sources</h2>
<ul>
<li><a href="https://www.minecraft.net/en-us/article/minecraft-live-2021-the-recap">Minecraft: Minecraft Live 2021 recap</a></li>
<li><a href="https://www.minecraft.net/en-us/article/taking-inventory--bucket-axolotl">Minecraft: Taking Inventory — Bucket of Axolotl</a></li>
<li><a href="https://www.minecraft.net/en-us/article/caves---cliffs-creative-collection">Minecraft: Caves & Cliffs Creative Collection</a></li>
<li><a href="https://books.disney.com/book/the-book-of-bill/">Disney Books: The Book of Bill by Alex Hirsch</a></li>
<li><a href="https://gravityfalls.fandom.com/wiki/The_Axolotl">Gravity Falls Wiki: The Axolotl (secondary fan reference for the series/cipher connection)</a></li>
<li><a href="https://www.encyclopedia.com/plants-and-animals/animals/vertebrate-zoology/axolotl">Encyclopedia.com: Julio Cortázar's “Axolotl” (1956)</a></li>
<li><a href="https://www.cambridge.org/core/books/abs/cambridge-history-of-latin-american-literature/twentiethcentury-short-story-in-spanish-america/26D3514B5C208080F9159E450AC198A3">Cambridge History of Latin American Literature: Cortázar bibliography</a></li>
</ul>
'''



# Canonical home-aquarium tank-size guidance (2026-09-18).
# Distinguishes intensive research housing from ordinary pet aquarium planning.
BODY_OVERRIDES["tank-setup/tank-size-by-age"] = r'''
<p><strong>For one adult pet axolotl, use a long aquarium of at least 20 gallons; if you are buying a permanent home from scratch, a 40-gallon breeder is MyAxolotl's preferred planning size because it gives substantially more floor area and water volume.</strong> The 40-gallon figure is a practical home-aquarium recommendation, not a scientifically proven biological threshold.</p>
<div class="role-note"><strong>This page owns tank-size requirements.</strong> Use it for age, body size, usable floor space, water volume and multiple-axolotl planning. For the full build sequence, filtration, cooling, substrate and cycling, use the <a href="/tank-setup/setup-guide/">tank setup guide</a>.</div>

<h2>What size tank does one adult axolotl need?</h2>
<p>Petco's current axolotl care sheet recommends a minimum habitat size of <strong>20+ gallons for an adult</strong> and specifically says aquarium length is more important than height, making a 20-gallon-long preferable to a 20-gallon-high. MyAxolotl uses that as the practical lower bound for a single adult home aquarium.</p>
<p><strong>If space and budget allow, choose a 40-gallon breeder instead.</strong> That is a site recommendation rather than a claim that 40 gallons is the only ethical or scientifically validated size. The wider footprint gives an adult more usable bottom area and gives the keeper more water volume in which to dilute waste and buffer maintenance mistakes.</p>

<h2>Why do tank-size recommendations conflict online?</h2>
<p>They often mix <strong>research housing</strong> with <strong>pet display aquariums</strong>. The 2024 Ambystoma Genetic Stock Center guide says housing-container size should scale with animal number and body size, and its laboratory uses small individual containers within intensive static or recirculating systems. It also states that filtered aquaria can house axolotls at densities far higher than most modern hobby recommendations.</p>
<p>Those laboratory systems use controlled water chemistry, frequent or automatic water replacement, standardized feeding, routine monitoring and institutional husbandry. A laboratory container is therefore not a sensible “minimum pet tank” citation. A home keeper usually benefits from more water volume and floor area because the system is less intensively managed.</p>

<h2>Tank size by life stage</h2>
<div class="table-wrap"><table>
<thead><tr><th>Life stage</th><th>How to plan housing</th><th>Why</th></tr></thead>
<tbody>
<tr><td>Larva / small baby</td><td>Use a manageable grow-out container sized to the animal and your cleaning routine; there is no universal evidence-based gallon minimum for this stage.</td><td>Small animals need easy feeding, observation and frequent maintenance.</td></tr>
<tr><td>Juvenile</td><td>A temporary grow-out tank can be smaller than the final adult home, but if buying one permanent aquarium, buy the adult-sized footprint early.</td><td>Avoid repeated upgrades and re-cycling.</td></tr>
<tr><td>One adult</td><td><strong>20-gallon long minimum; 40-gallon breeder preferred by MyAxolotl.</strong></td><td>Length/width provide usable floor space; larger volume is more forgiving for waste and maintenance.</td></tr>
<tr><td>Two adults</td><td>Do not rely on a simple “X gallons per animal” rule. Use a substantially larger footprint, separate hides and close monitoring; a 40-gallon breeder is a practical starting floor, with larger housing preferred.</td><td>Cohabitation adds territory, waste and bite-risk considerations that gallons alone cannot solve.</td></tr>
<tr><td>Three or more adults</td><td>Plan a large custom system or separate aquariums rather than multiplying a gallon formula.</td><td>Group management, size matching, feeding and injury monitoring become the limiting factors.</td></tr>
</tbody></table></div>

<h2>Does floor space matter more than height?</h2>
<p><strong>Yes for how the animal uses the enclosure, but water volume still matters for system stability.</strong> Axolotls spend much of their time on or near the bottom, so a long, wide aquarium gives more useful space than a tall tank with the same nominal volume. Extra height is not useless—it still adds water—but it should not come at the expense of length and width.</p>
<p>When comparing two tanks, check both the gallon rating and the actual footprint. Use the <a href="/tools/aquarium-volume-calculator/">Aquarium Volume Calculator</a> if you have dimensions but not a reliable volume figure.</p>

<h2>Is a 20-gallon long enough for one adult?</h2>
<p><strong>It is a current practical minimum, not the size MyAxolotl would choose when starting from scratch.</strong> A healthy adult can physically fit in a 20-gallon-long aquarium, and Petco currently lists 20+ gallons as the adult minimum. The tradeoff is less floor area, less dilution of waste and less room for hides and equipment.</p>
<p>A 40-gallon breeder gives a wider footprint and roughly twice the nominal water capacity, which is why this site prefers it as the long-term planning choice when the keeper has room for it.</p>

<h2>What size tank do two axolotls need?</h2>
<p><strong>There is no evidence-based gallon formula that makes two axolotls automatically compatible.</strong> Closely matched adults can sometimes be housed together, but nipping, feeding competition, breeding behavior and size differences still matter. If two adults share a tank, provide more floor space than you would for one, at least one suitable hide per animal, and a layout that lets them separate.</p>
<p>MyAxolotl treats a 40-gallon breeder as a <em>starting footprint</em> for two closely size-matched adults, not a guarantee. If bites, repeated displacement, a growing size gap or feeding problems appear, separate the animals. See <a href="/care-basics/keeping-multiple-axolotls/">Can Axolotls Live Together?</a>.</p>

<h2>What size tank do baby and juvenile axolotls need?</h2>
<p><strong>Do not force babies into a rigid gallon chart.</strong> The 2024 AGSC guide scales containers as animals grow and pairs container size with frequent cleaning. That research model demonstrates the important principle: housing size and maintenance intensity are linked.</p>
<p>For a pet keeper, a small grow-out setup can make feeding and observation easier, but it must stay clean and temperature-stable. If you already know you will keep the animal to adulthood, buying and cycling the permanent adult aquarium early can be simpler than repeatedly upgrading.</p>
<p>For the animal's body-size progression rather than aquarium gallons, use <a href="/care-basics/axolotl-age-and-size-chart/">How Big Do Axolotls Get?</a>.</p>

<h2>When should you upgrade the tank?</h2>
<p>Upgrade before the setup becomes difficult to manage. Warning signs include insufficient floor area for a full-size animal and hides, rapidly accumulating waste, repeated water-quality instability, equipment crowding, or multiple animals that cannot maintain separate resting areas. An arbitrary birthday or body-length cutoff is less useful than those practical constraints.</p>

<h2>What should you measure before buying a tank?</h2>
<ul>
<li><strong>External footprint:</strong> confirm the aquarium and stand fit the room.</li>
<li><strong>Internal length and width:</strong> these determine usable bottom area.</li>
<li><strong>Actual water depth:</strong> décor, substrate and headspace reduce real water volume.</li>
<li><strong>Filter and chiller space:</strong> equipment needs clearance and suitable flow routing.</li>
<li><strong>Loaded weight:</strong> water is heavy; use the <a href="/tools/aquarium-volume-calculator/">Aquarium Volume Calculator</a> to estimate water weight.</li>
</ul>

<h2>Sources and recommendation note</h2>
<p><strong>Evidence boundary:</strong> no source reviewed establishes a universal research-derived pet-aquarium gallon threshold. The AGSC 2024 guide is a research-husbandry reference and explicitly scales housing with animal number/body size while using intensive maintenance systems. Petco's current pet-care sheet supplies the clearest current consumer minimum we found: 20+ gallons for one adult, with a long tank preferred over a high tank.</p>
<ul>
<li><a href="https://ambystoma.uky.edu/genetic-stock-center/documents/AGSC%20_Guide_2024.pdf">Ambystoma Genetic Stock Center: Axolotl Guide 2024</a></li>
<li><a href="https://www.petco.com/pet-education/caresheets/axolotl">Petco: Axolotl Care Guide — 20+ gallon adult minimum</a></li>
</ul>
<p><strong>MyAxolotl recommendation:</strong> treat a 20-gallon long as the practical minimum for one adult and a 40-gallon breeder as the preferred long-term home when space and budget permit. That preference is deliberately more conservative than laboratory-density guidance.</p>
'''


# Evidence-bounded fungal-disease cluster (2026-09-18).
BODY_OVERRIDES["health/fungal-infections-saprolegnia"] = r'''
<p><strong>A white or cotton-like growth on an axolotl can be consistent with saprolegniasis, but appearance alone does not confirm the organism.</strong> <em>Saprolegnia</em>, <em>Aphanomyces</em> and <em>Achlya</em> are water molds (oomycetes) that can infect the skin or gills of aquatic amphibians. Veterinary diagnosis can involve a skin scraping examined for hyphae and zoospores.</p>
<div class="role-note"><strong>This page owns the condition and diagnostic pathway.</strong> The <a href="/health/black-tea-bath/">black-tea page</a> explains the evidence limits of a popular hobby practice; the <a href="/health/salt-bath/">salt-bath page</a> explains where saline appears in veterinary guidance. Neither page should replace diagnosis or veterinary care for a worsening lesion.</div>

<h2>What is axolotl saprolegniasis?</h2>
<p>Saprolegniasis is a disease caused by opportunistic water molds. Merck's veterinary amphibian guidance describes these organisms as affecting the skin and gills of aquatic and larval amphibians. They are often associated with tissue that has already been damaged or whose normal protective surface has been compromised.</p>

<h2>What can saprolegniasis look like?</h2>
<p>The classic gross finding is a <strong>whitish, cotton-like growth</strong> attached to skin or gill tissue. Older mats can appear greenish because algae can become incorporated. Once the material is removed from water, it may collapse and become much harder to see.</p>
<p>Other signs can include lethargy, respiratory difficulty, loss of appetite and weight loss, depending on lesion extent. None of those secondary signs is specific to saprolegniasis.</p>

<h2>What can be mistaken for fungus?</h2>
<p>Not every pale patch, gill change or skin lesion is a water mold. Bacterial disease, other fungal disease, parasites, injury, abnormal shedding or chemical irritation can overlap visually. Merck notes that many amphibian fungal diseases are difficult to distinguish grossly and may require wet mounts, culture, histology or special stains.</p>
<p><strong>Do not identify “columnaris,” “fungus” or a parasite from one photograph with certainty.</strong> Use photographs to document change, not to substitute for examination.</p>

<h2>Why can Saprolegnia take hold?</h2>
<p>Veterinary references describe saprolegniasis as opportunistic. Factors associated with disease include:</p>
<ul>
<li>previous abrasions or other skin trauma;</li>
<li>loss or damage of the protective surface layer from chemical irritants;</li>
<li>poor water quality, including ammonia exposure;</li>
<li>malnutrition, including vitamin-A problems in some amphibian cases; and</li>
<li>other conditions that leave tissue damaged or the animal compromised.</li>
</ul>
<p>For a pet axolotl, that means a visible lesion should trigger both a health assessment and a husbandry review rather than treatment of the white growth in isolation.</p>

<h2>What should you check first?</h2>
<ol>
<li><strong>Record the lesion.</strong> Take clear dated photographs in neutral light.</li>
<li><strong>Measure water quality.</strong> Record ammonia, nitrite, nitrate, pH and temperature. Use <a href="/tank-setup/how-to-test-water/">How to Test Axolotl Water</a> if needed.</li>
<li><strong>Look for trauma.</strong> Check tank mates, sharp décor, intake guards and recent handling.</li>
<li><strong>Review appetite and behavior.</strong> Note weight loss, breathing difficulty, abnormal swimming or rapid decline.</li>
<li><strong>Contact an amphibian-experienced veterinarian</strong> when the lesion is spreading, involves gills, is accompanied by systemic signs, or the diagnosis is uncertain.</li>
</ol>

<h2>How is saprolegniasis diagnosed?</h2>
<p>Merck describes a presumptive diagnosis by finding fungal-like hyphae and thin-walled zoospores on a skin scraping. Depending on the differential diagnosis, a veterinarian may use additional microscopy, culture or histopathology.</p>
<p>This is why “cottony = definitely Saprolegnia” is too strong for an evidence-based page.</p>

<h2>How is axolotl fungus treated?</h2>
<p><strong>Treatment depends on the organism, lesion location, extent and the animal's overall condition.</strong> Current veterinary amphibian references emphasize correcting poor water quality and using appropriate topical or systemic antifungal therapy. For localized saprolegniasis, veterinary references also describe debridement and saline application in selected cases.</p>
<p>Those options require clinical judgment. The concentration, exposure method and medication that is reasonable for one amphibian condition may not be safe for another. This page therefore does not convert veterinary treatments into a universal home recipe.</p>

<h2>Should you use a black tea bath?</h2>
<p>Black-tea baths are common in axolotl hobby discussions, but the veterinary sources reviewed for this page do not list black tea as a standard treatment for saprolegniasis. That means we should not describe a tea bath as a proven antifungal cure or assign it a fixed treatment timetable.</p>
<p>See <a href="/health/black-tea-bath/">Black Tea Bath for Axolotls: When & How to Use One</a> for the evidence boundary and questions to ask before using this hobby practice.</p>

<h2>Should you use a salt bath?</h2>
<p>Saline treatment has a stronger veterinary basis than black tea: Merck's professional amphibian guidance describes salt-water application for localized saprolegniasis. However, that is <strong>not</strong> the same as validating every online “teaspoons per liter for X minutes” protocol for pet axolotls.</p>
<p>See <a href="/health/salt-bath/">Axolotl Salt Bath: When It May Be Used & How It Works</a> for the distinction between veterinary saline use and improvised home recipes.</p>

<h2>When is veterinary care more urgent?</h2>
<p>Contact an amphibian-experienced veterinarian promptly when there is respiratory distress, substantial gill involvement, anorexia with deterioration, weight loss, ulceration, rapid spread, repeated recurrence, extensive skin damage, or uncertainty about whether the lesion is fungal at all.</p>
<p>Use <a href="/health/emergency-first-aid/">Axolotl Emergency Signs</a> for triage and <a href="/health/finding-an-exotic-vet/">Finding an Exotic Vet</a> to locate appropriate care.</p>

<h2>How do you reduce recurrence risk?</h2>
<p>Prevention is primarily husbandry: stable clean water, safe surfaces, appropriate nutrition, low-stress handling and correction of injuries or tank-mate problems. Treating a visible lesion without correcting the factor that damaged the skin makes recurrence more likely.</p>

<h2>Sources</h2>
<ul>
<li><a href="https://www.merckvetmanual.com/exotic-and-laboratory-animals/amphibians/infectious-diseases-of-amphibians">Merck Veterinary Manual: Infectious Diseases of Amphibians — Saprolegniasis</a></li>
<li><a href="https://www.merckvetmanual.com/all-other-pets/amphibians/common-infectious-diseases-of-amphibians">Merck Veterinary Manual, pet-owner version: Common Infectious Diseases of Amphibians, updated June 2026</a></li>
<li><a href="https://pubmed.ncbi.nlm.nih.gov/35628794/">Saprolegniosis in Amphibians: An Integrated Overview</a></li>
<li><a href="https://ambystoma.uky.edu/education1/guide-to-axolotl-husbandry">Ambystoma Genetic Stock Center: Guide to Axolotl Husbandry</a></li>
</ul>
'''

BODY_OVERRIDES["health/black-tea-bath"] = r'''
<p><strong>A black tea bath is a popular axolotl-keeping practice, but it is not a standard veterinary treatment for saprolegniasis in the amphibian references reviewed by MyAxolotl.</strong> Claims that a fixed tea ratio “kills fungus,” repairs the slime coat, or guarantees improvement within a certain number of days go beyond the evidence we found.</p>
<div class="role-note"><strong>This page explains a procedure's evidence limits; it does not diagnose fungus.</strong> Start with <a href="/health/fungal-infections-saprolegnia/">Axolotl Fungus: Symptoms, Causes & Treatment</a>.</div>

<h2>What is a black tea bath?</h2>
<p>In the hobby, a black tea bath usually means placing an axolotl temporarily in dechlorinated water containing diluted brewed black tea. The idea is based on plant tannins and their astringent or antimicrobial properties in other contexts.</p>
<p>The problem is standardization: tea type, brewing strength, dilution, water chemistry and exposure time vary widely between online protocols. We did not find a controlled axolotl clinical study establishing one therapeutic concentration or treatment schedule.</p>

<h2>Is black tea a proven treatment for axolotl fungus?</h2>
<p><strong>Not from the veterinary evidence reviewed here.</strong> Current Merck amphibian guidance for saprolegniasis discusses diagnosis, hygiene, correcting water quality, saline application in selected localized cases and antifungal medications. It does not list black tea as a standard treatment.</p>
<p>That absence does not prove that tannin exposure can never have a biological effect. It means MyAxolotl should not present a hobby recipe as though it were a validated veterinary protocol.</p>

<h2>What claims should you be cautious about?</h2>
<ul>
<li>“Use exactly a 1:3 tea-to-water ratio.”</li>
<li>“Ten to fifteen minutes is the proven therapeutic window.”</li>
<li>“Tea baths cure mild fungus in three days.”</li>
<li>“Black tea is antibacterial and antifungal at any hobby dilution.”</li>
<li>“Tea baths repair or tighten an axolotl's slime coat.”</li>
</ul>
<p>Those statements require axolotl-specific concentration and outcome data that the sources reviewed here do not provide.</p>

<h2>When might a veterinarian still discuss tannins?</h2>
<p>A veterinarian may consider environmental or supportive measures that include tannin-containing materials, depending on the animal and condition. If your veterinarian specifically recommends black tea, ask for the exact product, concentration, water volume, exposure duration, frequency and stop criteria rather than substituting a forum recipe.</p>

<h2>What should you do before any bath?</h2>
<ol>
<li>Confirm the water temperature and test ammonia, nitrite, nitrate and pH.</li>
<li>Photograph the lesion or irritation in neutral light.</li>
<li>Review recent injuries, new tank mates, cleaning chemicals and handling.</li>
<li>Determine whether the animal has systemic signs such as anorexia, respiratory difficulty, weight loss or abnormal swimming.</li>
<li>Use veterinary guidance for a spreading or uncertain lesion.</li>
</ol>

<h2>Can a tea bath delay needed treatment?</h2>
<p>Yes. The main risk is not only the bath itself; it is losing time while a bacterial, fungal or other lesion progresses under the assumption that “tea will fix it.” Amphibian skin diseases can overlap visually, and the correct treatment may require microscopy or medication.</p>

<h2>What is the safer evidence-based support?</h2>
<p>Correct poor water quality, keep the animal within an appropriate stable temperature range, minimize unnecessary handling, remove sources of trauma and obtain veterinary assessment when the lesion is spreading or the animal is deteriorating. Those steps are supported more directly than a universal tea-bath recipe.</p>

<h2>When should you contact an exotic veterinarian?</h2>
<p>Seek veterinary advice for gill involvement, rapidly enlarging lesions, ulceration, respiratory difficulty, substantial appetite loss, weight loss, repeated recurrence, severe lethargy or failure to improve after husbandry problems are corrected.</p>
<p>Use the <a href="/health/finding-an-exotic-vet/">axolotl vet guide</a> if you do not already have an amphibian-experienced clinician.</p>

<h2>Sources</h2>
<ul>
<li><a href="https://www.merckvetmanual.com/exotic-and-laboratory-animals/amphibians/infectious-diseases-of-amphibians">Merck Veterinary Manual: Infectious Diseases of Amphibians</a></li>
<li><a href="https://www.merckvetmanual.com/all-other-pets/amphibians/common-infectious-diseases-of-amphibians">Merck Veterinary Manual: Common Infectious Diseases of Amphibians, updated June 2026</a></li>
<li><a href="https://pubmed.ncbi.nlm.nih.gov/35628794/">Saprolegniosis in Amphibians: An Integrated Overview</a></li>
</ul>
'''

BODY_OVERRIDES["health/salt-bath"] = r'''
<p><strong>Salt has a documented role in veterinary management of saprolegniasis in amphibians, but that does not validate every axolotl salt-bath recipe found online.</strong> Amphibian skin and gills are highly permeable, so concentration, exposure method, lesion type and the animal's condition matter.</p>
<div class="role-note"><strong>This page owns the saline-treatment question, not diagnosis.</strong> First review <a href="/health/fungal-infections-saprolegnia/">Axolotl Fungus: Symptoms, Causes & Treatment</a>.</div>

<h2>What is an axolotl salt bath?</h2>
<p>“Salt bath” is a hobby term for temporary exposure to saline water. In professional amphibian medicine, saline solutions can be used for several different purposes, and Merck specifically describes salt-water application in selected localized cases of saprolegniasis.</p>
<p>That veterinary statement is much narrower than “all white fuzz should get a salt bath.”</p>

<h2>Does veterinary guidance support salt for saprolegniasis?</h2>
<p><strong>Yes, in selected cases.</strong> Merck's professional amphibian manual describes localized smaller saprolegniasis infections as potentially being debrided and treated with salt-water application, while also emphasizing correction of poor water quality and the possible use of antifungal medication.</p>
<p>The pet-owner version is even more conservative: it lists antifungals and dips prescribed by a veterinarian for saprolegniasis.</p>

<h2>Why doesn't MyAxolotl give a teaspoons-per-liter recipe?</h2>
<p>Because a household spoon recipe can hide several important variables:</p>
<ul>
<li>the actual salinity produced by the salt product;</li>
<li>the duration and frequency of exposure;</li>
<li>whether the lesion is truly saprolegniasis;</li>
<li>whether gill or skin tissue is already severely damaged;</li>
<li>the animal's hydration and systemic condition; and</li>
<li>differences between a topical saline application, an immersion dip and long-term water chemistry.</li>
</ul>
<p>Veterinary references express saline treatment in measured salinity/concentration terms and clinical context, not as one universal household recipe for every pet axolotl.</p>

<h2>Is stronger or longer better?</h2>
<p><strong>No.</strong> Amphibians exchange water and dissolved substances across permeable skin. Increasing salinity or exposure time can increase osmotic stress and tissue irritation. If a veterinarian prescribes a saline treatment, follow that concentration and exposure schedule rather than “adding a little more” for a stubborn lesion.</p>

<h2>Should salt be added permanently to the axolotl tank?</h2>
<p>Do not convert a short-term clinical saline treatment into routine aquarium salting. Axolotls are freshwater amphibians, and routine husbandry water chemistry is a different question from a veterinarian-directed treatment exposure. See <a href="/biology-and-science/wild-habitat-xochimilco/">Where Do Axolotls Live?</a> and <a href="/tank-setup/water-parameters-cycling/">Water Parameters & Nitrogen Cycle</a>.</p>

<h2>What should you check before considering saline treatment?</h2>
<ol>
<li>Confirm water quality and temperature.</li>
<li>Document the lesion and whether it is spreading.</li>
<li>Check for trauma or chemical exposure.</li>
<li>Review appetite, breathing, weight and behavior.</li>
<li>Get veterinary guidance when the diagnosis is uncertain or the lesion is more than a small localized surface problem.</li>
</ol>

<h2>What signs should move you away from DIY treatment?</h2>
<p>Respiratory difficulty, substantial gill involvement, ulceration, widespread or rapidly progressing lesions, weight loss, marked anorexia, abnormal swimming, severe swelling or repeated recurrence warrant veterinary assessment rather than repeated improvised baths.</p>

<h2>Salt bath vs black tea bath</h2>
<p>They do not have equal evidence. Veterinary amphibian sources describe saline use for selected saprolegniasis cases. The same sources reviewed by MyAxolotl do not list black tea as a standard treatment. That does not make salt universally appropriate; it means the saline question has a documented clinical basis that still needs correct diagnosis and dosing.</p>
<p>See <a href="/health/black-tea-bath/">Black Tea Bath for Axolotls</a> for that evidence boundary.</p>

<h2>What may a veterinarian use instead?</h2>
<p>Depending on diagnosis and severity, veterinarians may correct environmental conditions, debride a localized lesion, use a properly measured saline treatment, or prescribe topical/systemic antifungal medication. The treatment should match the organism and the animal rather than a generic “fungus protocol.”</p>

<h2>Sources</h2>
<ul>
<li><a href="https://www.merckvetmanual.com/exotic-and-laboratory-animals/amphibians/infectious-diseases-of-amphibians">Merck Veterinary Manual: Infectious Diseases of Amphibians — Saprolegniasis</a></li>
<li><a href="https://www.merckvetmanual.com/all-other-pets/amphibians/common-infectious-diseases-of-amphibians">Merck Veterinary Manual: Common Infectious Diseases of Amphibians, updated June 2026</a></li>
<li><a href="https://pubmed.ncbi.nlm.nih.gov/35628794/">Saprolegniosis in Amphibians: An Integrated Overview</a></li>
</ul>
'''


BODY_OVERRIDES["tank-setup/water-change-guide"] = r'''
<p><strong>For an established filtered axolotl aquarium, use regular partial water changes and measured water quality rather than one universal percentage for every tank.</strong> A useful evidence-based baseline is <strong>at least about 10% weekly</strong>: the 2024 Ambystoma Genetic Stock Center guide specifies weekly 10% changes for filtered axolotl aquaria, and Merck's pet-amphibian guidance likewise recommends at least 10% weekly in established aquatic tanks.</p>

<h2>How often should you change axolotl tank water?</h2>
<p><strong>Start with a weekly partial change, then adjust from your actual readings and waste load.</strong> Tank volume, number and size of animals, feeding, filter capacity, plant load and source-water chemistry all change how quickly water quality drifts.</p>
<p>Petco's current axolotl sheet gives a broader consumer schedule of 10–25% every 2–4 weeks or as needed. MyAxolotl uses the more conservative weekly baseline because both AGSC and Merck support weekly partial renewal in filtered aquatic systems and because weekly testing makes it easier to pair maintenance with measured trends.</p>

<h2>How much water should you change?</h2>
<p>There is no single percentage that fits every situation. For routine maintenance, a modest partial change is usually enough when ammonia and nitrite remain controlled and nitrate/waste are not rising rapidly. If water quality is abnormal, the <a href="/tank-setup/water-parameters-cycling/">Water Parameters & Nitrogen Cycle guide</a> should determine the corrective response rather than this page inventing a fixed emergency percentage.</p>
<p><strong>Do not confuse routine maintenance with an emergency correction.</strong> A tank with measurable ammonia/nitrite or another contamination problem may need a different response and repeat testing.</p>

<h2>What do you need before starting?</h2>
<ul>
<li>a siphon or dedicated aquarium bucket;</li>
<li>appropriate water conditioner when using chlorinated/chloraminated source water;</li>
<li>a thermometer;</li>
<li>water tests appropriate to your system; and</li>
<li>a clean container for preparing replacement water when needed.</li>
</ul>
<p>Keep aquarium equipment separate from food-preparation tools and never use soap or household-cleaner residue in the tank.</p>

<h2>Step 1: Test before changing water</h2>
<p>Record temperature, ammonia, nitrite, nitrate and pH before maintenance when possible. The reading gives you a baseline and helps distinguish routine maintenance from a chemistry problem.</p>
<p>Use <a href="/tank-setup/how-to-test-water/">How to Test Axolotl Water</a> for the sampling procedure.</p>

<h2>Step 2: Prepare safe replacement water</h2>
<p>Replacement water must be free of harmful chlorine/chloramine and suitable for the aquarium's chemistry. Follow the water conditioner's label for the volume of new water being treated unless the product specifically instructs otherwise.</p>
<p>Use the <a href="/tools/water-conditioner-dosage-calculator/">Water Conditioner Dosage Calculator</a> for volume math, then confirm the product label.</p>

<h2>Step 3: Match temperature closely</h2>
<p>Avoid creating a sudden thermal swing during maintenance. Measure both the aquarium and replacement water rather than judging by touch. The replacement water should be close enough that the change does not abruptly push the tank outside its intended temperature range.</p>
<p>For the actual target range and cooling decisions, use <a href="/tank-setup/temperature/">Axolotl Tank Temperature</a>.</p>

<h2>Step 4: Remove waste and part of the old water</h2>
<p>Siphon visible waste, uneaten food and debris while removing the planned portion of water. Keep the siphon away from the axolotl and from anything small enough to be accidentally sucked into the hose.</p>
<p>You do not need to strip the aquarium bare during every water change. The goal is routine waste removal and dilution while preserving a stable, established system.</p>

<h2>Step 5: Add replacement water gently</h2>
<p>Add conditioned, temperature-compatible water without blasting the animal or substrate. Pour against the glass, use a plate/baffle, or otherwise disperse the flow if necessary.</p>

<h2>Step 6: Recheck when you are correcting a problem</h2>
<p>For ordinary routine maintenance, logging the before-reading and continuing weekly monitoring may be enough. If the water change was performed because ammonia, nitrite, pH or another parameter was abnormal, retest according to the corrective plan and record the result.</p>
<p>The <a href="/tools/nitrogen-cycle-tracker/">Nitrogen Cycle Tracker</a> is useful for trend logging.</p>

<h2>Should you change water during cycling?</h2>
<p><strong>Do not use a calendar such as “change water every day for the first 4–6 weeks.”</strong> Cycling strategy depends on whether the system is fishless, what ammonia source is being used and what the measured ammonia/nitrite/nitrate values show. An axolotl should not be used as the ammonia source for a new uncycled tank.</p>
<p>Use the <a href="/tank-setup/water-parameters-cycling/">cycling guide</a> and your test results to decide whether a water change is appropriate during the cycling process.</p>

<h2>Should juveniles automatically get more water changes?</h2>
<p>Not because of age alone. Young axolotls may be fed more often and small grow-out containers can accumulate waste quickly, so maintenance often has to be more frequent. But the real drivers are container volume, food waste, stocking density and measured water quality—not the word <em>juvenile</em> by itself.</p>

<h2>Should you clean the filter during a water change?</h2>
<p>Filter maintenance is a separate task. Do not routinely replace all biological media just because you are changing water. Clean mechanical debris when needed and preserve established biological filtration unless the manufacturer or a specific problem requires replacement.</p>
<p>Use <a href="/tank-setup/filtration-for-axolotls/">Do Axolotls Need a Filter?</a> for filter care and biological-filtration principles.</p>

<h2>Common water-change mistakes</h2>
<ul>
<li>using untreated chlorinated/chloraminated water;</li>
<li>creating a large temperature or chemistry swing;</li>
<li>guessing water quality instead of testing;</li>
<li>allowing food and feces to accumulate between scheduled changes;</li>
<li>cleaning the aquarium with soap or chemical residue;</li>
<li>replacing biological filter media unnecessarily; and</li>
<li>following a fixed percentage even when test results show the tank needs a different response.</li>
</ul>

<h2>Sources</h2>
<ul>
<li><a href="https://ambystoma.uky.edu/genetic-stock-center/documents/AGSC%20_Guide_2024.pdf">Ambystoma Genetic Stock Center: Axolotl Guide 2024 — filtered aquaria and water quality</a></li>
<li><a href="https://www.merckvetmanual.com/all-other-pets/amphibians/housing-for-amphibians">Merck Veterinary Manual: Housing for Amphibians — established aquatic-tank water changes</a></li>
<li><a href="https://www.petco.com/pet-education/caresheets/axolotl">Petco Axolotl Care Guide — consumer maintenance schedule</a></li>
</ul>
'''


BODY_OVERRIDES["tank-setup/filtration-for-axolotls"] = r'''
<p><strong>For a conventional home axolotl aquarium, use biological filtration with gentle water movement.</strong> The filter's most important job is to support the nitrogen cycle so ammonia is converted through nitrite toward nitrate; its output should not create a current that continuously pushes or disturbs the axolotl.</p>
<div class="role-note"><strong>This page owns filtration principles, sizing logic and flow control.</strong> For the head-to-head purchase decision, use <a href="/tank-setup/canister-vs-sponge-filter/">Canister Filters vs Sponge Filters for Axolotls</a>.</div>

<h2>Do axolotls need a filter?</h2>
<p><strong>A home aquarium should normally use an established biological filter.</strong> Axolotls can technically be kept in static containers without filtration when water is replaced frequently—research facilities do this under controlled husbandry—but that is a different management system from an ordinary pet aquarium.</p>
<p>The 2024 Ambystoma Genetic Stock Center guide describes three housing approaches: static housing, filtered aquaria and recirculating systems. For filtered aquaria it recommends low-current power filtration with biological filtration, regular water changes and water-chemistry monitoring.</p>

<h2>What does an axolotl filter actually do?</h2>
<div class="table-wrap"><table>
<thead><tr><th>Filtration role</th><th>What it does</th><th>Priority</th></tr></thead>
<tbody>
<tr><td>Biological</td><td>Provides colonized surface area for microbes involved in processing nitrogenous waste</td><td>Essential in a conventional cycled aquarium</td></tr>
<tr><td>Mechanical</td><td>Captures suspended debris and food/waste particles</td><td>Useful; remove captured waste during maintenance</td></tr>
<tr><td>Chemical</td><td>Special-purpose media can remove selected dissolved compounds</td><td>Optional; not a substitute for biological filtration or water changes</td></tr>
</tbody></table></div>

<h2>Why does biological filtration matter?</h2>
<p>Ammonia is produced in an occupied aquatic system from animal waste and decomposing organic material. In a cycled filter, microbial communities convert ammonia through nitrite toward nitrate. Merck's aquatic-animal guidance identifies ammonia toxicosis as a common problem in systems without an established active biofilter.</p>
<p>Use <a href="/tank-setup/water-parameters-cycling/">Water Parameters & Nitrogen Cycle</a> for the chemistry and <a href="/tools/nitrogen-cycle-tracker/">the Nitrogen Cycle Tracker</a> for logging.</p>

<h2>Does changing water remove the beneficial bacteria?</h2>
<p><strong>Routine partial water changes do not mean you must “restart the cycle.”</strong> A functioning biofilter is based on microbial biofilms associated with filtration media and aquarium surfaces, while water changes dilute dissolved waste products. The real risk is destroying or replacing too much established biological media at once or exposing it to conditions that kill the biofilm.</p>
<p>This is why water changes and biological filtration work together rather than competing with each other.</p>

<h2>How much flow is safe for an axolotl?</h2>
<p><strong>There is no well-established axolotl GPH multiplier such as “5× target, 10× maximum” in the primary husbandry sources reviewed here.</strong> The defensible rule is functional: keep circulation slow enough that the animal can rest, walk and feed without being continuously displaced or forced to brace against a concentrated jet.</p>
<p>AGSC explicitly warns that rapidly circulating water is stressful and recommends keeping circulation as slow as possible in continuously circulated systems. A spray bar, baffle, broad outlet or adjustable flow can reduce concentrated current while preserving filtration.</p>

<h2>How do you know the filter flow is too strong?</h2>
<p>Watch the animal and the tank rather than relying only on the pump's box rating. Reduce or redirect flow if the outlet visibly pushes the axolotl, prevents it from settling normally, blows food away during feeding, or creates a strong current across most of the usable floor area.</p>
<p>Do not diagnose “flow stress” from curled gills alone; posture changes are nonspecific. Use <a href="/health/curled-gills-stress-signal/">the curled-gills guide</a> if that is the sign that concerns you.</p>

<h2>How should you size a filter?</h2>
<p>Filter sizing has two independent questions:</p>
<ol>
<li><strong>Biological capacity:</strong> can the media support a stable nitrogen cycle for the actual animal and feeding load?</li>
<li><strong>Outlet behavior:</strong> can the water return be adjusted or dispersed so current remains gentle?</li>
</ol>
<p>A filter can have plenty of media but an unsuitable outlet, or a gentle outlet but insufficient biological capacity. Tank volume alone cannot answer both questions.</p>

<h2>Sponge, HOB or canister filter?</h2>
<div class="table-wrap"><table>
<thead><tr><th>Filter type</th><th>Strengths</th><th>Watch for</th></tr></thead>
<tbody>
<tr><td>Sponge</td><td>Simple biological filtration, inherently gentle when correctly air-driven, inexpensive</td><td>Mechanical capture is limited; choose enough sponge/media area for the system</td></tr>
<tr><td>Hang-on-back (HOB)</td><td>Accessible media and good mechanical filtration</td><td>Waterfall/outlet may need baffling or flow reduction</td></tr>
<tr><td>Canister</td><td>Large customizable media capacity and flexible return plumbing</td><td>Can create strong output if not adjusted/dispersed; more complex maintenance</td></tr>
</tbody></table></div>
<p>No one type is automatically “best” for every axolotl tank. The dedicated <a href="/tank-setup/canister-vs-sponge-filter/">Canister vs Sponge</a> page owns that comparison.</p>

<h2>Should you oversize the filter?</h2>
<p>It can be reasonable to choose more biological-media capacity than the bare minimum, but <strong>do not assume a larger filter rating is automatically safer</strong>. Manufacturer tank ratings are not axolotl-specific, and a higher-capacity filter can also produce stronger flow. If you choose extra media capacity, make sure the return can still be made gentle.</p>

<h2>How do you cycle a new filter?</h2>
<p>Establish the biological filter before relying on it to process an axolotl's waste. A new filter does not become “cycled” merely because it has run for a set number of days. Cycling is confirmed from the pattern of ammonia, nitrite and nitrate under the method you are using.</p>
<p>Follow <a href="/tank-setup/water-parameters-cycling/">the cycling guide</a> and do not use the axolotl itself as the ammonia source for an uncycled aquarium.</p>

<h2>How do you maintain filter media?</h2>
<ul>
<li>Remove trapped debris before it decomposes in the filter.</li>
<li>Preserve established biological media when it is still functional.</li>
<li>Avoid replacing all mature biological media at the same time without a reason and a plan.</li>
<li>Keep chlorine/chloramine away from established biological media.</li>
<li>Follow the manufacturer's mechanical-maintenance instructions while protecting the biofilter.</li>
</ul>
<p>Filter maintenance frequency depends on debris load and the filter design; use declining flow, visible accumulation and water-quality trends rather than an arbitrary monthly replacement schedule.</p>

<h2>Do you still need water changes with a filter?</h2>
<p><strong>Yes.</strong> A biological filter processes nitrogenous waste; it does not make water changes obsolete. The 2024 AGSC guide specifies regular partial water replacement even in filtered and recirculating systems. Use <a href="/tank-setup/water-change-guide/">the Axolotl Water Change Guide</a> for the maintenance procedure.</p>

<h2>Sources</h2>
<ul>
<li><a href="https://ambystoma.uky.edu/genetic-stock-center/documents/AGSC%20_Guide_2024.pdf">Ambystoma Genetic Stock Center: Axolotl Guide 2024</a></li>
<li><a href="https://ambystoma.uky.edu/education1/guide-to-axolotl-husbandry">Ambystoma Genetic Stock Center: Guide to Axolotl Husbandry</a></li>
<li><a href="https://www.merckvetmanual.com/exotic-and-laboratory-animals/laboratory-animals/management-of-laboratory-animals">Merck Veterinary Manual: Management of Laboratory Animals — aquatic water quality and biofiltration</a></li>
<li><a href="https://www.merckvetmanual.com/all-other-pets/amphibians/housing-for-amphibians">Merck Veterinary Manual: Housing for Amphibians</a></li>
</ul>
'''


BODY_OVERRIDES["tank-setup/canister-vs-sponge-filter"] = r'''
<p><strong>Neither a canister filter nor a sponge filter is automatically “best” for every axolotl tank.</strong> A sponge filter is simple, inexpensive and naturally easy to run with gentle circulation. A canister filter offers more media capacity and stronger mechanical filtration, but its return flow often needs to be dispersed or reduced. The better choice is the one that provides enough biological filtration for your system without creating strong current at the animal's resting area.</p>
<div class="role-note"><strong>This page owns the canister-versus-sponge decision.</strong> For nitrogen-cycle biology, filter sizing principles and general flow control, start with <a href="/tank-setup/filtration-for-axolotls/">Do Axolotls Need a Filter?</a>.</div>

<h2>Canister vs sponge filter: quick comparison</h2>
<div class="table-wrap"><table>
<thead><tr><th>Question</th><th>Sponge filter</th><th>Canister filter</th></tr></thead>
<tbody>
<tr><td>Biological filtration</td><td>Good when the sponge/media area is adequate for the bioload</td><td>Good; typically offers more configurable biological-media volume</td></tr>
<tr><td>Mechanical debris capture</td><td>Basic to moderate</td><td>Usually stronger and multi-stage</td></tr>
<tr><td>Flow control</td><td>Often naturally gentle; depends on air pump and design</td><td>Return may need a spray bar, baffle or adjustment</td></tr>
<tr><td>Maintenance</td><td>Simple; sponge is easy to inspect and rinse</td><td>More parts, hoses and internal media to service</td></tr>
<tr><td>Cost / complexity</td><td>Lower</td><td>Higher</td></tr>
<tr><td>Media customization</td><td>Limited</td><td>High</td></tr>
<tr><td>Inline equipment integration</td><td>Not designed as a pressurized water loop</td><td>Can suit some inline equipment when manufacturer flow requirements are compatible</td></tr>
<tr><td>Best reason to choose it</td><td>Simplicity and gentle circulation</td><td>Media capacity and stronger debris removal</td></tr>
</tbody></table></div>

<h2>What matters more than the filter type?</h2>
<p>Three things matter more than the label on the filter:</p>
<ol>
<li><strong>Biological capacity.</strong> The system needs enough established biofilm to process the actual nitrogenous-waste load.</li>
<li><strong>Gentle circulation.</strong> The return should not continuously push the axolotl or create a strong current across its resting area.</li>
<li><strong>Maintainability.</strong> You need to be able to remove trapped debris and preserve mature biological media without letting the filter clog.</li>
</ol>
<p>The Ambystoma Genetic Stock Center specifically recommends biological filtration in filtered aquaria and warns that rapidly circulating water is stressful. Merck's 2026 amphibian husbandry guidance likewise notes that some aquatic amphibians need gentle filtration that keeps water clean without strong currents.</p>

<h2>How does a sponge filter work?</h2>
<p>An air-driven sponge filter pulls aquarium water through porous foam as rising bubbles move water up a lift tube. The sponge provides surface area for biological filtration while also trapping some suspended debris. The bubble column creates surface movement and gas exchange.</p>
<p>Because the water is drawn through a broad sponge rather than a narrow powered intake, the intake itself is generally gentle. Actual circulation still depends on the air pump, sponge size, lift-tube design and tank layout, so “sponge filter” should not be treated as a fixed flow rate.</p>

<h2>What are the advantages of a sponge filter?</h2>
<ul>
<li><strong>Simple biological filtration:</strong> one piece of foam can support biofilm and catch coarse debris.</li>
<li><strong>Gentle water movement:</strong> air-driven circulation is easy to keep mild for an axolotl tank.</li>
<li><strong>Easy inspection and maintenance:</strong> you can see when the sponge is dirty and clean it without opening a sealed filter body.</li>
<li><strong>Low complexity:</strong> fewer hoses, seals and moving water-system parts.</li>
<li><strong>Useful redundancy:</strong> a mature sponge filter can supplement another filter or provide a seeded biological filter for a quarantine/grow-out setup.</li>
</ul>

<h2>What are the limitations of a sponge filter?</h2>
<p>A sponge filter usually provides less fine mechanical “polishing” than a multi-stage canister and offers little room for specialized media. A single small sponge can also be undersized for a large or heavily stocked aquarium even though the current feels gentle.</p>
<p>If debris stays suspended or water-quality trends show that the system is not coping with the actual load, the answer may be more media capacity, better waste removal, a second filter, or a different filter design—not simply more air flow through the same small sponge.</p>

<h2>How does a canister filter work?</h2>
<p>A canister filter uses a pump to draw aquarium water through an external sealed body containing mechanical and biological media, then returns the filtered water to the tank. Most canisters can hold multiple layers or baskets, which lets the keeper separate coarse debris capture from biological media and optional chemical media.</p>
<p>This design can provide substantial media capacity, but the return is powered. The important axolotl question is therefore not merely the pump's advertised flow number; it is whether the return can be configured so the animal experiences gentle circulation.</p>

<h2>What are the advantages of a canister filter?</h2>
<ul>
<li><strong>More media capacity:</strong> useful when you want substantial mechanical and biological filtration in one unit.</li>
<li><strong>Better fine-debris capture:</strong> multiple mechanical stages can improve water clarity when maintained correctly.</li>
<li><strong>Configurable media:</strong> baskets can be assigned to mechanical, biological or special-purpose media.</li>
<li><strong>Flexible return plumbing:</strong> spray bars and other return arrangements can spread water movement across a wider area.</li>
<li><strong>External equipment loop:</strong> some aquarium chillers and other devices can be installed in compatible external plumbing, provided all manufacturer flow and pressure requirements are met.</li>
</ul>

<h2>What are the limitations of a canister filter?</h2>
<ul>
<li>higher cost and more complex maintenance;</li>
<li>hoses, seals and an impeller add potential failure points;</li>
<li>the outlet can create a concentrated current if it is not dispersed;</li>
<li>a dirty mechanical stage can reduce actual flow and filter performance; and</li>
<li>manufacturer “tank size” labels do not tell you whether the outlet pattern is appropriate for an axolotl.</li>
</ul>
<p>A canister's stronger pump is not automatically a disadvantage if the return is well controlled, just as a sponge filter is not automatically sufficient merely because it is gentle.</p>

<h2>Which filter gives better biological filtration?</h2>
<p><strong>It depends on the amount and condition of colonized media, not simply on the filter category.</strong> Both sponge and canister filters can provide effective biological filtration. A canister often has more space for dedicated biological media; a large mature sponge can also support substantial biofilm.</p>
<p>Merck's aquatic-life-support guidance emphasizes high surface area, oxygen and correct water chemistry for biofilter organisms. It does not establish a universal rule that ceramic rings always support a fixed multiple of the bacteria found on sponge foam.</p>

<h2>Which filter gives better mechanical filtration?</h2>
<p>A canister usually has the advantage when fine debris capture is important because water can pass through staged coarse and fine media. Sponge filters capture debris too, but the same foam commonly performs both biological and mechanical roles and may not polish fine particles as effectively.</p>
<p>Mechanical filtration should remove trapped organic waste from the system before it decomposes; Merck's aquatic-system guidance places mechanical filtration before biofiltration in larger recirculating designs for that reason.</p>

<h2>Which filter is better for low flow?</h2>
<p>A sponge filter is often the easier low-flow starting point because its circulation is air-driven and distributed. A canister can also work well when the return is spread through a spray bar, aimed against glass, throttled within the manufacturer's permitted operating range, or otherwise configured to avoid a concentrated jet.</p>
<p><strong>There is no evidence-based universal axolotl threshold of 100 GPH, 5× turnover or 10× turnover.</strong> Judge the animal's actual environment and use measured water quality to make sure reducing current has not also compromised filtration.</p>

<h2>Do you need a pre-filter sponge on a canister intake?</h2>
<p>A pre-filter sponge can be useful: it catches coarse debris before it reaches the canister and can reduce the chance that small body parts or food are drawn directly against an intake. Whether it is necessary depends on the intake design and animal size. Treat it as a practical risk-control option rather than a universal requirement.</p>
<p>If you add one, clean it often enough that it does not become a clogged waste trap.</p>

<h2>Can you run a sponge and canister together?</h2>
<p>Yes. Running both can provide redundancy and let the sponge remain as an established biological filter while the canister handles more mechanical debris. This is optional, not a requirement. Two filters are only useful if their combined circulation remains appropriate and both are maintained.</p>

<h2>Which filter should a beginner choose?</h2>
<p><strong>Choose a sponge filter when simplicity, low cost and easy gentle circulation are the main priorities.</strong> Choose a canister when you need more media capacity, stronger mechanical filtration, or compatible external plumbing and are comfortable maintaining the extra equipment.</p>
<p>For many home tanks, either can work. The decision should follow the aquarium's actual volume, animal load, water-quality trend, desired debris capture, noise tolerance, maintenance preference and equipment plan.</p>

<h2>Canister vs sponge: decision checklist</h2>
<div class="table-wrap"><table>
<thead><tr><th>If this matters most...</th><th>Lean toward...</th></tr></thead>
<tbody>
<tr><td>Lowest complexity and easiest gentle flow</td><td>Sponge filter</td></tr>
<tr><td>Large configurable media capacity</td><td>Canister filter</td></tr>
<tr><td>Fine mechanical water polishing</td><td>Canister filter</td></tr>
<tr><td>Simple backup/seeded biological filter</td><td>Sponge filter</td></tr>
<tr><td>Inline equipment compatibility</td><td>Canister/external loop, after checking manufacturer specs</td></tr>
<tr><td>Maximum redundancy</td><td>Both, if circulation remains gentle</td></tr>
</tbody></table></div>

<h2>Sources</h2>
<ul>
<li><a href="https://ambystoma.uky.edu/education1/guide-to-axolotl-husbandry">Ambystoma Genetic Stock Center: Guide to Axolotl Husbandry</a></li>
<li><a href="https://ambystoma.uky.edu/genetic-stock-center/documents/AGSC%20_Guide_2024.pdf">Ambystoma Genetic Stock Center: Axolotl Guide 2024</a></li>
<li><a href="https://www.merckvetmanual.com/all-other-pets/amphibians/housing-for-amphibians">Merck Veterinary Manual: Housing for Amphibians, updated February 2026</a></li>
<li><a href="https://www.merckvetmanual.com/exotic-and-laboratory-animals/aquatic-systems/aquatic-life-support-system-components">Merck Veterinary Manual: Aquatic Life Support System Components</a></li>
</ul>
'''


BODY_OVERRIDES["diet/fasting-and-vacation"] = r'''
<p><strong>There is no well-established research-based number of days that every healthy axolotl can safely go without food.</strong> Age, body condition, normal feeding schedule, temperature, health and recent intake all matter. For vacation planning, use the animal's normal feeding frequency and arrange a competent person to monitor the tank rather than treating an internet “maximum fasting window” as a safety guarantee.</p>
<div class="role-note"><strong>This page owns planned food gaps and vacations.</strong> If your axolotl has unexpectedly stopped eating, use <a href="/health/refusing-to-eat/">Axolotl Not Eating?</a> instead.</div>

<h2>How often are axolotls normally fed?</h2>
<p>The Ambystoma Genetic Stock Center's current 2024 research guide feeds newly feeding larvae frequently, then reduces feeding as animals grow; its husbandry timeline lists adult pelleted food about twice weekly in its system. The older AGSC husbandry guide describes adults around one year old being fed three or four times per week.</p>
<p>Those are husbandry schedules, not proof that an adult can safely be left unfed for a specific number of days. They do show why missing one scheduled adult feeding is a different situation from withholding food from a rapidly growing larva.</p>

<h2>How long can an adult axolotl go without food?</h2>
<p><strong>Do not use “14 days,” “21 days,” or any other fixed number as a universal safe limit.</strong> We did not find an axolotl study establishing a validated maximum fasting duration for healthy pets. An adult normally fed only a few times each week has more spacing between meals than a larva or small juvenile, but planned absence should still include monitoring of the animal and aquarium.</p>
<p>A thin adult, an animal recovering from illness, a breeding female, or an axolotl with recent appetite loss should not be treated like a healthy well-conditioned adult simply because they are the same age.</p>

<h2>How long can juvenile or baby axolotls go without food?</h2>
<p><strong>Young animals should not be assigned a “safe fasting window” from an age chart.</strong> AGSC feeds newly hatched larvae daily once they begin feeding and gradually transitions them to larger foods as they grow. Young animals are actively growing and are normally offered food much more frequently than adults.</p>
<p>If you will miss normal feedings for a larva or juvenile, arrange a trained sitter rather than planning a multi-day fast around an unsupported number.</p>

<h2>Does cold water make fasting safer?</h2>
<p>Axolotls are ectotherms, so temperature affects metabolism, but that does not justify deliberately chilling an animal to extend a vacation fast. Keep the aquarium in its normal stable husbandry range. Temperature manipulation can create additional stress and should not be used as a substitute for a feeding or monitoring plan.</p>

<h2>Can you leave an adult axolotl alone for a short trip?</h2>
<p>A healthy adult whose normal feeding schedule already includes days between meals may not need food every day. The bigger vacation risk is often <strong>lack of monitoring</strong>: filter failure, power outage, rising temperature, a leak or deteriorating water quality can become serious even if missing a meal would not.</p>
<p>For any absence longer than the gap you normally leave between feedings, arrange someone who can inspect the animal and equipment and follow written instructions.</p>

<h2>What should you do before a vacation?</h2>
<ol>
<li><strong>Test the water several days before departure.</strong> Correct problems before the trip rather than making a large last-minute change.</li>
<li><strong>Perform normal maintenance.</strong> Use the <a href="/tank-setup/water-change-guide/">Water Change Guide</a>; do not invent an oversized “vacation water change.”</li>
<li><strong>Check the filter and cooling system.</strong> Confirm normal operation without replacing mature biological media just before leaving.</li>
<li><strong>Remove waste and uneaten food.</strong></li>
<li><strong>Feed the normal scheduled portion.</strong> Do not double-feed “to store food up.”</li>
<li><strong>Write sitter instructions.</strong> Include temperature, what to feed, exact portions, what not to add, and who to call.</li>
</ol>

<h2>Is a pet sitter better than an automatic feeder?</h2>
<p><strong>For most axolotl vacations, a competent person is more useful than an automatic feeder.</strong> A sitter can see a leak, cooling failure, abnormal posture, dead equipment or spoiled food. Automatic feeders vary in reliability and may dispense food that an axolotl does not eat promptly.</p>
<p>If a feeder is used, test the exact device and food in advance while you are home. Do not first deploy it on departure day.</p>

<h2>What should the sitter actually do?</h2>
<div class="table-wrap"><table>
<thead><tr><th>Task</th><th>Instruction</th></tr></thead>
<tbody>
<tr><td>Temperature</td><td>Read and record the thermometer; contact you if outside the written normal range.</td></tr>
<tr><td>Animal check</td><td>Confirm normal posture, breathing, movement and absence of injury or major swelling.</td></tr>
<tr><td>Feeding</td><td>Feed only the pre-portioned amount on the written schedule; remove leftovers.</td></tr>
<tr><td>Equipment</td><td>Confirm filter and cooling equipment are operating normally.</td></tr>
<tr><td>Emergency</td><td>Use your vet/contact instructions rather than improvising baths, medication or temperature changes.</td></tr>
</tbody></table></div>

<h2>Should you overfeed before leaving?</h2>
<p>No. Give the animal its normal meal on its normal schedule. An extra-large meal can create uneaten food, regurgitation or extra waste and does not create a validated reserve that guarantees a longer safe fast.</p>

<h2>What should you do when you return?</h2>
<p>Inspect the animal, check temperature and water quality, remove any waste and resume the normal feeding schedule. There is no evidence-based rule that every axolotl must receive a “half-size restart meal” after a certain number of fasting days.</p>
<p>If the animal is unexpectedly refusing food, losing body condition or showing other signs, switch to <a href="/health/refusing-to-eat/">the appetite-loss health guide</a> rather than continuing to treat the situation as planned fasting.</p>

<h2>When is a feeding gap no longer a vacation question?</h2>
<p>It becomes a health question when the axolotl refuses food unexpectedly, loses weight or body condition, develops swelling or abnormal buoyancy, has skin/gill changes, becomes markedly lethargic, or continues to decline. Contact an amphibian-experienced veterinarian for concerning or persistent changes.</p>

<h2>Sources</h2>
<ul>
<li><a href="https://ambystoma.uky.edu/genetic-stock-center/documents/AGSC%20_Guide_2024.pdf">Ambystoma Genetic Stock Center: Axolotl Guide 2024 — feeding timeline</a></li>
<li><a href="https://ambystoma.uky.edu/education1/guide-to-axolotl-husbandry">Ambystoma Genetic Stock Center: Guide to Axolotl Husbandry — feeding and routine care</a></li>
</ul>
<p><strong>Evidence note:</strong> these sources describe feeding schedules; they do not validate a universal maximum fasting duration for pet axolotls.</p>
'''

BODY_OVERRIDES["health/impaction-symptoms-treatment"] = r'''
<p><strong>“Impaction” means a gastrointestinal foreign body or blockage, but appetite loss, swelling, reduced feces and abnormal floating do not confirm one from appearance alone.</strong> Amphibians can swallow gravel and other enclosure material, and axolotl foreign bodies have been confirmed and removed using veterinary imaging, endoscopy and surgery.</p>
<div class="role-note"><strong>This page owns suspected gastrointestinal blockage.</strong> For substrate prevention use <a href="/tank-setup/substrate-and-impaction/">the substrate guide</a>; for gravel specifically use <a href="/tank-setup/gravel-risks/">Gravel Risks</a>. Do not use this page as a reason to fridge or medicate an animal without diagnosis.</div>

<h2>What is axolotl impaction?</h2>
<p>A gastrointestinal foreign body is a swallowed non-food item that partially or completely obstructs the digestive tract. Veterinary Partner uses the broader amphibian term <em>gastrointestinal foreign body</em> or impaction, while <em>gastrointestinal overload</em> describes excessive food volume distending the stomach.</p>
<p>Gravel and other enclosure material are recognized amphibian foreign-body risks, and published axolotl case reports document gastric foreign bodies requiring endoscopic or surgical removal.</p>

<h2>What signs can occur with a gastrointestinal blockage?</h2>
<p>Possible signs include appetite loss, abdominal enlargement, reduced fecal output, abnormal buoyancy, lethargy or other changes in behavior. These signs are <strong>not specific</strong>. Overfeeding, parasites, infection, reproductive problems, fluid accumulation and other disease can look similar.</p>
<p>That is why “not eating + floating = impaction” is not an adequate diagnosis.</p>

<h2>What makes a foreign body more plausible?</h2>
<ul>
<li>known access to swallowable gravel, stones, moss or other enclosure material;</li>
<li>a witnessed ingestion event;</li>
<li>persistent abdominal distension after such exposure;</li>
<li>continuing appetite or fecal changes; or</li>
<li>diagnostic imaging that identifies a foreign object.</li>
</ul>
<p>Absence of visible gravel in feces does not prove there is an obstruction, and absence of feces for a particular number of days does not prove one either.</p>

<h2>Impaction vs constipation: can you tell at home?</h2>
<p><strong>Not reliably from external signs alone.</strong> “Constipation” is often used informally for slowed fecal passage, while a foreign-body obstruction is a physical blockage. They can overlap in appetite, swelling and fecal changes, but their management may differ substantially.</p>
<p>A veterinarian may use history, physical examination, fecal testing, radiographs, contrast imaging or ultrasound to distinguish gastrointestinal disease and locate a foreign body.</p>

<h2>Should you fridge an axolotl for impaction?</h2>
<p><strong>MyAxolotl does not recommend refrigerator fridging as a standard first-line impaction treatment.</strong> We did not find a veterinary source establishing 5°C refrigerator treatment for 1–2 weeks as a validated way to clear an axolotl foreign body. Cooling also slows metabolism and gut activity, so the common claim that extreme cold “makes the blockage pass” should not be presented as established physiology.</p>
<p>The separate <a href="/health/fridging-sick-axolotl/">fridging guide</a> explains why refrigeration should only be considered when an amphibian-experienced veterinarian specifically recommends it for the individual animal.</p>

<h2>Should you stop feeding?</h2>
<p>If a true obstruction is strongly suspected, do not force-feed or repeatedly add large meals while arranging veterinary assessment. However, a long unsupervised fast is not a substitute for diagnosis. The correct feeding plan depends on whether the problem is a foreign body, overload, another gastrointestinal disease or something unrelated to the gut.</p>

<h2>What should you do first?</h2>
<ol>
<li><strong>Remove access to the suspected foreign material.</strong> Move the animal only if needed to prevent continued ingestion or injury.</li>
<li><strong>Measure water quality and temperature.</strong> Correct husbandry problems without creating abrupt swings.</li>
<li><strong>Document the timeline.</strong> Record last normal meal, last observed feces, known ingestion, swelling, buoyancy and weight/body-condition change.</li>
<li><strong>Do not massage the abdomen.</strong> External pressure on a swallowed hard or sharp object can add risk.</li>
<li><strong>Do not give human laxatives or improvised medication.</strong></li>
<li><strong>Contact an amphibian/exotics veterinarian</strong> when signs persist, the animal is worsening, or foreign-body ingestion is likely.</li>
</ol>

<h2>How does a veterinarian diagnose impaction?</h2>
<p>Veterinary amphibian guidance describes radiographs, contrast studies and ultrasound as tools for investigating foreign bodies or gastrointestinal distension. Published axolotl cases have used radiography and direct visualization before foreign bodies were removed.</p>
<p>Dense gravel may be visible on radiographs; other material can be more difficult to detect and may require additional imaging or endoscopy.</p>

<h2>How can a foreign body be treated?</h2>
<p>Treatment depends on the object's location, size and effect on the animal. Veterinary Partner describes options including decompression, removal through the mouth, endoscopic retrieval and surgical removal. Axolotl case reports document successful endoscopic retrieval and gastric surgery under amphibian anesthesia.</p>
<p>Those procedures are veterinary interventions, not home techniques.</p>

<h2>When is the situation urgent?</h2>
<p>Seek prompt veterinary care for severe or increasing abdominal distension, inability to maintain normal position, prolapse, respiratory difficulty, marked lethargy, rapid decline, obvious painful trauma, or a known swallowed foreign body with continuing symptoms.</p>
<p>Use <a href="/health/emergency-first-aid/">Axolotl Emergency Signs</a> for triage.</p>

<h2>How do you prevent impaction?</h2>
<p>Prevention is more reliable than home treatment:</p>
<ul>
<li>avoid swallowable gravel and loose stones;</li>
<li>choose substrate using <a href="/tank-setup/substrate-and-impaction/">the substrate guide</a>;</li>
<li>remove broken décor and small foreign objects;</li>
<li>feed appropriately sized foods; and</li>
<li>observe feeding so the axolotl is not repeatedly suctioning food from unsafe material.</li>
</ul>

<h2>Which page owns each related problem?</h2>
<div class="table-wrap"><table>
<thead><tr><th>Question</th><th>Owner</th></tr></thead>
<tbody>
<tr><td>Which substrate should I use?</td><td><a href="/tank-setup/substrate-and-impaction/">Substrate & Impaction Prevention</a></td></tr>
<tr><td>Why is gravel dangerous?</td><td><a href="/tank-setup/gravel-risks/">Gravel Risks</a></td></tr>
<tr><td>My axolotl is floating</td><td><a href="/health/why-axolotl-floating/">Floating Guide</a></td></tr>
<tr><td>My axolotl stopped eating</td><td><a href="/health/refusing-to-eat/">Refusing to Eat</a></td></tr>
<tr><td>Is my axolotl overfed?</td><td><a href="/diet/overfeeding-and-impaction/">Body Condition / Overfeeding</a></td></tr>
</tbody></table></div>

<h2>Sources</h2>
<ul>
<li><a href="https://veterinarypartner.vin.com/default.aspx?catId=253985&amp;id=8030801&amp;ind=1817&amp;objTypeID=1007&amp;pid=19239">Veterinary Partner / VIN: Gastrointestinal Foreign Body or Overload in Amphibians</a></li>
<li><a href="https://pubmed.ncbi.nlm.nih.gov/31120693/">Burns et al.: Endoscopic removal of a foreign body in a Mexican axolotl</a></li>
<li><a href="https://pubmed.ncbi.nlm.nih.gov/21988819/">McMillan & Leece: anesthesia for surgical retrieval of gastric foreign bodies in an axolotl</a></li>
<li><a href="https://members.arav.org/resource/resmgr/files/proceedings_2016/Chapter_28_-_Clinical_Review.pdf">ARAV clinical review: surgical gastric foreign-body removal in a juvenile Mexican axolotl</a></li>
</ul>
'''


BODY_OVERRIDES["tank-setup/aquarium-chillers"] = r'''
<p><strong>An aquarium chiller is useful when room cooling, ventilation and evaporative methods cannot keep an axolotl tank reliably within the temperature range you have chosen for husbandry.</strong> Do not size a chiller from tank gallons alone. Total water volume, warmest room temperature, desired water temperature, pump/light heat, ventilation and the chiller's required water-flow range all affect performance.</p>
<div class="role-note"><strong>This page owns the chiller buying decision.</strong> For normal axolotl temperature husbandry and non-chiller cooling methods, use <a href="/tank-setup/temperature/">the temperature guide</a>. For a planning estimate, use the <a href="/tools/chiller-size-calculator/">Chiller Size Calculator</a>.</div>

<h2>Does every axolotl tank need a chiller?</h2>
<p>No. A chiller is equipment for a thermal-control problem, not a universal requirement. The Ambystoma Genetic Stock Center maintains its research colony around 15–17°C using building and auxiliary air cooling. Merck's amphibian husbandry guidance says water chillers and air conditioning should be considered when needed to keep amphibians within their appropriate temperature range.</p>
<p>If your room and aquarium remain reliably cool without a chiller, adding one only increases cost and complexity. If the tank repeatedly warms beyond your intended range, a correctly sized compressor chiller can provide much more predictable control than emergency cooling.</p>

<h2>What type of aquarium chiller should you consider?</h2>
<p>For a tank that needs a meaningful, sustained temperature pull-down below a warm room, a compressor-based aquarium chiller is the usual dedicated solution. Thermoelectric/Peltier devices can be useful for small heat loads but their practical cooling capacity depends heavily on ambient conditions and device design.</p>
<p><strong>Do not choose solely by the label “compressor” or “thermoelectric.”</strong> Compare the manufacturer's actual temperature-pull-down data, rated water volume, flow requirement and ventilation instructions for your setup.</p>

<h2>What determines chiller size?</h2>
<div class="table-wrap"><table>
<thead><tr><th>Factor</th><th>Why it matters</th></tr></thead>
<tbody>
<tr><td>Total system water volume</td><td>More water requires more heat removal.</td></tr>
<tr><td>Warmest room temperature</td><td>A hotter room increases the heat entering the aquarium and the required pull-down.</td></tr>
<tr><td>Target water temperature</td><td>The larger the difference between ambient and target, the harder the chiller must work.</td></tr>
<tr><td>Pumps, lights and other equipment</td><td>Electrical equipment can add heat to the system.</td></tr>
<tr><td>Open vs covered tank</td><td>Evaporation, lighting and ventilation change the heat balance.</td></tr>
<tr><td>Chiller ventilation</td><td>A compressor unit dumps removed heat into the surrounding room; recirculating hot exhaust reduces performance.</td></tr>
<tr><td>Actual water flow through the chiller</td><td>The heat exchanger must operate within the manufacturer's specified flow range.</td></tr>
</tbody></table></div>

<h2>Why tank volume alone is not enough</h2>
<p>A 40-gallon aquarium in a cool basement does not impose the same cooling load as the same aquarium in a hot upstairs room with pumps and lights adding heat. Manufacturer sizing notes for current aquarium chillers explicitly tell buyers to consider room temperature, desired temperature drop, equipment heat and ventilation—not only gallons.</p>
<p>This is why a generic table saying “40 gallons = 1/5 HP” is unreliable. The same nominal tank can require different chiller capacity under different conditions.</p>

<h2>How do you use the Chiller Size Calculator?</h2>
<p>The <a href="/tools/chiller-size-calculator/">Axolotl Chiller Size Calculator</a> asks for tank volume, warmest observed water/room conditions, target temperature and heat load, then returns a planning class. Treat the result as a shortlist, not the final purchase decision.</p>
<p>Before buying, compare that shortlist with the current manufacturer's sizing chart and flow range for the exact model.</p>

<h2>Why does flow rate matter?</h2>
<p>Inline chillers require water to pass through the heat exchanger within a specified range. Too little or too much flow can reduce performance or fall outside the manufacturer's operating specification. Pump labels usually quote flow at little or no head pressure, while actual flow drops through tubing, height, bends, filters and fittings.</p>
<p>Use the chiller manufacturer's <strong>minimum and maximum operating flow</strong> and estimate or measure the real flow through the installed loop.</p>

<h2>Can a canister filter run through a chiller?</h2>
<p>Sometimes. A canister filter can provide the circulation loop for an inline chiller when the filter's real output remains within the chiller's required flow range after head loss and plumbing restrictions. The filter manufacturer must also permit the plumbing arrangement.</p>
<p>If the combination falls outside either device's specification, use a separate pump or different plumbing design. Do not choose a canister solely because its box GPH appears to match a chiller.</p>

<h2>How much ventilation does a chiller need?</h2>
<p><strong>Do not enclose a compressor chiller in a sealed cabinet unless the manufacturer explicitly permits it.</strong> The unit removes heat from aquarium water and rejects that heat into room air. Current JBJ guidance and retailer installation notes both emphasize adequate ventilation and avoiding recirculation of warm exhaust.</p>
<p>Follow the exact clearance requirements in the model's current manual rather than a generic “12 inches on every side” rule.</p>

<h2>What features should you compare?</h2>
<ul>
<li><strong>Pull-down capacity:</strong> can it maintain your target under the warmest expected room conditions?</li>
<li><strong>Required flow range:</strong> compatible with your real pump/filter flow?</li>
<li><strong>Heat exchanger material:</strong> suitable for continuous aquarium use.</li>
<li><strong>Controller range and accuracy:</strong> adequate for the temperature you intend to maintain.</li>
<li><strong>Ventilation requirements:</strong> practical for where the unit will sit.</li>
<li><strong>Noise:</strong> check current owner/manufacturer data if bedroom placement matters.</li>
<li><strong>Warranty and service:</strong> verify current terms at purchase time.</li>
<li><strong>Replacement parts:</strong> availability of controller, fan, fuse and plumbing components.</li>
</ul>

<h2>Should you buy one size larger?</h2>
<p>A modest capacity margin can reduce continuous operation under peak heat load, but “always oversize” is not a universal engineering law. Follow the manufacturer's current sizing method. Some manufacturers recommend moving up when your system sits near the edge of a model's rating or requires a large temperature pull-down.</p>
<p>Oversizing also affects purchase price, physical size, pump/flow requirements and cycling behavior, so compare the actual model data rather than applying a fixed 1.5× multiplier.</p>

<h2>Can a fan replace a chiller?</h2>
<p>Surface fans cool water through evaporation. Their effect depends on room temperature, humidity, airflow, tank surface area and evaporation rate, so there is no universal “2–4°F” result. A fan can be enough in some rooms and inadequate in others.</p>
<p>Test your real tank during the warmest conditions you expect. If temperature cannot be held reliably, move to room air conditioning or a properly sized chiller instead of waiting for a heat emergency.</p>

<h2>How should you install a chiller?</h2>
<ol>
<li>Place it on a stable surface with the ventilation clearance specified by its manual.</li>
<li>Use tubing and fittings approved for the unit.</li>
<li>Provide water flow within the manufacturer's operating range.</li>
<li>Check all connections for leaks before unattended operation.</li>
<li>Use an independent aquarium thermometer to verify the chiller/controller reading.</li>
<li>Monitor the tank after installation to make sure the return flow is still gentle enough for the axolotl.</li>
</ol>

<h2>How much does a chiller cost to run?</h2>
<p>Operating cost depends on the model's real electrical draw, local electricity price and compressor duty cycle. Do not estimate cost from horsepower alone. Use the manufacturer's wattage/amp specification and your own measured or expected run time.</p>
<p>A simple estimate is:</p>
<p><strong>kWh per day = device kilowatts × compressor run hours per day</strong></p>
<p>Then multiply by your electricity price per kWh. Actual duty cycle changes with room temperature, insulation, ventilation and tank heat load.</p>

<h2>How do you maintain a chiller?</h2>
<p>Follow the model manual. Common tasks include keeping air intakes/condenser surfaces free of dust, checking tubing for restriction or leaks, maintaining the required water flow and confirming temperature with an independent thermometer. Service intervals vary by model and environment.</p>

<h2>Current product example: how to read a specification sheet</h2>
<p>As of September 2026, JBJ's current Arctica aquarium-series page publishes each model's compressor/output rating, titanium heat exchanger, inlet/outlet sizes and minimum/maximum flow range, and points buyers to a manufacturer chiller-sizing calculator. Those are the kinds of fields you should compare.</p>
<p><strong>This page does not rank one current model “best overall.”</strong> Model availability, warranty terms, pricing and specifications can change, while the sizing method above remains useful.</p>

<h2>Sources</h2>
<ul>
<li><a href="https://ambystoma.uky.edu/genetic-stock-center/documents/AGSC%20_Guide_2024.pdf">Ambystoma Genetic Stock Center: Axolotl Guide 2024 — colony temperature</a></li>
<li><a href="https://ambystoma.uky.edu/education1/guide-to-axolotl-husbandry">Ambystoma Genetic Stock Center: Guide to Axolotl Husbandry</a></li>
<li><a href="https://www.merckvetmanual.com/exotic-and-laboratory-animals/amphibians/environment-and-husbandry-for-amphibians">Merck Veterinary Manual: Environment and Husbandry for Amphibians, updated February 2026</a></li>
<li><a href="https://www.jbjaquarium.com/temperature-control/arctica-chillers/aquarium-series/">JBJ Aquariums: current Arctica Aquarium Series specifications</a></li>
</ul>
'''


# ---------------------------------------------------------------------------
# P0 hub rewrites — care guide + tank setup (2026-09-19)
# ---------------------------------------------------------------------------
# These pages are intentionally broad routers. Specialist pages own exact
# procedures, thresholds, diagnosis, and buying decisions.

INTRO_OVERRIDES["axolotls/care-guide"] = (
    "Axolotl care is built around a cool, stable aquatic environment, an established "
    "biological filter, safe housing, appropriate food, regular water testing, and "
    "early recognition of health changes. This guide gives the whole system in one "
    "place and routes each specialist task to its canonical page."
)

INTRO_OVERRIDES["tank-setup/setup-guide"] = (
    "Set up the aquarium before the axolotl arrives: choose a long tank with enough "
    "usable floor area, establish gentle biological filtration, make temperature "
    "control reliable, choose safe substrate and hides, and confirm the nitrogen "
    "cycle with measured water tests."
)

BODY_OVERRIDES["axolotls/care-guide"] = r'''
<p><strong>Good axolotl care is mostly environmental management.</strong> Keep the animal in a cool, stable freshwater aquarium with established biological filtration, gentle circulation, safe surfaces, appropriate food and regular water testing. Avoid trying to diagnose or treat a health problem from one visible sign; measure the environment first and use the specialist health page for the specific symptom.</p>
<div class="role-note"><strong>This is the overview page.</strong> It owns the broad “how do I care for an axolotl?” question. Tank size, temperature, water chemistry, feeding schedules, specific diseases, legality and buying decisions are owned by the specialist guides linked below.</div>

<h2>Axolotl care at a glance</h2>
<div class="table-wrap"><table>
<thead><tr><th>Care area</th><th>Practical rule</th><th>Detailed guide</th></tr></thead>
<tbody>
<tr><td>Tank</td><td>Use a long aquarium with enough floor area and water volume. Petco currently recommends 20+ gallons for one adult; MyAxolotl prefers a 40-gallon breeder when starting a permanent adult setup if space and budget allow.</td><td><a href="/tank-setup/tank-size-by-age/">Tank Size</a></td></tr>
<tr><td>Temperature</td><td>Keep water cool and stable; do not rely on how the water feels by hand.</td><td><a href="/tank-setup/temperature/">Temperature</a></td></tr>
<tr><td>Filtration</td><td>Use established biological filtration with circulation gentle enough that the animal can rest normally.</td><td><a href="/tank-setup/filtration-for-axolotls/">Filtration</a></td></tr>
<tr><td>Water testing</td><td>Measure ammonia, nitrite, nitrate, pH and temperature regularly instead of judging water by clarity.</td><td><a href="/tank-setup/how-to-test-water/">How to Test Water</a></td></tr>
<tr><td>Water changes</td><td>Use regular partial water changes and adjust maintenance from measured water quality and waste load.</td><td><a href="/tank-setup/water-change-guide/">Water Change Guide</a></td></tr>
<tr><td>Substrate</td><td>Avoid loose material that can be swallowed; choose substrate by animal size and setup.</td><td><a href="/tank-setup/substrate-and-impaction/">Substrate Guide</a></td></tr>
<tr><td>Food</td><td>Feed appropriate animal-based foods in portions and frequency suited to life stage and body condition.</td><td><a href="/diet/best-foods-list/">Diet Guide</a></td></tr>
<tr><td>Handling</td><td>Treat axolotls as observation-focused aquatic pets; handle only when necessary.</td><td><a href="/care-basics/handling/">Handling</a></td></tr>
<tr><td>Health</td><td>Record changes, test the environment and follow the page for the specific sign.</td><td><a href="/health/">Health Hub</a></td></tr>
</tbody></table></div>

<h2>What is an axolotl?</h2>
<p><em>Ambystoma mexicanum</em> is a Mexican salamander that normally becomes reproductively mature while retaining an aquatic body plan, including external gills. This developmental strategy is commonly described as paedomorphosis or neoteny.</p>
<p>For the entity definition and core facts, use <a href="/care-basics/axolotl-facts/">What Is an Axolotl?</a>. For fish-versus-amphibian classification, use <a href="/biology-and-science/is-axolotl-amphibian/">Is an Axolotl an Amphibian?</a>.</p>

<h2>Is an axolotl the right pet for you?</h2>
<p>An axolotl can suit someone who is comfortable maintaining an aquarium and prefers an animal that is watched rather than handled. The main commitment is not daily interaction; it is keeping the environment consistently appropriate over many years.</p>
<p>Before buying, make sure you can:</p>
<ul>
<li>maintain cool water in your actual room through the hottest part of the year;</li>
<li>test water chemistry and understand the nitrogen cycle;</li>
<li>provide an appropriately sized aquarium and stand;</li>
<li>source suitable food consistently;</li>
<li>arrange exotic/amphibian veterinary care if needed; and</li>
<li>verify that ownership and transport are legal where you live.</li>
</ul>
<p>Use <a href="/care-basics/are-axolotls-good-beginner-pets/">Are Axolotls Good Pets?</a> for the pros, cons and beginner-difficulty decision.</p>

<h2>What size tank does an adult axolotl need?</h2>
<p><strong>Use the dedicated tank-size page as the source of truth.</strong> Current Petco care guidance recommends a minimum of 20+ gallons for one adult and says length matters more than height. MyAxolotl treats a 20-gallon long as the practical lower bound and prefers a 40-gallon breeder as a more forgiving permanent home when space and budget permit.</p>
<p>The larger recommendation is a practical site preference, not a claim that one exact gallon number is a universal biological threshold. Animal number, floor area, filtration and husbandry intensity all matter.</p>
<p>See <a href="/tank-setup/tank-size-by-age/">What Size Tank Does an Axolotl Need?</a>.</p>

<h2>How cool should axolotl water be?</h2>
<p><strong>Cool and stable matters more than chasing one magic number.</strong> The Ambystoma Genetic Stock Center maintains its research colony in cool water, and current amphibian veterinary guidance emphasizes species-appropriate stable temperature because temperature affects metabolism and immune function.</p>
<p>For a home aquarium, measure the water continuously or at least daily during warm periods and build a cooling plan around the warmest room conditions you actually experience. A fan, room air conditioning or an aquarium chiller may be appropriate depending on the heat load.</p>
<p>Use <a href="/tank-setup/temperature/">Axolotl Tank Temperature</a> for the current home target and <a href="/tank-setup/aquarium-chillers/">Aquarium Chillers</a> if active cooling is needed.</p>

<h2>What water quality does an axolotl need?</h2>
<p>Amphibians absorb water and dissolved substances readily across their skin, so clean water is foundational. Merck's 2026 amphibian guidance advises regular testing of aquatic systems for temperature, pH, hardness, ammonia, nitrite and nitrate, and emphasizes water free from chlorine, ammonia and nitrite.</p>
<p>Do not use a broad care page to memorize a long table of fixed thresholds. Test the tank, understand the nitrogen cycle and use the specialist page to interpret the actual readings.</p>
<p>Start with <a href="/tank-setup/how-to-test-water/">How to Test Axolotl Water</a> and then use <a href="/tank-setup/water-parameters-cycling/">Water Parameters & Nitrogen Cycle</a>.</p>

<h2>Does an axolotl need a filter?</h2>
<p>For a conventional home aquarium, established biological filtration is the normal approach. The goal is enough biological capacity to process nitrogenous waste without creating a strong current across the animal's resting area.</p>
<p><strong>Do not size the filter from an invented axolotl turnover multiplier.</strong> Filter choice depends on biological-media capacity, actual waste load, mechanical debris capture and whether the output can be made gentle. See <a href="/tank-setup/filtration-for-axolotls/">Do Axolotls Need a Filter?</a> and <a href="/tank-setup/canister-vs-sponge-filter/">Canister vs Sponge</a>.</p>

<h2>How often should you change the water?</h2>
<p>Regular partial water replacement is still necessary in a filtered aquarium. The 2024 AGSC guide and Merck's 2026 pet-amphibian guidance both support routine weekly partial renewal in established aquatic systems, while the amount needed can change with measured chemistry and waste load.</p>
<p>Use <a href="/tank-setup/water-change-guide/">How to Change Axolotl Tank Water</a> rather than following an automatic percentage from an overview article.</p>

<h2>What substrate is safe?</h2>
<p><strong>Avoid loose gravel or objects small enough to be swallowed.</strong> Axolotls use suction feeding and can ingest material around the food. Substrate choice should account for animal size, grain size, cleanliness and the keeper's ability to remove waste.</p>
<p>The <a href="/tank-setup/substrate-and-impaction/">Substrate Guide</a> owns the safe-choice comparison; <a href="/tank-setup/gravel-risks/">Gravel Risks</a> explains the foreign-body hazard.</p>

<h2>What hides, plants and lighting are appropriate?</h2>
<p>Provide smooth hiding places and avoid sharp décor or openings that can trap the animal. Axolotls do not need bright display lighting for their own benefit, so any light used for viewing or plants should still leave shaded/refuge areas available.</p>
<p>For plants and décor, use <a href="/tank-setup/live-vs-artificial-plants/">Live vs Artificial Plants</a> and the <a href="/tank-setup/setup-guide/">Tank Setup Guide</a>.</p>

<h2>What do axolotls eat?</h2>
<p>Axolotls are carnivorous. Captive diets commonly use appropriately sized earthworms/nightcrawlers and nutritionally suitable sinking pellets, while larvae require much smaller live foods during early development. Feeding frequency changes with life stage, body condition, food size and the individual.</p>
<p>Use <a href="/diet/best-foods-list/">What Do Axolotls Eat?</a> for food choice and <a href="/diet/feeding-schedule-by-age/">Feeding Schedule by Age</a> for routine frequency.</p>

<h2>Can axolotls live with other animals?</h2>
<p>Do not add fish or another axolotl simply because the tank has enough gallons. Tank mates can introduce nipping, predation, food competition, disease and ingestion hazards. Multiple axolotls also need close size matching and monitoring.</p>
<p>Use <a href="/tank-setup/tank-mates/">Axolotl Tank Mates</a> for other species and <a href="/care-basics/keeping-multiple-axolotls/">Can Axolotls Live Together?</a> for same-species cohabitation.</p>

<h2>Can you hold or pet an axolotl?</h2>
<p>Routine petting is unnecessary. Amphibian skin is biologically important and easily disturbed, so handle only when the animal must be transferred for safety, veterinary care or essential husbandry.</p>
<p>Use <a href="/care-basics/handling/">Can You Hold an Axolotl?</a> for transfer methods and <a href="/care-basics/are-axolotls-poisonous/">Are Axolotls Poisonous or Dangerous?</a> for human-hygiene and bite questions.</p>

<h2>How do you know when an axolotl is unwell?</h2>
<p><strong>Look for a change from the animal's normal pattern, not one internet “diagnostic sign.”</strong> Concerning changes can involve appetite, body condition, gills, skin, wounds, buoyancy, swimming, breathing, fecal production or activity. The same sign can have more than one cause.</p>
<p>When something changes:</p>
<ol>
<li>measure temperature and water chemistry;</li>
<li>record appetite, feces, posture, behavior and recent changes;</li>
<li>take clear dated photographs if there is a visible lesion;</li>
<li>follow the specialist page for the specific sign; and</li>
<li>seek an amphibian-experienced veterinarian for severe, worsening or persistent problems.</li>
</ol>
<p>Use <a href="/health/stress-signs/">Axolotl Stress Signs</a> as the symptom router and <a href="/health/emergency-first-aid/">Axolotl Emergency Signs</a> for urgent triage.</p>

<h2>What should routine care look like?</h2>
<div class="table-wrap"><table>
<thead><tr><th>Cadence</th><th>What to do</th></tr></thead>
<tbody>
<tr><td>Daily</td><td>Check the animal, temperature and equipment; remove obvious uneaten food/waste.</td></tr>
<tr><td>Regularly / weekly</td><td>Test water chemistry, review trends and perform routine partial water replacement as needed.</td></tr>
<tr><td>As needed</td><td>Remove mechanical debris and maintain filter components without unnecessarily replacing mature biological media.</td></tr>
<tr><td>Before/after changes</td><td>Record new equipment, food, animals, treatments or major maintenance so later health changes have context.</td></tr>
</tbody></table></div>

<h2>How much does axolotl ownership cost?</h2>
<p>The animal's purchase price is only one part of ownership. Aquarium, stand, filtration, testing supplies, cooling, food, electricity and veterinary care can exceed the cost of the axolotl itself. Use <a href="/care-basics/cost-of-ownership-monthly/">Monthly Cost of Ownership</a> and <a href="/cost-and-buying/axolotl-price-by-morph/">Axolotl Price by Morph</a>.</p>

<h2>Is it legal to own an axolotl?</h2>
<p>Rules can change by country, state/province and locality. Do not rely on an old care article or a seller's willingness to ship. Check the current primary-source rules for your jurisdiction before buying or transporting an animal.</p>
<p>Use the <a href="/legal/">Axolotl Legality Guide</a>.</p>

<h2>Where should a new keeper go next?</h2>
<p>If you do not yet own the animal, continue in this order:</p>
<ol>
<li><a href="/care-basics/are-axolotls-good-beginner-pets/">Decide whether an axolotl fits your household.</a></li>
<li><a href="/legal/">Check legality.</a></li>
<li><a href="/tank-setup/setup-guide/">Build and cycle the aquarium.</a></li>
<li><a href="/cost-and-buying/where-to-buy-axolotls/">Choose a verified seller.</a></li>
<li><a href="/cost-and-buying/how-to-choose-a-healthy-axolotl/">Inspect the individual animal.</a></li>
<li><a href="/tank-setup/acclimating-a-new-axolotl/">Move it into the prepared system.</a></li>
</ol>

<h2>Sources</h2>
<ul>
<li><a href="https://ambystoma.uky.edu/genetic-stock-center/documents/AGSC%20_Guide_2024.pdf">Ambystoma Genetic Stock Center: Axolotl Guide 2024</a></li>
<li><a href="https://ambystoma.uky.edu/education1/guide-to-axolotl-husbandry">Ambystoma Genetic Stock Center: Guide to Axolotl Husbandry</a></li>
<li><a href="https://www.merckvetmanual.com/exotic-and-laboratory-animals/amphibians/environment-and-husbandry-for-amphibians">Merck Veterinary Manual: Environment and Husbandry for Amphibians, updated February 2026</a></li>
<li><a href="https://www.merckvetmanual.com/all-other-pets/amphibians/housing-for-amphibians">Merck Veterinary Manual: Housing for Amphibians, updated February 2026</a></li>
<li><a href="https://www.petco.com/pet-education/caresheets/axolotl">Petco: Axolotl Care Guide — current consumer tank-size guidance</a></li>
</ul>
'''

BODY_OVERRIDES["tank-setup/setup-guide"] = r'''
<p><strong>Set up and stabilize the aquarium before the axolotl arrives.</strong> The sequence is: choose a suitable long tank and stand, plan cooling, install gentle biological filtration, choose safe substrate and hides, fill with treated water, establish the nitrogen cycle, and confirm the system with measured water tests.</p>
<div class="role-note"><strong>This page owns the setup sequence.</strong> Exact tank-size decisions, filter comparison, temperature management, water chemistry and cycling interpretation are handled by their specialist pages so this guide does not create competing rules.</div>

<h2>Step 1: choose the tank before buying equipment</h2>
<p>For one adult, current Petco care guidance recommends a minimum of 20+ gallons and says length is more important than height. MyAxolotl treats a 20-gallon long as the practical lower bound and prefers a 40-gallon breeder as a more forgiving permanent setup when space and budget permit.</p>
<p>That preference is not a claim that one exact gallon number is a universal biological threshold. Use <a href="/tank-setup/tank-size-by-age/">What Size Tank Does an Axolotl Need?</a> for the full reasoning, including babies, juveniles and multiple adults.</p>

<h2>Step 2: choose a stable location and stand</h2>
<p>Place the aquarium where room temperature is easiest to control and where direct sun, radiators and other heat sources will not create avoidable thermal swings. The stand must be level and rated for the filled aquarium's weight.</p>
<p>If you only know the tank dimensions, use the <a href="/tools/aquarium-volume-calculator/">Aquarium Volume Calculator</a> to estimate water volume and water weight.</p>

<h2>Step 3: plan temperature control for your real room</h2>
<p><strong>Do not automatically buy a chiller and do not assume a fan will always be enough.</strong> Measure the room and tank through the warmest conditions you expect. Amphibian veterinary guidance emphasizes maintaining a species-appropriate stable temperature and notes that chillers or air conditioning may be needed for aquatic systems.</p>
<p>Use <a href="/tank-setup/temperature/">Axolotl Tank Temperature</a> for the target and non-purchase cooling methods. If active cooling is required, use <a href="/tank-setup/aquarium-chillers/">Aquarium Chillers</a> and the <a href="/tools/chiller-size-calculator/">Chiller Size Calculator</a>.</p>

<h2>Step 4: install biological filtration with gentle flow</h2>
<p>A conventional home aquarium should use established biological filtration. The filter needs enough colonized media for the actual waste load while returning water gently enough that the axolotl is not continuously pushed around the tank.</p>
<p><strong>Do not choose from a fixed “3×,” “5×,” or “10×” turnover rule.</strong> Manufacturer flow ratings do not describe the animal's actual current after media, tubing, spray bars and head loss. Choose by biological capacity, debris capture and controllable return flow.</p>
<p>Use <a href="/tank-setup/filtration-for-axolotls/">Do Axolotls Need a Filter?</a> and <a href="/tank-setup/canister-vs-sponge-filter/">Canister vs Sponge</a>.</p>

<h2>Step 5: choose safe substrate</h2>
<p>Avoid swallowable gravel and loose stones. Axolotls feed by suction and can ingest material around food. Bare-bottom housing and appropriately fine sand are common approaches, but the correct choice depends on life stage, grain size and maintenance.</p>
<p>Use <a href="/tank-setup/substrate-and-impaction/">Choosing the Best Axolotl Substrate</a>. If you are considering gravel, read <a href="/tank-setup/gravel-risks/">Gravel Risks</a> first.</p>

<h2>Step 6: add hides and safe décor</h2>
<p>Provide at least one smooth refuge large enough for the animal to use comfortably. Avoid sharp edges, small holes where the body can become trapped, unstable rockwork and small detachable objects that could be swallowed.</p>
<p>Lighting should support viewing or plants without removing the animal's ability to retreat into shade. See <a href="/tank-setup/live-vs-artificial-plants/">Live vs Artificial Plants</a> for plant/decor choices.</p>

<h2>Step 7: use a secure top when escape is possible</h2>
<p>A secure aquarium cover is useful where an axolotl could leave the tank or where household pets, objects or contaminants could enter it. Choose a cover that works with the cooling/ventilation plan and equipment rather than sealing a warm tank in a way that traps heat.</p>

<h2>Step 8: fill with appropriate treated water</h2>
<p>Municipal water may contain chlorine or chloramine. Use a conditioner or water-treatment method appropriate to the disinfectant in your supply. Do not assume that simply letting water stand removes chloramine.</p>
<p>Use <a href="/tank-setup/water-conditioners/">Water Conditioners</a> and the <a href="/tools/water-conditioner-dosage-calculator/">Water Conditioner Dosage Calculator</a> for product-volume math.</p>

<h2>Step 9: establish the biological filter before adding the axolotl</h2>
<p><strong>Do not use the axolotl as the ammonia source for a new uncycled aquarium.</strong> Establish the biofilter before the animal arrives. A cycling process uses a controlled ammonia source and water testing to demonstrate that the filter community is processing nitrogenous waste.</p>
<p>Do not declare the tank “cycled” because a certain number of weeks has passed. Confirm the process from measured ammonia, nitrite and nitrate trends. Use <a href="/tank-setup/water-parameters-cycling/">Water Parameters & Nitrogen Cycle</a> and log the readings in the <a href="/tools/nitrogen-cycle-tracker/">Nitrogen Cycle Tracker</a>.</p>

<h2>Step 10: learn to test the water correctly</h2>
<p>Before the animal arrives, you should be able to measure and record ammonia, nitrite, nitrate, pH and temperature reliably. Clear-looking water can still have unsafe chemistry.</p>
<p>Use <a href="/tank-setup/how-to-test-water/">How to Test Axolotl Water</a> for sample collection, test-kit technique and color-chart reading.</p>

<h2>Step 11: create a maintenance routine before the tank is occupied</h2>
<p>Regular testing, waste removal, partial water changes and filter maintenance are part of the setup—not tasks to invent after a problem appears. The 2024 AGSC guide and Merck's 2026 amphibian guidance both support routine partial water replacement in established aquatic systems.</p>
<p>Use <a href="/tank-setup/water-change-guide/">How to Change Axolotl Tank Water</a>. Do not replace all mature biological media on a routine calendar.</p>

<h2>Step 12: prepare food, transport and acclimation before pickup day</h2>
<p>Have the animal's normal food ready and know how the seller has been feeding it. Confirm the transport and arrival plan before purchase, especially for shipped animals.</p>
<p>Use <a href="/cost-and-buying/shipping-live-axolotls/">Shipping Live Axolotls</a> and <a href="/tank-setup/acclimating-a-new-axolotl/">Acclimating a New Axolotl</a>.</p>

<h2>What should be ready before the axolotl arrives?</h2>
<div class="table-wrap"><table>
<thead><tr><th>Item</th><th>Ready when...</th></tr></thead>
<tbody>
<tr><td>Tank and stand</td><td>Level, secure and sized for the intended animal count.</td></tr>
<tr><td>Temperature control</td><td>The tank remains in the planned range under the warmest expected room conditions.</td></tr>
<tr><td>Filter</td><td>Biological filtration is established and return flow is gentle.</td></tr>
<tr><td>Water</td><td>Source water is treated appropriately and you know how to test it.</td></tr>
<tr><td>Nitrogen cycle</td><td>Readings demonstrate a functioning biofilter rather than simply an elapsed timeline.</td></tr>
<tr><td>Substrate / décor</td><td>No swallowable gravel, sharp edges or trapping hazards.</td></tr>
<tr><td>Food</td><td>Suitable food is on hand and portion/frequency are understood.</td></tr>
<tr><td>Emergency plan</td><td>You know the nearest amphibian/exotics vet and have a temporary safe container if transfer is needed.</td></tr>
</tbody></table></div>

<h2>Common setup mistakes</h2>
<ul>
<li>buying the axolotl before the aquarium is cycled;</li>
<li>using a small tank because the animal is currently a juvenile without planning the adult home;</li>
<li>choosing a powerful filter that cannot be made gentle;</li>
<li>using swallowable gravel;</li>
<li>assuming clear water is chemically safe;</li>
<li>buying a chiller from tank gallons alone without considering room heat and required pull-down;</li>
<li>relying on a fixed cycling timeline rather than test results;</li>
<li>making large last-minute changes immediately before the animal arrives; and</li>
<li>copying treatment or emergency advice into the setup process instead of keeping the tank stable.</li>
</ul>

<h2>How should the setup pages fit together?</h2>
<div class="table-wrap"><table>
<thead><tr><th>Your question</th><th>Canonical page</th></tr></thead>
<tbody>
<tr><td>How large should the tank be?</td><td><a href="/tank-setup/tank-size-by-age/">Tank Size</a></td></tr>
<tr><td>Which filter and how much flow?</td><td><a href="/tank-setup/filtration-for-axolotls/">Filtration</a></td></tr>
<tr><td>Canister or sponge?</td><td><a href="/tank-setup/canister-vs-sponge-filter/">Canister vs Sponge</a></td></tr>
<tr><td>What temperature?</td><td><a href="/tank-setup/temperature/">Temperature</a></td></tr>
<tr><td>Do I need a chiller?</td><td><a href="/tank-setup/aquarium-chillers/">Chiller Buying Guide</a></td></tr>
<tr><td>Which substrate?</td><td><a href="/tank-setup/substrate-and-impaction/">Substrate</a></td></tr>
<tr><td>How do I test water?</td><td><a href="/tank-setup/how-to-test-water/">Water Testing</a></td></tr>
<tr><td>What do the readings mean?</td><td><a href="/tank-setup/water-parameters-cycling/">Water Parameters & Cycling</a></td></tr>
<tr><td>How do I change water?</td><td><a href="/tank-setup/water-change-guide/">Water Change Guide</a></td></tr>
</tbody></table></div>

<h2>Sources</h2>
<ul>
<li><a href="https://ambystoma.uky.edu/genetic-stock-center/documents/AGSC%20_Guide_2024.pdf">Ambystoma Genetic Stock Center: Axolotl Guide 2024</a></li>
<li><a href="https://ambystoma.uky.edu/education1/guide-to-axolotl-husbandry">Ambystoma Genetic Stock Center: Guide to Axolotl Husbandry</a></li>
<li><a href="https://www.merckvetmanual.com/exotic-and-laboratory-animals/amphibians/environment-and-husbandry-for-amphibians">Merck Veterinary Manual: Environment and Husbandry for Amphibians, updated February 2026</a></li>
<li><a href="https://www.merckvetmanual.com/all-other-pets/amphibians/housing-for-amphibians">Merck Veterinary Manual: Housing for Amphibians, updated February 2026</a></li>
<li><a href="https://www.petco.com/pet-education/caresheets/axolotl">Petco: current Axolotl Care Guide</a></li>
</ul>
'''

for _cfg in ARTICLES.values():
    if _cfg.get("slug") in {"axolotls/care-guide", "tank-setup/setup-guide"}:
        _cfg["date_modified"] = "2026-09-19"


BODY_OVERRIDES["tank-setup/water-parameters-cycling"] = r'''
<p><strong>Axolotl water quality should be managed from measured trends, not a memorized “perfect numbers” table.</strong> In a normal home aquarium, the priorities are a functioning biological filter, no accumulating ammonia or nitrite, controlled nitrate, stable pH, appropriate temperature, and source water that is free of chlorine/chloramine or treated correctly.</p>
<div class="role-note"><strong>This page owns interpretation and cycling.</strong> For how to take the readings, use <a href="/tank-setup/how-to-test-water/">How to Test Axolotl Water</a>. For the physical maintenance procedure, use <a href="/tank-setup/water-change-guide/">How to Change Axolotl Tank Water</a>.</div>

<h2>Which water parameters should you track?</h2>
<div class="table-wrap"><table>
<thead><tr><th>Parameter</th><th>Why it matters</th><th>How to use it</th></tr></thead>
<tbody>
<tr><td>Ammonia</td><td>Primary nitrogenous waste; toxicity rises as pH and temperature change.</td><td>Should not be allowed to accumulate in a functioning occupied aquarium.</td></tr>
<tr><td>Nitrite</td><td>Intermediate product of nitrification and an indicator of an incomplete/overloaded biofilter.</td><td>Should not accumulate in a mature occupied system.</td></tr>
<tr><td>Nitrate</td><td>End product that usually builds between water changes.</td><td>Use the trend to set maintenance; current Petco guidance keeps it below 20 ppm.</td></tr>
<tr><td>pH</td><td>Affects animal physiology and ammonia toxicity; sudden swings also affect the biofilter.</td><td>Prioritize stability and understand your source water rather than chasing one exact decimal.</td></tr>
<tr><td>Temperature</td><td>Affects metabolism, oxygen demand and water chemistry.</td><td>Interpret on the <a href="/tank-setup/temperature/">Temperature Guide</a>.</td></tr>
<tr><td>GH / KH / alkalinity</td><td>Describe mineral content and buffering capacity.</td><td>Useful when pH is unstable, source water is very soft/hard, or you are troubleshooting chemistry.</td></tr>
</tbody></table></div>

<h2>What does the AGSC 2024 guide actually say?</h2>
<p>The Ambystoma Genetic Stock Center uses a standardized research water formulation made from reverse-osmosis water and salts, buffered to roughly pH 7.1–7.6. The same guide explicitly notes that other laboratories have raised axolotls successfully in conditioned well and municipal water and says municipal chemistry can vary dramatically.</p>
<p><strong>That means the AGSC recipe is a research standard, not a command that every pet keeper must recreate.</strong> Its most transferable lesson is to know your source water, remove municipal disinfectants appropriately, monitor pH/ammonia/chlorine or chloramine, and respond to measured changes rather than assumptions.</p>

<h2>What should ammonia and nitrite read in an occupied axolotl tank?</h2>
<p><strong>They should not be allowed to accumulate.</strong> Merck's aquatic-animal guidance states that water should be free of ammonia and nitrite, and current Petco axolotl guidance says axolotls are very sensitive to both. A measurable reading therefore triggers investigation of the biofilter, waste load, source water, feeding and recent maintenance.</p>
<p>Do not turn a single test-strip color into a diagnosis of “ammonia burn.” Confirm the result, review pH/temperature, and look at the whole animal.</p>

<h2>What nitrate level should you aim for?</h2>
<p>Nitrate is normally managed through water changes, plant uptake and stocking/feeding control rather than expected to remain at zero. Current Petco axolotl guidance recommends keeping nitrate below 20 ppm. MyAxolotl uses that as a practical consumer ceiling while also watching the individual tank's trend.</p>
<p><strong>Do not claim that a particular nitrate number automatically causes fungus, gill shrinkage or appetite loss in every axolotl.</strong> A rising nitrate trend is a maintenance signal, but clinical signs still need their own assessment.</p>

<h2>What pH is appropriate?</h2>
<p>The AGSC's standardized rearing water is buffered around 7.1–7.6, but the same guide states that municipal-water chemistry varies and that other water sources can support axolotls. For a home tank, stability and a biologically functioning system are more useful than repeatedly dosing chemicals to force one exact value.</p>
<p>If your pH is persistently extreme, rapidly changing, or paired with ammonia problems, investigate source water, alkalinity/KH, substrate/rock chemistry and filtration. Avoid emergency baking-soda recipes without understanding the chemistry you are changing.</p>

<h2>Do GH and KH have universal axolotl target ranges?</h2>
<p><strong>Not from the sources used by MyAxolotl.</strong> Hardness and alkalinity matter because they influence mineral availability and pH buffering, but we did not find an axolotl-specific veterinary source validating one universal “GH 7–14 / KH 3–8” home target.</p>
<p>Measure them when your source water is unusually soft/hard, pH is unstable, or you are designing a reproducible water recipe. If you are deliberately remineralizing RO/distilled water, follow a defined formulation rather than improvising salt/bicarbonate doses.</p>

<h2>What is the nitrogen cycle?</h2>
<p>Biological filtration uses microbial communities to oxidize ammonia through nitrite toward nitrate. A new aquarium does not have enough established biofilm simply because the filter has been switched on for a certain number of days.</p>
<p>For an axolotl setup, establish the filter before the animal enters. A fishless cycling method uses a controlled ammonia source and repeated testing so you can see the system develop ammonia-processing and nitrite-processing capacity.</p>

<h2>How do you know when a tank is cycled?</h2>
<p><strong>Use the pattern of repeated test results rather than a fixed “4–8 week” promise.</strong> A mature biofilter should process the waste load without persistent ammonia or nitrite accumulation, while nitrate or other downstream nitrogen products reflect ongoing processing.</p>
<p>Because hobby cycling methods differ, this page does not prescribe one universal ammonia dose or one 24-hour pass/fail number. Record your method and readings in the <a href="/tools/nitrogen-cycle-tracker/">Nitrogen Cycle Tracker</a>.</p>

<h2>What should you do if ammonia or nitrite appears?</h2>
<ol>
<li><strong>Confirm the reading.</strong> Repeat the test correctly and check whether the reagent is in date.</li>
<li><strong>Measure pH and temperature.</strong> They affect ammonia toxicity and help interpret the situation.</li>
<li><strong>Remove obvious waste.</strong> Uneaten food, dead organisms or trapped debris may be contributing.</li>
<li><strong>Protect the animal.</strong> Use an appropriate partial water change and treated replacement water; if the main aquarium cannot be made safe promptly, a temporary holding setup may be needed.</li>
<li><strong>Investigate the biofilter.</strong> Recent filter-media replacement, chlorine exposure, power loss, medication or overloading can disrupt nitrification.</li>
<li><strong>Retest and record.</strong> One corrective change is not proof that the system is stable again.</li>
</ol>
<p><strong>Do not fridge an axolotl to manage an ammonia spike.</strong> Refrigeration is not a substitute for safe water and biological-filter repair. Use <a href="/health/fridging-sick-axolotl/">the fridging evidence page</a> if a veterinarian has raised that option for a separate clinical reason.</p>

<h2>Should you use an ammonia-binding conditioner?</h2>
<p>Conditioner products differ. Follow the product label and understand what the test kit measures after treatment. A conditioner can be part of an emergency response, but it does not repair an uncycled or damaged biofilter and does not remove the need for water changes and retesting.</p>
<p>Use <a href="/tank-setup/water-conditioners/">Water Conditioners</a> for chlorine/chloramine and product-selection questions.</p>

<h2>How often should you test?</h2>
<p>Test frequently while cycling, after a filter disruption, after unexplained health changes, and after any major change in stocking or maintenance. Merck's 2026 pet-amphibian guidance recommends weekly testing of temperature, pH, hardness, ammonia, nitrite and nitrate in aquatic setups.</p>
<p>A mature stable tank may not need daily full chemistry panels, but trends are useful: keep a log rather than relying on memory.</p>

<h2>How do water changes fit the nitrogen cycle?</h2>
<p>Water changes remove dissolved waste and replenish water; they do not replace biological filtration. Routine partial changes and an established biofilter work together.</p>
<p>The 2024 AGSC guide notes that filtered aquaria still need regular partial changes and monitoring. Follow <a href="/tank-setup/water-change-guide/">the Water Change Guide</a> for the procedure.</p>

<h2>Common interpretation mistakes</h2>
<ul>
<li>treating one off-color test as a confirmed emergency without repeating it;</li>
<li>assuming zero nitrate means the tank must be cycled;</li>
<li>using elapsed time instead of water-test trends to declare cycling complete;</li>
<li>forcing pH with bicarbonate without measuring alkalinity/KH and source water;</li>
<li>copying laboratory ARW chemistry as a universal pet-water requirement;</li>
<li>assuming a conditioner permanently solves ammonia without restoring the biofilter; and</li>
<li>diagnosing a health condition from chemistry alone instead of evaluating the animal too.</li>
</ul>

<h2>Sources</h2>
<ul>
<li><a href="https://ambystoma.uky.edu/genetic-stock-center/documents/AGSC%20_Guide_2024.pdf">Ambystoma Genetic Stock Center: Axolotl Guide 2024</a></li>
<li><a href="https://www.merckvetmanual.com/exotic-and-laboratory-animals/laboratory-animals/management-of-laboratory-animals">Merck Veterinary Manual: Management of Laboratory Animals — aquatic water quality</a></li>
<li><a href="https://www.merckvetmanual.com/all-other-pets/amphibians/housing-for-amphibians">Merck Veterinary Manual: Housing for Amphibians, updated February 2026</a></li>
<li><a href="https://www.petco.com/pet-education/caresheets/axolotl">Petco: current Axolotl Care Guide</a></li>
</ul>
'''


# ---------------------------------------------------------------------------
# Remaining legacy protocol cleanup (2026-09-19)
# ---------------------------------------------------------------------------

BODY_OVERRIDES["health/quarantine-tub"] = r'''
<p><strong>A quarantine or hospital container is a temporary controlled environment, not a treatment by itself.</strong> Its purpose is to separate an animal when isolation is needed, simplify observation, and make water quality easy to measure and manage while the underlying health problem is assessed.</p>

<h2>When is temporary isolation useful?</h2>
<p>Isolation can be appropriate for a new arrival, an injured animal that must be protected from tank mates, an animal being evaluated for infectious disease, or a patient whose veterinarian wants close observation in a simplified setup.</p>
<p>It is not automatically necessary for every missed meal, floating episode, fungal-looking patch or minor scrape.</p>

<h2>What should a hospital setup include?</h2>
<ul>
<li>a clean, inert container large enough for the animal to rest and turn normally;</li>
<li>treated water appropriate for the species;</li>
<li>stable temperature;</li>
<li>a secure cover when escape is possible;</li>
<li>a smooth hide when it does not interfere with observation; and</li>
<li>dedicated equipment that is not shared with other tanks.</li>
</ul>

<h2>Does an unfiltered tub need complete daily water changes?</h2>
<p><strong>Not as a universal rule.</strong> An unfiltered container has no established biofilter, so ammonia can accumulate quickly and water replacement may need to be frequent or complete. The correct schedule depends on container volume, animal size, feeding, waste and measured water quality.</p>
<p>Test the water and change enough to keep conditions safe. If the animal needs prolonged isolation, a properly cycled quarantine aquarium can be easier to stabilize than an indefinitely unfiltered tub.</p>

<h2>Should you add salt, tea or medication to the tub?</h2>
<p>No product should be added simply because the animal is in quarantine. A hospital container is not a default medication bath. Use medication, saline or another treatment only for a defined indication and preferably under veterinary guidance.</p>
<p>For white/cottony lesions, use <a href="/health/fungal-infections-saprolegnia/">the fungus guide</a>. For black tea and salt specifically, use the dedicated evidence pages.</p>

<h2>How should you monitor the animal?</h2>
<p>Record temperature, water chemistry, appetite, fecal production, posture, breathing, swimming, visible lesions and body condition. Photographs taken from the same angle can help show whether a wound or swelling is changing.</p>
<p>Merck's amphibian clinical guidance emphasizes exactly this kind of history and water-quality record when evaluating an amphibian patient.</p>

<h2>How do you prevent cross-contamination?</h2>
<ul>
<li>use separate nets, tubs, siphons and feeding tools;</li>
<li>wash hands and change gloves between enclosures;</li>
<li>do not pour quarantine water into an established aquarium; and</li>
<li>clean/disinfect equipment appropriately before reuse.</li>
</ul>

<h2>When should quarantine end?</h2>
<p>Do not use a fixed number of days as the only release criterion. The animal should be clinically appropriate to return, the reason for isolation should be resolved or controlled, and the destination aquarium should be safe. For an infectious-disease concern, follow the veterinarian's quarantine period.</p>

<h2>Sources</h2>
<ul>
<li><a href="https://www.merckvetmanual.com/exotic-and-laboratory-animals/amphibians/clinical-techniques-in-amphibians">Merck Veterinary Manual: Clinical Techniques in Amphibians, updated February 2026</a></li>
<li><a href="https://www.merckvetmanual.com/exotic-and-laboratory-animals/amphibians/environment-and-husbandry-for-amphibians">Merck Veterinary Manual: Environment and Husbandry for Amphibians</a></li>
</ul>
'''

BODY_OVERRIDES["health/ammonia-burns"] = r'''
<p><strong>Ammonia exposure is a water-quality emergency, but “ammonia burn” cannot be staged reliably from redness alone.</strong> Amphibians exposed to inappropriate ammonia may produce excess mucus, become dull in color, show abnormal behavior or attempt to escape; other skin and gill diseases can look similar.</p>

<h2>What should you do first?</h2>
<ol>
<li><strong>Test and confirm the water.</strong> Repeat the ammonia result correctly and record pH and temperature.</li>
<li><strong>Remove the animal from contaminated water when necessary.</strong> Merck's amphibian guidance recommends moving exposed amphibians to clean, dechlorinated, well-oxygenated water.</li>
<li><strong>Correct the source.</strong> Remove waste, check the biofilter and perform an appropriate water change.</li>
<li><strong>Retest.</strong> One water change is not proof the system is stable again.</li>
</ol>

<h2>Can you tell severity from an ammonia number alone?</h2>
<p>No. Ammonia toxicity depends on total ammonia, pH, temperature, exposure duration and species sensitivity. A chart that assigns “mild/moderate/severe” skin damage to fixed ppm bands gives false certainty.</p>
<p>The 2024 AGSC guide also notes that ammonia becomes a more serious problem as pH rises and treats elevated ammonia in recirculating research systems as a sign the nitrogen cycle is out of equilibrium.</p>

<h2>Should you use a conditioner?</h2>
<p>A conditioner may be part of an emergency water-management plan depending on the product, but it does not restore a damaged biofilter. Follow the label and keep testing. Use <a href="/tank-setup/water-conditioners/">Water Conditioners</a> for product-specific questions.</p>

<h2>Should you use tea, salt or methylene blue?</h2>
<p><strong>Do not add a bath or medication solely because the animal was exposed to ammonia.</strong> Treat the contaminated water first. Secondary infection, gill damage or another diagnosis may require veterinary treatment, but that decision belongs to the specific condition.</p>

<h2>When is veterinary care warranted?</h2>
<p>Seek prompt amphibian/exotics veterinary care for severe respiratory difficulty, extensive skin damage, uncontrolled bleeding, inability to maintain normal position, marked lethargy, rapid deterioration or signs that persist despite correction of the water problem.</p>

<h2>How do you prevent recurrence?</h2>
<p>Maintain an established biological filter, remove decomposing waste, test water regularly, avoid replacing mature filter media unnecessarily and investigate any recurring ammonia rise rather than repeatedly treating the symptom.</p>

<h2>Sources</h2>
<ul>
<li><a href="https://www.merckvetmanual.com/exotic-and-laboratory-animals/amphibians/amphibians-as-laboratory-animals">Merck Veterinary Manual: Amphibians as Laboratory Animals — ammonia toxicosis</a></li>
<li><a href="https://ambystoma.uky.edu/genetic-stock-center/documents/AGSC%20_Guide_2024.pdf">Ambystoma Genetic Stock Center: Axolotl Guide 2024</a></li>
</ul>
'''

BODY_OVERRIDES["health/minor-scrapes-and-wounds"] = r'''
<p><strong>A small superficial scrape may heal with stable clean water and protection from further trauma, but an amphibian wound should not automatically be treated with salt, tea or over-the-counter medication.</strong> Amphibian skin is biologically important and injuries can become infected or be deeper than they first appear.</p>

<h2>What should you do after noticing a scrape?</h2>
<ol>
<li>Identify and remove the source of injury if it is safe to do so.</li>
<li>Measure water quality and temperature.</li>
<li>Photograph the area in neutral light.</li>
<li>Reduce unnecessary handling.</li>
<li>Monitor appetite, swimming, swelling, bleeding and whether the lesion is enlarging.</li>
</ol>

<h2>When is a wound more than “minor”?</h2>
<p>Seek veterinary care for ongoing bleeding, deep laceration, exposed tissue, fracture, limb loss, substantial swelling, ulceration, spreading discoloration, respiratory difficulty or rapid decline. Merck's amphibian guidance emphasizes rapid assessment, supportive care and pain management for traumatic injuries.</p>

<h2>Should you use a tea or salt bath?</h2>
<p>No bath should be the default response to a scrape. White/cotton-like material can have several causes and needs its own assessment. Use <a href="/health/fungal-infections-saprolegnia/">the fungus guide</a> for that differential rather than treating fuzz from appearance alone.</p>

<h2>Should you use an antiseptic or antibiotic?</h2>
<p>Do not apply human topical products or start antimicrobial medication without veterinary guidance. Amphibian skin is highly permeable, and drug concentration and route matter.</p>

<h2>How do you prevent repeat injuries?</h2>
<p>Inspect décor, intake guards, tank mates, handling practices and transport containers. Smooth sharp edges, remove trapping hazards and separate incompatible animals when necessary.</p>

<h2>Sources</h2>
<ul>
<li><a href="https://www.merckvetmanual.com/exotic-and-laboratory-animals/amphibians/noninfectious-disorders-of-amphibians">Merck Veterinary Manual: Trauma of Amphibians</a></li>
<li><a href="https://www.merckvetmanual.com/all-other-pets/amphibians/introduction-to-amphibians">Merck Veterinary Manual: Injuries in Pet Amphibians</a></li>
</ul>
'''

BODY_OVERRIDES["health/limb-regeneration"] = r'''
<p><strong>Axolotls can regenerate lost limb tissue, but an owner should first manage the injury rather than assume regeneration guarantees a good outcome.</strong> The immediate priorities are protection from further trauma, stable husbandry, observation for infection or systemic decline, and veterinary assessment when the injury is significant.</p>
<div class="role-note"><strong>This is the owner lane.</strong> For the cellular science of regeneration, use <a href="/biology-and-science/regeneration-and-limb-regrowth/">Axolotl Regeneration</a>.</div>

<h2>What should you do after a limb injury?</h2>
<ol>
<li>Separate the animal from an aggressive tank mate or the injury source if needed.</li>
<li>Measure water quality and temperature.</li>
<li>Document the wound with dated photographs.</li>
<li>Minimize handling.</li>
<li>Contact an amphibian-experienced veterinarian for major tissue loss, fracture, uncontrolled bleeding or deterioration.</li>
</ol>

<h2>Does every lost limb grow back normally?</h2>
<p>No guarantee should be made. Axolotls have remarkable regenerative capacity, but outcome depends on injury level, tissue condition, health, age and whether complications occur. Regrowth can also differ in shape or function.</p>

<h2>How long does regeneration take?</h2>
<p>There is no single owner-facing timetable that applies to every injury. Research describes staged regeneration, but the time visible in a pet can vary with injury severity, animal size, temperature and health. Track the trend rather than expecting a fixed number of days or weeks.</p>

<h2>What does a healing limb look like?</h2>
<p>Early healing can include a wound surface and developing regenerative tissue. A photograph cannot reliably distinguish every normal stage from infection, so use progression, appetite, swelling, odor, bleeding and the animal's overall condition to decide whether veterinary review is needed.</p>

<h2>Should you use salt or black tea on the stump?</h2>
<p><strong>No treatment bath is required simply because a limb is regenerating.</strong> If a separate fungal or bacterial problem is suspected, diagnose and treat that problem on its own evidence rather than automatically bathing the wound.</p>

<h2>When should you see a veterinarian?</h2>
<p>Prompt care is appropriate for deep injury, fracture, uncontrolled bleeding, tissue necrosis, severe swelling, rapidly spreading lesions, systemic decline, pain concern or an injury caused by equipment that may have crushed internal tissue.</p>

<h2>Sources</h2>
<ul>
<li><a href="https://www.merckvetmanual.com/exotic-and-laboratory-animals/amphibians/noninfectious-disorders-of-amphibians">Merck Veterinary Manual: Trauma of Amphibians</a></li>
<li><a href="https://www.merckvetmanual.com/exotic-and-laboratory-animals/amphibians/emergency-care-of-amphibians">Merck Veterinary Manual: Emergency Care of Amphibians</a></li>
<li><a href="https://ambystoma.uky.edu/genetic-stock-center/husbandry.php">Ambystoma Genetic Stock Center: regeneration resources</a></li>
</ul>
'''

BODY_OVERRIDES["diet/feeding-schedule-by-age"] = r'''
<p><strong>Feeding frequency should become less frequent as an axolotl grows, but there is no universal age-by-age schedule that fits every individual.</strong> Use life stage, body size, food size, body condition, appetite and waste production together.</p>
<div class="role-note"><strong>This page owns routine feeding cadence.</strong> For planned food gaps use <a href="/diet/fasting-and-vacation/">Fasting & Vacation</a>; for unexpected appetite loss use <a href="/health/refusing-to-eat/">Refusing to Eat</a>.</div>

<h2>What does the AGSC feeding timeline show?</h2>
<p>The 2024 Ambystoma Genetic Stock Center guide feeds newly feeding larvae daily, then transitions growing animals through live foods and pellets, with adult pelleted food offered about twice weekly in its research system. An older AGSC husbandry guide describes adults around one year old being fed three or four times per week.</p>
<p><strong>Those examples show the direction of change—not one mandatory home schedule.</strong></p>

<h2>How often should hatchlings and larvae eat?</h2>
<p>Newly feeding larvae are growing rapidly and are normally offered very small appropriate foods frequently. Follow the <a href="/breeding/egg-and-larvae-care/">Egg & Larvae Care</a> guide for the transition from yolk to active feeding.</p>

<h2>How often should juveniles eat?</h2>
<p>Juveniles usually need food more frequently than adults because they are growing. Instead of using an exact age cutoff, monitor body condition, growth, appetite and how quickly the animal processes meals.</p>
<p>Use <a href="/breeding/raising-juveniles/">Baby Axolotl Care</a> for grow-out and size sorting.</p>

<h2>How often should adults eat?</h2>
<p>Adults are commonly fed only a few times per week rather than every day. AGSC examples range from roughly twice weekly in its 2024 timeline to three or four feedings weekly in an older husbandry guide.</p>
<p>Your individual may need adjustment based on body condition, reproductive status, food energy density and temperature.</p>

<h2>How much should you feed?</h2>
<p>There is no validated “pellets per inch” formula for all foods and animals. Offer an appropriate portion, observe body condition over time and adjust gradually. Remove uneaten food before it decomposes and affects water quality.</p>

<h2>What foods work for routine feeding?</h2>
<p>Appropriately sized earthworms/nightcrawlers and nutritionally suitable sinking pellets are common staples. AGSC uses formulated soft-moist pellets and transitions pellet size as animals grow.</p>
<p>Use <a href="/diet/best-foods-list/">What Do Axolotls Eat?</a> for food quality and variety.</p>

<h2>How do you know if the schedule is too much or too little?</h2>
<p>Watch body condition and growth rather than one meal. Persistent weight gain, leftover food, repeated regurgitation or excessive waste suggest the plan may need adjustment. Persistent weight loss, poor growth or appetite change needs review of diet, water quality and health.</p>

<h2>Does feeding frequency determine the water-change schedule?</h2>
<p>Feeding affects waste load, but there is no fixed rule such as “one adult eating two worms requires a 50% weekly change.” Test the aquarium and let water chemistry, waste accumulation and system capacity set the maintenance plan.</p>

<h2>How long can an axolotl safely fast?</h2>
<p>This page does not publish a universal “safe fasting period” table because the evidence does not establish one. Planned absences belong on <a href="/diet/fasting-and-vacation/">the fasting/vacation guide</a>.</p>

<h2>Sources</h2>
<ul>
<li><a href="https://ambystoma.uky.edu/genetic-stock-center/documents/AGSC%20_Guide_2024.pdf">Ambystoma Genetic Stock Center: Axolotl Guide 2024 — feeding timeline</a></li>
<li><a href="https://ambystoma.uky.edu/education1/guide-to-axolotl-husbandry">Ambystoma Genetic Stock Center: Guide to Axolotl Husbandry</a></li>
<li><a href="https://ambystoma.uky.edu/genetic-stock-center/food-info.php">Ambystoma Genetic Stock Center: Food Information</a></li>
</ul>
'''

BODY_OVERRIDES["tank-setup/substrate-and-impaction"] = r'''
<p><strong>Choose axolotl substrate by swallowing risk, animal size, cleanliness and the way you feed.</strong> The clearest rule is to avoid loose gravel or stones small enough to enter the mouth during suction feeding.</p>
<div class="role-note"><strong>This page owns substrate choice and prevention.</strong> If you suspect a gastrointestinal blockage, use <a href="/health/impaction-symptoms-treatment/">the Impaction Guide</a>.</div>

<h2>Why is gravel risky?</h2>
<p>Axolotls can ingest material while suction-feeding. The 2024 AGSC guide discourages substrate in filtered aquaria because axolotls may ingest small rocks and gravel during feeding, and AGSC food guidance specifically warns about gravel ingestion around pellets.</p>
<p>That is enough to justify avoiding swallowable gravel without claiming every swallowed particle is inevitably fatal.</p>

<h2>What substrate options are practical?</h2>
<div class="table-wrap"><table>
<thead><tr><th>Option</th><th>Strengths</th><th>Tradeoffs</th></tr></thead>
<tbody>
<tr><td>Bare bottom</td><td>No loose substrate to swallow; easy waste removal</td><td>Less natural-looking; surface traction/visual preference vary by setup</td></tr>
<tr><td>Appropriately fine sand</td><td>Natural appearance and broad continuous surface</td><td>Must be kept clean; particle size and animal size matter</td></tr>
<tr><td>Large fixed/smooth surfaces</td><td>Can provide traction without loose ingestible particles</td><td>Waste can collect around/under pieces</td></tr>
<tr><td>Loose gravel / small stones</td><td>Decorative</td><td>Swallowing/foreign-body risk during feeding</td></tr>
</tbody></table></div>

<h2>Is there one proven safe sand grain size?</h2>
<p><strong>MyAxolotl does not treat one millimeter cutoff as a universal biological law.</strong> Finer material is generally chosen to reduce the risk posed by coarse ingestible particles, but animal size, feeding method and maintenance also matter.</p>
<p>For very small juveniles, a bare-bottom grow-out setup can make feeding and waste removal easier.</p>

<h2>Can large river rocks be safe?</h2>
<p>Objects too large to swallow remove one foreign-body route, but they can trap waste underneath and create difficult cleaning zones. If used, they should be smooth, stable and arranged so the animal cannot become wedged.</p>

<h2>Does substrate cause fungus or ammonia by itself?</h2>
<p>No. Dirty substrate can trap organic waste and contribute to poor water quality, but it is not accurate to claim that a specific substrate automatically causes fungal infection or a fixed nitrate level. Husbandry, cleaning, stocking and filtration determine the system outcome.</p>

<h2>Should a hospital or quarantine setup be bare?</h2>
<p>A bare inert surface is often useful in temporary clinical housing because it simplifies cleaning and observation. That does not mean every hospital case requires medication or a fixed complete-water-change schedule.</p>
<p>See <a href="/health/quarantine-tub/">Quarantine & Hospital Setup</a>.</p>

<h2>How do you feed without increasing substrate ingestion?</h2>
<p>Place food where it is easy for the animal to find and where suction is less likely to pull in loose material. Feeding dishes or target feeding can help in some setups. Remove leftovers before they decompose.</p>

<h2>What if you think gravel was swallowed?</h2>
<p>Do not massage the abdomen, give laxatives or fridge the animal as a standard response. Record the exposure, watch appetite/fecal output/body shape and seek veterinary evaluation if symptoms develop or persist. Imaging may be needed to confirm a foreign body.</p>

<h2>Sources</h2>
<ul>
<li><a href="https://ambystoma.uky.edu/genetic-stock-center/documents/AGSC%20_Guide_2024.pdf">Ambystoma Genetic Stock Center: Axolotl Guide 2024</a></li>
<li><a href="https://ambystoma.uky.edu/genetic-stock-center/food-info.php">Ambystoma Genetic Stock Center: Food Information</a></li>
<li><a href="https://veterinarypartner.vin.com/default.aspx?catId=253985&amp;id=8030801&amp;ind=1817&amp;objTypeID=1007&amp;pid=19239">Veterinary Partner / VIN: Gastrointestinal Foreign Body or Overload in Amphibians</a></li>
</ul>
'''

for _cfg in ARTICLES.values():
    if _cfg.get("slug") in {
        "health/quarantine-tub",
        "health/ammonia-burns",
        "health/minor-scrapes-and-wounds",
        "health/limb-regeneration",
        "diet/feeding-schedule-by-age",
        "tank-setup/substrate-and-impaction",
    }:
        _cfg["date_modified"] = "2026-09-19"

# Build trigger: retry Cost & Buying after clearing the stale queued job.

# Keyword-reconciliation fix: strengthen the existing anatomy owner for teeth/oral anatomy.
INTRO_OVERRIDES['biology-and-science/anatomy-gills-and-lungs'] = (
    'Axolotl anatomy includes external gills, simple lungs, permeable skin, small oral teeth, '
    'lidless eyes, an inner ear and lateral-line system, olfactory organs, and a tongue with taste buds. '
    'This guide explains how those structures work without splitting closely related anatomy questions into separate pages.'
)
BODY_OVERRIDES['biology-and-science/anatomy-gills-and-lungs'] = r'''
<h2>Do axolotls have teeth?</h2>
<p><strong>Yes. Axolotls have real teeth in the mouth and palate, even though the teeth are small and easy to miss.</strong> Research on <em>Ambystoma mexicanum</em> describes organized outer and inner dental arcades and multiple tooth fields rather than a toothless mouth.</p>
<p>Studies of axolotl dentition also show that replacement teeth continue to develop. The teeth become more numerous as the animal develops, and their structure changes with developmental stage.</p>
<p>For owners, the practical point is simple: a smooth-looking axolotl mouth does not mean the animal has no teeth. Questions about whether a nip can hurt belong in the <a href="/care-basics/axolotls-and-children/">axolotls and children safety guide</a>; this page covers the anatomy itself.</p>
<div class="references-box"><h3>Dental anatomy sources</h3><ul>
<li><a href="https://pubmed.ncbi.nlm.nih.gov/11989966/">Wistuba, Greven &amp; Clemen (2002): development of axolotl teeth</a></li>
<li><a href="https://www.nature.com/articles/s41598-020-66142-2">Scientific Reports (2020): axolotl tooth structure and replacement</a></li>
<li><a href="https://pubmed.ncbi.nlm.nih.gov/33505974/">Oral and palatal dentition of axolotl (2021)</a></li>
</ul></div>

<h2>Do axolotls have lungs?</h2>
<p><strong>Yes, axolotls have lungs, plus external gills and oxygen-absorbing skin.</strong> They breathe through all three systems, with the feathery external gills and the skin doing most of the work underwater. The lungs are simple sacs used for surface gulps, which makes the axolotl one of the most flexible breathers among amphibians.</p>
<p>A true amphibian built for a life spent entirely underwater keeps this gill-lung-skin combo its whole life.</p>
<h2>How do axolotls breathe?</h2>
<p><strong>Axolotls breathe through three systems at once: external gills, skin, and lungs.</strong> Each system has a specific job:</p>
<div class="table-wrap"><table>
<thead><tr><th>System</th><th>What it does</th></tr></thead>
<tbody>
<tr><td>External gills</td><td>Three feathery gills per side extract oxygen from water</td></tr>
<tr><td>Skin</td><td>Absorbs oxygen directly through the moist skin</td></tr>
<tr><td>Lungs</td><td>Simple sacs gulp air at the surface</td></tr>
<tr><td>Gill flicking</td><td>Moves water over the gill filaments to boost oxygen uptake</td></tr>
<tr><td>Regeneration</td><td>Gills regrow if damaged or nipped</td></tr>
</tbody></table></div>
<p>The gills and skin handle the routine oxygen supply, and the lungs supplement them when the animal surfaces.</p>
<h2>How many gills does an axolotl have?</h2>
<p><strong>An axolotl has six external gill stalks, three on each side of the head.</strong> Each stalk carries fine filaments that increase surface area for gas exchange.</p>
<h2>Why are axolotl gills so large?</h2>
<p><strong>The gills are large because they provide substantial surface area for underwater gas exchange.</strong> Their feathery filaments expose blood-rich tissue to moving water. Gill condition can also change with stress and water quality, so persistent changes should be interpreted alongside husbandry conditions rather than on appearance alone.</p>
<h2>Why does my axolotl go to the surface for air?</h2>
<p><strong>Surface gulping can be normal because axolotls have lungs.</strong> Occasional trips to the surface are not automatically a problem. Frequent gulping or a sudden change should prompt a check of temperature, water quality, and aeration.</p>
<h2>Can axolotls breathe out of water?</h2>
<p><strong>Axolotls are fully aquatic and should remain in water.</strong> Their external gills are adapted for underwater gas exchange and can collapse and dry when exposed to air. Lungs allow surface air gulps, but they do not make an axolotl a land animal.</p>
<h2>What do healthy axolotl gills look like?</h2>
<p><strong>Healthy gills are typically full and feathery, but normal appearance varies between individuals.</strong> Persistent shrinking, loss of filaments, marked curling, or a sudden change should prompt a check of water quality, temperature, and other stressors rather than a diagnosis from gill shape alone.</p>
<h2>What is buccal pumping?</h2>
<p><strong>Buccal pumping is rhythmic movement of the mouth and throat region that helps move water across respiratory surfaces.</strong> It is one part of how aquatic amphibians maintain gas exchange while resting underwater.</p>
<h2>Do axolotls have lungs or gills?</h2>
<p><strong>Axolotls have both lungs and gills, plus skin respiration.</strong> The gills and skin dominate underwater, while the lungs allow occasional surface air gulps. All three systems are part of normal axolotl respiratory anatomy.</p>
<h2>What happens to axolotl gills in poor water?</h2>
<p><strong>Poor water quality can damage or reduce the condition of external gills.</strong> Ammonia and nitrite are especially concerning because they injure delicate aquatic tissues. If the gills change noticeably, test the water first and correct the underlying husbandry problem rather than treating the gills as a diagnosis by themselves.</p>
<h2>What other anatomy do axolotls have?</h2>
<p>Several common anatomy questions are best answered together because they describe the same paedomorphic aquatic body plan.</p>
<h3>Do axolotls have ears?</h3>
<p><strong>Axolotls have an inner ear, but no visible external ear flap.</strong> They also sense water movement through a lateral-line system of mechanoreceptive neuromasts. Research on <em>Ambystoma mexicanum</em> describes both inner-ear sensory hair cells and superficial lateral-line organs, so hearing and water-motion sensing are not limited to a visible outer ear.</p>
<h3>Do axolotls have eyelids?</h3>
<p><strong>Normal paedomorphic axolotls do not develop movable eyelids.</strong> The American Museum of Natural History and San Diego Zoo both identify lidless eyes as one of the juvenile traits retained into adulthood.</p>
<h3>Do axolotls have scales?</h3>
<p><strong>No. Axolotls do not have fish-like or reptile-like scales.</strong> Their skin is amphibian epidermis with mucus-producing cells and remains important for gas exchange. Histological studies describe specialized epidermal cells and a protective mucus layer rather than scales.</p>
<h3>Do axolotls have a nose and a sense of smell?</h3>
<p><strong>Yes. Axolotls have external nostrils, a nasal cavity, an olfactory epithelium, and a vomeronasal system.</strong> Anatomical studies show that their olfactory receptor cells project to the olfactory bulb, and experiments have recorded odor responses from the olfactory epithelium.</p>
<h3>Do axolotls have a tongue?</h3>
<p><strong>Yes. Axolotls have a tongue with specialized epithelium and taste buds.</strong> Microscopy studies describe taste buds on the tongue and elsewhere in the oral cavity, with sensory innervation through cranial nerves.</p>
<div class="references-box"><h3>Anatomy and sensory sources</h3><ul>
<li><a href="https://pubmed.ncbi.nlm.nih.gov/2124588/">Kornblum, Corwin &amp; Trevarrow (1990): inner-ear and lateral-line sensory hair cells</a></li>
<li><a href="https://pubmed.ncbi.nlm.nih.gov/8315607/">Northcutt &amp; Bleckmann (1993): axolotl lateral-line neuromasts</a></li>
<li><a href="https://www.amnh.org/explore/ology/ology-cards/366-axolotl">American Museum of Natural History: retained juvenile traits and lidless eyes</a></li>
<li><a href="https://pubmed.ncbi.nlm.nih.gov/7953608/">Eisthen et al. (1994): olfactory and vomeronasal anatomy</a></li>
<li><a href="https://pubmed.ncbi.nlm.nih.gov/10609049/">Wistuba &amp; Greven (1999): tongue epithelium and taste buds</a></li>
<li><a href="https://pubmed.ncbi.nlm.nih.gov/2630544/">Jarial (1989): epidermal Leydig cells and protective mucus</a></li>
</ul></div>
<p>Axolotl anatomy combines structures that look unusual together: oral teeth, external gills, permeable skin, simple lungs, lidless eyes, aquatic sensory organs, and a taste-bearing tongue. Together they reflect the animal's permanently aquatic, paedomorphic salamander biology.</p>
'''
