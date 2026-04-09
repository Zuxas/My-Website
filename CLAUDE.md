# CLAUDE.md — Team Resolve Project State
*Last updated: April 9, 2026 — commit 33ceec6*

> **Cross-project context:** See `E:\vscode ai project\ECOSYSTEM.md` for how this
> project connects to mtg-sim, mtg-meta-analyzer, and Team Resolve operations.

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

## MODERN META % — UPDATED (April 9, 2026)
All 17 Modern files updated with MTGGoldfish paper meta % (all decks, 14-day):
Boros Energy 17.3%, Ruby Storm 8.2%, Affinity 5.7%, Eldrazi Tron 5.6%,
Jeskai Blink 5.4%, Domain Zoo 4.8%, Amulet Titan 3.4%, Dimir Oculus 3.4%,
Living End 3.2%, Neoform 2.9%, Yawgmoth 2.6%, Goryo's Vengeance 2.5%,
Izzet Prowess 2.5%, Humans 1.0%, UW Blink 1.0%, UW Control 0.8%, Glockulous 0.5%

## PIONEER META % — UPDATED (April 9, 2026)
All 11 Pioneer files updated with MTGGoldfish paper meta % (all decks):
RDW 20.4%, UR Cutter 10.0%, Selesnya Company 9.4%, UW Control 9.2%,
Orzhov Greasefang 5.3%, Arclight Phoenix 4.2%, Izzet Control 0.5%,
Lotus Field 0.5%, Rakdos Midrange 0.5%, Mono-White Humans 0.3%,
Niv-Mizzet Reborn 0.3%

## QUALITY — 44/44 PASSING ALL CRITERIA

## RECENT COMMITS
33ceec6 — meta: update all 11 Pioneer playbooks with April 2026 meta %
f75e33f — meta: update all 17 Modern playbooks with April 2026 meta %
ce110f5 — docs: add ECOSYSTEM.md cross-reference
7b86f07 — refactor: reorganize all 44 playbooks into format folders

## TECHNICAL
- Scripts: write _a.py, run via DC start_process powershell, delete after
- Commit: git add -A ; git commit -m "..." ; git push origin main (25s timeout)
- Encoding: open files with encoding='utf-8', sys.stdout.reconfigure(encoding='utf-8')
- SB balance check: use row-by-row parsing, NOT r'sb-out[^>]*>.*?(\d+)' (buggy)
- Inline <style> overrides external CSS — check both when colors don't apply
- NEW: All playbook paths now have format prefix (modern/, standard/, pioneer/)
