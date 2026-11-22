const {chromium}=require('playwright');const fs=require('fs');
(async()=>{
 const jobs=JSON.parse(fs.readFileSync(process.argv[2]));
 const b=await chromium.launch({args:['--no-sandbox','--allow-file-access-from-files']});
 const ctx=await b.newContext({viewport:{width:1920,height:1080},deviceScaleFactor:1});
 const p=await ctx.newPage();
 let n=0;
 for(const j of jobs){
  if(j.skip_if_exists&&fs.existsSync(j.out))continue;
  await p.setViewportSize({width:j.w||1920,height:j.h||1080});
  await p.goto('file://'+j.html);
  await p.evaluate(()=>document.fonts.ready);
  const m=await p.evaluate(()=>window.__overflow?window.__overflow():0);
  if(m)console.log('OVERFLOW',j.out,m);
  await p.screenshot({path:j.out,omitBackground:!!j.transparent});
  if(j.textout){const t=await p.evaluate(()=>{const o=[];const w=document.createTreeWalker(document.body,NodeFilter.SHOW_TEXT);let n;while(n=w.nextNode()){const s=n.textContent.replace(/\s+/g,' ').trim();if(!s)continue;if(n.parentElement.closest('script,style'))continue;const r=document.createRange();r.selectNodeContents(n);const rs=r.getClientRects();if(!rs.length)continue;const b=r.getBoundingClientRect();o.push({t:s,x:b.left,y:b.top,w:b.width,h:b.height});}return o;});fs.writeFileSync(j.textout,JSON.stringify(t));}
  n++;
 }
 console.log('rendered',n);await b.close();
})();
