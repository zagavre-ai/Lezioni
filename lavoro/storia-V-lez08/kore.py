#!/usr/bin/env python3
# Pezzi animati con voce Kore: schede blu, approfondimenti, mappe BES ramo per ramo, pillole, glossario, quiz, riepilogo.
import os, sys, json, re, subprocess, wave, math
import numpy as np
from PIL import Image, ImageDraw, ImageFilter
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import lib_slide as L
from profpiece import scrivi_wav, CACHE, W
KIT = '/home/user/Lezioni/kit/suoni/'
VOX = '/tmp/w/work/vox/'      # voci Kore (reali) ricevute dalla master
SW = 48000; FPS = 30
F = L.font
BLU = (11, 21, 48); TEL = (32, 96, 175); GIA = (255, 230, 0); BIA = (255, 255, 255)
def ease(x): x = max(0.0, min(1.0, x)); return x * x * (3 - 2 * x)
def stima(testo): return len(testo.split()) / 2.5 + 0.6
# ---------------- audio ----------------
def leggi_wav(path):
    r = subprocess.run(['ffmpeg', '-v', 'error', '-i', path, '-ac', '2', '-ar', '48000', '-f', 'f32le', '-'], capture_output=True).stdout
    return np.frombuffer(r, np.float32).reshape(-1, 2).copy()
def voce(nome, testo_stima=None):
    """ritorna (audio stereo 48k, reale?) ; se manca: silenzio di durata stimata (voce PROVVISORIA)"""
    p = VOX + nome + '.wav'
    if os.path.exists(p):
        x = leggi_wav(p); n = int(0.03 * SW); r = np.linspace(0, 1, n)[:, None]; x[:n] *= r; x[-n:] *= r[::-1]; return x, True
    return np.zeros((int(stima(testo_stima or 'x') * SW), 2), np.float32), False
def suono(nome, gain=1.0): return leggi_wav(KIT + nome) * gain
def mix(dur, eventi):
    out = np.zeros((int(round(dur * SW)), 2), np.float32)
    for x, t, g in eventi:
        a = int(round(t * SW)); b = min(len(out), a + len(x))
        if b > a: out[a:b] += x[:b - a] * g
    return out
# ---------------- scrittura pezzo ----------------
def scrivi(out, dur, painter, audio, fade=0.3):
    n = int(round(dur * FPS)); wav = out + '.wav'; scrivi_wav(wav, audio)
    cmd = ['ffmpeg', '-v', 'error', '-y', '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-s', '1920x1080', '-r', '30', '-i', '-', '-i', wav,
           '-vf', f'fade=t=in:st=0:d={fade},fade=t=out:st={dur - fade:.3f}:d={fade},format=yuv420p', '-t', f'{dur:.4f}', '-r', '30', '-c:v', 'libx264', '-preset', 'ultrafast', '-crf', '14',
           '-c:a', 'pcm_s16le', '-ar', '48000', out]
    p = subprocess.Popen(cmd, stdin=subprocess.PIPE, stderr=subprocess.PIPE)
    for i in range(n): p.stdin.write(painter(i / FPS).convert('RGB').tobytes())
    p.stdin.close(); err = p.stderr.read().decode()
    if p.wait(): raise SystemExit(err[-1500:])
    os.remove(wav); return dur
# ---------------- sfondo blu animato ----------------
_g = None
def blu(t):
    global _g
    if _g is None:
        y, x = np.mgrid[0:270, 0:480]; k = (x / 480 + y / 270) / 2
        _g = np.stack([11 + 12 * k, 21 + 38 * k, 48 + 62 * k], -1).astype(np.float32)
    a = Image.new('L', (480, 270), 0); d = ImageDraw.Draw(a)
    for i, (r, sp, ph) in enumerate([(70, .35, 0), (95, .22, 2), (50, .5, 4)]):
        cx = 240 + 190 * math.sin(t * sp + ph); cy = 135 + 90 * math.cos(t * sp * 1.3 + ph)
        d.ellipse((cx - r, cy - r, cx + r, cy + r), fill=70)
    a = np.asarray(a.filter(ImageFilter.GaussianBlur(24)), np.float32)[..., None] / 255
    im = np.clip(_g + a * np.array([30, 70, 130], np.float32), 0, 255).astype(np.uint8)
    return Image.fromarray(im).resize((1920, 1080), Image.BILINEAR)
def testo_c(d, xy, s, f, fill, anchor='la'): d.text(xy, s, font=f, fill=fill, anchor=anchor)
def rise(im, layer, x, y, p, dy=40):
    """incolla layer RGBA con apparizione (dissolvenza + salita)"""
    if p <= 0: return
    q = ease(p); l = layer.copy()
    if q < 1: l.putalpha(l.getchannel('A').point(lambda v: int(v * q)))
    im.alpha_composite(l, (int(x), int(y + dy * (1 - q))))
def cartella(testo, w, size=36, lh=1.45, attiva=False, fondo=None, col=None, num=None, bold=False):
    f = F('Figtree-SemiBold.ttf' if bold else 'Figtree-Medium.ttf', size); d0 = ImageDraw.Draw(Image.new('RGB', (4, 4)))
    righe = L.wrap(d0, testo, f, w - 80); h = int(len(righe) * size * lh) + 36
    pad = 30; l = Image.new('RGBA', (w + pad * 2, h + pad * 2), (0, 0, 0, 0))
    L.ombra(l, (pad, pad, pad + w, pad + h), 18, 6, 14, 40 if attiva else 20)
    d = ImageDraw.Draw(l)
    if attiva: d.rounded_rectangle((pad, pad, pad + w, pad + h), 18, fill=(255, 251, 214), outline=GIA, width=6); d.ellipse((pad + 20, pad + 22, pad + 38, pad + 40), fill=GIA, outline=(200, 170, 0), width=2)
    else: d.rounded_rectangle((pad, pad, pad + w, pad + h), 18, fill=fondo or (246, 248, 252), outline=(220, 226, 236), width=2)
    c = col or (BLU if attiva else (92, 102, 128))
    for i, r in enumerate(righe): d.text((pad + 58, pad + 18 + int(i * size * lh)), r, font=f, fill=c)
    return l, h
def base_bianca(kicker, titolo, pag, tsize=58):
    im = L.cornice(pag=pag, riquadro=False); d = ImageDraw.Draw(im)
    d.text((80, 144), kicker.upper(), font=F('Figtree-ExtraBold.ttf', 26), fill=TEL)
    ft = F('BricolageGrotesque-ExtraBold.ttf', tsize); righe = L.wrap(d, titolo, ft, 1700); y = 182
    for r in righe: d.text((80, y), r, font=ft, fill=BLU); y += int(tsize * 1.17)
    d.rounded_rectangle((80, y + 4, 165, y + 10), 3, fill=TEL)
    return im, y + 40
# ---------------- schede blu ----------------
def scheda_titolo(out, n, titolo, kws, pag=None):
    dur = 4.0
    ft = F('BricolageGrotesque-ExtraBold.ttf', 76); d0 = ImageDraw.Draw(Image.new('RGB', (4, 4))); righe = L.wrap(d0, titolo, ft, 1500)
    def p(t):
        im = blu(t).convert('RGBA'); d = ImageDraw.Draw(im)
        a = ease(t / .6);
        d.text((120, 330 - 20 * (1 - a)), f'ARGOMENTO {n}', font=F('Figtree-ExtraBold.ttf', 34), fill=GIA)
        y = 400
        for r in righe: d.text((120, y), r, font=ft, fill=BIA); y += 96
        d.rounded_rectangle((120, y + 10, 330 * ease((t - .3) / .8) + 120, y + 18), 4, fill=GIA)
        xx = 120; yy = y + 70
        for i, k in enumerate(kws[:3]):
            pr = ease((t - 1.0 - i * .4) / .5)
            if pr > 0:
                fk = F('Figtree-Bold.ttf', 34); w = int(d.textlength(k, font=fk)) + 50
                lay = Image.new('RGBA', (w, 70), (0, 0, 0, 0)); ImageDraw.Draw(lay).rounded_rectangle((0, 0, w - 1, 66), 33, fill=GIA); ImageDraw.Draw(lay).text((25, 14), k, font=fk, fill=BLU)
                rise(im, lay, xx, yy, pr, 20); xx += w + 20
        return im
    return scrivi(out, dur, p, mix(dur, [(suono('titolo.wav'), 0, 1.0)]))
def scheda_quiz(out, titolo, verifica=False):
    dur = 5.0
    def p(t):
        im = blu(t).convert('RGBA'); d = ImageDraw.Draw(im); a = ease(t / .5)
        d.text((960, 340), 'VERIFICA FINALE' if verifica else 'QUIZ', font=F('BricolageGrotesque-ExtraBold.ttf', 120), fill=BIA, anchor='mm')
        d.text((960, 470), titolo, font=F('Figtree-Bold.ttf', 44), fill=GIA, anchor='mm')
        d.text((960, 600), ('Dieci domande · per continuare serve almeno l\'80%' if verifica else 'Cinque domande · per continuare serve almeno l\'80%'), font=F('Figtree-Medium.ttf', 40), fill=BIA, anchor='mm')
        return im
    return scrivi(out, dur, p, mix(dur, [(suono('quiz.wav'), 0.5, 1.0)]))
def scheda_compiti_intro(out):
    dur = 3.5; v, real = voce('CINTRO_R2', 'Ora, i compiti.')
    def p(t):
        im = blu(t).convert('RGBA'); d = ImageDraw.Draw(im)
        d.text((960, 520), 'COMPITI', font=F('BricolageGrotesque-ExtraBold.ttf', 130), fill=BIA, anchor='mm')
        d.rounded_rectangle((960 - 150 * ease(t / .8), 600, 960 + 150 * ease(t / .8), 610), 5, fill=GIA)
        return im
    return scrivi(out, dur, p, mix(dur, [(suono('titolo.wav'), 0, .9), (v, 0.8, 1.0)])), real
# ---------------- ancore dalla voce trascritta ----------------
def parole_voce(jpath):
    d = json.load(open(jpath)); W_ = []
    for s in d:
        for t, w in s['parole']:
            if w.startswith(' ') or not W_: W_.append([t, w.strip()])
            else: W_[-1][1] += w
    return W_
def trova(W_, stem, da=0.0):
    st = stem.lower()
    for t, w in W_:
        if t >= da - 1e-6 and w.lower().startswith(st): return t
    return None
# ---------------- mappe BES ----------------
COL = {'pesca': ((255, 218, 200), (196, 64, 20)), 'celeste': ((221, 238, 255), (28, 84, 200)), 'pagl': ((255, 241, 190), (170, 110, 8)), 'menta': ((222, 244, 230), (24, 130, 70)), 'lilla': ((236, 228, 250), (100, 50, 200))}
LEG = [('pesca', 'concetto centrale'), ('celeste', 'date e sequenze'), ('pagl', 'parole chiave'), ('menta', 'esempi e opere'), ('lilla', 'conseguenze')]
def nodo_img(testo, w, h, col, size=40, attivo=False):
    fill, bord = COL[col]; pad = 20; l = Image.new('RGBA', (w + 2 * pad, h + 2 * pad), (0, 0, 0, 0)); d = ImageDraw.Draw(l)
    d.rounded_rectangle((pad, pad, pad + w, pad + h), 22, fill=(255, 230, 0) if attivo else fill, outline=bord, width=6)
    f = F('Figtree-SemiBold.ttf' if col == 'pesca' else 'Figtree-Medium.ttf', size); righe = L.wrap(d, testo, f, w - 50)
    y0 = pad + (h - len(righe) * int(size * 1.3)) // 2
    for i, r in enumerate(righe): d.text((pad + w // 2, y0 + i * int(size * 1.3)), r, font=f, fill=BLU, anchor='ma')
    return l
def freccia(d, p0, p1, pr=1.0, col=BLU, w=6):
    x0, y0 = p0; x1, y1 = p1; x = x0 + (x1 - x0) * pr; y = y0 + (y1 - y0) * pr
    d.line((x0, y0, x, y), fill=col, width=w)
    if pr >= 0.999:
        a = math.atan2(y1 - y0, x1 - x0); s = 20
        d.polygon([(x1, y1), (x1 - s * math.cos(a - .45), y1 - s * math.sin(a - .45)), (x1 - s * math.cos(a + .45), y1 - s * math.sin(a + .45))], fill=col)
def mappa(out, titolo, nodi, archi, voce_nome, testo_voce, ancore, tempi_stima=None, fisso_finale=4.0, solo_png=None):
    """nodi: {id:(testo,cx,cy,w,h,colore)}; archi: [(da,a,etichetta,id_nodo_quando_compare)]; ancore: {id: tempo} istante in cui la voce nomina il nodo"""
    v, real = voce(voce_nome, testo_voce); dv = len(v) / SW
    dur = 1.2 + dv + fisso_finale
    # tempi di comparsa dei nodi (+1.2 s di attacco della voce)
    tc = {k: 1.2 + ancore[k] for k in nodi}
    imgs = {k: (nodo_img(n[0], n[3], n[4], n[5], n[6] if len(n) > 6 else 40), nodo_img(n[0], n[3], n[4], n[5], n[6] if len(n) > 6 else 40, True)) for k, n in nodi.items()}
    base = L.cornice(pag=1, riquadro=False); d = ImageDraw.Draw(base)
    x = 1840
    for c, nm in reversed(LEG):
        fl = F('Figtree-Medium.ttf', 24); w = int(d.textlength(nm, font=fl)); d.text((x, 62), nm, font=fl, fill=BLU, anchor='ra'); x -= w + 10
        d.rounded_rectangle((x - 30, 60, x, 82), 5, fill=COL[c][0], outline=COL[c][1], width=3); x -= 52
    ft = F('BricolageGrotesque-ExtraBold.ttf', 44); d.text((80, 134), titolo, font=ft, fill=BLU)
    base.convert('RGB').save(f'{CACHE}/map_base.png')
    BASE = Image.open(f'{CACHE}/map_base.png').convert('RGBA')
    def painter(t):
        im = BASE.copy(); d = ImageDraw.Draw(im)
        # nodo in evidenza: l'ultimo comparso finché la voce lo legge (fino al successivo)
        ordine = sorted(nodi, key=lambda k: tc[k]); att = None
        for i, k in enumerate(ordine):
            fine = tc[ordine[i + 1]] if i + 1 < len(ordine) else 1.2 + dv
            if tc[k] <= t < fine: att = k
        for da, a, et in archi:
            pr = ease((t - tc[a]) / 0.5) if t >= tc[a] else 0
            if pr <= 0: continue
            n0 = nodi[da]; n1 = nodi[a]
            p0 = (n0[1], n0[2] + n0[4] / 2); p1 = (n1[1], n1[2] - n1[4] / 2 - 4)
            tops = [nodi[a2][2] - nodi[a2][4] / 2 for d2, a2, e2 in archi if d2 == da]; ym = p0[1] + (min(tops) - p0[1]) * 0.35
            pts = [p0, p1] if abs(p0[0] - p1[0]) < 2 else [p0, (p0[0], ym), (p1[0], ym), p1]
            tot = sum(math.dist(pts[i], pts[i + 1]) for i in range(len(pts) - 1)); run = pr * tot
            for i in range(len(pts) - 1):
                l = math.dist(pts[i], pts[i + 1])
                if run <= 0: break
                f_ = min(1.0, run / l) if l else 1.0
                xe = pts[i][0] + (pts[i + 1][0] - pts[i][0]) * f_; ye = pts[i][1] + (pts[i + 1][1] - pts[i][1]) * f_
                d.line((pts[i][0], pts[i][1], xe, ye), fill=BLU, width=6); run -= l
            if pr >= 0.999:
                ang = math.atan2(p1[1] - pts[-2][1], p1[0] - pts[-2][0]); sz = 22
                d.polygon([(p1[0], p1[1] + 4), (p1[0] - sz * math.cos(ang - .45), p1[1] + 4 - sz * math.sin(ang - .45)), (p1[0] - sz * math.cos(ang + .45), p1[1] + 4 - sz * math.sin(ang + .45))], fill=BLU)
            if et and pr > 0.7:
                fe = F('Figtree-Medium.ttf', 34); w = int(d.textlength(et, font=fe)) + 16
                ey = (pts[-2][1] + p1[1]) / 2; ex = p1[0] + 14
                d.rounded_rectangle((ex, ey - 22, ex + w, ey + 22), 8, fill=BIA); d.text((ex + 8, ey), et, font=fe, fill=BLU, anchor='lm')
        for k in ordine:
            p = ease((t - tc[k]) / 0.45)
            if p <= 0: continue
            n = nodi[k]; lay = imgs[k][1 if k == att else 0]
            rise(im, lay, n[1] - n[3] / 2 - 20, n[2] - n[4] / 2 - 20, p, 20)
        return im
    if solo_png: painter(dur - 0.5).convert('RGB').save(solo_png)
    aud = mix(dur, [(v, 1.2, 1.0)])
    if out: scrivi(out, dur, painter, aud)
    return dur, real
# ---------------- approfondimento ----------------
def approfondimento(out, nome, testo, pag, kicker='APPROFONDIMENTO'):
    v, real = voce(nome, testo); dv = len(v) / SW; dur = 1.6 + dv + 1.5
    fr = [s.strip() for s in re.split(r'(?<=[.?!])\s+', testo) if s.strip()]
    titolo = fr[0]; corpo = fr[1:]
    # tempi: proporzionali ai caratteri (voce provvisoria) — con voce reale si sostituiscono con le ancore trascritte
    tot = sum(len(s) for s in fr); t0 = 1.6; tf = []
    acc = 0
    for s in fr: tf.append(t0 + dv * acc / tot); acc += len(s)
    wcol = 830; cards = []; y = [0, 0]
    base, y0 = base_bianca(kicker, titolo, pag)
    lay = []
    for i, s in enumerate(corpo):
        col = i % 2; l, h = cartella(s, wcol, 38, 1.4)
        lay.append((l, l_att := cartella(s, wcol, 34, 1.4, attiva=True)[0], col, h))
    # posizionamento a due colonne
    pos = []; yc = [y0 + 10, y0 + 10]
    for i, (l, la, col, h) in enumerate(lay):
        c = 0 if yc[0] <= yc[1] else 1; pos.append((80 - 30 + c * 870, yc[c])); yc[c] += h + 70 - 30
    def painter(t):
        im = base.copy(); d = ImageDraw.Draw(im)
        d.rounded_rectangle((80, 1060, 80 + (1760) * min(1, max(0, (t - 1.6) / dv)), 1066), 3, fill=GIA) if False else None
        att = -1
        for i in range(len(corpo)):
            if tf[i + 1] <= t: att = i
        for i, (l, la, col, h) in enumerate(lay):
            p = ease((t - tf[i + 1]) / 0.5)
            if p > 0: rise(im, la if i == att else l, pos[i][0], pos[i][1], p, 30)
        pr = min(1, max(0, (t - 1.6) / dv)); d = ImageDraw.Draw(im)
        d.rounded_rectangle((80, 960, 1840, 966), 3, fill=(226, 230, 238)); d.rounded_rectangle((80, 960, 80 + 1760 * pr, 966), 3, fill=GIA)
        return im
    aud = mix(dur, [(suono('trans.wav'), 0, .5), (v, 1.6, 1.0)])
    if out: scrivi(out, dur, painter, aud)
    return dur, real
# ---------------- pillola: intro blu + schema che si accende ----------------
def pillola(out, n, titolo, pi_nome, pi_testo, righe_nomi, righe_testi, pag):
    vp, rp = voce(pi_nome, pi_testo); dvp = len(vp) / SW
    vs = [voce(nm, tx) for nm, tx in zip(righe_nomi, righe_testi)]
    t_intro = 0.6 + dvp + 1.0
    starts = []; t = t_intro + 0.8
    for v, r in vs: starts.append(t); t += len(v) / SW + 0.5
    dur = t + 1.5
    base, y0 = base_bianca('Ripasso', titolo, pag)
    lays = []; y = y0 + 20
    pos = []
    for tx in righe_testi:
        tx2 = re.sub(r'^(Primo|Secondo|Terzo|Quarto|Quinto|Sesto):\s*', '', tx); tx2 = tx2[0].upper() + tx2[1:]
        l, h = cartella(tx2, 1700, 38, 1.4); la = cartella(tx2, 1700, 38, 1.4, attiva=True)[0]
        lays.append((l, la)); pos.append((50, y)); y += h + 14
    def painter(t):
        if t < t_intro:
            im = blu(t).convert('RGBA'); d = ImageDraw.Draw(im)
            d.text((960, 430), 'RIPASSO', font=F('BricolageGrotesque-ExtraBold.ttf', 110), fill=BIA, anchor='mm')
            d.text((960, 570), titolo, font=F('Figtree-Bold.ttf', 46), fill=GIA, anchor='mm')
            return im
        im = base.copy(); att = -1
        for i, s in enumerate(starts):
            if s <= t < s + len(vs[i][0]) / SW + 0.5: att = i
        for i, s in enumerate(starts):
            p = ease((t - s + 0.2) / 0.5)
            if p > 0: rise(im, lays[i][1 if i == att else 0], pos[i][0], pos[i][1], p, 25)
        return im
    ev = [(suono('repaso.wav'), 0, .8), (vp, 0.6 + 0.0, 1.0)] + [(v, s, 1.0) for (v, r), s in zip(vs, starts)]
    scrivi(out, dur, painter, mix(dur, ev)); return dur, rp and all(r for v, r in vs)
# ---------------- glossario ----------------
def glossario(out, termini, voce_intro_testo, pag):
    vi, ri = voce('LG0', 'Ripassiamo le parole chiave della lezione.')
    vs = [voce(f'LG{i + 1}', d) for i, (t, d) in enumerate(termini)]
    starts = []; t = 1.5 + len(vi) / SW + 0.6
    for v, r in vs: starts.append(t); t += len(v) / SW + 0.45
    dur = t + 1.5
    base, y0 = base_bianca('Glossario', 'Le parole chiave della lezione', pag)
    cols = 2; lays = []; pos = []; yc = [y0 + 10] * cols
    for i, (tm, df) in enumerate(termini):
        l = Image.new('RGBA', (1, 1)); txt = f'{tm}: {df}'
        l, h = cartella(txt, 830, 32, 1.35); la = cartella(txt, 830, 32, 1.35, attiva=True)[0]
        c = 0 if i < (len(termini) + 1) // 2 else 1; pos.append((50 + c * 880, yc[c])); lays.append((l, la)); yc[c] += h + 8
    def painter(t):
        im = base.copy(); att = -1
        for i, s in enumerate(starts):
            if s <= t < s + len(vs[i][0]) / SW + 0.45: att = i
        for i, s in enumerate(starts):
            p = ease((t - s + 0.2) / 0.5)
            if p > 0: rise(im, lays[i][1 if i == att else 0], pos[i][0], pos[i][1], p, 25)
        return im
    ev = [(suono('trans.wav'), 0, .5), (vi, 1.5, 1.0)] + [(v, s, 1.0) for (v, r), s in zip(vs, starts)]
    scrivi(out, dur, painter, mix(dur, ev)); return dur, ri and all(r for v, r in vs)
# ---------------- riepilogo finale ----------------
def riepilogo(out, voce_nome, voce_testo, items, pag, kicker='Ripasso finale'):
    v, real = voce(voce_nome, voce_testo); dv = len(v) / SW; dur = 1.6 + dv + 1.5
    base, y0 = base_bianca(kicker, 'Riepilogo della lezione', pag)
    lays = []; pos = []; y = y0 + 10
    for i, (tx, anc) in enumerate(items):
        l, h = cartella(tx, 1700, 36, 1.35); la = cartella(tx, 1700, 36, 1.35, attiva=True)[0]; lays.append((l, la)); pos.append((50, y)); y += h + 6
    tf = [1.6 + a for tx, a in items]
    def painter(t):
        im = base.copy(); att = -1
        for i in range(len(items)):
            if tf[i] <= t: att = i
        for i in range(len(items)):
            p = ease((t - tf[i] + 0.2) / 0.5)
            if p > 0: rise(im, lays[i][1 if i == att else 0], pos[i][0], pos[i][1], p, 25)
        return im
    scrivi(out, dur, painter, mix(dur, [(suono('trans.wav'), 0, .5), (v, 1.6, 1.0)])); return dur, real
def immagini_fisse(out, pngs, durs, voce_nome, voce_testo, titolo_fisso=None):
    """mappe finali ferme (4 s ciascuna) con voce"""
    v, real = voce(voce_nome, voce_testo); dur = max(sum(durs), len(v) / SW + 2.0) + 0.5
    ims = [Image.open(p).convert('RGB') for p in pngs]
    def painter(t):
        acc = 0
        for im, d in zip(ims, durs):
            if t < acc + d: return im
            acc += d
        return ims[-1]
    scrivi(out, dur, painter, mix(dur, [(suono('trans.wav'), 0, .5), (v, 1.2, 1.0)])); return dur, real
