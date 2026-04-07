# CLAUDE.md — Team Resolve Project State
*Last updated: April 7, 2026 — commit 75a9296*

## PROJECT
- Live: https://zuxas.github.io/TeamResolve/
- Repo: Zuxas/TeamResolve, branch: main
- Local: E:\vscode ai project\My-Website\
- Current commit: 75a9296

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

## LDXP SEA26 AUDIT — ALL 8 QUEUE DECKS PASS (April 7, 2026)
Criteria: SB plans>=10 balanced, card entries>=6, print-mu grid present
Domain Zoo:       PASS | plans=11, cards=17, print-mu=✅, balance=✅
Eldrazi Tron:     PASS | plans=12, cards=16, print-mu=✅, balance=✅
Glockulous:       PASS | plans=11, cards=16, print-mu=✅, balance=✅
Jeskai Blink:     PASS | plans=11, cards=18, print-mu=✅, balance=✅
Living End:       PASS | plans=11, cards=16, print-mu=✅, balance=✅
Neoform:          PASS | plans=11, cards=20, print-mu=✅, balance=✅
Izzet Prowess:    PASS | plans=11, cards=17, print-mu=✅, balance=✅
Golgari Yawgmoth: PASS | plans=11, cards=16, print-mu=✅, balance=✅

## INDEX.HTML — COMPLETE (April 7, 2026)
All visual fixes committed:
- Logo: tight-cropped transparent PNG (brightness-as-alpha)
- Hero: outside main, renders against body bg image
- Stat bar: count-up animation on scroll, 44/3/5/40
- Cards: glassmorphic, high contrast bg rgba(20,24,40,0.85)
- Conclusion: white text var(--text), gold CTA link var(--gold)
- Footer: spans at var(--text-muted), dark navy bg
- Back-to-top: z-index 9999, bottom-left, no footer clip
- Tab title: &mdash; entity (renders as —)
- Section spacing: 28px margins throughout

## QUALITY — 44/44 PASSING ALL CRITERIA
div=0, lines>=800, ratio>=1.4, SB>=9 entries, tuning>=3 entries,
prep: print-mu + checklist + testing + matchday, SB plans>=10 balanced

## RECENT COMMITS
75a9296 — index: fix inline style conclusion color + link to gold [CURRENT]
aba28d6 — index: fix footer + conclusion visibility, gold CTA link
3c08bae — index: increase card contrast, tighten column + card padding
0aec7d8 — index: tighten section spacing, fix dead grey space
dd07bad — index: fix tab title encoding, back-to-top z-index

## NEXT OPTIONS
1. Apply meta % updates to Standard playbooks (numbers captured April 5)
2. Matchup depth: 7 Pioneer files at ~155 MU lines (passing but could be richer)
3. Monitor for new archetypes crossing 2% in any format

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
- Encoding: open files with encoding='utf-8', use sys.stdout.reconfigure(encoding='utf-8')
- SB balance bug: regex r'sb-out[^>]*>.*?(\d+)' is BUGGY — use row-by-row parsing instead
- Index inline styles override styles.css — always check both when color isn't applying
