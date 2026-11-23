# Grafica comune delle videolezioni (modello Spagnolo/Letteratura): 1920x1080, fondo bianco
import os, re, textwrap, math
from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageChops
import numpy as np

FD = '/home/user/Lezioni/kit/caratteri/'
NAVY = (11, 21, 48); BLUE = (32, 96, 175); YEL = (255, 230, 0); GREY = (90, 101, 128)
LINE = (227, 232, 240); PALE = (243, 246, 251)
MATERIA = "STORIA DELL'ARTE V"
W, H = 1920, 1080
_fc = {}

def F(name, size):
    k = (name, size)
    if k not in _fc:
        f = {'title': 'BricolageGrotesque-ExtraBold.ttf', 'reg': 'Figtree-Regular.ttf', 'med': 'Figtree-Medium.ttf',
             'semi': 'Figtree-SemiBold.ttf', 'bold': 'Figtree-Bold.ttf', 'xbold': 'Figtree-ExtraBold.ttf'}[name]
        _fc[k] = ImageFont.truetype(FD + f, size)
    return _fc[k]

def tw(d, t, f, sp=0):
    return d.textlength(t, font=f) + sp * max(0, len(t) - 1)

def spaced(d, xy, t, f, fill, sp=0, anchor='l'):
    x, y = xy
    if anchor == 'r': x -= tw(d, t, f, sp)
    elif anchor == 'm': x -= tw(d, t, f, sp) / 2
    for ch in t:
        d.text((x, y), ch, font=f, fill=fill); x += d.textlength(ch, font=f) + sp

def wrap(d, t, f, maxw):
    words = t.split(); lines = []; cur = ''
    for w in words:
        c = (cur + ' ' + w).strip()
        if d.textlength(c, font=f) <= maxw: cur = c
        else:
            if cur: lines.append(cur)
            cur = w
    if cur: lines.append(cur)
    return lines

def shadow(img, box, r=22, blur=22, off=(0, 10), alpha=46, col=(70, 82, 110)):
    x0, y0, x1, y1 = box; pad = blur * 3
    lay = Image.new('RGBA', (x1 - x0 + 2 * pad, y1 - y0 + 2 * pad), (0, 0, 0, 0))
    ImageDraw.Draw(lay).rounded_rectangle((pad, pad, pad + x1 - x0, pad + y1 - y0), r, fill=col + (alpha,))
    lay = lay.filter(ImageFilter.GaussianBlur(blur))
    img.alpha_composite(lay, (x0 - pad + off[0], y0 - pad + off[1]))

_logo = {}
def logo(kind='blu', h=52):
    k = (kind, h)
    if k not in _logo:
        im = Image.open('/tmp/claude-0/w/build/logo_blu.png').convert('RGBA')
        if kind == 'white':
            a = im.split()[3]; im = Image.new('RGBA', im.size, (255, 255, 255, 255)); im.putalpha(a)
        _logo[k] = im.resize((int(im.width * h / im.height), h), Image.LANCZOS)
    return _logo[k]

def new_slide():
    im = Image.new('RGBA', (W, H), (255, 255, 255, 255)); d = ImageDraw.Draw(im)
    im.alpha_composite(logo('blu', 50), (80, 50))
    d.line((80, 124, 1840, 124), fill=LINE, width=2)
    d.line((80, 981, 1840, 981), fill=LINE, width=2)
    return im

def footer(im, page):
    d = ImageDraw.Draw(im)
    spaced(d, (80, 1003), MATERIA, F('bold', 22), BLUE, 3)
    if page: spaced(d, (1840, 1003), 'Pagina %d' % page, F('bold', 22), BLUE, 3, 'r')

def header(im, over, title, size=68, maxw=1300):
    d = ImageDraw.Draw(im)
    spaced(d, (80, 148), over.upper(), F('xbold', 24), BLUE, 4)
    f = F('title', size); lines = wrap(d, title, f, maxw)
    y = 190
    for ln in lines:
        d.text((80, y), ln, font=f, fill=NAVY); y += int(size * 1.08)
    d.rounded_rectangle((80, y + 8, 165, y + 14), 3, fill=BLUE)
    return y + 40   # y dove iniziano i contenuti

STRIP_NAME = 'Giorgio Mazzotti'; STRIP_SUB = "PROF. DI STORIA DELL'ARTE"
def right_column(im, keywords=None, box=True):
    """ombra del riquadro 4:3 (412x309 a x=1428,y=148), fascia gialla col nome, parole chiave"""
    d = ImageDraw.Draw(im)
    if box:
        shadow(im, (1428, 148, 1840, 457), r=16, blur=18, off=(0, 12), alpha=70)
        # fascia gialla leggermente inclinata
        sw, sh = 412, 100
        s = Image.new('RGBA', (sw + 40, sh + 40), (0, 0, 0, 0)); sd = ImageDraw.Draw(s)
        sd.rounded_rectangle((20, 20, 20 + sw, 20 + sh), 10, fill=YEL + (255,))
        sd.text((44, 34), STRIP_NAME, font=F('title', 38), fill=NAVY)
        spaced(sd, (44, 82), STRIP_SUB, F('bold', 21), NAVY, 1)
        s = s.rotate(2.2, resample=Image.BICUBIC, expand=True)
        shadow(im, (1432, 470, 1840, 565), r=10, blur=14, off=(0, 10), alpha=60)
        im.alpha_composite(s, (1428 - 20 - 8, 462 - 30))
    if keywords:
        y = 640
        spaced(d, (1428, y), 'PAROLE CHIAVE', F('xbold', 22), BLUE, 4); y += 44
        f = F('bold', 30)
        for k in keywords[:5]:
            w = int(d.textlength(k, font=f)) + 44
            d.rounded_rectangle((1428, y, 1428 + min(w, 412), y + 48), 24, fill=(232, 240, 252))
            d.ellipse((1442, y + 18, 1454, y + 30), fill=BLUE)
            d.text((1466, y + 6), k, font=f, fill=NAVY); y += 58

# ---------------------------------------------------------------- card
CARD_X0, CARD_X1 = 80, 1380
CARD_FONT = 40
def card_layout(d, texts, y0, gap=24):
    f = F('med', CARD_FONT); out = []; y = y0
    for t in texts:
        lines = wrap(d, t, f, CARD_X1 - CARD_X0 - 100)
        h = 2 * 22 + len(lines) * 54
        out.append((y, y + h, lines)); y += h + gap
    return out

def card_height(d, t):
    f = F('med', CARD_FONT)
    return 44 + len(wrap(d, t, f, CARD_X1 - CARD_X0 - 100)) * 54

def draw_card(im, lay, state):
    """state 0 nascosta, 1 attenuata, 2 accesa (bordo giallo + pallino giallo)"""
    if state == 0: return
    y0, y1, lines = lay; d = ImageDraw.Draw(im)
    box = (CARD_X0, y0, CARD_X1, y1)
    shadow(im, box, r=22, blur=18, off=(0, 8), alpha=60 if state == 2 else 34)
    d = ImageDraw.Draw(im)
    d.rounded_rectangle(box, 22, fill=(255, 255, 255) if state in (2, 3) else (246, 248, 252),
                        outline=YEL if state == 2 else (222, 228, 238), width=7 if state == 2 else 2)
    col = NAVY if state in (2, 3) else (100, 110, 135)
    cx, cy = CARD_X0 + 42, y0 + 22 + 27
    d.ellipse((cx - 11, cy - 11, cx + 11, cy + 11), fill=YEL if state == 2 else (BLUE if state == 3 else (200, 208, 222)),
              outline=NAVY if state == 2 else None, width=3 if state == 2 else 0)
    f = F('med', CARD_FONT); y = y0 + 22
    for ln in lines:
        d.text((CARD_X0 + 80, y), ln, font=f, fill=col); y += 54

# ---------------------------------------------------------------- immagine opera
def fit(img, mw, mh):
    r = min(mw / img.width, mh / img.height)
    return img.resize((max(1, int(img.width * r)), max(1, int(img.height * r))), Image.LANCZOS)

def draw_artwork(im, path, caption, area=(80, 150, 1380, 925)):
    d = ImageDraw.Draw(im)
    ax0, ay0, ax1, ay1 = area
    art = Image.open(path).convert('RGB'); art = fit(art, ax1 - ax0, ay1 - ay0)
    x = ax0 + (ax1 - ax0 - art.width) // 2; y = ay0 + (ay1 - ay0 - art.height) // 2
    shadow(im, (x, y, x + art.width, y + art.height), r=6, blur=22, off=(0, 14), alpha=80)
    im.paste(art, (x, y))
    d = ImageDraw.Draw(im); f = F('bold', 32); lines = wrap(d, caption, f, ax1 - ax0)
    yy = ay1 + 14
    for ln in lines[:2]:
        d.text(((ax0 + ax1) // 2 - d.textlength(ln, font=f) / 2, yy), ln, font=f, fill=NAVY); yy += 40

# ---------------------------------------------------------------- schede blu scure
def dark_bg(t=0.0):
    """sfondo blu scuro con bagliori morbidi; t in secondi per un lento movimento"""
    base = np.zeros((H // 4, W // 4, 3), np.float32)
    yy, xx = np.mgrid[0:H // 4, 0:W // 4].astype(np.float32)
    base[:] = (8, 14, 36)
    blobs = [(0.30 + 0.04 * math.sin(t * .4), 0.42, 0.34, (18, 62, 150), .85),
             (0.78 + 0.03 * math.cos(t * .3), 0.78 + 0.02 * math.sin(t * .5), 0.30, (120, 70, 40), .35),
             (0.88, 0.18 + 0.03 * math.sin(t * .35), 0.22, (28, 88, 190), .45)]
    for cx, cy, r, col, a in blobs:
        dd = ((xx / (W / 4) - cx) ** 2 * (16 / 9) ** 2 + (yy / (H / 4) - cy) ** 2) ** .5
        m = np.clip(1 - dd / r, 0, 1) ** 2 * a
        for c in range(3): base[..., c] += m * (col[c] - base[..., c] * .3)
    im = Image.fromarray(np.clip(base, 0, 255).astype(np.uint8)).resize((W, H), Image.BICUBIC).convert('RGBA')
    im.alpha_composite(logo('white', 46), (60, 40))
    return im

_dbc = {}
def dark_bg_cached(t=0.0, step=0.5):
    k = round(t / step)
    if k not in _dbc:
        if len(_dbc) > 200: _dbc.clear()
        _dbc[k] = dark_bg(k * step)
    return _dbc[k].copy()

def dark_label(im, text, y=300, x=140):
    d = ImageDraw.Draw(im); spaced(d, (x, y), text.upper(), F('xbold', 26), (255, 205, 60), 6)

def dark_title(im, text, y, size=120, x=140, col=(255, 255, 255), maxw=1500):
    d = ImageDraw.Draw(im); f = F('title', size)
    for ln in wrap(d, text, f, maxw):
        d.text((x, y), ln, font=f, fill=col); y += int(size * 1.05)
    return y

def sprinkle(im):
    return im
