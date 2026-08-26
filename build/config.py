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
        "title": "Axolotl Health & Illness: Recognizing and Treating Problems",
        "title_tag": "Axolotl Health Problems: Symptoms & Treatment",
        "meta": "Recognize the signs of a sick axolotl and learn how to treat the most common health problems - fungus, parasites, malnutrition, and more.",
        "h1": "Axolotl Health & Illness Guide",
        "intro": "Recognizing, preventing, and treating physical problems in a live axolotl. Most axolotl illnesses trace back to water quality, diet, or husbandry - and this is where you learn to spot them early.",
        "keywords": ["axolotl health", "sick axolotl", "axolotl fungus", "axolotl parasites"],
        "cat": "Health",
    },
    "legal": {
        "title": "Is It Legal to Own an Axolotl?",
        "title_tag": "Is It Legal to Own an Axolotl? Laws by State & Country (2026)",
        "meta": "Where are axolotls legal to own? State-by-state and country-by-country rules on keeping an axolotl, including permit requirements and restricted areas.",
        "h1": "Is It Legal to Own an Axolotl?",
        "intro": "Axolotls are banned or restricted in several U.S. states and a growing list of countries because they are an endangered species. This guide explains exactly where you can and cannot legally keep one, and how to verify the law where you live.",
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
        "intro": "Breeding axolotls is a rewarding but demanding process. This guide walks you through conditioning your breeders, getting a successful spawn, raising hundreds of larvae, and breeding ethically with an understanding of the genetics.",
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
        "title_override": "When and How to Fridge a Sick Axolotl",
    },
    "35 - axolotl salt bath.docx": {
        "slug": "health/salt-bath",
        "hub": "health",
        "title_override": "Axolotl Salt Baths for Fungal Infections",
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
    },
    "55 - Understanding Axolotl Limb Regeneration.docx": {
        "slug": "health/limb-regeneration",
        "hub": "health",
        "title_override": "Understanding Axolotl Limb Regeneration",
        "title_tag": "How Axolotl Limb Regeneration Works & What to Expect",
    },
    "56 - How to Treat Axolotl Ammonia Burns.docx": {
        "slug": "health/ammonia-burns",
        "hub": "health",
        "title_override": "How to Treat Axolotl Ammonia Burns",
        "title_tag": "Axolotl Ammonia Burn: Signs, Stages & Treatment",
    },
    "57 - Recognizing Red Leg Syndrome in Axolotls.docx": {
        "slug": "health/red-leg-syndrome",
        "hub": "health",
        "title_override": "Recognizing Red Leg Syndrome in Axolotls",
        "title_tag": "Axolotl Red Leg Disease: Signs, Treatment & Prevention",
    },
    "58 - Setting Up a Hospital Quarantine Tub for Axolotls.docx": {
        "slug": "health/quarantine-tub",
        "hub": "health",
        "title_override": "Setting Up an Axolotl Hospital Quarantine Tub",
        "title_tag": "Axolotl Hospital Quarantine Tub: Setup & Care",
    },
    "59 - The Causes of Shrinking Axolotl Gills.docx": {
        "slug": "health/shrinking-gills",
        "hub": "health",
        "title_override": "The Causes of Shrinking Axolotl Gills",
        "title_tag": "Why Are My Axolotl's Gills Shrinking? Causes & Fixes",
    },
    "60 - Treating Minor Scrapes and Wounds on Axolotls.docx": {
        "slug": "health/minor-scrapes-and-wounds",
        "hub": "health",
        "title_override": "Treating Minor Scrapes and Wounds on Axolotls",
        "title_tag": "Treating Minor Axolotl Scrapes & Wounds: What to Do",
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
    },
    "91 - Axolotl Breeder vs Pet Store.docx": {
        "slug": "cost-and-buying/breeder-vs-pet-store",
        "hub": "cost-and-buying",
        "title_override": "Axolotl Breeder vs Pet Store",
        "title_tag": "Axolotl Breeder vs Pet Store: Where to Buy (2026)",
    },
    "92 - How to Choose an Axolotl Breeder.docx": {
        "slug": "cost-and-buying/choosing-a-reputable-breeder",
        "hub": "cost-and-buying",
        "title_override": "How to Choose a Reputable Axolotl Breeder",
        "title_tag": "How to Choose an Axolotl Breeder: 12 Questions to Ask",
    },
    "93 - How to Choose a Healthy Axolotl.docx": {
        "slug": "cost-and-buying/how-to-choose-a-healthy-axolotl",
        "hub": "cost-and-buying",
        "title_override": "How to Choose a Healthy Axolotl",
        "title_tag": "How to Choose a Healthy Axolotl: Signs to Check Before Buying",
    },
    "94 - Axolotl Seller Red Flags.docx": {
        "slug": "cost-and-buying/red-flags-when-buying",
        "hub": "cost-and-buying",
        "title_override": "Axolotl Seller Red Flags",
        "title_tag": "Axolotl Seller Red Flags: How to Spot Scams and Bad Breeders",
    },
    "95 - How Axolotls Are Shipped.docx": {
        "slug": "cost-and-buying/shipping-live-axolotls",
        "hub": "cost-and-buying",
        "title_override": "How Axolotls Are Shipped",
        "title_tag": "How Are Axolotls Shipped: What to Expect",
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
        "title_tag": "Axolotl in Pop Culture: Memes, Games, TV & Why They're Famous",
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
        "title_tag": "How to Find an Axolotl Vet: What to Look For & How Much It Costs",
    },
    "104 - Axolotl Stress Signs.docx": {
        "slug": "health/stress-signs",
        "hub": "health",
        "title_override": "Axolotl Stress Signs",
        "title_tag": "Axolotl Stress Signs: Curled Gills, Floating & How to Fix It",
    },
    "105 - Axolotl Impaction Symptoms and Treatment.docx": {
        "slug": "health/impaction-symptoms-treatment",
        "hub": "health",
        "title_override": "Axolotl Impaction Symptoms and Treatment",
        "title_tag": "Axolotl Impaction: Symptoms, Causes & Treatment",
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
    "tank-setup/why-tank-water-smells": ["tank-setup/water-parameters-cycling", "tank-setup/uneaten-food-and-ammonia"],
    "tank-setup/uneaten-food-and-ammonia": ["tank-setup/water-parameters-cycling", "diet/feeding-schedule-by-age"],
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
    "diet/feeder-fish-risks": ["diet/beef-heart", "diet/live-vs-frozen-food"],
    "diet/beef-heart": ["diet/feeder-fish-risks"],
    "diet/overfeeding-and-impaction": ["health/refusing-to-eat", "health/impaction-symptoms-treatment", "diet/feeding-schedule-by-age"],
    "diet/blackworms-for-juveniles": ["diet/feeding-schedule-by-age", "diet/overfeeding-and-impaction",
                                      "breeding/raising-juveniles"],
    "diet/fasting-and-vacation": ["diet/feeding-schedule-by-age"],
    "diet/how-to-hand-feed": ["diet/best-foods-list"],
    "diet/shrimp-for-axolotls": ["diet/best-foods-list", "diet/feeder-fish-risks",
                                 "breeding/egg-and-larvae-care"],
    "diet/vitamin-and-supplement-needs": ["diet/best-foods-list", "health/malnutrition-signs"],
    "health": ["health/refusing-to-eat", "health/fungal-infections-saprolegnia", "health/parasite-treatment"],
    "health/refusing-to-eat": ["diet/overfeeding-and-impaction", "health/malnutrition-signs"],
    "health/malnutrition-signs": ["health/refusing-to-eat", "diet/vitamin-and-supplement-needs",
                                  "biology-and-science/regeneration-and-limb-regrowth"],
    "health/parasite-treatment": ["health/fungal-infections-saprolegnia"],
    "health/fungal-infections-saprolegnia": ["health/black-tea-bath", "health/salt-bath", "health/fridging-sick-axolotl",
                                             "biology-and-science/anatomy-gills-and-lungs"],
    "health/black-tea-bath": ["health/fungal-infections-saprolegnia", "health/fridging-sick-axolotl"],
    "health/fridging-sick-axolotl": ["health/black-tea-bath", "health/fungal-infections-saprolegnia"],
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
    "morphs/wild-type": ["morphs/chimera", "breeding/color-genetics-punnett-squares", "morphs/leucistic",
                         "cost-and-buying/axolotl-price-by-morph"],
    "morphs/chimera": ["morphs/wild-type", "morphs/enigma-firefly-mac", "morphs/mosaic"],
    "morphs/leucistic": ["morphs/melanoid", "morphs/golden-albino", "morphs/wild-type",
                         "cost-and-buying/axolotl-price-by-morph", "morphs/blue-and-pink-axolotl-myth"],
    "morphs/melanoid": ["morphs/leucistic", "morphs/wild-type", "morphs/pigment-cells"],
    "morphs/golden-albino": ["morphs/leucistic", "morphs/gfp-axolotl", "breeding/color-genetics-punnett-squares"],
    "morphs/gfp-axolotl": ["morphs/golden-albino", "morphs/leucistic"],
    "morphs/copper": ["morphs/pigment-cells", "breeding/color-genetics-punnett-squares", "breeding/egg-and-larvae-care"],
    "morphs/piebald": ["morphs/leucistic", "morphs/chimera", "morphs/wild-type"],
    "morphs/pigment-cells": ["morphs/melanoid", "morphs/copper", "morphs/enigma-firefly-mac"],
    "morphs/enigma-firefly-mac": ["morphs/pigment-cells", "morphs/chimera", "morphs/leucistic"],
    "morphs/blue-and-pink-axolotl-myth": ["morphs/wild-type", "morphs/leucistic",
                                          "morphs/morphs-comparison-chart"],
    "morphs/morphs-comparison-chart": ["morphs/wild-type", "morphs/leucistic",
                                       "cost-and-buying/axolotl-price-by-morph"],
    "morphs/mosaic": ["morphs/chimera", "morphs/morphs-comparison-chart", "morphs/piebald"],
    "breeding/egg-and-larvae-care": ["breeding/raising-juveniles", "breeding/breeding-triggers-temperature-cycling",
                                     "diet/shrimp-for-axolotls", "diet/feeding-schedule-by-age"],
    "breeding/genetics-and-inbreeding": ["breeding/color-genetics-punnett-squares", "breeding/raising-juveniles"],
    "breeding/breeding-triggers-temperature-cycling": ["breeding/sexing-axolotls", "breeding/egg-and-larvae-care"],
    "breeding/sexing-axolotls": ["breeding/breeding-triggers-temperature-cycling"],
    "breeding/raising-juveniles": ["breeding/egg-and-larvae-care", "breeding/genetics-and-inbreeding",
                                   "diet/feeding-schedule-by-age", "diet/blackworms-for-juveniles"],
    "breeding/color-genetics-punnett-squares": ["morphs/wild-type", "morphs/chimera", "breeding/genetics-and-inbreeding"],
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
                                                "biology-and-science/neoteny",
                                                "axolotl-in-culture/why-axolotls-are-suddenly-popular",
                                                "biology-and-science/lifespan-wild-vs-captivity"],
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
                                                    "biology-and-science/neoteny"],
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
                                                    "gifts-and-merch/best-axolotl-toys-and-plushies"],
    "axolotl-in-culture/axolotl-in-pop-culture-and-memes": ["axolotl-in-culture/why-axolotls-are-suddenly-popular",
                                                            "axolotl-in-culture/minecraft-axolotls-guide",
                                                            "gifts-and-merch/axolotl-squishmallow-guide"],
    "axolotl-in-culture/why-axolotls-are-suddenly-popular": ["axolotl-in-culture/minecraft-axolotls-guide",
                                                             "biology-and-science/conservation-status",
                                                             "care-basics/axolotl-facts",
                                                             "axolotl-in-culture/adopt-me-axolotl-guide"],
    "axolotl-in-culture/adopt-me-axolotl-guide": ["axolotl-in-culture/minecraft-axolotls-guide",
                                                  "care-basics/axolotl-facts",
                                                  "cost-and-buying/axolotl-price-by-morph"],
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
}

# Role callouts inserted directly under an article's intro. These state the
# page's semantic job (and where the neighbouring page lives) so intent split
# is visible to both readers and engines without new prose in the docx.
ROLE_CALLOUTS = {
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
        '<div class="role-note"><strong>Refusing food vs planned fasting.</strong> If you '
        "deliberately let your axolotl fast, see the "
        '<a href="/diet/fasting-and-vacation/">planned fasting guide</a>. If eating has stopped '
        "unexpectedly, you are in the right place for the medical diagnosis.</div>"
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
    "health/emergency-first-aid": (
        '<div class="role-note"><strong>Urgent?</strong> If the axolotl needs a vet now, find '
        'one: <a href="/health/finding-an-exotic-vet/">exotic vet guide</a>. Everything below '
        "stabilises the animal while you get help.</div>"
    ),
}

# Extra sections appended to the body of existing articles (surgeon-level
# content layer; the .docx source is untouched). Format: heading text + HTML.
EXTRA_SECTIONS = {
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
<li><strong>Watch closely (same day):</strong> curled gills, constant hiding, clamped or receding gills, floating that comes and goes, reduced appetite &mdash; test water first; many are a water-quality problem.</li>
<li><strong>Monitor (no panic):</strong> low activity for a short period, a single bad smell in the tank, or a small nip &mdash; fix water and watch.</li>
</ul>
<h2>First Steps for Any Stressed or Sick Axolotl</h2>
<p>Four first steps apply to any sick or stressed axolotl.</p>
<ol>
<li>Test ammonia and nitrite immediately &mdash; water chemistry is behind most emergencies; see <a href="/tank-setup/water-parameters-cycling/">managing ammonia and nitrate spikes</a>.</li>
<li>Do a partial water change and confirm the temperature is in the safe range (60&ndash;68&deg;F) &mdash; follow the <a href="/tank-setup/water-change-guide/">water-change guide</a>.</li>
<li>Stop feeding until the situation is understood &mdash; an impacted or stressed axolotl needs a rest, not food.</li>
<li>Move nothing yet; observe for 30&ndash;60 minutes before isolating.</li>
</ol>
<h2>Red Flags That Need a Vet Now</h2>
<p>Six signs call for a vet now.</p>
<ul>
<li>Heavy gasping at the surface combined with limp gills.</li>
<li>Blood, an open wound, or skin sloughing.</li>
<li>Extreme bloating with a rigid body.</li>
<li>A hard, swollen belly that is clearly an impaction &mdash; <a href="/health/impaction-symptoms-treatment/">impaction symptoms and treatment</a>.</li>
<li>Reddening skin that spreads quickly &mdash; <a href="/health/red-leg-syndrome/">red leg syndrome</a>.</li>
<li>A sudden, severe appetite loss lasting more than 72 hours &mdash; <a href="/health/refusing-to-eat/">refusing to eat</a>.</li>
</ul>
<p>Find and call an <a href="/health/finding-an-exotic-vet/">exotic veterinarian</a> &mdash; call ahead so they are ready for you.</p>
<h2>What NOT to Do in an Emergency</h2>
<ul>
<li>Do not shock the animal with a huge or ultra-cold water change.</li>
<li>Do not dose "human" or unidentified medications.</li>
<li>Do not do a tea bath or salt bath without a diagnosis &mdash; the <a href="/health/fungal-infections-saprolegnia/">fungus diagnosis guide</a> decides which, if any, treatment.</li>
<li>Do not move the axolotl to completely different water without acclimation &mdash; see <a href="/tank-setup/acclimating-a-new-axolotl/">acclimating a new axolotl</a>.</li>
<li>Do not raise temperature to "speed up" recovery &mdash; axolotls need cool water.</li>
</ul>
<h2>Emergency Care by Sickness</h2>
<p>Once you have stabilised the water and identified the condition, follow the right deep guide:</p>
<ul>
<li><strong>Ammonia burns or curled gills:</strong> <a href="/health/ammonia-burns/">ammonia burns</a> and <a href="/health/curled-gills-stress-signal/">curled gills</a>.</li>
<li><strong>Severe fungus:</strong> <a href="/health/fungal-infections-saprolegnia/">fungal infections</a>.</li>
<li><strong>Floating:</strong> <a href="/health/why-axolotl-floating/">why is my axolotl floating</a>.</li>
<li><strong>Not eating:</strong> <a href="/health/refusing-to-eat/">refusing to eat</a>.</li>
<li><strong>Bleeding or injury:</strong> <a href="/health/minor-scrapes-and-wounds/">minor scrapes and wounds</a>.</li>
</ul>
<h2>Aftercare and Prevention</h2>
<p>Once stable, keep the animal quiet and isolated while it recovers &mdash; <a href="/health/quarantine-tub/">quarantine tub</a> &mdash; and keep ammonia and nitrite at zero. Most medical reminders are husbandry reminders: stable cool temperature, gentle filtration, and a routine/weekly change cycle prevent the overwhelming majority of emergencies.</p>
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
