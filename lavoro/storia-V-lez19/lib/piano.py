import json,os,sys,re,subprocess
sys.path.insert(0,'/home/claude/w19/lib')
from pezzi import *
from scene2 import *
import viste
from viste import Stati,ARGT
from ui import B,chrome,LOGO
from slide import *
TIT_LEZ="L’ITALIA DAL ’68 ALLA CRISI DELLA PRIMA REPUBBLICA"
ARGS_H=lambda items:''.join(f'<div style="display:flex;gap:16px;margin:0 0 12px"><b style="color:#2060AF;font-size:34px;width:34px">{i}</b><span style="font:600 32px/1.25 Figtree">{viste.ARGT[i]}</span></div>' for i in items)
def cover_html(box,anim=False,pg=1):
    d=lambda t:(f'data-t0="{t}" ' if anim else '')
    st=lambda extra:f'opacity:{0 if anim else 1};'+extra
    h=(f'<div class=abs style="left:80px;top:48px;width:170px">{LOGO}</div><div class=abs style="left:80px;right:80px;top:124px;height:1px;background:#D5DCE8"></div>'
       f'<div {d(0.2)}class=abs style="{st("left:80px;top:160px;font:700 24px Figtree;letter-spacing:.16em;color:#2060AF")}">STORIA V · VIDEOLEZIONE</div>'
       f'<div {d(0.5)}class=abs style="{st("left:80px;top:210px;width:1320px;font:800 88px/1.08 \'Bricolage Grotesque\'")}">L’ITALIA DAL ’68 ALLA CRISI<br>DELLA PRIMA REPUBBLICA</div>'
       f'<div {d(0.9)}class=abs style="{st("left:80px;top:420px;width:86px;height:8px;border-radius:4px;background:#2060AF")}"></div>'
       f'<div {d(1.2)}class=abs style="{st("left:80px;top:470px;width:1305px;box-sizing:border-box;padding:24px 34px;border-radius:20px;background:#F4F7FC;border:3px solid #D5DCE8;box-shadow:0 10px 26px rgba(60,72,100,.14)")}"><div style="font:700 22px Figtree;letter-spacing:.16em;color:#2060AF;margin-bottom:16px">ARGOMENTI</div><div style="display:flex;gap:40px"><div style="width:600px">{ARGS_H(range(1,5))}</div><div style="width:600px">{ARGS_H(range(5,9))}</div></div></div>'
       f'<div class=abs style="left:80px;right:80px;top:980px;height:1px;background:#D5DCE8"></div><div class=abs style="left:80px;top:1000px;font:700 22px Figtree;letter-spacing:.14em;color:#2060AF">STORIA V</div><div class=abs style="right:80px;top:1000px;font:700 22px Figtree;letter-spacing:.1em;color:#2060AF">Pagina {pg}</div>')
    if box: h+=right_col([])
    return h
def argomenti_html(items,pg):
    cards=''.join(card_html(f'<b>{i}</b> · {viste.ARGT[i]}','off').replace('opacity:0.5','opacity:1') for i in items)
    return (chrome('STORIA V',pg,'STORIA V · VIDEOLEZIONE')+f'<div class=abs style="left:80px;top:190px;font:800 56px/1.15 \'Bricolage Grotesque\'">Di cosa parliamo</div>'
        f'<div class=abs style="left:80px;top:282px;width:86px;height:8px;border-radius:4px;background:#2060AF"></div><div class=abs style="left:80px;top:316px">{cards}</div>'+right_col([]))
def compiti_html(tit,testo,pg):
    return (chrome('STORIA V',pg,'COMPITI')+f'<div class=abs style="left:80px;top:190px;font:800 56px/1.15 \'Bricolage Grotesque\'">{tit}</div><div class=abs style="left:80px;top:282px;width:86px;height:8px;border-radius:4px;background:#2060AF"></div>'
        f'<div class=abs style="left:80px;top:326px;width:1760px;box-sizing:border-box;padding:28px 36px;border-radius:20px;border:6px solid #FFE600;background:#fff;box-shadow:0 10px 26px rgba(60,72,100,.2);font:400 40px/1.5 Figtree">{testo}</div>')
class Run:
    def __init__(s,name,pg0=1):
        s.name=name;s.tl=[];s.t=0;s.prev=None;s.items=[];s.pg=pg0;s.b=None;s.tab=[]
    def add(s,pid,d,tipo,**k):
        s.tl.append(dict(id=pid,inizio=round(s.t,3),durata=round(d,3),tipo=tipo,**k));s.t+=d
        f=f'{OUT}/{pid}.mkv';s.items.append(f);lf=f'{OUT}/{pid}.last.png'
        if not os.path.exists(lf): last_frame(f,lf)
        s.prev=lf
    def built(s,pid): return os.path.exists(f'{OUT}/{pid}.mkv') and os.path.exists(f'{OUT}/{pid}.ok')
    def mark(s,pid): open(f'{OUT}/{pid}.ok','w').write('1')
    def clip(s,pid,mp4,last=False,tipo='clip'):
        if not s.built(pid): clip(pid,mp4,s.prev,last);s.mark(pid)
        s.add(pid,dur(f'{OUT}/{pid}.mkv'),tipo)
    def scena(s,pid,f_ev,tipo,last=False,**k):
        f,ev=f_ev
        if not s.built(pid): scena(pid,f,ev,s.prev,last);s.mark(pid)
        s.add(pid,dur(f'{OUT}/{pid}.mkv'),tipo,**k)
    def prof(s,pid,a,b,cues,imgs,argn,cards_of,tipo='prof',drop=(),statesfn=None,last=False):
        R=ranges(a,b)
        if drop:
            # toglie i segmenti indicati (incespicamenti) spezzando l'intervallo nelle pause
            R2=[]
            for x,y in R:
                cur=x
                for k in sorted(drop):
                    sg=SEG[k]
                    if x<=sg['inizio']<=y: R2.append((cur,sg['inizio']-0.1));cur=sg['fine']+0.1
                R2.append((cur,y))
            R=[(x,y) for x,y in R2 if y-x>0.3]
        pid_s=pid
        if not s.built(pid):
            sl=statesfn(R) if statesfn else None
            if not statesfn:
                with B() as bb:
                    st=Stati(bb,s.pg);slides=st.make(pid,R,cues,imgs,argn,cards_of);s.pg=st.pg;meta=st.meta
            else: slides=sl;meta=[]
            prof(pid,R,slides,s.prev,last);s.mark(pid)
            json.dump(dict(R=R,pg=s.pg,meta=meta),open(f'{OUT}/{pid}.json','w'))
        else:
            j=json.load(open(f'{OUT}/{pid}.json'));R=[tuple(x) for x in j['R']];s.pg=j['pg']
        s.add(pid,dur(f'{OUT}/{pid}.mkv'),tipo,orig=[R[0][0],R[-1][1]],a=a,b=b,**tabella_fine(a,b))
