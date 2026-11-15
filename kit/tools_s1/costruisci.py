#!/usr/bin/env python3
"""Montaggio di una lezione Storia V (S1).
uso: python3 costruisci.py spec.py ancore.json lavoro_dir PARTE [--solo NOME] [--voci DIR_VOX]
- spec.py: contenuto (argomenti, animazioni, testi voce)
- ancore.json: video sorgente, trascrizione, finestre dei pezzi del docente, ancore di sincronia
Produce lavoro_dir/clips/*.mov, lista_ParteN.txt, timeline_ParteN.json, sottotitoli_ParteN.json
"""
import sys, os, json, re, importlib.util, subprocess, difflib, shutil, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib_s1 import *
import schede_s1 as SC
from slide_testo import struttura
import mappa_s1

mappa_s1.font_css = fonts

A = sys.argv
SPEC, ANC, W, PARTE = A[1], A[2], A[3], int(A[4])
SOLO = A[A.index('--solo') + 1] if '--solo' in A else None
VOX = A[A.index('--voci') + 1] if '--voci' in A else None
sp = importlib.util.spec_from_file_location('spec', SPEC)
S = importlib.util.module_from_spec(sp)
sp.loader.exec_module(S)
ANCH = json.load(open(ANC))
os.makedirs(W + '/clips', exist_ok=True)
os.makedirs(W + '/png', exist_ok=True)
os.makedirs(W + '/tmp', exist_ok=True)
SRC = ANCH['video']
PDF = ANCH['pdf']
TRANS = json.load(open(ANCH['trascrizione']))
GAIN_DOC = ANCH['gain_db']
R = Renderer()
LEAD = 1.0   # secondi di attacco prima della voce
TAIL = 3.4   # secondi di coda dopo la voce (la scheda completa resta visibile)
N_ARG = len(S.ARG)
ARG = {a['id']: a for a in S.ARG}
PART = [p for p in S.PARTI if p['n'] == PARTE][0]
TL = []      # (nome, inizio_s, durata_s)
CUES = []    # (inizio_abs, fine_abs, testo, tipo)
POS = [0.0]
LISTA = []
VOCAB = set()


# --------------------------------------------------------------- utilità
def png(name, html_str):
    p = '%s/png/%s.png' % (W, name)
    if not os.path.exists(p):
        R.shot(html_str, p)
    return p


def voce(nome, frasi):
    """(wav, durata_s, [inizio frase in s dall'inizio della voce]) dalla voce Kore se presente, altrimenti segnaposto."""
    testo = ' '.join(frasi)
    w = None
    if VOX and os.path.exists('%s/%s.wav' % (VOX, nome)):
        w = '%s/%s.wav' % (VOX, nome)
    if w:
        d = wav_dur(w)
        # normalizza a -16 LUFS circa
        n = '%s/tmp/%s_n.wav' % (W, nome)
        if not os.path.exists(n):
            m = subprocess.run(['ffmpeg', '-v', 'info', '-i', w, '-af', 'loudnorm=I=-16:TP=-1.5:LRA=11:print_format=json', '-f', 'null', '-'], capture_output=True, text=True).stderr
            j = json.loads(m[m.rfind('{'):m.rfind('}') + 1])
            g = -16 - float(j['input_i'])
            sh(['ffmpeg', '-y', '-v', 'error', '-i', w, '-af', 'volume=%fdB,alimiter=limit=0.89' % g, '-ar', '48000', '-ac', '2', n])
        w = n
        stima = False
    else:
        d = len(testo.split()) / 2.05 + 0.3 * len(frasi)
        w = silence_wav('%s/tmp/%s_sil.wav' % (W, nome), d)
        stima = True
    tot = sum(len(f) for f in frasi)
    ts = []
    c = 0
    for f in frasi:
        ts.append(d * c / tot)
        c += len(f)
    if not stima:
        ts = snap_pause(w, ts, d)
    return w, d, ts, stima


def snap_pause(w, ts, d):
    """Aggancia gli inizi di frase alla pausa più vicina (±1,2 s) nel parlato reale."""
    raw = subprocess.run(['ffmpeg', '-v', 'error', '-i', w, '-ac', '1', '-ar', '8000', '-f', 's16le', '-'], capture_output=True).stdout
    a = np.frombuffer(raw, np.int16).astype(np.float32) / 32768
    F = 160
    n = len(a) // F
    e = np.sqrt((a[:n * F].reshape(n, F) ** 2).mean(1)) + 1e-9
    db = 20 * np.log10(e)
    sil = db < max(np.percentile(db, 10) + 8, -50)
    pauses = []
    i = 0
    while i < n:
        if sil[i]:
            j = i
            while j < n and sil[j]:
                j += 1
            if (j - i) * 0.02 >= 0.25:
                pauses.append(((i + j) / 2 * 0.02, j * 0.02))
            i = j
        else:
            i += 1
    out = [0.0]
    for t in ts[1:]:
        c = [p for p in pauses if abs(p[0] - t) <= 1.2]
        out.append(min(c, key=lambda p: abs(p[0] - t))[1] - 0.05 if c else t)
    # primo suono
    lead = next((k * 0.02 for k in range(n) if not sil[k]), 0.0)
    out[0] = lead
    return out


def add_tl(name, d_s):
    TL.append((name, round(POS[0], 3), round(d_s, 3)))
    POS[0] += d_s


def add_clip(path):
    LISTA.append(path)


def sfx(nome, delay, db=-6):
    return ('%s/%s.wav' % (SND, nome), delay, db)


# --------------------------------------------------------------- scene a stati con voce (R, AN, MAP, ...)
def scena_voce(nome, tl_nome, builder, frasi, n_stati, extra_audio=(), lead=LEAD, tail=TAIL, riv_sfx=None, cue_tipo='V'):
    """builder(k) -> html dello stato k (k = numero di elementi visibili); la frase k+1 fa comparire l'elemento k."""
    out = '%s/clips/%s.mov' % (W, nome)
    wv, d, ts, stima = voce(nome, frasi)
    tot = lead + d + tail
    nf = fr(tot)
    # inizi stati in secondi dall'inizio della scena
    inizi = [0.0] + [lead + ts[k + 1] for k in range(n_stati)]  # stato 0 (nessun elemento) fino alla frase 1
    states = []
    for k in range(n_stati + 1):
        a = fr(inizi[k])
        b = fr(inizi[k + 1]) if k < n_stati else nf
        states.append((png('%s_s%d' % (nome, k), builder(k)), max(b - a, 1)))
    # correggi somma
    s = sum(n for p, n in states)
    if s != nf:
        states[-1] = (states[-1][0], states[-1][1] + nf - s)
    aud = [(wv, lead, 0)] + list(extra_audio)
    clip(states, out, aud, xf=6, workdir=W + '/tmp', tag=nome)
    # sottotitoli: una frase alla volta
    for k, f in enumerate(frasi):
        a = POS[0] + lead + ts[k]
        b = POS[0] + lead + (ts[k + 1] if k + 1 < len(ts) else d)
        CUES.append((a, b, f, cue_tipo))
    add_tl(tl_nome, nf / FPS)
    add_clip(out)
    return stima


# --------------------------------------------------------------- pezzi del docente
def finestra_pic(t):
    return None


_IMG = {}


def img_pagina(p):
    if p in _IMG:
        return _IMG[p]
    from PIL import ImageChops
    base = '%s/png/pg%02d' % (W, p)
    if not os.path.exists(base + '.png'):
        subprocess.run(['pdftoppm', '-r', '150', '-png', '-singlefile', '-f', str(p), '-l', str(p), PDF, base], check=True)
    im = Image.open(base + '.png').convert('RGB')
    w, h = im.size
    d = ImageChops.difference(im, Image.new('RGB', im.size, (255, 255, 255))).convert('L').point(lambda x: 255 if x > 18 else 0).crop((0, 0, int(w * 0.78), h))
    bb = d.getbbox()
    im.crop((max(bb[0] - 10, 0), max(bb[1] - 10, 0), bb[2] + 10, bb[3] + 10)).save(base + '_c.png')
    _IMG[p] = base + '_c.png'
    return _IMG[p]


def snap_seg(t):
    """aggancia t all'inizio di segmento di trascrizione più vicino (mai a metà parola)."""
    c = min(TRANS, key=lambda s: abs(s['s'] - t))
    return c['s']


def scena_docente(nome, tl_nome, t0, t1, pagina, kicker, ancore, immagini, intro=None):
    """ancore=[[t,unità],...]; immagini=[[ta,tb,pagina_pdf,didascalia],...]"""
    out = '%s/clips/%s.mov' % (W, nome)
    n0, n1 = fr(t0), fr(t1)
    nf = n1 - n0
    if intro is None:
        tt, cards = struttura(PDF, pagina)
        units = [(ci, fi) for ci, (l, frs) in enumerate(cards) for fi, f in enumerate(frs)]
    # eventi di cambio stato (in fotogrammi sorgente)
    ev = sorted(set([n0, n1] + [fr(a[0]) for a in ancore if t0 < a[0] < t1] + [fr(x[0]) for x in immagini if t0 < x[0] < t1] + [fr(x[1]) for x in immagini if t0 < x[1] < t1]))
    states = []
    for a, b in zip(ev, ev[1:]):
        tm = (a + b) / 2 / FPS
        if intro is not None:
            key = 'intro'
            html_s = SC.slide(intro[0], '', [], intro=True, sottotitolo=intro[1])
        else:
            im = next((x for x in immagini if x[0] <= tm < x[1]), None)
            u = 0
            for an in ancore:
                if an[0] <= tm:
                    u = an[1]
            ci, fi = units[u]
            if im:
                key = 'img%d' % im[2]
                html_s = SC.slide(tt, kicker, cards, img=img_pagina(im[2]), keyword=cards[ci][0].rstrip(':'))
            else:
                key = 'u%d' % u
                html_s = None
        p = '%s/png/%s_%s.png' % (W, nome, key)
        if not os.path.exists(p):
            if intro is None and not im:
                R.fit(SC.slide(tt, kicker, cards, att=(ci, fi)), p, '#cards', 945)
            else:
                R.shot(html_s, p)
        states.append((p, b - a))
    # video: sfondo da concat + docente da sorgente + audio sorgente
    if not (os.path.exists(out + '.ok') and open(out + '.ok').read().strip() == str(nf)):
        ov = out + '.v.mp4'
        slide_video(states, ov, 0, W + '/tmp', nome)
        tot = nf / FPS
        cmd = ['ffmpeg', '-y', '-v', 'error', '-i', ov, '-ss', '%.4f' % (n0 / FPS), '-t', '%.4f' % tot, '-i', SRC,
               '-filter_complex', "[1:v]crop=246:137:846:343,scale=368:205:flags=lanczos,fps=30[d];[0:v][d]overlay=1496:156:shortest=1[v];[1:a]volume=%fdB,alimiter=limit=0.9,aresample=48000,aformat=channel_layouts=stereo,apad=whole_dur=%.4f,atrim=0:%.4f[a]" % (GAIN_DOC, tot, tot),
               '-map', '[v]', '-map', '[a]'] + VENC + AENC + ['-frames:v', str(nf), '-t', '%.4f' % tot, out]
        sh(cmd)
        assert nframes(out) == nf, (out, nframes(out), nf)
        os.remove(ov)
        open(out + '.ok', 'w').write(str(nf))
    # sottotitoli dai segmenti di trascrizione
    for s in TRANS:
        if s['s'] >= t0 - 0.01 and s['e'] <= t1 + 0.01:
            CUES.append((POS[0] + s['s'] - t0, POS[0] + s['e'] - t0, s['t'], 'D'))
    add_tl(tl_nome, nf / FPS)
    add_clip(out)


# --------------------------------------------------------------- schede fisse
def scheda_fissa(nome, tl_nome, html_str, durata, audio=()):
    out = '%s/clips/%s.mov' % (W, nome)
    nf = fr(durata)
    clip([(png(nome, html_str), nf)], out, list(audio), workdir=W + '/tmp', tag=nome)
    add_tl(tl_nome, nf / FPS)
    add_clip(out)


def clip_modello(nome, tl_nome, ss, d):
    """Estrae dal video modello (sigla, chiusura) già in formato 1080p."""
    out = '%s/clips/%s.mov' % (W, nome)
    nf = fr(d)
    if not os.path.exists(out + '.ok'):
        sh(['ffmpeg', '-y', '-v', 'error', '-ss', str(ss), '-t', '%.4f' % (nf / FPS), '-i', ANCH['modello'], '-vf', 'scale=1920:1080,fps=30',
            '-af', 'aresample=48000,aformat=channel_layouts=stereo,apad=whole_dur=%.4f,atrim=0:%.4f' % (nf / FPS, nf / FPS)] + VENC + AENC + ['-frames:v', str(nf), out])
        assert nframes(out) == nf
        open(out + '.ok', 'w').write('1')
    add_tl(tl_nome, nf / FPS)
    add_clip(out)


# --------------------------------------------------------------- mappa
def scena_mappa(nome, tl_nome, mp, frasi):
    d = dict(materia='Storia', docente=SC.DOCENTE, titolo=mp['centro'], rami=mp['rami'])
    n = len(d['rami'])

    def b(k):
        return mappa_s1.pagina(d, k, 1920, 1080)
    # le frasi: 0 = apertura, k = ramo k
    scena_voce(nome, tl_nome, b, frasi, n, tail=2.5)
    return d


def dispensa_mappa(nome, mp):
    """pagina A4 della mappa per la dispensa."""
    d = dict(materia='Storia', docente=SC.DOCENTE, titolo=mp['centro'], rami=mp['rami'])
    p = '%s/mappe/%s.pdf' % (W, nome)
    os.makedirs(os.path.dirname(p), exist_ok=True)
    if not os.path.exists(p):
        pg = R.b.new_page(viewport={'width': 1123, 'height': 794})
        pg.set_content(mappa_s1.pagina(d, len(d['rami']), 1123, 794, stampa=True))
        pg.evaluate('document.fonts.ready')
        pg.wait_for_timeout(200)
        pg.pdf(path=p, width='297mm', height='210mm', print_background=True, margin={'top': '0', 'bottom': '0', 'left': '0', 'right': '0'})
        pg.close()
    return p


# --------------------------------------------------------------- costruzione della Parte
def an_builder(an, nome):
    t = an['tipo']
    if t == 'cards':
        return lambda k: SC.an_cards(an['kicker'], an['titolo'], an['items'], k)
    if t == 'timeline':
        return lambda k: SC.an_timeline(an['kicker'], an['titolo'], an['items'], k)
    if t == 'stats':
        return lambda k: SC.an_stats(an['kicker'], an['titolo'], an['items'], k)
    if t == 'immagine':
        img = img_pagina(an['pagina_img'])
        return lambda k: SC.an_img(an['kicker'], an['titolo'], img, 1.0 + 0.12 * k, '')
    raise ValueError(t)


def main():
    tot_arg = len(PART['argomenti'])
    nomi_arg = [ARG[i]['breve'] for i in PART['argomenti']]
    first = PART['argomenti'][0]
    # sigla
    clip_modello('SIGLA', 'SIGLA', 0.0, 16.3)
    # benvenuto con voce
    scena_voce('INTRO%d' % PARTE, 'INTRO%d' % PARTE, lambda k: SC.benvenuto(S.TITOLO, PARTE, nomi_arg), PART['intro'], 0, extra_audio=[])
    if PARTE == 1:
        scena_docente('D0', 'D0', ANCH['d0'][0], ANCH['d0'][1], None, '', [], [], intro=(S.TITOLO, 'Dall’immediato dopoguerra agli anni Sessanta'))
    for ai, aid in enumerate(PART['argomenti']):
        a = ARG[aid]
        idx = aid
        # titolo
        scheda_fissa('T%d' % idx, 'T%d' % idx, SC.titolo_arg(idx, N_ARG, a['titolo']), 4.5, [sfx('titolo', 0.0, -8)])
        # docente
        an_ = ANCH['arg'][str(aid)]
        scena_docente('D%d' % idx, 'D%d' % idx, an_['t0'], an_['t1'], a['pagine'][0], '%02d · %s' % (idx, a['breve'].upper()), an_['ancore'], an_.get('immagini', []))
        for ex in an_.get('dopo', []):
            scena_docente(ex['nome'], ex['nome'], ex['t0'], ex['t1'], None, '', [], [], intro=(ex['titolo'], ex['sottotitolo']))
        # approfondimenti
        for an in a['an']:
            scena_voce(an['nome'], an['nome'], an_builder(an, an['nome']), an['voce'], len(an['items']), extra_audio=[sfx('trans', 0.0, -12)])
        # mappa
        scena_mappa('MAP%d' % idx, 'MAP%d' % idx, a['mappa'], a['mappa']['voce'])
        dispensa_mappa('map%d' % idx, a['mappa'])
        # ripasso
        fr_r = a['ripasso']

        def rb(k, a=a, fr_r=fr_r):
            return SC.ripasso(a['breve'], ' '.join(fr_r[1:k + 1]) if k > 0 else fr_r[0])
        scena_voce('R%d' % idx, 'R%d' % idx, rb, fr_r, len(fr_r) - 1, lead=1.3, extra_audio=[sfx('repaso', 0.0, -8)])
        # quiz
        scheda_fissa('Q%d' % idx, 'Q%d' % idx, SC.quiz(idx, a['breve']), 4.0, [sfx('quiz', 0.5, 0)])
    # mappa finale, glossario, ripasso finale, fine
    scena_mappa('MAPF%d' % PARTE, 'MAPF%d' % PARTE, PART['mappa_fin'], PART['mappa_fin']['voce'])
    dispensa_mappa('mapf%d' % PARTE, PART['mappa_fin'])
    gl = PART['glossario']
    scena_voce('GL%d' % PARTE, 'GL%d' % PARTE, lambda k: SC.glossario(gl, k), PART['voce_gl'], len(gl))
    rf = PART['rf']
    scena_voce('RF%d' % PARTE, 'RF%d' % PARTE, lambda k: SC.rf('Parte %d' % PARTE, rf, k), PART['voce_rf'], len(rf))
    scena_voce('FIN%d' % PARTE, 'FIN%d' % PARTE, lambda k: SC.fine(PARTE, nomi_arg, PART['voce_fin'][0]), PART['voce_fin'], 0, lead=1.0, tail=2.0, extra_audio=[sfx('finale', 0.0, -8)])
    scheda_fissa('VER', 'VER', SC.pausa('Verifica finale', S.TITOLO, 'Test finale della lezione'), 5.0, [sfx('quiz', 0.5, 0)])
    clip_modello('SFIN', 'SFIN', ANCH['sfin'][0], 5.0)
    clip_modello('CINTRO', 'CINTRO', ANCH['cintro'][0], 3.5)
    scheda_fissa('COMP', 'COMP', SC.pausa('Compiti', S.TITOLO, 'Esercizi assegnati dal docente'), 5.0, [])
    if PARTE == 1 and hasattr(S, 'MAPPA_LEZIONE'):
        dispensa_mappa('lez', S.MAPPA_LEZIONE)
    # uscite
    with open('%s/lista_Parte%d.txt' % (W, PARTE), 'w') as f:
        for p in LISTA:
            f.write("file '%s'\n" % p)
    json.dump(TL, open('%s/timeline_Parte%d.json' % (W, PARTE), 'w'))
    json.dump(CUES, open('%s/cues_Parte%d.json' % (W, PARTE), 'w'), ensure_ascii=False)
    tot = POS[0]
    print('Parte %d: %d:%04.1f (%.1f s) · %d scene' % (PARTE, tot // 60, tot % 60, tot, len(TL)))


main()
R.close()
