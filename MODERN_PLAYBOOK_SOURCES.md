# MODERN PLAYBOOK SOURCES — Team Resolve
# Master reference for all remaining archetypes (Claude Code handoff)
# Updated: 2026-03-31 | Current meta from MTGDecks.net snapshot
# Reference event: LDXP SEA26 (Mar 27-29 2026)
# 
# STATUS:   BUILT    = playbook complete
#           TESTING  = active testing, reference list identified
#           NEXT     = current build queue, priority order
#
# FORMAT:
#   [★★★] = Deep primer/guide, 3000+ words, highly current, oracle-accurate
#   [★★]  = Solid guide or recent SB/matchup focus, 1000+ words
#   [★]   = Decklists, coverage, or meta context only
#
# ════════════════════════════════════════════════════════════════════════════
# SECTION 0: ALREADY BUILT (for reference / update tracking)
# ════════════════════════════════════════════════════════════════════════════

# Boros Energy    ~16% meta | accent: #DC2626 | BUILT ✅ (Mardu variant under eval)
# Jeskai Blink    ~7%  meta | accent: #7C3AED | BUILT ✅ | TESTING: Connor Mackenzie 9-0-4 list w/ Casey Jones
# Izzet Prowess   ~4%  meta | accent: #EF4444 | BUILT ✅
# Glockulous      ~1.5% meta| accent: #7B1FA2 | BUILT ✅ (Grixis Reanimator)
# UW Control      ~2%  meta | accent: #1E40AF | BUILT ✅ (updated to Evariel 8-0-2 Scepter-Chant, Mar 27 2026)
# Izzet Affinity  ~8%  meta | accent: #2563EB | BUILT ✅

# Currently testing (reference lists from LDXP SEA26, no playbook yet):
# Esper Blink     | robert seder 11-2-2 (rank 3) — https://melee.gg/Decklist/View/103cafd4-e5f3-4015-8d70-b41b008a10d9
# Dimir Midrange  | Roy Yang 10-1-3 (rank 5)     — https://melee.gg/Decklist/View/c5c9869a-7727-4589-aba5-b419009c2148
# Mono-U Belcher  | Tiendav1s 4-0-3 (note: SB Mountain > Island for Charbelcher damage)
#                   https://melee.gg/Decklist/View/fc766c7d-61af-43fa-8735-b41c004b9bd5

# ════════════════════════════════════════════════════════════════════════════
# SECTION 1: BUILD QUEUE — Priority ordered by meta share
# ════════════════════════════════════════════════════════════════════════════
# Instructions for Claude Code:
# For each deck, you MUST:
#   1. Fetch the ★★★ source(s) and read the full text
#   2. Run Scryfall API queries to verify oracle text for all key cards
#   3. Cross-reference against the meta snapshot at j6e.me/mtg-meta-analyzer
#   4. Build full 10-tab HTML playbook matching the structure of existing guides
#   5. Run wrap_cards.py on the completed file
#   6. Run site_audit.py to verify clean state
#   7. Commit and push

# ════════════════════════════════════════════════════════════════════════════
# 1. RUBY STORM — ~6.2% meta | accent: #DC2626
# ════════════════════════════════════════════════════════════════════════════
# Identity: Mono-red linear combo. Ruby Medallion + Ral, Monsoon Mage reduce
# red spells to 1 mana. Chain rituals + draw spells → Past in Flames → 
# Grapeshot for 20+. Fastest theoretical kill: turn 2.
# Reference list: Chance McDougal 9-0-4, LDXP SEA26 10k, Mar 28 2026
#   https://melee.gg/Decklist/View/5b97bdff-bc1f-4e37-8255-b419010af481
#   Key cards: Ral Monsoon Mage x4, Ruby Medallion x4, Artist's Talent x2 (new!)
#   Heroes' Hangout x1, Romantic Rendezvous x1. SB: Orim's Chant x2, Untimely Malfunction x3.
# Key oracle notes: Ruby Medallion does NOT reduce Ral's cost (Ral reduces Ruby's).
# Consign to Memory CAN counter Ruby Medallion (colorless spell MV 2).
# Force of Negation exiles Past in Flames (removing it from the GY entirely).

[★★★] Mystical Teachings — Ruby Storm Primer + SB Guide
URL: https://mystical-teachings.com/storm-primer-and-sideboard-guide/
Notes: Comprehensive heuristics guide, turn-by-turn sequencing, SB against all major
matchups. Focused on Modern-legal build. MUST READ FIRST.

[★★★] The Epic Storm — Deck Guide: Ruby Storm
URL: https://www.theepicstorm.com/deck-guide-ruby-storm/
Notes: Deep dive on fast mana, ritual sequencing, turn-2 kill lines, resilience vs
removal. Excellent on Ral tricks (flip mid-removal, hold priority with Flames).
Strong oracle accuracy on Storm trigger mechanics.

[★★★] MTGDecks — Mastering Ruby Storm in Modern
URL: https://mtgdecks.net/guides/mastering-ruby-storm-in-modern-mtg-269
Notes: Author: -Nausea-. Turn-by-turn combo examples, count management, Wish 
timing rules, Ral ultimate sequencing. Good on Birgi/Strike It Rich interactions.

[★★] Magic.gg Metagame Mentor — Post-Breach Modern Decks (Apr 2025)
URL: https://www.magic.gg/news/metagame-mentor-the-best-post-underworld-breach-modern-decks
Notes: Excellent current 75 decklist (4 Ruby Medallion, 4 Ral, 4 Desperate Ritual,
4 Manamorphose, 4 Pyretic Ritual, 4 Reckless Impulse, 4 Wrenn's Resolve, etc.)
with current SB (Orim's Chant, Prismatic Ending, Grapeshot, Empty the Warrens).

[★] MTGGoldfish — Ruby Storm (1st place Modern Challenge 64, Mar 24 2026)
URL: https://www.mtggoldfish.com/archetype/modern-ruby-storm
Notes: Current Challenge-winning 75 for comparison. Check here for latest list.

# 3 engines: (1) Ruby Medallion discounter chain, (2) Ral flip + ultimate,
# (3) Past in Flames GY rebuy. Sideboard: Orim's Chant hard-locks blue.
# File: ruby-storm-playbook.html

# ════════════════════════════════════════════════════════════════════════════
# 2. ELDRAZI TRON — ~5.5% meta | accent: #7C3AED
# ════════════════════════════════════════════════════════════════════════════
# Identity: Colorless big-mana. Assemble Urza Tron (7 mana T3) + Eldrazi Temple
# (2→4 for Eldrazi). Karn, the Great Creator fetches hate artifacts and shuts
# opponent's mana rocks. Thought-Knot Seer + Reality Smasher + Ugin top-end.
# Key oracle notes: Karn's static = activated abilities of artifacts opponents
# control are blank (Mox Opal, Aether Spellbomb etc.). Damping Sphere stops
# Tron lands (tapped lands produce C instead). Sowing Mycospawn exiles lands.

[★★★] MTGDecks — Mastering Eldrazi Tron (Lucas Giggs, Dec 2025)
URL: https://mtgdecks.net/guides/mastering-eldrazi-tron-in-modern-lucas-giggs-mtg-386
Notes: Author: LucasG1ggs, 5-0 MTGO League results. Pro Tour Edge of Eternities build
(11-5 record, 8-2 Modern). Full matchup guide. Excellent on Karn wish package,
Sowing Mycospawn lines, Ugin's Labyrinth mana efficiency. Post-MH3/EoE current.
Covers: Devourer of Destiny exile zone trick with Karn, land sequencing priority.
MUST READ FIRST.

[★★★] MTGDecks — Eldrazi Tron (LucasGiggs, full guide)
URL: https://mtgdecks.net/guides/modern-eldrazi-tron-guide-mtg-115
Notes: Earlier version of LucasGiggs guide (Oct 2025), good for card choice rationale.
Still relevant for Glaring Fleshraker vs Sowing Mycospawn debate context.

[★★] Ovinize Google Doc Primer (Daniel Staup)
URL: https://docs.google.com/document/d/1mowWYaoTTfC-Ux9b4itbqArbCSBrwnxRkc8LTsG_wvo
Notes: In guides DB. Legacy primer for Karn wish package + land sequencing theory.
May be pre-EoE but foundational oracle accuracy.

[★] MTGDecks — Current Eldrazi Tron decklists (March 2026)
URL: https://mtgdecks.net/Modern/eldrazi-tron
Notes: Aggregate current 75. Recent Challenge top finishes for list comparison.

# Key cards: Karn, the Great Creator + Ensnaring Bridge (SB) is lockout vs aggro.
# Thought-Knot Seer (MV 4, Eldrazi Temple makes it T2 with 1 mana floating).
# All Is Dust — wipes all colored permanents for 7 mana.
# File: eldrazi-tron-playbook.html

# ════════════════════════════════════════════════════════════════════════════
# 3. AMULET TITAN — ~3.1% meta | accent: #059669
# ════════════════════════════════════════════════════════════════════════════
# Identity: Combo-ramp. Amulet of Vigor untaps bounce lands, generating extra
# mana with each land drop. Primeval Titan fetches Slayer's Stronghold + 
# Sunhome, giving haste + double strike for same-turn kill. Highly technical.
# Reference lists (LDXP SEA26):
#   Option A: Devon Straub (PTQ Mar 27)  — https://melee.gg/Decklist/View/3f63eb45-ce53-47fc-b221-b41a010d5291
#     Malevolent Rumble x4, Scapeshift x3, Aftermath Analyst x2, Vexing Bauble x1
#     SB: Insidious Fungus, Dosan the Falling Leaf (lock pieces)
#   Option B: aljce (10k Winner, 13-1-2) — https://melee.gg/Decklist/View/2a4efd5e-3fcd-45d1-86bf-b41a0128ba82
#     Scapeshift x4, Green Sun's Zenith x3, Malevolent Rumble x3, Dryad Arbor x1
#     SB: Fire Magic x3, Force of Vigor x3, Trinisphere x2
#   → Use aljce (winner) as primary reference.
# Key oracle notes: Multiple Amulets stack (each untap trigger resolves separately).
# Amulet + bounce land = effectively ETB untapped + tap for mana immediately.
# Bounce land with 2 Amulets = 4 mana from a single land drop.
# Primeval Titan trigger: put 2 lands from library onto battlefield (can repeat
# on attacks). With Amulet, these ETB untapped.

[★★★] The Titan Bible — Dom Harvey (Google Doc, Jan 2026 update)
URL: https://docs.google.com/document/d/1qOGLSrY00VgTABkKQTF1bP-Prp-49k8l5lux6ESH_mw
Notes: ~32,000 words, 80+ pages. The authoritative Amulet Titan reference.
Updated for "Sunny Ringless" meta (post-One Ring). Essential. Read fully.

[★★★] MTGDecks — Mastering Amulet Titan: Pro Tour SB Guide (CrisMTG77)
URL: https://mtgdecks.net/guides/mastering-amulet-titan-mtg-232
Notes: CrisMTG77 Pro Tour Ghent qualifier. Full matchup + SB guide, key sequencing tips.
Excellent on Cursed Totem vs Yawgmoth, Force of Vigor lines, Spreading Seas play-around.

[★★] MTGDecks — Amulet Titan In-depth & SB Guide
URL: https://mtgdecks.net/guides/amulet-titan-guide-with-sideboard-mtg-27
Notes: Foundational primer on how Amulet creates mana, Titan win conditions, land tutor
lines. Slightly dated but oracle-accurate on core mechanics.

[★] Moxfield Community Primer
URL: https://moxfield.com/decks/olZ-BGSCoEqjJrHDRxSHgQ/primer
Notes: Community-maintained. Good for current 75 and recent updates.

# Win conditions: Slayer's Stronghold (haste) + Sunhome (double strike) + Titan.
# Alternate: Valakut, the Molten Pinnacle (mountain count triggers).
# File: amulet-titan-playbook.html

# ════════════════════════════════════════════════════════════════════════════
# 4. SIMIC NEOFORM — ~2.7% meta | accent: #16A34A
# ════════════════════════════════════════════════════════════════════════════
# Identity: Creature combo. Neoform sacrifices a creature to tutor 1-MV-higher
# creature onto battlefield. Full combo: Allosaurus Shepherd (uncounterable) →
# Neoform → Griselbrand → draw 7 → Nourishing Shoal exile Progenitus = gain 10
# → draw 7 again → find Life/Death combo, Angel's Grace + Laboratory Maniac etc.
# Key oracle notes: Allosaurus Shepherd makes green spells uncounterable.
# Griselbrand: pay 7 life, draw 7 cards (activated ability, not triggered).
# Nourishing Shoal: exile green card from hand = gain life equal to its CMC.

[★★★] Camari Bolger Google Doc — Simic Neoform Primer
URL: In guides DB as "Simic Neoform — Camari Bolger"
Notes: Search guides DB for this. Full primer with Griselbrand lines, hand categories,
mulligan theory, hate card navigation. Best available single source.
FETCH FROM DB BEFORE BUILDING.

[★★★] MTGDecks — Modern Neobrand Combo Deck Tech & SB Guide (Lucas Giggs)
URL: https://mtgdecks.net/guides/mastering-modern-neobrand-combo-deck-tech-mtg-xxx
Notes: Search MTGDecks for "Neobrand" guide. LucasGiggs authored.

[★★] MTGDecks — Neoform decklists (current 2026)
URL: https://mtgdecks.net/Modern/neoform
Notes: Current 75 for oracle verification. Check for Allosaurus Shepherd count.

# ════════════════════════════════════════════════════════════════════════════
# 5. DOMAIN AGGRO — ~2.6% meta | accent: #D97706
# ════════════════════════════════════════════════════════════════════════════
# Identity: 5-color aggro. Leyline of the Guildpact makes all creatures all types,
# enabling Scion of Draco at 2 mana (domain condition met) and Atraxa 
# cheaply. Tribal Flames for 5 damage. Aggressive clock with powerful ETBs.
# Key oracle notes: Scion of Draco MV 6, costs R/G/W/U/B to cast normally.
# With domain 5 and Leyline, all creatures have haste/deathtouch/hexproof/lifelink.
# Leyline of the Guildpact: static effect, makes all your creatures all types.

[★★★] MTGDecks — Multiple Domain Aggro guides (16 in DB)
URL: https://mtgdecks.net/Modern/domain-aggro
Notes: Check guides DB for most recent (2025-2026). Best author: search for
"Domain Zoo" guides on mtgdecks.net. There are 16 guides in guides DB.

[★★] Mystical Teachings — Domain Zoo primer
URL: https://mystical-teachings.com (search for Domain Zoo)
Notes: If available, excellent oracle accuracy and matchup guidance.

[★★] Magic.gg coverage — Domain Zoo at Pro Tours/RCs 2025
URL: https://magic.gg (search Domain Zoo Modern)
Notes: Pro Tour lists provide best reference for current builds.

# ════════════════════════════════════════════════════════════════════════════
# 6. LIVING END — ~2.4% meta | accent: #DC2626
# ════════════════════════════════════════════════════════════════════════════
# Identity: Cascade combo. Cascade spells (Violent Outburst, Ardent Plea at MV 3+)
# chain into Living End (MV 0). Cycle large creatures (Architects of Will, 
# Curator of Mysteries) to fill GY, then Living End wipes and reanimates.
# Key oracle notes: Cascade = when you cast, cascade; cast Violent Outburst = 
# reveal top until MV < 3 (Living End has no mana cost = 0) → cast for free.
# Force of Negation can counter Living End on the stack.

[★★★] Togores Primer — Sultai Living End (Mystical Teachings or Google Doc)
URL: Search guides DB for "Living End — Togores"
Notes: Paywalled but in guides DB. Most comprehensive current guide.
Covers Subtlety + Living End interaction, cascade protection lines.

[★★] MTGDecks — Living End decklists (current 2026)
URL: https://mtgdecks.net/Modern/living-end
Notes: 2727 decks in DB. Use for current 75 and SB structure.

[★★] Mystical Teachings — Living End primer (if available)
URL: https://mystical-teachings.com (search Living End)
Notes: Check for full primer. Excellent on cascade timing, Subtlety vs cascade.

# ════════════════════════════════════════════════════════════════════════════
# 7. DIMIR CONTROL/MIDRANGE — ~2.58% meta | accent: #1E40AF
# ════════════════════════════════════════════════════════════════════════════
# Identity: Reactive midrange. Counterspells + discard + Psychic Frog + Orcish 
# Bowmasters. Black gives Thoughtseize + Fatal Push. Blue gives Counterspell +
# Murktide Regent or Jace, the Perfected Mind. "Dimir Frog" variant wins with
# Psychic Frog growing off discard.
# Key oracle notes: Psychic Frog: whenever you discard, put a +1/+1 counter.
# Flying. "Whenever PF attacks, you may discard a card." Can get huge quickly.

[★★★] MTGDecks — Dimir Midrange decklists (current 2026)
URL: https://mtgdecks.net/Modern/dimir-midrange
Notes: Check for any guide-type articles. Search for "Dimir Control Modern 2026"
on MTGDecks for most recent guide. dylab SCG Houston Regional result is good 75.

[★★] MTGDecks — Modern Dimir Control decklists
URL: https://mtgdecks.net/Modern/dimir-control
Notes: 282 decklists. Backup if Midrange section insufficient.

[★★] Coverage notes — Dimir Frog / Dimir Murktide
URL: Search magic.gg + mtgdecks for "Dimir Frog Modern 2026"
Notes: Psychic Frog variant is newest iteration. Verify current 75 from Challenges.

# Note: This archetype is somewhat fluid (Dimir Control vs Midrange vs Frog).
# Identify current consensus 75 from Challenge results before building.

# ════════════════════════════════════════════════════════════════════════════
# 8. ELDRAZI RAMP — ~2.0% meta | accent: #6B7280
# ════════════════════════════════════════════════════════════════════════════
# Identity: Big colorless ramp (Tron-adjacent but without Urza lands). Uses 
# Ugin's Labyrinth, Eldrazi Temple + Cloudpost/Glimmerpost or pure ramp.
# Threats: Emrakul, the World Anew or Ulamog. More linear than E-Tron.
# Sometimes called "Eldrazi Post" or "Mono-Green Eldrazi Ramp."

[★★★] Giltspire Primer — Eldrazi Ramp (in guides DB)
URL: Search guides DB for "Eldrazi Ramp — Giltspire"
Notes: Full primer in DB. Read before building.

[★★] LucasGiggs MTGDecks Guide
URL: https://mtgdecks.net/guides/ (search Eldrazi Ramp LucasGiggs)
Notes: If guide exists, LucasGiggs has experience with colorless decks.

[★] MTGDecks — Eldrazi Tron (overlapping reference)
URL: https://mtgdecks.net/Modern/eldrazi-tron
Notes: Some overlap with Eldrazi Ramp. Use for 75 comparison.

# ════════════════════════════════════════════════════════════════════════════
# 9. ESPER REANIMATOR — ~1.8% meta | accent: #7C3AED
# ════════════════════════════════════════════════════════════════════════════
# Identity: Goryo's Vengeance reanimation. Reanimate Archon of Cruelty (draw,
# drain, discard, return creature, destroy creature) or Atraxa. Quantum Riddler
# fills GY + provides value. Grief + Ephemerate hand disruption.
# Key oracle notes: Goryo's targets a legendary creature with haste.
# Archon attack trigger: draw a card, opponent discards, you gain 3 life, opponent
# loses 3 life, destroy target nonland permanent, return target creature card from
# any GY. Finality counter = exiled when dies (can't Goryo's again).

[★★★] Esper Goryo's Primer — Google Doc (in guides DB)
URL: https://docs.google.com/document/d/1u8q4Tj-3KvQHY4hxczcB9ZGietUFHThuPdQkZdbRWmo/edit
Notes: In guides DB. Full primer. Best available Esper Reanimator source.

[★★★] MTGDecks — Esper Reanimator guides (10 in DB)
URL: https://mtgdecks.net/Modern/esper-reanimator (or search guides)
Notes: Check for most recent (2025-2026) by reputable author. 267 recent decklists.

[★★] BW Balemurk Primer — meanfannypack (Google Doc)
URL: https://docs.google.com/document/d/1GIfA_SmUrUwrA14zUuG_AuqfLTswEm3ocmjv62ec07U/edit?tab=t.0
Notes: In guides DB. Relevant for Overlord of the Balemurk + Grief lines.

# ════════════════════════════════════════════════════════════════════════════
# 10. ESPER BLINK — ~1.8% meta | accent: #F59E0B
# ════════════════════════════════════════════════════════════════════════════
# Identity: Value blink. Phelia + Ephemerate + Solitude (evoke blink) + Quantum
# Riddler (draw 2 on ETB). Flickerwisp recurs value. Teferi, Time Raveler locks
# opponent's instant-speed interaction during your combo turns. 
# Very similar to Jeskai Blink but cuts red for more black access (Thoughtseize,
# Overlord of the Balemurk instead of Consign to Memory or Voice of Victory).
# Key oracle notes: Same as Jeskai Blink for Phelia/Solitude interactions.

[★★★] Laplasjan — Mystical Teachings Esper Blink Primer
URL: https://mystical-teachings.com (search Esper Blink)
Notes: In guides DB as "Esper Blink — Laplasjan". Most comprehensive guide available.
Read fully before building. Focus on Riddler/Phelia synergy.

[★★] MTGDecks — Esper Blink / Orzhov Blink guides
URL: https://mtgdecks.net/guides/ (search Orzhov Blink, Esper Blink)
Notes: Several guides in DB. "Mastering Orzhov Blink" by LucasGiggs relevant.

[★] Magic.gg — Orzhov Blink Post-Breach Meta article
URL: https://www.magic.gg/news/metagame-mentor-the-best-post-underworld-breach-modern-decks
Notes: Full decklist + description. Good for current 75 baseline.

# Note: If Orzhov Blink and Esper Blink are distinct archetypes in current meta,
# build both or combine with clear differentiation section in Overview tab.

# ════════════════════════════════════════════════════════════════════════════
# 11. BOROS AGGRO — ~1.6% meta | accent: #F97316
# ════════════════════════════════════════════════════════════════════════════
# Identity: Aggro (non-Energy). Monastery Swiftspear, Goblin Guide, Eidolon of
# the Great Revel, Lightning Bolt, Shard Volley. Burn-heavy. Similar to Legacy
# Burn. Distinct from Boros Energy (no Guide of Souls / Ocelot Pride package).
# Also known as "Boros Burn" or "RW Burn."

[★★★] MTGDecks — Boros Aggro guides (16 in DB)
URL: https://mtgdecks.net/guides/ (search Boros Burn, Boros Aggro Modern)
Notes: Find most recent 2025-2026 guide. Multiple authors in DB.

[★★] Mystical Teachings — Burn Modern primer (if available)
URL: https://mystical-teachings.com (search Burn Modern)
Notes: Check for primer. Excellent matchup detail when available.

[★] MTGDecks — Boros Aggro decklists
URL: https://mtgdecks.net/Modern/boros-aggro (or search Boros Burn)
Notes: Current 75 reference. Note: Boros Aggro ≠ Boros Energy.

# ════════════════════════════════════════════════════════════════════════════
# 12. GOLGARI YAWGMOTH — ~2.02% meta | accent: #4B5563
# ════════════════════════════════════════════════════════════════════════════
# Identity: Creature combo-midrange. Yawgmoth, Thran Physician as engine:
# sacrifice undying creatures (Young Wolf, Geralf's Messenger) → draw cards +
# put -1/-1 counter → undying creature comes back → repeat ad infinitum.
# Win: Zulaport Cutthroat / Blood Artist drain OR Geralf's Messenger.
# Tutors: Eldritch Evolution, Chord of Calling.
# Key oracle notes: Undying = when creature dies without +1/+1 counter, return
# with +1/+1 counter. Yawgmoth: pay 1 life, sacrifice creature, target creature
# gets -1/-1 until EOT, draw card. The "engine" generates draw + -1/-1 counters
# to blank the undying counter, allowing repeat triggers.

[★★★] Reid Duke — Modern Golgari Yawgmoth Deep Dive (ChannelFireball)
URL: https://strategy.channelfireball.com/cfb-pro-content/modern-golgari-yawgmoth-combo-deep-dive/
Notes: Hall of Famer Reid Duke's deep dive. 12th place MTG Vegas Modern (1400 players).
Covers combo lines, resilience, tutors, matchup theory. May need CFB subscription.

[★★★] Reid Duke — Modern Yawgmoth Deck Guide Update (ChannelFireball)
URL: https://strategy.channelfireball.com/cfb-pro-content/modern-yawgmoth-combo-deck-guide-update/
Notes: Updated guide. Focus on undying combo sequence, key matchup decisions.
May need CFB subscription — paraphrase content for guide.

[★★] MTGDecks — Golgari Yawgmoth guides + decklists
URL: https://mtgdecks.net/Modern/golgari-yawgmoth
Notes: Current 75 for comparison. Check for any 2025-2026 MTGDecks guides.

# Key cards to verify: Yawgmoth, Thran Physician / Young Wolf / Geralf's Messenger
# / Melira, Sylvok Outcast (stops -1/-1 counters on your creatures) / Blood Artist.
# File: golgari-yawgmoth-playbook.html

# ════════════════════════════════════════════════════════════════════════════
# 13. TAMESHI BELCHER — ~2.03% meta | accent: #0EA5E9
# ════════════════════════════════════════════════════════════════════════════
# Identity: Mono-blue artifact combo. Goblin Charbelcher activated ability deals
# damage equal to cards until next land. Tameshi, Reality Architect bounces a 
# land to return Lotus Bloom from GY → reuse Bloom for 3 mana. 
# With Tameshi + suspended Bloom: untap turn 4 = 3 mana, return to bounce land,
# Bloom goes back to hand/GY, repeat. 12 mana available on turn 4 setup.
# Key oracle notes: Lotus Bloom: suspend 3, {T}: add 3 mana of one color.
# Tameshi: {W/U}: return target noncreature permanent with MV ≤ Tameshi's power
# from GY to hand. Pay 1 land return cost. Tameshi draws when opponent returns
# a noncreature permanent to hand.

[★★★] MTGDecks — Mastering Mono-Blue Belcher: Ultimate Guide (Alejandro Mora)
URL: https://mtgdecks.net/guides/mastering-mono-blue-belcher-ultimate-guide-mtg-382
Notes: Author: Ale_Mtg. Top 4 MTGO Challenge 64. Three Challenge Top 4s + MOCS/PT
qualification. Excellent on Tameshi mana counting, Disrupting Shoal timing,
Thundertrap sequencing. Full matchup guide. MUST READ FIRST.

[★★] DaVinciMtg — Tameshi Belcher SB Guide
URL: Search guides DB for "Tameshi Belcher — DaVinciMtg"
Notes: In guides DB. Focused SB guide. Good supplemental source.

[★] MTGDecks — Tameshi Belcher decklists (current 2026)
URL: https://mtgdecks.net/Modern/tameshi-belcher
Notes: 3597 decklists. Current 75 reference. 2.03% meta share.

# Key quick-count trick (from Ale_Mtg): Tameshi + Bloom mana = -1 + 3 = +2 per
# bounce activation. With 4 land drops and 1 Bloom: 2*4 = 8 mana available.
# File: tameshi-belcher-playbook.html

# ════════════════════════════════════════════════════════════════════════════
# 14. SIMIC RITUAL — ~1.83% meta | accent: #10B981
# ════════════════════════════════════════════════════════════════════════════
# Identity: Green-blue ritual combo. Uses Utopia Sprawl + Arbor Elf for explosive
# mana early, then chains into large payoffs (Emrakul, Scapeshift, or similar).
# Sometimes called "G/U Combo" or "Simic Ritual Ramp."

[★★] MTGDecks — Simic Ritual guides (3 in DB)
URL: https://mtgdecks.net/ (search Simic Ritual Modern guides)
Notes: 3 guides in DB from previous research. Fetch and read before building.

[★] MTGDecks — Simic Ritual decklists
URL: https://mtgdecks.net/Modern/simic-ritual (or closest archetype name)
Notes: Current 75 for list baseline. 1.83% meta share.

# ════════════════════════════════════════════════════════════════════════════
# 15. DIMIR FROG / DIMIR CONTROL (alternate) — ~1.44-2.58% meta | accent: #6366F1
# ════════════════════════════════════════════════════════════════════════════
# Identity: Blue-black control/midrange. Psychic Frog (Tidal Terror / The Gitrog,
# Horror of Zhava) as threat. Counterspells + Thoughtseize + Fatal Push. 
# Modern "UB Death's Shadow" adjacent but focused on Psychic Frog as primary threat.
# If Dimir Frog and Dimir Control have merged in current meta, build unified guide.

[★★] MTGDecks — Dimir Frog / Dimir Control decklists
URL: https://mtgdecks.net/Modern/dimir-frog (or dimir-control)
Notes: 1.44% (Frog) + 2.58% (Control). May be same archetype. Check current lists.

[★] MTGDecks — Recent Dimir Modern results
URL: https://mtgdecks.net/Modern
Notes: Check meta snapshot for exact archetype names and current split.

# ════════════════════════════════════════════════════════════════════════════
# SECTION 2: CRITICAL ORACLE FACTS BY DECK (for Claude Code verification)
# ════════════════════════════════════════════════════════════════════════════
# For EVERY card, run: GET https://api.scryfall.com/cards/named?fuzzy=CARDNAME
# Extract: oracle_text, mana_cost, type_line, power, toughness
# Never assume — always verify.

## IZZET AFFINITY (reference — already built)
# Pinnacle Emissary: {1}{U}{R} 3/3 — triggers on CAST of artifact spell (not ETB)
# Kappa Cannoneer: {5}{U} 4/4 Improvise — Ward 4 = TAX not immunity
# Weapons Manufacturing: triggers on NONtoken artifacts only
# EE at X=0: destroys all MV=0 permanents INCLUDING your own (Drones, Mox Opal)
# Grafdigger's Cage: DOES block Emry (stops casting from GY) — don't play in mirror
# Consign to Memory: can counter colorless spells (Ruby Medallion, EE's ability)
# Sink into Stupor: bounces ANY spell OR nonland permanent (versatile 2-for-1)
# Skateboard: {1}, ETB taps target permanent + equipped creature haste + equip 1

## RUBY STORM
# Ruby Medallion: reduces cost of RED spells by 1 (does NOT reduce Ral's cost)
# Ral, Monsoon Mage: flips when you win 6+ coin flips; ultimate = "cast instants/
#   sorceries for free this turn"
# Ral reduces Ruby's mana cost (so Ral + Ruby = Rituals cost {0}R in practice)
# Past in Flames: flashback = R. All instants/sorceries in GY gain flashback EOT.
# Grapeshot: storm. If held priority with Flames on stack, can cast instants first.
# Force of Negation: exiles Past in Flames (removes from game, can't flashback).
# Wish: cast a card from outside the game. Sideboard card. Not required to cast imm.
# Damping Sphere (vs Storm): each spell cast costs +1 more per previous spell this turn.

## ELDRAZI TRON
# Karn, the Great Creator: static = activated abilities of artifacts OPPONENTS control
#   are blank (your Mox Opal still works under Karn). Also: exile a card from outside
#   the game = tutor from SB.
# Thought-Knot Seer: {3}{C} (Eldrazi Temple + 1 mana = T2). ETB exile a card from
#   hand. When leaves, opponent draws a card.
# Ugin's Labyrinth: can exile a colorless MV 7+ card to untap as it enters.
# Sowing Mycospawn: {3}{G}, search for up to 2 lands AND exile target opponent's land.
# All Is Dust: {7}, tribal Sorcery Eldrazi — each player sacrifices all colored perms.
# Reality Smasher: {4}{C} 5/5 trample haste. "Whenever ~ is targeted by a spell an
#   opponent controls, counter it unless that player discards a card."

## AMULET TITAN
# Amulet of Vigor: triggered ability (not replacement effect). Multiple Amulets = 
#   multiple separate untap triggers per ETB. With 2 Amulets + bounce land = 4 mana.
# Primeval Titan: attack trigger = search for up to 2 lands, ETB untapped (with Amulet).
# Slayer's Stronghold: {R/W}: target creature gains haste + +2/+0 until EOT.
# Sunhome: {3}{R/W}: target creature gains double strike until EOT.
# Dryad of the Ilysian Groves: your lands are ALL basic land types (enables Valakut).
# Arboreal Grazer: put a land from hand onto battlefield tapped (triggers Amulet).

## GOLGARI YAWGMOTH
# Yawgmoth, Thran Physician: {3}{B}, Human Wizard. Cannot be sacrificed itself.
#   "{B}, Pay 1 life, sacrifice another creature: Put a -1/-1 counter on up to 1
#   target creature, then draw a card."
# Undying: when dies with no +1/+1 counter, returns with +1/+1 counter.
# Young Wolf: {G} 1/1 Undying.
# Geralf's Messenger: {B}{B}{B} 3/2 Undying — ETB opponent loses 2 life. Enters tapped.
# Blood Artist: when ANY creature dies, target player loses 1 life, you gain 1.
# Melira, Sylvok Outcast: creatures you control can't have -1/-1 counters placed.
#   (Breaks the Yawgmoth engine for your own creatures — but enables infinite loop with
#   Geralf's Messenger + undying: Messenger can never "fill" its counter slot.)
# Eldritch Evolution: sacrifice creature, find creature with MV exactly 2 higher.

## TAMESHI BELCHER
# Tameshi, Reality Architect: {W}{U} 2/3. Whenever opponent returns noncreature perm
#   to hand = draw. {W/U}, Return a land you control to hand: return target noncreature
#   perm with MV ≤ Tameshi's power from GY to hand.
# Lotus Bloom: Suspend 3—{0}. When suspending ends, {T}: Add {W}{W}{W} or {U}{U}{U}
#   or {R}{R}{R} or {G}{G}{G} or {B}{B}{B}.
# Goblin Charbelcher: {4}. {3}{T}: Reveal library until land card revealed. Deal 
#   damage = number of cards revealed. Put land on bottom, rest on top.
# Quick mana count: Tameshi + Bloom = -1 (land return cost) + 3 (Bloom tap) = +2 net.
# With 4 land drops + 1 Bloom in GY: 4 * 2 = 8 extra mana available.

# ════════════════════════════════════════════════════════════════════════════
# SECTION 3: BUILD WORKFLOW CHECKLIST (copy for each deck)
# ════════════════════════════════════════════════════════════════════════════

# [ ] 1. Fetch ★★★ source(s) from URL, read full text
# [ ] 2. Check guides DB: python check_guides_db.py (or similar query)
# [ ] 3. Pull current 75 from MTGDecks archetype page (most recent Challenge top 8)
# [ ] 4. Verify oracle text via Scryfall API for all non-trivial cards
# [ ] 5. Check j6e.me/mtg-meta-analyzer for current meta position + win rates
# [ ] 6. Write 10-tab HTML playbook (same structure as existing guides):
#         ch01: Overview → ch02: Decklist → ch03: Game Flow → ch04: Engines
#         ch05: Roles → ch06: Matchups (11 deep dives) → ch07: Sideboard
#         ch08: Heuristics (16+) → ch09: Tuning → ch10: Prep Sheet
# [ ] 7. python wrap_cards.py FILENAME.html
# [ ] 8. python site_audit.py
# [ ] 9. Add to deck-guides.html navigation
# [10] git add . && git commit -m "Add DECKNAME playbook" && git push

# ════════════════════════════════════════════════════════════════════════════
# END OF SOURCES FILE
# ════════════════════════════════════════════════════════════════════════════
