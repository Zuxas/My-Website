import re, os

base = r'E:\vscode ai project\My-Website'

# New cards appearing in the 4 new dive sets that need wrapping
NEW_CARDS = [
    # Boros new dives
    "Cranial Plating", "Vault Skirge", "Memnite", "Frogmite",
    "Expedition Map", "Karn Liberated", "Wurmcoil Engine",
    # Jeskai new dives  
    "Urza's Saga",
    # Prowess new dives
    # Glock new dives
    "Nihil Spellbomb", "Harvester of Misery",
]

def wrap_card(text, card):
    escaped = re.escape(card)
    result = []
    last = 0
    for m in re.finditer(escaped, text):
        start, end = m.start(), m.end()
        before = text[max(0, start-20):start]
        if 'class="c">' in before:
            result.append(text[last:end])
        else:
            result.append(text[last:start])
            result.append('<span class="c">' + card + '</span>')
        last = end
    result.append(text[last:])
    return ''.join(result)

files = {
    'boros': 'boros-energy-playbook.html',
    'jeskai': 'jeskai-blink-playbook.html',
    'prowess': 'prowess-playbook.html',
    'glock': 'glockulous-playbook.html',
}

for name, fname in files.items():
    path = os.path.join(base, fname)
    with open(path, encoding='utf-8') as f:
        c = f.read()

    wrapped = 0
    for card in NEW_CARDS:
        before = c.count('class="c">' + card)
        c = wrap_card(c, card)
        after = c.count('class="c">' + card)
        if after > before:
            wrapped += after - before

    # Fix any new doubles
    c = re.sub(
        r'<span class="c"><span class="c">([^<]+)</span>([^<]*)</span>',
        lambda m: '<span class="c">' + m.group(1) + m.group(2) + '</span>',
        c
    )

    with open(path, 'w', encoding='utf-8') as f:
        f.write(c)
    print(name, ':', wrapped, 'new wraps')

print('Done')
