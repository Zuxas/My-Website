# CLAUDE.md — Team Resolve Project State
*Last updated: April 8, 2026 — commit 7b86f07*

## PROJECT
- Live: https://zuxas.github.io/TeamResolve/
- Repo: Zuxas/TeamResolve, branch: main
- Local: E:\vscode ai project\My-Website\
- Current commit: 7b86f07

## FOLDER STRUCTURE (reorganized April 8, 2026)
Root: index.html, deck-guides.html, meta.html, team.html, analyze.html,
      deckbuilding.html, planning.html, bio.html, styles.css, images/

modern/  (17): amulet-titan, boros-energy, dimir-oculus, domain-zoo,
               eldrazi-tron, glockulous, goryos-vengeance, humans,
               izzet-affinity, jeskai-blink, living-end, neoform,
               prowess, ruby-storm, uw-blink, uw-control, yawgmoth

standard/ (16): azorius-flash, bant-rhythm, boros-aggro, boros-dragons,
                dimir-excruciator, dimir-midrange, izzet-elementals,
                izzet-lessons, izzet-prowess, izzet-spellementals,
                jeskai-control, mono-green-landfall, mono-red-aggro,
                rakdos-monument, simic-rhythm, temur-landfall

pioneer/ (11): arclight-phoenix, izzet-control-pioneer, lotus-field,
               mono-white-humans-pioneer, niv-mizzet-reborn,
               orzhov-greasefang, rakdos-midrange-pioneer, rdw-pioneer,
               selesnya-company, ur-cutter, uw-control-pioneer

legacy/   (0 — empty, ready)
pauper/   (0 — empty, ready)
premodern/(0 — empty, ready)

## LINK PATTERNS (IMPORTANT after reorganization)
- From playbook to root: href="../index.html", href="../styles.css"
- From playbook to same format: href="other-playbook.html"
- From playbook to other format: href="../modern/other-playbook.html"
- From root to playbook: href="modern/domain-zoo-playbook.html"

## LDXP SEA26 AUDIT — ALL 8 QUEUE DECKS PASS (April 7, 2026)
Domain Zoo: PASS | Eldrazi Tron: PASS | Glockulous: PASS
Jeskai Blink: PASS | Living End: PASS | Neoform: PASS
Izzet Prowess: PASS | Golgari Yawgmoth: PASS

## STANDARD META % — UPDATED (April 8, 2026)
All 16 Standard files updated with April 5 meta %:
Mono-Green 11.45%, Izzet Prowess 10.28%, Izzet Lessons 9.78%,
Dimir Excruciator 6.75%, Dimir Midrange 6.09%, Izzet Spellementals 5.22%,
Simic Rhythm 4.11%, Azorius Flash 3.00%, Mono-Red 3.00%,
Izzet Elementals 2.88%, Jeskai Control 2.48%, Boros Dragons 2.42%,
Temur Landfall 2.11%, Bant Rhythm 1.92%, Rakdos Monument 1.20%, Boros Aggro 1.00%

## QUALITY — 44/44 PASSING ALL CRITERIA

## RECENT COMMITS
7b86f07 — refactor: reorganize all 44 playbooks into format folders [CURRENT]
28f1b1a — docs: CLAUDE.md audit complete
75a9296 — index: fix inline style conclusion color + link to gold
aba28d6 — index: fix footer + conclusion visibility

## TECHNICAL
- Scripts: write _a.py, run via DC start_process powershell, delete after
- Commit: git add -A ; git commit -m "..." ; git push origin main (25s timeout)
- Encoding: open files with encoding='utf-8', sys.stdout.reconfigure(encoding='utf-8')
- SB balance check: use row-by-row parsing, NOT r'sb-out[^>]*>.*?(\d+)' (buggy)
- Inline <style> overrides external CSS — check both when colors don't apply
- NEW: All playbook paths now have format prefix (modern/, standard/, pioneer/)
