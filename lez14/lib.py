import json,re,subprocess,os,unicodedata
W='/tmp/w'
def norm(s):return re.sub(r'[^a-z0-9 ]',' ',unicodedata.normalize('NFD',s.lower()).encode('ascii','ignore').decode()).split()
def dur(f):return float(subprocess.run(['ffprobe','-v','error','-show_entries','format=duration','-of','csv=p=0',f],capture_output=True,text=True).stdout)
def words(path=W+'/asr/orig.json'):
    s=json.load(open(path));out=[]
    for x in s:
        for t,w in x['parole']:out.append((float(t),w))
    return s,out
def shots(jobs,name='jobs'):
    p=f'{W}/{name}.json';json.dump(jobs,open(p,'w'));subprocess.run(['node','/home/user/Lezioni/lez14/shot.js',p],check=True,cwd='/home/user/Lezioni/lez14',env={**os.environ,'NODE_PATH':'/opt/node-tools/node_modules'})

def parole(path=W+'/asr/orig.json'):
    """lista (t, parola_normalizzata) con i token uniti"""
    s=json.load(open(path));out=[];cur=None
    for x in s:
        for t,w in x['parole']:
            if w.startswith(' ') or cur is None:
                if cur:out.append(cur)
                cur=[float(t),w.strip()]
            else:cur[1]+=w
    if cur:out.append(cur)
    res=[]
    for t,w in out:
        for n in norm(w):res.append((t,n))
    return res
STOP=set('di a da in con su per tra fra il lo la le i gli un una uno e ed o ma che chi non si del della dei delle dello degli al alla alle ai allo agli nel nella nei nelle sul sulla sui come anche piu poi quindi ecco cioe questo questa questi queste quel quella essere sono e ha hanno'.split())
SIN={'onu':['nazioni','unite','organizzazione'],'nato':['alleanza','atlantico','nord'],'cee':['comunita','economica','europea','trattati','roma'],'ceca':['carbone','acciaio'],'fmi':['fondo','monetario'],'urss':['sovietica','unione','sovietico'],'usa':['stati','uniti','americani','americana'],'rft':['repubblica','federale','tedesca'],'rdt':['repubblica','democratica','tedesca'],'euratom':['atomica','energia']}
def chiavi(txt):
    out=[]
    for w in norm(txt):
        out+=SIN.get(w,[])
        if w not in STOP and len(w)>3:out.append(w)
    return out
def stem(w):return w[:5]
def allinea(unita,P,t0,t1,finestra=30):
    """unita: lista di testi in ordine; ritorna lista di tempi di inizio (monotoni) nel range [t0,t1] con DP semplice"""
    idx=[i for i,(t,w) in enumerate(P) if t0<=t<=t1]
    if not idx:return [t0]*len(unita)
    a,b=idx[0],idx[-1]+1;W_=[stem(w) for t,w in P[a:b]];T=[t for t,w in P[a:b]]
    n=len(W_);U=[set(stem(w) for w in chiavi(u)) for u in unita]
    def sc(k,p):
        win=set(W_[p:p+finestra]);u=U[k]
        return len(u&win)/max(1,min(len(u),8))
    import numpy as np
    S=np.array([[sc(k,p) for p in range(n)] for k in range(len(unita))])
    # DP: massimizza somma, posizioni crescenti
    D=np.full((len(unita),n),-1e9);B=np.zeros((len(unita),n),int)
    D[0]=S[0]
    for k in range(1,len(unita)):
        best=-1e9;bi=0
        for p in range(n):
            if D[k-1][p]>best:best=D[k-1][p];bi=p
            # posizione p valida se precedente < p
            D[k][p]=best+S[k][p]-0.001*0;B[k][p]=bi
        # (best comprende anche p stesso: forza stretta sotto)
    p=int(np.argmax(D[-1]));pos=[p]
    for k in range(len(unita)-1,0,-1):
        p=int(B[k][p]);pos.append(p)
    pos=pos[::-1]
    for k in range(len(pos)):
        lo=pos[k-1]+1 if k else 0;p=pos[k];thr=max(0.35,0.6*S[k][p])
        for q in range(lo,p+1):
            if S[k][q]>=thr:pos[k]=q;break
    return [T[min(q,n-1)] for q in pos],[float(S[k][pos[k]]) for k in range(len(unita))]
