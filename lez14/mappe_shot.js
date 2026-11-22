// uso: node mappe_shot.js job.json   job={html,tot,outdir}  -> outdir/frames.json = [[file,nframes],...]
const {chromium}=require('playwright');const fs=require('fs'),path=require('path');
(async()=>{const j=JSON.parse(fs.readFileSync(process.argv[2]));fs.mkdirSync(j.outdir,{recursive:true});
const b=await chromium.launch({args:['--allow-file-access-from-files']});const pg=await b.newPage({viewport:{width:1920,height:1080}});
await pg.goto('file://'+path.resolve(j.html));await pg.evaluate(()=>document.fonts.ready);await pg.waitForTimeout(300);
const N=Math.round(j.tot*30);const sigs=await pg.evaluate(N=>{const a=[];for(let i=0;i<N;i++)a.push(window.sig(i/30));return a},N);
const runs=[];let last=null,cnt=0,uniq=0;
for(let i=0;i<N;i++){ if(sigs[i]!==last){ const f=path.join(j.outdir,'f'+String(i).padStart(5,'0')+'.png');
  await pg.evaluate(t=>window.render(t),i/30);await pg.screenshot({path:f,type:'png'});runs.push([f,1]);last=sigs[i];uniq++}
  else runs[runs.length-1][1]++;}
if(j.final){await pg.evaluate(t=>window.render(t),j.tot);await pg.screenshot({path:j.final,type:'png'})}
fs.writeFileSync(path.join(j.outdir,'frames.json'),JSON.stringify(runs));console.log('frame',N,'unici',uniq);await b.close()})();
