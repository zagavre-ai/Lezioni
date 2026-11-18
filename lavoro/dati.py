# -*- coding: utf-8 -*-
# Storia V · Lezione 6 · La decolonizzazione (1945-1975). Tutti i testi vengono dalle slide del prof («LEZIONE 6.pdf»).
import re
LEZ = 6
LEZ_TITOLO = "Il primo dopoguerra (1919-1925)"
LEZ_COVER = "Il primo dopoguerra"
PDF_SLIDE = '/tmp/claude-0/l06/src/slide/SLIDE/LEZIONE 6.pdf'
TRASCR = '/tmp/claude-0/l06/tr/lez06.json'
NC = 4   # card per argomento
ARG = [
 dict(n=1, titolo="La riorganizzazione dell'Europa centro-orientale", nome="L'Europa centro-orientale", chip="Cecoslovacchia · Polonia · Stati cuscinetto", pag=[2],
      schema=[("Crollo degli imperi", "Primo: la fine dell'Impero zarista e di quello austro-ungarico stravolge la mappa europea."),
              ("Nuovi Stati nazionali", "Secondo: nascono Cecoslovacchia, Polonia e il Regno dei Serbi, Croati e Sloveni."),
              ("Stati cuscinetto", "Terzo: i vincitori creano Stati cuscinetto per arginare la Russia bolscevica e contenere la Germania."),
              ("Territori zaristi", "Quarto: la Finlandia resta indipendente, mentre Ucraina, Georgia e Bielorussia sono rioccupate dai bolscevichi entro il millenovecentoventidue.")]),
 dict(n=2, titolo="Instabilità e regimi autoritari nell'Europa dell'Est", nome="Regimi autoritari dell'Est", chip="Jugoslavia · Polonia · Ungheria", pag=[3, 4],
      schema=[("Jugoslavia", "Primo: prevale il centralismo serbo e il re instaura la dittatura nel millenovecentoventinove."),
              ("Polonia", "Secondo: dopo la pace di Riga del millenovecentoventuno, Piłsudski instaura una dittatura nel millenovecentotrenta."),
              ("Ungheria", "Terzo: dopo la Repubblica sovietica di Béla Kun, Horthy restaura la monarchia e governa da reggente."),
              ("Austria", "Quarto: piccola repubblica in grave crisi economica, con scontri tra socialdemocratici e conservatori.")]),
 dict(n=3, titolo="La Germania sconfitta e la Repubblica di Weimar", nome="La Repubblica di Weimar", chip="Weimar · Spartachisti · Versailles", pag=[5],
      schema=[("Nascita della Repubblica", "Primo: dopo l'abdicazione del Kaiser nel millenovecentodiciotto nasce una repubblica democratica guidata dai socialdemocratici."),
              ("Minacce rivoluzionarie", "Secondo: nel millenovecentodiciannove il governo reprime la rivolta spartachista di Liebknecht e Rosa Luxemburg."),
              ("Costituzione di Weimar", "Terzo: introduce il suffragio universale ma dà ampi poteri di emergenza al presidente."),
              ("Umiliazione di Versailles", "Quarto: la pace è vissuta come un diktat e alimenta l'odio dell'estrema destra.")]),
 dict(n=4, titolo="Crisi economica e tensioni in Germania (1920-1924)", nome="La crisi della Germania", chip="Iperinflazione · Ruhr · Piano Dawes", pag=[6],
      schema=[("Iperinflazione", "Primo: le riparazioni, centotrentadue miliardi di marchi oro, fanno collassare la moneta e azzerano i risparmi."),
              ("Colpi di Stato", "Secondo: fallisce il putsch di Kapp nel millenovecentoventi e quello di Monaco di Hitler nel millenovecentoventitré."),
              ("Occupazione della Ruhr", "Terzo: nel millenovecentoventitré truppe francesi e belghe occupano la Ruhr."),
              ("Stabilizzazione", "Quarto: Stresemann e il Piano Dawes del millenovecentoventiquattro portano prestiti americani e una ripresa.")]),
 dict(n=5, titolo="Francia e Regno Unito nel dopoguerra", nome="Francia e Regno Unito", chip="Lloyd George · IRA · Scioperi", pag=[7],
      schema=[("Francia", "Primo: ricostruzione costosa e inflazione, con l'alternanza tra Blocco nazionale e Cartello delle sinistre."),
              ("Regno Unito", "Secondo: Lloyd George introduce riforme sociali, tra cui il voto alle donne sopra i trent'anni."),
              ("Tensioni sociali", "Terzo: il malcontento culmina nei grandi scioperi dei minatori del millenovecentoventisei."),
              ("Questione irlandese", "Quarto: nel millenovecentoventuno nasce lo Stato Libero d'Irlanda, e scoppia una guerra civile.")]),
 dict(n=6, titolo="Il Medio Oriente e la nascita della Turchia moderna", nome="Il Medio Oriente e la Turchia", chip="Atatürk · Sèvres · Sykes-Picot", pag=[8, 9],
      schema=[("Crollo ottomano", "Primo: il trattato di Sèvres del millenovecentoventi prevede la spartizione dell'Impero ottomano."),
              ("Riscossa turca", "Secondo: Mustafa Kemal vince la guerra contro i greci e ottiene Losanna nel millenovecentoventitré."),
              ("Modernizzazione di Atatürk", "Terzo: Repubblica, capitale ad Ankara, alfabeto latino, fine della poligamia e Stato laico."),
              ("Promesse tradite agli arabi", "Quarto: l'accordo Sykes-Picot e i mandati affidano il Medio Oriente a Regno Unito e Francia.")]),
 dict(n=7, titolo="I movimenti anticoloniali in Africa e Asia", nome="I movimenti anticoloniali", chip="Egitto · Gandhi · Ho Chi Minh", pag=[10],
      schema=[("Egitto", "Primo: formale indipendenza dal Regno Unito nel millenovecentoventidue, ma controllo militare britannico."),
              ("India e non-violenza", "Secondo: dopo Amritsar, Gandhi guida disobbedienza civile, boicottaggio e marcia del sale."),
              ("Impero francese", "Terzo: rivolte in Marocco e in Indocina, dove si organizza il movimento di Ho Chi Minh.")]),
 dict(n=8, titolo="L'ascesa dei nazionalismi in Estremo Oriente", nome="Nazionalismi in Estremo Oriente", chip="Giappone · Guomintang · Chiang Kai-shek", pag=[11],
      schema=[("Giappone", "Primo: grande potenza imperialista, ottiene le ex colonie tedesche ma matura risentimento verso l'Occidente."),
              ("Cina nel caos", "Secondo: dopo la morte di Yuan Shikai nel millenovecentosedici governano i signori della guerra."),
              ("Svolta nazionalista", "Terzo: il Guomintang di Sun Yat-sen si allea con i comunisti per unificare il Paese."),
              ("Rottura e guerra civile", "Quarto: nel millenovecentoventisei Chiang Kai-shek rompe l'alleanza e reprime i comunisti.")]),
]
RIGHE = {1: ["La riorganizzazione", "dell'Europa centro-orientale"], 2: ["Instabilità e regimi autoritari", "nell'Europa dell'Est"], 3: ["La Germania sconfitta", "e la Repubblica di Weimar"], 4: ["Crisi economica e tensioni", "in Germania"],
         5: ["Francia e Regno Unito", "nel dopoguerra"], 6: ["Il Medio Oriente e la nascita", "della Turchia moderna"], 7: ["I movimenti anticoloniali", "in Africa e Asia"], 8: ["L'ascesa dei nazionalismi", "in Estremo Oriente"]}
PARTI = {1: [1, 2, 3, 4, 5, 6, 7, 8]}
POFF = {1: 0}
GLOBAL_ORDER = [1, 2, 3, 4, 5, 6, 7, 8]
BEN = {1: "BEN"}
FIN = {1: "FIN"}
GLOSS = [
 ("Stati cuscinetto", "gli Stati creati per separare e contenere Russia bolscevica e Germania"),
 ("Spartachisti", "i comunisti tedeschi guidati da Liebknecht e Rosa Luxemburg, repressi nel 1919"),
 ("Diktat", "la pace imposta alla Germania a Versailles, vissuta come umiliazione"),
 ("Iperinflazione", "la perdita di valore della moneta che azzera i risparmi"),
 ("Mandato", "l'amministrazione di un territorio affidata a una potenza dalla Società delle Nazioni"),
 ("Stato laico", "lo Stato separato dalla religione, come la Turchia di Atatürk"),
 ("Disobbedienza civile", "la protesta non violenta di Gandhi contro le leggi inglesi"),
 ("Guomintang", "il partito nazionalista cinese di Sun Yat-sen e poi di Chiang Kai-shek"),
]
GLP = {1: list(range(8))}
MAPPE = []
BENVENUTO_TXT = ("Benvenuti alla lezione di Storia. Oggi parliamo del primo dopoguerra, dal millenovecentodiciannove al millenovecentoventicinque. "
                 "Il professor Giorgio Mazzotti ci guida attraverso otto argomenti: l'Europa centro-orientale, la Germania di Weimar, Francia e Regno Unito, il Medio Oriente e la Turchia, e i movimenti anticoloniali e nazionalisti in Africa e Asia.")
FIN_TXT = ("Ricapitoliamo la lezione. La riorganizzazione dell'Europa centro-orientale e i regimi autoritari dell'Est. La Germania di Weimar e la sua crisi. "
           "Francia e Regno Unito, il Medio Oriente e la nascita della Turchia moderna, i movimenti anticoloniali in Africa e Asia, e i nazionalismi in Estremo Oriente.")

def _trim(s): return re.sub(r'^(Primo|Secondo|Terzo|Quarto): ', '', s)
NEWMAPS = {a['n']: ("Mappa concettuale: " + a['nome'], a['nome'].upper(), [(kw, _trim(fr)) for kw, fr in a['schema']]) for a in ARG}
def nc(n): return len(ARG[n - 1]['schema'])
def mappa_di(n): return ('new', n)
def mapvoice(n): return f"MAPN{n}"
def map_text(n):
    a = ARG[n - 1]; o = ["Primo", "Secondo", "Terzo", "Quarto"]
    t = f"Ecco la mappa di questo argomento: {a['nome']}. "
    for i, (kw, fr) in enumerate(a['schema']):
        d = _trim(fr); t += f"{o[i]} ramo, {kw[0].lower() + kw[1:]}: {d[0].lower() + d[1:]} "
    return t.strip()
