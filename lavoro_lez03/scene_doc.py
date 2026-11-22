# Scene con il prof: slide a card (finestre da 3), opere grandi con viste diverse; tagli sulle frasi intere, pause >2,5 s ridotte
import sys;sys.path.insert(0,'/home/user/Lezioni/lavoro_lez03')
from sorgente import *
import dati,lib,montaggio as M
SRC='/tmp/w/src/LEZIONE 3 IL REALISMO.mp4'
def K(t,**kw):return boundary_near(t,**kw)
IMGKW={'crystal':4,'parigi':5,'galleria':7,'opera':9,'pedrocchino':10,'mole':10,'spigolatrici':13,'spaccapietre':14,'atelier':15,'vagone':17,'rotonda':18,'invedetta':19,'toeletta':21}
TITOLI_IMG={'crystal':dati.TIT[3],'parigi':dati.TIT[3],'galleria':dati.TIT[6],'opera':dati.TIT[8],'pedrocchino':dati.TIT[8],'mole':dati.TIT[8],
 'spigolatrici':dati.TIT[12],'spaccapietre':dati.TIT[12],'atelier':dati.TIT[12],'vagone':dati.TIT[16],'rotonda':dati.TIT[18],'invedetta':dati.TIT[18],'toeletta':dati.TIT[20]}
VISTE={'crystal':[None,(0.1,0.3,0.95,0.85)],'spigolatrici':[None,(0.0,0.12,0.8,0.95)],'toeletta':[None,(0,0,0.6,1),(0.4,0,1,1)],
 'opera':[None,(0.3,0.0,1,0.62),(0,0.35,0.8,1)],'mole':[None,(0.2,0,0.8,0.5),(0,0.45,1,1)],'spaccapietre':[None,(0,0.1,0.55,1),(0.45,0.0,1,0.9)],
 'atelier':[None,(0.15,0.2,0.75,1)],'parigi':[None,(0.25,0.25,0.75,0.8)],'vagone':[None],'rotonda':[None],'invedetta':[None],'galleria':[None],'pedrocchino':[None]}
WIN={2:[[0,1,2],[3,4]],3:[[0,1,2],[3,4]],6:[[0,1,2],[3,4]],8:[[0,1,2],[3,4]],11:[[0,1,2],[3,4]],12:[[0,1,2],[3,4]],16:[[0,1],[2,3]],18:[[0,1]],20:[[0,1,2]]}
# (nome, tipo, pagina/immagine, tempo d'inizio sorgente in s)  -- confini poi spostati sulla frase più vicina
SCENE=[
 ('D1a','txt',2,None),
 ('D2a','txt',3,394),('D2b','img','crystal',675),('D2c','img','parigi',861),
 ('D3a','txt',6,1031),('D3b','img','galleria',1341),('D3c','txt',8,1406),('D3d','img','opera',1711),('D3e','img','pedrocchino',2018),('D3f','img','mole',2065),
 ('D4a','txt',11,2278),('D4b','txt',12,2489),('D4c','img','spigolatrici',2541),('D4d','txt',12,2724),('D4e','img','spaccapietre',2789),('D4f','img','atelier',2949),
 ('D5a','txt',16,3099),('D5b','img','vagone',3186),('D5c','txt',18,3279),('D5d','img','rotonda',3288),('D5e','img','invedetta',3374),('D5f','txt',20,3455),('D5g','img','toeletta',3538)]
def piano_scene(k_intro=None):
    """lista di dict: nome, tipo, id, k0, k1 (indici di frase)"""
    ks=[]
    for n,t,i,tt in SCENE:
        ks.append(K(tt) if tt else k_intro)
    ks.append(len(SENT))
    out=[]
    for j,(n,t,i,tt) in enumerate(SCENE):out.append(dict(nome=n,tipo=t,id=i,k0=ks[j],k1=ks[j+1]))
    return out
def out_frame(subs,t):
    """tempo sorgente t -> fotogramma nel pezzo (dopo i tagli delle pause)"""
    f=0
    for x,y in subs:
        if t<=x:return f
        if t<y:return f+round((t-x)*30)
        f+=round((y-x)*30)
    return f
PAGES={}
def page_of(key):
    if key not in PAGES:PAGES[key]=len(PAGES)+3   # 1 = copertina, 2 = argomenti
    return PAGES[key]
def build_scene(sc,render=True):
    a,b=piece_range(sc['k0'],sc['k1']);subs=tagli_pause(a,b)
    N=sum(round((y-x)*30) for x,y in subs);states=[];meta=dict(pagine=[])
    if sc['tipo']=='txt':
        p=sc['id'];cards=dati.cards(p);W_=WIN[p]
        ct=[c[1][0] for c in cards]
        tm=align_cards(ct,a,b)
        # card non trovate: distribuite in proporzione
        ts=[]
        for i,(t,s) in enumerate(tm):
            ts.append(t if (t is not None and s>0.35) else None)
        # monotonia e riempimento
        last=a
        for i in range(len(ts)):
            if ts[i] is None or ts[i]<last:
                nxt=next((x for x in ts[i+1:] if x is not None and x>last),b)
                ts[i]=last+(nxt-last)*0.5 if i>0 else last
            last=ts[i]
        # nelle scene corte con poche card interessate: solo le card che cadono nella scena
        sel=[i for i in range(len(cards)) if ts[i]<b-1.0 and (i==0 or ts[i]>a+0.2)]
        if sc['nome'] in('D4d',):sel=[2,3,4] if False else [i for i in range(2,5)]
        ev=[(a,sel[0],None)]+[(ts[i],i,i) for i in sel]
        # finestre
        def win_of(i):
            for wi,w in enumerate(W_):
                if i in w:return wi
        seq=[]
        for t,i,act in ev:
            seq.append((t,win_of(i),act))
        seq[0]=(a,seq[0][1],None)
        # se la prima card parte entro 1,5 s dall'inizio non serve lo stato senza accesa
        if len(seq)>1 and seq[1][0]-a<1.5:seq=seq[1:];seq[0]=(a,seq[0][1],seq[0][2])
        for si,(t,wi,act) in enumerate(seq):
            pg=page_of(('t',p,wi));meta['pagine'].append(pg)
            wc=[cards[i] for i in W_[wi]]
            img=lib.slide_cards(pg,dati.TIT[p],wc,None if act is None else W_[wi].index(act),dati.KW[p])
            t2=seq[si+1][0] if si+1<len(seq) else b
            states.append((M.save_png(img),max(1,out_frame(subs,t2)-out_frame(subs,t))))
        meta['card_t']=[(i,round(ts[i],2)) for i in sel]
    else:
        im=sc['id'];vs=VISTE[im];D=b-a
        nv=1 if D<150 else min(len(vs),int(D//100)+1)
        pg=page_of(('i',im));meta['pagine'].append(pg)
        vsel=vs[:nv]
        for vi,v in enumerate(vsel):
            t=a+D*vi/len(vsel);t2=a+D*(vi+1)/len(vsel)
            img=lib.slide_image(pg,TITOLI_IMG[im],im,dati.DID[im],dati.KW[IMGKW[im]],view=v)
            states.append((M.save_png(img),max(1,out_frame(subs,t2)-out_frame(subs,t))))
    if not render:return dict(sc=sc,subs=subs,states=states,N=N,meta=meta,a=a,b=b)
    pc=M.doc_piece(sc['nome'],SRC,subs,states)
    pc.update(meta=meta,a=a,b=b,topic=sc['nome'][1]);return pc
