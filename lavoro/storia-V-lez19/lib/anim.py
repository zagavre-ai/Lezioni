# Motore di scene animate: HTML con attributi data-t0 (compare/si accende) e data-t1 (fine evidenza). Rende 30 fps, fotografa solo quando qualcosa cambia.
import sys,json,subprocess
sys.path.insert(0,'/home/claude/w19/lib')
from ui import *
JS="""
window.R=function(t){
 const ease=x=>{x=Math.max(0,Math.min(1,x));return 1-Math.pow(1-x,3)};
 let sig=[];
 document.querySelectorAll('[data-t0]').forEach(el=>{
  const t0=parseFloat(el.dataset.t0),t1=el.dataset.t1!==undefined?parseFloat(el.dataset.t1):null,dur=parseFloat(el.dataset.d||0.45);
  const p=ease((t-t0)/dur);
  const lo=parseFloat(el.dataset.lo||0);
  let op=lo+(1-lo)*p;
  if(el.dataset.out!==undefined){const o=parseFloat(el.dataset.out);op*=1-ease((t-o)/0.4)}
  el.style.opacity=op.toFixed(3);
  el.style.transform='translateY('+((1-p)*(parseFloat(el.dataset.dy||16))).toFixed(1)+'px)';
  let on=(t1!==null&&t>=t0&&t<t1);
  el.classList.toggle('on',on);
  sig.push(el.style.opacity+on);
 });
 return sig.join('|');
}
"""
DARK_CSS="""
.dk{position:absolute;left:0;top:0;width:1920px;height:1080px;background:radial-gradient(1200px 700px at 85% 15%,#1b3a8a 0%,transparent 60%),radial-gradient(900px 600px at 10% 95%,#16306f 0%,transparent 60%),#0B1530;color:#fff}
.on{}
"""
def render(html,tot,out,fps=30,extra_css=''):
    with B() as b:
        open('/tmp/pagina_a.html','w').write('<!doctype html><html><head><meta charset=utf-8><style>'+BASE+DARK_CSS+extra_css+'</style></head><body>'+html+'</body></html>');b.pg.goto('file:///tmp/pagina_a.html')
        b.pg.add_script_tag(content=JS);b.pg.wait_for_timeout(250)
        ff=subprocess.Popen(['ffmpeg','-v','error','-y','-f','image2pipe','-framerate',str(fps),'-i','-','-c:v','libx264','-preset','veryfast','-crf','16','-pix_fmt','yuv420p','-r',str(fps),out],stdin=subprocess.PIPE)
        last=None;buf=None
        for i in range(int(round(tot*fps))):
            s=b.pg.evaluate(f'R({i/fps})')
            if s!=last or buf is None: buf=b.pg.screenshot(type='jpeg',quality=94);last=s
            ff.stdin.write(buf)
        ff.stdin.close();ff.wait()
def still(html,out,t=999,extra_css=''):
    with B() as b:
        open('/tmp/pagina_a.html','w').write('<!doctype html><html><head><meta charset=utf-8><style>'+BASE+DARK_CSS+extra_css+'</style></head><body>'+html+'</body></html>');b.pg.goto('file:///tmp/pagina_a.html')
        b.pg.add_script_tag(content=JS);b.pg.wait_for_timeout(250);b.pg.evaluate(f'R({t})');b.pg.screenshot(path=out)
