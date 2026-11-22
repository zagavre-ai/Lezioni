# Pezzi del video (segmenti) · Storia V lez. 3
import os, re, json, subprocess, glob, wave, hashlib
import numpy as np
from PIL import Image
from lib import *
import tpl
from tpl import *
import data as D

ORIG = '/home/user/w3/orig/lez3.mp4'
VOX_NEW = '/home/user/w3/vox_new'          # voci Kore nuove (dalla master)
VOX_OLD = '/home/user/w3/voci/scambio/storia-V-lez03/vox'
VOX_PROV = '/home/user/w3/vox_prov'        # provvisorie (espeak), solo se manca la Kore
ASR_DIR = '/home/user/w3/asr_vox'
SUONI = KIT + '/suoni'
TESTI = {x['nome']: x['testo'] for x in json.load(open('/home/user/w3/voci/scambio/storia-V-lez03/testi_voci.json'))}
os.makedirs(VOX_PROV, exist_ok=True)

# ---------------- voci ----------------
_vc = {}
def voice_path(name):
    for d in (VOX_NEW, VOX_OLD):
        p = f'{d}/{name}.wav'
        if os.path.exists(p): return p, True
    p = f'{VOX_PROV}/{name}.wav'
    if not os.path.exists(p):
        subprocess.run(['espeak-ng', '-v', 'it', '-s', '165', '-w', p, TESTI[name]], check=True)
    return p, False
def voice(name, target=-16.0):
    """float32 mono 48k a -16 LUFS, dissolvenza 30 ms ai bordi; (audio, è_kore)"""
    if name in _vc: return _vc[name]
    p, kore = voice_path(name)
    x = read_wav(p)
    # tolgo il silenzio ai bordi (lascio 60 ms) per controllarlo meglio
    a = np.abs(x); idx = np.where(a > 0.004)[0]
    if len(idx): x = x[max(0, idx[0] - int(0.06 * SR)): idx[-1] + int(0.1 * SR)]
    g = lufs_gain(x, target); x = x * (10 ** (g / 20))
    x = np.clip(x, -0.89, 0.89)
    x = fade(x, 0.03, 0.04)
    _vc[name] = (x, kore); return _vc[name]
def sfx(name, gain=1.0):
    x = read_wav(f'{SUONI}/{name}.wav') * gain
    return x

# tempi delle frasi dentro una voce (da ASR; frazione di caratteri agganciata alle pause)
def asr_words(name):
    p = f'{ASR_DIR}/{name}.json'
    if not os.path.exists(p):
        wp, k = voice_path(name)
        subprocess.run(['python3', '/home/user/w3/build/asr_batch.py', ASR_DIR, wp], check=True, capture_output=True)
        if not os.path.exists(p):
            os.rename(f'{ASR_DIR}/{os.path.basename(wp)[:-4]}.json', p)
    return json.load(open(p))
def sent_times(name, sentences, lead=0.0):
    """tempo d'inizio di ogni frase dentro la voce (secondi dal primo campione della voce ritagliata)"""
    j = asr_words(name); W = [w for w in j['parole']]
    if not W: return [lead + i * 3.0 for i in range(len(sentences))]
    # istanti: inizio del token i; pause = salti > 0.28 s
    toks = [(t, s) for t, s in W]
    cum = np.cumsum([max(1, len(re.sub(r'\W', '', s))) for t, s in toks]); tot = cum[-1]
    chars = [len(re.sub(r'\W', '', s)) for s in sentences]; ctot = sum(chars) or 1
    out = []; acc = 0
    t0 = toks[0][0]
    for k, c in enumerate(chars):
        f = acc / ctot; acc += c
        i = int(np.searchsorted(cum, f * tot)); i = min(i, len(toks) - 1)
        t = toks[i][0]
        # aggancio alla pausa più vicina (inizio di parola dopo un salto)
        best = None
        for q in range(max(0, i - 6), min(len(toks), i + 7)):
            gap = toks[q][0] - (toks[q - 1][0] if q > 0 else toks[0][0] - 1)
            if gap >= 0.28 and (best is None or abs(q - i) < abs(best - i)): best = q
        if best is not None and k > 0: t = toks[best][0]
        out.append(t - t0 + lead)
    out[0] = lead
    for k in range(1, len(out)): out[k] = max(out[k], out[k - 1] + 0.8)
    return out


def subs_voice(vname, offset, parts_split=None):
    """cue dei sottotitoli per una voce Kore: una per frase, tempi dentro il pezzo"""
    x, k = voice(vname); dur_v = len(x) / SR
    sents = parts_split or splitsent(TESTI[vname])
    tm = sent_times(vname, sents, 0.0)
    out = []
    for i, s in enumerate(sents):
        t1 = tm[i + 1] - 0.1 if i + 1 < len(sents) else dur_v
        out.append((offset + tm[i], offset + t1, s, None))
    return out
def subs_seq(vnames, start, gap):
    out = []; t = start
    for v in vnames:
        out += subs_voice(v, t); t += len(voice(v)[0]) / SR + gap
    return out

# ---------------- stati (immagini di sfondo) ----------------
def splitsent(text):
    t = D.digits(text)
    parts = re.split(r'(?<=[.!?])\s+', t.strip())
    return [p for p in parts if p]

def pack_cards(cards, lit, label, title, maxh=None, wide=False):
    maxh = maxh or (958 - tpl.cards_top(label, esc(title)))
    """finestra di card attorno a lit: indici in ordine, altezza misurata <= maxh"""
    n = len(cards)
    def h(idx):
        cs = [cards[i] for i in idx]
        top, bot = height_of(label, title, cs)
        return bot - top
    if lit is None:
        idx = []
        for i in range(n):
            if len(idx) < 3 and h(idx + [i]) <= maxh: idx.append(i)
        return idx or [0]
    idx = [lit]
    for cand in (lit + 1, lit - 1, lit + 2, lit - 2):
        if 0 <= cand < n and cand not in idx and len(idx) < 3:
            t = sorted(idx + [cand])
            if h(t) <= maxh: idx = t
    return sorted(idx)

_slide_cache = {}
def slide_state(label, title, cards, lit, page, kw, cam=True):
    key = hashlib.md5(repr((label, title, cards, lit, page, kw, cam)).encode()).hexdigest()
    if key in _slide_cache: return _slide_cache[key]
    idx = pack_cards(cards, lit, label, title)
    sub = [cards[i] for i in idx]; l2 = None if lit is None else idx.index(lit)
    a = shot(slide_html(label, esc(title), sub, l2, page, kw, cam=cam))
    _slide_cache[key] = (a, idx); return a, idx

def image_state(label, key, page, kw, cam=True):
    p, ttl, cap = D.IMG[key]
    return shot(image_slide_html(label, esc(ttl), p, cap, page, kw, cam=cam))

# ---------------- sfondi scuri animati ----------------
_glow = None
def glow():
    global _glow
    if _glow is None:
        yy, xx = np.mgrid[-450:450, -450:450]; r = np.sqrt(xx ** 2 + yy ** 2) / 450
        g = np.clip(1 - r, 0, 1) ** 2.2
        _glow = g.astype(np.float32)
    return _glow
def dark_base(t):
    base = np.zeros((H, W, 3), np.float32); base[:] = (11, 21, 48)
    g = glow()
    for (cx, cy, col, ph) in ((420, 330, (40, 90, 190), 0.0), (1500, 760, (30, 70, 160), 2.0), (960, 560, (20, 50, 130), 4.0)):
        x = int(cx + 140 * np.sin(t * 0.35 + ph)); y = int(cy + 90 * np.cos(t * 0.28 + ph))
        y0 = max(0, y - 450); y1 = min(H, y + 450); x0 = max(0, x - 450); x1 = min(W, x + 450)
        sub = g[y0 - (y - 450): y1 - (y - 450), x0 - (x - 450): x1 - (x - 450)]
        base[y0:y1, x0:x1] += sub[:, :, None] * np.array(col, np.float32) * 0.9
    return np.clip(base, 0, 255).astype(np.uint8)
def shot_rgba(html):
    pg = page(); pg.set_content(html); pg.evaluate('document.fonts.ready'); pg.wait_for_timeout(60)
    return np.asarray(Image.open(__import__('io').BytesIO(pg.screenshot(type='png', omit_background=True))).convert('RGBA'))
DARK_T = tpl.DARK.replace('html,body{background:#0B1530}', 'html,body{background:transparent}').replace('.dk{', '.dk{display:none;')
def dark_text(label, title, sub=None, extra=''):
    s = f'<div class="ds" style="top:430px">{esc(sub)}</div>' if sub else ''
    h = f'<!doctype html><html><head><meta charset="utf-8"><style>{DARK_T}</style></head><body>' \
        f'<div class="dl">{esc(label)}</div><div class="dt">{title}</div><div class="bar"></div>{s}{extra}' \
        f'<div class="dfoot">{MATERIA}</div><div class="dlogo">{tpl.LOGO_W}</div></body></html>'
    return shot_rgba(h)
def comp(base, layer, a=1.0):
    al = (layer[:, :, 3:4].astype(np.uint16) * int(256 * a)) >> 8
    return ((base.astype(np.uint16) * (256 - al) + layer[:, :, :3].astype(np.uint16) * al) >> 8).astype(np.uint8)

def dark_frame_fn(layers):
    """layers: [(t_inizio, rgba)]; ogni livello sostituisce il precedente con dissolvenza 0.3 s; sfondo animato"""
    def f(i):
        t = i / FPS; base = dark_base(t)
        k = -1
        for j, (ts, _) in enumerate(layers):
            if t >= ts: k = j
        if k < 0: return base
        ts, lay = layers[k]; u = min(1.0, (t - ts) / 0.3)
        if k > 0 and u < 1: base = comp(base, layers[k - 1][1], 1 - u)
        return comp(base, lay, u)
    return f

def dur_frames(s): return int(round(s * FPS))

# ---------------- segmenti ----------------
def mix(n, parts):
    a = np.zeros(n * SPF, np.float32)
    for t, x in parts:
        k = int(t * SR); e = min(len(a), k + len(x))
        if k < len(a): a[k:e] += x[:e - k]
    return a

def seg_dark_title(label, title, nsec=4.4, jingle='titolo', name='T', sub=None):
    n = dur_frames(nsec); lay = dark_text(label, esc(title), sub)
    f = dark_frame_fn([(0.5, lay)])
    j = sfx(jingle, 0.9)
    a = mix(n, [(0.9, j)])
    return Seg(n, a, f, name=name, first_word=0.9, last_word=0.9 + len(j) / SR, kind='dark')

def seg_quiz(title, name, nsec=5.5, extra_sub="5 domande · per continuare serve almeno l'80%", jingle='quiz'):
    n = dur_frames(nsec); lay = dark_text('QUIZ' if name.startswith('Q') else 'VERIFICA', esc(title), extra_sub)
    f = dark_frame_fn([(0.5, lay)])
    j = sfx(jingle, 0.9)
    a = mix(n, [(1.0, j)])  # scatto a +0,5 s dalla scheda (la scheda comincia a 0,5 s con la dissolvenza)
    return Seg(n, a, f, name=name, first_word=1.0, last_word=1.0 + len(j) / SR, kind='quiz')

# ---- pezzi con voce Kore e schede a comparsa ----
def seg_voice_cards(name, vname_list, label, title, sentence_lists, page_title=None, lead=0.9, tail=0.8, rep_extra=None, wide=True):
    """Voce (o più voci in fila) + card bianche che compaiono con la voce. sentence_lists: una lista di frasi per voce"""
    raise NotImplementedError

def build_cards_timeline(label, title, sents, times, total, maxh=650):
    """frasi con tempi d'ingresso -> pagine di card (max 3 visibili, altezza misurata); restituisce stati [(t, array)]"""
    states = [(0.0, shot(frame_wide(label, title, [], None)))]
    page_cards = []; pg_start = 0
    for k, s in enumerate(sents):
        cand = page_cards + [s]
        top, bot = height_of_wide(label, title, cand)
        if page_cards and (len(cand) > 3 or bot - top > maxh):
            page_cards = [s]
        else:
            page_cards = cand
        states.append((times[k], shot(frame_wide(label, title, page_cards, len(page_cards) - 1))))
    return states

def frame_wide(label, title, cards, lit):
    top = tpl.cards_top(label, esc(title))
    body = cards_html(cards, lit, top).replace(f'class="cards" style="top:{top}px"', f'class="cards" style="top:{top}px;width:1760px"') if cards else ''
    css = '<style>.card{font-size:38px !important}</style>'
    return tpl.frame(label, esc(title), body + css, None, cam=False)
def height_of_wide(label, title, cards):
    h = frame_wide(label, title, cards, None)
    top, bot = measure(h, "(()=>{const c=document.querySelector('.cards');if(!c)return [300,300];const r=c.getBoundingClientRect();return [r.top,r.bottom]})()")
    return top, bot

def trim_voice(an, x, maxs=60.0):
    """se la voce supera maxs secondi: taglia nella pausa più silenziosa vicina alla fine di una frase; restituisce (x, n_frasi_intere)"""
    sents = splitsent(TESTI[an]); tm = sent_times(an, sents, 0.0)
    dur_v = len(x) / SR
    if dur_v <= maxs: return x, len(sents)
    # fine della frase k = inizio frase k+1; scelgo l'ultima che finisce prima di maxs
    k = max(i for i in range(len(sents) - 1) if tm[i + 1] <= maxs - 0.3)
    c = tm[k + 1]; lo = int((c - 1.2) * SR); hi = int((c + 0.6) * SR)
    env = np.convolve(np.abs(x[lo:hi]), np.ones(int(0.08 * SR)) / int(0.08 * SR), 'same')
    cut = lo + int(np.argmin(env[int(0.2 * SR):-int(0.1 * SR)])) + int(0.2 * SR)
    return fade(x[:cut + int(0.05 * SR)], 0.03, 0.05), k + 1

def seg_ap(an, label='APPROFONDIMENTO', lead=0.9, tail=0.9, maxs=None):
    x, kore = voice(an)
    x, nfull = trim_voice(an, x)
    sents = splitsent(TESTI[an])[:nfull]
    title = sents[0].rstrip('.?!')
    body = sents[1:]
    dur = len(x) / SR
    times = sent_times(an, splitsent(TESTI[an]), lead)[:nfull][1:]
    n = dur_frames(lead + dur + tail)
    states = build_cards_timeline(label, title, body, times, dur + lead + tail)
    f = states_frame(states, 0.3)
    a = mix(n, [(lead, x)])
    sg = Seg(n, a, f, name=an, first_word=lead, last_word=lead + dur, kind='ap')
    sg.key = 'v2' if an == 'AN22' else ''
    sg.subs = [s for s in subs_voice(an, lead)[:nfull]]
    if nfull: sg.subs[-1] = (sg.subs[-1][0], lead + dur, sg.subs[-1][2], None)
    return sg

def seg_voice_plain(vname, lead=0.9, tail=0.8):
    x, k = voice(vname); return x

# ---------------- mappe del prof ----------------
MAPS = {
 1: dict(title="Quale svolta imprime Giolitti alla vita politica italiana?", voices=['MP1_1', 'MP1_2', 'MP1_3', 'MP1_4', 'MP1_5', 'MP1_6', 'MP1_7'],
   nodes=[  # id, testo, classe, x,y,w,h, freccia (da id, etichetta)
    ('N1', 'LA «CRISI DI FINE SECOLO»', 'l1', 600, 190, 720, 96, None),
    ('N2', 'la vittoria dei liberali progressisti', 'pag', 560, 372, 800, 100, ('N1', 'si risolve con')),
    ('N3', 'Giolitti', 'pag', 760, 558, 400, 92, ('N2', 'che con')),
    ('N4', "ministro dell'Interno (1901)", 'cel', 100, 756, 760, 92, ('N3', 'da')),
    ('N5', 'la neutralità nei conflitti sociali', 'pag', 100, 920, 760, 92, ('N4', 'sceglie')),
    ('N6', 'presidente del Consiglio (1903-1914)', 'cel', 1060, 756, 760, 92, ('N3', 'da')),
    ('N7', 'riforme a favore dei ceti popolari', 'lil', 1060, 920, 760, 92, ('N6', 'introduce'))]),
}

# ---------------- il prof ----------------
S = D.S
_clean = None
def clean_audio():
    global _clean
    if _clean is None:
        x = np.load('/home/user/w3/orig/clean_nr6.npy')
        g = lufs_gain(x[int(150 * SR):int(1100 * SR)], -16.0)
        _clean = (x * (10 ** (g / 20))).astype(np.float32)
    return _clean
def q30(t): return round(t * FPS) / FPS

def ranges_for(a, b, long_gap=2.5, keep=0.5):
    gb = S[a]['inizio'] - S[a - 1]['fine'] if a > 0 else 1.0
    ga = S[b + 1]['inizio'] - S[b]['fine'] if b + 1 < len(S) else 1.0
    ph = max(0.2, min(0.7, gb - 0.12)); pt = max(0.2, min(0.7, ga - 0.12))
    cut = []; cur = q30(S[a]['inizio'] - ph)
    for i in range(a, b):
        gap = S[i + 1]['inizio'] - S[i]['fine']
        if gap > long_gap:
            cut.append((cur, q30(S[i]['fine'] + keep))); cur = q30(S[i + 1]['inizio'] - keep)
    cut.append((cur, q30(S[b]['fine'] + pt)))
    return cut, ph, pt

def src2out_fn(rngs):
    offs = []; acc = 0.0
    for a, b in rngs: offs.append(acc); acc += round((b - a) * FPS) / FPS
    def f(t):
        for (a, b), o in zip(rngs, offs):
            if a - 1e-6 <= t <= b + 1e-6: return o + (t - a)
        # fuori da un intervallo: aggancia al più vicino
        best = min(range(len(rngs)), key=lambda k: min(abs(t - rngs[k][0]), abs(t - rngs[k][1])))
        a, b = rngs[best]; return offs[best] + (0 if t < a else (b - a))
    return f, acc

def seg_teacher(a, b, states_src, name, cam=True, nocam_until=None):
    """a,b: indici delle frasi (VAD) del prof, inclusi. states_src: [(t_sorgente, array_sfondo_senza_prof)]"""
    rngs, ph, pt = ranges_for(a, b)
    f_o, total = src2out_fn(rngs)
    n = int(round(total * FPS))
    states = [(0.0 if k == 0 else f_o(t), arr) for k, (t, arr) in enumerate(states_src)]
    # elimina stati con tempi non crescenti
    clean = [states[0]]
    for t, arr in states[1:]:
        if t > clean[-1][0] + 0.05: clean.append((t, arr))
    bgf = states_frame(clean, 0.25)
    gen = CamReader(ORIG, rngs).frames()
    def frame(i):
        bg = bgf(i); cm = next(gen)
        return paste_cam(bg, cm) if cam else bg
    # audio: pulito dall'originale, solo il parlato (padding muto)
    x = clean_audio(); parts = []; acc = 0.0
    first = f_o(S[a]['inizio']); last = f_o(S[b]['fine'])
    for ra, rb in rngs:
        k = int(round((rb - ra) * FPS)); seg = x[int(round(ra * SR)): int(round(ra * SR)) + k * SPF].copy()
        parts.append(seg)
    aud = np.concatenate(parts)
    # muto i bordi fuori dal parlato
    m0 = int(max(0, first - 0.03) * SR); aud[:m0] = 0
    m1 = int((last + 0.04) * SR); aud[m1:] = 0
    aud[m0:m0 + int(0.03 * SR)] *= np.linspace(0, 1, int(0.03 * SR), dtype=np.float32)[:len(aud[m0:m0 + int(0.03 * SR)])]
    sg = Seg(n, aud, frame, name=name, first_word=first, last_word=last, kind='prof')
    sg.pad_head = first; sg.pad_tail = n / FPS - last
    sg.src = (S[a]['inizio'], S[b]['fine']); sg.a = a; sg.b = b
    sg.subs = [(f_o(S[i]['inizio']), f_o(S[i]['fine']), S[i]['testo'], S[i].get('parole')) for i in range(a, b + 1)]
    sg.lastwords = ' '.join(S[b]['testo'].split()[-8:])
    return sg

def split_blocks(a, b, mids):
    """mids: indici j dopo cui si taglia (cut dopo S[j]). -> [(a1,b1),(a2,b2),...]"""
    out = []; s = a
    for j in sorted(mids):
        out.append((s, j)); s = j + 1
    out.append((s, b)); return out

PAGES = []
def arg_pages(arg, page0):
    """costruisce, per un argomento, i blocchi del prof con le slide a finestra; restituisce lista di elementi:
       ('prof', Seg) | ('mid', 'ANk')   e il prossimo numero di pagina"""
    A = D.ARG[arg]; ev = D.EV[arg]
    label = f'{arg:02d} · Argomento'; title, cards = D.card_list(arg); kw = A['kw']
    mids = []
    for e in ev:
        if e[0] == 'mid': mids.append((D.snap_cut(e[1], A['a'] + 1, A['b'] - 1), e[2]))
    mids.sort()
    blocks = split_blocks(A['a'], A['b'], [j for j, _ in mids])
    cardev = sorted([(e[1], e[2]) for e in ev if e[0] == 'card'])
    imgev = [(e[1], e[2], e[3]) for e in ev if e[0] == 'img']
    items = []; page = page0
    lit = None
    for bi, (ba, bb) in enumerate(blocks):
        t0 = S[ba]['inizio']; t1 = S[bb]['fine']
        # eventi nel blocco: (t, tipo, dato)
        evs = [(t, 'card', i) for t, i in cardev if t0 - 0.3 <= t < t1] + [(max(t0, s0), 'img', k) for s0, s1, k in imgev if s1 > t0 and s0 < t1] \
            + [(s1, 'imgend', k) for s0, s1, k in imgev if t0 < s1 < t1]
        # luce attuale all'inizio del blocco
        cur = None
        for t, i in cardev:
            if t < t0 + 0.05: cur = i
        evs.sort()
        states = []; pg = page
        def add(t, lit_idx, img=None):
            nonlocal pg
            if img:
                arr = image_state(label, img, pg, kw)
                PAGES.append(dict(page=pg, kind='img', label=label, title=D.IMG[img][1], img=img, kw=kw, arg=arg))
            else:
                arr, idx = slide_state(label, title, cards, lit_idx, pg, kw)
                PAGES.append(dict(page=pg, kind='slide', label=label, title=title, idx=idx, lit=lit_idx, cards=cards, kw=kw, arg=arg))
            states.append((t, arr)); pg += 1
        # stato iniziale
        init_img = None
        for t, k, d in evs:
            if k == 'img' and t <= t0 + 0.2: init_img = d
        add(t0, cur, init_img)
        active_img = init_img
        for t, k, d in evs:
            if k == 'card':
                cur = d
                if active_img is None and t > t0 + 0.2: add(t, cur)
            elif k == 'img' and t > t0 + 0.2:
                active_img = d; add(t, cur, d)
            elif k == 'imgend':
                active_img = None
                if not any(0 <= tt - t < 1.0 for tt, kk, dd in evs if kk == 'card'): add(t, cur)
        sg = seg_teacher(ba, bb, states, f'A{arg}' + (f'_{bi + 1}' if len(blocks) > 1 else ''))
        items.append(('prof', sg))
        page = pg
        if bi < len(mids): items.append(('mid', mids[bi][1]))
    return items, page

# ---------------- copertina, argomenti, schede ----------------
QUIZ = json.load(open('/home/user/w3/rev/revisione-storia-V-lez03/quiz_argomenti.json'))
COMPITI = json.load(open('/home/user/w3/rev/revisione-storia-V-lez03/compiti.json'))
def cover_html(args, cam):
    items = ''.join(f'<div style="display:flex;gap:18px;margin:7px 0"><span style="font:800 32px Fig;color:#2060AF;width:46px">{n:02d}</span><span>{esc(D.ARG[n]["titolo"])}</span></div>' for n in args)
    body = f'<div style="position:absolute;left:80px;top:560px;width:1290px;border:3px solid #D5DEEC;border-radius:20px;padding:20px 34px;background:#F8FAFD;box-shadow:0 10px 26px rgba(70,85,110,.13);font:500 32px/1.3 Fig">' \
           f'<div style="font:800 22px Fig;letter-spacing:.16em;color:#2060AF;margin-bottom:10px">ARGOMENTI</div>{items}</div>'
    h = tpl.frame('STORIA V · VIDEOLEZIONE', "L'Italia<br>di Giolitti", body, None, cam=cam)
    return h.replace('</style>', '.tit{font-size:112px !important;line-height:1.02 !important;top:190px !important}</style>', 1)
def cover_state(args, cam): return shot(cover_html(args, cam))

def seg_cover_voice(args, vname='BEN_R2', lead=0.9, tail=1.0):
    x, kore = voice(vname); dur = len(x) / SR; n = dur_frames(lead + dur + tail)
    a = cover_state(args, False)
    return Seg(n, mix(n, [(lead, x)]), states_frame([(0, a)]), name='COVERV', first_word=lead, last_word=lead + dur)

def seg_intro_prof(args, a, b):
    """introduzione del prof sopra la copertina: il riquadro compare solo quando il prof comincia a parlare"""
    nocam = cover_state(args, False); withcam = cover_state(args, True)
    rngs, ph, pt = ranges_for(a, b)
    first_out = ph
    return seg_teacher(a, b, [(rngs[0][0], nocam), (S[a]['inizio'] - 0.35, withcam)], 'D0')

def seg_dic(part, ids, vname):
    x, kore = voice(vname); dur = len(x) / SR; lead = 0.9; tail = 1.2
    text = TESTI[vname]; parts = re.split(r'[;:]\s*', text.replace('. In questa', ': In questa'))
    parts = [p for p in parts]
    # parts[0] = intro, poi uno per argomento
    sents = [D.ARG[n]['titolo'] for n in ids]
    times = sent_times(vname, parts, lead)[1:1 + len(ids)]
    n = dur_frames(lead + dur + tail)
    states = build_cards_timeline('DI COSA PARLIAMO', 'Di cosa parliamo', [f'{k:02d} · {s}' for k, s in zip(ids, sents)], times, dur)
    return Seg(n, mix(n, [(lead, x)]), states_frame(states, 0.3), name='DIC', first_word=lead, last_word=lead + dur)

def seg_pillola_intro(arg):
    vn = f'PIL{arg}'; x, kore = voice(vn); dur = len(x) / SR
    jin = sfx('repaso', 0.9); lead = 0.9; vstart = 4.2
    n = dur_frames(vstart + dur + 0.9)
    lay = dark_text('PILLOLA DI RIPASSO', esc(D.ARG[arg]['titolo']), 'Guarda lo schema e ripeti ad alta voce')
    return Seg(n, mix(n, [(lead, jin), (vstart, x)]), dark_frame_fn([(0.5, lay)]), name=f'PI{arg}', first_word=lead, last_word=vstart + dur)

def seg_pillola_schema(arg):
    k = 1; vs = []
    while True:
        nm = f'PS{arg}_{k}'
        if nm not in TESTI: break
        vs.append(nm); k += 1
    lead = 0.9; t = lead; parts = []; times = []; sents = []
    for nm in vs:
        x, kore = voice(nm); times.append(t); parts.append((t, x)); sents.append(D.digits(TESTI[nm])); t += len(x) / SR + 0.55
    total = t + 0.6
    n = dur_frames(total)
    states = [(0.0, shot(frame_wide('RIPASSO', D.ARG[arg]['titolo'], [], None)))]
    for k in range(len(vs)):
        shown = sents[:k + 1]
        # fino a 6 righe, finestra se troppo alte
        while height_of_wide('RIPASSO', D.ARG[arg]['titolo'], shown)[1] - height_of_wide('RIPASSO', D.ARG[arg]['titolo'], shown)[0] > 650 and len(shown) > 1: shown = shown[1:]
        states.append((times[k], shot(frame_wide('RIPASSO', D.ARG[arg]['titolo'], shown, len(shown) - 1))))
    return Seg(n, mix(n, parts), states_frame(states, 0.3), name=f'PS{arg}', first_word=lead, last_word=t - 0.55)

def seg_map(m, part_label='MAPPA DEL PROFESSORE'):
    import maps
    M = maps.MAPS[m]; lead = 0.9; t = lead; parts = []; states = [(0.0, shot(maps.map_html(M, 0, None)))]
    for k, vn in enumerate(M['voices']):
        x, kore = voice(vn)
        if k == 0: states.append((t, shot(maps.map_html(M, 1, 'N1'))))
        else: states.append((t, shot(maps.map_html(M, k + 1, M['nodes'][k][0]))))
        parts.append((t, x)); t += len(x) / SR + 0.7
    end_voice = t - 0.7
    states.append((end_voice + 0.4, shot(maps.map_html(M, len(M['nodes']), None))))
    total = end_voice + 0.4 + 4.0 + 0.4
    n = dur_frames(total)
    # sottofondo leggerissimo durante la mappa intera ferma (niente silenzio oltre 2,5 s)
    hold = total - end_voice - 0.5; tt = np.arange(int(hold * SR)) / SR
    pad = (0.5 * np.sin(2 * np.pi * 220 * tt) + 0.35 * np.sin(2 * np.pi * 329.6 * tt) + 0.25 * np.sin(2 * np.pi * 440 * tt)).astype(np.float32) * 0.03
    pad = fade(pad, 0.6, 0.6)
    parts.append((end_voice + 0.3, pad))
    return Seg(n, mix(n, parts), states_frame(states, 0.35), name=f'MAP{m}', first_word=lead, last_word=end_voice)

def seg_quiz_arg(arg):
    return seg_quiz(QUIZ[f'Q{arg}']['title'], f'Q{arg}')

def seg_list_voice(vname, label, title, skip_first=True, split_colon=False):
    x, kore = voice(vname); dur = len(x) / SR; lead = 0.9; tail = 1.0
    sents = splitsent(TESTI[vname])
    body = sents[1:] if skip_first else sents
    times = sent_times(vname, sents, lead)[(1 if skip_first else 0):]
    n = dur_frames(lead + dur + tail)
    states = build_cards_timeline(label, title, body, times, dur)
    return Seg(n, mix(n, [(lead, x)]), states_frame(states, 0.3), name=vname, first_word=lead, last_word=lead + dur)

def seg_fin_voice(vname, sub):
    x, kore = voice(vname); dur = len(x) / SR; lead = 0.9; n = dur_frames(lead + dur + 1.0)
    lay = dark_text('A PRESTO', esc(D.TITOLO), sub)
    return Seg(n, mix(n, [(lead, x)]), dark_frame_fn([(0.4, lay)]), name=vname, first_word=lead, last_word=lead + dur)

def seg_mp4(path, name, gain=1.0):
    dur_s = dur(path); n = int(round(dur_s * FPS))
    aud = read_wav(path) * gain
    cmd = ['ffmpeg', '-v', 'error', '-i', path, '-vf', f'scale={W}:{H},fps={FPS}', '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-']
    pr = subprocess.Popen(cmd, stdout=subprocess.PIPE); fs = W * H * 3; last = [None]
    def frame(i):
        b = pr.stdout.read(fs)
        if len(b) == fs: last[0] = np.frombuffer(b, np.uint8).reshape(H, W, 3)
        return last[0] if last[0] is not None else np.zeros((H, W, 3), np.uint8)
    sg = Seg(n, aud, frame, name=name, first_word=0.0, last_word=dur_s - 0.2, kind='mp4')
    sg.pad_head = 0.5; sg.pad_tail = 0.5
    return sg

def seg_verifica(title):
    return seg_quiz(title, 'VF', extra_sub="Per continuare serve almeno l'80%")

def seg_compiti():
    out = []
    n = dur_frames(3.9); lay = dark_text('COMPITI', 'Compiti', 'Adesso tocca a te')
    j = sfx('titolo', 0.9)
    out.append(Seg(n, mix(n, [(0.5, j)]), dark_frame_fn([(0.3, lay)]), name='COMPITI_I', first_word=0.5, last_word=0.5 + len(j) / SR))
    x, kore = voice('CMP_1'); dur_v = len(x) / SR
    ex = [e['testo'] for e in COMPITI['esercizi']]
    lead = 0.9; tail = 1.0
    # tempi per domanda (frazione di testo)
    sents = [f'Compito {i + 1}: ' + t if False else t for i, t in enumerate(ex)]
    parts = re.split(r'(?<=[.?!])\s+(?=(?:Primo|Secondo|Terzo|Quarto)\.)', TESTI['CMP_1'])
    times = sent_times('CMP_1', parts, lead)[1:5] if len(parts) >= 5 else [lead + k * dur_v / 4 for k in range(4)]
    n = dur_frames(lead + dur_v + tail)
    states = [(0.0, shot(frame_wide('COMPITI', 'Compiti del professore', [], None)))]
    shown = []
    for k, t in enumerate(sents):
        shown = (shown + [(f'Compito {k + 1}: ' + t)])[-2:]
        states.append((times[k], shot(frame_wide('COMPITI', 'Compiti del professore', shown, len(shown) - 1))))
    out.append(Seg(n, mix(n, [(lead, x)]), states_frame(states, 0.3), name='COMPITI', first_word=lead, last_word=lead + dur_v))
    return out

# ---------------- spiegone ----------------
def spiegone_html(title, img, sents, lit):
    cards = ''
    for i, t in enumerate(sents):
        cls = 'card on' if i == lit else 'card'
        cards += f'<div class="{cls}" style="font-size:36px;padding-left:44px"><span class="dot" style="top:30px"></span>{esc(t)}</div>'
    if img:
        left = f'<div style="position:absolute;left:80px;top:300px;width:720px;height:640px;display:flex;align-items:center;justify-content:center"><img src="{b64img(img)}" style="max-width:720px;max-height:620px;border-radius:14px;box-shadow:0 10px 26px rgba(70,85,110,.2);border:3px solid #D5DEEC"></div>'
        cx, cw = 840, 1000
    else:
        left = ''; cx, cw = 80, 1760
    body = left + f'<div class="cards" style="top:300px;left:{cx}px;width:{cw}px">{cards}</div>'
    return tpl.frame('RIPASSO DELLA PARTE PRECEDENTE', esc(title), body, None, cam=False)

def seg_spiegone(args, imgs, name='SPIEGONE', cover_args=None):
    """imgs: {arg: percorso immagine o None}. Voce SPG_0 + R<arg> (voci Kore esistenti), immagini e mappe della Parte precedente."""
    x0, k0 = voice('SPG_0'); lead = 0.9
    t = lead; parts = [(t, x0)]
    d0 = dark_text('SPIEGONE', 'Ripasso della parte precedente', 'Argomento per argomento')
    states = [(0.0, cover_state(cover_args, False) if cover_args else comp(dark_base(0.0), d0))]
    t += len(x0) / SR + 0.8
    for a in args:
        x, kr = voice(f'R{a}'); sents = splitsent(TESTI[f'R{a}']); sents = [s for s in sents if not s.lower().startswith('ripassiamo')] or sents
        tm = sent_times(f'R{a}', splitsent(TESTI[f'R{a}']), 0.0)[-len(sents):]
        parts.append((t, x))
        for k in range(len(sents)):
            states.append((t + tm[k], shot(spiegone_html(D.ARG[a]['titolo'], imgs.get(a), sents[:k + 1][-3:], min(k, 2)))))
        states.insert(len(states) - len(sents), (t - 0.05, shot(spiegone_html(D.ARG[a]['titolo'], imgs.get(a), [], None))))
        t += len(x) / SR + 0.9
    total = t + 0.4; n = dur_frames(total)
    sg = Seg(n, mix(n, parts), states_frame(states, 0.3), name=name, first_word=lead, last_word=t - 0.9); sg.key = 'cover1' if cover_args else ''; return sg
