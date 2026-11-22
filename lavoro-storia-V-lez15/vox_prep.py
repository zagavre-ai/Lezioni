# Prepara le voci Kore: taglia il silenzio in testa/coda, dissolvenze 30 ms, 48 kHz stereo, -16 LUFS; misura i bordi (ultimi 50 ms < 0,03)
import wave, numpy as np, sys, os, json, subprocess, glob
W = '/tmp/claude-0/l15'
def rd(f):
    w = wave.open(f); n = w.getnframes(); a = np.frombuffer(w.readframes(n), dtype=np.int16).astype(np.float32) / 32768
    a = a.reshape(-1, w.getnchannels()).mean(1); return a, w.getframerate()
def wr(f, a, sr):
    p = (np.clip(a, -1, 1) * 32767).astype(np.int16); st = np.repeat(p[:, None], 2, 1)
    w = wave.open(f, 'wb'); w.setnchannels(2); w.setsampwidth(2); w.setframerate(sr); w.writeframes(st.tobytes()); w.close()
def prep(nm, force=False):
    src = f'{W}/vox/{nm}.wav'; out = f'{W}/vox48/{nm}.wav'
    if os.path.exists(out) and not force and os.path.getmtime(out) > os.path.getmtime(src): return out
    a, sr = rd(src)
    m = np.abs(a); idx = np.where(m > 0.004)[0]
    i0 = max(0, idx[0] - int(0.10 * sr)); i1 = min(len(a), idx[-1] + int(0.18 * sr)); a = a[i0:i1]
    # dissolvenze 30 ms
    f = int(0.03 * sr); a = a.copy(); a[:f] *= np.linspace(0, 1, f); a[-f:] *= np.linspace(1, 0, f)
    tmp = f'{W}/vox48/_t_{nm}.wav'; os.makedirs(f'{W}/vox48', exist_ok=True); wr(tmp, a, sr)
    r = subprocess.run(['ffmpeg', '-v', 'error', '-y', '-i', tmp, '-af', 'loudnorm=I=-16:TP=-1.5:LRA=7,aresample=48000', '-ac', '2', '-c:a', 'pcm_s16le', out], capture_output=True, text=True)
    os.remove(tmp); return out
def bordi(f):
    a, sr = rd(f); n = int(0.05 * sr); return float(np.abs(a[-n:]).max()), float(np.abs(a[:n]).max()), len(a) / sr
if __name__ == '__main__':
    names = sys.argv[1:] or [os.path.basename(x)[:-4] for x in sorted(glob.glob(W + '/vox/*.wav'))]
    res = {}
    for nm in names:
        o = prep(nm); e, s, d = bordi(o); res[nm] = (round(e, 4), round(s, 4), round(d, 2))
    json.dump(res, open(W + '/vox48/_bordi.json', 'w')); bad = {k: v for k, v in res.items() if v[0] >= 0.03}
    print(len(res), 'voci; bordo finale >= 0,03:', bad)
