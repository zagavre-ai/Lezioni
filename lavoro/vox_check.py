# trascrive ogni voce Kore e la confronta con il testo (parola per parola; numeri in lettere)
import os, sys, json, re, subprocess, numpy as np, unicodedata, difflib
import sherpa_onnx
D = '/tmp/asr'; M = 'sherpa-onnx-nemo-parakeet-tdt-0.6b-v3-int8'; P = f'{D}/{M}/'
W = '/tmp/claude-0/l15'
rec = sherpa_onnx.OfflineRecognizer.from_transducer(encoder=P + 'encoder.int8.onnx', decoder=P + 'decoder.int8.onnx', joiner=P + 'joiner.int8.onnx', tokens=P + 'tokens.txt', model_type='nemo_transducer', num_threads=4)
T = {v['nome']: v['testo'] for v in json.load(open(sys.argv[1]))}
def norm(s):
    s = unicodedata.normalize('NFD', s.lower()); s = ''.join(c for c in s if unicodedata.category(c) != 'Mn')
    return re.sub(r'[^a-z0-9 ]', ' ', s).split()
names = sys.argv[2:] or sorted(T)
out = {}
for nm in names:
    f = f'{W}/vox/{nm}.wav'
    if not os.path.exists(f) or nm not in T: continue
    a = subprocess.run(['ffmpeg', '-v', 'error', '-i', f, '-ac', '1', '-ar', '16000', '-f', 's16le', '-'], capture_output=True).stdout
    x = np.frombuffer(a, np.int16).astype(np.float32) / 32768
    st = rec.create_stream(); st.accept_waveform(16000, x); rec.decode_stream(st); h = st.result.text
    A = norm(T[nm]); B = norm(h); sm = difflib.SequenceMatcher(None, A, B)
    diff = [(' '.join(A[i1:i2]), ' '.join(B[j1:j2])) for tag, i1, i2, j1, j2 in sm.get_opcodes() if tag != 'equal']
    out[nm] = dict(r=round(sm.ratio(), 3), diff=diff, dur=round(len(x) / 16000, 1))
    print(nm, out[nm]['r'], diff[:6], flush=True)
json.dump(out, open(W + '/vox48/_check.json', 'w'), ensure_ascii=False, indent=1)
