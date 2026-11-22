// uso: node shot.js jobs.json   jobs=[{html,out,t?}]  ; l'html puo' definire render(t)
const {chromium}=require('playwright');const fs=require('fs'),path=require('path');
(async()=>{const jobs=JSON.parse(fs.readFileSync(process.argv[2]));
const b=await chromium.launch({args:['--allow-file-access-from-files']});const pg=await b.newPage({viewport:{width:1920,height:1080}});
let cur=null;
for(const j of jobs){ if(fs.existsSync(j.out)&&!j.force)continue;
 if(cur!==j.html){await pg.goto('file://'+path.resolve(j.html));await pg.evaluate(()=>document.fonts.ready);await pg.waitForTimeout(150);cur=j.html}
 if(j.t!==undefined)await pg.evaluate(t=>window.render&&window.render(t),j.t);
 await pg.screenshot({path:j.out,type:'png'});}
await b.close()})();
