# Libreria grafica · modello Spagnolo (fondo bianco, blu notte, blu Telesio, giallo) · 1920x1080
import os, math, functools, subprocess, io
import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageChops
import cairosvg

W, H = 1920, 1080
FD = '/root/.fonts/'
NOTTE = (11, 21, 48); BLU = (32, 96, 175); GIALLO = (255, 230, 0); BIANCO = (255, 255, 255)
GRIGIO = (110, 118, 135)
MATERIA = "STORIA DELL'ARTE V"
B = '/home/user/w18/b/'

@functools.lru_cache(None)
def F(nome, size):
    f = {'bric': 'BricolageGrotesque-ExtraBold.ttf', 'bold': 'Figtree-Bold.ttf', 'semi': 'Figtree-SemiBold.ttf',
         'med': 'Figtree-Medium.ttf', 'reg': 'Figtree-Regular.ttf', 'xbold': 'Figtree-ExtraBold.ttf'}[nome]
    return ImageFont.truetype(FD + f, size)

def tw(d, s, font, sp=0):
    return d.textlength(s, font=font) + sp * max(0, len(s) - 1)

def text_sp(d, xy, s, font, fill, sp=0):
    x, y = xy
    if not sp:
        d.text((x, y), s, font=font, fill=fill); return
    for ch in s:
        d.text((x, y), ch, font=font, fill=fill); x += d.textlength(ch, font=font) + sp

def wrap(d, s, font, maxw):
    out = []; line = ''
    for w in s.split(' '):
        t = (line + ' ' + w).strip()
        if d.textlength(t, font=font) <= maxw: line = t
        else:
            if line: out.append(line)
            line = w
    if line: out.append(line)
    return out

def shadow(img, box, r=20, blur=22, off=(0, 10), alpha=60):
    sh = Image.new('RGBA', img.size, (0, 0, 0, 0)); dd = ImageDraw.Draw(sh)
    x0, y0, x1, y1 = box
    dd.rounded_rectangle((x0 + off[0], y0 + off[1], x1 + off[0], y1 + off[1]), r, fill=(70, 80, 100, alpha))
    sh = sh.filter(ImageFilter.GaussianBlur(blur))
    img.alpha_composite(sh)

def logo(color='blu', h=52):
    p = B + f'logo_{color}_{h}.png'
    if not os.path.exists(p):
        svg = open('/home/user/Lezioni/kit/docenti/Telesio_logo_blu.svg').read()
        if color == 'bianco': svg = svg.replace('#2060AF', '#FFFFFF')
        cairosvg.svg2png(bytestring=svg.encode(), write_to=p, output_height=h)
    return Image.open(p).convert('RGBA')

def base_slide(label, page, titolo=None, footer=True):
    """Fondo bianco + testata + piè di pagina (solo materia e Pagina N)."""
    im = Image.new('RGBA', (W, H), (255, 255, 255, 255)); d = ImageDraw.Draw(im)
    im.alpha_composite(logo('blu', 52), (80, 50))
    d.line((80, 124, 1840, 124), fill=(226, 230, 238), width=2)
    if label: text_sp(d, (80, 148), label.upper(), F('bold', 25), BLU, 3.2)
    if footer:
        d.line((80, 981, 1840, 981), fill=(226, 230, 238), width=2)
        text_sp(d, (80, 1003), MATERIA, F('bold', 22), BLU, 3.2)
        s = f'Pagina {page}' if page else ''
        if s: text_sp(d, (1840 - tw(d, s, F('bold', 22), 2.5), 1003), s, F('bold', 22), BLU, 2.5)
    return im

def prof_frame(im, nome='Giorgio Mazzotti', ruolo="PROF. DI STORIA DELL'ARTE", box=True):
    """Segnaposto ombra del riquadro 4:3 (412x309 a x=1428,y=148) + fascia gialla col nome."""
    d = ImageDraw.Draw(im)
    shadow(im, (1428, 148, 1840, 457), r=16, blur=18, off=(0, 12), alpha=70)
    ImageDraw.Draw(im).rounded_rectangle((1428, 148, 1840, 457), 16, fill=(235, 238, 244, 255))
    # fascia gialla leggermente inclinata
    st = Image.new('RGBA', (500, 190), (0, 0, 0, 0))
    shadow(st, (40, 40, 452, 142), r=8, blur=10, off=(0, 8), alpha=70)
    sd = ImageDraw.Draw(st)
    sd.rounded_rectangle((40, 40, 452, 142), 8, fill=GIALLO)
    sd.text((62, 52), nome, font=F('bric', 36), fill=NOTTE)
    text_sp(sd, (62, 102), ruolo, F('bold', 20), NOTTE, 1.5)
    st = st.rotate(2.2, resample=Image.BICUBIC, expand=False)
    im.alpha_composite(st, (1388, 422))
    return im

def keywords_panel(im, kws):
    """Parole chiave (max 5) nella colonna destra, sotto la fascia gialla."""
    kws = kws[:5]
    if not kws: return
    d = ImageDraw.Draw(im); x0, y0, x1 = 1428, 610, 1840
    f = F('semi', 28); lines = []
    for k in kws: lines.append(wrap(d, k, f, x1 - x0 - 80))
    hh = 78 + sum(len(l) * 40 + 10 for l in lines)
    shadow(im, (x0, y0, x1, y0 + hh), r=18, blur=16, off=(0, 8), alpha=50)
    d = ImageDraw.Draw(im)
    d.rounded_rectangle((x0, y0, x1, y0 + hh), 18, fill=(246, 248, 252, 255), outline=(220, 226, 238), width=2)
    text_sp(d, (x0 + 30, y0 + 24), 'PAROLE CHIAVE', F('bold', 20), BLU, 2.5)
    y = y0 + 66
    for l in lines:
        d.ellipse((x0 + 30, y + 14, x0 + 42, y + 26), fill=BLU)
        for ln in l:
            d.text((x0 + 58, y), ln, font=f, fill=NOTTE); y += 40
        y += 10

def title_block(im, titolo, y=200, size=62):
    d = ImageDraw.Draw(im); f = F('bric', size)
    lines = wrap(d, titolo, f, 1305)[:2]
    for i, ln in enumerate(lines):
        d.text((80, y + i * (size + 8)), ln, font=f, fill=NOTTE)
    yy = y + len(lines) * (size + 8) + 8
    d.rounded_rectangle((80, yy, 165, yy + 7), 3, fill=BLU)
    return yy + 40

def card_layout(d, cards, x0=80, x1=1385, size=40, lh=60, pad=34):
    f = F('reg', size); fb = F('bold', size); out = []
    for c in cards:
        lead, body = c if isinstance(c, tuple) else ('', c)
        # etichetta in grassetto + testo
        words = ([(w, fb) for w in lead.split(' ')] if lead else []) + [(w, f) for w in body.split(' ')]
        lines = []; cur = []; cw = 0
        for w, fo in words:
            wl = d.textlength(w + ' ', font=fo)
            if cw + wl > (x1 - x0 - 2 * pad - 20) and cur:
                lines.append(cur); cur = []; cw = 0
            cur.append((w, fo)); cw += wl
        if cur: lines.append(cur)
        out.append((lines, len(lines) * lh + 2 * 26))
    return out

def draw_cards(im, cards, active, y0, x0=80, x1=1385, size=40, lh=60, gap=26):
    d = ImageDraw.Draw(im); lay = card_layout(d, cards, x0, x1, size, lh)
    y = y0
    for i, (lines, h) in enumerate(lay):
        on = (i == active)
        shadow(im, (x0, y, x1, y + h), r=22, blur=18, off=(0, 8), alpha=55 if on else 28)
        d = ImageDraw.Draw(im)
        col = (255, 255, 255, 255) if on else (247, 249, 252, 255)
        d.rounded_rectangle((x0, y, x1, y + h), 22, fill=col, outline=GIALLO if on else (226, 231, 240), width=5 if on else 2)
        txtc = NOTTE if on else (120, 128, 148)
        if on: d.ellipse((x0 + 22, y + h // 2 - 8, x0 + 38, y + h // 2 + 8), fill=GIALLO, outline=(220, 190, 0), width=2)
        ty = y + 26
        for ln in lines:
            xx = x0 + 34 + 20
            for w, fo in ln:
                d.text((xx, ty), w, font=fo, fill=txtc); xx += d.textlength(w + ' ', font=fo)
            ty += lh
        y += h + gap
    return y

def slide_testo(label, titolo, cards, active, page, kws=None):
    im = base_slide(label, page)
    y = title_block(im, titolo)
    draw_cards(im, cards, active, y)
    prof_frame(im)
    if kws: keywords_panel(im, kws)
    return im

def sharpen(im, r=1.2, p=90):
    return im.filter(ImageFilter.UnsharpMask(radius=r, percent=p, threshold=2))

def fit_big(src, w, h):
    """Ingrandimento di qualità (Lanczos in due passi + nitidezza) per stare in w x h."""
    s = min(w / src.width, h / src.height)
    nw, nh = max(1, int(src.width * s)), max(1, int(src.height * s))
    if s > 1.5:
        mid = src.resize((int(src.width * s ** .5), int(src.height * s ** .5)), Image.LANCZOS)
        mid = sharpen(mid, 1.0, 60)
        out = mid.resize((nw, nh), Image.LANCZOS)
    else:
        out = src.resize((nw, nh), Image.LANCZOS)
    return sharpen(out, 1.0, 70 if s > 1 else 40)

def slide_immagine(label, page, img, kws=None, box=None, crop=None, titolo=None):
    """Immagine grande (alta qualità) nell'area sinistra 80..1385 x 150..960."""
    im = base_slide(label, page)
    src = img.convert('RGB')
    if crop: src = src.crop(crop)
    top = 200 if label else 150
    if titolo:
        y = title_block(im, titolo, y=190, size=52); top = y - 10
    big = fit_big(src, 1305, 960 - top - 10)
    x = 80 + (1305 - big.width) // 2; y = top + (960 - top - big.height) // 2
    shadow(im, (x, y, x + big.width, y + big.height), r=12, blur=20, off=(0, 10), alpha=60)
    im.paste(big.convert('RGBA'), (x, y))
    prof_frame(im)
    if kws: keywords_panel(im, kws)
    return im

# ---- fondo blu scuro animato (schede titolo, pillola, quiz, riepilogo) ----
_blob = None
def blob():
    global _blob
    if _blob is None:
        n = 900; yy, xx = np.mgrid[0:n, 0:n]; r = np.hypot(xx - n / 2, yy - n / 2) / (n / 2)
        a = np.clip(1 - r, 0, 1) ** 2
        _blob = a.astype(np.float32)
    return _blob

_bgbase = None
def bg_blu(t):
    """Fondo blu notte con grandi aloni lenti (nessun lampo)."""
    global _bgbase
    if _bgbase is None:
        yy = np.linspace(0, 1, H)[:, None, None]
        top = np.array([14, 28, 66], np.float32); bot = np.array([8, 15, 38], np.float32)
        _bgbase = (top * (1 - yy) + bot * yy) * np.ones((1, W, 1), np.float32)
    img = _bgbase.copy()
    bl = blob()
    for k, (cx, cy, sx, sy, col, sc) in enumerate([
            (500, 300, 0.11, 0.07, (32, 96, 175), 1.5), (1500, 800, 0.08, 0.10, (32, 96, 175), 1.7), (1000, 560, 0.06, 0.05, (255, 230, 0), 0.5)]):
        px = cx + 220 * math.sin(t * sx + k); py = cy + 140 * math.cos(t * sy + k * 2)
        s = int(900 * sc / 1.5 * (1.0 if k != 2 else 0.8)); s = max(100, s)
        small = np.array(Image.fromarray((bl * 255).astype(np.uint8)).resize((s, s), Image.BILINEAR), np.float32) / 255
        x0, y0 = int(px - s / 2), int(py - s / 2)
        xa, ya = max(0, x0), max(0, y0); xb, yb = min(W, x0 + s), min(H, y0 + s)
        if xb <= xa or yb <= ya: continue
        m = small[ya - y0:yb - y0, xa - x0:xb - x0, None] * (0.32 if k < 2 else 0.05)
        img[ya:yb, xa:xb] = img[ya:yb, xa:xb] * (1 - m) + np.array(col, np.float32) * m
    return Image.fromarray(img.clip(0, 255).astype(np.uint8)).convert('RGBA')

def ease(x):
    x = max(0.0, min(1.0, x)); return x * x * (3 - 2 * x)

def scheda_blu(t, label, titolo, size=96, y=None):
    im = bg_blu(t)
    d = ImageDraw.Draw(im)
    im.alpha_composite(logo('bianco', 52), (80, 50))
    return im

def mask_cam():
    p = B + 'mask_cam.png'
    if not os.path.exists(p):
        m = Image.new('L', (412, 309), 0); ImageDraw.Draw(m).rounded_rectangle((0, 0, 411, 308), 16, fill=255); m.save(p)
    return p

# ---------- copertina ----------
def copertina(titolo, argomenti, prof=True, page=1):
    im = base_slide('STORIA DELL\'ARTE V · VIDEOLEZIONE', page)
    d = ImageDraw.Draw(im); f = F('bric', 78)
    lines = wrap(d, titolo, f, 1300)
    y = 205
    for ln in lines:
        d.text((80, y), ln, font=f, fill=NOTTE); y += 92
    d.rounded_rectangle((80, y + 4, 165, y + 11), 3, fill=BLU)
    y += 40
    fl = F('semi', 31); step = 52
    h = 84 + len(argomenti) * step
    shadow(im, (80, y, 1385, y + h), r=22, blur=18, off=(0, 8), alpha=45)
    d = ImageDraw.Draw(im)
    d.rounded_rectangle((80, y, 1385, y + h), 22, fill=(246, 248, 252, 255), outline=(222, 228, 240), width=2)
    text_sp(d, (112, y + 26), 'ARGOMENTI', F('bold', 22), BLU, 3)
    for i, a in enumerate(argomenti):
        yy = y + 70 + i * step
        d.ellipse((112, yy + 11, 126, yy + 25), fill=BLU)
        d.text((146, yy), a, font=fl, fill=NOTTE)
    if prof: prof_frame(im)
    return im

def cornice_cam():
    """PNG con il foro arrotondato del riquadro 4:3: sopra al video fa gli angoli e l'ombra."""
    p = B + 'cornice_cam.png'
    if not os.path.exists(p):
        ref = Image.new('RGBA', (W, H), (255, 255, 255, 255)); shadow(ref, (1428, 148, 1840, 457), r=16, blur=18, off=(0, 12), alpha=70)
        ref = ref.crop((1428, 148, 1840, 457)); S = 4
        m = Image.new('L', (412 * S, 309 * S), 255); ImageDraw.Draw(m).rounded_rectangle((0, 0, 412 * S - 1, 309 * S - 1), 16 * S, fill=0)
        m = m.resize((412, 309), Image.LANCZOS); ref.putalpha(m); ref.save(p)
    return p
