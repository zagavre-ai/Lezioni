// uso: node render.js cartella_html cartella_png  [pdf]
const {chromium}=require('playwright');const fs=require('fs');const path=require('path');
(async()=>{const [hd,pd]=process.argv.slice(2);const b=await chromium.launch();const p=await b.newPage({viewport:{width:1920,height:1080}});
for(const f of fs.readdirSync(hd).filter(x=>x.endsWith('.html')).sort()){
 const out=path.join(pd,f.replace('.html','.png'));
 if(fs.existsSync(out)&&fs.statSync(out).mtimeMs>fs.statSync(path.join(hd,f)).mtimeMs)continue;
 await p.goto('file://'+path.resolve(hd,f));await p.evaluate(()=>document.fonts.ready);await p.screenshot({path:out});}
await b.close();})();
