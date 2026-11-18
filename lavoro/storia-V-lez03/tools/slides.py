# generatore slide bianche nel modello Spagnolo Lez.1 (1920x1080)
import os,json,base64,html
from playwright.sync_api import sync_playwright
Z='/tmp/w/tools'
LOGO=base64.b64encode(open('/home/user/Lezioni/kit/docenti/Telesio_logo_blu.svg','rb').read()).decode()
CSS="""
@font-face{font-family:'BG';font-weight:800;src:url('file://%(z)s/font/BricolageGrotesque-ExtraBold.ttf')}
@font-face{font-family:'FG';font-weight:500;src:url('file://%(z)s/font/Figtree-Medium.ttf')}
@font-face{font-family:'FG';font-weight:700;src:url('file://%(z)s/font/Figtree-Bold.ttf')}
@font-face{font-family:'FG';font-weight:800;src:url('file://%(z)s/font/Figtree-ExtraBold.ttf')}
*{box-sizing:border-box;margin:0;padding:0}
body{width:1920px;height:1080px;background:#fff;font-family:'FG';color:#0B1530;position:relative;overflow:hidden}
.abs{position:absolute}
#logo{position:absolute;left:80px;top:50px;height:56px}
.hl{position:absolute;left:80px;width:1760px;height:1px;background:#E3E6EE}
.kick{position:absolute;left:80px;font-weight:700;letter-spacing:.14em;font-size:26px;color:#2060AF;text-transform:uppercase;white-space:nowrap}
.ttl{position:absolute;left:80px;font-family:'BG';font-weight:800;color:#0B1530;line-height:1.05;letter-spacing:-.01em}
.bar{position:absolute;left:80px;width:85px;height:6px;background:#2060AF;border-radius:4px}
.foot{position:absolute;top:998px;font-weight:700;letter-spacing:.14em;font-size:21px;color:#2060AF;white-space:nowrap}
.card{position:absolute;left:80px;width:1305px;border:3px solid #E3E6EE;border-radius:20px;background:#fff;padding:10px 26px 10px 78px;font-size:28px;line-height:1.3;font-weight:500;box-shadow:0 6px 22px rgba(11,21,48,.05)}
.card.on{border-color:#FFE600;box-shadow:0 8px 26px rgba(255,200,0,.28);background:#FFFEF0}
.card b{font-weight:800;color:#0B1530}
.num{position:absolute;left:20px;top:50%;margin-top:-22px;width:44px;height:44px;border-radius:50%;background:#E3E6EE;color:#2060AF;font-weight:800;font-size:25px;display:flex;align-items:center;justify-content:center}
.card.on .num{background:#FFE600;color:#0B1530}
.shadow{position:absolute;left:1428px;top:146px;width:412px;height:309px;border-radius:18px;background:#fff;box-shadow:0 18px 44px rgba(11,21,48,.28)}
.band{position:absolute;left:1428px;top:474px;width:412px;height:98px;background:#FFE600;transform:rotate(-3deg);box-shadow:0 10px 26px rgba(11,21,48,.18);padding:14px 22px}
.band .n{font-family:'BG';font-weight:800;font-size:34px;line-height:1.1;color:#0B1530}
.band .r{font-weight:800;font-size:21px;letter-spacing:.05em;color:#0B1530;margin-top:6px;text-transform:uppercase}
.pk{position:absolute;left:1428px;top:640px;width:412px;border:3px solid #E3E6EE;border-radius:18px;padding:18px 22px 14px 22px;background:#F6F8FC}
.pk h4{font-size:22px;letter-spacing:.14em;color:#2060AF;font-weight:800;margin-bottom:10px}
.pk div{font-size:28px;font-weight:700;line-height:1.25;padding:6px 0 6px 18px;position:relative}
.pk div:before{content:'';position:absolute;left:0;top:19px;width:9px;height:9px;border-radius:50%;background:#2060AF}
.pill{position:absolute;left:80px;top:150px;font-weight:800;font-size:22px;letter-spacing:.16em;color:#2060AF;background:#EAF1FB;border-radius:30px;padding:8px 22px}
table.t{position:absolute;left:80px;width:1760px;border-collapse:separate;border-spacing:0;border:2px solid #E3E6EE;border-radius:20px;overflow:hidden;font-size:32px}
table.t th{background:#0B1530;color:#fff;text-align:left;padding:16px 26px;font-size:26px;letter-spacing:.12em;font-weight:800}
table.t td{padding:16px 26px;border-top:2px solid #EEF0F5;font-weight:500;line-height:1.28;vertical-align:middle}
table.t td:first-child{font-weight:800;color:#2060AF;width:520px}
table.t tr.on td{background:#FFF48A}
table.t tr.on td:first-child{color:#0B1530}
table.t tr.hid td{color:transparent}
""".replace("%(z)s",Z)
def esc(s): return html.escape(s,quote=False)
def head(kick,title,tsize=56,tt=186,ty=None,maxw=1290):
    if title: tsize=min(tsize,int(maxw/(0.5*len(title))))
    h=f'<img id=logo src="data:image/svg+xml;base64,{LOGO}"><div class=hl style="top:124px"></div>'
    if kick: h+=f'<div class=kick style="top:150px">{esc(kick)}</div>'
    if title: h+=f'<div class=ttl style="top:{tt}px;font-size:{tsize}px">{esc(title)}</div><div class=bar style="top:{tt+tsize*1.15+8:.0f}px"></div>'
    return h
def foot(mat,pg,prof=True):
    l=f'{mat.upper()} · Prof. Giorgio Mazzotti' if prof else mat.upper()
    h='<div class=hl style="top:981px"></div>'
    h+=f'<div class=foot style="left:80px">{esc(l.upper() if False else l)}</div>'
    if pg: h+=f'<div class=foot style="right:80px">Pagina {pg}</div>'
    return h
def prof_panel(keys,nome="Giorgio Mazzotti",ruolo="Prof. di Storia"):
    h='<div class=shadow></div>'
    h+=f'<div class=band><div class=n>{nome}</div><div class=r>{ruolo}</div></div>'
    if keys:
        h+='<div class=pk><h4>PAROLE CHIAVE</h4>'+''.join(f'<div>{esc(k)}</div>' for k in keys)+'</div>'
    return h
def cards_html(cards,on,top=292,bot=950,numbered=True):
    # altezza stimata per ogni card -> distribuiti
    n=len(cards);gap=12
    hs=[]
    for a,b in cards:
        L=len(a)+len(b)+2
        lines=1+(L-1)//88
        hs.append(10*2+lines*36.4+6)
    tot=sum(hs)+gap*(n-1);extra=max(0,(bot-top)-tot)
    pad=min(extra/(n*2),16)
    y=top;h=''
    for i,((a,b),hh) in enumerate(zip(cards,hs)):
        hh2=hh+2*pad
        cls='card on' if i==on else 'card'
        h+=f'<div class="{cls}" style="top:{y:.0f}px;min-height:{hh2:.0f}px;display:flex;align-items:center"><div class=num>{i+1}</div><div><b>{esc(a)}:</b> {esc(b)}</div></div>'
        y+=hh2+gap
    return h
def page(body): return f'<!doctype html><meta charset=utf-8><style>{CSS}</style><body>{body}</body>'
class R:
    def __enter__(self):
        self.p=sync_playwright().start()
        self.b=self.p.chromium.launch(executable_path='/opt/pw-browsers/chromium',args=['--allow-file-access-from-files','--no-sandbox'])
        self.pg=self.b.new_page(viewport={'width':1920,'height':1080},device_scale_factor=1.0)
        os.makedirs('/tmp/w/build/_h',exist_ok=True);return self
    def __exit__(self,*a): self.b.close();self.p.stop()
    def shot(self,body,out):
        f='/tmp/w/build/_h/p.html';open(f,'w').write(page(body))
        self.pg.goto('file://'+f);self.pg.evaluate("document.fonts.ready");self.pg.screenshot(path=out)

def cover(title,args,prof,pg=1,notice=False):
    h=head("STORIA V · VIDEOLEZIONE",None)
    h+=f'<div class=ttl style="top:222px;font-size:72px;text-transform:uppercase">{esc(title)}</div><div class=bar style="top:318px"></div>'
    half=(len(args)+1)//2
    def col(items,start): return ''.join(f'<div style="display:flex;gap:14px;padding:5px 0;font-size:28px;font-weight:600;line-height:1.25"><span style="color:#2060AF;font-weight:800">{start+i+1}.</span><span>{esc(t)}</span></div>' for i,t in enumerate(items))
    h+=f'<div class=abs style="left:80px;top:372px;width:1305px;background:#fff;border:2px solid #E3E6EE;border-radius:22px;box-shadow:0 10px 34px rgba(11,21,48,.08);padding:22px 30px 20px 30px"><div style="font-weight:800;letter-spacing:.16em;font-size:22px;color:#2060AF;margin-bottom:12px">ARGOMENTI</div><div style="display:block">{col(args,0)}</div></div>'
    if prof: h+=prof_panel(None)
    if notice: h+='<div class=abs style="left:160px;width:1600px;top:918px;text-align:center;font-size:24px;line-height:1.3;color:#6A7388">© Centro Studi Telesio. Tutti i contenuti riprodotti in questa videolezione (testi, grafiche, animazioni, voci e registrazioni) sono di proprietà del Centro Studi Telesio. È vietata la riproduzione, anche parziale, senza autorizzazione scritta.</div>'
    return h+foot("Storia V",pg,prof=True)
def schema(n_arg,nome,titolo,rows,k,pg,hi=True,label="PILLOLA DI STORIA",kicker=None):
    """k = quante righe visibili (0..N); hi = riga k-1 evidenziata"""
    h=head(kicker or f"{n_arg:02d} · {nome.upper()}",None)
    h+=f'<div class=pill>{label}</div>'
    h+=f'<div class=ttl style="top:206px;font-size:56px">{esc(titolo)}</div><div class=bar style="top:282px"></div>'
    r=''.join(f'<tr class="{("on" if (hi and i==k-1) else "")}{" hid" if i>=k else ""}"><td>{esc(a)}</td><td>{esc(b)}</td></tr>' for i,(a,b) in enumerate(rows))
    h+=f'<table class=t style="top:320px"><tr><th>COSA</th><th>CHE COSA SUCCEDE</th></tr>{r}</table>'
    return h+foot("Storia V",pg,prof=False)
def glossario(parte,items,k,pg,nome="GLOSSARIO · PAROLE CHIAVE"):
    h=head(nome,"Le parole chiave",tt=186)
    r=''.join(f'<tr class="{"on" if i==k else ""}"><td>{esc(a)}</td><td>{esc(b)}</td></tr>' for i,(a,b) in enumerate(items))
    h+=f'<table class=t style="top:290px;font-size:28px"><tr><th>PAROLA</th><th>DEFINIZIONE</th></tr>{r}</table>'
    return h+foot("Storia V",pg,prof=False)
def immagine(n_arg,nome,titolo,imgfile,pg,prof=True,keys=None):
    h=head(f"{n_arg:02d} · {nome.upper()}",titolo,tsize=52)
    h+=f'<img class=abs src="file://{imgfile}" style="left:80px;top:290px;width:1305px;height:660px;object-fit:contain;object-position:center">'
    if prof: h+=prof_panel(keys)
    return h+foot("Storia V",pg,prof)
def mappa(n_arg,imgfile,imgsize,zones,k,pg,nome):
    """zones: lista di rettangoli (x,y,w,h) in coordinate immagine, rivelati in ordine; k = quanti rivelati"""
    iw,ih=imgsize;W,Hh=1760,770;sc=min(W/iw,Hh/ih);w=iw*sc;hh=ih*sc;x0=80+(W-w)/2;y0=176+(Hh-hh)/2
    h=head(f"{n_arg:02d} · {nome.upper()} · MAPPA DEL PROFESSORE",None)
    h+=f'<img class=abs src="file://{imgfile}" style="left:{x0:.0f}px;top:{y0:.0f}px;width:{w:.0f}px;height:{hh:.0f}px">'
    for i,(x,y,ww,hh2) in enumerate(zones):
        if i>=k: h+=f'<div class=abs style="left:{x0+x*sc:.0f}px;top:{y0+y*sc:.0f}px;width:{ww*sc+1:.0f}px;height:{hh2*sc+1:.0f}px;background:#fff"></div>'
    return h+foot("Storia V",pg,prof=False)
def animaz(n_arg,nome,titolo,frasi,k,pg):
    """approfondimento: ultime 5 frasi come card; ultima evidenziata"""
    h=head(f"{n_arg:02d} · {nome.upper()}",titolo,tsize=52,maxw=1700)
    lo=max(0,k-5);out='<div class=abs style="left:80px;top:292px;width:1760px;display:flex;flex-direction:column;gap:14px">'
    for i in range(lo,k):
        cls='card on' if i==k-1 else 'card'
        out+=f'<div class="{cls}" style="position:relative;left:0;width:1760px;min-height:96px;display:flex;align-items:center"><div class=num>{i+1}</div><div>{esc(frasi[i])}</div></div>'
    out+='</div>'
    return h+out+foot("Storia V",pg,prof=False)
