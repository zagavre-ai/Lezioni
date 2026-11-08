# Voci a gruppi: una sola richiesta per più blocchi (fino a ~MAXC caratteri), poi il file viene diviso nei blocchi
# con la trascrizione. Ogni blocco viene poi controllato da voci_auto.py (e, se non va, rigenerato da solo).
# Meno richieste a parità di voce: utile con il limite giornaliero.
# uso: voci_gruppi.py cartella_lezione NOME1 NOME2 ...   (MAXC=3500 di default)
import sys,os,re,json,difflib,subprocess,numpy as np,soundfile as sf
sys.path.insert(0,'/home/claude/asr_pk');import pk
os.environ.pop('REGIA',None)
sys.path.insert(0,'/home/claude/tts');import gemini_tts as G
L=os.path.abspath(sys.argv[1])+'/';V=L+'voci/';os.makedirs(V+'vox',exist_ok=True);os.makedirs(V+'gruppi',exist_ok=True)
T=json.load(open(V+'testi_voci.json'));MAXC=int(os.environ.get('MAXC','3500'))
names=[n for n in sys.argv[2:] if not os.path.exists(V+f'vox/{n}.wav')]
groups=[];cur=[];c=0
for n in names:
    t=len(' '.join(T[n]))
    if cur and c+t>MAXC:groups.append(cur);cur=[];c=0
    cur.append(n);c+=t
if cur:groups.append(cur)
nm=lambda s:re.sub(r'[^a-zàèéìòóù0-9]','',s.lower())
for gi,g in enumerate(groups):
    gw=V+f'gruppi/{"_".join(g)}.wav'
    if not os.path.exists(gw):
        txt='\n\n'.join(' '.join(T[n]) for n in g)
        try:G.tts(txt,gw+'.tmp.wav');os.rename(gw+'.tmp.wav',gw)
        except RuntimeError as e:print('QUOTA FINITA:',e,flush=True);sys.exit(3)
    SR=24000
    y=np.frombuffer(subprocess.run(['ffmpeg','-v','error','-i',gw,'-ac','1','-ar',str(SR),'-f','f32le','-'],capture_output=True).stdout,np.float32).copy()
    x16=np.frombuffer(subprocess.run(['ffmpeg','-v','error','-i',gw,'-ac','1','-ar','16000','-f','f32le','-'],capture_output=True).stdout,np.float32).copy()
    Wd=[];t=0.0;TT=len(x16)/16000
    while t<TT-0.2:
        b=min(TT,t+20.0);Wd+=pk.words(pk.transcribe(x16[int(t*16000):int(b*16000)],t));t=b
    heard=[nm(w) for _,w in Wd];ht=[a for a,_ in Wd]
    exp=[];own=[]
    for i,n in enumerate(g):
        for w in re.findall(r"[\wàèéìòóù'’-]+",' '.join(T[n])):
            if nm(w):exp.append(nm(w));own.append(i)
    sm=difflib.SequenceMatcher(None,exp,heard,autojunk=False);fj={};lj={}
    for a,b_,sz in sm.get_matching_blocks():
        for k in range(sz):fj.setdefault(own[a+k],b_+k);lj[own[a+k]]=b_+k
    cuts=[0.0]
    for i in range(1,len(g)):
        if i not in fj or (i-1) not in lj:cuts.append(None);continue
        j0,j1=lj[i-1],fj[i]
        if j1-j0>=1:
            gaps=[(ht[j+1]-ht[j],j+1) for j in range(j0,j1)];_,jb=max(gaps);cuts.append(max(0,ht[jb]-0.25))
        else:cuts.append(max(0,ht[j1]-0.25))
    cuts.append(len(y)/SR)
    for i,n in enumerate(g):
        a,b=cuts[i],cuts[i+1]
        if a is None or b is None:print(n,'confine non trovato: lo rigenero da solo',flush=True);continue
        sf.write(V+f'vox/{n}.wav',y[int(a*SR):int(b*SR)],SR)
    print('gruppo',gi+1,'/',len(groups),g,flush=True)
# controllo blocco per blocco (rigenera da soli quelli che non vanno)
r=subprocess.run([sys.executable,'/home/claude/lezioni/tools/voci_auto.py',L]+sys.argv[2:])
sys.exit(r.returncode)
