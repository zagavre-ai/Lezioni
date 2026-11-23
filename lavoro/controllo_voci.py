# Controlla le voci Kore: bordi (ultimi 50 ms < 0,03), trascrizione confrontata col testo (numeri in lettere), durata.
# uso: python3 controllo_voci.py NOME [NOME...]
import sys, json, re, wave, difflib, numpy as np, sherpa_onnx
sys.path.insert(0,'/home/user/Lezioni/lavoro')
M='/tmp/asr/sherpa-onnx-nemo-parakeet-tdt-0.6b-v3-int8'
rec=sherpa_onnx.OfflineRecognizer.from_transducer(encoder=f'{M}/encoder.int8.onnx',decoder=f'{M}/decoder.int8.onnx',joiner=f'{M}/joiner.int8.onnx',tokens=f'{M}/tokens.txt',model_type='nemo_transducer',num_threads=2)
T={}
for p in ('/tmp/w/old_testi.json','/tmp/w/voci/testi_voci.json'):
    for x in json.load(open(p)): T[x['nome']]=x['testo']
def norm(s): return re.sub(r'[^a-z0-9àèéìòù ]',' ',s.lower()).split()
for nome in sys.argv[1:]:
    w=wave.open(f'/tmp/w/vox_new/{nome}.wav');sr=w.getframerate();x=np.frombuffer(w.readframes(w.getnframes()),np.int16).astype(np.float32)/32768
    edge=float(np.abs(x[-int(sr*0.05):]).max());ini=float(np.abs(x[:int(sr*0.02)]).max())
    y=x if sr==16000 else np.interp(np.arange(0,len(x),sr/16000),np.arange(len(x)),x).astype(np.float32)
    s=rec.create_stream();s.accept_waveform(16000,y);rec.decode_stream(s)
    a=norm(T[nome]);b=norm(s.result.text)
    sm=difflib.SequenceMatcher(None,a,b);diff=[(op,' '.join(a[i1:i2]),' '.join(b[j1:j2])) for op,i1,i2,j1,j2 in sm.get_opcodes() if op!='equal']
    print(f'{nome}: durata {len(x)/sr:.1f}s bordo_fine {edge:.4f} {"OK" if edge<0.03 else "BORDO>0,03"} inizio {ini:.3f} differenze {len(diff)}')
    for d in diff[:8]: print('   ',d)
