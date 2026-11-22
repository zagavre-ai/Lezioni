# Stati delle slide del prof (card a finestra, immagini) e parole chiave
import re,json,sys
sys.path.insert(0,'/home/claude/w19/lib')
from slide import *
from core import rel
P=json.load(open('/home/claude/w19/slide.json'))
ARGT={1:"Il Sessantotto e la protesta studentesca",2:"L'Autunno caldo e le riforme",3:"Gli anni di piombo e lo stragismo",4:"Il caso Moro e la solidarietà nazionale",5:"Conquiste sociali e crisi energetica",6:"Gli anni Ottanta: riflusso e Pentapartito",7:"Tangentopoli e il crollo dei partiti",8:"La transizione e i governi tecnici"}
PTIT={2:None,4:P[3]['titolo'],6:P[5]['titolo'],8:P[7]['titolo'],9:P[8]['titolo'],10:P[9]['titolo'],12:P[11]['titolo'],14:P[13]['titolo'],17:P[16]['titolo']}
def kicker(n): return f"{n:02d} · {ARGT[n].upper()}"
def pagina(pg): return P[pg-1]
def kws(pg,cards):
    out=[]
    for i in cards:
        t=pagina(pg)['par'][i]
        bs=re.findall(r'<b>(.*?)</b>',t)
        for j,b in enumerate(bs):
            b=b.strip().rstrip(':')
            if j==0: continue
            out.append(b)
    for i in cards:
        t=pagina(pg)['par'][i];b=re.findall(r'<b>(.*?)</b>',t)
        if b and len(out)<5: out.append(b[0].strip())
    res=[]
    for k in out:
        k=spiega(k)
        if k not in res and len(k)<=44: res.append(k)
    return res[:5]
IMG={ # chiave: (titolo, didascalia, file)
 'operai':("Gli operai in sciopero","Una marcia di operai metalmeccanici a Torino nel 1969.",'operai'),
 'fontana':("Gli effetti della strage di Piazza Fontana","La sede della Banca dell'agricoltura di Milano devastata, dopo lo scoppio della bomba il 12 dicembre 1969, che causò la morte di 17 persone e ne ferì 88.",'fontana'),
 'berlinguer':("Berlinguer e Moro","La fotografia ritrae la storica stretta di mano tra Enrico Berlinguer e Aldo Moro, nel 1977, un gesto che simboleggia il tentativo di cooperazione tra DC, cioè Democrazia Cristiana, e PCI, cioè Partito Comunista Italiano.",'berlinguer'),
 'moro_br':("Aldo Moro prigioniero delle Brigate rosse","La fotografia di Aldo Moro con il simbolo e la scritta delle Brigate rosse, inviata dai terroristi alla redazione del «Messaggero».",'moro_br'),
 'marcia':("La protesta di impiegati e dirigenti della Fiat","La cosiddetta «marcia dei quarantamila» sfila per le vie di Torino nell'ottobre 1980.",'marcia'),
 'craxi':("Bettino Craxi","Il leader socialista Bettino Craxi a un comizio del suo partito nel 1982.",'craxi'),
 'dipietro':("Antonio Di Pietro","L'avvocato Di Pietro durante una delle udienze di «Tangentopoli», 1993.",'dipietro'),
 'capaci':("La strage di Capaci","Il luogo della cosiddetta «strage di Capaci», il 23 maggio 1992.",'capaci')}
KW_IMG={'operai':['Operai','Sciopero','1969'],'fontana':['Piazza Fontana','12 dicembre 1969'],'berlinguer':['Berlinguer','Moro','1977'],'moro_br':['Aldo Moro','Brigate rosse'],'marcia':['Marcia dei quarantamila','Fiat','1980'],'craxi':['Bettino Craxi','Partito Socialista'],'dipietro':['Antonio Di Pietro','Tangentopoli'],'capaci':['Strage di Capaci','1992']}
def html_img(key,argn,pg,cam=True):
    tit,cap,f=IMG[key]
    from PIL import Image
    im=Image.open(f'/home/claude/w19/foto/{f}.png');w,h=im.size
    s=min(780/w,560/h);W_,H_=int(w*s),int(h*s)
    cardx=80+W_+40;cw=1385-cardx
    return (chrome('STORIA V',pg,kicker(argn))+
      f'<div class=abs style="left:80px;top:190px;width:1305px;font:800 52px/1.15 \'Bricolage Grotesque\'">{tit}</div>'
      f'<div class=abs style="left:80px;top:282px;width:86px;height:8px;border-radius:4px;background:#2060AF"></div>'
      f'<img class=abs src="file:///home/claude/w19/foto/{f}.png" style="left:80px;top:326px;width:{W_}px;height:{H_}px;border-radius:14px;box-shadow:0 12px 30px rgba(60,72,100,.28)">'
      f'<div class=abs style="left:{cardx}px;top:326px;width:{cw}px;box-sizing:border-box;padding:22px 26px;border-radius:18px;border:6px solid #FFE600;background:#fff;box-shadow:0 10px 26px rgba(60,72,100,.2);font:400 36px/1.45 Figtree">{cap}</div>'
      +right_col(KW_IMG[key],cam=cam))
class Stati:
    def __init__(s,b,pg0):
        s.b=b;s.pg=pg0;s.cache={};s.win={};s.meta=[]
    def paras(s,pg): return pagina(pg)['par']
    def h(s,pg):
        if pg not in s.cache: s.cache[pg]=measure(s.b,s.paras(pg))
        return s.cache[pg]
    def titolo(s,pg,argn):
        return ARGT[argn] if PTIT.get(pg) is None else PTIT[pg]
    def make(s,pid,R,cues,imgs,argn,cards_of):
        """cues=[(t_orig,page,card)], imgs=[(t0,t1,key)], cards_of={page:[indici delle card dell'argomento]} -> [(t_rel,png)]"""
        ev=sorted({c[0] for c in cues}|{i[0] for i in imgs}|{i[1] for i in imgs})
        D=sum(y-x for x,y in R);out=[];last=None;lastt=-999;cur=None
        def view_at(t):
            for a,b_,k in imgs:
                if a-1e-6<=t<b_-1e-6: return ('img',k)
            c=[x for x in cues if x[0]<=t+1e-6]
            return ('card',c[-1][1],c[-1][2]) if c else None
        times=[ev[0]] if ev else []
        tt=sorted(set(ev)|{R[0][0]})
        # aggiungi sotto-slide a ogni 150 s di permanenza
        pts=[];prev=None
        for t in tt:
            v=view_at(t)
            if v is None: continue
            pts.append((t,v))
        full=[]
        for i,(t,v) in enumerate(pts):
            t_end=pts[i+1][0] if i+1<len(pts) else R[-1][1]
            full.append((t,v))
            k=1
            while rel(R,t_end)-rel(R,t)>150*(k+0.0) and True:
                # punto intermedio ogni 150 s di tempo montato
                tt2=t
                # trova il tempo originale che corrisponde a +150k s
                target=rel(R,t)+150*k
                # inverti rel
                acc=0;to=None
                for x,y in R:
                    if acc+(y-x)>=target: to=x+(target-acc);break
                    acc+=y-x
                if to is None or to>=t_end-8: break
                full.append((to,v,'sub'));k+=1
        full.sort(key=lambda z:z[0])
        res=[];lastslide=None
        for item in full:
            t,v=item[0],item[1];sub=len(item)>2
            if v[0]=='img':
                slide=('img',v[1]);new=(slide!=lastslide) or sub
                if new: s.pg+=1
                png=f'/home/claude/w19/out/{pid}_{len(res):02d}.png'
                s.b.shot(html_img(v[1],argn,s.pg),png)
                if not s.meta or s.meta[-1]['pg']!=s.pg: s.meta.append(dict(pg=s.pg,kind='img',key=v[1],argn=argn))
                lastslide=slide;res.append((rel(R,t),png));continue
            _,pg,card=v;paras=s.paras(pg);h=s.h(pg)
            titolo=s.titolo(pg,argn)
            av=avail_for(titolo);cs=cards_of[pg]
            hh=[h[i] if i in cs else 9999 for i in range(len(h))]
            w=s.win.get(pg)
            newwin=False
            if w is None or card not in w or sub and False:
                w=window(hh,card,av);newwin=True;s.win[pg]=w
            slide=('card',pg,tuple(w));new=(slide!=lastslide) or sub
            if new: s.pg+=1
            png=f'/home/claude/w19/out/{pid}_{len(res):02d}.png'
            s.b.shot(slide_html(titolo,kicker(argn),s.pg,paras,card,w,kws(pg,cs)),png)
            if not s.meta or s.meta[-1]['pg']!=s.pg: s.meta.append(dict(pg=s.pg,kind='card',page=pg,win=list(w),argn=argn,titolo=titolo,keys=kws(pg,cs)))
            lastslide=slide;res.append((rel(R,t),png))
        # il primo stato parte da 0
        if res: res[0]=(0,res[0][1])
        return res
