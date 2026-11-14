# Specifica approfondimenti Lez 9 (Pascoli). Contenuti SOLO da videodispensa, libro (slide) e parole del docente.
import json, os
MAT = "Letteratura italiana"; DOC = "Prof. Giorgio Mazzotti"
def S(titolo, voce, cards=None, **k): return dict(titolo=titolo, voce=voce, cards=cards or [], **k)
def C(k, t, d=""): return dict(k=k, t=t, d=d)
def MP(id, parte, dopo, titolo, intro, rami):
    """rami: (concetto, parola, esempio, voce)"""
    return dict(id=id, parte=parte, dopo=dopo, tipo="mappa",
        mappa=dict(materia=MAT, docente=DOC, titolo=titolo, rami=[dict(concetto=c, parola=p, esempio=e) for c, p, e, v in rami]),
        voci=[intro] + [v for c, p, e, v in rami])
def AN(id, parte, dopo, tipo, titolo, schermate): return dict(id=id, parte=parte, dopo=dopo, tipo=tipo, materia=MAT, titolo=titolo, schermate=schermate)
ANS = []
# ---------------- PARTE 1 · Il primo Novecento e la lirica italiana ----------------
ANS.append(AN("AN1", 1, 1, "linea", "Dal 1903 al 1918: le date da ricordare", [
 S("L'Età giolittiana", "Mettiamo in fila le date. Dal millenovecentotré al millenovecentoquattordici l'Italia è guidata da Giovanni Giolitti. Si parla di Età giolittiana. Giolitti cerca un accordo tra le forze politiche. Lo Stato diventa mediatore nei conflitti sociali, non solo uno strumento di repressione. Nel settembre del millenovecentoundici arriva la guerra di Libia contro l'impero ottomano.",
   [C("1903-1914", "Età giolittiana", "politica dell'equilibrio"), C("1911", "Guerra di Libia", "settembre, contro l'impero ottomano")]),
 S("La guerra", "Il ventotto giugno del millenovecentoquattordici l'attentato di Sarajevo fa scoppiare la Prima guerra mondiale. L'Italia si divide. Entra in guerra il ventiquattro maggio del millenovecentoquindici. Nel millenovecentodiciassette crolla il regime zarista e in Russia ci sono la rivoluzione e la pace di Brest-Litovsk. La guerra finisce nel millenovecentodiciotto.",
   [C("1914", "Sarajevo", "28 giugno, scoppia la guerra"), C("1915", "L'Italia in guerra", "24 maggio"), C("1917", "Rivoluzione russa", "Lenin, pace di Brest-Litovsk")])]))
ANS.append(AN("AN2", 1, 1, "confronto", "Neutralisti e interventisti", [
 S("Un paese diviso", "Nel millenovecentoquattordici l'Italia si spacca. Da una parte ci sono i neutralisti. Sono la maggioranza del Parlamento, i cattolici e i socialisti. Dall'altra gli interventisti: i nazionalisti e alcuni intellettuali, come D'Annunzio e Marinetti. Per gli interventisti la guerra è un'occasione di riscatto nazionale e di rinascita. Il docente ricorda anche un dubbio. L'Italia aveva appena vinto con fatica la guerra di Libia. Non era un esercito molto potente.",
   [C("Neutralisti", "Contro la guerra", "maggioranza del Parlamento, cattolici, socialisti"), C("Interventisti", "A favore della guerra", "nazionalisti, D'Annunzio, Marinetti")])]))
ANS.append(MP("AN3", 1, 1, "L'Età giolittiana e la Grande Guerra", "Ecco la mappa concettuale del quadro storico. Al centro, l'Età giolittiana e la Grande Guerra.", [
 ("La politica", "equilibrio", "Giolitti, 1903-1914", "Primo ramo, la politica. Giolitti cerca l'accordo tra i partiti e fa dello Stato un mediatore."),
 ("Le riforme", "tutele sociali", "scuola fino a 12 anni", "Secondo ramo, le riforme. Tutele per il lavoro di donne e minori, miglior previdenza, obbligo scolastico fino a dodici anni."),
 ("L'economia", "divario Nord-Sud", "triangolo industriale", "Terzo ramo, l'economia. L'industria decolla solo al Nord e il divario con il Sud aumenta."),
 ("La Libia", "colonialismo", "settembre 1911", "Quarto ramo, la Libia. La guerra del millenovecentoundici vuole contrastare disoccupazione ed emigrazione."),
 ("La Grande Guerra", "Sarajevo", "24 maggio 1915", "Quinto ramo, la Grande Guerra. Scoppia dopo Sarajevo. L'Italia entra in guerra il ventiquattro maggio del millenovecentoquindici.")]))
ANS.append(AN("AN4", 1, 2, "scheda", "La nascita dell'italiano popolare", [
 S("Le trincee e la lingua", "Un effetto sorprendente della guerra riguarda la lingua. Nelle trincee soldati di regioni e classi sociali diverse devono comunicare tra loro. Contadini, studenti, professori. Per capirsi superano i dialetti locali. Così nasce l'italiano popolare, una lingua viva usata dalle classi subalterne. È un misto tra italiano ufficiale e forme dialettali. Aiuta anche il servizio militare obbligatorio, e poi l'urbanesimo e l'emigrazione interna. Il docente nota: forse l'Italia, nelle trincee, è davvero unita.",
   [C("", "Italiano popolare", "italiano ufficiale più forme dialettali"), C("", "Omologazione", "guerra, leva obbligatoria, urbanesimo, emigrazione interna")])]))
ANS.append(AN("AN5", 1, 2, "linea", "Le riviste e la crisi delle certezze", [
 S("Le riviste di Firenze", "Alla crisi dei valori si risponde con le riviste, fondate a Firenze. Il Leonardo esce dal millenovecentotré al millenovecentosette. È individualista e antipositivista. La Voce esce dal millenovecentootto al millenovecentosedici, e si concentra sull'impegno etico, civile e culturale. Lacerba esce dal millenovecentotredici al millenovecentoquindici, ed è legata alla avanguardia futurista e all'interventismo.",
   [C("1903-07", "Il Leonardo", "individualista, antipositivista"), C("1908-16", "La Voce", "impegno etico e civile"), C("1913-15", "Lacerba", "avanguardia futurista, interventismo")]),
 S("Le nuove idee", "Intanto crolla la fiducia cieca nella scienza e nel progresso. È la crisi del Positivismo. Arrivano nuove teorie. La psicoanalisi di Freud scopre l'inconscio. La teoria della relatività di Einstein cambia i concetti di tempo e di spazio. Il docente cita anche Nietzsche e Bergson. Per molti storici, il Novecento comincia davvero dopo la Prima guerra mondiale.",
   [C("", "Freud", "la scoperta dell'inconscio"), C("", "Einstein", "la relatività di tempo e spazio")])]))
ANS.append(AN("AN5b", 1, 2, "parole", "Parole chiave della crisi del Positivismo", [
 S("Tre parole", "Tre parole chiave. Positivismo: la fiducia cieca nella scienza e nel progresso illimitato, tipica della fine dell'Ottocento. Dopo i massacri della guerra, molti pensano che non fosse vero che andava sempre meglio. Psicoanalisi: la teoria di Freud, che scopre l'inconscio e apre la strada alla narrativa psicologica. Relatività: la teoria di Einstein, che scardina i concetti tradizionali di tempo e spazio. Il mondo fisico è diverso da come si pensava.",
   [C("", "Positivismo", "fiducia cieca nella scienza"), C("", "Psicoanalisi", "Freud e l'inconscio"), C("", "Relatività", "Einstein, tempo e spazio")])]))
ANS.append(MP("AN6", 1, 2, "Trasformazioni sociali e culturali", "Mappa concettuale del secondo argomento. Al centro, le trasformazioni sociali e culturali.", [
 ("La lingua", "italiano popolare", "trincee", "Primo ramo, la lingua. Nelle trincee nasce l'italiano popolare, mescolanza di italiano e dialetti."),
 ("L'unificazione", "omologazione", "leva obbligatoria", "Secondo ramo, l'unificazione. Servizio militare, urbanesimo ed emigrazione interna avvicinano gli italiani."),
 ("La stampa", "giornali", "Corriere della Sera", "Terzo ramo, la stampa. I giornali e le riviste popolari illustrate formano una coscienza linguistica comune."),
 ("La crisi", "Positivismo", "Freud, Einstein", "Quarto ramo, la crisi. Tramonta la fiducia nella scienza. Arrivano la psicoanalisi e la relatività."),
 ("Le riviste", "Firenze", "La Voce, Lacerba", "Quinto ramo, le riviste. Il Leonardo, La Voce e Lacerba sono luoghi di dibattito militante.")]))
ANS.append(AN("AN7", 1, 3, "confronto", "I crepuscolari contro il modello dannunziano", [
 S("Due modi di fare poesia", "Passiamo ai crepuscolari. Reagiscono al modello monumentale di D'Annunzio. Rifiutano la figura del poeta-veggente, del vate. Rifiutano anche l'estetismo aristocratico e il superuomo. Il tono è dimesso, malinconico, ironico e prosastico. Cantano le piccole cose, anche di pessimo gusto. La quotidianità grigia, la malattia e la nostalgia per un passato perduto.",
   [C("D'Annunzio", "Il vate", "estetismo aristocratico, superuomo"), C("Crepuscolari", "Piccole cose", "tono dimesso, quotidianità borghese, provincia")]),
 S("Gozzano e Corazzini", "Guido Gozzano è l'esponente principale. Nei Colloqui usa l'ironia e lo scontro tra la bellezza del passato e lo squallore del presente. Il suo personaggio emblematico è Signorina Felicità, una donna provinciale, semplice e quasi brutta. È l'opposto delle raffinate eroine dannunziane. Sergio Corazzini è invece il polo sentimentale: si presenta come un piccolo fanciullo che piange, e fa della sua sofferenza l'unica materia d'arte.",
   [C("Gozzano", "I colloqui", "ironia, Signorina Felicità"), C("Corazzini", "Il piccolo fanciullo che piange", "la sofferenza come materia d'arte")])]))
ANS.append(AN("AN8", 1, 3, "scheda", "Guido Gozzano e la fine del sublime", [
 S("Il linguaggio in urto", "Soffermiamoci su Gozzano. Affronta il dramma della degradazione dell'arte nella società borghese. Accoglie nei versi la realtà umile e anche il ciarpame, cioè le cose vecchie, abbandonate nei solai. Crea così un urto tra il linguaggio aulico della tradizione e la prosa semplice del presente. Non è carducciano, non è pascoliano e non è dannunziano. Dichiara la fine del sublime autentico.",
   [C("", "Dramma dell'arte", "degradazione nella società borghese"), C("", "Urto di linguaggi", "tradizione aulica e prosa del presente")])]))
ANS.append(MP("AN9", 1, 3, "I crepuscolari", "Mappa concettuale dei crepuscolari. Al centro, la poesia delle piccole cose.", [
 ("Il rifiuto", "anti-D'Annunzio", "niente vate", "Primo ramo. Rifiutano il poeta-veggente e l'estetismo."),
 ("Il tono", "dimesso", "malinconia, ironia", "Secondo ramo. Il tono è dimesso, malinconico, ironico e prosastico."),
 ("I temi", "piccole cose", "provincia, quotidianità", "Terzo ramo. Cantano la quotidianità borghese, gli ambienti provinciali, la malattia."),
 ("Gozzano", "ironia", "Signorina Felicità", "Quarto ramo. Gozzano è l'esponente principale e usa l'ironia."),
 ("Corazzini", "sofferenza", "il piccolo fanciullo", "Quinto ramo. Corazzini è il polo sentimentale del crepuscolarismo.")]))
ANS.append(AN("AN10", 1, 4, "scheda", "I vociani e Clemente Rebora", [
 S("La poetica del frammento", "I vociani sono legati alla rivista La Voce. Ne fanno parte Rebora, Campana, Sbarbaro. Scelgono la poetica del frammento. Rifiutano le forme metriche tradizionali. La poesia è espressione diretta della soggettività e ricerca interiore. Il linguaggio diventa aspro e spezzato, influenzato dall'espressionismo. Dà voce al disagio dell'uomo moderno.",
   [C("", "Il frammento", "rifiuto delle forme chiuse"), C("", "Linguaggio aspro", "espressionismo, parola deformata")]),
 S("Rebora e Viatico", "Clemente Rebora ha un forte impegno etico. Oppone la città, luogo di alienazione e disumanizzazione, alla campagna, spazio di pace. Con la guerra la sua poesia diventa un tragico realismo. In Viatico descrive l'agonia e lo strazio di un soldato ferito in trincea, ridotto a un tronco senza gambe. Il ritmo è convulso, i suoni sono duri e stridenti, i legami sintattici sono spezzati. È una contestazione morale contro l'interventismo e un richiamo alla solidarietà umana.",
   [C("", "Rebora", "impegno etico, città contro campagna"), C("", "Viatico", "il soldato ferito, richiamo alla fratellanza")])]))
ANS.append(MP("AN11", 1, 4, "I vociani e Rebora", "Mappa concettuale dei vociani. Al centro, la poesia del frammento.", [
 ("La rivista", "La Voce", "impegno etico e civile", "Primo ramo. I vociani sono figli della rivista La Voce."),
 ("La poetica", "frammento", "forme chiuse rifiutate", "Secondo ramo. Scelgono la poetica del frammento e rifiutano i generi tradizionali."),
 ("Il linguaggio", "espressionismo", "parola spezzata", "Terzo ramo. Il linguaggio è aspro e spezzato."),
 ("Rebora", "impegno etico", "città e campagna", "Quarto ramo. Rebora denuncia la disumanizzazione urbana."),
 ("Viatico", "trincea", "soldato ferito", "Quinto ramo. Viatico descrive lo strazio dei soldati e invoca la solidarietà umana.")]))
ANS.append(AN("AN3b", 1, 1, "scheda", "Riforme, industria e Sud", [
 S("Le riforme", "Sotto il governo Giolitti arrivano importanti riforme sociali. Ci sono tutele per il lavoro di donne e minori e un miglioramento della previdenza. L'obbligo scolastico sale fino a dodici anni. Questo processo di modernizzazione favorisce lo sviluppo industriale e l'urbanesimo. Nascono nuove classi sociali e le prime forme di consumo di massa.",
   [C("", "Tutele sociali", "lavoro di donne e minori, previdenza"), C("", "Scuola", "obbligo fino a dodici anni")]),
 S("Un'Italia a due velocità", "Lo sviluppo però non è uniforme. L'industria decolla solo al Nord, nel cosiddetto triangolo industriale. Il divario con il Sud aumenta: è la questione meridionale. Per frenare il malcontento e la disoccupazione, Giolitti riprende la politica coloniale. Nel settembre del millenovecentoundici l'Italia dichiara guerra all'impero ottomano e conquista la Libia.",
   [C("", "Nord industriale", "il triangolo industriale"), C("", "Questione meridionale", "il Sud resta indietro")])]))
ANS.append(AN("AN6b", 1, 2, "scheda", "Giornali e riviste popolari", [
 S("Una coscienza comune", "Cresce anche la stampa. Il Corriere della Sera diventa il principale quotidiano dell'epoca. Ci sono La Stampa, il Giornale d'Italia e tante altre testate, dall'estrema destra all'estrema sinistra. Escono riviste illustrate come La Domenica del Corriere. Immagini e disegni raggiungono anche chi legge poco. Con l'obbligo scolastico più alto e la diffusione dei giornali, l'analfabetismo si riduce. Nasce un'opinione pubblica più informata.",
   [C("", "Il Corriere della Sera", "il principale quotidiano"), C("", "Riviste illustrate", "La Domenica del Corriere, con disegni")])]))
ANS.append(AN("AN11b", 1, 4, "parole", "Rebora: parole chiave", [
 S("Tre parole per leggere Rebora", "Tre parole aiutano a leggere Rebora. La prima è espressionismo: la parola viene deformata per dare voce al disagio. La seconda è impegno etico. Per Rebora la poesia non è una consolazione formale. È un'indagine rigorosa sulle lacerazioni dell'animo umano. La terza è fratellanza. Davanti all'orrore della morte in guerra, il poeta chiede solidarietà tra gli uomini.",
   [C("", "Espressionismo", "parola deformata, suoni duri"), C("", "Impegno etico", "indagine sulle lacerazioni dell'animo"), C("", "Fratellanza", "richiamo alla solidarietà umana")])]))
ANS.append(MP("MF1", 1, 99, "Il primo Novecento", "Concludiamo con la mappa concettuale di tutta la lezione. Al centro, il primo Novecento e la lirica italiana.", [
 ("Il contesto", "Giolitti", "1903-1914", "Primo ramo, il contesto. L'Età giolittiana, la guerra di Libia e la Grande Guerra."),
 ("La società", "italiano popolare", "trincee", "Secondo ramo, la società. Le trincee e la leva obbligatoria uniscono gli italiani nella lingua."),
 ("La cultura", "crisi del Positivismo", "La Voce, Lacerba", "Terzo ramo, la cultura. Freud, Einstein e le riviste fiorentine."),
 ("I crepuscolari", "piccole cose", "Gozzano", "Quarto ramo. Poesia dimessa e ironica, contro il modello dannunziano."),
 ("I vociani", "frammento", "Rebora, Viatico", "Quinto ramo. Poesia del frammento, impegno etico e orrore della guerra.")]))
def voce_testo(a):
    return " ".join(a["voci"]) if a["tipo"] == "mappa" else " ".join(s["voce"] for s in a["schermate"])

if __name__ == "__main__":
    w = sum(len(voce_testo(a).split()) for a in ANS)
    print("parole", w, "min@2.24", round(w / 2.24 / 60, 1), "tot", round(42.6 + w / 2.24 / 60, 1))
