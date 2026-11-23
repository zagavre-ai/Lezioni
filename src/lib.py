# Libreria di disegno · Storia dell'arte V lez06 · modello grafico Spagnolo
import os, re, hashlib, subprocess, math, random
import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageChops

W, H = 1920, 1080
BLUE = (32, 96, 175); NAVY = (11, 21, 48); YEL = (255, 230, 0); GREY = (91, 101, 119)
FD = '/root/.fonts/'
_F = {}
def font(kind, size):
    f = {'t': 'BricolageGrotesque-ExtraBold.ttf', 'b': 'Figtree-Bold.ttf', 'sb': 'Figtree-SemiBold.ttf', 'r': 'Figtree-Regular.ttf', 'm': 'Figtree-Medium.ttf', 'x': 'Figtree-ExtraBold.ttf'}[kind]
    k = (kind, size)
    if k not in _F: _F[k] = ImageFont.truetype(FD + f, size)
    return _F[k]
MATERIA = "STORIA DELL'ARTE V"
PROF_NOME = 'Giorgio Mazzotti'
PROF_QUAL = "PROF. DI STORIA DELL'ARTE"
LOGO = Image.open('/tmp/w/build/logo_blu.png').convert('RGBA')
LOGO_W = Image.open('/tmp/w/build/logo_blu.png').convert('RGBA')

def spaced(d, xy, text, f, fill, track=3):
    x, y = xy
    for ch in text:
        d.text((x, y), ch, font=f, fill=fill); x += f.getlength(ch) + track
    return x

def shadow(img, box, radius=16, blur=18, off=(0, 10), alpha=60):
    sh = Image.new('RGBA', img.size, (0, 0, 0, 0)); d = ImageDraw.Draw(sh)
    x0, y0, x1, y1 = box
    d.rounded_rectangle((x0 + off[0], y0 + off[1], x1 + off[0], y1 + off[1]), radius, fill=(40, 50, 70, alpha))
    sh = sh.filter(ImageFilter.GaussianBlur(blur)); img.alpha_composite(sh)

REC = []
DRAW_CAM = True
def rec(text, x, y, size=30):
    REC.append((text, x, y, size))

def base(label=None, page=1, cam=False, keywords=None, draw_cam=None):
    if draw_cam is None: draw_cam = DRAW_CAM
    im = Image.new('RGBA', (W, H), (255, 255, 255, 255)); d = ImageDraw.Draw(im)
    lg = LOGO.resize((165, 52), Image.LANCZOS); im.alpha_composite(lg, (80, 52))
    d.line((80, 124, 1840, 124), fill=(226, 232, 240), width=2)
    d.line((80, 981, 1840, 981), fill=(226, 232, 240), width=2)
    spaced(d, (80, 1003), MATERIA, font('b', 21), BLUE, 3)
    t = 'Pagina %d' % page; f = font('b', 21); wt = sum(f.getlength(c) + 3 for c in t)
    spaced(d, (1840 - wt, 1003), t, f, BLUE, 3)
    if label: spaced(d, (80, 148), label.upper(), font('b', 22), BLUE, 4); rec(label, 80, 148, 22)
    rec(MATERIA, 80, 1003, 21); rec('Pagina %d' % page, 1700, 1003, 21)
    if cam and draw_cam:
        shadow(im, (1428, 148, 1840, 457), 16, 20, (0, 12), 70)
        # fascia gialla del nome, leggermente inclinata
        band = Image.new('RGBA', (440, 130), (0, 0, 0, 0)); bd = ImageDraw.Draw(band)
        bd.rounded_rectangle((8, 8, 432, 122), 6, fill=YEL + (255,))
        bd.text((30, 24), PROF_NOME, font=font('t', 34), fill=NAVY)
        bd.text((30, 74), PROF_QUAL, font=font('b', 22), fill=NAVY)
        band = band.rotate(2.5, resample=Image.BICUBIC, expand=True)
        shadow(im, (1428 - 4, 470, 1846, 580), 6, 14, (0, 8), 60)
        im.alpha_composite(band, (1418, 452))
    if cam and keywords:
        if True:
            rec('Parole chiave', 1428, 618, 22)
            spaced(d, (1428, 618), 'PAROLE CHIAVE', font('b', 22), BLUE, 4)
            y = 656
            for k in keywords[:5]:
                f = font('sb', 30); w = int(f.getlength(k)) + 36
                d.rounded_rectangle((1428, y, 1428 + min(w, 412), y + 48), 14, fill=(234, 241, 251), outline=(190, 208, 232), width=2)
                d.text((1428 + 18, y + 5), k, font=f, fill=NAVY); rec(k, 1446, y + 5, 30); y += 58
    return im

def title(im, text, y=186, maxw=1290, size=58):
    d = ImageDraw.Draw(im); f = font('t', size)
    words = text.split(); lines = []; cur = ''
    for w in words:
        t = (cur + ' ' + w).strip()
        if f.getlength(t) <= maxw: cur = t
        else: lines.append(cur); cur = w
    lines.append(cur)
    for i, l in enumerate(lines): d.text((80, y + i * (size + 8)), l, font=f, fill=BLUE); rec(l, 80, y + i * (size + 8), size)
    yy = y + len(lines) * (size + 8) + 6
    d.rounded_rectangle((80, yy, 160, yy + 6), 3, fill=BLUE)
    return yy + 30

def wrap_runs(runs, maxw):
    """runs: [(testo, fontkey)] -> righe di [(parola, font)]"""
    toks = []
    for t, k in runs:
        for w in t.split(' '):
            if w: toks.append((w, k))
    lines = []; cur = []; curw = 0
    for w, k in toks:
        f = font(k[0], k[1]); ww = f.getlength(w + ' ')
        if curw + ww - f.getlength(' ') > maxw and cur: lines.append(cur); cur = []; curw = 0
        cur.append((w, k)); curw += ww
    if cur: lines.append(cur)
    return lines

def card_height(label, text, width, size=40, lh=52):
    runs = ([(label + ':', ('b', size))] if label else []) + [(text, ('r', size))]
    n = len(wrap_runs(runs, width - 28 - 64)); return n * lh + 40

def draw_card(im, x, y, width, label, text, state='n', size=40, lh=52, dot=True):
    """state: 'n' normale, 'dim' attenuata, 'on' accesa (bordo giallo + pallino giallo)"""
    h = card_height(label, text, width, size, lh)
    runs = ([(label + ':', ('b', size))] if label else []) + [(text, ('r', size))]
    lines = wrap_runs(runs, width - 28 - 64)
    shadow(im, (x, y, x + width, y + h), 18, 14, (0, 8), 38 if state != 'dim' else 20)
    d = ImageDraw.Draw(im)
    if state == 'on': fill = (255, 252, 228); outl = (255, 214, 0); bw = 5; col = NAVY
    elif state == 'dim': fill = (250, 251, 253); outl = (222, 229, 239); bw = 2; col = (95, 106, 124)
    else: fill = (247, 249, 252); outl = (208, 218, 232); bw = 2; col = NAVY
    d.rounded_rectangle((x, y, x + width, y + h), 18, fill=fill, outline=outl, width=bw)
    if dot:
        d.ellipse((x + 22, y + 24, x + 44, y + 46), fill=YEL if state == 'on' else (214, 222, 234), outline=NAVY if state == 'on' else None, width=2)
    ty = y + 18
    for ln in lines:
        tx = x + 64
        rec(' '.join(w for w, k in ln), tx, ty, size)
        for w, k in ln:
            f = font(k[0], k[1]); c = col
            d.text((tx, ty), w, font=f, fill=c); tx += f.getlength(w + ' ')
        ty += lh
    return h

def fit_image(path_or_im, maxw, maxh, upscale_ok=True):
    im = Image.open(path_or_im).convert('RGB') if isinstance(path_or_im, str) else path_or_im.convert('RGB')
    s = min(maxw / im.width, maxh / im.height)
    if not upscale_ok: s = min(s, 1)
    return im.resize((max(1, int(im.width * s)), max(1, int(im.height * s))), Image.LANCZOS)

def paste_photo(im, ph, x, y, radius=14):
    shadow(im, (x, y, x + ph.width, y + ph.height), radius, 18, (0, 10), 60)
    m = Image.new('L', ph.size, 0); ImageDraw.Draw(m).rounded_rectangle((0, 0, ph.width - 1, ph.height - 1), radius, fill=255)
    im.paste(ph, (x, y), m)

def caption(im, x, y, w, text, size=28, color=GREY):
    d = ImageDraw.Draw(im); lines = wrap_runs([(text, ('r', size))], w); yy = y
    for ln in lines:
        d.text((x, yy), ' '.join(w_ for w_, k in ln), font=font('r', size), fill=color); rec(' '.join(w_ for w_, k in ln), x, yy, size); yy += size + 8
    return yy

# ---------------- schede blu animate ----------------
def dark_frame(t, w=W, h=H):
    """sfondo blu scuro con bagliori che si muovono lentamente (ciclo di 6 s)"""
    yy, xx = np.mgrid[0:h:4, 0:w:4].astype(np.float32)
    base_ = np.zeros((h // 4 + (1 if h % 4 else 0), w // 4 + (1 if w % 4 else 0), 3), np.float32)
    top = np.array([8, 16, 40], np.float32); bot = np.array([14, 34, 78], np.float32)
    g = (yy / h)[..., None]; base_ = top * (1 - g) + bot * g
    ph = 2 * math.pi * t / 6.0
    blobs = [(0.25 + 0.06 * math.sin(ph), 0.35 + 0.05 * math.cos(ph), 520, (30, 90, 200), 0.55),
             (0.78 + 0.05 * math.cos(ph), 0.7 + 0.06 * math.sin(ph), 600, (20, 120, 190), 0.35),
             (0.55 + 0.07 * math.sin(ph + 2), 0.2 + 0.05 * math.cos(ph + 1), 420, (70, 60, 170), 0.30)]
    for cx, cy, r, col, a in blobs:
        d2 = ((xx - cx * w) ** 2 + (yy - cy * h) ** 2) / (r * r)
        base_ += np.exp(-d2)[..., None] * np.array(col, np.float32) * a
    im = Image.fromarray(np.clip(base_, 0, 255).astype(np.uint8)).resize((w, h), Image.BILINEAR)
    return im.convert('RGBA')

def dark_overlay_base(label=None):
    """strato RGBA trasparente con logo bianco-azzurro in alto a sinistra"""
    im = Image.new('RGBA', (W, H), (0, 0, 0, 0))
    lg = LOGO.copy(); r, g, b, a = lg.split()
    wl = Image.merge('RGBA', (Image.new('L', lg.size, 235), Image.new('L', lg.size, 242), Image.new('L', lg.size, 255), a)).resize((165, 52), Image.LANCZOS)
    im.alpha_composite(wl, (80, 52))
    if label:
        spaced(ImageDraw.Draw(im), (80, 150), label.upper(), font('b', 22), (255, 200, 60), 5)
    return im

def blend_rgba(a, b, k):
    A = np.asarray(a, np.float32); B = np.asarray(b, np.float32)
    return Image.fromarray(np.clip(A * (1 - k) + B * k, 0, 255).astype(np.uint8), 'RGBA')

def save(im, path):
    os.makedirs(os.path.dirname(path), exist_ok=True); im.save(path); return path
