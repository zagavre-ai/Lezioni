import sys, json, subprocess, re, os
import numpy as np
sys.path.insert(0, '/home/user/w3/build')
N = sys.argv[1]; V = f'/home/user/w3/Storia_Lez3_Parte{N}_1080p.mp4'
TL = json.load(open(f'/home/user/w3/timeline_Parte{N}.json')); TG = json.load(open(f'/home/user/w3/tagli_Parte{N}.json'))
SR = 48000; out = []
def say(*a): s = ' '.join(str(x) for x in a); print(s, flush=True); out.append(s)
def sh(c): return subprocess.run(c, capture_output=True, text=True)
j = json.loads(sh(['ffprobe', '-v', 'error', '-count_packets', '-select_streams', 'v:0', '-show_entries', 'stream=nb_read_packets,width,height,r_frame_rate:format=duration,size', '-of', 'json', V]).stdout)
dur = float(j['format']['duration']); fr = int(j['streams'][0]['nb_read_packets']); mb = int(j['format']['size']) / 1e6
say(f"durata {int(dur//60)}:{dur%60:04.1f} ({dur:.2f} s) | fotogrammi {fr} (durata×30 = {round(dur*30)}) | peso {mb:.1f} MB | {j['streams'][0]['width']}x{j['streams'][0]['height']} {j['streams'][0]['r_frame_rate']}")
a = sh(['ffmpeg', '-v', 'info', '-i', V, '-af', 'ebur128=peak=true:framelog=quiet,silencedetect=n=-45dB:d=2.5', '-f', 'null', '-']).stderr
m = re.findall(r'I:\s+(-?[\d.]+) LUFS', a); tp = re.findall(r'Peak:\s+(-?[\d.]+) dBFS', a)
say(f"loudness {m[-1] if m else '?'} LUFS | picco vero {tp[-1] if tp else '?'} dBTP | pause oltre 2,5 s (< -45 dB): {len(re.findall('silence_end', a))}")
# audio finale
x = np.frombuffer(subprocess.run(['ffmpeg', '-v', 'error', '-i', V, '-vn', '-ac', '1', '-ar', str(SR), '-f', 'f32le', '-'], capture_output=True).stdout, np.float32)
o = np.load('/home/user/w3/orig/clean_nr6.npy')
oo = np.frombuffer(subprocess.run(['ffmpeg', '-v', 'error', '-i', '/home/user/w3/orig/lez3.mp4', '-vn', '-ac', '1', '-ar', str(SR), '-f', 'f32le', '-'], capture_output=True).stdout, np.float32)
def metric(y):
    w = 8192; f = np.fft.rfftfreq(w, 1 / SR); hi = lo = 0
    for i in range(0, len(y) - w, w * 2):
        s = y[i:i + w] * np.hanning(w)
        if np.sqrt(np.mean(s ** 2)) < 0.01: continue
        P = np.abs(np.fft.rfft(s)) ** 2; hi += P[f > 4000].sum(); lo += P[f > 100].sum()
    return 10 * np.log10(hi / lo)
S_ = json.load(open('/home/user/w3/orig/trasc.json')); fin = []; ori = []; lags = []
for nm, src, lw, st, d in TG:
    s0 = int(st * SR); fin.append(x[s0 + int(0.8 * SR): s0 + int(d * SR) - int(0.8 * SR)])
    a0, b0 = src; ori.append(oo[int(a0 * SR) + int(0.8 * SR): int(b0 * SR) - int(0.8 * SR)] if b0 - a0 > 2 else np.zeros(1))
    # scarto audio rispetto alla sorgente: correlazione su 6 s dell'inizio parlato
    ia = [i for i, z in enumerate(S_) if abs(z['inizio'] - a0) < 1e-6]
    if ia:
        i0 = ia[0]; gb = S_[i0]['inizio'] - (S_[i0 - 1]['fine'] if i0 > 0 else S_[i0]['inizio'] - 1.0); ph = max(0.2, min(0.7, gb - 0.12))
        t0 = st + ph + 0.3; seg = x[int(t0 * SR): int((t0 + 6) * SR)]
        ref = o[int((a0 + 0.3) * SR): int((a0 + 6.3) * SR)]
        env = lambda y: np.convolve(np.abs(y), np.ones(48) / 48, 'same')[::48]
        ca = env(seg); cb = env(ref); n_ = min(len(ca), len(cb)); ca = ca[:n_]; cb = cb[:n_]
        cc = np.correlate(ca - ca.mean(), cb - cb.mean(), 'full'); lag = (np.argmax(cc) - (n_ - 1)) * 48 / SR
        lags.append((nm, lag))
F = np.concatenate(fin); O = np.concatenate([z for z in ori if len(z) > 10])
say(f"timbre (acuti >4 kHz meno >100 Hz): originale {metric(O):.1f} dB | finale {metric(F):.1f} dB (deve stare tra -9 e -20)")
say('scarto del parlato finale rispetto alla sorgente (s), inviluppo su 6 s, atteso 0: ' + ', '.join(f'{n} {l:+.3f}' for n, l in lags[:40]))
say('Q: scheda e scatto atteso:'); 
q = np.frombuffer(subprocess.run(['ffmpeg', '-v', 'error', '-i', '/home/user/Lezioni/kit/suoni/quiz.wav', '-ac', '1', '-ar', '8000', '-f', 's16le', '-'], capture_output=True).stdout, np.int16).astype(float)[:16000]
for nm, t, l in TL:
    if re.fullmatch(r'Q\d+|VF', nm):
        s = t - 1.5; y = np.frombuffer(subprocess.run(['ffmpeg', '-v', 'error', '-ss', str(s), '-t', '5', '-i', V, '-ac', '1', '-ar', '8000', '-f', 's16le', '-'], capture_output=True).stdout, np.int16).astype(float)
        k = int(np.argmax(np.correlate(y, q, 'valid'))); say(f"  {nm} atteso {t+0.5:.3f} trovato {s+k/8000:.3f} scarto {s+k/8000-(t+0.5):+.3f}")
say('tagli del prof (fine di ogni pezzo):')
say('| pezzo | minuto fine | ultime parole (trascrizione) | frase finita |'); say('|---|---|---|---|')
for nm, src, lw, st, d in TG:
    e = st + d; fin_ok = 'sì' if re.search(r'[.?!…]["»]?$', (lw or '').strip()) else 'da verificare'
    say(f"| {nm} | {int(e//60)}:{e%60:04.1f} | …{lw} | {fin_ok} |")
open(f'/home/user/w3/verifica_Parte{N}.txt', 'w').write('\n'.join(out))
