import os,sys,json,re,subprocess,numpy as np
sys.path.insert(0,'/home/user/work18/lib')
from asm import *
VN=W+'/a/vn';os.makedirs(VN,exist_ok=True)
VOX=W+'/scambio/storia-V-lez18/vox'
TXT={x['nome']:x['testo'] for x in json.load(open(W+'/scambio/storia-V-lez18/testi_voci.json'))}
for _n in [k for k in TXT if k.endswith('_R2')]:TXT[_n[:-3]]=TXT[_n]
BAD={'INTRO1','INTRO2'}   # vecchie: dicono il nome del prof
PROV=set()
def rdwav(p):
    r=subprocess.run(['ffmpeg','-v','error','-i',p,'-ac','2','-ar',str(SR),'-f','f32le','-'],capture_output=True)
    return np.frombuffer(r.stdout,np.float32).reshape(-1,2).copy()
def vpath(name):
    out=f'{VN}/{name}.wav'
    real=f'{VOX}/{name}.wav'
    if name+'_R2' in TXT and os.path.exists(f'{VOX}/{name}_R2.wav'):real=f'{VOX}/{name}_R2.wav'
    if os.path.exists(real) and name not in BAD:
        if os.path.exists(out) and not os.path.exists(out+'.prov'):return out
        run(['ffmpeg','-y','-loglevel','error','-i',real,'-af','loudnorm=I=-16:TP=-1.5:LRA=11,aresample=48000','-ac','2','-ar','48000',out])
        if os.path.exists(out+'.prov'):os.remove(out+'.prov')
        return out
    if os.path.exists(out) and os.path.exists(out+'.prov'):PROV.add(name);return out
    run(['espeak-ng','-v','it','-s','158','-w',out+'.raw.wav',TXT[name]])
    run(['ffmpeg','-y','-loglevel','error','-i',out+'.raw.wav','-af','loudnorm=I=-16:TP=-1.5:LRA=11,aresample=48000','-ac','2','-ar','48000',out]);os.remove(out+'.raw.wav')
    open(out+'.prov','w').write('provvisoria');PROV.add(name);return out
def vdur(name):
    return float(run(['ffprobe','-v','error','-show_entries','format=duration','-of','csv=p=0',vpath(name)]).stdout)
sys.path.insert(0,'/home/user/work18/scambio/strumenti/letteratura_spagnolo')
from numeri_it import converti
_U={'uno':1,'un':1,'due':2,'tre':3,'tré':3,'quattro':4,'cinque':5,'sei':6,'sette':7,'otto':8,'nove':9}
_T={'vent':20,'trent':30,'quarant':40,'cinquant':50,'sessant':60,'settant':70,'ottant':80,'novant':90}
_TE={'dieci':10,'undici':11,'dodici':12,'tredici':13,'quattordici':14,'quindici':15,'sedici':16,'diciassette':17,'diciotto':18,'diciannove':19}
def _w2n(w):
    w=w.lower();n=0;rest=w
    m=re.match(r'^(due|tre|quattro|cinque|sei|sette|otto|nove)?cento',rest)
    if m:n+=100*(_U[m.group(1)] if m.group(1) else 1);rest=rest[m.end():]
    if rest in _TE:return n+_TE[rest]
    m=re.match(r'^(vent|trent|quarant|cinquant|sessant|settant|ottant|novant)(i|a)?',rest)
    if m:
        n+=_T[m.group(1)];rest=rest[m.end():]
    if rest in _U:n+=_U[rest];rest=''
    if rest or n<10:return None
    return n
def _pc(m):
    w=m.group(1).lower();v=_w2n(w) or _U.get(w)
    return f'{v}%' if v else m.group(0)
def disp(t):
    t=re.sub(r'\b([A-Za-zà-ÿ]+) per cento',_pc,t)
    t=converti(t)
    t=re.sub(r"[A-Za-zÀ-ÿ]+",lambda m:str(_w2n(m.group(0))) if (len(m.group(0))>=5 and _w2n(m.group(0))) else m.group(0),t)
    t=re.sub(r'(19\d\d), (\d\d)\b',r'\1-19\2',t)
    return t
def sents(name):
    return [s for s in re.split(r'(?<=[.!?])\s+',TXT[name]) if s.strip()]
def sent_times(name):
    """inizio di ogni frase in secondi (dall'inizio della voce), da pause + proporzione di lettere"""
    x=rdwav(vpath(name)).mean(1);fs=int(SR*0.01);m=len(x)//fs
    e=np.sqrt((x[:m*fs].reshape(m,fs)**2).mean(1))+1e-9;db=20*np.log10(e);thr=db.max()-38
    sil=db<thr;ss=[];i=0
    while i<m:
        if sil[i]:
            j=i
            while j<m and sil[j]:j+=1
            if j-i>=14 and i>5 and j<m-5:ss.append(((i+j)/2*0.01,(j-i)*0.01))
            i=j
        else:i+=1
    S=sents(name);L=[len(re.sub(r'\W','',s)) for s in S];T=sum(L)
    first=next((k for k in range(m) if not sil[k]),0)*0.01;last=(m-next((k for k in range(m) if not sil[m-1-k]),0))*0.01
    out=[first];acc=0;used=set()
    for i in range(len(S)-1):
        acc+=L[i];tg=first+(last-first)*acc/T
        c=[(abs(p-tg),p) for p,d in ss if p not in used and (not out or p>out[-1]+0.3)]
        if c and min(c)[0]<max(1.2,0.12*(last-first)):p=min(c)[1];used.add(p);out.append(p+0.0)
        else:out.append(tg)
    return out
def fade(a,ms=30):
    n=int(SR*ms/1000);a=a.copy()
    if len(a)>2*n:
        a[:n]*=np.linspace(0,1,n)[:,None];a[-n:]*=np.linspace(1,0,n)[:,None]
    return a
_TR=None
def whoosh():
    global _TR
    if _TR is None:
        a=rdwav('/home/user/Lezioni/kit/suoni/trans.wav')[:int(SR*0.8)].copy();n=int(SR*.3);a[-n:]*=np.linspace(1,0,n)[:,None];_TR=a*0.45
    return _TR
def jingle(n):return rdwav(f'/home/user/Lezioni/kit/suoni/{n}.wav')
class Part:
    def __init__(s,tag):
        s.tag=tag;s.items=[];s.n=0;s.prev=None;s.ev=[];s.tl=[];s.kind=None;s.page=1;s.slides=[];s.sub=[];s.qa=[];s.vl=[];s.pm=[]
    def scene(s,name,states,cam=None,aud=(),kind='kore',dissolve=True,xin=12,whoosh_=True,wmode=None,camfade=True):
        t0=s.n/FPS;first=not s.items
        mp4,last,n=render_scene(states,cam,s.prev if (dissolve and not first) else None,xin=xin,name=name,camfade=camfade)
        if whoosh_ and not first:
            mode=wmode or ('inside' if (s.kind=='prof') else 'before')
            s.ev.append((t0+0.05 if mode=='inside' else t0-0.8,whoosh(),1.0))
        for a_ in aud:
            off,arr,g=a_[:3];s.ev.append((t0+off,arr,g))
            if len(a_)>3:s.vl.append((round(t0+off,3),a_[3]))
        s.tl.append([name,round(t0,3),round(n/FPS,3)]);s.items.append(mp4);s.n+=n;s.prev=last;s.kind=kind
        return n
    def mix(s,total,pgain=1.0):
        out=np.zeros((int(total*SR)+SR,2),np.float32)
        for t,a,g in s.ev:
            i=int(round(t*SR))
            if isinstance(a,str):a=rdwav(a)
            a=a*g
            if i<0:a=a[-i:];i=0
            out[i:i+len(a)]+=a[:len(out)-i]
        return out[:int(total*SR)]

SIGLE=[('DC','Democrazia Cristiana'),('PCI','Partito comunista italiano'),('PSI','Partito socialista italiano'),('MSI','Movimento sociale italiano'),('NATO',"Organizzazione del Trattato dell'Atlantico del Nord"),('URSS','Unione Sovietica'),('CECA',"Comunità europea del carbone e dell'acciaio"),('Ceca',"Comunità europea del carbone e dell'acciaio"),('ENEL','ente energetico nazionale'),('Enel','ente energetico nazionale'),('CEE','Comunità economica europea'),('Cee','Comunità economica europea'),('CLN','Comitato di liberazione nazionale'),('PIL','prodotto interno lordo')]
def xs(t):
    for a,b in SIGLE:t=re.sub(r'\b'+a+r'\b(?!\s*\()(?!,? cioè)',f'{a} ({b})',t)
    return t

def bed(dur,level=0.035):
    n=int(dur*SR);t=np.arange(n)/SR
    pad=(np.sin(2*np.pi*220*t)+0.8*np.sin(2*np.pi*277.18*t)+0.6*np.sin(2*np.pi*329.63*t)+0.4*np.sin(2*np.pi*110*t))*(0.75+0.25*np.sin(2*np.pi*0.17*t))
    f=int(SR*0.6);env=np.ones(n);env[:f]=np.linspace(0,1,f);env[-f:]=np.linspace(1,0,f)
    a=(pad*env*level/2.2).astype(np.float32)
    return np.stack([a,a],1)
