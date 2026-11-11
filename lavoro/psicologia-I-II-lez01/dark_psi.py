import sys,os,json,shutil,subprocess,base64
from playwright.sync_api import sync_playwright
FZ='/home/claude/l1/fz/33157a64-Bricolage_GrotesqueDM_MonoFigtree'
import base64
LGW=base64.b64encode(open('/home/claude/logo/out/Telesio_logo_bianco.svg','rb').read()).decode()
FONTS="""
@font-face{font-family:'BG';font-weight:800;src:url('file://%(z)s/Bricolage_Grotesque/static/BricolageGrotesque-ExtraBold.ttf')}
@font-face{font-family:'FG';font-weight:500;src:url('file://%(z)s/Figtree/static/Figtree-Medium.ttf')}
@font-face{font-family:'FG';font-weight:700;src:url('file://%(z)s/Figtree/static/Figtree-Bold.ttf')}
@font-face{font-family:'FG';font-weight:800;src:url('file://%(z)s/Figtree/static/Figtree-ExtraBold.ttf')}
"""%{'z':FZ}
CSS=FONTS+"""
*{box-sizing:border-box;margin:0;padding:0}
body{background:#070C1F;width:1920px;height:1080px;overflow:hidden;font-family:'FG';color:#F3F5FA}
#bg{position:absolute;inset:0;background:radial-gradient(1400px 900px at 30% 20%,#13224A 0%,#0A1330 55%,#060A1B 100%)}
.orb{position:absolute;border-radius:50%;filter:blur(90px)}
#o1{width:900px;height:900px;background:#2060AF;opacity:.45}
#o2{width:700px;height:700px;background:#2060AF;opacity:.20}
#o3{width:620px;height:620px;background:#2060AF;opacity:.20}
#grid{position:absolute;inset:0;background-image:linear-gradient(rgba(255,255,255,.035) 1px,transparent 1px),linear-gradient(90deg,rgba(255,255,255,.035) 1px,transparent 1px);background-size:120px 120px;mask-image:radial-gradient(900px 600px at 50% 50%,#000,transparent);-webkit-mask-image:radial-gradient(900px 600px at 50% 50%,#000,transparent)}
#grain{position:absolute;inset:-100px;opacity:.10;mix-blend-mode:overlay;background-image:url("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='300' height='300'><filter id='n'><feTurbulence type='fractalNoise' baseFrequency='.9' numOctaves='2' stitchTiles='stitch'/></filter><rect width='300' height='300' filter='url(%23n)'/></svg>")}
#vig{position:absolute;inset:0;background:radial-gradient(ellipse at center,transparent 55%,rgba(0,0,0,.55) 100%)}
#logo{position:absolute;left:150px;top:78px;height:64px}
.abs{position:absolute}
.kick{font-weight:800;letter-spacing:.38em;font-size:30px;color:#FFE600;text-transform:uppercase;white-space:nowrap}
.kick span{display:inline-block}
.ttl{font-family:'BG';font-weight:800;color:#fff;line-height:1.0;letter-spacing:-.02em}
.mask{overflow:hidden;padding-bottom:14px}
.glass{background:rgba(255,255,255,.07);border:1.5px solid rgba(255,255,255,.18);border-radius:26px;backdrop-filter:blur(22px);-webkit-backdrop-filter:blur(22px);box-shadow:0 24px 60px rgba(0,0,0,.35)}
.ghost{font-family:'BG';font-weight:800;color:transparent;-webkit-text-stroke:3px rgba(255,255,255,.13);line-height:.8;white-space:nowrap}
.cy{color:#7FB2F0}.cu{color:#FFE600}.cr{color:#FF6B6B}
.bar7{height:8px;border-radius:8px;background:rgba(255,255,255,.18);overflow:hidden}
.bar7 i{display:block;height:100%;background:#FFE600;border-radius:8px}
"""
BODY="""<div id=bg></div><div class=orb id=o1></div><div class=orb id=o2></div><div class=orb id=o3></div><div id=grid></div>
<img id=logo src="data:image/svg+xml;base64,%s"><div id=scene></div><div id=grain></div><div id=vig></div>"""%LGW
JS=r"""
const E=x=>{x=Math.max(0,Math.min(1,x));return 1-Math.pow(1-x,3)};
const EB=x=>{x=Math.max(0,Math.min(1,x));const c=1.70158;return 1+(c+1)*Math.pow(x-1,3)+c*Math.pow(x-1,2)};
const EIO=x=>{x=Math.max(0,Math.min(1,x));return x<.5?4*x*x*x:1-Math.pow(-2*x+2,3)/2};
const $=id=>document.getElementById(id);
let SP=null;
function mk(h){$('scene').innerHTML=h}
window.init=function(sp){SP=sp;
 if(sp.type=='title'){
  const lines=sp.lines.map((l,i)=>`<div class=mask><div class="ttl ln" data-i=${i} style="font-size:${sp.fs||128}px">${l}</div></div>`).join('');
  mk(`<div class="abs ghost" id=gh style="left:1000px;top:90px;font-size:980px">${sp.num}</div>
  <div class="abs kick" id=kk style="left:160px;top:330px">${[...('Argomento '+sp.num+' / '+sp.total)].map(c=>`<span>${c==' '?'&nbsp;':c}</span>`).join('')}</div>
  <div class=abs id=tt style="left:160px;top:400px;width:1500px">${lines}</div>
  <div class=abs id=ln style="left:160px;top:${sp.lineY||720}px;height:6px;width:0;background:linear-gradient(90deg,#FFE600,#7FB2F0);border-radius:6px"></div>
  <div class="abs glass" id=ch style="left:160px;top:${(sp.lineY||720)+50}px;padding:26px 44px;font-weight:700;font-size:46px"><span class=cy>${sp.ex}</span></div>
  <div class="abs" id=pg style="left:160px;top:950px;display:flex;gap:14px">${Array.from({length:sp.total},(_,i)=>`<div class=bar7 style="width:92px"><i data-p=${i} style="width:${i<sp.num-1?100:0}%"></i></div>`).join('')}</div>`);
 }
 if(sp.type=='quiz'){
  mk(`<div class="abs ghost" id=gh style="left:900px;top:130px;font-size:620px;-webkit-text-stroke-color:rgba(127,178,240,.22)">?</div>
  <div class="abs kick" id=kk style="left:160px;top:300px;color:#7FB2F0">${[...'Pausa del video · Quiz'].map(c=>`<span>${c==' '?'&nbsp;':c}</span>`).join('')}</div>
  <div class=abs id=tt style="left:160px;top:350px"><div class=mask><div class="ttl ln" data-i=0 style="font-size:150px">${sp.act}</div></div><div class=mask style="max-width:1130px"><div class="ttl ln" data-i=1 style="font-size:66px;color:#FFE600;margin-top:10px;line-height:1.08">${sp.topic}</div></div></div>
  <div class="abs glass" id=ch style="left:160px;top:760px;padding:26px 44px;font-weight:700;font-size:40px">${sp.pts}</div>
  <div class="abs" id=hint style="left:160px;top:900px;font-weight:500;font-size:34px;color:rgba(243,245,250,.8)">Rispondi · premi <b class=cy>Check</b> · poi <b class=cy>Continua</b></div>
  <div class=abs id=ring style="left:1380px;top:420px;width:240px;height:240px"></div><div id=dots></div>`);
  $('dots').innerHTML=Array.from({length:22},(_,i)=>`<i class=abs data-d=${i} style="left:${1000+(i*83)%800}px;top:1080px;width:${8+(i%4)*4}px;height:${8+(i%4)*4}px;border-radius:50%;background:${['#7FB2F0','#FFE600','#fff'][i%3]};opacity:0"></i>`).join('');
  $('ring').innerHTML=`<div class=abs style="inset:0;border-radius:50%;border:4px solid #7FB2F0"></div><div class=abs style="inset:60px;border-radius:50%;background:#7FB2F0;display:flex;align-items:center;justify-content:center"><div style="margin-left:10px;border-left:44px solid #0B1530;border-top:28px solid transparent;border-bottom:28px solid transparent"></div></div>`;
 }
 if(sp.type=='repaso'){
  mk(`<div class="abs kick" id=kk style="left:160px;top:250px">${[...(sp.kicker||'Mini ripasso con voce')].map(c=>`<span>${c==' '?'&nbsp;':c}</span>`).join('')}</div>
  <div class=abs id=tt style="left:160px;top:320px"><div class=mask><div class="ttl ln" data-i=0 style="font-size:230px">RIPASSO</div></div><div class=mask><div class="ttl ln" data-i=1 style="font-size:70px;color:#7FB2F0;margin-top:6px;white-space:nowrap">${sp.topic}</div></div></div>
  <div class="abs" id=eq style="left:160px;top:790px;display:flex;gap:9px;align-items:flex-end;height:90px">${Array.from({length:34},(_,i)=>`<i data-e=${i} style="width:12px;border-radius:6px;background:linear-gradient(#7FB2F0,#2060AF);height:10px;display:block"></i>`).join('')}</div>
  <div class="abs glass" id=cap style="left:160px;top:900px;width:1600px;padding:18px 40px;font-weight:500;font-size:38px;min-height:96px;line-height:1.25"></div>`);
 }
 if(sp.type=='final'){
  const it=sp.items.map((x,i)=>`<div class="glass" data-c=${i} style="padding:16px 30px;display:flex;align-items:center;gap:22px"><div style="width:46px;height:46px;border-radius:50%;background:#FFE600;color:#0B1530;font-weight:800;font-size:26px;display:flex;align-items:center;justify-content:center">${i+1}</div><div><div style="font-weight:800;font-size:34px">${x[0]}</div><div style="font-weight:500;font-size:26px;color:#7FB2F0">${x[1]}</div></div></div>`).join('');
  mk(`<div class="abs kick" id=kk style="left:160px;top:230px">${[...'Lezione 1 · ¿De dónde eres?'].map(c=>`<span>${c==' '?'&nbsp;':c}</span>`).join('')}</div>
  <div class=abs id=tt style="left:160px;top:290px"><div class=mask><div class="ttl ln" data-i=0 style="font-size:150px">RESUMEN</div></div><div class=mask><div class="ttl ln" data-i=1 style="font-size:150px;color:#FFE600">RIEPILOGO</div></div></div>
  <div class="abs" id=its style="left:1030px;top:200px;width:740px;display:flex;flex-direction:column;gap:14px">${it}</div>
  <div class="abs" id=sub style="left:160px;top:690px;width:760px;font-weight:500;font-size:36px;line-height:1.35;color:rgba(243,245,250,.9)">${sp.sub}</div>`);
 }
};
window.draw=function(t,fr){
 const sp=SP;
 // sfondo: orb in parallasse, grana che cambia ad ogni frame
 $('o1').style.transform=`translate(${-200+Math.sin(t*.5)*160}px,${-150+Math.cos(t*.4)*90}px)`;
 $('o2').style.transform=`translate(${1250+Math.cos(t*.6)*140}px,${60+Math.sin(t*.5)*120}px)`;
 $('o3').style.transform=`translate(${900+Math.sin(t*.45)*180}px,${600+Math.cos(t*.55)*100}px)`;
 $('grain').style.transform=`translate(${(fr*37)%100-50}px,${(fr*53)%100-50}px)`;
 $('logo').style.opacity=E(t/.6)*.9;
 const out=sp.dur-.45, fo=1-E((t-out)/.45);
 $('scene').style.opacity=fo;$('scene').style.transform=`scale(${1+(1-fo)*.04})`;
 const kk=$('kk');if(kk)[...kk.children].forEach((s,i)=>{const v=E((t-.25-i*.025)/.4);s.style.opacity=v;s.style.transform=`translateY(${(1-v)*22}px)`});
 document.querySelectorAll('.ln').forEach(e=>{const i=+e.dataset.i;const v=E((t-.45-i*.16)/.65);e.style.transform=`translateY(${(1-v)*115}%)`});
 const gh=$('gh');if(gh){const v=E((t-.1)/1.1);gh.style.opacity=v;gh.style.transform=`translate(${(1-v)*160+t*-14}px,0)`}
 if(sp.type=='title'){
  $('ln').style.width=(E((t-1.0)/.7)*620)+'px';
  const c=$('ch'),v=EB((t-1.25)/.6);c.style.opacity=Math.min(1,v);c.style.transform=`translateY(${(1-v)*40}px) scale(${.92+.08*Math.min(1,v)})`;
  document.querySelectorAll('[data-p]').forEach(e=>{const i=+e.dataset.p;if(i==sp.num-1)e.style.width=(E((t-.5)/1.2)*100)+'%'});
  $('pg').style.opacity=E((t-.4)/.5);
 }
 if(sp.type=='quiz'){
  const c=$('ch'),v=EB((t-1.0)/.6);c.style.opacity=Math.min(1,v);c.style.transform=`translateY(${(1-v)*40}px)`;
  $('hint').style.opacity=E((t-1.5)/.5);
  const r=$('ring'),rv=EB((t-.6)/.7),pu=1+.06*Math.sin(t*6);r.style.opacity=Math.min(1,rv);r.style.transform=`scale(${rv*pu})`;
  document.querySelectorAll('[data-d]').forEach(e=>{const i=+e.dataset.d,s=(t*(120+i%5*40)+i*70)%1200;e.style.top=(1100-s)+'px';e.style.opacity=(s>50&&s<1000)?.55:0});
 }
 if(sp.type=='repaso'){
  document.querySelectorAll('[data-e]').forEach(e=>{const i=+e.dataset.e;const a=(Math.sin(t*9+i*.7)+Math.sin(t*5.3+i*1.9)*.8+Math.sin(t*13+i*.3)*.5)/2.3;e.style.height=(14+Math.abs(a)*74*E((t-.8)/.4))+'px'});
  $('eq').style.opacity=E((t-.6)/.4);
  const cap=$('cap');let cur='';for(const [a,b,tx] of sp.caps)if(t>=a&&t<b)cur=tx;
  if(cap.dataset.k!=cur){cap.dataset.k=cur;cap.innerHTML=cur;}
  cap.style.opacity=cur?1:0;cap.style.visibility=cur?'visible':'hidden';
 }
 if(sp.type=='final'){
  document.querySelectorAll('[data-c]').forEach(e=>{const i=+e.dataset.c;const v=EB((t-1.0-i*.32)/.55);e.style.opacity=Math.min(1,v);e.style.transform=`translateX(${(1-v)*120}px)`});
  $('sub').style.opacity=E((t-.8)/.6);
 }
}
"""
def render(spec,out,scale=0.5,fps=30):
    N=int(round(spec['dur']*fps));shutil.rmtree(out,ignore_errors=True);os.makedirs(out)
    html='<!doctype html><meta charset=utf-8><style>%s</style><body>%s'%(CSS,BODY)
    open(out+'/p.html','w').write(html)
    with sync_playwright() as p:
        b=p.chromium.launch(args=["--allow-file-access-from-files"]);pg=b.new_page(viewport={'width':1920,'height':1080},device_scale_factor=scale)
        pg.goto('file://'+os.path.abspath(out+'/p.html'));pg.evaluate("document.fonts.ready");pg.add_script_tag(content=JS)
        pg.evaluate("(s)=>init(s)",spec)
        for n in range(N):
            pg.evaluate("([t,f])=>draw(t,f)",[n/fps,n]);pg.screenshot(path='%s/%05d.jpg'%(out,n+1),type='jpeg',quality=93)
        b.close()
    subprocess.run(['ffmpeg','-y','-loglevel','error','-framerate',str(fps),'-i',out+'/%05d.jpg','-c:v','libx264','-preset','veryfast','-crf','17','-pix_fmt','yuv420p',out+'.mp4'],check=True)
if __name__=='__main__':
    spec=json.loads(sys.argv[1]);render(spec,sys.argv[2],float(sys.argv[3]) if len(sys.argv)>3 else .5)
