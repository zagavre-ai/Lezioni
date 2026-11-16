# Libreria di montaggio Storia V (chat S7): scene HTML -> PNG (Playwright) -> pezzi mp4 (ffmpeg)
import os,json,base64,subprocess,re,html,math
import numpy as np
from playwright.sync_api import sync_playwright
FONT='/home/user/Lezioni/kit/tools/mappa_font'
LOGO_BLU=base64.b64encode(open('/home/user/Lezioni/kit/docenti/Telesio_logo_blu.svg','rb').read()).decode()
LOGO_BIA=None
def _logo_bianco():
    s=open('/home/user/Lezioni/kit/docenti/Telesio_logo_blu.svg').read()
    return s
CSS="""
@font-face{font-family:BG;font-weight:800;src:url('file://%(f)s/BricolageGrotesque-ExtraBold.ttf')}
@font-face{font-family:FG;font-weight:400;src:url('file://%(f)s/Figtree-Regular.ttf')}
@font-face{font-family:FG;font-weight:600;src:url('file://%(f)s/Figtree-SemiBold.ttf')}
@font-face{font-family:FG;font-weight:700;src:url('file://%(f)s/Figtree-Bold.ttf')}
:root{--notte:#0B1530;--blu:#2060AF;--giallo:#FFE600;--grigio:#EEF0F4;--linea:#C9D0DC}
*{box-sizing:border-box;margin:0;padding:0}
body{width:1920px;height:1080px;overflow:hidden;font-family:FG,sans-serif;position:relative}
.bg-l{background:#F7F8FB;color:var(--notte)}
.bg-d{background:radial-gradient(1300px 800px at 25% 20%,#16295C 0%,#0B1530 60%,#070E22 100%);color:#fff}
.abs{position:absolute}
.logo{position:absolute;left:56px;top:34px;height:54px}
.logo-d{filter:brightness(0) invert(1)}
.kick{font-family:FG;font-weight:700;letter-spacing:.22em;font-size:30px;text-transform:uppercase;color:var(--blu)}
.d .kick,.bg-d .kick{color:var(--giallo)}
h1{font-family:BG;font-weight:800;line-height:1.02;letter-spacing:-.01em}
.card{background:#fff;border:2px solid var(--linea);border-radius:22px;padding:22px 30px;font-size:34px;line-height:1.28;color:var(--notte)}
.card b{color:var(--blu);font-weight:700}
.dim{opacity:.62}
.lit{border:4px solid var(--blu);box-shadow:0 0 0 8px rgba(255,230,0,.55);opacity:1}
.foot{position:absolute;left:56px;bottom:26px;font-size:30px;letter-spacing:.08em;color:#6B7690;font-weight:600}
.yl{background:var(--giallo);color:var(--notte)}
.band{position:absolute;left:0;right:0;height:130px;background:var(--blu)}
.wave{display:flex;gap:7px;align-items:flex-end;height:90px}
.wave i{display:block;width:10px;background:#3C86E0;border-radius:4px}
.cap{position:absolute;left:150px;right:150px;bottom:90px;background:rgba(255,255,255,.08);border:2px solid rgba(255,255,255,.18);border-radius:22px;padding:28px 44px;font-size:40px;line-height:1.3;font-weight:600}
""".replace('%(f)s',FONT)
def doc(body,cls='bg-l'):
    return f'<!doctype html><html><head><meta charset="utf-8"><style>{CSS}</style></head><body class="{cls}">{body}</body></html>'
def logo(dark=False):
    return f'<img class="logo{" logo-d" if dark else ""}" src="data:image/svg+xml;base64,{LOGO_BLU}">'
E=html.escape
class Shooter:
    def __init__(s):
        s.p=sync_playwright().start();s.b=s.p.chromium.launch(executable_path='/opt/pw-browsers/chromium-1243/chrome-linux64/chrome',args=['--no-sandbox','--allow-file-access-from-files']);s.pg=s.b.new_page(viewport={'width':1920,'height':1080})
    def shot(s,h,path):
        f=path+'.html';open(f,'w').write(h);s.pg.goto('file://'+f);s.pg.wait_for_timeout(60);s.pg.screenshot(path=path);os.remove(f)
    def close(s):s.b.close();s.p.stop()
def run(c,**k):
    r=subprocess.run(c,capture_output=True,text=True,**k)
    if r.returncode:raise RuntimeError(' '.join(map(str,c))[:200]+'\n'+r.stderr[-800:])
    return r.stdout
def dur(f):return float(run(['ffprobe','-v','error','-show_entries','format=duration','-of','csv=p=0',f]).strip())
FPS=30
def fr(t):return int(round(t*FPS))
def still_video(states,out,audio=None,total=None,bg_audio_delay=0.0,extra_args=None):
    """states=[(png,durata_s)]. Costruisce mp4 1920x1080@30 con audio esattamente lungo come il video (silenzio se manca).
    audio: wav (inizia a bg_audio_delay)."""
    ff=[round(d*FPS) for _,d in states];ff=[max(1,x) for x in ff]
    if total is not None:
        diff=fr(total)-sum(ff);ff[-1]=max(1,ff[-1]+diff)
    T=sum(ff)/FPS
    lst=out+'.txt'
    with open(lst,'w') as f:
        for (p,_),n in zip(states,ff):
            while n>0:
                m=min(n,30);n-=m;f.write(f"file '{os.path.abspath(p)}'\nduration {m/FPS:.6f}\n")
        f.write(f"file '{os.path.abspath(states[-1][0])}'\n")
    cmd=['ffmpeg','-y','-v','error','-f','concat','-safe','0','-i',lst]
    if audio:
        cmd+=['-i',audio,'-filter_complex',f'[1:a]adelay={int(bg_audio_delay*1000)}|{int(bg_audio_delay*1000)},aresample=48000,apad,atrim=0:{T:.6f}[a]','-map','0:v','-map','[a]']
    else:
        cmd+=['-f','lavfi','-i','anullsrc=r=48000:cl=stereo','-filter_complex',f'[1:a]atrim=0:{T:.6f}[a]','-map','0:v','-map','[a]']
    cmd+=['-vf','fps=30,format=yuv420p','-c:v','libx264','-preset','veryfast','-crf','14','-c:a','aac','-b:a','192k','-ar','48000','-ac','2','-t',f'{T:.6f}',out]
    run(cmd);os.remove(lst);return T
def cue_times(text,wavdur,cues):
    """tempo (s) in cui la voce arriva alla frase 'cue' (sottostringa di text). Peso: 1 per carattere, pause dopo punteggiatura."""
    w=[];tot=0.0;pos=[]
    for i,ch in enumerate(text):
        pos.append(tot);tot+=1
        if ch=='.' or ch=='?' or ch=='!':tot+=9
        elif ch in ',:;':tot+=4
    out=[]
    for c in cues:
        i=text.find(c)
        if i<0:raise ValueError('cue non trovata: '+c)
        out.append(round(pos[i]/tot*wavdur,2))
    return out
