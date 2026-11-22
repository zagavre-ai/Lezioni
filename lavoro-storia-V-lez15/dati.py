# -*- coding: utf-8 -*-
# Storia V · Lezione 15 · La decolonizzazione (1945-1975). Tutti i testi vengono dalle slide del prof («LEZIONE 15.pdf»).
import re
LEZ = 15
LEZ_TITOLO = "La decolonizzazione (1945-1975)"
LEZ_COVER = "La decolonizzazione"
PDF_SLIDE = '/tmp/claude-0/l15/src/slide/SLIDE/LEZIONE 15.pdf'
TRASCR = '/tmp/claude-0/l15/tr/lez15.json'
NC = 4   # card per argomento
ARG = [
 dict(n=1, titolo="Le premesse della decolonizzazione", nome="Le premesse della decolonizzazione", chip="Autodeterminazione · ONU · Superpotenze", pag=[2],
      schema=[("Indebolimento europeo", "Primo: la Seconda guerra mondiale segna la fine del primato politico ed economico delle potenze europee."),
              ("Ruolo delle superpotenze", "Secondo: Stati Uniti e Unione Sovietica sono contrari al colonialismo tradizionale."),
              ("Consapevolezza nazionale", "Terzo: crescono i movimenti indipendentisti guidati da leader che hanno studiato in Europa."),
              ("Autodeterminazione", "Quarto: il principio di autodeterminazione è nella Carta delle Nazioni Unite del millenovecentoquarantacinque.")]),
 dict(n=2, titolo="La Conferenza di Bandung e la Guerra fredda", nome="Bandung e la Guerra fredda", chip="Bandung · Non allineati · Dieci principi", pag=[3],
      schema=[("Conferenza di Bandung", "Primo: nel millenovecentocinquantacinque ventinove Stati afroasiatici condannano colonialismo e razzismo."),
              ("Non allineati", "Secondo: nasce la volontà di non schierarsi con nessuno dei due blocchi."),
              ("Dieci principi", "Terzo: i dieci principi si fondano su diritti umani, sovranità e uguaglianza tra le nazioni."),
              ("Pressioni della Guerra fredda", "Quarto: Stati Uniti e Unione Sovietica offrono aiuti per attirare i nuovi Stati.")]),
 dict(n=3, titolo="La decolonizzazione in Asia: India e Pakistan", nome="India e Pakistan", chip="Gandhi · Nehru · Kashmir", pag=[4],
      schema=[("Ritiro britannico", "Primo: nel millenovecentoquarantasette il Regno Unito concede l'indipendenza all'India."),
              ("Spartizione", "Secondo: nascono due Stati, l'Unione Indiana e il Pakistan."),
              ("Dramma umanitario", "Terzo: violenze religiose e circa quindici milioni di profughi."),
              ("Guerra del Kashmir", "Quarto: l'area contesa provoca subito un conflitto tra i due Stati.")]),
 dict(n=4, titolo="Altre indipendenze in Asia e l'Indocina", nome="Asia e Indocina", chip="Indonesia · Vietminh · Dien Bien Phu", pag=[5, 6],
      schema=[("Colonie inglesi", "Primo: Ceylon nel millenovecentoquarantotto e la Malesia nel millenovecentocinquantasette diventano indipendenti in modo pacifico."),
              ("Indonesia olandese", "Secondo: la resistenza locale porta alla Repubblica nel millenovecentoquarantanove."),
              ("Indocina francese", "Terzo: la Francia è sconfitta dal Vietminh a Dien Bien Phu nel millenovecentocinquantaquattro."),
              ("Divisione del Vietnam", "Quarto: gli accordi di Ginevra dividono il Vietnam in Nord comunista e Sud filoccidentale.")]),
 dict(n=5, titolo="La decolonizzazione nell'Africa del Nord", nome="L'Africa del Nord", chip="Libia · Algeria · FLN", pag=[7, 8],
      schema=[("Libia", "Primo: la Libia, colonia italiana, è indipendente dal millenovecentocinquantuno e diventa Repubblica con Gheddafi nel millenovecentosessantanove."),
              ("Marocco e Tunisia", "Secondo: ottengono l'indipendenza dalla Francia nel millenovecentocinquantasei."),
              ("Guerra d'Algeria", "Terzo: la Francia considera l'Algeria territorio nazionale e combatte il Fronte di Liberazione Nazionale."),
              ("Indipendenza algerina", "Quarto: nel millenovecentosessantadue nasce la Repubblica algerina.")]),
 dict(n=6, titolo="L'Africa subsahariana e il Corno d'Africa", nome="Africa subsahariana", chip="Ghana · Mau Mau · Congo", pag=[9],
      schema=[("Corno d'Africa", "Primo: l'Etiopia torna indipendente, l'Eritrea le viene aggregata e la Somalia è indipendente nel millenovecentosessanta."),
              ("Indipendenze britanniche", "Secondo: il Ghana si emancipa pacificamente nel millenovecentocinquantasette, mentre in Kenya ci sono le violenze dei Mau Mau."),
              ("Colonie francesi", "Terzo: nel millenovecentosessanta quasi tutte le colonie dell'Africa occidentale diventano indipendenti in modo pacifico."),
              ("Caso del Congo", "Quarto: il Belgio si ritira all'improvviso e il Paese cade nel caos, tra secessione del Katanga e guerra civile.")]),
 dict(n=7, titolo="Apartheid e conflitti nell'Africa meridionale", nome="Apartheid e Africa meridionale", chip="Apartheid · ANC · Mandela", pag=[10, 11],
      schema=[("Apartheid", "Primo: in Sudafrica nel millenovecentoquarantotto nasce l'apartheid, segregazione razziale della minoranza bianca."),
              ("Resistenza sudafricana", "Secondo: l'ANC, guidato anche da Nelson Mandela, combatte le leggi razziali."),
              ("Rhodesia", "Terzo: la minoranza bianca proclama un'indipendenza unilaterale e scatena una guerriglia."),
              ("Colonie portoghesi", "Quarto: Angola e Mozambico sono indipendenti solo nel millenovecentosettantacinque.")]),
 dict(n=8, titolo="Il Medio Oriente e la nascita di Israele", nome="Il Medio Oriente e Israele", chip="Israele · Risoluzione 181 · Ben Gurion", pag=[12, 13],
      schema=[("Fine dei mandati", "Primo: finiscono i mandati di Gran Bretagna e Francia, e nascono Libano, Siria e Transgiordania."),
              ("Questione palestinese", "Secondo: l'ONU approva nel millenovecentoquarantasette la Risoluzione centottantuno per dividere la Palestina."),
              ("Nascita di Israele", "Terzo: nel millenovecentoquarantotto Ben Gurion proclama lo Stato ebraico, non accettato dai Paesi arabi."),
              ("Prima guerra arabo-israeliana", "Quarto: Israele vince e allarga i confini, e fuggono centinaia di migliaia di profughi palestinesi.")]),
 dict(n=9, titolo="L'Egitto di Nasser e la crisi di Suez", nome="Nasser e la crisi di Suez", chip="Nasser · Suez · Assuan", pag=[14, 15],
      schema=[("Rivoluzione egiziana", "Primo: nel millenovecentocinquantadue Nasser prende il potere e promuove il nazionalismo arabo."),
              ("Canale di Suez", "Secondo: nel millenovecentocinquantasei Nasser nazionalizza il canale per finanziare la diga di Assuan."),
              ("Crisi internazionale", "Terzo: Francia, Regno Unito e Israele attaccano l'Egitto."),
              ("Superpotenze", "Quarto: Stati Uniti e Unione Sovietica impongono il ritiro, e Nasser ne esce rafforzato.")]),
 dict(n=10, titolo="Il mondo post-coloniale e il neocolonialismo", nome="Il neocolonialismo", chip="Terzo mondo · Neocolonialismo · FMI", pag=[16],
      schema=[("Terzo mondo", "Primo: l'espressione è di Alfred Sauvy e indica i Paesi di nuova indipendenza, poveri e arretrati."),
              ("Neocolonialismo", "Secondo: i nuovi Stati restano economicamente subordinati a multinazionali e mercati occidentali."),
              ("Dipendenza finanziaria", "Terzo: istituzioni come il Fondo Monetario Internazionale impongono misure che favoriscono i Paesi industrializzati."),
              ("Nuovo ordine economico", "Quarto: negli anni Settanta all'ONU si discute una riforma più equa, ostacolata dai Paesi occidentali.")]),
]
RIGHE = {1: ["Le premesse della", "decolonizzazione"], 2: ["La Conferenza di Bandung", "e la Guerra fredda"], 3: ["La decolonizzazione", "in Asia: India e Pakistan"], 4: ["Altre indipendenze", "in Asia e l'Indocina"],
         5: ["La decolonizzazione", "nell'Africa del Nord"], 6: ["L'Africa subsahariana", "e il Corno d'Africa"], 7: ["Apartheid e conflitti", "nell'Africa meridionale"], 8: ["Il Medio Oriente", "e la nascita di Israele"],
         9: ["L'Egitto di Nasser", "e la crisi di Suez"], 10: ["Il mondo post-coloniale", "e il neocolonialismo"]}
PARTI = {1: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]}
POFF = {1: 0}
GLOBAL_ORDER = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
BEN = {1: "BEN"}
FIN = {1: "FIN"}
GLOSS = [
 ("Decolonizzazione", "il processo con cui le colonie ottengono l'indipendenza dopo la Seconda guerra mondiale"),
 ("Autodeterminazione", "il diritto dei popoli di scegliere liberamente il proprio governo"),
 ("Non allineati", "gli Stati che rifiutano di schierarsi con uno dei due blocchi della Guerra fredda"),
 ("Spartizione", "la divisione di un territorio in due Stati, come India e Pakistan nel 1947"),
 ("Apartheid", "il sistema di segregazione razziale della minoranza bianca in Sudafrica"),
 ("Nazionalizzazione", "il passaggio allo Stato di un bene privato o straniero, come il Canale di Suez"),
 ("Neocolonialismo", "la subordinazione economica dei Paesi indipendenti alle potenze occidentali"),
 ("Terzo mondo", "l'insieme dei Paesi di nuova indipendenza, poveri e arretrati"),
]
GLP = {1: list(range(8))}
MAPPE = []   # nessuna mappa del prof per la lezione 15: tutte costruite dalle slide
BENVENUTO_TXT = ("Benvenuti alla lezione di Storia. Oggi parliamo della decolonizzazione, dal millenovecentoquarantacinque al millenovecentosettantacinque. "
                 "Il professor Giorgio Mazzotti ci guida attraverso dieci argomenti: dalle premesse e dalla Conferenza di Bandung all'Asia, all'Africa, al Medio Oriente e al neocolonialismo.")
FIN_TXT = ("Ricapitoliamo la lezione. Le premesse della decolonizzazione e la Conferenza di Bandung. Poi l'Asia, con India, Pakistan e Indocina, l'Africa del Nord, l'Africa subsahariana e l'apartheid. "
           "Infine il Medio Oriente e la nascita di Israele, Nasser e la crisi di Suez, e il neocolonialismo.")

def _trim(s): return re.sub(r'^(Primo|Secondo|Terzo|Quarto): ', '', s)
NEWMAPS = {a['n']: ("Mappa concettuale: " + a['nome'], a['nome'].upper(), [(kw, _trim(fr)) for kw, fr in a['schema']]) for a in ARG}
def mappa_di(n): return ('new', n)
def mapvoice(n): return f"MAPN{n}"
def map_text(n):
    a = ARG[n - 1]; o = ["Primo", "Secondo", "Terzo", "Quarto"]
    t = f"Ecco la mappa di questo argomento: {a['nome']}. "
    for i, (kw, fr) in enumerate(a['schema']):
        d = _trim(fr); t += f"{o[i]} ramo, {kw[0].lower() + kw[1:]}: {d[0].lower() + d[1:]} "
    return t.strip()
