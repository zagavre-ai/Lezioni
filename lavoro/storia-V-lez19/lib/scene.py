# Scene "blu scuro animato" (titolo, schema di ripasso, quiz, glossario, riepilogo, compiti) e approfondimenti. Tutte restituiscono (html, durata).
import re
LOGO_W='<div class=abs style="left:80px;top:48px;width:170px;filter:brightness(0) invert(1)">%s</div>'
def logo():
    from ui import LOGO
    return LOGO_W%LOGO
def T(t0,inner,style='',tag='div',t1=None,mode='reveal',extra=''):
    t1a=f' data-t1="{t1}"' if t1 is not None else ''
    return f'<{tag} data-t0="{t0}"{t1a} {extra} style="opacity:0;{style}">{inner}</{tag}>'
def titolo(n,tit,chips=None,dur=4.0):
    h='<div class="dk">'+logo()
    h+=T(0.2,f'ARGOMENTO {n}','position:absolute;left:140px;top:360px;font:800 34px Figtree;letter-spacing:.22em;color:#FFE600')
    fs=104 if len(tit)<28 else 84 if len(tit)<44 else 70
    h+=T(0.45,tit,f"position:absolute;left:140px;top:420px;width:1640px;font:800 {fs}px/1.08 'Bricolage Grotesque'")
    h+=T(0.9,'','position:absolute;left:140px;top:%dpx;width:140px;height:10px;border-radius:5px;background:#FFE600'%(420+int(fs*1.08)*(1+(len(tit)*fs*0.5>1640))+40))
    return h+'</div>',dur
def schema(tit,righe,voce_t,dur,kick='RIPASSO'):
    """righe: testi; voce_t: [(t_inizio,t_fine)] una per riga; la riga si accende col bordo giallo mentre la voce parla"""
    h='<div class="dk">'+logo()
    h+=T(0.2,kick,'position:absolute;left:140px;top:150px;font:800 30px Figtree;letter-spacing:.22em;color:#FFE600')
    h+=T(0.3,tit,"position:absolute;left:140px;top:200px;width:1640px;font:800 64px/1.1 'Bricolage Grotesque'")
    y=360;hh=min(112,int(560/len(righe))-14)
    for r,(a,b) in zip(righe,voce_t):
        h+=(f'<div data-t0="{a-0.1:.2f}" data-t1="{b+0.25:.2f}" data-lo="0.38" data-dy="0" style="opacity:.38;position:absolute;left:140px;top:{y}px;width:1640px;height:{hh}px;box-sizing:border-box;border-radius:18px;'
            f'background:rgba(255,255,255,.08);border:4px solid rgba(255,255,255,.18);display:flex;align-items:center;padding:0 34px;font:600 40px/1.25 Figtree">'
            f'<i class=pd style="width:22px;height:22px;border-radius:50%;background:#FFE600;margin-right:26px;flex:none"></i>{r}</div>')
        y+=hh+14
    return h+'</div>',dur
SCHEMA_CSS=".on{background:rgba(255,230,0,.16)!important;border-color:#FFE600!important;box-shadow:0 0 0 0 transparent}"
def quiz(tit,dur=5.0):
    h='<div class="dk">'+logo()
    h+=T(0.2,'QUIZ','position:absolute;left:0;right:0;top:330px;text-align:center;font:800 150px Figtree;letter-spacing:.14em;color:#FFE600')
    h+=T(0.6,tit,"position:absolute;left:200px;right:200px;top:560px;text-align:center;font:800 54px/1.15 'Bricolage Grotesque'")
    h+=T(1.0,'5 domande · per continuare serve almeno l’80%','position:absolute;left:0;right:0;top:760px;text-align:center;font:600 38px Figtree;color:#C9D6F5')
    return h+'</div>',dur
def elenco(kick,tit,voci,voce_t,dur,fs=40):
    """voci: lista di (grassetto,resto) o testo; si accendono con la voce"""
    return schema(tit,[ (f'<b>{a}</b>: {b}' if b else a) for a,b in voci],voce_t,dur,kick)
def testo_diviso(t,n=None):
    s=re.split(r'(?<=[.!?:])\s+',t.strip());return [x for x in s if x]
def approfondimento(tit,frasi,tempi,dur,img=None,kick='APPROFONDIMENTO'):
    """frasi compaiono a tempo con la voce; img = percorso foto ad alta risoluzione (a destra)"""
    h='<div class="dk">'+logo()
    h+=T(0.2,kick,'position:absolute;left:140px;top:150px;font:800 30px Figtree;letter-spacing:.22em;color:#FFE600')
    h+=T(0.3,tit,"position:absolute;left:140px;top:200px;width:1640px;font:800 62px/1.1 'Bricolage Grotesque'")
    w=1100 if img else 1640
    y=340
    n=len(frasi);hh=min(150,int(600/n)-14)
    for f,(a,b) in zip(frasi,tempi):
        h+=(f'<div data-t0="{a-0.1:.2f}" data-t1="{b+0.2:.2f}" style="opacity:0;position:absolute;left:140px;top:{y}px;width:{w}px;box-sizing:border-box;padding:12px 28px;border-radius:16px;background:rgba(255,255,255,.08);border-left:10px solid #FFE600;font:600 38px/1.3 Figtree">{f}</div>')
        y+=hh+14
    if img: h+=T(0.6,f'<img src="file://{img}" style="max-width:560px;max-height:620px;border-radius:14px;box-shadow:0 14px 34px rgba(0,0,0,.4)">','position:absolute;left:1280px;top:340px;width:520px')
    return h+'</div>',dur
