# -*- coding: utf-8 -*-
# Pezzi del prof: slide a 40 px, card intere, bordo giallo alla frase, riquadro 4:3, pause > 2,5 s accorciate.
import sys, os, json, numpy as np
sys.path.insert(0,'/home/work/build')
from lib import *
import av, plan as PL, sil
from dati import ARG
D=np.load('/home/work/an/D.npy');BEST=D.argmin(1)+1;DMIN=D.min(1)
IMGP={6:(3,"Iraq e Iran sul golfo Persico"),11:(6,"Margaret Thatcher, 1979"),12:(6,"François Mitterrand, 1981"),15:(7,"La Comunità degli Stati Indipendenti (1991)"),17:(8,"Piazza Tienanmen, 5 giugno 1989")}
IMGFILE={p:f'/home/work/l17/img/p{p:02d}.png' for p in IMGP}
KICK={a['n']:f"{a['n']:02d} · {a['nome'].upper()}" for a in ARG}
KW={a['n']:[k for k,_ in a['schema']] for a in ARG}
def img_runs(minlen=8):
    runs=[];i=0;n=len(BEST)
    while i<n:
        p=BEST[i] if DMIN[i]<18 else 0
        j=i
        while j<n and (BEST[j] if DMIN[j]<18 else 0)==p:j+=1
        if p in IMGP and j-i>=minlen:runs.append((p,i,j))
        i=j
    return runs
IR=img_runs()
def img_at(t):
    for p,a,b in IR:
        if a+0.5<=t<b-0.5: return p
    return 0
def kept(a,b):
    runs,_,_=sil.silent_runs('/home/work/an/prof_clean.wav',2.5)
    out=[];cur=a
    for s,e in runs:
        if s>cur and e<b:
            out.append((cur,s+0.5));cur=e-0.5
    out.append((cur,b));return [(x,y) for x,y in out if y-x>0.1]
def cut_points(n):
    """inizio e fine del pezzo: nelle pause, 0,15 s prima della frase che segue; mai su un riempitivo (Um, Yeah...)"""
    S=PL.S;i0=PL.START[n];a=max(S[i0-1]['fine']+0.03,S[i0]['inizio']-0.15)
    if n<8:
        i1=PL.START[n+1]-1
        while len(S[i1]['testo'].split())<3 and i1>i0: i1-=1     # ultimo segmento vero
        last=S[i1]['fine'];nx=S[i1+1]['inizio']
        b=min(S[PL.START[n+1]]['inizio']-0.15,last+1.2,nx-0.1);b=max(b,last+0.12)
    else: b=S[-1]['fine']+0.4
    return round(a,3),round(b,3)
def plan_topic(n,fps=30):
    a,b=cut_points(n);subs=kept(a,b)
    asg=PL.assign(n);cards=PL.CARDS[n]['cards']
    def cur_at(t):
        c=-1
        for t0,t1,k in asg:
            if t0-0.25<=t: c=k
            else:break
        return c
    N=sum(int(round((y-x)*30)) for x,y in subs) if len(subs)>1 else int(round((subs[0][1]-subs[0][0])*30))
    # stati a passo 0,1 s sul tempo "montato"
    steps=[];tt=0.0
    for x,y in subs:
        t=x
        while t<y-1e-6:
            p=img_at(t)
            steps.append((('img',p) if p and IMGP[p][0]==n else ('txt',cur_at(t)),t));t+=0.1
    runs=[]
    for k,t in steps:
        if runs and runs[-1][0]==k:runs[-1][1]+=1
        else:runs.append([k,1,t])
    # assorbi i tratti troppo brevi (card < 2 s, immagine < 4 s)
    ch=True
    while ch:
        ch=False
        for i in range(1,len(runs)):
            lim=40 if runs[i][0][0]=='img' else 20
            if runs[i][1]<lim and len(runs)>1:
                runs[i-1][1]+=runs[i][1];del runs[i];ch=True;break
        j=1
        while j<len(runs):
            if runs[j][0]==runs[j-1][0]:runs[j-1][1]+=runs[j][1];del runs[j];ch=True
            else:j+=1
    # spezza i tratti > 140 s: varianti di finestra / alternanza immagine-testo
    out=[]
    for k,nst,t0 in runs:
        if nst<=1400:out.append([k,nst,0,t0]);continue
        rem=nst;v=0;tc=t0
        while rem>0:
            take=min(rem,1200 if rem>1500 else rem)
            if k[0]=='img':
                if v%2==0: out.append([k,take,0,tc])
                else: out.append([('txt',cur_at(tc)),min(take,600),v//2+1,tc]);take=min(take,600)
            else: out.append([k,take,v,tc])
            rem-=take;tc+=take*0.1;v+=1
    # merge in frames
    frs=[];acc=0.0;used=0
    for k,nst,v,t0 in out:
        acc+=nst*3.0;f=int(round(acc))-used
        if f>0:frs.append((k,v,f));used+=f
    if frs:frs[-1]=(frs[-1][0],frs[-1][1],frs[-1][2]+N-used)
    return dict(n=n,subs=subs,N=N,states=frs,cut=(a,b))
def render_states(P,plans,reg,bases=None):
    """reg: dict chiave->pagina; bases: {n: pagina di partenza dell'argomento}"""
    items=[];png={}
    for pl in plans:
        if bases: reg['_next']=bases[pl['n']]
        n=pl['n'];c=PL.CARDS[n]['cards'];title=PL.CARDS[n]['title']
        for k,v,f in pl['states']:
            key=(k,v,n)
            if key not in reg: reg[key]=reg['_next'];reg['_next']+=1
            nm=f"P{P}_n{n}_{k[0]}_{k[1]}_v{v}"
            if k[0]=='img': h=slide_img(IMGP[k[1]][1],IMGFILE[k[1]],reg[key],KICK[n],KW[n])
            else: h=slide_text(n,title,c,k[1],v,reg[key],KW[n],KICK[n])
            items.append((nm,h));png[(k,v,n)]=f'/home/work/build/sl/{nm}.png'
    render(items,'/home/work/build/sl');return png
if __name__=='__main__':
    for n in range(1,9):
        pl=plan_topic(n);print(n,pl['cut'],round(pl['N']/30),'s',len(pl['states']),'stati',[(s[0][0]+str(s[0][1]),s[1],round(s[2]/30)) for s in pl['states']][:14])
