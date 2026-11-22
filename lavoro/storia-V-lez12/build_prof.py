import sys, json, os, time
sys.path.insert(0, '/home/user/Lezioni/lavoro/storia-V-lez12')
import slide, montaggio as M
ks = [int(x) for x in sys.argv[1:]]
# pagine prima di ogni argomento: copertina+argomenti (2) + per argomento (finestre prof + 1 approfondimento + 1 pillola)
def npag(k): return len({w['id'] for *_, w, a in slide.segmenti(k)})
base = {}; p = 3
base[0] = 1
for k in range(1, 7): base[k] = p; p += npag(k) + 2
for k in ks:
    t = time.time()
    r = M.pezzo_prof(k, base[k])
    json.dump({x: v for x, v in r.items()}, open(f'{M.OUT}/prof{k}.json', 'w'), ensure_ascii=False, indent=1)
    open(f'{M.OUT}/prof{k}.ok', 'w').write('ok')
    print(k, 'fatto', round(time.time() - t), 's', r['durata'], flush=True)
