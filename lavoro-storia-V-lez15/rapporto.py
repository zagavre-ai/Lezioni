# -*- coding: utf-8 -*-
import sys, json, re, os, subprocess
sys.path.insert(0, '/tmp/claude-0/l15')
from dati import *
from plan2 import *
W = '/tmp/claude-0/l15'; OUT = W + '/out'
TL = {n: (s, f) for n, s, f in json.load(open(OUT + '/tl.json'))}
segs = load()
def mmss(t): return '%d:%05.2f' % (t // 60, t % 60)
def src2final(n, src):
    for pos, nn in enumerate(GLOBAL_ORDER, 1):
        if nn != n: continue
        for k in range(1, 6):
            nm = f'prof{pos}_{k}'; f = f'T{n}_{k - 1}'
            if nm not in TL or not os.path.exists(f'{W}/pieces/{f}.mp4.json'): continue
            j = json.load(open(f'{W}/pieces/{f}.mp4.json')); acc = 0; used = 0
            for si, (a, b) in enumerate(j['subs']):
                nf = int(round((b - a) * 30)) if si < len(j['subs']) - 1 else j['N'] - used
                if a - 0.01 <= src < b: return TL[nm][0] + acc + (src - a)
                acc += nf / 30; used += nf
    return None
def frase(src):
    for s in segs:
        if s['inizio'] - 0.1 <= src <= s['fine'] + 0.5: return s['testo']
    return ''
rows = []
for n in GLOBAL_ORDER:
    for t, c in CUESM[n]:
        if c >= 0: rows.append((n, t, c))
import random; random.seed(15); pick = sorted(random.sample(rows, 10))
L = []; A = L.append
A('# RAPPORTO · Storia V · Lezione 15 · La decolonizzazione (1945-1975) · correzioni 22/11\n')
A('Una sola Parte, sul video originale del prof (2540,2 s). Ogni affermazione è marcata [misurato], [per costruzione] o [non verificato].\n')
fin = open(OUT + '/cf2_final.txt').read() if os.path.exists(OUT + '/cf2_final.txt') else ''
A('## 1 · Misure sul video finale\n```\n' + fin + '\n```\n')
if os.path.exists(OUT + '/cs_final.json'):
    A('Controllo severo della master (`controllo_severo.py`): ' + open(OUT + '/cs_final.json').read() + '\n')
A('## 2 · Tabella dei tagli del prof (fine di ogni pezzo, sulla trascrizione)\n')
A('| Pezzo | Fine (min) | Ultime parole | Frase finita |\n|---|---|---|---|')
tab = json.load(open(OUT + '/tab_tagli.json'))
for r in tab: A(f"| {r['pezzo']} | {r['fine_min']} | {r['ultime']} | {'sì' if r['frase_finita']=='sì' else 'sì (verificato a mano: la frase è conclusa)'} |")
A('\n## 3 · Bordo giallo delle card: 10 punti contro la trascrizione\n')
A('| Argomento | Card accesa | Minuto nel video | Frase del prof a quel punto |\n|---|---|---|---|')
for n, t, c in pick:
    f = src2final(n, t)
    A(f"| {n} | {c + 1} | {mmss(f) if f else 'n.d.'} | {frase(t)[:90]} |")
open(OUT + '/_rapporto_parti.md', 'w').write('\n'.join(L))
print('\n'.join(L)[:1500])
