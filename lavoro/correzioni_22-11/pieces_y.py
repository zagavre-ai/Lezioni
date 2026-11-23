# -*- coding: utf-8 -*-
import sys, os, re, json
sys.path.insert(0,'/home/work/build')
from anim import *
import av, mappe as MP
from pieces_x import V,OLD,NAME,IMG,OUT,SCD
from dati import ARG,GLOSS,GLP,PARTI
fr=av.fr
TITLE_EX="Le fasi conclusive della guerra fredda (1969-1991)"
NOTICE="© Centro Studi Telesio. Tutti i contenuti riprodotti in questa videolezione (testi, grafiche, animazioni, voci e registrazioni) sono di proprietà del Centro Studi Telesio. È vietata la riproduzione, anche parziale, senza autorizzazione scritta."
def cover_html(P,box=False,page=1):
    h=f"<img id=logo src='data:image/svg+xml;base64,{LOGO}'>"
    h+=f"<div class=kick style='left:80px;top:168px;font-size:28px'>STORIA V · VIDEOLEZIONE · PARTE {P}</div>"
    h+=f"<div class=title style='left:80px;top:230px;width:{1290 if box else 1700}px;font-size:92px;line-height:1.1'>{esc(TITLE_EX)}</div>"
    h+="<div class=bar style='left:80px;top:500px;width:140px'></div>"
    h+=f"<div style='position:absolute;left:80px;top:540px;font:600 40px FigS;color:#0B1530'>Storia · Quinto anno</div>"
    h+=f"<div style='position:absolute;left:80px;right:80px;bottom:90px;background:#0B1530;color:#fff;border-radius:14px;padding:14px 26px;font:500 22px/1.35 FigM;text-align:center'>{esc(NOTICE)}</div>"
    h+=f"<div class=foot style='left:80px'>STORIA V</div><div class=foot style='right:80px'>Pagina {page}</div>"
    if box: h+=prof_side(None)
    return shell(h)
def cover_piece(P,out):
    vn=f'BEN{P}_R2';d=vdur(vn);N=fr(d+1.6)
    render([(f'cov{P}',cover_html(P,False))],'/home/work/build/lit')
    av.states_video([(f'/home/work/build/lit/cov{P}.png',N)],out)
    return dict(path=out,n=N,audio=[(0.5,'wav',vpath(vn))])
def dcp_piece(P,out,page=2):
    topics=[ARG[n-1]['titolo'] for n in PARTI[P]];vn=f'DCP{P}'
    texts=topics
    # tempi: frase introduttiva + una per argomento, proporzionali ai caratteri
    t=V[vn];ss=sents(t);d=vdur(vn);tot=sum(len(x) for x in ss);x=0.6;ts=[]
    for q in ss: ts.append(x);x+=d*len(q)/tot
    total=0.6+d+1.6;N=fr(total)
    def H(i): return lit_html("Di cosa parliamo",f"STORIA V · PARTE {P}",[f"{k+1}. {tt}" for k,tt in enumerate(topics)],i,page,fs=48,tfs=64,allv=True,note="")
    items=[('dcp%d_s'%P,H(-1))]+[(f'dcp{P}_{i}',H(i)) for i in range(len(topics))]
    render(items,'/home/work/build/lit')
    st=[(f'/home/work/build/lit/dcp{P}_s.png',fr(ts[1]-0.15))]
    for i in range(len(topics)):
        end=fr(ts[i+2]-0.15) if i+2<len(ts) else N
        st.append((f'/home/work/build/lit/dcp{P}_{i}.png',end-sum(f for _,f in st)))
    nn=av.states_video(st,out);return dict(path=out,n=nn,audio=[(0.6,'wav',vpath(vn))])
def gloss_piece(P,out,page):
    gi=GLP[P];terms=[GLOSS[i] for i in gi]
    ev=[];t=0.7;ev.append((t,'wav',vpath('LG0')));t+=vdur('LG0')+0.9;starts=[]
    for i in gi:
        nm=f'LG{i+1}';ev.append((t,'wav',vpath(nm)));starts.append(t);t+=vdur(nm)+1.0
    total=t+0.8;N=fr(total)
    texts=[d for _,d in terms];leads=[k+':' for k,_ in terms]
    def H(i): return lit_html("Glossario: le parole chiave",f"STORIA V · GLOSSARIO",texts,i,page,leads=leads,fs=40,tfs=56,allv=True)
    items=[(f'gl{P}_s',H(-1))]+[(f'gl{P}_{i}',H(i)) for i in range(len(terms))]
    render(items,'/home/work/build/lit')
    st=[(f'/home/work/build/lit/gl{P}_s.png',fr(starts[0]-0.1))]
    for i in range(len(terms)):
        end=fr(starts[i+1]-0.1) if i+1<len(terms) else N
        st.append((f'/home/work/build/lit/gl{P}_{i}.png',end-sum(f for _,f in st)))
    nn=av.states_video(st,out);return dict(path=out,n=nn,audio=ev)
def map_piece(k,out,page):
    vn=f'MPR{k}_R2';d=vdur(vn);lead=0.8
    steps=MP.timing(k,d,lead);M=MP.MAPS[k]
    from playwright.sync_api import sync_playwright
    h=MP.html(k);f=f'/home/work/build/lit/map{k}.html';open(f,'w').write(h)
    # il testo di pagina: aggiungo il numero alla pagina
    open(f,'w').write(h.replace("<div id=n>",f"<div style='position:absolute;right:60px;bottom:60px;font:700 22px FigB;color:#2060AF'>Pagina {page}</div><div id=n>"))
    paths=[]
    with sync_playwright() as p:
        b=p.chromium.launch(executable_path=CHROME,args=['--allow-file-access-from-files','--no-sandbox']);pg=b.new_page(viewport={'width':1920,'height':1080})
        pg.goto('file://'+f);pg.wait_for_timeout(400);pg.evaluate(f"setSteps({json.dumps(steps)})")
        for i in range(-1,len(steps)+1):
            pg.evaluate(f"state({i})");pth=f'/home/work/build/lit/map{k}_{i}.png';pg.screenshot(path=pth);paths.append(pth)
        b.close()
    total=lead+d+4.0+0.3;N=fr(total);st=[];st.append((paths[0],fr(steps[0][2]-0.15)))
    for i in range(len(steps)):
        end=fr(steps[i+1][2]-0.15) if i+1<len(steps) else fr(lead+d+0.3)
        st.append((paths[i+1],end-sum(f for _,f in st)))
    st.append((paths[-1],N-sum(f for _,f in st)))
    nn=av.states_video(st,out);return dict(path=out,n=nn,audio=[(lead,'wav',vpath(vn)),(lead+d+0.1,'wav','/home/user/Lezioni/kit/suoni/trans.wav'),(lead+d+2.2,'wav','/home/user/Lezioni/kit/suoni/trans.wav')],final_png=paths[-1])
if __name__=='__main__':
    print(cover_piece(1,OUT+'/cover1.mp4'),dcp_piece(1,OUT+'/dcp1.mp4'))
