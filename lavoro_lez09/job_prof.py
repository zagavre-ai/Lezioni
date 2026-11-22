# uso: python3 job_prof.py PARTE   -> costruisce i pezzi del prof della Parte (cache: salta quelli già fatti)
import sys,os,subprocess,json,time
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from lezione import *
parte=int(sys.argv[1]);args={1:[1,2,3,4,5],2:[6,7,8,9,10,11]}[parte]
PG=plan_pagine(parte);pag=0;log=W+f'/job_p{parte}.log'
def L(s):open(log,'a').write(time.strftime('%H:%M:%S ')+s+'\n')
if parte==1:
    # D0: introduzione del prof sulla copertina con riquadro
    L('D0')
    t0,t1=arg_range(0);t0,t1=snap(t0,t1,silenzi());segs=segmenti(t0,t1,silenzi());f,tot=mappa(segs)
    with G.R() as r:
        p=W+'/D0_cover.png';r.shot(cover_html(ARG_P1,True,1,1),p)
    d=dict(n=0,segs=segs,tot=tot,stati=[],cards={},imm=[],title='')
    if not os.path.exists(W+'/D0.mkv'):subprocess.run(ffcmd(d,[(0.0,p)],W+'/D0.mkv',None,False,'D0'),check=True)
    L('D0 fatto %.1f s'%tot)
for n in args:
    d=build_riep() if n==11 else build(n,0,'x')
    out=W+f'/A{n}.mkv'
    ev,pag=render_stati(d,PG[f'A{n}'],W+f'/p{n}');tl=timeline(ev)
    if tl[0][0]>0.05:tl.insert(0,(0.0,tl[0][1]))
    json.dump(dict(n=n,tot=d['tot'],stati=[(round(s[0],2),s[1],s[2],s[3]) for s in d['stati']],imm=d['imm'],pag_fine=pag,segs=d['segs']),open(W+f'/A{n}.json','w'))
    if os.path.exists(out):L(f'A{n} gia fatto');continue
    L(f'A{n} inizio {d["tot"]:.0f}s')
    subprocess.run(ffcmd(d,tl,out,None,False,f'A{n}'),check=True)
    L(f'A{n} fatto')
L('TUTTO FATTO')
