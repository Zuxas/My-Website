"""
wrap_cards.py — wraps all MTG card name references with <span class="c">Name</span>
Processes all playbook HTML files in the My-Website directory.
Only wraps bare text occurrences — not ones already inside class="c" spans,
not ones inside HTML tags, and not ones inside <script> or <style> blocks.
"""

import re
import os

BASE = r"E:\vscode ai project\My-Website"

# Every card name that appears across any of the 5 playbooks
CARDS = [
    # Boros Energy core
    "Ragavan, Nimble Pilferer",
    "Ocelot Pride",
    "Guide of Souls",
    "Phlage, Titan of Fire's Fury",
    "Ajani, Nacatl Pariah", "Ajani, Nacatl Avenger",
    "Galvanic Discharge",
    "Goblin Bombardment",
    "Static Prison",
    "Thraben Charm",
    "Voice of Victory",
    # Boros SB
    "Surgical Extraction",
    "Celestial Purge",
    "Blood Moon",
    "Wrath of the Skies",
    "Deafening Silence",
    "High Noon",
    "Vexing Bauble",
    "Meltdown",
    "Wear // Tear",
    "Clarion Conqueror",
    "The Legend of Roku",
    # Jeskai Blink core
    "Phelia, Exuberant Shepherd",
    "White Orchid Phantom",
    "Starfield Shepherd",
    "Quantum Riddler",
    "Sanctifier en-Vec",
    "Witch Enchanter",
    "Mockingbird",
    "Solitude",
    "Ephemerate",
    "Consign to Memory",
    "Prismatic Ending",
    # Jeskai SB
    "Teferi, Time Raveler",
    "Mistcaller",
    "Rest in Peace",
    "Pithing Needle",
    "Stony Silence",
    "Orim's Chant",
    "Meticulous Archive",
    # Glockulous core
    "Psychic Frog",
    "Abhorrent Oculus",
    "Emperor of Bones",
    "Archon of Cruelty",
    "Troll of Khazad-dûm",
    "Faithless Looting",
    "Thought Scour",
    "Thoughtseize",
    "Fatal Push",
    "Persist",
    "Unearth",
    "Spell Pierce",
    # Glockulous SB
    "Harbinger of the Seas",
    "Mystical Dispute",
    "Nihil Spellbomb",
    "Pyroclasm",
    "Harvester of Misery",
    "Surgical Extraction",
    # Prowess core
    "Monastery Swiftspear",
    "Dragon's Rage Channeler",
    "Cori-Steel Cutter",
    "Lava Dart",
    "Lightning Bolt",
    "Mutagenic Growth",
    "Manamorphose",
    "Consider",
    "Sleight of Hand",
    "Mishra's Bauble",
    "Gut Shot",
    # Lands
    "Sacred Foundry",
    "Arid Mesa",
    "Sunbaked Canyon",
    "Inspiring Vantage",
    "Flooded Strand",
    "Hallowed Fountain",
    "Steam Vents",
    "Bloodstained Mire",
    "Watery Grave",
    "Blood Crypt",
    "Scalding Tarn",
    "Polluted Delta",
    "Raucous Theater",
    "Undercity Sewers",
    # Amulet Titan
    "Primeval Titan",
    "Amulet of Vigor",
    "Summoner's Pact",
    "Slayers' Stronghold",
    "Simic Growth Chamber",
    "Tolaria West",
    # UW Control
    "Counterspell",
    "Supreme Verdict",
    "Snapcaster Mage",
    "Jace, the Mind Sculptor",
    "Teferi, Hero of Dominaria",
    "Spell Snare",
    "Archmage's Charm",
    "Memory Deluge",
    "Dress Down",
    "Dovin's Veto",
    "Path to Exile",
    "Slickshot Show-Off",
    "Murktide Regent",
    # Izzet Affinity core
    "Pinnacle Emissary",
    "Kappa Cannoneer",
    "Weapons Manufacturing",
    "Engineered Explosives",
    "Mox Opal",
    "Mishra's Bauble",
    "Emry, Lurker of the Loch",
    "Arcbound Ravager",
    "Metallic Rebuke",
    "Thoughtcast",
    "Sink into Stupor",
    "Claws of Gix",
    "Tormod's Crypt",
    "Springleaf Drum",
    "Thought Monitor",
    "Ravenous Robots",
    "Krang, Master Mind",
    "Haywire Mite",
    "Shadowspear",
    "Damping Sphere",
    "Whipflare",
    "Galvanic Blast",
    "Welding Jar",
    "Urza's Saga",
    "Skateboard",
    # General
    "Force of Negation",
    "Chalice of the Void",
    "Leyline of the Void",
    "Consign to Memory",
    "Mystical Dispute",
    "Blood Moon",
    # Ruby Storm core
    "Ruby Medallion",
    "Ral, Monsoon Mage",
    "Desperate Ritual",
    "Pyretic Ritual",
    "Manamorphose",
    "Past in Flames",
    "Reckless Impulse",
    "Wrenn's Resolve",
    "Glimpse the Impossible",
    "Wish",
    "Grapeshot",
    "Empty the Warrens",
    "Strike It Rich",
    "Orim's Chant",
    "Valakut Awakening",
    "Galvanic Relay",
    "Gemstone Caverns",
    # Eldrazi Tron core
    "Karn, the Great Creator",
    "Ugin, Eye of the Storms",
    "Thought-Knot Seer",
    "Sowing Mycospawn",
    "Devourer of Destiny",
    "Ulamog, the Ceaseless Hunger",
    "Ugin's Labyrinth",
    "Expedition Map",
    "Kozilek's Command",
    "Dismember",
    "Relic of Progenitus",
    "All Is Dust",
    "Ensnaring Bridge",
    "Chalice of the Void",
    "Trinisphere",
    "Walking Ballista",
    "Torpor Orb",
    "Warping Wail",
    "Talisman of Resilience",
    # Amulet Titan core
    "Amulet of Vigor",
    "Primeval Titan",
    "Arboreal Grazer",
    "Dryad of the Ilysian Grove",
    "Summoner's Pact",
    "Cultivator Colossus",
    "Spelunking",
    "Valakut, the Molten Pinnacle",
    "Force of Vigor",
    "Defense Grid",
    "Cursed Totem",
    "Bojuka Bog",
]

# Sort longest first so "Ragavan, Nimble Pilferer" matches before "Ragavan"
CARDS_SORTED = sorted(set(CARDS), key=lambda x: -len(x))

PLAYBOOKS = [
    "boros-energy-playbook.html",
    "jeskai-blink-playbook.html",
    "prowess-playbook.html",
    "glockulous-playbook.html",
    "uw-control-playbook.html",
    "izzet-affinity-playbook.html",
    "ruby-storm-playbook.html",
    "eldrazi-tron-playbook.html",
    "amulet-titan-playbook.html",
]

def wrap_cards_in_html(html):
    """
    Walk through the HTML, skip <style>, <script>, and tag interiors,
    and in text nodes wrap card names with <span class="c">Name</span>.
    """
    result = []
    i = 0
    n = len(html)

    # Already-wrapped pattern — don't re-wrap
    already_wrapped = re.compile(r'class="c"')

    while i < n:
        # Skip <style>...</style>
        if html[i:i+7].lower() == '<style>':
            end = html.lower().find('</style>', i)
            if end == -1: end = n - 8
            result.append(html[i:end+8])
            i = end + 8
            continue

        # Skip <script>...</script>
        if html[i:i+7].lower() == '<script':
            end = html.lower().find('</script>', i)
            if end == -1: end = n - 9
            result.append(html[i:end+9])
            i = end + 9
            continue

        # Skip any HTML tag
        if html[i] == '<':
            end = html.find('>', i)
            if end == -1: end = n - 1
            result.append(html[i:end+1])
            i = end + 1
            continue

        # Text node — find the next tag
        end = html.find('<', i)
        if end == -1: end = n
        text = html[i:end]

        # Wrap card names in this text segment
        for card in CARDS_SORTED:
            # Skip if already inside a span.c — we check the surrounding context
            pattern = re.compile(r'(?<!["\w])' + re.escape(card) + r'(?!["\w])')
            replacement = f'<span class="c">{card}</span>'
            text = pattern.sub(replacement, text)

        result.append(text)
        i = end

    return ''.join(result)

for fname in PLAYBOOKS:
    fpath = os.path.join(BASE, fname)
    if not os.path.exists(fpath):
        print(f"SKIP (not found): {fname}")
        continue

    with open(fpath, 'r', encoding='utf-8') as f:
        original = f.read()

    # Don't re-process files that already have c spans
    if 'class="c"' in original:
        print(f"SKIP (already processed): {fname}")
        continue

    processed = wrap_cards_in_html(original)

    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(processed)

    # Count wraps
    count = processed.count('class="c"')
    print(f"OK: {fname} — {count} card references wrapped")

print("Done.")
