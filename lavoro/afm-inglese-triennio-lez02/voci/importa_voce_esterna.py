# Importa un file voce generato fuori (Vox Studio, ElevenLabs...) per un blocco: trova l'inizio di ogni frase
# con la trascrizione, toglie i silenzi iniziali/finali, normalizza e aggiorna wav/<NOME>.wav e il meta.
# uso: python3 importa_voce_esterna.py NOME file.mp3
# testo atteso: voci/testi_voci.json {NOME:[frasi]} se c'è, altrimenti estese_P1.F[NOME]
import sys,os,re,json,difflib,subprocess,numpy as np,soundfile as sf
sys.path.insert(0,'/home/claude/asr_pk');pass
import pk
D='/home/claude/lezioni/afm-inglese-triennio-lez02/voci/';W=D+'wav/';SR=24000
name,src=sys.argv[1],sys.argv[2]
TJ=D+'testi_voci.json'
texts=json.load(open(TJ))[name]
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
starts=[]
for i in range(len(texts)):
    s=first.get(i)
    if s is None:print('ATTENZIONE: frase',i,'non trovata');s=starts[-1]+1 if starts else 0.0
    starts.append(max(0.0,s-0.25))
# silenzio iniziale e finale
e=np.abs(y)>0.01;i0=max(0,int(np.argmax(e))-int(0.05*SR));i1=len(y)-int(np.argmax(e[::-1]))+int(0.25*SR)
y=y[i0:i1];off=i0/SR;starts=[round(max(0.0,s-off),2) for s in starts];starts[0]=0.0
y=y/max(1e-6,np.abs(y).max())*0.9;sf.write(W+name+'.wav',y,SR)
mf=W+'meta.json';M=json.load(open(mf)) if os.path.exists(mf) else {}
M[name]={'dur':round(len(y)/SR,2),'phrases':starts,'text':texts};json.dump(M,open(mf,'w'),ensure_ascii=False,indent=1)
ok=sum(1 for i in range(len(texts)) if i in first)
bad=[(op,exp[i1:i2],heard[j1:j2]) for op,i1,i2,j1,j2 in sm.get_opcodes() if op!='equal']
print(name,'durata',M[name]['dur'],'frasi trovate',ok,'/',len(texts),'parole diverse',sum(len(b[1]) for b in bad))
for b in bad[:12]:print('  ',b)
