# Trascrizione italiana con i tempi, SENZA HuggingFace (bloccato nelle sessioni): modelli scaricati da GitHub.
# Motore: sherpa-onnx + Parakeet TDT 0.6b v3 (multilingue, italiano compreso) + VAD Silero. Tempi parola per parola.
# uso:   python3 kit/tools/trascrivi.py VIDEO_O_AUDIO [uscita_senza_estensione]
# esce:  <uscita>.json  (segmenti: inizio, fine, testo, parole[[t,parola]])  e  <uscita>.srt
# Prima volta: pip install sherpa-onnx --break-system-packages   (lo fa da solo se manca)
# Velocità misurata (16/11): 90 s di audio in 14 s su 2 CPU, cioè 1 ora di audio ≈ 9-10 minuti.
import os, sys, json, subprocess, tarfile, urllib.request
D = os.environ.get('TELESIO_ASR', '/tmp/asr')
U = 'https://github.com/k2-fsa/sherpa-onnx/releases/download/asr-models/'
M = 'sherpa-onnx-nemo-parakeet-tdt-0.6b-v3-int8'

def prepara():
    os.makedirs(D, exist_ok=True)
    if not os.path.exists(f'{D}/{M}/tokens.txt'):
        print('scarico il modello (~640 MB)…', flush=True)
        t = f'{D}/{M}.tar.bz2'; urllib.request.urlretrieve(U + M + '.tar.bz2', t)
        with tarfile.open(t) as z: z.extractall(D)
        os.remove(t)
    if not os.path.exists(f'{D}/silero_vad.onnx'):
        urllib.request.urlretrieve(U + 'silero_vad.onnx', f'{D}/silero_vad.onnx')
    try: import sherpa_onnx  # noqa
    except ImportError:
        subprocess.run([sys.executable, '-m', 'pip', 'install', '-q', 'sherpa-onnx', '--break-system-packages'], check=True)

def ts(s):
    h, r = divmod(s, 3600); m, r = divmod(r, 60)
    return '%02d:%02d:%06.3f' % (h, m, r)

def main():
    src = sys.argv[1]; out = sys.argv[2] if len(sys.argv) > 2 else os.path.splitext(src)[0] + '_trascrizione'
    prepara()
    import numpy as np, sherpa_onnx
    a = subprocess.run(['ffmpeg', '-v', 'error', '-i', src, '-vn', '-ac', '1', '-ar', '16000', '-f', 's16le', '-'], capture_output=True, check=True).stdout
    x = np.frombuffer(a, np.int16).astype(np.float32) / 32768
    P = f'{D}/{M}/'
    rec = sherpa_onnx.OfflineRecognizer.from_transducer(encoder=P + 'encoder.int8.onnx', decoder=P + 'decoder.int8.onnx',
            joiner=P + 'joiner.int8.onnx', tokens=P + 'tokens.txt', model_type='nemo_transducer', num_threads=os.cpu_count() or 4)
    cfg = sherpa_onnx.VadModelConfig(); cfg.silero_vad.model = f'{D}/silero_vad.onnx'
    cfg.silero_vad.min_silence_duration = 0.35; cfg.silero_vad.max_speech_duration = 20; cfg.sample_rate = 16000
    vad = sherpa_onnx.VoiceActivityDetector(cfg, buffer_size_in_seconds=120)
    segs = []
    def svuota():
        while not vad.empty():
            s = vad.front; t0 = s.start / 16000; st = rec.create_stream(); st.accept_waveform(16000, s.samples); rec.decode_stream(st)
            r = st.result; testo = r.text.strip()
            if testo:
                parole = [[round(t0 + t, 2), w] for t, w in zip(r.timestamps, r.tokens)]
                segs.append(dict(inizio=round(t0, 2), fine=round(t0 + len(s.samples) / 16000, 2), testo=testo, parole=parole))
            vad.pop()
    for i in range(0, len(x), 512):
        vad.accept_waveform(x[i:i + 512]); svuota()
        if i % (16000 * 300) < 512: print(f'{i / 16000 / 60:.0f} min', flush=True)
    vad.flush(); svuota()
    json.dump(segs, open(out + '.json', 'w'), ensure_ascii=False, indent=0)
    with open(out + '.srt', 'w') as f:
        for n, s in enumerate(segs, 1):
            f.write(f"{n}\n{ts(s['inizio']).replace('.', ',')} --> {ts(s['fine']).replace('.', ',')}\n{s['testo']}\n\n")
    print('fatto:', out + '.json', out + '.srt', len(segs), 'segmenti')

if __name__ == '__main__':
    main()
