# libreria di grafica: HTML -> PNG 1920x1080 (Chromium), schede nel modello Spagnolo/Storia V
import os,hashlib,html as H,re
from playwright.sync_api import sync_playwright
W='/tmp/claude-0/w/prod';PNG=W+'/png/'
LOGO='file:///home/user/Lezioni/kit/docenti/Telesio_logo_blu.svg'
MATERIA="STORIA DELL'ARTE V"
CSS='''
*{box-sizing:border-box}
html,body{margin:0;width:1920px;height:1080px;overflow:hidden;font-family:Figtree;color:#0B1530}
body{background:#fff;position:relative}
.logo{position:absolute;left:80px;top:48px;height:58px}
.rule{position:absolute;left:80px;right:80px;top:124px;height:1px;background:#D5DCE8}
.frule{position:absolute;left:80px;right:80px;top:981px;height:1px;background:#D5DCE8}
.lab{position:absolute;left:80px;top:146px;font:700 24px Figtree;letter-spacing:.16em;color:#2060AF;text-transform:uppercase;width:1310px}
.tit{position:absolute;left:80px;top:188px;width:1310px;font:800 58px/1.08 'Bricolage Grotesque';color:#2060AF}
.tit:after{content:"";display:block;width:84px;height:6px;border-radius:3px;background:#2060AF;margin-top:16px}
.foot{position:absolute;left:80px;top:1000px;font:700 22px Figtree;letter-spacing:.14em;color:#2060AF}
.pag{position:absolute;right:80px;top:1000px;font:700 22px Figtree;letter-spacing:.1em;color:#2060AF}
#cam{position:absolute;left:1428px;top:148px;width:412px;height:309px;border-radius:18px;background:#E8ECF3;box-shadow:0 18px 40px rgba(60,70,90,.28)}
.band{position:absolute;left:1428px;top:470px;width:412px;height:106px;background:#FFE600;border-radius:8px;transform:rotate(-1.6deg);padding:20px 24px;box-shadow:0 12px 26px rgba(60,70,90,.25)}
.band b{display:block;font:800 31px/1.1 'Bricolage Grotesque';color:#0B1530}
.band i{display:block;font:700 19px Figtree;font-style:normal;letter-spacing:.06em;margin-top:8px;color:#0B1530}
.kw{position:absolute;left:1428px;top:640px;width:412px}
.kw h4{margin:0 0 12px;font:700 20px Figtree;letter-spacing:.16em;color:#2060AF}
.kw span{display:inline-block;margin:0 10px 10px 0;padding:8px 16px;border-radius:999px;background:#EAF1FB;border:2px solid #BFD3EE;font:700 27px Figtree;color:#0B1530}
.cards{position:absolute;left:80px;width:1310px}
.card{position:relative;margin-bottom:18px;padding:20px 28px 20px 52px;border:2px solid #D5DCE8;border-radius:18px;background:#fff;font:500 40px/1.5 Figtree;color:#0B1530;box-shadow:0 10px 26px rgba(60,70,90,.10);opacity:.5}
.card b{font-weight:800}
.card:before{content:"";position:absolute;left:20px;top:36px;width:16px;height:16px;border-radius:50%;background:#C3CBDA}
.card.lit{opacity:1;border:5px solid #FFE600;padding:18px 26px 18px 50px;box-shadow:0 14px 34px rgba(60,70,90,.2)}
.card.lit:before{background:#FFE600;left:18px;top:34px;width:20px;height:20px;box-shadow:0 0 0 3px #0B1530 inset}
.img{position:absolute;left:80px;width:1310px;display:flex;align-items:center;justify-content:center}
.img img{max-width:100%;max-height:100%;border-radius:10px;box-shadow:0 14px 34px rgba(60,70,90,.25)}
.cap{position:absolute;left:80px;width:1310px;text-align:center;font:600 28px Figtree;color:#0B1530}
/* schede scure */
.dk{position:absolute;inset:0;background:radial-gradient(1200px 700px at 78% 30%,#14407a 0%,#0B1E45 45%,#060E26 100%)}
.dk:before{content:"";position:absolute;inset:0;background:radial-gradient(500px 360px at 18% 85%,rgba(30,140,160,.28),transparent 70%),radial-gradient(380px 300px at 92% 90%,rgba(255,230,0,.07),transparent 70%)}
.dk .logo{filter:brightness(0) invert(1);opacity:.9}
.dk .big{position:absolute;left:150px;right:150px}
.dk .kick{font:700 26px Figtree;letter-spacing:.3em;color:#7fb3ff;text-transform:uppercase}
.dk h1{margin:14px 0 0;font:800 96px/1.05 'Bricolage Grotesque';color:#fff}
.dk h2{margin:18px 0 0;font:800 56px/1.1 'Bricolage Grotesque';color:#FFE600}
.dk .chip{display:inline-block;margin:6px 12px 0 0;padding:10px 22px;border-radius:999px;border:2px solid #3d6fb8;color:#cfe3ff;font:700 28px Figtree;background:rgba(20,60,120,.35)}
.dk .foot,.dk .pag{color:#9fc2f2}
.ghost{position:absolute;right:120px;top:120px;font:800 520px/1 'Bricolage Grotesque';color:rgba(255,255,255,.05)}
.rl{position:relative;margin:0 0 14px;padding:16px 28px 16px 56px;border-radius:16px;background:rgba(255,255,255,.06);border:2px solid rgba(255,255,255,.12);font:600 38px/1.35 Figtree;color:#e8f0ff;opacity:.45}
.rl:before{content:"";position:absolute;left:22px;top:30px;width:16px;height:16px;border-radius:50%;background:#5c86c4}
.rl.lit{opacity:1;background:rgba(255,230,0,.12);border:4px solid #FFE600;color:#fff;padding:14px 26px 14px 54px}
.rl.lit:before{background:#FFE600;left:20px}
'''
def esc(s):return H.escape(s,quote=False)
class Ren:
    def __init__(s):
        s.p=sync_playwright().start();s.b=s.p.chromium.launch(executable_path='/opt/pw-browsers/chromium-1243/chrome-linux64/chrome',args=['--no-sandbox']);s.pg=s.b.new_page(viewport={'width':1920,'height':1080})
    def shot(s,body,css='',name=None):
        if not hasattr(s,'text'):s.text={}
        h='<!doctype html><meta charset="utf-8"><style>'+CSS+css+'</style>'+body
        k=hashlib.md5(h.encode()).hexdigest()[:16];o=PNG+(name or k)+'.png'
        if not os.path.exists(o):
            open(W+'/_h.html','w').write(h);s.pg.goto('file://'+W+'/_h.html');s.pg.wait_for_timeout(80);s.pg.screenshot(path=o)
        s.text[o]=re.sub(r'\s+',' ',re.sub(r'<[^>]+>',' ',H.unescape(body))).strip()
        return o
    def measure(s,body,css=''):
        open(W+'/_h.html','w').write('<!doctype html><meta charset="utf-8"><style>'+CSS+css+'</style>'+body);s.pg.goto('file://'+W+'/_h.html');s.pg.wait_for_timeout(30)
        return s.pg.evaluate("Array.from(document.querySelectorAll('.card')).map(e=>e.getBoundingClientRect().height+18)")
    def close(s):s.b.close();s.p.stop()
def card_html(c,lit):
    lead,rest=c
    return f'<div class="card{" lit" if lit else ""}"><b>{esc(lead)}</b> {esc(rest)}</div>'
def head(label,title,page,prof=True,dark=False):
    return (f'<img class="logo" src="{LOGO}">'+('' if dark else '<div class="rule"></div>')+
      (f'<div class="lab">{esc(label)}</div><div class="tit">{esc(title)}</div>' if not dark else '')+
      f'<div class="foot">{MATERIA}</div><div class="pag">Pagina {page}</div>'+('' if dark else '<div class="frule"></div>'))
def prof_col(keywords):
    k=''.join(f'<span>{esc(x)}</span>' for x in keywords[:5])
    return ('<div id="cam"></div><div class="band"><b>Giorgio Mazzotti</b><i>PROF. DI STORIA DELL\'ARTE</i></div>'+
            (f'<div class="kw"><h4>PAROLE CHIAVE</h4>{k}</div>' if k else ''))
def title_top(title):  # altezza del titolo: 1 o 2 righe (misurata dal chiamante); cards partono sotto
    return 188
def slide_cards(label,title,cards,lit,keywords,page,top=None,prof=True):
    n=len(title)  # righe stimate
    top=top or (370 if len(title)*30>1250 else 304)
    body=head(label,title,page)+(prof_col(keywords) if prof else '')
    body+=f'<div class="cards" style="top:{top}px">'+''.join(card_html(c,i==lit) for i,c in enumerate(cards))+'</div>'
    return body
def slide_image(label,title,imgs,page,caption='',keywords=(),prof=True,top=300):
    body=head(label,title,page)+(prof_col(keywords) if prof else '')
    hh=960-top-(46 if caption else 0)
    body+=f'<div class="img" style="top:{top}px;height:{hh}px">'+''.join(f'<img src="file://{i}" style="margin:0 10px">' for i in imgs)+'</div>'
    if caption:body+=f'<div class="cap" style="top:{960-34}px">{esc(caption)}</div>'
    return body
def dark_scene(kind,page,inner,ghost=''):
    return '<div class="dk">'+head('', '',page,dark=True)+(f'<div class="ghost">{ghost}</div>' if ghost else '')+inner+'</div>'

# ---------- scene specifiche ----------
def cover(page,with_prof):
    args=["L'Italia fascista e il controllo delle arti","L'architettura: tradizione classica e Razionalismo","Il ritorno all'ordine e la Metafisica","Il Novecento italiano e l'opposizione"]
    li=''.join(f'<li>{esc(a)}</li>' for a in args)
    b=(f'<img class="logo" src="{LOGO}"><div class="rule"></div>'
       f'<div class="lab" style="top:150px">{MATERIA} · VIDEOLEZIONE</div>'
       f'<div class="tit" style="top:196px;font-size:104px;line-height:1.02;color:#0B1530;width:1300px">RAZIONALISMO<br>E METAFISICA</div>'
       f'<div style="position:absolute;left:80px;top:560px;width:1310px;padding:26px 40px;border-radius:22px;background:#F4F7FC;border:2px solid #D5DCE8;box-shadow:0 12px 30px rgba(60,70,90,.12)">'
       f'<div style="font:700 22px Figtree;letter-spacing:.2em;color:#2060AF;margin-bottom:10px">ARGOMENTI</div><ul style="margin:0;padding-left:34px;font:600 36px/1.5 Figtree">{li}</ul></div>'
       f'<div class="foot">{MATERIA}</div><div class="pag">Pagina {page}</div><div class="frule"></div>')
    return b+(prof_col([]) if with_prof else '')
def argomenti_card(page,lit):
    args=["L'Italia fascista, il controllo della cultura e delle arti","L'architettura tra tradizione classica e Razionalismo","Il ritorno all'ordine e l'universo della Metafisica","Il Novecento italiano e i movimenti di opposizione"]
    rows=''.join(f'<div class="card{" lit" if i==lit else ""}" style="margin-bottom:22px;padding-top:22px;padding-bottom:22px"><b>{i+1}.</b> {esc(a)}</div>' for i,a in enumerate(args))
    return head('Di cosa parliamo','Gli argomenti della lezione',page)+f'<div class="cards" style="top:300px;width:1760px">{rows}</div>'
def titolo_card(n,tot,title,chips,page,prog=1.0):
    ch=''.join(f'<span class="chip">{esc(c)}</span>' for c in chips)
    op=min(1,prog);ty=int(40*(1-op))
    return dark_scene('t',page,f'<div class="big" style="top:330px;opacity:{op};transform:translateY({ty}px)"><div class="kick">ARGOMENTO {n:02d} / {tot:02d}</div><h1>{esc(title)}</h1><div style="margin-top:34px">{ch}</div></div>',ghost=f'{n:02d}')
def ripasso_card(title,lines,lit,page,prog=1.0):
    rl=''.join(f'<div class="rl{" lit" if i==lit else ""}" style="{"" if i<=lit or lit<0 else "opacity:.0;"}">{esc(l)}</div>' for i,l in enumerate(lines))
    op=min(1,prog)
    return dark_scene('r',page,f'<div class="big" style="top:150px;opacity:{op}"><div class="kick">PILLOLA DI STORIA DELL\'ARTE</div><h1 style="font-size:84px">RIPASSO</h1><h2 style="font-size:40px;color:#9fd0ff;margin-bottom:26px">{esc(title)}</h2>{rl}</div>')
def quiz_card(n,title,page,prog=1.0):
    return dark_scene('q',page,f'<div class="big" style="top:330px;opacity:{min(1,prog)}"><div class="kick">PAUSA DEL VIDEO · QUIZ</div><h1>Quiz {n}</h1><h2>{esc(title)}</h2><div style="margin-top:46px;font:700 30px Figtree;color:#cfe3ff">5 domande · per continuare serve almeno l\'80%</div></div><div class="ghost" style="font-size:420px">?</div>')
def list_card(kick,title,lines,lit,page,fs=36):
    rl=''.join(f'<div class="rl{" lit" if i==lit else ""}" style="font-size:{fs}px;{"" if i<=lit or lit<0 else "opacity:.0;"}">{esc(l)}</div>' for i,l in enumerate(lines))
    return dark_scene('l',page,f'<div class="big" style="top:130px"><div class="kick">{esc(kick)}</div><h1 style="font-size:78px;margin-bottom:26px">{title}</h1>{rl}</div>')
def compiti_intro(page):
    return dark_scene('c',page,'<div class="big" style="top:400px"><div class="kick">PER TE</div><h1 style="font-size:150px">COMPITI</h1></div>')
def compito_card(label,text,page,fs=40):
    return head('Compiti',label,page)+f'<div class="cards" style="top:300px;width:1760px"><div class="card lit" style="font-size:{fs}px;opacity:1">{esc(text)}</div></div>'
def approf_card(label,title,imgs,sentence,page,cur,tot):
    im=''.join(f'<img src="file://{i}" style="max-width:100%;max-height:100%;border-radius:10px;box-shadow:0 14px 34px rgba(60,70,90,.25);margin:0 8px;min-width:0">' for i in imgs)
    return (head(label,title,page)+f'<div class="img" style="left:80px;top:270px;width:760px;height:690px;display:flex">{im}</div>'
        f'<div class="cards" style="left:900px;top:290px;width:940px"><div class="card lit" style="font-size:36px;line-height:1.5;opacity:1">{esc(sentence)}</div>'
        f'<div style="font:700 22px Figtree;letter-spacing:.14em;color:#2060AF;margin-top:20px">{cur} / {tot}</div></div>')
LEG='<div id="leg"><span><i style="background:#FFDCC6;border-color:#C2410C"></i>concetto centrale</span><span><i style="background:#DCEEFB;border-color:#1D4ED8"></i>date e sequenze</span><span><i style="background:#FFF3BF;border-color:#A16207"></i>parole chiave</span><span><i style="background:#DDF3E4;border-color:#15803D"></i>esempi e opere</span><span><i style="background:#EBE3F7;border-color:#6D28D9"></i>conseguenze</span></div>'
MAPCSS='''
#k{position:absolute;left:60px;top:34px;font:700 22px Figtree;letter-spacing:.14em;color:#2060AF}
#f{position:absolute;left:60px;bottom:22px;font:700 20px Figtree;color:#2060AF;letter-spacing:.06em}
#line{position:absolute;left:60px;right:60px;top:78px;height:2px;background:#CBD5E1}
#ttl{position:absolute;left:60px;right:60px;top:96px;text-align:center;font:800 46px 'Bricolage Grotesque';color:#2060AF}
.b{position:absolute;display:flex;align-items:center;justify-content:center;text-align:center;padding:8px 20px;border-radius:14px;font-family:Figtree;font-weight:600;line-height:1.28;color:#0B1530}
.l1{background:#FFDCC6;border:5px solid #C2410C;font:800 50px/1.1 'Bricolage Grotesque';border-radius:18px}
.cel{background:#DCEEFB;border:4px solid #1D4ED8;font-size:36px}
.lil{background:#EBE3F7;border:4px solid #6D28D9;font-size:36px}
.pag{background:#FFF3BF;border:4px solid #A16207;font-size:36px}
.men{background:#DDF3E4;border:4px solid #15803D;font-size:36px}
#leg{position:absolute;right:60px;top:24px;display:flex;gap:14px;font:600 18px Figtree;color:#0B1530}
#leg span{display:flex;align-items:center;gap:6px}#leg i{display:inline-block;width:22px;height:16px;border-radius:4px;border:3px solid}
.hl{box-shadow:0 0 0 9px #FFE600,0 10px 24px rgba(11,21,48,.18)}
svg{position:absolute;left:0;top:0}
'''
def mappa(title,boxes,arrows,shown,hl):
    s=f'<div id="k">MAPPA DEL PROFESSORE</div>{LEG}<div id="line"></div><div id="ttl">{esc(title)}</div><div id="f">{MATERIA}</div>'
    s+='<svg width="1920" height="1080"><defs><marker id="ah" markerUnits="userSpaceOnUse" markerWidth="40" markerHeight="40" refX="20" refY="20" orient="auto"><path d="M0,4 L36,20 L0,36 z" fill="#0B1530"/></marker></defs>'
    for (aid,x1,y1,x2,y2,bid) in arrows:
        if bid in shown:s+=f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="#0B1530" stroke-width="10" marker-end="url(#ah)"/>'
    s+='</svg>'
    for (bid,cls,x,y,w,h,text) in boxes:
        if bid in shown:s+=f'<div class="b {cls}{" hl" if bid==hl else ""}" style="left:{x}px;top:{y}px;width:{w}px;height:{h}px">{text}</div>'
    return s
