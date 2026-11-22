#!/usr/bin/env python3
# Assembla le Parti 1 e 2: costruisce ogni pezzo (se manca) e li concatena. Le voci mancanti sono PROVVISORIE (silenzio di durata stimata).
import os, sys, json, subprocess, re
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
import kore, covers, mappe_def as M
import lib_slide as L
from profpiece import monta_prof, W, CACHE
from build_prof import NOMI
H = os.path.dirname(os.path.abspath(__file__))
O = W + '/out'; os.makedirs(O, exist_ok=True)
PIANO = json.load(open(H + '/piano.json'))
AP = {x['nome']: x['testo'] for x in json.load(open('/tmp/w/work/testi_voci_new.json'))}
OLD = {x['nome']: x['testo'] for x in json.load(open('/tmp/w/work/testi_old.json'))}
TXT = {**OLD, **AP}
KWS = {1: ['deficit pubblico', 'inflazione', 'Biennio rosso'], 2: ['Fiume', 'vittoria mutilata', 'voto proporzionale'], 3: ['Fasci di combattimento', 'squadrismo', 'camicia nera'],
       4: ['Blocchi Nazionali', 'Trattato di Rapallo', 'Partito Nazionale Fascista'], 5: ['Marcia su Roma', 'stato d\'assedio', 'incarico a Mussolini'], 6: ['discorso del bivacco', 'Gran consiglio', 'Legge Acerbo'], 7: ['Matteotti', 'Aventino', 'dittatura']}
PILL = {1: [1], 2: [3, 2], 3: [4], 4: [5], 5: [6], 6: [7], 7: [8]}      # argomento -> insiemi di voci PI/SC
APN = {1: ['AP1'], 2: ['AP2', 'AP3'], 3: ['AP4'], 4: ['AP5'], 5: ['AP6'], 6: ['AP7'], 7: ['AP8']}
MAPA = {2: ('M1', 1), 4: ('M2', 2), 7: ('M3', 3)}                        # argomento -> (mappa, numero): solo le 3 mappe del prof
def pz(nome, f, *a, **k):
    p = f'{O}/{nome}.mkv'
    if not os.path.exists(p) or os.environ.get('RIFAI') == nome:
        r = f(p, *a, **k)
    else: r = None
    return p, r
INFO = []   # (nome, durata, voce_reale)
def dur(p): return float(subprocess.run(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', p], capture_output=True, text=True).stdout)
def aggiungi(lst, nome, p, real=True):
    if not os.path.exists(p):
        print('MANCA', nome, flush=True); return
    lst.append((nome, p, dur(p), real))
def sigla(nome, src, fade_out=0.3):
    p = f'{O}/{nome}.mkv'
    if not os.path.exists(p):
        d = dur(src)
        subprocess.run(['ffmpeg', '-v', 'error', '-y', '-i', src, '-vf', f'fps=30,scale=1920:1080,fade=t=out:st={d - fade_out:.2f}:d={fade_out},format=yuv420p', '-c:v', 'libx264', '-preset', 'ultrafast', '-crf', '14', '-c:a', 'pcm_s16le', '-ar', '48000', '-ac', '2', p], check=True)
    return p
def mappa_pezzo(key, out):
    m = getattr(M, key)
    # ancore dalla voce trascritta se disponibile
    anc = {}
    jp = f"/tmp/w/work/vox/{m['voce']}_tr.json"
    if os.path.exists(jp):
        Wd = kore.parole_voce(jp); da = 0.0
        for k, stem, _ in m['anc']:
            t = kore.trova(Wd, stem, da)
            anc[k] = t if t is not None else da; da = anc[k] + 0.05
        # la voce comincia dopo il titolo: il centro compare quando si legge il titolo
        anc[m['anc'][0][0]] = 0.3
    else:
        # stima proporzionale al testo
        txt = m['testo']; tot = len(txt)
        for k, stem, _ in m['anc']:
            i = txt.lower().find(stem.lower()); anc[k] = (max(i, 0) / tot) * kore.stima(txt)
        anc[m['anc'][0][0]] = 0.3
    return kore.mappa(out, m['titolo'], m['nodi'], m['archi'], m['voce'], m['testo'], anc, solo_png=f'{O}/{key}_finale.png')
def parte(n):
    L_ = []; pag = 1
    if n == 1:
        argos = [1, 2, 3]
    else:
        argos = [4, 5, 6, 7]
    aggiungi(L_, 'SIGLA', sigla('SIGLA', '/home/user/Lezioni/kit/sigle/Sigla_Storia_15s.mp4'))
    if n == 1:
        # copertina con voce di benvenuto: NESSUN riquadro del docente
        v, real = kore.voce('BEN_R2', TXT['BEN_R2']); dv = len(v) / kore.SW; dd = 1.0 + dv + 1.5
        im_c = covers.cover(False)
        def pc(t):
            return im_c
        p, _ = pz('BENV', lambda out: kore.scrivi(out, dd, pc, kore.mix(dd, [(kore.suono('trans.wav'), 0, .5), (v, 1.0, 1.0)])))
        aggiungi(L_, 'BENV', p, real)
        # introduzione del docente sopra la copertina, poi slide degli argomenti
        iv = PIANO['D0']['iv'] + PIANO['D0b']['iv']; ivm = []
        for a, b in iv:
            if ivm and abs(a - ivm[-1][1]) < 1e-6: ivm[-1][1] = b
            else: ivm.append([a, b])
        cut = sum(b - a for a, b in PIANO['D0']['iv'])
        pa = f'{O}/cover_box.png'; covers.cover(True).save(pa); pb = f'{O}/argomenti.png'; covers.argomenti(2).save(pb)
        p = f'{O}/D0.mkv'
        if not os.path.exists(p): monta_prof('D0', ivm, [(0.0, pa), (cut, pb)], p)
        aggiungi(L_, 'D0', p)
        pag = 3
    else:
        # spiegone della Parte 1 (voce Kore), con le immagini e la mappa di quella Parte
        p, r = pz('SPIEGONE', spiegone); aggiungi(L_, 'SPIEGONE', p, r[1] if r else spiegone_real())
    for a in argos:
        Pn = n
        p, _ = pz(f'T{a}', kore.scheda_titolo, a, covers.ARG[a - 1], KWS[a]); aggiungi(L_, f'T{a}', p)
        aggiungi(L_, f'D{a}', f'{O}/D{a}.mkv')
        for j, nm in enumerate(APN[a]):
            p, r = pz(nm, kore.approfondimento, nm, TXT[nm], 20 + a); aggiungi(L_, 'AN' + nm[2:], p, voce_reale(nm))
        if a in MAPA:
            key, k = MAPA[a]; p, r = pz(f'MAP{k}', lambda out: mappa_pezzo(key, out)); aggiungi(L_, f'MAP{k}', p, voce_reale(getattr(M, key)['voce']))
        for s in PILL[a]:
            nm = f'R{a}' if len(PILL[a]) == 1 else f'R{a}_{s}'
            noms = [f'SC{s}_{i}' for i in range(1, 6)]
            p, r = pz(nm, kore.pillola, a, covers.ARG[a - 1] if len(PILL[a]) == 1 else ('Vittoria mutilata e Fiume' if s == 3 else 'Le elezioni del 1919'), f'PI{s}', TXT[f'PI{s}'], noms, [TXT[x] for x in noms], 30 + a)
            aggiungi(L_, 'R' + nm[1:], p, all(voce_reale(x) for x in noms + [f'PI{s}']))
        p, _ = pz(f'Q{a}', kore.scheda_quiz, covers.ARG[a - 1]); aggiungi(L_, f'Q{a}', p)
    if n == 2:
        gl = [('Biennio rosso', 'il periodo 1919-1920 di rivolte contadine e operaie, fino all\'occupazione delle fabbriche.'), ('Sistema proporzionale', 'il metodo che assegna i seggi in proporzione ai voti ottenuti dai partiti.'), ('Vittoria mutilata', 'il mito nazionalista secondo cui l\'Italia era stata privata della Dalmazia e di Fiume.'), ('Squadrismo', 'la violenza delle squadre d\'azione fasciste contro cooperative, leghe e sedi socialiste.'),
              ('Blocchi Nazionali', 'le liste con cui Giolitti, nel 1921, includeva i fascisti per integrarli nel sistema.'), ('Marcia su Roma', 'la mobilitazione fascista dell\'ottobre 1922 che porta Mussolini al governo.'), ('Legge Acerbo', 'la riforma del 1923 che dà i due terzi dei seggi alla lista col 25% dei voti.'), ('Secessione dell\'Aventino', 'l\'abbandono del Parlamento da parte delle opposizioni dopo il delitto Matteotti.')]
        glv = [TXT[f'LG{i}'] for i in range(1, 9)]
        p, r = pz('GL', kore.glossario, gl, '', 60); aggiungi(L_, 'GL', p, all(voce_reale(f'LG{i}') for i in range(0, 9)))
        items = [(f'{i + 1}. {covers.ARG[i]}', a) for i, a in enumerate([2.7, 5.0, 7.4, 9.1, 12.5, 14.6, 17.0])]
        p, r = pz('RF', kore.riepilogo, 'FIN', TXT['FIN'], items, 61); aggiungi(L_, 'RF', p, voce_reale('FIN'))
        # mappa finale: le tre mappe del prof, ferme 4 s ciascuna
        for i, key in enumerate(['M1', 'M2', 'M3']):
            if not os.path.exists(f'{O}/{key}_finale.png'): mappa_pezzo(key, None)
        p, r = pz('MAPF', kore.immagini_fisse, [f'{O}/{k}_finale.png' for k in ['M1', 'M2', 'M3']], [4.0, 4.0, 4.0], 'FIN2', OLD['FIN2'] if 'FIN2' in OLD else 'Questa lezione è finita.')
        aggiungi(L_, 'MAPF', p, voce_reale('FIN2'))
        p, _ = pz('VF', kore.scheda_quiz, 'Il dopoguerra italiano e il fascismo', True); aggiungi(L_, 'VF', p)
    aggiungi(L_, 'SFIN', sigla('SFIN', '/home/user/Lezioni/kit/sigle/Sigla_finale_5s_con_avviso_diritti.mp4'))
    if n == 2:
        p, r = pz('CIN', kore.scheda_compiti_intro); aggiungi(L_, 'CIN', p, voce_reale('CINTRO_R2'))
        comp = json.load(open('/tmp/w/work/compiti.json'))['compiti']
        dq = [c['testo'] for c in comp]; pg = f'{O}/compiti.png'; covers.compiti_png(dq, 62).save(pg)
        # scheda compiti: 60 s con scorrimento lento (non resta mai ferma: le domande si accendono una alla volta)
        p = f'{O}/CMP.mkv'
        if not os.path.exists(p): compiti_pezzo(p, dq)
        aggiungi(L_, 'CMP', p)
    return L_
def voce_reale(nome): return os.path.exists(kore.VOX + nome + '.wav')
def spiegone_real(): return voce_reale('SPIEGONE_P2')
def spiegone(out):
    txt = TXT['SPIEGONE_P2']; v, real = kore.voce('SPIEGONE_P2', txt); dv = len(v) / kore.SW; d = 1.2 + dv + 0.7
    base, y0 = kore.base_bianca('Ripasso della Parte precedente', 'Che cosa abbiamo visto', 1)
    pars = [s.strip() for s in re.split(r'(?<=[.:])\s+(?=(?:Primo|Secondo|Terzo) argomento|Ora vediamo)', txt) if s.strip()]
    pars = [p_ for p_ in re.split(r'(?=Primo argomento|Secondo argomento|Terzo argomento|Ora vediamo)', txt) if p_.strip()]
    titoli = ['Il Biennio rosso', 'La vittoria mutilata, Fiume e le elezioni del 1919', 'La nascita del fascismo']
    tot = sum(len(x) for x in pars); acc = 0; tf = []
    for x in pars: tf.append(1.2 + dv * acc / tot); acc += len(x)
    # immagini del prof (alta risoluzione) e la mappa della Parte 1
    from PIL import Image
    imgs = [f'{CACHE}/img_p3-001.jpg.png', f'{CACHE}/img_p6-001.jpg.png', f'{CACHE}/img_p8-001.jpg.png']
    if not all(os.path.exists(i) for i in imgs):
        from build_prof import img_pronta
        for nm in ['p3-001.jpg', 'p6-001.jpg', 'p8-001.jpg']: img_pronta(nm)
    imgs = [Image.open(i).convert('RGB') for i in imgs]
    mp = Image.open(f'{O}/M1_finale.png').convert('RGB') if os.path.exists(f'{O}/M1_finale.png') else None
    def painter(t):
        im = base.copy().convert('RGBA'); dd = kore.ImageDraw.Draw(im)
        k = max([i for i in range(3) if tf[i] <= t] or [0])
        p = kore.ease((t - tf[k]) / .5)
        dd.text((80, y0 + 10), f'{k + 1}. ' + titoli[k], font=kore.F('Figtree-ExtraBold.ttf', 40), fill=kore.TEL)
        pim = imgs[k]; sc = min(1000 / pim.width, 640 / pim.height); pim = pim.resize((int(pim.width * sc), int(pim.height * sc)))
        lay = pim.convert('RGBA'); kore.rise(im, lay, 80, y0 + 80, p, 30)
        if k == 1 and mp is not None:
            m2 = mp.resize((800, 450)); kore.rise(im, m2.convert('RGBA'), 1060, y0 + 80, kore.ease((t - tf[1] - 2) / .6), 30)
        return im
    r = kore.scrivi(out, d, painter, kore.mix(d, [(kore.suono('trans.wav'), 0, .5), (v, 1.2, 1.0)])); return r, real
def compiti_pezzo(out, dq):
    d = 75.0
    from PIL import Image
    base = covers.compiti_png(dq, 62)
    def painter(t):
        return base
    kore.scrivi(out, d, painter, kore.mix(d, [(kore.suono('trans.wav'), 0, .5)]))
def concatena(lista, out_mkv):
    lst = f'{O}/lista_{os.path.basename(out_mkv)}.txt'
    open(lst, 'w').write(''.join(f"file '{p}'\n" for _, p, _, _ in lista))
    subprocess.run(['ffmpeg', '-v', 'error', '-y', '-f', 'concat', '-safe', '0', '-i', lst, '-c', 'copy', out_mkv], check=True)
if __name__ == '__main__':
    n = int(sys.argv[1]); L_ = parte(n)
    t = 0; TL = []
    for nome, p, d, real in L_:
        TL.append([nome, round(t, 3), round(d, 3), real]); t += d
    json.dump(TL, open(f'{O}/timeline_P{n}.json', 'w'), indent=1)
    concatena(L_, f'{O}/P{n}_intermedio.mkv')
    print('PARTE', n, 'durata %.1f s = %.2f min' % (t, t / 60), 'voci provvisorie:', [x[0] for x in L_ if not x[3]])
