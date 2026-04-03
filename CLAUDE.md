# CLAUDE.md — Team Resolve MTG Playbook Project
# Handoff document for continuing sessions
# Last updated: 2026-04-03 | Commit: 31b641e

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

## CURRENT STATE

### Modern (16 playbooks) — ALL COMPLETE
All 16 pass full compliance audit:
- div_diff=0, 11 tabs, parchment base, unique accent/primary per deck
- UI UX Pro Max palette applied (colors.csv row per deck)
- Scryfall card tooltips (PAD=24, 220px)
- `← Guides` nav + static brand on all 16
- Header white text on all 16

### Standard (6 playbooks) — ACTIVE RC PREP
| Deck | Meta % | Lessons MU |
|---|---|---|
| Izzet Prowess | 10.15% | ✅ |
| Dimir Midrange | 6.15% | ✅ |
| Mono-Green Landfall | ~11% | ✅ |
| Boros Aggro | ~2% | ✅ |
| Jeskai Control | 2.49% | ✅ |
| Bant Rhythm | 1.82% | ✅ (new, Fortunati RC Turin 1st 15-2) |

All 6 have current April 3 2026 meta % and Izzet Lessons matchup.

### deck-guides.html
- Modern tab: 17 (includes Boros Energy)
- Standard tab: 6 (includes Bant Rhythm)
- All deck cards show color identity + meta % (no palette credits)

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

**ALL playbooks use light/parchment base — NO dark themes.**

---

## CSS STANDARDS FOR ALL PLAYBOOKS
### (apply to every new playbook, enforce on all existing ones)

### :root variables — complete required set
```css
:root {
  --primary:      [darken(accent, 0.25)];   /* header bg — always very dark */
  --ink:          #0e0e0e;                  /* body text — always near-black */
  --paper:        #f2ede6;                  /* content bg — always parchment */
  --paper-dark:   #e8e1d6;                  /* slightly darker parchment */
  --rule:         #c8bfb0;                  /* dividers */
  --accent:       [palette accent hex];     /* links, titles, borders, underlines */
  --accent-light: rgba([accent RGB], 0.15); /* tinted backgrounds */
  --danger:       #8f1a1a;
  --danger-light: rgba(143,26,26,0.12);
  --gold:         [same as accent];
  --gold-light:   rgba([accent RGB], 0.15);
  --mid:          #5a5248;                  /* muted text */
  --card:         #ffffff;                  /* card backgrounds */
}
```

### --primary formula
`--primary` = the palette's Primary color darkened to 25% brightness:
```python
def darken(hex, factor=0.25):
    r,g,b = hex_to_rgb(hex)
    return '#{:02x}{:02x}{:02x}'.format(int(r*factor), int(g*factor), int(b*factor))
primary = darken(palette_row['Primary'])
```
Examples: `#0891B2` → `#02242c` | `#7C3AED` → `#1f0e3b` | `#CA8A04` → `#322201`

### Header band
```css
.header-band {
  background: var(--primary);            /* dark, deck-specific tint */
  border-bottom: 3px solid var(--accent);
  color: #f1f5f9;                        /* REQUIRED — white text on dark bg */
}
.header-band p, .header-band span, .header-band div { color: #f1f5f9; }
```

### Nav bar
```css
nav {
  background: var(--primary);            /* same dark as header */
  border-bottom: 2px solid var(--accent);
}
.nav-brand { color: var(--accent); }
.nav-link  { color: rgba(248,250,252,0.55); }
.nav-link.active, .nav-link:hover { color: rgba(248,250,252,1); }
```

### Nav structure (required elements, in order)
```html
<nav>
  <div class="nav-brand">Deck Name</div>
  <a class="nav-link" href="deck-guides.html" style="text-decoration:none;">&#8592; Guides</a>
  <button class="nav-link active" onclick="show('identity')">Overview</button>
  <!-- remaining tab buttons -->
</nav>
```
- Nav brand is a `<div>` (NOT an `<a>` tag — brand is not a link)
- `← Guides` is always the first nav-link after the brand
- No other back-links anywhere

### Scryfall card image tooltips
Inject before `</style>`:
```css
.card-tip { position:fixed; z-index:9999; pointer-events:none; width:220px;
  border-radius:8px; overflow:hidden; box-shadow:0 8px 32px rgba(0,0,0,0.6);
  opacity:0; transition:opacity 0.15s ease; background:#1a1a2e; }
.card-tip.visible { opacity:1; }
.card-tip img { width:220px; height:auto; display:block; }
.card-tip-loading { width:220px; height:308px; display:flex; align-items:center;
  justify-content:center; color:#94a3b8; font-size:12px; font-family:monospace;
  background:#1e293b; }
span.c { cursor:help; border-bottom:1px dashed var(--accent,#CA8A04); }
span.c:hover { border-bottom-style:solid; }
```

Inject before `</body>`:
```html
<script>
(function() {
  const TIP = document.createElement('div');
  TIP.className = 'card-tip';
  TIP.innerHTML = '<div class="card-tip-loading">loading...</div>';
  document.body.appendChild(TIP);
  const CACHE = {};
  let hideTimer = null;
  function pos(e) {
    const PAD=24,W=220,H=310;
    let x=e.clientX+PAD, y=e.clientY-H/2;
    if(x+W>window.innerWidth) x=e.clientX-W-PAD;
    if(y<8) y=8;
    if(y+H>window.innerHeight) y=window.innerHeight-H-8;
    TIP.style.left=x+'px'; TIP.style.top=y+'px';
  }
  async function show(name,e) {
    clearTimeout(hideTimer);
    TIP.innerHTML='<div class="card-tip-loading">loading...</div>';
    TIP.classList.add('visible'); pos(e);
    if(CACHE[name]){TIP.innerHTML=`<img src="${CACHE[name]}" alt="${name}">`;return;}
    try {
      const r=await fetch(`https://api.scryfall.com/cards/named?fuzzy=${encodeURIComponent(name)}`);
      if(!r.ok){TIP.classList.remove('visible');return;}
      const d=await r.json();
      const img=d.image_uris?.normal||d.card_faces?.[0]?.image_uris?.normal;
      if(!img){TIP.classList.remove('visible');return;}
      CACHE[name]=img; TIP.innerHTML=`<img src="${img}" alt="${name}">`;
    } catch(err){TIP.classList.remove('visible');}
  }
  function hide(){hideTimer=setTimeout(()=>TIP.classList.remove('visible'),80);}
  document.addEventListener('mouseover',e=>{const el=e.target.closest('span.c');if(!el)return;show(el.textContent.trim(),e);});
  document.addEventListener('mousemove',e=>{if(TIP.classList.contains('visible'))pos(e);});
  document.addEventListener('mouseout',e=>{if(e.target.closest('span.c'))hide();});
})();
</script>
```

### Compliance checklist for every new playbook
- [ ] `:root` has all 13 vars including `--primary`
- [ ] `--paper: #f2ede6` (parchment, NOT palette background color)
- [ ] `--ink: #0e0e0e` (dark text, NOT palette foreground color)
- [ ] `--primary` = palette Primary darkened to 25%
- [ ] `.header-band` uses `var(--primary)` bg + `var(--accent)` border + `color:#f1f5f9`
- [ ] `nav` uses `var(--primary)` bg + `var(--accent)` border-bottom
- [ ] Nav has static brand div + `← Guides` link + tab buttons
- [ ] Scryfall tooltip CSS injected once before `</style>`
- [ ] Scryfall tooltip JS injected once before `</body>`
- [ ] `div_diff == 0` (balanced divs)
- [ ] Footer has `Palette: [Name] (UI UX Pro Max Row [N])`

**Current palette assignments (all 16 Modern playbooks):**
| Deck | Row | Accent | Primary (darkened) |
|---|---|---|---|
| amulet-titan | 25 EV/Charging | #16A34A | #02242c |
| dimir-oculus | 96 Ride Hailing | #2563EB | #09183a |
| domain-zoo | 4 E-comm Luxury | #A16207 | #070605 |
| eldrazi-tron | 5 B2B Service | #0369A1 | #03050a |
| glockulous | 14 Fintech/Crypto | #8B5CF6 | #22173d |
| goryos-vengeance | 77 Theater/Cinema | #CA8A04 | #322201 |
| humans | 71 Membership | #D97706 | #2d1a00 |
| izzet-affinity | 8 Healthcare | #059669 | #02242c |
| jeskai-blink | 1 SaaS General | #EA580C | #09183a |
| living-end | 64 Brewery/Winery | #A16207 | #1f0b04 |
| neoform | 2 Micro SaaS | #059669 | #18193c |
| prowess | 9 Educational | #EA580C | #131139 |
| ruby-storm | 80 Cybersecurity | #FF3333 | #3f0c0c |
| uw-blink | 60 Dental Practice | #0EA5E9 | #03293a |
| uw-control | 30 Knowledge Base | #2563EB | #11151a |
| yawgmoth | 81 Developer Tool | #22C55E | #083117 |

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
