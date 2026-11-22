const {chromium}=require('playwright');const fs=require('fs');
(async()=>{const jobs=JSON.parse(fs.readFileSync(process.argv[2]));const b=await chromium.launch();const p=await b.newPage({viewport:{width:1920,height:1080}});
for(const j of jobs){await p.goto('file://'+j.html);await p.evaluate(()=>document.fonts.ready);await p.screenshot({path:j.png});}
await b.close();console.log('done',jobs.length)})();
