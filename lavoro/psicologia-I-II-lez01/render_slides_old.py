# Rende le slide dinamiche (righe che compaiono ed evidenziazione a tempo di voce) come immagini + durate
import json,os,sys,subprocess
from playwright.sync_api import sync_playwright
D='/home/claude/lezioni/psicologia-I-II-lez01/'
SL=json.load(open(D+(__import__('os').environ.get('SLJ','slides.json'))))
SY=json.load(open(D+'sync2.json'))
EV=sorted([(float(t),int(i)) for t,i in SY['events']])
END=float(__import__('os').environ.get('ENDT','1821.7'))
def ease(x):x=max(0,min(1,x));return 1-(1-x)**3
# eventi per slide
SEV=[[(t,i) for t,i in EV if i in set(s['ids'])] for s in SL]
starts=[e[0][0] for e in SEV]
for k in range(1,len(starts)): starts[k]=max(starts[k],starts[k-1]+3.0)
ends=starts[1:]+[END]
def state(k,t):
    ids=SL[k]['ids'];ev=SEV[k];v=[];h=[]
    for j,i in enumerate(ids):
        v.append(round(ease((t-starts[k]-0.06*j)/0.4),2))
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
        for k in range(len(SL)):
            if only and k+1 not in only: continue
            ids=SL[k]['ids'];ts=[max(t0,starts[k]) for t0,_ in SEV[k]]
            ev=sorted(set([starts[k]]+[x-0.35 for x in ts[1:]]+ts+[starts[k]+0.06*j+d for j in range(len(ids)) for d in (0.1,0.2,0.3)]))
            samples=[]
            for e in ev:
                for d in (0,.1,.2,.3,.45):
                    t=e+d
                    if starts[k]<=t<ends[k]: samples.append(round(t,3))
            samples=sorted(set(samples))
            el=pg.query_selector_all('.sheet')[k];cache={};seq=[]
            for t in samples:
                v,h=state(k,t);key=json.dumps([v,h])
                if key not in cache:
                    pg.evaluate(JS,{'k':k,'v':v,'h':h});f=f'{out}/s{k+1:03d}_{len(cache):03d}.png';el.screenshot(path=f);cache[key]=f
                if not seq or seq[-1][0]!=cache[key]: seq.append([cache[key],t])
            for j in range(len(seq)):
                seq[j].append((seq[j+1][1] if j+1<len(seq) else ends[k])-seq[j][1])
            plan+=[(f,round(d,3)) for f,_,d in seq]
            print(k+1,len(cache),round(starts[k],1),round(ends[k]-starts[k],1),flush=True)
    return plan
if __name__=='__main__':
    only=[int(x) for x in sys.argv[1:]]
    plan=run(only)
    json.dump({'plan':plan,'starts':starts,'ends':ends},open(D+'sv_plan.json','w'))
