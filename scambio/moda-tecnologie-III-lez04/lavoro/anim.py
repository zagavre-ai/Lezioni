# animazioni tecniche sopra la voce della prof: weave (intreccio su griglia), flow (processo a passi), fan (classificazione a ventaglio)
import json, sys
sys.path.insert(0,'/home/claude/prod')
from scenes import CSS, MAT, JS_COMMON, wr
CH="""
.k{color:#2060AF}.ti{position:absolute;left:60px;top:104px;width:1300px;font:800 54px/1.08 Bri;color:#0B1530}
.nome{position:absolute;left:1455px;top:500px;width:370px;padding:10px 0;text-align:center;background:#FFE600;color:#0B1530;font:700 30px FigB;transform:rotate(-3deg);border-radius:4px}
.ruolo{position:absolute;left:1440px;top:566px;width:400px;text-align:center;font:600 19px/1.25 FigS;color:#2060AF}
.cap{position:absolute;left:1455px;top:720px;width:400px;font:600 28px/1.3 FigS;color:#0B1530}
.cap div{margin-bottom:10px;padding:8px 14px;border-radius:10px;background:#F4F6FA;border:2px solid #CBD5E1;opacity:0}
"""
def chrome(label,title,body,js,extra_css="",caps=()):
    cp=''.join(f'<div id="cp{i}">{c}</div>' for i,c in enumerate(caps))
    return f"""<!doctype html><html><head><meta charset="utf-8"><style>{CSS}{CH}{extra_css}</style></head><body>
<div class="k">{label}</div><div class="rule"></div><div class="ti">{title}</div>{body}
<div class="nome">Prof.ssa Piera Caputi</div><div class="ruolo">{MAT}<br>Tecnico Sistema Moda · III anno</div><div class="cap">{cp}</div>
<div class="foot">{MAT.upper()} · Prof.ssa Piera Caputi</div><script>{JS_COMMON}
function caps(t,tot){{const n={len(caps)};for(let i=0;i<n;i++){{const e=document.getElementById('cp'+i);const s=1.0+i*(tot-3)/Math.max(n,1);const p=ease((t-s)/0.5);e.style.opacity=p}}}}
{js}</script></body></html>"""
def weave(name,label,title,mat,rapporto=None,caps=(),tot=30,cell=None):
    R=len(mat);C=len(mat[0]);cell=cell or min(56,int(560/max(R,C)))
    W=C*cell;H=R*cell;fx,fy=90,260;gx=fx+W+140
    body=f'<svg width="1920" height="1080" style="position:absolute;left:0;top:0" id="sv"></svg><div style="position:absolute;left:{fx}px;top:{fy-60}px;font:700 28px FigB;color:#2060AF">Tessuto: ordito e trama</div><div style="position:absolute;left:{gx}px;top:{fy-60}px;font:700 28px FigB;color:#2060AF">Messa in carta</div>'
    js=f"""const M={json.dumps(mat)},R={R},C={C},cell={cell},fx={fx},fy={fy},gx={gx},RP={json.dumps(rapporto)};const TOT={tot};
const sv=document.getElementById('sv');const NS='http://www.w3.org/2000/svg';
function el(n,a,p){{const e=document.createElementNS(NS,n);for(const k in a)e.setAttribute(k,a[k]);(p||sv).appendChild(e);return e}}
// riga 0 in basso (numerazione dall'angolo in basso a sinistra)
const cells=[];
for(let c=0;c<C;c++)el('rect',{{x:fx+c*cell+cell*0.3,y:fy,width:cell*0.4,height:R*cell,fill:'#2060AF',opacity:0.9}});
for(let r=0;r<R;r++){{const row=[];const y=fy+(R-1-r)*cell;
 const weft=el('rect',{{x:fx,y:y+cell*0.18,width:0,height:cell*0.64,fill:'#F59E0B'}});
 const tops=[];for(let c=0;c<C;c++){{if(M[r][c]=='1'){{tops.push(el('rect',{{x:fx+c*cell+cell*0.3,y:y+cell*0.18,width:cell*0.4,height:cell*0.64,fill:'#2060AF',opacity:0}}))}}else tops.push(null)}}
 const sq=[];for(let c=0;c<C;c++){{const g=el('rect',{{x:gx+c*cell,y:y,width:cell,height:cell,fill:'#fff',stroke:'#0B1530','stroke-width':2}});const b=el('rect',{{x:gx+c*cell+1,y:y+1,width:cell-2,height:cell-2,fill:'#0B1530',opacity:0}});sq.push([g,b,M[r][c]=='1'])}}
 cells.push({{weft,tops,sq}})}}
if(RP){{el('rect',{{x:gx,y:fy+(R-RP[1])*cell,width:RP[0]*cell,height:RP[1]*cell,fill:'none',stroke:'#E34234','stroke-width':6,id:'rp',opacity:0}})}}
const dt=(TOT-4)/R;
function render(t){{caps(t,TOT);for(let r=0;r<R;r++){{const s=1.2+r*dt;const p=Math.max(0,Math.min(1,(t-s)/(dt*0.8)));const o=cells[r];
 o.weft.setAttribute('width',p*C*cell);
 o.tops.forEach((e,c)=>{{if(e)e.setAttribute('opacity',(p*C>c+0.5)?1:0)}});
 o.sq.forEach(([g,b,on],c)=>{{b.setAttribute('opacity',on&&(p*C>c+0.5)?1:0)}})}}
 const rp=document.getElementById('rp');if(rp)rp.setAttribute('opacity',ease((t-(TOT-2.5))/0.5))}}"""
    return wr(name,chrome(label,title,body,js,caps=caps))
def flow(name,label,title,passi,caps=(),tot=30):
    n=len(passi);cols=3 if n>4 else n;rows=(n+cols-1)//cols;bw=min(430,int(1300/cols)-40);bh=170 if rows>1 else 230
    items=''
    for i,p in enumerate(passi):
        r,c=divmod(i,cols);x=60+c*(bw+50);y=260+r*(bh+90)
        items+=f'<div class="st" id="s{i}" style="left:{x}px;top:{y}px;width:{bw}px;height:{bh}px"><span class="nn">{i+1}</span><span>{p}</span></div>'
        if i<n-1 and c<cols-1: items+=f'<div class="ar" id="a{i}" style="left:{x+bw+4}px;top:{y+bh/2-22}px">➜</div>'
    css=""".st{position:absolute;box-sizing:border-box;padding:16px 20px;border-radius:16px;background:#F4F6FA;border:4px solid #CBD5E1;font:400 32px/1.25 Fig;color:#0B1530;display:flex;gap:14px;align-items:flex-start;opacity:0}
.st b{font-family:FigB}.st.on{border-color:#2060AF;box-shadow:0 0 0 7px #FFE600}.nn{flex:0 0 44px;height:44px;border-radius:50%;background:#2060AF;color:#fff;font:800 26px/44px Bri;text-align:center}
.ar{position:absolute;width:46px;font:700 40px FigB;color:#0B1530;opacity:0}"""
    js=f"""const N={n},TOT={tot};const dt=(TOT-3)/N;
function render(t){{caps(t,TOT);for(let i=0;i<N;i++){{const s=1.0+i*dt;const e=document.getElementById('s'+i);const p=ease((t-s)/0.5);e.style.opacity=p;e.style.transform=`translateY(${{14*(1-p)}}px)`;e.classList.toggle('on',t>=s&&t<s+dt);const a=document.getElementById('a'+i);if(a)a.style.opacity=ease((t-s-0.3)/0.5)}}}}"""
    return wr(name,chrome(label,title,items,js,css,caps))
def fan(name,label,title,centro,voci,caps=(),tot=30):
    n=len(voci);bh=min(120,int(760/n)-14);y0=250
    items=f'<div class="ce" id="ce">{centro}</div>'
    for i,v in enumerate(voci):
        y=y0+i*(bh+14); items+=f'<div class="fi" id="f{i}" style="top:{y}px;height:{bh}px">{v}</div><svg style="position:absolute;left:0;top:0" width="1920" height="1080"><path id="p{i}" d="M470,{y0+ (n*(bh+14)-14)/2} C560,{y0+(n*(bh+14)-14)/2} 540,{y+bh/2} 620,{y+bh/2}" stroke="#0B1530" stroke-width="5" fill="none" opacity="0"/></svg>'
    cy=y0+(n*(bh+14)-14)/2
    css=f""".ce{{position:absolute;left:60px;top:{cy-80}px;width:400px;height:160px;box-sizing:border-box;border-radius:16px;background:#FFDCC6;border:5px solid #C2410C;display:flex;align-items:center;justify-content:center;text-align:center;padding:10px;font:800 38px/1.1 Bri;color:#0B1530;opacity:0}}
.fi{{position:absolute;left:620px;width:740px;box-sizing:border-box;padding:8px 20px;border-radius:14px;background:#FFF3BF;border:4px solid #A16207;display:flex;align-items:center;font:400 32px/1.2 Fig;color:#0B1530;opacity:0}}.fi b{{font-family:FigB}}.fi.on{{box-shadow:0 0 0 7px #FFE600}}"""
    js=f"""const N={n},TOT={tot};const dt=(TOT-4)/N;
function render(t){{caps(t,TOT);document.getElementById('ce').style.opacity=ease((t-0.4)/0.5);for(let i=0;i<N;i++){{const s=1.6+i*dt;const e=document.getElementById('f'+i);const p=ease((t-s)/0.5);e.style.opacity=p;e.style.transform=`translateY(${{14*(1-p)}}px)`;e.classList.toggle('on',t>=s&&t<s+dt);document.getElementById('p'+i).setAttribute('opacity',p)}}}}"""
    return wr(name,chrome(label,title,items,js,css,caps))
