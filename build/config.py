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
        "title_override": "Best Aquarium Chillers for Axolotls",
        "meta_override": "Axolotls need 60–68°F water. Learn when a chiller is necessary, how to size one, and which compressor models suit typical home tanks.",
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
        "title_override": "Ammonia & Nitrate Spikes in Axolotl Tanks",
    },
    "7 - Best axolotl filters.docx": {
        "slug": "tank-setup/filtration-for-axolotls",
        "hub": "tank-setup",
        "title_override": "Best Axolotl Tank Filters: Types & Sizing",
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
        "title_override": "How Long Can Axolotls Fast?",
        "meta_override": "Adult axolotls can fast up to 14 days; juveniles and hatchlings need shorter limits based on age, condition, and tank temperature.",
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
        "meta_override": "Learn how to recognize cotton-like Saprolegnia growth, correct water and stress factors, and know when an axolotl needs veterinary care.",
    },
    "33 - The Black Tea Bath Protocol for Axolotls.docx": {
        "slug": "health/black-tea-bath",
        "hub": "health",
        "title_override": "Black Tea Bath for Axolotls: Step-by-Step Treatment",
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
        "title_override": "Axolotl Salt Baths for Fungal Infections",
        "date_modified": "2026-08-29",
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
        "title_override": "Raising Baby Axolotls (Juveniles) to Adulthood",
        "title_tag": "Raising Baby Axolotls: Feeding, Growth & Rehoming Juveniles",
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
        "title_override": "Understanding Axolotl Pigment Cells",
        "title_tag": "Axolotl Pigment Cells: Chromatophores, Melanophores & More",
        "meta_override": "Axolotl color comes from melanophores, xanthophores, and iridophores, which explain how common morphs and axanthic traits appear.",
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
        "title_override": "Understanding Axolotl Limb Regeneration",
        "title_tag": "How Axolotl Limb Regeneration Works & What to Expect",
        "date_modified": "2026-08-29",
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
        "title_override": "Are Axolotls Good Pets for Beginners?",
        "title_tag": "Are Axolotls Good Pets for Beginners? Honest Pros & Cons",
    },
    "73 - Axolotl Age and Size Chart.docx": {
        "slug": "care-basics/axolotl-age-and-size-chart",
        "hub": "care-basics",
        "title_override": "Axolotl Age and Size Chart",
        "title_tag": "Axolotl Age & Size Chart: How Big They Get at Every Stage",
    },
    "74 - Amazing Axolotl Facts.docx": {
        "slug": "care-basics/axolotl-facts",
        "hub": "care-basics",
        "title_override": "Amazing Axolotl Facts",
        "title_tag": "Axolotl Facts: 25 Amazing Things You Need to Know (2026)",
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
        "title_override": "How to Hold an Axolotl",
        "title_tag": "How to Hold an Axolotl: Safe Handling, Netting & Transport",
    },
    "80 - How to Pronounce Axolotl.docx": {
        "slug": "care-basics/how-to-pronounce-axolotl",
        "hub": "care-basics",
        "title_override": "How to Pronounce Axolotl",
        "title_tag": "How to Pronounce Axolotl: Correct Way & Common Mistakes",
        "date_modified": "2026-08-27",
    },
    "81 - Can Axolotls Live Together.docx": {
        "slug": "care-basics/keeping-multiple-axolotls",
        "hub": "care-basics",
        "title_override": "Can Axolotls Live Together?",
        "title_tag": "Can Axolotls Live Together? Housing Multiple Axolotls Safely",
    },
    "82 - Axolotl Anatomy Gills and Lungs.docx": {
        "slug": "biology-and-science/anatomy-gills-and-lungs",
        "hub": "biology-and-science",
        "title_override": "Axolotl Anatomy: Gills and Lungs",
        "title_tag": "Do Axolotls Have Lungs? Anatomy of Gills & Breathing",
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
        "title_override": "Axolotl Conservation Status",
        "title_tag": "Axolotl Conservation Status: Critically Endangered, Explained",
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
        "title_override": "Axolotl Wild Habitat: Xochimilco",
        "title_tag": "Axolotl Habitat: Life in Xochimilco, Mexico City",
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
        "title_override": "Axolotl Breeder vs Pet Store",
        "title_tag": "Axolotl Breeder vs Pet Store: Where to Buy (2026)",
        "meta_override": "Compare axolotl breeders, exotic pet stores, marketplaces, and local rehomes by records, husbandry, guarantees, inspection, and shipping risk.",
        "date_modified": "2026-08-27",
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
        "title_override": "How Axolotls Are Shipped",
        "title_tag": "How Are Axolotls Shipped: What to Expect",
        "meta_override": "Learn how captive-bred axolotls are packaged and shipped, what carrier and weather details to verify, and what to do when the box arrives.",
        "date_modified": "2026-08-27",
    },
    "96 - Axolotl Adopt Me Guide.docx": {
        "slug": "axolotl-in-culture/adopt-me-axolotl-guide",
        "hub": "axolotl-in-culture",
        "title_override": "Axolotl in Adopt Me: How to Get One",
        "title_tag": "Axolotl in Adopt Me: How to Get One & All Colors (2026)",
    },
    "97 - Axolotl in Pop Culture and Memes.docx": {
        "slug": "axolotl-in-culture/axolotl-in-pop-culture-and-memes",
        "hub": "axolotl-in-culture",
        "title_override": "Axolotl in Pop Culture and Memes",
        "title_tag": "Axolotl in Pop Culture: Memes, Games, TV & Media",
        "meta_override": "Where axolotls appear in pop culture, from Minecraft and memes to TV, merchandise, and science headlines, with links to deeper guides for each topic.",
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
        "title_override": "Blue and Pink Axolotl Myth",
        "title_tag": "Blue and Pink Axolotls: The Myth Explained (No Blue Morph Exists)",
    },
    "101 - Axolotl Morphs Comparison Chart.docx": {
        "slug": "morphs/morphs-comparison-chart",
        "hub": "morphs",
        "title_override": "Axolotl Morphs Comparison Chart",
        "title_tag": "Axolotl Morphs Comparison Chart: All Colors at a Glance",
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
        "title_override": "Axolotl Stress Signs",
        "title_tag": "Axolotl Stress Signs: Curled Gills, Floating & How to Fix It",
        "date_modified": "2026-08-28",
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
        "title_override": "Axolotl Tank Size by Age",
        "title_tag": "Axolotl Tank Size by Age: How Big of a Tank Do You Need?",
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
}

# Internal linking map (source_slug -> [target_slug, ...]) applied to article
# pages automatically. Keys/values are slugs from ARTICLES (without leading /).
LINKING = {
    # Flagship guide anchors the ownership -> legal-status gateway (phase 8).
    "axolotls/care-guide": ["legal"],
    "tank-setup/setup-guide": ["tank-setup/substrate-and-impaction", "tank-setup/filtration-for-axolotls",
                               "tank-setup/temperature", "tank-setup/water-parameters-cycling"],
    "tank-setup/substrate-and-impaction": ["health/refusing-to-eat", "tank-setup/gravel-risks",
                                           "health/impaction-symptoms-treatment"],
    "tank-setup/gravel-risks": ["tank-setup/substrate-and-impaction", "tank-setup/live-vs-artificial-plants",
                                "health/impaction-symptoms-treatment"],
    "tank-setup/filtration-for-axolotls": ["tank-setup/canister-vs-sponge-filter", "tank-setup/water-parameters-cycling"],
    "tank-setup/canister-vs-sponge-filter": ["tank-setup/filtration-for-axolotls"],
    "tank-setup/water-parameters-cycling": ["tank-setup/why-tank-water-smells", "tank-setup/uneaten-food-and-ammonia"],
    "tank-setup/why-tank-water-smells": ["tank-setup/setup-guide"],
    "tank-setup/uneaten-food-and-ammonia": ["tank-setup/setup-guide"],
    "tank-setup/temperature": ["tank-setup/aquarium-chillers", "health/refusing-to-eat"],
    "tank-setup/aquarium-chillers": ["tank-setup/temperature"],
    "tank-setup/water-conditioners": ["tank-setup/acclimating-a-new-axolotl",
                                      "tank-setup/lighting-for-axolotls"],
    "tank-setup/lighting-for-axolotls": ["tank-setup/hides-and-caves"],
    "tank-setup/hides-and-caves": ["tank-setup/live-vs-artificial-plants"],
    "tank-setup/live-vs-artificial-plants": ["tank-setup/hides-and-caves", "tank-setup/lighting-for-axolotls"],
    "tank-setup/tank-size-by-age": ["tank-setup/setup-guide", "tank-setup/gravel-risks",
                                    "care-basics/axolotl-age-and-size-chart", "tank-setup/tank-mates"],
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

# Full render-time replacements for Health pages whose external DOCX source is
# either overly prescriptive or too absolute for safe owner-facing guidance.
# The source files remain the editorial record; these bodies define the public
# semantic role until the external source is revised.
BODY_OVERRIDES = {
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
        ("At a Glance: All Nine Morphs Side by Side", """
<table>
<tr><th>Morph</th><th>Body colour</th><th>Eyes</th><th>Rarity</th><th>Read more</th></tr>
<tr><td>Wild type</td><td>Dark brown / olive speckled</td><td>Dark</td><td>Common</td><td><a href="/morphs/wild-type/">Wild type</a></td></tr>
<tr><td>Leucistic</td><td>Pale pink / white</td><td>Dark</td><td>Common</td><td><a href="/morphs/leucistic/">Leucistic</a></td></tr>
<tr><td>Melanoid</td><td>Black / dark grey</td><td>Dark</td><td>Common</td><td><a href="/morphs/melanoid/">Melanoid</a></td></tr>
<tr><td>Golden albino</td><td>Pale gold / white</td><td>Red / pink</td><td>Common</td><td><a href="/morphs/golden-albino/">Golden albino</a></td></tr>
<tr><td>Copper</td><td>Copper / tan</td><td>Varies</td><td>Uncommon</td><td><a href="/morphs/copper/">Copper</a></td></tr>
<tr><td>GFP</td><td>Glows green under UV</td><td>Varies</td><td>Uncommon</td><td><a href="/morphs/gfp-axolotl/">GFP</a></td></tr>
<tr><td>Piebald</td><td>Dark with white patches</td><td>Dark</td><td>Rare</td><td><a href="/morphs/piebald/">Piebald</a></td></tr>
<tr><td>Mosaic</td><td>Patchwork of two+ colours</td><td>Varies</td><td>Rare</td><td><a href="/morphs/mosaic/">Mosaic</a></td></tr>
<tr><td>Chimera</td><td>Two fused animals on one body</td><td>Varies</td><td>Rarest</td><td><a href="/morphs/chimera/">Chimera</a></td></tr>
</table>
<p>Prices by morph are on the <a href="/cost-and-buying/axolotl-price-by-morph/">price-by-morph page</a>.</p>"""),
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

# Build-level (HTML-authored) new pages. These exist nowhere in SOURCE_DIR and
# are inserted as full articles during the build. HARD-STOP-exempt: each fills
# a genuine entity/attribute/intent cell (procedural + decision), not a keyword.
CONFIG_ARTICLES = {
    "tank-setup/water-change-guide": {
        "slug": "tank-setup/water-change-guide",
        "hub": "tank-setup",
        "title": "How to Do an Axolotl Water Change Step by Step",
        "title_tag": "Axolotl Water Change: Step-by-Step Guide",
        "meta": "A complete step-by-step guide to changing your axolotl's water - how often, how much to remove, how to treat and match replacement water, and the mistakes that stress gills.",
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

# Build trigger: retry Cost & Buying after clearing the stale queued job.
