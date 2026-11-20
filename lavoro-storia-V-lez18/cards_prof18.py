# -*- coding: utf-8 -*-
"""Storia V · Lez. 18 · card dalle parole del prof (secondi dell'originale, 4274 s).

Uso:  python3 cards_prof18.py            -> controlla i vincoli e scrive cards_prof18.json + CARD_LEZ18.md
Regole (note della master): 2-3 card per slide, nessuna slide ferma oltre 180 s,
card = frase/punto intero, card sola solo con immagine.
Ogni card: (inizio, fine, titolo, parola chiave, testo). Le card di una slide sono
contigue e coprono tutta la finestra della slide; le slide sono contigue da 0 a 4274.
Parte 1 = introduzione + argomenti 1-3 (0-2129.7), Parte 2 = argomenti 4-6 (2129.7-4274).
"""
import json, sys, os

DUR = 4274.0
SPLIT = 2129.7          # taglio tra Parte 1 e Parte 2 (fine argomento 3)
MAXSLIDE = 180.0

ARG = {1: "Un Paese da ricostruire", 2: "La nascita della Repubblica", 3: "La Costituzione",
       4: "Il Centrismo (1948-1953)", 5: "Il miracolo economico", 6: "Il Centrosinistra (1953-1963)"}

# (id, argomento, titolo slide, [ (a, b, titolo, kw, testo), ... ])
S = []
def slide(i, arg, titolo, cards, **extra):
    S.append(dict(id=i, tipo="card", arg=arg, titolo=titolo, cards=cards, **extra))
def img(i, arg, a, b, didascalia, file):
    S.append(dict(id=i, tipo="immagine", arg=arg, a=a, b=b, didascalia=didascalia, immagine=file))

# ---------------------------------------------------------------- introduzione
S.append(dict(id="COP", tipo="copertina", arg=0, a=0.0, b=113.0,
              nota="introduzione sulla copertina; a 113 s (inizio di frase) la slide «Di cosa parliamo»"))
S.append(dict(id="AGE", tipo="agenda", arg=0, a=113.0, b=187.7, titolo="Di cosa parliamo",
              voci=[ARG[k] for k in range(1, 7)]))

# ---------------------------------------------------------------- argomento 1
slide("1.1", 1, "Un Paese materialmente devastato", [
 (187.7, 223.7, "Una profonda trasformazione", "Ricostruzione",
  "All'indomani della seconda guerra mondiale l'Italia affronta una profonda trasformazione: gravissime difficoltà economiche e sociali, ma anche una straordinaria spinta verso la ricostruzione democratica."),
 (223.7, 296.6, "I bombardamenti", "Bombardamenti",
  "Il Paese esce dal conflitto devastato: fino ad aprile-maggio 1945 il Nord resta in mano ai nazifascisti e i bombardamenti continuano proprio dove si concentrano le industrie; strade e ferrovie sono interrotte."),
 (296.6, 348.7, "Le rappresaglie naziste", "Rappresaglie",
  "Ai bombardamenti alleati si aggiungono le rappresaglie naziste, con le decimazioni (dieci italiani fucilati per ogni tedesco morto); i tedeschi in fuga fanno saltare i ponti per rallentare i nemici."),
])
slide("1.2", 1, "Un'economia in ginocchio", [
 (348.7, 391.2, "Da riconvertire e ricostruire", "Industrie",
  "Reti di trasporto saltate e impianti industriali messi a dura prova: bisogna riconvertire l'apparato bellico in produzione civile. Le stime parlano di circa il 20% delle industrie distrutte."),
 (391.2, 462.9, "Inflazione e mercato nero", "Mercato nero",
  "Inflazione galoppante e scarsità di beni alimentari: il mercato nero fa da padrone, con prodotti a prezzi altissimi. L'abolizione del prezzo politico del pane fa crescere la borsa nera e la povertà delle famiglie."),
 (462.9, 484.8, "Ricostruire senza sapere come", "Sopravvivere",
  "Finita la guerra ognuno deve cavarsela da solo. Oggi sappiamo che arriverà il Piano Marshall, ma all'epoca la maggior parte delle persone non sapeva nemmeno se il giorno dopo avrebbe mangiato."),
])
slide("1.3", 1, "Un clima di violenza: il Sud", [
 (484.8, 531.6, "Le lotte contadine", "Latifondi",
  "Nel Mezzogiorno le tensioni sono esasperate dalle lotte contadine per la redistribuzione delle terre dei latifondisti: «dateci le terre». Molte rivolte hanno ispirazione social-comunista e la forza pubblica le reprime."),
 (531.6, 587.9, "Mafia e Stato debole", "Mafia",
  "In parte queste lotte sono viziate da elementi mafiosi infiltrati, e la mafia approfitta anche del mercato nero. Le istituzioni locali sono deboli e il Paese è allo sbando, anche al Sud, dove la guerra era finita già nel 1943."),
])
slide("1.4", 1, "Un clima di violenza: il Centro-Nord", [
 (587.9, 627.4, "Regolamenti di conti", "Guerra civile",
  "Nel Centro-Nord, ancora più in guerra civile, gli antifascisti si vendicano sui fascisti: ex federali, vecchi podestà e miliziani vengono cercati nelle loro case e in molti casi uccisi."),
 (627.4, 664.6, "Un Paese sgomento", "Strascichi",
  "Sono gli ultimi strascichi di un'esperienza, quella fascista, nata con la violenza e poi perduta su quasi tutti i fronti: l'Italia resta sgomenta, arrabbiata e materialmente più povera di prima."),
])

# ---------------------------------------------------------------- argomento 2
slide("2.1", 2, "La pacificazione nazionale", [
 (664.6, 716.7, "Un governo di unità nazionale", "Pacificazione",
  "Urge la pacificazione nazionale, perseguita da Togliatti, ministro di Giustizia nel governo De Gasperi: un governo di unità nazionale con tutti i partiti antifascisti, tranne i repubblicani, che non possono governare sotto un re."),
 (716.7, 753.8, "L'amnistia", "Amnistia",
  "Togliatti e il governo promuovono un'ampia amnistia per i reati politici commessi durante la guerra: per questo in Italia non ci sarà un processo di Norimberga o di Tokyo."),
 (753.8, 790.5, "Un perdono necessario", "Perdono",
  "Sono le stranezze italiane, ma anche una necessità psicologica: superare in ogni modo quello che c'è stato e costruire un Paese democratico migliore di prima, anche a costo di perdonare i fascisti."),
])
slide("2.2", 2, "Un'amnistia per tutti", [
 (790.5, 817.4, "Per fascisti e partigiani", "Crimini di guerra",
  "L'amnistia copre tutte le violenze della guerra, quelle dei fascisti ma anche dei partigiani, che avevano ucciso dei fascisti: erano comunque italiani."),
 (817.4, 848.0, "L'unico modo per pacificare", "Pacificazione",
  "Il governo De Gasperi, abbastanza moderato, pensa che l'unico modo per pacificare il Paese sia un'amnistia generalizzata, per fascisti e antifascisti: per questo l'Italia non fa nessun processo come quelli di Norimberga e di Tokyo."),
])
img("2.I1", 2, 848.0, 880.9,
    "Alcide De Gasperi, ultimo presidente del Consiglio del Regno d'Italia e primo della Repubblica Italiana", "De Gasperi")
slide("2.3", 2, "Il panorama politico: il CLN e i tre partiti", [
 (880.9, 954.0, "Il Comitato di Liberazione Nazionale", "CLN",
  "Il CLN riunisce le forze antifasciste disposte a collaborare con il re e con gli anglo-americani. Nel Sud già libero, dove si rifugia il re, i partiti sono di nuovo legali e i leader accorrono, Togliatti dall'Unione Sovietica."),
 (954.0, 1018.5, "I tre grandi partiti", "DC · PSI · PCI",
  "I più importanti sono la Democrazia Cristiana di De Gasperi (erede del Partito popolare), il PSI di Pietro Nenni e il PCI di Palmiro Togliatti: saranno i più votati e scriveranno in buona parte la Costituzione."),
])
slide("2.4", 2, "Gli altri partiti e il governo De Gasperi", [
 (1018.5, 1061.3, "Le forze minori", "Altri partiti",
  "Nel CLN ci sono anche il Partito d'Azione, che poi si dissolverà a vantaggio dei socialisti, e i liberali, pochi. I repubblicani restano fuori: non vogliono avere a che fare con il re che aveva consegnato il Paese a Mussolini."),
 (1061.3, 1101.7, "Verso il referendum", "Governo De Gasperi",
  "Da dicembre 1945 il governo De Gasperi guida il Paese con democristiani, socialisti e comunisti, fino a giugno 1946: poi ci sarà il famoso referendum sulla forma politica dello Stato."),
])
slide("2.5", 2, "I primi governi: da Parri a De Gasperi", [
 (1101.7, 1156.4, "Il governo Parri", "Parri",
  "Roma è stata liberata nel giugno 1944. Finita la guerra, il governo Bonomi si dimette e nel giugno 1945 inizia il primo governo di unità nazionale del dopoguerra, guidato dal partigiano Ferruccio Parri."),
 (1156.4, 1235.5, "Un'epurazione impossibile", "Epurazione",
  "Parri vorrebbe una sorta di Norimberga per i fascisti, ma la DC, la Chiesa e i liberali frenano: punire tutti significherebbe azzerare la classe dirigente dello Stato, e come si farebbe a mandarlo avanti?"),
 (1235.5, 1259.6, "Si tollera e si perdona", "Amnistia",
  "Si tollerò e si fece l'amnistia: Parri, troppo radicale, lascia il posto a un governo De Gasperi più moderato, che lavorerà all'amnistia."),
])
slide("2.6", 2, "I partiti di massa", [
 (1259.6, 1311.4, "Due anime: moderati e rivoluzionari", "Partiti di massa",
  "Si affermano i grandi partiti di massa: da una parte i moderati democristiani, dall'altra i rivoluzionari social-comunisti. Repubblicani e liberali pesano poco, perché legati al mondo prefascista che non aveva fermato Mussolini."),
 (1311.4, 1362.1, "DC, PCI e PSI", "De Gasperi",
  "La DC di De Gasperi, trentino già deputato nell'impero austro-ungarico, è sostenuta dalla Chiesa e dai moderati. Il PCI di Togliatti e il PSI di Nenni riempiono le piazze con centinaia di migliaia di persone."),
 (1362.1, 1411.9, "Formazioni minori e monarchici", "Monarchici",
  "Accanto ai partiti di massa ci sono il Partito d'Azione, i liberali, che sosterranno sempre la DC, e i monarchici, che vorrebbero mantenere la monarchia mentre lo Stato si avvia a trasformarsi."),
])
slide("2.7", 2, "L'Uomo Qualunque e il Movimento sociale italiano", [
 (1411.9, 1486.0, "L'Uomo Qualunque", "Qualunquismo",
  "Nasce una destra qualunquista, né fascista né moderata, antipolitica e antistatale: «non mi interessa nulla, mi occupo solo del mio, lo Stato è cattivo perché ci spreme di tasse». Il movimento, antisistema, si scioglie pochi anni dopo."),
 (1486.0, 1526.2, "Il Movimento sociale italiano", "MSI",
  "C'è anche un partito fascista, che non può chiamarsi così: il Movimento sociale italiano, che si richiama alla Repubblica Sociale di Mussolini ed è fondato da un ex federale, un ex governatore provinciale fascista."),
])
slide("2.8", 2, "Il MSI: un partito parafascista", [
 (1526.2, 1570.1, "Violenza accantonata, classe dirigente fascista", "Neofascismo",
  "Per concorrere alle elezioni il MSI rinuncia alla componente di violenza, ma i suoi dirigenti e candidati appartenevano tutti al fascismo; dicono di essersi riconvertiti alla democrazia e non faranno campagne elettorali minacciando violenze."),
 (1570.1, 1630.8, "Parafascista, non ancora post-fascista", "Parafascista",
  "Per storici e politologi è un partito «parafascista», non ancora post-fascista. Col tempo supererà molti aspetti del fascismo e il nucleo di quelle idee confluirà in formazioni successive."),
])
slide("2.9", 2, "Il referendum del 2 giugno 1946", [
 (1630.8, 1684.3, "La svolta istituzionale", "Referendum",
  "Il 2 giugno 1946 il referendum istituzionale: per la prima volta votano le donne. Il voto, e poi anche la possibilità di essere elette, era già stato concesso nel 1945 dal governo Bonomi, ancora sotto la monarchia."),
 (1684.3, 1707.8, "12 milioni contro 10", "Repubblica o Monarchia",
  "Circa 12 milioni di voti vanno alla Repubblica e circa 10 milioni alla Monarchia. I monarchici contestano il risultato, ma i documenti storici confermano la vittoria repubblicana."),
 (1707.8, 1757.2, "Un voto antimonarchico", "Perché la Repubblica",
  "La Repubblica trionfa al Nord e al Centro: in Toscana ed Emilia-Romagna socialismo e comunismo erano fortissimi, al Nord si ricordava la guerra partigiana. Fu un voto antimonarchico, perché la monarchia era legata al fascismo."),
])
slide("2.10", 2, "Nasce la Repubblica", [
 (1757.2, 1805.0, "Umberto II, re per un mese", "Umberto II",
  "La monarchia prende 10 milioni di voti da moderati, ex fascisti e nobili. Vittorio Emanuele III aveva abdicato a favore del figlio Umberto II, re per un solo mese, che dopo il voto parte per l'esilio in Portogallo."),
 (1805.0, 1839.6, "Nasce la Repubblica Italiana", "Costituente",
  "Con lo stesso voto si eleggono i rappresentanti dell'Assemblea costituente: se avesse vinto la monarchia, la nuova Costituzione sarebbe stata democratica ma monarchica; ha vinto la Repubblica, quindi sarà democratica e repubblicana."),
])

# ---------------------------------------------------------------- argomento 3
slide("3.1", 3, "L'Assemblea costituente e le madri costituenti", [
 (1839.6, 1884.6, "556 deputati alla Costituente", "Assemblea costituente",
  "Vengono eletti 556 deputati costituenti. Il primo partito è la DC, con circa il 35% dei seggi, che raccoglie voti di repubblicani e di moderati che non possono votare social-comunista: una forza a metà tra due anime."),
 (1884.6, 1938.0, "Le madri costituenti", "21 donne",
  "Tra i 556 costituenti emergono 21 donne elette, le prime nella storia dell'Italia unita, ricordate come madri costituenti: democristiane, comuniste, socialiste, qualunquiste, un gruppo trasversale a tutti i partiti."),
 (1938.0, 1984.3, "Uguaglianza e famiglia", "Uguaglianza di genere",
  "Le costituenti garantiscono l'uguaglianza di genere davanti alla legge e la tutela della famiglia, voluta dai cattolici. Ma nelle leggi ordinarie il capo famiglia resta il maschio: ci vorranno decenni per superare il patriarcato."),
])
slide("3.2", 3, "La Costituzione repubblicana", [
 (1984.3, 2030.4, "La stesura e l'entrata in vigore", "1° gennaio 1948",
  "La Costituzione è scritta nel corso del 1947, non senza tensioni (i comunisti vorrebbero una sola camera). Firmata dal presidente provvisorio Enrico De Nicola, entra in vigore il 1° gennaio 1948, sotto il governo De Gasperi."),
 (2030.4, 2076.7, "Una struttura simile allo Statuto", "Tre poteri",
  "Ricorda lo Statuto del Regno: il Parlamento ha due camere dotate di potere legislativo, e ora anche il Senato è elettivo; l'esecutivo appartiene al governo e la magistratura ha il potere giudiziario."),
 (2076.7, 2129.7, "La fiducia al Parlamento", "Fiducia",
  "Nel Regno il governo era scelto dal re e restava finché il re voleva; nella Repubblica deve ottenere la fiducia del Parlamento, espressione del voto popolare. Sciolta la Costituente, si vota per la prima legislatura, di cinque anni."),
])

# ---------------------------------------------------------------- argomento 4
slide("4.1", 4, "Il Centrismo (1948-1953)", [
 (2129.7, 2157.6, "Perché «centrismo»", "Centro",
  "Il centrismo è la fase in cui la forza centrale è la Democrazia Cristiana: né di destra nazionalista né di sinistra social-comunista, ma un centro moderato e confessionale cattolico."),
 (2157.6, 2208.0, "Anticomunismo e filoamericanismo", "Filoamericanismo",
  "È una stagione di legislazione sociale ma anche cattolica, di anticomunismo e di buoni rapporti con gli Stati Uniti, perché è da lì che arrivano i soldi."),
])
slide("4.2", 4, "La conferenza di pace di Parigi", [
 (2208.0, 2294.1, "I trattati di pace", "Conferenza di Parigi",
  "La guerra non è ancora finita formalmente: alla conferenza di pace di Parigi si firmano i trattati e si fissano i confini. De Gasperi, che sotto Mussolini si era opposto, ne sente comunque tutta la responsabilità e cerca il perdono del mondo."),
 (2294.1, 2336.2, "Il perdono del mondo", "Cambio di fronte",
  "L'Italia lo ottiene perché il re e la classe dirigente avevano cacciato Mussolini e cambiato fronte con gli anglo-americani: così non viene divisa come la Germania né occupata per anni come il Giappone."),
 (2336.2, 2371.4, "Nell'orbita americana", "NATO",
  "L'Italia entrerà nell'orbita americana con la NATO, anche se la sua classe dirigente (magistrati, dipendenti pubblici, docenti) è ancora in parte parafascista: debole economicamente, sarà un partner essenziale."),
], immagine="confine", inserti=[dict(a=2238.0, b=2246.0, immagine="De Gasperi")])
slide("4.3", 4, "Cosa perde l'Italia", [
 (2371.4, 2423.1, "Colonie e indennità", "Pace di Parigi",
  "Con la pace di Parigi (febbraio 1947) l'Italia perde le colonie, cede alla Francia Tenda e Briga e paga indennità alle nazioni che ha aggredito, tra cui Jugoslavia, Grecia, Unione Sovietica ed Etiopia."),
 (2423.1, 2478.3, "L'Istria e Trieste", "Confine orientale",
  "L'Istria è ceduta alla Jugoslavia; Trieste, contesa, è divisa in Zona A anglo-americana, che tornerà all'Italia, e Zona B jugoslava, che non sarà più italiana. Al confine con una potenza comunista l'Italia diventa centrale per l'Occidente."),
], immagine="confine")
slide("4.4", 4, "Le elezioni del 1948", [
 (2478.3, 2528.6, "La rottura dell'unità antifascista", "Elezioni 1948",
  "Il 1948 segna la rottura definitiva dell'unità antifascista: comunisti e socialisti sono esclusi dal governo. Alle prime elezioni per il Parlamento la DC prende il 48% dei voti, quasi la maggioranza assoluta, con i voti di moderati, monarchici, liberali ed ex fascisti."),
 (2528.6, 2592.8, "Governi De Gasperi e Piano Marshall", "Piano Marshall",
  "Partono i governi del centrismo, tre governi De Gasperi in successione (1948-1953), sotto l'influenza della guerra fredda e degli aiuti del Piano Marshall, regalati in gran parte anche in chiave antisovietica. Stalin sperava in una rivoluzione in Italia, ma non andrà così."),
])
slide("4.5", 4, "Il trionfo della DC e le tensioni sociali", [
 (2592.8, 2641.2, "La propaganda della DC", "Propaganda",
  "Nei manifesti del 1948 la DC dice: votare PCI o PSI significa votare Stalin e la dittatura; votare DC significa America, soldi, benessere, lavoro e famiglia. Fa breccia soprattutto tra i contadini, che erano tanti."),
 (2641.2, 2684.0, "Governi con piccoli alleati", "Alleati laici",
  "La DC vince con i voti dei moderati, della tradizione, dei filoamericani e della «paura rossa». Governa con piccoli partiti laici (repubblicani, liberali, socialdemocratici): con il 48% deve arrivare al 51% per governare."),
 (2684.0, 2746.9, "Stabilità e tensioni sociali", "Attentato a Togliatti",
  "Il periodo è stabile ma con forti tensioni: l'attentato a Togliatti (luglio 1948) porta il Paese sull'orlo della guerra civile; seguono dura repressione di ex partigiani e sindacati e progressiva delegittimazione della Resistenza."),
])
slide("4.6", 4, "Gli interventi pubblici ed economici", [
 (2746.9, 2790.1, "La stabilità della lira", "Einaudi",
  "I governi centristi avviano importanti interventi pubblici ed economici, con i beni del Piano Marshall e una linea di stabilità monetaria promossa dal primo presidente della Repubblica, Luigi Einaudi: la lira, poverissima, si stabilizza grazie ai dollari."),
 (2790.1, 2842.5, "Riforma agraria e Cassa per il Mezzogiorno", "Riforma agraria",
  "Con la riforma agraria, per decreto di De Gasperi, la terra è ridistribuita ai contadini, con incentivi per gli agrari che perdono terreni: si toglie una bandiera alla rivoluzione comunista. Nasce la Cassa per il Mezzogiorno, che finanzia il Sud con benefici ma anche inefficienze."),
])
slide("4.7", 4, "Politica estera e democrazia", [
 (2842.5, 2874.9, "L'integrazione nel blocco occidentale", "NATO · CECA",
  "In politica estera l'Italia sceglie il blocco occidentale: entra nella NATO nell'aprile 1949 e partecipa alle prime tappe dell'integrazione europea, dalla CECA (l'Europa dei Sei) ai trattati di Roma del 1957."),
 (2874.9, 2926.6, "Una democrazia tollerante", "Democrazia",
  "L'Italia si accredita come nazione democratica e parlamentare, anticomunista ma non antiliberale: né il PCI né il MSI vengono messi al bando. Il centrismo allontana le ali estreme: le sinistre volevano una repubblica atea e comunista, le destre ancora il Duce."),
])
img("4.I1", 4, 2926.6, 2969.6,
    "Piano INA-Casa: case costruite con i soldi pubblici per le famiglie che vivevano in grotte, cantine e solai", "INA-Casa")
slide("4.8", 4, "Gli anni Cinquanta e la DC", [
 (2969.6, 3009.0, "Il ritorno alla normalità", "Anni Cinquanta",
  "Negli anni Cinquanta l'Italia colma il divario: per bilancio dello Stato e occupazione torna alla situazione prebellica, fascismo o meno. È normalità, non ancora crescita, ma gli anni Cinquanta prefigurano il boom."),
 (3009.0, 3079.0, "Una DC di massa ma divisa", "Correnti DC",
  "De Gasperi non è più presidente del Consiglio ed è morto: seguono altri governi democristiani (Segni, Fanfani, Pella, Scelba). La DC ha una corrente di destra, spesso autoritaria e parafascista, e una di sinistra, vicina al cattolicesimo sociale e al dialogo con i socialisti."),
])
slide("4.9", 4, "La crisi del centrismo", [
 (3079.0, 3124.0, "Una Costituzione non attuata", "Corte costituzionale",
  "Il centrismo entra in crisi negli anni Cinquanta per l'instabilità, le correnti e la crescente domanda di riforme: la Costituzione prevede la Corte costituzionale e le Regioni, ma dieci anni dopo non esistono ancora."),
 (3124.0, 3163.8, "Leggi ancora fasciste", "Codice Rocco",
  "Restano in vigore leggi del fascismo, come il Codice Rocco. La società vuole essere più moderna e le sinistre chiedono il divorzio, che in Francia esiste dall'inizio dell'Ottocento ma in Italia non c'è ancora."),
])

# ---------------------------------------------------------------- argomento 5
slide("5.1", 5, "Il miracolo economico (1958-1963)", [
 (3163.8, 3234.4, "Da Paese agricolo a potenza industriale", "Boom economico",
  "Tra il 1958 e il 1963 si verifica il miracolo economico: un Paese essenzialmente agricolo diventa una potenza industriale, magari di serie B. Gli operai e il settore secondario superano l'agricoltura, dove fino agli anni Cinquanta lavorava la maggior parte degli italiani."),
 (3234.4, 3280.2, "Auto ed elettrodomestici", "Fiat 500",
  "Il boom è trainato dall'automobile (la Fiat 500, a prezzi popolari, e l'acquisto a rate) e dall'arrivo in ogni casa di frigorifero e lavatrice: le donne non devono più lavare i panni al fiume. Negli anni Sessanta arriva la televisione."),
])
slide("5.2", 5, "Crescita economica e nuovi stili di vita", [
 (3280.2, 3314.7, "Siderurgia, chimica e auto", "Export",
  "Siderurgia, chimica e settore automobilistico fanno da padroni e i prodotti italiani si fanno apprezzare all'estero. C'è crescita economica, ma non dei salari, ancora quasi quelli dell'anteguerra: i lavoratori vorrebbero una ricchezza meglio distribuita."),
 (3314.7, 3376.7, "Consumi, vacanze e ferie pagate", "Vacanze di massa",
  "La crescita cambia consumi e stili di vita: motorizzazione di massa, televisore e vacanze balneari. Prima né il contadino né l'operaio andavano in vacanza; ora, con le ferie retribuite volute dalle sinistre nella Costituzione, nasce il turismo di massa."),
])
slide("5.3", 5, "Le criticità del boom", [
 (3376.7, 3432.4, "Più case, speculazione, emigrazione", "Abusivismo",
  "Si fanno più figli e si costruisce di più, chiudendo un occhio sulle regole: palazzinari e abusivismo edilizio, anche sulle spiagge. Il lavoro è al Nord e dal Sud parte una massiccia emigrazione interna: il sogno è la Fiat, la stabilità."),
 (3432.4, 3501.2, "Torino e le periferie", "Periferie",
  "Torino diventa la città più meridionale del Nord: due terzi dei suoi abitanti sono di origine meridionale. Operai con contratto stabile dormono sulle panchine della stazione perché molti non affittano ai meridionali; le periferie triplicano ma senza servizi, mentre il Sud si spopola."),
])

# ---------------------------------------------------------------- argomento 6
slide("6.1", 6, "Il centrosinistra: l'apertura ai socialisti", [
 (3501.2, 3584.1, "La DC si apre ai socialisti", "Fanfani e Moro",
  "Per rispondere ai cambiamenti sociali la DC di sinistra, con Amintore Fanfani e poi Aldo Moro, si avvicina ai socialisti, che rinunciano alla vicinanza a Unione Sovietica e PCI. Il governo Fanfani (1960-62) è sostenuto in Parlamento anche dal PSI, in cambio di riforme sociali."),
 (3584.1, 3647.2, "La scuola media unica", "Scuola media unica",
  "Prima del 1962 i figli dei ricchi andavano alla scuola media che portava a ginnasio e liceo, i figli dei poveri all'avviamento professionale. Su richiesta dei socialisti nasce la scuola media unica: tre anni nello stesso istituto per ricchi e poveri, poi si sceglie liceo o istituto tecnico-professionale."),
])
slide("6.2", 6, "Le grandi riforme", [
 (3647.2, 3712.2, "La nazionalizzazione dell'energia elettrica", "ENEL",
  "Nasce l'ENEL, l'ente nazionale per l'energia elettrica: lo Stato controlla la corrente e si fa carico di portarla in tutte le case, non solo in quelle dei ricchi del centro. Con capitali pubblici le bollette non saranno altissime, per aiutare le classi povere."),
 (3712.2, 3742.9, "Obbligo scolastico fino a 14 anni", "Obbligo scolastico",
  "Viene rafforzato l'obbligo scolastico fino a 14 anni, già previsto dal ministro Gentile durante il fascismo. Il dialogo con i socialisti prepara, alle elezioni del 1963, il primo governo organico di centrosinistra."),
])
slide("6.3", 6, "Dal dialogo al governo", [
 (3742.9, 3781.4, "I socialisti al governo", "Governo Moro",
  "Negli anni Cinquanta c'era solo un dialogo; dal 1963, con il primo governo Moro a guida democristiana, i socialisti entrano al governo come ministri: Pietro Nenni sarà ministro di Moro. Nel 1964 muore Palmiro Togliatti."),
 (3781.4, 3815.0, "Il PCI all'opposizione", "Distensione",
  "Sono gli anni del dialogo USA-URSS: il PCI è sempre più all'opposizione e il PSI sempre più al governo. Moro guarda a sinistra e attua una legislazione per i più poveri, che toglie consensi elettorali ai comunisti."),
])
img("6.I1", 6, 3815.0, 3833.1,
    "Amintore Fanfani e Aldo Moro, che guiderà il primo governo organico di centrosinistra nel 1963", "Fanfani e Moro")
slide("6.4", 6, "Il boom in cifre", [
 (3833.1, 3887.9, "Il quinquennio d'oro 1958-1963", "PIL",
  "Il boom economico è il quinquennio 1958-1963 (nel 1964 arriva una prima crisi, poi una ripresa): il PIL cresce del 6,7% all'anno per cinque anni, più del 50% rispetto a prima. L'Italia fa balzi da gigante."),
 (3887.9, 3919.0, "Spesa pubblica e debito", "Debito pubblico",
  "Aumentano le spese pubbliche e il debito pubblico, ma in quegli anni resta inferiore al 100% del PIL (lo supererà dagli anni Ottanta): è l'onda lunga del Piano Marshall e della gestione moderata della DC."),
])
slide("6.5", 6, "L'apertura a sinistra e la Chiesa", [
 (3919.0, 3958.6, "La distensione", "Kennedy · Chruščëv",
  "Nasce il centrosinistra nella fase della distensione: Kennedy e Chruščëv avviano il dialogo, nonostante la crisi di Cuba del 1962. In questi anni c'è anche il pontificato di papa Giovanni XXIII."),
 (3958.6, 4003.1, "Giovanni XXIII e il Concilio", "Concilio Vaticano II",
  "Giovanni XXIII inaugura una svolta epocale: la fine dei papi conservatori. Invita la DC ad aprire a sinistra in chiave sociale («applicate il Vangelo») e apre il Concilio Vaticano II: la messa potrà essere celebrata nelle lingue nazionali."),
 (4003.1, 4063.2, "Integrare le sinistre", "Apertura a sinistra",
  "Il papa vuole integrare le sinistre e farle andare d'accordo con i cattolici in chiave antisovietica e antifascista: «se non riusciamo con i comunisti, riusciremo con i socialisti». Così la DC è tranquilla e Moro può governare con loro."),
])
slide("6.6", 6, "Luci e ombre: il Piano Solo", [
 (4063.2, 4101.1, "Luci e ombre", "Riforme e tensioni",
  "Le riforme del governo Moro, l'apertura della Chiesa e la volontà di distaccarsi da nazionalismo e fascismo scontentano i fascisti ancora presenti in Italia e molti membri degli apparati dello Stato, nostalgici del vecchio ordine."),
 (4101.1, 4167.5, "Il Piano Solo (1964)", "Piano Solo",
  "Nel 1964 le tensioni emergono sui giornali con il Piano Solo, un piano di colpo di Stato con i Carabinieri guidati dal generale De Lorenzo: proclamare lo stato d'emergenza per impedire alle sinistre di restare al potere. Non è mai stato chiarito se fosse un vero piano o solo un modo per spaventare le sinistre."),
])
slide("6.7", 6, "Un'Italia al bivio", [
 (4167.5, 4230.3, "Il piano non scatta", "De Lorenzo",
  "Coinvolti uomini dei servizi segreti e degli apparati dello Stato, anche della magistratura, nostalgici del fascismo. Il colpo di Stato non scatta e il generale De Lorenzo viene fermato: lascia la divisa, ma poi diventa parlamentare nelle file del MSI."),
 (4230.3, 4274.0, "L'Italia all'inizio degli anni Sessanta", "Democrazia parlamentare",
  "Ci si libera della minaccia comunista: i socialisti prendono le distanze e si cerca una piena democrazia parlamentare, liberale e pluripartitica; la DC si apre a sinistra, a destra restano le tensioni. Negli anni Settanta arriveranno terrorismo e stragismo di estrema sinistra e di estrema destra."),
])

# ---------------------------------------------------------------- controlli e uscita
def controlla():
    err = []
    t = 0.0
    for s in S:
        a = s["a"] if s["tipo"] != "card" else s["cards"][0][0]
        b = s["b"] if s["tipo"] != "card" else s["cards"][-1][1]
        if abs(a - t) > 0.05:
            err.append(f"{s['id']}: inizia a {a} ma la precedente finisce a {t}")
        if b - a > MAXSLIDE:
            err.append(f"{s['id']}: ferma {b-a:.1f} s (> {MAXSLIDE:.0f})")
        if s["tipo"] == "card":
            n = len(s["cards"])
            if not 2 <= n <= 3:
                err.append(f"{s['id']}: {n} card")
            p = a
            for (x, y, tit, kw, txt) in s["cards"]:
                if abs(x - p) > 0.05 or y <= x:
                    err.append(f"{s['id']}: card non contigua {x}-{y}")
                p = y
                lim = 245 if n == 3 else 300
                L = len(tit) + len(txt)
                if L > lim + 40:
                    err.append(f"{s['id']}: card «{tit}» lunga {L} caratteri")
                if not txt.rstrip().endswith((".", "»", "?", "!")):
                    err.append(f"{s['id']}: card «{tit}» non finisce con un punto")
        t = b
    if abs(t - DUR) > 0.05:
        err.append(f"fine {t} invece di {DUR}")
    return err

def parte(t):
    return 1 if t < SPLIT else 2

def esporta(base):
    out = []
    for s in S:
        d = dict(s)
        if s["tipo"] == "card":
            d["a"], d["b"] = s["cards"][0][0], s["cards"][-1][1]
            d["cards"] = [dict(a=x, b=y, titolo=tit, kw=kw, testo=txt) for x, y, tit, kw, txt in s["cards"]]
        d["parte"] = parte(d["a"])
        out.append(d)
    json.dump(dict(durata=DUR, taglio_parti=SPLIT, argomenti=ARG, slide=out),
              open(os.path.join(base, "cards_prof18.json"), "w"), ensure_ascii=False, indent=1)
    md = ["# Storia V · Lez. 18 · card dalle parole del prof\n",
          f"Secondi dell'originale ({DUR:.0f} s). Parte 1 = 0–{SPLIT} s, Parte 2 = {SPLIT}–{DUR:.0f} s.\n"]
    k = 0
    for d in out:
        if d["arg"] != k:
            k = d["arg"]
            if k:
                md.append(f"\n## Argomento {k} · {ARG[k]}\n")
        r = f"{d['a']:.1f}–{d['b']:.1f} s ({d['b']-d['a']:.0f} s)"
        if d["tipo"] == "card":
            md.append(f"\n### {d['id']} · {d['titolo']}  \n{r}" + (f" · con immagine «{d['immagine']}»" if d.get("immagine") else "") + "\n")
            for c in d["cards"]:
                md.append(f"- **{c['titolo']}** ({c['a']:.1f}–{c['b']:.1f}) · _{c['kw']}_: {c['testo']}")
        elif d["tipo"] == "immagine":
            md.append(f"\n### {d['id']} · immagine «{d['immagine']}»  \n{r}\n- {d['didascalia']}")
        elif d["tipo"] == "agenda":
            md.append(f"\n### {d['id']} · {d['titolo']}  \n{r}\n- " + "\n- ".join(d["voci"]))
        else:
            md.append(f"\n### {d['id']} · {d['tipo']}  \n{r}\n- {d.get('nota','')}")
    open(os.path.join(base, "CARD_LEZ18.md"), "w").write("\n".join(md) + "\n")
    return out

if __name__ == "__main__":
    e = controlla()
    if e:
        print("\n".join(e)); sys.exit(1)
    base = os.path.dirname(os.path.abspath(__file__))
    out = esporta(base)
    cs = [s for s in out if s["tipo"] == "card"]
    nc = sum(len(s["cards"]) for s in cs)
    mx = max(s["b"] - s["a"] for s in cs)
    print(f"OK: {len(out)} segmenti, {len(cs)} slide con card, {nc} card, "
          f"{sum(1 for s in out if s['tipo']=='immagine')} immagini, slide più lunga {mx:.0f} s")
    for p in (1, 2):
        sl = [s for s in cs if s["parte"] == p]
        print(f"Parte {p}: {len(sl)} slide, {sum(len(s['cards']) for s in sl)} card")
