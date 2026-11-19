# -*- coding: utf-8 -*-
# Correzioni ai sottotitoli (solo errori certi del riconoscimento: nomi propri, termini, numeri). Il parlato non viene riscritto.
import re, json
RULES = [
 (r"\bmillenovecentonovantuno\b","1991"),
 (r"\bGorbachev\b","Gorbačev"),(r"\bGorbaciov\b","Gorbačev"),(r"\bGorbach\b","Gorbačev"),(r"\bGorba\b","Gorbačev"),(r"\bBriesnev\b","Brežnev"),(r"\bGriesnev\b","Brežnev"),
 (r"\bComeini\b","Khomeini"),(r"\bTien Amen\b","Tienanmen"),(r"\bTienamen\b","Tienanmen"),(r"\bsciaria\b","sharia"),(r"\bPinocchio\b","Pinochet"),(r"\bPinocch\b","Pinochet"),(r"\bPinoce\b","Pinochet"),
 (r"\bBete Woods\b","Bretton Woods"),(r"\bPerestroica\b","Perestrojka"),(r"\bGlasson\b","Glasnost"),(r"\bCem David\b","Camp David"),(r"\bAl Sadat\b","Al-Sadat"),(r"\bYom Kippur\b","Yom Kippur"),
 (r"\bSAT uno\b","SALT 1"),(r"\bOlp\b","OLP"),(r"\bFranco Mitterrand\b","François Mitterrand"),(r"\bRon Reagan\b","Ronald Reagan"),
 (r"\bMikhail\b","Michail"),(r"\bBriezhnev\b","Brežnev"),(r"\bpiopare\b","bipolare"),(r"\bURS\b","URSS"),
]
def corregge(t):
    for a, b in RULES: t = re.sub(a, b, t)
    return t

def words_of(seg):
    """parole con tempo (inizio parola) dai token"""
    W_ = []
    for t, tok in seg['parole']:
        if tok.startswith(' ') or not W_: W_.append([t, tok.strip()])
        else: W_[-1][1] += tok
    return W_

def cues(segs, max_chars=84, line=42):
    """segmenti -> cue [(t0,t1,testo)] max 2 righe, tempi dalle parole; testo corretto"""
    out = []
    for s in segs:
        ws = words_of(s)
        new = corregge(s['testo']).split()
        old = ' '.join(w for _, w in ws).split()
        # allinea i tempi: stessa lunghezza -> per indice, altrimenti proporzionale
        if len(new) == len(ws): tw = [(w[0], n) for w, n in zip(ws, new)]
        else:
            tw = []
            for i, n in enumerate(new):
                j = min(len(ws) - 1, int(i * len(ws) / max(1, len(new)))); tw.append((ws[j][0], n))
        cur = [];
        def flush(end):
            if not cur: return
            out.append((cur[0][0], end, ' '.join(n for _, n in cur)))
        for i, (t, n) in enumerate(tw):
            txt = ' '.join(x for _, x in cur + [(t, n)])
            if cur and (len(txt) > max_chars or (cur and cur[-1][1].endswith(('.', '?', '!')) and len(' '.join(x for _, x in cur)) > 28)):
                flush(t); cur = []
            cur.append((t, n))
        flush(s['fine'])
    # durata minima/massima, niente sovrapposizioni
    res = []
    for i, (a, b, t) in enumerate(out):
        nxt = out[i + 1][0] if i + 1 < len(out) else b + 1
        b = min(max(b, a + 0.8), nxt - 0.02, a + 7.0)
        res.append((a, b, t))
    return res

def wrap2(t, line=42):
    if len(t) <= line: return t
    ws = t.split(); best = None
    for k in range(1, len(ws)):
        a = ' '.join(ws[:k]); b = ' '.join(ws[k:])
        sc = max(len(a), len(b))
        if best is None or sc < best[0]: best = (sc, a, b)
    return best[1] + '\n' + best[2]
