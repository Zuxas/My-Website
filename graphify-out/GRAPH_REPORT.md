# Graph Report - E:\vscode ai project\My-Website  (2026-04-10)

## Corpus Check
- 56 files · ~1,792,712 words
- Verdict: corpus is large enough that graph structure adds value.

## Summary
- 37 nodes · 28 edges · 14 communities detected
- Extraction: 100% EXTRACTED · 0% INFERRED · 0% AMBIGUOUS
- Token cost: 0 input · 0 output

## God Nodes (most connected - your core abstractions)
1. `patchTable()` - 3 edges
2. `createTooltip()` - 2 edges
3. `showTooltip()` - 2 edges
4. `positionTooltip()` - 2 edges
5. `init()` - 2 edges
6. `verdictClass()` - 2 edges
7. `verdictText()` - 2 edges
8. `get_decklist_cards()` - 2 edges
9. `audit_all()` - 2 edges
10. `wrap_cards_in_html()` - 2 edges

## Surprising Connections (you probably didn't know these)
- None detected - all connections are within the same source files.

## Communities

### Community 0 - "Community 0"
Cohesion: 0.28
Nodes (4): createTooltip(), init(), positionTooltip(), showTooltip()

### Community 1 - "Community 1"
Cohesion: 0.6
Nodes (3): patchTable(), verdictClass(), verdictText()

### Community 2 - "Community 2"
Cohesion: 0.5
Nodes (3): wrap_cards.py — wraps all MTG card name references with <span class="c">Name</sp, Walk through the HTML, skip <style>, <script>, and tag interiors,     and in tex, wrap_cards_in_html()

### Community 3 - "Community 3"
Cohesion: 0.67
Nodes (0): 

### Community 4 - "Community 4"
Cohesion: 1.0
Nodes (2): audit_all(), get_decklist_cards()

### Community 5 - "Community 5"
Cohesion: 1.0
Nodes (1): Add edge cases sections to eldrazi-tron, ruby-storm, and uw-blink playbooks. Eac

### Community 6 - "Community 6"
Cohesion: 1.0
Nodes (0): 

### Community 7 - "Community 7"
Cohesion: 1.0
Nodes (0): 

### Community 8 - "Community 8"
Cohesion: 1.0
Nodes (0): 

### Community 9 - "Community 9"
Cohesion: 1.0
Nodes (0): 

### Community 10 - "Community 10"
Cohesion: 1.0
Nodes (0): 

### Community 11 - "Community 11"
Cohesion: 1.0
Nodes (0): 

### Community 12 - "Community 12"
Cohesion: 1.0
Nodes (0): 

### Community 13 - "Community 13"
Cohesion: 1.0
Nodes (0): 

## Knowledge Gaps
- **3 isolated node(s):** `Add edge cases sections to eldrazi-tron, ruby-storm, and uw-blink playbooks. Eac`, `wrap_cards.py — wraps all MTG card name references with <span class="c">Name</sp`, `Walk through the HTML, skip <style>, <script>, and tag interiors,     and in tex`
  These have ≤1 connection - possible missing edges or undocumented components.
- **Thin community `Community 5`** (2 nodes): `_patch_edges_3files.py`, `Add edge cases sections to eldrazi-tron, ruby-storm, and uw-blink playbooks. Eac`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 6`** (2 nodes): `_patch_et1.py`, `sec_bounds()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 7`** (2 nodes): `wrap_dive_cards.py`, `wrap_card()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 8`** (2 nodes): `wrap_new_cards.py`, `wrap_card()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 9`** (1 nodes): `_decode_tien.py`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 10`** (1 nodes): `_sb_cards.py`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 11`** (1 nodes): `_update_meta_pcts.py`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 12`** (1 nodes): `fetch_oracle.py`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 13`** (1 nodes): `site_audit.py`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **What connects `Add edge cases sections to eldrazi-tron, ruby-storm, and uw-blink playbooks. Eac`, `wrap_cards.py — wraps all MTG card name references with <span class="c">Name</sp`, `Walk through the HTML, skip <style>, <script>, and tag interiors,     and in tex` to the rest of the system?**
  _3 weakly-connected nodes found - possible documentation gaps or missing edges._