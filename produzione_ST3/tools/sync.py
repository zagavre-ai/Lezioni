# allineamento monotono dei segmenti di trascrizione alle carte della slide
import re,json,numpy as np
SW=set('il lo la le gli i un una di a da in con su per tra fra e che del della dei delle degli al alla alle ai nel nella nei nelle sul sulla non si è sono come ma anche più ha hanno questo questa quello cui o se poi quindi ecco dunque allora ad ed l d all dell'.split())
def toks(s):
    w=re.findall(r"[a-zàèéìòù0-9]+",s.lower());return [x[:5] for x in w if x not in SW and len(x)>2]
def attiva(R,t0,t1,srcs):
    """R: segmenti [a,b,testo]; srcs: testi sorgente delle carte. -> tempi di attivazione (assoluti) di ogni carta"""
    seg=[r for r in R if r[0]>=t0-0.01 and r[0]<t1]
    K=len(srcs);N=len(seg)
    if N==0:return [t0+i*(t1-t0)/K for i in range(K)]
    ts=[set(toks(s)) for s in srcs]
    from collections import Counter
    df=Counter()
    for s in ts:df.update(s)
    S=np.zeros((N,K))
    for i,r in enumerate(seg):
        a=set(toks(r[2]))
        for k in range(K):
            if a and ts[k]:S[i,k]=sum(1.0/df[w] for w in a&ts[k])/(len(a)**0.5)
    # ogni carta sceglie un segmento-àncora; àncore crescenti, massima somma di similarita'
    NEG=-1e9;D=np.full((K,N),NEG);B=np.zeros((K,N),int)
    D[0,0]=0.0   # la prima carta e' attiva dall'inizio
    for k in range(1,K):
        best=NEG;bj=0
        for i in range(N):
            # miglior D[k-1,j] con j<i
            if i>0 and D[k-1,i-1]>best:best=D[k-1,i-1];bj=i-1
            if i>0 and best>NEG/2:D[k,i]=best+S[i,k];B[k,i]=bj
        # (best aggiornato in modo incrementale: massimo prefisso)
    # ricostruzione
    i=int(np.argmax(D[K-1]));A=[0]*K
    for k in range(K-1,-1,-1):
        A[k]=i;i=B[k,i]
    act=[seg[A[k]][0] for k in range(K)];act[0]=t0
    for k in range(1,K):act[k]=max(act[k],act[k-1]+3.0)
    return act
