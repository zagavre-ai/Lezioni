import json,html as H
from render import *
COL={'pesca':('#FFD9C2','#F28B50'),'celeste':('#D3EAFB','#3C9AE0'),'paglierino':('#FFF1B8','#D9AE00'),'menta':('#CFF1DE','#2FAE72'),'lilla':('#E4DAF8','#8467D6')}
LEG=[('pesca','Concetto centrale'),('celeste','Date e sequenze'),('paglierino','Parole chiave'),('menta','Esempi e opere'),('lilla','Conseguenze')]
# riquadri: id,x,y,w,testo,colore,grassetto ; archi: da,a,etichetta,tipo ('v' dall'alto al basso; 'l' bus a sinistra; 'b' bus verticale a sinistra del figlio)
MAPS={
'A':dict(title="Come nasce la Repubblica italiana?",boxes=[
 ('r',620,290,640,"Le italiane e gli italiani",'pesca',1),
 ('a',250,470,300,"1946",'celeste',0),('b',1150,470,300,"1948",'celeste',0),
 ('c',80,650,400,"la repubblica",'paglierino',1),('d',540,650,500,"l'Assemblea costituente",'paglierino',1),
 ('e',1060,650,500,"la Democrazia cristiana",'paglierino',1),('f',1060,820,500,"il Fronte popolare democratico",'lilla',0)],
 edges=[('r','a',"nel",'v'),('r','b',"nel",'v'),('a','c',"scelgono",'v'),('a','d',"eleggono",'v'),('b','e',"votano",'v'),('e','f',"che sconfigge",'v')]),
'B':dict(title="Quali sono i principali avvenimenti dell'età detta del centrismo?",boxes=[
 ('r',560,330,880,"La crescita economica dell'età del centrismo",'pesca',1),
 ('a',110,500,520,"l'appartenenza al blocco occidentale",'paglierino',0),('b',110,640,520,"la partecipazione alla Cee",'paglierino',0),('c',110,780,520,"il basso costo del lavoro",'paglierino',0),
 ('d',700,500,520,"cambiamenti nel costume e nei consumi",'paglierino',1),('e',700,720,520,"elettrodomestici, televisori, automobili e scooter",'menta',0),
 ('f',1300,500,500,"intensi flussi migratori",'paglierino',1),('g',1370,680,430,"dal Sud al Nord",'menta',0),('h',1370,810,430,"dalle campagne alle città",'menta',0)],
 edges=[('r','a',"si basa su",'l'),('r','b','','l'),('r','c','','l'),('r','d',"causa",'v'),('r','f','','v'),('d','e',"con la diffusione di",'v'),('f','g',"diretti",'b'),('f','h','','b')]),
'C':dict(title="Come nascono i governi di centrosinistra?",boxes=[
 ('r',700,290,520,"La Democrazia cristiana",'pesca',1),('a',700,450,520,"Fanfani e Moro",'paglierino',0),
 ('b',150,640,560,"un'alleanza con il Partito socialista di Nenni",'paglierino',0),('c',1000,640,520,"governi di centrosinistra (dal 1962)",'celeste',1),
 ('d',740,830,500,"la nazionalizzazione dell'energia elettrica",'lilla',0),('e',1290,830,500,"la riforma della scuola media",'lilla',0)],
 edges=[('r','a',"con",'v'),('a','b',"raggiunge",'v'),('a','c',"e forma",'v'),('c','d',"che approvano",'v'),('c','e','','v')]),
}
ORDER={'A':['r','a','b','c','d','e','f'],'B':['r','a','b','c','d','e','f','g','h'],'C':['r','a','b','c','d','e']}
JS="""
(spec)=>{const st=document.getElementById('stage');st.innerHTML='';const NS='http://www.w3.org/2000/svg';
const svg=document.createElementNS(NS,'svg');svg.setAttribute('width',1920);svg.setAttribute('height',1080);svg.style.position='absolute';svg.style.left=0;svg.style.top=0;st.appendChild(svg);
const df=document.createElementNS(NS,'defs'),mk=document.createElementNS(NS,'marker');mk.setAttribute('id','ah');mk.setAttribute('markerWidth',14);mk.setAttribute('markerHeight',14);mk.setAttribute('refX',12);mk.setAttribute('refY',7);mk.setAttribute('orient','auto');mk.setAttribute('markerUnits','userSpaceOnUse');const pp=document.createElementNS(NS,'path');pp.setAttribute('d','M1,1 L13,7 L1,13 z');pp.setAttribute('fill','#0B1530');mk.appendChild(pp);df.appendChild(mk);svg.appendChild(df);
const B={};
spec.boxes.forEach(b=>{const d=document.createElement('div');d.className='mb';d.style.cssText=`left:${b.x}px;top:${b.y}px;width:${b.w}px;background:${b.f};border-color:${b.c};font-weight:${b.b?800:500}`;d.textContent=b.t;d.dataset.id=b.id;st.appendChild(d);B[b.id]=d});
const R=id=>{const r=B[id].getBoundingClientRect();return{x:r.left,y:r.top,w:r.width,h:r.height,cx:r.left+r.width/2,cy:r.top+r.height/2,b:r.bottom,r:r.right}};
function path(d,lab,lx,ly){const p=document.createElementNS(NS,'path');p.setAttribute('d',d);p.setAttribute('fill','none');p.setAttribute('stroke','#0B1530');p.setAttribute('stroke-width',3);p.setAttribute('marker-end','url(#ah)');p.dataset.to=spec._cur;svg.appendChild(p);
 if(lab){const t=document.createElement('div');t.className='el';t.textContent=lab;t.style.left=lx+'px';t.style.top=ly+'px';t.dataset.to=spec._cur;st.appendChild(t)}}
spec.edges.forEach(e=>{spec._cur=e[1];const a=R(e[0]),b=R(e[1]);
 if(e[3]=='v'){const my=(a.b+b.y)/2;path(`M${a.cx},${a.b} L${a.cx},${my} L${b.cx},${my} L${b.cx},${b.y-3}`,e[2],(a.cx+b.cx)/2+(a.cx==b.cx?12:-26),a.cx==b.cx?my-34:my-34)}
 if(e[3]=='l'){const bx=62;path(`M${a.x},${a.y+a.h/2} L${bx},${a.y+a.h/2} L${bx},${b.cy} L${b.x-3},${b.cy}`,e[2],70,a.y+a.h/2-38)}
 if(e[3]=='b'){const bx=b.x-34,ax=a.x+30;path(`M${ax},${a.b} L${ax},${b.cy} L${b.x-3},${b.cy}`,e[2],ax+8,a.b+2)}
});
window.__B=B;}
"""
HC=""".mb{position:absolute;border:4px solid;border-radius:20px;padding:14px 20px;font-size:36px;line-height:1.25;text-align:center;color:#0B1530;box-shadow:0 8px 22px rgba(60,70,90,.14)}
.mb.hot{background:#FFE600 !important;border-color:#0B1530 !important}
.el{position:absolute;font-size:30px;font-weight:700;background:#fff;padding:0 8px;color:#0B1530;white-space:nowrap}
"""
def map_step(key,step,out,page,total=1,idx=1):
    """step: numero di riquadri mostrati (1..n); l'ultimo è acceso in giallo; step>n = mappa intera ferma"""
    m=MAPS[key];order=ORDER[key]
    spec=dict(boxes=[dict(id=i,x=x,y=y,w=w,t=t,f=COL[c][0],c=COL[c][1],b=bd) for i,x,y,w,t,c,bd in m['boxes']],edges=m['edges'])
    lab=f'Mappa{"" if total==1 else f" · {idx} di {total}"}'
    h=f'<img id=logo src="data:image/svg+xml;base64,{LOGO}"><div class=hl style="top:124px"></div><div class=lab>{lab}</div>'
    if m['title']:h+=f'<div class=ttl style="top:196px;font-size:52px;width:930px;line-height:1.1">{H.escape(m["title"])}</div>'
    h+='<div class=legend>'+''.join(f'<span style="background:{COL[c][0]};border-color:{COL[c][1]}">{t}</span>' for c,t in LEG)+'</div>'
    if key=='B':h+='<div style="position:absolute;left:80px;top:925px;font-size:28px;font-weight:700;color:#0B1530">Cee: Comunità economica europea</div>'
    h+='<div id=stage></div><div class=hl style="top:981px"></div><div class=foot style="left:80px">STORIA</div><div class=foot style="right:80px">Pagina '+str(page)+'</div>'
    vis=order[:min(step,len(order))];hot=order[step-1] if step<=len(order) else None
    if os.path.exists(out):return out
    pg=rr().pg;os.makedirs(os.path.dirname(out),exist_ok=True)
    f=W+'/st/_map.html';open(f,'w').write('<!doctype html><meta charset=utf-8><style>%s%s</style><body>%s'%(CSS,HC,h));pg.goto('file://'+f);pg.evaluate("document.fonts.ready");pg.wait_for_timeout(30)
    pg.evaluate(JS,spec)
    pg.evaluate("([vis,hot])=>{document.querySelectorAll('.mb').forEach(b=>{b.style.visibility=vis.includes(b.dataset.id)?'visible':'hidden';b.classList.toggle('hot',b.dataset.id===hot)});document.querySelectorAll('svg path,.el').forEach(e=>{e.style.visibility=vis.includes(e.dataset.to)?'visible':'hidden'})}",[vis,hot])
    pg.screenshot(path=out+'.t.png');os.rename(out+'.t.png',out);return out
