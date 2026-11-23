import sys
sys.path.insert(0, '/tmp/claude-0/w/build')
from scenes import *

DIM = (128, 148, 190)

def karaoke(layer, words, wtimes, t, x0, x1, y0, size, center=False, spoken=(255, 255, 255), cur=(255, 230, 0)):
    """parole di un frammento, evidenziate man mano che la voce le pronuncia"""
    d = ImageDraw.Draw(layer); f = F('semi', size); sp = d.textlength(' ', font=f)
    lines = [[]]; cw = 0
    for i, w in enumerate(words):
        ww = d.textlength(w, font=f)
        if lines[-1] and cw + sp + ww > x1 - x0: lines.append([]); cw = 0
        lines[-1].append((i, w, ww)); cw += (sp if len(lines[-1]) > 1 else 0) + ww
    y = y0; lh = int(size * 1.34)
    for ln in lines:
        tot = sum(w for _, _, w in ln) + sp * (len(ln) - 1); x = x0 + ((x1 - x0 - tot) / 2 if center else 0)
        for i, w, ww in ln:
            nxt = wtimes[i + 1] if i + 1 < len(wtimes) else wtimes[i] + 0.5
            col = DIM if t < wtimes[i] - 0.02 else (cur if t < nxt - 0.02 else spoken)
            d.text((x, y), w, font=f, fill=col); x += ww + sp
        y += lh
    return y

def lines_h(words, size, width):
    im = Image.new('RGBA', (10, 10)); d = ImageDraw.Draw(im); f = F('semi', size); sp = d.textlength(' ', font=f)
    n = 1; cw = 0
    for i, w in enumerate(words):
        ww = d.textlength(w, font=f)
        if cw and cw + sp + ww > width: n += 1; cw = ww
        else: cw += (sp if cw else 0) + ww
    return n * int(size * 1.34)

def ken(art, boxw, boxh, z, dx, dy):
    aw, ah = art.size
    cw, ch = aw / z, ah / z
    x0 = (aw - cw) / 2 + dx * (aw - cw) / 2; y0 = (ah - ch) / 2 + dy * (ah - ch) / 2
    return art.resize((aw, ah), Image.BILINEAR, box=(x0, y0, x0 + cw, y0 + ch))

def appro_scene(sid, vname, fr_img, topic, lead=0.8, tail=1.2):
    fr = [f for f, _ in fr_img]; v = voice(vname)
    times, wt = asr.align(v['words'], fr, span=v['span'], want_words=True)
    N = int(math.ceil((lead + v['span'][1] + tail) * FPS)); e = Enc(OUT + 'seg/%s.mp4' % sid)
    track = np.zeros(N * 1600 + SR, np.float32); place(track, v['a'], lead, 1.0)
    # immagini: intervalli
    arts = {}
    for _, im in fr_img:
        if im and im not in arts:
            a = Image.open(R + 'opere2/%s.png' % im).convert('RGB'); arts[im] = fit(a, 960, 640)
    segs = []   # (img, t_start, t_end)
    for i, (_, im) in enumerate(fr_img):
        t0 = lead + times[i][0]; t1 = lead + times[i][1]
        if segs and segs[-1][0] == im: segs[-1][2] = t1
        else: segs.append([im, t0, t1])
    segs[0][1] = 0.0; segs[-1][2] = N / FPS
    mpos = [(i, words) for i, words in enumerate(fr)]
    for i in range(N):
        t = i / FPS; im = dark_bg_cached(t, 0.5); d = ImageDraw.Draw(im)
        # frammento corrente
        k = 0
        for j in range(len(fr)):
            if t >= lead + times[j][0] - 0.05: k = j
        cur_img = None; seg = None
        for s in segs:
            if s[1] - 0.001 <= t < s[2]: cur_img = s[0]; seg = s
        words = digits(fr[k]).split(); wtimes = [lead + x for x in wt[k]]
        layer = Image.new('RGBA', (W, H), (0, 0, 0, 0)); ld = ImageDraw.Draw(layer)
        spaced(ld, (140, 160), 'APPROFONDIMENTO', F('xbold', 26), (255, 205, 60), 6)
        ld.text((140, 200), topic, font=F('bold', 34), fill=(92, 214, 255))
        tf = fade_alpha(t, lead + times[k][0] - 0.05, 0.3)
        if cur_img:
            art = arts[cur_img]; p = (t - seg[1]) / max(1.0, seg[2] - seg[1]); aw, ah = art.size
            kb = ken(art, aw, ah, 1.0 + 0.07 * p, 0.6 * (p - .5), 0.3 * (p - .5))
            bx = 140 + (960 - aw) // 2; by = 270 + (640 - ah) // 2
            pre = fade_alpha(t, seg[1] + (0.0 if seg[1] == 0 else 0.0), 0.7) if seg[1] > 0 else 1
            sh = Image.new('RGBA', (W, H), (0, 0, 0, 0)); gfx.shadow(sh, (bx, by, bx + aw, by + ah), r=6, blur=26, off=(0, 16), alpha=140, col=(0, 0, 0))
            sh.paste(kb.convert('RGBA'), (bx, by)); overlay_alpha(layer, sh, pre)
            cap = spec.CAP[cur_img]; capf = F('bold', 30)
            ld.text((140 + (960 - ld.textlength(cap, font=capf)) / 2, 930), cap, font=capf, fill=(255, 255, 255, int(255 * pre)))
            hh = lines_h(words, 42, 640); y0 = 270 + (640 - hh) // 2
            tl = Image.new('RGBA', (W, H), (0, 0, 0, 0)); karaoke(tl, words, wtimes, t, 1180, 1820, y0, 42)
            overlay_alpha(layer, tl, tf)
        else:
            hh = lines_h(words, 56, 1300); y0 = 270 + (700 - hh) // 2
            tl = Image.new('RGBA', (W, H), (0, 0, 0, 0)); karaoke(tl, words, wtimes, t, 310, 1610, y0, 56, center=True)
            overlay_alpha(layer, tl, tf)
        im.alpha_composite(layer); e.put(im)
    return finish(sid, e.close(), track, dict(kind='appro', real=v['real'], images=[s[0] for s in segs if s[0]]))

# ------------------------------------------------------------ copertina
def cover_scene(sid, title, items, lead=0.6, tail=1.4):
    vname = 'INTRO'; fr = [s for s in re.split(r'(?<=[.!?])\s+', TXT[vname])]
    v = voice(vname); times = frags(vname, fr)
    off = len(fr) - len(items)
    N = int(math.ceil((lead + v['span'][1] + tail) * FPS)); e = Enc(OUT + 'seg/%s.mp4' % sid)
    track = np.zeros(N * 1600 + SR, np.float32); place(track, v['a'], lead, 1.0)
    for i in range(N):
        t = i / FPS; im = new_slide(); d = ImageDraw.Draw(im)
        spaced(d, (80, 170), "STORIA DELL'ARTE V · VIDEOLEZIONE", F('xbold', 28), BLUE, 5)
        a = fade_alpha(t, 0.1, 0.6); d.text((80, 230 + int(20 * (1 - a))), title, font=F('title', 150), fill=NAVY)
        d.rounded_rectangle((80, 430, 200, 438), 4, fill=BLUE)
        # card argomenti
        y0 = 500; hh = 52 * len(items) + 90
        gfx.shadow(im, (80, y0, 1840, y0 + hh), r=22, blur=20, off=(0, 8), alpha=34); d = ImageDraw.Draw(im)
        d.rounded_rectangle((80, y0, 1840, y0 + hh), 22, fill=(247, 249, 253), outline=(222, 228, 238), width=2)
        spaced(d, (120, y0 + 24), 'ARGOMENTI', F('xbold', 22), BLUE, 4)
        for j, it in enumerate(items):
            yy = y0 + 70 + j * 52; on = t >= lead + times[off + j][0] - 0.05
            cur = on and t < lead + times[off + j][1]
            if cur: d.rounded_rectangle((104, yy - 4, 1816, yy + 48), 14, fill=(255, 250, 205), outline=YEL, width=4)
            d.ellipse((130, yy + 14, 146, yy + 30), fill=(YEL if cur else (BLUE if on else (200, 208, 222))), outline=NAVY if cur else None, width=3 if cur else 0)
            d.text((170, yy), it, font=F('semi' if on else 'reg', 36), fill=NAVY if on else (150, 160, 180))
        footer(im, 1); e.put(im)
    return finish(sid, e.close(), track, dict(kind='cover', real=v['real']))

# ------------------------------------------------------------ compiti
def compiti_scene(sid, compiti, final_line, lead=0.8, tail=1.5):
    vname = 'COMPITI'; v = voice(vname); fr = compiti + [final_line]
    # i frammenti sono le frasi del testo voce: Primo. ... Secondo. ... Quarto. ... Svolgi...
    vt = TXT[vname]; parts = re.split(r'(?=\b(?:Secondo|Terzo|Quarto)\. )', vt); parts = [p.strip() for p in parts if p.strip()]
    tail_i = parts[-1].find('Svolgi i compiti'); parts[-1], last = parts[-1][:tail_i].strip(), parts[-1][tail_i:]
    parts.append(last)
    times = frags(vname, parts)
    N = int(math.ceil((lead + v['span'][1] + tail) * FPS)); e = Enc(OUT + 'seg/%s.mp4' % sid)
    track = np.zeros(N * 1600 + SR, np.float32); place(track, v['a'], lead, 1.0)
    f = F('med', 36); im0 = Image.new('RGBA', (10, 10)); d0 = ImageDraw.Draw(im0)
    lines = [wrap(d0, c, f, 1180) for c in compiti]
    for i in range(N):
        t = i / FPS; im = new_slide(); d = ImageDraw.Draw(im)
        spaced(d, (80, 148), 'COMPITI', F('xbold', 24), BLUE, 4); d.text((80, 190), 'Compiti', font=F('title', 64), fill=NAVY)
        d.rounded_rectangle((80, 276, 165, 282), 3, fill=BLUE)
        k = max([j for j in range(4) if t >= lead + times[j][0] - 0.05] or [0]); scr = 0 if k < 2 else 1
        idxs = [0, 1] if scr == 0 else [2, 3]; y = 310
        for j in idxs:
            hh = len(lines[j]) * 48 + 44
            if t >= lead + times[j][0] - 0.05:
                cur = (j == k and t < lead + times[4][0] - 0.05)
                gfx.shadow(im, (80, y, 1380, y + hh), r=22, blur=18, off=(0, 8), alpha=60 if cur else 34); d = ImageDraw.Draw(im)
                d.rounded_rectangle((80, y, 1380, y + hh), 22, fill=(255, 255, 255) if cur else (246, 248, 252), outline=YEL if cur else (222, 228, 238), width=7 if cur else 2)
                d.ellipse((104, y + 22, 126, y + 44), fill=YEL if cur else (200, 208, 222), outline=NAVY if cur else None, width=3 if cur else 0)
                yy = y + 22
                for ln in lines[j]: d.text((150, yy), ln, font=f, fill=NAVY if cur else (100, 110, 135)); yy += 48
            y += hh + 24
        if t >= lead + times[4][0] - 0.05:
            d.rounded_rectangle((80, 900, 1840, 960), 16, fill=(255, 250, 205), outline=YEL, width=4)
            d.text((110, 910), final_line, font=F('bold', 34), fill=NAVY)
        footer(im, 0); e.put(im)
    return finish(sid, e.close(), track, dict(kind='compiti', real=v['real']))
