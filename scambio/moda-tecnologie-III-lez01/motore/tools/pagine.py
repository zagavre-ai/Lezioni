import re,json,sys,pymupdf,numpy as np
sys.path.insert(0,'/home/user/lav/tools')
from frasi import norm
def allinea_pagine(pdf,tr):
    d=pymupdf.open(pdf);tok=lambda s:set(w for w in re.findall(r"[a-zàèéìòù0-9]+",s.lower()) if len(w)>3)
    P=[tok(p.get_text()) for p in d];n,m=len(tr),len(P)
    sc=np.zeros((n,m),dtype=np.float32)
    for i,s in enumerate(tr):
        T=tok(s['testo'])
        for j in range(m):sc[i,j]=len(T&P[j])/max(1,len(T))-0.35
    dp=np.full((n,m),-1e9,dtype=np.float32);bp=np.zeros((n,m),dtype=np.int32);dp[0]=sc[0]
    for i in range(1,n):
        b=0;arg=np.zeros(m,dtype=np.int32)
        for j in range(m):
            if dp[i-1][j]>=dp[i-1][b]:b=j
            arg[j]=b
        dp[i]=np.maximum.accumulate(dp[i-1])+sc[i];bp[i]=arg
    j=int(np.argmax(dp[-1]));path=[0]*n
    for i in range(n-1,-1,-1):path[i]=j;j=int(bp[i][j])
    return path
if __name__=='__main__':
    pdf,tr,out=sys.argv[1:4];T=json.load(open(tr));path=allinea_pagine(pdf,T);json.dump(path,open(out,'w'))
    first={}
    for i,p in enumerate(path):first.setdefault(p,i)
    for p in sorted(first):
        s=T[first[p]];print(f"pag{p+1:2d} {int(s['inizio']//60)}:{int(s['inizio']%60):02d}")
