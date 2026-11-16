# Scene Telesio: ogni funzione restituisce HTML 1920x1080
from lib import *
def esc(x):return html.escape(x)
def page(kick,title,body,dark=False,foot=True):
    return doc(f'''{logo(dark)}
<div class="abs kick" style="left:56px;top:104px">{esc(kick)}</div>
<h1 class="abs" style="left:56px;top:150px;font-size:64px;width:1808px">{esc(title)}</h1>
{body}{'<div class="foot">STORIA · Prof. Giorgio Mazzotti</div>' if foot else ''}''','bg-d' if dark else 'bg-l')
# ---------- approfondimenti (AN) ----------
def an_html(spec,k,imgs):
    L=spec.get('layout','cards');it=spec['items'];n=len(it);body=''
    img=imgs.get(spec.get('img'))
    if L=='timeline':
        x0,x1=140,1780;y=560
        body+=f'<div class="abs" style="left:{x0}px;top:{y}px;width:{x1-x0}px;height:8px;background:var(--linea);border-radius:6px"></div>'
        for i,e in enumerate(it):
            if i>k:continue
            cx=x0+(x1-x0)*(i+.5)/n;cls='lit' if i==k else 'dim'
            w=min(420,(x1-x0)/n-30)
            body+=f'''<div class="abs" style="left:{cx-w/2}px;top:{y-170}px;width:{w}px;text-align:center;font-family:BG;font-weight:800;font-size:56px;color:var(--blu);line-height:1.05;{'opacity:.5' if i!=k else ''}">{esc(e['lab'])}</div>
<div class="abs" style="left:{cx-17}px;top:{y-13}px;width:34px;height:34px;border-radius:50%;background:{'var(--giallo)' if i==k else 'var(--blu)'};border:5px solid var(--blu)"></div>
<div class="abs card {cls}" style="left:{cx-w/2}px;top:{y+70}px;width:{w}px;text-align:center"><b style="font-family:BG;font-size:40px;color:var(--notte)">{esc(e['h'])}</b><div style="font-size:34px;margin-top:8px">{esc(e.get('s',''))}</div></div>'''
    else:
        if img:
            W=1100;cols=1;x0=56;gx=0
        else:
            W=1808;x0=56
            cols=2 if n==4 else n
        rows=math.ceil(n/cols);gap=16 if img else 28
        cw=(W-gap*(cols-1))/cols;top=270 if img else 300;H=(1000 if img else 960)-top
        ch=(H-gap*(rows-1))/rows
        if img:ch=min(ch,172)
        for i,e in enumerate(it):
            if i>k:continue
            r,c=divmod(i,cols);cls='lit' if i==k else 'dim'
            big=e.get('big')
            hs=f'<div style="font-family:BG;font-weight:800;font-size:{110 if big else (42 if img else 46)}px;line-height:1.05;color:var(--blu)">{esc(e["h"])}</div>'
            body+=f'<div class="abs card {cls}" style="left:{x0+c*(cw+gap)}px;top:{top+r*(ch+gap)}px;width:{cw}px;height:{ch}px;display:flex;flex-direction:column;justify-content:center">{hs}<div style="font-size:{40 if big else (32 if img else 36)}px;margin-top:6px">{esc(e.get("s",""))}</div></div>'
        if img:
            body+=f'<img class="abs" src="file://{img}" style="left:1230px;top:270px;width:634px;height:720px;object-fit:contain;border-radius:16px">'
    return page('Approfondimento · '+spec['kick'],spec['title'],body)
# ---------- ripasso / caption su scuro ----------
def wave(phase,n=44):
    h=[int(18+60*abs(math.sin((i*0.7)+phase*1.3))*abs(math.cos(i*0.23+phase*.4))) for i in range(n)]
    return '<div class="wave">'+''.join(f'<i style="height:{x}px"></i>' for x in h)+'</div>'
def ripasso_html(kind,sub,caption,phase):
    big={'R':'RIPASSO','RF':'RIPASSO','RS':'RIPASSO'}[kind]
    k={'R':"Ripasso dell'argomento",'RF':'Ripasso finale','RS':'Ripasso della prima parte'}[kind]
    return doc(f'''{logo(True)}
<div class="abs kick" style="left:150px;top:300px">{esc(k)}</div>
<h1 class="abs" style="left:150px;top:350px;font-size:150px">{big}</h1>
<div class="abs" style="left:150px;top:530px;font-family:BG;font-weight:800;font-size:56px;color:#5DA3F0;width:1500px">{esc(sub)}</div>
<div class="abs" style="left:150px;top:690px">{wave(phase)}</div>
<div class="cap">{esc(caption)}</div>''','bg-d')
def title_html(num,total,title,ex):
    return doc(f'''{logo(True)}
<div class="abs" style="left:1000px;top:60px;font-family:BG;font-weight:800;font-size:900px;line-height:1;color:transparent;-webkit-text-stroke:3px rgba(255,255,255,.12)">{num:02d}</div>
<div class="abs kick" style="left:150px;top:330px">Argomento {num:02d} / {total:02d}</div>
<h1 class="abs" style="left:150px;top:400px;font-size:112px;width:1450px">{esc(title)}</h1>
<div class="abs" style="left:150px;top:790px;width:180px;height:8px;background:var(--giallo);border-radius:6px"></div>
<div class="abs" style="left:150px;top:830px;font-size:36px;color:#C9D0DC;width:1400px">{esc(ex)}</div>
<div class="abs" style="left:150px;top:960px;display:flex;gap:14px">{''.join(f'<div style="width:92px;height:8px;border-radius:6px;background:{"var(--giallo)" if i<num else "rgba(255,255,255,.25)"}"></div>' for i in range(total))}</div>''','bg-d')
def pausa_html(kicker,big,sub,pill):
    return doc(f'''<div class="band" style="top:0"></div><div class="band" style="bottom:0"></div>
{logo(True).replace('top:34px','top:34px')}
<div class="abs" style="left:1300px;top:300px;font-family:BG;font-weight:800;font-size:680px;line-height:1;color:transparent;-webkit-text-stroke:3px rgba(255,255,255,.10)">?</div>
<div class="abs" style="left:1330px;top:420px;width:250px;height:250px;border-radius:50%;border:8px solid #4FC3E8;display:flex;align-items:center;justify-content:center;background:rgba(79,195,232,.12)"><div style="margin-left:18px;border-left:80px solid #4FC3E8;border-top:48px solid transparent;border-bottom:48px solid transparent"></div></div>
<div class="abs kick" style="left:150px;top:320px;color:#fff">{esc(kicker)}</div>
<h1 class="abs" style="left:150px;top:380px;font-size:140px">{esc(big)}</h1>
<div class="abs" style="left:150px;top:560px;font-family:BG;font-weight:800;font-size:54px;color:var(--giallo);width:1100px;line-height:1.1">{esc(sub)}</div>
{f'<div class="abs" style="left:150px;top:780px;padding:18px 36px;border-radius:14px;background:rgba(255,255,255,.1);border:2px solid rgba(255,255,255,.2);font-size:38px;font-weight:600">{esc(pill)}</div>' if pill else ''}''','bg-d').replace('.logo{position:absolute;left:56px;top:34px','.logo{position:absolute;left:56px;top:150px')
def intro_html(lez_title,parte,args,line='Benvenuta e benvenuto alla lezione di Storia.'):
    big=len(args)>4
    fs=32 if big else 36
    cards=''.join(f'<div style="display:flex;align-items:center;gap:18px;padding:10px 22px;border-radius:16px;background:rgba(255,255,255,.08);border:2px solid rgba(255,255,255,.18);font-size:{fs}px;font-weight:600;{"" if big else "margin-bottom:12px"}"><span style="background:var(--giallo);color:var(--notte);width:44px;height:44px;border-radius:50%;display:flex;align-items:center;justify-content:center;font-weight:700;font-size:30px;flex:none">{i+1}</span>{esc(a)}</div>' for i,a in enumerate(args))
    box=f'<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;width:1640px">{cards}</div>' if big else f'<div style="width:1200px">{cards}</div>'
    py=420 if parte else 400
    return doc(f'''{logo(True)}
<div class="abs kick" style="left:150px;top:190px">Storia · Quinto anno</div>
<h1 class="abs" style="left:150px;top:{215 if len(lez_title)<30 or not big else 235}px;font-size:{104 if len(lez_title)<30 else 72}px;width:1700px;white-space:nowrap">{esc(lez_title)}</h1>
{f'<div class="abs" style="left:150px;top:420px;font-family:BG;font-weight:800;font-size:52px;color:#5DA3F0">{esc(parte)}</div>' if parte else ''}
<div class="abs" style="left:150px;top:{500 if parte else 400}px"><div class="kick" style="margin-bottom:18px">{'In questa parte' if parte else 'In questa lezione'}</div>{box}</div>
<div class="cap" style="bottom:50px;padding:22px 44px;font-size:40px">{esc(line)}</div>''','bg-d')
def glossario_html(items,k):
    body=''
    n=len(items)
    for i,(t,d) in enumerate(items):
        if i>k:continue
        cls='lit' if i==k else 'dim'
        body+=f'<div class="abs card {cls}" style="left:56px;top:{290+i*(560//n+8)}px;width:1808px;height:{560//n-8}px;display:flex;align-items:center;gap:36px"><b style="font-family:BG;font-weight:800;font-size:46px;color:var(--blu);width:620px;flex:none">{esc(t)}</b><span style="font-size:38px">{esc(d)}</span></div>'
    return page('Parole chiave','Glossario',body)
# ---------- slide del docente ----------
def cam_col(kw,lit):
    k=''.join(f'<div style="padding:8px 14px;margin-bottom:8px;border-radius:10px;font-size:30px;line-height:1.15;font-weight:600;{"background:var(--giallo);color:var(--notte)" if i==lit else "color:#3B4560"}">{esc(w)}</div>' for i,w in enumerate(kw))
    return f'''<div class="abs" style="left:1486px;top:36px;width:402px;height:226px;border:4px solid var(--blu);border-radius:12px;background:#d9dde8"></div>
<div class="abs yl" style="left:1490px;top:262px;width:394px;padding:10px 16px;border-radius:0 0 10px 10px"><div style="font-weight:700;font-size:32px">Prof. Giorgio Mazzotti</div><div style="font-size:30px;letter-spacing:.02em;font-weight:600;white-space:nowrap">STORIA · QUINTO ANNO</div></div>
{('<div class="abs" style="left:1490px;top:380px;width:394px"><div class="kick" style="font-size:30px;border-bottom:3px solid var(--blu);padding-bottom:6px;margin-bottom:12px;letter-spacing:.14em">Parole chiave</div>'+k+'</div>') if kw else ''}'''
def slide_html(title,kick,cards,state):
    ci,si=state;tot=sum(len(l)+len(' '.join(s)) for l,s in cards)
    fs=34 if tot<700 else (32 if tot<850 else 30)
    body='<div class="abs" style="left:56px;top:262px;width:1384px;display:flex;flex-direction:column;gap:22px">'
    for i,(l,ss) in enumerate(cards):
        cls='card lit' if i==ci else ('card dim' if ci is not None else 'card')
        txt=''.join((f'<mark style="background:var(--giallo);padding:0 4px;border-radius:5px">{esc(x)}</mark> ' if (i==ci and j==si) else esc(x)+' ') for j,x in enumerate(ss))
        body+=f'<div class="{cls}" style="font-size:{fs}px;line-height:1.3"><b>{esc(l)}:</b> {txt}</div>'
    body+='</div>'
    return doc(f'''{logo(False)}
<div class="abs kick" style="left:56px;top:104px">{esc(kick)}</div>
<h1 class="abs" style="left:56px;top:140px;font-size:52px;width:1400px;line-height:1.05">{esc(title)}</h1>
{body}{cam_col([l for l,_ in cards],ci)}<div class="foot" style="width:1380px">STORIA · Prof. Giorgio Mazzotti</div>''','bg-l')
def intro_slide_html(lez,args):
    sm=len(args)>6
    items=''.join(f'<div style="display:flex;gap:20px;align-items:center;padding:{6 if sm else 14}px 26px;margin-bottom:{8 if sm else 14}px;border-radius:14px;background:#fff;border:2px solid var(--linea);font-size:{32 if sm else 38}px;font-weight:600"><span class="yl" style="width:{38 if sm else 46}px;height:{38 if sm else 46}px;border-radius:50%;display:flex;align-items:center;justify-content:center;font-weight:700;font-size:30px;flex:none">{i+1}</span>{esc(a)}</div>' for i,a in enumerate(args))
    return doc(f'''{logo(False)}
<div class="abs kick" style="left:56px;top:104px">Storia · Quinto anno</div>
<h1 class="abs" style="left:56px;top:140px;font-size:{64 if len(lez)<30 else 52}px;width:1400px;line-height:1.05">{esc(lez)}</h1>
<div class="abs" style="left:56px;top:{270 if not sm else 250}px;width:1380px"><div class="kick" style="margin-bottom:18px;font-size:30px">In questa lezione</div>{items}</div>
{cam_col([],None)}<div class="foot">STORIA · Prof. Giorgio Mazzotti</div>''','bg-l')
