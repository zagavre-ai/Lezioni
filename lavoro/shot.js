// uso: node shot.js lista.json  -> lista: [{"html":"/path.html","png":"/path.png","omit":false}]
const { chromium } = require('playwright');
const fs=require('fs');
(async()=>{
  const L=JSON.parse(fs.readFileSync(process.argv[2]));
  const b=await chromium.launch(); const pg=await b.newPage({viewport:{width:1920,height:1080}});
  for(const it of L){
    await pg.goto('file://'+it.html); await pg.evaluate(()=>document.fonts.ready); await pg.waitForTimeout(80);
    await pg.screenshot({path:it.png,omitBackground:!!it.omit});
  }
  await b.close();
})();
