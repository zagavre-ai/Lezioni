// uso: node shot.js manifest.json  -> manifest: [{html:'file.html', out:'file.png', measure:true}]
const {chromium}=require('playwright');const fs=require('fs');
(async()=>{const m=JSON.parse(fs.readFileSync(process.argv[2]));const b=await chromium.launch();const p=await b.newPage({viewport:{width:1920,height:1080}});const res=[];
for(const it of m){await p.setContent(fs.readFileSync(it.html,'utf8'),{waitUntil:'load'});await p.evaluate(()=>document.fonts.ready);
 let r={};if(it.measure){r=await p.evaluate(()=>{const c=document.querySelector('#cards');if(!c)return{};const k=[...c.children].map(e=>{const b=e.getBoundingClientRect();return [b.top,b.bottom]});return {bottom:c.lastElementChild?c.lastElementChild.getBoundingClientRect().bottom:0,cards:k}})}
 if(it.out)await p.screenshot({path:it.out,omitBackground:!!it.transparent});res.push(r)}
fs.writeFileSync(process.argv[2]+'.res',JSON.stringify(res));await b.close()})();
