# dispensa A4 orizzontale (stesse slide del video, a tutta larghezza) + PDF delle mappe
import sys, os, json, subprocess, re
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from plan import *; from gfx import *; from slidedata import SL
import build_prof as bp
from build_prof import cards_of, PG
B='/tmp/w/b'; OUT='/tmp/w/out'; Hh=1357; ZOOM=1123/1920
CSS2=CSS.replace('html,body{width:1920px;height:1080px;','html,body{width:1920px;').replace('overflow:hidden;','')+'''
@page{size:297mm 210mm;margin:0}
.pg{position:relative;width:1920px;height:1357px;page-break-after:always;overflow:hidden;background:#fff}
.pg .rule2{top:1262px}.pg .foot,.pg .pag{top:1277px}
.pg .card{font-size:44px;margin-bottom:26px;padding:26px 36px 26px 60px;box-shadow:none;border:2px solid #DCE3EE;background:#F5F8FC}
.pg .card .dot{top:38px}
.kc{position:absolute;left:80px;display:flex;gap:16px;flex-wrap:wrap;width:1760px}
.kc span{background:#EAF1FB;border-left:8px solid #2060AF;border-radius:8px;padding:8px 18px;font-weight:700;font-size:30px}
.dk{background:#0B1530;color:#fff}.dk .k2{position:absolute;left:0;right:0;text-align:center;font-weight:700;letter-spacing:.2em;font-size:34px;color:#FFE600;text-transform:uppercase}
.dk .h2{position:absolute;left:120px;right:120px;text-align:center;font-family:'Bricolage Grotesque';font-weight:800;line-height:1.08;color:#fff}
.dk .ln2{position:absolute;left:170px;right:170px;font-size:46px;font-weight:600;line-height:1.22;padding:18px 34px 18px 70px;border-radius:18px;background:rgba(255,255,255,.1);border:4px solid rgba(255,255,255,.25)}
.dk .ln2 b{color:#FFE600}
.dk .ft2{position:absolute;left:0;right:0;top:1277px;text-align:center;font-weight:700;letter-spacing:.2em;font-size:24px;color:#9fb4dc}
'''
def page(n,inner,dark=False):
    foot='' if dark else f'<div class="rule2"></div><div class="foot">{MATERIA}</div><div class="pag">Pagina {n}</div>'
    if dark: foot=f'<div class="ft2">{MATERIA} · Pagina {n}</div>'
    return f'<div class="pg {"dk" if dark else ""}">{inner}{foot}</div>'
def head(label,title,lines=1):
    return f'<div class="logo">{LOGO}</div><div class="rule"></div><div class="label">{esc(label)}</div><div class="title" style="width:1760px;font-size:68px;top:190px">{esc(title)}</div><div class="bar" style="top:290px"></div>'
def keys_row(keys,top): return f'<div class="kc" style="top:{top}px">'+''.join(f'<span>{esc(k)}</span>' for k in keys[:5])+'</div>'
def build():
    P=[]; num=0
    # copertina: solo materia e titolo (grafica della copertina delle slide)
    arg=''.join(f'<li><b>{n}</b>{esc(t)}</li>' for n,t in ARG.items())
    cov=f'<div class="logo">{LOGO}</div><div class="rule"></div><div class="label">{MATERIA.replace(" V","")} · Videolezione</div><div class="title" style="font-size:120px;top:240px;width:1760px">{esc(TITOLO)}</div><div class="bar" style="top:420px"></div>'
    P.append(page(1,cov))
    for p in PROF:
        for i,sc in enumerate(p['scenes']):
            n=PG[(p['id'],i)]
            if sc['kind']=='cover': continue
            arg_n=sc.get('arg',p['arg'])
            if sc['kind']=='cards':
                t,c=cards_of(sc['page'])
                ch=''.join(card_html(x,'') for x in c)
                P.append(page(n,head(LAB[arg_n],t)+f'<div id="cards" style="position:absolute;left:80px;top:330px;width:1760px">{ch}</div>'+keys_row(sc['keys'],1190)))
            else:
                cap=sc['cap']
                P.append(page(n,head(LAB[arg_n],'')+f'<div style="position:absolute;left:80px;top:170px;width:1760px;height:1000px;display:flex;align-items:center;justify-content:center"><img alt="{re.sub("<[^>]+>","",cap)}" src="file:///tmp/w/op/{sc["img"]}.png" style="max-width:1760px;max-height:1000px;box-shadow:0 12px 34px rgba(70,80,100,.3)"></div><div class="cap" style="top:1190px;width:1760px;font-size:34px">{cap}</div>'+keys_row(sc['keys'],1225) if False else head(LAB[arg_n],'')+f'<div style="position:absolute;left:80px;top:170px;width:1760px;height:980px;display:flex;align-items:center;justify-content:center"><img alt="{re.sub("<[^>]+>","",cap)}" src="file:///tmp/w/op/{sc["img"]}.png" style="max-width:1760px;max-height:980px;box-shadow:0 12px 34px rgba(70,80,100,.3)"></div><div class="cap" style="top:1170px;width:1760px;font-size:34px">{cap}</div>'))
    last=max(PG.values()); n=last
    # pagine di ripasso (come nel video): pillole, glossario, ripasso finale, compiti
    from anim import PILL, GLOS, RIP, COMP
    for k in range(1,7):
        n+=1; L=''.join(f'<div class="ln2" style="top:{360+i*130}px"><span></span>{esc(x)}</div>' for i,x in enumerate(PILL[k]))
        P.append(page(n,f'<div class="k2" style="top:120px">Pillola di ripasso</div><div class="h2" style="top:190px;font-size:70px">{esc(ARG[k])}</div>{L}',True))
    for g in range(2):
        n+=1; L=''.join(f'<div class="ln2" style="top:{300+i*170}px"><b>{esc(t)}</b> · {esc(x)}</div>' for i,(t,x) in enumerate(GLOS[g*5:g*5+5]))
        P.append(page(n,f'<div class="k2" style="top:120px">Glossario</div><div class="h2" style="top:190px;font-size:70px">Glossario · {g+1} di 2</div>{L}',True))
    n+=1; P.append(page(n,'<div class="k2" style="top:120px">Ripasso finale</div><div class="h2" style="top:190px;font-size:70px">Argomento per argomento</div>'+''.join(f'<div class="ln2" style="top:{330+i*130}px">{esc(x)}</div>' for i,x in enumerate(RIP)),True))
    n+=1; P.append(page(n,'<div class="k2" style="top:120px">Compiti</div><div class="h2" style="top:190px;font-size:70px">Svolgi i compiti qui sotto e premi «Consegna»</div>'+''.join(f'<div class="ln2" style="top:{360+i*220}px;font-size:36px">{i+1}. {esc(x)}</div>' for i,x in enumerate(COMP)),True))
    return P
def to_pdf(pages,out,css=CSS2):
    html=f'<!doctype html><html><head><meta charset="utf-8"><style>{css}html{{zoom:{ZOOM}}}</style></head><body>{"".join(pages)}</body></html>'
    f=out+'.html'; open(f,'w').write(html)
    js=f'''const {{chromium}}=require('playwright');(async()=>{{const b=await chromium.launch();const p=await b.newPage();await p.goto('file://{f}');await p.evaluate(()=>document.fonts.ready);await p.pdf({{path:'{out}',width:'297mm',height:'210mm',printBackground:true,tagged:true,outline:true,margin:{{top:0,right:0,bottom:0,left:0}}}});await b.close()}})()'''
    open('/tmp/w/b/pdf.js','w').write(js); r=subprocess.run(['node','/tmp/w/b/pdf.js'],capture_output=True,text=True)
    if r.returncode: raise SystemExit(r.stderr)
if __name__=='__main__':
    P=build(); to_pdf(P,f'{OUT}/Storia_arte_V_Lez8_dispensa_A4.pdf'); print(len(P),'pagine')
