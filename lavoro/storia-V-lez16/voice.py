import os,json,subprocess,re,difflib,hashlib
import numpy as np
from engine import sh,dur,norm,W
VOX=W+'/vox/scambio/storia-V-lez16/vox'
PV=W+'/voicepr';os.makedirs(PV,exist_ok=True)
CPS=15.0
_rec=None
def _asr():
    global _rec
    if _rec is None:
        import sherpa_onnx
        D='/tmp/asr/sherpa-onnx-nemo-parakeet-tdt-0.6b-v3-int8/'
        _rec=sherpa_onnx.OfflineRecognizer.from_transducer(encoder=D+'encoder.int8.onnx',decoder=D+'decoder.int8.onnx',joiner=D+'joiner.int8.onnx',tokens=D+'tokens.txt',model_type='nemo_transducer',num_threads=2)
    return _rec
def words_of(wav):
    """[(t,parola)] dalla trascrizione di un file (cache)"""
    c=PV+'/'+hashlib.md5((wav+str(os.path.getmtime(wav))).encode()).hexdigest()[:10]+'.json'
    if os.path.exists(c):return json.load(open(c))
    x=np.frombuffer(sh(['ffmpeg','-v','error','-i',wav,'-ac','1','-ar','16000','-f','f32le','-']).stdout if False else subprocess.run(['ffmpeg','-v','error','-i',wav,'-ac','1','-ar','16000','-f','f32le','-'],capture_output=True).stdout,np.float32)
    rec=_asr();out=[];step=16000*18
    for i in range(0,len(x),step):
        ch=x[i:i+step+16000*2] if i+step<len(x) else x[i:]
        st=rec.create_stream();st.accept_waveform(16000,ch);rec.decode_stream(st);r=st.result
        cur=None
        for t,tok in zip(r.timestamps,r.tokens):
            if tok.startswith(' ') or cur is None:
                if cur:out.append(cur)
                cur=[i/16000+t,tok.strip()]
            else:cur[1]+=tok
        if cur:out.append(cur)
        if i+step>=len(x):break
    json.dump(out,open(c,'w'),ensure_ascii=False);return out
def real(name):
    p=f'{VOX}/{name}.wav';return p if os.path.exists(p) and os.path.getsize(p)>2000 else None
def prepare(name,text):
    """-> (wav48 stereo trattato, durata, provvisoria?)"""
    o=f'{PV}/{name}.wav';src=real(name)
    if src:
        if os.path.exists(o) and os.path.getmtime(o)>os.path.getmtime(src):return o,dur(o),False
        sh(['ffmpeg','-v','error','-y','-i',src,'-af','silenceremove=start_periods=1:start_threshold=-50dB:start_silence=0.05,areverse,silenceremove=start_periods=1:start_threshold=-50dB:start_silence=0.05,areverse,loudnorm=I=-16:TP=-1.5:LRA=11,afade=t=in:d=0.03,areverse,afade=t=in:d=0.04,areverse,aresample=48000,pan=stereo|c0=c0|c1=c0',o])
        return o,dur(o),False
    d=max(1.0,len(text)/CPS)
    if not os.path.exists(o) or abs(dur(o)-d)>0.05 or os.path.exists(o+'.prov')==False:
        sh(['ffmpeg','-v','error','-y','-f','lavfi','-i',f'anullsrc=r=48000:cl=stereo','-t',f'{d:.3f}',o]);open(o+'.prov','w').write('1')
    return o,d,True
def starts(name,text,sentences):
    """tempo d'inizio di ciascuna frase nel file preparato (reale: allineamento con la trascrizione; provvisorio: proporzionale)"""
    o,d,prov=prepare(name,text)
    if prov:
        tot=sum(len(s) for s in sentences);t=0;out=[]
        for s in sentences:out.append(d*t/tot);t+=len(s)
        return out,d,True
    W_=words_of(o);ws=[norm(w) for t,w in W_]
    exp=[];idx=[]
    for s in sentences:
        k=[norm(x) for x in s.split() if norm(x)];idx.append(len(exp));exp+=k
    sm=difflib.SequenceMatcher(None,exp,ws,autojunk=False)
    mp={}
    for a,b,n in sm.get_matching_blocks():
        for j in range(n):mp[a+j]=b+j
    out=[]
    for i,ix in enumerate(idx):
        j=None
        for q in range(ix,min(ix+6,len(exp))):
            if q in mp:j=mp[q];break
        if j is None:out.append(out[-1] if out else 0.0)
        else:out.append(max(0.0,W_[j][0]-0.12))
    for i in range(1,len(out)):out[i]=max(out[i],out[i-1])
    return out,d,False
