from slides import *
from plan import *
from edl import *
import os
IMG='/home/claude/w/img'
def img_uri(k): return 'file://'+f'{IMG}/{k}.png'
def img_size(k):
    from PIL import Image
    return Image.open(f'{IMG}/{k}.png').size
SL='/home/claude/w/slides';os.makedirs(SL,exist_ok=True)
def windows(rend,a):
    """partizione delle card in finestre (max 3 card, altezza che entra)"""
    cards=[c for c,_ in a['cards']]
    rend.load(slide_html(f"Argomento {a['n']} · {a['tit']}",a['slide'],cards,None,a['kw']))
    m=rend.pg.evaluate('''()=>{var cs=[].slice.call(document.querySelectorAll(".card"));var t=document.getElementById("cards").offsetTop;
      return {top:t,h:cs.map(c=>c.offsetHeight+24)}}''')
    maxh=975-m['top']
    wins=[];cur=[];h=0
    for i,hh in enumerate(m['h']):
        if cur and (len(cur)>=3 or h+hh>maxh): wins.append(cur);cur=[];h=0
        cur.append(i);h+=hh
    if cur: wins.append(cur)
    # finestra con una sola card: aggiungo la precedente come contesto (attenuata)
    for k in range(1,len(wins)):
        if len(wins[k])==1 and len(wins[k-1])>=1:
            prev=wins[k-1][-1]
            if m['h'][prev]+m['h'][wins[k][0]]<=maxh: wins[k]=[prev]+wins[k]
    return wins,m
def lit_at(a,t):
    l=None
    for i,(c,s) in enumerate(a['cards']):
        if s is not None and s<=t: l=i
    return l
def events(a,B):
    """[(t0,t1,chiave)] in tempo originale; chiave=('win',wi,lit)|('photo',k)"""
    t0=B['iv'][0][0];t1=B['iv'][-1][1]
    pts={t0,t1}
    for c,s in a['cards']:
        if s is not None and t0<s<t1: pts.add(s)
    for k,x,y in a['photos']:
        for v in (x,y):
            if t0<v<t1: pts.add(v)
    pts=sorted(pts);ev=[]
    return pts
def key_at(a,wins,t):
    for k,x,y in a['photos']:
        if x<=t<y: return ('photo',k)
    l=lit_at(a,t)
    if l is None: return ('win',0,None)
    for wi,w in enumerate(wins):
        if l in w: return ('win',wi,l)
    return ('win',0,l)
def render_key(rend,a,wins,key,page,out,mod=None):
    cards=[c for c,_ in a['cards']]
    kick=f"Argomento {a['n']} · {a['tit']}"
    if key[0]=='win':
        w=wins[key[1]];on=None if key[2] is None else w.index(key[2])
        rend.load(slide_html(kick,a['slide'],[cards[i] for i in w],on,a['kw'],page))
    else:
        ks=key[1].split('+');ph=[(img_uri(k),)+img_size(k) for k in ks]
        cap=' '.join(CAP[k] for k in ks)
        cap=cap if len(ks)==1 else ' '.join(CAP[k] for k in ks)
        rend.load(slide_html(kick,a['slide'],None,None,a['kw'],page,photos=ph,cap=cap_short(ks),title_size=None))
    rend.shot(out)
def cap_short(ks):
    if '+'.join(ks) in CAP: return CAP['+'.join(ks)]
    if len(ks)==1: return '**'+CAP[ks[0]].split('. ',1)[0]+'.** '+(CAP[ks[0]].split('. ',1)[1] if '. ' in CAP[ks[0]] else '')
    return ' · '.join(CAP[k].split('.')[0] for k in ks)
