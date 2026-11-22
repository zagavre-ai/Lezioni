import sys, json, time, os; sys.path.insert(0, '/home/user/w3/build')
from pieces import *
part = int(sys.argv[1]); preview = len(sys.argv) > 2 and sys.argv[2] == 'prev'
only = int(sys.argv[3]) if len(sys.argv) > 3 else None
ARGS = {1: [1, 2, 3, 4, 5], 2: [6, 7, 8, 9, 10, 11]}[part]
def subs_ps(a):
    vs = []; k = 1
    while f'PS{a}_{k}' in TESTI: vs.append(f'PS{a}_{k}'); k += 1
    return subs_seq(vs, 0.9, 0.55)
def maps_voices(m):
    import maps
    return maps.MAPS[m]['voices']
def PAGES_OUT(): return PAGES
t0 = time.time(); log = open(f'/home/user/w3/log_part{part}.txt', 'a')
def L(*a): print(*a, file=log, flush=True)
segs = []; tl = []   # tl: (nome, indice seg)
def add(sg, nome=None, subs=None):
    if subs is not None: sg.subs = subs
    segs.append(sg); tl.append(nome or sg.name)
page = 1
SIGLA = KIT + '/sigle/Sigla_Storia_15s.mp4'; FINALE = KIT + '/sigle/Sigla_finale_5s_con_avviso_diritti.mp4'
add(seg_mp4(SIGLA, 'SIGLA'))
if part == 1:
    add(seg_cover_voice(ARGS), subs=subs_voice('BEN_R2', 0.9))
    add(seg_intro_prof(ARGS, 0, 30), 'D0')
    add(seg_dic(1, ARGS, 'DIC_1'), 'DIC', subs_voice('DIC_1', 0.9))
else:
    imgs = {1: D.IMG['regicidio'][0], 2: '/home/user/w3/fr/map1_final.png', 3: D.IMG['turati'][0], 4: D.IMG['murri'][0], 5: None}
    add(seg_spiegone([1, 2, 3, 4, 5], imgs, cover_args=ARGS), 'SPIEGONE', subs_seq(['SPG_0', 'R1', 'R2', 'R3', 'R4', 'R5'], 0.9, 0.8 if False else 0.8))
    add(seg_dic(2, ARGS, 'DIC_2'), 'DIC', subs_voice('DIC_2', 0.9))
for a in ARGS:
    if only and a != only: continue
    add(seg_dark_title(f'Argomento {a:02d}', D.ARG[a]['titolo'], name=f'T{a}'), f'T{a}')
    items, page = arg_pages(a, page)
    for k, x in items:
        if k == 'prof': add(x, x.name)
        else: add(seg_ap(x), x)
    if D.END_AP.get(a): add(seg_ap(D.END_AP[a]), D.END_AP[a])
    if a in D.MAPPE: add(seg_map(D.MAPPE[a]), f'MAP{D.MAPPE[a]}', subs_seq(maps_voices(D.MAPPE[a]), 0.9, 0.7))
    add(seg_pillola_intro(a), f'PI{a}', subs_voice(f'PIL{a}', 4.2)); add(seg_pillola_schema(a), f'PS{a}', subs_ps(a)); add(seg_quiz_arg(a), f'Q{a}')
    L('argomento', a, 'pronto', round(time.time() - t0), 's')
if part == 1:
    add(seg_list_voice('GL1', 'GLOSSARIO', 'Le parole chiave'), 'GL', subs_voice('GL1', 0.9)); add(seg_list_voice('RF1', 'RIPASSO FINALE', 'Ripasso finale della prima parte'), 'RIEP', subs_voice('RF1', 0.9))
    add(seg_fin_voice('FIN1', 'Nella parte successiva: il suffragio universale maschile e il Patto Gentiloni, la questione meridionale e la guerra di Libia'), 'FIN', subs_voice('FIN1', 0.9))
    add(seg_mp4(FINALE, 'FINALE'), 'FINALE')
else:
    add(seg_list_voice('GL2', 'GLOSSARIO', 'Le parole chiave'), 'GL', subs_voice('GL2', 0.9)); add(seg_list_voice('RF2', 'RIPASSO FINALE', 'Ripasso finale della seconda parte'), 'RIEP', subs_voice('RF2', 0.9))
    add(seg_fin_voice('FIN2', 'Adesso mettiti alla prova con la verifica finale'), 'FIN', subs_voice('FIN2', 0.9))
    add(seg_verifica("Verifica finale · Storia V · L'Italia di Giolitti"), 'VF')
    add(seg_mp4(FINALE, 'FINALE'), 'FINALE')
    ci, cc = seg_compiti(); add(ci, 'COMPITI_I'); add(cc, 'COMPITI', subs_voice('CMP_1', 0.9))
out = f'/home/user/w3/Storia_Lez3_Parte{part}_1080p.mp4' if not only else f'/home/user/w3/prev_p{part}_a{only}.mp4'
L('assemblo', len(segs), 'pezzi', round(time.time() - t0))
r = assemble2(segs, out, KIT + '/suoni/trans.wav', f'/home/user/w3/work_p{part}', workers=int(os.environ.get('WORKERS', '4')), log=log, preview=preview)
# timeline [nome, inizio, durata] (le schede Q: inizio visibile = inizio pezzo + dissolvenza)
TL = []
for i, (nm, sg) in enumerate(zip(tl, segs)):
    st = r['starts'][i]
    if nm.startswith('Q') or nm == 'VF':
        st += r['Ls'][i - 1] if i > 0 else 0
    TL.append([nm, round(st, 3), round(sg.n / FPS, 3)])
json.dump(TL, open(f'/home/user/w3/timeline_Parte{part}.json', 'w'), ensure_ascii=False)
json.dump(r, open(f'/home/user/w3/assemble_Parte{part}.json', 'w'))
SUBS = []
for i, sg in enumerate(segs):
    if hasattr(sg, 'subs'):
        for a_, b_, t_, w_ in sg.subs: SUBS.append([r['starts'][i] + a_, r['starts'][i] + b_, t_, tl[i]])
json.dump(SUBS, open(f'/home/user/w3/subs_Parte{part}.json', 'w'), ensure_ascii=False)
json.dump(PAGES_OUT(), open(f'/home/user/w3/pages_Parte{part}.json', 'w'), ensure_ascii=False)
json.dump([[tl[i], getattr(sg, 'src', None), getattr(sg, 'lastwords', None), r['starts'][i], sg.n / FPS] for i, sg in enumerate(segs) if hasattr(sg, 'src')], open(f'/home/user/w3/tagli_Parte{part}.json', 'w'), ensure_ascii=False)
L('FATTO', r['dur'], round(time.time() - t0), 's')
