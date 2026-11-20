import os,base64,json,html as H
from playwright.sync_api import sync_playwright
Z='/tmp/L18/str'
LOGO=base64.b64encode(open('/home/user/Lezioni/kit/docenti/Telesio_logo_blu.svg','rb').read()).decode()
CSS="""
@font-face{font-family:'BG';font-weight:800;src:url('file://%(z)s/font/BricolageGrotesque-ExtraBold.ttf')}
@font-face{font-family:'FG';font-weight:500;src:url('file://%(z)s/font/Figtree-Medium.ttf')}
@font-face{font-family:'FG';font-weight:700;src:url('file://%(z)s/font/Figtree-Bold.ttf')}
@font-face{font-family:'FG';font-weight:800;src:url('file://%(z)s/font/Figtree-ExtraBold.ttf')}
*{box-sizing:border-box;margin:0;padding:0}
body{width:1920px;height:1080px;background:#fff;overflow:hidden;font-family:'FG';color:#0B1530;position:relative}
#logo{position:absolute;left:80px;top:52px;height:52px}
.hl{position:absolute;left:80px;right:80px;height:1px;background:#E3E8F0}
.lab{position:absolute;left:80px;top:148px;font-weight:700;font-size:23px;letter-spacing:.17em;color:#2060AF;text-transform:uppercase;white-space:nowrap}
.ttl{position:absolute;left:80px;font-family:'BG';font-weight:800;font-size:72px;line-height:1.05;color:#0B1530;letter-spacing:-.015em}
.bar{position:absolute;left:80px;width:85px;height:6px;border-radius:4px;background:#2060AF}
.foot{position:absolute;top:998px;font-weight:700;font-size:22px;letter-spacing:.14em;color:#2060AF;white-space:nowrap}
.card{position:absolute;background:#fff;border:2px solid #E3E8F0;border-radius:22px;box-shadow:0 10px 30px rgba(20,40,90,.07);padding:20px 28px 20px 96px;font-size:30px;line-height:1.32;font-weight:500}
.card.on{border:4px solid #FFE600;box-shadow:0 0 0 6px rgba(255,230,0,.28),0 12px 30px rgba(20,40,90,.1);padding:19px 27px 19px 95px}
.card b{font-weight:800}
.num{position:absolute;left:28px;top:22px;width:46px;height:46px;border-radius:50%;background:#E3E8F0;color:#5a6786;font-weight:800;font-size:26px;display:flex;align-items:center;justify-content:center}
.card.on .num{background:#FFE600;color:#0B1530}
.cam{position:absolute;left:1428px;top:146px;width:412px;height:309px;border-radius:22px;box-shadow:0 18px 40px rgba(60,70,90,.28);background:#f1f3f7}
.fas{position:absolute;left:1428px;top:466px;width:416px;height:106px;background:#FFE600;border-radius:10px;transform:rotate(-3deg);box-shadow:0 10px 24px rgba(60,70,90,.22);padding:18px 24px}
.fas .n{font-family:'BG';font-weight:800;font-size:37px;line-height:1.05;color:#0B1530;white-space:nowrap}
.fas .m{font-weight:800;font-size:20px;letter-spacing:.06em;color:#0B1530;margin-top:6px;text-transform:uppercase}
.pc{position:absolute;left:1428px;top:640px;width:412px}
.pc h4{font-weight:800;font-size:20px;letter-spacing:.2em;color:#2060AF;margin-bottom:14px}
.pc div{font-weight:700;font-size:28px;line-height:1.2;padding:6px 12px;margin:0 0 6px;border-radius:6px;display:inline-block;color:#0B1530;background:transparent;opacity:.55}
.pc div.on{background:#FFE600;opacity:1}
.pill{position:absolute;left:80px;top:148px;font-weight:800;font-size:20px;letter-spacing:.2em;color:#2060AF;background:#E9F0FB;padding:8px 18px;border-radius:30px;text-transform:uppercase}
.tab{position:absolute;left:80px;border-radius:22px;overflow:hidden;box-shadow:0 12px 34px rgba(20,40,90,.10);border:1.5px solid #E3E8F0;background:#fff}
.tr{display:flex;border-top:1.5px solid #E9EDF4;font-size:32px;font-weight:700;line-height:1.25;opacity:0;transition:none}
.tr .c1{width:560px;padding:16px 28px;color:#2060AF;background:#F1F5FC;font-weight:800}
.tr .c2{flex:1;padding:16px 28px}
.tr.v{opacity:1}
.tr.on{background:#FFF7B0}.tr.on .c1{background:#FFF1A0}
.th{display:flex;background:#0B1530;color:#fff;font-weight:800;font-size:23px;letter-spacing:.17em;text-transform:uppercase}
.th div{padding:14px 28px}
""".replace('%(z)s',Z)
class R:
    def __init__(s):
        s.p=sync_playwright().start();s.b=s.p.chromium.launch(executable_path='/opt/pw-browsers/chromium',args=['--no-sandbox','--allow-file-access-from-files'])
        s.pg=s.b.new_page(viewport={'width':1920,'height':1080});os.makedirs('/tmp/L18/html',exist_ok=True)
    def shot(s,body,out,extra=''):
        h='<!doctype html><meta charset=utf-8><style>%s%s</style><body>%s'%(CSS,extra,body)
        f='/tmp/L18/html/_cur.html';open(f,'w').write(h);s.pg.goto('file://'+f);s.pg.evaluate("document.fonts.ready");s.pg.wait_for_timeout(50)
        s.pg.screenshot(path=out)
    def close(s):s.b.close();s.p.stop()
def frame(mat,page,label=None,title=None,tsize=72,prof=True,titley=222,pill=None):
    h=f'<img id=logo src="data:image/svg+xml;base64,{LOGO}"><div class=hl style="top:124px"></div>'
    if label:h+=f'<div class=lab>{H.escape(label)}</div>'
    if pill:h+=f'<div class=pill>{H.escape(pill)}</div>'
    if title:
        h+=f'<div class=ttl style="top:{titley}px;font-size:{tsize}px">{title}</div><div class=bar style="top:{titley+tsize*1.18+14:.0f}px"></div>'
    h+=f'<div class=hl style="top:981px"></div><div class=foot style="left:80px">{mat}</div><div class=foot style="right:80px">Pagina {page}</div>'
    return h
def prof_box(kw=None,on=()):
    h='<div class=cam></div><div class=fas><div class=n>Giorgio Mazzotti</div><div class=m>Prof. di Storia</div></div>'
    if kw:
        h+='<div class=pc><h4>PAROLE CHIAVE</h4>'+''.join(f'<div class="{"on" if i in on else ""}">{H.escape(k)}</div><br>' for i,k in enumerate(kw))+'</div>'
    return h

CSS2="""
.col{position:absolute;left:80px;width:1305px;top:322px}
.col.wide{width:1760px}
.col .card{position:relative;margin-bottom:14px;font-size:var(--fs,30px);padding:16px 26px 16px 92px;line-height:1.3}
.col .card.on{padding:15px 25px 15px 91px}
.col .card .num{top:16px;left:26px}
.card b{display:inline}
.card .t{font-weight:800;color:#0B1530}
.card.ex{font-size:var(--fs,30px)}
"""
FIT="""()=>{const c=document.querySelector('.col');if(!c)return 0;let fs=parseFloat(getComputedStyle(c).getPropertyValue('--fs'))||30;
 while(c.getBoundingClientRect().bottom>965&&fs>28){fs-=1;c.style.setProperty('--fs',fs+'px')}
 return [fs,c.getBoundingClientRect().bottom]}"""
def shot(r,body,out,extra=''):
    h='<!doctype html><meta charset=utf-8><style>%s%s%s</style><body>%s'%(CSS,CSS2,extra,body)
    f='/tmp/L18/html/_cur.html';open(f,'w').write(h);r.pg.goto('file://'+f);r.pg.evaluate("document.fonts.ready");r.pg.wait_for_timeout(40)
    res=r.pg.evaluate(FIT);r.pg.screenshot(path=out);return res
