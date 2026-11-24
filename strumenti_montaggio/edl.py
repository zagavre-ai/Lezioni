import re, json
from plan import *
FPS=30
def fr(t): return round(t*FPS)/FPS
def words(s): return re.findall(r"\w+",s['testo'])
BAD_END=set('e che di a da in con per ma o il lo la le un una dei del della delle nel nella sul sulla come se non più poi anche quindi perché cioè'.split())
def valid_cut(i):
    """taglio dopo il segmento i: gli deve finire una frase intera"""
    s=SEGS[i]; t=s['testo'].strip()
    if i+1>=len(SEGS): return True
    n=SEGS[i+1]
    if not re.search(r'[.?!…]["»]?$',t): return False
    w=words(s)
    if len(w)<4: return False
    if w[-1].lower() in BAD_END: return False
    if n['inizio']-s['fine']<0.25: return False
    nt=n['testo'].strip()
    if not (nt[:1].isupper() or nt[:1].isdigit()): return False
    if len(words(n))<=1: return False
    return True
def junk(i):
    s=SEGS[i];t=s['testo'].strip()
    return (t in DROP_TXT or t.rstrip('.') in {'Um','Uh','Yeah','Okay','Tiny','Answer','Cut it','Four to see','All right'}) and s['fine']-s['inizio']<1.6
def kept_segments(a):
    out=[]
    for (x,y) in a['segs']:
        for i in range(x,y+1):
            if not junk(i): out.append(i)
    return out
def intervals(seglist, pre=0.15, post=0.40, maxgap=2.5, keepgap=1.0):
    """intervalli originali da tenere (start,end) con pause lunghe accorciate"""
    iv=[]
    for i in seglist:
        s=SEGS[i];a=s['inizio'];b=s['fine']
        if iv and a-iv[-1][1]-post<=maxgap and (i-1 in seglist or True):
            # stessa sequenza se il vuoto e' breve
            gap=a-iv[-1][1]
            if gap<=maxgap+0.55 and not (gap>maxgap):
                iv[-1][1]=b;continue
        iv.append([a,b])
    # ora gap oltre maxgap: gia' spezzati; unisco intervalli con vuoto <= keepgap lasciando 0.5+0.5
    res=[]
    for k,(a,b) in enumerate(iv):
        res.append([max(0,a-(0.45 if k else pre)),b+(post if k==len(iv)-1 else 0.55)])
    # rendi non sovrapposti
    for k in range(1,len(res)):
        if res[k][0]<res[k-1][1]:
            mid=(res[k][0]+res[k-1][1])/2;res[k-1][1]=mid;res[k][0]=mid
    return res
def build(a):
    sl=kept_segments(a)
    iv=intervals(sl)
    # mappa originale->compressa
    acc=0;maps=[]
    for (x,y) in iv:
        maps.append((x,y,acc));acc+=y-x
    return dict(sl=sl,iv=iv,maps=maps,dur=acc)
def o2c(B,t):
    """tempo originale -> tempo compresso (se cade in un vuoto tolto, va al punto di taglio)"""
    m=B['maps']
    for (x,y,c) in m:
        if x<=t<=y: return c+(t-x)
    # nel vuoto: prendo il successivo
    for (x,y,c) in m:
        if t<x: return c
    return B['dur']
if __name__=='__main__':
    tot=0
    for a in ARG:
        B=build(a);tot+=B['dur']
        print(a['n'],'seg',len(B['sl']),'intervalli',len(B['iv']),'durata',round(B['dur']/60,1),'min')
    print('totale prof',round(tot/60,1))
    for a in ARG:
        for (v,t) in a['ap']:
            # primo taglio valido a partire dal tempo t
            c=[i for i in range(len(SEGS)) if SEGS[i]['fine']>=t-0.01 and valid_cut(i)]
            i=c[0];print(a['n'],v,'dopo seg',i,round(SEGS[i]['fine'],1),SEGS[i]['testo'][-60:])
