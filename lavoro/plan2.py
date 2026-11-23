# -*- coding: utf-8 -*-
# Piano dei pezzi del prof (correzioni 22/11): argomenti, tratti (tagli solo su frase finita), stati slide a finestra, card dal parlato.
import json, sys, re, numpy as np
sys.path.insert(0, '/tmp/claude-0/l15')
from dati import *
from cues import OVERRIDE
W = '/tmp/claude-0/l15'
IMGPAGES = {6, 8, 11, 13, 15}
IMG_TOPIC = {6: 4, 8: 5, 11: 7, 13: 8, 15: 9}
ANCORE = [(1, 108.6), (2, 430.7), (3, 619.3), (4, 826.9), (5, 1067.9), (6, 1214.9), (7, 1550.0), (8, 1897.8), (9, 2173.5), (10, 2394.0)]
END = 2538.9
STARTV = 0.6

CUESM = {
 1: [(109.2, -1), (178.0, 0), (214.2, 2), (283.4, 1), (304.4, 3), (324.4, 2), (377.4, 1), (395.8, 3)],
 2: [(430.4, -1), (437.4, 3), (458.8, 0), (567.4, 2), (592.0, 1)],
 3: [(618.7, -1), (639.6, 0), (705.0, 1), (757.2, 2)],
 4: [(826.7, -1), (827.1, 1), (875.3, 0), (916.2, 2), (1031.7, 3)],
 5: [(1067.9, -1), (1114.1, 0), (1136.4, 1), (1142.3, 2), (1198.3, 3)],
 6: [(1215.0, -1), (1221.9, 1), (1234.2, 2), (1266.9, 3), (1493.8, 1), (1498.5, 0)],
 7: [(1549.8, -1), (1554.5, 0), (1634.6, 1), (1711.4, 2)],
 8: [(1897.7, -1), (1913.9, 0), (1946.3, 1), (2047.6, 2), (2082.4, 3)],
 9: [(2172.7, -1), (2175.2, 0), (2203.1, 1), (2266.6, 2), (2310.6, 3)],
 10: [(2393.3, -1), (2401.9, 0), (2431.3, 1), (2463.8, 2), (2515.4, 3)],
}
import os
WIN = json.load(open(W + '/win.json')) if os.path.exists(W + '/win.json') else {}
def windows(n): return [tuple(x) for x in WIN.get(str(n), [[0, 1, 2], [1, 2, 3]])]
def cue_track(n):
    """[(secondo, card, finestra)]: la finestra cambia se la card accesa non e' nella finestra corrente, oppure (se e' anche nell'altra)
    quando la finestra e' la stessa da piu' di 100 s: nessuna schermata resta uguale a lungo"""
    ws = windows(n); cur = 0; out = []; wstart = CUESM[n][0][0]
    for t, c in CUESM[n]:
        if c >= 0:
            if c not in ws[cur]:
                cur = next(i for i, w in enumerate(ws) if c in w); wstart = t
            elif t - wstart > 100 and len(ws) > 1 and c in ws[1 - cur]:
                cur = 1 - cur; wstart = t
        out.append((t, c, cur))
    return out

def load(): return json.load(open(W + '/tr/lez15.json'))
def fine_frase(t): return bool(re.search(r'[\.\?\!]\s*$', t)) and not t.strip().endswith('...') and not t.strip().endswith('…')

def sub_intervals(segs, a, b, soglia=2.5, tieni=0.5):
    """toglie le pause oltre `soglia` s riducendole a circa 1 s (0,5 s di coda + 0,5 s di testa); non taglia mai dentro una frase"""
    inside = [s for s in segs if s['inizio'] >= a - 0.01 and s['fine'] <= b + 0.5]
    out = []; cur = a
    for i in range(len(inside) - 1):
        g = inside[i + 1]['inizio'] - inside[i]['fine']
        if g > soglia:
            out.append((cur, inside[i]['fine'] + tieni)); cur = inside[i + 1]['inizio'] - tieni
    out.append((cur, b))
    return out

def plan():
    segs = load()
    D = np.load(W + '/fr/D.npy'); pageidx = D.argmin(1) + 1; dmin = D.min(1)
    isimg = np.array([(p in IMGPAGES and d < 5.6) for p, d in zip(pageidx, dmin)])
    idx = [int(np.argmin([abs(s['inizio'] - t) for s in segs])) for _, t in ANCORE]
    topics = []
    for k, (nn, t) in enumerate(ANCORE):
        s0 = segs[idx[k]]['inizio'] - 0.35
        e = (segs[idx[k + 1] - 1]['fine'] + 0.45) if k + 1 < len(ANCORE) else END
        topics.append(dict(n=nn, src_a=round(s0, 3), src_b=round(e, 3), i0=idx[k], i1=(idx[k + 1] if k + 1 < len(ANCORE) else len(segs))))
    intro = dict(src_a=STARTV, src_b=round(segs[idx[0] - 1]['fine'] + 0.45, 3))
    for T in topics: T['cards'] = cue_track(T['n'])
    return segs, topics, intro, pageidx, dmin, isimg

ZOOM = {11: [(1722.0, 0), (1738.0, 1), (1765.0, 2), (1793.0, 3), (1815.0, 4), (1837.0, 5), (1878.0, 0)], 13: [(2102.0, 0)]}
def zoom_idx(pg, t):
    z = 0
    for a, k in ZOOM.get(pg, []):
        if t >= a: z = k
    return z

def state_at(t, T, pageidx, isimg):
    """chiave slide al secondo sorgente t dentro l'argomento T: ('txt', n, finestra, card) oppure ('img', pagina, argomento)"""
    for a, b, n2, c2 in OVERRIDE.get(T['n'], []):
        if a <= t < b: return ('txt', n2, 1 if c2 >= 2 else 0, c2)
    ts = int(min(max(t, 0), len(pageidx) - 1)); w = isimg[max(0, ts - 2):ts + 3]
    if w.sum() >= 3:
        pg = int(np.bincount(pageidx[max(0, ts - 2):ts + 3][w]).argmax())
        return ('img', pg, IMG_TOPIC.get(pg, T['n']), zoom_idx(pg, t))
    c = -1; w = 0
    for tt, k, ww in T['cards']:
        if tt <= t: c = k; w = ww
    return ('txt', T['n'], w, c)

SPLIT = {1: [296.9], 2: [592.0], 3: [763.6], 4: [916.2], 5: [1142.3], 6: [1304.7], 7: [1711.4, 1793.3], 8: [2046.6], 9: [2304.4], 10: [2463.8]}
# digressioni del prof rimesse nell'argomento a cui appartengono (nessuna slide o immagine in due argomenti):
#   Maghreb/Gheddafi (segmenti 240-251) -> argomento 5; colonie portoghesi (segmenti 231-239) -> argomento 7
EXTRA = {5: (240, 251), 7: (231, 239)}
SKIP = {6: [(1304.5, 1480.0)]}
DROPS = [(103.0, 105.40), (827.78, 828.58), (511.85, 512.65), (1065.8, 1066.4), (1249.75, 1250.55), (1255.55, 1257.70), (1436.0, 1436.65), (1797.95, 1799.7), (2340.45, 2341.2)]
# ripetizioni, incespicamenti e riempitivi del prof (Per il loro. Per le loro. / L'Indonesia appunto / Um / ehm / Mm): tolti
AN_OF = {1: (1, 2), 2: (3, 4), 3: (5, 6), 4: (7, 8), 5: (9, 10), 6: (12, 11), 7: (13, 14), 8: (15, 16), 9: (17, 18), 10: (19, 20)}

def cut_intervals(subs, cuts):
    out = []
    for x, y in subs:
        cur = [(x, y)]
        for a, b in cuts:
            nxt = []
            for p, q in cur:
                if b <= p or a >= q: nxt.append((p, q)); continue
                if a - p > 0.2: nxt.append((p, a))
                if q - b > 0.2: nxt.append((b, q))
            cur = nxt
        out += cur
    return out

def tracts(segs, T):
    """tratti del prof dentro l'argomento: tagli solo a fine frase, 0,15 s prima della frase che segue. Ritorna [(a,b)] e la tabella dei tagli."""
    ss = segs[T['i0']:T['i1']]; cuts = []
    for t in SPLIT[T['n']]:
        j = min(range(1, len(ss)), key=lambda j: abs(ss[j]['inizio'] - t))
        cuts.append(j)
    a0 = T['src_a']; out = []; info = []
    for j in cuts:
        end = min(ss[j - 1]['fine'] + 0.45, ss[j]['inizio'] - 0.3)
        out.append((a0, round(end, 3))); info.append((round(end, 1), ss[j - 1]['testo'], fine_frase(ss[j - 1]['testo'])))
        a0 = round(ss[j]['inizio'] - 0.15, 3)
    out.append((a0, T['src_b']))
    if T['n'] in EXTRA:
        i0, i1 = EXTRA[T['n']]
        a = round(segs[i0]['inizio'] - 0.15, 3); b = round(min(segs[i1]['fine'] + 0.45, segs[i1 + 1]['inizio'] - 0.3), 3)
        out.append((a, b)); info.append((b, segs[i1]['testo'], fine_frase(segs[i1]['testo'])))
    return out, info

def subs_of(segs, a, b, n):
    return cut_intervals(sub_intervals(segs, a, b), DROPS + SKIP.get(n, []))

if __name__ == '__main__':
    segs, topics, intro, pageidx, dmin, isimg = plan()
    print('intro', intro)
    for T in topics:
        tr, info = tracts(segs, T)
        print(T['n'], T['src_a'], T['src_b'], [ (round(a),round(b)) for a,b in tr], info)
        prev = None; st = []
        for t in np.arange(T['src_a'], T['src_b'], 1.0):
            s = state_at(t, T, pageidx, isimg)
            if s != prev: st.append((round(float(t)), s)); prev = s
        print('   ', [(a, '/'.join(map(str, b[1:]))) for a, b in st])
