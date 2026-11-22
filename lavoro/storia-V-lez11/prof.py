import sys,os,json,hashlib,subprocess,shutil
sys.path.insert(0,'/home/user/work/build')
from L import *
from slides import *
from PIL import Image
ORIG=W+'/orig/LEZIONE 11 L_URSS DI STALIN (1924-1939).mp4'
G=lambda s:s.replace('URSS','URSS (Unione delle Repubbliche Socialiste Sovietiche)')
PAGES={
 'p3':dict(kick="01 · L'ascesa di Stalin",title="L'ascesa di Stalin e il controllo del partito",
  cards=["Il contesto (metà anni Venti): dopo la morte di Lenin nel 1924, si apre una dura lotta per la successione alla guida del Partito Comunista dell'Unione Sovietica (PCUS).",
  "La posizione di «sinistra»: guidata da Lev Trockij, critica la concentrazione del potere nel partito e difende l'idea della «rivoluzione permanente» come necessaria per la sopravvivenza del socialismo.",
  "La posizione di «destra»: guidata da Nikolaj Bucharin, favorevole alla Nuova politica economica (NEP), alla liberalizzazione agricola e a uno sviluppo economico pacifico e graduale.",
  "La strategia di Stalin: si inserisce nello scontro teorizzando il «socialismo in un solo paese» (consolidare la rivoluzione nella sola URSS, cioè Unione delle Repubbliche Socialiste Sovietiche, prima di esportarla) ed emerge come leader supremo eliminando politicamente tutti gli oppositori."],
  kws=["Morte di Lenin","Rivoluzione permanente","Nuova politica economica","Socialismo in un solo paese"]),
 'p4':dict(kick="02 · La grande svolta e i piani quinquennali",title="La «grande svolta» e i piani quinquennali",
  cards=["La pianificazione dell'economia: nel 1929 Stalin avvia la «grande svolta», trasformando l'URSS (Unione delle Repubbliche Socialiste Sovietiche) da paese agricolo a grande potenza industriale attraverso un'economia totalmente pianificata dallo Stato.",
  "I piani quinquennali: strumenti che fissavano in anticipo gli obiettivi produttivi da raggiungere in cinque anni, concentrandosi in particolare sull'industria pesante, sugli armamenti e sulle infrastrutture.",
  "I risultati industriali: nonostante i costi umani e l'imposizione di una rigida disciplina di fabbrica, la produzione industriale cresce in modo straordinario e la disoccupazione scompare quasi completamente."],
  kws=["Grande svolta","Piani quinquennali","Industria pesante"]),
 'p5':dict(kick="03 · La collettivizzazione e la carestia",title="La collettivizzazione forzata e la carestia",
  cards=["La fine delle proprietà private: lo Stato avvia la collettivizzazione forzata delle campagne, requisendo le terre per creare grandi aziende pubbliche (sovchoz) o cooperative (kolchoz).",
  "La repressione dei kulaki: i contadini benestanti (kulaki) che si oppongono alla collettivizzazione vengono perseguitati, deportati o eliminati fisicamente («dekulakizzazione»).",
  "La carestia del 1932-1933: le requisizioni forzate di grano per finanziare l'industrializzazione provocano una catastrofica carestia (in particolare in Ucraina, dove viene chiamata Holodomor), causando milioni di morti."],
  kws=["Collettivizzazione forzata","Kulaki","Holodomor"]),
 'p6':dict(kick="04 · Il totalitarismo e il Grande Terrore",title="Il totalitarismo staliniano e il «Grande Terrore»",
  cards=["Accentramento del potere: Stalin instaura una dittatura personale, eliminando la separazione tra gli organi del partito e quelli dello Stato.",
  "Le «grandi purghe» (1936-1938): una massiccia campagna di epurazione interna per eliminare ogni potenziale oppositore nel partito, nell'esercito e nella società.",
  "I processi pubblici e il Gulag: molti storici dirigenti bolscevichi vengono condannati a morte in tribunale dopo confessioni estorte con la forza; milioni di cittadini comuni finiscono nei campi di concentramento (Gulag) come lavoratori forzati.",
  "I pilastri del regime: il controllo assoluto della popolazione viene esercitato tramite la polizia segreta, il sospetto diffuso, la censura della cultura e la propaganda."],
  kws=["Dittatura personale","Grandi purghe","Gulag","Polizia segreta"]),
 'p7':dict(kick="05 · La società staliniana",title="La società staliniana: propaganda, giovani e donne",
  cards=["Il culto della personalità: la propaganda esalta Stalin come leader infallibile e «piccolo padre dei popoli», imponendo il realismo socialista come unico stile artistico ammesso.",
  "L'indottrinamento dei giovani: il controllo inizia fin dall'infanzia attraverso la scuola e organizzazioni di partito come il Komsomol (l'organizzazione giovanile comunista), volte a creare cittadini obbedienti.",
  "Il mito del lavoro (Stachanovismo): nasce il mito del minatore Aleksej Stachanov per incentivare i lavoratori a sacrificarsi e superare i record di produzione.",
  "Il cambio di rotta sui diritti femminili: dopo le riforme degli anni Venti (voto, divorzio, aborto), gli anni Trenta vedono un ritorno a modelli tradizionali; l'aborto diventa illegale e lo Stato promuove la natalità, pur celebrando le donne come «eroine del lavoro» nell'industria."],
  kws=["Culto della personalità","Komsomol","Stachanovismo","Diritti femminili"]),
 'p8':dict(kick="06 · La politica estera e le relazioni internazionali",title="La politica estera e le relazioni internazionali",
  cards=["Uscita dall'isolamento: negli anni Venti l'Unione Sovietica ristabilisce relazioni diplomatiche con le potenze occidentali ed entra nella Società delle Nazioni nel 1934.",
  "La strategia del «Fronte unito»: per contrastare l'ascesa del fascismo e del nazismo, il Comintern (l'Internazionale comunista) promuove l'alleanza tra comunisti, socialisti e forze democratiche (come nella guerra civile spagnola a sostegno della Repubblica).",
  "Il Patto Molotov-Ribbentrop: nell'agosto del 1939, con una svolta improvvisa, l'URSS (Unione delle Repubbliche Socialiste Sovietiche) firma un patto di non aggressione con la Germania nazista di Hitler, che include un accordo segreto per la spartizione dell'Europa orientale."],
  kws=["Società delle Nazioni","Fronte unito","Patto Molotov-Ribbentrop"]),
}
# clip: (id, orig_a, orig_b, [(t_orig,page,active)])
EV={
 'T1':(57.6,357.35,[(57.6,'p3',None),(64.1,'p3',1),(150.9,'p3',2),(217.5,'p3',3),(256.0,'p3',4)]),
 'T2':(357.35,471.7,[(357.35,'p4',None),(360.2,'p4',1),(408.5,'p4',2)]),
 'T3':(471.7,871.3,[(471.7,'p5',None),(472.4,'p5',1),(531.3,'p5',2),(604.0,'p5',3),(765.4,'p4',3),]),
 'T4':(871.3,1013.8,[(871.3,'p6',3),(896.4,'p6',2),(922.8,'p6',3),(962.4,'p6',4),(982.2,'p6',1)]),
 'T5':(1013.8,1145.55,[(1013.8,'p7',1),(1023.0,'p7',2),(1062.6,'p7',1),(1084.8,'p7',3),(1087.8,'p7',4)]),
 'T6':(1145.55,1506.13,[(1145.55,'p8',None),(1161.0,'p8',1),(1183.8,'p8',2),(1275.3,'p8',3)]),
}
SUBCLIPS=[('T1',57.6,357.35),('T2',357.35,471.7),('T3',471.7,871.3),('T4',871.3,1013.8),('T5',1013.8,1145.55),
          ('T6a',1145.55,1322.3),('T6b',1322.3,1413.8),('T6c',1413.8,1506.13)]
def states_for(key,a,b):
    ta,tb,ev=EV[key[:2]]
    out=[]
    cur=None;winmemo={}
    for i,(t,pg,act) in enumerate(ev):
        t1=ev[i+1][0] if i+1<len(ev) else tb
        s,e=max(t,a),min(t1,b)
        if e<=s: continue
        out.append((s,e,pg,act))
    return out
_meas={}
def get_meas(r,pg):
    if pg not in _meas:
        P=PAGES[pg];_meas[pg]=measure(r,P['kick'],P['title'],P['cards'],P.get('prof',True))
    return _meas[pg]
def windows(r):
    """finestra per ogni evento in ordine globale (stato persistente per pagina)"""
    wins={};cur={}
    for key,(ta,tb,ev) in EV.items():
        for (t,pg,act) in ev:
            hs,cy=get_meas(r,pg)
            if act is None:
                w=cur.get(pg) or choose_window(hs,cy,1,None) if False else None
                # senza evidenza: finestra che contiene le prime card che entrano
                n=len(hs);w=[]
                for i in range(1,n+1):
                    if sum(hs[j-1] for j in w+[i])+16*len(w)<=960-cy and len(w)<3: w.append(i)
                    else: break
                if pg=='p4' and key=='T3': w=[2,3]
            else:
                w=choose_window(hs,cy,act,cur.get(pg))
            cur[pg]=w;wins[(key,t)]=w
    return wins
def render_state(r,pg,win,act,out):
    if os.path.exists(out): return
    P=PAGES[pg]
    kwa=act
    h,_=frame(P['kick'],P['title'],P['cards'],win,act,P['kws'],kwa,0)
    r.shot(h,out)
def clip_seq(r,wins,sub,a,b,pagenum):
    key=sub[:2];ta,tb,ev=EV[key]
    seq=[]
    evs=[(t,pg,act) for (t,pg,act) in ev]
    for i,(t,pg,act) in enumerate(evs):
        t1=evs[i+1][0] if i+1<len(evs) else tb
        s,e=max(t,a),min(t1,b)
        if e<=s: continue
        w=wins[(key,t)]
        pn=pagenum[(pg,tuple(w))]
        png=f'{B}/st/{pg}_{"".join(map(str,w))}_{act}_{pn}.png'
        os.makedirs(B+'/st',exist_ok=True)
        P=PAGES[pg];h,_=frame(P['kick'],P['title'],P['cards'],w,act,P['kws'],act,pn,prof=P.get('prof',True))
        if not os.path.exists(png): r.shot(h,png)
        seq.append([s-a,e-a,png])
    return seq
def fade_list(seq,dur,fd=0.25,fps=30):
    """seq [[s,e,png]]; restituisce lista (png,durata) a 30 fps con dissolvenza tra stati"""
    N=int(round(dur*fps));frames=[None]*N
    for i,(s,e,png) in enumerate(seq):
        f0=int(round(s*fps));f1=N if i==len(seq)-1 else int(round(e*fps))
        for f in range(f0,min(f1,N)): frames[f]=png
        if i>0:
            prev=seq[i-1][2];nf=int(fd*fps)
            for k in range(nf):
                f=f0+k
                if f>=N: break
                key=hashlib.md5((prev+png+str(k)).encode()).hexdigest()[:10]
                fn=f'{B}/st/x_{key}.png'
                if not os.path.exists(fn):
                    Image.blend(Image.open(prev).convert('RGB'),Image.open(png).convert('RGB'),(k+1)/(nf+1)).save(fn)
                frames[f]=fn
    last=None
    for i in range(N):
        if frames[i] is None: frames[i]=last
        else: last=frames[i]
    first=next((f for f in frames if f),None)
    frames=[first if f is None else f for f in frames]
    out=[];
    for f in frames:
        if out and out[-1][0]==f: out[-1][1]+=1
        else: out.append([f,1])
    return out
def write_concat(frames,fn):
    with open(fn,'w') as fh:
        for p,n in frames: fh.write(f"file '{p}'\nduration {n/30:.6f}\n")
        fh.write(f"file '{frames[-1][0]}'\n")
MASK=B+'/mask412.png'
def make_mask():
    from PIL import ImageDraw
    im=Image.new('L',(412*4,309*4),0);d=ImageDraw.Draw(im);d.rounded_rectangle([0,0,412*4-1,309*4-1],radius=18*4,fill=255)
    im.resize((412,309),Image.LANCZOS).save(MASK)
def compose(concat,a,b,wavfile,out,cam=True):
    """video: sfondo da concat + webcam originale a..b; audio non incluso (wav separato)"""
    make_mask()
    d=b-a
    cmd=['ffmpeg','-y','-v','error','-f','concat','-safe','0','-i',concat,'-ss',f'{a:.3f}','-t',f'{d:.3f}','-i',ORIG,'-loop','1','-i',MASK,
     '-filter_complex',"[0:v]fps=30,format=yuv420p[bg];[1:v]crop=180:135:881:345,scale=412:309:flags=lanczos,eq=contrast=1.05:saturation=1.06:brightness=0.01,fps=30,format=rgba[c];[2:v]format=gray[m];[c][m]alphamerge[cam];[bg][cam]overlay=1428:148:shortest=1,format=yuv420p[v]",
     '-map','[v]','-frames:v',str(int(round(d*30))),'-c:v','libx264','-preset','veryfast','-crf','16','-pix_fmt','yuv420p',out]
    subprocess.run(cmd,check=True)
