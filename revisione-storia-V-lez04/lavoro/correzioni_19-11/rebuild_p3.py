# Parte 3: rinumera le pagine nell'ordine del video (6, 8, 9, 11, 10) e rifà i pezzi di 11 e 10
import sys, os, json, glob
sys.argv = ['build2.py', '3']
src = open('/home/user/w/l04/work/build2.py').read().split("if __name__")[0]
exec(src)
segs, topics, intro, pageidx, dmin, isimg, cp = plan()
order = PARTI[3]; TT = {T['n']: T for T in topics}
d = json.load(open(f'{NEWP}/pages_P3_6_8_9_10.json'))
def parse(k):
    out = []
    for i, t in enumerate(k.split('|')):
        try: out.append(eval(t))
        except Exception: out.append(t)
    return tuple(out)
pageno = {}
for k, v in d.items():
    key = parse(k); topic = key[1] if key[0] == 'cards' else (key[2] if key[0] in ('img', 'imgc') else None)
    if key[0] == 'cover' or topic in (6, 8, 9): pageno[key] = v
# cancello i PNG vecchi di 11 e 10 e ripartiamo
for f in set(glob.glob(f'{SLP}/P3_*_11_*') + glob.glob(f'{SLP}/P3_*_10_*') + glob.glob(f'{SLP}/P3_imgc_*')):
    os.remove(f)
for n in (11, 10):
    pos = order.index(n) + 1; T = TT[n]; g = pos + POFF[3]
    subs = sub_intervals(segs, T['src_a'], T['src_b']); runs = topic_states(T, pageidx, isimg, subs)
    fr = frames_from_runs(runs, int(round(sum(y - x for x, y in subs) * 30)))
    seq = build_piece(3, f'T{n}', subs, fr, len(cp[n]), cp, order, pageno)
    print('rifatto T', n, 'pagine', sorted(v for k, v in pageno.items() if len(k) > 2 and (k[1] if k[0]=='cards' else k[2]) == n), flush=True)
json.dump({'|'.join(map(str, k)): v for k, v in pageno.items()}, open(f'{NEWP}/pages_P3_all.json', 'w'))
