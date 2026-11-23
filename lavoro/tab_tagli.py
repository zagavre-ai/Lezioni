# Tabella con la fine di ogni pezzo del docente: minuto nel video finale, ultime 8 parole, frase finita sì/no (sulla trascrizione)
import sys, json, re
sys.path.insert(0, '/tmp/claude-0/l15')
from plan2 import load, fine_frase
W = '/tmp/claude-0/l15'
TL = {n: (s, f) for n, s, f in json.load(open(W + '/out/tl.json'))}
segs = load()
rows = []
for name in sorted([n for n in TL if n == 'intro' or n.startswith('prof')], key=lambda n: TL[n][0]):
    f = 'intro' if name == 'intro' else None
    if name != 'intro':
        pos, k = re.match(r'prof(\d+)_(\d+)', name).groups()
        from dati import GLOBAL_ORDER
        f = f'T{GLOBAL_ORDER[int(pos) - 1]}_{int(k) - 1}'
    j = json.load(open(f'{W}/pieces/{f}.mp4.json')); subs = j['subs']
    a0 = subs[0][0]; b = subs[-1][1]
    inside = [s for s in segs if s['inizio'] >= a0 - 0.05 and s['fine'] <= b + 0.05]
    last = inside[-1]; words = last['testo'].split()[-8:]
    s0, nf = TL[name]; end = s0 + nf / 30.0
    inizio = inside[0]['testo'].split()[:8]
    rows.append(dict(pezzo=name, inizio_min='%d:%04.1f' % (s0 // 60, s0 % 60), fine_min='%d:%04.1f' % (end // 60, end % 60), prime=' '.join(inizio), ultime=' '.join(words), frase_finita='sì' if fine_frase(last['testo']) else 'DA VERIFICARE'))
json.dump(rows, open(W + '/out/tab_tagli.json', 'w'), ensure_ascii=False, indent=1)
for r in rows: print(r['pezzo'], r['fine_min'], '|', r['ultime'], '|', r['frase_finita'])
