# Schede di chiusura e sigla segnaposto (Psicologia): Verifica finale, intro Compiti, Compiti, sigla iniziale 15 s
import sys,os,json,base64,subprocess,shutil
from playwright.sync_api import sync_playwright
D='/home/claude/lezioni/psicologia-I-II-lez02/ch/'
FZ='/home/claude/l1/fz/33157a64-Bricolage_GrotesqueDM_MonoFigtree'
LGW=base64.b64encode(open('/home/claude/logo/out/Telesio_logo_bianco.svg','rb').read()).decode()
CSS="""
@font-face{font-family:'BG';font-weight:800;src:url('file://@@Z@@/Bricolage_Grotesque/static/BricolageGrotesque-ExtraBold.ttf')}
@font-face{font-family:'FG';font-weight:500;src:url('file://@@Z@@/Figtree/static/Figtree-Medium.ttf')}
@font-face{font-family:'FG';font-weight:700;src:url('file://@@Z@@/Figtree/static/Figtree-Bold.ttf')}
@font-face{font-family:'FG';font-weight:800;src:url('file://@@Z@@/Figtree/static/Figtree-ExtraBold.ttf')}
*{box-sizing:border-box;margin:0;padding:0}
body{width:1920px;height:1080px;overflow:hidden;font-family:'FG';color:#fff;background:#081127}
.mid{position:absolute;left:0;right:0;top:173px;height:669px;background:radial-gradient(circle at 30% 30%,#1d3a78,#0B1530 70%);display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center}
.band{position:absolute;left:0;right:0;background:#081127}
.bt{top:0;height:173px;display:flex;align-items:center;padding:0 90px;justify-content:space-between}
.bb{bottom:0;height:238px}
.bt img{height:64px}.bt span{font:800 26px 'FG';letter-spacing:.3em;color:#FFE600}
small{font:800 30px 'FG';letter-spacing:.32em;color:#FFE600;display:block}
b{font:800 150px/1 'BG';letter-spacing:-.02em;display:block;margin:26px 0 22px}
i{display:block;height:12px;width:260px;background:#FFE600;border-radius:12px;margin:0 auto}
p{font:600 44px 'FG';margin-top:36px;max-width:1500px;line-height:1.3}
""".replace("@@Z@@",FZ)
def page(kick,title,sub,band=True,extra=''):
    return f"""<!doctype html><meta charset=utf-8><style>{CSS}</style><body>
<div class="band bt"><img src="data:image/svg+xml;base64,{LGW}"><span>PSICOLOGIA</span></div>
<div class="mid" id=mid><small id=k>{kick}</small><b id=t>{title}</b><i id=w></i><p id=s>{sub}</p></div><div class="band bb"></div>{extra}"""
def shot(html,name,t=None):
    open(D+name+'.html','w').write(html)
def render_static(name,html):
    with sync_playwright() as p:
        b=p.chromium.launch(args=["--allow-file-access-from-files"]);pg=b.new_page(viewport={'width':1920,'height':1080})
        open(D+name+'.html','w').write(html);pg.goto('file://'+D+name+'.html');pg.evaluate("document.fonts.ready");pg.wait_for_timeout(300)
        pg.screenshot(path=D+name+'.png');b.close()
def render_anim(name,html,dur):
    N=int(round(dur*30));d=D+name+'_f/';shutil.rmtree(d,ignore_errors=True);os.makedirs(d)
    js="""t=>{const E=x=>{x=Math.max(0,Math.min(1,x));return 1-Math.pow(1-x,3)};const EB=x=>{x=Math.max(0,Math.min(1,x));const c=1.70158;return 1+(c+1)*Math.pow(x-1,3)+c*Math.pow(x-1,2)};
    const k=document.getElementById('k'),tt=document.getElementById('t'),w=document.getElementById('w'),s=document.getElementById('s');
    k.style.opacity=E((t-.2)/.5);tt.style.opacity=Math.min(1,EB((t-.35)/.6));tt.style.transform='scale('+(.8+.2*Math.min(1,EB((t-.35)/.6)))+')';
    w.style.width=(260*E((t-.8)/.7))+'px';s.style.opacity=E((t-1.1)/.6);
    document.getElementById('mid').style.opacity=1-E((t-%f)/.4)*0;}"""%dur
    with sync_playwright() as p:
        b=p.chromium.launch(args=["--allow-file-access-from-files"]);pg=b.new_page(viewport={'width':1920,'height':1080})
        open(D+name+'.html','w').write(html);pg.goto('file://'+D+name+'.html');pg.evaluate("document.fonts.ready");pg.wait_for_timeout(300)
        for n in range(N):
            pg.evaluate(js,n/30.0);pg.screenshot(path=d+'%05d.png'%(n+1))
        b.close()
    subprocess.run(['ffmpeg','-y','-loglevel','error','-framerate','30','-i',d+'%05d.png','-c:v','libx264','-preset','veryfast','-crf','17','-pix_fmt','yuv420p',D+name+'.mp4'],check=True)
    shutil.rmtree(d)
if __name__=='__main__':
    what=sys.argv[1:] or ['verifica','compiti','intro_compiti','sigla']
    if 'verifica' in what:
        render_static('verifica',page('PRIMA DI CHIUDERE','Verifica finale','Rispondi alle domande: per continuare serve almeno l’80%'))
    if 'compiti' in what:
        render_static('compiti',page('DOPO LA LEZIONE','Compiti','Svolgi gli esercizi: ora metti in pratica quello che hai imparato'))
    if 'intro_compiti' in what:
        render_anim('intro_compiti',page('DOPO LA LEZIONE','Compiti','Ora metti in pratica quello che hai imparato').replace('<div class="band bt">','<div class="band bt" style="opacity:0">').replace('class="band bb"','class="band bb" style="opacity:0"').replace('.mid{position:absolute;left:0;right:0;top:173px;height:669px;','.mid{position:absolute;left:0;right:0;top:0;height:1080px;'),3.5)
    if 'sigla' in what:
        render_static('sigla',page('CENTRO STUDI TELESIO','Psicologia','Videolezioni · I-II anno').replace('<div class="band bt"><img src="data:image/svg+xml;base64,%s"><span>PSICOLOGIA</span></div>'%LGW,'').replace('top:173px;height:669px','top:0;height:1080px'))
