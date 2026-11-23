# Sottotitoli .vtt sul video finale: docente = trascrizione corretta (tempi originali -> tempi finali); schede Kore = testo delle voci.
import sys, json, re, textwrap
sys.path.insert(0, '/home/user/Lezioni/lez12')
import piano as PI
from voci import VOCI
W = '/home/user/Lezioni/lavoro/'
LEAD, PRE = 0.35, 0.15
NUM = {'millenovecentosedici': '1916', 'millenovecentotredici': '1913', 'millenovecentoventiquattro': '1924', 'millenovecentotrentasette': '1937'}
def disp(t):
    for k, v in NUM.items(): t = t.replace(k, v)
    return re.sub(r'\s+', ' ', t.replace('«', '“').replace('»', '”')).strip()
def ts(t):
    h, r = divmod(t, 3600); m, r = divmod(r, 60); return '%02d:%02d:%06.3f' % (h, m, r)
def split(text, maxc=84):
    """pezzi <= maxc caratteri, spezzati su punteggiatura/parole"""
    if len(text) <= maxc: return [text]
    parts = re.split(r'(?<=[.;:!?,])\s+', text); out = []; cur = ''
    for p in parts:
        if len(cur) + len(p) + 1 <= maxc: cur = (cur + ' ' + p).strip()
        else:
            if cur: out.append(cur)
            if len(p) > maxc:
                w = p.split(); cur = ''
                for x in w:
                    if len(cur) + len(x) + 1 <= maxc: cur = (cur + ' ' + x).strip()
                    else: out.append(cur); cur = x
            else: cur = p
    if cur: out.append(cur)
    return out
def cue(a, b, text):
    L = textwrap.wrap(text, 42) or ['']
    if len(L) > 2: L = [' '.join(L[:len(L) // 2 + len(L) % 2]), ' '.join(L[len(L) // 2 + len(L) % 2:])]
    return f'{ts(a)} --> {ts(b)}\n' + '\n'.join(L) + '\n'
def main(tl_path, out):
    tl = json.load(open(tl_path)); start = {n: t for n, t, d in tl}; dur = {n: d for n, t, d in tl}
    segs = json.load(open(W + 'trascr.json')); corr = {}
    try: corr = {x['i']: x['testo'] for x in json.load(open(W + 'trascr_corretta.json'))['segmenti']}
    except Exception: print('ATTENZIONE: trascrizione corretta non trovata, uso la grezza')
    meta = json.load(open(W + 'build/meta.json')); cues = []
    for pid, a, t0, t1, st in PI.P:
        S0 = start[pid]; t0p = t0 - PRE
        for i, s in enumerate(segs):
            if s['inizio'] < t0 - 0.25 or s['fine'] > t1 + 0.4: continue
            tx = disp(corr.get(i, s['testo']))
            if not tx: continue
            a0 = S0 + LEAD + (s['inizio'] - t0p); b0 = S0 + LEAD + (s['fine'] - t0p)
            ps = split(tx); n = sum(len(p) for p in ps); c = a0
            for p in ps:
                d = (b0 - a0) * len(p) / n; cues.append((c, c + d, p)); c += d
    for name, m in list(meta.items()):
        if name == 'MAPPA':
            for v, mm in m.items():
                S0 = start['MAPPA']; txt = disp(VOCI[v]); a0 = S0 + mm['v0']; b0 = a0 + mm['ve'] - mm['vs']
                cues.append((a0, b0, txt))
            continue
        if name not in start: continue
        txt = disp(VOCI[m['voice']]); a0 = start[name] + m['v0']; b0 = a0 + m['ve'] - m['vs']
        sents = [x for x in re.split(r'(?<=[.!?])\s+', txt) if x]; n = sum(len(x) for x in sents); c = a0
        for sn in sents:
            d = (b0 - a0) * len(sn) / n
            ps = split(sn); nn = sum(len(p) for p in ps); cc = c
            for p in ps: dd = d * len(p) / nn; cues.append((cc, cc + dd, p)); cc += dd
            c += d
    cues.sort()
    # niente sovrapposizioni
    fixed = []
    for i, (a, b, t) in enumerate(cues):
        if i + 1 < len(cues) and b > cues[i + 1][0]: b = cues[i + 1][0] - 0.01
        if b - a >= 0.3: fixed.append((a, b, t))
    open(out, 'w').write('WEBVTT\n\n' + '\n'.join(cue(a, b, t) for a, b, t in fixed))
    print(len(fixed), 'sottotitoli')
if __name__ == '__main__': main(sys.argv[1], sys.argv[2])
