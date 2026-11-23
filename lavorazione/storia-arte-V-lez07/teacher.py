# Pezzi del docente: slide sincronizzate + riquadro 4:3 + audio pulito, tagli solo nelle pause
import os, json, sys, subprocess, wave, math, hashlib
import numpy as np
sys.path.insert(0, '/tmp/claude-0/w/build')
from gfx import *
import spec

R = '/tmp/claude-0/w/lez07/'
OUT = '/tmp/claude-0/w/out/'
os.makedirs(OUT + 'states', exist_ok=True); os.makedirs(OUT + 'teacher', exist_ok=True)
FPS = 30; SR = 48000

def load_wav(p):
    w = wave.open(p); a = np.frombuffer(w.readframes(w.getnframes()), np.int16).astype(np.float32) / 32768
    if w.getnchannels() == 2: a = a.reshape(-1, 2).mean(1)
    return a
def save_wav(p, a, sr=SR):
    w = wave.open(p, 'wb'); w.setnchannels(1); w.setsampwidth(2); w.setframerate(sr)
    w.writeframes((np.clip(a, -1, 1) * 32767).astype(np.int16).tobytes()); w.close()

_orig = None
def orig():
    global _orig
    if _orig is None: _orig = load_wav(R + 'doc_orig.wav')
    return _orig

def rms_db(a, s, e):
    seg = a[int(s * SR):int(e * SR)]
    return 20 * math.log10(float(np.sqrt((seg ** 2).mean())) + 1e-9) if len(seg) else -99

def snap(t, lo, hi, a):
    """sposta il taglio t (s) nel punto piu' silenzioso (finestra 60 ms) tra lo e hi"""
    best = (99, t)
    x = lo
    while x <= hi:
        v = rms_db(a, x - 0.03, x + 0.03)
        if v < best[0] - 0.5 or (abs(v - best[0]) <= 0.5 and abs(x - t) < abs(best[1] - t)): best = (v, x)
        x += 0.01
    return best[1], best[0]

# tagli espliciti dentro il pezzo (secondi sorgente): pausa lunga 2,93 s -> 1 s ; il docente si sposta ("Pazienza, io mi sposto...")
CUTS = [(1058.3, 1060.2), (1442.3, 1453.9)]

def bounds():
    a = orig(); T = spec.T; res = []
    for i, t in enumerate(T):
        s0, e0 = t['t']
        nxt = T[i + 1]['t'][0] if i + 1 < len(T) else 2290
        prv = T[i - 1]['t'][1] if i else 0
        s, vs = snap(s0 - 0.2, max(prv + 0.15, s0 - 0.6), s0 - 0.05, a)
        e, ve = snap(e0 + 0.3, e0 + 0.08, min(e0 + (0.30 if t['n'] == 6 else 0.8), nxt - 0.12), a)
        res.append((s, e, vs, ve))
    return res

def keep_frames(s, e):
    """intervalli (fotogrammi sorgente) tenuti, tolti i tagli interni"""
    f0, f1 = round(s * FPS), round(e * FPS); iv = [(f0, f1)]
    for cs, ce in CUTS:
        c0, c1 = round(cs * FPS), round(ce * FPS); out = []
        for a, b in iv:
            if c1 <= a or c0 >= b: out.append((a, b)); continue
            if a < c0: out.append((a, c0))
            if c1 < b: out.append((c1, b))
        iv = out
    return iv

def mapper(iv):
    def m(t):
        f = round(t * FPS); n = 0
        for a, b in iv:
            if f >= b: n += b - a
            elif f >= a: return n + f - a
            else: return n
        return n
    return m

# ---------------------------------------------------------------- schermate
PAGES = {}      # identita' -> numero di pagina
def page_no(key):
    if key not in PAGES: PAGES[key] = len(PAGES) + 2   # la 1 e' la copertina
    return PAGES[key]

def header_for(im, t, size_hint=None):
    d = ImageDraw.Draw(im)
    title = spec.ptitle(t['pdf']); over = '%02d · %s' % (t['n'], t['short'])
    for sz in (64, 58, 52):
        if len(wrap(d, title, F('title', sz), 1300)) == 1: break
    else: sz = 52
    return header(im, over, title, size=sz, maxw=1300)

def build_screens(t):
    """ordine e raggruppamento delle card (max 3, e devono stare nella pagina): ritorna screens=[[idx..]], card_screen{idx:screen}"""
    im = Image.new('RGBA', (W, H)); d = ImageDraw.Draw(im)
    ycs = header_for(im, t); cs = spec.cards(t['pdf'])
    screens = []; cur = []; used = 0
    for idx, _ in t['cards']:
        h = card_height(d, cs[idx]) + (24 if cur else 0)
        if cur and (len(cur) >= 3 or ycs + used + h > 950): screens.append(cur); cur = []; used = 0; h = card_height(d, cs[idx])
        cur.append(idx); used += h
    if cur: screens.append(cur)
    return screens, ycs

def render_state(t, st, screens, ycs, page, with_box_shadow=True):
    cs = spec.cards(t['pdf'])
    im = new_slide()
    if st[0] == 'title':
        d = ImageDraw.Draw(im)
        title = spec.ptitle(t['pdf']); over = '%02d · %s' % (t['n'], t['short'])
        spaced(d, (80, 148), over.upper(), F('xbold', 24), BLUE, 4)
        fs = 76 if t['n'] == 1 else 84; f = F('title', fs); y = 260 if t['n'] == 1 else 300
        for ln in wrap(d, title, f, 1260): d.text((80, y), ln, font=f, fill=NAVY); y += int(fs * 1.1)
        d.rounded_rectangle((80, y + 14, 165, y + 20), 3, fill=BLUE)
        if t['n'] == 1:
            y += 50
            shadow(im, (80, y, 1080, y + 340), r=22, blur=18, off=(0, 8), alpha=40)
            d = ImageDraw.Draw(im); d.rounded_rectangle((80, y, 1080, y + 340), 22, fill=(247, 249, 253), outline=(222, 228, 238), width=2)
            spaced(d, (118, y + 26), 'ARGOMENTI DELLA LEZIONE', F('xbold', 22), BLUE, 4)
            yy = y + 74
            for tt in spec.T:
                d.ellipse((124, yy + 14, 136, yy + 26), fill=BLUE); d.text((152, yy), tt['short'], font=F('semi', 30), fill=NAVY); yy += 38
    elif st[0] == 'img':
        header_small(im, t)
        draw_artwork(im, R + 'opere2/%s.png' % st[1], spec.CAP[st[1]], area=(80, 215, 1380, 905))
    else:
        _, si, states = st
        ycs_ = header_for(im, t); d = ImageDraw.Draw(im)
        lay = card_layout(d, [cs[i] for i in screens[si]], ycs_)
        for l, s in zip(lay, states): draw_card(im, l, s)
    right_column(im, t['kw'])
    footer(im, page)
    return im

def header_small(im, t):
    d = ImageDraw.Draw(im)
    spaced(d, (80, 148), ('%02d · %s' % (t['n'], t['short'])).upper(), F('xbold', 24), BLUE, 4)

def state_png(t, st, screens, ycs, page):
    key = '%d_%s.png' % (t['n'], hashlib.md5((json.dumps(st, default=str) + str(page)).encode()).hexdigest()[:10])
    p = OUT + 'states/' + key
    if not os.path.exists(p): render_state(t, st, screens, ycs, page).convert('RGB').save(p)
    return p

def timeline_states(t, m, nout):
    """lista (frame_uscita, stato, label) in ordine; stato card = ('cards', schermata, (stati...))"""
    screens, ycs = build_screens(t)
    scr_of = {i: si for si, s in enumerate(screens) for i in s}
    ev = [(m(ts), 'card', idx) for idx, ts in t['cards']] + [(m(ts), 'img', nm) for ts, nm in t['imgs']]
    ev.sort(key=lambda x: x[0])
    seq = [(0, ('title',), 'title')]; lit = {}; cur_screen = None
    for f, k, a in ev:
        if k == 'img': seq.append((f, ('img', a), 'img:' + a)); continue
        si = scr_of[a]
        if si != cur_screen:   # nuova schermata: le card delle schermate precedenti non contano
            cur_screen = si
        lit.setdefault(si, {})
        for j in list(lit[si]):
            if lit[si][j] == 2: lit[si][j] = 1
        lit[si][a] = 2
        states = tuple(lit[si].get(i, 0) for i in screens[si])
        seq.append((f, ('cards', si, states), 'card:%d' % a))
    return seq, screens, ycs

_pg = False
def ensure_pages():
    global _pg
    if _pg: return
    _pg = True
    B = bounds()
    for j, t in enumerate(spec.T):
        iv = keep_frames(B[j][0], B[j][1]); m = mapper(iv)
        seq, screens, ycs = timeline_states(t, m, sum(y - x for x, y in iv))
        for f, st, lab in seq:
            key = (t['n'], 'title') if st[0] == 'title' else ((t['n'], 'img', st[1]) if st[0] == 'img' else (t['n'], 'cards', st[1]))
            page_no(key)

def build_topic(i, force=False):
    ensure_pages()
    t = spec.T[i]; a = orig(); b = bounds()[i]; s, e = b[0], b[1]
    iv = keep_frames(s, e); m = mapper(iv); nout = sum(y - x for x, y in iv)
    seq, screens, ycs = timeline_states(t, m, nout)
    # numeri di pagina in ordine di prima comparsa
    states = []
    for k, (f, st, lab) in enumerate(seq):
        key = (t['n'], 'title') if st[0] == 'title' else ((t['n'], 'img', st[1]) if st[0] == 'img' else (t['n'], 'cards', st[1]))
        states.append((f, st, lab, page_no(key)))
    out = OUT + 'teacher/T%d.mp4' % t['n']
    info = dict(n=t['n'], src=(s, e), iv=iv, frames=nout, states=[(f, lab, pg) for f, st, lab, pg in states])
    wav = []
    for x, y in iv: wav.append(proc_audio()[x * 1600:y * 1600].copy())
    for k in range(1, len(wav)):   # sfumature di 15 ms ai punti di giunzione
        n = int(.015 * SR); wav[k - 1][-n:] *= np.linspace(1, 0, n); wav[k][:n] *= np.linspace(0, 1, n)
    audio = np.concatenate(wav); assert len(audio) == nout * 1600, (len(audio), nout * 1600)
    save_wav(OUT + 'teacher/T%d.wav' % t['n'], audio)
    json.dump(info, open(OUT + 'teacher/T%d.json' % t['n'], 'w'), default=str)
    if os.path.exists(out) and not force: return info
    # elenchi per ffmpeg
    L = open(OUT + 'teacher/T%d_base.txt' % t['n'], 'w'); last = None
    for k, (f, st, lab, pg) in enumerate(states):
        f2 = states[k + 1][0] if k + 1 < len(states) else nout
        if f2 <= f: continue
        p = state_png(t, st, screens, ycs, pg)
        L.write("file '%s'\nduration %.6f\n" % (p, (f2 - f) / FPS)); last = p
    L.write("file '%s'\n" % last); L.close()
    C = open(OUT + 'teacher/T%d_cam.txt' % t['n'], 'w')
    for x, y in iv: C.write("file '%scam_all.mp4'\ninpoint %.6f\noutpoint %.6f\n" % (R, x / FPS, y / FPS))
    C.close()
    mask = OUT + 'mask.png'
    if not os.path.exists(mask):
        mk = Image.new('L', (412, 309), 0); ImageDraw.Draw(mk).rounded_rectangle((0, 0, 411, 308), 16, fill=255); mk.save(mask)
    base = OUT + 'teacher/T%d_base.mkv' % t['n']
    from vid import Enc as _E
    e = _E(base)
    for k, (f, st, lab, pg) in enumerate(states):
        f2 = states[k + 1][0] if k + 1 < len(states) else nout
        if f2 <= f: continue
        e.put(Image.open(state_png(t, st, screens, ycs, pg)), f2 - f)
    assert e.close() == nout
    cmd = ['ffmpeg', '-v', 'error', '-y', '-i', base, '-f', 'concat', '-safe', '0', '-i', OUT + 'teacher/T%d_cam.txt' % t['n'],
           '-filter_complex', "[0:v]format=rgb24[b];[1:v]fps=30,format=rgba,geq=r='r(X,Y)':g='g(X,Y)':b='b(X,Y)':a='255*lte(pow(max(max(16-X,X-395),0),2)+pow(max(max(16-Y,Y-292),0),2),256)'[c];[b][c]overlay=1428:148:shortest=1,format=yuv420p[v]",
           '-map', '[v]', '-threads', '3', '-frames:v', str(nout), '-r', '30', '-c:v', 'libx264', '-preset', 'veryfast', '-crf', '19', '-an', out + '.part.mp4']
    subprocess.run(cmd, check=True); os.replace(out + '.part.mp4', out); os.remove(base)
    return info

_pa = None
def proc_audio():
    global _pa
    if _pa is None:
        p = R + 'doc_proc.wav'
        if not os.path.exists(p):
            subprocess.run(['ffmpeg', '-v', 'error', '-y', '-i', R + 'doc_orig.wav', '-af', 'highpass=f=90,afftdn=nr=6:nf=-50:tn=1', '-c:a', 'pcm_s16le', p], check=True)
        _pa = load_wav(p)
    return _pa

if __name__ == '__main__':
    for i in [int(x) for x in sys.argv[1:]] or range(7):
        info = build_topic(i); print(i + 1, info['frames'], info['src'], len(info['states']), flush=True)
