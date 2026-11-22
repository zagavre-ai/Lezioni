# Specifica degli argomenti: intervalli del video originale e scene (slide del prof / immagini del suo PDF)
KEYS={'2':['Cinquanta milioni di morti','Norimberga e Tokyo','ONU','Diritti umani'],
'3':['Bretton Woods','Bipolarismo','Cortina di ferro','Dollaro'],
'5':['Guerra Fredda','Dottrina Truman','Piano Marshall','Cominform'],
'6':['Quattro zone','Blocco di Berlino','Ponte aereo','Due Germanie'],
'8':['Welfare State','NATO','CECA','Trattati di Roma'],
'9':['Stati satelliti','Economia pianificata','Tito','Patto di Varsavia'],
'11':['Maccartismo','Rosenberg','Rollback','Destalinizzazione','Ungheria 1956'],
'12':['Cina comunista','Giappone','Guerra di Corea','38° parallelo'],
'14':['Grande balzo in avanti','Rivoluzione Culturale']}
PAGINA={'2':2,'3':3,'5':5,'6':6,'8':8,'9':9,'11':11,'12':12,'14':14}
IMG={'eu46':('im-004.jpg','L’Europa dopo la conferenza di Parigi del 1946'),
'ger':('im-008.jpg','La divisione della Germania e di Berlino'),
'eu55':('im-012.jpg','L’Europa divisa in due blocchi (1955)'),
'cor':('im-016.jpg','La guerra di Corea (1950-1953)')}
# argomento: (titolo, t_inizio_approssimato, t_fine_approssimata, scene)
# scena cards: ('c',pagina,[indici card],t0,t1)   scena immagine: ('i',chiave,t0,t1)
ARG={
1:('Il dopoguerra e la nuova geopolitica',60,982,[('c','2',[0,1,2,3],60,9999,[(60,0),(295,1),(562,2),(650,3)])]),
2:('Bretton Woods e il bipolarismo',982,1625,[('c','3',[0,1,2],982,1371,[(982,0),(1122,1),(1333,2)]),('i','eu46',1371,1552),('c','5',[0],1552,1562,[(1552,0)]),('i','eu46',1562,9999)]),
3:('La dottrina Truman, il piano Marshall e Berlino',1625,2322,[('c','5',[1,2,3],1625,1962,[(1625,1),(1715,2),(1884,3)]),('c','6',[0],1962,2019,[(1962,0)]),('i','ger',2019,2158),('c','6',[1,2,3],2158,9999,[(2158,1),(2188,2),(2245,3)])]),
4:('L’Europa del blocco occidentale',2322,2783,[('c','8',[0,1,2],0,9999,[(2322,0),(2453,1),(2603,2)])]),
5:('Gli Stati Uniti negli anni Cinquanta',2783,2990,[('c','11',[0,1],0,9999,[(2783,0),(2909,1)])]),
6:('Il blocco orientale e la destalinizzazione',2990,3568,[('c','9',[0,1,2,3],0,3024,[(2990,0)]),('i','eu55',3024,3081),('c','9',[0,1,2,3],3081,3255,[(3081,0),(3148,1),(3193,3),(3215,2)]),('c','11',[2],3255,9999,[(3255,2)])]),
7:('La guerra fredda in Asia',3568,4310,[('c','12',[0,1,2],3568,3825,[(3568,None),(3594,0),(3635,None),(3806,1)]),('i','cor',3825,4007),('c','12',[0,1,2],4007,4210,[(4007,2),(4084,None),(4112,0)]),('c','14',[0,1,2],4210,9999,[(4210,1),(4215,0),(4234,2)])]),
}

# ---- numerazione delle pagine della dispensa (cover = 1): finestre di slide / immagini in ordine, poi schema e mappa dell'argomento
MAPPE_ARG={1:'MAP1',6:'MAP2',7:'MAP3'}
def numeri_pagina():
    import slide as S,json
    SL=json.load(open('/tmp/w/slides.json'));num={};elenco=[]
    for parte,args in [(1,[1,2,3]),(2,[4,5,6,7])]:
        p=2
        for n in args:
            for sc in ARG[n][3]:
                if sc[0]=='i':
                    k=('i',sc[1])
                    if (parte,k) not in num:num[(parte,k)]=p;elenco.append((parte,p,k));p+=1
                else:
                    idx=sc[2];wins=S.finestre([SL[sc[1]]['par'][i] for i in idx])
                    for w in wins:
                        k=('c',sc[1],tuple(idx[x] for x in w))
                        if (parte,k) not in num:num[(parte,k)]=p;elenco.append((parte,p,k));p+=1
            if n in MAPPE_ARG:elenco.append((parte,p,('MAP',n)));p+=1
            elenco.append((parte,p,('PS',n)));p+=1
    return num,elenco
