# -*- coding: utf-8 -*-
# Piano dei pezzi del prof: intervalli sorgente, slide mostrate (immagini dal video, card dal parlato).
import json, sys, re, numpy as np
sys.path.insert(0, '/tmp/claude-0/l06')
from dati import *
from analisi import load, norm, card_vocab, STOP, W
import slides as SL

IMGPAGES = {4, 9}
# ancore (secondi sorgente) degli argomenti, nell'ordine del video: (n argomento PDF, ancora di inizio)
ANCORE = [(1, 88.0), (2, 673.0), (3, 1043.8), (4, 1412.0), (5, 1566.0), (6, 1755.0), (7, 2029.0), (8, 2149.6)]
END = 2376.5

def snap(segs, t):
    i = int(np.argmin([abs(s['inizio'] - t) for s in segs])); return i

def sub_intervals(segs, a, b):
    """togli i silenzi > 3 s riducendoli a 1,6 s: restituisce lista di (src_a, src_b)"""
    inside = [s for s in segs if s['inizio'] >= a - 0.01 and s['fine'] <= b + 0.5]
    out = []; cur = a
    for i in range(len(inside) - 1):
        g = inside[i + 1]['inizio'] - inside[i]['fine']
        if g > 3.0:
            out.append((cur, inside[i]['fine'] + 0.8)); cur = inside[i + 1]['inizio'] - 0.8
    out.append((cur, b))
    return out

def plan():
    segs = load()
    D = np.load(W + '/fr/D.npy'); n = len(D)
    pageidx = D.argmin(1) + 1; dmin = D.min(1)
    # immagine mostrata se la pagina migliore e' di immagine con distanza bassa; mediana mobile 5 s
    isimg = np.array([(p in IMGPAGES and d < 5.6) for p, d in zip(pageidx, dmin)])
    cp = SL.cards_from_pdf(); V = card_vocab(cp)
    # confini
    idx = [snap(segs, t) for _, t in ANCORE]
    topics = []
    for k, (nn, t) in enumerate(ANCORE):
        s0 = segs[idx[k]]['inizio'] - 0.35
        if k + 1 < len(ANCORE): e = segs[idx[k + 1] - 1]['fine'] + 0.45
        else: e = END
        topics.append(dict(n=nn, src_a=round(s0, 3), src_b=round(e, 3), i0=idx[k], i1=(idx[k + 1] if k + 1 < len(ANCORE) else len(segs))))
    intro = dict(src_a=0.6 - 0.0, src_b=round(segs[idx[0] - 1]['fine'] + 0.45, 3))
    # card per segmento: parole-guida (cues.py) + Viterbi monotono nell'ordine in cui il prof parla delle card
    from cues import CUES, ORD
    for T in topics:
        n = T['n']; cu = CUES[n]; od = ORD[n]; ss = segs[T['i0']:T['i1']]; M = len(ss)
        K = nc(n) + 1
        E = np.zeros((M, K))
        for i, s in enumerate(ss):
            txt = s['testo'].lower()
            nb = (ss[i - 1]['testo'].lower() if i > 0 else '') + ' ' + (ss[i + 1]['testo'].lower() if i + 1 < M else '')
            for j, k in enumerate(od):
                E[i, j + 1] = 2.0 * sum(c in txt for c in cu[k]) + 0.5 * sum(c in nb for c in cu[k])
            E[i, 0] = 0.4
        Tm = np.full((K, K), -40.0)
        for k in range(K):
            Tm[k, k] = 0.0
            if k + 1 < K: Tm[k, k + 1] = -0.6
            if k + 2 < K: Tm[k, k + 2] = -1.8
            for j in range(k + 3, K): Tm[k, j] = -3.5
        dp = np.zeros((M, K)); bp = np.zeros((M, K), int)
        dp[0] = E[0] + np.array([0, -1.0, -2.5, -4, -5, -6][:K])
        for i in range(1, M):
            for k in range(K):
                c = dp[i - 1] + Tm[:, k]; bp[i, k] = c.argmax(); dp[i, k] = c.max() + E[i, k]
        k = int(dp[-1].argmax()); path = [k]
        for i in range(M - 1, 0, -1): k = bp[i, k]; path.append(int(k))
        path = path[::-1]
        T['cards'] = [(round(s['inizio'], 2), round(s['fine'], 2), (od[p - 1] if p > 0 else -1)) for s, p in zip(ss, path)]
    return segs, topics, intro, pageidx, dmin, isimg, cp

def state_at(t, T, pageidx, isimg):
    """chiave slide al secondo sorgente t dentro l'argomento T"""
    from cues import OVERRIDE
    for a, b, n2, c2 in OVERRIDE.get(T['n'], []):
        if a <= t < b: return ('txt', n2, c2)
    ts = int(min(max(t, 0), len(pageidx) - 1))
    # immagine: richiede stabilita' (3 secondi su 5 vicini)
    w = isimg[max(0, ts - 2):ts + 3]
    if w.sum() >= 3:
        pg = int(np.bincount(pageidx[max(0, ts - 2):ts + 3][w]).argmax())
        return ('img', pg, {9: 6}.get(pg, T['n']))
    c = -1
    for a, b, k in T['cards']:
        if a - 0.2 <= t:
            c = k
    return ('txt', T['n'], c)

if __name__ == '__main__':
    segs, topics, intro, pageidx, dmin, isimg, cp = plan()
    print('intro', intro)
    for T in topics:
        print(T['n'], T['src_a'], T['src_b'], round(T['src_b'] - T['src_a']), 'segs', T['i1'] - T['i0'])
        # stati
        st = []; prev = None
        for t in np.arange(T['src_a'], T['src_b'], 1.0):
            s = state_at(t, T, pageidx, isimg)
            if s != prev: st.append((round(float(t)), s)); prev = s
        print('   cambi:', len(st), [(a, b[0] + str(b[1]) + ('/' + str(b[2]))) for a, b in st[:14]])
