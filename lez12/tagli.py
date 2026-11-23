# Tabella dei tagli del docente: per ogni pezzo, inizio e fine (minuto nel video finale), prime/ultime parole, frase finita sì/no.
import sys, json, re
sys.path.insert(0, '/home/user/Lezioni/lez12')
import piano as PI
W = '/home/user/Lezioni/lavoro/'
LEAD, PRE = 0.35, 0.15
tl = json.load(open(sys.argv[1])); start = {n: t for n, t, d in tl}
segs = json.load(open(W + 'trascr.json')); corr = {x['i']: x['testo'] for x in json.load(open(W + 'trascr_corretta.json'))['segmenti']}
mm = lambda t: f'{int(t//60)}:{int(t%60):02d}'
rows = ['| Pezzo | Inizio (video) | Prime parole | Fine (video) | Ultime 8 parole | Frase finita | Pausa dopo l\'ultima parola |', '|---|---|---|---|---|---|---|']
for pid, a, t0, t1, st in PI.P:
    S0 = start[pid]
    inside = [(i, s) for i, s in enumerate(segs) if s['inizio'] >= t0 - 0.25 and s['fine'] <= t1 + 0.4 and corr.get(i, s['testo']).strip()]
    first = corr[inside[0][0]].split()[:6]; lastt = corr[inside[-1][0]]; last = lastt.split()[-8:]
    fin = 'sì' if re.search(r'[.?!…»”]$', lastt.strip()) else 'no'
    nxt = [s['inizio'] for s in segs if s['inizio'] > t1 + 0.05]
    pausa = (nxt[0] - inside[-1][1]['fine']) if nxt else 9
    rows.append(f"| {pid} | {mm(S0 + LEAD)} | {' '.join(first)} | {mm(S0 + LEAD + (t1 - (t0 - PRE)))} | …{' '.join(last)} | {fin} | {pausa:.2f} s |")
open(W + 'consegna/tabella_tagli.md', 'w').write('\n'.join(rows) + '\n'); print('\n'.join(rows))
