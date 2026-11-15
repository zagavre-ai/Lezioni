# Voci Kore ricevute -> voci/wav/NOME.wav (48 kHz stereo) + meta con l'inizio di ogni frase (aggancio alle pause, senza riconoscimento)
# uso: importa2.py NN   (legge voci/kore/NOME.wav e voci/testi_voci.json)
import sys, os, json, subprocess, numpy as np
NN = sys.argv[1]; D = f'/home/claude/w/l{NN}/voci/'; TV = json.load(open(D + 'testi_voci.json')); os.makedirs(D + 'wav', exist_ok=True)
for k, fr in TV.items():
    src = D + f'kore/{k}.wav'
    if not os.path.exists(src): print('manca', k); continue
    out = D + f'wav/{k}.wav'
    subprocess.run(['ffmpeg', '-y', '-v', 'error', '-i', src, '-ac', '2', '-ar', '48000', out], check=True)
    x = np.frombuffer(subprocess.run(['ffmpeg', '-v', 'error', '-i', src, '-ac', '1', '-ar', '16000', '-f', 'f32le', '-'], capture_output=True).stdout, np.float32)
    sr = 16000; h = int(0.02 * sr); e = np.array([float((x[i:i+h]**2).mean()) for i in range(0, len(x)-h, h)]); d = len(x) / sr
    thr = max(np.percentile(e, 20) * 4, 1e-7); quiet = e < thr
    # pause >= 0,22 s: punto di ripartenza = fine della pausa
    cand = []; i = 0
    while i < len(quiet):
        if quiet[i]:
            j = i
            while j < len(quiet) and quiet[j]: j += 1
            if (j - i) * 0.02 >= 0.22 and 0.3 < j * 0.02 < d - 0.3: cand.append(j * 0.02)
            i = j
        else: i += 1
    ch = [len(s) for s in fr]; tot = sum(ch); cum = 0; P = [0.0]
    for c in ch[:-1]:
        cum += c; tgt = cum / tot * d
        near = min(cand, key=lambda t: abs(t - tgt)) if cand else tgt
        P.append(round(max(near - 0.15, P[-1] + 0.5), 2))
    json.dump({'phrases': P, 'dur': round(d, 2), 'vera': True}, open(D + f'wav/meta_{k}.json', 'w'))
    print(k, round(d, 1), 's frasi', P)
