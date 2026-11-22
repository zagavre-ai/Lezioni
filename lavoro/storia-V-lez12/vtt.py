# -*- coding: utf-8 -*-
# Sottotitoli .vtt dal video finale: prof (trascrizione con tempi, termini corretti) + voci Kore (testo noto, tempi per frase).
import json, re, sys, textwrap
sys.path.insert(0, '/home/user/Lezioni/lavoro/storia-V-lez12')
import voce, contenuti as C
W = '/home/user/w12'
ASR = json.load(open(f'{W}/trascr.json'))
def parole_intere(seg):
    out = []
    for t, w in (seg.get('parole') or []):
        if w.startswith(' ') or not out: out.append([t, w.strip()])
        else: out[-1][1] += w
    return [(t, w) for t, w in out if w]
for _s in ASR: _s['parole'] = parole_intere(_s)
CORR = [(r'\b(Moslim|Mosli|Mosle\w*|Moseley)\b', 'Mosley'), (r'\b[Pp]e?a?s[ei]?ment\w*|\b[Pp]iscant\w*|\b[Pp]isment\w*', 'appeasement'), (r'\b(Mc ?Donald|McDonald)\b', 'MacDonald'),
        (r'\b[Pp]izzski|\b[Pp]ilsudski\b', 'Piłsudski'), (r'\bItler\w*', 'Hitler'), (r'\b[Gg]uernica\b|\b[Gg]ernica\b', 'Guernica'), (r'\bGoming ?[Dd]an\b', 'Guomindang'),
        (r'\bAnchul?us\b|\bAnschl?us\w*', 'Anschluss'), (r'\bFjurer\b', 'Führer'), (r'\bPatto d.?acciaio\b', "Patto d'acciaio"), (r'\bMolotov[ -]?[Rr]i?b+e?ntrop\b', 'Molotov-Ribbentrop'),
        (r'\bLebensraum\b|\bebesraum\b', 'Lebensraum'), (r'\bmuss?olini\w*|\bmusuliniana\b', 'Mussolini'), (r'\bWeist Mister\b|\bWestminster\b', 'Westminster'), (r'\bBlum\b|\bBlun\b', 'Blum')]
def pulisci(t):
    for a, b in CORR: t = re.sub(a, b, t)
    return t
def ts(t):
    h = int(t // 3600); m = int(t % 3600 // 60); s = t % 60
    return '%02d:%02d:%06.3f' % (h, m, s)
def cues_da_parole(par):  # par = [(t_video, parola)]
    out = []; cur = []; 
    def flush():
        if not cur: return
        txt = ' '.join(w for _, w in cur); txt = pulisci(re.sub(r'\s+([,.;:?!])', r'\1', txt))
        righe = textwrap.wrap(txt, 42)
        out.append((cur[0][0], cur[-1][0] + 0.5, '\n'.join(righe[:2]) if len(righe) <= 2 else '\n'.join(righe[:2]) + '\n' + '\n'.join(righe[2:])))
        cur.clear()
    for i, (t, w) in enumerate(par):
        if cur and (t - cur[0][0] > 5.0 or len(' '.join(x for _, x in cur)) + len(w) > 80 or (t - cur[-1][0] > 0.7) or re.search(r'[.?!]$', cur[-1][1])): flush()
        cur.append((t, w))
    flush()
    # evita sovrapposizioni
    for i in range(len(out) - 1):
        if out[i][1] > out[i + 1][0]: out[i] = (out[i][0], out[i + 1][0] - 0.02, out[i][2])
    return out
VOCI_PEZZO = {'cover_ben': ('I1_BENVENUTO', .6), 'cover_ben2': ('I3_BENVENUTO2', .6), 'argomenti': ('I2_ARGOMENTI', .6), 'spiegone': ('S1_SPIEGONE', .8), 'glossario': ('G1_GLOSSARIO', 1.3),
              'ripasso': ('R1_RIPASSO_FINALE', 1.3), 'mappe_fin': ('F1_MAPPE_FINALE', .8), 'verifica': ('V1_VERIFICA', 1.2), 'compiti': ('C2_COMPITI', .8)}
for k in range(1, 7): VOCI_PEZZO.update({f'app{k}': (f'A{k}_APPROF', .8), f'pil{k}': (f'P{k}_PILLOLA', 1.3), f'mappa{k}': (f'M{k}_MAPPA', .8)})
def vtt(n, out):
    tl = json.load(open(f'{W}/asm{n}/timeline.json'))['pezzi']; cues = []
    for nome, t0, d, fr in tl:
        if nome.startswith('prof'):
            j = json.load(open(f'{W}/pezzi/{nome}.json')); rng = j['intervalli']; off = 0.0; par = []
            for a, b in rng:
                for s in ASR:
                    for tt, w in (s.get('parole') or []):
                        if a - 0.02 <= tt < b: par.append((t0 + off + (tt - a), w.strip()))
                off += b - a
            cues += cues_da_parole([p for p in par if p[1]])
        elif nome in VOCI_PEZZO:
            vn, o = VOCI_PEZZO[nome]
            if vn not in C.VOCI: continue
            v = voce.get(vn)
            for fr_, (a, b) in zip(v['frasi'], v['tempi']):
                par = []; ws = fr_.split()
                if not ws: continue
                for i, w in enumerate(ws): par.append((t0 + o + a + (b - a) * i / len(ws), w))
                cues += cues_da_parole(par)
    cues.sort()
    with open(out, 'w', encoding='utf8') as f:
        f.write('WEBVTT\n\n')
        for i, (a, b, t) in enumerate(cues, 1): f.write(f'{i}\n{ts(a)} --> {ts(b)}\n{t}\n\n')
    return len(cues)
if __name__ == '__main__':
    for n in (1, 2): print(n, vtt(n, f'{W}/consegna/Storia_Lez12_Parte{n}.vtt'))
