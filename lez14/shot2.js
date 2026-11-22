// uso: node shot2.js jobs.json ; jobs=[{html,transparent,frames:[{t,out}]}]
const {chromium}=require('playwright');const fs=require('fs'),path=require('path');
(async()=>{const jobs=JSON.parse(fs.readFileSync(process.argv[2]));
const b=await chromium.launch({args:['--allow-file-access-from-files']});
const pg=await b.newPage({viewport:{width:1920,height:1080}});
for(const j of jobs){
 await pg.goto('file://'+path.resolve(j.html));await pg.evaluate(()=>document.fonts.ready);await pg.waitForTimeout(200);
 for(const f of j.frames){ if(fs.existsSync(f.out))continue;
  await pg.evaluate(t=>window.render&&window.render(t),f.t);
  await pg.screenshot({path:f.out+'.tmp.png',type:'png',omitBackground:!!j.transparent});fs.renameSync(f.out+'.tmp.png',f.out);}
}
await b.close()})();
