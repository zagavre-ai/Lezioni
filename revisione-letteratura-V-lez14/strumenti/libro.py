import json,re,collections,sys
sys.path.insert(0,'/tmp/w14')
from fettine import slices,NOV
from evid import ricostruisci,W,norm
words=[(t,norm(x)[:5]) for t,w in ricostruisci(W) for x in re.split(r"['’]",w) if len(norm(x))>=5]
STOP=set('della delle degli dello dalla dalle quello quella questo questa sono anche perch quindi allora cosa cose molto ancora senza dopo prima sempre fatto tutti tutto essere stato stata'.split())
SL={n:[s for p in ps for s in slices(p)] for n,ps in NOV.items()}
for n,v in SL.items():
    a,b=v[0],v[1]
    v[0:2]=[{'p':a['p'],'y0':a['y0'],'y1':b['y1'],'x0':min(a['x0'],b['x0']),'x1':max(a['x1'],b['x1']),'testo':a['testo']+' '+b['testo']}]
for n,v in SL.items():
    for i,s in enumerate(v):
        if n=='B' and i>0: s['x1']=min(s['x1'],1660)
        if n=='B': s['x0']=min(s['x0'],270)
ST={n:[set(norm(x)[:5] for x in re.split(r"[\s'’]",s['testo']) if len(norm(x))>=5 and norm(x)[:5] not in STOP) for s in v] for n,v in SL.items()}
def stato(n,a,b,win=8,thr=9):
    """lista [t0,t1,indice_fettina] su tempo originale: default fettina 0; cambia solo se il prof cita il testo"""
    S=ST[n];ts=[a+x for x in range(int(b-a)+1)]
    seq=[]
    for t in ts:
        ws=[s for tt,s in words if t-win<=tt<=t+win and s not in STOP]
        sc=[len(set(ws)&k) for k in S]
        m=max(sc);seq.append(sc.index(m) if m>=thr else 0)
    # dwell minimo 10 s
    iv=[]
    for t,v in zip(ts,seq):
        if iv and iv[-1][2]==v: iv[-1][1]=t+1
        elif iv and iv[-1][1]-iv[-1][0]<20: iv[-1][2]=v;iv[-1][1]=t+1
        else: iv.append([t,t+1,v])
    iv[-1][1]=b;iv[0][0]=a
    R=[]
    for x in iv:
        if R and R[-1][2]==x[2]: R[-1][1]=x[1]
        else: R.append(x)
    return R
if __name__=='__main__':
    for n,(a,b) in {'C':(2728,3145.5),'B':(3145.5,3860)}.items():
        r=stato(n,a,b);print(n,len(SL[n]),[(round(x),round(y),k,SL[n][k]['p']) for x,y,k in r])

def stato2(n,a,b,win=90):
    """una fettina diversa almeno ogni 90 s: in avanti nell'ordine del brano, guidata dal testo citato (stima)"""
    S=ST[n];cur=0;res=[];t=a
    while t<b-1:
        e=min(b,t+win)
        ws={s for tt,s in words if t<=tt<e and s not in STOP}
        sc=[len(ws&k) for k in S]
        cand=[i for i in range(cur,min(len(S),cur+4))]
        best=max(cand,key=lambda i:(sc[i],-i))
        if t>a and best==cur: best=min(cur+1,len(S)-1)
        cur=best;res.append([t,e,cur]);t=e
    if len(res)>1 and res[-1][1]-res[-1][0]<30: res[-2][1]=res[-1][1];res.pop()
    return res
