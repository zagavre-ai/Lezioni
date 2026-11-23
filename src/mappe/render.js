// uso: node render.js <modo> <html> <uscita|-> [fps total]
const { chromium } = require('playwright');
const fs=require('fs');
(async()=>{
  const [mode,html,out,fps,total]=process.argv.slice(2);
  const br=await chromium.launch({args:['--no-sandbox','--font-render-hinting=none','--disable-gpu']});
  const vp=mode==='pdf'?{width:1123,height:794}:{width:1920,height:1080};
  const pg=await br.newPage({viewport:vp,deviceScaleFactor:1});
  await pg.goto('file://'+html+'?mode='+(mode==='frames'?'video':mode));
  await pg.waitForFunction('window.READY===true',null,{timeout:120000});
  if(mode==='still'){const ts=(total||'').split(',');for(const t of ts){await pg.evaluate(`render(${t})`);await pg.screenshot({path:out+'_'+t+'.png'});}}
  else if(mode==='png'||mode==='pdf'){
    await pg.evaluate('showAll()');
    const ov=await pg.evaluate('overlaps()');console.error('OVERLAPS',JSON.stringify(ov));
    fs.writeFileSync(out+'.rects.json',await pg.evaluate('rectsOut()'));
    if(mode==='png')await pg.screenshot({path:out});
    else await pg.pdf({path:out,width:'1123px',height:'794px',printBackground:true,pageRanges:'1'});
  }else{
    const n=parseInt(total),f=parseFloat(fps);let last=null,lastSig=null;
    for(let i=0;i<n;i++){
      const sig=await pg.evaluate(`render(${i/f})`);
      if(sig!==lastSig){last=await pg.screenshot({type:'jpeg',quality:94});lastSig=sig;}
      process.stdout.write(last);
    }
  }
  await br.close();
})();
