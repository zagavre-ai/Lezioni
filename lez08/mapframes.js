const {chromium}=require('playwright');const {spawn}=require('child_process');const fs=require('fs');
(async()=>{const [html,stepsf,total,wav,out,fin]=process.argv.slice(2);const S=JSON.parse(fs.readFileSync(stepsf));const T=parseFloat(total);const n=Math.floor(T*30);
const ff=spawn('ffmpeg',['-v','error','-y','-f','image2pipe','-framerate','30','-i','-','-i',wav,'-map','0:v','-map','1:a','-c:v','libx264','-preset','veryfast','-crf','18','-pix_fmt','yuv420p','-c:a','pcm_s16le','-shortest',out],{stdio:['pipe','inherit','inherit']});
const b=await chromium.launch();const p=await b.newPage({viewport:{width:1920,height:1080}});await p.goto('file://'+html);await p.waitForTimeout(500);
let last=null;for(let i=0;i<n;i++){const t=i/30;const mv=S.some(s=>Math.abs(t-s[2])<0.7||Math.abs(t-s[2]-s[3])<0.7);
 if(mv||!last){await p.evaluate(([S,t])=>render(S,t),[S,t]);last=await p.screenshot({type:'png'})}
 if(!ff.stdin.write(last))await new Promise(r=>ff.stdin.once('drain',r));if(i==n-1)fs.writeFileSync(fin,last)}
ff.stdin.end();await new Promise(r=>ff.on('close',r));await b.close()})();
