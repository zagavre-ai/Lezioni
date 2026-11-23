# Schede e animazioni con la voce Kore (copertina, titolo argomento, approfondimento, pillola, quiz, glossario, riepilogo, compiti...)
import os, sys, json, re, math
sys.path.insert(0, '/tmp/claude-0/w/build')
import numpy as np
from PIL import Image, ImageDraw
from gfx import *
import gfx, vid, asr, spec
from vid import *

R = '/tmp/claude-0/w/lez07/'
VOX_DIRS = ['/tmp/claude-0/w/vox_new/', '/tmp/claude-0/w/old/scambio/storia-arte-V-lez07/vox/']
TXT = {}
for p in ('/tmp/claude-0/w/old/scambio/storia-arte-V-lez07/testi_voci.json', '/tmp/claude-0/w/build/nuove_voci.json', '/tmp/claude-0/w/build/compiti_voce.json'):
    for x in json.load(open(p)): TXT[x['nome']] = x['testo']

NUM = {'millenovecentotto': '1908', 'millenovecentoventicinque': '1925', 'millenovecentoquattordici': '1914', 'millenovecentododici': '1912', 'millenovecentocinque': '1905',
       'millenovecentosei': '1906', 'millenovecentosette': '1907', 'millenovecentootto': '1908', 'millenovecentonove': '1909', 'millenovecento': '1900'}
def digits(t):
    for k in sorted(NUM, key=len, reverse=True): t = t.replace(k, NUM[k])
    return t.replace('Scukin', 'Shchukin').replace('Brancusi', 'Brâncuși')

_v = {}
def voice(name):
    """ritorna dict(a=audio 48k mono normalizzato, words, span, real)"""
    if name in _v: return _v[name]
    os.makedirs(OUT + 'vox48', exist_ok=True)
    for d, nm in [(d, n) for n in (name + '_R2', name) for d in VOX_DIRS]:
        p = d + nm + '.wav'
        if os.path.exists(p):
            q = OUT + 'vox48/%s_%s.wav' % (name, hashlib_md5(p))
            if not os.path.exists(q): to48(p, q)
            a = load_wav(q); a = norm_lufs(a, -17.0)
            w = asr.words(q); s = asr.speech_span(q)
            _v[name] = dict(a=a, words=w, span=(float(s[0]), float(s[1])), real=True, path=p); return _v[name]
    n = len(TXT[name].split()); dur = max(2.5, n * 0.40 + 0.6)
    a = np.zeros(int(dur * SR), np.float32)
    w = [(0.3 + i * (dur - 0.6) / n, x) for i, x in enumerate(TXT[name].split())]
    _v[name] = dict(a=a, words=w, span=(0.3, dur - 0.3), real=False, path=None); return _v[name]

def hashlib_md5(p):
    import hashlib; return hashlib.md5(open(p, 'rb').read()).hexdigest()[:8]

def norm_lufs(a, target):
    import pyloudnorm as pyln
    if len(a) < SR * 0.5 or np.abs(a).max() < 1e-4: return a
    m = pyln.Meter(SR); l = m.integrated_loudness(a.astype(np.float64))
    g = 10 ** ((target - l) / 20); b = a * g
    pk = np.abs(b).max()
    if pk > 0.89: b = b * (0.89 / pk)
    return b.astype(np.float32)

def frags(name, fr):
    v = voice(name); assert norm_join(fr) == norm_join([TXT[name]]), name
    return asr.align(v['words'], fr, span=v['span'])

def norm_join(fr): return re.sub(r'\s+', ' ', ' '.join(fr)).strip()

def sentences(t, minlen=45):
    ss = re.split(r'(?<=[.!?])\s+', t.strip()); out = []
    for s in ss:
        if out and (len(out[-1]) < minlen or len(s) < 30): out[-1] += ' ' + s
        else: out.append(s)
    return out

# ============================================================ componenti
def fade_alpha(t, t0, d=0.35): return ease((t - t0) / d)

def overlay_alpha(base, layer, a):
    if a >= 0.999: base.alpha_composite(layer); return
    if a <= 0.001: return
    l = layer.copy(); al = l.split()[3].point(lambda v: int(v * a)); l.putalpha(al); base.alpha_composite(l)

def row_layers(texts, x0, x1, ytop, ybot, size=36, bold_first=False, pad=22, gap=16, badge=True):
    """pre-calcola le righe (altezza, righe di testo) e le centra in verticale"""
    im = Image.new('RGBA', (10, 10)); d = ImageDraw.Draw(im); f = F('semi', size)
    rows = []
    for t in texts:
        ls = wrap(d, t, f, x1 - x0 - 150); rows.append((ls, len(ls) * int(size * 1.3) + 2 * pad))
    tot = sum(h for _, h in rows) + gap * (len(rows) - 1)
    y = ytop + max(0, (ybot - ytop - tot) // 2); out = []
    for ls, h in rows: out.append((y, y + h, ls)); y += h + gap
    return out

def draw_row(im, lay, x0, x1, n, state, size=36, label_bold=None):
    """state 1 vista, 2 in corso"""
    y0, y1, ls = lay; d = ImageDraw.Draw(im, 'RGBA')
    fill = (255, 255, 255, 36) if state == 1 else (255, 255, 255, 56)
    d.rounded_rectangle((x0, y0, x1, y1), 22, fill=fill, outline=YEL + (255,) if state == 2 else (255, 255, 255, 60), width=5 if state == 2 else 2)
    cy = (y0 + y1) // 2
    d.ellipse((x0 + 22, cy - 25, x0 + 72, cy + 25), fill=YEL if state == 2 else (60, 120, 210, 255))
    nf = F('xbold', 28); s = str(n); d.text((x0 + 47 - d.textlength(s, font=nf) / 2, cy - 17), s, font=nf, fill=NAVY if state == 2 else (255, 255, 255))
    f = F('semi', size); y = y0 + (y1 - y0 - len(ls) * int(size * 1.3)) // 2
    for ln in ls:
        d.text((x0 + 100, y), ln, font=f, fill=(255, 255, 255) if state == 2 else (200, 216, 242)); y += int(size * 1.3)

def rows_scene(sid, label, title, sub, rows, vname, fr, lead=1.0, jingle_name=None, jingle_at=0.0, jingle_gain=0.8, tail=1.4, size=36,
               x0=900, bullets_numbered=True, title_size=120, meta=None):
    """scheda blu: titolo a sinistra, righe a destra che si accendono con la voce"""
    v = voice(vname); times = frags(vname, fr)   # (inizio,fine) per riga, relativi alla voce
    if isinstance(rows, int): pass
    assert len(rows) <= len(fr)
    off = len(fr) - len(rows)             # i primi 'off' frammenti sono introduzioni (non righe)
    sp0 = v['span'][0]; start = lead
    dur = lead + v['span'][1] + tail
    N = int(math.ceil(dur * FPS)); lays = row_layers(rows, x0, 1840, 200, 960, size=size)
    e = Enc(OUT + 'seg/%s.mp4' % sid)
    # voce
    track = np.zeros(N * 1600 + SR, np.float32)
    if jingle_name: place(track, vid.jingle(jingle_name), jingle_at, jingle_gain, 0.01, 0.4)
    place(track, v['a'], lead, 1.0)
    t_on = [lead + times[off + i][0] - 0.05 for i in range(len(rows))]
    t_off = [lead + times[off + i][1] for i in range(len(rows))]
    for i in range(N):
        t = i / FPS; im = dark_bg_cached(t, 0.5)
        a = fade_alpha(t, 0.0, 0.5)
        d = ImageDraw.Draw(im)
        spaced(d, (140, 260), label.upper(), F('xbold', 26), (255, 205, 60), 6)
        y = dark_title(im, title, 310, size=title_size, maxw=700)
        if sub:
            for ln in wrap(d, sub, F('bold', 40), 700): d.text((140, y + 14), ln, font=F('bold', 40), fill=(92, 214, 255)); y += 48
        for k, lay in enumerate(lays):
            if t >= t_on[k]:
                st = 2 if (t < t_off[k] or k == len(lays) - 1 and t < t_off[k] + 0.3) else 1
                lay2 = (lay[0] + int(18 * (1 - fade_alpha(t, t_on[k], 0.3))), lay[1] + int(18 * (1 - fade_alpha(t, t_on[k], 0.3))), lay[2])
                layer = Image.new('RGBA', (W, H), (0, 0, 0, 0)); draw_row(layer, lay2, x0, 1840, k + 1, st, size=size)
                overlay_alpha(im, layer, fade_alpha(t, t_on[k], 0.3))
        e.put(im)
    n = e.close()
    m = dict(kind='rows', real=v['real']); m.update(meta or {}); m['t_rows'] = [(round(a, 2), round(b, 2)) for a, b in zip(t_on, t_off)]
    return finish(sid, n, track, m)

# ============================================================ titolo argomento
def title_scene(sid, n, title, dur=3.2):
    N = int(dur * FPS); e = Enc(OUT + 'seg/%s.mp4' % sid); track = np.zeros(N * 1600 + SR, np.float32)
    place(track, vid.jingle('titolo'), 0.0, 1.0, 0.01, 0.4)
    for i in range(N):
        t = i / FPS; im = dark_bg_cached(t, 0.5); d = ImageDraw.Draw(im)
        a = fade_alpha(t, 0.15, 0.6)
        layer = Image.new('RGBA', (W, H), (0, 0, 0, 0)); ld = ImageDraw.Draw(layer)
        spaced(ld, (140, 330), 'ARGOMENTO %d' % n, F('xbold', 30), (255, 205, 60), 8)
        yy = 390 + int(26 * (1 - a))
        for ln in wrap(ld, title, F('title', 104), 1600): ld.text((140, yy), ln, font=F('title', 104), fill=(255, 255, 255)); yy += 112
        bw = int(260 * ease((t - 0.5) / 0.8)); ld.rounded_rectangle((140, yy + 24, 140 + bw, yy + 32), 4, fill=(92, 214, 255))
        overlay_alpha(im, layer, a); e.put(im)
    return finish(sid, e.close(), track, dict(kind='titolo', n=n))

# ============================================================ quiz / verifica
def quiz_scene(sid, label, title, sub, chip, dur=4.6):
    N = int(dur * FPS); e = Enc(OUT + 'seg/%s.mp4' % sid); track = np.zeros(N * 1600 + SR, np.float32)
    place(track, vid.jingle('quiz'), 0.5, 0.9, 0.0, 0.3)       # scatto a +0,5 s
    for i in range(N):
        t = i / FPS; im = dark_bg_cached(t, 0.5); d = ImageDraw.Draw(im)
        a = fade_alpha(t, 0.1, 0.5); layer = Image.new('RGBA', (W, H), (0, 0, 0, 0)); ld = ImageDraw.Draw(layer)
        spaced(ld, (140, 330), label.upper(), F('xbold', 28), (255, 205, 60), 7)
        y = 390
        for ln in wrap(ld, title, F('title', 120), 1100): ld.text((140, y), ln, font=F('title', 120), fill=(255, 255, 255)); y += 128
        for ln in wrap(ld, sub, F('bold', 48), 1100): ld.text((140, y + 8), ln, font=F('bold', 48), fill=(255, 205, 60)); y += 58
        cw = int(ld.textlength(chip, font=F('semi', 34))) + 60
        ld.rounded_rectangle((140, y + 50, 140 + cw, y + 124), 37, fill=(255, 255, 255, 40), outline=(255, 255, 255, 90), width=2)
        ld.text((170, y + 68), chip, font=F('semi', 34), fill=(255, 255, 255))
        # icona play con anello che pulsa
        cx, cy = 1560, 540; pr = 1 + 0.04 * math.sin(t * 5)
        for r, al in ((int(190 * pr), 60), (int(150 * pr), 110)):
            ld.ellipse((cx - r, cy - r, cx + r, cy + r), outline=(92, 214, 255, al), width=5)
        ld.ellipse((cx - 112, cy - 112, cx + 112, cy + 112), fill=(92, 214, 255, 255))
        ld.polygon([(cx - 34, cy - 56), (cx - 34, cy + 56), (cx + 62, cy)], fill=NAVY + (255,))
        overlay_alpha(im, layer, a); e.put(im)
    return finish(sid, e.close(), track, dict(kind='quiz', t_scatto=0.5))
