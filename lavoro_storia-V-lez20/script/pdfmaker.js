const {chromium}=require('playwright');const fs=require('fs');
(async()=>{const jobs=JSON.parse(fs.readFileSync(process.argv[2]));const b=await chromium.launch();const p=await b.newPage({viewport:{width:1920,height:1080}});
for(const j of jobs){await p.goto('file://'+j.html);await p.evaluate(()=>document.fonts.ready);
await p.pdf({path:j.pdf,width:'1122.5px',height:'793.7px',scale:0.5846,printBackground:true,margin:{top:'0',right:'0',bottom:'0',left:'0'},pageRanges:'1'});}
await b.close();console.log('pdf',jobs.length)})();
