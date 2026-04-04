# CLAUDE.md — Team Resolve Project State
*Last updated: April 4, 2026 — commit 3eebb9a*

---

## PROJECT OVERVIEW

Team Resolve competitive MTG playbook site for Regional Championship prep.

- **Live site:** https://zuxas.github.io/TeamResolve/
- **GitHub:** Zuxas/TeamResolve, branch: main
- **Local:** `E:\vscode ai project\My-Website\`
- **Current commit:** `3eebb9a`

---

## SITE STRUCTURE

### Modern (17 playbooks) — ALL COMPLETE ✅
Files: amulet-titan, boros-energy, dimir-oculus, domain-zoo, eldrazi-tron, glockulous, goryos-vengeance, humans, izzet-affinity, jeskai-blink, living-end, neoform, prowess, ruby-storm, uw-blink, uw-control, yawgmoth

### Standard (14 playbooks) — ALL COMPLETE ✅
Full coverage of every archetype above 2% meta share as of April 3, 2026.

| # | File | Meta % |
|---|---|---|
| 1 | izzet-prowess-playbook.html | 10.15% |
| 2 | dimir-midrange-playbook.html | 6.15% |
| 3 | mono-green-landfall-playbook.html | ~11% |
| 4 | boros-aggro-playbook.html | ~2% |
| 5 | jeskai-control-playbook.html | 2.49% |
| 6 | bant-rhythm-playbook.html | 1.82% |
| 7 | izzet-lessons-playbook.html | 9.77% |
| 8 | dimir-excruciator-playbook.html | 6.81% |
| 9 | izzet-spellementals-playbook.html | 5.26% |
| 10 | simic-rhythm-playbook.html | 4.11% |
| 11 | azorius-flash-playbook.html | 3.03% |
| 12 | mono-red-aggro-playbook.html | 3.00% |
| 13 | boros-dragons-playbook.html | 2.44% |
| 14 | izzet-elementals-playbook.html | 2.87% |

### Pioneer (13 playbooks) — ALL COMPLETE ✅ (completed April 4, 2026)
Full coverage of all archetypes above ~2% meta share (AetherHub Pioneer April 2026).

| # | File | Meta % | Commit |
|---|---|---|---|
| 1 | ur-cutter-playbook.html | ~23% | prior |
| 2 | orzhov-greasefang-playbook.html | ~11% | prior |
| 3 | rdw-pioneer-playbook.html | ~10% | 81c9ca1 |
| 4 | selesnya-company-playbook.html | ~9% | b9f97ca |
| 5 | uw-control-pioneer-playbook.html | ~9% | 9ab898b |
| 6 | arclight-phoenix-playbook.html | ~5% | 0e50ceb |
| 7 | lotus-field-playbook.html | ~4% | 9481487 |
| 8 | izzet-control-pioneer-playbook.html | ~3% | 0d2d0b9 |
| 9 | niv-mizzet-reborn-playbook.html | ~2% | b037480 |
| 10 | rakdos-midrange-pioneer-playbook.html | ~2% | 3ece66b |
| 11 | mono-white-humans-pioneer-playbook.html | ~2% | 3eebb9a |

**Note:** deck-guides.html Pioneer tab links niv-to-light-playbook.html → updated to niv-mizzet-reborn-playbook.html.

---

## CSS STANDARDS (all three formats)

```css
:root {
  --primary:    [darken accent ~40%];
  --ink:        #0e0e0e;
  --paper:      #f2ede6;   /* ALWAYS parchment — never change */
  --paper-dark: #e8e1d6;
  --rule:       #c8bfb0;
  --accent:     [palette accent];
  --accent-light: rgba([accent], 0.08-0.12);
  --mid:        #5a5248;
  --card:       #ffffff;
}
.header-band { background:var(--primary); border-bottom:3px solid var(--accent); padding:48px 80px 40px; }
.header-band,.header-band * { color:#f1f5f9; }
.header-title { font-family:'DM Mono',monospace; font-size:clamp(32px,4vw,52px); }
nav { background:var(--primary); border-bottom:2px solid var(--accent); position:sticky; top:0; }
.nav-brand { color:var(--accent); }  /* static div, NOT a link */
```

Tooltip JS: PAD=24, W=220, H=310. One IIFE per file.

**Compliance checklist (11 checks):**
div_diff=0, 11 tabs, --primary in :root, --paper=#f2ede6, header white text, nav-brand, card-tip-loading, PAD=24, .edge-case CSS, `<footer`, nav BEFORE header-band in HTML.

**11-tab structure:** identity, decklist, gameplan, engines, lines, roles, matchups, sideboard, heuristics, tuning, prep

---

## METAGAME SNAPSHOT

### Pioneer (AetherHub April 2026 — last 90 days)
UR Cutter 22.83% · Greasefang 10.78% · RDW 10.41% · Selesnya Company 9.41%
UW Control 8.68% · Arclight Phoenix 4.84% · Lotus Field 4.20%
Izzet Control 3.01% · Niv-Mizzet 2.19% · Rakdos Boomer ~2% · Mono-White Humans ~2%

### Standard (mtgdecks.net April 3, 2026)
Mono-Green Landfall ~11% · Izzet Prowess 10.15% · Izzet Lessons 9.77%
Dimir Excruciator 6.81% · Dimir Midrange 6.15% · Izzet Spellementals 5.26%
Simic Rhythm 4.11% · Azorius Flash 3.03% · Mono-Red Aggro 3.00%
Izzet Elementals 2.87% · Jeskai Control 2.49% · Boros Dragons 2.44%
Boros Aggro ~2% · Bant Rhythm 1.82%

---

## OUTSTANDING / NEXT SESSION OPTIONS

### Option A — Modern LDXP SEA26 Audit Queue ✅ COMPLETE (April 4, 2026)
All 8 queue files audited and passed content + compliance review:
Domain Zoo (2.19) · Eldrazi Tron (1.71) · Glockulous (1.58) · Jeskai Blink (1.23)
Living End (2.13) · Neoform (4.02) · Izzet Prowess (1.74) · Yawgmoth (2.94)

Compliance batch fix commit: ec9bb7e — PAD=24 format + color:#f1f5f9 combined selector
applied to all 15 Modern files that were using old spaced format.
**42/42 playbooks site-wide now pass all 10 compliance checks.**

### Option B — Standard Meta % Update
Several Standard playbooks have stale meta percentages in their header-band meta-row.
Pull fresh numbers from mtgdecks.net and patch all 14 files.

### Option C — New Standard/Pioneer Entries
Monitor for new decks crossing 2% threshold (Pioneer: Izzet Elementals, Azorius Blink, Mono-White Shepherd noted as new entries). Build new playbooks as needed.

### Option D — Pioneer Meta % Refresh
Pioneer playbooks used AetherHub 90-day numbers. Pull a tighter window (last 30 days) for more current meta share values.

---

## TECHNICAL PATTERNS

**Python patch scripts:** Written to `E:\vscode ai project\My-Website\_a.py`, run via DC start_process (powershell, 6-8s timeout), deleted after run.

**Darken formula:** `primary = '#{:02x}{:02x}{:02x}'.format(int(r*0.4), int(g*0.4), int(b*0.4))`

**Commit pattern:** `git add -A ; git commit -m "..." ; git push origin main` via powershell, 25s timeout.

**Audit audit script pattern:**
```python
diff = c.count('<div') - c.count('</div>')
btns = re.findall(r"onclick=\"show\('([^']+)'\)\"", nav_region)
fails = [] # check: div==0, parchment, primary, header_white, nav_brand, card-tip-loading, PAD, len(btns)==11, edge_css, footer
```
