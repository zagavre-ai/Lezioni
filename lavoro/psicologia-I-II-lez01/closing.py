# Chiusura nuova: scheda statica «Verifica finale» (5 s, bande blu), intro «Compiti» (3,5 s), scheda statica «Compiti» (5 s, bande blu)
import os,sys,json,shutil,subprocess,base64
from playwright.sync_api import sync_playwright
D='/home/claude/lezioni/psicologia-I-II-lez01/'
FZ='/home/claude/l1/fz/33157a64-Bricolage_GrotesqueDM_MonoFigtree'
LG=base64.b64encode(open('/home/claude/logo/out/Telesio_logo_blu.svg','rb').read()).decode()
LGW=base64.b64encode(open('/home/claude/logo/out/Telesio_logo_bianco.svg','rb').read()).decode()
CSS="""@font-face{font-family:'BG';font-weight:800;src:url('file://%(z)s/Bricolage_Grotesque/static/BricolageGrotesque-ExtraBold.ttf')}
@font-face{font-family:'FG';font-weight:500;src:url('file://%(z)s/Figtree/static/Figtree-Medium.ttf')}
@font-face{font-family:'FG';font-weight:700;src:url('file://%(z)s/Figtree/static/Figtree-Bold.ttf')}
@font-face{font-family:'FG';font-weight:800;src:url('file://%(z)s/Figtree/static/Figtree-ExtraBold.ttf')}
*{box-sizing:border-box;margin:0;padding:0}body{width:1920px;height:1080px;overflow:hidden;font-family:'FG';color:#0B1530;position:relative;background:#F5F8FC}
.band{position:absolute;left:0;right:0;background:#0B1530}.bt{top:0;height:173px}.bb{bottom:0;height:238px}
.mid{position:absolute;left:0;right:0;top:173px;height:669px;display:flex;flex-direction:column;justify-content:center;padding:0 160px}
.k{font-weight:800;letter-spacing:.3em;font-size:30px;color:#2060AF;text-transform:uppercase}
.t{font-family:'BG';font-weight:800;font-size:150px;line-height:1;letter-spacing:-.02em;margin:18px 0 0}
.u{height:12px;width:360px;background:#FFE600;border-radius:8px;margin:26px 0 0}
.p{font-weight:600;font-size:42px;line-height:1.3;margin-top:34px;max-width:1400px}
.lg{position:absolute;left:160px;top:50px;height:64px}
"""%{'z':FZ}
def card(kicker,title,text):
    return f"""<!doctype html><meta charset=utf-8><style>{CSS}</style><body><div class="band bt"></div><img class="lg" src="data:image/svg+xml;base64,{LGW}">
<div class="mid"><div class="k">{kicker}</div><div class="t">{title}</div><div class="u"></div><div class="p">{text}</div></div><div class="band bb"></div></body>"""
INTRO=f"""<!doctype html><meta charset=utf-8><style>{CSS}
body{{background:radial-gradient(circle at 30% 30%,#1d3a78,#0B1530 70%);color:#fff}}
#c{{position:absolute;inset:0;display:flex;align-items:center;justify-content:center;flex-direction:column;text-align:center}}
#s{{font-weight:800;letter-spacing:.3em;font-size:30px;color:#FFE600}}#b{{font-family:BG;font-weight:800;font-size:230px;line-height:1;letter-spacing:-.02em;margin:22px 0}}
#i{{height:12px;width:0;background:#FFE600;border-radius:9px}}#p{{font-weight:600;font-size:44px;margin-top:36px}}</style><body><div id=c><div id=s>DOPO LA LEZIONE</div><div id=b>Compiti</div><div id=i></div><div id=p>Ora metti in pratica quello che hai imparato</div></div>
<script>const E=x=>{{x=Math.max(0,Math.min(1,x));return 1-Math.pow(1-x,3)}};
const EB=x=>{{x=Math.max(0,Math.min(1,x));const c=1.4;return 1+(c+1)*Math.pow(x-1,3)+c*Math.pow(x-1,2)}};
window.draw=function(t){{document.getElementById('s').style.opacity=E((t-.2)/.5);const b=document.getElementById('b'),v=EB((t-.35)/.6);b.style.opacity=Math.min(1,v);b.style.transform='scale('+(.8+.2*v)+')';
document.getElementById('i').style.width=(E((t-.8)/.7)*260)+'px';document.getElementById('p').style.opacity=E((t-1.1)/.6);
document.body.style.opacity=1-E((t-3.1)/.4);return Math.round(t*30)}}</script></body>"""
def png(html,out):
    open(out+'.html','w').write(html)
    with sync_playwright() as p:
        b=p.chromium.launch(args=["--allow-file-access-from-files"]);pg=b.new_page(viewport={'width':1920,'height':1080})
        pg.goto('file://'+out+'.html');pg.evaluate("document.fonts.ready");pg.wait_for_timeout(300);pg.screenshot(path=out+'.png');b.close()
def still(png_f,out,dur=5.0):
    subprocess.run(['ffmpeg','-y','-loglevel','error','-loop','1','-framerate','30','-i',png_f,'-t','%.2f'%dur,'-c:v','libx264','-preset','veryfast','-crf','16','-pix_fmt','yuv420p','-r','30',out],check=True)
if __name__=='__main__':
    os.makedirs(D+'dk',exist_ok=True)
    png(card('Psicologia','Verifica finale','Rispondi alle domande: per continuare serve almeno l’80%'),D+'dk/VERIFICA');still(D+'dk/VERIFICA.png',D+'dk/VERIFICA.mp4')
    png(card('Psicologia','Compiti','Ora metti in pratica quello che hai imparato'),D+'dk/COMPITI');still(D+'dk/COMPITI.png',D+'dk/COMPITI.mp4')
    d=D+'dk/INTRO_f';shutil.rmtree(d,ignore_errors=True);os.makedirs(d)
    open(D+'dk/INTRO.html','w').write(INTRO)
    with sync_playwright() as p:
        b=p.chromium.launch(args=["--allow-file-access-from-files"]);pg=b.new_page(viewport={'width':1920,'height':1080})
        pg.goto('file://'+D+'dk/INTRO.html');pg.evaluate("document.fonts.ready");pg.wait_for_timeout(300)
        for n in range(105):
            pg.evaluate("t=>draw(t)",n/30.0);pg.screenshot(path='%s/%05d.png'%(d,n+1))
        b.close()
    subprocess.run(['ffmpeg','-y','-loglevel','error','-framerate','30','-i',d+'/%05d.png','-c:v','libx264','-preset','veryfast','-crf','16','-pix_fmt','yuv420p',D+'dk/INTRO.mp4'],check=True)
    shutil.rmtree(d);print('ok')
