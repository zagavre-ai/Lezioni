# Modelli grafici (HTML) delle schede e delle slide. Modello: Spagnolo lez. 1 con le aggiunte approvate.
import html as _h, json
from PIL import ImageFont
FD='/root/.fonts'
LOGO='file:///home/user/Lezioni/kit/docenti/Telesio_logo_blu.svg'
MATERIA="STORIA DELL'ARTE V"
BLU='#2060AF'; NOTTE='#0B1530'; GIALLO='#FFE600'
CSS=f"""
@font-face{{font-family:Fig;font-weight:400;src:url(file://{FD}/Figtree-Regular.ttf)}}
@font-face{{font-family:Fig;font-weight:600;src:url(file://{FD}/Figtree-SemiBold.ttf)}}
@font-face{{font-family:Fig;font-weight:700;src:url(file://{FD}/Figtree-Bold.ttf)}}
@font-face{{font-family:Fig;font-weight:800;src:url(file://{FD}/Figtree-ExtraBold.ttf)}}
@font-face{{font-family:Bri;font-weight:800;src:url(file://{FD}/BricolageGrotesque-ExtraBold.ttf)}}
*{{box-sizing:border-box}}
html,body{{margin:0;width:1920px;height:1080px;overflow:hidden;background:#fff;font-family:Fig;color:{NOTTE}}}
.logo{{position:absolute;left:80px;top:52px;height:54px}}
.hl{{position:absolute;left:80px;right:80px;top:124px;height:1px;background:#E2E8F0}}
.fl{{position:absolute;left:80px;right:80px;top:981px;height:1px;background:#E2E8F0}}
.foot{{position:absolute;left:80px;top:998px;font:700 21px Fig;letter-spacing:.14em;color:{BLU}}}
.pag{{position:absolute;right:80px;top:998px;font:700 21px Fig;letter-spacing:.1em;color:{BLU}}}
.kick{{position:absolute;left:80px;top:146px;font:700 24px Fig;letter-spacing:.16em;color:{BLU};text-transform:uppercase;max-width:1300px;white-space:nowrap}}
.tit{{position:absolute;left:80px;top:184px;width:1305px;font:800 62px/1.08 Bri;color:{NOTTE}}}
.bar{{position:absolute;left:80px;width:86px;height:7px;border-radius:4px;background:{BLU}}}
.card{{position:absolute;left:80px;width:1305px;background:#fff;border:3px solid #E2E8F0;border-radius:20px;
  box-shadow:0 10px 26px rgba(15,23,42,.10);padding:24px 36px 24px 66px;font:600 40px/52px Fig;color:{NOTTE};opacity:.5}}
.card.on{{opacity:1;border:6px solid {GIALLO};padding:21px 33px 21px 63px;box-shadow:0 14px 32px rgba(15,23,42,.16)}}
.card.on:before{{content:"";position:absolute;left:26px;top:34px;width:20px;height:20px;border-radius:50%;background:{GIALLO};box-shadow:0 0 0 3px {NOTTE}22}}
.card b{{font-weight:800}}
.shadow{{position:absolute;left:1428px;top:148px;width:412px;height:309px;border-radius:18px;background:#fff;box-shadow:0 14px 34px rgba(15,23,42,.28)}}
.band{{position:absolute;left:1428px;top:466px;width:416px;height:104px;background:{GIALLO};transform:rotate(-3deg);border-radius:6px;
  box-shadow:0 10px 24px rgba(15,23,42,.20);padding:16px 22px}}
.band .n{{font:800 36px/1.1 Bri;color:{NOTTE}}}
.band .m{{font:700 19px/1.4 Fig;letter-spacing:.06em;color:{NOTTE};margin-top:6px}}
.kwh{{position:absolute;left:1428px;top:636px;font:700 20px Fig;letter-spacing:.16em;color:{BLU}}}
.kw{{position:absolute;left:1428px;width:412px}}
.kw span{{display:inline-block;margin:0 10px 12px 0;padding:6px 16px;border-radius:999px;background:#EAF1FB;color:{NOTTE};font:700 28px/1.25 Fig;border:2px solid #C9DAF2}}
.dark{{background:radial-gradient(1200px 700px at 78% 18%,#16336E 0%,#0B1530 62%);color:#fff}}
.dark .dl{{position:absolute;left:80px;right:80px;top:124px;height:1px;background:#ffffff33}}
.dark .logo{{filter:brightness(0) invert(1)}}
.dark .foot,.dark .pag{{color:#9FB6E0}}
.dark .fl{{background:#ffffff33}}
.dk{{position:absolute;left:80px;top:158px;font:700 26px Fig;letter-spacing:.2em;color:{GIALLO};text-transform:uppercase}}
.dt{{position:absolute;left:80px;width:1400px;font:800 92px/1.05 Bri;color:#fff}}
.dbar{{position:absolute;left:80px;width:120px;height:9px;border-radius:5px;background:{GIALLO}}}
"""
_f40=ImageFont.truetype(f'{FD}/Figtree-SemiBold.ttf',40)
def n_lines(text,width=1205):
    n=1;cur=''
    for w in text.split():
        t=(cur+' '+w).strip()
        if _f40.getlength(t)>width and cur:n+=1;cur=w
        else:cur=t
    return n
def card_h(text,width=1205):return n_lines(text,width)*52+54
def esc(s):return _h.escape(s,quote=False)
def md(s):  # **grassetto** minimo
    out='';b=False
    for i,p in enumerate(esc(s).split('**')):out+=('<b>%s</b>'%p) if i%2 else p
    return out
def head(pageno=None,dark=False,foot=True,prof=False):
    s=f'<img class=logo src="{LOGO}">'+('<div class=dl></div>' if dark else '<div class=hl></div>')
    return s
def foot(pageno,dark=False):
    return f'<div class=fl></div><div class=foot>{esc(MATERIA)}</div><div class=pag>Pagina {pageno}</div>'
def doc(body,cls=''):
    return f'<!doctype html><html><head><meta charset=utf-8><style>{CSS}</style></head><body class="{cls}">{body}</body></html>'

def slide_text(kicker,title,cards,active,kws,pageno,prof=True):
    """cards: lista di testi; active: indice acceso (None=tutte spente)."""
    nt=n_lines(title,1300) if False else 1
    # titolo: una riga; se lunga va su due (larghezza 1305)
    ft=ImageFont.truetype(f'{FD}/BricolageGrotesque-ExtraBold.ttf',62)
    two=ft.getlength(title)>1290
    ty=184;bar=ty+(140 if two else 74)
    y=max(bar+36,330) if not two else bar+36
    body=head()+f'<div class=kick>{esc(kicker)}</div><div class=tit style="top:{ty}px">{md(title)}</div><div class=bar style="top:{bar}px"></div>'
    for i,c in enumerate(cards):
        h=card_h(c)
        body+=f'<div class="card{" on" if i==active else ""}" data-chk="c{i}" style="top:{y}px;height:{h}px">{md(c)}</div>'
        y+=h+22
    body+=prof_col(kws,prof)+foot(pageno)
    return doc(body),y-22

def prof_col(kws,prof=True):
    s=''
    if prof:
        s+='<div class=shadow></div><div class=band><div class=n>Giorgio Mazzotti</div><div class=m>PROF. DI STORIA DELL\'ARTE</div></div>'
    if kws:
        s+='<div class=kwh>PAROLE CHIAVE</div><div class=kw style="top:676px">'+''.join(f'<span>{esc(k)}</span>' for k in kws[:5])+'</div>'
    return s

def slide_image(kicker,title,img,caption,kws,pageno,prof=True):
    ft=ImageFont.truetype(f'{FD}/BricolageGrotesque-ExtraBold.ttf',62)
    two=ft.getlength(title)>1290
    ty=184;bar=ty+(140 if two else 74);y=bar+30
    h=930-y
    body=head()+f'<div class=kick>{esc(kicker)}</div><div class=tit style="top:{ty}px">{md(title)}</div><div class=bar style="top:{bar}px"></div>'
    body+=f'<div style="position:absolute;left:80px;top:{y}px;width:1305px;height:{h}px;display:flex;align-items:center;justify-content:center"><img src="file://{img}" style="max-width:1305px;max-height:{h}px;border-radius:10px;box-shadow:0 14px 34px rgba(15,23,42,.30)"></div>'
    body+=f'<div style="position:absolute;left:80px;top:{930}px;width:1305px;text-align:center;font:600 27px/1.2 Fig;color:#334155">{esc(caption)}</div>'
    body+=prof_col(kws,prof)+foot(pageno)
    return doc(body)

def dark_title(n,title,pageno):
    ft=ImageFont.truetype(f'{FD}/BricolageGrotesque-ExtraBold.ttf',92)
    lines=1 if ft.getlength(title)<1380 else 2
    ty=420;bar=ty+lines*97+26
    body=head(dark=True)+f'<div class=dk style="top:300px">Argomento {n}</div><div class=dt style="top:{ty}px">{esc(title)}</div><div class=dbar style="top:{bar}px"></div>'+foot(pageno)
    return doc(body,'dark')

def dark_simple(label,title,sub,pageno,tag=None):
    ft=ImageFont.truetype(f'{FD}/BricolageGrotesque-ExtraBold.ttf',92)
    lines=1 if ft.getlength(title)<1380 else 2
    ty=400;bar=ty+lines*97+28
    body=head(dark=True)+f'<div class=dk style="top:290px">{esc(label)}</div><div class=dt style="top:{ty}px">{esc(title)}</div><div class=dbar style="top:{bar}px"></div>'
    if sub:body+=f'<div style="position:absolute;left:80px;top:{bar+50}px;width:1500px;font:600 44px/1.35 Fig;color:#DCE7FA">{esc(sub)}</div>'
    return doc(body+foot(pageno),'dark')

def dark_lines(label,title,lines,active,pageno,fs=44,hl=GIALLO):
    """pillola / ripasso: righe che si accendono con la voce (active = n righe accese, l'ultima in giallo)."""
    body=head(dark=True)+f'<div class=dk>{esc(label)}</div><div class=dt style="top:206px;font-size:54px;width:1760px;white-space:nowrap">{esc(title)}</div><div class=dbar style="top:290px"></div>'
    y=336
    for i,t in enumerate(lines):
        if i>active:break
        cur=(i==active)
        hh=n_lines_f(t,1560,fs)*round(fs*1.3)+36
        bg='#FFE60022' if cur else '#ffffff10'
        bd=f'3px solid {GIALLO}' if cur else '3px solid #ffffff22'
        body+=f'<div data-chk="l{i}" style="position:absolute;left:80px;top:{y}px;width:1700px;height:{hh}px;border-radius:18px;background:{bg};border:{bd};padding:16px 36px 16px 76px;font:700 {fs}px/1.3 Fig;color:#fff"><span style="position:absolute;left:30px;top:{hh//2-11}px;width:22px;height:22px;border-radius:50%;background:{GIALLO if cur else "#6F8BC6"}"></span>{esc(t)}</div>'
        y+=hh+18
    return doc(body+foot(pageno),'dark')
def n_lines_f(text,width,fs):
    f=ImageFont.truetype(f'{FD}/Figtree-Bold.ttf',fs);n=1;cur=''
    for w in text.split():
        t=(cur+' '+w).strip()
        if f.getlength(t)>width and cur:n+=1;cur=w
        else:cur=t
    return n

def dark_approf(title,bullets,active,img,imgcap,pageno):
    """approfondimento: punti a sinistra che si accendono, immagine a destra."""
    body=head(dark=True)+f'<div class=dk>Approfondimento</div><div class=dt style="top:196px;font-size:54px;width:1760px;white-space:nowrap">{esc(title)}</div><div class=dbar style="top:276px"></div>'
    y=312
    for i,t in enumerate(bullets):
        if i>active:break
        cur=(i==active);fs=33
        hh=n_lines_f(t,790,fs)*44+30
        bg='#FFE60022' if cur else '#ffffff10';bd=f'3px solid {GIALLO}' if cur else '3px solid #ffffff22'
        body+=f'<div data-chk="b{i}" style="position:absolute;left:80px;top:{y}px;width:900px;height:{hh}px;border-radius:18px;background:{bg};border:{bd};padding:13px 30px 13px 70px;font:700 {fs}px/44px Fig;color:#fff"><span style="position:absolute;left:28px;top:{hh//2-10}px;width:20px;height:20px;border-radius:50%;background:{GIALLO if cur else "#6F8BC6"}"></span>{esc(t)}</div>'
        y+=hh+16
    if img:
        body+=f'<div style="position:absolute;left:1030px;top:330px;width:810px;height:590px;display:flex;align-items:center;justify-content:center"><img src="file://{img}" style="max-width:810px;max-height:560px;border-radius:12px;box-shadow:0 18px 40px rgba(0,0,0,.45)"></div>'
        if imgcap:body+=f'<div style="position:absolute;left:1030px;top:918px;width:810px;text-align:center;font:600 24px Fig;color:#BCD0F2">{esc(imgcap)}</div>'
    return doc(body+foot(pageno),'dark')

def copertina(titolo,argomenti,pageno,prof=False):
    cols=[argomenti[:3],argomenti[3:]]
    body=head()+f'<div class=kick style="top:226px">STORIA DELL\'ARTE V · VIDEOLEZIONE</div><div class=tit style="top:274px;font-size:92px;line-height:1.05;width:1300px">{esc(titolo)}</div><div class=bar style="top:396px;width:110px;height:8px"></div>'
    body+='<div style="position:absolute;left:80px;top:470px;width:1305px;background:#F5F8FD;border:3px solid #E2E8F0;border-radius:22px;box-shadow:0 12px 30px rgba(15,23,42,.10);padding:28px 40px 20px 40px">'
    body+=f'<div style="font:800 20px Fig;letter-spacing:.18em;color:{BLU};margin-bottom:14px">ARGOMENTI</div><div style="display:flex;gap:40px">'
    for col in cols:
        body+='<ul style="margin:0;padding:0 0 0 0;list-style:none;width:600px">'+''.join(f'<li style="font:600 31px/1.35 Fig;margin-bottom:10px;padding-left:34px;position:relative"><span style="position:absolute;left:4px;top:15px;width:12px;height:12px;border-radius:50%;background:{BLU}"></span>{esc(a)}</li>' for a in col)+'</ul>'
    body+='</div></div>'
    if prof:body+=prof_col([],True)
    return doc(body+foot(pageno))

def argomenti_slide(argomenti,active,pageno):
    body=head()+f'<div class=kick>STORIA DELL\'ARTE V · VIDEOLEZIONE</div><div class=tit style="top:184px">Gli argomenti di oggi</div><div class=bar style="top:258px"></div>'
    y=300
    for i,a in enumerate(argomenti):
        cur=(i==active);on=cur or active is None
        body+=f'<div class="card{" on" if cur else ""}" style="top:{y}px;height:92px;padding-top:{16 if not cur else 13}px;opacity:{1 if on else .45}"><span style="font:800 34px Bri;color:{BLU};margin-right:20px">{i+1:02d}</span>{esc(a)}</div>'
        y+=108
    return doc(body+foot(pageno))

def glossario(terms,active,pageno):
    """terms: [(termine, definizione)]; mostra tutti i gia' detti, l'ultimo in evidenza."""
    body=head(dark=True)+f'<div class=dk>Glossario</div><div class=dt style="top:190px;font-size:54px">Le parole da ricordare</div><div class=dbar style="top:272px"></div>'
    n=len(terms);half=(n+1)//2;cols=[terms[:half],terms[half:]]
    base=0
    for ci,col in enumerate(cols):
        y=300
        for j,(t,d) in enumerate(col):
            idx=base+j
            if idx>active:break
            cur=(idx==active)
            bg='#FFE60022' if cur else '#ffffff10';bd=f'3px solid {GIALLO}' if cur else '3px solid #ffffff22'
            hh=124
            body+=f'<div data-chk="g{idx}" style="position:absolute;left:{80+ci*870}px;top:{y}px;width:830px;height:{hh}px;border-radius:16px;background:{bg};border:{bd};padding:8px 22px;overflow:hidden"><div style="font:800 31px/1.2 Fig;color:{GIALLO}">{esc(t)}</div><div style="font:600 28px/1.25 Fig;color:#fff">{esc(d)}</div></div>'
            y+=hh+10
        base+=len(col)
    return doc(body+foot(pageno),'dark')

def compiti(items,active,pageno,finale=None):
    body=head(dark=True)+f'<div class=dk>Compiti</div><div class=dt style="top:190px;font-size:64px">Il compito per te</div><div class=dbar style="top:278px"></div>'
    y=320
    for i,t in enumerate(items):
        if i>active:break
        cur=(i==active);fs=33;hh=n_lines_f(t,1560,fs)*44+34
        bg='#FFE60022' if cur else '#ffffff10';bd=f'4px solid {GIALLO}' if cur else '3px solid #ffffff22'
        body+=f'<div data-chk="k{i}" style="position:absolute;left:80px;top:{y}px;width:1760px;height:{hh}px;border-radius:16px;background:{bg};border:{bd};padding:14px 30px 14px 100px;font:600 {fs}px/44px Fig;color:#fff"><span style="position:absolute;left:28px;top:{hh//2-26}px;font:800 44px Bri;color:{GIALLO}">{i+1}</span>{esc(t)}</div>'
        y+=hh+12
    if finale:
        body+=f'<div style="position:absolute;left:80px;top:{y+14}px;width:1760px;font:700 36px/1.3 Fig;color:{GIALLO}">{esc(finale)}</div>'
    return doc(body+foot(pageno),'dark')

# ---- mappa del docente (modello BES) ----
COL={'pesca':('#FFDCC6','#C2410C'),'celeste':('#DCEEFB','#1D4ED8'),'paglierino':('#FFF3BF','#A16207'),'menta':('#DDF3E4','#15803D'),'lilla':('#EBE3F7','#6D28D9')}
def mappa(title,boxes,arrows,shown,hl,pageno,final=False):
    """boxes: {id:(x,y,w,h,colore,testo)}; arrows: {id:(x1,y1,x2,y2)}; shown: ids visibili; hl: id acceso in giallo."""
    leg=''.join(f'<span style="display:flex;align-items:center;gap:7px"><i style="display:inline-block;width:24px;height:17px;border-radius:4px;border:3px solid {COL[k][1]};background:{COL[k][0]}"></i>{t}</span>' for k,t in [('pesca','concetto centrale'),('celeste','date e sequenze'),('paglierino','parole chiave'),('menta','esempi e opere'),('lilla','conseguenze')])
    body=head()+f'<div class=kick>MAPPA</div><div style="position:absolute;right:80px;top:148px;display:flex;gap:18px;font:700 19px Fig;color:{NOTTE}">{leg}</div>'
    body+=f'<div style="position:absolute;left:80px;top:182px;width:1760px;font:800 46px/1.12 Bri;color:{NOTTE}">{esc(title)}</div>'
    body+='<svg width=1920 height=1080 style="position:absolute;left:0;top:0"><defs><marker id=ah markerUnits=userSpaceOnUse markerWidth=40 markerHeight=40 refX=22 refY=20 orient=auto><path d="M0,5 L36,20 L0,35 z" fill="#0B1530"/></marker></defs>'
    for k,(x1,y1,x2,y2) in arrows.items():
        if k in shown:body+=f'<line x1={x1} y1={y1} x2={x2} y2={y2} stroke="#0B1530" stroke-width=9 marker-end="url(#ah)"/>'
    body+='</svg>'
    for k,(x,y,w,h,c,t) in boxes.items():
        if k not in shown:continue
        bg,bd=COL[c];on=(k==hl)
        sh=f'box-shadow:0 0 0 9px {GIALLO},0 12px 26px rgba(11,21,48,.20);' if on else 'box-shadow:0 8px 20px rgba(11,21,48,.12);'
        fs=44 if c=='pesca' else 38
        body+=f'<div data-chk="m{k}" style="position:absolute;left:{x}px;top:{y}px;width:{w}px;height:{h}px;background:{bg};border:5px solid {bd};border-radius:16px;{sh}display:flex;align-items:center;justify-content:center;text-align:center;padding:10px 24px;font:600 {fs}px/1.28 Fig;color:{NOTTE}"><div>{md(t)}</div></div>'
    return doc(body+foot(pageno))

def quiz_card(n,pageno):
    return dark_simple('Quiz',f'Quiz · argomento {n}','Cinque domande. Per continuare serve almeno l\'80% di risposte giuste.',pageno)
