import json,re,sys,os
sys.path.insert(0,'/home/claude/w19/lib')
from anim import *
from scene import *
from testo import cifre
from core import VD
import viste
VX='/home/claude/w19/voxn/'
TV={x['nome']:x['testo'] for x in json.load(open('/home/claude/voci/scambio/storia-V-lez19/testi_voci.json'))}
O='/home/claude/w19/out/'
def vd(n): return VD[n]
def frasi(t): return [x for x in re.split(r'(?<=[.!?])\s+',t.strip()) if x]
def tempi_frasi(fr,t0,d):
    """tempi proporzionali ai caratteri dentro una voce che comincia a t0 e dura d"""
    tot=sum(len(x) for x in fr);t=t0;out=[]
    for x in fr:
        a=t;t+=d*len(x)/tot;out.append((round(a,2),round(t,2)))
    return out
def render_scene(pid,html,dur,css=''):
    f=O+pid+'.mp4'
    if not os.path.exists(f): render(html,dur,f,extra_css=css+SCHEMA_CSS)
    return f
def s_titolo(n):
    h,d=titolo(n,viste.ARGT[n]);f=render_scene(f't{n}',h,d)
    return f,[(KIT+'/suoni/titolo.wav',0.2,-4)]
KIT='/home/user/Lezioni/kit'
def s_schema(n):
    pill=f'P{n}';sc=sorted([k for k in VD if k.startswith(f'SC{n}_')],key=lambda x:int(x.split('_')[1]))
    righe=[cifre(TV[k]) for k in sc]
    t=1.6;ev=[(KIT+'/suoni/repaso.wav',0.1,-8),(VX+pill+'.wav',t,0)];t+=vd(pill)+0.5
    tv=[]
    for k in sc:
        ev.append((VX+k+'.wav',t,0));tv.append((t,t+vd(k)));t+=vd(k)+0.55
    dur=round(t+1.2,2)
    h,d=schema(viste.ARGT[n],righe,tv,dur);f=render_scene(f'sch{n}',h,dur)
    return f,ev
def s_quiz(n):
    h,d=quiz(viste.ARGT[n]);f=render_scene(f'q{n}',h,d)
    return f,[(KIT+'/suoni/quiz.wav',0.5,-2)]
def s_an(pid,parti):
    """parti = [(voce, foto|None, titolo)] voci in sequenza, ciascuna con le sue frasi; foto a destra"""
    ev=[];t=1.0;html='<div class="dk">'+logo()
    html+=T(0.2,'APPROFONDIMENTO','position:absolute;left:140px;top:150px;font:800 30px Figtree;letter-spacing:.22em;color:#FFE600')
    tmax=0
    for i,(v,foto,tit) in enumerate(parti):
        d=vd(v);fr=[cifre(x) for x in frasi(TV[v])]
        # il primo frammento (titolo) è la prima frase breve della voce: la usiamo come titolo
        tt=tit or frasi(TV[v])[0].rstrip('.')
        fr=fr[1:] if len(fr)>1 else fr
        tm=tempi_frasi(fr,t+ (d*len(frasi(TV[v])[0])/len(TV[v])),d-(d*len(frasi(TV[v])[0])/len(TV[v])))
        ev.append((VX+v+'.wav',t,0))
        t0=t;t1=t+d+0.6
        foto=None if foto=='none' else foto;w=1100 if foto else 1640
        html+=T(t0-0.1,tt,"position:absolute;left:140px;top:200px;width:1640px;font:800 62px/1.1 'Bricolage Grotesque'",extra=f'data-out="{t1-0.2:.2f}"')
        html+=f'<div style="position:absolute;left:140px;top:340px;width:{w}px;display:flex;flex-direction:column;gap:14px">'
        for f_,(a,b) in zip(fr,tm):
            html+=(f'<div data-t0="{a-0.1:.2f}" data-t1="{b+0.2:.2f}" data-out="{t1-0.2:.2f}" style="opacity:0;box-sizing:border-box;padding:12px 28px;border-radius:16px;background:rgba(255,255,255,.08);border-left:10px solid #FFE600;font:600 38px/1.3 Figtree">{f_}</div>')
        html+='</div>'
        if foto and foto!='none': html+=T(t0,f'<img src="file:///home/claude/w19/foto/{foto}.png" style="max-width:520px;max-height:620px;border-radius:14px;box-shadow:0 14px 34px rgba(0,0,0,.4)">','position:absolute;left:1280px;top:340px;width:520px',extra=f'data-out="{t1-0.2:.2f}"')
        t=t1+0.3
    dur=round(t+0.6,2)
    f=render_scene(pid,html+'</div>',dur)
    return f,ev
MAPPE={}
def s_mappa(k):
    import mappe
    m=mappe.MAPPE[k];dur={n:VD[n] for n,_ in m['voci']}
    st,tot,vt=mappe.schedule(m,m['voci'],dur)
    f=O+f'map{k}.mp4';still=O+f'map{k}.png'
    if not os.path.exists(f): mappe.render_map(m,st,tot,f,still=still)
    return f,[(VX+n+'.wav',t,0) for n,t,d in vt]
def s_gloss(n):
    v=f'GL{n}';d=vd(v);fr=frasi(TV[v]);tit=fr[0].rstrip('.');voci=[cifre(x) for x in fr[1:]]
    tm=tempi_frasi(voci,1.8,d-1.8)
    html='<div class="dk">'+logo()+T(0.2,'GLOSSARIO','position:absolute;left:140px;top:150px;font:800 30px Figtree;letter-spacing:.22em;color:#FFE600')
    html+=T(0.3,tit,"position:absolute;left:140px;top:200px;width:1640px;font:800 62px/1.1 'Bricolage Grotesque'")
    nn=len(voci);hh=min(120,int(590/nn)-12);y=340
    for x,(a,b) in zip(voci,tm):
        if ':' in x: g,r=x.split(':',1);x=f'<b style="color:#FFE600">{g}</b>:{r}'
        html+=(f'<div data-t0="{a-0.1:.2f}" data-t1="{b+0.2:.2f}" data-lo="0.38" data-dy="0" style="opacity:.38;position:absolute;left:140px;top:{y}px;width:1640px;height:{hh}px;box-sizing:border-box;border-radius:18px;background:rgba(255,255,255,.08);border:4px solid rgba(255,255,255,.18);display:flex;align-items:center;padding:0 34px;font:600 38px/1.25 Figtree">{x}</div>')
        y+=hh+12
    dur=round(d+1.8+1.0,2)
    return render_scene(f'gl{n}',html+'</div>',dur),[(VX+v+'.wav',1.0,0)]
def s_ripasso_finale(part):
    v=f'RF{part}';d=vd(v);base=1 if part==1 else 5;args=list(range(base,base+4))
    html='<div class="dk">'+logo()+T(0.2,'RIPASSO FINALE','position:absolute;left:140px;top:150px;font:800 30px Figtree;letter-spacing:.22em;color:#FFE600')
    html+=T(0.3,'Argomento per argomento',"position:absolute;left:140px;top:200px;width:1640px;font:800 62px/1.1 'Bricolage Grotesque'")
    seg=(d-0.5)/4;y=360
    for i,a in enumerate(args):
        t0=1.0+i*seg
        html+=(f'<div data-t0="{t0:.2f}" data-t1="{t0+seg:.2f}" data-lo="0.38" data-dy="0" style="opacity:.38;position:absolute;left:140px;top:{y}px;width:1640px;height:120px;box-sizing:border-box;border-radius:18px;background:rgba(255,255,255,.08);border:4px solid rgba(255,255,255,.18);display:flex;align-items:center;padding:0 34px;font:700 42px/1.2 Figtree"><span style="color:#FFE600;margin-right:24px">{a}</span>{viste.ARGT[a]}</div>')
        y+=140
    dur=round(d+2.2,2)
    return render_scene(f'rf{part}',html+'</div>',dur),[(VX+v+'.wav',1.0,0)]
def s_testo(pid,kick,tit,voce,rows=None,dur=None,jingle=None,voce_t=1.0):
    """scheda semplice blu: titolo grande + eventuale voce"""
    html='<div class="dk">'+logo()+T(0.2,kick,'position:absolute;left:0;right:0;top:360px;text-align:center;font:800 40px Figtree;letter-spacing:.22em;color:#FFE600')
    html+=T(0.5,tit,"position:absolute;left:160px;right:160px;top:440px;text-align:center;font:800 100px/1.1 'Bricolage Grotesque'")
    if rows: html+=T(1.0,rows,'position:absolute;left:160px;right:160px;top:700px;text-align:center;font:600 40px Figtree;color:#C9D6F5')
    ev=[]
    if jingle: ev.append((KIT+'/suoni/'+jingle[0],jingle[1],jingle[2]))
    if voce: ev.append((VX+voce+'.wav',voce_t,0))
    return render_scene(pid,html+'</div>',dur),ev
