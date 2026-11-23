import sys, json, re
part = sys.argv[1]; out = sys.argv[2]
subs = json.load(open(f'/home/user/w3/subs_Parte{part}.json'))
FILL = re.compile(r'^(um+|uh+|hm+|hola\.?|and|in debt\.?|it\'s|the|they|i said it\'s meant\.?|solo que\.\.\.|s come|ecco\.?|d\'accordo\??)$', re.I)
CORR = [(r'\bDoga\b', 'Dogali'), (r'\bGioetti\b', 'Giolitti'), (r'\bPretto subito\b', 'Premetto subito'), (r'\bFalc\b\.?', 'Falck'), (r'\bsalvemini lo che ho\b', 'Salvemini, lo ha'), (r'\bGi[eo]l[ie]tt?i\b|\bGioli?te\b|\bGioletti\b|\bGielitti\b|\bGioritti\b|\bGiuriti\b|\bGiuniti\b|\bGiolite\b|\bCiolitti\b|\bGioliti\b|\bgiolitti\b|\bGiorgi ti\b', 'Giolitti'),
        (r'\bCrispy\b', 'Crispi'), (r'\bBava Peccaris\b|\bBava Beccari\b|\bBeccaris\b', 'Bava Beccaris'), (r'\bBava Bava Beccaris\b', 'Bava Beccaris'),
        (r'\bGian?ardelli\b|\bZanardeli\b', 'Zanardelli'), (r'\bDi Rudini\b|\bDi Rudinì\b', 'Di Rudinì'), (r'\bPerlu\b|\bPellù\b|\bPelù\b|\bPerlù\b', 'Pelloux'),
        (r'\bKulisov\b', 'Kuliscioff'), (r'\bSalve Vini\b|\bGatano\b', 'Salvemini'), (r'\bAdu\b', 'Adua'), (r'\bOgali\b', 'Dogali'),
        (r'\bTuratti\b', 'Turati'), (r'\bGentilone\b', 'Gentiloni'), (r'\bGaetano Salvemini\b', 'Gaetano Salvemini'),
        (r'\bgiolittiana\b', 'giolittiana'), (r'\bmillovacento\b|\bmillocentoun?\b', 'mille'), (r'\bUmberito\b', 'Umberto'),
        (r'\bFiate?\b', 'Fiat'), (r'\bAssal\b|\bl\'aldo\b|\bl\'assal\b', "l'Ansaldo"), (r'\bBisolati\b', 'Bissolati'), (r'\bLosanne\b', 'Losanna'),
        (r'\bIps\b', 'INPS'), (r'\bCgdl\b|\bCGDL\b', 'CGdL')]
def fix(t):
    t = t.strip()
    for a, b in CORR: t = re.sub(a, b, t)
    t = re.sub(r'\s+', ' ', t)
    return t
def ts(s):
    s = max(0, s); h = int(s // 3600); m = int(s % 3600 // 60); return '%02d:%02d:%06.3f' % (h, m, s % 60)
cues = []
for t0, t1, txt, nm in sorted(subs, key=lambda x: x[0]):
    txt = fix(txt)
    if not txt or FILL.match(txt): continue
    words = txt.split(); lines = []; cur = ''
    for w in words:
        if len(cur) + len(w) + 1 > 42 and cur: lines.append(cur); cur = w
        else: cur = (cur + ' ' + w).strip()
    if cur: lines.append(cur)
    blocks = [lines[i:i + 2] for i in range(0, len(lines), 2)]
    tot = sum(len(' '.join(b)) for b in blocks) or 1; t = t0
    for b in blocks:
        d = (t1 - t0) * len(' '.join(b)) / tot
        cues.append([t, min(t + max(d, 0.9), t1 + 0.3), '\n'.join(b)]); t += d
# nessuna sovrapposizione
for i in range(len(cues) - 1):
    if cues[i][1] > cues[i + 1][0] - 0.02: cues[i][1] = cues[i + 1][0] - 0.02
with open(out, 'w') as f:
    f.write('WEBVTT\n\n')
    for i, (a, b, t) in enumerate(cues):
        if b - a < 0.3: continue
        f.write(f'{i + 1}\n{ts(a)} --> {ts(b)}\n{t}\n\n')
print(len(cues), 'cue', out)
