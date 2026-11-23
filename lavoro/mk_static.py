# -*- coding: utf-8 -*-
# Pezzi bianchi che dipendono dalle voci: copertina, "Di cosa parliamo", approfondimenti, schemi di ripasso, glossario, compiti.
import sys, os, json, re, subprocess, difflib, unicodedata
sys.path.insert(0, '/tmp/claude-0/l15')
from dati import *
import sl2
from plan2 import AN_OF
from extra import vdur, vname, static_piece, fr, VOX48
W = '/tmp/claude-0/l15'
PAGES = {eval(k): v for k, v in json.load(open(W + '/pieces/pages.json')).items()}
TXT = {v['nome']: v['testo'] for v in json.load(open(W + '/voci_testi_nuovi.json'))}
TEMPI = json.load(open(W + '/vox48/_tempi.json')) if os.path.exists(W + '/vox48/_tempi.json') else {}
os.makedirs(W + '/info', exist_ok=True)
def vf(name): return f'{VOX48}/{vname(name)}.wav'
def norm(s):
    s = unicodedata.normalize('NFD', s.lower()); s = ''.join(c for c in s if unicodedata.category(c) != 'Mn')
    return re.sub(r'[^a-z0-9 ]', ' ', s).split()
def sents(t): return [x for x in re.split(r'(?<=[\.\!\?])\s+', t.strip()) if x]

def starts(name, ss):
    """secondo (nella voce preparata) in cui comincia ogni frase: dai tempi di parola; altrimenti proporzionale"""
    d = vdur(name); nm = vname(name); tp = TEMPI.get(nm)
    if tp:
        ws = [(t, norm(w)) for t, w in tp['w']]; ws = [(t, x[0]) for t, x in ws if x]
        flat = [w for _, w in ws]; out = []; pos = 0
        for s in ss:
            key = norm(s)[:3]; best = None
            for i in range(pos, len(flat)):
                sc = sum(1 for a, b in zip(key, flat[i:i + 3]) if difflib.SequenceMatcher(None, a, b).ratio() > .75)
                if sc >= min(2, len(key)): best = i; break
            if best is None: out = None; break
            out.append(ws[best][0]); pos = best + 1
        if out: return out
    tot = sum(len(s) for s in ss); t = 0.0; out = []
    for s in ss: out.append(t); t += d * len(s) / tot
    return out

def save(name, N, audio, extra=None):
    json.dump(dict(n=N, audio=audio, **(extra or {})), open(f'{W}/info/{name}.json', 'w'))

def done(name, sig):
    f = f'{W}/info/{name}.json'
    if os.path.exists(f) and os.path.exists(f'{W}/pieces/{name}.mp4'):
        j = json.load(open(f))
        if j.get('sig') == sig: return True
    return False

def build_cover():
    d = vdur('BEN_R2'); sig = [round(d, 2)]
    if done('cover', sig): return
    sl2.render([('cover_np', sl2.cover(False))], W + '/slpng')
    N = fr(0.5 + d + 1.4)
    static_piece([(f'{W}/slpng/cover_np.png', N)], f'{W}/pieces/cover.mp4')
    save('cover', N, [(0.5, 'wav', vf('BEN_R2'))], dict(sig=sig))

def build_agenda():
    d = vdur('DP'); ss = sents(TXT['DP']); sig = [round(d, 2), os.path.exists(vf('DP') + '.prov') or False]
    if done('agenda', sig): return
    st = starts('DP', ss)   # prima frase = "Di cosa parliamo."
    rows = st[1:]; lead = 0.5
    items = [(f'ag_{i}', sl2.agenda(i, PAGES[('agenda',)])) for i in range(-1, 10)]
    sl2.render(items, W + '/slpng')
    N = fr(lead + d + 1.4); states = []; used = 0
    ev = [(0, -1)] + [(lead + t - 0.1, i) for i, t in enumerate(rows)] + [(lead + d + 0.2, -1)]
    for k, (t, i) in enumerate(ev):
        end = fr(ev[k + 1][0]) if k + 1 < len(ev) else N
        if end - used > 0: states.append((f'{W}/slpng/ag_{i}.png', end - used)); used = end
    static_piece(states, f'{W}/pieces/agenda.mp4')
    save('agenda', N, [(lead, 'wav', vf('DP'))], dict(sig=sig))

def build_an():
    for n in GLOBAL_ORDER:
        for k, an in enumerate(AN_OF[n], 1):
            name = f'AN{an}'; d = vdur(name); ss = sents(TXT[name]); sig = [round(d, 2), vname(name)]
            piece = f'an{n}_{k}'
            if done(piece, sig): continue
            title = ss[0].rstrip('.'); body = ss[1:]; st = starts(name, ss)[1:]
            lab = f"{GLOBAL_ORDER.index(n) + 1:02d} · {ARG[n - 1]['nome']} · APPROFONDIMENTO"
            lead = 0.8; items = []; ev = [(0.0, -1, 0)]
            for i, t in enumerate(st): ev.append((lead + t - 0.05, i, i + 1))
            ev.append((lead + d + 0.1, -1, len(body)))
            for i in range(len(body)): items.append((f'{piece}_{i}', sl2.an_slide(lab, title, body, i, i + 1, PAGES[('an', an)])))
            items.append((f'{piece}_e', sl2.an_slide(lab, title, body, -1, len(body), PAGES[('an', an)]))); items.append((f'{piece}_0e', sl2.an_slide(lab, title, body, -1, 0, PAGES[('an', an)])))
            sl2.render(items, W + '/slpng')
            N = fr(lead + d + 2.4); states = []; used = 0
            for j, (t, i, sh) in enumerate(ev):
                end = fr(ev[j + 1][0]) if j + 1 < len(ev) else N
                png = f'{W}/slpng/{piece}_0e.png' if j == 0 else (f'{W}/slpng/{piece}_e.png' if i == -1 else f'{W}/slpng/{piece}_{i}.png')
                if end - used > 0: states.append((png, end - used)); used = end
            static_piece(states, f'{W}/pieces/{piece}.mp4')
            save(piece, N, [(lead, 'wav', vf(name))], dict(sig=sig, title=title, sents=body))
            print('approfondimento', piece, round(N / 30, 1), flush=True)

def build_schema():
    for pos, n in enumerate(GLOBAL_ORDER, 1):
        names = [f'SC{n}_{k}' for k in range(1, NC + 1)]; ds = [vdur(x) for x in names]; sig = [round(x, 2) for x in ds] + [vname(x) for x in names]
        piece = f'S{pos}'
        if done(piece, sig): continue
        pg = PAGES[('schema', n)]
        items = [(f'sch{n}_{k}', sl2.schema(n, k, pg)) for k in range(NC)] + [(f'sch{n}_x', sl2.schema(n, 99, pg)), (f'sch{n}_e', sl2.schema(n, -1, pg))]
        sl2.render(items, W + '/slpng')
        t = 0.6; starts_ = []; audio = []
        for k in range(NC): audio.append((t, 'wav', vf(names[k]))); starts_.append(t); t += ds[k] + 0.9
        tot = t - 0.9 + 1.3; N = fr(tot); st = [(f'{W}/slpng/sch{n}_e.png', fr(starts_[0] - 0.1))]
        for k in range(NC):
            end = fr(starts_[k + 1] - 0.1) if k < NC - 1 else N - fr(1.2)
            st.append((f'{W}/slpng/sch{n}_{k}.png', end - sum(f for _, f in st)))
        st.append((f'{W}/slpng/sch{n}_x.png', N - sum(f for _, f in st)))
        static_piece(st, f'{W}/pieces/{piece}.mp4'); save(piece, N, audio, dict(sig=sig))

def build_gloss():
    names = ['GL0'] + [f'GL{i + 1}' for i in range(len(GLOSS))]; ds = [vdur(x) for x in names]; sig = [round(x, 2) for x in ds] + [vname(x) for x in names]
    if done('GL', sig): return
    pg = PAGES[('gloss',)]
    items = [(f'gl_{j}', sl2.gloss(j, pg)) for j in range(len(GLOSS))] + [('gl_e', sl2.gloss(-1, pg))]
    sl2.render(items, W + '/slpng')
    t = 0.5; audio = [(t, 'wav', vf('GL0'))]; t += ds[0] + 0.8; starts_ = []
    for j in range(len(GLOSS)): audio.append((t, 'wav', vf(names[j + 1]))); starts_.append(t); t += ds[j + 1] + 0.9
    N = fr(t - 0.9 + 1.4); st = [(f'{W}/slpng/gl_e.png', fr(starts_[0] - 0.1))]
    for j in range(len(GLOSS)):
        end = fr(starts_[j + 1] - 0.1) if j + 1 < len(GLOSS) else N
        st.append((f'{W}/slpng/gl_{j}.png', end - sum(f for _, f in st)))
    static_piece(st, f'{W}/pieces/GL.mp4'); save('GL', N, audio, dict(sig=sig))

def build_compiti():
    comp = [c['testo'] for c in json.load(open(W + '/compiti.json'))['compiti']]
    for g in (1, 2):
        names = [f'CPT{2 * g - 1}', f'CPT{2 * g}']; ds = [vdur(x) for x in names]; sig = [round(x, 2) for x in ds]; piece = f'CPS{g}'
        if done(piece, sig): continue
        pg = PAGES[('cmp', g)]; k0 = 2 * g - 1; tt = comp[k0 - 1:k0 + 1]
        sl2.render([(f'cps{g}_{i}', sl2.compiti2(k0, tt, i, pg)) for i in (-1, 0, 1)], W + '/slpng')
        t = 0.5; ev = []; audio = []
        for i in range(2): audio.append((t, 'wav', vf(names[i]))); ev.append(t); t += ds[i] + 0.9
        N = fr(t - 0.9 + 1.2); st = [(f'{W}/slpng/cps{g}_-1.png', fr(ev[0] - 0.1)), (f'{W}/slpng/cps{g}_0.png', fr(ev[1] - 0.1) - fr(ev[0] - 0.1)), (f'{W}/slpng/cps{g}_1.png', N - fr(ev[1] - 0.1))]
        static_piece(st, f'{W}/pieces/{piece}.mp4'); save(piece, N, audio, dict(sig=sig))

if __name__ == '__main__':
    for f in (sys.argv[1:] or ['cover', 'agenda', 'an', 'schema', 'gloss', 'compiti']): globals()['build_' + f]()
    print('ok')
