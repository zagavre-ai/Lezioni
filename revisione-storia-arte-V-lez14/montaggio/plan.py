# Piano di montaggio della lezione 14: costruisce la sequenza (video + audio) e la timeline.
import sys,os,json,random,hashlib,numpy as np
sys.path.insert(0,'/tmp/w/build')
from engine import *
import tpl
from contents import *
import voci
TESTI=dict(voci.V)
trasc=json.load(open('/tmp/w/lav/trasc.json'));SEG=trasc['segmenti'] if isinstance(trasc,dict) else trasc
PROF=load_stereo(f'{B}/prof_clean.wav')   # mono duplicato
PROFM=PROF[:,0].copy()
# livello del docente: -16 LUFS sul parlato
import pyloudnorm as pyln
_m=pyln.Meter(SR);PROF_GAIN=10**((-16.0-_m.integrated_loudness(PROFM[:SR*600]))/20)
HTML={};PAGE=[0];TLN=TL();DISP=[]   # DISP: pagine per la dispensa (html senza prof)
def png(html):
    h=hashlib.md5(html.encode()).hexdigest()[:16];p=f'{B}/png/{h}.png'
    HTML[p]=html;return p
def newpage():PAGE[0]+=1;return PAGE[0]
def md5(s):return hashlib.md5(s.encode()).hexdigest()
IMGP=lambda k:f'{IMG}{k}.png'
LASTV=[None];VC=[]
def KOREV(n):
    LASTV[0]=n;return voice(n,TESTI)
def pv(a,v,L):
    place(a,v,L);VC.append((len(TLN.segs),LASTV[0],L))

# ---------- pezzi del docente ----------
GAPS=[(599.6,602.8),(1117.1,1120.5),(1614.0,1616.5)]   # pause > 2,2 s: tolta la parte centrale, ne restano ~1 s
def cuts():return [(a+0.5,b-0.5) for a,b in GAPS]
def piece_bounds(pz):
    a=pz['a']-0.15;b=pz['b']
    nxt=min([s['inizio'] for s in SEG if s['inizio']>b+0.01]+[b+1])
    e=b+min(0.6,max(0.15,nxt-b-0.2))
    return max(0,a),e
def states_for_piece(pz,pg):
    """lista di (t_inizio, png, pagina) per il docente; pg = funzione che da' un numero pagina"""
    st=[];n=pz['n'];kick=f'{n:02d} · {ARG[n-1]}'
    for blk in pz['blocks']:
        if blk[0]=='cards':
            _,tit,kws,cards=blk
            # impacchetta le card in schermate: max 3 e che entrino (630 px)
            scr=[];cur=[];h=0
            for t,c in cards:
                ch=tpl.card_h(c)
                if cur and (len(cur)>=3 or h+ch+22>600):scr.append(cur);cur=[];h=0
                cur.append((t,c));h+=ch+22
            if cur:scr.append(cur)
            for sc in scr:
                page=pg();texts=[c for _,c in sc]
                for i,(t,c) in enumerate(sc):
                    html,_=tpl.slide_text(kick,tit,texts,i,kws,page);st.append((t,png(html),page))
                DISP.append((tpl.slide_text(kick,tit,texts,None,kws,page,prof=False)[0].replace('opacity:.5','opacity:1'),page))
        else:
            _,tit,kws,imgs=blk
            for t,k,cap in imgs:
                page=pg();html=tpl.slide_image(kick,tit,IMGP(k),cap,kws,page);st.append((t,png(html),page))
                DISP.append((tpl.slide_image(kick,tit,IMGP(k),cap,kws,page,prof=False),page))
    return st
def prof_scene(name,a,b,states,xf=True,first_extra=None):
    """crea i segmenti 'prof' (atomi) per [a,b) secondi, con le pause lunghe accorciate"""
    f0=fr(a);f1=fr(b)
    # intervalli da togliere (in fotogrammi)
    rem=[(fr(c0),fr(c1)) for c0,c1 in cuts() if c0>=a and c1<=b]
    # confini degli stati
    bounds=sorted(set([f0]+[fr(t) for t,_,_ in states if f0<fr(t)<f1]+[x for r in rem for x in r]+[f1]))
    stt=sorted(states,key=lambda s:s[0])
    def png_at(f):
        cur=stt[0][1]
        for t,p,_ in stt:
            if fr(t)<=f:cur=p
        return cur
    atoms=[]
    for x0,x1 in zip(bounds[:-1],bounds[1:]):
        if any(r0<=x0 and x1<=r1 for r0,r1 in rem):continue
        atoms.append((x0,x1,png_at(x0)))
    aud=[]
    for x0,x1,_ in atoms:aud.append(PROF[x0*SPF:x1*SPF]*PROF_GAIN)
    A=np.concatenate(aud)
    k=int(0.015*SR);A[:k]*=np.linspace(0,1,k)[:,None];A[-k:]*=np.linspace(1,0,k)[:,None]
    n_tot=sum(x1-x0 for x0,x1,_ in atoms)
    # il pezzo e' un blocco unico per l'audio; i clip sono separati. dissolvenza solo alla fine del pezzo
    off=0;first=True
    for i,(x0,x1,p) in enumerate(atoms):
        n=x1-x0
        seg=TLN.add('prof',n,A[off*SPF:(off+n)*SPF],dict(k='prof',png=p,f0=x0),f'{name}' if first else f'{name}_{i}',xf=(xf and i==len(atoms)-1))
        first=False;off+=n
    return n_tot

def kore_scene(name,x,spec_frames,tail=0.9,lead=0.5,extra=None):
    pass

def sent_voice(n):return KOREV(n)

# ================= SEQUENZA =================
def build():
    pgs=newpage
    # 1 sigla
    tl=TLN
    sig=load_stereo(f'{KIT}/sigle/Sigla_Storia_arte_15s.mp4')
    tl.add('video',450,sig,dict(k='video',path=f'{KIT}/sigle/Sigla_Storia_arte_15s.mp4'),'SG')
    # 2 copertina con voce di benvenuto (nessun riquadro del docente)
    pg_cov=pgs()
    cov=png(tpl.copertina(TITOLO,ARG,pg_cov,prof=False))
    DISP.append((tpl.copertina(TITOLO,ARG,pg_cov,prof=False),pg_cov))
    v,starts,sents,prov=KOREV('BENVENUTO');d=len(v)/SR
    n=fr(0.6+d+0.9);a=np.zeros((n*SPF,2),'float32');pv(a,v,0.6);
    tl.add('still',n,a,dict(k='still',png=cov),'CO')
    # 3 copertina con il docente (introduzione, max 3 minuti)
    s0,e0=0.9,96.6
    p_cov=png(tpl.copertina(TITOLO,ARG,pg_cov,prof=True))
    prof_scene('D0',s0,e0,[(s0,p_cov,pg_cov)])
    # 4 slide degli argomenti (voce, nessun riquadro)
    pg_arg=pgs();v,starts,sents,prov=KOREV('ARGOMENTI')
    n=fr(0.6+len(v)/SR+1.0);a=np.zeros((n*SPF,2),'float32');pv(a,v,0.6)
    # sentence 0 e' l'introduzione; frasi 1..6 = argomenti
    frames=[];tt=0.0
    marks=[0.0]+[0.6+s-0.1 for s in starts[1:]]+[n/FPS]
    # primo stato: tutti spenti fino alla frase 1
    frames=[]
    idx=[None]+list(range(len(ARG)))
    for i in range(len(marks)-1):
        f_a=fr(marks[i]);f_b=fr(marks[i+1]) if i<len(marks)-2 else n
        act=idx[i] if i<len(idx) else None
        html=tpl.argomenti_slide(ARG,act,pg_arg);frames.append((png(html),max(1,f_b-f_a)))
    frames[-1]=(frames[-1][0],frames[-1][1]+ (n-sum(x for _,x in frames)))
    DISP.append((tpl.argomenti_slide(ARG,None,pg_arg),pg_arg))
    tl.add('seq',n,a,dict(k='seq',frames=frames),'AR')
    # 5 argomenti
    for pz in PEZZI:
        idn=pz['id'];n_=pz['n']
        # titolo + jingle
        pgt=pgs();tt=png(tpl.dark_title(n_,ARG[n_-1],pgt));DISP.append((tpl.dark_title(n_,ARG[n_-1],pgt),pgt))
        a=np.zeros((120*SPF,2),'float32');place(a,JING['titolo'],0.0,0.8)
        tl.add('still',120,a,dict(k='still',png=tt),idn)
        # docente
        a_,b_=piece_bounds(pz);st=states_for_piece(pz,pgs)
        prof_scene('D'+str(n_),a_,b_,st)
        # approfondimento
        approf(n_,pgs)
        # mappa del docente
        if idn=='T1':mappa_scene('M2',pgs,final=False)
        if idn=='T2':mappa_scene('M1',pgs,final=False)
        # pillola
        pill(n_,pgs)
        # quiz
        quiz(n_,pgs)
    # glossario
    glossario_scene(pgs)
    ripasso_scene(pgs)
    mappa_scene('M3',pgs,final=True)
    verifica_scene(pgs)
    # sigla finale
    sg=load_stereo(f'{KIT}/sigle/Sigla_finale_5s_con_avviso_diritti.mp4')
    tl.add('video',150,sg,dict(k='video',path=f'{KIT}/sigle/Sigla_finale_5s_con_avviso_diritti.mp4'),'FS')
    compiti_scene(pgs)
    return tl

def approf(n,pgs):
    key=f'APPR_{n}';v,starts,sents,prov=KOREV(key);tit,grp=APPROF[f'T{n}']
    pg=pgs();L=0.7;d=len(v)/SR;ntot=fr(L+d+1.0)
    a=np.zeros((ntot*SPF,2),'float32');pv(a,v,L)
    bullets=[g[1] for g in grp];imgs=[g[2] for g in grp];caps=[g[3] for g in grp]
    frames=[];gs=[g[0] for g in grp]
    times=[fr(L+starts[min(g,len(starts)-1)]-0.15) for g in gs]
    times[0]=0
    for i in range(len(grp)):
        f_a=times[i];f_b=times[i+1] if i+1<len(grp) else ntot
        # immagine mostrata: l'ultima disponibile finora
        im=None;cp=None
        for j in range(i,-1,-1):
            if imgs[j]:im=IMGP(imgs[j]);cp=caps[j];break
        frames.append((png(tpl.dark_approf(tit,bullets,i,im,cp,pg)),f_b-f_a))
    DISP.append((tpl.dark_approf(tit,bullets,len(grp)-1,im,cp,pg),pg))
    TLN.add('seq',ntot,a,dict(k='seq',frames=frames),f'A{n}')

def pill(n,pgs):
    key=f'PILL_{n}';v,starts,sents,prov=KOREV(key);lines=PILL[f'T{n}']
    pg=pgs();L=0.9;d=len(v)/SR;ntot=fr(L+d+1.0)
    a=np.zeros((ntot*SPF,2),'float32');place(a,JING['repaso'],0.0,0.8);pv(a,v,L)
    k=len(lines);st=[L+starts[min(i,len(starts)-1)] for i in range(k)]
    # le righe = frasi della voce; se sono di piu' o di meno, si assegnano in ordine
    frames=[];tm=[0]+[fr(st[i]-0.1) for i in range(1,k)]+[ntot]
    for i in range(k):
        frames.append((png(tpl.dark_lines('Ripasso',ARG[n-1],lines,i,pg,fs=40)),tm[i+1]-tm[i]))
    DISP.append((tpl.dark_lines('Ripasso',ARG[n-1],lines,k-1,pg,fs=40),pg))
    TLN.add('seq',ntot,a,dict(k='seq',frames=frames),f'PL{n}')

def quiz(n,pgs):
    v,starts,sents,prov=KOREV('QUIZ_INTRO');pg=pgs()
    L=1.4;ntot=fr(L+len(v)/SR+0.9);a=np.zeros((ntot*SPF,2),'float32')
    place(a,JING['quiz'],0.5,0.8);pv(a,v,L)
    p=png(tpl.quiz_card(n,pg));DISP.append((tpl.quiz_card(n,pg),pg))
    TLN.add('still',ntot,a,dict(k='still',png=p),f'Q{n}')

def mappa_scene(mk,pgs,final):
    M=MAPPE[mk];v,starts,sents,prov=KOREV(M['voce']);pg=pgs();L=0.7
    d=len(v)/SR;hold=4.0
    ntot=fr(L+d+0.5+hold);a=np.zeros((ntot*SPF,2),'float32');pv(a,v,L)
    place(a,JING['repaso'],L+d+0.4,0.5)   # copre i 4 secondi di mappa intera (nessun silenzio oltre 2,5 s)
    # passi: frase 0 = titolo (mappa vuota), poi un riquadro per frase
    shown=[];frames=[];order=M['order'];tm=[0]
    t_steps=[fr(L+starts[1+i]-0.1) for i in range(len(order))]
    # stato 0: solo titolo
    seqs=[(set(),None,0,t_steps[0])]
    for i,(b,ar) in enumerate(order):
        shown_i=set()
        for (bb,aa) in order[:i+1]:
            shown_i.add(bb)
            if aa:shown_i.add(aa)
        t_end=t_steps[i+1] if i+1<len(order) else fr(L+d+0.4)
        seqs.append((shown_i,b,t_steps[i],t_end))
    # finale: tutta la mappa ferma
    allb=set(M['boxes'])|set(M['arrows'])
    seqs.append((allb,None,fr(L+d+0.4),ntot))
    for sh_,hl,t0,t1 in seqs:
        frames.append((png(tpl.mappa(M['title'],M['boxes'],M['arrows'],sh_,hl,pg)),t1-t0))
    TLN.add('seq',ntot,a,dict(k='seq',frames=frames),'MF' if final else 'M'+mk[1])
    DISP.append((tpl.mappa(M['title'],M['boxes'],M['arrows'],allb,None,pg),pg))
    DISP.append(('MAPPA:'+mk,pg))

def glossario_scene(pgs):
    v,starts,sents,prov=KOREV('GLOSSARIO');pg=pgs();L=0.8;d=len(v)/SR;ntot=fr(L+d+1.2)
    a=np.zeros((ntot*SPF,2),'float32');place(a,JING['repaso'],0.0,0.7);pv(a,v,L)
    k=len(GLOSS);tm=[0]+[fr(L+starts[1+i]-0.1) for i in range(k)]+[ntot]
    # frase 0 = "Glossario." ; poi un termine per frase (alcune definizioni possono avere piu' frasi: si usa il primo inizio utile)
    frames=[(png(tpl.glossario(GLOSS,-1,pg)),tm[1]-tm[0])]
    for i in range(k):
        frames.append((png(tpl.glossario(GLOSS,i,pg)),tm[i+2]-tm[i+1]))
    DISP.append((tpl.glossario(GLOSS,k-1,pg),pg))
    TLN.add('seq',ntot,a,dict(k='seq',frames=frames),'GL')

def ripasso_scene(pgs):
    v,starts,sents,prov=KOREV('RIPASSO');pg=pgs();L=0.8;d=len(v)/SR;ntot=fr(L+d+1.2)
    a=np.zeros((ntot*SPF,2),'float32');place(a,JING['repaso'],0.0,0.7);pv(a,v,L)
    k=len(ARG);tm=[0]+[fr(L+starts[1+i]-0.1) for i in range(k)]+[ntot]
    lines=[f'{i+1}. {t}' for i,t in enumerate(ARG)]
    frames=[(png(tpl.dark_lines('Ripasso finale','Che cosa abbiamo visto',[],-1,pg,fs=40)),tm[1]-tm[0])]
    for i in range(k):
        frames.append((png(tpl.dark_lines('Ripasso finale','Che cosa abbiamo visto',lines,i,pg,fs=38)),tm[i+2]-tm[i+1]))
    DISP.append((tpl.dark_lines('Ripasso finale','Che cosa abbiamo visto',lines,k-1,pg,fs=38),pg))
    TLN.add('seq',ntot,a,dict(k='seq',frames=frames),'RF')

def verifica_scene(pgs):
    v,starts,sents,prov=KOREV('VERIFICA_INTRO');pg=pgs()
    L=1.4;ntot=fr(L+len(v)/SR+0.9);a=np.zeros((ntot*SPF,2),'float32')
    place(a,JING['quiz'],0.5,0.8);pv(a,v,L)
    html=tpl.dark_simple('Verifica finale','Verifica finale','Dieci domande su tutta la lezione. Per superarla serve almeno l\'80% di risposte giuste.',pg)
    p=png(html);DISP.append((html,pg))
    TLN.add('still',ntot,a,dict(k='still',png=p),'Q7')

def compiti_scene(pgs):
    # intro Compiti ~3,5 s con jingle
    pg=pgs();html=tpl.dark_simple('Compiti','Compiti','',pg);p=png(html);DISP.append((html,pg))
    a=np.zeros((105*SPF,2),'float32');place(a,JING['titolo'],0.0,0.8)
    TLN.add('still',105,a,dict(k='still',png=p),'CI')
    # compiti letti dalla voce
    v,starts,sents,prov=KOREV('COMPITI');pg=pgs();L=0.8;d=len(v)/SR;ntot=fr(L+d+1.4)
    a=np.zeros((ntot*SPF,2),'float32');pv(a,v,L)
    k=len(COMPITI);fin="Svolgi i compiti qui sotto e premi Consegna: arrivano al docente nel tuo quaderno dei compiti."
    # frasi: 0 'Compiti.'; per ogni compito: 'Compito uno.' + testo; ultima: frase finale (il testo puo' avere piu' frasi)
    # si accende il compito quando la voce dice «Compito N»
    idx=[i for i,s in enumerate(sents) if s.lower().startswith('compito ')]
    marks=[L+starts[i]-0.1 for i in idx]+[L+starts[-1]-0.1]
    tm=[0]+[fr(m) for m in marks]+[ntot]
    frames=[(png(tpl.compiti(COMPITI,-1,pg)),tm[1]-tm[0])]
    for i in range(k):
        t1=tm[i+2]
        frames.append((png(tpl.compiti(COMPITI,i,pg)),t1-tm[i+1]))
    frames.append((png(tpl.compiti(COMPITI,k-1,pg,finale=fin)),ntot-tm[k+1]))
    DISP.append((tpl.compiti(COMPITI,k-1,pg,finale=fin),pg))
    TLN.add('seq',ntot,a,dict(k='seq',frames=frames),'CP2',xf=False)
