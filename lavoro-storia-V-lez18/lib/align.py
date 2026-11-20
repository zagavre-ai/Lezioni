import os,re,subprocess,numpy as np,sherpa_onnx
D='/tmp/asr';M='sherpa-onnx-nemo-parakeet-tdt-0.6b-v3-int8';P=f'{D}/{M}/'
_rec=None
def rec():
    global _rec
    if _rec is None:
        _rec=sherpa_onnx.OfflineRecognizer.from_transducer(encoder=P+'encoder.int8.onnx',decoder=P+'decoder.int8.onnx',joiner=P+'joiner.int8.onnx',tokens=P+'tokens.txt',model_type='nemo_transducer',num_threads=2)
    return _rec
def tokens(wav):
    a=subprocess.run(['ffmpeg','-v','error','-i',wav,'-ac','1','-ar','16000','-f','s16le','-'],capture_output=True,check=True).stdout
    x=np.frombuffer(a,np.int16).astype(np.float32)/32768
    st=rec().create_stream();st.accept_waveform(16000,x);rec().decode_stream(st);r=st.result
    return list(zip(r.timestamps,r.tokens)),len(x)/16000
def sentence_times(wav,sents):
    tk,dur=tokens(wav)
    # lettere cumulative per token
    cum=[];n=0
    for t,w in tk:
        n+=len(re.sub(r'[^A-Za-zÀ-ÿ0-9]','',w));cum.append((t,n))
    tot=max(n,1)
    lens=[len(re.sub(r'[^A-Za-zÀ-ÿ0-9]','',s)) for s in sents];T=sum(lens);out=[];acc=0
    for i,l in enumerate(lens):
        f0=acc/T;acc+=l;f1=acc/T
        def at(f,first):
            target=f*tot
            if first and f==0:return max(0,tk[0][0]-0.05)
            if not first and f>=1:return dur
            # primo token il cui cumulato supera target
            for t,c in cum:
                if c>=target:return t
            return dur
        s0=at(f0,True); s1=at(f1,False)
        out.append((round(s0,2),round(s1,2)))
    return out,dur
if __name__=='__main__':
    import json
    txt={x['nome']:x['testo'] for x in json.load(open('/tmp/L18/voci/scambio/storia-V-lez11/testi_voci.json'))}
    s=re.split(r'(?<=[.!?:])\s+',txt['R1']);print(s);print(sentence_times('/tmp/L18/vn/R1.wav',s))
