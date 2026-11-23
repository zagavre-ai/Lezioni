# -*- coding: utf-8 -*-
# Controllo delle voci Kore ricevute: durata, bordi (ultimi 50 ms < 0,03), trascrizione confrontata col testo (numeri e date compresi).
# uso: python3 vcheck.py DIR_WAV TESTI.json [nomi...]
import sys, os, re, json, wave, unicodedata, difflib
import numpy as np
sys.path.insert(0,'/home/work/build'); from anim import digits
import sherpa_onnx
D='/tmp/asr';M='sherpa-onnx-nemo-parakeet-tdt-0.6b-v3-int8';P=f'{D}/{M}/'
rec=sherpa_onnx.OfflineRecognizer.from_transducer(encoder=P+'encoder.int8.onnx',decoder=P+'decoder.int8.onnx',joiner=P+'joiner.int8.onnx',tokens=P+'tokens.txt',model_type='nemo_transducer',num_threads=4)
def norm(t):
    t=digits(t).lower();t=unicodedata.normalize('NFD',t);t=''.join(c for c in t if unicodedata.category(c)!='Mn');t=re.sub(r"[^a-z0-9 ]",' ',t);return t.split()
def load(f):
    w=wave.open(f);sr=w.getframerate();ch=w.getnchannels();a=np.frombuffer(w.readframes(w.getnframes()),dtype=np.int16).astype(np.float32)/32768
    if ch>1:a=a.reshape(-1,ch).mean(1)
    return a,sr
d,tj=sys.argv[1:3];T={v['nome']:v['testo'] for v in json.load(open(tj))};names=sys.argv[3:] or sorted(T)
out=[]
for n in names:
    f=f'{d}/{n}.wav'
    if not os.path.exists(f):out.append((n,'MANCA'));print(n,'MANCA');continue
    a,sr=load(f);dur=len(a)/sr;n50=int(sr*0.05)
    edge=float(np.abs(a[-n50:]).max());edge0=float(np.abs(a[:n50]).max())
    import subprocess
    x=np.frombuffer(subprocess.run(['ffmpeg','-v','error','-i',f,'-ac','1','-ar','16000','-f','s16le','-'],capture_output=True).stdout,np.int16).astype(np.float32)/32768
    st=rec.create_stream();st.accept_waveform(16000,x);rec.decode_stream(st);hyp=norm(st.result.text);ref=norm(T[n])
    r=difflib.SequenceMatcher(None,ref,hyp).ratio()
    diff=[(op,' '.join(ref[i1:i2]),' '.join(hyp[j1:j2])) for op,i1,i2,j1,j2 in difflib.SequenceMatcher(None,ref,hyp).get_opcodes() if op!='equal']
    ok=r>=0.92 and edge<0.03
    out.append((n,round(dur,1),round(edge,4),round(edge0,4),round(r,3),diff[:6],'OK' if ok else 'DA RIVEDERE'))
    print(n,round(dur,1),'bordo fine',round(edge,4),'ini',round(edge0,4),'somiglianza',round(r,3),'OK' if ok else 'DA RIVEDERE',diff[:4] if not ok else '',flush=True)
json.dump(out,open('/home/work/build/vcheck_out.json','w'),ensure_ascii=False,indent=1)
