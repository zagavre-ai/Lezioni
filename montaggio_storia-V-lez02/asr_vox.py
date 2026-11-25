import sys,os,json,glob,subprocess
sys.path.insert(0,'/home/user/Lezioni/kit/tools')
import trascrivi as T
import numpy as np, sherpa_onnx
D=T.D;M=T.M;P=f'{D}/{M}/'
rec=sherpa_onnx.OfflineRecognizer.from_transducer(encoder=P+'encoder.int8.onnx',decoder=P+'decoder.int8.onnx',joiner=P+'joiner.int8.onnx',tokens=P+'tokens.txt',model_type='nemo_transducer',num_threads=2)
outd='/tmp/w/trvox';os.makedirs(outd,exist_ok=True)
for f in sorted(glob.glob(sys.argv[1]+'/*.wav')):
    n=os.path.basename(f)[:-4]
    if os.path.exists(f'{outd}/{n}.json'): continue
    a=subprocess.run(['ffmpeg','-v','error','-i',f,'-vn','-ac','1','-ar','16000','-f','s16le','-'],capture_output=True).stdout
    x=np.frombuffer(a,np.int16).astype(np.float32)/32768
    # chunks of <=25 s on 16k with 1s overlap-free split at low energy
    words=[];i=0;L=16000*22
    while i<len(x):
        j=min(len(x),i+L)
        if j<len(x):
            seg=np.abs(x[j-16000*3:j]);k=np.argmin(np.convolve(seg,np.ones(1600)/1600,'same'));j=j-16000*3+k
        st=rec.create_stream();st.accept_waveform(16000,x[i:j]);rec.decode_stream(st);r=st.result
        words+=[[round(i/16000+t,2),w] for t,w in zip(r.timestamps,r.tokens)]
        i=j
    json.dump({'dur':len(x)/16000,'parole':words,'testo':''.join(w for _,w in words)},open(f'{outd}/{n}.json','w'),ensure_ascii=False)
    print(n,len(x)/16000,flush=True)
