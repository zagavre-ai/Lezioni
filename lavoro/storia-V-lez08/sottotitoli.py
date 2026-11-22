#!/usr/bin/env python3
# Sottotitoli .vtt sul video FINALE: parole del docente (trascrizione dell'originale rimappata sui tempi del montaggio) con i termini
# corretti presi dal materiale del docente. Uso: sottotitoli.py <parte 1|2> <timeline.json> <uscita.vtt>
import sys, os, json, re, difflib
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from plan import S, mappa
H = os.path.dirname(os.path.abspath(__file__))
PIANO = json.load(open(H + '/piano.json'))
VOC = ['Mussolini', 'Giolitti', "d'Annunzio", 'Fiume', 'Rapallo', 'Matteotti', 'Facta', 'Nitti', 'Sturzo', 'Acerbo', 'Aventino', 'quadrumviri', 'Balbo', 'Grandi', 'Bonomi', 'Diaz', 'Cadorna',
       'Bordiga', 'Gramsci', 'Marinetti', 'Dumini', 'Livorno', 'Bologna', 'Cremona', 'Ravenna', 'Trieste', 'Dalmazia', 'Jugoslavia', 'bolscevica', 'squadrismo', 'squadristi', 'fascisti', 'fascismo',
       'liberali', 'socialisti', 'comunisti', 'proporzionale', 'suffragio', 'latifondi', 'inflazione', 'commesse', 'Parigi', 'Londra', 'Vittorio', 'Emanuele', 'Savoia', 'Giacomo', 'Benito', 'Luigi',
       'Francesco', 'Saverio', 'Palazzo', 'Accursio', 'Milizia', 'Gran', 'Consiglio', 'bivacco', 'massimalisti', 'Villa', 'Giusti', 'Carso', 'Isonzo', 'Piave', 'Vittorio', 'Veneto', 'Popolo', 'Italia']
VL = {v.lower(): v for v in VOC}
def corr(w):
    m = re.match(r"^([^\wàèéìòù']*)([\wàèéìòù']+)([^\wàèéìòù']*)$", w, re.I)
    if not m: return w
    a, c, b = m.groups(); cl = c.lower()
    if len(cl) >= 6:
        best = difflib.get_close_matches(cl, list(VL), 1, 0.84)
        if best: c = VL[best[0]]
    return a + c + b
def parole_seg(s):
    ws = []
    for t, w in s['parole']:
        if w.startswith(' ') or not ws: ws.append([t, w.strip()])
        else: ws[-1][1] += w
    return ws
def blocchi(parole):
    """parole: [(t_inizio_video, testo)] ; ritorna [(t0,t1,righe)]"""
    out = []; cur = [];
    def chiudi(fine):
        nonlocal cur
        if not cur: return
        txt = ' '.join(w for t, w in cur); t0 = cur[0][0]
        righe = []; r = ''
        for w in txt.split():
            if len((r + ' ' + w).strip()) <= 42: r = (r + ' ' + w).strip()
            else: righe.append(r); r = w
        righe.append(r)
        while len(righe) > 2: righe = [' '.join(righe[:2])] + righe[2:]
        out.append((t0, max(fine, t0 + 0.8), righe)); cur = []
    for k, (t, w) in enumerate(parole):
        if cur and (t - cur[0][0] > 5.5 or len(' '.join(x[1] for x in cur)) > 78 or (t - cur[-1][0] > 1.2) or (re.search(r'[.?!]$', cur[-1][1]) and len(' '.join(x[1] for x in cur)) > 30)):
            chiudi(min(t - 0.02, cur[-1][0] + 2.0) if t - cur[-1][0] > 1.2 else t - 0.02)
        cur.append((t, w))
    if cur: chiudi(cur[-1][0] + 1.5)
    return out
def ts(x):
    h, r = divmod(x, 3600); m, r = divmod(r, 60); return '%02d:%02d:%06.3f' % (h, m, r)
if __name__ == '__main__':
    parte, TL, OUT = sys.argv[1], sys.argv[2], sys.argv[3]
    tl = json.load(open(TL)); P = []
    for nome, t0, d, *_ in tl:
        if nome == 'D0': key = ['D0', 'D0b']
        elif nome.startswith('D') and nome[1:].isdigit(): key = [nome[1:]]
        else: continue
        iv = PIANO['D0']['iv'] + PIANO['D0b']['iv'] if nome == 'D0' else PIANO[key[0]]['iv']
        # unisci intervalli contigui
        ivm = []
        for a, b in iv:
            if ivm and abs(a - ivm[-1][1]) < 1e-6: ivm[-1][1] = b
            else: ivm.append([a, b])
        f = mappa(ivm); a0, b1 = ivm[0][0], ivm[-1][1]
        for s in S:
            if s['inizio'] < a0 - 0.01 or s['fine'] > b1 + 0.3: continue
            if not any(a - 0.2 <= s['inizio'] <= b for a, b in ivm): continue
            for t, w in parole_seg(s):
                if w and any(a - 0.05 <= t <= b + 0.05 for a, b in ivm): P.append((t0 + f(t), corr(w)))
    P.sort()
    B = blocchi(P)
    with open(OUT, 'w') as fo:
        fo.write('WEBVTT\n\n')
        for k, (a, b, r) in enumerate(B): fo.write(f'{ts(a)} --> {ts(b)}\n' + '\n'.join(r) + '\n\n')
    print(OUT, len(B), 'blocchi')
