import sys,os,json,re,math
sys.path.insert(0,'/tmp/claude-0/w/prod')
from eng import *
from lib import *
from slides import pages,card
from content import *
import content as C
P=pages();REN=Ren()
PAGES={};
def pg(key):
    if key not in PAGES:PAGES[key]=len(PAGES)+2
    return PAGES[key]
CARDS={k:[card(x) for x in v[1:]] for k,v in P.items() if k in C.PACK}
def st_png(key,arg):
    if key[0]=='C':
        _,p,sub,lit=key;idx=C.PACK[p][sub];cs=[CARDS[p][i] for i in idx];kw=C.KW.get((p,idx[lit]),[])
        t=P[p][0];top=370 if len(t)>42 else 304
        return REN.shot(slide_cards(C.LAB[arg-1],t,cs,lit,kw,pg(key),top=top))
    n=key[1];t,fs,cap,kw=C.IMG[n]
    imgs=[C.IM+f+'.png' for f in fs]
    return REN.shot(slide_image(C.LAB[arg-1],t,imgs,pg(key),cap,kw,top=304 if len(t)<40 else 304),css='.img img{max-width:%s}'%('49%' if len(imgs)>1 else '100%'))
ITEMS=[]
def add(it):ITEMS.append(it);return it
def secs(s):return math.ceil(s*FPS)
def kore(it,name,t,gain=1.0):it.audio.append((t,vox(name),gain))
def jingle(it,name,t,gain=0.8):it.audio.append((t,K+f'suoni/{name}.wav',gain))
def piece_prof(name,a,b,states,arg,bg=None,note=''):
    iv,good=keep(a,b);fr=frames_ranges(iv);tot=sum(n for _,n in fr)
    it=Item(name,'prof');it.fr=fr;it.nf=tot+24;it.src_a=a;it.src_b=b;it.good=good
    # mappa tempo sorgente -> tempo di uscita
    cum=0;mp=[]
    for (s,n) in fr:mp.append((s,s+n/FPS,cum));cum+=n/FPS
    def out_t(t):
        for s,e,c in mp:
            if t<=e:return c+max(0,t-s)
        return cum
    sts=[]
    for (t,key) in states:
        k=key if isinstance(key,tuple) else key
        sts.append((0.0 if not sts else out_t(t)+0.4,key))
    it.states=[(t,bg if bg else st_png(k,arg)) for t,k in sts]
    it.keys=[k for _,k in sts];it.name_lst=f'{W}/seq/{name}.bg.txt'
    # lista dei fondi (durate in fotogrammi)
    f0=[round(t*FPS) for t,_ in it.states]+[it.nf];L=[]
    for i,(t,p) in enumerate(it.states):
        n=f0[i+1]-f0[i]
        if n>0:L.append(f"file '{p}'\nduration {n/FPS:.6f}")
    L.append(f"file '{it.states[-1][1]}'");os.makedirs(W+'/seq',exist_ok=True);open(it.name_lst,'w').write('\n'.join(L))
    it.meta={'a':a,'b':b,'dur':tot/FPS,'ranges':fr}
    return add(it)
def voiced(name,render,vname,extra=0.8,lead=0.5):
    d=dur(vox(vname));it=Item(name);it.nf=secs(lead+d+extra);kore(it,vname,lead);it.vd=d;return it
def build():
    arg_it={}
    # 1 sigla
    it=Item('SIGLA','clip');it.src=K+'sigle/Sigla_Storia_arte_15s.mp4';it.nf=450;add(it)
    # 2 copertina + benvenuto
    it=voiced('COPERTINA',None,'BENVENUTO',1.0);it.states=[(0,REN.shot(cover(1,False)))];add(it)
    # 3 introduzione del prof sulla copertina (riquadro solo ora)
    piece_prof('INTRO',1.16,168.3,[(1.16,'x')],0,bg=REN.shot(cover(1,True)))
    # 4 argomenti
    st=sent_times('ARGOMENTI');it=voiced('ARGOMENTI',None,'ARGOMENTI',1.2)
    lit=[(0.0,-1)]+[(0.5+st[k+1][1],k) for k in range(4)]
    it.states=[(t,REN.shot(argomenti_card(2,l))) for t,l in lit];add(it)
    # argomenti
    A=[
     [('A1a',169.4,239.1,[(169.4,('I','vittoria'))]),('A1b',239.8,299.1,[(239.8,('C',3,0,0))]),('A1c',299.6,364.9,[(299.6,('C',3,0,0))]),
      ('A1d',370.1,484.2,[(370.1,('C',3,0,0)),(384.9,('C',3,0,1)),(405.2,('C',3,1,0))]),('A1e',484.5,556.7,[(484.5,('I','vittoria'))]),
      ('AP','A1_APPROF'),
      ('A1f',557.5,715.1,[(557.5,('I','vittoria')),(567.0,('I','conc_dopo'))]),('AP','A1B_APPROF'),
      ('A1g',717.4,826.0,[(717.4,('I','conc_dopo')),(738.3,('I','conc_2'))])],
     [('A2a',827.6,942.3,[(827.6,('C',11,0,0)),(888.8,('C',12,1,0))]),('A2b',943.6,1032.0,[(943.6,('C',11,0,0)),(996.5,('C',11,0,1)),(1011.0,('C',11,1,0))]),
      ('A2c',1033.2,1123.4,[(1033.2,('I','casa_facciata'))]),('A2d',1123.8,1184.5,[(1123.8,('I','casa_pianta')),(1167.7,('I','casa_int'))]),('AP','A2_APPROF'),
      ('A2e',1185.5,1245.7,[(1185.5,('C',12,0,0))]),('A2f',1246.1,1302.7,[(1246.1,('C',12,1,0)),(1269.0,('I','casa_int')),(1279.2,('I','palazzo'))]),
      ('A2g',1303.9,1384.4,[(1303.9,('C',12,0,1)),(1342.2,('I','e42'))]),('A2h',1385.5,1435.0,[(1385.5,('I','palazzo'))]),('AP','A2B_APPROF'),
      ('A2i',1436.1,1554.7,[(1436.1,('I','palazzo')),(1480.4,('C',12,1,1))]),('MAP','arch')],
     [('A3a',1559.0,1628.0,[(1559.0,('C',5,0,0))]),('A3b',1629.1,1680.4,[(1629.1,('C',5,0,1)),(1661.4,('C',5,1,0))]),
      ('A3c',1681.8,1825.7,[(1681.8,('I','canto'))]),('AP','A3_APPROF'),
      ('A3e',1828.5,1927.7,[(1828.5,('C',7,0,0)),(1845.7,('I','muse'))]),('AP','A3B_APPROF'),
      ('A3f',1928.5,1974.5,[(1928.5,('I','muse'))]),
      ('A3g',1977.1,2101.6,[(1977.1,('C',7,0,1)),(1998.6,('I','carra'))]),('AP','A3C_APPROF'),
      ('A3h',2102.0,2183.0,[(2102.0,('C',7,1,0)),(2109.7,('I','morandi'))]),('MAP','meta')],
     [('A4a',2184.2,2276.9,[(2184.2,('C',10,0,0)),(2237.6,('C',10,0,1))]),('AP','A4_APPROF'),
      ('A4b',2278.6,2353.5,[(2278.6,('C',10,1,0))])]]
    for ai,seq in enumerate(A,1):
        # titolo argomento
        it=Item(f'T{ai}');it.nf=secs(4.0);jingle(it,'titolo',0.4)
        t,chips=C.ARG[ai-1]
        it.states=[(0,REN.shot(titolo_card(ai,4,t,chips,pg(('T',ai)),prog=0.0))),(0.4,REN.shot(titolo_card(ai,4,t,chips,pg(('T',ai)),prog=0.35))),(0.5,REN.shot(titolo_card(ai,4,t,chips,pg(('T',ai)),prog=0.7))),(0.6,REN.shot(titolo_card(ai,4,t,chips,pg(('T',ai)),prog=1.0)))];add(it)
        for e in seq:
            if e[0]=='AP':add(approf(e[1],ai))
            elif e[0]=='MAP':add(mappa_item(e[1],ai))
            else:piece_prof(e[0],e[1],e[2],e[3],ai)
        add(pillola(ai));add(quizcard(ai))
    add(glossario());add(riepilogo());add(mappa_finale());add(verifica())
    it=Item('FINALE','clip');it.src=K+'sigle/Sigla_finale_5s_con_avviso_diritti.mp4';it.nf=150;add(it)
    for it in compiti():add(it)
APPR={'A1_APPROF':("Piazza della Vittoria",['vittoria']),'A1B_APPROF':("Via della Conciliazione",['conc_prima','conc_dopo']),
 'A2_APPROF':("La Casa del Fascio di Como",['casa_facciata','casa_pianta']),'A2B_APPROF':("L'EUR e il Colosseo quadrato",['palazzo','e42']),
 'A3_APPROF':("Canto d'amore",['canto']),'A3B_APPROF':("Le muse inquietanti",['muse']),'A3C_APPROF':("Carrà e Morandi",['carra','morandi']),
 'A4_APPROF':("Il Novecento italiano e Corrente",[])}
def approf(vn,ai):
    st=sent_times(vn);title,imgs=APPR[vn];d=dur(vox(vn));it=Item(vn);it.nf=secs(0.5+d+0.8);kore(it,vn,0.5);n=len(st)
    paths=[C.IM+i+'.png' for i in imgs]
    for k,(s,t0,t1) in enumerate(st):
        scr=digits(s)
        if not imgs:
            html=approf_card('Approfondimento',title,[],scr,pg(('AP',vn)),k+1,n).replace('<div class="img" style="left:80px;top:270px;width:760px;height:690px;display:flex"></div>','<div style="position:absolute;left:80px;top:290px;width:760px">'+''.join(f'<span class="chip" style="display:inline-block;margin:0 10px 12px 0;padding:10px 20px;border-radius:999px;background:#EAF1FB;border:2px solid #BFD3EE;font:700 30px Figtree">{x}</span>' for x in ['Novecento Italiano','1922','Margherita Sarfatti','Mario Sironi','Arturo Martini','Felice Casorati','Corrente','Scuola di via Cavour'])+'</div>')
        else:html=approf_card('Approfondimento',title,paths,scr,pg(('AP',vn)),k+1,n)
        it.states.append((0 if k==0 else max(0.0,0.5+t0-0.15),REN.shot(html)))
    return it
def mappa_item(mk,ai):
    M=C.MAPPE[mk];vn=M['voce'];d=dur(vox(vn));st=sent_times(vn);ref=TESTI[vn].split()
    import asr;T=asr.align(ref,voxwords(vn))
    def idx(phrase):
        w=phrase.split()
        for i in range(len(ref)-len(w)+1):
            if [x.strip('.,:?').lower() for x in ref[i:i+len(w)]]==[x.strip('.,:?').lower() for x in w]:return i
        raise KeyError(phrase)
    steps=[(bid,T[idx(ph)]) for bid,ph in M['passi']]
    it=Item('MAPPA_'+mk.upper());hold=4.0;tl=st[-1][1];it.nf=secs(0.5+tl+hold+0.4);kore(it,vn,0.5)
    shown=[];sts=[(0.0,REN.shot(mappa(M['titolo'],M['boxes'],M['arrows'],[],None),MAPCSS))]
    steps=[(bid,t0) for bid,t0 in steps]
    for k,(bid,t0) in enumerate(steps):
        shown=shown+[bid];t=0.5+t0-0.2
        sts.append((max(0.0,t),REN.shot(mappa(M['titolo'],M['boxes'],M['arrows'],list(shown),bid),MAPCSS)))
    tend=0.5+tl-0.05
    sts.append((tend,REN.shot(mappa(M['titolo'],M['boxes'],M['arrows'],list(shown),None),MAPCSS)))
    it.states=sts;it.meta={'passi':[(b,round(0.5+t,2)) for b,t in steps]};return it
def pillola(ai):
    vn=f'PIL{ai}';st=sent_times(vn);d=dur(vox(vn));title=C.ARG[ai-1][0]
    lines=[digits(s) for s,_,_ in st[1:]];lead=3.6;it=Item(f'PIL{ai}');it.nf=secs(lead+d+1.0);jingle(it,'repaso',0.4);kore(it,vn,lead)
    it.states=[(0,REN.shot(ripasso_card(title,lines,-1,pg(('P',ai)),prog=0.0))),(0.5,REN.shot(ripasso_card(title,lines,-1,pg(('P',ai)),prog=1.0)))]
    for k in range(len(lines)):it.states.append((lead+st[k+1][1]-0.1,REN.shot(ripasso_card(title,lines,k,pg(('P',ai))))))
    return it
def quizcard(ai):
    it=Item(f'Q{ai}');it.nf=secs(5.0);jingle(it,'quiz',0.5,1.0);t=C.QUIZ[f'Q{ai}'][0].split(' · ',1)[1]
    it.states=[(0,REN.shot(quiz_card(ai,t,pg(('Q',ai)),prog=0.0))),(0.3,REN.shot(quiz_card(ai,t,pg(('Q',ai)),prog=1.0)))];return it
def listcard_item(name,vn,kick,title,intro=1,lead=0.5,fs=34):
    st=sent_times(vn);d=dur(vox(vn));lines=[digits(s) for s,_,_ in st[intro:]];it=Item(name);it.nf=secs(lead+d+1.0);kore(it,vn,lead)
    pgn=pg((name,))
    it.states=[(0,REN.shot(list_card(kick,title,lines,-1,pgn,fs)))]
    for k in range(len(lines)):it.states.append((lead+st[k+intro][1]-0.1,REN.shot(list_card(kick,title,lines,k,pgn,fs))))
    return it
def glossario():return listcard_item('GLOSSARIO','GLOSSARIO','GLOSSARIO ANIMATO','Glossario',1,0.5,34)
def riepilogo():return listcard_item('RIEPILOGO','RIEPILOGO',"STORIA DELL'ARTE V",'RIEPILOGO <span style="color:#FFE600">FINALE</span>',1,0.5,34)
def mappa_finale():
    vn='MAPPA_FINALE';d=dur(vox(vn));st=sent_times(vn);it=Item('MAPPA_FINALE');it.nf=secs(0.5+d+1.0);kore(it,vn,0.5)
    Mm=C.MAPPE['meta'];Ma=C.MAPPE['arch']
    f=lambda M:REN.shot(mappa(M['titolo'],M['boxes'],M['arrows'],[b[0] for b in M['boxes']],None),MAPCSS)
    it.states=[(0,f(Mm)),(0.5+st[2][1]-0.1,f(Ma))];return it
def verifica():
    vn='VERIFICA';d=dur(vox(vn));it=Item('VERIFICA');it.nf=secs(0.5+d+1.2);jingle(it,'quiz',0.5,1.0);kore(it,vn,3.6 if False else 0.5+0.0+3.0)
    it.nf=secs(3.5+d+1.0)
    html=dark_scene('v',pg(('V',)),'<div class="big" style="top:300px"><div class="kick">PROVA FINALE</div><h1>Verifica di sbarramento</h1><h2>10 domande · per continuare serve almeno l\'80%</h2></div><div class="ghost" style="font-size:420px">?</div>')
    it.states=[(0,REN.shot(html))];return it
def compiti():
    out=[];vn='COMPITI';txt=TESTI[vn];ref=txt.split();import asr;T=asr.align(ref,voxwords(vn));d=dur(vox(vn))
    def widx(w):return next(i for i,x in enumerate(ref) if x==w)
    marks=[('Primo.',widx('Primo.')),('Secondo.',widx('Secondo.')),('Terzo.',widx('Terzo.')),('Quarto.',widx('Quarto.')),('Svolgi',widx('Svolgi'))]
    it=Item('COMPITI_INTRO');it.nf=secs(3.6);jingle(it,'titolo',0.4);it.states=[(0,REN.shot(compiti_intro(pg(('CI',)))))];out.append(it)
    it=Item('COMPITI');lead=0.5;it.nf=secs(lead+d+1.2);kore(it,vn,lead)
    texts=[]
    for k in range(4):
        a=marks[k][1]+1;b=marks[k+1][1];texts.append(digits(' '.join(ref[a:b])))
    sts=[]
    for k in range(4):
        t0=0.0 if k==0 else lead+T[marks[k][1]]-0.15
        sts.append((t0,REN.shot(compito_card(f'Compito {k+1} di 4',texts[k],pg(('CP',k)),fs=40))))
    sts.append((lead+T[marks[4][1]]-0.15,REN.shot(head('Compiti','Ora tocca a te',pg(('CP',9)))+'<div class="cards" style="top:300px;width:1760px"><div class="card lit" style="font-size:44px;opacity:1"><b>Svolgi i compiti qui sotto e premi Consegna:</b> arrivano al docente nel tuo quaderno dei compiti.</div></div>')))
    it.states=sts;out.append(it);return out
if __name__=='__main__':
    build()
    json.dump([dict(name=i.name,kind=i.kind,nf=i.nf,meta=i.meta) for i in ITEMS],open(W+'/items.json','w'),indent=0,default=str)
    print(len(ITEMS),'elementi;',round(sum(i.nf for i in ITEMS)/FPS/60,1),'min (senza dissolvenze)')
    REN.close()
