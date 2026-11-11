# Rende le slide dinamiche (righe che compaiono ed evidenziazione a tempo di voce) come immagini + durate
import json,os,sys,subprocess
from playwright.sync_api import sync_playwright
D='/home/claude/lezioni/psicologia-I-II-lez01/'
SL=json.load(open(D+(__import__('os').environ.get('SLJ','slides.json'))))
SY=json.load(open(D+'sync2.json'))
EV=sorted([(float(t),int(i)) for t,i in SY['events']])
END=float(__import__('os').environ.get('ENDT','1821.7'))
def ease(x):x=max(0,min(1,x));return 1-(1-x)**3
# segmenti: serie consecutive di eventi sulla stessa slide (una slide può essere rivista)
def slide_of(u):
    for k,sl in enumerate(SL):
        if u in sl['ids']: return k
SEG=[]
for t,i in EV:
    k=slide_of(i)
    if SEG and SEG[-1]['k']==k: SEG[-1]['ev'].append((t,i))
    else: SEG.append({'k':k,'ev':[(t,i)],'first':not any(s['k']==k for s in SEG)})
for q,sg in enumerate(SEG):
    sg['t0']=sg['ev'][0][0] if q==0 else max(sg['ev'][0][0],SEG[q-1]['t0']+3.0)
    sg['t1']=None
for q in range(len(SEG)): SEG[q]['t1']=SEG[q+1]['t0'] if q+1<len(SEG) else END
starts=[s['t0'] for s in SEG];ends=[s['t1'] for s in SEG]
def state(sg,t):
    k=sg['k'];ids=SL[k]['ids'];ev=sg['ev'];v=[];h=[]
    for j,i in enumerate(ids):
        v.append(round(ease((t-sg['t0']-0.06*j)/0.4),2) if sg['first'] else 1.0)
        hh=0.0
        for q,(te,ie) in enumerate(ev):
            if ie!=i: continue
            tn=ev[q+1][0] if q+1<len(ev) else 1e9
            hh=max(hh,ease((t-te)/0.3)*(1-ease((t-tn)/0.3)))
        h.append(round(hh,2))
    return v,h
JS="""(a)=>{const sh=document.querySelectorAll('.sheet')[a.k];document.querySelectorAll('.sheet').forEach((s,i)=>s.style.display=i==a.k?'':'none');
 const us=[...sh.querySelectorAll('.bd .un')];const card=e=>e.matches('p.pl,p.bu');
 us.forEach((e,j)=>{const h=a.h[j],v=a.v[j];const f=e.classList.contains('lead')?(.8+.2*h):(card(e)?(.5+.5*h):1);
  e.style.opacity=v*f;e.style.transform='translateY('+((1-v)*10)+'px)';
  if(card(e)){e.style.borderColor=h>.5?'#2060AF':'';e.style.boxShadow=h>0?'0 0 0 '+(.3*h)+'cqw rgba(255,230,0,'+h+'),0 .7cqw 2cqw rgba(11,21,48,.10)':''}
  else{e.style.background=h>0?'rgba(255,230,0,'+(0.42*h)+')':'';e.style.boxShadow=h>0?'0 0 0 .35cqw rgba(255,230,0,'+(0.42*h)+')':''}
  const nb=e.dataset.i;sh.querySelectorAll('.nk .t[data-u="'+nb+'"]').forEach(t=>{t.style.opacity=.55+.45*Math.max(h,0)+(v<1?0:0);t.style.background=h>.5?'#0B1530':'#fff';
   const vv=t.querySelector('.v'),lb=t.querySelector('.lb');vv.style.color=h>.5?'#FFE600':'';lb.style.color=h>.5?'#fff':''})})}"""
def run(only=None,out=D+'sv'):
    os.makedirs(out,exist_ok=True)
    plan=[]
    with sync_playwright() as p:
        br=p.chromium.launch();pg=br.new_page(viewport={'width':1920,'height':1080})
        pg.goto('file://'+D+__import__('os').environ.get('SLH','slides_spoken.html'));pg.wait_for_timeout(800)
        assert pg.evaluate('window.SLIDES.length')==len(SL)
        for q,sg in enumerate(SEG):
            if only and q+1 not in only: continue
            k=sg['k'];ids=SL[k]['ids'];ts=[t0 for t0,_ in sg['ev']]
            ev=sorted(set([sg['t0']]+[x-0.35 for x in ts[1:]]+ts+([sg['t0']+0.06*j+d for j in range(len(ids)) for d in (0.1,0.2,0.3)] if sg['first'] else [])))
            samples=[]
            for e in ev:
                for d in (0,.1,.2,.3,.45):
                    t=e+d
                    if sg['t0']<=t<sg['t1']: samples.append(round(t,3))
            samples=sorted(set(samples))
            el=pg.query_selector_all('.sheet')[k];cache={};seq=[]
            for t in samples:
                v,h=state(sg,t);key=json.dumps([v,h])
                if key not in cache:
                    pg.evaluate(JS,{'k':k,'v':v,'h':h});f=f'{out}/g{q+1:03d}_{len(cache):03d}.png';el.screenshot(path=f);cache[key]=f
                if not seq or seq[-1][0]!=cache[key]: seq.append([cache[key],t])
            for j in range(len(seq)):
                seq[j].append((seq[j+1][1] if j+1<len(seq) else sg['t1'])-seq[j][1])
            plan+=[(f,round(d,3)) for f,_,d in seq]
            print(q+1,'slide',k+1,len(cache),round(sg['t0'],1),round(sg['t1']-sg['t0'],1),flush=True)
    return plan
if __name__=='__main__':
    only=[int(x) for x in sys.argv[1:]]
    plan=run(only)
    json.dump({'plan':plan,'starts':starts,'ends':ends},open(D+'sv_plan_new.json','w'))
