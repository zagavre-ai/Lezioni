import sys,os,json,subprocess,html as H
sys.path.insert(0,'/home/claude/w/b')
from lib import *
import vox
JS='''
function ease(x){x=Math.max(0,Math.min(1,x));return 1-Math.pow(1-x,3)}
function render(t){
 document.querySelectorAll('[data-in]').forEach(e=>{
  const ti=parseFloat(e.dataset.in),d=parseFloat(e.dataset.d||0.5),dy=parseFloat(e.dataset.dy||26);
  let p=ease((t-ti)/d); if(e.dataset.out){const to=parseFloat(e.dataset.out); p=Math.min(p,1-ease((t-to)/0.4));}
  e.style.opacity=p; const sc=e.dataset.pop?(0.9+0.1*p):1;
  e.style.transform=(e.dataset.base||'')+` translateY(${(1-p)*dy}px) scale(${sc})`;
 });
 document.querySelectorAll('[data-lit]').forEach(e=>{
  const L=e.dataset.lit.split(';').filter(x=>x).map(s=>s.split(',').map(parseFloat));
  e.classList.toggle('on',L.some(([a,b])=>t>=a&&t<b));
 });
 document.querySelectorAll('[data-count]').forEach(e=>{
  const [f,to,t0,d,suf,pre]=e.dataset.count.split('|'); const p=ease((t-parseFloat(t0))/parseFloat(d));
  e.textContent=(pre||'')+Math.round(parseFloat(f)+(parseFloat(to)-parseFloat(f))*p)+(suf||'');
 });
 document.querySelectorAll('[data-draw]').forEach(e=>{
  const [t0,d]=e.dataset.draw.split(',').map(parseFloat); const L=e.getTotalLength?e.getTotalLength():100;
  e.style.strokeDasharray=L; e.style.strokeDashoffset=L*(1-ease((t-t0)/d)); e.style.opacity=(t>=t0-0.01)?1:0;
 });
 document.querySelectorAll('[data-bar]').forEach(e=>{
  const [a,b]=e.dataset.bar.split(',').map(parseFloat); e.style.width=(100*Math.max(0,Math.min(1,(t-a)/(b-a))))+'%';
 });
 document.querySelectorAll('.glow').forEach((e,i)=>{
  const k=t*0.35+i*2.1; e.style.transform=`translate(${Math.sin(k)*90}px,${Math.cos(k*0.8)*60}px)`;
 });
}
'''
BASE='''
html,body{margin:0}
.dark{background:#0B1530;color:#fff}
.dark .glow{position:absolute;border-radius:50%;filter:blur(90px);opacity:.55}
.chip{display:inline-block;font-weight:700;font-size:26px;letter-spacing:.14em;text-transform:uppercase;padding:8px 20px;border-radius:10px}
.h1{font-family:'Bricolage Grotesque';font-weight:800;line-height:1.05}
.yl{background:linear-gradient(transparent 58%,#FFE600 58%,#FFE600 92%,transparent 92%)}
'''
def scene(body,css='',dark=False):
    cls='dark' if dark else ''
    bg='#0B1530' if dark else '#ffffff'
    return head(BASE+css).replace('<body>',f'<body class="{cls}">')+body+f'<div id="fo" style="position:absolute;left:0;top:0;width:1920px;height:1080px;background:{bg};opacity:0;pointer-events:none;z-index:99"></div><script>{JS}\nfunction fade(t,d){{const f=Math.max(0,1-t/0.3,(t-(d-0.3))/0.3);document.getElementById("fo").style.opacity=Math.min(1,f)}}</script></body></html>'
def mp(path):return path
def render_scene(html,dur,out,fps=30,quality=88):
    pg=page(); pg.set_content(html); pg.wait_for_timeout(250)
    n=int(round(dur*fps))
    p=subprocess.Popen(['ffmpeg','-y','-v','error','-f','image2pipe','-framerate',str(fps),'-c:v','mjpeg','-i','-','-c:v','libx264','-preset','veryfast','-crf','14','-pix_fmt','yuv420p','-r',str(fps),'-an',out],stdin=subprocess.PIPE)
    last=None;lastb=None
    for i in range(n):
        t=i/fps
        pg.evaluate(f'render({t:.4f});fade({t:.4f},{dur:.4f})')
        b=pg.screenshot(type='jpeg',quality=quality)
        p.stdin.write(b)
    p.stdin.close(); p.wait()
    return n
_gain={}
def vgain(wavpath,target=-19.0):
    """gain (dB) per portare la voce a target LUFS mono (=-16 LUFS stereo doppio mono)"""
    if wavpath in _gain: return _gain[wavpath]
    r=subprocess.run(['ffmpeg','-hide_banner','-nostats','-i',wavpath,'-af','ebur128','-f','null','-'],capture_output=True,text=True).stderr
    import re
    m=re.findall(r'I:\s+(-?[\d.]+) LUFS',r); g=target-float(m[-1]) if m else 0
    _gain[wavpath]=max(-6,min(14,g)); return _gain[wavpath]
def mux(video,events,dur,out,keep_video=True):
    """events: [(file,start_s,kind)] kind: 'voce' (normalizza) o 'fx' (come e')"""
    ins=[];fl=[]
    for i,(f,t0,kind) in enumerate(events):
        ins+=['-i',f]
        g=vgain(f) if kind=='voce' else 0
        fl.append(f"[{i+1}:a]aformat=sample_rates=48000:channel_layouts=stereo,volume={g:.2f}dB,afade=t=in:st=0:d=0.03,adelay={int(t0*1000)}|{int(t0*1000)}[x{i}]")
    mix=''.join(f'[x{i}]' for i in range(len(events)))
    fg=';'.join(fl)+(';' if fl else '')+(f"{mix}amix=inputs={len(events)}:normalize=0,apad[am];[am]atrim=duration={dur:.3f},afade=t=out:st={dur-0.03:.3f}:d=0.03[ao]" if events else f"anullsrc=r=48000:cl=stereo,atrim=duration={dur:.3f}[ao]")
    cmd=['ffmpeg','-y','-v','error','-i',video]+ins+['-filter_complex',fg,'-map','0:v','-map','[ao]','-c:v','copy','-c:a','pcm_s16le','-ar','48000','-ac','2','-shortest',out]
    r=subprocess.run(cmd,capture_output=True,text=True)
    if r.returncode: raise SystemExit('mux '+out+': '+r.stderr[-800:])
SU=KIT+'/suoni/'
