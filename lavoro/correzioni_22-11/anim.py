# -*- coding: utf-8 -*-
# Schede animate con voce: approfondimenti, ripasso (schema), glossario, Di cosa parliamo, spiegoni, compiti.
import sys, os, re, json, subprocess
sys.path.insert(0,'/home/work/build')
from lib import *
import av
fr=av.fr
VOXOLD='/home/work/voci/scambio/storia-V-lez17/vox'
VOXNEW='/home/work/build/vox_new'      # voci Kore nuove ricevute dalla master (controllate)
VOXPROV='/home/work/build/vox_prov'    # voci provvisorie
def vpath(n):
    for d in (VOXNEW,VOXOLD,VOXPROV):
        if os.path.exists(f'{d}/{n}.wav'):return f'{d}/{n}.wav'
    raise FileNotFoundError(n)
def vreal(n): return os.path.exists(f'{VOXNEW}/{n}.wav') or os.path.exists(f'{VOXOLD}/{n}.wav')
def vdur(n): return av.probe_dur(vpath(n))
def sents(t): return [x for x in re.split(r'(?<=[\.\!\?])\s+',t.strip()) if x]
DARKCSS="""
html,body{background:radial-gradient(900px 700px at 25% 30%,rgba(32,96,175,.5),transparent 70%),radial-gradient(800px 600px at 85% 85%,rgba(255,176,60,.18),transparent 70%),#0B1530}
.title{color:#fff}.kick,.foot{color:#7FB6F2}#logo{filter:brightness(0) invert(1);opacity:.9}
.card{background:rgba(255,255,255,.08);border-color:rgba(255,255,255,.2);color:#fff;box-shadow:none}.card b{color:#fff}
.card.dim{opacity:.6}.card.on{background:rgba(255,255,255,.16);border-color:#FFE600;box-shadow:0 0 0 6px #FFE600}
.card .dot{background:rgba(255,255,255,.35)}.card.on .dot{background:#FFE600;box-shadow:0 0 0 3px #fff}
.chip{background:#FFE600}
div[style*="bottom:68px"]{color:#FFB03C !important}
"""
LIT_CSS="""
.lc{position:absolute;display:flex;flex-direction:column;gap:20px}
.lc .card{position:relative;font:400 38px/1.5 Fig;padding:18px 30px 18px 66px}
.lc .card .dot{top:32px}
.chip{position:absolute;left:300px;top:30px;background:#FFE600;color:#0B1530;border-radius:30px;padding:6px 22px;font:800 24px FigX;letter-spacing:.12em}
"""
_TENS=[('cinquant',50),('sessant',60),('settant',70),('ottant',80),('novant',90),('quarant',40),('trent',30),('vent',20)]
_TEEN={'dieci':10,'undici':11,'dodici':12,'tredici':13,'quattordici':14,'quindici':15,'sedici':16,'diciassette':17,'diciotto':18,'diciannove':19}
_UN=[('quattro',4),('cinque',5),('sette',7),('otto',8),('nove',9),('due',2),('tre',3),('tré',3),('sei',6),('uno',1),('un',1)]
def _parse(r):
    if r in _TEEN: return 1900+_TEEN[r]
    if r=='': return 1900
    for k,v in _TENS:
        if r.startswith(k):
            q=r[len(k):];q=q[1:] if q[:1] in ('a','i') else q
            if q=='': return 1900+v
            for u,w in _UN:
                if q==u: return 1900+v+w
            return None
    for u,w in _UN:
        if r==u: return 1900+w
    return None
def _yr(m):
    rest=m.group(1).lower()
    for r in (rest[1:] if rest[:1]=='o' else None, rest):
        if r is None: continue
        v=_parse(r)
        if v: return str(v)
    return m.group(0)
def digits(t):
    t=re.sub(r'(?i)\bmillenovecent([a-zé]*)',_yr,t)
    for a,b in [('il nove novembre','il 9 novembre'),('otto anni','8 anni'),('due milioni','2 milioni')]: t=t.replace(a,b)
    return t
def est(t,w,fs=38): 
    cpl=int((w-100)/(fs*0.47));return max(1,-(-len(t)//cpl))*int(fs*1.5)+40
def win(texts,cur,w,avail,fs=38):
    K=len(texts);c=max(cur,0)
    for lo,hi in [(c-1,c+1),(c,c+2),(c-2,c),(c-1,c),(c,c+1),(c,c)]:
        lo=max(lo,0);hi=min(hi,K-1)
        idx=list(range(lo,hi+1))
        if c in idx and sum(est(texts[i],w,fs) for i in idx)+20*(len(idx)-1)<=avail: return idx
    return [c]
def lit_html(title,kicker,texts,cur,page,img=None,leads=None,chip=None,note=None,materia=MATERIA,fs=38,tfs=56,allv=False,dark=False):
    texts=[digits(x) for x in texts];title=digits(title)
    w=960 if img else 1290
    h=chrome(page,materia,kicker)
    if chip: h+=f"<div class=chip style='left:{300+len(kicker)*17}px'>{esc(chip)}</div>"
    h+=f"<div class=title style='font-size:{tfs}px'>{esc(title)}</div>"
    top=190 if tfs>=54 else 240
    idx=(list(range(len(texts))) if allv else win(texts,cur,w,1000-top-70,fs)) if texts else []
    h+=f"<div class='lc' style='left:80px;top:{top}px;width:{w}px'>"
    for i in idx:
        lead=(f"<b>{esc(leads[i])}</b> " if leads and leads[i] else "")
        h+=f"<div class='card {'on' if i==cur else 'dim'}' style='width:{w}px;font-size:{fs}px'><span class=dot></span>{lead}{esc(texts[i])}</div>"
    h+="</div>"
    if img: h+=f"<div style='position:absolute;left:1080px;top:200px;width:760px;height:780px;display:flex;align-items:center;justify-content:center'><img src='file://{img}' style='max-width:760px;max-height:780px;border-radius:14px;box-shadow:0 10px 28px rgba(80,90,110,.28)'></div>"
    if note is None: note=sigle_for(" ".join(texts[i] for i in idx))
    if note: h+=f"<div style='position:absolute;left:80px;right:80px;bottom:68px;font:600 30px/1.3 FigS;color:#2060AF'>{esc(note)}</div>"
    return shell(h,LIT_CSS+(DARKCSS if dark else ''))
def sigle_for(t):
    f=[f"{k} = {v}" for k,v in SIGLE.items() if re.search(r'\b'+k+r'\b',t)]
    return ' · '.join(f)
def times_from_voice(texts,vname,lead=0.5,tail=1.2):
    """tempi d'inizio di ogni riga, proporzionali ai caratteri; durata totale"""
    d=vdur(vname);tot=sum(len(t) for t in texts);t=lead;out=[]
    for x in texts: out.append(t);t+=d*len(x)/tot
    return out,lead+d+tail
def lit_piece(name,P,html_fn,texts,vname,out,lead=0.5,tail=1.2,starts=None):
    """html_fn(cur) -> html; stato 0 = riga 0 (prima riga accesa alla partenza della voce). Ritorna (frames, audio events)"""
    st,total=times_from_voice(texts,vname,lead,tail) if starts is None else starts
    N=fr(total);items=[];states=[];prev=0
    cuts=[fr(s-0.15) for s in st[1:]]+[N]
    first=fr(max(st[0]-0.1,0.2))
    # stato iniziale: nessuna riga accesa (cur=-1) fino alla prima frase
    items.append((f'{name}_s',html_fn(-1)));states.append((f'/home/work/build/lit/{name}_s.png',first))
    for i in range(len(texts)):
        items.append((f'{name}_{i}',html_fn(i)))
        end=cuts[i];states.append((f'/home/work/build/lit/{name}_{i}.png',end-sum(f for _,f in states)))
    render(items,'/home/work/build/lit')
    n=av.states_video(states,out);return n,[(lead,'wav',vname)],len(texts)
