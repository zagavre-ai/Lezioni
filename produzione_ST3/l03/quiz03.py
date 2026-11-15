import json
Q={}
def q(n,t,items):Q['Q%d'%n]={'title':'Quiz %d · %s'%(n,t),'items':[{'p':a,'a':b,'w':c,'e':d} for a,b,c,d in items]}
q(1,'La rinascita demografica ed economica',[
("Che cosa succede alla popolazione europea dopo l'anno Mille?","Torna gradualmente a crescere",["Continua a diminuire","Resta invariata","Scompare dalle campagne"],"Dopo secoli di crisi la popolazione cresce."),
("Che cosa favorisce la ripresa dell'agricoltura?","Un clima più caldo e favorevole",["Un clima più freddo","Le invasioni","La chiusura dei mercati"],"Il miglioramento climatico accelera la ripresa."),
("Perché si vive più a lungo?","Più cibo e meno guerre",["Più tasse","Più epidemie","Meno terre coltivate"],"Aumentano le risorse alimentari e diminuiscono le guerre."),
("Che cosa sono i polders?","Terre strappate al mare con le dighe",["Villaggi di montagna","Mulini a vento","Tipi di aratro"],"Si trovano nelle Fiandre e nei Paesi Bassi."),
("Chi abita le villefranche o villenuove?","Contadini liberi da tasse",["Cavalieri","Monaci","Mercanti di spezie"],"Sono nuovi villaggi fondati per volere dei signori feudali."),
])
q(2,'La rivoluzione delle tecniche agricole',[
("Che cosa ha l'aratro pesante?","Un vomere e un versoio in ferro",["Una ruota di legno","Due soli buoi","Un motore ad acqua"],"Rivolta in profondità i terreni argillosi."),
("A che cosa servono giogo frontale e collare rigido?","A evitare il soffocamento e moltiplicare la forza di traino",["A seminare","A macinare il grano","A irrigare i campi"],"Il giogo è per i buoi, il collare per i cavalli."),
("Quanto campo resta a riposo con la rotazione triennale?","Un terzo",["La metà","Tutto","Nulla"],"Prima, con la biennale, restava a riposo metà campo."),
("Quanti raccolti garantisce la rotazione triennale?","Due all'anno",["Uno ogni due anni","Quattro all'anno","Nessuno"],"Cereali invernali, legumi e cereali primaverili."),
("Quali energie usano i mulini?","Acqua e vento",["Carbone e vapore","Fuoco e legna","Elettricità"],"Macinano il grano, spremono olive e azionano macchinari."),
])
q(3,'Il tramonto del sistema curtense',[
("Come è divisa la curtis?","In parte del signore e parte dei contadini",["In tre parti uguali","In campi e boschi","In città e borghi"],"La parte del signore è la dominica, quella dei contadini la massaricia."),
("Che cosa finisce con la crisi della curtis?","Le corvées",["I mulini","Le città","Le dighe"],"I contadini pagano affitti."),
("Come pagano ora i contadini?","Con affitti in denaro o in natura",["Con lavoro gratuito","Con armi","Non pagano"],"Le corvées vengono sostituite dai pagamenti."),
("Che cosa riattiva la vendita delle eccedenze nei mercati?","L'uso della moneta e le prime zecche",["Le invasioni","Il feudo","Il baratto esclusivo"],"Circolazione monetaria e nascita delle zecche."),
("Che cosa fanno alcuni contadini arricchiti?","Comprano terre",["Diventano vescovi","Lasciano l'Europa","Costruiscono castelli"],"Altri si specializzano in mestieri artigianali."),
])
q(4,'Le città, la borghesia e le Arti',[
("Che cos'è l'inurbamento?","Il trasferimento dalle campagne alle città",["La costruzione di castelli","La bonifica delle paludi","La fondazione di monasteri"],"Si cerca libertà dai vincoli feudali."),
("Che cosa sono i borghi?","Nuovi quartieri fuori dalle vecchie mura romane",["Castelli dei signori","Monasteri","Fiere"],"I loro abitanti sono i borghesi."),
("Che cosa ottengono i cittadini?","Diritti propri e tribunali cittadini",["Terre dal re","Il titolo di conte","Il comando dell'esercito"],"Si riduce l'influenza di signori e vescovi."),
("Quale settore è il motore delle manifatture urbane?","Quello tessile",["Quello minerario","Quello navale","Quello librario"],"Impiega manodopera maschile e femminile."),
("Che cosa sono le Arti?","Corporazioni di artigiani e mercanti",["Scuole di pittura","Ordini monastici","Tribunali"],"Stabiliscono prezzi e salari e proteggono i membri malati."),
])
q(5,'Cultura cortese, cittadina e università',[
("Chi era depositaria della cultura nell'Alto Medioevo?","La Chiesa",["I mercanti","I contadini","Le corporazioni"],"Quasi solo gli ecclesiastici sapevano leggere e scrivere in latino."),
("Che cosa esalta la cultura cortese?","Coraggio, onore e fedeltà",["Il guadagno","L'ascesi","Il lavoro manuale"],"Sono i valori cavallereschi riassunti nella cortesia."),
("Che cosa insegnano le scuole urbane?","Saperi pratici: calcolo, lingue, diritto",["Solo teologia","Solo latino","Solo musica"],"Usano le lingue volgari."),
("In che anno è fondata l'Università di Bologna?","Nel 1088",["Nel 962","Nel 1284","Nel 1500"],"Bologna e Parigi sono tra le prime università."),
("Come si svolgeva una lezione scolastica?","Con la lectio e poi la disputatio",["Con una gita","Con un esame scritto","Con una preghiera"],"Si usavano ragione e logica per risolvere le quaestiones."),
])
q(6,'La rivoluzione commerciale e le città marinare',[
("Che cosa innesca la rivoluzione commerciale?","L'aumento demografico e agricolo",["Le invasioni","La peste","La chiusura dei porti"],"Rinascono i commerci a lungo raggio."),
("Quali sono le città marinare italiane?","Venezia, Amalfi, Genova e Pisa",["Roma, Milano, Napoli e Torino","Firenze, Siena, Lucca e Pavia","Palermo, Bari, Ancona e Trieste"],"Godono di autonomia politica e basi marittime."),
("Che cosa crea Amalfi?","Le Tavole amalfitane",["Il fiorino","La Lega Anseatica","Le fiere"],"È il primo codice di diritto marittimo."),
("Che cosa ottiene Venezia dall'Impero Bizantino?","Enormi privilegi commerciali",["Un esercito","Il titolo imperiale","Nulla"],"Domina i mercati orientali."),
("Quando Genova vince la Meloria?","Nel 1284",["Nel 1088","Nel 962","Nel 1130"],"La vittoria chiude la rivalità con Pisa."),
])
q(7,'Vie del commercio, fiere e strumenti finanziari',[
("Quali sono i tre poli commerciali?","Italia del Nord, Fiandre e Germania del Nord",["Spagna, Francia e Inghilterra","Roma, Parigi e Londra","Africa, Asia e Americhe"],"La Germania del Nord forma la Lega Anseatica."),
("Dove si tengono le fiere più importanti?","In Champagne, nel Nord della Francia",["A Venezia","A Bologna","In Sicilia"],"Vi si incontrano mercanti del Nord e del Sud."),
("Quale è un bene di lusso?","La seta",["Il grano","Il vino","Il legname"],"Anche spezie e metalli preziosi."),
("Che cos'è la commenda?","Un investitore finanzia un mercante e si dividono i guadagni",["Un tipo di moneta","Una corporazione","Un tribunale"],"Si usava soprattutto per i viaggi per mare."),
("A che serve la lettera di cambio?","A trasferire denaro senza portare contanti",["A comprare terre","A pagare le tasse al re","A fondare un'università"],"È l'antenata dell'assegno."),
])
json.dump(Q,open('/home/user/lav/l03/quiz_argomenti.json','w'),ensure_ascii=False,indent=1);print(len(Q))
