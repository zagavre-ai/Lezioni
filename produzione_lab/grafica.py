# -*- coding: utf-8 -*-
# Schede grafiche Telesio 1920x1080 (HTML -> PNG con Chromium).
import html,os,sys
A='/home/user/work/assets/'
C=dict(notte='#0B1530',blu='#2060AF',giallo='#FFE600',grigio='#EEF0F4',linea='#C9D0DC')
CSS="""
@font-face{font-family:'Bricolage Grotesque';src:url('file://%(a)sBricolageGrotesque-ExtraBold.ttf');font-weight:800}
@font-face{font-family:'Figtree';src:url('file://%(a)sFigtree-Regular.ttf');font-weight:400}
@font-face{font-family:'Figtree';src:url('file://%(a)sFigtree-SemiBold.ttf');font-weight:600}
@font-face{font-family:'Figtree';src:url('file://%(a)sFigtree-Bold.ttf');font-weight:700}
*{box-sizing:border-box;margin:0;padding:0}
html,body{width:1920px;height:1080px;background:#0B1530;overflow:hidden;font-family:'Figtree',sans-serif;color:#fff}
.logo{position:absolute;left:70px;top:48px;height:54px}
.kick{position:absolute;left:70px;top:130px;font-weight:700;font-size:34px;letter-spacing:.14em;color:#FFE600;text-transform:uppercase}
h1{font-family:'Bricolage Grotesque';font-weight:800;font-size:76px;line-height:1.05;position:absolute;left:70px;top:185px;width:1360px}
.cards{position:absolute;left:70px;top:420px;width:1360px;display:flex;flex-direction:column;gap:26px}
.card{border-radius:26px;padding:30px 40px;font-weight:600;font-size:46px;line-height:1.2;background:#2060AF;color:#fff;border:6px solid #2060AF}
.card.on{background:#FFE600;color:#0B1530;border-color:#FFE600}
.card.off{visibility:hidden}
.foot{position:absolute;left:70px;bottom:36px;font-size:30px;color:#C9D0DC;font-weight:400}
.foot b{font-weight:700;color:#fff}
.mid{position:absolute;left:0;right:0;text-align:center}
"""%dict(a=A)
def E(s):return html.escape(s)
def base(body,extra=''):
    return '<!doctype html><html><head><meta charset="utf-8"><style>'+CSS+extra+'</style></head><body>'+body+'</body></html>'
def logo():return '<img class="logo" src="file://%sTelesio_logo_bianco.svg">'%A
def foot(mat,doc):return '<div class="foot"><b>Centro Studi Telesio</b> · %s · %s</div>'%(E(mat),E(doc))
def slide(mat,doc,kick,titolo,cards,attiva):
    """attiva: -1 = solo titolo; i = mostra le schede 0..i, la i evidenziata."""
    cs=''
    for i,c in enumerate(cards):
        cl='card'+(' off' if i>attiva else (' on' if i==attiva else ''))
        cs+='<div class="%s">%s</div>'%(cl,E(c))
    ring='<div style="position:absolute;left:1519px;top:284px;width:372px;height:372px;border:6px solid #FFE600;border-radius:50%%"></div>'
    return base(logo()+'<div class="kick">%s</div><h1>%s</h1><div class="cards">%s</div>%s%s'%(E(kick),E(titolo),cs,ring,foot(mat,doc)))
def titolo_arg(mat,doc,n,titolo):
    return base(logo()+'<div class="mid" style="top:330px"><div style="font-weight:700;font-size:44px;letter-spacing:.18em;color:#FFE600">ARGOMENTO %d</div>'
      '<div style="font-family:Bricolage Grotesque;font-weight:800;font-size:104px;line-height:1.05;margin:34px 160px 0">%s</div></div>%s'%(n,E(titolo),foot(mat,doc)))
def quiz(mat,doc,n,titolo,ncart=5):
    return base(logo()+'<div class="mid" style="top:250px"><div style="font-weight:700;font-size:44px;letter-spacing:.18em;color:#FFE600">QUIZ %d</div>'
      '<div style="font-family:Bricolage Grotesque;font-weight:800;font-size:92px;line-height:1.05;margin:30px 200px 0">%s</div>'
      '<div style="margin:60px auto 0;display:inline-block;background:#FFE600;color:#0B1530;border-radius:60px;padding:26px 70px;font-weight:700;font-size:50px">&#9654;&nbsp; 5 domande · per continuare almeno l\'80%%</div></div>%s'%(n,E(titolo),foot(mat,doc)))
def scheda_unica(mat,doc,kick,titolo,sotto=''):
    return base(logo()+'<div class="mid" style="top:320px"><div style="font-weight:700;font-size:44px;letter-spacing:.18em;color:#FFE600">%s</div>'
      '<div style="font-family:Bricolage Grotesque;font-weight:800;font-size:104px;line-height:1.05;margin:34px 160px 0">%s</div>'
      '<div style="margin:36px 200px 0;font-size:46px;color:#C9D0DC">%s</div></div>%s'%(E(kick),E(titolo),E(sotto),foot(mat,doc)))
def ripasso(mat,doc,kick,titolo,chips):
    ch=''.join('<div class="card" style="display:inline-block;margin:0 14px 24px 0;font-size:44px">%s</div>'%E(c) for c in chips)
    return base(logo()+'<div class="kick">%s</div><h1>%s</h1><div style="position:absolute;left:70px;top:440px;width:1700px">%s</div>%s'%(E(kick),E(titolo),ch,foot(mat,doc)))
def an(mat,doc,kick,titolo,items,attivi):
    """items=[(big,small)], attivi = quanti mostrare (l'ultimo evidenziato)."""
    cs=''
    for i,(b,s) in enumerate(items):
        on=(i==attivi-1);vis=i<attivi
        cs+=('<div style="width:520px;height:520px;border-radius:34px;padding:34px;background:%s;color:%s;visibility:%s;text-align:center;display:flex;flex-direction:column;justify-content:center">'
             '<div style="font-family:Bricolage Grotesque;font-weight:800;font-size:%dpx;line-height:1.05">%s</div>'
             '<div style="margin-top:26px;font-size:44px;font-weight:600">%s</div></div>')%(
             '#FFE600' if on else '#2060AF','#0B1530' if on else '#fff','visible' if vis else 'hidden',(120 if len(b)<=5 else 74),E(b),E(s))
    return base(logo()+'<div class="kick">%s</div><h1>%s</h1><div style="position:absolute;left:70px;top:400px;display:flex;gap:40px">%s</div>%s'%(E(kick),E(titolo),cs,foot(mat,doc)))
def glossario(mat,doc,termini,attivi):
    n=len(termini);fs=34 if n<=8 else 31;pad=14 if n<=8 else 8
    cs=''
    for i,(t,d) in enumerate(termini):
        cl='card'+(' off' if i>=attivi else (' on' if i==attivi-1 else ''))
        cs+='<div class="%s" style="padding:%dpx 30px;font-size:%dpx;border-radius:18px;border-width:4px"><b style="font-weight:700">%s</b> · %s</div>'%(cl,pad,fs,E(t),E(d))
    return base(logo()+'<div class="kick">GLOSSARIO</div><h1 style="font-size:64px">Le parole chiave</h1><div class="cards" style="top:290px;gap:8px;width:1780px">%s</div>%s'%(cs,foot(mat,doc)))
def riepilogo(mat,doc,args,attivi):
    n=len(args);fs=36 if n<=8 else 31;pad=12 if n<=8 else 6
    cs=''
    for i,t in enumerate(args):
        cl='card'+(' off' if i>=attivi else (' on' if i==attivi-1 else ''))
        cs+='<div class="%s" style="padding:%dpx 30px;font-size:%dpx;border-radius:18px;border-width:4px">%d · %s</div>'%(cl,pad,fs,i+1,E(t))
    return base(logo()+'<div class="kick">RIPASSO FINALE</div><h1 style="font-size:64px">Che cosa abbiamo visto</h1><div class="cards" style="top:290px;gap:8px;width:1500px">%s</div>%s'%(cs,foot(mat,doc)))
def render(pagine,uscite):
    from playwright.sync_api import sync_playwright
    with sync_playwright() as p:
        b=p.chromium.launch(executable_path='/opt/pw-browsers/chromium-1243/chrome-linux64/chrome',args=['--no-sandbox'])
        pg=b.new_page(viewport={'width':1920,'height':1080})
        for h,u in zip(pagine,uscite):
            if os.path.exists(u):continue
            open(u+'.html','w').write(h)
            pg.goto('file://'+u+'.html');pg.wait_for_timeout(60);pg.screenshot(path=u);os.remove(u+'.html')
        b.close()
