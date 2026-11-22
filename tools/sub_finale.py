# Sottotitoli del video FINALE, solo sulla voce del docente (segmenti D* della timeline).
# uso: python3 sub_finale.py video_finale.mp4 timeline.json uscita.vtt
# 1) trascrive con Parakeet solo i tratti del docente, già nei tempi del video finale
# 2) blocchi da max 2 righe x 42 caratteri, 1-6 s, spezzati sulle pause e sulla punteggiatura
# 3) inizio di ogni blocco agganciato all'attacco reale della voce (energia) entro -0,6/+0,2 s
import sys, json, subprocess, os, numpy as np
sys.path.insert(0, '/home/claude/asr_pk'); import pk
V, TL, OUT = sys.argv[1], sys.argv[2], sys.argv[3]
wav = OUT + '.16k.wav'
if not os.path.exists(wav):
    subprocess.run(['ffmpeg', '-v', 'error', '-y', '-i', V, '-vn', '-ac', '1', '-ar', '16000', wav], check=True)
x = pk.load(wav); sr = 16000
tl = json.load(open(TL))
segs = [(t, t + l) for n, t, l in tl if n.startswith('D') and l > 1.0]
cache = OUT + '.words.json'
W = json.load(open(cache)) if os.path.exists(cache) else []
done = {round(w[2], 2) for w in W}
e = np.convolve(x ** 2, np.ones(1600) / 1600, 'same')
for a, b in segs:
    if round(a, 2) in done: continue
    t = a
    while t < b - 0.2:
        c = min(b, t + 24.0)
        if c < b:
            i0 = int((c - 4) * sr); i1 = int(c * sr); c = (i0 + int(np.argmin(e[i0:i1:160])) * 160) / sr
        seg = x[int(t * sr):int(c * sr)]
        if np.abs(seg).max() > 0.01:
            for tt, w in pk.words(pk.transcribe(seg, t)):
                if a <= tt < b: W.append([tt, w, a, b])
        t = c
    json.dump(W, open(cache, 'w'), ensure_ascii=False)
    print('segmento', round(a, 1), round(b, 1), 'parole', len(W), flush=True)
W.sort()
# attacco reale della voce: primo punto, prima della parola, in cui l'energia sale dopo un tratto basso
db = 10 * np.log10(np.convolve(x ** 2, np.ones(480) / 480, 'same')[::160] + 1e-10)  # 10 ms
def onset(t, lo):
    i0 = max(int((t - 0.6) * 100), int(lo * 100)); i1 = int((t + 0.2) * 100)
    if i1 <= i0 + 2: return t
    seg = db[i0:i1]; thr = np.median(db[max(0, i0 - 300):i1]) - 6
    k = [j for j in range(1, len(seg)) if seg[j] > -45 and seg[j - 1] <= -45]
    return (i0 + k[-1]) / 100 if k else t
cues = []; cur = []
def flush():
    global cur
    if not cur: return
    txt = ' '.join(w for _, w, _, _ in cur)
    s = cur[0][0]; en = cur[-1][0] + 0.45
    cues.append([s, en, txt, cur[0][2]]); cur = []
for k, (t, w, a, b) in enumerate(W):
    if cur:
        gap = t - cur[-1][0]
        txt = ' '.join(z for _, z, _, _ in cur) + ' ' + w
        if gap > 1.3 or len(txt) > 78 or t - cur[0][0] > 6 or cur[-1][2] != a or (cur[-1][1][-1:] in '.?!' and len(txt) > 30):
            flush()
    cur.append([t, w, a, b])
flush()
# unisce i blocchi troppo corti (una o due parole) al successivo, se vicino
m = []
for c in cues:
    if m and len(m[-1][2]) < 22 and c[0] - m[-1][1] < 1.6 and c[3] == m[-1][3] and len(m[-1][2]) + len(c[2]) < 78 and c[1] - m[-1][0] < 7:
        m[-1] = [m[-1][0], c[1], m[-1][2] + ' ' + c[2], c[3]]
    else:
        m.append(c)
cues = m
# tempi: inizio agganciato all'attacco, durata 1-6 s, niente sovrapposizioni, mai oltre il segmento del docente
segend = {a: b for a, b in segs}
for i, c in enumerate(cues):
    lo = cues[i - 1][1] if i else 0
    c[0] = max(lo, onset(c[0], max(lo, c[3])))
for i, c in enumerate(cues):
    nxt = cues[i + 1][0] if i + 1 < len(cues) else 1e9
    c[1] = min(max(c[1], c[0] + 1.0), c[0] + 6.0, nxt - 0.05, segend[c[3]])
def wrap(t):
    if len(t) <= 42: return t
    ws = t.split(); best = None
    for k in range(1, len(ws)):
        l1 = ' '.join(ws[:k]); l2 = ' '.join(ws[k:])
        if len(l1) <= 44 and len(l2) <= 44:
            sc = abs(len(l1) - len(l2))
            if best is None or sc < best[0]: best = (sc, l1 + '\n' + l2)
    return best[1] if best else t
def ts(t):
    h = int(t // 3600); m = int(t % 3600 // 60); s = t % 60
    return '%02d:%02d:%06.3f' % (h, m, s)
with open(OUT, 'w', encoding='utf-8') as o:
    o.write('WEBVTT\n\n')
    for i, (a, b, t, _) in enumerate(cues, 1):
        o.write('%d\n%s --> %s\n%s\n\n' % (i, ts(a), ts(b), wrap(t)))
print('blocchi', len(cues), '->', OUT)
