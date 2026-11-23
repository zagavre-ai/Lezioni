# tempi di parola delle voci (sulle voci preparate vox48): serve per accendere le card all'inizio della frase
import os, sys, json, re, subprocess, numpy as np, unicodedata, difflib
import sherpa_onnx
D = '/tmp/asr'; M = 'sherpa-onnx-nemo-parakeet-tdt-0.6b-v3-int8'; P = f'{D}/{M}/'
W = '/tmp/claude-0/l15'
rec = sherpa_onnx.OfflineRecognizer.from_transducer(encoder=P + 'encoder.int8.onnx', decoder=P + 'decoder.int8.onnx', joiner=P + 'joiner.int8.onnx', tokens=P + 'tokens.txt', model_type='nemo_transducer', num_threads=3)
T = {v['nome']: v['testo'] for v in json.load(open(W + '/voci_testi_nuovi.json'))}
OUT = W + '/vox48/_tempi.json'
res = json.load(open(OUT)) if os.path.exists(OUT) else {}
def norm(s):
    s = unicodedata.normalize('NFD', s.lower()); s = ''.join(c for c in s if unicodedata.category(c) != 'Mn')
    return re.sub(r'[^a-z0-9 ]', ' ', s).split()
def words(r):
    W_ = []
    for t, tok in zip(r.timestamps, r.tokens):
        if tok.startswith(' ') or not W_: W_.append([float(t), tok.strip()])
        else: W_[-1][1] += tok
    return W_
for nm in sys.argv[1:]:
    f = f'{W}/vox48/{nm}.wav'
    if not os.path.exists(f) or os.path.exists(f + '.prov'): continue
    a = subprocess.run(['ffmpeg', '-v', 'error', '-i', f, '-ac', '1', '-ar', '16000', '-f', 's16le', '-'], capture_output=True).stdout
    x = np.frombuffer(a, np.int16).astype(np.float32) / 32768
    st = rec.create_stream(); st.accept_waveform(16000, x); rec.decode_stream(st)
    ws = words(st.result); res[nm] = dict(w=ws, dur=len(x) / 16000)
    print(nm, len(ws), flush=True)
json.dump(res, open(OUT, 'w'), ensure_ascii=False)
