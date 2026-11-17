import json,os,sys,hashlib,math,subprocess
sys.path.insert(0,'.')
from tpl import *
import tpl,data,plan,align
FPS=30
HT='html';os.makedirs(HT,exist_ok=True)
# ---- frame per blocco (vecchi) e nuovi ----
old=[(n,round((b-a)*FPS)) for n,a,b in plan.blocks]
TOTF=round(plan.TOT*FPS)
fix=sum(f for n,f in old)
for i,(n,f) in enumerate(old):
    if n=='COMP': old[i]=(n,f+(TOTF-fix))
oldf=dict(old)
DELTA=0
newf=dict(oldf)
core_old={k:round(plan.OLD_D[k][1]*FPS) for k in plan.DSEG}
core_new={k:round((b-a)*FPS) for k,(a,b) in plan.DSEG.items()}
for k in plan.DSEG:
    gap=15; newf[k]=core_new[k]+gap; DELTA+=core_old[k]-core_new[k]
import wave
RDUR={}
for blk,(rv,steps) in data.MAPS.items():
    w=wave.open(f'../voci/scambio/letteratura-V-lez12/vox/{rv}.wav');RDUR[blk]=w.getnframes()/w.getframerate()
    newf[blk]=round((RDUR[blk]+0.5+1.6)*FPS)
newf['AN13']-=30
for _k in range(1,6): newf[f'S{_k}']+=100
newf['FIN1']=210;newf['VER']=105;newf['CI1']=96;newf['COMP']=120
newf['AN15']=newf['AN15'];TOTN=sum(newf.values())
START={};c=0
for n,_ in old: START[n]=c;c+=newf[n]
# ---- registro pagine e stati ----
PAGES={};PG=[0]
def pg(key):
    if key not in PAGES: PG[0]+=1;PAGES[key]=PG[0]
    return PAGES[key]
STATES={}   # blocco -> [(frame_rel, htmlname)]
HTMLS={}
SLIDE_FINAL={}  # chiave pagina -> html (stato completo, per il PDF)
def reg(html):
    h=hashlib.md5(html.encode()).hexdigest()[:12]
    if h not in HTMLS: HTMLS[h]=html;open(f'{HT}/{h}.html','w').write(html)
    return h
def add(blk,t_s,html): STATES.setdefault(blk,[]).append((round(t_s*FPS),reg(html)))
PROF={}   # blocco D -> (orig_a, orig_b)

# ---- numerazione pagine nell'ordine del video ----
for _n,_a,_b in plan.blocks:
    if _n=='INTRO1': pg(('cover',))
    elif _n[0]=='T' and _n[1:].isdigit(): pg(('T',int(_n[1:])))
    elif _n in data.D_SLIDES:
        for _g in data.D_SLIDES[_n]: pg(('D',_n,_g[1][0]))
    elif _n in data.AN: pg(('AN',_n))
    elif _n in data.MAPS: pg(('MAP',_n))
    elif _n[0]=='S' and _n[1:].isdigit(): pg(('S',int(_n[1:])))
    elif _n[0]=='Q' and _n[1:].isdigit(): pg(('Q',int(_n[1:])))
    elif _n=='GL1': pg(('GL',))
    elif _n=='RF1': pg(('RF',))
    elif _n=='FIN1': pg(('FIN',))
    elif _n=='VER': pg(('VER',))
    elif _n=='CI1': pg(('CI',))
    elif _n=='COMP': pg(('COMP',))
PG_PRE=PG[0]
# ---- INTRO / D0 : copertina ----
cov=lambda prof,active=None:cover(data.ARGS,active,pg(('cover',)),prof=prof)
add('INTRO1',0,cov(False)); SLIDE_FINAL[pg(('cover',))]=cov('none')
add('D0',0,cov('tag'));PROF['D0']=plan.DSEG['D0']
add('D0',(core_new['D0']-14)/FPS,cov('tagonly'))
# ---- schede dei D ----
def cards_d(k):
    return None
import pptx_cards
CARDS=pptx_cards.CARDS
PORT={1:None,2:None,3:'../pic/s7.jpg',4:'../pic/s9.jpg',5:'../pic/s12.jpg'}
def dslide(Dk,arg,idxs,active,prof):
    items=[(CARDS[Dk][i]['lead'],CARDS[Dk][i]['text']) for i in idxs]
    act=None if active is None else idxs.index(active)
    first=idxs[0]
    key=('D',Dk,first)
    n=pg(key)
    html=content(data.TOP(arg),CARDS[Dk][first]['title'],items,act,n,prof=prof,port=PORT[arg])
    return key,html
for Dk,arg in (('D1',1),('D2',2),('D3',3),('D4',4),('D5',5)):
    a0,b0=plan.DSEG[Dk]; PROF[Dk]=(a0,b0)
    groups=data.D_SLIDES[Dk]
    anch=data.D_ANCH[Dk]
    def grp_of(t):
        g=groups[0]
        for gg in groups:
            if t>=gg[0]-1e-6: g=gg
        return g
    for i,(t,idx) in enumerate(anch):
        g=grp_of(t)
        if idx is not None and idx not in g[1]:
            # l'indice appartiene al gruppo successivo: sposta il gruppo
            for gg in groups:
                if idx in gg[1]: g=gg
        key,html=dslide(Dk,arg,g[1],idx,'tag')
        add(Dk,t-a0,html)
        # stato finale completo per il PDF (senza evidenziazione)
        key2,html2=dslide(Dk,arg,g[1],None,'none')
        SLIDE_FINAL[PAGES[key2]]=html2
    # cambio gruppo senza ancora
    for gg in groups[1:]:
        pass
    # ultimo stato: riquadro bianco (per la dissolvenza finale)
    t_end=(b0-a0)-14/FPS
    g=grp_of(b0-0.1);k_,h_=dslide(Dk,arg,g[1],anch[-1][1],'tagonly');add(Dk,t_end,h_)
    STATES[Dk].sort(key=lambda x:x[0])
# ---- T (titoli argomento), Q (quiz) ----
for k in range(1,6):
    n=pg(('T',k))
    html=simple(f'ARGOMENTO {k}',data.ARGS[k-1],data.TSUB[k],n)
    add(f'T{k}',0,html);SLIDE_FINAL[n]=html
    nq=pg(('Q',k))
    qh=simple('PAUSA DEL VIDEO · QUIZ',f'Quiz {k}',f'{e(data.QT[k])}<br><span style="font-size:34px;color:#2060AF">5 domande · per continuare almeno l\'80%</span><br><span style="font-size:30px">Rispondi · premi Check · poi Continua</span>',nq)
    add(f'Q{k}',0,qh);SLIDE_FINAL[nq]=qh
# ---- AN: schede (tempi agganciati alla voce reale) ----
import re as _re
SYNCLOG=[]
for name,spec in data.AN.items():
    kind=spec[0];blk=name;a_,b_=plan.OLDS[name] if hasattr(plan,'OLDS') else (None,None)
    a_,b_=[(x,y) for n,x,y in plan.blocks if n==name][0]
    if kind=='cards':
        _,arg,chip,title,cols,cs=spec
        n=pg(('AN',name));cards_l=[(c[1],c[2],c[3]) for c in cs]
        ts=[];prev=0.5
        for (t,tag,head,body) in cs:
            words=[w for w in _re.findall(r"[A-Za-zàèéìòùÀÈÉÌÒÙ']+",head)]+[w for w in _re.findall(r"[A-Za-zàèéìòùÀÈÉÌÒÙ']+",tag)]
            st=align.spoken_time(a_,b_,words,max(0,prev-1.0),window=22)
            tn=max(prev+0.8,(st-0.4)) if (st is not None and abs(st-0.4-t)<=6) else max(prev+0.8,t)
            if abs(tn-t)>3: SYNCLOG.append((name,head,round(t,1),round(tn,1)))
            ts.append(tn);prev=tn
        add(blk,0,cards(data.TOP(arg),title,chip,cards_l,0,None,n,cols=cols))
        for i,c in enumerate(cs): add(blk,ts[i],cards(data.TOP(arg),title,chip,cards_l,i+1,i,n,cols=cols))
        SLIDE_FINAL[n]=cards(data.TOP(arg),title,chip,cards_l,len(cs),None,n,cols=cols)
    elif kind=='sent':
        _,arg,title,text,hl=spec
        n=pg(('AN',name));add(blk,0,sentence(data.TOP(arg),title,text,{},n))
        wt=align.word_times(text,a_,b_);hi={}
        for t,w in hl:
            tn=wt.get(w,t)
            if abs(tn-t)>6: tn=t
            if abs(tn-t)>3: SYNCLOG.append((name,text.split(' ')[w],round(t,1),round(tn,1)))
            for j in range(0,w): hi.setdefault(j,'d')
            hi[w]='now'
            add(blk,max(0.3,tn-0.2),sentence(data.TOP(arg),title,text,dict(hi),n))
            hi[w]='d'
        SLIDE_FINAL[n]=sentence(data.TOP(arg),title,text,{},n)
# ---- mappe del prof ----
RT={x['nome']:x['testo'] for x in json.load(open('../voci/scambio/letteratura-V-lez12/testi_voci.json'))}
MARK={'AN4':[(None,['root']),('Da qui parte la prima freccia',['b1'])],
'AN9':[(None,['root','b2']),("Dall'inetto parte",['b3'])],
'AN14':[(None,['root','aut','pr'])],'AN20':[(None,['root','ka'])],'AN26':[(None,['root','wo'])],
'ANF':[(None,['root']),('Primo riquadro',['b1']),('Secondo riquadro',['b2']),('Da qui la freccia',['b3']),('In basso, gli autori',['aut','pr']),('Franz Kafka e l',['ka']),('Virginia Woolf e la condizione',['wo']),('Guarda la mappa intera',['root','b1','b2','b3','aut','pr','ka','wo'])]}
for blk,(rv,_) in list(data.MAPS.items()):
    t=RT[rv];steps=[]
    for m,on in MARK[blk]:
        f=0 if m is None else t.index(m)/len(t)
        steps.append((f,on))
    data.MAPS[blk]=(rv,steps)
def mapslide(on,n):
    return maphtml(on,n)
import maphtml_mod
maphtml=maphtml_mod.maphtml
for blk,(rv,steps) in data.MAPS.items():
    n=pg(('MAP',blk))
    L=RDUR[blk]
    for fr,on in steps: add(blk,0.5+fr*L,maphtml(on,n,plain=(len(on)>=8)))
    SLIDE_FINAL[n]=maphtml([],n,plain=True)
# ---- ripasso S1..S5 : evidenziazione allineata al parlato ----
import align
TA=json.load(open('../testi_altri.json'))
OLDS={n:(a,b) for n,a,b in plan.blocks}
def ostart(blk): return OLDS[blk]
for k in range(1,6):
    blk=f'S{k}';sents=data.RIP[k];n=pg(('S',k))
    a,b=ostart(blk);st=align.starts(TA[blk],a,b)
    mk=lambda act:content(data.TOP(k),'Schema di ripasso',[(s,'') for s in sents],act,n,prof=False,size=32 if len(sents)>3 else 38,chip='SCHEMA DI RIPASSO',lead=False)
    add(blk,0,mk(None))
    for i in range(len(sents)): add(blk,max(0.3,st[i+1]-0.1)+100/30,mk(i))
    SLIDE_FINAL[n]=mk(None)
# ---- glossario e riepilogo ----
data.GLOS=[g for g in data.GLOS]
order=["Positivismo","Durata","Inconscio","Inetto","Flusso di coscienza","Memoria involontaria","Straniamento"]
GL=dict(data.GLOS);data.GLOS=[(w,GL[w]) for w in order]
blk='GL1';n=pg(('GL',));a,b=ostart(blk);st=align.starts(TA[blk],a,b)
mkg=lambda act:content('Parole chiave','Il glossario della lezione',list(data.GLOS),act,n,prof=False,size=30,chip='GLOSSARIO',lead=True)
add(blk,0,mkg(None))
for i in range(len(data.GLOS)): add(blk,max(0.3,st[i+1]-0.1),mkg(i))
SLIDE_FINAL[n]=mkg(None)
blk='RF1';n=pg(('RF',));a,b=ostart(blk);st=align.starts(TA[blk],a,b)
mkr=lambda act:content('Riepilogo finale','Ricapitoliamo la lezione',[(s.split(':')[0],s.split(': ',1)[1]) for s in data.RFIN],act,n,prof=False,size=32,chip='RIEPILOGO FINALE',lead=True)
add(blk,0,mkr(None))
for i in range(len(data.RFIN)): add(blk,max(0.3,st[i+1]-0.1),mkr(i))
SLIDE_FINAL[n]=mkr(None)
# ---- finali ----
n=pg(('FIN',));h=simple('FINE · LETTERATURA ITALIANA V','Fine della lezione',"Grazie per l'attenzione, e ci vediamo alla prossima lezione.",n);add('FIN1',0,h);SLIDE_FINAL[n]=h
n=pg(('VER',));h=simple('DOPO LA LEZIONE','Verifica finale','Rispondi alle domande del test',n);add('VER',0,h);SLIDE_FINAL[n]=h
n=pg(('CI',));h=simple('DOPO LA LEZIONE','Compiti',"Esercizi da svolgere<br><span style='font-size:34px'>Li trovi qui sotto, sulla pagina. Svolgili con calma dopo il video.</span>",n);add('CI1',0,h);SLIDE_FINAL[n]=h
n=pg(('COMP',));COMPITI=["Le certezze positivistiche in crisi: coordinate del romanzo e figura dell'inetto","Marcel Proust: memoria volontaria e memoria involontaria","Kafka: straniamento, significato della metamorfosi, conflitti e camera","Virginia Woolf: flusso di coscienza e Una stanza tutta per sé"]
h=content('Dopo la lezione','Gli esercizi da svolgere',[(f'{i+1}.',t) for i,t in enumerate(COMPITI)],None,n,prof=False,size=34,lead=True);add('COMP',0,h);SLIDE_FINAL[n]=h
json.dump({'STATES':STATES,'START':START,'NEWF':newf,'PAGES':{'|'.join(map(str,k)):v for k,v in PAGES.items()},'PROF':PROF,'DELTA':DELTA},open('states.json','w'))
json.dump({str(k):v for k,v in SLIDE_FINAL.items()},open('slides_final.json','w'))
json.dump(SYNCLOG,open('synclog.json','w'),ensure_ascii=False);print('correzioni sync >3s:',len(SYNCLOG));print('frame totali nuovi',TOTN,'vecchi',TOTF,'durata nuova s',round(TOTN/30,1));print('stati:',sum(len(v) for v in STATES.values()),'html unici:',len(HTMLS),'pagine:',PG[0],'delta fotogrammi',DELTA)
