# -*- coding: utf-8 -*-
# Schede animate con voce narrante (Kore o provvisoria): titolo, approfondimento, pillola, quiz, mappe, glossario, ripasso, verifica, compiti.
import os, json, subprocess, math, re
from PIL import Image
import rend, voce, contenuti as C, piano as P, slide
from montaggio import sh, X264, FPS, OUT, KIT
W = rend.WORK
ASSET = f'{W}/asset'; os.makedirs(ASSET, exist_ok=True)
E = lambda s: rend.esc(s)

def nfr(d): return max(1, round(d * FPS))

def audio_filtro(tracce, dur):
    """tracce = [(wav, t_inizio, volume)] -> filtro amix, durata esatta"""
    ins = []; parts = []
    for i, (w, t0, vol) in enumerate(tracce):
        parts.append(f"[{{n{i}}}:a]aresample=48000,pan=stereo|c0=c0|c1=c{'1' if True else '0'},volume={vol},adelay={int(t0*1000)}|{int(t0*1000)}[t{i}]")
    return parts

def compone(nome, dur, base, elementi, tracce, anim_luce=True, extra_in=None):
    """elementi: dict(png,x,y,t0,d=0.4,t1=None,slide=0,enable=None). tracce: [(wav,t_inizio,volume)]"""
    d = f'{OUT}/{nome}'; os.makedirs(d, exist_ok=True)
    n = nfr(dur); dur = n / FPS
    cmd = ['ffmpeg', '-v', 'error', '-y', '-loop', '1', '-framerate', '30', '-t', f'{dur:.3f}', '-i', base]
    idx = 1; fc = []; cur = '[0:v]'
    if anim_luce:
        lz = f'{ASSET}/luce.png'
        if not os.path.exists(lz): rend.luce(lz)
        cmd += ['-loop', '1', '-framerate', '30', '-t', f'{dur:.3f}', '-i', lz]
        fc.append(f"{cur}[{idx}:v]overlay=x='-250+220*sin(t/3.1)':y='-300+120*cos(t/4.3)':shortest=0[b{idx}]"); cur = f'[b{idx}]'; idx += 1
    for k, e in enumerate(elementi):
        cmd += ['-loop', '1', '-framerate', '30', '-t', f'{dur:.3f}', '-i', e['png']]
        t0 = e.get('t0', 0); dd = e.get('d', 0.4); lab = f'e{idx}'
        f = f"[{idx}:v]format=rgba"
        if e.get('fade', True): f += f",fade=t=in:st={t0:.3f}:d={dd:.3f}:alpha=1"
        if e.get('t1') is not None: f += f",fade=t=out:st={e['t1']:.3f}:d=0.25:alpha=1"
        f += f"[{lab}]"; fc.append(f)
        y = e['y']; sl = e.get('slide', 0)
        ye = f"{y}+max(0,{t0+dd:.3f}-t)*{sl/dd:.1f}" if sl else f"{y}"
        en = e.get('enable')
        ens = f":enable='{en}'" if en else ''
        fc.append(f"{cur}[{lab}]overlay=x={e['x']}:y='{ye}'{ens}:shortest=0[b{idx}]"); cur = f'[b{idx}]'; idx += 1
    fc.append(f"{cur}format=yuv420p[vout]")
    ai = []
    for i, tr in enumerate(tracce):
        w, t0, vol = tr[:3]; vd = tr[3] if len(tr) > 3 else None
        cmd += ['-i', w]
        fd = f",afade=t=in:d=0.03,afade=t=out:st={max(0, vd - 0.04):.3f}:d=0.035" if vd else ''
        fc.append(f"[{idx}:a]aresample=48000,aformat=channel_layouts=stereo,volume={vol}{fd},adelay={int(t0*1000)}|{int(t0*1000)}[t{i}]"); ai.append(f'[t{i}]'); idx += 1
    fc.append(''.join(ai) + f"amix=inputs={len(ai)}:normalize=0:duration=longest,apad,atrim=0:{dur:.3f}[aout]")
    mp4 = f'{d}/v.mp4'; wav = f'{d}/a.wav'
    cmd += ['-filter_complex', ';'.join(fc), '-map', '[vout]', '-frames:v', str(n)] + X264 + [mp4,
            '-map', '[aout]', '-t', f'{dur:.3f}', '-ar', '48000', '-ac', '2', '-c:a', 'pcm_s16le', wav]
    sh(cmd)
    sh(['ffmpeg', '-v', 'error', '-y', '-sseof', '-0.06', '-i', mp4, '-frames:v', '1', f'{d}/ultimo.png'])
    return dict(nome=nome, mp4=mp4, wav=wav, durata=dur, frames=n, ultimo=f'{d}/ultimo.png')

def snd(n): return f'{KIT}/suoni/{n}.wav'
def base_scura():
    f = f'{ASSET}/base_scura.png'
    if not os.path.exists(f): rend.base_dark(f)
    return f
def el(nome, inner, estile='', css=''):
    out = f'{ASSET}/{nome}.png'; w, h = rend.elem(inner, out, estile, extra_css=css); return out, w, h

# ---------- titolo dell'argomento ----------
def titolo(k):
    t = P.TOP[k]['titolo']
    a, wa, ha = el(f'T{k}_lab', f'<div class="d-lab">Argomento {k}</div>')
    b, wb, hb = el(f'T{k}_tit', f'<div class="d-tit" style="width:1500px">{E(t)}</div>')
    c, wc, hc = el(f'T{k}_rig', f'<div style="width:260px;height:10px;background:{rend.GIALLO};border-radius:5px"></div>')
    els = [dict(png=a, x=160, y=330, t0=0.15, d=0.4, slide=25), dict(png=b, x=160, y=400, t0=0.35, d=0.5, slide=40), dict(png=c, x=160, y=400 + hb + 24, t0=0.9, d=0.5)]
    return compone(f'tit{k}', 3.0, base_scura(), els, [(snd('titolo'), 0.0, 1.0)])

# ---------- approfondimento ----------
APPROF_TRIGGER = {  # frase della voce da cui compare ogni punto (indice di frase)
}
def approfondimento(k, immagine=None):
    v = voce.get(f'A{k}_APPROF'); titolo_s, punti = C.APPROF_SCHERMO[k]; nf = len(v['frasi'])
    lab, _, _ = el(f'AP{k}_lab', '<div class="d-lab">Approfondimento</div>')
    tit, _, ht = el(f'AP{k}_tit', f'<div class="d-tit" style="font-size:72px;width:{1000 if immagine else 1500}px">{E(titolo_s)}</div>')
    els = [dict(png=lab, x=100, y=170, t0=0.1, d=0.4), dict(png=tit, x=100, y=225, t0=0.3, d=0.5, slide=30)]
    y = 225 + ht + 50; w_p = 1000 if immagine else 1600
    # punti: legati alle frasi della voce, distribuiti
    n = len(punti)
    for i, p in enumerate(punti):
        fi = 1 + round(i * (nf - 2) / max(1, n - 1)) if nf > 2 else 0
        t0 = max(0.8, v['tempi'][min(fi, nf - 1)][0] + 0.8 - 0.1)
        png, w, h = el(f'AP{k}_p{i}', f'<div style="display:flex;gap:22px;align-items:flex-start;width:{w_p}px"><div style="flex:none;width:18px;height:18px;margin-top:20px;border-radius:50%;background:{rend.GIALLO}"></div><div class="d-line" style="font-size:42px">{E(p)}</div></div>')
        els.append(dict(png=png, x=100, y=y, t0=t0, d=0.5, slide=26)); y += h + 22
    if immagine:
        hi = slide.immagine_alta(immagine); im = Image.open(hi); r = min(740 / im.width, 640 / im.height); w, h = int(im.width * r), int(im.height * r)
        png, ww, hh = el(f'AP{k}_img', f'<div style="background:#fff;border-radius:22px;padding:14px;box-shadow:0 14px 40px rgba(0,0,0,.45)"><img src="file://{hi}" style="width:{w}px;height:{h}px;display:block;border-radius:10px"></div>')
        els.append(dict(png=png, x=1100, y=300, t0=1.5, d=0.8, slide=30))
    dur = 0.8 + v['durata'] + 0.9
    return compone(f'app{k}', dur, base_scura(), els, [(v['wav'], 0.8, 1.0, v['durata'])])

# ---------- pillola di ripasso ----------
PILLOLA = {
 1: ["Regno Unito: disoccupazione e taglio dei sussidi", "1931 · Statuto di Westminster: nasce il Commonwealth", "Francia: la crisi arriva più tardi", "1936 · il Fronte Popolare vince le elezioni", "Settimana di 40 ore e ferie retribuite"],
 2: ["1926 · Polonia: Piłsudski", "Ungheria: Horthy", "Balcani: regimi autoritari", "1933 · Portogallo: Estado Novo di Salazar", "America Latina: colpi di Stato militari", "Giappone: regime militarista"],
 3: ["1931 · il Giappone occupa la Manciuria", "Nasce lo Stato fantoccio del Manchukuo", "1937 · invasione della Cina", "Cina: nazionalisti contro comunisti", "Lunga marcia: 10.000 chilometri"],
 4: ["1931 · in Spagna nasce la Repubblica", "Luglio 1936 · Franco guida il colpo di Stato", "Italia e Germania sostengono Franco", "L'URSS e le Brigate internazionali aiutano la Repubblica", "1939 · cade la Repubblica"],
 5: ["1933 · Hitler sale al potere", "Abbandona la Società delle Nazioni", "1935 · coscrizione obbligatoria", "1936 · militarizza la Renania", "Francia e Gran Bretagna: Appeasement"],
 6: ["1938 · Anschluss: annessione dell'Austria", "1938 · Monaco: si cede sui Sudeti", "Marzo 1939 · Hitler occupa Praga", "Maggio 1939 · Patto d'acciaio", "23 agosto 1939 · Patto Molotov-Ribbentrop"],
}
def pillola(k):
    v = voce.get(f'P{k}_PILLOLA'); righe = PILLOLA[k]; nf = len(v['frasi'])
    assert nf - 1 == len(righe), (k, nf, len(righe))
    lab, _, _ = el(f'PI{k}_lab', '<div class="d-lab">Ripasso</div>')
    tit, _, ht = el(f'PI{k}_tit', f'<div class="d-tit" style="font-size:64px;width:1600px">{E(P.TOP[k]["titolo"])}</div>')
    els = [dict(png=lab, x=100, y=160, t0=0.2, d=0.4), dict(png=tit, x=100, y=215, t0=0.4, d=0.5, slide=30)]
    y = 215 + ht + 40; T0 = 1.3   # la voce parte dopo l'attacco del jingle
    for i, r in enumerate(righe):
        norm, w, h = el(f'PI{k}_r{i}', f'<div style="width:1500px;background:rgba(255,255,255,.08);border-left:12px solid #fff;border-radius:14px;padding:12px 28px"><div class="d-line" style="font-size:44px"><b style="color:{rend.GIALLO}">{i+1}</b> &nbsp;{E(r)}</div></div>')
        acc, _, _ = el(f'PI{k}_a{i}', f'<div style="width:1500px;background:{rend.GIALLO};border-left:12px solid #fff;border-radius:14px;padding:12px 28px"><div class="d-line" style="font-size:44px;color:#0B1530"><b>{i+1}</b> &nbsp;{E(r)}</div></div>')
        a0, a1 = v['tempi'][i + 1]; t0 = T0 + a0 - 0.15; t1 = T0 + a1 + 0.2
        els.append(dict(png=norm, x=100, y=y, t0=t0, d=0.4, slide=20))
        els.append(dict(png=acc, x=100, y=y, t0=t0, d=0.2, fade=False, enable=f"between(t,{t0:.3f},{t1:.3f})"))
        y += h + 16
    dur = T0 + v['durata'] + 0.8
    return compone(f'pil{k}', dur, base_scura(), els, [(snd('repaso'), 0.0, 1.0), (v['wav'], T0, 1.0, v['durata'])])

# ---------- quiz ----------
def quiz(k):
    lab, _, _ = el(f'Q{k}_lab', '<div class="d-lab">Quiz</div>')
    tit, _, ht = el(f'Q{k}_tit', f'<div class="d-tit" style="font-size:80px;width:1600px">Mettiti alla prova</div>')
    sub, _, _ = el(f'Q{k}_sub', f'<div class="d-line" style="width:1500px;font-size:42px">{E(P.TOP[k]["titolo"])}<br><span style="color:{rend.GIALLO}">5 domande · per continuare serve almeno l\'80%</span><br><span style="font-size:36px;color:#cfd8ee">Rispondi · premi Controlla · poi Continua</span></div>')
    els = [dict(png=lab, x=160, y=340, t0=0.5, d=0.3), dict(png=tit, x=160, y=395, t0=0.5, d=0.4, slide=30), dict(png=sub, x=160, y=395 + ht + 30, t0=1.0, d=0.5)]
    return compone(f'quiz{k}', 4.2, base_scura(), els, [(snd('quiz'), 0.5, 1.0)])

# ---------- mappe del prof, ridisegnate (modello BES) e costruite ramo per ramo ----------
COL = {  # riempimento, bordo
 'pesca': ('#FFD9C2', '#E8743B'), 'celeste': ('#D6EAFB', '#2F86D6'), 'paglierino': ('#FFF3C4', '#D4A500'),
 'menta': ('#D4F3E2', '#2FA866'), 'lilla': ('#E7DCF8', '#7E57C2')}
LEG = {'pesca': 'concetto centrale', 'celeste': 'date e sequenze', 'paglierino': 'parole chiave', 'menta': 'esempi e opere', 'lilla': 'conseguenze'}
MAPPE = {
 2: dict(titolo="In quali paesi si diffonde l'autoritarismo?", nota="Comintern = Internazionale comunista",
   nodi=[('c', ["L'AUTORITARISMO"], 'pesca', 700, 250, 520, 100),
         ('eu', ["in Europa"], 'paglierino', 100, 470, 480, 90),
         ('am', ["in America Latina"], 'paglierino', 720, 470, 480, 90),
         ('gi', ["in Giappone"], 'paglierino', 1340, 470, 480, 90),
         ('eu2', ["Polonia", "Ungheria", "Iugoslavia", "Grecia", "Romania", "Portogallo"], 'menta', 100, 690, 480, 300),
         ('am2', ["Argentina", "Brasile"], 'menta', 720, 690, 480, 150),
         ('gi2', ["il patto anti-Comintern"], 'lilla', 1340, 690, 480, 100)],
   archi=[('c', 'eu', 'si diffonde'), ('c', 'am', ''), ('c', 'gi', ''), ('eu', 'eu2', 'in'), ('am', 'am2', 'in'), ('gi', 'gi2', 'che firma')],
   passi=[(None, 0), ('c', 1), ('eu', 2), ('eu2', 3), ('am', 4), ('am2', 5), ('gi', 6), ('gi2', 7)]),
 4: dict(titolo="Come si svolge la guerra civile di Spagna?", nota="",
   nodi=[('c', ["LA GUERRA CIVILE SPAGNOLA"], 'pesca', 560, 250, 800, 100),
         ('rep', ["i repubblicani"], 'paglierino', 200, 470, 520, 100),
         ('naz', ["i nazionalisti"], 'paglierino', 1200, 470, 520, 100),
         ('bri', ["Brigate internazionali"], 'menta', 200, 700, 520, 100),
         ('ger', ["Germania e Italia"], 'menta', 1200, 700, 520, 100),
         ('fra', ["la dittatura di Franco"], 'lilla', 1200, 900, 520, 100)],
   archi=[('c', 'rep', 'vede contrapposti'), ('c', 'naz', ''), ('rep', 'bri', 'sostenuti da'), ('naz', 'ger', 'sostenuti da'), ('ger', 'fra', 'che instaurano')],
   passi=[(None, 0), ('c', 1), ('rep', 2), ('bri', 3), ('naz', 4), ('ger', 5), ('fra', 6)]),
 6: dict(titolo="Che cosa fa Hitler prima della guerra?", nota="",
   nodi=[('c', ["HITLER"], 'pesca', 760, 250, 400, 100),
         ('au', ["l'Austria (1938)"], 'celeste', 80, 440, 520, 100),
         ('su', ["i Sudeti (1939)"], 'celeste', 700, 440, 520, 100),
         ('da', ["Danzica"], 'paglierino', 1320, 440, 500, 100),
         ('fr', ["Francia e Regno Unito"], 'paglierino', 80, 630, 520, 100),
         ('ap', ["l'appeasement", "(pacificazione)"], 'lilla', 80, 820, 520, 140),
         ('ce', ["l'intera Cecoslovacchia"], 'lilla', 700, 630, 520, 100),
         ('pa', ["il patto di non aggressione", "con l'Unione Sovietica"], 'lilla', 1320, 630, 500, 150)],
   archi=[('c', 'au', 'annette'), ('c', 'su', 'invade'), ('c', 'da', 'rivendica'), ('au', 'fr', 'mentre'), ('fr', 'ap', 'rispondono con'), ('su', 'ce', 'e poi'), ('da', 'pa', 'e firma')],
   passi=[(None, 0), ('c', 1), ('au', 2), ('fr', 3), ('ap', 4), ('su', 5), ('ce', 6), ('da', 7), ('pa', 8)]),
}

def nodo_html(testo_righe, col, lit=False, w=300, h=100, bold=False, centro=False):
    fill, bord = COL[col]
    if lit: fill = rend.GIALLO
    righe = ''.join(f'<div>{E(r)}</div>' for r in testo_righe)
    if len(testo_righe) > 1 and not centro and col == 'menta':
        righe = ''.join(f'<div style="text-align:left">• {E(r)}</div>' for r in testo_righe)
        al = 'flex-start'
    else: al = 'center'
    fw = 800 if centro else 600
    return (f'<div style="width:{w}px;height:{h}px;background:{fill};border:5px solid {bord};border-radius:22px;box-shadow:0 8px 22px rgba(60,70,100,.18);'
            f'display:flex;flex-direction:column;justify-content:center;align-items:{al};padding:0 28px;font:{fw} {38 if not centro else 40}px/1.3 Figtree;color:{rend.NOTTE};letter-spacing:{2 if centro else 0}px">{righe}</div>')

def base_mappa(k, usati):
    m = MAPPE[k]
    f = f'{ASSET}/mappa{k}_base.png'
    leg = ''.join(f'<div style="display:flex;align-items:center;gap:12px;margin-bottom:8px"><div style="width:30px;height:30px;border-radius:8px;background:{COL[c][0]};border:4px solid {COL[c][1]}"></div><div style="font:600 26px Figtree;color:{rend.NOTTE}">{LEG[c]}</div></div>' for c in usati)
    body = (f'<img class="logo" src="file://{rend.LOGO}"><div class="hr" style="top:125px"></div>'
            f'<div style="position:absolute;left:80px;top:150px;display:flex;align-items:center;gap:18px"><div style="width:34px;height:34px;background:#F5A623;border-radius:6px"></div><div style="font:800 50px Bricolage Grotesque;color:{rend.BLU}">{E(m["titolo"])}</div></div>'
            f'<div style="position:absolute;right:80px;top:40px;background:#fff;border:2px solid #dfe3ea;border-radius:14px;padding:14px 20px">{leg}</div>')
    if m['nota']: body += f'<div style="position:absolute;right:80px;top:820px;font:600 28px Figtree;color:{rend.NOTTE}">{E(m["nota"])}</div>'
    rend.png(rend.doc(body), f, name=f'mb{k}.html'); return f

def mappa(k):
    m = MAPPE[k]; v = voce.get(f'M{k}_MAPPA'); nodi = {n[0]: n for n in m['nodi']}
    usati = [c for c in COL if any(n[2] == c for n in m['nodi'])]
    base = base_mappa(k, usati)
    # archi: PNG trasparente a tutto schermo con linee e scritta
    def arco_png(a, b, lab):
        na, nb = nodi[a], nodi[b]
        x1 = na[3] + na[5] // 2; y1 = na[4] + na[6]; x2 = nb[3] + nb[5] // 2; y2 = nb[4]
        ym = (y1 + y2) // 2
        path = f'M{x1},{y1} L{x1},{ym} L{x2},{ym} L{x2},{y2 - 4}'
        txt = f'<text x="{x2 + 16}" y="{(ym + y2) // 2 + 12}" text-anchor="start" font-family="Figtree" font-weight="500" font-size="34" fill="#0B1530" stroke="#fff" stroke-width="8" paint-order="stroke">{E(lab)}</text>' if lab else ''
        svg = (f'<svg width="1920" height="1080" xmlns="http://www.w3.org/2000/svg"><defs><marker id="h" markerWidth="12" markerHeight="12" refX="6" refY="6" orient="auto"><path d="M1,1 L11,6 L1,11 Z" fill="#0B1530"/></marker></defs>'
               f'<path d="{path}" fill="none" stroke="#0B1530" stroke-width="3.5" marker-end="url(#h)"/>{txt}</svg>')
        out = f'{ASSET}/mappa{k}_arco_{a}_{b}.png'
        rend.png(f'<!doctype html><html><body style="margin:0;background:transparent">{svg}</body></html>', out, transparent=True, name=f'arc{k}_{a}_{b}.html'); return out
    els = []; T0 = 0.8
    tempi = v['tempi']; nseg = len(tempi); fine_voce = tempi[-1][1]
    passo_nodo = {}
    for nid, idx in m['passi']:
        if nid is not None: passo_nodo[nid] = idx
    # frase -> nodo
    ordine = [(idx, nid) for nid, idx in m['passi'] if nid is not None]
    for j, (idx, nid) in enumerate(ordine):
        n = nodi[nid]
        a0 = T0 + tempi[idx][0] - 0.1
        a1 = T0 + (tempi[ordine[j + 1][0]][0] if j + 1 < len(ordine) else tempi[idx][1]) - 0.1
        # arco entrante
        for (a, b, lab) in m['archi']:
            if b == nid:
                els.append(dict(png=arco_png(a, b, lab), x=0, y=0, t0=a0, d=0.35))
        h = n[6]; w = n[5]
        norm = f'{ASSET}/mappa{k}_{nid}.png'; acc = f'{ASSET}/mappa{k}_{nid}_acc.png'
        rend.elem(nodo_html(n[1], n[2], False, w, h, centro=(nid == 'c')), norm, extra_css='')
        rend.elem(nodo_html(n[1], n[2], True, w, h, centro=(nid == 'c')), acc)
        els.append(dict(png=norm, x=n[3], y=n[4], t0=a0, d=0.35))
        els.append(dict(png=acc, x=n[3], y=n[4], t0=a0, d=0.2, fade=False, enable=f"between(t,{a0:.3f},{a1:.3f})"))
    dur = T0 + fine_voce + 0.4 + 4.0   # la mappa intera resta ferma 4 s
    r = compone(f'mappa{k}', dur, base, els, [(v['wav'], T0, 1.0, v['durata']), (snd('repaso'), T0 + fine_voce + 0.3, 0.45)], anim_luce=False)
    return r

# ---------- glossario ----------
def glossario():
    v = voce.get('G1_GLOSSARIO'); G = C.GLOSSARIO; T0 = 1.3
    assert len(v['frasi']) == len(G) + 1, len(v['frasi'])
    lab, _, _ = el('GL_lab', '<div class="d-lab">Parole chiave</div>')
    tit, _, ht = el('GL_tit', '<div class="d-tit" style="font-size:72px">Glossario</div>')
    els = [dict(png=lab, x=100, y=150, t0=0.2, d=0.4), dict(png=tit, x=100, y=200, t0=0.3, d=0.5, slide=30)]
    for i, (term, df) in enumerate(G):
        col = i // 5; row = i % 5; x = 100 + col * 900; y = 330 + row * 130
        def blocco(bg, fg, tc):
            return (f'<div style="width:860px;height:116px;background:{bg};border-radius:16px;padding:10px 24px;border-left:12px solid #fff">'
                    f'<div style="font:800 38px Figtree;color:{tc}">{E(term)}</div><div style="font:500 30px/1.25 Figtree;color:{fg}">{E(df)}</div></div>')
        n_, _, _ = el(f'GL_n{i}', blocco('rgba(255,255,255,.10)', '#fff', rend.GIALLO))
        a_, _, _ = el(f'GL_a{i}', blocco(rend.GIALLO, '#0B1530', '#0B1530'))
        a0, a1 = v['tempi'][i + 1]; t0 = T0 + a0 - 0.15; t1 = T0 + a1 + 0.2
        els.append(dict(png=n_, x=x, y=y, t0=t0, d=0.4, slide=20)); els.append(dict(png=a_, x=x, y=y, t0=t0, d=0.2, fade=False, enable=f"between(t,{t0:.3f},{t1:.3f})"))
    return compone('glossario', T0 + v['durata'] + 1.5, base_scura(), els, [(snd('repaso'), 0.0, 1.0), (v['wav'], T0, 1.0, v['durata'])])

# ---------- ripasso finale ----------
RIEP = ["Francia e Gran Bretagna: crisi, Commonwealth, Fronte Popolare", "Dittature e autoritarismi: Europa, America Latina, Giappone",
        "Espansionismo asiatico: Manciuria, invasione della Cina, Lunga marcia", "Guerra civile spagnola: da Franco alla caduta della Repubblica (1939)",
        "Aggressività nazista: Hitler smantella Versailles", "Verso la guerra: Appeasement, Anschluss, Monaco, Praga, Patti"]
def ripasso_finale():
    v = voce.get('R1_RIPASSO_FINALE'); T0 = 1.3
    assert len(v['frasi']) == len(RIEP) + 1, len(v['frasi'])
    lab, _, _ = el('RF_lab', '<div class="d-lab">Ripasso finale</div>')
    tit, _, ht = el('RF_tit', '<div class="d-tit" style="font-size:72px">Argomento per argomento</div>')
    els = [dict(png=lab, x=100, y=150, t0=0.2, d=0.4), dict(png=tit, x=100, y=200, t0=0.3, d=0.5, slide=30)]
    y = 340
    for i, r in enumerate(RIEP):
        def b(bg, fg, nc): return f'<div style="width:1700px;background:{bg};border-left:12px solid #fff;border-radius:14px;padding:12px 28px"><div class="d-line" style="font-size:42px;color:{fg}"><b style="color:{nc}">{i+1}</b> &nbsp;{E(r)}</div></div>'
        n_, _, h = el(f'RF_n{i}', b('rgba(255,255,255,.08)', '#fff', rend.GIALLO)); a_, _, _ = el(f'RF_a{i}', b(rend.GIALLO, '#0B1530', '#0B1530'))
        a0, a1 = v['tempi'][i + 1]; t0 = T0 + a0 - 0.15; t1 = T0 + a1 + 0.2
        els.append(dict(png=n_, x=100, y=y, t0=t0, d=0.4, slide=20)); els.append(dict(png=a_, x=100, y=y, t0=t0, d=0.2, fade=False, enable=f"between(t,{t0:.3f},{t1:.3f})"))
        y += h + 18
    return compone('ripasso', T0 + v['durata'] + 1.5, base_scura(), els, [(snd('repaso'), 0.0, 1.0), (v['wav'], T0, 1.0, v['durata'])])

# ---------- mappa finale della lezione (le 3 mappe del prof, in sequenza) ----------
def mappe_finale():
    v = voce.get('F1_MAPPE_FINALE'); T0 = 0.8; assert len(v['frasi']) == 4
    lab, _, _ = el('MF_lab', '<div class="d-lab">Mappe</div>')
    tit, _, ht = el('MF_tit', '<div class="d-tit" style="font-size:84px">Le mappe della lezione</div>')
    els = [dict(png=lab, x=160, y=380, t0=0.3, d=0.4), dict(png=tit, x=160, y=440, t0=0.4, d=0.5, slide=30)]
    for i, k in enumerate((2, 4, 6)):
        t0 = T0 + v['tempi'][i + 1][0] - 0.2
        els.append(dict(png=f'{OUT}/mappa{k}/ultimo.png', x=0, y=0, t0=t0, d=0.6))
    dur = T0 + v['tempi'][3][1] + 0.4 + 4.0
    return compone('mappe_fin', dur, base_scura(), els, [(v['wav'], T0, 1.0, v['durata']), (snd('repaso'), T0 + v['tempi'][3][1] + 0.3, 0.45)])

# ---------- verifica ----------
def verifica():
    v = voce.get('V1_VERIFICA')
    lab, _, _ = el('VF_lab', '<div class="d-lab">Verifica di sbarramento</div>')
    tit, _, ht = el('VF_tit', '<div class="d-tit" style="font-size:84px">Verifica finale</div>')
    sub, _, _ = el('VF_sub', f'<div class="d-line" style="width:1500px;font-size:44px">10 domande<br><span style="color:{rend.GIALLO}">per superarla serve almeno l\'80%</span><br><span style="font-size:36px;color:#cfd8ee">Rispondi · premi Controlla · poi Continua</span></div>')
    els = [dict(png=lab, x=160, y=340, t0=0.5, d=0.3), dict(png=tit, x=160, y=395, t0=0.5, d=0.4, slide=30), dict(png=sub, x=160, y=395 + ht + 30, t0=1.0, d=0.5)]
    return compone('verifica', 0.9 + v['durata'] + 1.6, base_scura(), els, [(snd('quiz'), 0.5, 1.0), (v['wav'], 1.2, 1.0, v['durata'])])

# ---------- compiti ----------
def compiti_intro():
    lab, _, _ = el('CI_lab', '<div class="d-lab">Compiti</div>')
    tit, _, ht = el('CI_tit', '<div class="d-tit" style="font-size:110px">Compiti</div>')
    els = [dict(png=tit, x=160, y=440, t0=0.3, d=0.5, slide=40)]
    return compone('compiti_intro', 3.5, base_scura(), els, [(snd('titolo'), 0.0, 1.0)])

def compiti():
    v = voce.get('C2_COMPITI'); assert len(v['frasi']) == 8, len(v['frasi']); T0 = 0.8
    els = []
    lab, _, _ = el('CO_lab', '<div class="d-lab">Compiti</div>')
    els.append(dict(png=lab, x=100, y=140, t0=0.1, d=0.4))
    for i, txt in enumerate(C.COMPITI):
        card, _, h = el(f'CO_c{i}', f'<div style="width:1700px;background:rgba(255,255,255,.10);border-left:14px solid {rend.GIALLO};border-radius:18px;padding:22px 36px"><div style="font:800 40px Figtree;color:{rend.GIALLO};margin-bottom:6px">Compito {i+1}</div><div style="font:500 40px/1.45 Figtree;color:#fff">{E(txt)}</div></div>')
        t0 = T0 + v['tempi'][2 * i][0] - 0.2; t1 = T0 + v['tempi'][2 * i + 1][1] + 0.4
        els.append(dict(png=card, x=100, y=210, t0=t0, d=0.5, slide=30, t1=t1 if i < 3 else None))
    return compone('compiti', T0 + v['durata'] + 1.0, base_scura(), els, [(v['wav'], T0, 1.0, v['durata'])])

# ---------- copertina + argomenti ----------
def cover_html(con_prof, lit=None):
    t = C.TITOLO_MAIUSC
    h = f'<img class="logo" src="file://{rend.LOGO}"><div class="hr" style="top:125px"></div>'
    h += f'<div class="lab">STORIA · VIDEOLEZIONE</div>'
    h += f'<div style="position:absolute;left:80px;top:200px;width:1280px;font:800 110px/1.05 \'Bricolage Grotesque\';color:{rend.NOTTE}">{E(t)}</div><div style="position:absolute;left:80px;top:{200+240}px;width:90px;height:8px;background:{rend.BLU}"></div>'
    arg = ''.join(f'<div style="font:600 34px/1.3 Figtree;color:{rend.NOTTE};margin:8px 0"><b style="color:{rend.BLU}">{n}</b>&nbsp; {E(tt)}</div>' for n, tt in C.ARGOMENTI)
    h += f'<div style="position:absolute;left:80px;top:520px;width:1305px;background:#F4F7FC;border-radius:20px;padding:20px 34px;box-shadow:0 10px 30px rgba(40,50,80,.10)"><div style="font:700 22px Figtree;letter-spacing:3px;color:{rend.BLU};margin-bottom:8px">ARGOMENTI</div>{arg}</div>'
    h += f'<div class="hr" style="top:981px"></div><div class="foot"><span>STORIA</span><span>Pagina 1</span></div>'
    if con_prof:
        h += f'<div class="ombra"></div><div class="band"><div class="a">{E(C.DOCENTE_FASCIA[0])}</div><div class="b">{E(C.DOCENTE_FASCIA[1])}</div></div>'
    return rend.doc(h)

def cover_png(con_prof):
    f = f'{ASSET}/cover_{"prof" if con_prof else "sola"}.png'
    rend.png(cover_html(con_prof), f, name=f'cover{con_prof}.html'); return f

def cover_benvenuto():
    v = voce.get('I1_BENVENUTO')
    return compone('cover_ben', 0.6 + v['durata'] + 0.8, cover_png(False), [], [(v['wav'], 0.6, 1.0, v['durata'])], anim_luce=False)

def cover_benvenuto2():
    v = voce.get('I3_BENVENUTO2')
    return compone('cover_ben2', max(11.0, 0.6 + v['durata'] + 2.4), cover_png(False), [], [(v['wav'], 0.6, 1.0, v['durata']), (snd('titolo'), 0.6 + v['durata'] + 0.2, 0.8)], anim_luce=False)

def argomenti_scheda():
    v = voce.get('I2_ARGOMENTI'); assert len(v['frasi']) == 8; T0 = 0.6
    base = f'{ASSET}/arg_base.png'
    h = f'<img class="logo" src="file://{rend.LOGO}"><div class="hr" style="top:125px"></div><div class="lab">STORIA</div><div class="tit" style="width:1700px">Di cosa parliamo</div><div class="hr" style="top:981px"></div><div class="foot"><span>STORIA</span><span>Pagina 2</span></div>'
    rend.png(rend.doc(h), base, name='argbase.html')
    els = []; y = 300
    for i, (n, tt) in enumerate(C.ARGOMENTI):
        def b(bg, bord, tc): return f'<div style="width:1700px;background:{bg};border:4px solid {bord};border-radius:18px;padding:12px 30px;font:700 42px Figtree;color:{tc}"><span style="color:{rend.BLU if bg=="#fff" else "#0B1530"}">{n}</span> &nbsp;{E(tt)}</div>'
        n_, _, hh = el(f'AR_n{i}', b('#fff', '#dfe3ea', rend.NOTTE)); a_, _, _ = el(f'AR_a{i}', b('#FFFBD6', rend.GIALLO, rend.NOTTE))
        a0, a1 = v['tempi'][i + 2]; t0 = T0 + a0 - 0.15; t1 = T0 + a1 + 0.2
        els.append(dict(png=n_, x=80, y=y, t0=t0 - 0.3 if False else 0.3 + i * 0.12, d=0.4, slide=20))
        els.append(dict(png=a_, x=80, y=y, t0=t0, d=0.2, fade=False, enable=f"between(t,{t0:.3f},{t1:.3f})"))
        y += hh + 22
    return compone('argomenti', T0 + v['durata'] + 1.0, base, els, [(v['wav'], T0, 1.0, v['durata'])], anim_luce=False)

# ---------- sigle ----------
def pezzo_da_file(nome, mp4):
    d = f'{OUT}/{nome}'; os.makedirs(d, exist_ok=True)
    dur = float(sh(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', mp4]).stdout); n = round(dur * FPS)
    sh(['ffmpeg', '-v', 'error', '-y', '-i', mp4, '-vf', 'scale=1920:1080,fps=30,format=yuv420p', '-frames:v', str(n)] + X264 + [f'{d}/v.mp4'])
    sh(['ffmpeg', '-v', 'error', '-y', '-i', mp4, '-t', f'{n/FPS:.4f}', '-af', 'apad', '-ar', '48000', '-ac', '2', '-c:a', 'pcm_s16le', f'{d}/a.wav'])
    sh(['ffmpeg', '-v', 'error', '-y', '-sseof', '-0.06', '-i', f'{d}/v.mp4', '-frames:v', '1', f'{d}/ultimo.png'])
    return dict(nome=nome, mp4=f'{d}/v.mp4', wav=f'{d}/a.wav', durata=n / FPS, frames=n, ultimo=f'{d}/ultimo.png')

# ---------- spiegone (apertura della Parte 2): ripasso della Parte 1 con immagini e mappe ----------
def spiegone():
    v = voce.get('S1_SPIEGONE'); T = v['tempi']; assert len(T) == 8, len(T); T0 = 0.8
    els = []
    def scheda(nome, lab_t, tit_t, punti, img=None):
        lab, _, _ = el(f'{nome}_l', f'<div class="d-lab">{E(lab_t)}</div>')
        tit, _, ht = el(f'{nome}_t', f'<div class="d-tit" style="font-size:66px;width:{1000 if img else 1650}px">{E(tit_t)}</div>')
        L = [(lab, 100, 150), (tit, 100, 205)]; y = 205 + ht + 40
        for i, p in enumerate(punti):
            png, w, h = el(f'{nome}_p{i}', f'<div style="display:flex;gap:22px;width:{1000 if img else 1650}px"><div style="flex:none;width:18px;height:18px;margin-top:20px;border-radius:50%;background:{rend.GIALLO}"></div><div class="d-line" style="font-size:42px">{E(p)}</div></div>')
            L.append((png, 100, y)); y += h + 20
        if img:
            hi = slide.immagine_alta(img); im = Image.open(hi); r = min(740 / im.width, 640 / im.height); w, h = int(im.width * r), int(im.height * r)
            png, _, _ = el(f'{nome}_i', f'<div style="background:#fff;border-radius:22px;padding:14px;box-shadow:0 14px 40px rgba(0,0,0,.45)"><img src="file://{hi}" style="width:{w}px;height:{h}px;display:block;border-radius:10px"></div>')
            L.append((png, 1100, 300))
        return L
    G = {
     0: [(el('SP_t', '<div class="d-tit" style="font-size:90px;width:1500px">Ripasso della Parte precedente</div>')[0], 160, 420)],
     1: scheda('SP1', 'Argomento 1', 'Francia e Gran Bretagna', ["Regno Unito: crisi, disoccupazione, taglio dei sussidi", "1931 · Statuto di Westminster: nasce il Commonwealth", "1936 · Fronte Popolare di Léon Blum: 40 ore e ferie retribuite"]),
     2: scheda('SP2', 'Argomento 2', 'Dittature e autoritarismi', ["Polonia, Ungheria, Balcani, Portogallo", "America Latina: colpi di Stato militari", "Giappone: regime militarista"]),
     3: [(f'{OUT}/mappa2/ultimo.png', 0, 0)],
     4: scheda('SP4', 'Argomento 3', "L'espansionismo asiatico", ["1931 · Manciuria e Manchukuo", "1937 · invasione della Cina", "Lunga marcia: 10.000 km verso lo Shaanxi"], 'asia'),
     5: scheda('SP5', 'Argomento 4', 'La guerra civile spagnola', ["Luglio 1936 · colpo di Stato di Franco", "Italia e Germania con i nazionalisti", "Brigate internazionali con la Repubblica"], 'spagna'),
     6: [(f'{OUT}/mappa4/ultimo.png', 0, 0)],
    }
    for i, L in G.items():
        t0 = T0 + T[i][0] - 0.2; t1 = (T0 + T[i + 1][0] - 0.1) if i + 1 < len(T) and (i + 1) in G else None
        if i == 7: continue
        for j, (png, x, y) in enumerate(L):
            els.append(dict(png=png, x=x, y=y, t0=t0 + 0.12 * j, d=0.5, slide=0 if x == 0 and y == 0 else 24, t1=t1 if t1 and i != 6 else None))
    dur = T0 + v['durata'] + 1.5
    return compone('spiegone', dur, base_scura(), els, [(v['wav'], T0, 1.0, v['durata'])])
