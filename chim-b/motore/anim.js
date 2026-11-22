// Libreria di animazioni vettoriali (SVG 1330x900) per le lezioni di Chimica. Ogni animazione ha init(root,a) e draw(root,p,d,a).
// p = secondi dall'inizio dell'animazione; a.steps = tempi relativi dei passi (letti dalla trascrizione).
const NS='http://www.w3.org/2000/svg';
const clamp=(x,a=0,b=1)=>Math.max(a,Math.min(b,x));
const E=x=>{x=clamp(x);return 1-Math.pow(1-x,3)};
const pr=(p,t0,d=0.6)=>E((p-t0)/d);
function S(tag,at,par){const e=document.createElementNS(NS,tag);for(const k in at)e.setAttribute(k,at[k]);if(par)par.appendChild(e);return e}
function T(par,x,y,txt,sz=34,col='#0B1530',w='Fig',anc='start',extra={}){const e=S('text',Object.assign({x,y,'font-size':sz,fill:col,'text-anchor':anc,'font-family':w==='B'?'FigB':w==='H'?'Bri':'Fig'},extra),par);e.textContent=txt;return e}
function R(par,x,y,w,h,fill,stroke,sw=4,rx=14){return S('rect',{x,y,width:w,height:h,rx,fill,stroke:stroke||'none','stroke-width':sw},par)}
function mk(root,title){root.innerHTML='';const s=S('svg',{width:1330,height:900,viewBox:'0 0 1330 900'},root);if(title){T(s,0,40,title,46,'#0B1530','H')};return s}
function show(e,v){e.setAttribute('opacity',v.toFixed(3))}
function setT(e,dx,dy){e.setAttribute('transform',`translate(${dx.toFixed(1)},${dy.toFixed(1)})`)}
const C={blu:'#2060AF',notte:'#0B1530',pe:'#FFDCC6',peB:'#C2410C',pa:'#FFF3BF',paB:'#A16207',me:'#DDF3E4',meB:'#15803D',ce:'#DCEEFB',ceB:'#1D4ED8',li:'#EADFF7',liB:'#7E22CE',gr:'#CBD5E1',gi:'#FFE600'};
const stp=(a,i,def)=>(a.steps&&a.steps[i]!=null)?a.steps[i]:def;
const ANIM={};
// ---------- sequenza di passi con frecce (processi) ----------
// a.passi=[{t:'Sgranatura',s:'rottura delle parti legnose',ic:'rottura'}], a.titolo
function icona(g,nome,cx,cy){
 const col=C.notte;
 if(nome==='rottura'){S('rect',{x:cx-50,y:cy-12,width:100,height:24,rx:6,fill:'#D9B382',stroke:col,'stroke-width':3,transform:`rotate(-12 ${cx} ${cy})`},g);S('path',{d:`M${cx-6} ${cy-24} l10 22 l-10 14 l12 24`,stroke:C.peB,'stroke-width':5,fill:'none'},g)}
 else if(nome==='battitura'){S('rect',{x:cx-60,y:cy+8,width:120,height:22,rx:5,fill:'#D9B382',stroke:col,'stroke-width':3},g);S('rect',{x:cx+10,y:cy-52,width:22,height:70,rx:5,fill:C.blu,stroke:col,'stroke-width':3,transform:`rotate(25 ${cx+20} ${cy-20})`},g)}
 else if(nome==='pettine'){for(let i=0;i<9;i++)S('line',{x1:cx-48+i*12,y1:cy-6,x2:cx-48+i*12,y2:cy+44,stroke:col,'stroke-width':4},g);S('rect',{x:cx-56,y:cy-22,width:112,height:18,rx:5,fill:C.blu,stroke:col,'stroke-width':3},g);for(let i=0;i<5;i++)S('path',{d:`M${cx-40+i*20} ${cy-70} q8 20 0 40 t4 40`,stroke:'#C9A66B','stroke-width':4,fill:'none'},g)}
 else if(nome==='acqua'){S('rect',{x:cx-60,y:cy-30,width:120,height:80,rx:10,fill:'#BFE0F5',stroke:col,'stroke-width':3},g);for(let i=0;i<4;i++)S('rect',{x:cx-44+i*24,y:cy-48,width:10,height:84,rx:4,fill:'#C9A66B',stroke:col,'stroke-width':2},g);S('path',{d:`M${cx-56} ${cy-6} q14 -10 28 0 t28 0 t28 0 t28 0`,stroke:C.ceB,'stroke-width':3,fill:'none'},g)}
 else if(nome==='prato'){S('rect',{x:cx-64,y:cy+20,width:128,height:22,rx:6,fill:'#9BD07E',stroke:col,'stroke-width':3},g);for(let i=0;i<5;i++)S('rect',{x:cx-50+i*22,y:cy+10,width:12,height:12,fill:'#C9A66B'},g);S('circle',{cx:cx+30,cy:cy-30,r:22,fill:C.gi,stroke:col,'stroke-width':3},g)}
 else if(nome==='fiocco'){S('path',{d:`M${cx-50} ${cy+30} q-10 -40 20 -50 q20 -30 50 -6 q36 4 20 40 q-10 20 -40 16 z`,fill:'#fff',stroke:col,'stroke-width':4},g)}
 else if(nome==='soda'){S('path',{d:`M${cx-34} ${cy-50} h68 l-8 30 v40 q0 30 -26 30 q-26 0 -26 -30 v-40 z`,fill:'#E9DDF7',stroke:col,'stroke-width':4},g);T(g,cx,cy+16,'NaOH',28,col,'B','middle')}
 else if(nome==='forno'){S('rect',{x:cx-56,y:cy-40,width:112,height:80,rx:10,fill:'#F4F6FA',stroke:col,'stroke-width':4},g);S('rect',{x:cx-40,y:cy-24,width:80,height:48,rx:6,fill:C.pa,stroke:col,'stroke-width':3},g);for(let i=0;i<3;i++)S('path',{d:`M${cx-24+i*24} ${cy+4} q-8 -10 0 -18 q8 10 0 18`,fill:C.peB},g)}
 else if(nome==='macchina'){S('rect',{x:cx-60,y:cy-10,width:120,height:50,rx:8,fill:'#F4F6FA',stroke:col,'stroke-width':4},g);S('circle',{cx:cx-30,cy:cy-26,r:22,fill:C.ce,stroke:col,'stroke-width':4},g);S('circle',{cx:cx+30,cy:cy-26,r:22,fill:C.ce,stroke:col,'stroke-width':4},g)}
 else {S('circle',{cx,cy,r:44,fill:C.ce,stroke:col,'stroke-width':4},g)}
}
ANIM.passi={init(root,a){const s=mk(root,a.titolo);root._s=s;const n=a.passi.length;const w=Math.min(300,(1330-(n-1)*50)/n);root._w=w;
  const y0=150;root._g=a.passi.map((p,i)=>{const g=S('g',{opacity:0},s);const x=i*(w+50);R(g,x,y0,w,560,'#F4F6FA',C.gr,4,20);
    S('circle',{cx:x+w/2,cy:y0+46,r:30,fill:C.blu},g);T(g,x+w/2,y0+58,String(i+1),38,'#fff','B','middle');
    icona(g,p.ic,x+w/2,y0+200);
    const lines=wrap(p.t,Math.floor(w/22));lines.forEach((l,k)=>T(g,x+w/2,y0+330+k*40,l,36,C.notte,'B','middle'));
    if(p.s){wrap(p.s,Math.floor(w/16)).forEach((l,k)=>T(g,x+w/2,y0+400+lines.length*8+k*34,l,28,'#334155','Fig','middle'))}
    if(i<n-1)S('path',{d:`M${x+w+6} ${y0+200} h38 m-14 -14 l14 14 l-14 14`,stroke:C.blu,'stroke-width':6,fill:'none','stroke-linecap':'round'},g);
    return g})},
  draw(root,p,d,a){const n=a.passi.length;root._g.forEach((g,i)=>{const t=stp(a,i,0.6+i*(d-2)/n);show(g,pr(p,t,0.6));setT(g,0,18*(1-pr(p,t,0.6)))})}};
function wrap(txt,max){const w=txt.split(' ');const out=[];let cur='';w.forEach(x=>{if((cur+' '+x).trim().length>max&&cur){out.push(cur);cur=x}else cur=(cur+' '+x).trim()});if(cur)out.push(cur);return out}
// ---------- barre con numeri che crescono ----------
// a.voci=[{n:'Cellulosa',v:77,txt:'dal 70% all\'84%',col:'pe'}], a.max=100
ANIM.barre={init(root,a){const s=mk(root,a.titolo);root._s=s;const n=a.voci.length;const h=Math.min(90,640/n);root._r=a.voci.map((v,i)=>{const y=120+i*(h+26);const g=S('g',{opacity:0},s);
    T(g,0,y+h*0.66,v.n,34,C.notte,'B');R(g,360,y,820,h,'#F4F6FA',C.gr,3,12);const b=R(g,360,y,10,h,C[v.col||'ce'],C[(v.col||'ce')+'B']||C.ceB,4,12);const tx=T(g,1196,y+h*0.66,'',36,C.notte,'B');return {g,b,tx,v,h}})},
  draw(root,p,d,a){root._r.forEach((r,i)=>{const t=stp(a,i,0.5+i*(d-2)/a.voci.length);const k=pr(p,t,1.2);show(r.g,pr(p,t,0.4));r.b.setAttribute('width',Math.max(10,(820*r.v.v/(a.max||100))*k));r.tx.textContent=k>0.98?r.v.txt:Math.round(r.v.v*k)+'%'})}};
// ---------- sezione del fusto ----------
ANIM.fusto={init(root,a){const s=mk(root,'La struttura del fusto');root._s=s;const cx=450,cy=480;
  root._c=[];
  const ring=(r,fill,st,sw)=>{const e=S('circle',{cx,cy,r,fill,stroke:st,'stroke-width':sw,opacity:0},s);root._c.push(e);return e};
  ring(330,'#B98B5A','#6B4423',6);                      // corteccia
  ring(300,'#E7CDA2','#B98B5A',3);                      // floema zona
  // fasci liberiani (vasi liberiani) disposti a cerchio sotto la corteccia
  root._f=[];for(let i=0;i<22;i++){const an=i/22*Math.PI*2,rr=268;const f=S('ellipse',{cx:cx+rr*Math.cos(an),cy:cy+rr*Math.sin(an),rx:20,ry:13,transform:`rotate(${an*180/Math.PI+90} ${cx+rr*Math.cos(an)} ${cy+rr*Math.sin(an)})`,fill:'#F7F1DF',stroke:'#C9A66B','stroke-width':3,opacity:0},s);root._f.push(f)}
  ring(236,'#9DC4E8','#2060AF',5);                      // cambio
  ring(222,'#D9B382','#8A5A2B',4);                      // legno
  root._x=[];for(let i=0;i<10;i++){const an=i/10*Math.PI*2,rr=140;const x=S('circle',{cx:cx+rr*Math.cos(an),cy:cy+rr*Math.sin(an),r:22,fill:'#C28A4A',stroke:'#6B4423','stroke-width':3,opacity:0},s);root._x.push(x)}
  ring(46,'#A9763A','#6B4423',3);
  const pt=(deg,r)=>[cx+r*Math.cos(deg*Math.PI/180),cy+r*Math.sin(deg*Math.PI/180)];
  const lab=[['Corteccia','all\'esterno',200,pt(-40,318),C.peB],['Vasi liberiani','nel floema, sotto la corteccia',330,pt(-12,268),C.meB],['Cambio','tessuto meristematico aderente al legno',640,pt(60,236),C.ceB],['Legno','zona centrale cilindrica',770,pt(40,150),C.paB]];
  root._l=lab.map(l=>{const g=S('g',{opacity:0},s);S('line',{x1:l[3][0],y1:l[3][1],x2:790,y2:l[2],stroke:l[4],'stroke-width':4},g);S('circle',{cx:l[3][0],cy:l[3][1],r:8,fill:l[4]},g);R(g,790,l[2]-48,530,100,'#fff',l[4],4,14);T(g,810,l[2]-6,l[0],36,C.notte,'B');T(g,810,l[2]+30,l[1],25,'#334155');return g});
 },
 draw(root,p,d,a){show(root._c[0],pr(p,stp(a,0,0.3)));show(root._c[1],pr(p,stp(a,0,0.5)));root._f.forEach((f,i)=>show(f,pr(p,stp(a,1,2)+i*0.05)));
  show(root._c[2],pr(p,stp(a,2,5)));show(root._c[3],pr(p,stp(a,3,7)));root._x.forEach((x,i)=>show(x,pr(p,stp(a,3,7)+0.3+i*0.04)));show(root._c[4],pr(p,stp(a,3,7)));
  root._l.forEach((g,i)=>show(g,pr(p,stp(a,i==0?0:i==1?1:i==2?2:3,0.8+i*1.5),0.6)))}};
// ---------- macerazione: steli in acqua, la colla pectica si scioglie, la fibra si separa ----------
const RND=(()=>{let x=12345;return()=>{x=(x*1664525+1013904223)%4294967296;return x/4294967296}})();
ANIM.macerazione={init(root,a){const s=mk(root,a.titolo||'La macerazione');root._s=s;
  R(s,0,200,1330,560,'#CFE8F7','#2060AF',5,26);
  S('path',{d:'M0 230 '+'q40 -14 80 0 t80 0 '.repeat(9),fill:'none',stroke:'#2060AF','stroke-width':5},s);
  root._st=[];root._fb=[];for(let i=0;i<7;i++){const x=120+i*150;const g=S('g',{opacity:0},s);
    S('rect',{x:x-26,y:300,width:52,height:380,rx:14,fill:'#B98B5A',stroke:'#6B4423','stroke-width':4},g);
    root._fb.push([S('rect',{x:x-14,y:330,width:28,height:320,rx:10,fill:'#F7F1DF',stroke:'#C9A66B','stroke-width':3},g),x]);root._st.push(g)}
  root._pec=[];for(let i=0;i<26;i++){root._pec.push([S('circle',{cx:90+RND()*1150,cy:380+RND()*260,r:7,fill:'#E4B83A',opacity:0},s),RND()])}
  root._b=[];for(let i=0;i<14;i++){root._b.push([S('circle',{cx:100+RND()*1120,cy:640,r:5+RND()*4,fill:'#fff',stroke:'#2060AF','stroke-width':2,opacity:0},s),RND()*420])}
  root._t1=T(s,0,150,'Gli steli restano sommersi nell\'acqua',38,C.notte,'B');root._t2=T(s,0,190,'',32,C.blu,'B');
  root._lg=S('g',{opacity:0},s);S('circle',{cx:20,cy:830,r:9,fill:'#E4B83A'},root._lg);T(root._lg,40,840,'sostanze pectiche e gommose che tengono unite le fibre',30,C.notte);
 },
 draw(root,p,d,a){root._st.forEach((g,i)=>show(g,pr(p,stp(a,0,0.5)+i*0.12)));
  show(root._t1,pr(p,stp(a,0,0.4)));root._t2.textContent=p>stp(a,1,3)?'I batteri sciolgono le sostanze pectiche e gommose':'';show(root._t2,pr(p,stp(a,1,3)));
  show(root._lg,pr(p,stp(a,1,3)));
  const k=clamp((p-stp(a,1,3))/Math.max(2,(stp(a,2,8)-stp(a,1,3))));
  root._pec.forEach(([e,r])=>{show(e,pr(p,stp(a,0,0.5)+r)*(1-clamp((k-r*0.7)*3)))});
  root._b.forEach(([e,ph])=>{e.setAttribute('cy',(690-((p*55+ph)%420)).toFixed(1));show(e,pr(p,0.8)*0.9)});
  root._fb.forEach(([f,x])=>{const w=28+26*k;f.setAttribute('width',w.toFixed(1));f.setAttribute('x',(x-w/2).toFixed(1))});
 }};
