// Libreria di disegno delle mappe: layout calcolato sulle misure reali del testo, frecce ortogonali.
const COL={p:{bg:'#FFDCC6',bd:'#C2410C'},c:{bg:'#DCEEFB',bd:'#1D4ED8'},g:{bg:'#FFF3BF',bd:'#A16207'},m:{bg:'#DDF3E4',bd:'#15803D'},l:{bg:'#EBE3F7',bd:'#6D28D9'}};
const LEG=[['p','concetto centrale'],['c','date e sequenze'],['g','parole chiave'],['m','esempi e opere'],['l','conseguenze']];
const INK='#0B1530', YEL=[255,230,0];
function hex(h){return [1,3,5].map(i=>parseInt(h.substr(i,2),16))}
function mix(a,b,k){return 'rgb('+a.map((v,i)=>Math.round(v+(b[i]-v)*k)).join(',')+')'}
const clamp=x=>Math.max(0,Math.min(1,x)), ease=x=>1-Math.pow(1-clamp(x),3);
const FONTS=()=>Promise.all(['600 38px Fig','500 34px Fig','700 22px Fig','800 46px Bri'].map(f=>document.fonts.load(f))).then(()=>document.fonts.ready);
const TX=s=>s.replace(/'/g,'\u2019');
const NS='http://www.w3.org/2000/svg';
function el(tag,cls,parent,css){const e=document.createElement(tag);if(cls)e.className=cls;if(css)e.style.cssText=css;parent.appendChild(e);return e}

// costruisce la mappa dentro "root" (div 1920x1080). Ritorna oggetto con render(t) e issues
function buildMap(root,M,opts){
  opts=opts||{};
  root.classList.add('mp');
  const kick=el('div','kick',root);kick.textContent='MAPPA CONCETTUALE';
  const leg=el('div','leg',root);
  LEG.forEach(([c,t])=>{const s=el('span','',leg);const i=el('i','',s,`background:${COL[c].bg};border-color:${COL[c].bd}`);s.appendChild(document.createTextNode(t))});
  el('div','rule',root);
  const ti=el('div','ttl',root);ti.textContent=TX(M.titolo);
  if(!opts.nofooter){const f=el('div','foot',root);f.textContent='STORIA V'}
  const svg=document.createElementNS(NS,'svg');svg.setAttribute('width',1920);svg.setAttribute('height',1080);svg.style.cssText='position:absolute;left:0;top:0';root.appendChild(svg);
  const R={},N={};
  M.nodi.forEach(n=>{
    const d=el('div','bx'+(n.c==='p'?' ctr':''),root);
    d.style.background=COL[n.c].bg;d.style.borderColor=COL[n.c].bd;
    n.testo.split('\n').forEach((ln,i)=>{if(i)d.appendChild(document.createElement('br'));d.appendChild(document.createTextNode(TX(ln)))});
    if(n.w)d.style.minWidth=n.w+'px';
    root.appendChild(d);
    const w=d.offsetWidth,h=d.offsetHeight;
    let l=n.rel?R[n.rel[0]].l+n.rel[1]:(n.cx!==undefined?n.cx-w/2:(n.left!==undefined?n.left:n.right-w));
    d.style.left=l+'px';d.style.top=n.y+'px';
    R[n.id]={l:l,t:n.y,r:l+w,b:n.y+h,w:w,h:h,cx:l+w/2,cy:n.y+h/2};N[n.id]=d;
  });
  const E={},issues=[];
  const HL=24,HW=13,GAP=3;
  M.archi.forEach(e=>{
    const T=R[e.a],paths=[];
    const F=e.da?(Array.isArray(e.da)?e.da.map(i=>R[i]):R[e.da]):null;
    if(e.tipo==='v'){const x=e.x??F.cx;paths.push({pts:[[x,F.b],[x,T.t-GAP]],arrow:1})}
    else if(e.tipo==='bus'){const px=e.px??F.cx;paths.push({pts:[[px,F.b],[px,e.busy],[T.cx,e.busy],[T.cx,T.t-GAP]],arrow:1})}
    else if(e.tipo==='lato'){const sx=e.sx??(F.l+40);
      if(e.busy!==undefined){const px=e.px??F.cx;paths.push({pts:[[px,F.b],[px,e.busy],[sx,e.busy],[sx,T.cy],[T.l-GAP,T.cy]],arrow:1})}
      else paths.push({pts:[[sx,F.b],[sx,T.cy],[T.l-GAP,T.cy]],arrow:1})}
    else if(e.tipo==='unisci'){F.forEach(f=>paths.push({pts:[[f.cx,f.b],[f.cx,e.busy],[T.cx,e.busy]],arrow:0}));paths.push({pts:[[T.cx,e.busy],[T.cx,T.t-GAP]],arrow:1})}
    const g=document.createElementNS(NS,'g');svg.appendChild(g);
    paths.forEach(p=>{
      const pts=p.pts.map(a=>a.slice());
      if(p.arrow){const n=pts.length,a=pts[n-1],b=pts[n-2];const dx=Math.sign(a[0]-b[0]),dy=Math.sign(a[1]-b[1]);
        pts[n-1]=[a[0]-dx*HL,a[1]-dy*HL];
        const poly=document.createElementNS(NS,'polygon');
        const px=dx?[a[0],a[1]-HW,a[0]-dx*HL,a[1],a[0],a[1]+HW]:[a[0]-HW,a[1],a[0],a[1]-dy*HL,a[0]+HW,a[1]];
        const q=dx?[[a[0],a[1]],[a[0]-dx*HL,a[1]-HW],[a[0]-dx*HL,a[1]+HW]]:[[a[0],a[1]],[a[0]-HW,a[1]-dy*HL],[a[0]+HW,a[1]-dy*HL]];
        poly.setAttribute('points',q.map(z=>z.join(',')).join(' '));poly.setAttribute('fill',INK);g.appendChild(poly)}
      const pl=document.createElementNS(NS,'polyline');pl.setAttribute('points',pts.map(z=>z.join(',')).join(' '));
      pl.setAttribute('fill','none');pl.setAttribute('stroke',INK);pl.setAttribute('stroke-width',5);pl.setAttribute('stroke-linejoin','round');
      g.insertBefore(pl,g.firstChild);
    });
    let lab=null;
    if(e.et){
      const L=e.lp||{},p=paths[L.path||0].pts,s=L.seg||0;
      const a=p[s],b=p[s+1],t=L.t??.5;
      const x=a[0]+(b[0]-a[0])*t+(L.dx||0),y=a[1]+(b[1]-a[1])*t+(L.dy||0);
      lab=el('div','lab'+((L.pos||'c')==='c'?' lc':''),root);lab.textContent=TX(e.et);
      const w=lab.offsetWidth,h=lab.offsetHeight,pos=L.pos||'c';
      lab.style.top=(y-h/2)+'px';
      lab.style.left=(pos==='c'?x-w/2:(pos==='r'?x+14:x-14-w))+'px';
      lab._r={l:parseFloat(lab.style.left),t:y-h/2,r:parseFloat(lab.style.left)+w,b:y+h/2};
    }
    E[e.id]={g:g,lab:lab,paths:paths,def:e};
  });
  // ---- controlli geometrici
  const ids=Object.keys(R);
  for(let i=0;i<ids.length;i++){const a=R[ids[i]];
    if(a.l<40||a.r>1880||a.t<150||a.b>1035)issues.push('fuori area: '+ids[i]+' '+[a.l,a.t,a.r,a.b].map(Math.round));
    for(let j=i+1;j<ids.length;j++){const b=R[ids[j]];if(a.l<b.r+30&&b.l<a.r+30&&a.t<b.b+30&&b.t<a.b+30)issues.push('riquadri vicini/sovrapposti '+ids[i]+' '+ids[j])}}
  Object.values(E).forEach(en=>{
    const dd=en.def,own=[dd.a].concat(Array.isArray(dd.da)?dd.da:(dd.da?[dd.da]:[]));
    en.paths.forEach(p=>{for(let s=0;s<p.pts.length-1;s++){const a=p.pts[s],b=p.pts[s+1];
      const x0=Math.min(a[0],b[0]),x1=Math.max(a[0],b[0]),y0=Math.min(a[1],b[1]),y1=Math.max(a[1],b[1]);
      ids.forEach(id=>{if(own.includes(id))return;const r=R[id];if(x0<r.r+6&&x1>r.l-6&&y0<r.b+6&&y1>r.t-6)issues.push('freccia '+dd.id+' attraversa '+id)})}});
    if(en.lab){const r=en.lab._r;ids.forEach(id=>{const q=R[id];if(r.l<q.r+6&&r.r>q.l-6&&r.t<q.b+6&&r.b>q.t-6)issues.push('etichetta "'+dd.et+'" tocca '+id)});
      if(r.l<40||r.r>1880)issues.push('etichetta fuori '+dd.et)}
  });
  const labs=Object.values(E).filter(x=>x.lab).map(x=>x.lab._r);
  for(let i=0;i<labs.length;i++)for(let j=i+1;j<labs.length;j++){const a=labs[i],b=labs[j];if(a.l<b.r&&b.l<a.r&&a.t<b.b&&b.t<a.b)issues.push('etichette sovrapposte')}
  // ---- tempi
  const T=M.tempi; // {nodi:{id:{entra,acc:[[a,b]...]}}, archi:{id:t}}
  function render(t){
    let key=[];
    Object.keys(N).forEach(id=>{const tn=T.nodi[id];const p=ease((t-tn.entra)/0.3);
      let k=0;(tn.acc||[]).forEach(([a,b])=>{k=Math.max(k,Math.min(clamp((t-a)/0.15),clamp((b-t)/0.15)))});
      k=Math.round(k*50)/50;const pp=Math.round(p*50)/50;
      const d=N[id];d.style.opacity=pp;d.style.transform=`translateY(${(12*(1-pp)).toFixed(1)}px)`;
      d.style.background=mix(hex(COL[M.nodi.find(n=>n.id===id).c].bg),YEL,k);
      d.style.boxShadow=`0 0 0 ${(7*k).toFixed(1)}px rgba(255,230,0,${k}), 0 8px 18px rgba(70,80,100,.22)`;
      key.push(pp,k)});
    Object.keys(E).forEach(id=>{const p=Math.round(ease((t-T.archi[id])/0.3)*50)/50;E[id].g.style.opacity=p;if(E[id].lab)E[id].lab.style.opacity=p;key.push(p)});
    return key.join(',');
  }
  return {render,issues,R};
}
