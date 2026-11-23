# Sottotitoli .vtt sul video finale: prof (trascrizione corretta coi termini del materiale) + voci narranti
import sys, os, re, json
sys.path.insert(0, '/home/user/w18')
import prof, kore
from kore import *
R = '/home/user/w18/'
CORR = [  # (regex, corretto) · nomi e termini presi dalle slide, dalle mappe e dalle domande del prof
 (r'Hansel Kiefer|Hansel Kief\w*|Hansel', 'Anselm Kiefer'), (r'Achille Vonito Oliva|Achille Bonito Oliva', 'Achille Bonito Oliva'),
 (r'Sherry Levin\b|Sherry Levine', 'Sherrie Levine'), (r'\bLevin\b', 'Levine'), (r'Ron Mook|Ron Mook\w*|Make\b', 'Ron Mueck'), (r'Mark Queen', 'Marc Quinn'),
 (r'Jake e Dino\b', 'Jake e Dinos'), (r'Zygothica Celebration', 'Zygotic Acceleration'), (r'Fang Li Jun|Fang Yu\.?|Li Jun|Li Gun|li Yun|Fang Li Jun', 'Fang Lijun'),
 (r'Inka Shonibare|Inka Schonibare', 'Yinka Shonibare'), (r'Schonibare|Shonibare', 'Shonibare'), (r'Le Magician de la Terre', 'Les Magiciens de la terre'),
 (r'Sandro Kia|Sandro Chia', 'Sandro Chia'), (r'\bKia\b', 'Chia'), (r'Palladino', 'Paladino'), (r'Keith Herring', 'Keith Haring'), (r'\bHerring\b', 'Haring'),
 (r'Radian Baby', 'Radiant Baby'), (r'Andreas Gurski|Girski|Gurski', 'Gursky'), (r'Cyndee Sherman|Cyndi Sherman', 'Cindy Sherman'), (r'Shirin Ashat|Ne Shat|Shirin Ne Shat', 'Shirin Neshat'),
 (r'Bruce Neumann', 'Bruce Nauman'), (r'Matthew Burney|Bernie|Bonnet\b', 'Matthew Barney'), (r'Jeff Kuhnz|Jeff Kunz|Kuhnz|Kunz', 'Jeff Koons'), (r'Anish Kapur|Anish Kapoor', 'Anish Kapoor'),
 (r'Catteran|Catalan\b', 'Cattelan'), (r'Franco Gary|Frank Gary|Gary\b', 'Gehry'), (r'Zara Hadid', 'Zaha Hadid'), (r'Maxi Aroma|Maxi\b', 'MAXXI'),
 (r'Lyotard', 'Lyotard'), (r'Torreggi Emile|Toreggi Emile', 'Twin Towers'), (r'Tuttomondo|tutto mondo', 'Tuttomondo'), (r'Cree Master|Creemaster', 'Cremaster'),
]
def corr(t):
    for a, b in CORR: t = re.sub(a, b, t)
    return t.strip()

def ts(x):
    h, r = divmod(x, 3600); m, r = divmod(r, 60); return '%02d:%02d:%06.3f' % (h, m, r)

def spezza(testo, t0, t1, maxc=84):
    w = testo.split(); cue = []; cur = []
    for x in w:
        if len(' '.join(cur + [x])) > maxc and cur: cue.append(' '.join(cur)); cur = []
        cur.append(x)
    if cur: cue.append(' '.join(cur))
    n = sum(len(c) for c in cue); out = []; t = t0
    for c in cue:
        d = (t1 - t0) * len(c) / n; out.append((t, t + d, c)); t += d
    return out

def due_righe(c):
    if len(c) <= 42: return c
    m = len(c) // 2; i = c.rfind(' ', 0, m + 8)
    return c[:i] + '\n' + c[i + 1:] if i > 0 else c

def vtt(timeline, out):
    st = {n: t for n, t, d in timeline}
    cues = []
    for pid, a, b, arg, states in prof.PEZZI:
        t0 = st['prof_' + pid]
        K = prof.intervalli(a, b); snap = lambda x: round(x * 30) / 30; KK = []
        for (s_, e_) in K:
            s_ = snap(s_); e_ = s_ + max(1, round((e_ - s_) * 30)) / 30; KK.append((s_, e_))
        cum = [0]
        for s_, e_ in KK: cum.append(cum[-1] + (e_ - s_))
        def f(x):
            for i, (s_, e_) in enumerate(KK):
                if x < s_: return cum[i]
                if x <= e_: return cum[i] + (x - s_)
            return cum[-1]
        for s in prof.SEG:
            if s['fine'] <= a or s['inizio'] >= b: continue
            txt = corr(s['testo'].strip())
            if not txt: continue
            for (c0, c1, c) in spezza(txt, t0 + f(max(s['inizio'], a)), t0 + f(min(s['fine'], b)) + 0.1): cues.append((c0, c1, c))
    # voci narranti
    def voce_cues(scena, nome_voce, units, v0, text_units):
        p, dur_v, stt, real = vinfo(nome_voce, units)
        for i, u in enumerate(text_units):
            t0 = st[scena] + v0 + stt[i]; t1 = st[scena] + v0 + (stt[i + 1] if i + 1 < len(stt) else dur_v)
            for c in spezza(unfix(u), t0, t1 - 0.05): cues.append(c)
    voce_cues('welcome', 'BENVENUTO', split_sent(BENVENUTO), 0.8, split_sent(BENVENUTO))
    for a, tit in ARGOMENTI:
        tu = split_sent(AP[a]); voce_cues(f'ap_{a}', f'{a}_APPROF', [voce(unfix(u)) for u in tu], 0.8, tu)
        voce_cues(f'rip_{a}', f'{a}_RIPASSO', [voce(u) for u in RIP[a]], 2.4, RIP[a])
    for k, nm, sc in (('MAP2', 'MAP2_STREETART', 'map2'), ('MAP3', 'MAP3_ARTISTAR_ARCHISTAR', 'map3'), ('MAP1', 'MAP1_FINALE', 'map1')):
        tu = split_sent(MAPV[k]); voce_cues(sc, nm, [voce(unfix(u)) for u in tu], 0.8, tu)
    gu = ['Il glossario della lezione.'] + [f"{t}. {d}" for t, d in GLOSS]; voce_cues('gloss', 'GLOSSARIO', [voce(u.replace('World Wide Web (WWW)', 'World Wide Web, in sigla WWW')) for u in gu], 1.0, gu)
    n = ['Primo', 'Secondo', 'Terzo', 'Quarto', 'Quinto', 'Sesto', 'Settimo']
    ru = ['Ripassiamo la lezione, argomento per argomento.'] + [f'{n[i]}: {t}, {d}' for i, (t, d) in enumerate(RF)]; voce_cues('rf', 'RIPASSO_FINALE', [voce(u) for u in ru], 1.0, ru)
    voce_cues('verifica', 'VERIFICA', [VER], 2.6, [VER])
    cu = [f'Compito {ORD[i]}. {t}' for i, t in enumerate(COMPITI)] + [COMPITI_FINALE]; voce_cues('compiti', 'COMPITI', [voce(u) for u in cu], 0.8, cu)
    cues.sort()
    with open(out, 'w') as fh:
        fh.write('WEBVTT\n\n')
        for i, (a, b, c) in enumerate(cues, 1):
            fh.write(f'{i}\n{ts(a)} --> {ts(max(b, a + 0.4))}\n{due_righe(c)}\n\n')
    return len(cues)
