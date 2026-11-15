import json
Q={}
def q(n,t,items):Q['Q%d'%n]={'title':'Quiz %d · %s'%(n,t),'items':[{'p':a,'a':b,'w':c,'e':d} for a,b,c,d in items]}
q(1,'La crisi morale e i centri di potere',[
("Quale periodo comincia con l'anno Mille?","Il Basso Medioevo",["L'Alto Medioevo","L'età moderna","L'epoca carolingia"],"Con l'anno Mille comincia il Basso Medioevo."),
("Che cosa diventano monasteri, abbazie e diocesi?","Ricchi centri economici e politici",["Scuole per i contadini","Fortezze militari","Mercati di città"],"Sono centri di potere ecclesiastici."),
("Da chi sono gestiti questi centri di potere?","Dall'aristocrazia",["Dai contadini","Dai mercanti","Dagli studenti"],"A guidarli sono famiglie aristocratiche."),
("Che cosa vive la Chiesa nell'anno Mille?","Una crisi morale",["Un periodo di grande rigore","Una completa indipendenza","Una rapida espansione in Asia"],"La Chiesa attraversa una crisi morale, oltre che politica."),
("Che cosa deve fare la Chiesa, secondo il docente?","Staccarsi dall'impero ed essere ripulita",["Unirsi all'impero","Abbandonare le città","Eleggere un imperatore"],"Serve una riforma che la renda indipendente e pura."),
])
q(2,"L'alto clero senza vocazione",[
("Chi eredita il feudo in una famiglia nobile?","Il primogenito maschio",["La figlia maggiore","Tutti i figli in parti uguali","Il figlio più piccolo"],"Il feudo passa al primogenito maschio."),
("Dove finiscono spesso gli altri figli maschi?","Nella Chiesa",["In esilio","Nell'esercito imperiale","Nelle città come mercanti"],"Diventano membri della Chiesa."),
("Che cos'è l'alto clero senza vocazione?","Nobili scelti per prestigio e ricchezze",["Monaci poveri","Contadini istruiti","Preti di parrocchia"],"Guidano la Chiesa solo per ottenere prestigio e patrimoni terrieri."),
("Che cosa fa spesso il basso clero?","Aiuta i poveri",["Governa i feudi","Nomina gli imperatori","Riscuote le tasse"],"Monaci e preti spesso fanno del bene per i poveri."),
("Quali figure fanno parte dell'alto clero?","Vescovi e arcivescovi",["Monaci e parroci","Cavalieri","Notai"],"L'alto clero sono le alte gerarchie."),
])
q(3,'Vescovi-conte e i tre mali',[
("Chi sono i vescovi-conte ottoniani?","Vescovi fidati nominati dagli imperatori",["Conti eletti dal papa","Monaci di Cluny","Vescovi dell'Oriente"],"Sono personalità politiche e amministratori più che guide spirituali."),
("Che cos'è la simonia?","La compravendita delle cariche ecclesiastiche",["Il matrimonio dei preti","Il rifiuto delle ricchezze","Il digiuno dei monaci"],"Si compravano cariche con denaro o beni materiali."),
("Che cos'è il concubinato?","Condotta del clero che viola l'obbligo di castità",["Un ordine monastico","Un tributo feudale","Un tipo di investitura"],"Dà vita a convivenze e famiglie di fatto."),
("Che cosa indica il nicolaismo?","La tendenza dei preti a sposarsi o a vivere con concubine",["La vendita delle cariche","La riforma di Cluny","Il potere dei cardinali"],"È strettamente collegato al concubinato."),
("Quanti sono i «tre mali» della Chiesa?","Simonia, concubinato e nicolaismo",["Scisma, eresia e crociata","Povertà, guerra e peste","Simonia, pataria e Cluny"],"Sono i tre mali che la riforma vuole combattere."),
])
q(4,'I movimenti di riforma',[
("Dove nasce l'abbazia di Cluny?","In Borgogna",["In Normandia","A Milano","In Sicilia"],"Nel 910 nasce in Borgogna."),
("Da chi dipende Cluny?","Direttamente dal papa",["Dai nobili locali","Dall'imperatore","Dal re di Francia"],"Così evita il controllo dei nobili."),
("Quali ordini rigorosi nascono?","I cistercensi e i certosini",["I patarini","I cardinali","Gli altavilla"],"Si caratterizzano per eremitismo e ascesi."),
("Che cosa distingue il clero regolare?","Segue una regola monastica in isolamento",["Vive nel mondo","Governa le diocesi","Non prende i voti"],"Il clero secolare invece vive nel mondo."),
("Chi sono i patarini di Milano?","Laici che contestano i sacerdoti corrotti",["Cavalieri normanni","Monaci di Cluny","Cardinali riformatori"],"Artigiani e mercanti boicottano i preti corrotti e contestano la ricchezza del clero."),
])
q(5,"I papi riformatori e lo Scisma d'Oriente",[
("Quali papi combattono la corruzione?","Leone IX e Niccolò II",["Gregorio VII e Urbano II","Giovanni XII e Silvestro II","Leone X e Pio II"],"Sono i papi riformatori."),
("Che cosa stabilisce Niccolò II nel 1059?","Che il papa sia eletto solo dai cardinali",["Che il papa sia scelto dall'imperatore","Che i preti possano sposarsi","Che il papa viva a Costantinopoli"],"Così finisce l'intromissione dell'imperatore."),
("Quando avviene lo Scisma d'Oriente?","Nel 1054",["Nel 962","Nel 1075","Nel 1122"],"È la rottura definitiva tra Roma e Costantinopoli."),
("Quali Chiese si separano?","Quella cattolica di Roma e quella ortodossa di Costantinopoli",["Quella cattolica e quella protestante","Quella latina e quella normanna","Quella monastica e quella secolare"],"Le ragioni sono teologiche e politiche."),
("Chi sono i cardinali, secondo il docente?","I grandi prelati che eleggono il papa",["I capi dell'esercito","I feudatari minori","I monaci di Cluny"],"Dal 1059 l'elezione spetta a loro."),
])
q(6,'Gregorio VII e il Dictatus papae',[
("Che cosa vuole Gregorio VII?","Una Chiesa libera e indipendente dal potere politico",["Una Chiesa sottomessa all'imperatore","Una Chiesa solo monastica","La fine del papato"],"Per lui la Chiesa deve tornare libera, anche politicamente."),
("In che anno scrive il Dictatus papae?","Nel 1075",["Nel 1054","Nel 1122","Nel 1066"],"È un insieme di precetti."),
("Che cosa afferma il Dictatus papae?","Il primato del papa su tutta la cristianità",["L'autorità dell'imperatore sul papa","L'uguaglianza tra i vescovi","La fine dei monasteri"],"Il papa è al vertice della cristianità."),
("Quale potere rivendica il papa?","Deporre gli imperatori",["Nominare i duchi","Coniare moneta","Eleggere i cardinali a vita"],"Può deporre gli imperatori."),
("Da quale monastero proveniva Gregorio VII?","Cluny",["Montecassino","Citeaux","Canossa"],"Prima di diventare papa era un monaco di Cluny."),
])
q(7,'La lotta per le investiture',[
("Con quale imperatore si scontra Gregorio VII?","Enrico IV",["Ottone I","Corrado II","Federico I"],"Lo scontro riguarda la nomina dei vescovi."),
("Che cosa accade a Canossa nel 1077?","Enrico IV chiede perdono al papa",["Il papa chiede perdono all'imperatore","Si firma il Concordato","Nasce la pataria"],"L'imperatore attende tre giorni nella neve."),
("Quanto attende Enrico IV nella neve?","Tre giorni",["Un'ora","Una settimana","Un mese"],"Così raccontano le cronache."),
("Quando è firmato il Concordato di Worms?","Nel 1122",["Nel 1059","Nel 1077","Nel 1130"],"È l'accordo finale della lotta per le investiture."),
("Che cosa separa il Concordato di Worms?","L'investitura religiosa da quella temporale",["Roma da Costantinopoli","La Francia dall'Inghilterra","Il clero secolare dal regolare"],"La prima spetta al clero, la seconda al sovrano."),
])
q(8,"L'espansione normanna in Europa",[
("Da dove provengono i Normanni?","Dalla Scandinavia",["Dall'Africa del Nord","Dall'Asia","Dalla Spagna"],"Si stanziano nel Nord della Francia."),
("Quale ducato fondano nel Nord della Francia?","Il Ducato di Normandia",["Il Ducato di Borgogna","Il Ducato di Aquitania","Il Ducato di Sassonia"],"È formalmente un feudo del re di Francia."),
("Chi sconfigge gli anglosassoni a Hastings?","Guglielmo il Conquistatore",["Ruggero II","Roberto il Guiscardo","Enrico IV"],"La battaglia avviene nel 1066."),
("In che anno avviene la battaglia di Hastings?","Nel 1066",["Nel 1054","Nel 1130","Nel 1075"],"Il duca di Normandia diventa re d'Inghilterra."),
("Che cosa fa Guglielmo dopo la conquista?","Centralizza il potere monarchico",["Divide il regno in feudi autonomi","Rinuncia al titolo di duca","Si sottomette al papa"],"Il regno d'Inghilterra diventa fortemente centralizzato."),
])
q(9,'I Normanni nel Sud e il Regno di Sicilia',[
("Quale famiglia normanna è citata nel Sud Italia?","Gli Altavilla",["I Capetingi","Gli Ottoni","I Salii"],"Sono cavalieri mercenari."),
("Che cosa sfruttano i Normanni nel Sud?","Le divisioni tra bizantini e longobardi",["L'alleanza con l'imperatore","La debolezza dei Vichinghi","Le guerre in Britannia"],"Così conquistano territori."),
("Chi nomina Roberto il Guiscardo suo vassallo, nel 1059?","Papa Niccolò II",["L'imperatore Enrico IV","Guglielmo il Conquistatore","Gregorio VII"],"Il papa cerca protezione militare contro l'Impero."),
("Chi fonda il Regno di Sicilia nel 1130?","Ruggero II",["Roberto il Guiscardo","Guglielmo","Ottone I"],"Strappa l'isola ai musulmani."),
("Come è descritto il Regno di Sicilia?","Uno Stato centralizzato e multiculturale",["Un regno solo cattolico","Un insieme di feudi indipendenti","Un territorio senza capitale"],"Ha influenze cattoliche, bizantine e arabo-islamiche."),
])
json.dump(Q,open('/home/user/lav/l02/quiz_argomenti.json','w'),ensure_ascii=False,indent=1)
print(len(Q))
