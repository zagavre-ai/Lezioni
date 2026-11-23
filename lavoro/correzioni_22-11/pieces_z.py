# -*- coding: utf-8 -*-
import sys, os, re, json
sys.path.insert(0,'/home/work/build')
from anim import *
import av
from pieces_x import V,OLD,NAME,IMG,OUT
from pieces_y import *
fr=av.fr
DARK="""
html,body{background:#0B1530}
.bg{position:absolute;inset:0;background:radial-gradient(900px 700px at var(--x1) var(--y1),rgba(32,96,175,.55),transparent 70%),radial-gradient(800px 600px at var(--x2) var(--y2),rgba(255,176,60,.22),transparent 70%),#0B1530}
.dk{position:absolute;left:150px;right:150px;top:0;bottom:0;display:flex;flex-direction:column;justify-content:center}
.dk .k{font:700 28px FigB;letter-spacing:.2em;color:#7FB6F2;margin-bottom:26px}
.dk .b{font:800 130px/1.05 Bri;color:#fff}
.dk .s{font:800 64px/1.15 Bri;color:#FFB03C;margin-top:20px}
.dk .i{margin-top:46px;display:inline-block;align-self:flex-start;background:rgba(255,255,255,.1);border-radius:14px;padding:16px 30px;font:600 34px FigS;color:#fff}
.star{position:absolute;width:8px;height:8px;border-radius:50%;background:rgba(255,255,255,.5)}
"""
def dark_html(kicker,big,sub,info,t=0.0,foot=''):
    import math
    x1=30+10*math.sin(t*0.9);y1=30+12*math.cos(t*0.7);x2=78+8*math.cos(t*0.8);y2=75+9*math.sin(t*0.6)
    st="".join(f"<div class=star style='left:{(137*k)%1900}px;top:{(89*k+30*math.sin(t+k))%1040}px;opacity:{0.3+0.3*math.sin(t*1.3+k)}'></div>" for k in range(1,26))
    h=f"<div class=bg style='--x1:{x1}%;--y1:{y1}%;--x2:{x2}%;--y2:{y2}%'></div>{st}<img id=logo src='data:image/svg+xml;base64,{LOGO}' style='filter:brightness(0) invert(1);opacity:.85;left:80px'>"
    h+=f"<div class=dk><div class=k>{esc(kicker)}</div><div class=b>{esc(big)}</div>"+(f"<div class=s>{esc(sub)}</div>" if sub else "")+(f"<div class=i>{esc(info)}</div>" if info else "")+(f"<div style='margin-top:34px;font:600 34px FigS;color:#7FB6F2'>{esc(foot)}</div>" if foot else "")+"</div>"
    return shell(h,DARK)
def dark_piece(name,kicker,big,sub,info,dur,out,foot=''):
    N=fr(dur);ns=max(2,int(dur/0.6));items=[]
    for i in range(ns): items.append((f'{name}_{i}',dark_html(kicker,big,sub,info,i*0.6,foot)))
    render(items,'/home/work/build/lit')
    per=N//ns;st=[(f'/home/work/build/lit/{name}_{i}.png',per) for i in range(ns)];st[-1]=(st[-1][0],N-per*(ns-1))
    return av.states_video(st,out,xf=0.3)
def verifica_piece(out): return dict(path=out,n=dark_piece('verifica',"VERIFICA FINALE","Verifica finale","Storia · "+TITLE_EX,"10 domande · per continuare serve almeno l'80%",4.2,out,'Rispondi · premi Controlla · poi Continua'),audio=[(0.5,'wav',SND+'/quiz.wav')])
def compiti_intro(out): return dict(path=out,n=dark_piece('compitiintro',"A CASA","Compiti","", "",3.5,out),audio=[(0,'wav',SND+'/titolo.wav')])
SND='/home/user/Lezioni/kit/suoni'
COMP=json.load(open('/home/work/prev/video/compiti.json'))['esercizi']
def compiti_piece(out,page):
    texts=[e['testo'] for e in COMP]+["Svolgi i compiti qui sotto e premi Consegna: arrivano al docente nel tuo quaderno dei compiti."]
    d=vdur('COMPITI');lead=0.8;full=V['COMPITI'];ss=sents(full)
    # inizio di ogni compito: proporzionale ai caratteri (frasi 'Primo compito.' ... )
    marks=['Primo compito','Secondo compito','Terzo compito','Quarto compito','Svolgi i compiti'];tot=len(full);st=[]
    for m in marks:
        st.append(lead+d*full.index(m)/tot)
    total=lead+d+1.5;N=fr(total)
    leads=[f"{i+1}." for i in range(len(COMP))]+[""]
    def H(i): return lit_html("Compiti",f"STORIA V · A CASA",texts,i,page,leads=leads,fs=36,tfs=60,allv=False)
    items=[('comp_s',H(-1))]+[(f'comp_{i}',H(i)) for i in range(len(texts))]
    render(items,'/home/work/build/lit')
    states=[(f'/home/work/build/lit/comp_s.png',fr(st[0]-0.1))]
    for i in range(len(texts)):
        end=fr(st[i+1]-0.1) if i+1<len(texts) else N
        states.append((f'/home/work/build/lit/comp_{i}.png',end-sum(f for _,f in states)))
    return dict(path=out,n=av.states_video(states,out),audio=[(lead,'wav',vpath('COMPITI'))])
def spiegone_piece(P,out):
    """ripasso animato (voce Kore) di tutto quello che si è visto nella Parte precedente, argomento per argomento"""
    prev=PARTI[P-1];states=[];ev=[];t=0.7;items=[];first=True
    mapfinal={1:'/home/work/build/lit/map1_%d.png'%(len(MP.MAPS[1]['steps']))}
    SIMG={1:mapfinal[1] if os.path.exists(mapfinal[1]) else None,3:IMG(6),4:IMG(3),5:None,2:None}
    cum=[]
    for j,n in enumerate(prev):
        vn=f'SPG{P}_{j+1}';ss=sents(V[vn]);d=vdur(vn);tot=sum(len(x) for x in ss);x=t;ts=[]
        for q in ss: ts.append(x);x+=d*len(q)/tot
        ev.append((t,'wav',vpath(vn)));cum.append((n,ss,ts,t,t+d))
        t=t+d+0.9
    total=t+0.6;N=fr(total)
    seq=[]   # (png, start)
    for n,ss,ts,a,b in cum:
        for i in range(len(ss)):
            nm=f'spg{P}_{n}_{i}'
            img=SIMG.get(n)
            items.append((nm,lit_html("Ripasso: "+ARG[n-1]['nome'],"RIPASSO DELLA PARTE PRECEDENTE",ss,i,None,img=img,fs=38,tfs=56,chip=None).replace("Pagina None","")))
            seq.append((f'/home/work/build/lit/{nm}.png',ts[i]-0.15 if i>0 else ts[i]-0.6))
    render(items,'/home/work/build/lit')
    seq[0]=(seq[0][0],0.0)
    st=[]
    for k,(p,s) in enumerate(seq):
        e=seq[k+1][1] if k+1<len(seq) else total
        st.append((p,fr(e)-fr(s)))
    st[-1]=(st[-1][0],N-sum(f for _,f in st[:-1]))
    return dict(path=out,n=av.states_video(st,out),audio=ev)
if __name__=='__main__':
    print(verifica_piece(OUT+'/verifica.mp4'),compiti_intro(OUT+'/compiti_intro.mp4'))

def quiz_card(g,n,out):
    nm=ARG[n-1]['nome'].replace("Il crollo dell'URSS","Il crollo dell'Unione Sovietica")
    return dark_piece(f'quizc{g}',"PAUSA DEL VIDEO · QUIZ",f"Quiz {g}",nm,"5 domande · per continuare serve almeno l'80%",4.2,out,'Rispondi · premi Controlla · poi Continua')
