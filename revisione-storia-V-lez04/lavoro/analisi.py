# -*- coding: utf-8 -*-
# Analisi: pagine mostrate dal prof nel tempo + argomenti + card accese dal parlato.
import json, re, sys, numpy as np
sys.path.insert(0, '/tmp/claude-0/w')
from dati import *
W = '/tmp/claude-0/w'
STOP = set("""che con per una uno dei del della delle degli dello nel nella nelle negli sono viene vengono come anche molto quindi allora quello quella questo questa questi queste
sulla sulle dalla dalle tutti tutto tutte più però perché cosa fatto fatti loro suo sua suoi proprio stato stati fronte guerra""".split())

def load():
    return json.load(open(W + '/tr/lez04.json'))

def norm(s):
    return re.findall(r"[a-zàèéìòù]{5,}", s.lower())

def pages_timeline():
    """pagina PDF mostrata a ogni secondo (mediana mobile, runs minimi 3 s)."""
    D = np.load(W + '/fr/D.npy'); best = D.argmin(1) + 1
    n = len(best); sm = best.copy()
    for t in range(n):
        w = best[max(0, t - 2):t + 3]; sm[t] = np.bincount(w).argmax()
    return sm

def runs(sm):
    out = []; st = 0
    for t in range(1, len(sm) + 1):
        if t == len(sm) or sm[t] != sm[st]:
            out.append((st, t, int(sm[st]))); st = t
    return out

TOPIC_OF_PAGE = {2: 1, 3: 2, 4: 2, 5: 3, 6: 3, 7: 4, 8: 4, 9: 4, 10: 5, 11: 5, 12: 6, 13: 6, 14: 6, 15: 7, 16: 7, 17: 8, 18: 8, 19: 9, 20: 10, 21: 10, 22: 11, 23: 11, 24: 11}
TEXT_PAGE = {a['pag'][0]: a['n'] for a in ARG}

def card_vocab(cp):
    V = {}
    for n, cards in cp.items():
        V[n] = []
        for c in cards:
            m = re.match(r'^(.{3,110}?):\s(.*)$', c)
            h, b = (m.group(1), m.group(2)) if m else ('', c)
            V[n].append((set(norm(h)) - STOP, set(norm(b)) - STOP))
    return V

def card_states(segs, sm, cp):
    """per ogni segmento: indice card (0-4) o -1, solo se la pagina mostrata e' una pagina di testo"""
    V = card_vocab(cp); out = []
    # gruppi di segmenti consecutivi sulla stessa pagina di testo -> Viterbi
    cur = []; curp = None
    def flush():
        if not cur: return
        n = TEXT_PAGE[curp]; vs = V[n]
        K = 6  # 5 card + nessuna
        E = np.zeros((len(cur), K))
        for i, s in enumerate(cur):
            ws = set(norm(s['testo']))
            for k in range(5):
                E[i, k] = 2.5 * len(ws & vs[k][0]) + 1.0 * len(ws & vs[k][1])
            E[i, 5] = 0.4
        # Viterbi: penalita' di salto
        T = np.full((K, K), -3.0)
        for k in range(K): T[k, k] = 0.0
        for k in range(4): T[k, k + 1] = -0.8
        T[5, :5] = -1.0; T[:5, 5] = -0.2
        dp = np.zeros((len(cur), K)); bp = np.zeros((len(cur), K), int)
        dp[0] = E[0] + np.array([0, -1, -2, -3, -4, -0.5])
        for i in range(1, len(cur)):
            for k in range(K):
                c = dp[i - 1] + T[:, k]; bp[i, k] = c.argmax(); dp[i, k] = c.max() + E[i, k]
        k = dp[-1].argmax(); path = [k]
        for i in range(len(cur) - 1, 0, -1): k = bp[i, k]; path.append(k)
        path = path[::-1]
        for s, k in zip(cur, path): out.append((s['inizio'], s['fine'], n, int(k) if k < 5 else -1))
    for s in segs:
        t = int((s['inizio'] + s['fine']) / 2); p = int(sm[min(t, len(sm) - 1)])
        if p in TEXT_PAGE:
            if curp != p: flush(); cur = []; curp = p
            cur.append(s)
        else:
            flush(); cur = []; curp = None
    flush()
    return out
