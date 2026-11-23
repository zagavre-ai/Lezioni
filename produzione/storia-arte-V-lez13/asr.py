import os,sys,json,subprocess,re
import numpy as np,sherpa_onnx
D='/tmp/asr';M='sherpa-onnx-nemo-parakeet-tdt-0.6b-v3-int8';P=f'{D}/{M}/'
_rec=None
def rec():
    global _rec
    if _rec is None:_rec=sherpa_onnx.OfflineRecognizer.from_transducer(encoder=P+'encoder.int8.onnx',decoder=P+'decoder.int8.onnx',joiner=P+'joiner.int8.onnx',tokens=P+'tokens.txt',model_type='nemo_transducer',num_threads=4)
    return _rec
def words(path):
    """trascrive un file breve (voce) -> lista (t,parola) a livello di parola"""
    a=subprocess.run(['ffmpeg','-v','error','-i',path,'-vn','-ac','1','-ar','16000','-f','s16le','-'],capture_output=True,check=True).stdout
    x=np.frombuffer(a,np.int16).astype(np.float32)/32768
    out=[];r=rec()
    # a blocchi da 25 s (taglio nel punto più silenzioso)
    i=0;N=len(x)
    while i<N:
        j=min(N,i+16000*25)
        if j<N:
            w=x[j-16000*3:j];k=np.argmin([np.abs(w[q:q+800]).mean() for q in range(0,len(w)-800,400)])*400;j=j-16000*3+k
        st=r.create_stream();st.accept_waveform(16000,x[i:j]);r.decode_stream(st);res=st.result
        cur=None
        for t,tok in zip(res.timestamps,res.tokens):
            if tok.startswith(' ') or cur is None:
                if cur:out.append(cur)
                cur=[i/16000+t,tok.strip()]
            else:cur[1]+=tok
        if cur:out.append(cur)
        i=j
    return out
def norm(w):return re.sub(r'[^a-z0-9àèéìòù]','',w.lower())
def align(ref_words,heard):
    """per ogni parola di riferimento indice -> tempo (difflib); le non trovate si interpolano"""
    import difflib
    a=[norm(w) for w in ref_words];b=[norm(w) for _,w in heard]
    sm=difflib.SequenceMatcher(None,a,b,autojunk=False);T=[None]*len(a)
    for blk in sm.get_matching_blocks():
        for k in range(blk.size):T[blk.a+k]=heard[blk.b+k][0]
    # interpolazione
    last=None
    for i in range(len(T)):
        if T[i] is None:
            p=next((j for j in range(i-1,-1,-1) if T[j] is not None),None);n=next((j for j in range(i+1,len(T)) if T[j] is not None),None)
            if p is None and n is None:T[i]=0
            elif p is None:T[i]=max(0,T[n]-0.3*(n-i))
            elif n is None:T[i]=T[p]+0.3*(i-p)
            else:T[i]=T[p]+(T[n]-T[p])*(i-p)/(n-p)
    return T
