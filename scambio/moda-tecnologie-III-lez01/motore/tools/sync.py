# Sincronia voce narrante -> pezzi di testo (nodi della mappa, righe di ripasso, termini del glossario)
import os,sys,json,subprocess,difflib,re
sys.path.insert(0,'/home/user/lav/tools')
from frasi import norm
D='/tmp/asr';M='sherpa-onnx-nemo-parakeet-tdt-0.6b-v3-int8'
_rec=None
def _prep():
    global _rec
    if _rec:return _rec
    import sherpa_onnx
    P=f'{D}/{M}/'
    _rec=sherpa_onnx.OfflineRecognizer.from_transducer(encoder=P+'encoder.int8.onnx',decoder=P+'decoder.int8.onnx',joiner=P+'joiner.int8.onnx',tokens=P+'tokens.txt',model_type='nemo_transducer',num_threads=2)
    return _rec
def parole_wav(path):
    """[(tempo, parola)] con VAD a pezzi (le voci lunghe, come il glossario, sono spezzate)"""
    import numpy as np,sherpa_onnx
    rec=_prep()
    a=subprocess.run(['ffmpeg','-v','error','-i',path,'-vn','-ac','1','-ar','16000','-f','s16le','-'],capture_output=True,check=True).stdout
    x=np.frombuffer(a,np.int16).astype(np.float32)/32768
    cfg=sherpa_onnx.VadModelConfig();cfg.silero_vad.model=f'{D}/silero_vad.onnx';cfg.silero_vad.min_silence_duration=0.25;cfg.silero_vad.max_speech_duration=15;cfg.sample_rate=16000
    vad=sherpa_onnx.VoiceActivityDetector(cfg,buffer_size_in_seconds=300)
    W=[]
    def svuota():
        while not vad.empty():
            s=vad.front;t0=s.start/16000;st=rec.create_stream();st.accept_waveform(16000,s.samples);rec.decode_stream(st);r=st.result
            cur=None
            for t,w in zip(r.timestamps,r.tokens):
                if w.startswith(' ') or cur is None:
                    cur=[round(t0+t,2),w.strip()];W.append(cur)
                else:cur[1]+=w
            vad.pop()
    for i in range(0,len(x),512):vad.accept_waveform(x[i:i+512]);svuota()
    vad.flush();svuota()
    return [(t,w) for t,w in W]
def tok(s):return [n for n in (norm(w) for w in re.split(r"[\s'’]+",s)) if n]
def allinea(W,testi,durata):
    """start (s) di ciascun testo in `testi` (lista di stringhe lette in ordine) dentro la voce; W=parole_wav. Fine di ciascuno = inizio del successivo."""
    A=[];idx=[]
    for k,t in enumerate(testi):
        for w in tok(t):A.append(w);idx.append(k)
    B=[norm(w) for _,w in W]
    sm=difflib.SequenceMatcher(None,A,B,autojunk=False)
    mappa={}
    for a,b,n in sm.get_matching_blocks():
        for i in range(n):mappa[a+i]=b+i
    starts=[None]*len(testi)
    for k in range(len(testi)):
        pos=[i for i,x in enumerate(idx) if x==k]
        for i in pos[:4]:                # primo token del pezzo trovato (entro i primi 4)
            if i in mappa:
                starts[k]=W[mappa[i]][0]-0.05*(i-pos[0]);break
    # buchi: interpola sul numero di parole
    tot=sum(len(tok(t)) for t in testi);acc=0
    for k,t in enumerate(testi):
        if starts[k] is None:starts[k]=None
    for k in range(len(testi)):
        if starts[k] is None:
            prev=max([j for j in range(k) if starts[j] is not None],default=None)
            nxt=min([j for j in range(k+1,len(testi)) if starts[j] is not None],default=None)
            t0=starts[prev] if prev is not None else 0.0;t1=starts[nxt] if nxt is not None else durata
            lo=prev if prev is not None else -1;hi=nxt if nxt is not None else len(testi)
            parole=[len(tok(testi[j])) for j in range(lo+1,hi)];tt=sum(parole) or 1;a=0
            for j,p in zip(range(lo+1,hi),parole):
                if starts[j] is None:starts[j]=t0+(t1-t0)*a/tt
                a+=p
    for k in range(1,len(starts)):starts[k]=max(starts[k],starts[k-1]+0.2)
    starts[0]=max(0.0,starts[0]-0.1)
    ends=[starts[k+1] for k in range(len(starts)-1)]+[durata]
    return [(round(a,2),round(b-a,2)) for a,b in zip(starts,ends)]
def sync(path,testi):
    d=float(subprocess.run(['ffprobe','-v','error','-show_entries','format=duration','-of','csv=p=0',path],capture_output=True,text=True).stdout)
    return allinea(parole_wav(path),testi,d),d
