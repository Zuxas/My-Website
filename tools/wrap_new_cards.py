import re

src = r'E:\vscode ai project\My-Website\uw-control-playbook.html'
with open(src, encoding='utf-8') as f:
    c = f.read()

# Cards that appear in the new dives not yet wrapped
NEW_CARDS = [
    'Mox Opal', 'Cranial Plating', 'Arcbound Ravager', 'Urza\'s Saga',
    'Thoughtcast', 'Shadowspear', 'Ornithopter', 'Inkmoth Nexus',
    'Expedition Map', 'Thought-Knot Seer', 'Reality Smasher',
    'Karn Liberated', 'Wurmcoil Engine', 'Chalice of the Void',
    'Territorial Kavu', 'Scion of Draco', 'Ignoble Hierarch',
    'Tribal Flames',
    'Atraxa, Grand Unifier',
    'Goryo\'s Vengeance', 'Griselbrand',
    'Grief', 'Faithful Mending',
    'Ruby Medallion', 'Past in Flames',
    'Empty the Warrens', 'Grapeshot',
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

for card in NEW_CARDS:
    before = c.count('class="c">' + card)
    c = wrap_card(c, card)
    after = c.count('class="c">' + card)
    if after > before:
        print('Wrapped', card, ':', before, '->', after)

# Final double-nest fix
c = re.sub(
    r'<span class="c"><span class="c">([^<]+)</span>([^<]*)</span>',
    lambda m: '<span class="c">' + m.group(1) + m.group(2) + '</span>',
    c
)

with open(src, 'w', encoding='utf-8') as f:
    f.write(c)

doubles = len(re.findall(r'class="c"><span class="c">', c))
print('Doubles after fix:', doubles)
print('Final size:', round(len(c)/1024, 1), 'KB')
