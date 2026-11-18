# -*- coding: utf-8 -*-
# Correzioni ai sottotitoli (solo errori certi del riconoscimento: nomi propri, termini, numeri). Il parlato non viene riscritto.
import re, json
RULES = [
 (r"\bAbrizar\b","Amritsar"),(r"\bBalfur\b","Balfour"),(r"\bPilduzchi\b","Piłsudski"),(r"\bPizzucsky\b","Piłsudski"),(r"\bottano\b","ottomano"),(r"\bRur\b","Ruhr"),
 (r"\bSykes Picot\b","Sykes-Picot"),(r"\bmillovecentosedici\b","1916"),(r"\bmillovecent\b","1917"),(r"\bdict\b","diktat"),(r"\bPuc\b","putsch"),
 (r"\bMeinkampf\b","Mein Kampf"),(r"\bSevre\b","Sèvres"),(r"\bAaturk\b","Atatürk"),(r"\bAtaturk\b","Atatürk"),(r"\bGoming Ta\w*\b","Guomintang"),
 (r"\bShankai Shek\b","Chiang Kai-shek"),(r"\bWudruv\b","Wilson"),(r"\bWoodwils\b","Wilson"),(r"\bVersai\b","Versailles"),(r"\bUraina\b","Ucraina"),
 (r"\bBelorussia\b","Bielorussia"),(r"\bTransordania\b","Transgiordania"),(r"\bTrangian\b","Transgiordania"),(r"\bUnheria\b","Ungheria"),(r"\bUngria\b","Ungheria"),
 (r"\bOrti\b","Horthy"),(r"\bRIF\b","Rif"),(r"\bAmestà\b","Maestà"),(r"\bsuffraggio\b","suffragio"),
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
