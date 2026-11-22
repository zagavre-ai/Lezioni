# Generatori HTML delle schermate (1920x1080), modello Spagnolo con le correzioni 22/11
import html as H, json, os
B='/home/user/w/build'
NOCAM=False
BLU='#2060AF';NOTTE='#0B1530';GIALLO='#FFE600'
CSS=f"""
*{{box-sizing:border-box;margin:0;padding:0}}
html,body{{width:1920px;height:1080px;overflow:hidden;background:#fff;font-family:'Figtree',sans-serif;color:{NOTTE}}}
.logo{{position:absolute;left:80px;top:50px;height:56px}}
.rule{{position:absolute;left:80px;right:80px;top:124px;height:1px;background:#e3e8f1}}
.eyebrow{{position:absolute;left:80px;top:146px;font-weight:800;font-size:23px;letter-spacing:.13em;color:{BLU};text-transform:uppercase;width:1300px;white-space:nowrap;overflow:hidden}}
.cards{{position:absolute;left:80px;width:1300px;display:flex;flex-direction:column;gap:16px}}
.title{{position:absolute;left:80px;top:184px;width:1280px;font-family:'Bricolage Grotesque';font-weight:800;font-size:54px;line-height:62px;color:{NOTTE}}}
.bar{{position:absolute;left:80px;width:84px;height:6px;border-radius:3px;background:{BLU}}}
.foot{{position:absolute;left:80px;right:80px;top:981px;height:1px;background:#e3e8f1}}
.fl{{position:absolute;left:80px;top:1000px;font-weight:700;font-size:22px;letter-spacing:.14em;color:{BLU}}}
.fr{{position:absolute;right:80px;top:1000px;font-weight:700;font-size:22px;letter-spacing:.1em;color:{BLU}}}
.card{{position:relative;width:100%;background:#F6F9FD;border:4px solid #e6ecf5;border-radius:20px;padding:14px 30px 14px 118px;font-size:40px;line-height:60px;box-shadow:0 10px 28px rgba(60,70,90,.10);transition:none}}
.card b{{font-weight:800}}
.card .n{{position:absolute;left:30px;top:16px;width:58px;height:58px;border-radius:29px;background:{BLU};color:#fff;font-weight:800;font-size:32px;line-height:58px;text-align:center}}
.card.dim{{opacity:.78}}
.card.lit{{background:#fff;border:6px solid {GIALLO};padding:10px 28px 10px 116px;box-shadow:0 12px 32px rgba(60,70,90,.16)}}
.card.lit .n{{left:28px;top:14px}}
.card .dot{{display:none}}
.card.lit .dot{{display:block;position:absolute;right:26px;top:24px;width:20px;height:20px;border-radius:10px;background:{GIALLO};box-shadow:0 0 0 3px rgba(11,21,48,.12)}}
.cam{{position:absolute;left:1428px;top:148px;width:412px;height:309px;border-radius:14px;background:#eef1f6;box-shadow:0 14px 34px rgba(60,70,90,.28)}}
.tag{{position:absolute;left:1432px;top:474px;width:410px;height:102px;background:{GIALLO};transform:rotate(-2deg);border-radius:6px;padding:16px 22px;box-shadow:0 8px 20px rgba(60,70,90,.25)}}
.tag .nm{{font-family:'Bricolage Grotesque';font-weight:800;font-size:30px;line-height:36px;color:{NOTTE}}}
.tag .ma{{font-weight:800;font-size:19px;letter-spacing:.07em;color:{NOTTE};margin-top:6px}}
.pc{{position:absolute;left:1428px;top:640px;width:412px}}
.pc .lab{{font-weight:800;font-size:20px;letter-spacing:.14em;color:{BLU};margin-bottom:14px}}
.pc .chip{{display:inline-block;background:#EEF3FB;border:2px solid #d5e0f2;border-radius:999px;padding:6px 18px;margin:0 8px 10px 0;font-weight:700;font-size:26px;line-height:34px;color:{NOTTE}}}
.imgbox{{position:absolute;left:80px;width:1300px;display:flex;align-items:center;justify-content:center}}
.imgbox img{{max-width:1300px;max-height:100%;border-radius:12px;box-shadow:0 12px 30px rgba(60,70,90,.22)}}
"""
def head(extra=''):return f"<!doctype html><meta charset=utf-8><style>{CSS}{extra}</style>"
def chrome(eyebrow,title,pageno,teacher,kw,mat='STORIA V',tl=1,top=0,logo=True):
    x=f'<img class=logo src="{B}/img/logo.svg"><div class=rule></div>'
    if eyebrow:x+=f'<div class=eyebrow>{H.escape(eyebrow)}</div>'
    tH=60*tl+0
    if title:x+=f'<div class=title style="top:{top or 184}px">{H.escape(title)}</div><div class=bar style="top:{(top or 184)+tH+16}px"></div>'
    x+=f'<div class=foot></div><div class=fl>{mat}</div>'
    if pageno:x+=f'<div class=fr>Pagina {pageno}</div>'
    if teacher:
        if not NOCAM:x+='<div class=cam></div><div class=tag><div class=nm>Prof. Giorgio Mazzotti</div><div class=ma>PROF. DI STORIA</div></div>'
        if kw:x+='<div class=pc><div class=lab>PAROLE CHIAVE</div>'+''.join(f'<span class=chip>{H.escape(k)}</span>' for k in kw[:5])+'</div>'
    return x
def nlines(text,cpl=52):
    import math
    return max(1,math.ceil(len(text)/cpl))
def card_h(c):return nlines(c['t'])*60+44
def cards_html(cards,lit,top):
    """cards: lista di dict(t=testo, l=etichetta) ; lit: indice acceso o None"""
    out='';y=top
    for i,c in enumerate(cards):
        cls='card'
        if lit is not None: cls+=' lit' if i==lit else ' dim'
        lab=f"<b>{H.escape(c['l'])}:</b> " if c.get('l') else ''
        out+=f'<div class="{cls}"><div class=n>{i+1}</div>{lab}{H.escape(c["t"])}<div class=dot></div></div>'
    return f'<div class=cards style="top:{top}px">{out}</div>',y
OVERFLOW="<script>window.__overflow=function(){var m=0;var c=document.querySelector('.cards');if(c){var b=c.getBoundingClientRect().bottom;if(b>966)m=Math.round(b-966)}return Math.round(m)}</script>"
def slide(eyebrow,title,cards,lit,pageno,kw,tl=1):
    top=180;cy=top+60*tl+34
    c,_=cards_html(cards,lit,cy)
    return head()+chrome(eyebrow,title,pageno,True,kw,tl=tl,top=top)+c+OVERFLOW
def image_slide(eyebrow,title,img,pageno,kw,tl=1,cap=None):
    top=184;cy=top+60*tl+46
    h=972-cy
    return head()+chrome(eyebrow,title,pageno,True,kw,tl=tl,top=top)+f'<div class=imgbox style="top:{cy}px;height:{h}px"><img src="{img}"></div>'
def cover(title_lines,args,teacher,pageno=1,mappe=False):
    t='<br>'.join(H.escape(x) for x in title_lines)
    items=''.join(f'<li><span>{i+1}</span>{H.escape(a)}</li>' for i,a in enumerate(args))
    css="""
    .ct{position:absolute;left:80px;top:230px;width:1280px;font-family:'Bricolage Grotesque';font-weight:800;font-size:92px;line-height:100px}
    .cb{position:absolute;left:80px;width:110px;height:8px;border-radius:4px;background:#2060AF}
    .arg{position:absolute;left:80px;top:520px;width:1240px;background:#F6F9FD;border-radius:22px;padding:26px 36px;box-shadow:0 12px 30px rgba(60,70,90,.12)}
    .arg h4{font-weight:800;font-size:20px;letter-spacing:.14em;color:#2060AF;margin-bottom:12px}
    .arg ul{list-style:none;columns:2;column-gap:40px}
    .arg li{font-size:30px;line-height:40px;margin-bottom:8px;break-inside:avoid;display:flex;gap:14px}
    .arg li span{flex:none;width:36px;height:36px;border-radius:18px;background:#2060AF;color:#fff;font-weight:800;font-size:22px;text-align:center;line-height:36px;margin-top:2px}
    """
    dy=100 if mappe else 0
    chip='<div style="position:absolute;left:80px;top:210px;font-family:Bricolage Grotesque;font-weight:800;font-size:60px;letter-spacing:.22em;color:#FFE600;background:#0B1530;padding:4px 30px;border-radius:12px">MAPPE</div>' if mappe else ''
    css+=f".ct{{top:{230+dy}px}}.arg{{top:{520+dy}px}}"
    return head(css)+chrome('STORIA · VIDEOLEZIONE',None,pageno,teacher,None)+chip+f'<div class=ct>{t}</div><div class=cb style="top:{230+dy+100*len(title_lines)+24}px"></div><div class=arg><h4>ARGOMENTI</h4><ul>{items}</ul></div>'

# ---------- schermate senza docente ----------
def wslide(eyebrow,title,cards,lit,pageno,tl=1,extra_css=''):
    top=180;cy=top+60*tl+34
    c,_=cards_html(cards,lit,cy)
    css=".cards{width:1760px}.title{width:1760px}.eyebrow{width:1760px}"+extra_css
    return head(css)+chrome(eyebrow,title,pageno,False,None,tl=tl,top=top)+c+OVERFLOW

BLUCSS="""
html,body{background:transparent}
.t{position:absolute;color:#fff}
.eb{font-weight:800;font-size:26px;letter-spacing:.2em;color:#FFC93C}
.big{font-family:'Bricolage Grotesque';font-weight:800;color:#fff}
.sub{font-weight:800;color:#5FD0F0}
.blogo{position:absolute;left:80px;top:50px;height:56px;filter:brightness(0) invert(1);opacity:.9}
"""
def blu_bg():
    return head("body{background:#0B1530}")+"""<div style="position:absolute;inset:0;background:
    radial-gradient(900px 700px at 15% 20%,rgba(32,96,175,.55),transparent 70%),
    radial-gradient(1100px 800px at 85% 85%,rgba(20,60,130,.55),transparent 70%),
    radial-gradient(500px 400px at 70% 15%,rgba(95,208,240,.18),transparent 70%),
    radial-gradient(600px 500px at 30% 95%,rgba(255,201,60,.10),transparent 70%),#0B1530"></div>"""
def blu_fg(inner):
    return head(BLUCSS)+f'<img class=blogo src="{B}/img/logo.svg">'+inner
def blu_title(n,tot,nome):
    segs=''.join(f'<span style="display:inline-block;width:70px;height:6px;border-radius:3px;margin-right:10px;background:{"#FFC93C" if i+1==n else "rgba(255,255,255,.25)"}"></span>' for i in range(tot))
    return blu_fg(f'<div class="t eb" style="left:120px;top:380px">ARGOMENTO {n:02d} / {tot:02d}</div><div class="t big" style="left:120px;top:440px;width:1500px;font-size:96px;line-height:104px">{H.escape(nome)}</div><div class=t style="left:120px;top:820px">{segs}</div>')
def blu_pill(nome):
    return blu_fg(f'<div class="t eb" style="left:120px;top:300px">PILLOLA DI RIPASSO</div><div class="t big" style="left:120px;top:350px;font-size:190px;line-height:200px">RIPASSO</div><div class="t sub" style="left:120px;top:590px;width:1500px;font-size:66px;line-height:74px">{H.escape(nome)}</div><div class=t style="left:120px;top:820px;font-size:34px;font-weight:600;background:rgba(255,255,255,.1);border-radius:14px;padding:14px 26px;color:#dbe6f8">Guarda lo schema e ripeti ad alta voce.</div>')
def blu_quiz(n,nome):
    return blu_fg(f'<div class="t eb" style="left:120px;top:330px">PAUSA DEL VIDEO · QUIZ</div><div class="t big" style="left:120px;top:390px;font-size:120px;line-height:130px">Quiz {n}</div><div class="t sub" style="left:120px;top:540px;width:1300px;font-size:64px;line-height:72px;color:#FFC93C">{H.escape(nome)}</div><div class=t style="left:120px;top:800px;font-size:34px;font-weight:600;background:rgba(255,255,255,.1);border-radius:14px;padding:14px 26px;color:#dbe6f8">5 domande · serve almeno l\'80% per continuare</div><div style="position:absolute;left:1480px;top:400px;width:260px;height:260px;border-radius:130px;border:5px solid #5FD0F0"></div><div style="position:absolute;left:1560px;top:468px;width:0;height:0;border-left:92px solid #5FD0F0;border-top:62px solid transparent;border-bottom:62px solid transparent"></div>')
def blu_rows(titolo,eb,righe,lit,txt=None):
    """righe: lista (num,nome); lit: indice acceso; txt: testo grande del ripasso"""
    r=''
    for i,(n,nome) in enumerate(righe):
        on=(i==lit);bg='rgba(255,201,60,.95)' if on else 'rgba(255,255,255,.10)';col='#0B1530' if on else '#e6eefb'
        r+=f'<div style="position:absolute;left:1260px;top:{190+i*104}px;width:560px;height:88px;border-radius:16px;background:{bg};color:{col};font-weight:800;font-size:30px;line-height:34px;padding:10px 20px 10px 78px;display:flex;align-items:center"><span style="position:absolute;left:18px;top:18px;width:52px;height:52px;border-radius:26px;background:{"#0B1530" if on else "#2060AF"};color:#fff;font-size:28px;line-height:52px;text-align:center">{n}</span>{H.escape(nome)}</div>'
    body=f'<div class="t eb" style="left:120px;top:190px">{H.escape(eb)}</div><div class="t big" style="left:120px;top:240px;font-size:104px;line-height:110px;color:#FFC93C;width:1000px">{H.escape(titolo)}</div>'
    if txt:body+=f'<div class=t style="left:120px;top:520px;width:1030px;font-size:44px;line-height:64px;font-weight:600">{H.escape(txt)}</div>'
    return blu_fg(body+r)
def blu_text(eb,big,sub=None):
    s=f'<div class="t eb" style="left:120px;top:380px">{H.escape(eb)}</div><div class="t big" style="left:120px;top:440px;width:1600px;font-size:100px;line-height:108px">{H.escape(big)}</div>'
    if sub:s+=f'<div class="t sub" style="left:120px;top:660px;width:1600px;font-size:50px;line-height:62px">{H.escape(sub)}</div>'
    return blu_fg(s)

# ---------- mappe del prof (ridisegnate, modello BES) ----------
COL={'pesca':('#FFD9C2','#F08A4B'),'celeste':('#CFE8FB','#3FA0E0'),'paglierino':('#FFF4B8','#D9B500'),'menta':('#CDEFD9','#3DB874'),'lilla':('#E3D7F7','#8F63D6')}
LEG=[('pesca','Concetto centrale'),('celeste','Date e sequenze'),('paglierino','Parole chiave'),('menta','Esempi e opere'),('lilla','Conseguenze')]
MAPS=[
 dict(titolo="Quali aspetti presentano gli anni Sessanta negli Stati Uniti?",centro="GLI STATI UNITI",cols=[
   [("vedono","la presidenza Kennedy (1961-1963)",'celeste'),("con","la lotta contro la miseria, le disuguaglianze e la segregazione razziale",'paglierino')],
   [("si impegnano nella","guerra del Vietnam (1964-1973)",'celeste'),("che si rivela","fallimentare e impopolare",'lilla')],
   [("vedono","studenti, afroamericani e cittadini ostili alla guerra in Vietnam",'paglierino'),("dare vita a","un movimento di contestazione mondiale (1968)",'lilla')]]),
 dict(titolo="Cosa accade nel mondo socialista negli anni Sessanta?",centro="L'UNIONE SOVIETICA",cols=[
   [("vede al governo","Chruščëv (1953)",'celeste'),("che teorizza","la coesistenza pacifica con gli Stati Uniti",'paglierino')],
   [("approva","la costruzione del muro di Berlino (1961)",'celeste'),("e provoca","la crisi dei missili a Cuba",'lilla')],
   [("passa sotto il governo di","Brežnev (1964)",'celeste'),("che","reprime le riforme in Cecoslovacchia (1968)",'lilla')]]),
 dict(titolo="Cosa accade in Medio Oriente negli anni Sessanta?",centro="IN MEDIO ORIENTE",cols=[
   [("lo","Egitto",'paglierino'),("si avvicina a","l'Unione Sovietica",'paglierino'),("dalla quale","riceve aiuti militari",'lilla')],
   [("nasce","l'Organizzazione per la liberazione della Palestina (1964)",'celeste')],
   [("lo","Stato di Israele",'paglierino'),("inizia","la guerra dei Sei giorni (1967)",'celeste'),("contro","i paesi arabi confinanti",'lilla')]]),
]
CX=[330,960,1590];BW=540
def map_nodes(m):
    """elenco ordinato dei nodi (ramo per ramo): ('c',...) centro poi (col,riga)"""
    n=[('centro',None)]
    for ci,col in enumerate(m['cols']):
        for ri in range(len(col)):n.append(((ci,ri),None))
    return n
def _wid(n,txt):return 720 if (n==3 and len(txt)>50) else BW
def _nl(txt,w):
    import math
    cpl=27 if w==BW else 37
    return max(1,math.ceil(len(txt)/cpl))
def map_geom(m):
    nb=len(m['cols']);rows=max(len(c) for c in m['cols'])
    hs=[[_nl(c[ri][1],_wid(nb and 3 if m['centro']=="IN MEDIO ORIENTE" and len(c[ri][1])>50 else 0,c[ri][1]))*44+48 if ri<len(c) else 0 for c in m['cols']] for ri in range(rows)]
    tops=[450 if rows==2 else 410]
    for ri in range(rows-1):tops.append(tops[-1]+max(hs[ri])+(100 if rows==2 else 76))
    return tops,hs
def map_html(m,shown,lit,pageno,show_title=True):
    tops,hs=map_geom(m);three=len(tops)==3;CY=214 if three else 232;BY=330 if three else 372
    svg='';boxes='';labs=''
    if 'centro' in shown:
        on=(lit=='centro');f,b=COL['pesca']
        boxes+=f'<div class=mb style="left:{960-290}px;top:{CY}px;width:580px;height:88px;background:{"#FFE600" if on else f};border-color:{b};font-weight:800;letter-spacing:.08em;line-height:88px;text-align:center;padding:0">{H.escape(m["centro"])}</div>'
    xs=[CX[i] for i,c in enumerate(m['cols']) if (i,0) in shown]
    if 'centro' in shown and xs:
        svg+=f'<line x1=960 y1={CY+88} x2=960 y2={BY} stroke="#0B1530" stroke-width=3 />'
        svg+=f'<line x1={min(xs+[960])} y1={BY} x2={max(xs+[960])} y2={BY} stroke="#0B1530" stroke-width=3 />'
    for ci,col in enumerate(m['cols']):
        prev_bottom=BY
        for ri,(lab,txt,c) in enumerate(col):
            if (ci,ri) not in shown:continue
            on=((ci,ri)==lit);f,b=COL[c]
            y=tops[ri];wd=720 if (m['centro']=="IN MEDIO ORIENTE" and len(txt)>50) else BW;h=hs[ri][ci]
            boxes+=f'<div class=mb style="left:{CX[ci]-wd//2}px;top:{y}px;width:{wd}px;height:{h}px;background:{"#FFE600" if on else f};border-color:{b}">{H.escape(txt)}</div>'
            ys=prev_bottom
            svg+=f'<line x1={CX[ci]} y1={ys} x2={CX[ci]} y2={y-4} stroke="#0B1530" stroke-width=3 /><path d="M{CX[ci]-10} {y-18} L{CX[ci]} {y-3} L{CX[ci]+10} {y-18}" fill=none stroke="#0B1530" stroke-width=3 />'
            labs+=f'<div class=ml style="left:{CX[ci]-260}px;top:{(ys+y)//2-24}px;width:520px"><span>{H.escape(lab)}</span></div>'
            prev_bottom=y+h
    css="""
    .mb{position:absolute;border:4px solid;border-radius:20px;padding:0 18px;font-weight:700;font-size:34px;line-height:44px;text-align:center;box-shadow:0 8px 18px rgba(60,70,90,.14);display:flex;align-items:center;justify-content:center;color:#0B1530}
    .ml{position:absolute;white-space:nowrap;text-align:center;font-weight:600;font-size:34px;line-height:48px;height:48px}
    .ml span{background:#fff;padding:0 10px}
    .leg{position:absolute;left:1540px;top:140px;width:300px}
    .leg div{display:flex;align-items:center;gap:10px;font-weight:700;font-size:20px;line-height:34px;color:#0B1530}
    .leg i{display:inline-block;width:22px;height:22px;border-radius:6px;border:3px solid}
    .mt{position:absolute;left:80px;width:1400px;font-family:'Bricolage Grotesque';font-weight:800;font-size:46px;line-height:54px;color:#2060AF}
    svg{position:absolute;left:0;top:0}
    """
    leg='<div class=leg>'+''.join(f'<div><i style="background:{COL[k][0]};border-color:{COL[k][1]}"></i>{n}</div>' for k,n in LEG)+'</div>'
    t=(f'<div class=mt>{H.escape(m["titolo"])}</div>' if show_title else '').replace('class=mt>',f'class=mt style="top:{135 if three else 150}px">')
    base=head(css)+f'<img class=logo src="{B}/img/logo.svg"><div class=rule></div>'
    return base+t+leg+f'<svg width=1920 height=1080>{svg}</svg>'+boxes+labs+f'<div class=foot></div><div class=fl>STORIA V</div><div class=fr>Pagina {pageno}</div>'
