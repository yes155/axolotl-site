# MyAxolotl Final Keyword Reconciliation Matrix

Last reconciled: 2026-09-19  
Branch: `chatgpt-work`  
Verified build: 121 articles / 121 images / 149 total pages

## Decision rules

- One canonical URL owns one primary entity + attribute + user task.
- Same-task keyword variants stay on one page.
- Split only when the user task, content format, or evidence need is meaningfully different.
- Hubs stay navigational when a specialist page owns the intent.
- Health/legal/scientific pages avoid unsupported fixed thresholds or home-treatment protocols.
- Raw keyword volumes are directional and must not be summed as unique demand.
- Teeth and general external anatomy are consolidated into the existing anatomy/gills/lungs owner; do not recreate separate URLs.

## A. New canonical content pages now implemented

| Priority | Canonical URL | Primary intent / cluster | Status | Cannibalization boundary |
|---|---|---|---|---|
| P0 | `/cost-and-buying/where-to-buy-axolotls/` | where to buy axolotl, for sale, near me, online, Petco/PetSmart availability | LIVE IN BUILD | Seller comparison, breeder vetting, healthy-animal inspection, shipping and price stay on specialists |
| P1 | `/biology-and-science/metamorphosis/` | do axolotls turn into salamanders, metamorphosed axolotl, iodine/metamorphosis | LIVE IN BUILD | Neoteny owns the developmental concept; handling owns out-of-water care |
| P1 | `/biology-and-science/axolotl-life-cycle/` | axolotl life cycle, egg-larva-juvenile-adult stages | LIVE IN BUILD | Egg Care owns husbandry; Baby Axolotl owns grow-out; Age & Size owns growth chart |
| P1 | `/morphs/albino/` | albino axolotl, white albino, albino vs leucistic, albino genetics | LIVE IN BUILD | Golden Albino remains specialist; Leucistic owns dark-eyed pale phenotype |
| P2 | `/morphs/axanthic/` | axanthic axolotl, axanthic vs melanoid, gray/lavender confusion | LIVE IN BUILD | Pigment Cells owns mechanism; Melanoid owns melanoid phenotype |
| P1 | `/tank-setup/water-change-guide/` | how to change axolotl water, how often, how much, procedure | LIVE IN BUILD | Water Parameters owns chemistry/cycling; Water Testing owns obtaining readings |
| P1 | `/tank-setup/how-to-test-water/` | how to test axolotl water, ammonia/nitrite/nitrate/pH testing, test kit procedure | LIVE IN BUILD | Water Parameters interprets results; Tracker logs results |
| P2 | `/health/healthy-axolotl-poop/` | axolotl poop, normal stool, poop frequency, fecal warning signs | LIVE IN BUILD | Parasites and Impaction own confirmed/suspected conditions |
| P1 | `/care-basics/are-axolotls-poisonous/` | are axolotls poisonous, venomous, dangerous, bites, human safety | LIVE IN BUILD | Kids page owns family suitability; Handling owns touching/transport |
| P1 | `/biology-and-science/axolotl-adaptations/` | axolotl adaptations, feeding adaptations, aquatic survival | LIVE IN BUILD | Anatomy owns structures; Habitat owns place/range; Regeneration owns regeneration |
| P2 | `/biology-and-science/axolotl-history-discovery/` | when were axolotls discovered, scientific history, 1798, Paris research history | LIVE IN BUILD | Facts keeps a short definition bridge; Habitat owns origin/location |
| P2 | `/axolotl-in-culture/do-people-eat-axolotls/` | do people eat axolotls, taste/history/culture | LIVE IN BUILD | Culture/history only; no recipe/harvest intent |
| P2 | `/axolotl-in-culture/minecraft-axolotl-enclosure-builds/` | Minecraft axolotl enclosure/build ideas | LIVE IN BUILD | Main Minecraft guide owns gameplay mechanics |
| P2 | `/axolotl-in-culture/axolotl-names/` | axolotl names, cute/funny/color name ideas | LIVE IN BUILD | Culture-only; optional generator can live on same page |
| P1 support | `/health/emergency-first-aid/` | axolotl emergency signs, triage, when to call a vet | LIVE IN BUILD | Triage/router only; individual conditions own diagnosis/treatment |

## B. Tools now implemented

| Tool URL | Primary job | Status | Boundary |
|---|---|---|---|
| `/tools/chiller-size-calculator/` | estimate chiller class from tank volume, heat load and target temperature | LIVE IN BUILD | Chiller guide owns buying/install decision; Temperature owns husbandry |
| `/tools/aquarium-volume-calculator/` | calculate gallons/liters from tank dimensions and usable fill | LIVE IN BUILD | Tank Size owns animal housing requirements |
| `/tools/tank-size-calculator/` | planning guidance by life stage and animal count | REBUILT | No invented dimension formula or per-animal multiplier |
| `/tools/nitrogen-cycle-tracker/` | record ammonia/nitrite/nitrate and track cycle trends | KEEP | Water Testing obtains readings; Water Parameters interprets them |

## C. Existing canonical pages retargeted or expanded

| Canonical URL | Primary keyword / task owner | Action completed | Key boundary |
|---|---|---|---|
| `/care-basics/axolotl-facts/` | what is an axolotl, broad entity facts | RETARGETED | Classification, habitat, history, conservation and care route to specialists |
| `/biology-and-science/conservation-status/` | are axolotls endangered, how many left | REBUILT | 2014 density is date-labeled; no invented current headcount |
| `/biology-and-science/wild-habitat-xochimilco/` | where do axolotls live, Mexico/Xochimilco habitat | RETARGETED | Adaptations split to its own page |
| `/care-basics/axolotl-age-and-size-chart/` | how big do axolotls get, size/growth chart | RETARGETED | Tank gallons belong to Tank Size |
| `/axolotls/care-guide/` | how to care for an axolotl | KEEP / STRENGTHEN | Overview/router; specialists own deep procedures |
| `/tank-setup/tank-size-by-age/` | what size tank does an axolotl need | REBUILT | 20-gallon-long practical minimum; 40 breeder preferred site recommendation |
| `/breeding/raising-juveniles/` | baby axolotl care, juvenile feeding/growth | RETARGETED | Egg care owns eggs/hatching |
| `/morphs/morphs-comparison-chart/` | axolotl colors, morph types, rarity comparison | REBUILT | Pigment Cells owns mechanism; individual morphs own details |
| `/morphs/blue-and-pink-axolotl-myth/` | pink/blue/purple/green/lavender color labels | REBUILT | Recognized morph pages own actual phenotypes |
| `/biology-and-science/anatomy-gills-and-lungs/` | axolotl anatomy, gills, lungs, teeth, ears, eyelids, senses | CONSOLIDATED | No standalone Teeth or general Anatomy URL |
| `/care-basics/are-axolotls-good-beginner-pets/` | are axolotls good pets, beginner difficulty, pros/cons | RETARGETED | Care Guide owns procedures |
| `/care-basics/handling/` | can you hold/pet an axolotl, safe handling/transport | RETARGETED | Poison/Safety owns human danger |
| `/legal/` | axolotl legality / US state overview | RETAIN AS CONSOLIDATOR | State pages only where regulation/demand warrants |
| `/biology-and-science/regeneration-and-limb-regrowth/` | axolotl regeneration science | EXPAND | Health Limb Regeneration owns injured-pet recovery |
| `/health/limb-regeneration/` | my axolotl lost a limb | RETARGETED | Biology page owns mechanism |
| `/tank-setup/water-parameters-cycling/` | axolotl water parameters, nitrogen cycle, ammonia/nitrite/nitrate/pH | RETARGETED | Water Testing obtains readings; Water Change performs procedure |
| `/tank-setup/filtration-for-axolotls/` | do axolotls need a filter, filtration/flow/sizing | REBUILT | Canister vs Sponge owns comparison |
| `/tank-setup/canister-vs-sponge-filter/` | canister vs sponge filter | REBUILT | No universal winner or invented GPH ceiling |
| `/tank-setup/temperature/` | ideal axolotl temperature, overheating, cooling methods | KEEP | Chiller page owns purchase/sizing |
| `/tank-setup/aquarium-chillers/` | best chiller approach, sizing, buying, installation | REBUILT | No stale product ranking; calculator handles estimate |
| `/diet/feeding-schedule-by-age/` | how often to feed axolotl by age/size | KEEP / DE-DUPLICATE | Fasting owns planned no-food periods |
| `/diet/fasting-and-vacation/` | how long can axolotls go without food, vacation planning | REBUILT | No unsupported universal maximum fasting windows |
| `/health/refusing-to-eat/` | axolotl not eating / appetite loss | KEEP | Unexpected appetite change, not planned fasting |
| `/health/impaction-symptoms-treatment/` | axolotl impaction / suspected GI blockage | REBUILT | No fridging protocol; substrate/gravel pages own prevention causes |
| `/health/fungal-infections-saprolegnia/` | axolotl fungus symptoms/causes/treatment decisions | REBUILT | Tea/Salt are procedure/evidence pages |
| `/health/black-tea-bath/` | black tea bath | REBUILT | Evidence limits; not canonical fungus treatment |
| `/health/salt-bath/` | axolotl salt bath | REBUILT | Veterinary saline context; no universal home recipe |
| `/health/stress-signs/` | axolotl stress signs / symptom routing | REBUILT | Curled Gills/Floating/etc. own specific symptoms |
| `/health/curled-gills-stress-signal/` | curled gills / curled tail tip | KEEP | Specific sign only |
| `/health/why-axolotl-floating/` | why is my axolotl floating | KEEP | Buoyancy-specific differential |
| `/care-basics/behavior/` | normal axolotl behavior | NARROW | Diagnostic signs route to Health |
| `/care-basics/keeping-multiple-axolotls/` | can axolotls live together, one vs two | RETARGETED | Fish/tankmates route to Tank Mates |
| `/care-basics/axolotl-intelligence-and-bonding/` | intelligence, recognition, sight/hearing/senses | EXPAND | Anatomy owns structures |
| `/axolotl-in-culture/axolotl-in-pop-culture-and-memes/` | Minecraft/Gravity Falls/Cortázar/memes/media appearances | REBUILT | Why Popular owns causes of popularity |
| `/cost-and-buying/breeder-vs-pet-store/` | breeder vs pet store | RETARGETED | Where to Buy owns discovery |
| `/cost-and-buying/choosing-a-reputable-breeder/` | how to choose a breeder | KEEP | Seller-quality evaluation |
| `/cost-and-buying/how-to-choose-a-healthy-axolotl/` | signs of a healthy axolotl before buying | KEEP / EXPAND | Animal inspection, not seller credibility |
| `/cost-and-buying/red-flags-when-buying/` | scam/bad seller red flags | KEEP / EXPAND | Transaction/seller risk |
| `/cost-and-buying/shipping-live-axolotls/` | how axolotls are shipped, unboxing, arrival | RETARGETED | Where to Buy owns discovery |
| `/cost-and-buying/axolotl-price-by-morph/` | how much does an axolotl cost, price by morph | EXPAND | Monthly ownership cost remains separate |
| `/care-basics/how-to-pronounce-axolotl/` | pronounce/spell/meaning/ajolote | RETARGETED | History page owns discovery timeline |
| `/morphs/pigment-cells/` | pigment cells, why colors change | RETARGETED | Morph comparison owns color/type discovery |
| `/breeding/egg-and-larvae-care/` | axolotl eggs, hatchling care | KEEP / EXPAND | Life Cycle owns biology sequence |
| `/diet/earthworms-vs-bloodworms/` | earthworms/red wigglers/nightcrawlers vs bloodworms | KEEP / RETARGET IF NEEDED | Best Foods remains broad diet owner |

## D. Existing owner mappings that do not need new URLs

| Keyword cluster | Canonical owner |
|---|---|
| group of axolotls called | `/care-basics/axolotl-facts/` |
| fish vs reptile vs amphibian | `/biology-and-science/is-axolotl-amphibian/` |
| axolotl predators | `/biology-and-science/wild-habitat-xochimilco/` |
| sleep / nocturnal / hibernation | `/care-basics/behavior/` |
| cannibalism / same-species biting | `/care-basics/keeping-multiple-axolotls/` and juvenile biting on Baby Axolotl |
| eyesight / hearing / recognition | `/care-basics/axolotl-intelligence-and-bonding/` |
| immortality / aging / oldest | lifespan page |
| appearance / body parts / teeth / ears / eyelids / scales | `/biology-and-science/anatomy-gills-and-lungs/` |
| giant axolotl / body size | `/care-basics/axolotl-age-and-size-chart/` |
| axolotl lookalikes / olm / tiger salamander | classification/comparison pages |
| origin / Mexico / where from | `/biology-and-science/wild-habitat-xochimilco/` |
| pet difficulty / high maintenance | `/care-basics/are-axolotls-good-beginner-pets/` |
| hold / pet / touch | `/care-basics/handling/` |
| diet classification | broad diet owner |
| feeding mechanism / hunting | `/biology-and-science/axolotl-adaptations/` |
| rarity / rarest morph | `/morphs/morphs-comparison-chart/` |
| color change | `/morphs/pigment-cells/` |
| swimming / movement mechanics | `/biology-and-science/axolotl-adaptations/` |
| reproduction / mating / birth | breeding hub + existing specialists |
| freshwater / saltwater / water type | habitat for wild context; water parameters/conditioner for aquarium |
| breathing / breathe air | `/biology-and-science/anatomy-gills-and-lungs/` |
| fish tankmates | `/tank-setup/tank-mates/` |
| one vs two axolotls | `/care-basics/keeping-multiple-axolotls/` |
| spelling / pronunciation / meaning | `/care-basics/how-to-pronounce-axolotl/` |
| lifespan | lifespan page |
| what do axolotls eat | `/diet/best-foods-list/` |
| substrate safety | `/tank-setup/substrate-and-impaction/` |
| gravel danger | `/tank-setup/gravel-risks/` |
| obesity / overfeeding | existing obesity/overfeeding page |
| ammonia injury | `/health/ammonia-burns/` |
| uneaten food → ammonia | `/tank-setup/uneaten-food-and-ammonia/` |
| smelly tank water | `/tank-setup/why-tank-water-smells/` |
| chlorine/chloramine/dechlorinator | `/tank-setup/water-conditioners/` |

## E. HOLD / conditional / exclude

| Cluster | Decision | Reason |
|---|---|---|
| Texas legality standalone page | CONDITIONAL | Create only if primary-source regulatory depth and demand justify a dedicated state URL |
| Colorado legality standalone page | HOLD | Keep in 50-state table unless demand/regulation changes |
| how to draw an axolotl | OPTIONAL P2 | Useful visual/culture page only if original step illustrations are produced |
| axolotl pictures / wallpapers / GIFs | HOLD | Image-heavy intent; weak strategic value unless building a real media asset section |
| where can I see an axolotl near me / zoo | HOLD | Local intent; better handled later with location-specific data |
| why did my axolotl die | HOLD | Too broad and medically risky for a thin generic page; health hub/triage routes symptoms |
| separate Teeth page | DO NOT CREATE | Consolidated into Anatomy owner |
| separate general Anatomy page | DO NOT CREATE | Existing Anatomy/Gills/Lungs page is the consolidated owner |
| separate Petco page | DO NOT CREATE | FAQ/date-sensitive section inside Where to Buy |
| separate PetSmart page | DO NOT CREATE | FAQ/date-sensitive section inside Where to Buy |
| separate purple/green/yellow/lavender morph pages | DO NOT CREATE | Color-label page + real morph pages own intent |
| Mudkip / Pokémon standalone page | DO NOT CREATE | Pop Culture section |
| Toothless standalone page | DO NOT CREATE | Pop Culture section |
| generic aquarium dimension pages | DO NOT CREATE | Aquarium Volume Calculator + common dimensions chart |
| xylitol / ocelot / unrelated salamander/skink/Petco contamination | EXCLUDE | Not MyAxolotl topical intent |

## F. Production order

| Phase | Work |
|---|---|
| 1 | Verify final build output and internal-link ownership on `chatgpt-work` |
| 2 | Run technical QA: canonicals, sitemap, duplicate titles/meta, missing assets, broken links, orphan pages |
| 3 | Merge `chatgpt-work` into `main` |
| 4 | Verify Cloudflare deployment on live `myaxolotl.us` |
| 5 | Submit/re-submit sitemap in Google Search Console |
| 6 | Prioritize indexing and internal links for P0/P1 pages |
| 7 | Monitor impressions/cannibalization and only create conditional pages when evidence warrants |

## Freeze decision

The topical architecture is frozen at this point. Do not create additional URLs solely because a low-KD variant exists. New pages require either:
1. a genuinely new task/entity/attribute not already owned,
2. enough depth to justify a standalone document, and
3. a clear internal-link position that does not recreate cannibalization.
