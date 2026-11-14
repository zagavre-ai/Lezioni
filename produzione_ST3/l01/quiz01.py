import json
Q={}
def q(n,t,items):Q['Q%d'%n]={'title':'Quiz %d · %s'%(n,t),'items':[{'p':a,'a':b,'w':c,'e':d} for a,b,c,d in items]}
q(1,'La frammentazione del potere',[
("Che cosa accadde in Europa occidentale dopo la fine dell'Impero carolingio?","Il territorio si divise nei regni di Francia, Germania e Italia",["Nacque un unico grande regno europeo","Il potere dei sovrani si rafforzò","L'Europa tornò unita sotto Roma"],"Dopo l'Impero carolingio si formarono tre regni: Francia, Germania e Italia."),
("Che cosa accadde al potere dei sovrani in questo periodo?","Si indebolì drasticamente",["Aumentò in modo stabile","Passò tutto al papa","Restò identico al tempo di Carlo Magno"],"Il potere dei sovrani si indebolì e a governare furono sempre più le grandi famiglie aristocratiche."),
("Chi iniziò a governare in modo autonomo all'interno di ciascun regno?","Le grandi famiglie aristocratiche",["I contadini","I mercanti delle città","I soli vescovi"],"Le grandi famiglie aristocratiche governarono in autonomia i propri territori."),
("Quali erano i poteri locali che nacquero in questo mosaico?","Contee, marchesati e ducati",["Repubbliche e consolati","Province e prefetture","Satrapie e tetrarchie"],"Il mosaico di poteri locali autonomi era fatto di contee, marchesati e ducati."),
("A quali secoli si riferisce questo periodo?","Al decimo e all'undicesimo secolo",["Al quinto e al sesto secolo","Al quindicesimo e al sedicesimo secolo","Al terzo e al quarto secolo"],"Il periodo studiato va dal X all'XI secolo, cioè dagli anni 900 al 1100 circa."),
])
q(2,'Vassalli e feudo',[
("Che cosa riceveva il vassallo sotto Carlo Magno?","Un territorio in beneficio, in cambio di sostegno militare",["Un titolo senza terre","Una somma di denaro ogni anno","Il comando dell'esercito del re"],"Il beneficio era un territorio da sfruttare economicamente in cambio di sostegno militare."),
("Che cosa succedeva alla morte del vassallo, ai tempi di Carlo Magno?","La terra tornava al re",["La terra passava ai figli","La terra veniva divisa tra i contadini","La terra restava alla Chiesa"],"Il beneficio non era ereditario: alla morte del vassallo tornava al re."),
("Che cosa stabilì il Capitolare di Quierzy dell'877?","Rese ereditarie le cariche e i benefici dei grandi feudatari",["Abolì il vassallaggio","Creò il Sacro Romano Impero","Vietò ai vescovi di possedere terre"],"Fu emanato da Carlo il Calvo e rese ereditari cariche e benefici dei grandi feudatari."),
("Che cosa stabilì la Constitutio de feudis del 1037?","Estese l'ereditarietà ai feudatari minori, i valvassori",["Tolse i feudi ai valvassori","Vietò la successione ai figli","Cancellò il Capitolare di Quierzy"],"Fu emanata dall'imperatore Corrado II e allargò l'ereditarietà ai valvassori."),
("Quale termine sostituì progressivamente «beneficio»?","Feudo",["Contea","Ducato","Marca"],"Il termine germanico «feudo» sostituì «beneficio» e formalizzò la nascita del sistema feudale."),
])
q(3,'Le nuove invasioni e l\'incastellamento',[
("Da dove provenivano i Saraceni?","Dall'Africa del Nord e dalla Sicilia",["Dalla Scandinavia","Dall'Asia centrale","Dalla Spagna cristiana"],"I Saraceni erano pirati musulmani che colpivano le coste italiane e francesi."),
("Che cosa facevano gli Ungari?","Saccheggiavano Germania, Francia e Italia settentrionale",["Attaccavano soltanto l'Irlanda","Navigavano verso l'Islanda","Difendevano le coste italiane"],"Gli Ungari, popolazione asiatica, saccheggiavano la Germania, la Francia e l'Italia settentrionale."),
("Chi erano i Normanni, detti anche Vichinghi?","Navigatori provenienti dalla Scandinavia",["Pirati dell'Africa del Nord","Cavalieri provenienti dall'Asia","Mercanti genovesi"],"Attaccarono Inghilterra, Francia e Irlanda e si stabilirono in zone come la Normandia."),
("Come risposero i signori locali all'insicurezza?","Fortificando i villaggi con palizzate, fossati e castelli di pietra",["Aspettando l'aiuto del re","Abbandonando le campagne","Pagando un tributo agli invasori"],"I signori presero l'iniziativa senza attendere il re."),
("Come si chiama il fenomeno della costruzione dei castelli?","Incastellamento",["Feudalesimo","Vassallaggio","Frammentazione"],"L'incastellamento permise ai signori di consolidare il controllo politico ed economico sul territorio."),
])
q(4,'I poteri di banno e la rete di relazioni',[
("Che cosa erano i poteri di banno?","Diritti originariamente regi di cui i signori si appropriarono",["Tasse pagate al papa","Cariche ecclesiastiche","Privilegi dei soli contadini"],"Erano diritti del re che i signori locali presero per sé."),
("Quale di questi NON è un potere di banno?","L'elezione del papa",["La difesa militare","L'amministrazione della giustizia","La riscossione delle tasse"],"I poteri di banno comprendevano difesa militare, giustizia, tasse e corvées."),
("Che cosa sono le corvées?","Giornate di lavoro obbligatorie e gratuite dei contadini",["Tributi pagati in denaro dai mercanti","Feste religiose","Titoli nobiliari"],"Erano giornate di lavoro imposte ai contadini senza compenso."),
("Che cosa pensano oggi gli storici della «piramide feudale»?","L'hanno superata come idea classica",["La considerano una descrizione esatta","La attribuiscono a Carlo Magno","La vedono solo nell'Italia del Sud"],"La realtà era una complessa rete di relazioni."),
("Che cosa poteva accadere a un vassallo, secondo il docente?","Poteva essere legato a più signori contemporaneamente",["Poteva avere un solo signore, il re","Non poteva giurare fedeltà","Doveva vivere sempre alla corte"],"Questo creava frequenti conflitti di interesse e guerre locali."),
])
q(5,'Francia e Italia',[
("Chi fu eletto re di Francia nel 987?","Ugo Capeto",["Ottone I","Carlo il Calvo","Corrado II"],"Con Ugo Capeto comincia la dinastia dei Capetingi."),
("Quanto era esteso, all'inizio, il potere effettivo dei Capetingi?","Alla regione tra Parigi e Orléans",["A tutta la Francia","A Francia e Germania","Alla sola Normandia"],"Il resto del territorio era in mano a potenti duchi e conti."),
("Come era la situazione politica dell'Italia?","Frammentata e instabile",["Unita sotto un solo re","Governata dai Capetingi","Sotto il controllo dei Normanni"],"L'Italia era divisa tra più poteri."),
("Che cosa si estendeva al centro dell'Italia?","Lo Stato della Chiesa",["Il Regno di Francia","Il Califfato di Cordova","Il Ducato di Normandia"],"Al centro c'era lo Stato della Chiesa."),
("Chi aveva conquistato la Sicilia?","Gli arabi",["I Franchi","I Capetingi","Gli Ungari"],"Il Sud era diviso tra domini longobardi, territori bizantini e la Sicilia conquistata dagli arabi."),
])
q(6,'Ottone I e il Sacro Romano Impero',[
("Quale dinastia segnò la svolta nel Regno di Germania?","La dinastia di Sassonia",["La dinastia dei Capetingi","La dinastia carolingia","La dinastia normanna"],"Prima Enrico I l'Uccellatore e poi il figlio Ottone I."),
("Quale vittoria diede grande prestigio a Ottone I?","La battaglia di Lechfeld, nel 955, contro gli Ungari",["La battaglia di Poitiers","La conquista della Sicilia","La presa di Parigi"],"Sconfisse definitivamente gli Ungari, bloccando le loro invasioni."),
("Quando e da chi fu incoronato imperatore Ottone I?","Nel 962, da papa Giovanni XII",["Nel 877, da papa Silvestro II","Nel 987, da Ugo Capeto","Nel 1037, da Corrado II"],"Nacque così il Sacro Romano Impero Germanico."),
("Quale differenza c'era rispetto all'impero di Carlo Magno?","Il nuovo impero escludeva la Francia",["Comprendeva anche l'Inghilterra","Era incentrato sulla Francia","Non includeva l'Italia"],"Era fortemente incentrato su Germania e Italia."),
("Che cosa stabilì il Privilegium Othonis?","Che l'elezione del papa richiedeva il consenso dell'imperatore",["Che il papa eleggeva l'imperatore","Che i feudi diventavano ereditari","Che i vescovi potevano sposarsi"],"Sottometteva di fatto il pontefice al controllo imperiale."),
])
q(7,'La strategia dei vescovi-conti',[
("A chi Ottone I affidò poteri pubblici e territori?","Ai vescovi anziché ai nobili laici",["Ai soli valvassori","Ai contadini liberi","Ai mercanti"],"Era la strategia dei vescovi-conti."),
("Contro quale effetto era diretta questa strategia?","L'ereditarietà dei feudi introdotta dal Capitolare di Quierzy",["Le invasioni dei Normanni","Il potere del papa","La perdita della Sicilia"],"Ottone voleva contrastare l'ereditarietà dei feudi."),
("Perché i vescovi non potevano avere figli legittimi?","Per l'obbligo del celibato",["Per un divieto del re","Perché non possedevano terre","Per una legge dei Capetingi"],"Per il celibato non potevano avere eredi legittimi."),
("Che cosa accadeva ai feudi alla morte di un vescovo?","Tornavano automaticamente al sovrano",["Passavano ai figli","Erano distrutti","Passavano ai contadini"],"Il sovrano poteva così riassegnarli."),
("Che cosa guadagnava il sovrano con questa strategia?","Il controllo sulle terre, che tornavano a lui",["Il diritto di eleggere i duchi","Il titolo di papa","L'esenzione dalle tasse"],"I feudi non restavano nelle famiglie dei nobili."),
])
q(8,'Ottone III e la fine della dinastia',[
("Che cosa sognò Ottone III?","La renovatio imperii, la rinascita dell'antico Impero romano",["La conquista della Francia","L'abolizione del papato","La divisione dell'impero"],"Voleva far rinascere l'antico Impero romano."),
("Dove trasferì la sua corte?","A Roma",["A Parigi","A Palermo","A Aquisgrana"],"Trasferì la corte a Roma."),
("Con quale papa strinse un forte legame?","Silvestro II",["Giovanni XII","Corrado II","Ugo Capeto"],"Il legame fu con papa Silvestro II."),
("Perché i suoi piani fallirono?","A causa delle rivolte dell'aristocrazia romana",["Per una sconfitta contro gli Ungari","Per l'invasione dei Saraceni","Per un decreto del papa"],"Le rivolte dell'aristocrazia romana bloccarono il progetto."),
("Che cosa accadde nel 1002?","Ottone III morì senza eredi e si estinse la dinastia degli Ottoni",["Nacque il Sacro Romano Impero","Fu eletto Ugo Capeto","Fu emanata la Constitutio de feudis"],"La morte prematura senza eredi aprì nuove ribellioni e indebolì il potere imperiale."),
])
json.dump(Q,open('/home/user/lav/l01/quiz_argomenti.json','w'),ensure_ascii=False,indent=1)
print(len(Q),sum(len(v['items']) for v in Q.values()))
