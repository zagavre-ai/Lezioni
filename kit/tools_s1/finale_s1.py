#!/usr/bin/env python3
"""Sottotitoli (.vtt) dalle battute della timeline di una Parte.
uso: python3 finale_s1.py cues_ParteN.json spec.py uscita.vtt [pdf_slide]
Le battute del docente vengono da Whisper base: i nomi propri, le date e i termini sono corretti con il vocabolario
delle slide e della scheda della lezione (correzioni automatiche: la revisione di un umano resta consigliata)."""
import sys, json, re, difflib, importlib.util, unicodedata, subprocess

cues = json.load(open(sys.argv[1]))
sp = importlib.util.spec_from_file_location('spec', sys.argv[2])
S = importlib.util.module_from_spec(sp)
sp.loader.exec_module(S)
OUT = sys.argv[3]
PDF = sys.argv[4] if len(sys.argv) > 4 else None

VOC = set()
txt = ''
if PDF:
    txt += subprocess.run(['pdftotext', '-layout', PDF, '-'], capture_output=True, text=True).stdout
for a in S.ARG:
    txt += ' ' + ' '.join(a['ripasso']) + ' ' + ' '.join(' '.join(an['voce']) for an in a['an'])
for w in re.findall(r"[A-Za-zÀ-ÿ']{5,}", txt):
    VOC.add(w)
VOC_L = {}
for w in VOC:
    VOC_L.setdefault(w.lower(), w)
# solo parole "forti" del vocabolario (iniziale maiuscola nei testi o parole lunghe)
KEYS = list(VOC_L.keys())

REG = [
    (r"\b(?:dei|de|del|da|di) ?gasper\w*", "De Gasperi"), (r"\bgasper\w*", "De Gasperi"),
    (r"\bto[g]?li?a?t+i\w*|\btogli\w+", "Togliatti"), (r"\bfa[mn]+fan\w*|\bfanfan\w*|\bfampan\w*", "Fanfani"),
    (r"\bnenn?i\w*", "Nenni"), (r"\bcon?sti?tuzion\w*", "Costituzione"), (r"\bcon?sti?tuent\w*", "Costituente"),
    (r"\bmarsh?all?\w*|\bmarcial\w*|\bpiano marsc\w*", "Marshall"), (r"\bei?naudi\w*", "Einaudi"),
    (r"\bdemocra[sz]ia cris\w+|\bdemocresti?\w+|\bdemocris\w+", "democristiana"),
    (r"\bi[l']? ?partito comunis\w*", "il Partito comunista"),
]


def corr(t):
    for pat, rep in REG:
        t = re.sub(pat, rep, t, flags=re.I)
    out = []
    for w in re.split(r'(\s+)', t):
        m = re.fullmatch(r"([^\wÀ-ÿ']*)([\wÀ-ÿ']+)([^\wÀ-ÿ']*)", w)
        if not m or len(m.group(2)) < 6:
            out.append(w)
            continue
        a, core, b = m.groups()
        if core.lower() in VOC_L:
            out.append(w)
            continue
        c = difflib.get_close_matches(core.lower(), KEYS, 1, 0.87)
        if c and c[0][0] == core[0].lower():
            r = VOC_L[c[0]]
            if core[0].isupper():
                r = r[0].upper() + r[1:]
            elif r[0].isupper() and not core[0].isupper():
                r = r  # nome proprio: maiuscola
            out.append(a + r + b)
        else:
            out.append(w)
    s = ''.join(out)
    s = re.sub(r'\s+', ' ', s).strip()
    return s[0].upper() + s[1:] if s else s


def blocchi(t, a, b):
    """spezza in blocchi di max 2 righe da 42 caratteri, 1-6 s"""
    parole = t.split()
    righe = []
    cur = ''
    for p in parole:
        if len(cur) + len(p) + 1 > 42 and cur:
            righe.append(cur)
            cur = p
        else:
            cur = (cur + ' ' + p).strip()
    if cur:
        righe.append(cur)
    bl = [righe[i:i + 2] for i in range(0, len(righe), 2)]
    tot = sum(len(' '.join(x)) for x in bl) or 1
    out = []
    c = a
    for x in bl:
        d = (b - a) * len(' '.join(x)) / tot
        out.append((c, c + d, '\n'.join(x)))
        c += d
    return out


def ts(x):
    h = int(x // 3600)
    m = int(x % 3600 // 60)
    s = x % 60
    return '%02d:%02d:%06.3f' % (h, m, s)


rows = []
for a, b, t, tipo in cues:
    t = corr(t) if tipo == 'D' else t
    if not t.strip():
        continue
    rows += blocchi(t, a, b)
rows.sort()
# niente sovrapposizioni
for i in range(len(rows) - 1):
    if rows[i][1] > rows[i + 1][0]:
        rows[i] = (rows[i][0], rows[i + 1][0] - 0.02, rows[i][2])
with open(OUT, 'w') as f:
    f.write('WEBVTT\n\n')
    for i, (a, b, t) in enumerate(rows):
        if b - a < 0.3:
            continue
        f.write('%d\n%s --> %s\n%s\n\n' % (i + 1, ts(a), ts(b), t))
print(OUT, len(rows), 'blocchi')
