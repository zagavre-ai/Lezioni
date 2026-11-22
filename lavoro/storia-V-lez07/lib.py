import json, os, subprocess, re, html
from playwright.sync_api import sync_playwright
W='/home/claude/w'; B=W+'/b'; KIT='/home/user/Lezioni/kit'
_pw=None; _br=None; _pg=None
def page():
    global _pw,_br,_pg
    if _pg is None:
        _pw=sync_playwright().start(); _br=_pw.chromium.launch(executable_path='/opt/pw-browsers/chromium',args=['--no-sandbox'])
        _pg=_br.new_page(viewport={'width':1920,'height':1080})
    return _pg
CSS='''
:root{--notte:#0B1530;--blu:#2060AF;--giallo:#FFE600;--linea:#E3E8F0}
*{box-sizing:border-box;margin:0;padding:0}
body{width:1920px;height:1080px;background:#fff;font-family:Figtree,sans-serif;color:var(--notte);position:relative;overflow:hidden}
.abs{position:absolute}
.logo{position:absolute;left:80px;top:48px;height:58px}
.hr{position:absolute;left:80px;right:80px;top:124px;border-top:1px solid #DDE3EC}
.hr2{position:absolute;left:80px;right:80px;top:980px;border-top:1px solid #DDE3EC}
.lab{position:absolute;left:80px;top:146px;font-weight:700;font-size:28px;letter-spacing:.14em;color:var(--blu);text-transform:uppercase;white-space:nowrap}
.foot{position:absolute;left:80px;top:998px;font-weight:700;font-size:24px;letter-spacing:.12em;color:var(--blu)}
.pg{position:absolute;right:80px;top:998px;font-weight:700;font-size:24px;letter-spacing:.1em;color:var(--blu)}
.cam{position:absolute;left:1428px;top:148px;width:412px;height:309px;border-radius:22px;box-shadow:0 14px 34px rgba(60,72,96,.22);background:#e9edf3}
.band{position:absolute;left:1428px;top:466px;width:416px;height:110px;background:var(--giallo);transform:rotate(-2deg);border-radius:8px;box-shadow:0 10px 24px rgba(60,72,96,.22);padding:20px 22px}
.band b{display:block;font-family:'Bricolage Grotesque';font-weight:800;font-size:34px;line-height:1.1}
.band i{display:block;font-style:normal;font-weight:700;font-size:24px;letter-spacing:.06em;margin-top:8px}
.kw{position:absolute;left:1428px;top:650px;width:412px}
.kw h4{font-weight:700;font-size:24px;letter-spacing:.16em;color:var(--blu);margin-bottom:12px}
.kw span{display:inline-block;background:#F2F5FA;border:2px solid #D6DEEA;border-radius:999px;padding:6px 18px;margin:0 8px 10px 0;font-weight:700;font-size:28px}
.card{position:relative;width:100%;background:#fff;border:2px solid var(--linea);border-radius:22px;padding:8px 34px 8px 52px;font-size:40px;line-height:1.5;box-shadow:0 10px 26px rgba(60,72,96,.13);transition:none}
.card b{font-weight:800;color:var(--blu)}
.card.dim{opacity:.55}
.card.on{border:5px solid var(--giallo);padding:5px 31px 5px 49px;box-shadow:0 12px 30px rgba(60,72,96,.2)}
.card.on::before{content:'';position:absolute;left:-14px;top:-14px;width:30px;height:30px;border-radius:50%;background:var(--giallo);box-shadow:0 2px 6px rgba(0,0,0,.2)}
'''
import base64
LOGO='data:image/svg+xml;base64,'+base64.b64encode(open('/home/claude/w/b/logo.svg','rb').read()).decode()
def head(extra=''):
    return f'<html><head><meta charset="utf-8"><style>{CSS}{extra}</style></head><body>'
def shot(htm,out,transparent=False):
    pg=page(); pg.set_content(htm); pg.wait_for_timeout(60)
    pg.screenshot(path=out,omit_background=transparent)
def dur(f): return float(subprocess.run(['ffprobe','-v','error','-show_entries','format=duration','-of','csv=p=0',f],capture_output=True,text=True).stdout)
def ff(*a,**k):
    r=subprocess.run(['ffmpeg','-y','-v','error']+[str(x) for x in a],capture_output=True,text=True)
    if r.returncode: raise SystemExit('ffmpeg: '+r.stderr[-1500:])
