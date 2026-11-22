import json, random, sys, re
sys.path.insert(0, '/home/user/w3/build')
import data as D
S = D.S
random.seed(11)
def ph_of(i0):
    gb = S[i0]['inizio'] - (S[i0 - 1]['fine'] if i0 > 0 else S[i0]['inizio'] - 1.0); return max(0.2, min(0.7, gb - 0.12))
rows = []
for part in (1, 2):
    tg = json.load(open(f'/home/user/w3/tagli_Parte{part}.json'))
    ev_all = []
    for arg, evs in D.EV.items():
        if (arg <= 5) != (part == 1): continue
        title, cards = D.card_list(arg)
        for e in evs:
            if e[0] == 'card': ev_all.append((arg, e[1], e[2], cards[e[2]][0]))
    for arg, t, idx, text in random.sample(ev_all, 5):
        # pezzo del prof che contiene t
        for nm, src, lw, st, d in tg:
            if src[0] - 1 <= t <= src[1] + 0.5:
                i0 = [i for i, z in enumerate(S) if abs(z['inizio'] - src[0]) < 1e-6][0]
                fin = st + ph_of(i0) + (t - src[0])
                seg = min(S, key=lambda z: abs(z['inizio'] - t))
                rows.append((part, fin, arg, text[:50], seg['inizio'], seg['testo'][:70], fin - 0 - (st + ph_of(i0) + (seg['inizio'] - src[0]))))
                break
print('| Parte | Minuto video | Arg. | Card accesa | Frase del prof che comincia | Scarto |\n|---|---|---|---|---|---|')
for p, fin, arg, tx, ts, st_, sc in rows:
    print(f"| {p} | {int(fin//60)}:{fin%60:05.2f} | {arg} | «{tx}…» | «{st_}…» ({ts:.1f} s dell'originale) | {sc:+.2f} s |")
print()
print('| Immagine del prof (pagina PDF) | Argomento in cui compare (uno solo) |\n|---|---|')
for k, a, p in [('regicidio', 1, 3), ('giolitti', 2, 3), ('turati', 3, 6), ('murri', 4, 8), ('emigrazione', 9, 14), ('libia', 10, 16)]:
    print(f"| {D.IMG[k][1]} (p. {p}) | {a} · {D.ARG[a]['titolo']} |")
