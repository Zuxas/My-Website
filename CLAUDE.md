# CLAUDE.md — Team Resolve MTG Playbook Project
# Handoff document for continuing sessions
# Last updated: 2026-03-31 | Commit: cb70208

---

## WHO YOU ARE WORKING WITH

**Jermey** (operating as **Zuxas**, captain of Team Resolve)
- Building a competitive Modern MTG playbook website
- Signals continuation with **"Continue"** — never ask which task to do next, just execute
- Never ask for check-ins mid-task; complete the full workflow autonomously
- Prefers prose responses, not bullet lists

---

## PROJECT LOCATION

```
E:\vscode ai project\My-Website\
```
- GitHub: https://github.com/Zuxas/TeamResolve.git  (branch: main)
- Latest commit: 6572487 (Boros Energy full audit)
- Local-only file: `planning.html` (gitignored — never commit)

---

## CURRENT STATE: 15 PLAYBOOKS

### ✅ COMPLETE (audited against LDXP SEA26 where applicable)
| Deck | melee.gg Reference | Record |
|---|---|---|
| Amulet Titan | https://melee.gg/Decklist/View/2a4efd5e (aljce) | 13-1-2, 1st |
| Boros Energy | https://melee.gg/Decklist/View/02cc5e0e (Pfenning) | 10-3-0, 9th |
| Domain Zoo | https://melee.gg/Decklist/View/51023674 (MasT1) | 9-4-0, 19th |
| Eldrazi Tron | — (needs audit) | — |
| Glockulous (Grixis Reanimator) | — (needs audit) | — |
| Izzet Affinity | https://melee.gg/Decklist/View/f8e13375 (Jeffrey Chang) | 10-0-4 |
| Jeskai Blink | — (needs audit) | — |
| Living End | — (needs audit) | — |
| Neoform | — (needs audit) | — |
| Golgari Yawgmoth | — (needs audit) | — |
| Izzet Prowess | — (needs audit) | — |
| Ruby Storm | https://melee.gg/Decklist/View/5b97bdff (Chance McDougal) | 9-0-4 |
| UW Blink | intentionally pre-LDXP shell | — |
| UW Control | https://melee.gg/Decklist/View/a6a4917b (Evariel) | 8-0-2 |

### 📋 NEXT IN QUEUE (alphabetical)
1. **Eldrazi Tron** ← next target
2. Glockulous
3. Jeskai Blink
4. Living End
5. Neoform
6. Izzet Prowess
7. Golgari Yawgmoth
3. Glockulous
4. Jeskai Blink
5. Living End
6. Neoform
7. Izzet Prowess
8. Golgari Yawgmoth

---

## LDXP SEA26 TOURNAMENT REFERENCE

**Event:** LDXP SEA26 3/28 Modern 10k  
**melee.gg Tournament:** https://melee.gg/Tournament/View/402502

**Top 9 with known decks:**
1. aljce — Mono-Green Amulet Titan — 13-1-2 ✅ audited
2. Andrew Sullano — Izzet Affinity — 12-3-1
3. robert seder — Esper Blink — 11-2-2
4. Will Hagmann — Simic Ritual — 11-4-0
5. Roy Yang — Dimir Midrange — 10-3-1
6. Quentin Wilebski — Mono-Red Combo — 10-4-0
7. DylanHeisey — Sultai — 10-4-0
8. Jeffrey Chang — Izzet Affinity — 10-4-0 ✅ audited (earlier session)
9. Reese Pfenning — Boros Energy — 10-3-0 ✅ audited

To find more results: navigate to tournament page and use JS:
```javascript
const deckLinks = [...document.querySelectorAll('a[href*="Decklist/View"]')];
deckLinks.slice(N, N+15).map(a => {
  const row = a.closest('tr');
  return row ? row.textContent.trim().replace(/\s+/g,' ').slice(0,150) + '\n  -> ' + a.href : a.href;
}).join('\n\n');
```

---

## THE AUDIT WORKFLOW (execute in strict order, no deviation)

### Step 1 — Find the LDXP reference list
Navigate to melee.gg tournament page 402502, use JavaScript to scan standings for the deck's archetype name. Get the decklist URL. Navigate to it and use `get_page_text` to read the full 75.

### Step 2 — Read the full playbook
`Desktop Commander:read_file` the HTML file in chunks (offset 0 length 200, then 200+, etc.) until you have all 10 chapters mapped.

### Step 3 — Diff old vs new
Compare every card in old decklist vs new decklist. Track:
- Cards added (new)
- Cards removed (cut)
- Count changes (3→4, etc.)
- Sideboard changes card by card

### Step 4 — Plan all changes needed across all 10 chapters
Typically affected sections:
- **CH02**: Decklist grid + mana curve + key card notes
- **CH03**: Kill line descriptions, game flow references
- **CH04**: Engine names and descriptions, tricks list
- **CH05**: Role descriptions referencing specific cards
- **CH06**: Every matchup SB table (In/Out) — all must use real SB cards
- **CH07**: Full card-by-card sideboard guide (rewrite completely)
- **CH08**: Heuristics referencing removed/changed cards
- **CH09**: Tuning grid (remove stale conditions, add new ones)
- **CH10**: Kill line reference cards + all print grid SB tables

### Step 5 — Execute with Python scripts for bulk changes
For changes involving Unicode minus (−, U+2212), HTML entities (&minus;), or multiline blocks:
- Write a Python script to `E:\vscode ai project\My-Website\_fix_DECKNAME_p1.py`
- Run it with `Desktop Commander:start_process`
- Check output for MISS vs OK per replacement
- For missed items: read the exact file bytes to find actual text, then retry

For small targeted changes: use `Desktop Commander:edit_block` directly.

**CRITICAL — Unicode minus:** The files use real Unicode minus U+2212 (−), NOT HTML entity &minus; and NOT ASCII hyphen (-). In Python scripts, always use `'\u2212'` for the minus character in search strings.

**CRITICAL — str_replace / edit_block failures:** If edit_block fails, use a Python script instead. Edit_block fails on large blocks and newline differences.

### Step 6 — Verify no stale references remain
```python
stale_cards = ['OldCardName', 'AnotherCutCard']
for s in stale_cards:
    count = c.count(s)
    if count > 0: print(f'{count}x: {s}')
```
Any stale card in narrative text that's now out of the 75 should be updated.

### Step 7 — Run tools
```powershell
cd "E:\vscode ai project\My-Website"
python tools/wrap_cards.py FILENAME.html
python tools/site_audit.py
```
`wrap_cards.py` is idempotent (skips already-processed files). site_audit checks tab count, heuristics, dates, etc.

### Step 8 — Clean up and commit
```powershell
Remove-Item _fix_*.py
git add FILENAME.html
git commit -m "DECKNAME: audit message"
git push origin main
```
Git uses PowerShell semicolon-chained syntax, 30s timeout.

---

## PALETTE SYSTEM — UI UX PRO MAX COLORS.CSV

Every playbook gets a named palette from `UI_UX_Pro_Max_colors.csv`.
File location: `E:\vscode ai project\My-Website\UI_UX_Pro_Max_colors.csv`

**How it works:**
- Each row in the CSV is a named palette with columns: Row# | Name | Primary | Accent | Background | Foreground
- Pick a palette that matches the deck's personality
- Note the row number — it goes in the footer: `"Palette: [Name] (UI UX Pro Max Row [N])"`
- The Accent color becomes `--accent` in the CSS `:root` vars

**Selection guide:**
- Aggro/burn → warm (red, orange, amber rows)
- Control → cool (blue, slate, indigo rows)
- Combo/reanimator → dramatic (Theater/Cinema, deep purple rows)
- Midrange → earth tones (forest green, teal, olive rows)

**Full MTG color combo → archetype → row mapping:**
See `PALETTE_GUIDE.md` in the project root.
This file assigns a specific Row # to every color combination + archetype style
(e.g. Izzet Aggro → Row 9, Jund Midrange → Row 122, Esper Reanimator → Row 77).
Always check this file before picking a palette for a new guide.

**CSS vars to set:**
```css
--accent:       [Accent hex]
--accent-light: rgba([accent RGB], 0.18)
--gold:         [same as accent for single-accent designs]
--gold-light:   rgba([accent RGB], 0.18)
```

**Dark vs light theme:**
- Light theme (default): `--paper: #FAFAF8`, `--ink: #1C1917`
- Dark theme (e.g. Goryo's Vengeance Row 77): `--paper: #0F0F23`, `--ink: #F8FAFC`
  Dark theme requires extra contrast work on cards, print-grid, SB tables.

**Current palette assignments** (check each playbook's footer for Row #):
- Goryo's Vengeance: Theater/Cinema, Row 77, `--accent: #CA8A04` (gold), dark theme
- All others: check `<footer>` tag in the HTML file for `Palette:` credit

---



### Reading melee.gg decklists
Navigate to the URL, then `get_page_text` — returns full decklist as plain text with card names and quantities. Works reliably.

### Finding melee.gg tournament standings
```javascript
// In Claude in Chrome on the tournament page:
const deckLinks = [...document.querySelectorAll('a[href*="Decklist/View"]')];
deckLinks.slice(0, 20).map(a => {
  const row = a.closest('tr');
  return row ? row.textContent.trim().replace(/\s+/g,' ').slice(0,150) + '\n  -> ' + a.href : '';
}).join('\n\n');
```

### Finding a tournament ID from a known decklist
```javascript
// On any decklist page:
const links = [...document.querySelectorAll('a[href*="Tournament/View"]')];
links.map(a => a.href + ' | ' + a.textContent.trim()).join('\n');
```

### Python replacement pattern (Unicode-safe)
```python
import sys
sys.stdout.reconfigure(encoding='utf-8')
minus = '\u2212'  # U+2212, NOT regular hyphen

with open(r'E:\vscode ai project\My-Website\FILENAME.html', encoding='utf-8') as f:
    c = f.read()

old = 'exact text from file with ' + minus + '2 entries'
new = 'replacement text'

if old in c:
    c = c.replace(old, new, 1)
    print('OK')
else:
    print('MISS')
    # debug: find nearby text
    idx = c.find('partial search term')
    print(repr(c[idx-100:idx+200]))

with open(r'E:\vscode ai project\My-Website\FILENAME.html', 'w', encoding='utf-8') as f:
    f.write(c)
```

### Scryfall API (for oracle text verification)
```javascript
// In browser console or Claude in Chrome:
const delay = ms => new Promise(r => setTimeout(r, ms));
async function getCard(name) {
    const r = await fetch(`https://api.scryfall.com/cards/named?fuzzy=${encodeURIComponent(name)}`);
    const d = await r.json();
    await delay(80);
    // For MDFCs, check d.card_faces[0].oracle_text and d.card_faces[1].oracle_text
    return d.oracle_text || d.card_faces?.map(f => f.name + ': ' + f.oracle_text).join(' // ');
}
// Usage:
getCard('Primeval Titan').then(console.log);
```
Rate limit: 80ms between requests. Store results in `window._deckOracle`.

---

## FILE STRUCTURE

```
E:\vscode ai project\My-Website\
├── CLAUDE.md                        ← this file
├── MODERN_PLAYBOOK_SOURCES.md       ← master source/queue reference (360 lines)
├── deck-guides.html                 ← index of all playbooks
├── planning.html                    ← LOCAL ONLY, gitignored
├── *-playbook.html                  ← 15 playbook files
└── tools/
    ├── wrap_cards.py                ← wraps card names in <span class="c">
    ├── site_audit.py                ← checks all playbooks for issues
    ├── wrap_dive_cards.py
    ├── wrap_new_cards.py
    ├── fetch_oracle.py
    └── playbook_audit.py            ← consolidated audit tool
```

The `tools/` folder is tracked by git (added `.gitignore` exception `!tools/`).  
Temp fix scripts (`_fix_*.py`) are always deleted before commit.

---

## PLAYBOOK HTML STRUCTURE (11 tabs)

**Gold standard: Goryo's Vengeance (April 2026). All new guides match this.**
Template: `playbook-template.txt` | Intake form: `deck-guide-intake.md`

```
CH01: Identity       — key cards oracle-verified + edge cases
CH02: Decklist       — 75 + melee.gg reference
CH03: Gameplan       — kill line + alt lines + mulligan guide + play/draw + backup plans
CH04: Engines        — engine A/B/C + priority order + speed math
CH05: Lines          — 3 priority lines + timing/target/decision edge cases
CH06: Roles          — 3 roles + how to identify + mistakes + switching signals
CH07: Matchups       — table (role/verdict/key play) + expand (SB + point edges)
CH08: Sideboard      — card-by-card guide + SB matrix
CH09: Heuristics     — 12–16 numbered rules
CH10: Tuning         — flex slot analyses + register conditions + SB priority order
CH11: Prep           — crash course → SB matrix → testing → matchday
```

**Section quality bar:**
- Identity: oracle text verified via Scryfall. Edge cases = non-obvious rules only.
- Gameplan: mulligan is card-grid-3 with specific hands, not vague conditions.
- Engines: priority order explicit. Speed math includes exact mana costs.
- Lines: 3 priority lines at top. Edge cases under Timing/Target/Decision headers.
- Roles: switching signals are explicit triggers. Mistake list has 4 items.
- Matchups: every matchup has point edges (+N pts format). SB note explains cuts.
- Tuning: register conditions are specific (%, meta density), not generic.
- Prep: SB matrix prints on 1 page portrait (printSB() function, not window.print()).

**Pilot-perspective voice standard:**
Every section answers "what do you do" — never describes what the opponent does
without immediately telling the pilot what to do in response.
Audit: you/your ratio vs they/their/them should skew heavily toward "you."

**Key site_audit checks:**
- `tabs=11` (all 11 tabs present)
- `doubles=0` (no duplicate card entries)
- `heur=True` (heuristics section present)
- `date=True` (date in header)
- `sw=True` (wrap_cards has been run)
- `print_btn=True` (printSB() not window.print())

**Common HTML structure pitfalls (learned from Goryo's build):**
- div balance MUST be 0 globally and per-section before committing
- Never use an anchor that includes the section's closing </div> — content inserted after it floats outside the section and shows on every tab
- Prep reorders require surgery on h2 blocks only — never reassemble the full section wrapper
- The page wrapper </div><!-- end .page --> must be AFTER the last section's </div>
- @media print needs body class toggle (printSB()) not window.print() for isolated printing
- table-layout:fixed + colgroup required on matchup tables to prevent column shift on row expand

---

## WHAT CHANGED THIS SESSION (2026-03-31)

### Amulet Titan full audit (commit 3c0d238)
Reference: aljce LDXP SEA26 10k, 1st place (13-1-2)
Key changes across all 10 chapters:
- Kill line: Slayers' Stronghold + Sunhome → **Hanweir Battlements + Mirrorpool**
- Secondary win: Valakut/Dryad → **Scapeshift + Amulet Burst**
- Oracle entries: Dryad of the Ilysian Grove → **Scapeshift + Malevolent Rumble + Green Sun's Zenith**
- SB 15: Defense Grid/Endurance/Cursed Totem/EE/Haywire → **Fire Magic ×3, Force of Vigor ×3, Dismember ×2, Trinisphere ×2, Bojuka Bog, Collector Ouphe, Icetill Explorer, Six, The Wandering Minstrel**

### Domain Zoo full audit (commit cb70208)
Reference: MasT1 LDXP SEA26 10k, 19th (9-4-0)
https://melee.gg/Decklist/View/51023674-0659-459c-b917-b41b0018e03b
Key maindeck changes: -Nishoba Brawler x3, -Kraven x2, -Spectral Denial x2,
-Consign x2 main, Ragavan/Phlage 4->3; +Psychic Frog x3, +Tribal Flames x3,
+Thraben Charm x1 main, lands 17->21 (Indatha Triome, Spara's HQ, Blood Crypt etc)
SB completely replaced: old (Soul-Guide, Endurance, Mystical Dispute, Wear//Tear,
Wrath, Celestial Purge) → new (Consign x4, Pyroclasm x2, Pest Control x2,
Magebane Lizard x2, Clarion Conqueror x2, Thraben Charm x2, Stubborn Denial x1)
All 10 chapters updated.

### Domain Zoo important notes for future reference
- Spectral Denial is NOT in this list — all references purged
- Nishoba Brawler and Kraven are NOT in this list
- Consign to Memory is SB only (x4), not main
- Triomes: Spara's Headquarters + Indatha Triome (not Xander's Lounge/Lush Portico)
- Psychic Frog combos with Territorial Kavu rummage: discard triggers Frog +1/+1 + flying

### Boros Energy full audit (commit 6572487)
Reference: Reese Pfenning LDXP SEA26 10k, 9th (10-3-0)
Key changes:
- Maindeck: +4 Seasoned Pyromancer (new), Ajani 3→4, +1 Ranger-Captain, -3 Static Prison, Thraben 3→2, +1 Blood Moon main, land base overhaul (Arena of Glory/Flooded/Marsh/Parlor/Heath)
- SB: -Deafening Silence, -Vexing Bauble, -Clarion Conqueror; +2 Obsidian Charmaw, +1 Orim's Chant, +1 Tunnel Ignus, Wear//Tear ×2, Legend of Roku ×2

### Filesystem cleanup (commit 60d0917)
- Created `tools/` folder with 6 permanent scripts
- Deleted all 119 session-temp `_*.py` scripts from root
- Updated `.gitignore`

---

## SOURCES REFERENCE

The file `MODERN_PLAYBOOK_SOURCES.md` (360 lines) has:
- All remaining archetypes with meta % and accent colors
- Tiered source quality ratings (★★★ = primary, must read fully)
- Key oracle facts per deck
- Build workflow checklist
- Meta percentages

**For each new deck:** read `MODERN_PLAYBOOK_SOURCES.md` section for that deck before building/auditing.

---

## COMMON PITFALLS TO AVOID

1. **Never reference Slayers' Stronghold or Sunhome** in Amulet Titan — those lands are not in the list
2. **Never reference Dryad of the Ilysian Grove or Valakut** in Amulet Titan — not in the list
3. **Never reference Defense Grid, Endurance, Cursed Totem** in Amulet Titan SB — not in SB
4. **Never reference Static Prison, Deafening Silence, Vexing Bauble, Clarion Conqueror** in Boros Energy — cut
5. **Unicode minus** (−) not ASCII hyphen (-) for sb-qty values in HTML
6. **Tolaria West finds MV 0 cards** (Summoner's Pact), NOT Amulet of Vigor (MV 1)
7. **Karn's static does NOT stop Amulet of Vigor** — Amulet is triggered, not activated
8. **Always verify oracle text** before writing card descriptions — use Scryfall API

---

## GIT COMMANDS

```powershell
# Standard commit+push (semicolons for PowerShell chaining)
git add FILENAME.html ; git commit -m "message" ; git push origin main

# Check current status
git status ; git log --oneline -5
```
