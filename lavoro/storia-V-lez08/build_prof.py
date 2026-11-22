#!/usr/bin/env python3
# Costruisce i pezzi docente+slide (D0, D1..D7) con slide a finestra, card intere (40 px), bordo giallo sulla frase in corso.
import json, os, re, sys, subprocess
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from PIL import Image, ImageDraw, ImageFilter, ImageFont
import lib_slide as L
from plan import S, mappa, fine_frase
from profpiece import monta_prof, W, CACHE
CARDS=json.load(open(os.path.dirname(os.path.abspath(__file__))+'/cards.json'))
PIANO=json.load(open(os.path.dirname(os.path.abspath(__file__))+'/piano.json'))
TIT=['Il contesto del dopoguerra e la crisi del «Biennio rosso» (1919-1920)','Le elezioni del 1919 e il nuovo sistema di voto','La crisi di Fiume e il mito della «vittoria mutilata»','La nascita del fascismo e lo squadrismo agrario','Il ritorno di Giolitti e le elezioni del 1921','La Marcia su Roma e la conquista del potere','Il primo governo fascista e la svolta autoritaria','Il delitto Matteotti e il passaggio alla dittatura']
KW=[['deficit pubblico','inflazione','disoccupazione','consigli di fabbrica','massimalisti'],['suffragio universale maschile','sistema proporzionale','Partito Popolare Italiano','Francesco Saverio Nitti'],['vittoria mutilata','Fiume','d\'Annunzio','Patto di Londra'],['Fasci di combattimento','squadre d\'azione','camicia nera','spedizioni punitive'],['Blocchi Nazionali','Trattato di Rapallo','PNF = Partito Nazionale Fascista'],['Luigi Facta','quadrumviri','stato d\'assedio','Vittorio Emanuele III'],['discorso del bivacco','Gran consiglio','MVSN = Milizia volontaria per la sicurezza nazionale','Legge Acerbo'],['Lista nazionale','Matteotti','Secessione dell\'Aventino','3 gennaio 1925']]
NOMI={1:'Il Biennio rosso',2:'Vittoria mutilata, Fiume e le elezioni del 1919',3:'La nascita del fascismo',4:'Giolitti e le elezioni del 1921',5:'La Marcia su Roma',6:'Il primo governo fascista',7:'Il delitto Matteotti'}
SEZ={1:[0],2:[2,1],3:[3],4:[4],5:[5],6:[6],7:[7]}
# (tempo originale, sezione, card) : il prof comincia la frase della card
ATT={1:[(223.0,0,0),(292.0,0,2),(586.0,0,0),(600.0,0,1),(662.0,0,3),(711.0,0,4),(773.0,0,3),(881.0,0,4)],
 2:[(1010.0,2,0),(1066.0,2,1),(1093.0,2,3),(1170.4,2,0),(1194.0,2,2),(1258.5,2,2),(1330.0,2,4),(1408.0,1,0),(1495.0,1,1),(1542.0,1,3),(1638.0,1,2),(1677.0,1,4)],
 3:[(1780.0,3,0),(1943.0,3,1),(2123.0,3,2),(2253.0,3,3),(2424.0,3,4),(2459.0,3,3),(2516.0,3,4)],
 4:[(2606.0,4,0),(2615.0,4,1),(2674.0,4,2),(2825.0,4,4),(2869.0,4,2),(2957.0,4,3),(3153.0,4,4)],
 5:[(3177.1,5,0),(3306.0,5,1),(3353.0,5,2),(3398.0,5,3),(3809.0,5,4)],
 6:[(4003.7,6,0),(4179.0,6,1),(4308.0,6,2),(4361.0,6,3),(4448.0,6,4)],
 7:[(4831.2,7,0),(4846.0,7,1),(4892.0,7,2),(5051.0,7,3),(5176.0,7,4)]}
IMG={1:[(946.0,1010.0,'p3-001.jpg')],2:[(1202.0,1258.5,'p6-001.jpg')],3:[(2411.0,2449.5,'p8-001.jpg')],4:[(2838.0,2858.5,'p10-001.jpg')],6:[(4777.5,4829.0,'p14-001.jpg')],7:[]}
def tipo(c): return re.sub(r'"([^"]+)"',r'«\1»',c)
def cardtext(si,ci):
    return tipo(CARDS[si]['cards'][ci])
_m=ImageDraw.Draw(Image.new('RGB',(10,10)))
def altezza(txt): return len(L.wrap(_m,txt,L.font('Figtree-Medium.ttf',40),1300-90))*60+44
def finestre(si):
    """suddivisione delle card della sezione in finestre consecutive (max 3 card, entro lo spazio)"""
    n=len(CARDS[si]['cards']); H=[altezza(cardtext(si,i)) for i in range(n)]
    LIM=625; ws=[]; i=0
    while i<n:
        j=i; h=0
        while j<n and j-i<3 and h+H[j]+(22 if j>i else 0)<=LIM: h+=H[j]+(22 if j>i else 0); j+=1
        if j==i: j=i+1
        ws.append(list(range(i,j))); i=j
    for k,g in enumerate(ws):
        if len(g)==1:
            c=g[0]; ws[k]=[c-1,c] if c>0 else [c,c+1]
    return ws
def alternative(si,ci):
    """finestre scorrevoli che contengono la card ci (per spezzare le soste lunghe)"""
    n=len(CARDS[si]['cards']); H=[altezza(cardtext(si,i)) for i in range(n)]; out=[]
    for a in range(max(0,ci-2),ci+1):
        for b in range(a+1,min(n,a+3)+1):
            if a<=ci<b and sum(H[a:b])+22*(b-a-1)<=625 and b-a>=2: out.append(list(range(a,b)))
    return out
def img_pronta(nome):
    p=f'{CACHE}/img_{nome}.png'
    if not os.path.exists(p):
        im=Image.open(f'{W}/pimg/{nome}').convert('RGB'); sc=max(1,min(1300/im.width,640/im.height))
        im=im.resize((int(im.width*sc),int(im.height*sc)),Image.LANCZOS).filter(ImageFilter.UnsharpMask(radius=2,percent=90,threshold=2))
        im.save(p)
    return p
def render(si,top,win,attiva,pag,img=None):
    im=L.slide(TIT[si],f'{top:02d} · {NOMI[top]}',[cardtext(si,i) for i in win],(win.index(attiva) if attiva is not None else None),pag,KW[si]) if img is None else None
    if img is not None:
        im=L.slide(TIT[si],f'{top:02d} · {NOMI[top]}',[],None,pag,KW[si])
        pi=Image.open(img_pronta(img)); x=80+(1300-pi.width)//2; y=350+(625-pi.height)//2
        sh=Image.new('RGBA',im.size,(0,0,0,0)); ImageDraw.Draw(sh).rectangle((x,y+8,x+pi.width,y+pi.height+8),fill=(90,100,120,70)); sh=sh.filter(ImageFilter.GaussianBlur(14))
        im=Image.alpha_composite(im.convert('RGBA'),sh).convert('RGB'); im.paste(pi,(x,y))
    return im
def sent_start(t):
    """inizio del segmento (frase) più vicino a t entro ±3 s"""
    c=min(S,key=lambda s:abs(s['inizio']-t)); return c['inizio'] if abs(c['inizio']-t)<=3 else t
def stati_topic(top,pag0):
    P=PIANO[str(top)]; f=mappa(P['iv']); si_list=SEZ[top]
    ev=[]
    for t,si,ci in ATT[top]: ev.append((t,'att',si,ci))
    for a,b,nm in IMG.get(top,[]): ev.append((a,'img',nm,None)); ev.append((b,'fine_img',None,None))
    ev.sort(key=lambda e:e[0])
    t0=P['orig'][0]; stati=[]; pag=pag0-1; cur=None
    wins={si:finestre(si) for si in si_list}
    # stato iniziale: finestra della prima sezione senza evidenza (se la prima attivazione è tardi)
    def add(t_o,key,img,si,win,att):
        nonlocal pag,cur
        if cur is None or cur[0]!=(key,tuple(win) if win else None,si): pag+=1
        cur=((key,tuple(win) if win else None,si),)
        stati.append(dict(t=f(max(t_o,t0)),si=si,win=win,att=att,img=img,pag=pag,orig=t_o))
    first=ev[0]
    if first[0]>t0+3 and first[1]=='att':
        si=first[2]; w=[w for w in wins[si] if first[3] in w][0] if True else None
        w=wins[si][0]; add(t0,'c',None,si,w,None)
    lastsi=None; lastwin=None; lastatt=None
    for t,k,a,b in ev:
        if k=='att':
            si,ci=a,b; cand=[w for w in wins[si] if ci in w]
            w=lastwin if (lastsi==si and lastwin and ci in lastwin) else cand[0]
            add(t,'c',None,si,w,ci); lastsi,lastwin,lastatt=si,w,ci
        elif k=='img': add(t,'i',a,lastsi if lastsi is not None else si_list[0],None,None)
        elif k=='fine_img':
            si=lastsi; add(t,'c',None,si,lastwin,lastatt)
    # spezza le soste lunghe (>150 s) cambiando finestra a un inizio di frase
    fin=[]; 
    for k,s in enumerate(stati):
        t_end=stati[k+1]['t'] if k+1<len(stati) else f.durata
        fin.append(s)
        if s['img'] or s['att'] is None: continue
        cur_s=s; tt=s['t']
        while t_end-tt>150:
            tc=tt+130
            # cerca inizio di frase nell'originale a partire da tc (tempo pezzo -> originale approssimato)
            cand=[g for g in S if mappa(P['iv'])(g['inizio'])>=tc and g['inizio']>=P['orig'][0] and fine_frase(S[S.index(g)-1])] if True else []
            if not cand: break
            g=cand[0]; tn=mappa(P['iv'])(g['inizio'])
            if t_end-tn<20: break
            alts=[w for w in alternative(cur_s['si'],cur_s['att']) if w!=cur_s['win']]
            if not alts: break
            pag+=1; new=dict(cur_s); new.update(t=tn,win=alts[0],pag=pag); fin.append(new); cur_s=new; tt=tn
            # le pagine dopo questo cambiano numero: gestito dal chiamante rinumerando
    # rinumera le pagine in ordine
    out=[];lastkey=None;p=pag0-1
    for s in sorted([x for x in fin if x['t']<f.durata-0.5],key=lambda x:x['t']):
        key=(s['img'],tuple(s['win']) if s['win'] else None,s['si'])
        if key!=lastkey: p+=1; lastkey=key
        s['pag']=p; out.append(s)
    return out,p
def build(top,pag0,outdir):
    os.makedirs(outdir,exist_ok=True)
    st,pag=stati_topic(top,pag0); states=[]
    for k,s in enumerate(st):
        png=f'{outdir}/D{top}_{k:02d}.png'
        render(s['si'],top,s['win'],s['att'],s['pag'],s['img']).save(png)
        states.append((s['t'],png))
    # il primo stato comincia a 0
    states[0]=(0.0,states[0][1])
    dur=monta_prof(f'D{top}',PIANO[str(top)]['iv'],states,f'{outdir}/D{top}.mkv')
    json.dump([dict(t=s['t'],pag=s['pag'],att=s['att'],si=s['si'],img=s['img'],win=s['win'],orig=s['orig']) for s in st],open(f'{outdir}/D{top}_stati.json','w'),indent=1)
    return dur,pag
if __name__=='__main__':
    top=int(sys.argv[1]); pag0=int(sys.argv[2]); out=sys.argv[3]
    d,p=build(top,pag0,out); print('D%d'%top,'%.1f s'%d,'ultima pagina',p)
