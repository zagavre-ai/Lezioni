# Slide del prof con card a 40 px, finestra mobile (max 3 card), bordo giallo sulla frase in corso, colonna destra (riquadro 4:3 + fascia gialla + parole chiave)
import re,sys
sys.path.insert(0,'/home/claude/w19/lib')
from ui import *
SIGLE={'DC':'Democrazia Cristiana','PSI':'Partito Socialista Italiano','P2':'Propaganda Due'}
def spiega(t):
    # ogni sigla si rispiega ogni volta che compare (BES): «DC, cioè Democrazia Cristiana»
    t=re.sub(r'\(DC, PSI\)','(DC, cioè Democrazia Cristiana, e PSI, cioè Partito Socialista Italiano)',t)
    t=re.sub(r'Loggia P2','Loggia P2, cioè Propaganda Due',t)
    t=re.sub(r'(?<![\w])DC(?![\w,])','DC, cioè Democrazia Cristiana',t)
    return t
CAM=(1428,148,412,309)
def right_col(keys,name='Giorgio Mazzotti',mat='PROF. DI STORIA',cam=True):
    x,y,w,h=CAM
    if not cam:
        li=''.join(f'<div style="margin:0 0 10px;padding-left:34px;position:relative;font:600 29px/1.25 Figtree"><i style="position:absolute;left:6px;top:11px;width:13px;height:13px;border-radius:50%;background:#2060AF"></i>{k}</div>' for k in keys[:5])
        return (f'<div class=abs style="left:{x}px;top:{y}px;width:{w}px;"><div style="font:700 22px Figtree;letter-spacing:.16em;color:#2060AF;margin-bottom:12px">PAROLE CHIAVE</div>{li}</div>') if keys else ''
    s=(f'<div class=abs style="left:{x}px;top:{y}px;width:{w}px;height:{h}px;border-radius:14px;background:#E8EDF5;box-shadow:0 14px 34px rgba(60,72,100,.28)"></div>'
       f'<div class=abs style="left:{x}px;top:{y+h+10}px;width:{w+4}px;height:112px;background:#FFE600;transform:rotate(-1.4deg);box-shadow:0 10px 22px rgba(60,72,100,.25);">'
       f'<div class=abs style="left:22px;top:14px;font:800 38px Figtree;line-height:1.1">{name}</div><div class=abs style="left:22px;top:66px;font:800 23px Figtree;letter-spacing:.04em">{mat}</div></div>')
    if keys:
        li=''.join(f'<div style="margin:0 0 10px;padding-left:34px;position:relative;font:600 29px/1.25 Figtree"><i style="position:absolute;left:6px;top:11px;width:13px;height:13px;border-radius:50%;background:#2060AF"></i>{k}</div>' for k in keys[:5])
        s+=(f'<div class=abs style="left:{x}px;top:{y+h+150}px;width:{w}px;"><div style="font:700 22px Figtree;letter-spacing:.16em;color:#2060AF;margin-bottom:12px">PAROLE CHIAVE</div>{li}</div>')
    return s
def card_html(txt,state):
    # state: 'on' | 'off'
    if state=='on':
        st='border:6px solid #FFE600;background:#fff;box-shadow:0 10px 26px rgba(60,72,100,.20);'
        dot='<i style="position:absolute;left:-20px;top:-20px;width:34px;height:34px;border-radius:50%;background:#FFE600;border:5px solid #fff;box-shadow:0 2px 8px rgba(60,72,100,.3)"></i>'
        op=1
    elif state=='plain':
        st='border:6px solid #D5DCE8;background:#fff;box-shadow:0 6px 16px rgba(60,72,100,.12);';dot='';op=1
    else:
        st='border:6px solid #D5DCE8;background:#fff;box-shadow:0 6px 16px rgba(60,72,100,.10);';dot='';op=.5
    return f'<div class=card style="position:relative;box-sizing:border-box;width:1305px;padding:20px 28px;border-radius:20px;{st}opacity:{op};font:400 40px/1.5 Figtree;margin-bottom:18px">{dot}{txt}</div>'
def measure(b,paras):
    b.pg.set_content('<!doctype html><html><head><meta charset=utf-8><style>'+BASE+'</style></head><body>'+''.join(card_html(spiega(p),'off') for p in paras)+'</body></html>')
    b.pg.wait_for_timeout(100)
    return b.pg.evaluate("[...document.querySelectorAll('.card')].map(e=>e.getBoundingClientRect().height+18)")
def window(h,active,avail):
    """indici (max 3) che contengono la card attiva e stanno nello spazio; prima le precedenti, poi le seguenti"""
    win=[active];tot=h[active]
    for cand in (active-1,active+1,active-2,active+2):
        if len(win)>=3 or cand<0 or cand>=len(h) or cand in win: continue
        if tot+h[cand]<=avail: win.append(cand);tot+=h[cand]
    return sorted(win)
def slide_html(titolo,kicker,pagina,paras,active,win,keys,materia='STORIA V',cam=True):
    ncap=1 if len(titolo)<46 else 2
    top=198+ncap*70
    cards=''.join(card_html(spiega(paras[i]),'plain' if active<0 else ('on' if i==active else 'off')) for i in win)
    return (chrome(materia,pagina,kicker)+
        f'<div class=abs style="left:80px;top:190px;width:1305px;font:800 56px/1.15 \'Bricolage Grotesque\';color:#0B1530">{titolo}</div>'
        f'<div class=abs style="left:80px;top:{top-8}px;width:86px;height:8px;border-radius:4px;background:#2060AF"></div>'
        f'<div class=abs style="left:80px;top:{top+22}px">{cards}</div>'+right_col(keys,cam=cam))
def avail_for(titolo):
    ncap=1 if len(titolo)<46 else 2
    return 972-(198+ncap*70+22)
