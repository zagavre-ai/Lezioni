import os, sys, json, subprocess, glob
import numpy as np, sherpa_onnx
D='/tmp/asr'; M='sherpa-onnx-nemo-parakeet-tdt-0.6b-v3-int8'; P=f'{D}/{M}/'
out=sys.argv[1]; files=sys.argv[2:]
os.makedirs(out,exist_ok=True)
rec=sherpa_onnx.OfflineRecognizer.from_transducer(encoder=P+'encoder.int8.onnx',decoder=P+'decoder.int8.onnx',joiner=P+'joiner.int8.onnx',tokens=P+'tokens.txt',model_type='nemo_transducer',num_threads=2)
for f in files:
    n=os.path.splitext(os.path.basename(f))[0]; o=f'{out}/{n}.json'
    if os.path.exists(o): continue
    a=subprocess.run(['ffmpeg','-v','error','-i',f,'-vn','-ac','1','-ar','16000','-f','s16le','-'],capture_output=True).stdout
    x=np.frombuffer(a,np.int16).astype(np.float32)/32768
    # voci brevi: una sola decodifica con tempi parola
    st=rec.create_stream(); st.accept_waveform(16000,x); rec.decode_stream(st); r=st.result
    words=[[round(t,2),w] for t,w in zip(r.timestamps,r.tokens)]
    json.dump(dict(testo=r.text.strip(),parole=words,durata=len(x)/16000),open(o,'w'),ensure_ascii=False)
    print(n,round(len(x)/16000,1),flush=True)
