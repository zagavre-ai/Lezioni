import re,html,json
from PIL import ImageFont
F='/root/.fonts/'
FM=ImageFont.truetype(F+'Figtree-Medium.ttf',40);FB=ImageFont.truetype(F+'Figtree-Bold.ttf',40)
TXTW=1305-2*34-8  # larghezza testo card
def split_card(p):
    m=re.match(r'^([^:]{2,70}):\s*(.*)$',p)
    return (m.group(1),m.group(2)) if m else ('',p)
def lines(lead,body):
    words=([(w,FB) for w in (lead+':').split()] if lead else [])+[(w,FM) for w in body.split()]
    n=1;x=0
    for w,f in words:
        l=f.getlength(w+' ')
        if x+l>TXTW and x>0:n+=1;x=0
        x+=l
    return n
def altezza(p):
    lead,body=split_card(p);return lines(lead,body)*60+44
def clausole(p):
    lead,body=split_card(p)
    parts=re.split(r'(?<=[,;:])\s+',body)
    # unisci pezzi molto corti
    out=[];
    for x in parts:
        if out and len(x)<28:out[-1]+=' '+x
        else:out.append(x)
    return lead,out
def finestre(pars,maxh=640,maxn=3):
    """raggruppa le card (in ordine) in finestre da <=3 card e che entrano nello spazio"""
    W=[];cur=[];h=0
    for i,p in enumerate(pars):
        hh=altezza(p)+22
        if cur and (len(cur)>=maxn or h+hh>maxh):W.append(cur);cur=[];h=0
        cur.append(i);h+=hh
    if cur:W.append(cur)
    return W
CSS="""
@font-face{font-family:Fig;font-weight:500;src:url(file:///root/.fonts/Figtree-Medium.ttf)}
@font-face{font-family:Fig;font-weight:700;src:url(file:///root/.fonts/Figtree-Bold.ttf)}
@font-face{font-family:Fig;font-weight:800;src:url(file:///root/.fonts/Figtree-ExtraBold.ttf)}
@font-face{font-family:Bri;font-weight:800;src:url(file:///root/.fonts/BricolageGrotesque-ExtraBold.ttf)}
*{box-sizing:border-box;margin:0}
html,body{width:1920px;height:1080px;background:#fff;overflow:hidden;font-family:Fig;color:#0B1530}
#logo{position:absolute;left:80px;top:48px;height:58px}
#hl{position:absolute;left:80px;right:80px;top:124px;height:2px;background:#E3E8F0}
#fl{position:absolute;left:80px;right:80px;top:981px;height:2px;background:#E3E8F0}
#kick{position:absolute;left:80px;top:146px;font:700 24px Fig;letter-spacing:.14em;color:#2060AF;text-transform:uppercase}
#tit{position:absolute;left:80px;top:188px;width:1290px;font:800 60px/1.08 Bri;color:#0B1530}
#bar{position:absolute;left:80px;width:85px;height:7px;border-radius:4px;background:#2060AF}
#foot{position:absolute;left:80px;top:1004px;font:700 22px Fig;letter-spacing:.12em;color:#2060AF}
#pag{position:absolute;right:80px;top:1004px;font:700 22px Fig;letter-spacing:.1em;color:#2060AF}
#cam{position:absolute;left:1428px;top:148px;width:412px;height:309px;border-radius:18px;background:#fff;box-shadow:0 14px 34px rgba(60,70,90,.28)}
#band{position:absolute;left:1428px;top:478px;width:416px;height:102px;background:#FFE600;transform:rotate(-3deg);border-radius:6px;box-shadow:0 10px 24px rgba(60,70,90,.25);padding:20px 24px}
#band b{display:block;font:800 36px Bri;color:#0B1530}#band i{display:block;font:700 20px Fig;font-style:normal;letter-spacing:.06em;margin-top:6px}
#kw{position:absolute;left:1428px;top:640px;width:412px}
#kw h4{font:800 20px Fig;letter-spacing:.16em;color:#2060AF;margin-bottom:12px}
#kw div.k{font:700 28px/1.2 Fig;padding:7px 14px;margin-bottom:8px;background:#EEF3FB;border-radius:10px;border-left:6px solid #2060AF}
#cards{position:absolute;left:80px;width:1305px}
.c{position:relative;padding:11px 34px 11px 34px;margin-bottom:22px;border-radius:20px;background:#fff;border:3px solid #E3E8F0;box-shadow:0 8px 22px rgba(60,70,90,.12);font:500 40px/60px Fig;opacity:.5}
.c b{font-weight:800}
.c.on{opacity:1;border:6px solid #FFE600;padding:8px 31px;box-shadow:0 10px 26px rgba(60,70,90,.2)}
.c.on::before{content:"";position:absolute;left:-17px;top:24px;width:26px;height:26px;border-radius:50%;background:#FFE600;box-shadow:0 0 0 3px #fff,0 2px 8px rgba(60,70,90,.35)}
#sig{position:absolute;left:80px;top:905px;width:1305px;display:flex;flex-wrap:wrap;gap:8px 12px}#sig span{font:500 26px/1.2 Fig;background:#EEF3FB;border-radius:10px;padding:6px 14px;border-left:6px solid #2060AF}#sig b{font-weight:800}
#cards.z .c{display:none}#cards.z .c.on{display:block;font-size:52px;line-height:80px;padding:22px 44px;margin-top:10px}#cards.z .c.on::before{top:44px}
mark{background:#FFF08A;color:#0B1530;padding:0 2px;border-radius:5px}
"""
SIGLE={'USA':'Stati Uniti d\'America','URSS':'Unione delle Repubbliche Socialiste Sovietiche','ONU':'Organizzazione delle Nazioni Unite','FMI':'Fondo Monetario Internazionale','NATO':'Organizzazione del Trattato dell\'Atlantico del Nord','CECA':'Comunità Europea del Carbone e dell\'Acciaio','CEE':'Comunità Economica Europea','RFT':'Repubblica Federale Tedesca','RDT':'Repubblica Democratica Tedesca','Euratom':'Comunità Europea dell\'Energia Atomica','Cominform':'Ufficio d\'informazione dei partiti comunisti'}
LOGO=open('/tmp/w/logo.svg').read()
def e(s):return html.escape(s)
def page(kick,title,pars,win,attiva,clau,pag,keys,cam=True,nome_band=True,zoom=0):
    """pars: testi; win: indici delle card in questa finestra; attiva: indice card attiva (o None); clau: indice clausola evidenziata"""
    nl=1 if len(title)<44 else 2
    top=188+nl*65+20
    cards=''
    for i in win:
        lead,cl=clausole(pars[i]);on=(i==attiva)
        body=''
        for j,c in enumerate(cl):
            body+=(f'<mark>{e(c)}</mark>' if on and j==clau else e(c))+' '
        cards+=f'<div class="c{" on" if on else ""}">'+(f'<b>{e(lead)}:</b> ' if lead else '')+body.strip()+'</div>'
    sig=[]
    if attiva is not None:
        for k,v in SIGLE.items():
            if re.search(r'\b'+k+r'\b',pars[attiva]):sig.append((k,v))
    sg=''.join(f'<span><b>{e(k)}</b> = {e(v)}</span>' for k,v in sig)
    kws=''.join(f'<div class="k">{e(k)}</div>' for k in keys[:5])
    return f"""<!doctype html><html><head><meta charset=utf-8><style>{CSS}</style></head><body>
<img id=logo src="file:///tmp/w/logo.svg"><div id=hl></div><div id=kick>{e(kick)}</div><div id=tit>{e(title)}</div>
<div id=bar style="top:{top-6}px"></div>
<div id=cards{" class=z" if zoom else ""} style="top:{top+30}px">{cards}</div>
{'<div id=sig>'+sg+'</div>' if sig else ''}
{'<div id=cam></div><div id=band><b>Giorgio Mazzotti</b><i>PROF. DI STORIA</i></div>' if cam else ''}
{'<div id=kw><h4>PAROLE CHIAVE</h4>'+kws+'</div>' if keys else ''}
<div id=fl></div><div id=foot>STORIA V</div><div id=pag>Pagina {pag}</div></body></html>"""
