# -*- coding: utf-8 -*-
# Correzioni ai sottotitoli (solo errori certi del riconoscimento: nomi propri, termini, numeri). Il parlato non viene riscritto.
import re, json
RULES = [
 (r"\bvon Tirpit\b", "von Tirpitz"), (r"\bTirpiz\b", "Tirpitz"),
 (r"\bSalievo\b", "Sarajevo"), (r"\bSarievo\b", "Sarajevo"),
 (r"\bRipsiamo la cina\b", "Riprendiamo la cartina"), (r"\bla cina\b", "la cartina"), (r"\bpure la cina\b", "pure la cartina"),
 (r"\bRamanov\b", "Romanov"), (r"\bGavino Principe\b", "Gavrilo Princip"),
 (r"\bultimato un durissimo\b", "ultimatum durissimo"), (r"\bcar armati\b", "carri armati"), (r"\bcarro armato\b", "carro armato"),
 (r"\bantenne cordial\b", "Entente cordiale"), (r"\bpolveria\b", "polveriera"), (r"\bBnia\b", "Bosnia"),
 (r"\bSchlefen\b", "Schlieffen"), (r"\bmillovecentotto\b", "1908"), (r"\bnel millovecento\.", "nel 1908."),
 (r"\bmillovecentoquindici\b", "1915"), (r"\bmillovecentosedici\b", "1916"), (r"\bmillenoventosedici\b", "1916"),
 (r"\bAustrunheria\b", "Austria-Ungheria"), (r"\bAustra-Ungheria\b", "Austria-Ungheria"), (r"\bAustra Ungheria\b", "Austria-Ungheria"), (r"\bAstra Ungheria\b", "Austria-Ungheria"),
 (r"\baustrugarico\b", "austro-ungarico"), (r"\bastrungarico\b", "austro-ungarico"), (r"\bastrongarico\b", "austro-ungarico"), (r"\bstrongarico\b", "austro-ungarico"),
 (r"\bL'Asazia\b", "L'Alsazia"), (r"\bl'Asazia\b", "l'Alsazia"), (r"\bdalla Sazia dalla Lorena\b", "dall'Alsazia e dalla Lorena"),
 (r"\ba Salse e Lorena\b", "l'Alsazia e la Lorena"), (r"\bSazia della Lorena\b", "Alsazia e Lorena"), (r"\bla Sazia e la Lorena\b", "l'Alsazia e la Lorena"),
 (r"\bItesa\b", "Intesa"), (r"\bl'intese\b", "l'Intesa"),
 (r"\bVittorio Manone II\b", "Vittorio Emanuele III"), (r"\bministro degli esseri\b", "ministro degli Esteri"),
 (r"\b30 Trieste\b", "Trento e Trieste"), (r"\bTente Trieste\b", "Trento e Trieste"), (r"\bTrent Trieste\b", "Trento e Trieste"), (r"\btrento Trieste\b", "Trento e Trieste"), (r"\bTrento Trieste\b", "Trento e Trieste"),
 (r"\bfronte al pino\b", "fronte alpino"), (r"\bscopiat([aoe])\b", r"scoppiat\1"), (r"\bscopiare\b", "scoppiare"), (r"\bscopiò\b", "scoppiò"),
 (r"\bimpero ottano\b", "impero ottomano"), (r"\bigeniche\b", "igieniche"), (r"\brassunto\b", "riassunto"), (r"\bimmicidiali\b", "micidiali"),
 (r"\bDudine\b", "Udine"), (r"\bVerdan\b", "Verdun"), (r"\bStrafe Expedition\b", "Strafexpedition"), (r"\bstrafa expedition\b", "Strafexpedition"), (r"\bLorens D'Arabia\b", "Lawrence d'Arabia"),
 (r"\bL'orest d'Arabia\b", "Lawrence d'Arabia"), (r"\bCidente Lorens\b", "Lawrence"), (r"\bUusitania\b", "Lusitania"), (r"\bdell'usitane\b", "del Lusitania"),
 (r"\bOrlano\b", "Orlando"), (r"\bWoodru Wilson\b", "Woodrow Wilson"), (r"\bVud Wilson\b", "Woodrow Wilson"), (r"\bFerdinand Fauche\b", "Ferdinand Foch"),
 (r"\bEric e Ludendorff\b", "Erich Ludendorff"), (r"\bErik e Ludendorff\b", "Erich Ludendorff"), (r"\bCadorno\b", "Cadorna"), (r"\bGulielmo II\b", "Guglielmo II"),
 (r"\bCompègne\b", "Compiègne"), (r"\bAmion\b", "Amiens"), (r"\bsburgico\b", "asburgico"), (r"\bcina europea\b", "cartina europea"),
 (r"\bconduttrici di trame\b", "conduttrici di tram"), (r"\bil morbogo\b", "il morbo"), (r"\bPietroba\b", "Pietroburgo"),
 (r"\bisons\b", "Isonzo"), (r"\bl'Isons\b", "l'Isonzo"), (r"\bdisonzo\b", "dall'Isonzo"),
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
