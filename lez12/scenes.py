import os, sys, json, html, subprocess
sys.path.insert(0, '/home/user/Lezioni/lez12')
from rend import R, MAT
import piano as PI
from piano import SL, IM, P, SEQ, EYEB, ARGO
import engine as E
from voci import VOCI
PNG = E.W + 'build/png/'; os.makedirs(PNG, exist_ok=True)
_r = None
def rr():
    global _r
    if _r is None: _r = R()
    return _r
# ---- numeri di pagina: ordine di prima comparsa nel video
PAGES = {}
for pid, a, t0, t1, st in P:
    for t, k, ac in st:
        if k not in PAGES and k != 'COVERP' and k != 'COVER': PAGES[k] = len(PAGES) + 2
def cache(path, fn):
    if not os.path.exists(path): fn(path)
    return path
def png_slide(key, active, kwn, prof=True, zoom=False):
    nm = f'{PNG}{key}_{active}_{kwn}_{int(prof)}{"z" if zoom else ""}.png'
    def f(o):
        if key in SL:
            a, title, cards, kw = SL[key]
            rr().slide(EYEB[a], title, cards, active, PAGES[key], o, kw=kw[:kwn] if kwn is not None else kw, prof=prof, zoom=zoom)
        else:
            a, title, items = IM[key]
            rr().imgslide(EYEB[a], title, items, PAGES[key], o, prof=prof)
    return cache(nm, f)
def cover_html(prof):
    h = f'<img class=logo src="file://{pj("LOGO")}"><div class=hl0></div>'
    return h
def pj(k):
    from rend import LOGO
    return LOGO
def png_cover(prof):
    nm = f'{PNG}cover_{int(prof)}.png'
    def f(o):
        li = ''.join(f'<li>{html.escape(v)}</li>' for v in ARGO.values())
        h = f'<img class=logo src="file://{pj(0)}"><div class=hl0></div>'
        h += f'<div class=eb style="top:150px">STORIA DELL\'ARTE V · VIDEOLEZIONE</div>'
        h += f'<div class=ti style="top:230px;font-size:120px;width:1300px">{PI.TITOLO}</div><div class=bar style="top:520px"></div>'
        h += f'<div class=card style="top:580px;width:1000px;padding:22px 34px"><div style="font:700 22px Figtree;letter-spacing:.14em;color:#2060AF;margin-bottom:8px">ARGOMENTI</div><ul style="margin:0;padding-left:34px;font:600 38px/1.5 Figtree">{li}</ul></div>'
        h += f'<div class=ft><b style="left:0">{MAT}</b></div>'
        if prof: h += '<div class=cam></div><div class=fascia><div class=n>Giorgio Mazzotti</div><div class=m>PROF. DI STORIA DELL\'ARTE</div></div>'
        rr().page(h, o)
    return cache(nm, f)
# ---------- scena del docente ----------
LEAD, TAIL, PRE, TAILO = 0.35, 0.35, 0.15, 0.12
def expand(states, t_end):
    """stati lunghi (>70 s) -> finestre alternate normale/zoom di ~50 s, così la schermata cambia sempre; la colonna Parole chiave si riempie"""
    out = []
    for i, (t, k, ac) in enumerate(states):
        e = states[i + 1][0] if i + 1 < len(states) else t_end
        if k in SL and e - t > 45:
            nk = len(SL[k][3]); n = max(1, round((e - t) / 50)) if ac is not None and e - t > 70 else max(1, int((e - t) // 40))
            for j in range(n + 1 if ac is None or e - t <= 70 else n):
                tt = t + (e - t) * j / (n + 1 if ac is None or e - t <= 70 else n)
                out.append((tt, k, ac, min(nk, j + 1), bool(ac is not None and e - t > 70 and j % 2 == 1)))
        else: out.append((t, k, ac, len(SL[k][3]) if k in SL else None, False))
    return out
def scene_prof(pid):
    p = [x for x in P if x[0] == pid][0]; _, a, t0, t1, st = p
    t0p, t1p = t0 - PRE, t1 + TAILO
    d = t1p - t0p; D = LEAD + d + TAIL
    ex = expand([(t, k, ac) for t, k, ac in st], t1p)
    S = []
    for i, (t, k, ac, kwn, zm) in enumerate(ex):
        if k == 'COVERP': png = png_cover(True)
        else: png = png_slide(k, ac, kwn, True, zm)
        ts = 0.0 if i == 0 else LEAD + (t - t0p)
        te = None if i + 1 == len(ex) else LEAD + (ex[i + 1][0] - t0p)
        S.append((png, ts, te, True))
    return E.make(pid, D, 'white', S, cam=(t0p, d, LEAD), audio=[(E.PROF, t0p + 0.030, d, LEAD, 0)]), E.snap(D)
# ---------- schede Kore ----------
def loud(wav):
    o = E.B + 'vn_' + os.path.basename(wav)
    if not os.path.exists(o) or os.path.getmtime(o) < os.path.getmtime(wav):
        E.run(['ffmpeg', '-y', '-v', 'error', '-i', wav, '-af', 'loudnorm=I=-16:TP=-1.5:LRA=7,aresample=48000', '-ac', '1', o])
    return o
def line_times(text, markers, vs, ve):
    n = len(text); out = []
    for m in markers:
        i = text.find(m)
        if i < 0: raise ValueError(f'marcatore non trovato: {m!r}')
        out.append(vs + (ve - vs) * i / n)
    return out
JG = {'finale': (E.K + 'finale.wav', 3.5), 'trans': (E.K + 'trans.wav', 2.02), 'titolo': (E.K + 'titolo.wav', 2.72), 'repaso': (E.K + 'repaso.wav', 3.32), 'quiz': (E.K + 'quiz.wav', 3.32)}
META = {}
def kore(name, voice, markers, render, start_j='trans', end_j=None, hold=1.2, bg='dark', v0=None):
    """render(k): png dell'avanzamento k (k=-1 = scheda prima della prima riga, k=len-1 = tutto)"""
    wav = loud(E.vox(voice)); vs, ve = E.voice_span(wav)
    v0 = v0 if v0 is not None else (1.9 if start_j else 0.9)
    text = VOCI[voice]; lt = line_times(text, markers, vs, ve) if markers else []
    META[name] = dict(voice=voice, v0=v0, vs=vs, ve=ve)
    aud = [(wav, vs, ve - vs, v0, 0)]
    if start_j: aud.append((JG[start_j][0], None, None, 0.0, -6))
    D = v0 + (ve - vs) + hold
    if end_j: D = max(D, v0 + (ve - vs) + JG[end_j][1] + 0.35); aud.append((JG[end_j][0], None, None, D - JG[end_j][1] - 0.2, -6))
    S = []; ts = [0.0] + [v0 + (t - vs) for t in lt]
    for k in range(len(ts)):
        png = render(k - 1)
        S.append((png, ts[k], ts[k + 1] if k + 1 < len(ts) else None, False))
    return E.make(name, D, bg, S, audio=aud), E.snap(D)
def kore_lines(name, voice, eyebrow, title, lines, markers, start_j='trans', end_j=None, imgs=None, fs=None):
    """schede con righe che si accendono con la voce; imgs: lista (indice riga da cui vale, (path,x,y,w,h), didascalia)"""
    def render(k):
        nm = f'{PNG}{name}_{k}.png'
        def f(o):
            im = None; cap = None
            if imgs:
                for fromk, ii, cc in imgs:
                    if k >= fromk: im, cap = ii, cc
            rr().dark_lines(eyebrow, title, lines, k if k >= 0 else None, o, img=im, imgcap=cap, fs=fs)
        return cache(nm, f)
    return kore(name, voice, markers, render, start_j, end_j)
