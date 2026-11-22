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
.kw{{position:absolute;left:1428px;top:640px;width:412px}}
.kw h4{{margin:0 0 12px;font:700 20px Fig;letter-spacing:.16em;color:{BLU}}}
.kw div{{font:600 28px/1.25 Fig;color:{NAVY};background:#F1F5FB;border-left:6px solid {BLU};border-radius:8px;padding:8px 14px;margin-bottom:10px}}
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
def card_inner(c):
    t=esc(c['testo']);l=c.get('lead')
    if l and t.startswith(esc(l)): t='<b>'+esc(l)+'</b>'+t[len(esc(l)):]
    return t
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
            if 0<=cand<len(cards) and cand not in idx and h+22+card_h(cards[cand])<=H:
                idx.append(cand);h+=22+card_h(cards[cand]);break
        else:break
    return sorted(idx)
def slide_cards(label,title,pagina,cards,cur,kw,cam=True,**k):
    """cards: lista completa; cur: indice acceso. Mostra una finestra di al massimo 3 card che contiene la corrente."""
    top,H=area(title);idx=finestra(cards,cur,title) if cur is not None else finestra(cards,0,title)
    body=head(label,title,pagina);y=top
    for i in idx:
        c=cards[i];h=card_h(c)
        body+=f'<div class="card{" on" if i==cur else ""}" style="top:{y}px;min-height:{h}px">{card_inner(c)}</div>'
        y+=h+22
    body+=prof_col(kw,cam)
    return page(body),idx
