import re, os

base = r'E:\vscode ai project\My-Website'
files = {
    'boros': 'boros-energy-playbook.html',
    'jeskai': 'jeskai-blink-playbook.html',
    'prowess': 'prowess-playbook.html',
    'glock': 'glockulous-playbook.html',
    'uw': 'uw-control-playbook.html',
}

for name, fname in files.items():
    path = os.path.join(base, fname)
    with open(path, encoding='utf-8') as f:
        c = f.read()

    nav_tabs = len(re.findall(r'onclick="show\(', c))
    doubles = len(re.findall(r'class="c"><span class="c">', c))
    bare_teferi = c.count('class="c">Teferi<')
    bare_ragavan = c.count('class="c">Ragavan<')
    bare_drc = c.count('class="c">DRC<')
    heur_fixed = 'display:block' in c and 'float:left' in c
    dated = 'March 30, 2026' in c
    sw_fixed = 'card-grid card-grid-2' in c
    size_kb = round(os.path.getsize(path) / 1024, 1)

    print(name, size_kb, 'tabs=' + str(nav_tabs), 'doubles=' + str(doubles),
          'bare_tef=' + str(bare_teferi), 'bare_rag=' + str(bare_ragavan),
          'bare_drc=' + str(bare_drc), 'heur=' + str(heur_fixed),
          'date=' + str(dated), 'sw=' + str(sw_fixed))
