import sys,json;sys.path.insert(0,'/tmp/w/b')
from scenes import *
from content import *
IMG={'cecenia':("Dove si trova la Cecenia",3),'kuwait':("Dove si trova il Kuwait",2),'iugoslavia':("L'ex Iugoslavia (1991-2008)",3),'ue':("Le tappe dell'integrazione europea (1957-2024)",4),'ritratti':("Silvio Berlusconi e Romano Prodi",5)}
from PIL import Image
class Reg:
    def __init__(self,start=3): self.n=start-1; self.d={}; self.order=[]
    def pn(self,key):
        if key not in self.d: self.n+=1; self.d[key]=self.n; self.order.append(key)
        return self.d[key]
JOBS=[]
def want(html_str,name):
    out=f'{B}/png/{name}.png'
    JOBS.append((html_str,out));return out
def slide_png(reg,arg,active,focus=False):
    A=ARGS[arg-1];P=pages(A['cards'])
    pg=[p for p in P if active in p][0]
    key=('slide',arg,P.index(pg),active if focus else None,focus)
    n=reg.pn(key)
    return want(slide_state(arg,pg,active,n,focus=focus),f's_{arg}_{P.index(pg)}_{active}_{int(focus)}_p{n}')
def img_png(reg,arg,iid):
    cap,_=IMG[iid];n=reg.pn(('img',iid))
    p=f'{B}/img/{iid}.png';w,h=Image.open(p).size
    return want(image_state(arg,p,cap,n,w,h),f'i_{iid}_p{n}')
def prof_states(name,meta,reg,lead=0.8,maxhold=150,alt=70):
    c=CHUNKS[name];iv=[tuple(x) for x in meta['iv']]
    from prof import mapper
    f,dur=mapper(iv)
    ev=c['ev'];arg=c['arg']
    # eventi -> intervalli nel tempo del pezzo
    T0=lead;Tend=lead+dur+0.5
    pts=[(lead+f(t),k,v) for t,k,v in ev]
    # 'ue': dopo 2560 torna la card 3 (allargamento a Est)
    if name=='A4': pts.append((lead+f(2560.0),'c',3));pts.sort()
    pts[0]=(0.0,pts[0][1],pts[0][2])
    states=[]
    for i,(t,k,v) in enumerate(pts):
        te=pts[i+1][0] if i+1<len(pts) else Tend
        if k=='img':
            states.append((t,img_png(reg,arg,v)));continue
        if te-t<=maxhold: states.append((t,slide_png(reg,arg,v)));continue
        # stato lungo: alterna panoramica e focus sulla card
        tt=t;mode=False
        while tt<te-1e-6:
            seg=min(alt if mode else alt+0,te-tt)
            if te-(tt+seg)<25: seg=te-tt   # non lasciare code troppo corte
            states.append((tt,slide_png(reg,arg,v,focus=mode)));tt+=seg;mode=not mode
    return states,dur
