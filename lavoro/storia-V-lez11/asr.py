# asr.py file1.wav file2.wav ... -> accanto a ciascuno scrive asr/<nome>.json (segmenti con parole). Carica il modello una volta.
import sys,os,json,subprocess
sys.path.insert(0,'/home/user/Lezioni/kit/tools')
import numpy as np, sherpa_onnx
D=os.environ.get('TELESIO_ASR','/tmp/asr');M='sherpa-onnx-nemo-parakeet-tdt-0.6b-v3-int8';P=f'{D}/{M}/'
rec=sherpa_onnx.OfflineRecognizer.from_transducer(encoder=P+'encoder.int8.onnx',decoder=P+'decoder.int8.onnx',joiner=P+'joiner.int8.onnx',tokens=P+'tokens.txt',model_type='nemo_transducer',num_threads=2)
os.makedirs('asr',exist_ok=True)
for src in sys.argv[1:]:
    n=os.path.basename(src)[:-4]
    out=f'asr/{n}.json'
    if os.path.exists(out): continue
    a=subprocess.run(['ffmpeg','-v','error','-i',src,'-vn','-ac','1','-ar','16000','-f','s16le','-'],capture_output=True,check=True).stdout
    x=np.frombuffer(a,np.int16).astype(np.float32)/32768
    segs=[]
    # voci brevi (<40 s): un solo blocco; più lunghe: finestre da 25 s
    L=16000*25
    for i in range(0,len(x),L):
        ch=x[i:i+L]
        if len(ch)<1600: continue
        st=rec.create_stream();st.accept_waveform(16000,ch);rec.decode_stream(st);r=st.result
        t0=i/16000
        segs.append(dict(inizio=round(t0,2),testo=r.text.strip(),parole=[[round(t0+t,2),w] for t,w in zip(r.timestamps,r.tokens)]))
    json.dump(segs,open(out,'w'),ensure_ascii=False)
    print(n,flush=True)
