# CLAUDE.md — Team Resolve Project State
*Last updated: April 5, 2026 — commit 5957225*

## PROJECT
- Live: https://zuxas.github.io/TeamResolve/
- Repo: Zuxas/TeamResolve, branch: main
- Local: E:\vscode ai project\My-Website\
- Current commit: 5957225

## SITE — 44 PLAYBOOKS, ALL COMPLETE
Modern (17): amulet-titan, boros-energy, dimir-oculus, domain-zoo, eldrazi-tron,
glockulous, goryos-vengeance, humans, izzet-affinity, jeskai-blink, living-end,
neoform, prowess, ruby-storm, uw-blink, uw-control, yawgmoth

Standard (16): Mono Green Landfall, Izzet Prowess, Izzet Lessons, Dimir Excruciator,
Dimir Midrange, Izzet Spellementals, Simic Rhythm, Mono-Red Aggro, Azorius Flash,
Izzet Elementals, Jeskai Control, Boros Dragons, Temur Landfall, Rakdos Monument,
Bant Rhythm, Boros Aggro

Pioneer (11): UR Cutter, Greasefang, RDW, Selesnya Company, UW Control,
Arclight Phoenix, Lotus Field, Izzet Creativity, Niv-Mizzet Reborn,
Rakdos Boomer, Mono-White Humans

## QUALITY — 44/44 PASSING ALL CRITERIA
div=0, lines>=800, ratio>=1.4, SB>=9 entries, tuning>=3 entries,
prep: print-mu + checklist + testing + matchday, SB plans>=10 balanced

## RECENT COMMITS
ea59544 — Matchup depth expansion (7 thin files)
167216d — Meta refresh (modern-meta.json + meta.html + glockulous SB)
e16d412 — deck-guides meta % refresh + copyright year fixes
919cf96 — Tuning expansion (5 playbooks)
96128a9 — Tuning expansion (11 more playbooks)
5957225 — SB tab expansion: 19 files to 9+ entries [CURRENT]

## NEXT OPTIONS
1. Matchup depth: 7 Pioneer files at ~155 MU lines (passing but could be richer)
2. SB entries: some files at exactly 9, could push to 10+
3. Ratio buffer: a few files at exactly 1.4
4. New decks: monitor for new archetypes crossing 2% in any format

## META (April 5, 2026)
Modern (mtgdecks.net): Boros Energy 16.37%, Izzet Affinity 8.68%, Jeskai Blink 7.60%,
Eldrazi Tron 6.38%, Ruby Storm 4.60%, Izzet Prowess 3.99%, Amulet Titan 3.85%,
Domain Aggro 3.72%, Esper Reanimator 3.33%, Living End 2.63%, Neoform 2.45%,
Yawgmoth 1.73%

Standard (mtgdecks.net): Mono Green 11.45%, Izzet Prowess 10.28%, Izzet Lessons 9.78%,
Dimir Excruciator 6.75%, Dimir Midrange 6.09%, Izzet Spellementals 5.22%,
Simic Rhythm 4.11%, Azorius Flash 3.00%, Mono-Red 3.00%, Izzet Elementals 2.88%,
Jeskai Control 2.48%, Boros Dragons 2.42%, Temur Landfall 2.11%, Bant Rhythm 1.92%

## TECHNICAL
- Scripts: write _a.py, run via DC start_process powershell, delete after
- Commit: git add -A ; git commit -m "..." ; git push origin main (25s timeout)
- Keep sessions short — one commit per session to avoid context window errors
