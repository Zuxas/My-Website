import urllib.request, json, time

CARDS = [
    "Psychic Frog",
    "Emperor of Bones",
    "Harbinger of the Seas",
    "Troll of Khazad-dum",
    "Archon of Cruelty",
    "Thoughtseize",
    "Fatal Push",
    "Thought Scour",
    "Faithless Looting",
    "Persist",
    "Unearth",
    "Nihil Spellbomb",
    "Mystical Dispute",
    "Spell Pierce",
    "Drown in the Loch",
    "Surgical Extraction",
    "Blood Moon",
]

results = {}
for card in CARDS:
    url = f"https://api.scryfall.com/cards/named?fuzzy={urllib.parse.quote(card)}"
    try:
        import urllib.parse
        url = f"https://api.scryfall.com/cards/named?fuzzy={urllib.parse.quote(card)}"
        req = urllib.request.Request(url, headers={"User-Agent": "TeamResolveGuide/1.0"})
        with urllib.request.urlopen(req, timeout=8) as r:
            data = json.loads(r.read())
        oracle = data.get("oracle_text", "")
        type_line = data.get("type_line", "")
        mc = data.get("mana_cost", "")
        results[card] = {"mana": mc, "type": type_line, "oracle": oracle}
        time.sleep(0.15)
    except Exception as e:
        results[card] = {"error": str(e)}

for card, info in results.items():
    print(f"\n=== {card} ===")
    if "error" in info:
        print(f"ERROR: {info['error']}")
    else:
        print(f"Cost: {info['mana']}  Type: {info['type']}")
        print(info['oracle'])
