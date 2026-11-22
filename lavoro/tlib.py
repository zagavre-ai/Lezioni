# Libreria grafica Telesio per Storia V lez10: genera HTML 1920x1080 (slide con riquadro prof, schede blu, mappe)
import html, json, os, subprocess
from PIL import ImageFont
F='/root/.fonts/'
LOGO='file:///home/user/Lezioni/kit/docenti/Telesio_logo_blu.svg'
MATERIA='STORIA'
NAVY='#0B1530'; BLU='#2060AF'; GIALLO='#FFE600'
BASE_CSS=f'''
@font-face{{font-family:Fig;font-weight:400;src:url(file://{F}Figtree-Regular.ttf)}}
@font-face{{font-family:Fig;font-weight:500;src:url(file://{F}Figtree-Medium.ttf)}}
@font-face{{font-family:Fig;font-weight:600;src:url(file://{F}Figtree-SemiBold.ttf)}}
@font-face{{font-family:Fig;font-weight:700;src:url(file://{F}Figtree-Bold.ttf)}}
@font-face{{font-family:Fig;font-weight:800;src:url(file://{F}Figtree-ExtraBold.ttf)}}
@font-face{{font-family:Bri;font-weight:800;src:url(file://{F}BricolageGrotesque-ExtraBold.ttf)}}
*{{box-sizing:border-box}}
html,body{{margin:0;width:1920px;height:1080px;background:#fff;overflow:hidden;font-family:Fig;color:{NAVY}}}
.logo{{position:absolute;left:80px;top:48px;height:58px}}
.hl{{position:absolute;left:80px;right:80px;top:124px;height:1px;background:#E2E8F0}}
.fl{{position:absolute;left:80px;right:80px;top:981px;height:1px;background:#E2E8F0}}
.ft{{position:absolute;left:80px;top:998px;font:700 22px Fig;letter-spacing:.14em;color:{BLU}}}
.pg{{position:absolute;right:80px;top:998px;font:700 22px Fig;letter-spacing:.14em;color:{BLU}}}
.lab{{position:absolute;left:80px;top:146px;font:700 24px Fig;letter-spacing:.14em;color:{BLU};text-transform:uppercase}}
.tit{{position:absolute;left:80px;top:184px;width:1300px;font:800 60px/1.08 Bri;color:{BLU}}}
.card{{position:absolute;left:80px;width:1305px;background:#fff;border:2px solid #E2E8F0;border-radius:22px;padding:14px 34px 14px 58px;
  font:500 40px/1.5 Fig;color:{NAVY};box-shadow:0 12px 30px rgba(71,85,105,.16);opacity:.5}}
.card b{{font-weight:800}}
.card.on{{opacity:1;border:6px solid {GIALLO};padding:11px 31px 11px 55px;box-shadow:0 14px 34px rgba(71,85,105,.28)}}
.card.on::before{{content:"";position:absolute;left:20px;top:34px;width:20px;height:20px;border-radius:50%;background:{GIALLO};box-shadow:0 0 0 3px #fff,0 0 0 5px {NAVY}}}
.cam{{position:absolute;left:1428px;top:148px;width:412px;height:309px;border-radius:14px;background:#EEF2F7;box-shadow:0 14px 34px rgba(71,85,105,.40)}}
.nome{{position:absolute;left:1428px;top:476px;width:412px;height:98px;background:{GIALLO};transform:rotate(-1.4deg);padding:14px 24px;
  box-shadow:0 10px 24px rgba(71,85,105,.30);border-radius:4px}}
.nome .n{{font:800 30px/1.15 Bri;color:{NAVY}}} .nome .m{{font:700 20px/1.3 Fig;letter-spacing:.06em;color:{NAVY};margin-top:2px}}
.kw{{position:absolute;left:1428px;top:606px;width:412px}}
.kw h4{{margin:0 0 12px;font:700 20px Fig;letter-spacing:.16em;color:{BLU}}}
.kw div{{font:600 26px/1.2 Fig;color:{NAVY};background:#F1F5FB;border-left:6px solid {BLU};border-radius:8px;padding:6px 14px;margin-bottom:8px}}
'''
def esc(s): return html.escape(s,quote=False)
_fm={}
def _font(w,sz):
    k=(w,sz)
    if k not in _fm:_fm[k]=ImageFont.truetype(F+w,sz)
    return _fm[k]
def nlines(testo,width=1305-92,size=40,bold_lead=None):
    """righe stimate di una card (Figtree Medium 40px)"""
    f=_font('Figtree-Medium.ttf',size);fb=_font('Figtree-ExtraBold.ttf',size)
    righe=1;x=0
    for i,w in enumerate(testo.split(' ')):
        wd=f.getlength(w+' ')
        if bold_lead and i<len(bold_lead.split(' ')): wd=fb.getlength(w+' ')
        if x+wd>width and x>0: righe+=1;x=wd
        else:x+=wd
    return righe
def card_h(c): return nlines(c['testo'],bold_lead=c.get('lead'))*60+28+4
import re
def chunks(c):
    """frasi/segmenti della card dopo il titoletto (per le evidenze)"""
    t=c['testo'];l=c.get('lead') or '';r=t[len(l):] if t.startswith(l) else t
    parts=re.split(r'(?<=[,;:.])\s+',r.strip());parts=[p for p in parts if p]
    # unisci pezzi troppo corti (<18 caratteri) al successivo
    out=[]
    for p in parts:
        if out and len(out[-1])<22: out[-1]+=' '+p
        else: out.append(p)
    if len(out)>1 and len(out[-1])<22: out[-2]+=' '+out.pop()
    return out
def card_inner(c,ev=None):
    l=c.get('lead') or '';t=c['testo']
    if l and t.startswith(l):
        head='<b>'+esc(l)+'</b>';rest=t[len(l):].strip()
    else: head='';rest=t
    if ev is None or not rest: return head+(' ' if head and rest and rest[0] not in ',;.' else '')+esc(rest)
    ch=chunks(c);out=[]
    for i,p in enumerate(ch): out.append(f'<mark>{esc(p)}</mark>' if i==ev else esc(p))
    return head+(' ' if ch and ch[0][0] not in ',;.' else '')+' '.join(out)
def head(label,title,pagina,materia=MATERIA):
    return f'''<img class="logo" src="{LOGO}"><div class="hl"></div><div class="lab">{esc(label)}</div><div class="tit">{esc(title)}</div>
<div class="fl"></div><div class="ft">{esc(materia)}</div><div class="pg">Pagina {pagina}</div>'''
def prof_col(kw=None, cam=True, nome='Giorgio Mazzotti', mat='PROF. DI STORIA'):
    h=''
    if cam: h+='<div class="cam"></div>'+f'<div class="nome"><div class="n">{nome}</div><div class="m">{mat}</div></div>'
    if kw: h+='<div class="kw"><h4>PAROLE CHIAVE</h4>'+''.join(f'<div>{esc(k)}</div>' for k in kw[:5])+'</div>'
    return h
def page(body,extra_css=''):
    return f'<!doctype html><html><head><meta charset="utf-8"><style>{BASE_CSS}{extra_css}</style></head><body>{body}</body></html>'
def title_lines(title,size=60,width=1300):
    f=_font('BricolageGrotesque-ExtraBold.ttf',size);n=1;x=0
    for w in title.split(' '):
        wd=f.getlength(w+' ')
        if x+wd>width and x>0:n+=1;x=wd
        else:x+=wd
    return n
def area(title):
    n=title_lines(title);top=290 if n==1 else 358
    return top,965-top
def finestra(cards,k,title,maxn=3):
    top,H=area(title);idx=[k];h=card_h(cards[k])
    while len(idx)<maxn:
        for cand in (max(idx)+1,min(idx)-1):
            if 0<=cand<len(cards) and cand not in idx and h+18+card_h(cards[cand])<=H:
                idx.append(cand);h+=18+card_h(cards[cand]);break
        else:break
    return sorted(idx)
def slide_cards(label,title,pagina,cards,cur,kw,cam=True,ev=None,**k):
    """cards: lista completa; cur: indice acceso. Mostra una finestra di al massimo 3 card che contiene la corrente."""
    top,H=area(title);idx=finestra(cards,cur,title) if cur is not None else finestra(cards,0,title)
    body=head(label,title,pagina);y=top
    for i in idx:
        c=cards[i];h=card_h(c)
        body+=f'<div class="card{" on" if i==cur else ""}" style="top:{y}px;min-height:{h}px">{card_inner(c,ev if i==cur else None)}</div>'
        y+=h+18
    body+=prof_col(kw,cam)
    return page(body),idx

def lista_argomenti(args,dim=False):
    """card con l'elenco degli argomenti (copertina / Di cosa parliamo)"""
    h=''
    for i,(n,t) in enumerate(args):
        h+=f'<div class="arg"><span>{n}</span>{esc(t)}</div>'
    return h
COVER_CSS='''
.arg{display:flex;align-items:center;gap:22px;font:600 38px/1.2 Fig;color:#0B1530;margin:0 0 18px}
.arg span{flex:none;width:56px;height:56px;border-radius:50%;background:#2060AF;color:#fff;font:800 30px/56px Bri;text-align:center}
.box{position:absolute;left:80px;width:1305px;background:#F7F9FC;border:2px solid #E2E8F0;border-radius:22px;padding:30px 40px;box-shadow:0 12px 30px rgba(71,85,105,.16)}
.box h5{margin:0 0 20px;font:700 22px Fig;letter-spacing:.16em;color:#2060AF}
.big{position:absolute;left:80px;top:230px;width:1300px;font:800 104px/1.04 Bri;color:#0B1530}
.und{position:absolute;left:80px;width:120px;height:8px;background:#2060AF;border-radius:4px}
'''
def copertina(titolo,args,cam,parte=None):
    n=len(args);y=470
    body=f'<img class="logo" src="{LOGO}"><div class="hl"></div><div class="lab">STORIA · VIDEOLEZIONE{(" · PARTE "+str(parte)) if parte else ""}</div>'
    body+=f'<div class="big">{esc(titolo)}</div><div class="und" style="top:436px"></div>'
    body+=f'<div class="box" style="top:470px"><h5>ARGOMENTI</h5>{lista_argomenti(args)}</div>'
    body+=f'<div class="fl"></div><div class="ft">STORIA</div><div class="pg">Pagina 1</div>'+prof_col(None,cam)
    return page(body,COVER_CSS)
def di_cosa_parliamo(args,pagina,cam=True):
    body=head('STORIA · VIDEOLEZIONE','Di cosa parliamo',pagina)
    body+=f'<div class="box" style="top:300px"><h5>ARGOMENTI</h5>{lista_argomenti(args)}</div>'+prof_col(None,cam)
    return page(body,COVER_CSS)
IMG_CSS='''
.im{position:absolute;left:80px;top:300px;width:1305px;height:640px;display:flex;align-items:center;justify-content:center;background:#fff;border-radius:22px;box-shadow:0 12px 30px rgba(71,85,105,.16);overflow:hidden}
.im img{max-width:100%;max-height:100%;object-fit:contain}
.dd{position:absolute;left:80px;top:945px;width:1305px;font:600 26px/1.25 Fig;color:#0B1530}
'''
def slide_img(label,title,pagina,img,did,kw,cam=True):
    body=head(label,title,pagina)+f'<div class="im" style="height:560px"><img src="file://{img}"></div><div class="dd" style="top:872px"><b style="color:#2060AF">{esc(title).upper()}</b> · {esc(did)}</div>'+prof_col(kw,cam)
    return page(body,IMG_CSS)
