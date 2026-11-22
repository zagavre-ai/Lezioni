import sys,json,re,openpyxl,pymupdf
sys.path.insert(0,'/home/user/lav/tools')
from num2it import conv
from build_voci import voci_argomento,vopz
L='/home/user/lav/lez01/'
LET='ABCD'
def cella(v):
    if isinstance(v,(int,float)):return f"{round(v*100)}%"
    return str(v).strip()
def test():
    ws=openpyxl.load_workbook(L+'Lezione.1.-.Preparazione.pt.1.1.xlsx').active;T=[]
    for i,r in enumerate(ws.iter_rows(min_row=2,max_row=21,values_only=True)):
        q=str(r[0]).strip();ok=cella(r[1]);w=[cella(x) for x in r[2:7]]
        s=i%5;sel=[w[(s+k)%5] for k in range(3)];pos=(i*3+1)%4
        o=sel[:pos]+[ok]+sel[pos:];T.append(dict(d=q,o=o,ok=pos))
    return T
def compiti():
    t=''.join(p.get_text() for p in pymupdf.open(L+'Lezione.1_.Preparazione.parte.I.1.pdf'))
    t=re.sub(r'\s+',' ',t)
    parti=re.split(r'(?<=\?)\s+',t.split('Rispondi alle seguenti domande:')[1].strip())
    return [p.strip() for p in parti if p.strip()]
def vq(t):  # testo di domanda -> voce
    t=t.replace('UE n. 1007/2011','U E, cioè Unione Europea, numero mille e sette del duemilaundici').replace('ZIRPRO','ZIRPRO')
    t=t.replace('Bombix','Bombix')
    return conv(t)
RIP1=["Le fibre tessili si dividono in naturali, vegetali o animali, e chimiche, artificiali o sintetiche.",
 "Le proprietà sono morfologiche, chimiche, fisico-meccaniche e fisiologiche.",
 "Le fibre naturali sono scese al trentasette per cento della produzione, mentre le fibre chimiche coprono il sessantatré per cento del consumo.",
 "La lana è fatta soprattutto di cheratina, e le lane migliori vengono dalle spalle e dai fianchi.",
 "Il valore della lana dipende da razza, finezza in micron, filabilità, morbidezza, lunghezza e colore.",
 "I trattamenti della lana sono chimici o meccanici: per esempio lo ZIRPRO, la follatura e il superwash."]
RIPF=RIP1+["La lana è ingualcibile, ignifuga, idrorepellente e igroscopica, fino al trenta per cento del proprio peso.",
 "Tra le lane speciali, la vigogna è la più fine e costosa; a pelo fine corrisponde il prezzo più elevato.",
 "La seta è l'unica fibra naturale continua: con la trattura e la sgommatura si ottengono seta cruda, mezza cotta e cotta.",
 "La seta è resistente, leggera e termoisolante, ma delicata: va lavata tiepida e stirata a rovescio, senza vapore diretto."]
GLOS=[("Fibra tessile","elemento di forma allungata, flessibile e sottile, che si può filare"),
 ("Man-made","fibre chimiche, prodotte con l'intervento dell'uomo su una materia prima"),
 ("Pilling","formazione di antiestetici pallini sulla superficie del tessuto"),
 ("Micron","unità equivalente a un millesimo di millimetro"),
 ("Igroscopicità","capacità delle fibre di assorbire umidità"),
 ("Coibenza","capacità di isolamento termico"),
 ("Sporcabilità","tendenza di un materiale a trattenere lo sporco grasso"),
 ("Pulibilità","facilità di rimozione delle macchie durante il lavaggio"),
 ("Cheratina","proteina principale della lana"),
 ("Lanolina","sostanza grassa che dà alla lana il colore giallognolo"),
 ("Cernita","selezione del vello in base al pregio commerciale"),
 ("Infeltrimento","le squame della lana si saldano e si compenetrano"),
 ("Follatura","infeltrimento voluto della lana"),
 ("Bradford System","misura la filabilità: matasse, o hanks, da 560 yard ottenibili da 1 libbra di fibra"),
 ("Trattura","unione di 4-8 bave per formare il filamento continuo di seta"),
 ("Sericina","sostanza proteica gommosa che ricopre la seta"),
 ("Sgommatura","lavaggio che libera la seta dalla sericina"),
 ("Bachicoltura","allevamento dei bachi da seta a scopo industriale")]
MAPF=[("Classificazione: naturali (vegetali, animali) e chimiche (artificiali, sintetiche)","Classificazione: fibre naturali, vegetali o animali, e fibre chimiche, artificiali o sintetiche."),
 ("Proprietà: morfologiche, chimiche, fisico-meccaniche, fisiologiche","Proprietà: morfologiche, chimiche, fisico-meccaniche e fisiologiche."),
 ("Mercato: naturali 37%, chimiche 63%; sporcabilità e pulibilità","Mercato: fibre naturali al trentasette per cento, chimiche al sessantatré per cento; poi sporcabilità e pulibilità."),
 ("Lana: razze, finezza in micron, Bradford System, trattamenti, pregi","Lana: razze, finezza in micron, Bradford System, trattamenti e pregi."),
 ("Lane speciali: vigogna, cashmere, mohair, alpaca, lama, yak","Lane speciali: vigogna, cashmere, mohair, alpaca, lama e yak."),
 ("Seta: baco, trattura, sgommatura, trattamenti, proprietà, cura","Seta: baco, trattura, sgommatura, trattamenti, proprietà e cura.")]
def gl_voce(a,b):return f"{a}: {conv(b.replace('1 libbra','una libbra').replace('4-8','da quattro a otto'))}."
def tutte():
    V=[('P1_BENVENUTO',None)]
    return V
TITOLI=["Che cos'è una fibra tessile e come si classifica","Le proprietà delle fibre tessili","Il mercato delle fibre e come si sporcano","La lana di pecora: dalla tosatura alla struttura della fibra","Qualità e valore commerciale della lana","I trattamenti chimici e meccanici della lana","I pregi della lana e come si lavora","Lane e peli speciali","La seta: dal baco al filo","La seta: trattamenti, proprietà e cura"]
MAT="Tecnologie dei materiali e dei processi produttivi e organizzativi della moda"
def lista(a,b):return '; '.join(TITOLI[a-1:b]).lower().replace("che cos'è","che cos'è")
def benv(parte,a,b,extra=''):
    nome=['prima','seconda','terza'][parte-1]
    return f"Benvenuti alla {nome} parte della lezione Preparazione, di {MAT}. In questa parte vedremo: {lista(a,b)}.{extra}"
if __name__=='__main__':
    V=[]
    ben=json.load(open(L+'testi_voci_giro1.json'))[0]
    V.append((ben['nome'],ben['testo']))
    V=[(k,t) for k,t in V if k!='P1_BENVENUTO']
    V.insert(0,('P1_BENVENUTO_V3',"Benvenuti alla lezione Preparazione, di "+MAT+". Parleremo di classificazione generale delle fibre tessili e approfondiremo le caratteristiche, l'origine e i processi di lavorazione delle fibre naturali di origine animale: lana e seta. In questa prima parte vedremo: "+lista(1,4)+"."))
    V.append(('P1_CHIUSURA_V2',"Fine della prima parte. Nella seconda parte vedremo la qualità e il valore commerciale della lana, i suoi trattamenti e i suoi pregi, e le lane e i peli speciali."))
    V.append(('P2_BENVENUTO_V3',benv(2,5,8)))
    V.append(('P2_RIPASSO_V2',"Prima di ricominciare, ripassiamo la prima parte. "+' '.join(RIPF[:4])))
    V.append(('P2_CHIUSURA_V2',"Fine della seconda parte. Nella terza parte parleremo della seta, e poi faremo la verifica finale."))
    V.append(('P3_BENVENUTO_V3',benv(3,9,10)+" Alla fine, il glossario, il ripasso, la mappa della lezione e la verifica finale."))
    V.append(('P3_RIPASSO_V2',"Prima di ricominciare, ripassiamo la seconda parte. "+' '.join(RIPF[4:8])))
    for n in range(1,11):V+=voci_argomento(n)
    V.append(('P2_GLOSSARIO',"Glossario. "+' '.join(gl_voce(a,b) for a,b in GLOS)))
    V.append(('P2_RIPASSO_FINALE',"Ripasso finale, argomento per argomento. "+' '.join(RIPF)))
    V.append(('P2_MAPPA_FINALE',"La mappa della lezione. "+' '.join(v for _,v in MAPF)))
    T=test();json.dump(T,open(L+'test.json','w'),ensure_ascii=False,indent=1)
    V.append(('P2_TEST_INTRO',"Verifica finale. Sono venti domande: per superare la lezione serve almeno l'ottanta per cento di risposte corrette."))
    for i,t in enumerate(T,1):
        V.append((f'T{i:02d}_D',f"Domanda {conv(str(i))}. {vq(t['d'])}"))
        V.append((f'T{i:02d}_R',f"La risposta corretta è la {LET[t['ok']]}: {vq(t['o'][t['ok']])}"))
    C=compiti();json.dump(C,open(L+'compiti.json','w'),ensure_ascii=False,indent=1)
    V.append(('P2_COMPITI_INTRO',"Compiti. Rispondi alle seguenti domande."))
    for i,c in enumerate(C,1):V.append((f'C{i}_D',vq(c)))
    V.append(('P2_CHIUSURA',"Per oggi è tutto. Buon lavoro!"))
    bad=[(k,re.findall(r'\d+',t)) for k,t in V if re.search(r'\d',t)]
    print('voci',len(V),'con cifre:',bad);print('compiti',len(C),'test',len(T))
    json.dump([{'nome':k,'testo':t} for k,t in V],open(L+'testi_voci_completo.json','w'),ensure_ascii=False,indent=1)
