import os,sys,json,re
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from asm import *
from asm import _lista
import render,piano
from lib import ASSET
PROF=WK+'prof.wav'
def png(im,key):
    p=ST+key+'.png'
    if not os.path.exists(p):im.save(p)
    return p
def stati_slide(argn,a,b,pagine,titolo_arg):
    """sequenza (png,durata) per l'intervallo orig [a,b] dalle slide dell'argomento argn. pagine: dict (argn,i)->n pagina"""
    ev=[]  # (t_inizio,t_fine,png)
    for i,s in enumerate(piano.SLIDE[argn]):
        t0,t1=s['t0'],s['t1']
        if t1<=a or t0>=b:continue
        cards=s['cards'];pg=pagine[(argn,i)]
        times=[max(t0,c[0]) for c in cards]
        # intervalli: [t0,times0) -> -1 ; [times_k,times_k+1) -> k
        bounds=[(t0,-1)]+[(times[k],k) for k in range(len(cards))]
        for j,(tb,k) in enumerate(bounds):
            te=bounds[j+1][0] if j+1<len(bounds) else t1
            if te<=tb:continue
            key=f"s{argn}_{i}_{k}"
            if not os.path.exists(ST+key+'.png'):render.slide(s,k,argn,titolo_arg,pg).convert('RGB').save(ST+key+'.png')
            ev.append([tb,te,ST+key+'.png'])
    ev.sort()
    # copri buchi e taglia su [a,b]
    out=[];cur=a
    for tb,te,p in ev:
        tb=max(tb,a);te=min(te,b)
        if te<=tb:continue
        if tb>cur+1e-6 and out:out[-1][1]=tb   # buco: estendi la precedente
        elif tb>cur+1e-6 and not out:tb=cur
        out.append([tb,te,p]);cur=te
    if out:out[0][0]=a;out[-1][1]=b
    # unisci stati identici adiacenti
    m=[]
    for tb,te,p in out:
        if m and m[-1][2]==p:m[-1][1]=te
        else:m.append([tb,te,p])
    return m
def prof_piece(name,argn,a,b,pre,pagine,titolo_arg,intro=False):
    ca=a-pre
    if intro:
        p=ST+'cover_prof.png'
        if not os.path.exists(p):render.slide_cover_prof(1).convert('RGB').save(p)
        stati=[(p,b-ca)]
    else:
        m=stati_slide(argn,a,b,pagine,titolo_arg)
        stati=[]
        for k,(tb,te,p) in enumerate(m):
            s0=ca if k==0 else tb
            stati.append((p,te-s0))
    # durata totale = b-ca ; frame esatti: ridistribuisci arrotondamenti
    tot=fr(b-ca);acc=0;st2=[]
    for k,(p,d) in enumerate(stati):
        n=fr(d) if k<len(stati)-1 else tot-acc
        if n<=0:continue
        st2.append((p,n/FPS));acc+=n
    v,D=video_stati(name,st2,cam=ca)
    parts=[(PROF,0,0,ca,D,0)]
    if pre>0.05:parts.append((SND+'trans.wav',0,-9,0,pre,0))
    aud=audio_pezzo(name,D,parts)
    return v,aud,D
