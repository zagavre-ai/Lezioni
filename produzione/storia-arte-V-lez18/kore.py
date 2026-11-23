# Schede animate (voce Kore) · motore di rendering a fotogrammi + audio mixato
import sys, os, re, json, subprocess, math
import numpy as np
sys.path.insert(0, '/home/user/w18')
from lib import *
from dati import *
import piano
R = '/home/user/w18/'; OUT = R + 'b/'; SUON = '/home/user/Lezioni/kit/suoni/'
SR = 48000; FPS = 30
DARK = '0x0E1C42'

# ---------------- audio ----------------
def load(p):
    return np.frombuffer(subprocess.run(['ffmpeg', '-v', 'error', '-i', p, '-ac', '1', '-ar', str(SR), '-f', 'f32le', '-'], capture_output=True).stdout, np.float32)

def savewav(y, p):
    subprocess.run(['ffmpeg', '-v', 'error', '-y', '-f', 'f32le', '-ar', str(SR), '-ac', '1', '-i', '-', p], input=y.astype(np.float32).tobytes(), check=True)

def split_sent(t):
    t = t.replace('Frank O. Gehry', 'Frank O.§Gehry').replace('L.O.V.E.', 'L§O§V§E§')
    return [x.replace('§', ' ' if False else '§').strip() for x in re.split(r'(?<=[.?!])\s+', t) if x.strip()]
def unfix(t): return t.replace('Frank O.§Gehry', 'Frank O. Gehry').replace('L§O§V§E§', 'L.O.V.E.')

def nparole(t): return max(1, len(t.split()))

def vox_path(name):
    for d in ('vox/', 'b/prov_'):
        p = R + d + name + '.wav'
        if os.path.exists(p): return p, d == 'vox/'
    return None, False

def vinfo(name, units):
    """-> (percorso wav, durata, [inizio di ogni unità in s relativi all'inizio della voce], reale?)"""
    n = [nparole(u) for u in units]; tot = sum(n)
    p, real = vox_path(name)
    if real:
        key = R + 'vox/' + name + '.json'
        if not os.path.exists(key):
            subprocess.run([sys.executable, '/home/user/Lezioni/kit/tools/trascrivi.py', p, R + 'vox/' + name], check=True, capture_output=True)
        S = json.load(open(key))
        W = [x for s in S for x in s['parole']]
        dur = len(load(p)) / SR
        st = []; c = 0
        for k in n:
            i = min(len(W) - 1, int(round(c * len(W) / tot))); st.append(max(0.0, W[i][0] - 0.05)); c += k
        return p, dur, st, True
    dur = tot / 2.6 + 0.3 * len(units)
    st = []; c = 0
    for i, k in enumerate(n):
        st.append(c / 2.6 + 0.3 * i); c += k
    if p is None:
        p = R + 'b/prov_' + name + '.wav'; savewav(np.zeros(int(dur * SR), np.float32), p)
    return p, dur, st, False

def vnorm(p, real):
    """Kore: −16 LUFS (solo voci vere)"""
    if not real: return p
    o = OUT + 'vn_' + os.path.basename(p)
    if not os.path.exists(o) or os.path.getmtime(o) < os.path.getmtime(p):
        subprocess.run(['ffmpeg', '-v', 'error', '-y', '-i', p, '-af', 'highpass=f=70,loudnorm=I=-16:TP=-1.5:LRA=9', '-ar', str(SR), '-ac', '1', o], check=True)
    return o

def mixa(ev, dur):
    y = np.zeros(int(dur * SR) + SR, np.float32)
    for p, t, g in ev:
        x = load(p) * g; s = int(t * SR)
        if s < 0: x = x[-s:]; s = 0
        m = min(len(x), len(y) - s)
        if m > 0: y[s:s + m] += x[:m]
    y = y[:int(dur * SR)]
    f = int(0.025 * SR)
    y[:f] *= np.linspace(0, 1, f); y[-f:] *= np.linspace(1, 0, f)
    return y

# ---------------- scena ----------------
FADE = {}
def scena(nome, dur, frame_fn, ev, fin='dark', fout='dark', fade=0.3, force=False):
    if nome in FADE: fin, fout = FADE[nome]
    out = OUT + nome + '.mp4'
    if os.path.exists(out) and not force: return out
    dur = round(dur * FPS) / FPS
    wav = OUT + nome + '.wav'; savewav(mixa(ev, dur), wav)
    col = lambda c: 'white' if c == 'white' else DARK
    ff = subprocess.Popen(['ffmpeg', '-v', 'error', '-y', '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-s', f'{W}x{H}', '-r', str(FPS), '-i', '-', '-i', wav,
        '-vf', f'fade=t=in:st=0:d={fade}:color={col(fin)},fade=t=out:st={dur - fade:.3f}:d={fade}:color={col(fout)},format=yuv420p',
        '-c:v', 'libx264', '-preset', 'ultrafast', '-crf', '14', '-pix_fmt', 'yuv420p', '-c:a', 'aac', '-b:a', '256k', '-ar', '48000', '-ac', '2', '-t', f'{dur:.3f}', out], stdin=subprocess.PIPE)
    last = None; lb = None
    for i in range(int(round(dur * FPS))):
        im = frame_fn(i / FPS)
        if im is not last: lb = np.asarray(im.convert('RGB')).tobytes(); last = im
        ff.stdin.write(lb)
    ff.stdin.close(); ff.wait()
    return out

# ---------------- fondo blu veloce ----------------
_spr = {}
def sprite(s):
    if s not in _spr:
        yy, xx = np.mgrid[0:s, 0:s]; r = np.hypot(xx - s / 2, yy - s / 2) / (s / 2)
        _spr[s] = (np.clip(1 - r, 0, 1) ** 2).astype(np.float32)
    return _spr[s]
_base = None
def bgb(t):
    global _base
    w, h = 960, 540
    if _base is None:
        yy = np.linspace(0, 1, h)[:, None, None]
        _base = (np.array([14, 28, 66], np.float32) * (1 - yy) + np.array([8, 15, 38], np.float32) * yy) * np.ones((1, w, 1), np.float32)
    img = _base.copy()
    for k, (cx, cy, sx, sy, col, sz, al) in enumerate([(250, 150, .11, .07, (32, 96, 175), 520, .34), (750, 400, .08, .10, (32, 96, 175), 600, .34), (500, 280, .06, .05, (255, 230, 0), 300, .05)]):
        px = cx + 110 * math.sin(t * sx + k); py = cy + 70 * math.cos(t * sy + k * 2)
        s = sz; sp = sprite(s); x0, y0 = int(px - s / 2), int(py - s / 2)
        xa, ya = max(0, x0), max(0, y0); xb, yb = min(w, x0 + s), min(h, y0 + s)
        if xb <= xa or yb <= ya: continue
        m = sp[ya - y0:yb - y0, xa - x0:xb - x0, None] * al
        img[ya:yb, xa:xb] = img[ya:yb, xa:xb] * (1 - m) + np.array(col, np.float32) * m
    return Image.fromarray(img.clip(0, 255).astype(np.uint8)).resize((W, H), Image.BILINEAR).convert('RGBA')

class Blu:
    """cache di fondo blu a 15 Hz + logo"""
    def __init__(self): self.k = None; self.im = None
    def get(self, t):
        k = int(t * 15)
        if k != self.k:
            self.k = k; self.im = bgb(k / 15); self.im.alpha_composite(logo('bianco', 52), (80, 50))
        return self.im

def card_scuro(im, box, lines, active, size=36, lh=52, lead=None, alpha_text=255):
    x0, y0, x1, y1 = box
    lay = Image.new('RGBA', im.size, (0, 0, 0, 0)); d = ImageDraw.Draw(lay)
    d.rounded_rectangle(box, 24, fill=(255, 255, 255, 46 if active else 22), outline=GIALLO + (255,) if active else (255, 255, 255, 70), width=6 if active else 2)
    ty = y0 + 20
    for ln in lines:
        xx = x0 + 44
        for w_, fo in ln:
            d.text((xx, ty), w_, font=fo, fill=(255, 255, 255, 255 if active else 175)); xx += d.textlength(w_ + ' ', font=fo)
        ty += lh
    if active: d.ellipse((x0 + 14, (y0 + y1) // 2 - 8, x0 + 30, (y0 + y1) // 2 + 8), fill=GIALLO + (255,))
    im.alpha_composite(lay)

def layout_testo(d, lead, body, size, maxw):
    f = F('reg', size); fb = F('bold', size)
    words = ([(w, fb) for w in lead.split(' ')] if lead else []) + [(w, f) for w in body.split(' ')]
    lines = []; cur = []; cw = 0
    for w, fo in words:
        wl = d.textlength(w + ' ', font=fo)
        if cw + wl > maxw and cur: lines.append(cur); cur = []; cw = 0
        cur.append((w, fo)); cw += wl
    if cur: lines.append(cur)
    return lines

def intestazione(im, label, titolo=None, size=60, y=160):
    d = ImageDraw.Draw(im)
    text_sp(d, (100, y), label.upper(), F('bold', 28), GIALLO, 4)
    yy = y + 52
    if titolo:
        f = F('bric', size)
        for ln in wrap(d, titolo, f, 1720)[:2]:
            d.text((100, yy), ln, font=f, fill=BIANCO); yy += size + 10
    return yy

# ---------------- schede ----------------
def titolo_scheda(i, a, titolo, force=False):
    n = f'tit_{a}'
    B_ = Blu(); dur = 3.4
    def fr(t):
        im = B_.get(t).copy(); d = ImageDraw.Draw(im)
        e = ease(t / 0.6); dy = int((1 - e) * 40)
        lay = Image.new('RGBA', im.size, (0, 0, 0, 0)); dl = ImageDraw.Draw(lay)
        text_sp(dl, (140, 330 + dy), f'ARGOMENTO {i}', F('bold', 36), GIALLO, 6)
        f = F('bric', 92); y = 400 + dy
        for ln in wrap(dl, titolo, f, 1640)[:3]:
            dl.text((140, y), ln, font=f, fill=BIANCO); y += 106
        w = int(ease((t - 0.3) / 0.7) * 300)
        dl.rounded_rectangle((140, y + 14, 140 + max(4, w), y + 24), 5, fill=GIALLO)
        lay.putalpha(lay.getchannel('A').point(lambda v: int(v * ease(t / 0.5))))
        im.alpha_composite(lay); return im
    return scena(n, dur, fr, [(SUON + 'trans.wav', 0.0, 0.7), (SUON + 'titolo.wav', 0.3, 0.8)], 'white', 'white', force=force)

def quiz_scheda(a, titolo, force=False):
    B_ = Blu(); dur = 4.3
    def fr(t):
        im = B_.get(t).copy(); lay = Image.new('RGBA', im.size, (0, 0, 0, 0)); dl = ImageDraw.Draw(lay)
        text_sp(dl, (140, 330), 'QUIZ', F('bold', 36), GIALLO, 8)
        dl.text((140, 396), 'Cinque domande', font=F('bric', 100), fill=BIANCO)
        dl.text((140, 540), 'Per continuare serve almeno l’80% di risposte giuste.', font=F('semi', 44), fill=(255, 255, 255, 235))
        dl.rounded_rectangle((140, 626, 140 + int(ease((t - 0.3) / 0.8) * 300), 636), 5, fill=GIALLO)
        lay.putalpha(lay.getchannel('A').point(lambda v: int(v * ease(t / 0.5)))); im.alpha_composite(lay); return im
    return scena(f'quiz_{a}', dur, fr, [(SUON + 'quiz.wav', 0.5, 0.9)], 'white', 'dark', force=force)

def lista_scheda(nome, label, titolo, items, voice, units, jingle=None, jt=0.3, v0=None, size=36, lh=52, tail=1.2, modo='acc', fout='dark', fin='dark',
                 titolo_size=56, force=False):
    """items: [(lead, body)] una per unità `units[k]` che parte da unità `first` (le unità extra senza riga)"""
    p, dur_v, st, real = vinfo(voice, units)
    p = vnorm(p, real)
    v0 = (v0 if v0 is not None else 0.7)
    dur = v0 + dur_v + tail
    B_ = Blu()
    d0 = ImageDraw.Draw(Image.new('RGBA', (10, 10)))
    maxw = 1560
    lays = [layout_testo(d0, l, b, size, maxw) for l, b in items]
    hs = [len(x) * lh + 40 for x in lays]
    # unità -> riga (la prima unità può essere l'intestazione letta)
    off = len(units) - len(items)
    starts = [v0 + st[off + k] for k in range(len(items))]
    ends = [starts[k + 1] if k + 1 < len(items) else v0 + dur_v for k in range(len(items))]
    cache = {}
    def fr(t):
        key = (int(t * 15), tuple(1 if t >= s else 0 for s in starts), tuple(1 if s <= t < e else 0 for s, e in zip(starts, ends)))
        if key in cache: return cache[key]
        im = B_.get(t).copy()
        y = intestazione(im, label, titolo, size=titolo_size) + 24
        if modo == 'acc':
            for k in range(len(items)):
                if t < starts[k]: continue
                act = starts[k] <= t < ends[k] + 0.05
                e = ease((t - starts[k]) / 0.35)
                card_scuro(im, (100, y, 1820, y + hs[k]), lays[k], act)
                y += hs[k] + 16
        else:  # una per volta
            for k in range(len(items)):
                if starts[k] <= t < ends[k] + 0.2 or (k == len(items) - 1 and t >= starts[k]):
                    y0 = 330 if len(items) > 1 else y
                    card_scuro(im, (100, y0, 1820, y0 + hs[k]), lays[k], True); break
        cache[key] = im; return im
    ev = [(SUON + 'trans.wav', 0.0, 0.6)]
    if jingle: ev.append((SUON + jingle, jt, 0.8))
    ev.append((p, v0, 1.0))
    return scena(nome, dur, fr, ev, fin, fout, force=force)

def pillola(a, titolo, force=False):
    units = RIP[a]; units_v = [voce(u) for u in units]
    items = [('', u) for u in units]
    return lista_scheda(f'rip_{a}', 'Ripasso', titolo, items, f'{a}_RIPASSO', units_v, jingle='repaso.wav', jt=0.25, v0=2.4, titolo_size=54,
                        fin='white', fout='white', force=force)

def ripasso_finale(force=False):
    n = ['Primo', 'Secondo', 'Terzo', 'Quarto', 'Quinto', 'Sesto', 'Settimo']
    units = ['Ripassiamo la lezione, argomento per argomento.'] + [f'{n[i]}: {t}, {d}' for i, (t, d) in enumerate(RF)]
    items = [(f'{i + 1} · {t}:', d) for i, (t, d) in enumerate(RF)]
    return lista_scheda('rf', 'Ripasso finale', 'Argomento per argomento', items, 'RIPASSO_FINALE', [voce(u) for u in units], v0=1.0, size=34, lh=48, tail=1.5,
                        titolo_size=52, force=force)

def glossario(force=False):
    units = ['Il glossario della lezione.'] + [f"{t.replace('World Wide Web (WWW)', 'World Wide Web, in sigla WWW')}. {d}" for t, d in GLOSS]
    items = [(t + ':', d.replace('World Wide Web', 'World Wide Web')) for t, d in GLOSS]
    items[2] = ('World Wide Web (WWW), cioè la rete mondiale dei siti:', GLOSS[2][1])
    return lista_scheda('gloss', 'Glossario', 'Le parole della lezione', items, 'GLOSSARIO', [voce(u) for u in units], jingle='titolo.wav', jt=0.3, v0=1.0, size=40, lh=58, modo='uno',
                        tail=1.5, force=force)

def compiti(force=False):
    units = [f'Compito {ORD[i]}. {t}' for i, t in enumerate(COMPITI)] + [COMPITI_FINALE]
    items = [(f'Compito {i + 1}:', t) for i, t in enumerate(COMPITI)] + [('', COMPITI_FINALE)]
    return lista_scheda('compiti', 'Compiti', 'Da svolgere dopo la lezione', items, 'COMPITI', [voce(u) for u in units], v0=0.8, size=34, lh=50, modo='uno', tail=2.0,
                        titolo_size=52, force=force)

def compiti_intro(force=False):
    B_ = Blu(); dur = 3.5
    def fr(t):
        im = B_.get(t).copy(); lay = Image.new('RGBA', im.size, (0, 0, 0, 0)); dl = ImageDraw.Draw(lay)
        text_sp(dl, (140, 400), 'ORA TOCCA A TE', F('bold', 36), GIALLO, 6)
        dl.text((140, 470), 'Compiti', font=F('bric', 130), fill=BIANCO)
        dl.rounded_rectangle((140, 640, 140 + int(ease((t - 0.3) / 0.8) * 320), 650), 5, fill=GIALLO)
        lay.putalpha(lay.getchannel('A').point(lambda v: int(v * ease(t / 0.5)))); im.alpha_composite(lay); return im
    return scena('compiti_intro', dur, fr, [(SUON + 'titolo.wav', 0.2, 0.9)], 'dark', 'dark', force=force)

def verifica(force=False):
    p, dur_v, st, real = vinfo('VERIFICA', [VER]); p = vnorm(p, real)
    B_ = Blu(); v0 = 2.6; dur = v0 + dur_v + 1.2
    def fr(t):
        im = B_.get(t).copy(); lay = Image.new('RGBA', im.size, (0, 0, 0, 0)); dl = ImageDraw.Draw(lay)
        text_sp(dl, (140, 330), 'VERIFICA FINALE', F('bold', 36), GIALLO, 8)
        dl.text((140, 396), 'Dieci domande', font=F('bric', 100), fill=BIANCO)
        dl.text((140, 540), 'Per superarla servono almeno 8 risposte giuste su 10 (80%).', font=F('semi', 44), fill=(255, 255, 255, 235))
        dl.rounded_rectangle((140, 626, 140 + int(ease((t - 0.3) / 0.8) * 300), 636), 5, fill=GIALLO)
        lay.putalpha(lay.getchannel('A').point(lambda v: int(v * ease(t / 0.5)))); im.alpha_composite(lay); return im
    return scena('verifica', dur, fr, [(SUON + 'quiz.wav', 0.5, 0.9), (p, v0, 1.0)], 'dark', 'dark', force=force)

def benvenuto(force=False):
    units = split_sent(BENVENUTO)
    p, dur_v, st, real = vinfo('BENVENUTO', units); p = vnorm(p, real)
    v0 = 0.8; dur = v0 + dur_v + 0.8
    cov = copertina(TITOLO, [t for _, t in ARGOMENTI], prof=False, page=1)
    # evidenzia l'argomento letto
    def fr_i(k):
        im = cov.copy(); d = ImageDraw.Draw(im)
        return im
    base = cov.copy(); cache = {}
    # righe argomenti: y = 205+92*? ricalcolo con la stessa geometria di copertina()
    d = ImageDraw.Draw(base)
    lines = wrap(d, TITOLO, F('bric', 78), 1300); y = 205 + 92 * len(lines) + 40
    def fr(t):
        t_ = t - v0
        k = -1
        for i in range(len(units)):
            if t_ >= st[i]: k = i
        # unità 0 = benvenuto, 1 = «oggi...», 2..8 = argomenti 1..7
        idx = k - 2 if 2 <= k <= 8 else -1
        if idx in cache: return cache[idx]
        im = cov.copy()
        if idx >= 0:
            dd = ImageDraw.Draw(im); yy = y + 70 + idx * 52
            dd.rounded_rectangle((104, yy - 6, 1360, yy + 46), 14, outline=GIALLO, width=5)
        cache[idx] = im; return im
    return scena('welcome', dur, fr, [(p, v0, 1.0)], 'dark', 'white', force=force)

# ---------------- approfondimenti ----------------
def kb_image(src, w, h, t, dur, z=0.07):
    s = 1 + z * (t / dur)
    base = fit_big(src, int(w * 1.0), int(h * 1.0)) if False else None
    return None

def _fit_cover(src, w, h):
    s = max(w / src.width, h / src.height)
    return src.resize((int(src.width * s) + 1, int(src.height * s) + 1), Image.LANCZOS)

AP_CFG = {
 'A2': ('I4L', [('Dopo l', 'Ritorno alla figurazione, in chiave ironica e disincantata', 0), ('Nel 1991', '1991 · Sherrie Levine · Fountain (After Marcel Duchamp)', 0),
               ('fonde in bronzo', 'Bronzo lucido: da oggetto provocatorio a feticcio da museo', 0), ('È l\'appropriazionismo', 'Appropriazionismo: si mettono in discussione originalità e unicità', 0),
               ('Così Levine', 'Mercificazione dell’arte e perdita dell’aura', 0)]),
 'A3': ('I8', [('Nomade ed eclettico', 'Transavanguardia: nomade ed eclettica (1979)', 0), ('Gli artisti rivendicano', 'Libertà di attraversare tutti gli stili del passato', 0),
               ('Sandro Chia', 'Sandro Chia · Gioco di mano, 1980', 0), ('Francesco Clemente', 'Francesco Clemente · Il cerchio di Milarepa, 1982', 0),
               ('Mimmo Paladino', 'Mimmo Paladino · La verità del fornaio in carrozza, 1981', 0)]),
 'A4': ('I10', [('Il Tuttomondo', 'Tuttomondo · Sant’Antonio, Pisa · 1989', 0), ('Trenta figure', 'Trenta figure antropomorfe concatenate', 0),
               ('Ogni figura', 'Un inno alla vita, alla pace e alla solidarietà globale', 0), ('Il suo alfabeto', 'Radiant Baby: il bambino radiante, innocenza e speranza', 0)]),
 'A5': ('I12', [('Per questo', 'La fotografia perde la funzione documentaria', 0), ('Amazon', 'Andreas Gursky · Amazon, 2016', 0),
               ('Prospettiva zenitale', 'Prospettiva zenitale, luce fredda, post-produzione digitale', 0), ('Lo spazio diventa', 'Un pattern geometrico, ipnotico e infinito', 0),
               ('I milioni', 'Iperconsumismo, alienazione del lavoro, logistica globale', 0)]),
 'A6': ('I19L', [('Le Artistar', 'Artistar: artisti diventati celebrità globali', 0), ('Si trova', 'Piazza degli Affari, Milano · 2010', 0),
               ('marmo bianco', 'Marmo bianco di Carrara · 11 metri', 0), ('Il titolo', 'L.O.V.E. = libertà, odio, vendetta, eternità', 0),
               ('Collocata', 'Critica ai totalitarismi e ribellione al potere economico', 0)]),
 'A7': ('I22', [('Il Centre', 'Centre Georges Pompidou · Parigi · 1977', 0), ('Piano e Rogers svuotano', 'Tubature e strutture portanti sulla facciata', 0),
               ('I tubi', 'Blu · aria condizionata', .30), ('I tubi', 'Giallo · elettricità', .50), ('I tubi', 'Verde · acqua', .66), ('I tubi', 'Rosso · ascensori e scale mobili', .82),
               ('All\'interno', 'Spazi immensi, fluidi, senza pilastri portanti', 0)]),
}
CHIP = {'Blu': (60, 120, 220), 'Giallo': (255, 214, 0), 'Verde': (40, 170, 90), 'Rosso': (220, 50, 50)}

def img_ap(sid):
    if sid == 'I8': f, cr = 'p-008-011.jpg', None
    else: _, f, cr, _k = piano.IMG[sid]
    src = Image.open(R + 'img/' + f).convert('RGB')
    if cr: src = src.crop((int(cr[0] * src.width), int(cr[1] * src.height), int(cr[2] * src.width), int(cr[3] * src.height)))
    return src

def approfondimento(a, titolo, force=False):
    text = AP[a]; units_d = split_sent(text); units = [voce(unfix(u)) for u in units_d]
    p, dur_v, st, real = vinfo(f'{a}_APPROF', units); p = vnorm(p, real)
    v0 = 0.8; tail = 1.4; dur = v0 + dur_v + tail
    B = {}
    if a == 'A1': return ap_a1(units_d, units, p, dur_v, st, v0, tail, force)
    sid, cfg = AP_CFG[a]
    src = img_ap(sid)
    IW, IH = 900, 740; IX, IY = 80, 215
    big = _fit_cover(src, int(IW * 1.1), int(IH * 1.1))
    # tempi delle card
    tri = []
    for kw, txt, fr_ in cfg:
        i = next((k for k, u in enumerate(units_d) if kw in unfix(u)), 0)
        t0 = v0 + st[i]; t1 = v0 + (st[i + 1] if i + 1 < len(st) else dur_v)
        tri.append(t0 + fr_ * (t1 - t0))
    d0 = ImageDraw.Draw(Image.new('RGBA', (10, 10)))
    lays = [layout_testo(d0, '', c[1], 32, 700) for c in cfg]
    hs = [len(x) * 46 + 36 for x in lays]
    ends = [tri[k + 1] if k + 1 < len(tri) else v0 + dur_v for k in range(len(tri))]
    from pages import PG
    static = base_slide('Approfondimento', PG['AP_' + a], footer=True)
    shadow(static, (IX, IY, IX + IW, IY + IH), r=18, blur=20, off=(0, 10), alpha=60)
    dd = ImageDraw.Draw(static); text_sp(dd, (80, 148), ('APPROFONDIMENTO · ' + titolo).upper()[:70], F('bold', 25), BLU, 3)
    mask = Image.new('L', (IW, IH), 0); ImageDraw.Draw(mask).rounded_rectangle((0, 0, IW - 1, IH - 1), 18, fill=255)
    SP = {}
    def sprite_card(k, act):
        if (k, act) in SP: return SP[(k, act)]
        M = 30; w_ = 820; h_ = hs[k]
        sp = Image.new('RGBA', (w_ + 2 * M, h_ + 2 * M), (0, 0, 0, 0))
        shadow(sp, (M, M, M + w_, M + h_), r=20, blur=14, off=(0, 6), alpha=50 if act else 25)
        dl = ImageDraw.Draw(sp)
        dl.rounded_rectangle((M, M, M + w_, M + h_), 20, fill=(255, 255, 255, 255) if act else (247, 249, 252, 255), outline=GIALLO if act else (226, 231, 240), width=5 if act else 2)
        txt = cfg[k][1]; ch_ = txt.split(' · ')[0]; tx = M + 34
        if a == 'A7' and 2 <= k <= 5 and ch_ in CHIP:
            dl.rounded_rectangle((M + 26, M + h_ // 2 - 22, M + 70, M + h_ // 2 + 22), 10, fill=CHIP[ch_], outline=NOTTE, width=2); tx = M + 90
        ty = M + 18
        for ln in lays[k]:
            xx = tx
            for w2, fo in ln:
                dl.text((xx, ty), w2, font=F('semi', 32), fill=NOTTE if act else (120, 128, 148)); xx += dl.textlength(w2 + ' ', font=F('semi', 32))
            ty += 46
        SP[(k, act)] = sp; return sp
    def fr(t):
        im = static.copy()
        z = 1 + 0.08 * (t / dur); cw, ch = int(IW / z), int(IH / z)
        bx = (big.width - cw) // 2; by = (big.height - ch) // 2
        crop = big.crop((bx, by, bx + cw, by + ch)).resize((IW, IH), Image.BILINEAR)
        im.paste(crop.convert('RGBA'), (IX, IY), mask)
        y = IY
        for k in range(len(cfg)):
            if t < tri[k]: continue
            act = tri[k] <= t < ends[k] + 0.05
            e = ease((t - tri[k]) / 0.35); dx = int((1 - e) * 60)
            sp = sprite_card(k, act)
            if e < 1:
                sp = sp.copy(); sp.putalpha(sp.getchannel('A').point(lambda v: int(v * e)))
            im.alpha_composite(sp, (1020 + dx - 30, y - 30))
            y += hs[k] + 16
        return im
    return scena(f'ap_{a}', dur, fr, [(SUON + 'trans.wav', 0.0, 0.6), (p, v0, 1.0)], 'white', 'white', force=force)

def ap_a1(units_d, units, p, dur_v, st, v0, tail, force):
    dur = v0 + dur_v + tail
    def when(kw, frac=0):
        i = next((k for k, u in enumerate(units_d) if kw in u), 0)
        t0 = v0 + st[i]; t1 = v0 + (st[i + 1] if i + 1 < len(st) else dur_v)
        return t0 + frac * (t1 - t0)
    phases = [('Agricoltura', when('agricoltura', 0.0)), ('Industria', when('agricoltura', 0.35)), ('Terziario tecnologico', when('agricoltura', 0.65))]
    mil = [('1979', 'Lyotard teorizza la condizione postmoderna', when('1979', .15)), ('1989', 'Cade il muro di Berlino', when('Nel 1989', .0)),
           ('1991', 'Si scioglie l’Unione Sovietica', when('Nel 1989', .55)), ('2001', 'Attacco alle Twin Towers', when('Twin Towers', .3))]
    from pages import PG
    static = base_slide('Approfondimento', PG['AP_A1'])
    cache = {}
    def fr(t):
        anim = any(0 <= t - x[1] < 0.45 for x in phases) or any(0 <= t - x[2] < 0.45 for x in mil)
        key = (int(t * 30) if anim else -1, tuple(1 if t >= x[1] else 0 for x in phases), tuple(1 if t >= x[2] else 0 for x in mil))
        if key in cache: return cache[key]
        im = static.copy(); d = ImageDraw.Draw(im)
        # fasi
        xs = [80, 700, 1320]; wbox = 520
        for k, (n, ts) in enumerate(phases):
            if t < ts: continue
            e = ease((t - ts) / 0.4); lay = Image.new('RGBA', im.size, (0, 0, 0, 0))
            shadow(lay, (xs[k], 230, xs[k] + wbox, 380), r=22, blur=14, off=(0, 6), alpha=45)
            dl = ImageDraw.Draw(lay)
            dl.rounded_rectangle((xs[k], 230, xs[k] + wbox, 380), 22, fill=(255, 255, 255, 255), outline=BLU, width=4)
            text_sp(dl, (xs[k] + 30, 252), f'FASE {k + 1}', F('bold', 22), BLU, 3)
            for j, ln in enumerate(wrap(dl, n, F('bric', 44), wbox - 60)): dl.text((xs[k] + 30, 288 + j * 48), ln, font=F('bric', 44), fill=NOTTE)
            lay.putalpha(lay.getchannel('A').point(lambda v: int(v * e))); im.alpha_composite(lay)
            if k < 2 and t >= phases[k + 1][1]:
                ax = xs[k] + wbox + 20; d = ImageDraw.Draw(im)
                d.line((ax, 305, ax + 60, 305), fill=NOTTE, width=8); d.polygon([(ax + 80, 305), (ax + 52, 288), (ax + 52, 322)], fill=NOTTE)
        # linea del tempo
        d = ImageDraw.Draw(im); d.line((120, 700, 1800, 700), fill=NOTTE, width=6)
        text_sp(d, (120, 450), 'DATE', F('bold', 24), BLU, 3)
        px = {'1979': 260, '1989': 760, '1991': 1060, '2001': 1560}
        for yv, txt, ts in mil:
            if t < ts: continue
            e = ease((t - ts) / 0.4); lay = Image.new('RGBA', im.size, (0, 0, 0, 0)); dl = ImageDraw.Draw(lay)
            cx = px[yv]; dl.ellipse((cx - 16, 684, cx + 16, 716), fill=GIALLO, outline=NOTTE, width=4)
            up = yv in ('1979', '1991')
            by0 = 500 if up else 740
            wbox = 420; bx0 = cx - wbox // 2
            dl.line((cx, 716 if not up else 684, cx, (740 if not up else 650)), fill=NOTTE, width=4)
            shadow(lay, (bx0, by0, bx0 + wbox, by0 + 150), r=20, blur=12, off=(0, 6), alpha=45)
            dl = ImageDraw.Draw(lay)
            dl.rounded_rectangle((bx0, by0 if not up else by0, bx0 + wbox, by0 + 150), 20, fill=(255, 255, 255, 255), outline=BLU, width=4)
            dl.text((bx0 + 28, by0 + 14), yv, font=F('bric', 50), fill=BLU)
            for j, ln in enumerate(wrap(dl, txt, F('semi', 30), wbox - 56)): dl.text((bx0 + 28, by0 + 74 + j * 38), ln, font=F('semi', 30), fill=NOTTE)
            lay.putalpha(lay.getchannel('A').point(lambda v: int(v * e))); im.alpha_composite(lay)
        cache[key] = im; return im
    return scena('ap_A1', dur, fr, [(SUON + 'trans.wav', 0.0, 0.6), (p, v0, 1.0)], 'white', 'white', force=force)

# ---------------- mappe ----------------
COL = {'centro': ((255, 220, 198), (194, 65, 12)), 'date': ((220, 238, 251), (29, 78, 216)), 'chiave': ((255, 243, 191), (161, 98, 7)),
       'esempi': ((221, 243, 228), (21, 128, 61)), 'conseg': ((235, 227, 247), (109, 40, 217))}
LEG = [('centro', 'concetto centrale'), ('date', 'date e sequenze'), ('chiave', 'parole chiave'), ('esempi', 'esempi e opere'), ('conseg', 'conseguenze')]
MAPDEF = {   # centro, larghezza, altezza, ruolo colore; posizioni come nella mappa del prof
 'MAP1': dict(box=[((960, 310), 940, 130, 'centro', 54), ((380, 640), 640, 220, 'chiave', 42), ((1000, 840), 800, 150, 'esempi', 42), ((1520, 560), 620, 230, 'conseg', 42)],
              arrows=[(0, 1), (0, 2), (0, 3)], units=[None, 0, None, 1, 2, 3]),
 'MAP2': dict(box=[((1000, 360), 760, 150, 'centro', 54), ((440, 740), 700, 200, 'chiave', 42), ((1460, 700), 700, 240, 'esempi', 42)],
              arrows=[(0, 1), (0, 2)], units=[None, 0, None, 1, 2]),
 'MAP3': dict(box=[((1000, 380), 1100, 210, 'centro', 42), ((620, 640), 900, 190, 'chiave', 42), ((1400, 860), 760, 190, 'esempi', 42)],
              arrows=[], units=[None, 0, 1, 2]),
}
MAPTXT = {k: [n[1] for n in v['nodi']] for k, v in MAPPE.items()}

def draw_arrow(d, p0, p1, prog):
    x0, y0 = p0; x1, y1 = p1
    xe = x0 + (x1 - x0) * prog; ye = y0 + (y1 - y0) * prog
    d.line((x0, y0, xe, ye), fill=NOTTE, width=10)
    if prog >= 0.98:
        ang = math.atan2(y1 - y0, x1 - x0); L = 40
        pts = [(x1, y1), (x1 - L * math.cos(ang - 0.45), y1 - L * math.sin(ang - 0.45)), (x1 - L * math.cos(ang + 0.45), y1 - L * math.sin(ang + 0.45))]
        d.polygon(pts, fill=NOTTE)

def edge_pt(c, w, h, toward):
    cx, cy = c; tx, ty = toward; dx, dy = tx - cx, ty - cy
    if dx == 0 and dy == 0: return c
    s = min((w / 2) / abs(dx) if dx else 1e9, (h / 2) / abs(dy) if dy else 1e9)
    return (cx + dx * s, cy + dy * s)

def mappa_scheda(key, nome, page, force=False):
    M = MAPPE[key]; D = MAPDEF[key]; texts = MAPTXT[key]
    units_d = split_sent(MAPV[key]); units = [unfix(u) for u in units_d]
    p, dur_v, st, real = vinfo(key + {'MAP1': '_FINALE', 'MAP2': '_STREETART', 'MAP3': '_ARTISTAR_ARCHISTAR'}[key], [voce(u) for u in units]); p = vnorm(p, real)
    assert len(units) == len(D['units']), (key, len(units))
    v0 = 0.8; hold = 4.0; dur = v0 + dur_v + 0.6 + hold
    # tempi riquadri
    tb = {}; te = {}
    for ui, b in enumerate(D['units']):
        if b is None: continue
        tb[b] = v0 + st[ui]; te[b] = v0 + (st[ui + 1] if ui + 1 < len(st) else dur_v)
    t_end_voice = v0 + dur_v
    f_t = F('bric', 46)
    base = base_slide('', page)
    d = ImageDraw.Draw(base)
    # legenda in alto a destra
    x = 1840; fl = F('semi', 20)
    for k_, lab in reversed(LEG):
        w_ = d.textlength(lab, font=fl); x -= w_; d.text((x, 64), lab, font=fl, fill=NOTTE); x -= 34
        d.rounded_rectangle((x, 66, x + 24, 86), 4, fill=COL[k_][0], outline=COL[k_][1], width=3); x -= 22
    # domanda-titolo
    q = M['domanda']
    d.text((80, 150), q, font=F('bric', 50), fill=NOTTE)
    fills = {}
    ar_t = {}
    for (a, b) in D['arrows']: ar_t[b] = a
    cache = {}
    def fr(t):
        anim = any(0 <= t - (tb[i] - 0.5) < 0.95 for i in range(len(texts)))
        key_ = (int(t * 30) if anim else -1, tuple(1 if t >= tb[i] - 0.5 else 0 for i in range(len(texts))),
                tuple(1 if tb[i] <= t < te[i] and t < t_end_voice + 0.1 else 0 for i in range(len(texts))))
        if key_ in cache: return cache[key_]
        im = base.copy(); d = ImageDraw.Draw(im)
        for i, (c, w_, h_, role, sz) in enumerate(D['box']):
            if t < tb[i] - 0.5: continue
            # freccia
            if i in ar_t:
                a_ = ar_t[i]; ca, wa, ha = D['box'][a_][0], D['box'][a_][1], D['box'][a_][2]
                p0 = edge_pt(ca, wa + 30, ha + 30, c); p1 = edge_pt(c, w_ + 30, h_ + 30, ca)
                prog = ease((t - (tb[i] - 0.5)) / 0.5); draw_arrow(d, p0, p1, prog)
            if t < tb[i]: continue
            e = ease((t - tb[i]) / 0.35)
            act = tb[i] <= t < te[i] + (0.0 if i < len(texts) - 1 else 0.0) and t < t_end_voice + 0.1
            fill, bord = COL[role]
            x0, y0 = c[0] - w_ / 2, c[1] - h_ / 2 + (1 - e) * 18
            lay = Image.new('RGBA', im.size, (0, 0, 0, 0)); dl = ImageDraw.Draw(lay)
            if act: dl.rounded_rectangle((x0 - 10, y0 - 10, x0 + w_ + 10, y0 + h_ + 10), 22, fill=GIALLO)
            dl.rounded_rectangle((x0, y0, x0 + w_, y0 + h_), 16, fill=fill, outline=bord, width=6 if role == 'centro' else 5)
            f_ = F('bric', sz) if role == 'centro' else F('semi', sz)
            lines = wrap(dl, texts[i], f_, w_ - 50); lh_ = int(sz * 1.3); ty = y0 + (h_ - lh_ * len(lines)) / 2 + 2
            for ln in lines:
                dl.text((x0 + (w_ - dl.textlength(ln, font=f_)) / 2, ty), ln, font=f_, fill=NOTTE); ty += lh_
            if e < 1: lay.putalpha(lay.getchannel('A').point(lambda v: int(v * e)))
            im.alpha_composite(lay)
        cache[key_] = im; return im
    return scena(nome, dur, fr, [(SUON + 'trans.wav', 0.0, 0.6), (p, v0, 1.0)], 'white', 'white', force=force)

if __name__ == '__main__':
    pass
