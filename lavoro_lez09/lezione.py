import os,re,json,subprocess,sys,math
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from scenes import *
from mappe_dati import MAPPE
TIT_ESATTO="L’Italia del regime fascista (1925-1938)"
QZ=json.load(open('/home/user/Lezioni/w/quiz.json'))
QT={'Q1':'La svolta autoritaria','Q2':'La fascistizzazione dello Stato','Q3':'Il consolidamento del potere','Q4':'La gioventù fascista','Q5':'La scuola fascista','Q6':'I media e i Patti Lateranensi','Q7':'Il corporativismo','Q8':'Quota 90 e autarchia','Q9':'Il ruolo della donna','Q10':'L’Impero e le Leggi Razziali'}
# ---------- mappe ----------
CAT={'c':('#FFDCC6','#C2410C'),'d':('#DCEEFB','#1D4ED8'),'k':('#FFF3BF','#A16207'),'e':('#DDF3E4','#15803D'),'q':('#EBE3F7','#6D28D9')}
def map_html(m,vis,hl,arcs,full=False,pag=''):
    nodes={n[0]:n for n in m['nodi']};svg='';boxes=''
    # archi visibili: (da,a) in arcs
    for (da,a,lab) in m['archi']:
        if (da,a) not in arcs:continue
        A=nodes[da];B=nodes[a];x1=A[3]+A[5]/2;y1=A[4]+A[6];x2=B[3]+B[5]/2;y2=B[4]-4
        straight=abs(x1-x2)<=2
        ym=y1 if straight else y1+26
        path=f'M{x1},{y1} L{x2},{y2-8}' if straight else f'M{x1},{y1} L{x1},{ym} L{x2},{ym} L{x2},{y2-8}'
        tip=y2-3
        svg+=f'<path d="{path}" fill="none" stroke="#0B1530" stroke-width="5" stroke-linejoin="round"/><path d="M{x2-15},{tip-24} L{x2},{tip} L{x2+15},{tip-24}" fill="none" stroke="#0B1530" stroke-width="5" stroke-linecap="round" stroke-linejoin="round"/>'
        ly=(ym+tip-24)/2 if not straight else (y1+tip-24)/2
        boxes+=f'<div class="lab" style="left:{x2}px;top:{ly}px">{G.esc(lab)}</div>'
    for nid in vis:
        n=nodes[nid];bg,bd=CAT[n[2]];fs=50 if n[2]=='c' else 36
        fam='Bri' if n[2]=='c' else 'Fig'
        wt=800 if n[2]=='c' else 600
        txt='<div>'+re.sub(r'(\(\d{4}-\d{4}\))',r'<span style="white-space:nowrap">\1</span>',G.esc(n[1]))+'</div>'
        hlc=' hl' if nid==hl else ''
        boxes+=f'<div class="b{hlc}" style="left:{n[3]}px;top:{n[4]}px;width:{n[5]}px;height:{n[6]}px;background:{bg};border:5px solid {bd};font:{wt} {fs}px/1.3 {fam}">{txt}</div>'
    leg=''.join(f'<span><i style="background:{CAT[k][0]};border-color:{CAT[k][1]}"></i>{t}</span>' for k,t in (('c','concetto centrale'),('d','date e sequenze'),('k','parole chiave'),('e','esempi e opere'),('q','conseguenze')))
    css='''.b{position:absolute;box-sizing:border-box;display:flex;align-items:center;justify-content:center;text-align:center;padding:8px 20px;border-radius:18px;color:#0B1530;box-shadow:0 8px 20px rgba(60,72,100,.15)}
.b.hl{box-shadow:0 0 0 10px #FFE600,0 12px 26px rgba(60,72,100,.25)}
.lab{position:absolute;transform:translate(-50%,-50%);background:#fff;padding:2px 12px;font:600 30px Fig;color:#0B1530;white-space:nowrap}
#leg{position:absolute;right:60px;top:28px;display:flex;gap:16px;font:600 20px Fig;color:#0B1530}#leg span{display:flex;align-items:center;gap:7px}#leg i{display:inline-block;width:24px;height:17px;border-radius:4px;border:3px solid}
#mt{position:absolute;left:60px;top:22px;width:860px;font:800 34px/1.15 Bri;color:#2060AF}#mk{position:absolute;left:60px;top:116px;font:700 22px Fig;letter-spacing:.14em;color:#2060AF}'''
    return f'''<!doctype html><html><head><meta charset="utf-8"><style>{G.CSS}{css}</style></head><body>
<div id="mt">{G.esc(m["titolo"])}</div><div id="mk">MAPPA DEL PROFESSORE{(" · "+m["sub"]) if m["sub"] else ""}</div><div id="leg">{leg}</div>
<svg width="1920" height="1080" style="position:absolute;left:0;top:0">{svg}</svg>{boxes}
<div style="position:absolute;left:60px;bottom:24px;font:700 20px Fig;letter-spacing:.1em;color:#2060AF">STORIA V</div><div style="position:absolute;right:60px;bottom:24px;font:700 20px Fig;letter-spacing:.1em;color:#2060AF">{("Pagina %s"%pag) if pag else ""}</div></body></html>'''
def map_states(key,pag=''):
    m=MAPPE[key];vis=[];arcs=set();S=[]
    for i,(nid,arc,txt) in enumerate(m['passi'],1):
        vis.append(nid)
        if arc:da,a=arc.split('>');arcs.add((da,a))
        S.append(dict(html=map_html(m,list(vis),nid,set(arcs),pag=pag),voce=f'MAP_{key}_{i}'))
    S.append(dict(html=map_html(m,list(vis),None,set(arcs),pag=pag),hold=4.0))
    return S
# ---------- scene titolo / quiz / AP / PI-PS ----------
def dark(kicker,big,small='',sz=84):
    inner=f'<div style="position:absolute;left:140px;top:300px;width:1640px"><div style="font:800 {sz}px/1.1 Bri;color:#fff">{G.esc(big)}</div><div style="margin-top:34px;font:600 40px/1.4 Fig;color:#BFD3F2">{G.esc(small)}</div></div>'
    return hdoc(inner,kicker,'',0,'',True)
def t_states(n,titolo):return [dict(html=dark(f'ARGOMENTO {n}',titolo),hold=3.3)]
def quiz_states(q):
    return [dict(html=dark('QUIZ',QZ[q]['title'].split('· ',1)[-1],'5 domande · per continuare serve almeno l’80%',sz=76),hold=4.3)]
def rolling(kicker,title,texts,voices,dark_=False,cap='',onfinal=False,pag=''):
    S=[]
    for i,v in enumerate(voices):
        vis=list(range(max(0,i-1),i+1))  # corrente + precedente
        body=''.join(f'<div class="card {"on" if j==i else "dim"}"><span class=n>{j+1}</span>{G.esc(texts[j])}</div>' for j in vis)
        inner=f'<div style="position:absolute;left:80px;top:300px;width:1760px;display:flex;flex-direction:column;gap:24px">{body}</div>'
        S.append(dict(html=hdoc(inner,kicker,title,260 if len(title)<60 else 270,pag,False),voce=v))
    return S

ARGT={1:'La svolta autoritaria',2:'La fascistizzazione dello Stato',3:'Il consolidamento del potere',4:'La gioventù fascista',5:'La scuola fascista',6:'I media e i Patti Lateranensi',7:'Il corporativismo',8:'Quota 90 e autarchia',9:'Il ruolo della donna',10:'L’Impero e le Leggi Razziali'}
APR={'AP2_2':'AP2_2_R2','AP6_1':'AP6_1_R2'}
def ap_states(n,pag=''):
    vs=[APR.get(f'AP{n}_{i}',f'AP{n}_{i}') for i in (1,2,3,4)]
    return rolling('APPROFONDIMENTO',ARGT[n],[cifre(TESTI[v]) for v in vs],vs,pag=pag)
def pips_states(n,pag=''):
    pi=dark('RIPASSO',ARGT[n],'Guarda lo schema e ripeti ad alta voce',sz=80)
    S=[dict(html=pi,voce=f'PI{n}')]
    vs=[f'PS{n}_{i}' for i in range(1,7) if f'PS{n}_{i}' in TESTI]
    tx=[cifre(TESTI[v]) for v in vs]
    for i,v in enumerate(vs):
        body=''.join(f'<div class="card {"on" if j==i else ("dim" if j<i else "")}" style="{"visibility:hidden" if j>i else ""}"><span class=n>{j+1}</span>{G.esc(tx[j])}</div>' for j in range(len(vs)))
        inner=f'<div style="position:absolute;left:80px;top:300px;width:1760px;display:flex;flex-direction:column;gap:14px">{body}</div>'
        S.append(dict(html=hdoc(inner,'RIPASSO',ARGT[n],260,pag,False),voce=v))
    return S

def cover_html(args_titles,cam=False,parte=None,pag=1,label=None):
    li=''.join(f'<li>{G.esc(t)}</li>' for t in (args_titles or []))
    inner=f'''<div style="position:absolute;left:80px;top:230px;width:1290px;font:800 84px/1.08 Bri;color:#0B1530;text-transform:uppercase">{G.esc(TIT_ESATTO)}</div>
<div style="position:absolute;left:80px;top:495px;width:1290px;height:6px;border-radius:3px;background:#2060AF;width:90px"></div>
<div style="display:{'block' if args_titles else 'none'};position:absolute;left:80px;top:560px;width:1290px;padding:26px 36px;border-radius:20px;background:#F4F8FD;border:3px solid #DDE7F5;box-shadow:0 10px 26px rgba(60,72,100,.12)"><div style="font:800 22px Fig;letter-spacing:.14em;color:#2060AF;margin-bottom:12px">ARGOMENTI</div><ul style="margin:0;padding-left:34px;font:600 34px/1.45 Fig;color:#0B1530">{li}</ul></div>'''
    h=G.doc(inner,(label or 'STORIA V · VIDEOLEZIONE')+(f' · PARTE {parte}' if parte else ''),'',0,'',cam,None)
    return h.replace('<div id="tit"></div>','').replace('<div id="pag">Pagina </div>',f'<div id="pag">Pagina {pag}</div>')
ARG_P1=[ARGT[i] for i in range(1,6)];ARG_P2=[ARGT[i] for i in range(6,11)]

def gl_states(k,args_t,pag=''):
    t=TESTI[k];terms=[x.strip() for x in re.split(r'(?<=\.)\s+',t)][1:]
    items=[]
    for x in terms:
        a,b=x.split(': ',1);items.append((a,cifre(b)))
    tot=sum(len(a)+len(b) for a,b in items)+len('Glossario');acc=len('Glossario');S=[];dv=None
    w,_=voce(k);dv=dur(w)
    for i,(a,b) in enumerate(items):
        vis=list(range(max(0,i-2),i+1))
        body=''.join(f'<div class="card {"on" if j==i else "dim"}"><span class=n>{j+1}</span><b>{G.esc(items[j][0])}:</b> {G.esc(items[j][1])}</div>' for j in vis)
        inner=f'<div style="position:absolute;left:80px;top:300px;width:1760px;display:flex;flex-direction:column;gap:22px">{body}</div>'
        st=dict(html=hdoc(inner,'GLOSSARIO','Le parole da ricordare',250,pag,False));
        if i==0:st['voce']=k
        else:st['rel']=dv*acc/tot
        S.append(st);acc+=len(a)+len(b)
    return S
def rf_states(k,part,pag=''):
    t=TESTI[k];sents=[x.strip() for x in re.split(r'(?<=\.)\s+',t)][1:]
    w,_=voce(k);dv=dur(w);tot=sum(len(x) for x in sents)+10;acc=10;S=[]
    for i,x in enumerate(sents):
        body=''.join(f'<div class="card {"on" if j==i else "dim"}"><span class=n>{j+1}</span>{G.esc(cifre(sents[j]))}</div>' for j in range(i+1))
        inner=f'<div style="position:absolute;left:80px;top:300px;width:1760px;display:flex;flex-direction:column;gap:22px">{body}</div>'
        st=dict(html=hdoc(inner,'RIPASSO FINALE',f'Parte {part}',250,pag,False))
        if i==0:st['voce']=k
        else:st['rel']=dv*acc/tot
        S.append(st);acc+=len(x)
    return S
def fin_states(k):
    return [dict(html=dark('PER OGGI È TUTTO','Ci vediamo alla prossima' if False else 'A presto','',sz=96),voce=k)]
def dp_states(k,part,pag=''):
    items=ARG_P1 if part==1 else ARG_P2
    li=''.join(f'<div class="card" style="font-size:40px"><span class=n>{i+1}</span>{G.esc(t)}</div>' for i,t in enumerate(items))
    inner=f'<div style="position:absolute;left:80px;top:300px;width:1760px;display:flex;flex-direction:column;gap:16px">{li}</div>'
    return [dict(html=hdoc(inner,'DI COSA PARLIAMO','Gli argomenti di oggi',250,pag,False),voce=k)]
def cover_states(k,part,pag=1):
    return [dict(html=cover_html(ARG_P1 if part==1 else ARG_P2,False,part,pag),voce=k)]

def plan_pagine(parte):
    """numero di pagina di ogni pezzo (stessa numerazione di video e dispensa)"""
    from prof import build,build_riep,seq_pagine
    P={};c=0
    if parte==1:
        P['COVERV']=1;P['D0']=1;P['DP']=2;c=2;args=[1,2,3,4,5];maps={2:['M1a','M1b']}
    else:
        P['SPIEGONE']=1;c=5;P['COVERV']=c+1;P['DP']=c+2;c+=2;args=[6,7,8,9,10];maps={6:['M2'],8:['M3'],10:['M4']}
    for n in args:
        d=build(n,0,'x');_,pe=seq_pagine(d,c);P[f'A{n}']=c;c=pe
        c+=1;P[f'AP{n}']=c
        for mk in maps.get(n,[]):c+=1;P[f'MAP_{mk}']=c
        c+=1;P[f'PS{n}']=c
    if parte==2:
        d=build_riep();_,pe=seq_pagine(d,c);P['A11']=c;c=pe
    c+=1;P['GL']=c;c+=1;P['RF']=c
    return P
