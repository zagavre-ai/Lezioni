# Sottotitoli .vtt sul video finale: prof = trascrizione automatica con i termini corretti dal materiale della lezione; voci Kore = testo della voce
import re, json, sys, os
sys.path.insert(0, '/tmp/w/build')
import timing, content as K
from pieces import VOCI, sentences

FIX = [  # (espressione, sostituzione) applicate in ordine, senza distinguere maiuscole
 (r"\b(l['’]\s?)?\b(?:art|ar|h)[\s-]?n(?:ou|uo|u)(?:veau|vo|va|bo|x|vou)\b", lambda m: (m.group(1) or '') + 'Art Nouveau'),
 (r"\bla nuvo\b", "l'Art Nouveau"), (r"\bl['’]arriva anche\b", "L'Art Nouveau arriva anche"), (r"\bArnoux\b", "Art Nouveau"), (r"\bl['’]?Ar\b", "l'Art"), (r"\bnuova italiana\b", 'Liberty italiana'),
 (r"\bAudien Redon\b", "Odilon Redon"), (r"\bMorau\b", "Moreau"), (r"\bPierre Pouvis de Chavalnet\b|\bPouvis de Chavalnet\b", "Pierre Puvis de Chavannes"),
 (r"\bNabi\b", "Nabis"), (r"\bPaul Servusier\b", "Paul Sérusier"), (r"\bHto Guimar\b|\bEctogima\b", "Hector Guimard"), (r"\bGuimar\b", "Guimard"),
 (r"\bYoris Carl Guismans\b", "Joris-Karl Huysmans"), (r"\bChar Boder\b", "Charles Baudelaire"), (r"\bPaul Verlin\b", "Paul Verlaine"), (r"\bVerlain\b|\bVerlin\b", "Verlaine"), (r"\bMarlamme\b|\bMarlarmé\b", "Mallarmé"),
 (r"\bSulivan\b|\bSalvan\b", "Sullivan"), (r"\bChikego\b", "Chicago"), (r"\bLewis Henry\b", "Louis Henry"), (r"\bgattocello di Sullivan\b", "grattacielo di Sullivan"), (r"\bGuarantee\b", "Guaranty"),
 (r"\bGustave Klimt\b|\bGustav Klimft\b|\bGustav Klim\b|\bGustav Grim\b|\bKlimft\b", "Gustav Klimt"), (r"\bClimate Torna\b", "Klimt"), (r"\bClint\b|\bClinton\b|\bClimt\b", "Klimt"),
 (r"\bStocklet\b|\bStocket\b", "Stoclet"), (r"\bHoffman\b|\bHofman\b", "Hoffmann"), (r"\bCola Man Moser\b", "Koloman Moser"), (r"\bHolbrich\b", "Olbrich"),
 (r"\bout of l['’]ose\b", "Adolf Loos"), (r"\bl['’]ose\b", "Loos"), (r"\blo usa anticipa\b", "Loos anticipa"),
 (r"\bAubrey Bursley\b|\bBursley\b", "Aubrey Beardsley"), (r"\bCharles Rainey McIntosh\b", "Charles Rennie Mackintosh"), (r"\bMcIntosh\b|\bMacintosh\b", "Mackintosh"),
 (r"\bAnthony Gaudí\b|\bAntonio Gaudi\b", "Antoni Gaudí"), (r"\bCaudi\b|\bGaudì\b|\bGaudi\b", "Gaudí"), (r"\bCasa Batloau\b|\bCasa Batlloau\b|\bCasa but\b", "Casa Batlló"), (r"\bcasa mia\b", "Casa Milà"), (r"\bSagrada Famiglia\b", "Sagrada Família"),
 (r"\bFernandes\b", "Fernand Khnopff"), (r"\bEmil Galletti\b", "Émile Gallé"), (r"\bEmil Tassé\b", "Émile Tassel"), (r"\bTano previati\b", "Gaetano Previati"), (r"\boggetto Sommaruga\b", "Giuseppe Sommaruga"),
 (r"\bEmil Flogging\b", "Emilie Flöge"), (r"\bLoferne\b", "Oloferne"), (r"\bLambra di Granada\b", "Alhambra di Granada"), (r"\bUno ditta prima\b", "Giuditta I"), (r"\bFant Fatale\b|\bFan fatale\b", "femme fatale"),
 (r"\bArsenc Society\b", "Arts and Crafts Society"), (r"\bAs and Craft\b", "Arts and Crafts"), (r"\bBursel\b", "Bruxelles"), (r"\bL['’]art Modern\b", "L'Art moderne"), (r"\bmillenovue\b", "millenovecentodue"),
 (r"\bEt l['’]", "E l'"), (r"\bsimbolic,", "Simbolismo,"),
]
DROP = re.compile(r"^(um|yeah|mm-hmm|uh um|uh|again that\.?|the|exemplo\.?|mm|uh ma|uh-huh|ma\.?)\W*$", re.I)

def fix(t):
    for a, b in FIX: t = re.sub(a, b, t, flags=re.I)
    return t

def vtt_time(t):
    h = int(t // 3600); m = int(t % 3600 // 60); s = t % 60
    return '%02d:%02d:%06.3f' % (h, m, s)

def chunks(text, maxc=78):
    words = text.split(); out = []; cur = ''
    for w in words:
        if cur and len(cur) + 1 + len(w) > maxc: out.append(cur); cur = w
        else: cur = (cur + ' ' + w).strip()
    if cur: out.append(cur)
    return out

def asr_segments():
    A = json.load(open('/tmp/w/trasc.json')); T = json.load(open('/tmp/w/tail.json'))
    S = [s for s in A if s['inizio'] < 2425]
    for s in T:
        if s['inizio'] + 2425 >= 2425: s = dict(s); s['inizio'] += 2425; s['fine'] += 2425; s['parole'] = [[t + 2425, w] for t, w in s['parole']]; S.append(s)
    return S

def teacher_cues(c0, c1, start):
    cues = []
    for s in asr_segments():
        if s['inizio'] < c0 - 0.05 or s['inizio'] >= c1: continue
        txt = s['testo'].strip()
        if DROP.match(txt): continue
        txt = fix(txt); txt = txt[0].upper() + txt[1:] if txt else txt
        ch = chunks(txt); a = s['inizio']; b = min(s['fine'], c1)
        if len(ch) == 1: cues.append((a - c0 + start, b - c0 + start, ch[0])); continue
        tot = sum(len(c) for c in ch); t = a
        for c in ch:
            d = (b - a) * len(c) / tot; cues.append((t - c0 + start, t + d - c0 + start, c)); t += d
    return cues

def voice_cues(vname, lead, start):
    S = sentences(VOCI[vname]); blocks = []
    for s in S: blocks += chunks(s)
    W = timing.wav_words(vname, VOCI[vname]); tm = timing.align(blocks, W)
    return [(lead + a + start, lead + b + start, t) for (a, b), t in zip(tm, blocks)]

VOICE_OF = {'COVER': ('B0_BENVENUTO', 0.8), 'GLOSS': ('G_GLOSSARIO', 0.8), 'RIEPILOGO': ('F_RIPASSO_FINALE', 1.6), 'VERIFICA': ('V_VERIFICA', 2.0), 'COMPITI': ('COMPITI', 0.8),
            'MAPPA_M1': ('M1_MAPPA', None), 'MAPPA_M2': ('M2_MAPPA', None)}
for i in range(1, 6): VOICE_OF[f'APP{i}'] = (f'A{i}_APPROF', 0.8); VOICE_OF[f'RIP{i}'] = (f'R{i}_RIPASSO', 1.6)

def build(timeline, order, out_vtt, map_leads):
    cues = []
    for (tn, start, dur), pn in zip(timeline, order):
        if pn in ('INTRO_A', 'INTRO_B'): c0, c1 = (0.3, 122.6) if pn == 'INTRO_A' else (122.35, 254.15); cues += teacher_cues(c0, c1, start)
        elif pn in K.PEZZI_PROF: P = K.PEZZI_PROF[pn]; cues += teacher_cues(P['c0'], P['c1'], start)
        elif pn in VOICE_OF:
            v, lead = VOICE_OF[pn]
            if lead is None: lead = map_leads.get(pn, 0.5)
            cues += voice_cues(v, lead, start)
    cues.sort()
    # evita sovrapposizioni
    out = ['WEBVTT', '']
    for i, (a, b, t) in enumerate(cues):
        if i + 1 < len(cues): b = min(b, cues[i + 1][0] - 0.02)
        if b - a < 0.4: b = a + 0.4
        out += [vtt_time(a) + ' --> ' + vtt_time(b), t, '']
    open(out_vtt, 'w').write('\n'.join(out))
    return len(cues)
