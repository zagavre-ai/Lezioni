# dati degli 11 argomenti (nomi dalle slide del prof)
ARG=[
 dict(n=1,page=2,titolo="La crisi di fine secolo e la svolta liberale",lines=["La crisi di fine secolo","e la svolta liberale"],fs=120,chip="Adua · Bava Beccaris · Bresci",breve="Crisi di fine secolo e svolta liberale"),
 dict(n=2,page=4,titolo="La nuova linea politica di Giolitti",lines=["La nuova linea politica","di Giolitti"],fs=120,chip="Neutralità · Camere del lavoro · CGdL",breve="La nuova linea politica di Giolitti"),
 dict(n=3,page=5,titolo="I rapporti con i socialisti e lo Sciopero del 1904",lines=["I rapporti con i socialisti","e lo sciopero del 1904"],fs=108,chip="Turati · Massimalisti · 1904",breve="I socialisti e lo sciopero del 1904"),
 dict(n=4,page=7,titolo="Il rapporto con i cattolici e il trasformismo",lines=["Il rapporto con i cattolici","e il trasformismo"],fs=108,chip="Non expedit · Pio X · Trasformismo",breve="I cattolici e il trasformismo"),
 dict(n=5,page=9,titolo="Le riforme sociali e scolastiche",lines=["Le riforme sociali","e scolastiche"],fs=128,chip="Legge Orlando · Daneo-Credaro · INA",breve="Le riforme sociali e scolastiche"),
 dict(n=6,page=10,titolo="Il suffragio universale maschile e il Patto Gentiloni",lines=["Il suffragio universale","maschile e il Patto Gentiloni"],fs=100,chip="Suffragio 1912 · Patto Gentiloni",breve="Suffragio universale e Patto Gentiloni"),
 dict(n=7,page=11,titolo="Le riforme mancate: le donne in lotta",lines=["Le riforme mancate:","le donne in lotta"],fs=128,chip="Anna Kuliscioff · Lucciola",breve="Le riforme mancate: le donne in lotta"),
 dict(n=8,page=12,titolo="Il decollo industriale italiano",lines=["Il decollo industriale","italiano"],fs=128,chip="Protezionismo · Fiat · Ansaldo",breve="Il decollo industriale italiano"),
 dict(n=9,page=13,titolo="Il divario Nord-Sud e l'emigrazione",lines=["Il divario Nord-Sud","e l'emigrazione"],fs=128,chip="Triangolo industriale · Salvemini",breve="Il divario Nord-Sud e l'emigrazione"),
 dict(n=10,page=15,titolo="La politica coloniale e la guerra in Libia",lines=["La politica coloniale","e la guerra in Libia"],fs=120,chip="Libia 1911 · Pascoli · Losanna",breve="Politica coloniale e guerra in Libia"),
 dict(n=11,page=17,titolo="La caduta di Giolitti e la «settimana rossa»",lines=["La caduta di Giolitti","e la «settimana rossa»"],fs=120,chip="Salandra · Mussolini · Ancona",breve="Caduta di Giolitti e settimana rossa"),
]
def tfs(txt,maxw=1190,cap=84,mn=48):
    return int(max(mn,min(cap,maxw/(0.44*len(txt)))))

# righe degli schemi di ripasso: una riga per frase della voce R<n> (la frase "Ripassiamo l'argomento." è esclusa)
ROWS={
1:[("1896 · Adua","La sconfitta di Adua fa cadere Crispi"),("Crisi del pane","Il caro prezzi scatena proteste in tutta Italia"),("1898 · Milano","Bava Beccaris spara sulla folla: oltre 80 morti"),("1900 · Regicidio","Ostruzionismo della sinistra; Bresci uccide re Umberto I"),("Svolta liberale","Vittorio Emanuele III affida il governo a Zanardelli e Giolitti")],
2:[("1903 · Giolitti","Diventa presidente del Consiglio"),("Stato mediatore","Neutrale: non usa più la forza contro gli scioperi"),("Sindacati","Nascono le Camere del lavoro, la Federterra e la CGdL"),("Obiettivo","Modernizzare il Paese ascoltando le masse popolari")],
3:[("Due correnti","Riformisti di Turati e massimalisti rivoluzionari"),("Dialogo","Giolitti dialoga con i riformisti per la pace sociale"),("Settembre 1904","Primo sciopero generale nazionale"),("Strategia","Nessuna forza: lo sciopero si esaurisce da solo")],
4:[("Non expedit","La Chiesa si riavvicina allo Stato per fermare i socialisti"),("1904 · Pio X","Permette ai cattolici di votare dove rischia la sinistra"),("Deputati cattolici","Entrano alla Camera i primi eletti"),("Trasformismo","Alleanze flessibili, a destra e a sinistra")],
5:[("Tutela","Vietato il lavoro sotto i 12 anni; riposo settimanale e fondo maternità"),("1912 · INA","Monopolio statale che finanzia le pensioni di invalidità"),("Legge Orlando","Obbligo scolastico a 12 anni e corsi serali"),("1911 · Daneo-Credaro","Le scuole elementari passano allo Stato")],
6:[("1912 · Suffragio","Voto a tutti i maschi: gli elettori da 3 a 8 milioni"),("Indennità","Anche chi non è ricco può fare il deputato"),("1913 · Gentiloni","Patto segreto tra Giolitti e i cattolici"),("Lo scambio","Voti ai liberali in cambio: niente divorzio, difesa delle scuole cattoliche")],
7:[("Esclusione","Dopo il 1912 le donne restano senza voto"),("Le voci","Anna Kuliscioff e la rivista Lucciola chiedono parità"),("Repressione","Attiviste ricoverate a forza negli ospedali psichiatrici"),("Pregiudizi","Donna moglie e madre; tollerato il delitto d'onore")],
8:[("Sostegni","Protezionismo e commesse dello Stato"),("Banche miste","Prestano capitali alla grande industria"),("Grandi imprese","Ansaldo, Fiat, Pirelli e Montecatini"),("Servizi","Lo Stato statalizza telefoni e ferrovie")],
9:[("Triangolo","Industria tra Torino, Milano e Genova"),("Il Sud","Agricolo e povero, dominato dal latifondo"),("Salvemini","Accusa Giolitti di clientelismo"),("Proteste","Le proteste contadine al Sud vengono represse"),("1901-1915","Circa 9 milioni di italiani emigrano")],
10:[("Pressioni","Industriali e nazionalisti spingono Giolitti all'impresa coloniale"),("1911 · Guerra","L'Italia attacca la Libia e dichiara guerra all'Impero ottomano"),("Propaganda","Pascoli: la Libia come terra promessa per gli emigranti"),("1912 · Losanna","Libia e Dodecaneso all'Italia, ma scarsi risultati economici")],
11:[("Socialisti","La guerra di Libia li spacca: espulsi i riformisti, sale Mussolini"),("Patto Gentiloni","Indebolisce la maggioranza liberale"),("Marzo 1914","Giolitti si dimette: arriva il conservatore Salandra"),("Giugno 1914","Morti di Ancona: scoppia la settimana rossa")],
}
