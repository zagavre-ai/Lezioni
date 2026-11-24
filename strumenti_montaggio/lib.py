# Libreria comune: font, colori, render con Playwright (stati fermi e animazioni a fotogrammi)
import os, json, subprocess, html, re, hashlib
from playwright.sync_api import sync_playwright
W=os.environ.get('LEZ_W','/home/claude/w')
LOGO=open('/home/user/Lezioni/kit/docenti/Telesio_logo_blu.svg').read()
LOGO_URI='data:image/svg+xml;utf8,'+LOGO.replace('#','%23').replace('"',"'").replace('\n','')
FONTS='''
@font-face{font-family:Fig;font-weight:400;src:url(file:///root/.fonts/Figtree-Regular.ttf)}
@font-face{font-family:Fig;font-weight:500;src:url(file:///root/.fonts/Figtree-Medium.ttf)}
@font-face{font-family:Fig;font-weight:600;src:url(file:///root/.fonts/Figtree-SemiBold.ttf)}
@font-face{font-family:Fig;font-weight:700;src:url(file:///root/.fonts/Figtree-Bold.ttf)}
@font-face{font-family:Fig;font-weight:800;src:url(file:///root/.fonts/Figtree-ExtraBold.ttf)}
@font-face{font-family:Bri;font-weight:800;src:url(file:///root/.fonts/BricolageGrotesque-ExtraBold.ttf)}
'''
BASE=FONTS+'''
*{box-sizing:border-box}
html,body{margin:0;width:1920px;height:1080px;background:#fff;overflow:hidden;font-family:Fig;color:#0B1530}
'''
def esc(s): return html.escape(s,quote=False)
def rich(s):
    """**grassetto** -> <b>"""
    s=esc(s); return re.sub(r'\*\*(.+?)\*\*',r'<b>\1</b>',s)

class R:
    """un browser; page(html) -> still; anim(html, n, fn) -> fotogrammi"""
    def __init__(s):
        s.p=sync_playwright().start(); s.b=s.p.chromium.launch(executable_path='/opt/pw-browsers/chromium',args=['--no-sandbox'])
        s.pg=s.b.new_page(viewport={'width':1920,'height':1080})
    def load(s,doc):
        f=f'{W}/tmp_{os.getpid()}.html'; open(f,'w').write(doc); s.pg.goto('file://'+f); s.pg.evaluate('document.fonts.ready'); s.pg.wait_for_timeout(120)
    def shot(s,out,fmt='png'):
        if fmt=='png': s.pg.screenshot(path=out)
        else: s.pg.screenshot(path=out,type='jpeg',quality=93)
        try: open(out+'.txt','w').write(s.pg.evaluate('document.body.innerText'))
        except Exception: pass
    def close(s):
        s.b.close(); s.p.stop()

def frames_to_mp4(rend, doc, tot, fps, out, audio=None, state_js='render', crf=17):
    """doc: html con window.render(t) che ritorna una firma di stato; fotogrammi uguali non rifotografati"""
    rend.load(doc)
    cmd=['ffmpeg','-v','error','-y','-f','image2pipe','-framerate',str(fps),'-i','-','-c:v','libx264','-preset','veryfast','-crf',str(crf),'-pix_fmt','yuv420p','-r',str(fps),out]
    ff=subprocess.Popen(cmd,stdin=subprocess.PIPE)
    n=int(round(tot*fps)); last=None; buf=None
    for i in range(n):
        sig=rend.pg.evaluate(f'{state_js}({i/fps})')
        if sig!=last or buf is None:
            buf=rend.pg.screenshot(type='jpeg',quality=94); last=sig
        ff.stdin.write(buf)
    ff.stdin.close(); ff.wait()
    return n
