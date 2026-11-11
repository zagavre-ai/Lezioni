# Importa un file voce generato fuori (Vox Studio, ElevenLabs...) per un blocco: trova l'inizio di ogni frase
# con la trascrizione, toglie i silenzi iniziali/finali, normalizza e aggiorna wav/<NOME>.wav e il meta.
# uso: python3 importa_voce_esterna.py NOME file.mp3
# testo atteso: voci/testi_voci.json {NOME:[frasi]} se c'è, altrimenti estese_P1.F[NOME]
import sys,os,re,json,difflib,subprocess,numpy as np,soundfile as sf
sys.path.insert(0,'/home/claude/asr_pk');sys.path.insert(0,'/home/claude/moda_tec/voci')
import pk,estese_P1 as X
try:
    import estese_P2 as X2;X.F.update(X2.F)
except Exception:pass
D='/home/claude/moda_tec/voci/';W=D+'wav/';SR=24000
name,src=sys.argv[1],sys.argv[2]
TJ=D+'testi_voci.json'
texts=(json.load(open(TJ)).get(name) if os.path.exists(TJ) else None) or X.F[name]
y=np.frombuffer(subprocess.run(['ffmpeg','-v','error','-i',src,'-ac','1','-ar',str(SR),'-f','f32le','-'],capture_output=True).stdout,np.float32).copy()
x16=np.frombuffer(subprocess.run(['ffmpeg','-v','error','-i',src,'-ac','1','-ar','16000','-f','f32le','-'],capture_output=True).stdout,np.float32).copy()
Wd=[];t=0.0;T=len(x16)/16000
while t<T-0.2:
    b=min(T,t+20.0);Wd+=pk.words(pk.transcribe(x16[int(t*16000):int(b*16000)],t));t=b
n=lambda s:re.sub(r'[^a-zàèéìòóù0-9]','',s.lower())
heard=[n(w) for _,w in Wd];ht=[a for a,_ in Wd]
exp=[];own=[]
for i,p in enumerate(texts):
    for w in re.findall(r"[\wàèéìòóù'’-]+",p):
        if n(w):exp.append(n(w));own.append(i)
sm=difflib.SequenceMatcher(None,exp,heard,autojunk=False);first={}
for a,b_,sz in sm.get_matching_blocks():
    for k in range(sz):first.setdefault(own[a+k],ht[b_+k])
# inizio di ogni frase: nella pausa più lunga tra l'ultima parola riconosciuta della frase prima e la prima di questa
fj={};lj={}
for a,b_,sz in sm.get_matching_blocks():
    for k in range(sz):
        fj.setdefault(own[a+k],b_+k);lj[own[a+k]]=b_+k
starts=[]
for i in range(len(texts)):
    if i not in fj:print('ATTENZIONE: frase',i,'non trovata');starts.append(starts[-1]+1 if starts else 0.0);continue
    j1=fj[i];j0=lj.get(i-1,-1) if i>0 else -1
    if i>0 and j0>=0 and j1-j0>1:
        gaps=[(ht[j+1]-ht[j],j+1) for j in range(j0,j1)];g,jb=max(gaps);s=ht[jb]
    else:s=ht[j1]
    starts.append(max(0.0,s-0.25))
# silenzio iniziale e finale
e=np.abs(y)>0.01;i0=max(0,int(np.argmax(e))-int(0.05*SR));i1=len(y)-int(np.argmax(e[::-1]))+int(0.25*SR)
y=y[i0:i1];off=i0/SR;starts=[round(max(0.0,s-off),2) for s in starts];starts[0]=0.0
y=y/max(1e-6,np.abs(y).max())*0.9;sf.write(W+name+'.wav',y,SR)
mf=[W+f for f in os.listdir(W) if f.startswith('meta_') and name in json.load(open(W+f))]
mf=mf[0] if mf else W+'meta_S1.json';M=json.load(open(mf)) if os.path.exists(mf) else {}
M[name]={'dur':round(len(y)/SR,2),'phrases':starts,'text':texts};json.dump(M,open(mf,'w'),ensure_ascii=False,indent=1)
ok=sum(1 for i in range(len(texts)) if i in first)
bad=[(op,exp[i1:i2],heard[j1:j2]) for op,i1,i2,j1,j2 in sm.get_opcodes() if op!='equal']
print(name,'durata',M[name]['dur'],'frasi trovate',ok,'/',len(texts),'parole diverse',sum(len(b[1]) for b in bad))
for b in bad[:12]:print('  ',b)
