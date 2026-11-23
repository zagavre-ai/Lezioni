# Costruzione dei pezzi · Storia dell'arte V · lez06
import os, re, json, sys, glob
import numpy as np
from PIL import Image, ImageDraw
sys.path.insert(0, '/tmp/w/build')
import lib, core, timing
from lib import W, H, font, NAVY, BLUE, YEL
from core import *
import content as K

VOCI = {v['nome']: v['testo'] for v in json.load(open('/tmp/w/voci/testi_voci.json'))}
PAGES_F = '/tmp/w/build/pages.json'
def pg(key):
    P = json.load(open(PAGES_F)) if os.path.exists(PAGES_F) else {}
    if key not in P: P[key] = len(P) + 1; json.dump(P, open(PAGES_F, 'w'), indent=0)
    return P[key]

# ---------------- immagini delle opere (ritaglio + ingrandimento) ----------------
_IM = {}
def work_image(key):
    if key in _IM: return _IM[key]
    src, box, cap = K.IMG[key]
    up = f'/tmp/w/up/{src}.png'
    if os.path.exists(up): im = Image.open(up).convert('RGB'); s = 4
    else: im = Image.open(f'/tmp/w/l6s/img/{src}.jpg').convert('RGB'); s = 1
    c = im.crop(tuple(int(v * s) for v in box))
    if s == 1: c = c.resize((c.width * 3, c.height * 3), Image.LANCZOS)
    _IM[key] = c; return c

def cap_of(key): return K.IMG[key][2]

# ---------------- slide: schede a card ----------------
CARD_W = 1290
def slide_cards(slide, on=None, label=None, page=1, cam=True, width=CARD_W, kw=True):
    im = lib.base(label, page, cam, slide['kw'] if (cam and kw) else None)
    y = lib.title(im, slide['title'], 186, maxw=1290 if cam else 1700)
    tot = 0
    for k, (e, t, h) in enumerate(slide['cards']):
        st = 'on' if on == k else 'n'
        hgt = lib.draw_card(im, 80, y, width, e, t, st); y += hgt + 20; tot = y
    assert y < 972, ('card oltre il piede', slide['title'], y)
    return im

def slide_img(keys, card=None, card_on=False, label=None, page=1, cam=True, kw=None):
    im = lib.base(label, page, cam, kw)
    imgs = [work_image(k) for k in keys]
    x0, y0, x1, y1 = 80, 196, 1360 if cam else 1840, 958
    area_w = x1 - x0
    if len(imgs) == 1:
        a = imgs[0]; asp = a.width / a.height
        if card is None:
            if asp >= 1.2:
                ph = lib.fit_image(a, area_w, 640); x = x0 + (area_w - ph.width) // 2
                lib.paste_photo(im, ph, x, y0); lib.caption(im, x0, y0 + ph.height + 22, area_w, cap_of(keys[0]))
            else:
                ph = lib.fit_image(a, 640 if not cam else 560, 720); lib.paste_photo(im, ph, x0, y0)
                cx = x0 + ph.width + 44; lib.caption(im, cx, y0 + 40, (x1 - cx), cap_of(keys[0]), 32)
        else:
            if asp >= 1.2:
                ph = lib.fit_image(a, area_w, 400); x = x0 + (area_w - ph.width) // 2
                lib.paste_photo(im, ph, x, y0); yy = lib.caption(im, x0, y0 + ph.height + 18, area_w, cap_of(keys[0]))
                lib.draw_card(im, x0, yy + 14, area_w, card[0], card[1], 'on' if card_on else 'n')
            else:
                ph = lib.fit_image(a, 470, 700); lib.paste_photo(im, ph, x0, y0)
                lib.caption(im, x0, y0 + ph.height + 14, ph.width + 60, cap_of(keys[0]), 26)
                cx = x0 + ph.width + 60; lib.draw_card(im, cx, y0 + 20, x1 - cx, card[0], card[1], 'on' if card_on else 'n')
    else:
        hh = 380 if card else 560; x = x0; bots = []
        for k in keys:
            ph = lib.fit_image(work_image(k), area_w, hh)
            lib.paste_photo(im, ph, x, y0)
            bots.append(lib.caption(im, x, y0 + ph.height + 12, max(ph.width + 40, 330), cap_of(k), 26)); x += max(ph.width + 40, 330) + 30
        if card:
            lib.draw_card(im, x0, max(bots) + 16, area_w, card[0], card[1], 'on' if card_on else 'n')
    return im

# ---------------- pezzi del prof ----------------
def build_teacher(name):
    P = K.PEZZI_PROF[name]; c0 = P['c0']; c1 = P['c1']
    n = nfr(c1 - c0); seq = Seq('tp_' + name)
    scenes = P['scene']; label = P['label']; first = True
    for si, sc in enumerate(scenes):
        t0 = max(0.0, sc[2] - c0) if si else 0.0
        ff = 0 if first else 9; first = False
        if sc[0] == 'cards':
            s = sc[1]; page = pg(f"{name}_{si}")
            seq.add(t0, slide_cards(s, None, label, page), ff)
            for k, (e, t, h) in enumerate(s['cards']):
                if h: seq.add(h - c0, slide_cards(s, k, label, page), 3)
        else:
            keys, card = sc[1], sc[3]; page = pg(f"{name}_{si}")
            seq.add(t0, slide_img(keys, card, False, label, page), ff)
            if card and card[2]: seq.add(card[2] - c0, slide_img(keys, card, True, label, page), 3)
    out = f'{PIECES}/{name}.mp4'
    video_teacher(seq, n, c0, out)
    return finish(name, n, out, teacher_audio(c0, n))

# ---------------- voce Kore (o segnaposto) ----------------
def voice(nome):
    x = load_audio(timing.voice_path(nome))
    if timing.is_real(nome):   # livello omogeneo, sempre con la voce intatta
        x = load_audio(timing.voice_path(nome), af='loudnorm=I=-16:TP=-1.5:LRA=7')
    return fade(x, 30, 40)

def voice_blocks(nome, blocks):
    W_ = timing.wav_words(nome, VOCI[nome]); return timing.align(blocks, W_)

def sentences(text): return [s for s in re.split(r'(?<=[.?!])\s+', text.strip()) if s]

# ---------------- schede blu ----------------
def dark_text(im, items):
    d = ImageDraw.Draw(im)
    for it in items: it(d)

def card_title(i):
    n = i; name = f'TIT{i}'
    t, short = K.ARGOMENTI[i - 1]; N = 120
    def frame(k):
        im = lib.dark_overlay_base(); d = ImageDraw.Draw(im)
        a = min(1.0, k)
        num = f'{i:02d}'
        big = font('t', 520); d.text((1130, 130), num, font=big, fill=(255, 255, 255, int(26 * a)))
        lib.spaced(d, (160, 360), 'ARGOMENTO %02d / %02d' % (i, len(K.ARGOMENTI)), font('b', 26), (255, 200, 60, int(255 * a)), 6)
        f = font('t', 92); words = t.split(); lines = []; cur = ''
        for w in words:
            tt = (cur + ' ' + w).strip()
            if f.getlength(tt) <= 1300: cur = tt
            else: lines.append(cur); cur = w
        lines.append(cur)
        for j, l in enumerate(lines): d.text((160, 420 + j * 104), l, font=f, fill=(255, 255, 255, int(255 * a)))
        yy = 420 + len(lines) * 104 + 18
        d.rounded_rectangle((160, yy, 330, yy + 6), 3, fill=(80, 170, 255, int(255 * a)))
        return im
    seq = Seq(name)
    for k, tt in enumerate([0.0, 0.15, 0.3, 0.45, 0.6]): seq.add(tt, frame(min(1, (k + 1) / 4)), 0)
    out = f'{PIECES}/{name}.mp4'; video_dark(seq, N, out)
    a = mix(N, [(0.0, jingle('titolo'), 0.8)])
    return finish(name, N, out, a)

def card_quiz(i):
    name = f'QZ{i}'; N = 150; t, short = K.ARGOMENTI[i - 1]
    im = lib.dark_overlay_base(); d = ImageDraw.Draw(im)
    lib.spaced(d, (160, 330), 'PAUSA DEL VIDEO · QUIZ', font('b', 26), (80, 190, 255, 255), 6)
    d.text((160, 390), 'Quiz %d' % i, font=font('t', 120), fill=(255, 255, 255, 255))
    d.text((160, 535), short, font=font('b', 56), fill=(255, 200, 60, 255))
    d.rounded_rectangle((160, 650, 760, 712), 16, fill=(255, 255, 255, 28))
    d.text((184, 660), "5 domande · serve almeno l'80%", font=font('sb', 32), fill=(235, 242, 255, 255))
    d.text((160, 750), 'Rispondi alle domande, poi premi «Continua».', font=font('r', 30), fill=(170, 195, 235, 255))
    d.ellipse((1380, 400, 1620, 640), outline=(80, 200, 255, 255), width=5)
    d.polygon([(1470, 450), (1470, 590), (1570, 520)], fill=(80, 200, 255, 255))
    d.text((1190, 170), '?', font=font('t', 620), fill=(255, 255, 255, 18))
    seq = Seq(name); seq.add(0, im, 0)
    out = f'{PIECES}/{name}.mp4'; video_dark(seq, N, out)
    a = mix(N, [(0.5, jingle('quiz'), 0.9)])           # scatto a +0,5 s dall'inizio della scheda
    return finish(name, N, out, a)

def card_pillola(i):
    p = K.PILLOLE[f'R{i}']; name = f'RIP{i}'; vname = p['voce']
    sents = sentences(VOCI[vname]); assert len(sents) == len(p['righe']), (vname, len(sents))
    A = voice(vname); tm = voice_blocks(vname, sents)
    lead = 1.6                                      # il jingle apre la scheda, la voce parte dopo
    dur = lead + len(A) / SR + 1.6; N = nfr(dur)
    def frame(on, shown):
        im = lib.dark_overlay_base(); d = ImageDraw.Draw(im)
        lib.spaced(d, (160, 190), 'PILLOLA DI RIPASSO', font('b', 26), (255, 200, 60, 255), 6)
        d.text((160, 235), 'RIPASSO', font=font('t', 96), fill=(255, 255, 255, 255))
        d.text((160, 350), p['titolo'], font=font('b', 46), fill=(90, 200, 255, 255))
        y = 440
        for k, r in enumerate(p['righe']):
            if k >= shown: break
            f = font('sb', 40); lines = lib.wrap_runs([(r, ('sb', 40))], 1450); hh = len(lines) * 52 + 28
            act = (k == on)
            d.rounded_rectangle((160, y, 1760, y + hh), 18, fill=(255, 255, 255, 40 if act else 16), outline=(255, 230, 0, 255) if act else (255, 255, 255, 40), width=5 if act else 2)
            d.ellipse((186, y + hh // 2 - 11, 208, y + hh // 2 + 11), fill=(255, 230, 0, 255) if act else (120, 150, 200, 255))
            yy = y + 14
            for ln in lines:
                d.text((232, yy), ' '.join(w for w, _ in ln), font=f, fill=(255, 255, 255, 255 if act else 175)); yy += 52
            y += hh + 14
        return im
    seq = Seq(name); seq.add(0, frame(-1, 0), 0)
    for k, (a, b) in enumerate(tm): seq.add(lead + a - 0.1, frame(k, k + 1), 4)
    seq.add(lead + tm[-1][1] + 0.4, frame(-1, len(tm)), 4)
    out = f'{PIECES}/{name}.mp4'; video_dark(seq, N, out)
    a = mix(N, [(0.0, jingle('repaso'), 0.7), (lead, A, 1.0)])
    return finish(name, N, out, a)

# ---------------- approfondimento (voce Kore + immagine con movimento lento) ----------------
def build_approf(i):
    a = K.APPROF[f'A{i}']; name = f'APP{i}'; vname = a['voce']
    sents = sentences(VOCI[vname]); A = voice(vname); tm = voice_blocks(vname, sents)
    lead = 0.8; dur = lead + len(A) / SR + 1.6; N = nfr(dur); page = pg(name)
    im0 = lib.base('Approfondimento', page, False); lib.title(im0, a['titolo'], 186, maxw=1700)
    src = work_image(a['img'][0]); asp = src.width / src.height
    ph_h = 640; ph_w = int(ph_h * asp); ph_w = min(ph_w, 900); ph_h = int(ph_w / asp)
    px, py = 80, 300
    base_ = im0.copy(); lib.shadow(base_, (px, py, px + ph_w, py + ph_h), 14, 18, (0, 10), 60)
    def frame(shown, on):
        im = base_.copy(); d = ImageDraw.Draw(im); x = px + ph_w + 60; y = 300
        for k, (txt, si) in enumerate(a['punti']):
            if k >= shown: break
            hh = lib.card_height(None, txt, 1840 - x, 38, 50)
            lib.draw_card(im, x, y, 1840 - x, None, txt, 'on' if k == on else 'n', 38, 50); y += hh + 16
        return im
    seq = Seq(name); seq.add(0, frame(0, -1), 0)
    tt = []
    for k, (txt, si) in enumerate(a['punti']):
        t0 = lead + tm[si - 1][0] - 0.1; tt.append(t0); seq.add(t0, frame(k + 1, k), 4)
    seq.add(lead + tm[-1][1] + 0.3, frame(len(a['punti']), -1), 4)
    # sfondo statico + foto con ingrandimento lento (zoompan) sovrapposta
    lst = seq.build(N)
    tmp = f'{WORK}/{name}_photo.png'; src.resize((ph_w * 2, ph_h * 2), Image.LANCZOS).save(tmp)
    mp = f'{WORK}/{name}_mask.png'; m = Image.new('L', (ph_w, ph_h), 0); ImageDraw.Draw(m).rounded_rectangle((0, 0, ph_w - 1, ph_h - 1), 14, fill=255); m.save(mp)
    g = (f'[0:v]fps=30,format=yuv420p[bg];[1:v]zoompan=z=\'1+0.10*on/{N}\':x=\'(iw-iw/zoom)/2\':y=\'(ih-ih/zoom)/2\':d={N}:s={ph_w}x{ph_h}:fps=30,format=rgba[p];'
         f'[2:v]format=gray[m];[p][m]alphamerge[pm];[bg][pm]overlay={px}:{py},format=yuv420p[v]')
    out = f'{PIECES}/{name}.mp4'
    encode(['-f', 'concat', '-safe', '0', '-i', lst, '-loop', '1', '-i', tmp, '-loop', '1', '-i', mp], g, N, out)
    return finish(name, N, out, mix(N, [(lead, A, 1.0)]))

# ---------------- cover, agenda ----------------
def cover_img(cam, shown=5, on=None, label='Videolezione'):
    page = 1
    im = lib.base(None, page, cam)
    d = ImageDraw.Draw(im)
    lib.spaced(d, (80, 148), "STORIA DELL'ARTE · VIDEOLEZIONE", font('b', 22), BLUE, 4)
    f = font('t', 92); words = K.TITOLO.split(); lines = []; cur = ''
    for w in words:
        t = (cur + ' ' + w).strip()
        if f.getlength(t) <= (1290 if cam else 1700): cur = t
        else: lines.append(cur); cur = w
    lines.append(cur)
    y = 210
    for l in lines: d.text((80, y), l, font=f, fill=NAVY); y += 104
    d.rounded_rectangle((80, y + 4, 180, y + 10), 3, fill=BLUE)
    y += 50
    # riquadro argomenti
    bx0, bx1 = 80, (1360 if cam else 1500)
    lib.shadow(im, (bx0, y, bx1, 960), 20, 16, (0, 8), 36)
    d.rounded_rectangle((bx0, y, bx1, 960), 20, fill=(247, 249, 252), outline=(214, 223, 236), width=2)
    lib.spaced(d, (bx0 + 36, y + 26), 'ARGOMENTI', font('b', 24), BLUE, 4)
    yy = y + 76; step = min(104, (960 - yy - 24) // 5)
    for k, (t, short) in enumerate(K.ARGOMENTI):
        act = (on == k)
        if k >= shown: break
        if act: d.rounded_rectangle((bx0 + 20, yy - 6, bx1 - 20, yy + step - 14), 14, fill=(255, 252, 228), outline=(255, 214, 0), width=4)
        d.ellipse((bx0 + 44, yy + 16, bx0 + 66, yy + 38), fill=YEL if act else (190, 205, 228), outline=NAVY if act else None, width=2)
        d.text((bx0 + 90, yy + 4), t, font=font('sb', 40), fill=NAVY); yy += step
    return im

def build_cover():
    name = 'COVER'; vname = 'B0_BENVENUTO'; A = voice(vname)
    blocks = ["Benvenuti alla lezione «Simbolismo e Art Nouveau».", "Partiremo dal Simbolismo e dalla crisi di fine Ottocento.", "Poi vedremo l'Art Nouveau in Francia e in Belgio,", "la Secessione viennese di Gustav Klimt,", "l'estetismo inglese, la Scuola di Glasgow e il Modernismo catalano di Antoni Gaudí.", "Arriveremo infine al Liberty in Italia e alla Scuola di Chicago.", "Cominciamo."]
    assert ' '.join(blocks).replace('«', '').replace('»', '') == VOCI[vname].replace('«', '').replace('»', '')
    tm = voice_blocks(vname, blocks); lead = 0.8; dur = lead + len(A) / SR + 1.2; N = nfr(dur)
    seq = Seq(name); seq.add(0, cover_img(False, 0, None), 0)
    for t, k in [(tm[1][0], 0), (tm[2][0], 1), (tm[3][0], 2), (tm[4][0], 3), (tm[5][0], 4)]:
        seq.add(lead + t - 0.1, cover_img(False, k + 1, k), 4)
    seq.add(lead + tm[6][0] - 0.1, cover_img(False, 5, None), 4)
    out = f'{PIECES}/{name}.mp4'; video_white(seq, N, out)
    return finish(name, N, out, mix(N, [(lead, A, 1.0)]))

def build_agenda_im(on=None):
    im = lib.base('Argomenti della lezione', pg('agenda'), True, None)
    y = lib.title(im, 'Argomenti', 186, maxw=1290)
    for k, (t, s) in enumerate(K.ARGOMENTI):
        h = lib.draw_card(im, 80, y, 1290, '%d' % (k + 1), t, 'n'); y += h + 14
    return im

def build_intro(part):
    """INTRO_A: prof sopra la copertina (0,6 -> 122,2 s) ; INTRO_B: prof con la slide degli argomenti (122,9 -> 253,7 s)"""
    name = 'INTRO_' + part
    c0, c1 = (0.3, 122.6) if part == 'A' else (122.35, 254.15)
    n = nfr(c1 - c0); seq = Seq(name)
    seq.add(0, cover_img(True, 5, None), 0) if part == 'A' else seq.add(0, build_agenda_im(), 0)
    out = f'{PIECES}/{name}.mp4'; video_teacher(seq, n, c0, out)
    return finish(name, n, out, teacher_audio(c0, n))

# ---------------- glossario, ripasso finale, verifica, compiti ----------------
def build_glossario():
    name = 'GLOSS'; vname = 'G_GLOSSARIO'; A = voice(vname)
    S = sentences(VOCI[vname]); assert len(S) == 11, len(S)
    tm = voice_blocks(vname, S); lead = 0.8; N = nfr(lead + len(A) / SR + 1.6)
    pages = [[0, 1, 2], [3, 4, 5], [6, 7], [8, 9]]
    seq = Seq(name); first = True
    def slide(pi, on):
        im = lib.base('Glossario', pg(f'gloss{pi}'), False); y = lib.title(im, 'Glossario', 186, maxw=1700)
        for k in pages[pi]:
            t, dfn = K.GLOSSARIO[k]
            h = lib.draw_card(im, 80, y, 1760, t, dfn, 'on' if k == on else 'n'); y += h + 22
        assert y < 975, (pi, y); return im
    seq.add(0, slide(0, -1), 0)
    for k in range(10):
        pi = [i for i, p in enumerate(pages) if k in p][0]
        seq.add(lead + tm[k + 1][0] - 0.1, slide(pi, k), 9 if (k == pages[pi][0] and k) else 3)
    out = f'{PIECES}/{name}.mp4'; video_white(seq, N, out)
    return finish(name, N, out, mix(N, [(lead, A, 1.0)]))

def build_ripasso_finale():
    name = 'RIEPILOGO'; vname = 'F_RIPASSO_FINALE'; A = voice(vname)
    S = sentences(VOCI[vname]); blocks = [S[0]]; cur = []
    for s in S[1:]:
        if re.match(r'^(Primo|Secondo|Terzo|Quarto|Quinto) argomento\.$', s):
            if cur: blocks.append(' '.join(cur)); cur = []
        cur.append(s)
    blocks.append(' '.join(cur)); assert len(blocks) == 6, len(blocks)
    tm = voice_blocks(vname, blocks); lead = 1.6; N = nfr(lead + len(A) / SR + 1.6)
    def frame(on, shown):
        im = lib.dark_overlay_base(); d = ImageDraw.Draw(im)
        lib.spaced(d, (160, 190), 'ARGOMENTO PER ARGOMENTO', font('b', 26), (255, 200, 60, 255), 6)
        d.text((160, 225), 'RIPASSO FINALE', font=font('t', 80), fill=(255, 255, 255, 255))
        y = 335
        for k, (t, txt) in enumerate(K.RIPASSO_FINALE):
            if k >= shown: break
            act = (k == on); lines = lib.wrap_runs([(txt, ('r', 32))], 1000); hh = max(len(lines) * 42, 90) + 26
            d.rounded_rectangle((160, y, 1760, y + hh), 18, fill=(255, 255, 255, 40 if act else 16), outline=(255, 230, 0, 255) if act else (255, 255, 255, 40), width=5 if act else 2)
            d.ellipse((186, y + hh // 2 - 11, 208, y + hh // 2 + 11), fill=(255, 230, 0, 255) if act else (120, 150, 200, 255))
            tl = lib.wrap_runs([(t, ('b', 34))], 400); yy0 = y + (hh - len(tl) * 44) // 2
            for ln in tl: d.text((232, yy0), ' '.join(w for w, _ in ln), font=font('b', 34), fill=(120, 215, 255, 255 if act else 190)); yy0 += 44
            yy = y + 13
            for ln in lines:
                d.text((690, yy), ' '.join(w for w, _ in ln), font=font('r', 32), fill=(255, 255, 255, 255 if act else 175)); yy += 42
            y += hh + 10
        assert y < 1075, y; return im
    seq = Seq(name); seq.add(0, frame(-1, 0), 0)
    for k in range(5): seq.add(lead + tm[k + 1][0] - 0.1, frame(k, k + 1), 4)
    seq.add(lead + tm[5][1] + 0.3, frame(-1, 5), 4)
    out = f'{PIECES}/{name}.mp4'; video_dark(seq, N, out)
    return finish(name, N, out, mix(N, [(0.0, jingle('repaso'), 0.7), (lead, A, 1.0)]))

def build_verifica():
    name = 'VERIFICA'; vname = 'V_VERIFICA'; A = voice(vname); lead = 1.0; N = nfr(lead + len(A) / SR + 2.0)
    im = lib.dark_overlay_base(); d = ImageDraw.Draw(im)
    lib.spaced(d, (160, 330), 'PAUSA DEL VIDEO · VERIFICA', font('b', 26), (80, 190, 255, 255), 6)
    d.text((160, 390), 'Verifica finale', font=font('t', 112), fill=(255, 255, 255, 255))
    d.text((160, 530), 'Verifica di sbarramento', font=font('b', 54), fill=(255, 200, 60, 255))
    d.rounded_rectangle((160, 640, 900, 702), 16, fill=(255, 255, 255, 28))
    d.text((184, 650), "10 domande · serve almeno l'80%", font=font('sb', 32), fill=(235, 242, 255, 255))
    d.text((160, 740), 'Rispondi alle domande, poi premi «Continua».', font=font('r', 30), fill=(170, 195, 235, 255))
    d.ellipse((1380, 400, 1620, 640), outline=(80, 200, 255, 255), width=5)
    d.polygon([(1470, 450), (1470, 590), (1570, 520)], fill=(80, 200, 255, 255))
    seq = Seq(name); seq.add(0, im, 0)
    out = f'{PIECES}/{name}.mp4'; video_dark(seq, N, out)
    return finish(name, N, out, mix(N, [(0.0, jingle('titolo'), 0.7), (lead + 1.0, A, 1.0)]))

def build_compiti_intro():
    name = 'COMPITI_INTRO'; N = nfr(3.5)
    im = lib.dark_overlay_base(); d = ImageDraw.Draw(im)
    lib.spaced(d, (160, 400), 'DA SVOLGERE', font('b', 28), (255, 200, 60, 255), 6)
    d.text((160, 450), 'Compiti', font=font('t', 150), fill=(255, 255, 255, 255))
    d.rounded_rectangle((160, 640, 330, 646), 3, fill=(80, 170, 255, 255))
    seq = Seq(name); seq.add(0, im, 0)
    out = f'{PIECES}/{name}.mp4'; video_dark(seq, N, out)
    return finish(name, N, out, mix(N, [(0.0, jingle('titolo'), 0.8)]))

def build_compiti():
    name = 'COMPITI'; vname = 'COMPITI'; A = voice(vname); S = sentences(VOCI[vname])
    # blocchi: un compito ciascuno + la frase finale
    blocks = []; cur = []
    for s in S:
        if re.match(r'^Compito (uno|due|tre|quattro)\.$', s):
            if cur: blocks.append(' '.join(cur)); cur = []
        cur.append(s)
    blocks.append(' '.join(cur))
    # separa la frase finale
    last = blocks[-1]; i = last.rfind('Svolgi'); blocks[-1] = last[:i].strip(); blocks.append(last[i:])
    assert len(blocks) == 5, len(blocks)
    tm = voice_blocks(vname, blocks); lead = 0.8; N = nfr(lead + len(A) / SR + 1.5)
    labels = ['Compito 1', 'Compito 2', 'Compito 3', 'Compito 4']
    def slide(pi, on):
        im = lib.base('Compiti', pg(f'compiti{pi}'), False); y = lib.title(im, 'Compiti', 186, maxw=1700)
        if pi < 2:
            for k in (2 * pi, 2 * pi + 1):
                h = lib.draw_card(im, 80, y, 1760, labels[k], K.COMPITI[k], 'on' if k == on else 'n'); y += h + 22
        else:
            h = lib.draw_card(im, 80, y, 1760, None, 'Svolgi i compiti qui sotto e premi «Consegna»: arrivano al docente nel tuo quaderno dei compiti.', 'on' if on == 4 else 'n', 44, 58); y += h
            d = ImageDraw.Draw(im); d.rounded_rectangle((80, y + 40, 460, y + 130), 22, fill=BLUE); d.text((130, y + 62), 'Consegna', font=font('t', 46), fill=(255, 255, 255))
        assert y < 980, (pi, y); return im
    seq = Seq(name); seq.add(0, slide(0, -1), 0)
    for k in range(5):
        pi = 0 if k < 2 else (1 if k < 4 else 2)
        seq.add(lead + tm[k][0] - 0.1, slide(pi, k), 9 if k in (2, 4) else 3)
    out = f'{PIECES}/{name}.mp4'; video_white(seq, N, out)
    return finish(name, N, out, mix(N, [(lead, A, 1.0)]))

# ---------------- sigle ----------------
def build_sigla(path, name, gain=1.0):
    d = float(sh(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', path]).stdout)
    N = nfr(d); out = f'{PIECES}/{name}.mp4'
    sh(['ffmpeg', '-y', '-v', 'error', '-i', path, '-vf', 'scale=1920:1080:flags=lanczos,fps=30,format=yuv420p', '-frames:v', str(N)] + ENC + ['-force_key_frames', kf(N), '-an', out])
    A = load_audio(path)[:N * SPF]
    if len(A) < N * SPF: A = np.vstack([A, np.zeros((N * SPF - len(A), 2), np.float32)])
    return finish(name, N, out, A * gain)
