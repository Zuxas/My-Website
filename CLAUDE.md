# CLAUDE.md — Team Resolve Project State
*Last updated: April 3, 2026 — commit dd0ed18*

---

## PROJECT OVERVIEW

Team Resolve competitive MTG playbook site for Regional Championship Standard 2026 play.

- **Live site:** https://zuxas.github.io/TeamResolve/
- **GitHub:** Zuxas/TeamResolve, branch: main
- **Local:** `E:\vscode ai project\My-Website\`
- **Current commit:** `dd0ed18`

---

## SITE STRUCTURE

### Modern (16 playbooks) — ALL COMPLETE
All pass full compliance: div_diff=0, 11 tabs, parchment base `#f2ede6`, unique accent/primary, UI UX Pro Max palette, Scryfall tooltips (PAD=24, 220px), `← Guides` nav + static brand, header white text `color:#f1f5f9`.

Files: amulet-titan, boros-energy, dimir-oculus, domain-zoo, eldrazi-tron, glockulous, goryos-vengeance, humans, izzet-affinity, jeskai-blink, living-end, neoform, prowess, ruby-storm, uw-blink, uw-control, yawgmoth

### Standard (14 playbooks) — ALL COMPLETE ✅
Full coverage of every archetype above 2% meta share as of April 3, 2026.

| # | File | Meta % | Accent | Primary |
|---|---|---|---|---|
| 1 | izzet-prowess-playbook.html | 10.15% | #5c1a1a | #240a0a |
| 2 | dimir-midrange-playbook.html | 6.15% | #1a3a5c | #0a1724 |
| 3 | mono-green-landfall-playbook.html | ~11% | #1a4a1a | #0a1d0a |
| 4 | boros-aggro-playbook.html | ~2% | #6b2a0a | #2a1004 |
| 5 | jeskai-control-playbook.html | 2.49% | #1a2a5c | #0a1024 |
| 6 | bant-rhythm-playbook.html | 1.82% | #16A34A | #083117 |
| 7 | izzet-lessons-playbook.html | 9.77% | #EA580C | #09183a |
| 8 | dimir-excruciator-playbook.html | 6.81% | #7C3AED | #0a0e28 |
| 9 | izzet-spellementals-playbook.html | 5.26% | #DC2626 | existing |
| 10 | simic-rhythm-playbook.html | 4.11% | #0891B2 | #033a47 |
| 11 | azorius-flash-playbook.html | 3.03% | #60A5FA | #0c1a2e |
| 12 | mono-red-aggro-playbook.html | 3.00% | #EF4444 | #1c0606 |
| 13 | boros-dragons-playbook.html | 2.44% | #D97706 | #1a0b00 |
| 14 | izzet-elementals-playbook.html | 2.87% | #06B6D4 | #042026 |

### deck-guides.html
- Modern tab: 16 decks
- Standard tab: 14 decks
- All deck cards show color identity + meta %

---

## CSS STANDARDS

```css
:root {
  --primary:    [darken accent ~40%];
  --ink:        #0e0e0e;
  --paper:      #f2ede6;   /* ALWAYS parchment — never change */
  --paper-dark: #e8e1d6;
  --rule:       #c8bfb0;
  --accent:     [palette accent];
  --accent-light: rgba([accent], 0.10-0.12);
  --mid:        #5a5248;
  --card:       #ffffff;
}
.header-band { background:var(--primary); border-bottom:3px solid var(--accent); }
.header-band,.header-band * { color:#f1f5f9; }
nav { background:var(--primary); border-bottom:2px solid var(--accent); }
.nav-brand { color:var(--accent); }  /* static div, NOT a link */
.nav-link { color:rgba(248,250,252,0.55); }
.nav-link.active { color:rgba(248,250,252,1); border-bottom-color:var(--accent); }
```

Tooltip JS: PAD=24, W=220, H=310. Function named `showTip`. One IIFE per file.

**Compliance checklist:** div_diff=0, 11 tabs, --primary in :root, --paper=#f2ede6, header white text, nav var(--primary), static brand div, ← Guides link, tooltip CSS+JS (PAD=24), edge-case CSS present.

**Audit regex fix:** Use `id="([a-z]+)" class="section` (no closing quote) to match both `class="section"` and `class="section active"`.

---

## BUG FIXES APPLIED (commit 3117a4f)

- **Tooltip double-image fix:** All 16 Modern files corrected from PAD=16/W=200/H=280 to PAD=24/W=220/H=310 matching CSS.
- **Edge-case CSS fix:** 11 Modern playbooks were missing `.edge-case {}` CSS rules. Added to: boros-energy, domain-zoo, eldrazi-tron, glockulous, izzet-affinity, jeskai-blink, neoform, prowess, ruby-storm, uw-blink, uw-control.

---

## TECHNICAL PATTERNS

**Python patch scripts:** Written to `E:\vscode ai project\My-Website\_r.py`, run via `Desktop Commander:start_process`, deleted before commit.

**Div balance:** MUST be 0 globally.

**Darken formula:** `primary = '#{:02x}{:02x}{:02x}'.format(int(r*0.4), int(g*0.4), int(b*0.4))`

**11-tab structure:** identity, decklist, gameplan, engines, lines, roles, matchups, sideboard, heuristics, tuning, prep

**Commit pattern:** PowerShell semicolons, 30s timeout

---

## METAGAME SNAPSHOT (April 3, 2026 — mtgdecks.net)

1. Mono-Green Landfall ~11%
2. Izzet Prowess 10.15%
3. Izzet Lessons 9.77%
4. Dimir Excruciator 6.81%
5. Dimir Midrange 6.15%
6. Izzet Spellementals 5.26%
7. Simic Rhythm 4.11%
8. Azorius Flash 3.03%
9. Mono-Red Aggro 3.00%
10. Izzet Elementals 2.87%
11. Jeskai Control 2.49%
12. Boros Dragons 2.44%
13. Boros Aggro ~2%
14. Bant Rhythm 1.82%

---

## NEXT SESSION — PIONEER

**Start Pioneer work next session.** Do NOT continue Modern audit queue yet.

### Pioneer approach:
- Pull recent MTGO Pioneer Challenge results (mtgdecks.net / mtgo.com decklists)
- Identify top archetypes by challenge finishes — NO LDXP SEA26 framework (that is Modern-only)
- Same 2%+ meta share threshold as Standard for playbook candidates
- Decide: new Pioneer section on existing site, or separate Pioneer playbook site?
- Establish Pioneer CSS palette scheme (distinct from Standard + Modern visually)

### Outstanding (lower priority):
- Monitor Standard new entrants crossing 2%
- Modern audit queue (LDXP SEA26 — Modern only): Domain Zoo → Eldrazi Tron → Glockulous → Jeskai Blink → Living End → Neoform → Izzet Prowess → Golgari Yawgmoth
- Consider updating Standard meta % values as April RCs produce results
