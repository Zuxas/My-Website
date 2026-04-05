# CLAUDE.md — Team Resolve Project State
*Last updated: April 5, 2026 — commit 96128a9 (PENDING: SB expansion commit)*

---

## PROJECT OVERVIEW

Team Resolve competitive MTG playbook site for Regional Championship prep.

- **Live site:** https://zuxas.github.io/TeamResolve/
- **GitHub:** Zuxas/TeamResolve, branch: main
- **Local:** `E:\vscode ai project\My-Website\`
- **Current clean commit:** `96128a9`

---

## PENDING COMMIT (run this next session to push)

```powershell
cd "E:\vscode ai project\My-Website"
git add -A
git commit -m "SB tab expansion: 19 files upgraded from 8 to 9+ entries

All 44 playbooks now have 9+ SB card explanation entries.
Each new entry covers: mechanics, correct targets, matchup context,
and a Mistake line identifying the most common misplay.

Files updated (8->9 entries):
  azorius-flash, boros-dragons, dimir-excruciator, goryos-vengeance,
  izzet-elementals, izzet-lessons, izzet-spellementals, lotus-field,
  mono-red-aggro, orzhov-greasefang, rdw-pioneer, selesnya-company,
  simic-rhythm, ur-cutter, uw-control-pioneer, arclight-phoenix,
  mono-white-humans-pioneer, temur-landfall (8->9 each)
  uw-control (8->10)

All 44 files: div=0, 44/44 PASS on all quality criteria"
git push origin main
```

---

## SITE STRUCTURE — 44 PLAYBOOKS TOTAL

### Modern (17) — ALL COMPLETE ✅
amulet-titan, boros-energy, dimir-oculus, domain-zoo, eldrazi-tron, glockulous,
goryos-vengeance, humans, izzet-affinity, jeskai-blink, living-end, neoform,
prowess, ruby-storm, uw-blink, uw-control, yawgmoth

### Standard (16) — ALL COMPLETE ✅
Mono Green Landfall · Izzet Prowess · Izzet Lessons · Dimir Excruciator
Dimir Midrange · Izzet Spellementals · Simic Rhythm · Mono-Red Aggro
Azorius Flash · Izzet Elementals · Jeskai Control · Boros Dragons
Temur Landfall · Rakdos Monument · Bant Rhythm · Boros Aggro

### Pioneer (11) — ALL COMPLETE ✅
UR Cutter · Greasefang · RDW · Selesnya Company · UW Control
Arclight Phoenix · Lotus Field · Izzet Creativity · Niv-Mizzet Reborn
Rakdos Boomer · Mono-White Humans

---

## QUALITY METRICS (post-pending commit)

All 44 files pass ALL criteria:
- div balance = 0 ✅
- ≥800 lines ✅
- you/they ratio ≥1.4 ✅
- SB tab ≥9 card explanations ✅
- Tuning section ≥3 entries ✅
- Prep: print-mu grid ✅
- Prep: 20-min crash course checklist ✅
- Prep: testing framework ✅
- Prep: matchday routine ✅
- SB plans ≥10 matchups, balanced ins=outs ✅

---

## RECENT COMMITS (this session)

| Commit | Work |
|---|---|
| `ea59544` | Matchup depth expansion: 7 thin Pioneer/Standard files |
| `167216d` | Meta refresh (modern-meta.json, meta.html) + glockulous SB |
| `e16d412` | deck-guides meta % refresh + copyright year fixes |
| `919cf96` | Tuning section expansion: 5 playbooks, 22 new tuning cards |
| `96128a9` | Tuning section expansion: 11 more playbooks, 55 new tuning cards |
| PENDING | SB tab expansion: 19 files → 9+ entries |

---

## META SNAPSHOT (April 5, 2026)

### Modern (mtgdecks.net, last 2 months)
Boros Energy 16.37% · Izzet Affinity 8.68% · Jeskai Blink 7.60%
Eldrazi Tron 6.38% · Ruby Storm 4.60% · Izzet Prowess 3.99%
Amulet Titan 3.85% · Domain Aggro 3.72% · Esper Reanimator 3.33%
Living End 2.63% · Esper Blink 2.50% · Simic Neoform 2.45%
Dimir Control 2.44% · Golgari Yawgmoth 1.73%

### Standard (mtgdecks.net, last 2 months)
Mono Green Landfall 11.45% · Izzet Prowess 10.28% · Izzet Lessons 9.78%
Dimir Excruciator 6.75% · Dimir Midrange 6.09% · Izzet Spellementals 5.22%
Simic Rhythm 4.11% · Mono-Red Aggro 3.00% · Azorius Flash 3.00%
Izzet Elementals 2.88% · Jeskai Control 2.48% · Boros Dragons 2.42%
Temur Landfall 2.11% · Rakdos Monument 1.99% · Bant Rhythm 1.92%

---

## CSS STANDARDS

:root variables, nav structure, header-band pattern — unchanged from prior CLAUDE.md.
Audit script pattern — unchanged.
Python patch scripts → `_a.py`, run via DC start_process (powershell, 6-8s), deleted after.
Commit: `git add -A ; git commit -m "..." ; git push origin main` — 25s timeout.
