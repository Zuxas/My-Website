# Road to Pro Tour — My Website Workspace

You are working inside the Road to Pro Tour website project.
This is Jermey Wallace's (Zuxas) public-facing site documenting his journey
from competitive grinder to Pro Tour qualification through Team Resolve.

---

## Project Location

`E:/vscode ai project/My-Website/`

---

## Folder Structure

```
My-Website/
├── CLAUDE.md                      ← you are here
├── index.html                     ← homepage
├── bio.html                       ← about Zuxas
├── meta.html                      ← Modern metagame — loads from data/modern-meta.json
├── planning.html                  ← decks currently being tested
├── deckbuilding.html              ← Team Resolve deck building process
├── analyze.html                   ← how to analyze deck lists
├── deck-guides.html               ← links to all playbooks
├── styles.css                     ← shared stylesheet
├── card-tooltips.js               ← Scryfall hover tooltips for .c spans
├── wrap_cards.py                  ← wraps card names in .c spans across all playbooks
├── matchup-data-loader.js         ← loads live win rates from DB into matchup tables
├── deck-guide-intake.md           ← intake form template for new playbooks
├── playbook-template.html         ← blank 10-tab playbook template
├── playbook-template.txt          ← fill-in-the-blank text intake form (10-tab)
├── boros-energy-playbook.html     ← Boros Energy full playbook
├── glockulous-playbook.html       ← Grixis Reanimator (Glockulous) playbook
├── jeskai-blink-playbook.html     ← Jeskai Blink playbook
├── prowess-playbook.html          ← Izzet Prowess playbook
├── uw-control-playbook.html       ← UW Control playbook (10-tab, most complete)
├── uw-blink-2025-10-07.html       ← UW Blink (legacy template reference)
├── journey/                       ← season log entries
├── data/                          ← GENERATED JSON from MTG Meta Analyzer DB
│   ├── modern-meta.json           ← meta share, deck counts, trends
│   ├── modern-matchups.json       ← real matchup win rates per deck
│   └── modern-guides.json         ← guide links per deck from Skill Issue sheet
├── fonts/                         ← pirulen, gamecube fonts
└── images/                        ← site images
```

---

## !! DATA PIPELINE — READ THIS FIRST !!

**The site does NOT hardcode meta percentages, win rates, or guide links.**
All of that comes from the MTG Meta Analyzer database via pre-generated JSON files.

### How to refresh site data:
```bash
cd "E:\vscode ai project\mtg-meta-analyzer"
python scripts/generate_site_data.py
```

This writes 3 JSON files to `My-Website/data/`:
- `modern-meta.json` — meta share % per archetype (from 50k+ tournament decklists)
- `modern-matchups.json` — real matchup win rates per our 5 decks (from 262k+ match results)
- `modern-guides.json` — guide links per deck (from Skill Issue Magic spreadsheet)

### Source database:
`E:/vscode ai project/mtg-meta-analyzer/data/mtg_meta.db`
- `matchup_matrix` table — real match win rates
- `decks` + `events` tables — tournament decklists

---

## Playbook Spec (Current Standard)

### Tab Structure
UW Control is on the **10-tab spec** (most complete):
`Overview → Decklist → Game Flow → Engines → Roles → Matchups → Sideboard → Heuristics → Tuning → Prep`

All other 4 playbooks (Boros, Jeskai, Prowess, Glockulous) are on the **8-tab spec**:
`Identity → Decklist → Gameplan → Roles → Matchups → SB Guide → Heuristics → Prep`

Retrofitting the 4 older guides to 10-tab is a future task.

### Matchup Deep Dives — Current State
Every playbook has **11 deep dives** each (55 total across the site).
Each dive contains: overview paragraph, play vs draw split, sideboard table, 4–6 if/then decision trees.

Standard 6 dives (in all 5 guides):
- vs Boros Energy · vs Jeskai Blink · vs Izzet Prowess · vs Glockulous/Reanimator · vs Amulet Titan · vs Mirror

New 5 dives (added this session, based on live meta Feb–Mar 2026 top 9 by share):
- vs Izzet Affinity (6.1%) · vs Eldrazi Tron (5.0%) · vs Domain Zoo (4.3%)
- vs Esper Reanimator (3.5%) · vs Ruby Storm (6.5%)

Live meta data source: `https://j6e.me/mtg-meta-analyzer/metagame?format=Modern&from=2026-02-01&to=2026-03-30`
(103 tournaments, 3,787 players, Feb–Mar 2026)

---

## Oracle Accuracy Requirements

**Oracle accuracy is foundational.** Every card note must reflect confirmed oracle text.
Key facts confirmed across all playbooks:

### Glockulous
- **Psychic Frog** `{U}{B}` 2/2 — combat damage → draw; discard → +1/+1 counter; exile 3 GY cards → flying until EOT
- **Emperor of Bones** `{1}{B}` 2/2 — beginning of combat: exile target GY card. `{1}{B}`: Adapt 2. Whenever counters placed: put exiled creature onto battlefield with finality counter, haste. Sacrifice at beginning of NEXT end step (delayed triggered ability).
- **Consign to Memory** `{U}` Instant, Replicate `{1}` — counters triggered abilities or colorless spells ONLY
- **Persist** `{1}{B}` black sorcery — not a triggered ability, not colorless → Consign CANNOT counter it
- **Finality counter** — creature goes to exile instead of GY on death (permanent exile)
- **Harbinger of the Seas** — static effect, not destruction; nonbasic lands ARE Islands
- **Faithless Looting** — draws THEN discards (draw 2, discard 2); flashback `{2}{R}`
- **Troll of Khazad-dûm** — MV 6, can't be blocked except by 3+ creatures; Swampcycling `{1}`
- **Drown in the Loch** — both modes check controller's graveyard card count for MV threshold
- **Surgical Extraction** `{B/P}` (B or 2 life) — target card in a GY other than basic land, exile all copies from GY+hand+library, then shuffle

### CRITICAL Consign to Memory Offensive Lines (Glockulous)
1. **Emperor sacrifice trigger line**: Emperor adapts → Archon enters with finality counter + haste, attacks, ETB fires → at beginning of NEXT end step the delayed "sacrifice it" trigger fires → fire Consign at your own sacrifice trigger → Archon stays on battlefield permanently. This is the primary reason Consign is in the main deck.
2. **Quantum Riddler Warp trigger bait** (testing consideration, not in current 75): Warp exile trigger is a delayed triggered ability → Consign can counter it to keep the permanent.

### Glockulous — Quantum Riddler / Consign consideration
Current 75 does NOT include Quantum Riddler or Consign to Memory main deck.
These are noted as future testing considerations in the heuristics section.
Quantum Riddler oracle: `{3}{U}{U}` 4/6 Flying. ETB draw. Replacement effect when you have ≤1 card in hand. Warp `{1}{U}` (Edge of Eternities). Warp = alternative cost, permanent exiles at beginning of next end step, can be recast from exile later.

### Psychic Frog — Dual Role
Frog is NOT just a setup piece for Persist. It is a legitimate primary win condition:
- By turn 4-5 with consistent discarding: commonly 5/5 or 6/6 flying lifelink
- Draws a card every time it connects — self-sustaining engine
- Correct pivot when GY plan is shut off by RiP / Surgical / Nihil Spellbomb
- Protect with Mystical Dispute + Thoughtseize same as Archon

### UW Control
- **Teferi TRav static** — always active on entry, NOT from +1. +1 gives YOU sorcery flash
- **Teferi Hero +1** — untaps two lands at beginning of NEXT end step (delayed)
- **Teferi Hero -3** — puts permanent THIRD from top (not exiled, not on top)
- **Snapcaster** — targets GY card immediately on ETB; flashback cost = original mana cost
- **Supreme Verdict** — cannot be countered; destroys all creatures including yours
- **Force of Negation** — only free on opponent's turn; only noncreature spells
- **Consign to Memory** — cannot counter Persist (colored sorcery), cannot counter Counterspell

---

## Design System

- Colors: `#3b3c4d` bg, `#39465c` panels, `#65bcd5` accent cyan, `#f0f0f0` text
- Fonts: Pirulen (h1/h2/nav brand), DM Mono (labels/nav/metadata), Arial (body)
- All styles in external `styles.css` — no inline styles
- Playbooks use embedded CSS (Bebas Neue + DM Mono + Crimson Pro, paper bg #f2ede6)
- Playbook accent colors: Boros=#c0392b, Jeskai=#c0622b, Prowess=#b03a1a, Glockulous=#1a1a8f, UW Control=#3a5fa0

## Known CSS Fixes Applied (All 5 Playbooks)
- **Heuristics layout** — changed `display:flex` to `display:block; overflow:hidden` on `li`, `float:left` on `::before` counter. Fixes card tooltip spans breaking into columns inside flex containers.
- **S&W grid** — added `.card-grid-2 { grid-template-columns:repeat(2,1fr) }` and applied it to Strengths/Weaknesses sections. Fixes phantom empty third column from auto-fill at desktop width.
- **Date** — "March 30, 2026" in all 5 playbook header eyebrows
- **Tooltip double-nesting** — removed shorthand aliases (Ragavan, Teferi, Phlage, Ajani, Phelia, DRC) from wrap_cards.py to prevent double-wrapping on future runs

## wrap_cards.py — Important Notes
- Run after any new playbook content to apply `.c` span wraps to card names
- All shorthand aliases that caused double-wrapping have been removed from the CARDS list
- File marks playbooks as processed (SKIP on re-run) — to force re-run, edit the processed marker
- New cards added to list: Spell Snare, Archmage's Charm, Memory Deluge, Dress Down, Dovin's Veto, Path to Exile, Slickshot Show-Off, Murktide Regent, Goryo's Vengeance, Grapeshot, Past in Flames, Territorial Kavu, etc.

---

## Routing Table

| Task                          | Read these files                         |
|-------------------------------|------------------------------------------|
| Editing any main page         | relevant .html + styles.css              |
| Editing a playbook            | that playbook's .html (self-contained)   |
| Refreshing meta/WR data       | Run generate_site_data.py (see above)    |
| Adding a new playbook         | Copy playbook-template.html              |
| Wrapping card tooltips        | Run wrap_cards.py                        |
| Auditing site health          | Run site_audit.py (checks doubles, dates, heuristics fix, S&W grid) |

## Git Workflow

After making changes that are tested and working, commit and push them to `origin/main`.
Do not let working updates sit uncommitted.

---

## Active Decks (Current 75s on the site)

| Deck | File | Notes |
|---|---|---|
| Boros Energy | boros-energy-playbook.html | Zuxas's current list |
| Grixis Reanimator | glockulous-playbook.html | Team Resolve pet name: Glockulous |
| Jeskai Blink | jeskai-blink-playbook.html | Red splash for Orim's Chant |
| Izzet Prowess | prowess-playbook.html | Cori-Steel Cutter build |
| UW Control | uw-control-playbook.html | Meta-dependent pick, 10-tab spec |

## Voice and Tone

- First person, honest, technical
- Audience: competitive MTG players who understand the format
- No need to explain basic MTG rules — assume format knowledge
- Specific over vague: name the cards, name the matchups, name the decisions
- Oracle accuracy is non-negotiable — verify before writing card notes

## Results (accurate)

- Last Standard season: 23 RCQ Top 8s, qualified on Dimir Midrange
- Last Modern season: 17 RCQ Top 8s, qualified on Boros Energy
- Career: 5 RC qualifications total
