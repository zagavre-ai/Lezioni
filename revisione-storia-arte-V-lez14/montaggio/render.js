// uso: node render.js jobs.json   jobs: [{html:"/abs.html", out:"/abs.png", w:1920,h:1080, eval:"js opz", checks:true}]
const {chromium}=require('playwright');const fs=require('fs');
(async()=>{
  const jobs=JSON.parse(fs.readFileSync(process.argv[2]));
  const br=await chromium.launch({args:['--no-sandbox','--allow-file-access-from-files']});
  const pg=await br.newPage({viewport:{width:1920,height:1080}});
  const rep=[];
  for(const j of jobs){
    await pg.goto('file://'+j.html);await pg.evaluate(()=>document.fonts.ready);
    if(j.eval){await pg.evaluate(j.eval)}
    await pg.waitForTimeout(60);
    const chk=await pg.evaluate(()=>{const bad=[];document.querySelectorAll('[data-chk]').forEach(e=>{const r=e.getBoundingClientRect();if(r.bottom>972||r.right>1900||e.scrollHeight>e.clientHeight+2)bad.push((e.dataset.chk||'')+':'+Math.round(r.bottom))});return bad});
    if(chk.length)rep.push({out:j.out,overflow:chk});
    await pg.screenshot({path:j.out});
  }
  await br.close();fs.writeFileSync(process.argv[2]+'.rep',JSON.stringify(rep));
})();
