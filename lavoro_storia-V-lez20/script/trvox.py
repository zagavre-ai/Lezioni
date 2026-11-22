import os,sys,json,subprocess,numpy as np,sherpa_onnx
D='/tmp/asr';M='sherpa-onnx-nemo-parakeet-tdt-0.6b-v3-int8';P=f'{D}/{M}/'
rec=sherpa_onnx.OfflineRecognizer.from_transducer(encoder=P+'encoder.int8.onnx',decoder=P+'decoder.int8.onnx',joiner=P+'joiner.int8.onnx',tokens=P+'tokens.txt',model_type='nemo_transducer',num_threads=2)
src=sys.argv[1];out=sys.argv[2];res={}
if os.path.exists(out):res=json.load(open(out))
for f in sorted(os.listdir(src)):
    if not f.endswith('.wav') or f[:-4] in res:continue
    a=subprocess.run(['ffmpeg','-v','error','-i',f'{src}/{f}','-ac','1','-ar','16000','-f','s16le','-'],capture_output=True).stdout
    x=np.frombuffer(a,np.int16).astype(np.float32)/32768
    words=[];txt=[]
    for i in range(0,len(x),16000*25):  # blocchi da 25 s, tagliati nei punti piu' silenziosi
        pass
    # tronchi da <=25 s con taglio al minimo di energia
    pos=0
    while pos<len(x):
        end=min(len(x),pos+16000*24)
        if end<len(x):
            seg=np.abs(x[end-16000*4:end]);w=1600;e=[seg[j:j+w].mean() for j in range(0,len(seg)-w,800)];end=end-16000*4+int(np.argmin(e))*800+w//2
        st=rec.create_stream();st.accept_waveform(16000,x[pos:end]);rec.decode_stream(st);r=st.result
        txt.append(r.text.strip());words+=[[round(pos/16000+t,2),w] for t,w in zip(r.timestamps,r.tokens)]
        pos=end
    res[f[:-4]]=dict(dur=round(len(x)/16000,3),testo=' '.join(txt),parole=words)
    json.dump(res,open(out,'w'),ensure_ascii=False)
print('fatto')
