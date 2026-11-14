# Voci Kore ricevute: trova l'inizio di ogni frase (trascrizione con i tempi), scrive voci/wav/NOME.wav e meta_NOME.json (vera=True)
import sys,os,json,re,subprocess,wave,numpy as np,difflib
sys.path.insert(0,'/home/claude/w/bin');from allinea import norm
from faster_whisper import WhisperModel
NN=sys.argv[1];D=f'/home/claude/w/l{NN}/voci/';TV=json.load(open(D+'testi_voci.json'))
m=WhisperModel('base',device='cpu',compute_type='int8',cpu_threads=2);REP=[]
for k,fr in TV.items():
    src=D+f'kore/{k}.wav';out=D+f'wav/{k}.wav'
    subprocess.run(['ffmpeg','-y','-v','error','-i',src,'-ac','2','-ar','48000',out],check=True)
    subprocess.run(['ffmpeg','-y','-v','error','-i',src,'-ac','1','-ar','16000','/tmp/v16.wav'],check=True)
    wf=wave.open('/tmp/v16.wav');a=np.frombuffer(wf.readframes(wf.getnframes()),np.int16).astype(np.float32)/32768
    segs,_=m.transcribe(a,language='it',word_timestamps=True)
    W=[(w.start,x) for s in segs for w in s.words for x in norm(w.word)]
    # allineamento parole del testo <-> parole trascritte
    T=[];own=[]
    for i,f in enumerate(fr):
        for x in norm(f):T.append(x);own.append(i)
    sm=difflib.SequenceMatcher(None,T,[w for _,w in W],autojunk=False)
    pos={}
    for bl in sm.get_matching_blocks():
        for j in range(bl.size):pos.setdefault(bl.a+j,W[bl.b+j][0])
    P=[]
    for i in range(len(fr)):
        idx=[n for n,o in enumerate(own) if o==i]
        t=next((pos[n]-(0.25 if q==0 else 0.5) for q,n in enumerate(idx) if n in pos),None)
        P.append(t)
    d=float(subprocess.run(['ffprobe','-v','error','-show_entries','format=duration','-of','csv=p=0',out],capture_output=True,text=True).stdout)
    # buchi: interpolazione
    for i in range(len(P)):
        if P[i] is None:
            a0=next((P[j] for j in range(i-1,-1,-1) if P[j] is not None),0.0);b0=next((P[j] for j in range(i+1,len(P)) if P[j] is not None),d)
            P[i]=(a0+b0)/2
    P[0]=0.0;P=[round(max(0,x),2) for x in P]
    ok=sum(1 for b in sm.get_matching_blocks() for _ in range(b.size))/max(1,len(T))
    json.dump({'phrases':P,'dur':round(d,2),'vera':True},open(D+f'wav/meta_{k}.json','w'))
    diff=[(T[a1:a2],[w for _,w in W][b1:b2]) for op,a1,a2,b1,b2 in sm.get_opcodes() if op!='equal']
    REP.append(f'{k}: {d:.1f} s, frasi {P}, parole riconosciute {ok:.0%}, differenze {diff[:12]}')
    print(REP[-1],flush=True)
open(D+'import_voci.txt','w').write('\n'.join(REP)+'\n')
