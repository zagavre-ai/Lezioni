import json, openpyxl
def q(p,a,w,ref): return {"p":p,"a":a,"w":w,"ref":ref}
Q={
"Q1":("Quiz 1 · L'Impero tedesco e la metropoli moderna",[
 q("Quanti abitanti raggiunge la popolazione dell'Impero tedesco nei primi anni del Novecento?","67 milioni",["47 milioni","57 milioni","87 milioni"],"La popolazione tocca i 67 milioni di abitanti."),
 q("Che cos'è l'agorafobia?","La paura delle folle e degli spazi aperti",["La paura dei luoghi chiusi","La paura delle macchine","La paura del buio"],"L'agorafobia è la paura delle folle e degli spazi aperti."),
 q("Che cosa fa Sigmund Freud a Vienna per curare i pazienti con fobie?","Disegna piantine urbane per collegare le fobie agli spazi",["Organizza mostre d'arte","Fonda un'associazione di architetti","Studia la produzione d'acciaio"],"Freud affronta le fobie dei suoi pazienti disegnando piantine urbane."),
 q("Chi analizza nel 1903 le conseguenze della vita metropolitana sulla mente umana?","Il sociologo Georg Simmel",["L'architetto Hermann Muthesius","L'imprenditore Karl Schmidt","Il politico Friedrich Naumann"],"Georg Simmel analizza pubblicamente le conseguenze della vita metropolitana."),
 q("Dove e quando nasce il Deutscher Werkbund?","A Monaco, nel 1907",["A Dresda, nel 1905","A Vienna, nel 1897","A Berlino, nel 1898"],"L'associazione nasce a Monaco nel 1907 per unire arte e industria.")]),
"Q2":("Quiz 2 · Le Secessioni e la svolta espressionista",[
 q("In quali città e anni nascono le Secessioni?","Monaco (1892), Vienna (1897) e Berlino (1898)",["Dresda (1892), Vienna (1905) e Berlino (1911)","Parigi (1874), Vienna (1897) e Londra (1851)","Monaco (1907), Vienna (1903) e Dresda (1898)"],"Le Secessioni nascono a Monaco (1892), Vienna (1897) e Berlino (1898)."),
 q("Contro che cosa si oppongono i gruppi di artisti dissidenti?","Contro le accademie ufficiali",["Contro la fotografia","Contro l'industria","Contro la pittura a olio"],"Gruppi di artisti dissidenti si oppongono alle accademie ufficiali."),
 q("L'Espressionismo sposta il baricentro…","dall'estetica esteriore all'interiorità emotiva",["dall'interiorità all'estetica esteriore","dalla pittura alla scultura","dal colore al disegno"],"Sposta il baricentro dall'estetica esteriore all'interiorità emotiva."),
 q("Quali caratteristiche ha il linguaggio espressionista?","Forme distorte, colori antinaturalistici e forte carica polemica",["Forme armoniose e colori naturali","Prospettiva rigorosa e soggetti mitologici","Pennellata leggera e luce del mattino"],"Forme distorte, colori antinaturalistici e una forte carica polemica."),
 q("A quale mentalità reagisce l'Espressionismo?","Al conformismo borghese",["All'arte medievale","Alla cultura contadina","All'arte orientale"],"Reagisce al conformismo borghese.")]),
"Q3":("Quiz 3 · I precursori: Ensor e Munch",[
 q("Quale artista belga rappresenta l'angoscia della condizione umana con maschere e scheletri?","James Ensor",["Edvard Munch","Ernst Ludwig Kirchner","Paul Klee"],"James Ensor usa visioni grottesche, maschere e scheletri."),
 q("La bambina malata di Munch è radicata nella perdita di chi?","Della sorella Sofie, morta di tubercolosi",["Del padre","Di un amico pittore","Della moglie"],"È radicata nella perdita della sorella Sofie, morta di tubercolosi."),
 q("Da quale ricordo nasce L'urlo?","Da una passeggiata lungo un fiordo all'imbrunire",["Da un viaggio a Parigi","Da una visita a un ospedale","Da una festa a Berlino"],"Nasce dal ricordo di una passeggiata lungo un fiordo all'imbrunire."),
 q("Di che colore si tinge il cielo nell'Urlo?","Rosso sangue, innaturale",["Blu notte","Verde acido","Giallo oro"],"Il cielo si tinge di un rosso sangue, innaturale."),
 q("In Pubertà, che cosa proietta la parete dietro la ragazza?","Un'ombra scura e inquietante, simbolo di un futuro ignoto",["Un paesaggio di montagna","Un vaso di fiori","La luce di una finestra"],"L'ombra scura e inquietante è simbolo di un futuro ignoto.")]),
"Q4":("Quiz 4 · Die Brücke e Kirchner",[
 q("Dove e quando nasce Die Brücke?","A Dresda, nel 1905",["A Monaco, nel 1911","A Berlino, nel 1898","A Vienna, nel 1897"],"Die Brücke è fondato a Dresda nel 1905."),
 q("Da chi è fondato Die Brücke?","Da studenti di architettura come Ernst Ludwig Kirchner",["Da Vasilij Kandinskij e Franz Marc","Da Egon Schiele e Oskar Kokoschka","Da Paul Klee e James Ensor"],"Fondato da studenti di architettura come Kirchner."),
 q("Quale scena descrive Potsdamer Platz?","Una convulsa scena urbana di Berlino prima della Grande Guerra",["Un paesaggio di montagna","Un interno borghese","Una battaglia"],"È l'emblema della nevrosi urbana della Berlino moderna prima della Grande Guerra."),
 q("Chi sta in primo piano su una piattaforma rotonda in Potsdamer Platz?","Due donne in abiti scuri",["Due bambini","Tre cavalli","Un gruppo di soldati"],"In primo piano si stagliano due donne in abiti scuri su una piattaforma rotonda."),
 q("Come sono i colori nelle scene berlinesi di Kirchner?","Lividi, stridenti e antinaturalistici",["Dolci e naturali","Tenui come in un acquerello","Soltanto bianco e nero"],"I colori lividi e stridenti caricano la scena di squallore.")]),
"Q5":("Quiz 5 · Der Blaue Reiter: Marc, Kandinskij e Klee",[
 q("Chi fonda Der Blaue Reiter a Monaco nel 1911?","Vasilij Kandinskij e Franz Marc",["Ernst Ludwig Kirchner e Erich Heckel","Egon Schiele e Oskar Kokoschka","Paul Klee e Edvard Munch"],"Fondato a Monaco nel 1911 da Kandinskij e Marc."),
 q("Verso quale pittura punta Der Blaue Reiter?","Una pittura lirica, spirituale e orientata verso l'astrazione",["Una pittura realistica","Una pittura sulla vita di città","Una pittura religiosa medievale"],"Punta su una pittura lirica, spirituale e orientata verso l'astrazione."),
 q("Che cosa mostrano i Grandi cavalli azzurri di Franz Marc?","Tre cavalli azzurri a testa bassa, in uno spazio senza profondità prospettica",["Un cavaliere in battaglia","Cavalli gialli al galoppo","Una corsa di cavalli a Berlino"],"Tre cavalli di un azzurro intenso pascolano con la testa bassa."),
 q("Come traduce Kandinskij la musica in pittura?","Associando la tonalità dei colori ai suoni degli strumenti musicali",["Dipingendo strumenti musicali","Ritraendo i musicisti","Copiando gli spartiti"],"Associa la tonalità dei colori ai suoni degli strumenti musicali."),
 q("Quale opera di Paul Klee mostra quattro uccellini meccanici su una manovella?","Macchina per cinguettare",["Senecio","Impressione III (Concerto)","Improvvisazione 28"],"Quattro uccellini meccanici appollaiati su un trespolo con manovella.")]),
"Q6":("Quiz 6 · L'Espressionismo austriaco",[
 q("Con quali esperienze mantiene legami l'Espressionismo a Vienna?","Con la pittura simbolista e la Secessione",["Con l'Impressionismo francese","Con il Cubismo","Con il Neoclassicismo"],"Mantiene legami con la pittura simbolista e la Secessione."),
 q("Quali sono i due artisti dell'Espressionismo austriaco in questa lezione?","Oskar Kokoschka ed Egon Schiele",["Ernst Ludwig Kirchner ed Erich Heckel","Vasilij Kandinskij e Franz Marc","James Ensor ed Edvard Munch"],"Oskar Kokoschka ed Egon Schiele."),
 q("Che cosa rappresenta La sposa del vento di Kokoschka?","La tormentata relazione del pittore con Alma Mahler",["Una festa di nozze","Un paesaggio marino","Un ritratto di famiglia"],"Rappresenta la tormentata relazione amorosa con Alma Mahler."),
 q("Chi dipinge Autoritratto nudo, smorfie?","Egon Schiele",["Oskar Kokoschka","Edvard Munch","Franz Marc"],"Schiele si ritrae nudo con il volto distorto in una smorfia."),
 q("Che cosa celebra L'abbraccio di Schiele (1917)?","La passione e l'amore carnale, con un linguaggio lineare tagliente",["Un paesaggio invernale","Una scena di guerra","Una cerimonia religiosa"],"Celebra la passione e l'amore carnale attraverso la cruda anatomia dei corpi.")]),
}
out={k:{"title":t,"items":it} for k,(t,it) in Q.items()}
json.dump(out,open('/tmp/w/out/quiz_argomenti.json','w'),ensure_ascii=False,indent=1)
wb=openpyxl.load_workbook('/tmp/w/d/DOMANDE.LEZIONE.8.xlsx'); ws=wb.active; items=[]
for r in list(ws.iter_rows(values_only=True))[1:]:
    if not r[0]: continue
    items.append({"p":r[0].strip(),"a":r[1],"w":[r[2],r[3],r[4]],"ref":r[1]})
json.dump({"title":"Verifica finale · L'Espressionismo","soglia":0.8,"items":items},open('/tmp/w/out/verifica_finale.json','w'),ensure_ascii=False,indent=1)
comp=[x for x in open('/dev/null')]
print(sum(len(v['items']) for v in out.values()),len(items))
