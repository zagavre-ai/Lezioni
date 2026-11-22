import sys,os,json,re,html as H
sys.path.insert(0,'/home/claude/w/b')
from anim import *
from data import *
import vox
ARGLIST=[ARG[i] for i in range(1,6)]
TITOLO='GLI STATI UNITI: DAL BOOM ECONOMICO AL NEW DEAL'
e=H.escape
# ---------- elementi comuni ----------
def chrome(label='',pg=None,cam=False,foot='STORIA'):
    s=f'<img class="logo" src="{LOGO}"><div class="hr"></div><div class="hr2"></div><div class="foot">{foot}</div>'
    if pg: s+=f'<div class="pg">Pagina {pg}</div>'
    if label: s+=f'<div class="lab">{e(label)}</div>'
    if cam: s+='<div class="cam"></div><div class="band"><b>Giorgio Mazzotti</b><i>PROF. DI STORIA</i></div>'
    return s
def glows():
    return '<div class="glow" style="left:-200px;top:-150px;width:700px;height:700px;background:#2060AF"></div><div class="glow" style="right:-150px;bottom:-200px;width:800px;height:800px;background:#E04F8B;opacity:.28"></div><div class="glow" style="left:900px;top:300px;width:500px;height:500px;background:#FFE600;opacity:.10"></div>'
# ---------- copertina ----------
def cover_html(cam=False,anim=True,hl=None):
    items=''.join(f'<li data-in="{1.6+0.4*i if anim else 0}" data-d="0.5">{e(a)}</li>' for i,a in enumerate(ARGLIST))
    css='''.ct{position:absolute;left:80px;top:230px;width:1300px;font-size:104px;color:#0B1530}
    .bar{position:absolute;left:80px;top:600px;width:170px;height:10px;background:#2060AF;border-radius:5px}
    .arg{position:absolute;left:80px;top:650px;width:1180px;background:#F5F8FC;border:2px solid #DCE4EF;border-radius:22px;box-shadow:0 12px 30px rgba(60,72,96,.14);padding:22px 36px 18px}
    .arg h4{font-weight:700;font-size:24px;letter-spacing:.16em;color:#2060AF;margin-bottom:8px}
    .arg ul{list-style:none;font-size:32px;font-weight:600;line-height:1.38}
    .arg li:before{content:'';display:inline-block;width:12px;height:12px;border-radius:50%;background:#2060AF;margin-right:16px;vertical-align:middle}'''
    LL=['GLI STATI UNITI:','DAL BOOM ECONOMICO','AL NEW DEAL']
    LL=[f'<span class="yl">{x}</span>' if hl==i else x for i,x in enumerate(LL)]
    L0,L1,L2=LL
    t=f'<div class="lab" style="top:146px">STORIA · VIDEOLEZIONE</div><div class="ct h1" data-in="0.2" data-d="0.7">{L0}<br>{L1}<br>{L2}</div><div class="bar" data-in="0.9" data-d="0.5"></div><div class="arg" data-in="1.2" data-d="0.5"><h4>ARGOMENTI</h4><ul>{items}</ul></div>'
    body=f'<img class="logo" src="{LOGO}"><div class="hr"></div><div class="hr2"></div><div class="foot">STORIA</div><div class="pg">Pagina 1</div>'+t
    if cam: body+='<div class="cam"></div><div class="band"><b>Giorgio Mazzotti</b><i>PROF. DI STORIA</i></div>'
    return scene(body,css)
# ---------- di cosa parliamo ----------
def dic_scene():
    v=vox.info('DIC1'); S=v['sent']
    rows=''
    for i,a in enumerate(ARGLIST):
        t0,t1,_=S[i+1] if i+1<len(S) else (v['dur']-1,v['dur'],'')
        rows+=f'<div class="row" data-in="{0.6+0.25*i}" data-d="0.5" data-lit="{t0:.2f},{t1:.2f}"><span class="n">{i+1}</span><span class="tt">{e(a)}</span></div>'
    css='''.rows{position:absolute;left:80px;top:300px;width:1500px;display:flex;flex-direction:column;gap:26px}
    .row{display:flex;align-items:center;gap:30px;background:#fff;border:2px solid #E3E8F0;border-radius:22px;padding:18px 34px;box-shadow:0 10px 26px rgba(60,72,96,.12);font-size:46px;font-weight:700}
    .row.on{border:5px solid #FFE600;padding:15px 31px}
    .row .n{width:72px;height:72px;border-radius:50%;background:#2060AF;color:#fff;font-family:'Bricolage Grotesque';font-weight:800;font-size:44px;display:flex;align-items:center;justify-content:center}
    .tt{color:#0B1530}
    h2{position:absolute;left:80px;top:170px;font-size:84px;color:#0B1530}'''
    body=chrome(pg=2)+f'<h2 class="h1" data-in="0.1">Di cosa parliamo</h2><div class="rows">{rows}</div>'
    dur=v['dur']+1.2
    return dict(html=scene(body,css),dur=dur,events=[(v['path'],0.3,'voce')],prov=v['prov'])
# ---------- titolo argomento ----------
def title_scene(a):
    css='''.tt{position:absolute;left:140px;top:380px;width:1640px;font-size:96px;color:#fff}
    .ch{position:absolute;left:140px;top:290px;background:#FFE600;color:#0B1530}
    .ul{position:absolute;left:140px;top:700px;height:12px;max-width:1640px;background:#FFE600;border-radius:6px}'''
    body=glows()+f'<div class="chip ch" data-in="0.15">Argomento {a}</div><div class="tt h1" data-in="0.3" data-d="0.7">{e(ARG[a])}</div><div style="position:absolute;left:140px;top:700px;width:900px"><div class="ul2" data-bar="0.8,1.8" style="height:12px;background:#FFE600;border-radius:6px;width:0"></div></div>'
    return dict(html=scene(body,css,True),dur=3.6,events=[(SU+'titolo.wav',0.1,'fx')])

# ---------- blocchi a finestra (max 3 card visibili) ----------
def pages(S,per=3,cls='c',w=1180,left=80,top=330,gap=24,fs=38):
    out=''
    for k in range(0,len(S),per):
        grp=S[k:k+per]; t_in=grp[0][0]; t_out=(S[k+per][0] if k+per<len(S) else None)
        cs=''
        for (a,b,s) in grp:
            cs+=f'<div class="{cls}" data-in="{a:.2f}" data-d="0.45" data-lit="{a:.2f},{b:.2f}">{s}</div>'
        oc=f' data-out="{t_out-0.0:.2f}"' if t_out is not None else ''
        out+=f'<div class="pgbox" data-in="{t_in-0.05:.2f}" data-d="0.01" data-dy="0"{oc} style="position:absolute;left:{left}px;top:{top}px;width:{w}px;display:flex;flex-direction:column;gap:{gap}px">{cs}</div>'
    return out
CARDCSS='''.c{background:#fff;border:2px solid #E3E8F0;border-radius:22px;padding:14px 32px;font-size:40px;line-height:1.45;box-shadow:0 10px 26px rgba(60,72,96,.12)}
.c.on{border:5px solid #FFE600;padding:11px 29px}
.c b{color:#2060AF;font-weight:800}'''
HERO={'AN1':('+50%','reddito nazionale in dieci anni'),'AN2':('Jazz','radio, cinema e grandi città'),'AN3':('1920','suffragio universale alle donne'),
'AN4':('Flappers','una nuova moda, nuovi comportamenti'),'AN5':('Harding e Coolidge','isolazionismo e liberismo'),'AN6':('1927','Sacco e Vanzetti condannati a morte'),'AN6_R2':('1927','Sacco e Vanzetti condannati a morte'),
'AN7':('Sovrapproduzione','l\'offerta supera la domanda'),'AN8':('Ottobre 1929','Giovedì e Martedì nero'),'AN9':('1932','Roosevelt e il New Deal'),'AN10':('1935','il Social Security Act')}
def appro_scene(name):
    v=vox.info(name); S=v['sent']; title=digits(S[0][2].rstrip('.:'))
    cards=[(a,b,H.escape(digits(s))) for a,b,s in S[1:]]
    hero,cap=HERO[name]
    hf=96 if len(hero)<9 else (64 if len(hero)<=13 else 50)
    css=CARDCSS+'''.hero{position:absolute;left:1330px;top:330px;width:510px;height:470px;background:#FFF3B0;border:4px solid #E3C340;border-radius:30px;box-shadow:0 14px 34px rgba(60,72,96,.18);display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center;padding:30px}
    .hero .hh{font-family:'Bricolage Grotesque';font-weight:800;color:#0B1530;line-height:1.05}
    .hero .cp{font-size:34px;font-weight:700;color:#0B1530;margin-top:18px}
    h2{position:absolute;left:80px;top:196px;width:1700px;font-size:76px;color:#0B1530}'''
    body=chrome(label='Approfondimento',pg=None)+f'<h2 class="h1" data-in="0.1">{e(title)}</h2>'
    body+=pages(cards,3,'c')
    cnt=''
    if re.match(r'^\+?\d+%?$',hero.replace('+','').replace('%','')) and hero.startswith('+'):
        cnt=f'data-count="0|50|0.6|1.4|%|+"'
    body+=f'<div class="hero" data-in="0.5" data-pop="1"><div class="hh" style="font-size:{hf*1.6 if len(hero)<6 else hf}px" {cnt}>{e(hero)}</div><div class="cp">{e(cap)}</div></div>'
    return dict(html=scene(body,css),dur=v['dur']+1.0,events=[(v['path'],0.3,'voce')],prov=v['prov'])

# ---------- mappe del prof (modello BES) ----------
COL={'root':('#FFD7C2','#F0834A'),'key':('#FFF2A8','#D9B92E'),'ex':('#CFEFDC','#3DAA72'),'cons':('#E4D9F6','#8A63C8'),'date':('#CFE5F7','#3F95D1')}
LEG=[('root','Concetto centrale'),('date','Date e sequenze'),('key','Parole chiave'),('ex','Esempi e opere'),('cons','Conseguenze')]
MAPS={
1:dict(title='Qual è la situazione economica e sociale degli Stati Uniti dopo la guerra?',vox=['M1_0','M1_1','M1_2','M1_3','M1_4','M1_5','M1_6'],
 boxes=[('r','I “RUGGENTI ANNI VENTI”','root',960,430,760,110,None,None),
  ('a','una crescita economica','key',330,640,540,130,'r','vedono'),('a2','l’aumento dei consumi','ex',330,880,540,150,'a','e'),
  ('b','cambiamenti nel costume','key',960,640,540,130,'r',None),('b2','la diffusione della musica jazz e del cinema di Hollywood','ex',960,880,540,210,'b','con'),
  ('c','fenomeni negativi','key',1590,640,540,130,'r',None),('c2','la diffidenza verso gli immigrati e la paura dei comunisti','ex',1590,880,540,210,'c','come')],
 order=['r','a','a2','b','b2','c','c2']),
2:dict(title='Quali sono le cause e gli effetti della Grande depressione?',vox=['M2_0','M2_1','M2_2','M2_3','M2_4','M2_5'],
 boxes=[('r','LA BORSA STATUNITENSE','root',960,400,780,100,None,None),('a','una bolla speculativa','key',960,590,640,100,'r','vede formarsi'),
  ('b','crollo del valore delle azioni','cons',960,770,760,100,'a','che porta al'),
  ('c1','l’impoverimento degli investitori','cons',330,960,540,130,'b','che provoca'),('c2','il fallimento delle banche','cons',960,960,540,130,'b',None),('c3','il fallimento delle aziende e la disoccupazione','cons',1590,960,540,130,'b',None)],
 order=['r','a','b','c1','c2','c3']),
3:dict(title='Che cosa prevede il New Deal?',vox=['M3_0_R2','M3_1','M3_2','M3_3','M3_4'],
 boxes=[('r','IL NEW DEAL','root',960,330,560,110,None,None),('a','l’intervento dello Stato nell’economia','key',960,570,820,130,'r','prevede'),
  ('c1','il sostegno dello Stato a consumatori e imprenditori','ex',330,860,540,210,'a','con'),('c2','la realizzazione di grandi opere che creano lavoro','ex',960,860,540,210,'a',None),('c3','provvedimenti sociali come le pensioni di anzianità','ex',1590,860,540,210,'a',None)],
 order=['r','a','c1','c2','c3'])}
def map_scene(n,hold=4.0):
    M=MAPS[n]; B_={b[0]:b for b in M['boxes']}
    css='''.bx{position:absolute;border:4px solid;border-radius:20px;display:flex;align-items:center;justify-content:center;text-align:center;font-size:38px;line-height:1.25;font-weight:600;color:#0B1530;padding:10px 18px}
    .bx.on{background:#FFE600!important;border-color:#0B1530!important}
    .bx.rt{font-weight:800;font-size:40px;letter-spacing:.06em}
    .lb{position:absolute;font-size:34px;font-weight:600;color:#0B1530;background:#fff;padding:2px 14px;transform:translate(-50%,-50%)}
    .leg{position:absolute;right:70px;top:140px;width:420px}
    .leg div{display:flex;align-items:center;gap:14px;font-size:34px;font-weight:600;margin-bottom:6px}.leg i{width:38px;height:28px;border-radius:7px;border:3px solid}
    .tt{position:absolute;left:80px;top:150px;width:1260px;font-size:54px;color:#2060AF}'''
    t=0.9; steps=[]
    for bid,vn in zip(M['order'],M['vox']):
        v=vox.info(vn); t0=t+0.7; steps.append((bid,vn,t0,t0+v['dur'],v)); t=t0+v['dur']+0.5
    total=t+hold
    svg='';boxes='';lbls=''
    for bid,vn,t0,t1,v in steps:
        _,txt,kind,cx,cy,w,h,par,lab=B_[bid]; fill,bd=COL[kind]
        boxes+=f'<div class="bx{" rt" if kind=="root" else ""}" data-in="{t0-0.35:.2f}" data-d="0.4" data-pop="1" data-lit="{t0:.2f},{t1:.2f}" style="left:{cx-w/2}px;top:{cy-h/2}px;width:{w}px;height:{h}px;background:{fill};border-color:{bd}">{e(txt)}</div>'
        if par:
            _,_,_,px,py,pw,ph,_,_=B_[par]; ys=py+ph/2; ye=cy-h/2; ym=(ys+ye)/2
            svg+=f'<path data-draw="{t0-0.7:.2f},0.5" d="M{px},{ys} V{ym} H{cx} V{ye-6}" fill="none" stroke="#0B1530" stroke-width="4" marker-end="url(#ah)"/>'
            if lab: lbls+=f'<div class="lb" data-in="{t0-0.6:.2f}" data-d="0.4" data-dy="0" style="left:{(px+cx)/2 if abs(px-cx)<5 else px}px;top:{ym}px">{e(lab)}</div>'
    leg=''.join(f'<div><i style="background:{COL[k][0]};border-color:{COL[k][1]}"></i>{e(l)}</div>' for k,l in LEG)
    tt=f'<div class="tt h1" data-in="0.1">{e(M["title"])}</div>' if M['title'] else ''
    body=f'<svg style="position:absolute;left:0;top:0" width="1920" height="1080"><defs><marker id="ah" markerUnits="userSpaceOnUse" markerWidth="30" markerHeight="30" refX="20" refY="15" orient="auto"><path d="M4,5 L20,15 L4,25" fill="none" stroke="#0B1530" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/></marker></defs>{svg}</svg>{tt}<div class="leg" data-in="0.2">{leg}</div>{boxes}{lbls}'
    ev=[(s[4]['path'],s[2],'voce') for s in steps]+[(SU+'repaso.wav',steps[-1][3]+0.6,'fx')]
    return dict(html=scene(body,css),dur=total,events=ev,prov=any(s[4]['prov'] for s in steps),steps=[(s[0],s[1],s[2],s[3]) for s in steps])

# ---------- numeri in cifre sullo schermo ----------
_U={'uno':1,'due':2,'tre':3,'quattro':4,'cinque':5,'sei':6,'sette':7,'otto':8,'nove':9,'dieci':10,'undici':11,'dodici':12,'tredici':13,'quattordici':14,'quindici':15,'sedici':16,'diciassette':17,'diciotto':18,'diciannove':19}
_T={'venti':20,'trenta':30,'quaranta':40,'cinquanta':50,'sessanta':60,'settanta':70,'ottanta':80,'novanta':90}
_NUM=dict(_U)
for tn,tv in _T.items():
    _NUM[tn]=tv
    base=tn[:-1]
    for un,uv in list(_U.items())[:9]:
        _NUM[(tn if un in('uno','otto') and False else base)+un]=tv+uv   # ventuno, ventotto, ventitre...
        _NUM[tn+un]=tv+uv
def digits(t):
    def anno(m):
        r=m.group(1).lower()
        if r in _NUM: return str(1900+_NUM[r])
        if r=='': return '1900'
        return m.group(0)
    t=re.sub(r'\b[Mm]illenovecento(\w*)',anno,t)
    t=re.sub(r'\b[Mm]illenovecento\b','1900',t)
    t=re.sub(r'\b(\w+) per cento',lambda m: (str(_NUM[m.group(1).lower()])+'%') if m.group(1).lower() in _NUM else m.group(0),t)
    t=re.sub(r'\b(quattordici|nove|cinquecentomila) milioni',lambda m:{'quattordici':'14','nove':'9'}.get(m.group(1),m.group(1))+' milioni',t)
    t=t.replace('mezzo milione','500.000')
    return t
# ---------- schede scure ----------
def dark_card(chip,big,sub='',hold=4.0,jingle=None,jt=0.1,voice=None):
    css='''.ch{position:absolute;left:140px;top:300px;background:#FFE600;color:#0B1530}
    .bg1{position:absolute;left:140px;top:400px;width:1640px;font-size:150px;color:#fff;line-height:1.05}
    .sb{position:absolute;left:140px;top:640px;width:1500px;font-size:56px;font-weight:600;color:#DCE6F7}'''
    body=glows()+f'<div class="chip ch" data-in="0.15">{e(chip)}</div><div class="bg1 h1" data-in="0.3" data-d="0.6">{e(big)}</div><div class="sb" data-in="0.9">{e(sub)}</div>'
    return css,body
def quiz_scene(a):
    css,body=dark_card('Ora tocca a te','Quiz',f'{ARG[a]} · 5 domande · almeno l’80% per continuare')
    body+='<div class="sb" data-in="1.4" style="top:760px;color:#FFE600">Rispondi · premi Controlla · poi Continua</div>'
    return dict(html=scene(body,css,True),dur=4.4,events=[(SU+'quiz.wav',0.5,'fx')])
def verifica_scene():
    css,body=dark_card('Verifica finale','Verifica di sbarramento','10 domande · per superarla serve almeno l’80%, cioè 8 risposte giuste')
    body+='<div class="sb" data-in="1.4" style="top:780px;color:#FFE600">Rispondi · premi Controlla · poi Continua</div>'
    return dict(html=scene(body,css,True),dur=4.4,events=[(SU+'quiz.wav',0.5,'fx')])
def compiti_intro():
    v=vox.info('COMPI')
    css,body=dark_card('Compiti','Compiti','')
    return dict(html=scene(body,css,True),dur=max(3.5,v['dur']+0.8),events=[(SU+'titolo.wav',0.1,'fx'),(v['path'],0.5,'voce')],prov=v['prov'])
def pillola_scene(a):
    v=vox.info(f'P{a}'); S=v['sent']
    css='''.ch{position:absolute;left:140px;top:300px;background:#FFE600;color:#0B1530}
    .bg1{position:absolute;left:140px;top:400px;width:1640px;font-size:110px;color:#fff;line-height:1.05}
    .sb{position:absolute;left:140px;top:700px;width:1500px;font-size:56px;font-weight:600;color:#DCE6F7}'''
    sub=S[1][2] if len(S)>1 else ''
    body=glows()+f'<div class="chip ch" data-in="0.15">Ripasso</div><div class="bg1 h1" data-in="0.3">{e(ARG[a])}</div><div class="sb" data-in="{S[1][0]+0.2 if len(S)>1 else 1:.2f}">{e(sub)}</div>'
    return dict(html=scene(body,css,True),dur=v['dur']+1.2,events=[(SU+'repaso.wav',0.1,'fx'),(v['path'],0.4,'voce')],prov=v['prov'])
def schema_scene(a):
    names=[]; k=1
    while f'SC{a}_{k}' in vox.T: names.append(f'SC{a}_{k}_R2' if f'SC{a}_{k}_R2' in vox.T else f'SC{a}_{k}'); k+=1
    css='''.ch{position:absolute;left:140px;top:150px;background:#FFE600;color:#0B1530}
    .hh{position:absolute;left:140px;top:230px;width:1640px;font-size:70px;color:#fff}
    .ln{background:rgba(255,255,255,.08);border:3px solid rgba(255,255,255,.28);border-radius:22px;padding:16px 34px;font-size:46px;font-weight:600;line-height:1.3;color:#fff}
    .ln.on{border:6px solid #FFE600;background:rgba(255,230,0,.14);padding:13px 31px}'''
    t=0.9; rows='';ev=[];prov=False
    n=len(names)
    for i,nm in enumerate(names):
        v=vox.info(nm); prov|=v['prov']; t0=t+0.2
        rows+=f'<div class="ln" data-in="{t0-0.2:.2f}" data-d="0.4" data-lit="{t0:.2f},{t0+v["dur"]:.2f}">{e(digits(v["text"]))}</div>'
        ev.append((v['path'],t0,'voce')); t=t0+v['dur']+0.35
    body=glows()+f'<div class="chip ch" data-in="0.1">Schema di ripasso</div><div class="hh h1" data-in="0.2">{e(ARG[a])}</div><div style="position:absolute;left:140px;top:360px;width:1640px;display:flex;flex-direction:column;gap:22px">{rows}</div>'
    return dict(html=scene(body,css,True),dur=t+1.2,events=ev,prov=prov)
DKCSS='''.c{background:rgba(255,255,255,.09);border:3px solid rgba(255,255,255,.3);border-radius:22px;padding:14px 32px;font-size:40px;line-height:1.45;color:#fff}
.c.on{border:6px solid #FFE600;background:rgba(255,230,0,.14);padding:11px 29px}
.c b{color:#FFE600}'''
def ripasso_scene(a):
    v=vox.info(f'R{a}'); S=[(x,y,e(digits(s))) for x,y,s in v['sent']]
    S=S[1:] if S[0][2].lower().startswith('ripassiamo') else S
    css=DKCSS+'''.ch{position:absolute;left:140px;top:150px;background:#FFE600;color:#0B1530}.hh{position:absolute;left:140px;top:230px;width:1640px;font-size:70px;color:#fff}'''
    body=glows()+f'<div class="chip ch" data-in="0.1">Ripasso finale</div><div class="hh h1" data-in="0.2">{e(ARG[a])}</div>'+pages(S,3,'c',w=1640,left=140,top=380)
    return dict(html=scene(body,css,True),dur=v['dur']+1.2,events=[(v['path'],0.4,'voce')],prov=v['prov'])
def glossario_scene():
    v=vox.info('GL1'); S=v['sent']
    cards=[]
    for a,b,s in S[1:]:
        if ':' in s: t,d=s.split(':',1); cards.append((a,b,f'<b>{e(digits(t))}:</b> {e(digits(d.strip()))}'))
        else: cards.append((a,b,e(digits(s))))
    css=CARDCSS+'h2{position:absolute;left:80px;top:196px;font-size:76px;color:#0B1530}'
    body=chrome(label='Glossario')+'<h2 class="h1" data-in="0.1">Le parole chiave della lezione</h2>'+pages(cards,3,'c',w=1700,top=330)
    return dict(html=scene(body,css),dur=v['dur']+1.2,events=[(v['path'],0.4,'voce')],prov=v['prov'])
def mappa_finale_scene(hold=4.0):
    vs=[vox.info(f'MF_{i}') for i in range(3)]
    cols=[('I “RUGGENTI ANNI VENTI”',[('una crescita economica','key'),('cambiamenti nel costume','key'),('fenomeni negativi','key')]),
          ('LA BORSA STATUNITENSE',[('una bolla speculativa','key'),('crollo del valore delle azioni','cons')]),
          ('IL NEW DEAL',[('l’intervento dello Stato nell’economia','key')])]
    css='''.pn{position:absolute;top:330px;width:540px;display:flex;flex-direction:column;gap:22px;align-items:stretch}
    .bx{border:4px solid;border-radius:20px;display:flex;align-items:center;justify-content:center;text-align:center;font-size:38px;line-height:1.25;font-weight:600;color:#0B1530;padding:14px 18px;min-height:110px}
    .bx.on{background:#FFE600!important;border-color:#0B1530!important}
    .ar{align-self:center;font-size:44px;color:#0B1530;line-height:1}
    .leg{position:absolute;right:70px;top:140px;width:420px}.leg div{display:flex;align-items:center;gap:14px;font-size:34px;font-weight:600;margin-bottom:6px}.leg i{width:38px;height:28px;border-radius:7px;border:3px solid}
    h2{position:absolute;left:80px;top:170px;font-size:70px;color:#2060AF}'''
    t=0.9;pn='';ev=[];prov=False
    for i,(root,kids) in enumerate(cols):
        v=vs[i]; prov|=v['prov']; t0=t+0.6
        inner=f'<div class="bx" data-lit="{t0:.2f},{t0+v["dur"]:.2f}" style="background:{COL["root"][0]};border-color:{COL["root"][1]};font-weight:800;letter-spacing:.05em">{e(root)}</div>'
        for k,kind in kids: inner+=f'<div class="ar">↓</div><div class="bx" style="background:{COL[kind][0]};border-color:{COL[kind][1]}">{e(k)}</div>'
        pn+=f'<div class="pn" data-in="{t0-0.3:.2f}" data-d="0.5" style="left:{80+i*610}px">{inner}</div>'
        ev.append((v['path'],t0,'voce')); t=t0+v['dur']+0.5
    leg=''.join(f'<div><i style="background:{COL[k][0]};border-color:{COL[k][1]}"></i>{e(l)}</div>' for k,l in LEG)
    body=f'<h2 class="h1" data-in="0.1">Mappa di tutta la lezione</h2><div class="leg" data-in="0.2">{leg}</div>{pn}'
    return dict(html=scene(body,css),dur=t+hold,events=ev,prov=prov)
def compiti_scene(k,items):
    v=vox.info(f'CP{k}'); S=v['sent']
    css=CARDCSS+'h2{position:absolute;left:80px;top:170px;font-size:76px;color:#0B1530}.c{font-size:40px}'
    cs=''
    for i,(n,t) in enumerate(items):
        a=S[2*i][0]+0.3; b=S[2*i+1][1]+0.3
        cs+=f'<div class="c" data-in="{0.5+0.4*i}" data-d="0.5" data-lit="{a:.2f},{b:.2f}"><b>{n}.</b> {e(t)}</div>'
    body=chrome(label='Compiti')+'<h2 class="h1" data-in="0.1">Compiti</h2>'+f'<div style="position:absolute;left:80px;top:300px;width:1700px;display:flex;flex-direction:column;gap:30px">{cs}</div>'
    return dict(html=scene(body,css),dur=v['dur']+1.6,events=[(v['path'],0.3,'voce')],prov=v['prov'])
