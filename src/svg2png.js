const {chromium}=require('playwright');const fs=require('fs');
(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:660,height:208},deviceScaleFactor:2});
const svg=fs.readFileSync('/home/user/Lezioni/kit/docenti/Telesio_logo_blu.svg','utf8');
await p.setContent(`<html><body style="margin:0;background:transparent"><img style="width:660px" src="data:image/svg+xml;base64,${Buffer.from(svg).toString('base64')}"></body></html>`);
await p.screenshot({path:'logo_blu.png',omitBackground:true});await b.close()})();
