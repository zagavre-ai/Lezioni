const {chromium}=require('playwright');const fs=require('fs');const path=require('path');
(async()=>{const [dir,outdir]=process.argv.slice(2);fs.mkdirSync(outdir,{recursive:true});const b=await chromium.launch();const p=await b.newPage({viewport:{width:1920,height:1080}});
for(const f of fs.readdirSync(dir).filter(x=>x.endsWith('.html')).sort()){
 await p.goto('file://'+path.resolve(dir,f));await p.evaluate(()=>document.fonts.ready);
 await p.pdf({path:path.join(outdir,f.replace('.html','.pdf')),format:'A4',landscape:true,printBackground:true,scale:0.5849,margin:{top:'0',right:'0',bottom:'0',left:'0'},pageRanges:'1'});}
await b.close();})();
