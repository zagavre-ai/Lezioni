# -*- coding: utf-8 -*-
# Controllo di sincronia: 10 punti a caso in cui si accende una card, con la trascrizione parola per parola. uso: python3 sync.py PARTE [seme]
import sys, json, random
sys.path.insert(0, '/tmp/claude-0/w')
from dati import PARTI, POFF, ARG
P = int(sys.argv[1]); seed = int(sys.argv[2]) if len(sys.argv) > 2 else 4
WK = '/home/user/w/l04/work'; order = PARTI[P]
segs = json.load(open('/tmp/claude-0/w/tr/lez04.json'))
B = '/home/user/w/b04/revisione-storia-V-lez04'; ST = dict(json.load(open(f'{B}/timeline_Parte{P}.json')))
ev = []
for pos, n in enumerate(order, 1):
    js = json.load(open(f'{WK}/pieces/P{P}_T{n}.mp4.json')); subs = js['subs']
    cum = []; acc = 0
    for a, b in subs: cum.append((acc, a, b)); acc += b - a
    def src(tpiece):
        for c0, a, b in cum:
            if c0 <= tpiece <= c0 + (b - a) + 1e-6: return a + (tpiece - c0)
        return None
    t = 0; prev = None
    for sk, act, f in js['seq']:
        if sk[0] == 'cards' and act >= 0 and (prev is None or prev != (sk[2], act)) and t > 0:
            ev.append((n, pos + POFF[P], t / 30, src(t / 30), act, sk))
        prev = (sk[2], act) if sk[0] == 'cards' else None; t += f
random.seed(seed); pick = sorted(random.sample(ev, min(10, len(ev))), key=lambda e: (e[1], e[2]))
print('| minuto video | argomento | card accesa | inizio frase del prof (sorgente) | prima parola della frase | scarto |')
print('|---|---|---|---|---|---|')
for n, g, tp, ts, act, sk in pick:
    vm = ST[f'prof{g}'] + tp
    seg = None
    for s in segs:
        if s['inizio'] - 0.35 <= ts <= s['fine'] + 0.1: seg = s; break
    seg = seg or min(segs, key=lambda s: abs(s['inizio'] - ts))
    w0 = seg['parole'][0][0] if seg.get('parole') else seg['inizio']
    from slides import cards_from_pdf
    cp = cards_from_pdf()
    head = cp[n][act].split(':')[0][:40]
    print(f"| {int(vm // 60)}:{vm % 60:04.1f} | {n} | {act + 1}. {head} | {seg['inizio']:.1f} s: «{seg['testo'][:70]}» | {seg['parole'][0][1] if seg.get('parole') else ''} | {ts - w0:+.1f} s |")
