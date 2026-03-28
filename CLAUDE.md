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
├── deck-guides.html               ← links to all 6 playbooks
├── styles.css                     ← shared stylesheet
├── boros-energy-playbook.html     ← Boros Energy full playbook
├── glockulous-playbook.html       ← Grixis Reanimator (Glockulous) playbook
├── uw-blink-2025-10-07.html       ← UW Blink full playbook (canonical template)
├── uw-control-playbook.html       ← UW Control playbook
├── prowess-playbook.html          ← Izzet Prowess playbook
├── jeskai-blink-playbook.html     ← Jeskai Blink playbook
├── journey/                       ← season log entries
├── data/                          ← GENERATED JSON from MTG Meta Analyzer DB
│   ├── modern-meta.json           ← meta share, deck counts, trends
│   ├── modern-matchups.json       ← real matchup win rates per deck
│   └── modern-guides.json        ← guide links per deck from Skill Issue sheet
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
- `modern-guides.json` — guide links per deck (from Skill Issue Magic spreadsheet, 331 entries)

### When to run the data script:
- Before any RC event (get fresh meta read)
- After a major ban/unban announcement
- When new tournament data is scraped (6 AM daily task runs automatically)
- Anytime meta.html or playbook win rates look stale

### Source database:
`E:/vscode ai project/mtg-meta-analyzer/data/mtg_meta.db`
- `matchup_matrix` table — 6,159 rows of real match win rates
- `decks` + `events` tables — 50,416 decklists across 4,338 events
- `guides` table — 331 guide links from Skill Issue Magic sheet

### How pages consume the data:
- `meta.html` — `fetch('data/modern-meta.json')` on load, renders dynamically
- All 6 playbooks — `fetch('data/modern-matchups.json')` fills real win rates into matchup tables
- Win rates shown as: `54.2% (574 matches)` — always with sample size

---

## Design System

- Colors: `#3b3c4d` bg, `#39465c` panels, `#65bcd5` accent cyan, `#f0f0f0` text
- Fonts: Pirulen (h1/h2/nav brand), DM Mono (labels/nav/metadata), Arial (body)
- h2 tags: font-size 1rem (project spec — do not change)
- All styles in external `styles.css` — no inline styles
- Playbooks use their own embedded CSS (Bebas Neue + DM Mono + Crimson Pro, paper bg #f2ede6)
- Playbook h2 = 1rem as per project spec

## Routing Table

| Task                          | Read these files                        |
|-------------------------------|------------------------------------------|
| Editing any main page         | relevant .html + styles.css              |
| Editing a playbook            | that playbook's .html (self-contained)   |
| Refreshing meta/WR data       | Run generate_site_data.py (see above)    |
| Adding a new playbook         | Use uw-blink-2025-10-07.html as template |

## Git Workflow

After making changes that are tested and working, commit and push them to `origin/main` so GitHub stays in sync with local work. Do not let working updates sit uncommitted — if a session produced good changes, stage, commit, and push before wrapping up.

---

## Playbook Template

UW Blink (`uw-blink-2025-10-07.html`) is the canonical 8-chapter template:
Identity → Decklist → Gameplan → Roles → Matchups (clickable expand panels) →
SB Guide → Heuristics → Prep/Print sheet.

## Active Decks (Current 75s on the site)

| Deck | File | Moxfield | Notes |
|---|---|---|---|
| Boros Energy | boros-energy-playbook.html | AluChvBLD0qav8oZINYvGw | Zuxas's current list |
| Grixis Reanimator | glockulous-playbook.html | — | Team Resolve pet name: Glockulous |
| UW Blink | uw-blink-2025-10-07.html | — | Canonical template |
| UW Control | uw-control-playbook.html | — | Meta-dependent pick |
| Izzet Prowess | prowess-playbook.html | — | Cori-Steel Cutter build |
| Jeskai Blink | jeskai-blink-playbook.html | — | Red splash for Orim's Chant |

## Voice and Tone

- First person, honest, technical
- Audience: competitive MTG players who understand the format
- No need to explain basic MTG rules — assume format knowledge
- Specific over vague: name the cards, name the matchups, name the decisions

## Results (accurate)

- Last Standard season: 23 RCQ Top 8s, qualified on Dimir Midrange
- Last Modern season: 17 RCQ Top 8s, qualified on Boros Energy
- Career: 5 RC qualifications total
- Current Modern testing: Boros Energy, UW Blink, Jeskai Blink, Grixis Reanimator, UW Control, Prowess
