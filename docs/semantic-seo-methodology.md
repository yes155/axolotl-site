# Semantic SEO Methodology (AxolotlCare)

Working methodology for the Axolotl Care Guide site (`axolotlcare`), grounded in the
semantic-SEO literature of Koray Tuğberk Gübür / Holistic SEO and applied to this
corpus. This document exists so that every later audit decision — content, linking,
architecture — is made against an explicit, consistent model instead of generic
"good SEO" intuition.

**Status:** Phase 7A bootstrap. Approved, this document becomes the lens for the
Phase 7/7 later audit. Per §16, nothing on the site may change until this methodology
is agreed.

---

## 0. Purpose and scope

- This is a **working methodology**, not a literature review. Every concept below is
  written so it can be *acted on* against the Axolotl corpus.
- The site is a static hub-and-spoke corpus: 106 articles, 12 hubs, 6 tools, plus
  boilerplate (130 pages total). Primary hub clusters:
  - Core care: tank-setup, diet, health, care-basics
  - Progression / outer: morphs, breeding, cost-and-buying, legal,
    biology-and-science, axolotl-in-culture, gifts-and-merch, tools
- Sources studied (primary where possible):
  - Gübür, K. *Importance of Topical Authority for SEO* — holisticseo.digital/theoretical-seo/topical-authority/
  - Gübür, K. *Entity Attribute Value* — holisticseo.digital/seo-research-study/entity-attribute-value/
  - Gübür, K. *Ranking* — holisticseo.digital/theoretical-seo/ranking/
  - Gübür, K. *Outer Section of Topical Maps — Why It Matters* — LinkedIn (2025-08-12)
  - Gübür, K. interview — sitechecker.pro (2023-03-13)
  - Community application notes on Prominence/Popularity/Relevance scoring (PPR) —
    treated as an *operational approximation only*, not an official Google or Koray metric.

---

## 1. Core concepts

Each concept follows the same 8 facets:

1. Definition
2. Why it matters
3. On-site (AxolotlCare) evidence
4. How it is measured / audited
5. Effect on content architecture
6. Effect on internal linking
7. Effect on page-level content
8. Common mistakes

### 1.1 Semantic SEO

1. **Definition.** Semantic SEO is optimizing for **meaning** — entities, their
   attributes, their states and the relationships between them — rather than for
   individual keyword strings. The unit of work is the **concept**, not the query.
2. **Why it matters.** Search engines now parse documents into entity graphs. A page
   that *means* a concept completely and correctly is more useful than a page that
   merely repeats a phrase. Meaning compounds across a site; keyword targeting does
   not.
3. **On-site evidence.** The site already has healthy semantic raw material: 130
   pages about one central entity (the axolotl) with strong cross-topic links
   (e.g. `/health/refusing-to-eat` ↔ diet, tank-setup). The failure risk is that these
   relations were authored informally, not against a model.
4. **How it is measured.** For each page, ask: "What entity/attribute/state does this
   page answer, and does it answer the *dominant* information need completely?" — a
   manual review checklist, not a keyword-density tool.
5. **Effect on architecture.** Content is organized by entity-and-attribute space
   (topical map), not by keyword buckets.
6. **Effect on internal linking.** Links exist to assert *semantic relationships*
   (cause → effect, symptom → treatment, prerequisite → procedure), never to "spread
   authority."
7. **Effect on page content.** The page is written as a complete answer to one
   distinct need, with all relevant attributes/states covered, in natural,
   evidence-first prose.
8. **Common mistakes.** Treating semantic SEO as "write about related keywords";
   assuming any long-form article is automatically semantic; measuring success by
   keyword rank alone.

### 1.2 Topical Authority

1. **Definition.** The degree to which a site is, per Google, "an authority for [a]
   specific niche" — a comprehensive, expertly-maintained body of content around one
   central topic. Concept founding (per Gübür): Holistic SEO's Topical Authority
   line, first published 18 May 2022, with a documented case of one site going from
   ~0 to ~128,000 organic clicks/month in 123 days.
2. **Why it matters.** Authority is **interpretive**: Google decides how much weight a
   page's answers deserve based on how completely the site covers the surrounding
   topic. Authority cannot be purchased; it is accumulated by coverage + agreement
   with the site's source context.
3. **On-site evidence.** The site is topically narrow (one species), which is ideal
   soil. Its gaps are conceptual, not keyword gaps — e.g. the morphs cluster answers
   "what is this morph" but mostly lacks the related "how do the pigment-cell
   mechanisms differ" layer.
4. **How it is measured.** Qualitative: does every entity/attribute/state in the
   map have an authoritative answer on-site, and do answers agree with each other?
   Quantitative proxy: coverage ratio of map nodes → built pages.
5. **Effect on architecture.** The whole site is a single topical tree with one
   central entity at the root (see §4).
6. **Effect on internal linking.** Links concentrate relevance toward the central
   entity and its core sections, so authority accumulates topically.
7. **Effect on page content.** Every page is written as a complete, consistent answer
   within the corpus; contradictions between pages destroy authority.
8. **Common mistakes.** Adding volume without cohesion; monetizing the core before
   the outer authority sections exist; treating "we have an article about everything"
   as authority.

### 1.3 Topical Maps

1. **Definition.** A structured, layered model of everything relevant to the central
   topic, from broadest context down to individual pages. It is the *operational
   tool* of Topical Authority: the map is designed first, pages are written to fill
   map cells.
2. **Why it matters.** Without a map, decisions about what to write and how to link
   are ad hoc. The map makes coverage, gaps, and cannibalization visible and
   debatable.
3. **On-site evidence.** `/docs/phase7/topical-map.json` and `topical-map.md` describe
   the *existing* corpus clusters (11 clusters). Phase 7A's job is to rebuild this as
   a *normative* map using the §4 hierarchy, not just describe what exists.
4. **How it is measured.** Does every layer of the hierarchy exist? Is each node
   represented by a built page or an explicit decision to omit it?
5. **Effect on architecture.** The site's folder/hub structure mirrors the map.
6. **Effect on internal linking.** Parent/child and sibling relations in the map are
   the primary link patterns.
7. **Effect on page content.** Each page is scoped to one node's job (see §14 roles).
8. **Common mistakes.** A map that is just a keyword list; maps that flatten layers
   into "categories"; maps that never get used to audit the site.

### 1.4 Source Context

1. **Definition.** The framing, purpose, and expert standpoint from which the whole
   site speaks — e.g. "evidence-based axolotl pet-keeping for owners and prospective
   owners," not "a generic pet blog."
2. **Why it matters.** The source context scopes *which* meanings are relevant and
   *how strong* claims may be. It is the top layer of the topical map; everything
   below it must be coherent with it.
3. **On-site evidence.** The site's own tagline: "Evidence-based axolotl care, tank
   setup, diet, and health guides." That is the source context to hold everything to.
4. **How it is measured.** Consistency audit: does any page make claims that fight
   the evidence-first, owner-focused framing (e.g. sales-y hype in a health page)?
5. **Effect on architecture.** Determines which clusters are *inside* the map at all
   (e.g. gifts-and-merch is peripheral, see §5).
6. **Effect on internal linking.** Content linking is chosen to build the owner's
   decision journey, not to maximize clicks.
7. **Effect on page content.** Tonal and evidentiary standards set at this layer
   (cite sources, distinguish fact from opinion, no medical overreach).
8. **Common mistakes.** No stated context (site drifts); context so broad it can't
   exclude anything.

### 1.5 Central Entity

1. **Definition.** The single most important entity the site is about — the object
   every other node ultimately serves. Here: **the axolotl (*Ambystoma mexicanum*)**.
2. **Why it matters.** Topical authority is impossible without a defined central
   entity; Google needs to be able to label the site's purpose in one entity.
3. **On-site evidence.** The corpus is 130 pages deep, all about one animal — strong.
   The weak spot is the homepage H1 (`My Axolotl — Everything...`), which does not
   restate the entity/name the map says is central.
4. **How it is measured.** "If a reader saw only the homepage and hub titles, could
   they name the central entity and its context in one sentence?" — a 5-second test.
5. **Effect on architecture.** Everything flows from this root; hubs are its major
   attribute/facet groups.
6. **Effect on internal linking.** All paths should converge toward the central
   entity's canonical page (`/axolotls/care-guide`).
7. **Effect on page content.** Pages keep the entity present in intro, title, and
   FAQ without keyword-stuffing.
8. **Common mistakes.** Fuzzy entity ("pets"); multiple competing central entities;
   letting individual hubs act like separate sites.

### 1.6 Central Search Intent

1. **Definition.** The single dominant need the entire site exists to satisfy (the
   "big query" users come with). For AxolotlCare: *"How do I properly care for an
   axolotl — and what do I need to know before I keep one?"*
2. **Why it matters.** The site's information hierarchy and the ordering of the map
   layers are driven by this intent. It decides what belongs in the core section vs.
   the outer section.
3. **On-site evidence.** The current hub hierarchy (care/tank/diet/health first) already
   anticipates this; it needs to be *stated* so it can be enforced.
4. **How it is measured.** Every page answers a sub-question of the central intent —
   if a page's question cannot be traced back to it, the page is out-of-scope or
   misfiled.
5. **Effect on architecture.** Core section = the direct path through the central
   intent; outer section = supporting/contextual questions.
6. **Effect on internal linking.** Primary journeys link along the spine of the
   central intent; auxiliary journeys branch off.
7. **Effect on page content.** Each page states its question in the H1/title and
   answers it completely before diverting.
8. **Common mistakes.** Trying to serve several incompatible intents on one page;
   losing the central intent in the outer-section sprawl.

### 1.7 Core Section

1. **Definition.** The cluster of pages that directly fulfills the central search
   intent and, per Gübür's "outer section" framing, serves as the **monetization and
   conversion hub** — the part users must land on to get their need met and where the
   site earns trust (and, where applicable, revenue).
2. **Why it matters.** Authority is earned *through* the core; the outer section
   feeds it. If the core is weak, no amount of outer content helps.
3. **On-site evidence.** Tank-setup, diet, health, care-basics are the natural core.
   Several are falling short: e.g. `/tank-setup/water-parameters-cycling` has the
   highest inbound (15) but no FAQ block; `/health/refusing-to-eat` is strong (in=11).
4. **How it is measured.** Do core pages comprehensively answer their central question
   (coverage of attributes/states), and does the graph funnel inbound links into the
   core rather than away from it?
5. **Effect on architecture.** Core pages sit close to the root (≤2 clicks), always
   linked from hubs.
6. **Effect on internal linking.** Core pages receive the densest inbound context;
   they link down to supporting detail rather than to other core pages redundantly.
7. **Effect on page content.** Highest rigour standard; most complete attribute
   coverage; FAQ blocks expected.
8. **Common mistakes.** Monetizing before building the core; making the core thin
   while spending all effort on trendy outer content.

### 1.8 Outer Section

1. **Definition.** All nodes outside the direct fulfillment of the central intent —
   supporting, contextual, adjacent, and peripheral topics that *build and deepen
   authority* around the central entity (Gübür: the outer section is what makes the
   core an authority rather than an ordinary how-to page).
2. **Why it matters.** The outer section proves the site *knows* its topic deeply,
   captures intent variants (e.g. "is it legal," "what morph is this"), and feeds
   contextual links into the core.
3. **On-site evidence.** Morphs, breeding, legal, biology, culture, gifts serve this
   role — unevenly: morphology pages are thin (many <600 words), which weakens their
   authority-building job.
4. **How it is measured.** Does each outer node link to (and get linked from) the
   core with a *meaningful* relationship, and does it fully answer its own question?
5. **Effect on architecture.** Outer nodes are the leaves and branches; depth of a
   leaf is bounded (≤3-4 clicks) so relevance still flows.
6. **Effect on internal linking.** Outer pages link *up* to the core through
   contextual vectors; the core links *down* to outer pages for specifics.
7. **Effect on page content.** Complete answer for their narrow question + explicit
   link back to where they fit in the core journey.
8. **Common mistakes.** Letting the outer section become link farms or keyword
   variations; outer pages that never connect back to the core.

### 1.9 Topical Borders

1. **Definition.** The crisp line between what is *inside* the topic (in the map),
   *adjacent* (directly relevant context), *peripheral* (loosely related, optional),
   and *outside* (do not create). Keeping this line is what makes authority coherent.
2. **Why it matters.** Content outside the borders dilutes the entity focus the map
   and Google depend on.
3. **On-site evidence.** Gifts-and-merch is *peripheral* for an owner-focused, care
   site; "biology vs. pet care" tension is *adjacent* (needed to support care claims);
   general aquarium content (e.g. fishes unrelated to axolotls) would be *outside*.
4. **How it is measured.** A node is placed by answering (a) does it serve the
   central entity? (b) does it serve the central search intent? (c) does it support
   the core? Score = inside/adjacent/peripheral/outside.
5. **Effect on architecture.** The map is pruned to the inside/adjacent ring; outside
   topics get no page, no budget.
6. **Effect on internal linking.** No links across the border in either direction
   (a link is a relevance endorsement).
7. **Effect on page content.** Peripheral pages are kept slim so they do not pull
   focus from the core.
8. **Common mistakes.** Infinite sprawl ("we could cover all salamander species");
   adding pages to chase search volume regardless of border relevance.

### 1.10 Topical Coverage

1. **Definition.** The proportion of the *conceptual* map (entities, attributes,
   states, relationships, intents, and bridges) that the corpus actually answers.
2. **Why it matters.** Coverage is what authority is scored on. A missing *attribute*
   of the central entity is a gap even if no search query for it exists yet.
3. **On-site evidence.** Probable gaps under this lens: tank-setup lacks an explicit
   "water quality troubleshooting decision tree"; morphs lacks a connective
   "pigment-cell mechanisms" explanatory layer (§8).
4. **How it is measured.** Compare map nodes → built pages (coverage ratio), *then*
   verify coverage qualitatively with the E-A-V checklist (§6).
5. **Effect on architecture.** New pages are justified by map nodes, not by ad hoc
   topic ideas.
6. **Effect on internal linking.** Bridging content (nodes that connect two clusters)
   is considered its own coverage goal.
7. **Effect on page content.** A page's completeness is judged as "does it cover the
   node's attributes/states" rather than "does it hit an arbitrary word count."
8. **Common mistakes.** Treating coverage as keyword-count; declaring coverage
   complete because a page exists for every cluster name.

### 1.11 Topical Relevance

1. **Definition.** How closely a page's meaning aligns with the topical map and the
   central entity — a *structural* property (is it about the right thing?) distinct
   from popularity (do people want it?) and prominence (how central is it in the
   graph?).
2. **Why it matters.** Relevance is the gate: a highly popular but irrelevant page
   (e.g. a viral meme article) actually *hurts* a care site's authority if it pulls
   the entity focus off-center.
3. **On-site evidence.** Pop-culture pages (e.g. Adopt Me, Minecraft) are relevant
   *because* they concern the central entity's popularity context; they become
   irrelevant if they slide into generic gaming content.
4. **How it is measured.** Manual placement on the inside/adjacent/peripheral scale
   §1.9 + does each claims link back to the central entity.
5. **Effect on architecture.** Relevance decides membership in the map; see borders §1.9.
6. **Effect on internal linking.** Only relevant nodes may link into the core.
7. **Effect on page content.** Every page keeps a visible, honest connection to the
   central entity.
8. **Common mistakes.** Confusing relevance with traffic volume; relevance scored by
   keyword overlap rather than meaning.

### 1.12 Prominence, Popularity, Relevance (PPR)

1. **Definition.** A tri-factor way of thinking about how to prioritize nodes in the
   topical map:
   - **Prominence** — the node's *centrality* in the site's semantic network (how many
     routes pass through it).
   - **Popularity** — evidence of *search intent + usage frequency* (people actually
     ask for this).
   - **Relevance** — alignment with the central entity and source context (§1.11).
2. **Why it matters.** PPR keeps prioritization honest: a page can be prominent and
   relevant but unpopular (deep care detail), or popular and relevant but not yet
   prominent (a morph someone keeps searching for). Each gets a different treatment.
3. **On-site evidence.** Example: `/tank-setup/water-parameters-cycling` is prominent
   (in=15) and highly relevant, medium popularity → protect and expand it.
   `/morphs/leucistic` is high inbound *because* morph searches are popular → use it as
   a hub for the outer morph cluster.
4. **How it is measured.** Manual scoring with the site's own data (linkgraph in/out,
   FAQ coverage, page quality flags). **Important caveat (per §16):** any numeric PPR
   score we compute is an *operational approximation* of the concept, *not* an
   official Google metric or a published Koray scoring algorithm. We will say so in
   every report that uses numbers.
5. **Effect on architecture.** PPR ranks candidate pages for creation/expansion;
   prominence is a *result* of good structure, not a target to fake.
6. **Effect on internal linking.** Links create prominence; so prominence is steered
   by how we link, and we link toward the nodes we want to be prominent (core + popular
   relevant outer nodes).
7. **Effect on page content.** Popularity tells us which content needs *depth and
   freshness* first; relevance tells us which content must exist at all.
8. **Common mistakes.** Treating PPR as a magic formula; maximizing popularity at the
   expense of relevance; mistaking inbound-links-only for prominence.

### 1.13 Semantic Content Networks

1. **Definition.** The graph of pages connected by *meaningful relationships*
   (parent→child, prerequisite→procedure, cause→effect, symptom→cause, problem→solution,
   general→specific, concept→tool, comparison→alternatives, biology→practical) — the
   practical realization of the topical map in the site's link structure.
2. **Why it matters.** A network is how a crawler and an LLM both assemble the site's
   meaning. "Related articles" with no relationship semantics is noise, not a network.
3. **On-site evidence.** The existing LINKING map in `build/config.py` already encodes
   meaningful edges (e.g. `/health/fungal-infections-saprolegnia` → tea bath/salt
   bath/fridging = treatment-procedure relations). The job is to re-type every edge by
   *relation kind*, not just existence.
4. **How it is measured.** Every internal link is tagged with its semantic relation
   type; untagged or "related for the sake of relatedness" links are flagged.
5. **Effect on architecture.** The network *is* the architecture: hubs are the
   high-degree nodes, bridges connect clusters.
6. **Effect on internal linking.** Links are chosen by relation type (see §9 list),
   not by "this page mentioned the other topic."
7. **Effect on page content.** Content is written to make relations explicit in
   anchor text and in-flow sentences ("like ammonia burns, fungus responds to... see
   treatment").
8. **Common mistakes.** Link swamps; "related articles" widgets that point to
   anything in the same folder; accepting generic topical similarity as a real edge.

### 1.14 Contextual Vectors

1. **Definition.** The set of *surrounding concepts* that must be present (on the
   page or via links) for a page's meaning to be fully understood — e.g. "water
   temperature" is a vector *around* "stringing/refusing to eat," because metabolism,
   cooling, and stress all travel with it.
2. **Why it matters.** A page that answers a question without its contextual vectors
   leaves meaning gaps the engine must guess; vectors are what make single pages
   semantically complete in context.
3. **On-site evidence.** `/health/curled-gills-stress-signal` correctly pulls in
   water parameters, shrinking gills, ammonia burns, stress signs — that *is* a
   contextual vector set, currently implemented as links without being modeled.
4. **How it is measured.** For each page: list the concepts that must co-occur for
   the answer to be complete; check page body + first-hop links against the list.
5. **Effect on architecture.** Vectors justify bridge pages and cross-cluster links;
   they are the "why" behind §5's relevance rules.
6. **Effect on internal linking.** Contextual vectors determine *which* links a page
   needs beyond its parent/child spine.
7. **Effect on page content.** Vectors surface as short definitional/relationship
   passages and in-flow links, not stuffed keyword clusters.
8. **Common mistakes.** Equating vectors with keyword lists; adding every possible
   vector instead of only the ones needed for comprehension.

### 1.15 Entity-Attribute-Value (E-A-V)

1. **Definition.** The modeling unit of semantic SEO: an **Entity** (thing) has
   **Attributes** (properties) that take **Values** (or States). E.g. Entity = axolotl
   gills; Attribute = curl; Values/States = healthy / slightly curled / tightly curled
   (stress). In Gübür's EAV material this is the "object–attribute–value" / open-schema
   backbone search systems and LLMs both use.
2. **Why it matters.** Every useful page decomposes to structured fact triples; a
   corpus that covers attributes and their states consistently is *machine-readable
   meaning*.
3. **On-site evidence.** The health cluster is naturally E-A-V rich (symptom →
   attribute-state). Morphs are attribute-state rich *in fact* but written thinly.
4. **How it is measured.** Audit a page by extracting its triples; a page is complete
   when the attribute's full state space is covered for its job.
5. **Effect on architecture.** The map's middle layers are literally E-A-V layers
   (§4 layers 7-10: topics → subtopics → entities → attributes → values/states).
6. **Effect on internal linking.** Related-attribute pages link to each other
   (e.g. curling gills ↔ shrinking gills share the attribute *gill morphology*).
7. **Effect on page content.** Each section is written to answer one or more
   attribute-state questions explicitly ("What does a healthy gill look like?").
8. **Common mistakes.** Listing attributes without states; covering one popular value
   and ignoring the rest of the state space (e.g. "sick gills" but never "healthy").

### 1.16 Search Intent

1. **Definition.** The *type of need* behind a query. The taxonomy used for
   AxolotlCare:
   - informational, definitional, procedural, diagnostic, comparative, transactional,
     navigational, tool/calculator, location-specific, problem-solving.
2. **Why it matters.** Intent decides page type, role, and structure (a diagnostic
   page and a comparative page about the same entity are different deliverables).
3. **On-site evidence.** The phase-7 audit classified pages with a 4-bucket scheme
   (informational 84 / commercial 12 / commercial-investigation 10 / trans 5); Phase 7A
   refines this to the 10-value taxonomy above. Many pages sit in more than one intent;
   the rule is the **dominant** one wins.
4. **How it is measured.** For each page: state its dominant intent in one clause; the
   page's H1, structure, and intro must match it.
5. **Effect on architecture.** The map holds intent as a property of each page-node;
   tool pages (calculators) are a real intent, not a separate category.
6. **Effect on internal linking.** Intent transitions chain naturally
   (diagnostic → procedural → transactional), and links can signal those transitions.
7. **Effect on page content.** Structure follows intent: procedural = ordered steps;
   diagnostic = symptom → cause → fix; comparative = criteria table; location = legality
   per region.
8. **Common mistakes.** Writing every page as informational; mixing intents on one
   page so no intent is served completely; ignoring tool/calculator and
   location-specific intents.

### 1.17 Information Hierarchy

1. **Definition.** The intended ordering of information on and across pages: what is
   stated first, what is linked first, what is deferred — all driven by the central
   search intent (§1.6).
2. **Why it matters.** Both users and engines extract meaning in reading order.
   Priority inversion (burying the answer three sections down) breaks the page's job.
3. **On-site evidence.** Hub layout already implies a hierarchy (intro → guides);
   several pages read as "everything we know" instead of "answer first, then context."
4. **How it is measured.** The "answer above the fold" test per page + ordering of H2s
   vs. the dominant intent.
5. **Effect on architecture.** Root→hub→spoke mirrors the hierarchy; depth is bounded.
6. **Effect on internal linking.** First links carry the strongest relevance signal;
   they point to the most central next step.
7. **Effect on page content.** Title/H1 holds the question, first section the direct
   answer, later sections the context, FAQ the long-tail variants.
8. **Common mistakes.** Answer-late pages; hierarchy copied from another site's
   outline instead of from the intent.

### 1.18 Query Networks

1. **Definition.** The connected cloud of queries people actually ask about the
   topic — clusters of questions that share entities, attributes, or intents
   (Gübür's "query templates" / "query paths" concept: related queries form paths of
   progressive refinement).
2. **Why it matters.** Query networks show which pages users will thread through;
   covering a query *network* (not isolated keywords) is how a site becomes the
   default answer set.
3. **On-site evidence.** E.g. the network "tank cycling → ammonia spike → curled gills
   → refusing to eat → treatment" already exists as pages + links; it needs to be
   *completed and typed*.
4. **How it is measured.** Group the corpus's questions into networks; coverage is
   per-network (a network with a hole is a hole in the journey).
5. **Effect on architecture.** Bridge pages are placed where two query networks meet.
6. **Effect on internal linking.** Links enumerate the query path ("next question a
   reader with this one is likely to have") = a real semantic edge.
7. **Effect on page content.** FAQ blocks are drawn from the surrounding query
   network, so they feel like the next questions, not filler.
8. **Common mistakes.** Optimizing single keywords in isolation; FAQ sections that
   invent questions nobody chains together.

### 1.19 Contextual Internal Linking

1. **Definition.** Internal links chosen because they advance *understanding of the
   current content*, in-flow (in the body where the concept is discussed), not in
   generic widgets. The rule from Gübür that anchors this methodology: **link to build
   the correct semantic relationships, not to maximize the number of links.**
2. **Why it matters.** A link is a relevance vote *with meaning* attached. Wrong or
   bloated links dilute the signal and waste authority on low-value targets.
3. **On-site evidence.** The current LINKING map is mostly thoughtful; the phase-7
   "cross-topic secondary signals" list shows a few forced edges worth questioning
   (e.g. slides toward cost-buying from health/tank pages via cheap word-boundary
   hits like "price" — see §13).
4. **How it is measured.** Every link gets a relation type (§9); links with no
   defensible relation type are candidates for removal; anchor text describes the
   target's meaning.
5. **Effect on architecture.** Link structure is a *projection of the map*, so map
   corrections flow through to links automatically.
6. **Effect on internal linking.** In-flow contextual links preferred; hub links for
   navigation; "related articles" only when the relation is real.
7. **Effect on page content.** Content is written with link *points* in mind (a
   sentence that needs a supporting reference), never links bolted onto the end.
8. **Common mistakes.** Footer/link-swamp link spam; using exact-match anchors
   everywhere; linking to prove coverage instead of meaning.

### 1.20 Content Consolidation

1. **Definition.** The practice of merging or pruning pages that serve the *same*
   entity-attribute-intent cell into one strong page (and 301/redirecting the rest),
   so the site has exactly one best answer per node.
2. **Why it matters.** Duplicate answers split the authority that a single complete
   answer would own; consolidation is what turns a "set of articles" into a *corpus*.
3. **On-site evidence.** Candidate consolidations under this lens: multiple legal
   state pages share a single methodology (they are variant *location-specific* intents
   of one node — see §14) and morph pages that all thin out on the same shared
   "pigment cells" question.
4. **How it is measured.** Cluster pages by central entity + attribute + dominant
   intent; within a cluster, one canonical winner per distinct question cell.
5. **Effect on architecture.** The map's node budget consciously limits pages per node.
6. **Effect on internal linking.** All links to a consolidated node point to the one
   surviving page (authority is no longer split).
7. **Effect on page content.** The survivor absorbs the best of each; the intro states
   the merged scope explicitly.
8. **Common mistakes.** Merging pages that actually serve different intents (that is
   cannibalization removal done wrong — §13); consolidating away needed variants
   (location pages usually stay separate).

### 1.21 Semantic Distance

1. **Definition.** How far two nodes are from each other in meaning — measured in
   *conceptual* hops (how many intermediate concepts you must pass through), not link
   hops or string similarity.
2. **Why it matters.** Semantic distance decides *where* relationships are real
   (direct link) versus *contextual* (bridge page needed). Clusters on the map are
   formed by small semantic distance within and large distance between.
3. **On-site evidence.** E.g. "curl stress" is semantically close to "water
   parameters" (same cause), far from "Build-A-Bear." The current link graph mixes
   both distances indiscriminately.
4. **How it is measured.** Judgment call (this is qualitative): for a candidate link,
   ask "how many concepts does the reader need to hold to see the connection?" — 0-1 =
   direct link, 2+ = bridge page or no link.
5. **Effect on architecture.** Bridge pages exist precisely to shorten long-range
   semantic distance between two clusters.
6. **Effect on internal linking.** Direct links only across small distance; large
   distance is bridged, not force-linked.
7. **Effect on page content.** Content may *mention* a distant concept (as context)
   without a link; linking it would create a noisy edge.
8. **Common mistakes.** Linking everything that merely mentions another topic; putting
   unrelated content in the same folder because the URLs are adjacent.

### 1.22 Topical Completeness

1. **Definition.** The state where every entity, attribute, state, relationship,
   intent, and bridge the map calls for has a complete answer on-site — the terminal
   goal of this methodology.
2. **Why it matters.** Completeness is what a search engine can credit as authority;
   an otherwise perfect corpus with one unfilled core attribute is incomplete.
3. **On-site evidence.** The site is *not* complete: dozens of thin/no-FAQ pages flag
   this; the conceptual gaps in §1.10/§8 forms the completeness backlog.
4. **How it is measured.** Coverage ratio + E-A-V state-space check + query-network
   audit, all three reporting to one completeness scorecard.
5. **Effect on architecture.** Completeness is the target the map is audited against;
   the map is updated when the last node is built or consciously pruned.
6. **Effect on internal linking.** Completeness unlocks the dense, typed network in
   §1.13; partial coverage keeps some links one-directional.
7. **Effect on page content.** Content plans aim for *map-down* completeness rather
   than *keyword-up* volume.
8. **Common mistakes.** Treating "something on every topic" as completeness; never
   pruning — completeness includes the *ability to say no* to nodes outside borders.

---

## 2. Semantic SEO vs. generic SEO

Generic ("keyword") SEO optimizes for **query strings**: pick keywords, target page
per keyword, optimize meta/title/density, add links "for authority." Semantic SEO
optimizes for **meaning**: model the topic, build coverage of entity-attribute-value
space, and link to express relationships.

**Why generic tactics are insufficient here (each is a trap for this site):**

| Generic tactic | Semantic critique |
|---|---|
| Keyword density/DEK optimization | Density says nothing about whether the page answers the question. A page can be thin in meaning and dense in a phrase. |
| Targeting keyword volume | Volume measures *demand*, not *importance*. A rare morph query is low-volume but must exist for completeness. Volume-driven only finds the popular 10%, not the authority 100%. |
| Creating keyword variations as pages | Variations of one meaning = cannibalization (e.g. three "shrimp" pages differing only in phrasing). One complete page wins. |
| Publishing many articles | Volume without map-coherence dilutes the entity; 30 well-linked, complete pages beat 130 disconnected ones. |
| Adding FAQ blocks everywhere | Only helpful when the FAQs are the *next questions in the network* (query network §1.18). Mechanical FAQs are filler. |
| Adding internal links everywhere | More links ≠ more authority. **Correct semantic relationships** do (see §1.19). Wrong links cost authority. |
| Building category pages | A category list is not a semantic hub unless it aggregates meaning around an entity-attribute, not a tag. |
| Exact-match keyword focus | Exact matching ignores synonymy and paraphrase — meaning survives rephrasing; phrases don't. |

**Operational summary:** generic SEO asks *what should we rank for*; semantic SEO asks
*what must we know, and have we answered it completely, correctly, and connected*. The
Axolotl site is built to be audited the second way.

---

## 3. Building the topical map (12 layers)

The map is constructed top-down in these layers. **Do not flatten layers into
"categories."** A category is a label; a layer is a *level of abstraction in meaning*.

1. **Source Context** — the framing "evidence-based axolotl pet care for owners."
2. **Central Entity** — the axolotl (*Ambystoma mexicanum*).
3. **Central Search Intent** — "how do I care for an axolotl correctly."
4. **Core Section** — the clusters that fulfill the central intent: tank-setup, diet,
   health, care-basics.
5. **Outer Section** — supporting/contextual clusters: morphs, breeding,
   cost-and-buying, legal, biology, culture, gifts, tools.
6. **Topics** — the large subject-matter groups (e.g. water quality, feeding,
   illness, morph appearance, reproduction, legality).
7. **Subtopics** — the specialties inside a topic (e.g. cycling, temperature,
   filtration inside water quality).
8. **Entities** — the concrete things in the subtopic (e.g. the nitrogen cycle, the
   aquarium chiller, *Saprolegnia* fungus).
9. **Attributes** — properties of those entities (e.g. gill curl state, ammonia
   concentration, morph color pigment).
10. **Values/States** — the values or states of each attribute (e.g. normal/flushed,
    curled/tight, healthy/stressed).
11. **Search Intents** — the questions/needs attached to each node
    (diagnosis vs. prevention vs. shopping vs. legality).
12. **Pages** — the concrete pages that answer the intents.

**How it applies to AxolotlCare today:** the existing `topical-map.json` was built
*bottom-up* (it describes pages that exist). The rebuild must be *top-down* (from
layer 1) so that layer 4/5 (core vs. outer) and layer 8-10 (entity-attribute-value)
are definite, and pages (layer 12) hang off a designed tree instead of defining it.

---

## 4. Topical borders and dilution

- **Inside** — serves the central entity and central intent (all of core;
  most of morphs/breeding/legal/cost as owner-related).
- **Adjacent** — needed context to support inside claims (biology-and-science:
  regeneration, neoteny, habitat give the scientific backing for care claims).
- **Peripheral** — loosely related, optional, kept slim (gifts-and-merch, some
  pop-culture pages; they feed popularity without diluting care authority).
- **Outside** — not in the map at all (general aquarium-keeping; other amphibians as
  subjects; unrelated gaming content).

**Topical dilution:** every page outside the inside-adjacent ring, or inside the ring
but off-entity, pulls the site's labeled purpose away from "axolotl care." The
tripwire: if a page's *dominant* subject is not the axolotl and its care/context, it is
a dilution candidate.

**Application:** score each current cluster on this scale (scorecard in the next phase);
keep peripheral clusters *shallow* on purpose so budget flows to the core.

---

## 5. Entity model and relationships (E-A-V → CAUSE → EFFECT → ACTION)

The full relation chain a good page/corpus expresses:

```
ENTITY → ATTRIBUTE → STATE → CAUSE → EFFECT → ACTION/SOLUTION
```

**Worked example (gills):** axolotl (entity) → gill posture (attribute) →
healthy/curled/tight (states) → warm water, ammonia, stress (causes) → appetite loss,
decreased movement (effects) → cool water, water change, quarantine (action).

**Where relations come from:** they come from the **subject matter** (the biology of
axolotls, veterinary practice, water chemistry), *not* from keyword co-occurrence.
That is the difference between a semantic model and a word cloud.

**Application:** the health and tank-setup clusters should be re-read along this chain;
a page is complete when the chain for its question is fully expressed (state — cause —
effect — action) somewhere in the corpus, either on-page or through links.

---

## 6. Search intent and the cannibalization shield

**Dominant intent per page.** Label each page with exactly one of:

- informational | definitional | procedural | diagnostic | comparative | transactional
  | navigational | tool/calculator | location-specific | problem-solving

Two pages may target the same *entity* and *attribute* only if their dominant intents
(or semantic roles, §14) differ. Example: `/morphs/morphs-comparison-chart`
(comparative) and `/morphs/leucistic` (definitional) both describe the leucistic morph
but serve different intents — that is *legitimate overlap* (§13), not cannibalization.
Two pages with the same entity+attribute+intent+role are cannibalizing.

**Application:** re-label every page with the 10-value taxonomy (the phase-7 4-bucket
scheme is a coarse input, not the answer).

---

## 7. Contextual vectors (worked inventory)

Each core topic carries a set of concepts that must co-occur for comprehension:

- **Water quality** → temperature, cycling/ammonia, filtration, plants/substrate,
  water-conditioner, feeding leftover food ("uneaten food → ammonia" is an existing
  correct vector).
- **Feeding** → age/size, seasonal temperature (metabolism), live vs. frozen, nutrition,
  impaction/overfeeding, fasting/vacation.
- **Health** → water parameters first, quarantine, treatment protocols (tea bath /
  salt bath / fridging), when to see an exotic vet.
- **Morphs** → pigment cell biology, breeding genetics, price (popularity vector).
- **Legality/buying** → source/breeder quality, shipping stress, acclimation
  (acclimation is the direct bridge from "buying" to "tank").

These vectors are the *link-target list* for each cluster. They are concepts, not
keywords — the anchor and destination must express the concept, whatever phrasing
appears.

---

## 8. The semantic content network (relation types)

Every internal link should be typed. The type budget for this corpus:

1. **parent → child** (hub → spoke)
2. **prerequisite → procedure** (explain the cycle → then how to fix a spike)
3. **cause → effect/symptom** (temperature → floating)
4. **symptom → cause** (curled gills → ammonia)
5. **problem → solution** (fungus → tea bath/salt bath)
6. **general → specific** (morphology → a specific morph)
7. **concept → tool** (nitrogen cycle → tracker)
8. **comparison → alternatives** (sales comparison → each option)
9. **biology → practical application** (neoteny → why behavior differs)

**Not allowed:** links with no typed relation ("related articles" garden-paths,
footer link lines). If a link cannot be typed, it should not exist.

**Application:** the next phase re-types every edge in `linkgraph.json`. This is the
single highest-leverage linking change and it is gated behind this methodology.

---

## 9. Internal linking principles (contextual)

1. **Correct semantics over quantity** — the absolute rule.
2. Hub pages link to their spokes; spokes link *up* to hub + *across* on real
   relations; bridge pages connect clusters with small semantic distance (§1.21).
3. Contextual vectors (§7) drive body links: link *where the concept is discussed*.
4. Authority flows toward the core: keep the densest inbound on core pages
   (water-parameters-cycling, refusing-to-eat, fungal infections already have it).
5. **When NOT to link:** out-of-border nodes, distant-context mentions, duplicate
   target pages, and any link whose anchor can't state the target's meaning.
6. Anchor text: descriptive of the *destination's* meaning; avoid forcing exact-match.

---

## 10. PPR practical scoring (with the required caveat)

Method (operational, site-internal, **approximation — not an official Google/Koray
metric**):

- **Prominence** ≈ graph centrality within our own linkgraph (in-degree weighted by
  core membership + typed-edge strength).
- **Popularity** ≈ evidence of search/usage demand (query observations, FAQ mining,
  page visit signals where available).
- **Relevance** ≈ placement on inside/adjacent/peripheral + claim connection to the
  central entity.

**Uses:**

- Prominent + relevant, low popularity (e.g. water-parameters-cycling) → protect,
  deepen, use as authority hub.
- Popular + relevant, low prominence (e.g. leucistic, Minecraft pages) → promote
  prominence with inbound contextual links.
- Relevant + neither → completeness backlog, build out.
- Popular + not relevant (none should exist) → border enforcement, page pruning/
  repositioning.

Every report that uses PPR numbers must carry the approximation disclaimer verbatim.

---

## 11. Coverage and gaps (conceptual)

A gap is defined as a missing:

- entity (a thing the map says exists),
- attribute (a property never described),
- value/state (a state space half-covered),
- relationship (a real connection never made/bridged),
- intent (a question the node should answer but doesn't),
- contextual bridge (a vector missing between clusters),
- prerequisite knowledge (a base concept assumed but never explained).

A **missing keyword is never, by itself, a gap.** Example: if the corpus fully covers
temperature stress but the phrase "axolotl water too hot" is absent, there is no gap —
but if the diagnosis page never mentions cooling as a *fix*, that *action* value is a
gap.

---

## 12. Semantic cannibalization

Two pages cannibalize when they share **all** of: central entity, attribute,
dominant search intent, and semantic role — i.e. they are trying to be the same node.
Similar-sounding words alone are not cannibalization.

**Examples (current corpus risk):** forced secondary edges like health pages citing
"price/cost" produce *cheap word-boundary overlap* with cost-and-buying (the data
flagged these in phase 7's secondary-signals list). That is a *link* problem
(unjustified edges per §8/§9), and a *relevance* problem (§1.11), not necessarily a
cannibalization problem.

**Legitimate overlap** (do NOT merge): same entity, different intent
(definitional morph page vs. comparative chart), or different location variant
(distinct legal pages), or different role (hub vs. spoke).

---

## 13. Page roles (11 types)

Each page is assigned one primary role; the role drives its content, its links in and
out, and its information priority (§1.17):

1. **Foundational** — the central entity hub (`/axolotls/care-guide`).
2. **Hub** — cluster aggregator (tank-setup, diet, health, …).
3. **Supporting** — narrower detail page under a hub/featured article.
4. **Explanatory** — answers a definition/why question (neoteny, amphibian, gills).
5. **Procedural** — step-by-step how-to (hand feeding, acclimation, tea bath).
6. **Diagnostic** — symptom → cause → fix (refusing to eat, floating, red leg).
7. **Comparative** — option comparison (chillers, filters, live vs. frozen).
8. **Transactional** — buying decisions (where to buy, breeder selection).
9. **Location-specific** — legal pages per state/country (variant intent, separate
   pages are correct here).
10. **Tool** — calculators/trackers/checkers.
11. **Bridge/contextual** — connects two clusters (acclimation links buying→tank;
    pigment-cells links morphs→breeding).

---

## 14. Hard STOP rule for this phase

After this document is delivered, **until the methodology is agreed**:

- No content edits, title/H1/URL changes.
- No articles added or removed.
- No internal links added, moved, or removed.
- No category/hub changes.
- No metadata/schema changes.

The next phase audits the corpus *against this methodology* (coverage scorecard,
link re-typing, intent re-labelling, gap analysis, border scoring) before any change
is proposed.

---

## 15. Self-check (to be answered in the report, per §16 of the brief)

The 14 questions are answered in the accompanying report. They verify that this
methodology was understood and applied, not merely copied:

1. In one sentence: what is a topical map?
2. What is NOT a topical map?
3. What is the difference between a topic and a keyword?
4. What's the difference between topical coverage and keyword coverage?
5. What is a topical border, and why does it matter here?
6. What is a contextual vector? Give one from the corpus.
7. What is a semantic content network? How does it differ from "related articles"?
8. Explain E-A-V with an example from this corpus, extended to
   CAUSE→EFFECT→ACTION.
9. How does search intent drive content architecture?
10. Why are links "semantic relationships," not authority plumbing?
11. How does PPR guide prioritization for AxolotlCare?
12. What counts as a true topical gap? A missing keyword is not one — why?
13. When is same-topic overlap legitimate, and when is it cannibalization?
14. Why is article count alone not topical authority?

---

*End of methodology. Amendments require agreement before they change audit criteria.*