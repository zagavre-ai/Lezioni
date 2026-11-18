import json,sys,bisect
sys.path.insert(0,'/tmp/w/tools')
from sync import norm,keys
SEG=json.load(open('/tmp/w/trasc.json'))
WORDS=[]  # (t, normword) con parole intere ricostruite
for s in SEG:
    cur='';t0=None
    for t,p in s['parole']:
        if p.startswith(' ') and cur:
            WORDS.append((t0,norm(cur)));cur='';t0=None
        if t0 is None: t0=t
        cur+=p
    if cur: WORDS.append((t0,norm(cur)))
TS=[t for t,_ in WORDS]
def timeline(cards,t0,t1,step=1.0):
    K=[keys(a+' '+b) for a,b in cards]
    n=len(cards);T=[];t=t0
    prev=-1;out=[]
    while t<t1:
        i0=bisect.bisect_left(TS,t-2);i1=bisect.bisect_right(TS,t+8)
        W={w[:6] for _,w in WORDS[i0:i1]}
        sc=[len(W&k) for k in K]
        best=max(range(n),key=lambda i:(sc[i],-abs(i-prev) if prev>=0 else 0))
        if sc[best]>=2 and (prev<0 or sc[best]>=sc[prev]+1 or sc[prev]<2): prev=best
        out.append((t,prev))
        t+=step
    # compatta
    res=[];last=None
    for t,c in out:
        if c!=last: res.append((round(t,1),c));last=c
    return res
def viterbi(cards,t0,t1,bin=4.0,win=10.0,pf=2.0,pb=6.0):
    K=[keys(a+' '+b) for a,b in cards];n=len(cards)
    bins=[];t=t0
    while t<t1: bins.append(t);t+=bin
    import numpy as np
    SC=np.zeros((len(bins),n))
    for bi,t in enumerate(bins):
        c=t+bin/2
        i0=bisect.bisect_left(TS,c-win);i1=bisect.bisect_right(TS,c+win)
        W={w[:6] for _,w in WORDS[i0:i1]}
        SC[bi]=[len(W&k) for k in K]
    NEG=-1e9;D=np.full((len(bins),n),NEG);B=np.zeros((len(bins),n),int)
    D[0]=SC[0]-np.array([i*0.3 for i in range(n)])
    for bi in range(1,len(bins)):
        for j in range(n):
            best=NEG;bk=0
            for i in range(n):
                v=D[bi-1][i]-(0 if i==j else (pf if j>i else pb))
                if v>best:best=v;bk=i
            D[bi][j]=best+SC[bi][j];B[bi][j]=bk
    j=int(D[-1].argmax());path=[j]
    for bi in range(len(bins)-1,0,-1):
        j=B[bi][j];path.append(j)
    path=path[::-1]
    res=[];last=None
    for t,c in zip(bins,path):
        if c!=last:res.append((round(t,1),c));last=c
    return res
if __name__=='__main__':
    S=json.load(open('/tmp/w/mat/slides_text.json'))
    for pg,(a,b) in {'2':(149.6,1147.2),'4':(1147.2,1447.1),'7':(1610.35,1786.5)}.items():
        print(pg,viterbi(S[pg]['cards'],a,b))
