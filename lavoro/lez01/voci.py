# Testi delle voci Kore della lezione 1 (Storia dell'arte V · Il Neoclassicismo).
# Solo materiale del docente (slide, parole della lezione, mappa). Numeri in lettere per la voce.
import json,re,sys
U=['zero','uno','due','tre','quattro','cinque','sei','sette','otto','nove','dieci','undici','dodici','tredici','quattordici','quindici','sedici','diciassette','diciotto','diciannove']
T=['','','venti','trenta','quaranta','cinquanta','sessanta','settanta','ottanta','novanta']
def n99(n):
    if n<20:return U[n]
    d,u=divmod(n,10);t=T[d]
    if u in(1,8):t=t[:-1]
    return t+(U[u] if u else '')
def n999(n):
    c,r=divmod(n,100);s='' if c==0 else ('cento' if c==1 else U[c]+'cento')
    if r==0:return s
    if c and r//10==8 and False:pass
    x=n99(r)
    if c and r<100 and (r//10==8 or r==8):s=s[:-1] if False else s
    return s+x
def num(n):
    if n<1000:return n999(n)
    m,r=divmod(n,1000);s='mille' if m==1 else n999(m)+'mila'
    return s+(n999(r) if r else '')
def lettere(t):
    f=lambda n:(lambda w:w[:-3]+'tré' if n>20 and w.endswith('tre') else w)(num(n))
    return re.sub(r'\d+',lambda m:f(int(m.group())),t)
VOCI={}
VOCI['INTRO']="Benvenuti alla prima videolezione di Storia dell'arte: Il Neoclassicismo, il ritorno all'antico. In questa lezione vedremo come nasce il movimento, tra Grand Tour, musei e scoperte archeologiche; l'architettura, da Piranesi a Piermarini; i teorici e la scultura di Canova; e la pittura di David e di Ingres. Buona visione!"
VOCI['ARG']="Ecco gli argomenti della lezione. Primo: le origini, il Grand Tour, i musei e la moda. Secondo: l'architettura, Piranesi e i visionari francesi. Terzo: l'architettura in Italia e in Europa. Quarto: i teorici e la scultura di Canova. Quinto: la pittura di David e di Ingres."
VOCI['A1']="Approfondimento. Guardiamo da vicino questo dipinto: Johann Wolfgang Goethe visita il Colosseo a Roma, di Jakob Philipp Hackert, 1790, olio su tela. Due signori vestiti alla moda del Settecento osservano il Colosseo, che si staglia all'orizzonte. Sono figure piccole, un po' sperdute tra le maestose rovine: l'artista le inserisce per accentuare, per contrasto, la monumentalità e l'immensità dello spazio architettonico romano. È un'opera pittorica, ma anche la riproduzione di un'architettura che vuole rendere glorioso il passato di Roma. Il soggetto è proprio il Grand Tour, il viaggio di formazione dei giovani europei, che aveva l'Italia come meta obbligatoria. La veduta è costruita sulla falsariga delle vedute di Piranesi."
VOCI['A2']="Approfondimento. Il Cenotafio di Newton, di Étienne-Louis Boullée, 1784: un progetto mai realizzato. Doveva essere una tomba enorme, di forma sferica, con un ingresso che conduce lo spettatore, microscopico, dentro la grandiosità dell'edificio. Nel disegno si vedono dei cipressi. Era la tomba di Newton, lo scienziato inglese, il padre della gravità. Ma non è soltanto la tomba di un uomo: è l'esaltazione di figure illuminate, che hanno dato la loro vita per la scienza e per la razionalità, e dell'intelligenza umana sul volto della Terra. È l'architettura visionaria: un'architettura monumentale, basata su pure forme geometriche come la sfera, e su un ideale di bellezza universale."
VOCI['A3']="Approfondimento. Il Teatro alla Scala di Milano, costruito da Giuseppe Piermarini tra il 1776 e il 1778. La pianta è rettangolare e chiara. Si accede da due ingressi, sul fronte e sul retro, con un porticato non monumentale, progettato per agevolare il passaggio delle carrozze dei visitatori al riparo dalla pioggia. La facciata è articolata su tre livelli rigorosi, dominata da elementi classici di chiara derivazione greco-romana. L'interno ha la forma di un ferro di cavallo, con cinque ordini di palchi in legno sovrapposti e una galleria, il loggione superiore, studiati per garantire una visibilità e un'acustica eccellenti. Nel 1778 il teatro viene inaugurato con l'opera L'Europa riconosciuta, di Antonio Salieri."
VOCI['A4']="Approfondimento. Amore e Psiche, di Antonio Canova, realizzato tra il 1787 e il 1793 su commissione del colonnello inglese John Campbell. L'opera raffigura il momento esatto poco prima del bacio: il dio Amore rianima con un bacio la giovane Psiche, svenuta per aver aperto un vaso proibito. Canova organizza la composizione secondo uno schema perfetto di linee tese e curve, che si incrociano diagonalmente formando una grande X strutturale. Le ali spiegate di Amore formano un arco teso, mentre le braccia delle due figure si intrecciano creando un cerchio geometrico perfetto, che incornicia i volti dei due amanti, a pochissimi millimetri dal bacio. Il marmo viene lavorato fino a ottenere una levigatezza specchiante, e infine rifinito con una patina di cera per imitare la morbidezza della pelle umana."
VOCI['A5']="Approfondimento. Napoleone valica il Gran San Bernardo, di Jacques-Louis David, eseguito tra il 1800 e il 1801. Il primo console della Repubblica è in sella a un impetuoso cavallo bianco rampante. È calmo e idealizzato, con un mantello rosso gonfiato dal vento, e indica con il braccio destro teso verso l'alto la direzione della vittoria, oltre le montagne. Nelle fonti storiche, invece, Napoleone avrebbe valicato le Alpi a piedi o su un asino: per questo doveva essere monumentalizzato e rappresentato. Sulle rocce scure, in basso a sinistra, David incide i nomi dei grandi condottieri che compirono la stessa impresa: Annibale, prima di lui, e Carlo Magno. Così inserisce Napoleone nella leggenda della storia universale."
# pillole: righe a schermo (con cifre) = voce (cifre in lettere)
PIL={
'R1':["Il Neoclassicismo nasce da Roma e si diffonde in tutta Europa.",
"Il Grand Tour è il viaggio di formazione in Italia dei giovani aristocratici europei.",
"Gli scavi di Ercolano e Pompei alimentano l'amore per l'antichità classica.",
"Nascono i musei pubblici: il British Museum a Londra e il Louvre a Parigi.",
"L'antico invade la vita quotidiana: arredamento, stile impero e moda."],
'R2':["L'architettura neoclassica privilegia forme geometriche semplici, piante simmetriche e ordini classici.",
"Piranesi diffonde il fascino delle rovine con le Vedute fantastiche di Roma e le Prigioni immaginarie.",
"Boullée propone un'architettura visionaria, fatta di pure forme geometriche come la sfera.",
"Il Cenotafio di Newton, mai realizzato, è l'esempio perfetto.",
"Soufflot progetta la chiesa di Sainte-Geneviève a Parigi: è una chiesa, ma sembra un tempio.",
"Nel 1791 diventa il Panthéon nazionale dei grandi uomini."],
'R3':["Piermarini progetta il Palazzo Reale e il Teatro alla Scala di Milano: sobrietà e funzionalità.",
"In Inghilterra Robert Adam progetta Kedleston Hall, dal Neopalladianesimo allo stile Adam.",
"A Berlino la Porta di Brandeburgo si ispira ai modelli ateniesi.",
"A Ratisbona il Walhalla riproduce un tempio greco.",
"Il riferimento è sempre greco-romano, ma ogni paese lo declina a modo suo."],
'R4':["Winckelmann identifica l'ideale nell'arte greca: «nobile semplicità e quieta grandezza».",
"Imitare gli antichi non è copiare: è cercare la bellezza ideale.",
"Mengs applica i principi classici a un disegno geometrico e simmetrico.",
"Canova segue un processo rigoroso: dal disegno al modello in argilla, dalla sbozzatura alla finitura del marmo.",
"Opere celebri: Amore e Psiche, Venere vincitrice, Le tre Grazie.",
"Il Monumento a Maria Cristina d'Austria rinnova il monumento funebre."],
'R5':["David lega l'arte all'impegno etico e politico.",
"Il giuramento degli Orazi è il manifesto del Neoclassicismo pittorico.",
"La Morte di Marat trasforma un delitto politico in un'immagine sacra.",
"Napoleone valica il Gran San Bernardo celebra il mito di Napoleone.",
"Ingres, allievo di David, difende il primato del disegno.",
"La grande odalisca, del 1814, porta il fascino dell'Oriente."],
}
for k,v in PIL.items():VOCI[k]="Ripasso. "+" ".join(v)
GLOSS=[("Neoclassicismo","ritorno all'antico: movimento artistico e culturale internazionale, nato dalla seconda metà del Settecento."),
("Grand Tour","viaggio di formazione dei giovani aristocratici europei, con l'Italia come meta obbligatoria."),
("Veduta","immagine di Roma e dei suoi monumenti, fedele o inventata, come quelle di Piranesi."),
("Cenotafio","monumento funebre: quello di Newton, di Boullée, non fu mai realizzato."),
("Neopalladianesimo","riscoperta dell'architettura di Andrea Palladio."),
("Pronao","ingresso con un frontone triangolare, sorretto da colonne."),
("Quadriga","carro con quattro cavalli, condotto da un auriga: sta sopra la Porta di Brandeburgo."),
("Stile impero","lo stile di arredo che Napoleone adotta per la nuova Francia imperiale, ma neoclassica."),
("Agrippina","divano in stile impero."),
("Accademia di Belle Arti","centro statale per l'insegnamento e la diffusione dei principi artistici classici.")]
VOCI['GL']="Glossario. Le parole da ricordare. "+" ".join(f"{t}: {d}" for t,d in GLOSS)
RFS=[("Le origini: Grand Tour, musei e moda","Il Neoclassicismo nasce da Roma e si diffonde in tutta Europa, come ritorno all'antico. Il Grand Tour porta in Italia i giovani aristocratici europei; gli scavi di Ercolano e Pompei alimentano l'amore per l'antichità. Nascono i musei pubblici e le Accademie di Belle Arti, e il gusto per l'antico entra nell'arredamento e nella moda."),
("L'architettura: Piranesi e i visionari francesi","L'architettura neoclassica usa forme geometriche semplici e piante simmetriche. Piranesi diffonde il fascino delle rovine; Boullée immagina un'architettura visionaria, come il Cenotafio di Newton; Soufflot progetta Sainte-Geneviève, una chiesa che sembra un tempio."),
("L'architettura in Italia e in Europa","Piermarini progetta il Palazzo Reale e il Teatro alla Scala di Milano. In Inghilterra, Robert Adam progetta Kedleston Hall. In Germania, la Porta di Brandeburgo guarda ai modelli ateniesi e a Ratisbona sorge il Walhalla."),
("I teorici e la scultura di Canova","Winckelmann cerca l'ideale nell'arte greca, nobile semplicità e quieta grandezza, e Mengs lo applica alla pittura. Canova lavora dal disegno al marmo: Amore e Psiche, la Venere vincitrice, Le tre Grazie e il monumento a Maria Cristina d'Austria."),
("La pittura: David e Ingres","David lega l'arte all'impegno etico e politico: il Giuramento degli Orazi, la Morte di Marat, Napoleone che valica il Gran San Bernardo. Ingres, suo allievo, difende il primato del disegno e porta il fascino dell'Oriente con la grande odalisca.")]
VOCI['RF']="Ripasso finale, argomento per argomento. "+" ".join(f"{i+1}. {t}. {x}".replace(f"{i+1}.",['Primo argomento:','Secondo argomento:','Terzo argomento:','Quarto argomento:','Quinto argomento:'][i]) for i,(t,x) in enumerate(RFS))
SPS=RFS[:3]
VOCI['SP']="Prima di continuare, ripassiamo quello che abbiamo visto nella Parte precedente. "+" ".join(f"{['Primo argomento:','Secondo argomento:','Terzo argomento:'][i]} {t}. {x}" for i,(t,x) in enumerate(SPS))
VOCI['MF']="Mappa della lezione. Che cos'è il Neoclassicismo? Il Neoclassicismo, arte. È un movimento artistico e culturale, che riscopre l'arte classica greco-romana. Nasce in contrasto alle stravaganze del Barocco e del Rococò. Il periodo: dal 1750 al 1815, tra Illuminismo, Rivoluzione francese e Napoleone. Rinasce l'interesse per l'arte classica grazie alla scoperta di Pompei ed Ercolano e a Winckelmann, archeologo. L'architettura: rispetto al Barocco non ci sono decorazioni e le forme sono semplici. Gli architetti: Giuseppe Piermarini, Luigi Cagnola e Leopoldo Pollack. La scultura: soggetti idealizzati, perfetti. Con Antonio Canova. La pittura: temi storici e mitologici. Con Jacques-Louis David e Jean-Auguste-Dominique Ingres."
COMPITI=["Analizza il contesto culturale e sociale in cui nasce e si diffonde il Neoclassicismo, spiegando il ruolo del Grand Tour in Italia, l'importanza delle scoperte archeologiche di Ercolano e Pompei, la nascita dei musei pubblici e delle Accademie di Belle Arti, fino alle ricadute sulla moda, sull'arredamento e sull'urbanistica europea.",
"Descrivi le caratteristiche principali dell'architettura neoclassica e confronta le diverse declinazioni europee, soffermandoti sulle visioni e incisioni di Giambattista Piranesi, sui progetti visionari illuministi di Étienne-Louis Boullée in Francia, sull'opera di Giuseppe Piermarini in Italia e sugli sviluppi in Inghilterra e Germania.",
"Illustra i principi estetici elaborati dai teorici Johann Joachim Winckelmann (con particolare riferimento ai concetti di «nobile semplicità e quieta grandezza» e di imitazione degli antichi) e Anton Raphael Mengs, spiegando poi come tali ideali trovino applicazione nella scultura e nel metodo creativo di Antonio Canova attraverso le sue opere principali.",
"Metti a confronto la pittura di Jacques-Louis David e quella del suo allievo Jean-Auguste-Dominique Ingres, analizzando da un lato l'impegno etico-politico e la visione epica della storia nelle opere di David (come Il giuramento degli Orazi e La Morte di Marat) e dall'altro il primato del disegno e l'apertura ai temi esotici in Ingres (come ne La grande odalisca)."]
CHIUSURA="Svolgi i compiti qui sotto e premi Consegna: arrivano al docente nel tuo quaderno dei compiti."
VOCI['COMPITI']="Compiti. "+" ".join(f"{['Primo','Secondo','Terzo','Quarto'][i]} compito. {t}" for i,t in enumerate(COMPITI))+" "+CHIUSURA
def per_voce(t):
    t=t.replace('«','').replace('»','')
    return lettere(t)
if __name__=='__main__':
    out=[{"nome":"NC_"+k,"testo":per_voce(v)} for k,v in VOCI.items()]
    json.dump(out,open(sys.argv[1],'w'),ensure_ascii=False,indent=1)
    for o in out:print(o['nome'],len(o['testo'].split()),'parole')
