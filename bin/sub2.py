# Sottotitoli .vtt dal video FINALE sui pezzi D* (Whisper base sherpa-onnx, tagli nelle pause, parole distribuite nel pezzo)
# uso: python3 sub2.py video.mp4 timeline.json uscita.vtt fix.json
import sys, json, subprocess, re, numpy as np, sherpa_onnx
V, TL, OUT, FX = sys.argv[1:5]
FIX = json.load(open(FX)); tl = json.load(open(TL)); sr = 16000
segs = [(t, t + l) for n, t, l in tl if re.fullmatch(r'D\d+', n) and l > 1.0]
x = np.frombuffer(subprocess.run(['ffmpeg', '-v', 'error', '-i', V, '-vn', '-ac', '1', '-ar', '16000', '-f', 'f32le', '-'], capture_output=True).stdout, np.float32)
D = '/tmp/whisper/whisper-base/'
rec = sherpa_onnx.OfflineRecognizer.from_whisper(encoder=D+'base-encoder.int8.onnx', decoder=D+'base-decoder.int8.onnx', tokens=D+'base-tokens.txt', language='it', task='transcribe', num_threads=4)
h = int(0.05 * sr); W = []
def chunks(a, b):
    y = x[int(a*sr):int(b*sr)]; e = np.array([float((y[i:i+h]**2).mean()) for i in range(0, len(y)-h, h)])
    cuts = [0]
    while (len(e) - cuts[-1]) * 0.05 > 9.0:
        lo = cuts[-1] + int(3.0/0.05); hi = cuts[-1] + int(8.0/0.05); cuts.append(lo + int(np.argmin(e[lo:hi])))
    cuts.append(len(e)); return [(a + cuts[i]*0.05, a + cuts[i+1]*0.05) for i in range(len(cuts)-1)]
for s0, s1 in segs:
    for a, b in chunks(s0, s1):
        st = rec.create_stream(); st.accept_waveform(sr, x[int(a*sr):int(b*sr)]); rec.decode_stream(st)
        ws = st.result.text.split()
        if not ws: continue
        # stima del parlato effettivo nel pezzo: tra primo e ultimo istante sopra soglia
        y = x[int(a*sr):int(b*sr)]; en = np.array([float((y[i:i+h]**2).mean()) for i in range(0, len(y)-h, h)]); thr = np.percentile(en, 40)
        idx = np.where(en > thr)[0]; t0 = a + (idx[0]*0.05 if len(idx) else 0); t1 = a + ((idx[-1]+1)*0.05 if len(idx) else b-a)
        dd = (t1 - t0) / len(ws)
        for k, w in enumerate(ws): W.append([t0 + k*dd, t0 + (k+1)*dd, ' ' + w])
B = []; cur = []
for w in W:
    if cur and (w[0] - cur[-1][1] > 0.5 or len(''.join(q[2] for q in cur + [w])) > 84 or w[1] - cur[0][0] > 6): B.append(cur); cur = []
    cur.append(w)
    if re.search(r'[.?!]$', w[2].strip()) and w[1] - cur[0][0] >= 1: B.append(cur); cur = []
if cur: B.append(cur)
def ts(t): return '%02d:%02d:%06.3f' % (t//3600, t % 3600//60, t % 60)
def wrap(s):
    if len(s) <= 42: return s
    k = s.rfind(' ', 0, len(s)//2 + 8); return s[:k] + '\n' + s[k+1:]
L = ['WEBVTT', '']; prev = 0
for b in B:
    tx = ''.join(q[2] for q in b).strip(); tx = re.sub(r'\s+', ' ', tx)
    for p, r in FIX: tx = re.sub(p, r, tx)
    t0 = max(b[0][0], prev + 0.01); t1 = max(b[-1][1], t0 + 1.0)
    L += [f'{ts(t0)} --> {ts(t1)}', wrap(tx), '']; prev = t1
open(OUT, 'w').write('\n'.join(L)); print('blocchi', len(B))
