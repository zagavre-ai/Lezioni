# Scarto audio finale vs originale del docente per ogni pezzo D* (correlazione sui primi 20 s): atteso 0,00 s (±0,04)
import sys, json, subprocess, numpy as np
sys.path.insert(0, '/home/user/Lezioni/lez12')
import piano as PI
V, TL = sys.argv[1], sys.argv[2]; SR = 8000
def rd(f, ss, d):
    return np.frombuffer(subprocess.run(['ffmpeg', '-v', 'error', '-ss', str(ss), '-t', str(d), '-i', f, '-vn', '-ac', '1', '-ar', str(SR), '-f', 's16le', '-'], capture_output=True).stdout, np.int16).astype(float)
O = '/home/user/Lezioni/lavoro/in/video/LEZIONE 12 DADAISMO E SURREALISMO.mp4'
start = {n: t for n, t, d in json.load(open(TL))}; out = []
for pid, a, t0, t1, st in PI.P:
    S0 = start[pid] + 0.35 + 0.15  # = istante del video dove cade t0 (inizio frase)
    for off in (5.0, 60.0):
        if t0 + off + 15 > t1: continue
        x = rd(V, S0 + off, 15); y = rd(O, t0 + off, 15)
        x = np.abs(x); y = np.abs(y); n = min(len(x), len(y))
        # inviluppo
        k = np.ones(80) / 80; x = np.convolve(x[:n], k, 'same'); y = np.convolve(y[:n], k, 'same')
        c = np.correlate(x - x.mean(), y - y.mean(), 'full'); lag = (np.argmax(c) - (n - 1)) / SR
        out.append((pid, off, round(lag, 3)))
print(out); print('max |scarto| =', max(abs(l) for _, _, l in out))
