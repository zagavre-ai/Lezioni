# -*- coding: utf-8 -*-
# Storia V · Lezione 17 · Le fasi conclusive della Guerra fredda (1969-1991). Tutti i testi vengono dalle slide del prof («LEZIONE 17.pdf»).
import re
LEZ = 17
LEZ_TITOLO = "Le fasi conclusive della Guerra fredda (1969-1991)"
LEZ_COVER = "Le fasi conclusive della Guerra fredda"
PDF_SLIDE = '/tmp/claude-0/l17/src/slide/SLIDE/LEZIONE 17.pdf'
TRASCR = '/tmp/claude-0/l17/tr/lez17.json'
ARG = [
 dict(n=1, titolo="Il Medio Oriente e la crisi economica mondiale (Anni '70)", nome="La crisi economica degli anni Settanta", chip="Bretton Woods · Kippur · Shock petrolifero", pag=[2],
      schema=[("Deficit americano", "Primo: nel millenovecentosessantanove Nixon eredita un forte deficit, causato dalla guerra in Vietnam e dai programmi di assistenza sociale."),
              ("Fine di Bretton Woods", "Secondo: nell'agosto del millenovecentosettantuno Nixon sospende la convertibilità del dollaro in oro e finisce il sistema dei cambi fissi."),
              ("Guerra del Kippur", "Terzo: nel millenovecentosettantatré Egitto e Siria attaccano Israele, gli Stati Uniti lo sostengono e i paesi arabi reagiscono."),
              ("Shock petrolifero", "Quarto: i paesi arabi dell'OPEC riducono l'offerta e quadruplicano il prezzo del petrolio, e arrivano inflazione e recessione, la stagflazione.")]),
 dict(n=2, titolo="Tensioni e accordi in Medio Oriente", nome="Tensioni e accordi in Medio Oriente", chip="Camp David · Libano · Intifada", pag=[4],
      schema=[("Camp David", "Primo: nel millenovecentosettantotto Sadat e Begin firmano gli accordi di Camp David, ma Sadat è isolato e assassinato nel millenovecentottantuno."),
              ("Libano", "Secondo: nel millenovecentosettantacinque scoppia la guerra civile in Libano, e nel millenovecentottantadue Israele lo invade per cacciare l'OLP."),
              ("Intifada", "Terzo: nel millenovecentottantasette nei territori occupati scoppia la rivolta popolare palestinese e cresce il peso di Hamas.")]),
 dict(n=3, titolo="Le rivoluzioni in Iran e la guerra con l'Iraq", nome="Iran e guerra con l'Iraq", chip="Khomeini · Ostaggi · Saddam Hussein", pag=[5],
      schema=[("Caduta dello Shah", "Primo: nel millenovecentosettantanove una rivoluzione popolare travolge il regime dello Shah Reza Pahlavi."),
              ("Repubblica Islamica", "Secondo: Khomeini fonda una teocrazia basata sulla sharia e su un forte sentimento anti-occidentale."),
              ("Crisi degli ostaggi", "Terzo: nel novembre del millenovecentosettantanove gli studenti assaltano l'ambasciata americana e tengono in ostaggio il personale per oltre un anno."),
              ("Guerra Iran-Iraq", "Quarto: Saddam Hussein attacca l'Iran, e la guerra del millenovecentottanta finisce dopo otto anni con quasi due milioni di morti.")]),
 dict(n=4, titolo="Gli Stati Uniti da Nixon a Reagan", nome="Da Nixon a Reagan", chip="Cina · SALT · Watergate · Reagan", pag=[7],
      schema=[("Apertura alla Cina", "Primo: nel millenovecentosettantadue Nixon apre relazioni diplomatiche con la Cina di Mao, per isolare l'URSS."),
              ("Distensione", "Secondo: nascono i trattati SALT uno e gli accordi di Helsinki sui confini europei e sui diritti umani."),
              ("Watergate e Carter", "Terzo: lo scandalo Watergate costringe Nixon alle dimissioni nel millenovecentosettantaquattro, poi arrivano Ford e Carter."),
              ("Svolta di Reagan", "Quarto: nel millenovecentottantuno Reagan adotta una linea dura contro l'impero del male e rilancia le spese militari, con lo scudo spaziale.")]),
 dict(n=5, titolo="Instabilità e dittature in America Latina", nome="America Latina", chip="Cile · Argentina · Desaparecidos", pag=[9],
      schema=[("Cile", "Primo: eletto Allende nel millenovecentosettanta, nel millenovecentosettantatré un golpe di Pinochet instaura una dittatura feroce."),
              ("Argentina", "Secondo: tra il millenovecentosettantasei e il millenovecentottantatré la giunta militare fa sparire migliaia di oppositori, i desaparecidos."),
              ("Ritorno alla democrazia", "Terzo: la crisi economica e la sconfitta nelle Falkland del millenovecentottantadue portano al ritorno della democrazia.")]),
 dict(n=6, titolo="L'Europa occidentale tra crisi e integrazione", nome="Europa occidentale", chip="Thatcher · Neoliberismo · CEE", pag=[10],
      schema=[("Difficoltà economiche", "Primo: gli shock petroliferi colpiscono le industrie europee con inflazione, disoccupazione e conflitti sindacali."),
              ("Thatcher", "Secondo: eletta nel millenovecentosettantanove, la Lady di ferro avvia privatizzazioni, tagli allo stato sociale e lotta ai sindacati."),
              ("Allargamento della CEE", "Terzo: nel millenovecentosettantatré entrano Regno Unito, Irlanda e Danimarca; poi Grecia, Spagna e Portogallo.")]),
 dict(n=7, titolo="La crisi del comunismo e il crollo dell'URSS", nome="Il crollo dell'URSS", chip="Gorbačev · Muro di Berlino · CSI", pag=[13],
      schema=[("Era Brežnev", "Primo: l'URSS vive una lunga stagnazione economica, logorata dall'invasione dell'Afghanistan del millenovecentosettantanove."),
              ("Riforme di Gorbačev", "Secondo: nel millenovecentottantacinque Gorbačev lancia la Perestrojka e la Glasnost e avvia il disarmo con gli Stati Uniti."),
              ("Fine dei satelliti", "Terzo: nel millenovecentottantanove crollano i regimi comunisti dell'Est, cade il Muro di Berlino e la Germania si riunifica."),
              ("Fine dell'URSS", "Quarto: nel dicembre del millenovecentonovantuno l'URSS si dissolve, nasce la CSI e Gorbačev si dimette.")]),
 dict(n=8, titolo="L'altro 1989: la svolta della Cina", nome="La svolta della Cina", chip="Deng Xiaoping · Tienanmen", pag=[16],
      schema=[("Riforme di Deng", "Primo: dalla fine degli anni Settanta Deng apre la Cina al capitalismo con le Quattro modernizzazioni e l'economia cresce in modo vertiginoso."),
              ("Nessuna apertura politica", "Secondo: il Partito Comunista mantiene il controllo assoluto dello Stato, senza riforme democratiche."),
              ("Piazza Tienanmen", "Terzo: nella primavera del millenovecentottantanove studenti e cittadini chiedono democrazia, e a giugno i carri armati reprimono la protesta nel sangue.")]),
]
RIGHE = {1: ["Il Medio Oriente e la crisi", "economica mondiale"], 2: ["Tensioni e accordi", "in Medio Oriente"], 3: ["Le rivoluzioni in Iran", "e la guerra con l'Iraq"], 4: ["Gli Stati Uniti", "da Nixon a Reagan"],
         5: ["Instabilità e dittature", "in America Latina"], 6: ["L'Europa occidentale", "tra crisi e integrazione"], 7: ["La crisi del comunismo", "e il crollo dell'URSS"], 8: ["L'altro 1989:", "la svolta della Cina"]}
PARTI = {1: [1, 2, 3], 2: [4, 5], 3: [6, 7, 8]}
POFF = {1: 0, 2: 3, 3: 5}
GLOBAL_ORDER = [1, 2, 3, 4, 5, 6, 7, 8]
BEN = {1: "BEN1", 2: "BEN2", 3: "BEN3"}
FIN = {1: "FZ1", 2: "FZ2", 3: "FZ3"}
GLOSS = [
 ("Bretton Woods", "il sistema di cambi fissi legato alla convertibilità del dollaro in oro, finito nel 1971"),
 ("Stagflazione", "la combinazione di inflazione e recessione seguita allo shock petrolifero"),
 ("Teocrazia", "il governo fondato sulla legge religiosa, come l'Iran di Khomeini"),
 ("Distensione", "la fase di dialogo tra USA e URSS, con i trattati SALT e gli accordi di Helsinki"),
 ("Desaparecidos", "gli oppositori fatti sparire dalla giunta militare argentina"),
 ("Neoliberismo", "la politica di privatizzazioni e tagli allo stato sociale di Thatcher e Reagan"),
 ("Perestrojka e Glasnost", "la ristrutturazione economica e la trasparenza lanciate da Gorbačev"),
 ("CSI", "la Comunità degli Stati Indipendenti nata dopo lo scioglimento dell'URSS"),
]
GLP = {1: [0, 1, 2], 2: [3, 4], 3: [5, 6, 7]}
# mappe del prof (pagina del PDF «MAPPE LEZIONE 17», dopo quale argomento, titolo, testo letto dalla voce)
MAPPE = [
 dict(p=1, dopo=1, titolo="Quali sono le cause e le conseguenze della crisi degli anni Settanta?",
      voce="Ecco la mappa della crisi degli anni Settanta. La guerra del Kippur del millenovecentosettantatré è causata dall'attacco di Egitto e Siria a Israele, e provoca l'aumento del prezzo del petrolio. Da questo derivano il calo della produzione, la disoccupazione e l'inflazione."),
 dict(p=2, dopo=6, titolo="Quale risposta offre alla crisi il neoliberismo?",
      voce="Ecco la mappa della risposta neoliberista alla crisi. Il neoliberismo critica l'intervento dello Stato in economia e sostiene meno Stato, più mercato. Pratica l'affidamento dei servizi ai privati e promette la riduzione delle tasse. Viene messo in atto da Reagan negli Stati Uniti, dal millenovecentottantuno al millenovecentottantotto, e da Thatcher nel Regno Unito, dal millenovecentosettantanove al millenovecentonovanta."),
 dict(p=3, dopo=7, titolo="Come si arriva alla fine dell'URSS?",
      voce="Ecco la mappa di Michail Gorbačev, del millenovecentottantacinque. Introduce riforme basate su trasparenza e ristrutturazione. Riconosce l'autonomia dei paesi dell'Est europeo, dove il socialismo cade nel millenovecentottantanove e viene aperto il Muro di Berlino, il nove novembre. Subisce un tentativo di colpo di Stato nel millenovecentonovantuno e la separazione di molti Stati dell'Unione, fino alla dissoluzione dell'Unione Sovietica, a dicembre del millenovecentonovantuno."),
]
BENVENUTO_TXT = {
 1: ("Benvenuti alla lezione di Storia. Oggi parliamo delle fasi conclusive della Guerra fredda, dal millenovecentosessantanove al millenovecentonovantuno. "
     "In questa prima parte il professor Giorgio Mazzotti ci guida attraverso tre argomenti: la crisi economica degli anni Settanta, le tensioni in Medio Oriente e la rivoluzione iraniana."),
 2: ("Benvenuti alla seconda parte della lezione sulle fasi conclusive della Guerra fredda. "
     "Con il professor Giorgio Mazzotti vediamo due argomenti: gli Stati Uniti da Nixon a Reagan e le dittature in America Latina."),
 3: ("Benvenuti alla terza parte della lezione sulle fasi conclusive della Guerra fredda. "
     "Con il professor Giorgio Mazzotti vediamo tre argomenti: l'Europa occidentale tra crisi e integrazione, il crollo dell'URSS e la svolta della Cina."),
}
FIN_TXT = {
 1: ("Ricapitoliamo questa prima parte. La crisi economica degli anni Settanta, le tensioni e gli accordi in Medio Oriente, "
     "e la rivoluzione in Iran con la guerra contro l'Iraq."),
 2: ("Ricapitoliamo questa seconda parte. Gli Stati Uniti da Nixon a Reagan, dalla distensione alla linea dura contro l'URSS, "
     "e le dittature militari in America Latina, dal Cile all'Argentina."),
 3: ("Ricapitoliamo questa terza parte. L'Europa occidentale tra crisi e integrazione, il crollo dell'URSS con Gorbačev e la fine della Guerra fredda, "
     "e la svolta della Cina, da Deng Xiaoping a Piazza Tienanmen."),
}

def _trim(s): return re.sub(r'^(Primo|Secondo|Terzo|Quarto|Quinto): ', '', s)
NEWMAPS = {a['n']: ("Mappa concettuale: " + a['nome'], a['nome'].upper(), [(kw, _trim(fr)) for kw, fr in a['schema']]) for a in ARG}
def nc(n): return len(ARG[n - 1]['schema'])
def mappa_di(n):
    for k, m in enumerate(MAPPE, 1):
        if m['dopo'] == n: return ('prof', k)
    return ('new', n)
def mapvoice(n):
    for k, m in enumerate(MAPPE, 1):
        if m['dopo'] == n: return f"MPR{k}"
    return f"MAPN{n}"
def map_text(n):
    for m in MAPPE:
        if m['dopo'] == n: return m['voce']
    a = ARG[n - 1]; o = ["Primo", "Secondo", "Terzo", "Quarto", "Quinto"]
    t = f"Ecco la mappa di questo argomento: {a['nome']}. "
    for i, (kw, fr) in enumerate(a['schema']):
        d = _trim(fr); t += f"{o[i]} ramo, {kw[0].lower() + kw[1:]}: {d[0].lower() + d[1:]} "
    return t.strip()
