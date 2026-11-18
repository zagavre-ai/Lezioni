# scene.py — copertina, animazioni di approfondimento (4c) e schema guidato di ripasso (4f) su fondo bianco, grafica Telesio.
# uso: python3 scene.py spec.json out.mp4 [fps=30] [procs=4]
# spec: {"type":"cover"|"anim"|"schema", "dur":s, ...}  Tutto è funzione del tempo t: draw(t).
import sys,os,json,shutil,subprocess,base64
from concurrent.futures import ProcessPoolExecutor
QUI=os.path.dirname(os.path.abspath(__file__))
FONT=os.path.join(QUI,'..','..','strumenti','font')
CHROME='/opt/pw-browsers/chromium-1243/chrome-linux64/chrome'
LOGO=base64.b64encode(open(QUI+'/Telesio_logo_blu.svg','rb').read()).decode()
HTML=r"""<!doctype html><meta charset=utf-8><style>
@font-face{font-family:BG;font-weight:800;src:url('file://@@F@@/BricolageGrotesque-ExtraBold.ttf')}
@font-face{font-family:FG;font-weight:500;src:url('file://@@F@@/Figtree-Medium.ttf')}
@font-face{font-family:FG;font-weight:700;src:url('file://@@F@@/Figtree-Bold.ttf')}
@font-face{font-family:FG;font-weight:800;src:url('file://@@F@@/Figtree-ExtraBold.ttf')}
*{box-sizing:border-box;margin:0;padding:0}
body{width:1920px;height:1080px;background:#fff;overflow:hidden;font-family:FG;color:#0B1530;position:relative}
.logo{position:absolute;left:80px;top:48px;height:60px}
.hr{position:absolute;left:80px;right:80px;height:1px;background:#E3E7EE}
.kick{position:absolute;left:80px;font-weight:700;font-size:28px;letter-spacing:.14em;text-transform:uppercase;color:#2060AF;white-space:nowrap}
.ttl{position:absolute;left:80px;font-family:BG;font-weight:800;color:#0B1530;line-height:1.05;letter-spacing:-.01em}
.bar{position:absolute;left:80px;height:6px;width:86px;border-radius:3px;background:#2060AF}
.foot{position:absolute;bottom:44px;font-weight:700;font-size:24px;letter-spacing:.12em;color:#2060AF;white-space:nowrap}
.card{position:absolute;background:#fff;border:3px solid #DDE2EA;border-radius:22px;box-shadow:0 10px 30px rgba(11,21,48,.07);padding:22px 34px 22px 100px}
.card.on{border-color:#FFE600;box-shadow:0 0 0 6px rgba(255,230,0,.35),0 10px 30px rgba(11,21,48,.08)}
.num{position:absolute;left:28px;top:50%;margin-top:-27px;width:54px;height:54px;border-radius:50%;background:#DDE2EA;color:#0B1530;font:800 28px FG;display:flex;align-items:center;justify-content:center}
.card.on .num{background:#FFE600}
.h{font-weight:800;font-size:30px;color:#2060AF;margin-bottom:6px}
.l{font-weight:500;font-size:34px;line-height:1.28}
.sub{position:absolute;left:80px;font-weight:700;font-size:30px;color:#2060AF;letter-spacing:.04em;text-transform:uppercase}
.pill{position:absolute;left:80px;top:150px;background:#E8EFFA;color:#2060AF;font-weight:800;font-size:24px;letter-spacing:.2em;padding:10px 22px;border-radius:999px}
.row{position:absolute;left:80px;width:1760px;border-radius:18px;display:flex;align-items:center;background:#fff;border:3px solid #DDE2EA}
.row.on{background:#FFF9C2;border-color:#FFE600}
.row .k{width:560px;background:#0B1530;color:#fff;font:800 34px BG;padding:0 32px;display:flex;align-items:center;height:100%;border-radius:15px 0 0 15px}
.row .d{flex:1;font-weight:700;font-size:34px;padding:0 36px;line-height:1.2}
.ag{position:absolute;background:#fff;border:2px solid #E3E7EE;border-radius:20px;box-shadow:0 14px 40px rgba(11,21,48,.08);padding:34px 48px}
.ag .lab{font-weight:800;font-size:22px;letter-spacing:.2em;color:#2060AF;margin-bottom:16px}
.ag li{font-weight:500;font-size:32px;line-height:1.55;margin-left:30px}
</style><body><img class=logo src="data:image/svg+xml;base64,@@L@@"><div id=s></div>
<script>
const E=x=>{x=Math.max(0,Math.min(1,x));return 1-Math.pow(1-x,3)};
const $=(h)=>{const d=document.createElement('div');d.innerHTML=h;return d.firstChild};
let S,els=[];
function el(css,html,cls){const d=document.createElement('div');d.style.cssText=css;if(cls)d.className=cls;d.innerHTML=html||'';document.getElementById('s').appendChild(d);return d}
function init(s){S=s;const R=document.getElementById('s');R.innerHTML='';els=[];
 if(s.type=='cover'){
  el('left:80px;top:160px','','');
  els.push({e:el('position:absolute;left:80px;top:200px;font-weight:800;font-size:30px;letter-spacing:.2em;color:#2060AF',s.materia.toUpperCase()+' · VIDEOLEZIONE'),a:0.2});
  els.push({e:el('position:absolute;left:80px;top:270px;width:1500px;font:800 92px/1.04 BG;letter-spacing:-.01em',s.titolo),a:0.5});
  els.push({e:el('position:absolute;left:80px;top:500px;width:90px;height:7px;border-radius:4px;background:#2060AF',''),a:0.8});
  const L=s.argomenti,c=Math.ceil(L.length/2);
  const li=(a)=>'<ul>'+a.map(x=>'<li>'+x+'</li>').join('')+'</ul>';
  els.push({e:el('position:absolute;left:80px;top:580px;width:1760px',`<div class=ag style="position:relative;display:flex;gap:80px"><div style="flex:1"><div class=lab>ARGOMENTI</div>${li(L.slice(0,c))}</div><div style="flex:1;padding-top:44px">${li(L.slice(c))}</div></div>`),a:1.2});
  el('left:80px;bottom:44px','','foot').innerHTML=s.materia.toUpperCase()+' · '+s.docente;
 }else{
  const t=s.arg;
  const k=el('top:150px','','kick');k.textContent=t;
  el('top:122px','','hr');
  el('bottom:84px','','hr');
  const f=el('','','foot');f.style.left='80px';f.textContent=s.materia.toUpperCase();
  s.sl=[];
  if(s.type=='anim'){ s.slides.forEach((sl,si)=>{
    const g=el('left:0;top:0;width:1920px;height:1080px;opacity:0','','');
    const fs=sl.t.length>38?64:78;
    el('left:80px;top:215px;width:1760px;font:800 '+fs+'px/1.05 BG;color:#0B1530','',null);
    const tt=document.createElement('div');tt.className='ttl';tt.style.cssText='top:205px;font-size:'+fs+'px;width:1760px';tt.textContent=sl.t;g.appendChild(tt);
    const br=document.createElement('div');br.className='bar';br.style.top=(205+fs*1.12)+'px';g.appendChild(br);
    let y=205+fs*1.12+40; if(sl.sub){const sb=document.createElement('div');sb.className='sub';sb.style.top=y+'px';sb.textContent=sl.sub;g.appendChild(sb);y+=56}
    const n=sl.items.length,avail=1080-84-30-y,gap=22;
    // altezza di ogni card in base al contenuto: si misura
    const cards=sl.items.map((it,ii)=>{const c=document.createElement('div');c.className='card';c.style.cssText='left:80px;width:1760px;top:'+y+'px;opacity:0';
      c.innerHTML='<div class=num>'+(ii+1)+'</div>'+(it.h?'<div class=h>'+it.h+'</div>':'')+it.lines.map(l=>'<div class=l>'+l+'</div>').join('');g.appendChild(c);return c});
    let yy=y;cards.forEach(c=>{c.style.top=yy+'px';yy+=c.offsetHeight+gap});
    s.sl.push({g,cards,sl});
  });}
  if(s.type=='schema'){
   const p=el('','','pill');p.textContent='PILLOLA DI '+s.materia.toUpperCase();
   const tt=el('top:205px;font-size:72px','','ttl');tt.textContent=s.titolo;
   el('top:'+(205+82)+'px','','bar');
   const n=s.rows.length,h=108,gap=20,y0=330;
   s.rr=s.rows.map((r,i)=>{const d=el('top:'+(y0+i*(h+gap))+'px;height:'+h+'px;opacity:0','<div class=k>'+r[0]+'</div><div class=d>'+r[1]+'</div>','row');return d});
  }
 }
}
function draw(t){
 if(S.type=='cover'){els.forEach(o=>{const k=E((t-o.a)/.7);o.e.style.opacity=k;o.e.style.transform='translateY('+(1-k)*24+'px)'})}
 else if(S.type=='anim'){
  S.sl.forEach(o=>{const a=o.sl.t0,b=o.sl.t1;let op=0;
    if(t>=a&&t<=b+.5){op=Math.min(E((t-a)/.5),1-Math.max(0,(t-b)/.5))}
    o.g.style.opacity=op;
    o.cards.forEach((c,i)=>{const it=o.sl.items[i];const k=E((t-it.t0+.35)/.5);c.style.opacity=k;c.style.transform='translateY('+(1-k)*30+'px)';
      c.className='card'+((t>=it.t0&&t<it.t1)?' on':'')})});
 }else{
  S.rr.forEach((d,i)=>{const r=S.rows[i];const k=E((t-r[2]+.3)/.5);d.style.opacity=k;d.style.transform='translateY('+(1-k)*24+'px)';d.className='row'+((t>=r[2]&&t<r[3])?' on':'')});
 }
}
</script>"""
def _render(args):
    spec,tmp,a,b,fps=args
    from playwright.sync_api import sync_playwright
    with sync_playwright() as p:
        br=p.chromium.launch(executable_path=CHROME,args=['--allow-file-access-from-files','--no-sandbox'])
        pg=br.new_page(viewport={'width':1920,'height':1080})
        pg.goto('file://'+tmp+'/p.html');pg.evaluate("document.fonts.ready");pg.evaluate("(s)=>init(s)",spec)
        for n in range(a,b):
            pg.evaluate("(t)=>draw(t)",n/fps);pg.screenshot(path='%s/%05d.jpg'%(tmp,n+1),type='jpeg',quality=94)
        br.close()
def render(spec,out,fps=30,procs=4):
    tmp=out+'_f';shutil.rmtree(tmp,ignore_errors=True);os.makedirs(tmp)
    open(tmp+'/p.html','w').write(HTML.replace('@@F@@',os.path.abspath(FONT)).replace('@@L@@',LOGO))
    N=int(round(spec['dur']*fps));ch=[(spec,os.path.abspath(tmp),i*N//procs,(i+1)*N//procs,fps) for i in range(procs)]
    with ProcessPoolExecutor(procs) as ex:list(ex.map(_render,ch))
    subprocess.run(['ffmpeg','-y','-loglevel','error','-framerate',str(fps),'-i',tmp+'/%05d.jpg','-vf','format=yuv420p','-c:v','libx264','-preset','veryfast','-crf','17',out],check=True)
    shutil.rmtree(tmp);return N
if __name__=='__main__':
    spec=json.load(open(sys.argv[1]));print(render(spec,sys.argv[2],int(sys.argv[3]) if len(sys.argv)>3 else 30,int(sys.argv[4]) if len(sys.argv)>4 else 4),'fotogrammi')
