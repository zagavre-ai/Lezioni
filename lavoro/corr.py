# -*- coding: utf-8 -*-
# Correzioni ai sottotitoli (solo errori certi del riconoscimento: nomi propri, termini, numeri). Il parlato non viene riscritto.
import re, json
RULES = [
 (r"\bUSA e Urs\b", "USA e URSS"), (r"\bUrs\b", "URSS"), (r"\bSaria\b", "Siria"), (r"\bl'indonesia\b", "l'Indonesia"), (r"\bViet Minh\b", "Vietminh"),
 (r"\bDire Idris I\b", "Re Idris I"), (r"\bguerra in civile\b", "guerra civile"), (r"\bil canali di Suez istanzialmente\b", "il canale di Suez sostanzialmente"),
 (r"\bl'onu\b", "l'ONU"), (r"\bonu\b", "ONU"), (r"\bONU\b", "ONU"),
 (r"\bUm\b[,.]?\s*", ""),
 (r"\bSeylon\b", "Ceylon"), (r"\bGana\b", "Ghana"), (r"\bBandum\b", "Bandung"), (r"\bYen Bien plus\b", "Dien Bien Phu"),
 (r"\bJaharlal Neru\b", "Jawaharlal Nehru"), (r"\bGamad Hab\b", "Gamal Abd"), (r"\bHel nascer\b", "el-Nasser"),
 (r"\bLindocina\b", "L'Indocina"), (r"\bGeddafi\b", "Gheddafi"), (r"\bGet Davi\b", "Gheddafi"), (r"\bmandella\b", "Mandela"),
 (r"\bgandy\b", "Gandhi"), (r"\bsessante\b", "sessanta"), (r"\bpenisola del Sine\b", "penisola del Sinai"),
 (r"\bLause Camposo\b", "Laos e Cambogia"), (r"\bdalla partite\b", "dall'apartheid"), (r"\bappartare\b", "l'apartheid"),
 (r"\bscopiò\b", "scoppiò"), (r"\bscopia\b", "scoppia"), (r"\bscopi\b", "scoppiò"), (r"\bandioriente\b", "andiamo in Medio Oriente"),
 (r"\bintreciano\b", "intrecciano"), (r"\bintracciò\b", "intrecciò"), (r"\bmillenovecentosessantove\b", "1969"), (r"\bduemilaundici\b", "2011"),
 (r"\bmillenovecentoquarantacinque\b", "1945"), (r"\bmillenovecentosettantacinque\b", "1975"), (r"\bmille novecentocinquantadue\b", "1952"),
 (r"\bdeconalizzazione\b", "decolonizzazione"), (r"\bindipendendenze\b", "indipendenze"), (r"\bsubsahriana\b", "subsahariana"),
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
