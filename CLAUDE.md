# CLAUDE.md — Team Resolve MTG Playbook Project
# Handoff document for continuing sessions
# Last updated: 2026-03-31 | Commit: 6572487

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
| Domain Zoo | — (needs audit) | — |
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
1. **Domain Zoo** ← next target
2. Eldrazi Tron
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

## KEY TECHNICAL PATTERNS

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

## PLAYBOOK HTML STRUCTURE (10 tabs)

Every playbook follows this identical structure:
```
CH01: Overview / Identity / Philosophy
CH02: The 75 (decklist + mana curve + key card notes)
CH03: Game Plan / Game Flow  
CH04: Engines / Core Engines
CH05: Roles / Role Assignment
CH06: Matchup Deep Dives (matchup table + SB tables)
CH07: Sideboard Guide (card-by-card)
CH08: Heuristics & Quick Rules (16 items)
CH09: Tuning Notes
CH10: Event Day Prep / Prep Sheet (print grid)
```

Key site_audit checks:
- `tabs=10` (all 10 tabs present)
- `doubles=0` (no duplicate card entries)
- `heur=True` (heuristics section present)
- `date=True` (date in header)
- `sw=True` (wrap_cards has been run)

---

## WHAT CHANGED THIS SESSION (2026-03-31)

### Amulet Titan full audit (commit 3c0d238)
Reference: aljce LDXP SEA26 10k, 1st place (13-1-2)
Key changes across all 10 chapters:
- Kill line: Slayers' Stronghold + Sunhome → **Hanweir Battlements + Mirrorpool**
- Secondary win: Valakut/Dryad → **Scapeshift + Amulet Burst**
- Oracle entries: Dryad of the Ilysian Grove → **Scapeshift + Malevolent Rumble + Green Sun's Zenith**
- SB 15: Defense Grid/Endurance/Cursed Totem/EE/Haywire → **Fire Magic ×3, Force of Vigor ×3, Dismember ×2, Trinisphere ×2, Bojuka Bog, Collector Ouphe, Icetill Explorer, Six, The Wandering Minstrel**

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
