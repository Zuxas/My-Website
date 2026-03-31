#!/usr/bin/env python3
"""
playbook_audit.py — Team Resolve Site Tools
============================================
Consolidated audit for all 14 Modern playbooks.

Usage:
    python tools/playbook_audit.py           # full audit
    python tools/playbook_audit.py --back    # check ← Guides button only
    python tools/playbook_audit.py --decks   # decklist cards only
    python tools/playbook_audit.py --stale   # stale card check only
"""
import sys, re, os, glob, argparse

sys.stdout.reconfigure(encoding='utf-8')
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# ── Verified LDXP reference lists ────────────────────────────────────────────
VERIFIED = {
    'amulet-titan':    {'source': 'aljce 13-1-2 + Devon Straub PTQ (LDXP SEA26)',
                        'melee': 'https://melee.gg/Decklist/View/2a4efd5e-3fcd-45d1-86bf-b41a0128ba82',
                        'keys': ['Arboreal Grazer','Primeval Titan','Scapeshift','Amulet of Vigor','Spelunking','Malevolent Rumble','Green Sun']},
    'boros-energy':    {'source': 'No LDXP ref pinned — cards look current',
                        'melee': None,
                        'keys': ['Ragavan','Ocelot Pride','Guide of Souls','Phlage','Ajani','Galvanic Discharge']},
    'domain-zoo':      {'source': 'No LDXP ref pinned — cards look current',
                        'melee': None,
                        'keys': ['Scion of Draco','Territorial Kavu','Doorkeeper Thrull','Phlage']},
    'eldrazi-tron':    {'source': 'No LDXP ref pinned — cards look current',
                        'melee': None,
                        'keys': ['Thought-Knot Seer','Sowing Mycospawn','Karn, the Great Creator']},
    'glockulous':      {'source': 'No LDXP ref pinned — cards look current',
                        'melee': None,
                        'keys': ['Psychic Frog','Emperor of Bones','Archon of Cruelty','Persist']},
    'izzet-affinity':  {'source': 'Jeffrey Chang 10-0-4 (LDXP SEA26)',
                        'melee': 'https://melee.gg/Decklist/View/f8e13375-d4ff-44dc-956b-b41b0052c321',
                        'keys': ['Kappa Cannoneer','Pinnacle Emissary','Weapons Manufacturing','Engineered Explosives','Mox Opal','Emry','Arcbound Ravager','Sink into Stupor','Metallic Rebuke']},
    'jeskai-blink':    {'source': 'Connor Mackenzie 9-0-4 (LDXP SEA26)',
                        'melee': 'https://melee.gg/Decklist/View/8dad6cf1-a10c-4fae-94aa-b41b001ae110',
                        'keys': ['Phelia','Phlage','Quantum Riddler','Ragavan','Solitude','Casey Jones','Consign to Memory','Galvanic Discharge','Ephemerate','Arena of Glory']},
    'living-end':      {'source': 'No LDXP ref pinned — cards look current',
                        'melee': None,
                        'keys': ['Living End','Violent Outburst','Street Wraith','Overlord of the Balemurk','Force of Negation']},
    'neoform':         {'source': 'No LDXP ref pinned — cards look current',
                        'melee': None,
                        'keys': ['Allosaurus Rider','Neoform','Ghalta','Summoner\'s Pact','Consign to Memory']},
    'prowess':         {'source': 'No LDXP ref pinned — cards look current',
                        'melee': None,
                        'keys': ['Dragon\'s Rage Channeler','Monastery Swiftspear','Slickshot Show-Off','Cori-Steel Cutter','Lava Dart']},
    'ruby-storm':      {'source': 'Chance McDougal 9-0-4 (LDXP SEA26)',
                        'melee': 'https://melee.gg/Decklist/View/5b97bdff-bc1f-4e37-8255-b419010af481',
                        'keys': ['Ruby Medallion','Ral, Monsoon Mage','Desperate Ritual','Manamorphose','Pyretic Ritual','Past in Flames','Artist\'s Talent','Heroes\' Hangout','Romantic Rendezvous']},
    'uw-blink':        {'source': 'Team Resolve internal — pre-LDXP shell (intentional)',
                        'melee': None,
                        'keys': ['Phelia','Ephemerate','Solitude','White Orchid Phantom']},
    'uw-control':      {'source': 'Evariel 8-0-2 (LDXP SEA26 PTQ)',
                        'melee': 'https://melee.gg/Decklist/View/a6a4917b-1556-4e52-8a55-b4190176e8fe',
                        'keys': ['Narset, Parter of Veils','Teferi, Time Raveler','Orim\'s Chant','Isochron Scepter','Wrath of the Skies','Tune the Narrative','Stock Up','Day\'s Undoing','Wan Shi Tong']},
    'yawgmoth':        {'source': 'No LDXP ref pinned — cards look current',
                        'melee': None,
                        'keys': ['Yawgmoth, Thran Physician','Melira','Blood Artist','Young Wolf','Collected Company','Chord of Calling']},
}


def get_decklist_cards(html):
    dl = re.search(r'id="decklist"(.*?)(?:id="gameplan"|id="engines"|GAMEPLAN|GAME FLOW)', html, re.DOTALL)
    if not dl:
        return []
    rows = re.findall(r'<div class="dl-card-row">.*?</div>', dl.group(0))
    cards = []
    for r in rows:
        name = re.sub(r'<[^>]+>', '', r.split('<span class="dl-qty">')[0] if '<span class="dl-qty">' in r else r).strip()
        qty_m = re.search(r'dl-qty">(.*?)</span>', r)
        qty = qty_m.group(1) if qty_m else '?'
        if name:
            cards.append((name, qty))
    return cards


def audit_all(check_back=True, check_decks=True, check_stale=True):
    playbooks = sorted(glob.glob(os.path.join(BASE, '*-playbook.html')))
    
    print('=' * 70)
    print('TEAM RESOLVE PLAYBOOK AUDIT')
    print('=' * 70)

    summary = {'ok': 0, 'warn': 0, 'ref_needed': 0}

    for path in playbooks:
        fname = os.path.basename(path)
        deck_key = fname.replace('-playbook.html', '')
        ref = VERIFIED.get(deck_key, {})

        with open(path, encoding='utf-8') as f:
            html = f.read()

        issues = []

        # ── Back button check ─────────────────────────────────────────────
        if check_back:
            if 'deck-guides.html' not in html:
                issues.append('MISSING ← Guides back button')

        # ── Decklist card check ───────────────────────────────────────────
        if check_decks and ref.get('keys'):
            cards = get_decklist_cards(html)
            card_names = ' '.join(c[0].lower() for c in cards)
            missing = [k for k in ref['keys'] if k.lower() not in card_names]
            if missing:
                issues.append(f'MISSING KEY CARDS: {missing}')

        # ── Melee link check ──────────────────────────────────────────────
        if check_decks and ref.get('melee') and ref['melee'] not in html:
            issues.append('MISSING melee.gg link in decklist')

        # ── Stale card check ──────────────────────────────────────────────
        if check_stale:
            dl_section = re.search(r'id="decklist".*?(?:id="gameplan"|id="engines")', html, re.DOTALL)
            dl_text = dl_section.group(0) if dl_section else ''
            STALE = ['Snapcaster Mage','Memory Deluge','Archmage\'s Charm','Dress Down',
                     'Dovin\'s Veto','Stony Silence','Counterspell'] if deck_key not in ['uw-control'] else []
            stale_found = [s for s in STALE if s in dl_text]
            if stale_found:
                issues.append(f'STALE CARDS IN DECKLIST: {stale_found}')

        # ── Status line ───────────────────────────────────────────────────
        has_melee_link = bool(ref.get('melee'))
        melee_in_file = has_melee_link and ref['melee'] in html

        if issues:
            status = '⚠️ '
            summary['warn'] += 1
        elif not has_melee_link:
            status = '📋'
            summary['ref_needed'] += 1
        else:
            status = '✅'
            summary['ok'] += 1

        print(f'\n{status} {fname}')
        print(f'   Source : {ref.get("source","Unknown")}')
        print(f'   Melee  : {"✓ linked" if melee_in_file else ("no ref" if not has_melee_link else "LINK MISSING FROM FILE")}')

        # Show card count
        cards = get_decklist_cards(html)
        print(f'   Cards  : {len(cards)} dl-card-row entries')

        for issue in issues:
            print(f'   ❌ {issue}')

    print('\n' + '=' * 70)
    print(f'SUMMARY: {summary["ok"]} verified | {summary["ref_needed"]} needs LDXP ref | {summary["warn"]} has issues')
    print('=' * 70)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Team Resolve playbook audit tool')
    parser.add_argument('--back',  action='store_true', help='Check back button only')
    parser.add_argument('--decks', action='store_true', help='Check decklists only')
    parser.add_argument('--stale', action='store_true', help='Check stale cards only')
    args = parser.parse_args()

    if args.back or args.decks or args.stale:
        audit_all(check_back=args.back, check_decks=args.decks, check_stale=args.stale)
    else:
        audit_all()
