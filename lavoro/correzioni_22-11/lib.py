# -*- coding: utf-8 -*-
import os, base64, html, re, subprocess, json
CHROME='/opt/pw-browsers/chromium_headless_shell-1243/chrome-headless-shell-linux64/chrome-headless-shell'
LOGO=base64.b64encode(open('/home/user/Lezioni/kit/docenti/Telesio_logo_blu.svg','rb').read()).decode()
MATERIA="STORIA V"
esc=html.escape
CSS="""
@font-face{font-family:Fig;src:url(file:///root/.fonts/Figtree-Regular.ttf)}
@font-face{font-family:FigM;src:url(file:///root/.fonts/Figtree-Medium.ttf)}
@font-face{font-family:FigS;src:url(file:///root/.fonts/Figtree-SemiBold.ttf)}
@font-face{font-family:FigB;src:url(file:///root/.fonts/Figtree-Bold.ttf)}
@font-face{font-family:FigX;src:url(file:///root/.fonts/Figtree-ExtraBold.ttf)}
@font-face{font-family:Bri;src:url(file:///root/.fonts/BricolageGrotesque-ExtraBold.ttf)}
*{box-sizing:border-box}
html,body{margin:0;width:1920px;height:1080px;background:#fff;overflow:hidden;color:#0B1530;font-family:Fig}
#logo{position:absolute;left:70px;top:26px;height:46px}
.kick{position:absolute;left:300px;top:38px;font:700 24px FigB;letter-spacing:.14em;color:#2060AF}
.title{position:absolute;left:80px;top:84px;width:1290px;font:800 56px/1.08 Bri;color:#2060AF}
.bar{position:absolute;left:80px;width:90px;height:6px;background:#FFE600;border-radius:3px}
.foot{position:absolute;bottom:22px;font:700 22px FigB;color:#2060AF;letter-spacing:.08em}
.shadow{position:absolute;left:1428px;top:148px;width:412px;height:309px;border-radius:14px;box-shadow:0 12px 34px rgba(80,90,110,.35);background:#e8ecf2}
.fascia{position:absolute;left:1414px;top:440px;width:440px;height:104px;background:#FFE600;transform:rotate(-1.6deg);border-radius:6px;box-shadow:0 8px 20px rgba(80,90,110,.3);padding:30px 22px 0}
.fascia .n{font:800 36px/1.1 Bri;color:#0B1530}.fascia .r{font:700 20px FigB;letter-spacing:.08em;color:#0B1530;margin-top:4px}
.kw{position:absolute;left:1428px;top:580px;width:412px;padding:18px 22px;border-radius:14px;background:#F4F7FB;box-shadow:0 8px 22px rgba(80,90,110,.2)}
.kw h5{margin:0 0 10px;font:700 20px FigB;letter-spacing:.12em;color:#2060AF}
.kw div{font:600 30px/1.3 FigS;color:#0B1530;padding:3px 0}
.cards{position:absolute;left:80px;width:1290px;display:flex;flex-direction:column;gap:20px}.card{position:relative;width:1290px;border-radius:18px;padding:20px 34px 20px 70px;background:#fff;border:4px solid #E2E8F0;box-shadow:0 8px 22px rgba(80,90,110,.16);font:400 40px/1.5 Fig;color:#0B1530}
.card b{font-family:FigB;font-weight:700}
.card.dim{opacity:.55}
.card.on{border-color:#FFE600;box-shadow:0 0 0 6px #FFE600,0 10px 26px rgba(80,90,110,.25);opacity:1}
.card .dot{position:absolute;left:26px;top:36px;width:24px;height:24px;border-radius:50%;background:#CBD5E1}
.card.on .dot{background:#FFE600;box-shadow:0 0 0 3px #0B1530}
"""
def shell(body,extra=""):
    return f"<!doctype html><html><head><meta charset=utf-8><style>{CSS}{extra}</style></head><body>{body}</body></html>"
def chrome(page,materia=MATERIA,kick=""):
    return (f"<img id=logo src='data:image/svg+xml;base64,{LOGO}'>"+(f"<div class=kick>{esc(kick)}</div>" if kick else "")+
            f"<div class=foot style='left:80px'>{materia}</div><div class=foot style='right:80px'>Pagina {page}</div>")
def prof_side(kw=None,box=True):
    h=""
    if box: h+="<div class=shadow></div><div class=fascia><div class=n>Giorgio Mazzotti</div><div class=r>PROF. DI STORIA</div></div>"
    if kw: h+="<div class=kw><h5>PAROLE CHIAVE</h5>"+"".join(f"<div>{esc(k)}</div>" for k in kw[:5])+"</div>"
    return h
def card_html(c,y,on):
    lead=f"<b>{esc(c['lead'])}:</b> " if c['lead'] else ""
    return f"<div class='card {'on' if on else 'dim'}'><span class=dot></span>{lead}{esc(c['text'])}</div>"
def est_h(c):
    n=len(c['lead'])+len(c['text'])+(2 if c['lead'] else 0)
    lines=max(1,-(-n//52)); return lines*60+48
def windows(cards,cur,avail=740):
    """finestre candidate (al massimo 3 card intere, mai una sola se ce ne sono altre) che contengono la card corrente"""
    K=len(cards);c=max(cur,0);cand=[]
    for lo,hi in [(c-1,c+1),(c,c+2),(c-2,c),(c-1,c),(c,c+1),(c-2,c-1),(c-1,c+1),(c-3,c-1)]:
        if lo<0 or hi>=K: continue
        if lo>c or hi<c: continue
        idx=tuple(range(lo,hi+1))
        if len(idx)>3 or len(idx)<2: continue
        if sum(est_h(cards[k]) for k in idx)+20*(len(idx)-1)>avail: continue
        if idx not in cand: cand.append(idx)
    if not cand:
        for lo,hi in [(c,c+1),(c-1,c)]:
            if 0<=lo and hi<K and sum(est_h(cards[k]) for k in range(lo,hi+1))+20<=avail: cand.append(tuple(range(lo,hi+1)))
    if not cand: cand=[(c,)]
    return cand
def slide_text(n,title,cards,cur,variant,page,kw,kick,rows=None):
    """cur = card in corso (-1: nessuna, p.es. inizio); la prima card se cur<0"""
    two=len(title)>46
    top=250 if two else 190
    W_=windows(cards,cur,avail=1000-top-90);idx=W_[variant%len(W_)];cyc=variant//len(W_);fs={0:40,1:38,2:42}.get(cyc%3,40)
    if fs==42 and len(idx)>2: fs=36
    h=chrome(page,kick=kick)+f"<div class=title style='{'font-size:52px' if two else ''}'>{esc(title)}</div>"
    h+=f"<div class=cards style='top:{top}px'>"
    for i in idx: h+=card_html(cards[i],0,i==cur).replace("<div class='card",f"<div style='font-size:{fs}px' class='card",1)
    h+="</div>"
    h+=sigle_note(' '.join(cards[i]['lead']+' '+cards[i]['text'] for i in idx))
    h+=prof_side(kw)
    return shell(h)
SIGLE={'USA':"Stati Uniti d'America",'URSS':"Unione delle Repubbliche Socialiste Sovietiche",'OPEC':"Organizzazione dei paesi esportatori di petrolio",
 'OLP':"Organizzazione per la liberazione della Palestina",'CEE':"Comunità economica europea",'CSI':"Comunità degli Stati Indipendenti",'SALT':"trattati per limitare gli armamenti nucleari"}
def sigle_note(t):
    f=[f"{k} = {v}" for k,v in SIGLE.items() if re.search(r'\b'+k+r'\b',t)]
    if not f: return ""
    return "<div style='position:absolute;left:80px;right:80px;bottom:70px;font:600 30px/1.3 FigS;color:#2060AF'>"+esc(' · '.join(f))+"</div>"
def slide_img(title,img,page,kick,kw=None,w=1290,hmax=800):
    h=chrome(page,kick=kick)+f"<div class=title>{esc(title)}</div>"
    h+=f"<div style='position:absolute;left:80px;top:200px;width:{w}px;height:{hmax}px;display:flex;align-items:center;justify-content:center'><img src='file://{img}' style='max-width:{w}px;max-height:{hmax}px;border-radius:14px;box-shadow:0 10px 28px rgba(80,90,110,.28)'></div>"
    h+=prof_side(kw)
    return shell(h)
def render(items,outdir):
    from playwright.sync_api import sync_playwright
    os.makedirs(outdir,exist_ok=True)
    with sync_playwright() as p:
        b=p.chromium.launch(executable_path=CHROME,args=['--allow-file-access-from-files','--no-sandbox'])
        pg=b.new_page(viewport={'width':1920,'height':1080})
        for name,h in items:
            f=f'{outdir}/{name}.html';open(f,'w').write(h)
            pg.goto('file://'+f);pg.wait_for_timeout(120);pg.screenshot(path=f'{outdir}/{name}.png')
        b.close()
