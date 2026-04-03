# TEAM RESOLVE — MTG PALETTE ASSIGNMENT GUIDE
# Maps each color combination + archetype to a specific UI UX Pro Max row
# Source: E:\vscode ai project\claude-skills\ui-ux-pro-max-skill\cli\assets\data\colors.csv
# Format: Row | Name | Accent | Background | Rationale
#
# USAGE: Find your color combo, find your archetype, use that row.
# Copy --accent and --background into the playbook's CSS :root vars.
# Dark theme = Background darker than #1F1F1F. Light theme = Background lighter than #EFEFEF.
#
# CURRENTLY ASSIGNED (from existing playbooks — do not reassign):
#   Goryo's Vengeance (Esper Reanimator/Combo) → Row 77 Theater/Cinema | #CA8A04 | #0F0F23
#   UW Control                                 → Row 66 News/Media     | #1E40AF | #FEF2F2 (check footer)
#   Izzet Affinity                             → Row  1 SaaS General   | #EA580C | #F8FAFC (check footer)


# ════════════════════════════════════════════════════════════════
# MONO-WHITE (W)
# Feel: Order, law, community, light. Clean whites, gold authority.
# ════════════════════════════════════════════════════════════════

# Aggro (Soldiers, Tokens, White Weenie)
W-AGGRO     → Row 75  | Sports Team/Club        | #DC2626  | #FEF2F2  | Championship red + gold on cream — combat, formation, victory

# Control (Prison, Enchantress, Draw-Go)
W-CONTROL   → Row 13  | Government/Public Svc   | #0369A1  | #F8FAFC  | Institutional authority — high contrast navy + blue, law + order

# Midrange (Death & Taxes, Hatebears)
W-MIDRANGE  → Row 40  | Legal Services          | #B45309  | #F8FAFC  | Trust gold on clean white — authority without aggression

# Combo (Heliod, Enchantment Storm)
W-COMBO     → Row 29  | Micro-Credentials       | #A16207  | #F0F9FF  | Achievement gold + sky blue — divine ascension


# ════════════════════════════════════════════════════════════════
# MONO-BLUE (U)
# Feel: Intellect, control, sea, knowledge. Cool blues and cyans.
# ════════════════════════════════════════════════════════════════

# Aggro/Tempo (Merfolk, Faeries, Delver)
U-TEMPO     → Row 60  | Dental Practice         | #0EA5E9  | #F0F9FF  | Fresh sky blue on crisp white — precise, fast, clean

# Control (Draw-Go, Tron splash, Lock)
U-CONTROL   → Row  5  | B2B Service             | #0369A1  | #F8FAFC  | Professional navy + blue — authoritative, institutional, cold

# Combo (Storm, Paradox Engine, Cheerios)
U-COMBO     → Row 83  | Space Tech/Aerospace    | #3B82F6  | #0B0B10  | Launch blue on near-black — explosive, technical, void-dark


# ════════════════════════════════════════════════════════════════
# MONO-BLACK (B)
# Feel: Power, death, ambition, wealth. Darks with gold or crimson.
# ════════════════════════════════════════════════════════════════

# Aggro (Zombies, Mono-B Aggro, Devotion)
B-AGGRO     → Row 87  | Autonomous Drone Fleet  | #FF3333  | #0D1117  | Alert red on terminal dark — relentless, unstoppable

# Control (8-Rack, Discard, Smallpox)
B-CONTROL   → Row 53  | Photography Studio      | #F8FAFC  | #000000  | Pure black + white contrast — surgical, absolute

# Combo (Reanimator, Breach, Necro)
B-COMBO     → Row 77  | Theater/Cinema          | #CA8A04  | #0F0F23  | Spotlight gold on dramatic dark — reserved for Esper builds too

# Midrange (Rack, Rock, BX Midrange)
B-MIDRANGE  → Row  6  | Financial Dashboard     | #22C55E  | #020617  | Dark bg + green indicators — profit in the shadows


# ════════════════════════════════════════════════════════════════
# MONO-RED (R)
# Feel: Chaos, fire, speed, impulse. Hot reds, oranges, pure aggression.
# ════════════════════════════════════════════════════════════════

# Aggro (Burn, Sligh, Goblins)
R-AGGRO     → Row 80  | Cybersecurity Platform  | #FF3333  | #000000  | Maximum alert red on black — pure burn, no filter

# Combo (Storm, Goblin Storm, Grinding)
R-COMBO     → Row 27  | Podcast Platform        | #F97316  | #0F0F23  | Warm fire orange on dark audio — explosive, fast, hot

# Midrange (Blood Moon, Ponza, Rabble)
R-MIDRANGE  → Row 34  | Restaurant/Food Svc     | #A16207  | #FEF2F2  | Warm gold on red-tinted cream — earthy red power


# ════════════════════════════════════════════════════════════════
# MONO-GREEN (G)
# Feel: Nature, growth, power, creatures. Deep greens, forest earth.
# ════════════════════════════════════════════════════════════════

# Aggro (Stompy, Elves, Devotion)
G-AGGRO     → Row 35  | Fitness/Gym App         | #22C55E  | #1F2937  | Powerful green on dark gray — physical dominance, raw strength

# Combo (Amulet Titan, Pod, CoCo)
G-COMBO     → Row 25  | EV/Charging Ecosystem   | #16A34A  | #ECFEFF  | Electric green on light cyan — system firing on all cylinders

# Ramp/Control (Tron, Eldrazi Green)
G-RAMP      → Row 90  | Sustainable Energy      | #059669  | #ECFDF5  | Deep green on natural light — long game, resource dominance


# ════════════════════════════════════════════════════════════════
# ALLIED COLOR PAIRS
# ════════════════════════════════════════════════════════════════

# ── AZORIUS (WU) — Law + Knowledge. Clean, precise, institutional. ──
WU-CONTROL  → Row 30  | Knowledge Base/Docs     | #2563EB  | #F8FAFC  | Link blue on neutral grey — the draw-go deck's home
WU-TEMPO    → Row 60  | Dental Practice         | #0EA5E9  | #F0F9FF  | Crisp sky blue — Blink, Spirits, precise interaction
WU-COMBO    → Row 29  | Micro-Credentials       | #A16207  | #F0F9FF  | Achievement gold on sky — Scepter-Chant, lock pieces

# ── DIMIR (UB) — Knowledge + Death. Shadow, deception, disruption. ──
UB-MIDRANGE → Row148  | Anonymous Community     | #0891B2  | #0F172A  | Protective teal on deep dark — secretive, disruptive
UB-CONTROL  → Row 96  | Ride Hailing/Transport  | #2563EB  | #0F172A  | Map dark + route blue — precision control, dark field
UB-COMBO    → Row 14  | Fintech/Crypto          | #8B5CF6  | #0F172A  | Purple tech on dark — shadowy engine, graveyard combo

# ── RAKDOS (BR) — Death + Chaos. Brutal, theatrical, sacrifice. ──
BR-AGGRO    → Row 46  | Video Streaming/OTT     | #E11D48  | #000000  | Cinema dark + crimson play — theatrical violence
BR-MIDRANGE → Row 64  | Brewery/Winery          | #A16207  | #FEF2F2  | Craft gold on deep burgundy bg — Jund-adjacent, rich and dark
BR-SACRIFICE→ Row 87  | Autonomous Drone        | #FF3333  | #0D1117  | Relentless red on void — sacrifice triggers, unstoppable

# ── GRUUL (RG) — Chaos + Nature. Savage, earthy, fast. ──
RG-AGGRO    → Row  3  | E-commerce              | #EA580C  | #ECFDF5  | Urgency orange on green-tinted bg — smash face, trample over
RG-MIDRANGE → Row 50  | Agriculture/Farm Tech   | #A16207  | #F0FDF4  | Earth gold on natural green — land creatures, big things
RG-COMBO    → Row 16  | Productivity Tool       | #EA580C  | #F0FDFA  | Orange action on teal bg — mana acceleration, go-off

# ── SELESNYA (GW) — Nature + Order. Community, tokens, wide boards. ──
GW-TOKENS   → Row 56  | Childcare/Daycare       | #16A34A  | #FDF2F8  | Safe green on soft pink — wide boards, populate, grow
GW-MIDRANGE → Row 50  | Agriculture/Farm Tech   | #A16207  | #F0FDF4  | Harvest gold on natural green — value creatures, resilient
GW-COMBO    → Row 41  | Insurance Platform      | #16A34A  | #F0F9FF  | Protected green on trust blue — CoCo/Company, reliable engine


# ════════════════════════════════════════════════════════════════
# ENEMY COLOR PAIRS
# ════════════════════════════════════════════════════════════════

# ── ORZHOV (WB) — Law + Death. Aristocrats, taxation, wealth. ──
WB-AGGRO    → Row  4  | E-commerce Luxury       | #A16207  | #FAFAF9  | Premium gold on near-black — aristocrat aggression, sacrifice
WB-MIDRANGE → Row 33  | Luxury/Premium Brand    | #A16207  | #FAFAF9  | Black + gold — patient, wealthy, grindy
WB-CONTROL  → Row 42  | Banking/Finance         | #A16207  | #F8FAFC  | Authority gold on white — extraction, taxation

# ── IZZET (UR) — Knowledge + Chaos. Experiments, spells, cantrips. ──
UR-AGGRO    → Row  9  | Educational App         | #EA580C  | #EEF2FF  | Electric indigo bg + orange CTA — Prowess, fast spell triggers
UR-MIDRANGE → Row  7  | Analytics Dashboard     | #D97706  | #F8FAFC  | Blue data + amber highlights — Affinity, artifact synergy
UR-COMBO    → Row 83  | Space Tech/Aerospace    | #3B82F6  | #0B0B10  | Launch blue on near-void — Storm, Breach, explosion dark

# ── GOLGARI (BG) — Death + Nature. Recursion, sacrifice, graveyard. ──
BG-MIDRANGE → Row 81  | Developer Tool/IDE      | #22C55E  | #0F172A  | Code green on dark — efficient engine, GY recursion
BG-SACRIFICE→ Row 79  | Coding Bootcamp         | #22C55E  | #020617  | Terminal dark + success green — Yawgmoth loop, sacrifice combo
BG-CONTROL  → Row 91  | Personal Finance        | #059669  | #0F172A  | Dark resourceful blue-black + profit green — Rock, BG Depths

# ── BOROS (RW) — Chaos + Law. Combat, military, burn + removal. ──
RW-AGGRO    → Row 75  | Sports Team/Club        | #DC2626  | #FEF2F2  | Championship red + gold on cream — speed, teamwork, combat
RW-MIDRANGE → Row  7  | Analytics Dashboard     | #D97706  | #F8FAFC  | Amber energy on white — Boros Energy, mid-combat triggers
RW-COMBO    → Row 34  | Restaurant/Food Svc     | #A16207  | #FEF2F2  | Warm gold on red — combo-burn, sustained pressure

# ── SIMIC (GU) — Nature + Knowledge. Adaptation, evolution, tempo. ──
GU-TEMPO    → Row 25  | EV/Charging Ecosystem   | #16A34A  | #ECFEFF  | Electric green + cyan — fast adaptation, efficient clock
GU-COMBO    → Row  2  | Micro SaaS              | #059669  | #F5F3FF  | Evolving indigo bg + emerald — Neoform, Pod, evolve engine
GU-CONTROL  → Row  8  | Healthcare App          | #059669  | #ECFEFF  | Calm cyan + health green — Growth Spiral, draw-grow


# ════════════════════════════════════════════════════════════════
# THREE-COLOR (SHARDS + WEDGES)
# ════════════════════════════════════════════════════════════════

# ── ESPER (WUB) — Order + Knowledge + Death. Elegant, authoritative, artifact. ──
WUB-CONTROL  → Row 40  | Legal Services         | #B45309  | #F8FAFC  | Authority gold on white — Scepter, Chalice, soft lock
WUB-MIDRANGE → Row 38  | Hotel/Hospitality      | #A16207  | #F8FAFC  | Gold service on white — value, planeswalkers, artifacts
WUB-REANIMATOR→Row 77  | Theater/Cinema         | #CA8A04  | #0F0F23  | Spotlight gold on dark — dramatic reanimation (Goryo's = this)

# ── GRIXIS (UBR) — Knowledge + Death + Chaos. Shadow, brutality, precision. ──
UBR-CONTROL  → Row142  | Sleep Tracker          | #7C3AED  | #0F172A  | Deep indigo on dark — death's shadow, long game oppression
UBR-MIDRANGE → Row 96  | Ride Hailing           | #2563EB  | #0F172A  | Dark precision blue — Grixis Shadow, tempo-midrange
UBR-COMBO    → Row 14  | Fintech/Crypto         | #8B5CF6  | #0F172A  | Purple tech dark — Grixis Living End, breach combo

# ── JUND (BRG) — Death + Chaos + Nature. The quintessential midrange. Discard + removal. ──
BRG-MIDRANGE → Row122  | Card & Board Game      | #D97706  | #0F172A  | Felt-green dark + amber — the grind, value, card advantage
BRG-AGGRO    → Row 35  | Fitness/Gym App        | #22C55E  | #1F2937  | Savage dark + power green — Jund aggressive variant

# ── NAYA (RGW) — Chaos + Nature + Order. Big creatures, wide boards. ──
RGW-AGGRO    → Row 37  | Travel/Tourism         | #EA580C  | #F0F9FF  | Adventure orange on sky — Naya Zoo, creature beatdown
RGW-MIDRANGE → Row 50  | Agriculture/Farm Tech  | #A16207  | #F0FDF4  | Earth gold on natural green — CoCo, value creatures, resilient

# ── BANT (GWU) — Nature + Order + Knowledge. Noble, trustworthy, efficient. ──
GWU-MIDRANGE → Row 36  | Real Estate/Property   | #0369A1  | #F0FDFA  | Trust teal-blue on clean bg — Bant CoCo, fair value
GWU-CONTROL  → Row 30  | Knowledge Base         | #2563EB  | #F8FAFC  | Link blue on neutral — Bant Control, counters + removal
GWU-BLINK    → Row 41  | Insurance Platform     | #16A34A  | #F0F9FF  | Protected green on sky blue — Blink, ETB value

# ── ABZAN (WBG) — Order + Death + Nature. Patient, resilient, value. ──
WBG-MIDRANGE → Row 33  | Luxury/Premium Brand   | #A16207  | #FAFAF9  | Black + gold premium — classic Abzan, patient inevitability
WBG-COMBO    → Row  4  | E-commerce Luxury      | #A16207  | #FAFAF9  | Dark premium gold — Abzan Company, Melira pod

# ── JESKAI (URW) — Knowledge + Chaos + Order. Tempo, spells, precision. ──
URW-TEMPO    → Row 54  | Coworking Space        | #2563EB  | #FFFBEB  | Energetic amber bg + booking blue — Jeskai Tempo, Monastery
URW-CONTROL  → Row  7  | Analytics Dashboard    | #D97706  | #F8FAFC  | Blue data + amber highlights — Jeskai Control, draw-go
URW-MIDRANGE → Row 37  | Travel/Tourism         | #EA580C  | #F0F9FF  | Adventure orange on sky — Jeskai Fires, Blink value

# ── SULTAI (BGU) — Death + Nature + Knowledge. Resourceful, opulent, grindy. ──
BGU-MIDRANGE → Row 91  | Personal Finance       | #059669  | #0F172A  | Dark blue-black + profit green — Sultai Midrange, BUG Rock
BGU-CONTROL  → Row  6  | Financial Dashboard    | #22C55E  | #020617  | Very dark + green growth — draw-fill-win, Leovold, grind
BGU-COMBO    → Row 14  | Fintech/Crypto         | #8B5CF6  | #0F172A  | Purple dark tech — Sultai Reanimator, cascade, broken stuff

# ── MARDU (RWB) — Chaos + Order + Death. War, violence, conquest. ──
RWB-AGGRO    → Row 75  | Sports Team/Club       | #DC2626  | #FEF2F2  | Championship red on cream — Mardu Warriors, fast combat
RWB-MIDRANGE → Row 64  | Brewery/Winery         | #A16207  | #FEF2F2  | Craft gold on burgundy — Mardu Pyromancer, removal pile
RWB-COMBO    → Row 66  | News/Media Platform    | #1E40AF  | #FEF2F2  | Breaking red bg + authority blue — Mardu Shadow, disrupt+win

# ── TEMUR (GUR) — Nature + Knowledge + Chaos. Elemental, big spells, ramp. ──
GUR-MIDRANGE → Row 16  | Productivity Tool      | #EA580C  | #F0FDFA  | Teal bg + action orange — Temur Cascade, elemental energy
GUR-COMBO    → Row 25  | EV/Charging Ecosystem  | #16A34A  | #ECFEFF  | Electric green on cyan — Temur Rhinos, cascade engine
GUR-TEMPO    → Row  2  | Micro SaaS             | #059669  | #F5F3FF  | Evolving indigo bg + emerald — Temur Tempo, efficient threats


# ════════════════════════════════════════════════════════════════
# FOUR-COLOR
# ════════════════════════════════════════════════════════════════

# WUBR (No Green) — Artifact, control, aggression
WUBR         → Row 32  | Beauty/Spa/Wellness    | #8B5CF6  | #FDF2F8  | Lavender luxury — complex, layered, non-green power

# UBRG (No White) — Dark value engine
UBRG         → Row 14  | Fintech/Crypto         | #8B5CF6  | #0F172A  | Deep purple dark — all resources except law

# BRGW (No Blue) — Aggressive value
BRGW         → Row 50  | Agriculture/Farm Tech  | #A16207  | #F0FDF4  | Earth gold on nature — land + creatures + removal + burn

# RGWU (No Black) — Pure value + tempo
RGWU         → Row 43  | Online Course          | #EA580C  | #F0FDFA  | Growth teal + achievement orange — progress, all colors learning

# GWUB (No Red) — Grind + control + value
GWUB         → Row 40  | Legal Services         | #B45309  | #F8FAFC  | Trust gold on authority white — law + growth + knowledge + death

# Generic 4-color (unknown or flexible)
4C-GENERIC   → Row  9  | Educational App        | #EA580C  | #EEF2FF  | Indigo depth + orange energy — complex system


# ════════════════════════════════════════════════════════════════
# FIVE-COLOR / DOMAIN
# ════════════════════════════════════════════════════════════════

# Domain / 5-color Aggro (Domain Zoo, Tribal Flames)
5C-AGGRO     → Row  3  | E-commerce             | #EA580C  | #ECFDF5  | Every basic land type — green + orange, full domain

# 5-color Control / Good Stuff
5C-CONTROL   → Row 85  | Quantum Computing      | #FF00FF  | #050510  | Full spectrum interference — everything at once, multidimensional

# 5-color Combo (Omniscience, Bring to Light)
5C-COMBO     → Row 19  | NFT/Web3 Platform      | #FBBF24  | #0F0F23  | Gold value on darkest dark — every card type, maximum power


# ════════════════════════════════════════════════════════════════
# COLORLESS / ARTIFACT / ELDRAZI
# ════════════════════════════════════════════════════════════════

# Eldrazi (Colorless Eldrazi, Eldrazi Tron)
COLORLESS-ELDRAZI → Row 5 | B2B Service        | #0369A1  | #F8FAFC  | Slate/grey authority — ancient, cold, annihilator
# NOTE: Eldrazi Tron already uses #475569 slate — Row 5 primary is close

# Eldrazi Tron specifically
ELDRAZI-TRON → Row  5  | B2B Service           | #475569  | #F8FAFC  | Slate grey on white — temple, waste, colorless power
# (manually override --accent to #475569 since Row 5 uses #0369A1)

# Artifact Aggro (Affinity, Hardened Scales)
ARTIFACT     → Row  1  | SaaS (General)         | #EA580C  | #F8FAFC  | Trust blue + orange CTA — fast artifact deployment

# Tron (Mono-Green Tron)
TRON         → Row 90  | Sustainable Energy     | #059669  | #ECFDF5  | Power grid green on light — three lands, full power online


# ════════════════════════════════════════════════════════════════
# QUICK REFERENCE — ARCHETYPE PERSONALITY → ROW
# ════════════════════════════════════════════════════════════════
# Use when the specific color combo row isn't dramatic enough.

# DRAMA/COMBO         → Row 77 Theater/Cinema      | #CA8A04 | #0F0F23  | Dark + spotlight (reanimator, storm, dramatic finishes)
# SPEED/BURN          → Row 80 Cybersecurity        | #FF3333 | #000000  | Maximum intensity (burn, aggro, no-ceiling)
# AUTHORITY/CONTROL   → Row  5 B2B Service          | #0369A1 | #F8FAFC  | Clean professional (control, lock, prison)
# GRIND/MIDRANGE      → Row122 Card & Board Game    | #D97706 | #0F172A  | Felt-table dark (Jund, rock, value midrange)
# NATURE/RAMP         → Row 90 Sustainable Energy   | #059669 | #ECFDF5  | Green living system (ramp, landfall, tron)
# ARISTOCRATS/WEALTH  → Row 33 Luxury/Premium       | #A16207 | #FAFAF9  | Black + gold (aristocrats, taxation, orzhov)
# ELEMENTAL/CHAOS     → Row 37 Travel/Tourism       | #EA580C | #F0F9FF  | Adventure (Gruul, Naya, big red, chaos)
# SHADOW/SECRETS      → Row148 Anonymous Community  | #0891B2 | #0F172A  | Protective dark (Dimir, UB, secretive)
# PRECISION/TEMPO     → Row 60 Dental Practice      | #0EA5E9 | #F0F9FF  | Crisp blue (tempo, Merfolk, Spirits, Blink)
# ELECTRIC/IZZET      → Row  9 Educational App      | #EA580C | #EEF2FF  | Indigo+orange spark (Izzet, Prowess, cantrips)

