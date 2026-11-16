// uso: node render.js job.json  ; job = [{out, k, t, rows:[[bold,testo]], on:i, done:n, pg}]
const {chromium}=require('playwright');const fs=require('fs');
(async()=>{const J=JSON.parse(fs.readFileSync(process.argv[2]));const b=await chromium.launch();const p=await b.newPage({viewport:{width:1920,height:1080}});
await p.goto('file://'+process.cwd()+'/slide.html');
for(const j of J){await p.evaluate(j=>{
 k.textContent=j.k;t.textContent=j.t;
 const tl=Math.ceil(j.t.length*34/1280);const ty=215;t.style.top=ty+'px';
 const tb=ty+(j.t.length>38?135:75)+14;bar.style.top=tb+'px';
 card.style.top=(tb+34)+'px';
 card.innerHTML=j.rows.map((r,i)=>`<div class="row ${i==j.on?'on':(i<j.on||j.on==-2?'done':'')}"><b>${r[0]}</b>: ${r[1]}</div>`).join('');
 document.querySelector('.row:last-child').style.borderBottom='0';
 pg.textContent='Pagina '+j.pg;
 document.querySelector('.prof').style.display=j.noprof?'none':'';document.querySelector('.name').style.display=j.noprof?'none':'';
},j);await p.waitForTimeout(80);await p.screenshot({path:j.out});}
await b.close()})();
