import sys,os,json,base64,html
sys.path.insert(0,'/home/user/work/build')
from L import *
from playwright.sync_api import sync_playwright
LOGO=base64.b64encode(open(B+'/Telesio_logo_blu.svg','rb').read()).decode()
CSS="""
@font-face{font-family:BG;font-weight:800;src:url('file:///root/.fonts/BricolageGrotesque-ExtraBold.ttf')}
@font-face{font-family:FG;font-weight:500;src:url('file:///root/.fonts/Figtree-Medium.ttf')}
@font-face{font-family:FG;font-weight:700;src:url('file:///root/.fonts/Figtree-Bold.ttf')}
@font-face{font-family:FG;font-weight:800;src:url('file:///root/.fonts/Figtree-ExtraBold.ttf')}
*{box-sizing:border-box;margin:0;padding:0}
html,body{width:1920px;height:1080px;background:#fff;overflow:hidden;font-family:FG;color:#0B1530}
#logo{position:absolute;left:80px;top:48px;height:58px}
#hl{position:absolute;left:80px;right:80px;top:124px;height:2px;background:#E5E9F0}
#fl{position:absolute;left:80px;right:80px;top:981px;height:2px;background:#E5E9F0}
#ft{position:absolute;left:80px;top:998px;font:700 22px FG;letter-spacing:.14em;color:#2060AF}
#pg{position:absolute;right:80px;top:998px;font:700 22px FG;letter-spacing:.14em;color:#2060AF}
#kick{position:absolute;left:80px;top:146px;font:700 24px FG;letter-spacing:.16em;color:#2060AF;text-transform:uppercase}
#flow{position:absolute;left:80px;top:184px;width:1305px}
#ttl{width:1290px;font:800 58px/1.08 BG;letter-spacing:-.01em;color:#0B1530}
#bar{height:6px;margin:14px 0 36px;width:85px;background:#2060AF;border-radius:3px}
#cards{width:1305px;display:flex;flex-direction:column;gap:16px}
.card{font-size:inherit;position:relative;background:#fff;border:2px solid #E2E8F0;border-radius:22px;padding:20px 30px 20px 100px;font-weight:500;line-height:1.5;font-family:FG;box-shadow:0 14px 34px rgba(60,72,100,.13);transition:none}
.card b{font-weight:800}
.card .n{position:absolute;left:28px;top:24px;width:50px;height:50px;border-radius:50%;background:#E3E8F1;color:#2A3550;font:800 26px/50px FG;text-align:center}
.card.dim{opacity:.74}
.card.on{border:5px solid #FFE600;padding:18px 28px 18px 98px;box-shadow:0 0 0 4px rgba(255,230,0,.35),0 16px 36px rgba(60,72,100,.16)}
.card.on .n{background:#FFE600;color:#0B1530}
#cam{position:absolute;left:1428px;top:148px;width:412px;height:309px;border-radius:18px;box-shadow:0 18px 40px rgba(60,72,100,.28);background:#e8ebf0}
#band{position:absolute;left:1428px;top:466px;width:416px;height:104px;background:#FFE600;transform:rotate(-3deg);transform-origin:left top;box-shadow:0 10px 24px rgba(60,72,100,.22);padding:16px 22px}
#band .nm{font:800 38px/1.1 BG;color:#0B1530}
#band .ms{font:800 20px FG;letter-spacing:.04em;margin-top:8px;color:#0B1530}
#kw{position:absolute;left:1428px;top:640px;width:420px}
#kw .h{font:800 22px FG;letter-spacing:.16em;color:#2060AF;margin-bottom:14px}
#kw .k{font:700 30px/1.25 FG;color:#5B6478;padding:4px 12px;margin:0 0 8px -12px;border-radius:8px;display:inline-block}
#kw .k.on{background:#FFE600;color:#0B1530}
#kw div.r{display:block}
"""
LOGO_W=base64.b64encode(open(B+'/Telesio_logo_bianco.svg','rb').read()).decode()
DARK='''<style>html,body{background:radial-gradient(1400px 900px at 30% 20%,#13224A 0%,#0A1330 55%,#060A1B 100%)!important;color:#F3F5FA}
#hl,#fl{background:rgba(255,255,255,.16)!important}#kick,#ft,#pg{color:#E3A95C!important}#ttl{color:#fff!important}#bar{background:#E3A95C!important}
.card{background:rgba(255,255,255,.08)!important;border:2px solid rgba(255,255,255,.2)!important;color:#F3F5FA;box-shadow:0 18px 40px rgba(0,0,0,.35)!important}
.card .n{background:rgba(255,255,255,.2)!important;color:#fff!important}.card.on{border:5px solid #FFE600!important;background:rgba(255,255,255,.14)!important}.card.on .n{background:#FFE600!important;color:#0B1530!important}</style>'''
class R:
    def __init__(s):
        s.p=sync_playwright().start()
        s.b=s.p.chromium.launch(executable_path='/opt/pw-browsers/chromium-1243/chrome-linux64/chrome',args=['--no-sandbox','--allow-file-access-from-files'])
        s.pg=s.b.new_page(viewport={'width':1920,'height':1080})
    def shot(s,body,out,extra_css=''):
        open('/tmp/_s.html','w').write(f'<!doctype html><meta charset=utf-8><style>{CSS}{extra_css}</style><body>{body}</body>')
        s.pg.goto('file:///tmp/_s.html');s.pg.evaluate('document.fonts.ready');s.pg.wait_for_timeout(30)
        s.pg.screenshot(path=out)
    def close(s): s.b.close();s.p.stop()
def cardhtml(i,txt,state,num=None):
    lab,_,rest=txt.partition(':')
    t=f'<b>{lab}:</b>{rest}' if rest else txt
    return f'<div class="card {state}" id="c{i}"><span class=n>{num or i}</span>{t}</div>'
def frame(kick,title,cards,win,active,kws,kwa,pagen,prof=True,materia='STORIA V',top=None,wide=False,fs=40,dark=False):
    """cards: lista testi; win: indici (1-based) mostrati; active: indice o None"""
    cy=0
    h=(DARK if dark else '')+f'<img id=logo src="data:image/svg+xml;base64,{LOGO_W if dark else LOGO}"><div id=hl></div><div id=kick>{html.escape(kick)}</div><div id=flow{' style="width:1760px"' if wide else ''}><div id=ttl{' style="width:1760px"' if wide else ''}>{title}</div><div id=bar></div>'
    h+=f'<div id=cards style="{"width:1760px;" if wide else ""}font-size:{fs}px">'
    for pos,i in enumerate(win,1):
        st='on' if i==active else ('dim' if active else '')
        h+=cardhtml(i,cards[i-1],st,pos)
    h+='</div></div>'
    if prof:
        h+='<div id=cam></div><div id=band><div class=nm>Giorgio Mazzotti</div><div class=ms>PROF. DI STORIA</div></div>'
        if kws:
            h+='<div id=kw><div class=h>PAROLE CHIAVE</div>'+''.join(f'<div class=r><span class="k {"on" if (j+1)==kwa else ""}">{html.escape(k)}</span></div>' for j,k in enumerate(kws))+'</div>'
    h+=f'<div id=fl></div><div id=ft>{materia}</div><div id=pg>Pagina {pagen}</div>'
    return h,cy
def measure(r,kick,title,cards,prof=True):
    h,cy=frame(kick,title,cards,range(1,len(cards)+1),None,[],None,1,prof=prof,wide=not prof,fs=40 if prof else 46)
    r.shot(h,'/tmp/m.png')
    hs=r.pg.evaluate("[...document.querySelectorAll('.card')].map(e=>e.getBoundingClientRect().height)")
    cy=r.pg.evaluate("document.getElementById('cards').getBoundingClientRect().top")
    return hs,cy
def choose_window(hs,cy,k,cur):
    avail=960-cy
    if cur and k in cur: return cur
    def fits(w): return sum(hs[i-1] for i in w)+16*(len(w)-1)<=avail
    n=len(hs)
    for w in ([k-1,k,k+1],[1,2,3] if k==1 else [0],[k-1,k],[k,k+1],[k]):
        if all(1<=i<=n for i in w) and len(w)<=3 and fits(w): return w
    return [k]
def foto_html(num,cam):
    h=f'<img id=logo src="data:image/svg+xml;base64,{LOGO}"><div id=hl></div><div id=kick>01 · L\'ascesa di Stalin</div>'
    h+='<div style="position:absolute;left:80px;top:200px;width:566px;height:713px;border-radius:22px;overflow:hidden;box-shadow:0 18px 40px rgba(60,72,100,.25);background:#fff"><img src="file:///home/user/work/build/stalin_up.png" style="width:566px;height:713px;object-fit:cover"></div>'
    h+='<div style="position:absolute;left:700px;top:520px;font:800 72px/1.05 BG;color:#0B1530">Iosif Stalin</div><div id=bar style="position:absolute;left:700px;top:620px"></div>'
    if cam: h+='<div id=cam></div><div id=band><div class=nm>Giorgio Mazzotti</div><div class=ms>PROF. DI STORIA</div></div>'
    h+=f'<div id=fl></div><div id=ft>STORIA V</div><div id=pg>Pagina {num}</div>'
    return h
