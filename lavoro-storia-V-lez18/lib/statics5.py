import sys,json,re,os,base64,html as H
sys.path.insert(0,'/tmp/L18/lib')
from slides import *
from content5 import *
import slides as _s
from align import sentence_times
OUT='/tmp/L18/st'
MAT='STORIA V &nbsp;·&nbsp; Prof. Giorgio Mazzotti'
TXT={x['nome']:x['testo'] for x in json.load(open('/tmp/L18/voci/scambio/storia-V-lez18/testi_voci.json'))}
# ---- ordine pagine (PDF = video)
order=['cover','INTRO2']
for n in range(1,10):
    order+=[f'S{n}{"abcd"[j]}' for j in range(len(SL[n]))]
    if n==3:order+=['IMGlenin']
    if n==4:order+=['IMGtrockij']
    order+=[f'A{n}']
    if n in (2,4,6,8):order+=[f'M{ {2:1,4:2,6:3,8:4}[n] }']
    order+=[f'P{n}']
    if n==9:order+=['IMGbrest','IMGurss']
    if n==4:order+=['GL1']
order+=['GL2']
# nota: per i PDF le pagine IMG di T6/T9 usate come approfondimento coincidono con le slide immagine
PAGES={k:i for i,k in enumerate(order,1)};json.dump(PAGES,open(OUT+'/pages.json','w'))
R_=R()
def b64(p):return base64.b64encode(open(p,'rb').read()).decode()
def cardhtml(l,b,i,on):return f'<div class="card {"on" if on else ""}"><div class=num>{i+1}</div><span class=t>{l}:</span> {b}</div>'
# ---- copertina (titolo su 2 righe: la card scende)
def cover(prof,part=1):
    items=[NOMI[n] for n in (range(1,10) if True else [])]
    h=f'<img id=logo src="data:image/svg+xml;base64,{LOGO}"><div class=hl style="top:124px"></div>'
    h+=f'<div class=lab style="top:168px">STORIA V &nbsp;·&nbsp; VIDEOLEZIONE{" &nbsp;·&nbsp; PARTE 2" if part==2 else ""}</div>'
    h+='<div class=ttl style="top:222px;font-size:76px;width:1300px;line-height:1.04">La Rivoluzione russa e la nascita dell\'URSS (1917-1922)</div><div class=bar style="top:396px"></div>'
    lst=''.join(f'<li style="padding:5px 0 5px 36px;position:relative"><span style="position:absolute;left:0;top:19px;width:12px;height:12px;border-radius:50%;background:#2060AF"></span>{H.escape(x)}</li>' for x in items)
    h+=f'<div style="position:absolute;left:80px;top:440px;width:1240px;background:#fff;border:2px solid #E3E8F0;border-radius:24px;box-shadow:0 12px 34px rgba(20,40,90,.09);padding:24px 40px"><div style="font-weight:800;font-size:21px;letter-spacing:.2em;color:#2060AF;background:#E9F0FB;display:inline-block;padding:7px 16px;border-radius:20px;margin-bottom:14px">ARGOMENTI</div><ul style="list-style:none;font-size:29px;font-weight:700;line-height:1.2">{lst}</ul></div>'
    h+=f'<div class=hl style="top:981px"></div><div class=foot style="left:80px">{MAT}</div><div class=foot style="right:80px">Pagina 1</div>'
    if prof:h+=prof_box()
    return h
shot(R_,cover(False),OUT+'/cover_np.png');shot(R_,cover(True),OUT+'/cover_p.png')
shot(R_,cover(False,2),OUT+'/cover2_np.png');shot(R_,cover(True,2),OUT+'/cover2_p.png')
# ---- intro2 (percorso)
for prof in (True,False):
    h=frame(MAT,PAGES['INTRO2'],'Introduzione','Il percorso della lezione',tsize=56,titley=194)
    h+='<div style="position:absolute;left:80px;top:320px;width:1290px;display:grid;grid-template-columns:1fr 1fr 1fr;gap:16px">'+''.join(f'<div class=card style="position:relative;padding:18px 20px 18px 74px;font-size:27px;font-weight:700;line-height:1.2;min-height:112px"><div class=num style="top:20px;left:18px">{n}</div>{H.escape(t)}</div>' for n,t in NOMI.items())+'</div>'
    if prof:h+=prof_box()
    shot(R_,h,f'{OUT}/intro2_{"p" if prof else "np"}.png')
IMGHTML='<div style="position:absolute;left:80px;top:540px;border-radius:22px;overflow:hidden;box-shadow:0 14px 36px rgba(20,40,90,.14);border:2px solid #E3E8F0;background:#fff;padding:10px"><img src="data:image/png;base64,'+base64.b64encode(open(OUT+'/img_brest.png','rb').read()).decode()+'" style="height:410px;display:block"></div>'
# ---- slide dei temi
for n in range(1,10):
    for j,cards in enumerate(SL[n]):
        key=f'S{n}{"abcd"[j]}';pg=PAGES[key];lab=f'{n:02d} · {NOMI[n]}'
        ttl=TITLES[n] if n!=6 else 'Brest-Litovsk e la Guerra Civile (1918-1922)'
        ex=' style="--fs:34px"' if len(cards)==1 else ''
        kw=[c[2] for c in cards]
        for st in range(0,len(cards)+1):
            body=frame(MAT,pg,lab,ttl,tsize=56,titley=194)+f'<div class=col{ex}>'+''.join(cardhtml(l,b_,i,i==st-1) for i,(l,b_,k_) in enumerate(cards))+'</div>'+prof_box(kw,(st-1,) if st>0 else ())+(IMGHTML if (n==6 and j==0) else '')
            res=shot(R_,body,f'{OUT}/{key}_{st}.png');print(key,st,res)
        shot(R_,frame(MAT,pg,lab,ttl,tsize=56,titley=194)+f'<div class=col{ex}>'+''.join(cardhtml(l,b_,i,False) for i,(l,b_,k_) in enumerate(cards))+'</div>'+(IMGHTML if (n==6 and j==0) else ''),f'{OUT}/{key}_pdf.png')
# ---- slide immagine (con e senza prof)
IMG={'lenin':('03',"Dualismo di potere e Lenin","Vladimir Lenin"),'trockij':('04',"Dalle giornate di luglio a Ottobre","Lev Trockij"),'brest':('09',"La nascita dell'URSS e la successione","La Russia dopo il trattato di Brest-Litovsk"),'urss':('09',"La nascita dell'URSS e la successione","La nascita dell'Unione Sovietica (1922)")}
from PIL import Image
for k,(nn,nome,tt) in IMG.items():
    pg=PAGES['IMG'+k];im=Image.open(f'{OUT}/img_{k}.png');W0,H0=im.size
    h=min(660,int(H0*1230/W0)) ;w=int(W0*h/H0)
    if w>1290:w=1290;h=int(H0*w/W0)
    for prof in (False,True):
        body=frame(MAT,pg,f'{nn} · {nome}',tt,tsize=56,titley=194)
        body+=f'<div style="position:absolute;left:80px;top:300px;width:{w+24}px;border-radius:22px;overflow:hidden;box-shadow:0 14px 36px rgba(20,40,90,.14);border:2px solid #E3E8F0;background:#fff;padding:12px"><img src="data:image/png;base64,{b64(f"{OUT}/img_{k}.png")}" style="width:{w}px;height:{h}px;display:block"></div>'
        if prof:body+=prof_box()
        shot(R_,body,f'{OUT}/IMG{k}_{"p" if prof else "np"}.png')
# ---- approfondimenti: 3 card dalle frasi della voce (o la carta)
ANC={}
for n in range(1,10):
    pg=PAGES[f'A{n}'];lab=f'{n:02d} · {NOMI[n]}'
    v=f'AN{AN1[n]}'
    if n in ANMAP:
        k='brest' if n==6 else 'urss';shutil=__import__('shutil');shutil.copy(f'{OUT}/IMG{k}_np.png',f'{OUT}/A{n}_0.png');ANC[n]=None;continue
    ss=re.split(r'(?<=[.!?])\s+',TXT[v]);
    # raggruppa in 3 card: la 1a frase = titolo della card 1
    g=[ss[:1+ (len(ss)-1)//3],ss[1+(len(ss)-1)//3:1+2*((len(ss)-1)//3)+1],[]]
    k3=(len(ss)+2)//3;g=[ss[i*k3:(i+1)*k3] for i in range(3)];g=[x for x in g if x]
    cards=[(x[0].rstrip('.'),' '.join(x[1:]) if len(x)>1 else '') for x in g]
    ANC[n]=[x for x in g]
    for st in range(0,len(cards)+1):
        body=frame(MAT,pg,lab,'Per approfondire',tsize=56,titley=194)+'<div class="col wide" style="top:316px;--fs:28px">'+''.join(f'<div class="card {"on" if i==st-1 else ""}"><div class=num>{i+1}</div><span class=t>{H.escape(l)}</span><br>{H.escape(b)}</div>' for i,(l,b) in enumerate(cards))+'</div>'
        res=shot(R_,body,f'{OUT}/A{n}_{st}.png');print('A',n,st,res)
    shot(R_,frame(MAT,pg,lab,'Per approfondire',tsize=56,titley=194)+'<div class="col wide" style="top:316px;--fs:28px">'+''.join(f'<div class=card><div class=num>{i+1}</div><span class=t>{H.escape(l)}</span><br>{H.escape(b)}</div>' for i,(l,b) in enumerate(cards))+'</div>',f'{OUT}/A{n}_pdf.png')
json.dump({str(k):v for k,v in ANC.items()},open(OUT+'/anc.json','w'),ensure_ascii=False)
# ---- schema
for n in range(1,10):
    pg=PAGES[f'P{n}'];rows=SCH[n]
    def tab(vis,on):
        h='<div class=tab style="top:330px;width:1760px"><div class=th><div style="width:560px">PUNTO CHIAVE</div><div>IN BREVE</div></div>'
        for i,(a,b) in enumerate(rows):
            h+=f'<div class="tr {"v" if i<vis else ""} {"on" if i==on else ""}"><div class=c1>{H.escape(a)}</div><div class=c2>{H.escape(b)}</div></div>'
        return h+'</div>'
    base=lambda:frame('STORIA V',pg,None,NOMI[n],tsize=64,titley=190,pill='Pillola di storia')
    for r in range(-1,len(rows)):shot(R_,base()+tab(max(r+1,0),r),f'{OUT}/P{n}_{r+1}.png')
    shot(R_,base()+tab(len(rows),-1),f'{OUT}/P{n}_end.png')
# ---- glossari
for gk,T,pgk in (('GL1',TERMS1,'GL1'),('GL2',TERMS2,'GL2')):
    for on in range(-1,len(T)):
        h=frame(MAT,PAGES[pgk],None,'Parole chiave',tsize=56,titley=194,pill='Glossario')
        h+='<div class=tab style="top:300px;width:1760px">'+''.join(f'<div class="tr v {"on" if i==on else ""}" style="font-size:30px"><div class=c1 style="width:520px;padding:14px 24px">{H.escape(a)}</div><div class=c2 style="padding:14px 24px">{H.escape(b)}</div></div>' for i,(a,b) in enumerate(T))+'</div>'
        shot(R_,h,f'{OUT}/{gk}_{on+1}.png')
R_.close();print('fine')
