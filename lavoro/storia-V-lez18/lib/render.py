# Rendering delle slide bianche (modello Spagnolo) con Playwright. Tutto a 1920x1080.
import os,base64,hashlib,html as H,json
from playwright.sync_api import sync_playwright
W='/home/user/work18';FD='/home/user/Lezioni/kit/caratteri'
LOGO=base64.b64encode(open('/home/user/Lezioni/kit/docenti/Telesio_logo_blu.svg','rb').read()).decode()
CSS="""
@font-face{font-family:'BG';font-weight:800;src:url('file://@@Z@@/BricolageGrotesque-ExtraBold.ttf')}
@font-face{font-family:'FG';font-weight:500;src:url('file://@@Z@@/Figtree-Medium.ttf')}
@font-face{font-family:'FG';font-weight:700;src:url('file://@@Z@@/Figtree-Bold.ttf')}
@font-face{font-family:'FG';font-weight:800;src:url('file://@@Z@@/Figtree-ExtraBold.ttf')}
*{box-sizing:border-box;margin:0;padding:0}
body{width:1920px;height:1080px;background:#fff;overflow:hidden;font-family:'FG';color:#0B1530;position:relative}
#logo{position:absolute;left:80px;top:52px;height:52px}
.hl{position:absolute;left:80px;right:80px;height:1px;background:#E3E8F0}
.lab{position:absolute;left:80px;top:148px;font-weight:700;font-size:23px;letter-spacing:.17em;color:#2060AF;text-transform:uppercase;white-space:nowrap}
.ttl{position:absolute;left:80px;width:1300px;font-family:'BG';font-weight:800;font-size:58px;line-height:1.05;color:#0B1530;letter-spacing:-.015em}
.bar{position:absolute;left:80px;width:85px;height:6px;border-radius:4px;background:#2060AF}
.foot{position:absolute;top:998px;font-weight:700;font-size:22px;letter-spacing:.14em;color:#2060AF;white-space:nowrap}
.col{position:absolute;left:80px;width:1305px}
.card{position:relative;background:#fff;border:2px solid #D5DCE8;border-radius:22px;box-shadow:0 10px 30px rgba(60,70,90,.10);padding:12px 66px 12px 100px;font-size:40px;line-height:1.46;font-weight:500;margin-bottom:14px;opacity:.62}
.card.on{opacity:1;border:5px solid #FFE600;box-shadow:0 0 0 6px rgba(255,230,0,.28),0 12px 30px rgba(60,70,90,.14);padding:9px 63px 9px 97px}
.card .num{position:absolute;left:26px;top:20px;width:50px;height:50px;border-radius:50%;background:#E3E8F0;color:#3b4766;font-weight:800;font-size:28px;display:flex;align-items:center;justify-content:center;line-height:1}
.card.on .num{background:#FFE600;color:#0B1530}
.card.on::after{content:'';position:absolute;right:22px;top:22px;width:20px;height:20px;border-radius:50%;background:#FFE600;box-shadow:0 0 0 4px rgba(255,230,0,.35)}
.cam{position:absolute;left:1428px;top:148px;width:412px;height:309px}
.fas{position:absolute;left:1428px;top:466px;width:416px;height:106px;background:#FFE600;border-radius:10px;transform:rotate(-3deg);box-shadow:0 10px 24px rgba(60,70,90,.22);padding:18px 24px}
.fas .n{font-family:'BG';font-weight:800;font-size:37px;line-height:1.05;white-space:nowrap}
.fas .m{font-weight:800;font-size:20px;letter-spacing:.06em;margin-top:6px;text-transform:uppercase}
.pc{position:absolute;left:1428px;top:608px;width:412px}
.pc h4{font-weight:800;font-size:20px;letter-spacing:.2em;color:#2060AF;margin-bottom:10px}
.pc div{font-weight:700;font-size:27px;line-height:1.15;padding:4px 10px;margin:0 0 6px;border-radius:6px;display:table;color:#0B1530;opacity:.55}
.pc div.on{background:#FFE600;opacity:1}
.pill{display:inline-block;font-weight:800;font-size:20px;letter-spacing:.2em;color:#2060AF;background:#E9F0FB;padding:8px 18px;border-radius:30px;text-transform:uppercase}
.big{font-family:'BG';font-weight:800;color:#0B1530;letter-spacing:-.02em}
.legend{position:absolute;right:80px;top:148px;display:flex;gap:14px;flex-wrap:wrap;justify-content:flex-end;width:1200px}
.legend span{font-weight:700;font-size:20px;padding:6px 12px;border-radius:8px;border:2.5px solid;color:#0B1530}
""".replace("@@Z@@",FD)
_r=None
LAY="()=>{const t=document.getElementById('ttl'),b=document.getElementById('bar'),c=document.getElementById('col');if(t&&b){const y=t.getBoundingClientRect().bottom+12;b.style.top=y+'px';if(c)c.style.top=(y+34)+'px'}}"
class R:
    def __init__(s):
        s.p=sync_playwright().start();s.b=s.p.chromium.launch(executable_path='/opt/pw-browsers/chromium',args=['--no-sandbox','--allow-file-access-from-files'])
        s.pg=s.b.new_page(viewport={'width':1920,'height':1080})
def rr():
    global _r
    if _r is None:_r=R()
    return _r
def shot(body,out,extra='',force=False):
    if os.path.exists(out) and not force:return out
    os.makedirs(os.path.dirname(out),exist_ok=True)
    h='<!doctype html><meta charset=utf-8><style>%s%s</style><body>%s'%(CSS,extra,body)
    f=W+'/st/_cur.html';open(f,'w').write(h);pg=rr().pg;pg.goto('file://'+f);pg.evaluate("document.fonts.ready");pg.wait_for_timeout(30);pg.evaluate(LAY)
    over=pg.evaluate("()=>{let m=0;document.querySelectorAll('.col,.pc,.fas,.ttl').forEach(e=>{m=Math.max(m,e.getBoundingClientRect().bottom)});return m}")
    pg.screenshot(path=out+'.t.png');os.rename(out+'.t.png',out)
    if over>972 and 'ok_overflow' not in extra:print('ATTENZIONE: contenuto oltre il piede',out,over)
    return out
def frame(label,title,page,tsize=58,materia='STORIA'):
    h=f'<img id=logo src="data:image/svg+xml;base64,{LOGO}"><div class=hl style="top:124px"></div><div class=lab>{H.escape(label)}</div>'
    h+=f'<div class=ttl id=ttl style="top:196px;font-size:{tsize}px">{H.escape(title)}</div>'
    h+=f'<div class=hl style="top:981px"></div><div class=foot style="left:80px">{materia}</div><div class=foot style="right:80px">Pagina {page}</div>'
    return h
def barjs():  # posiziona la barra blu sotto il titolo e la colonna sotto la barra
    return "<script>const t=document.getElementById('ttl');const b=document.getElementById('bar');const c=document.getElementById('col');if(t&&b){const y=t.getBoundingClientRect().bottom+14;b.style.top=y+'px';if(c)c.style.top=(y+34)+'px'}</script>"
def cam_block(kw=None,on=()):
    h='<div class=fas><div class=n>Giorgio Mazzotti</div><div class=m>Prof. di Storia</div></div>'
    if kw:
        h+='<div class=pc><h4>PAROLE CHIAVE</h4>'+''.join(f'<div class="{"on" if i in on else ""}">{H.escape(k)}</div>' for i,k in enumerate(kw[:5]))+'</div>'
    return h
def card_html(i,t,on):
    return f'<div class="card {"on" if on else ""}"><div class=num>{i}</div>{H.escape(t)}</div>'
def slide_cards(label,title,cards,active,page,kw=None,kw_on=(),cam=True,out=None,extra=''):
    b=frame(label,title,page)+'<div class=bar id=bar></div><div class=col id=col>'+''.join(card_html(i+1,c,i==active) for i,c in enumerate(cards))+'</div>'
    if cam:b+=cam_block(kw,kw_on)
    return shot(b,out,extra)

# ---------- altre schede bianche ----------
def cam_block(kw=None,on=()):
    h='<div class=cam style="border-radius:22px;box-shadow:0 18px 40px rgba(60,70,90,.30);background:#e8ebf0"></div>'
    h+='<div class=fas><div class=n>Giorgio Mazzotti</div><div class=m>Prof. di Storia</div></div>'
    if kw:
        h+='<div class=pc><h4>PAROLE CHIAVE</h4>'+''.join(f'<div class="{"on" if i in on else ""}">{H.escape(k)}</div>' for i,k in enumerate(kw[:5]))+'</div>'
    return h
def cover_png(args,out,cam=False,lit=-1):
    h=f'<img id=logo src="data:image/svg+xml;base64,{LOGO}"><div class=hl style="top:124px"></div>'
    h+='<div class=lab>STORIA · VIDEOLEZIONE</div><div class=ttl id=ttl style="top:222px;font-size:110px;line-height:1.05">L\'Italia repubblicana</div><div class=bar id=bar style="top:350px"></div>'
    items=''.join(f'<div style="font-size:38px;font-weight:700;padding:10px 0 10px 8px;opacity:{1 if (lit<0 or i<=lit) else .25};display:flex;gap:18px"><span style="color:#2060AF;font-weight:800">{i+1}</span><span>{H.escape(a)}</span></div>' for i,a in enumerate(args))
    h+=f'<div style="position:absolute;left:80px;top:420px;width:1000px;background:#F4F7FC;border:2px solid #E3E8F0;border-radius:22px;padding:30px 44px;box-shadow:0 10px 30px rgba(60,70,90,.10)"><div class=pill style="margin-bottom:16px">Argomenti</div>{items}</div>'
    h+='<div class=hl style="top:981px"></div><div class=foot style="left:80px">STORIA</div><div class=foot style="right:80px">Pagina 1</div>'
    if cam:h+=cam_block()
    return shot(h,out,'.ttl{width:1300px}')
def argomenti_png(args,out,page,cam=True):
    cards=[a for a in args]
    return slide_cards('Di cosa parliamo','Di cosa parliamo',cards,-1,page,None,(),cam,out)
def label_slide(label,title,page,body_html,out,kw=None,cam=False,extra=''):
    b=frame(label,title,page)+'<div class=bar id=bar></div><div class=col id=col>'+body_html+'</div>'
    if cam:b+=cam_block(kw)
    return shot(b,out,extra)
def img_slide(label,title,page,imgpath,cards,active,out,kw=None,kw_on=(),cam=True,extra2=''):
    """immagine a sinistra (560 px) e fino a 2 card a destra (36 px)"""
    b64=base64.b64encode(open(imgpath,'rb').read()).decode()
    ext=imgpath.rsplit('.',1)[-1]
    body=f'<img src="data:image/{ext};base64,{b64}" style="position:absolute;left:0;top:0;max-width:640px;max-height:600px;border-radius:16px;box-shadow:0 10px 30px rgba(60,70,90,.18)">'
    body+='<div style="position:absolute;left:670px;top:0;width:635px">'+''.join(card_html(i+1,c,i==active) for i,c in enumerate(cards))+'</div>'
    b=frame(label,title,page)+'<div class=bar id=bar></div><div class=col id=col>'+body+'</div>'
    if cam:b+=cam_block(kw,kw_on)
    return shot(b,out,'#col .card{font-size:36px;line-height:1.4;padding:12px 56px 12px 84px}#col .card .num{left:18px;width:44px;height:44px;font-size:24px}#col .card.on{padding:9px 53px 9px 81px}'+extra2)

def quiz_png(label,qi,qn,q,opts,correct,reveal,expl,page,out):
    """opts: 4 testi nell'ordine mostrato; correct: indice; reveal: bool"""
    L='ABCD'
    h=frame(label,f'Domanda {qi} di {qn}',page,tsize=44)
    h+=f'<div style="position:absolute;left:80px;top:262px;width:1760px;font-family:BG;font-weight:800;font-size:46px;line-height:1.2">{H.escape(q)}</div>'
    if not reveal:
        cards=''
        for i,o in enumerate(opts):
            cards+=f'<div class=card style="opacity:1;position:absolute;left:{(i%2)*890}px;top:{(i//2)*250}px;width:870px;height:232px;font-size:32px;line-height:1.35;padding:18px 24px 18px 96px;margin:0;display:flex;align-items:center"><div class=num style="top:24px">{L[i]}</div>{H.escape(o)}</div>'
        h+=f'<div id=qa style="position:absolute;left:80px;top:470px;width:1760px;height:500px">{cards}</div>'
    else:
        h+=f'<div class="card on" style="position:absolute;left:80px;top:470px;width:1760px;font-size:36px;line-height:1.35;padding:18px 28px 18px 100px"><div class=num>{L[correct]}</div><b>Risposta corretta · {L[correct]}</b><br>{H.escape(opts[correct])}</div>'
        if expl:h+=f'<div class=card style="opacity:1;position:absolute;left:80px;top:740px;width:1760px;font-size:32px;line-height:1.4;padding:16px 28px;background:#F4F7FC"><div style="font-weight:800;color:#2060AF;letter-spacing:.14em;font-size:22px;margin-bottom:6px">PERCHÉ</div>{H.escape(expl)}</div>'
    return shot(h,out,'ok_overflow')
def table_png(label,title,page,rows,lit,out,head=("PUNTO","IN BREVE")):
    body=f'<div style="border-radius:22px;overflow:hidden;box-shadow:0 12px 34px rgba(60,70,90,.12);border:1.5px solid #E3E8F0;width:1760px"><div style="display:flex;background:#0B1530;color:#fff;font-weight:800;font-size:24px;letter-spacing:.17em"><div style="width:560px;padding:16px 32px">{head[0]}</div><div style="flex:1;padding:16px 32px">{head[1]}</div></div>'
    for i,(a,b) in enumerate(rows):
        on=i==lit;bg='#FFF4A8' if on else '#fff';bd='border-left:12px solid #FFE600;' if on else 'border-left:12px solid transparent;'
        body+=f'<div style="display:flex;border-top:1.5px solid #E9EDF4;background:{bg};{bd}font-size:38px;line-height:1.35"><div style="width:548px;padding:22px 32px 22px 20px;color:#2060AF;font-weight:800">{H.escape(a)}</div><div style="flex:1;padding:22px 32px;font-weight:500">{H.escape(b)}</div></div>'
    body+='</div>'
    b=frame(label,title,page)+'<div class=bar id=bar></div><div class=col id=col style="width:1760px">'+body+'</div>'
    return shot(b,out)
