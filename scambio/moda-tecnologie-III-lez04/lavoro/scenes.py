import json, os, re, subprocess
BASE='/home/claude/prod'
CSS=open(f'{BASE}/base.css').read()
MAT="Tecnologie dei materiali e dei processi produttivi e organizzativi della moda"
DARK="""html,body{background:#0B1530}
.bg{position:absolute;inset:0;background:radial-gradient(ellipse at 20% 10%,#1B3A7A 0%,#0B1530 60%)}
.dk{color:#fff}.hl{background:linear-gradient(transparent 58%,#FFE600 58%,#FFE600 92%,transparent 92%);color:#fff;padding:0 6px}
.foot.dkf{color:#9DB4E0}
"""
JS_COMMON="""window.STEPS=[];function setSteps(s){window.STEPS=s}
const ease=x=>{x=Math.max(0,Math.min(1,x));return 1-Math.pow(1-x,3)};
function show(id,t0,t,d){const e=document.getElementById(id);if(!e)return;const p=ease((t-t0)/(d||0.5));e.style.opacity=p;e.style.transform=`translateY(${18*(1-p)}px)`}"""
def wr(name,html):
    p=f'{BASE}/html/{name}.html'; os.makedirs(f'{BASE}/html',exist_ok=True); open(p,'w').write(html); return p
def titolo(name,n,titolo_txt):
    h=f"""<!doctype html><html><head><meta charset="utf-8"><style>{CSS}{DARK}
.a{{position:absolute;left:160px;top:330px;font:700 30px FigB;letter-spacing:.2em;color:#FFE600;opacity:0}}
.b{{position:absolute;left:160px;top:400px;width:1500px;font:800 104px/1.08 Bri;color:#fff;opacity:0}}
.l{{position:absolute;left:160px;top:760px;height:10px;background:#FFE600;width:0}}
.c{{position:absolute;border-radius:50%;border:3px solid rgba(255,255,255,.12)}}
</style></head><body><div class="bg"></div>
<div class="c" id="c1" style="left:1250px;top:120px;width:620px;height:620px"></div><div class="c" id="c2" style="left:1420px;top:290px;width:420px;height:420px"></div>
<div class="a" id="a">ARGOMENTO {n}</div><div class="b" id="b">{titolo_txt}</div><div class="l" id="l"></div>
<div class="foot dkf" style="color:#9DB4E0">{MAT.upper()} · Prof.ssa Piera Caputi</div>
<script>{JS_COMMON}
function render(t){{show('a',0.2,t);show('b',0.5,t,0.7);document.getElementById('l').style.width=(900*ease((t-1.0)/1.0))+'px';
const r=(t*20)%360;document.getElementById('c1').style.transform=`scale(${{1+0.04*Math.sin(t*1.3)}})`;document.getElementById('c2').style.transform=`scale(${{1+0.06*Math.sin(t*1.7+1)}})`}}
</script></body></html>"""
    return wr(name,h)
def ripasso(name,titolo_txt,righe):
    """righe: html delle righe; steps = [[t,dur]] per ogni riga (voce)"""
    rows=''.join(f'<div class="r" id="r{i}"><span class="nn">{i+1}</span><span class="tx">{r}</span></div>' for i,r in enumerate(righe))
    h=f"""<!doctype html><html><head><meta charset="utf-8"><style>{CSS}{DARK}
.k2{{position:absolute;left:120px;top:90px;font:700 28px FigB;letter-spacing:.2em;color:#FFE600}}
.t2{{position:absolute;left:120px;top:140px;width:1650px;font:800 64px/1.1 Bri;color:#fff}}
.w{{position:absolute;left:120px;top:290px;width:1680px;display:flex;flex-direction:column;gap:18px}}
.r{{display:flex;gap:26px;align-items:center;padding:14px 28px;border-radius:16px;background:rgba(255,255,255,.07);border:3px solid rgba(255,255,255,.12);opacity:0;font:400 38px/1.3 Fig;color:#fff}}
.r b{{font-family:FigB;color:#FFE600;font-weight:700}}.nn{{flex:0 0 54px;height:54px;border-radius:50%;background:#FFE600;color:#0B1530;font:800 32px/54px Bri;text-align:center}}
.r.on{{background:rgba(255,230,0,.16);border-color:#FFE600}}
</style></head><body><div class="bg"></div><div class="k2">PILLOLA DI RIPASSO</div><div class="t2">{titolo_txt}</div><div class="w">{rows}</div>
<div class="foot dkf" style="color:#9DB4E0">{MAT.upper()} · Prof.ssa Piera Caputi</div>
<script>{JS_COMMON}
function render(t){{STEPS.forEach((s,i)=>{{const e=document.getElementById('r'+i);if(!e)return;const p=ease((t-s[0]+0.15)/0.45);e.style.opacity=p;e.style.transform=`translateY(${{14*(1-p)}}px)`;e.classList.toggle('on',t>=s[0]-0.1&&t<s[0]+s[1]+0.2)}})}}
</script></body></html>"""
    return wr(name,h)
def quizscheda(name,titolo_txt):
    h=f"""<!doctype html><html><head><meta charset="utf-8"><style>{CSS}{DARK}
.a{{position:absolute;left:160px;top:300px;font:700 30px FigB;letter-spacing:.2em;color:#FFE600;opacity:0}}
.b{{position:absolute;left:160px;top:370px;width:1500px;font:800 150px/1.0 Bri;color:#fff;opacity:0}}
.c{{position:absolute;left:160px;top:600px;width:1500px;font:400 48px/1.3 Fig;color:#fff;opacity:0}}
.d{{position:absolute;left:160px;top:720px;width:1500px;font:400 40px/1.3 Fig;color:#9DB4E0;opacity:0}}
</style></head><body><div class="bg"></div><div class="a" id="a">METTITI ALLA PROVA</div><div class="b" id="b">Quiz</div>
<div class="c" id="c">5 domande · per continuare serve almeno l'<span class="hl">80%</span></div><div class="d" id="d">{titolo_txt}</div>
<div class="foot dkf" style="color:#9DB4E0">{MAT.upper()} · Prof.ssa Piera Caputi</div>
<script>{JS_COMMON}
function render(t){{show('a',0.4,t);show('b',0.6,t,0.5);show('c',1.2,t);show('d',1.7,t)}}</script></body></html>"""
    return wr(name,h)
def approf(name,label,titolo_txt,img,cards):
    cs=''.join(f'<div class="card" id="c{i}">{c}</div>' for i,c in enumerate(cards))
    h=f"""<!doctype html><html><head><meta charset="utf-8"><style>{CSS}
.k{{color:#2060AF}}.im{{position:absolute;left:60px;top:130px;width:760px;height:830px;display:flex;align-items:center;justify-content:center;opacity:0}}
.im img{{max-width:720px;max-height:700px;object-fit:contain}}
.ti{{position:absolute;left:880px;top:104px;width:980px;font:800 58px/1.08 Bri;color:#0B1530;opacity:0}}
.wp{{position:absolute;left:880px;top:290px;width:980px;display:flex;flex-direction:column;gap:26px}}
.card{{position:relative;opacity:0;transform:none}}.card.old{{border-color:#CBD5E1}}
.badge{{position:absolute;left:60px;top:92px}}
</style></head><body><div class="k">{label}</div><div class="rule"></div>
<div class="im" id="im"><img src="file://{img}"></div><div class="ti" id="ti">{titolo_txt}</div><div class="wp">{cs}</div>
<div class="foot">{MAT.upper()} · Prof.ssa Piera Caputi</div>
<script>{JS_COMMON}
function render(t){{show('im',0.2,t,0.8);show('ti',0.5,t);const z=1+0.03*Math.min(t/20,1);document.querySelector('#im img').style.transform=`scale(${{z}})`;
STEPS.forEach((s,i)=>{{const e=document.getElementById('c'+i);if(!e)return;const p=ease((t-s[0]+0.15)/0.45);e.style.opacity=t>=s[0]-0.15?(t>=s[0]+s[1]+0.2?0.55:1):0;e.style.transform=`translateY(${{14*(1-p)}}px)`;e.classList.toggle('on',t>=s[0]-0.1&&t<s[0]+s[1]+0.2)}})}}
</script></body></html>"""
    return wr(name,h)

def copertina(name,titolo_txt,punti,img,anno="III anno",kicker=MAT):
    li=''.join(f'<div id="l{i}"><span class="cn">{i+1}</span>{p}</div>' for i,p in enumerate(punti))
    h=f"""<!doctype html><html><head><meta charset="utf-8"><style>{CSS}
#k1{{position:absolute;left:100px;top:130px;width:1250px;font:700 24px/1.3 FigB;letter-spacing:.1em;color:#2060AF}}
#t1{{position:absolute;left:96px;top:215px;width:1300px;font:800 112px/1.02 Bri;opacity:0;color:#0B1530}}
#s1{{position:absolute;left:100px;top:470px;font:600 34px FigS;color:#2060AF;opacity:0}}
#li{{position:absolute;left:100px;top:560px;font:400 38px/1.5 Fig;width:1250px}}
#li div{{opacity:0;display:flex;align-items:center;gap:20px;margin-bottom:6px}}#li b{{font-family:FigB}}
.cn{{display:inline-block;width:46px;height:46px;border:3px solid #0B1530;border-radius:50%;text-align:center;font:500 28px/46px Fig;flex:0 0 46px}}
#fig{{position:absolute;right:90px;top:90px;width:520px;height:880px;display:flex;align-items:center;justify-content:center;opacity:0}}#fig img{{max-width:520px;max-height:760px}}
</style></head><body><div id="k1">{kicker.upper()}</div><div id="t1">{titolo_txt}</div><div id="s1">Tecnico Sistema Moda · {anno} · Prof.ssa Piera Caputi</div>
<div id="li">{li}</div><div id="fig"><img src="file://{img}"></div><div class="foot">{kicker.upper()} · Prof.ssa Piera Caputi</div>
<script>{JS_COMMON}
function render(t){{show('t1',0.2,t,0.8);show('s1',0.8,t);document.getElementById('fig').style.opacity=ease((t-0.4)/1.2);
const s=STEPS[0]?STEPS[0][0]:1;{len(punti)}&&[...Array({len(punti)}).keys()].forEach(i=>show('l'+i,s+4.0+i*1.6,t));}}
</script></body></html>"""
    return wr(name,h)
def ritorno(name,sotto):
    h=f"""<!doctype html><html><head><meta charset="utf-8"><style>{CSS}
#f{{position:absolute;left:0;top:0;width:1920px;height:1080px;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:30px}}
#a{{font:800 78px Bri;opacity:0}}#b{{font:600 40px FigS;color:#2060AF;opacity:0}}</style></head><body>
<div id="f"><div id="a">Ora torniamo dalla professoressa</div><div id="b">{sotto}</div></div><div class="foot">{MAT.upper()} · Prof.ssa Piera Caputi</div>
<script>{JS_COMMON}
function render(t){{show('a',0.2,t,0.6);show('b',1.0,t,0.6)}}</script></body></html>"""
    return wr(name,h)
COL={'centro':('#FFDCC6','#C2410C'),'sequenza':('#DCEEFB','#1D4ED8'),'parola':('#FFF3BF','#A16207'),'esempio':('#DDF3E4','#15803D'),'conseguenza':('#EAE1FA','#6D28D9')}
LEG={'centro':'concetto centrale','sequenza':'date e sequenze','parola':'parole chiave','esempio':'esempi','conseguenza':'conseguenze'}
def mappa(name,titolo_txt,m,label='MAPPA'):
    """m: {'domanda','centro','rami':[{'nome','tipo','figli':[{'nome','tipo'}]}]} -> (html, ordine_nodi)"""
    rami=m['rami']; slots=sum(max(1,len(r.get('figli',[]))) for r in rami)
    top,H=170,830; sh=H/slots; nodes=[];lines=[]
    nodes.append(dict(id=0,txt=m['centro'],tipo='centro',x=60,y=top+H/2-95,w=380,h=190,parent=None))
    y=top; used=set()
    for r in rami:
        n=max(1,len(r.get('figli',[]))); bh=min(150,n*sh-14) if n==1 else 150
        cy=y+n*sh/2
        bid=len(nodes); nodes.append(dict(id=bid,txt=r['nome'],tipo=r['tipo'],x=560,y=cy-bh/2,w=520,h=bh,parent=0)); used.add(r['tipo'])
        for j,f in enumerate(r.get('figli',[])):
            fy=y+j*sh+sh/2; fh=min(120,sh-14)
            nodes.append(dict(id=len(nodes),txt=f['nome'],tipo=f['tipo'],x=1200,y=fy-fh/2,w=660,h=fh,parent=bid)); used.add(f['tipo'])
        y+=n*sh
    used.add('centro')
    ns=''.join(f'<div class="n" id="N{n["id"]}" style="left:{n["x"]}px;top:{n["y"]:.0f}px;width:{n["w"]}px;height:{n["h"]:.0f}px;background:{COL[n["tipo"]][0]};border:4px solid {COL[n["tipo"]][1]};{"font:800 46px/1.1 Bri;" if n["id"]==0 else ""}"><span>{n["txt"]}</span></div>' for n in nodes)
    ls=''
    for n in nodes:
        if n['parent'] is None: continue
        p=nodes[n['parent']]; x1=p['x']+p['w']; y1=p['y']+p['h']/2; x2=n['x']; y2=n['y']+n['h']/2
        ls+=f'<path id="L{n["id"]}" d="M{x1},{y1} C{(x1+x2)/2},{y1} {(x1+x2)/2},{y2} {x2},{y2}" stroke="#0B1530" stroke-width="5" fill="none" marker-end="url(#ah)"/>'
    leg=''.join(f'<span><i style="background:{COL[t][0]};border-color:{COL[t][1]}"></i>{LEG[t]}</span>' for t in COL if t in used)
    h=f"""<!doctype html><html><head><meta charset="utf-8"><style>{CSS}
.n{{position:absolute;box-sizing:border-box;display:flex;align-items:center;justify-content:center;text-align:center;padding:8px 18px;border-radius:16px;font:400 34px/1.2 Fig;color:#0B1530;opacity:0}}
.n.hl{{box-shadow:0 0 0 8px #FFE600}}
.q{{position:absolute;left:60px;top:92px;font:800 40px Bri;color:#0B1530}}
</style></head><body><div class="k">{label}</div><div class="leg">{leg}</div><div class="rule"></div><div class="q">{titolo_txt}</div>
<svg width="1920" height="1080" style="position:absolute;left:0;top:0"><defs><marker id="ah" markerWidth="8" markerHeight="8" refX="6" refY="4" orient="auto"><path d="M0,0 L8,4 L0,8 z" fill="#0B1530"/></marker></defs>{ls}</svg>{ns}
<div class="foot">{MAT.upper()} · Prof.ssa Piera Caputi</div>
<script>{JS_COMMON}
function render(t){{STEPS.forEach((s,i)=>{{const e=document.getElementById('N'+i);if(!e)return;const p=ease((t-s[0]+0.2)/0.45);e.style.opacity=p;e.style.transform=`translateY(${{16*(1-p)}}px)`;
const l=document.getElementById('L'+i);if(l)l.style.opacity=ease((t-s[0]+0.6)/0.5);const last=(i==STEPS.length-1);e.classList.toggle('hl',t>=s[0]-0.15&&t<s[0]+s[1]+0.3&&!(last&&t>s[0]+s[1]+0.5))}})}}
</script></body></html>"""
    return wr(name,h),nodes
