# Allineamento parola per parola (PDF <-> parlato) dentro la finestra di ogni pagina. Restituisce per ogni frase: inizio, copertura, parole agganciate.
import json,re,sys
import numpy as np
sys.path.insert(0,'/home/user/lav/tools')
from frasi import *
def lev1(a,b):
    if abs(len(a)-len(b))>1:return False
    if a==b:return True
    i=0
    while i<min(len(a),len(b)) and a[i]==b[i]:i+=1
    return a[i+1:]==b[i+1:] or a[i:]==b[i+1:] or a[i+1:]==b[i:]
def pts(a,b):
    if a==b:return 3.0 if len(a)>=4 else 1.0
    if len(a)>=6 and lev1(a,b):return 2.0
    return -1.2
def dp_pagina(A,B,gap=0.7):
    n,m=len(A),len(B)
    S=np.zeros((n+1,m+1),dtype=np.float32);T=np.zeros((n+1,m+1),dtype=np.int8)
    for i in range(1,n+1):S[i,0]=-gap*i;T[i,0]=1
    for i in range(1,n+1):
        for j in range(1,m+1):
            d=S[i-1,j-1]+pts(A[i-1],B[j-1]);u=S[i-1,j]-gap;l=S[i,j-1]-0.05   # saltare parole del parlato costa poco
            if d>=u and d>=l:S[i,j]=d;T[i,j]=0
            elif u>=l:S[i,j]=u;T[i,j]=1
            else:S[i,j]=l;T[i,j]=2
    j=int(np.argmax(S[n]));i=n;match=[None]*n
    while i>0:
        t=T[i,j] if j>0 else 1
        if t==0:
            if pts(A[i-1],B[j-1])>0:match[i-1]=j-1
            i-=1;j-=1
        elif t==1:i-=1
        else:j-=1
    return match
def allinea_frasi(fr,tr,pag_seg,W,margine=25.0):
    """fr=[(pg,testo)]; pag_seg[i]=pagina (0-based) del segmento ASR i. Ritorna lista dict(k,t0,cop,n)"""
    # finestra temporale di ogni pagina
    ts={}
    for i,p in enumerate(pag_seg):ts.setdefault(p+1,[1e9,0]);ts[p+1][0]=min(ts[p+1][0],tr[i]['inizio']);ts[p+1][1]=max(ts[p+1][1],tr[i]['fine'])
    out=[None]*len(fr)
    for p in sorted(set(x[0] for x in fr)):
        js=[j for j,(pg,_) in enumerate(fr) if pg==p]
        if p not in ts:continue
        a0,a1=ts[p][0]-margine,ts[p][1]+margine
        ib=[i for i,(t,w,n) in enumerate(W) if a0<=t<=a1 and n]
        B=[W[i][2] for i in ib]
        A=[];idx=[]
        for j in js:
            for x in fr[j][1].split():
                n=norm(x)
                if n:A.append(n);idx.append(j)
        mt=dp_pagina(A,B)
        for j in js:
            pos=[k for k,jj in enumerate(idx) if jj==j];mm=[(k-pos[0],ib[mt[k]]) for k in pos if mt[k] is not None]
            cont=[k for k in pos if len(A[k])>=4];cm=[k for k in cont if mt[k] is not None]
            cop=len(cm)/max(1,len(cont))
            t0=None
            if mm:
                off,wi=mm[0];t0=W[wi][0]-0.30*off   # prima parola agganciata, riportata all'inizio della frase
                if off>8:t0=W[wi][0]-0.30*8
            out[j]=dict(k=j,pg=p,t0=t0,cop=round(cop,2),nm=len(mm),n=len(pos),prima=(W[mm[0][1]][2] if mm else None))
    return out
