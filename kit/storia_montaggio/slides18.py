# Testo delle slide del docente (dal PDF del prof): per argomento titolo, kicker e card (lead, testo)
import re
SLIDES=[
 ("Un Paese da ricostruire","Il Secondo Dopoguerra",[
  ("La situazione economico-sociale","l'Italia esce dalla guerra distrutta dai bombardamenti alleati e dalle rappresaglie tedesche. Le fabbriche e le infrastrutture sono devastate, la produzione è ferma e mancano i beni di prima necessità."),
  ("Le difficoltà della popolazione","cresce la disoccupazione e si diffonde il mercato nero. Molti reduci e sfollati faticano a trovare una stabilità economica e professionale."),
  ("Il clima di violenza","l'ordine pubblico è precario; nel Centro-Nord si verificano regolamenti di conti contro gli ex fascisti, mentre nel Sud esplodono i disordini legati alle occupazioni delle terre dei latifondisti da parte dei contadini.")]),
 ("Il panorama politico e la nascita della Repubblica","Un nuovo quadro politico",[
  ("I partiti di massa","la scena politica vede il protagonismo della Democrazia Cristiana (DC) guidata da Alcide De Gasperi, affiancata dal Partito comunista (PCI) di Palmiro Togliatti e dal Partito socialista (PSI) di Pietro Nenni."),
  ("La pacificazione nazionale","Palmiro Togliatti, in veste di ministro della Giustizia, promuove un'amnistia per i reati politici commessi durante la guerra per favorire la stabilità dello Stato."),
  ("Il referendum istituzionale (2 giugno 1946)","per la prima volta votano anche le donne. Il popolo sceglie la Repubblica (con circa 12 milioni di voti) contro la Monarchia (circa 10 milioni). Nasce l'Assemblea Costituente.")]),
 ("La Costituzione e il nuovo sistema politico","La Carta del 1948",[
  ("Le madri costituenti","tra i membri dell'Assemblea Costituente ci sono 21 donne (tra cui Nilde Iotti, Lina Merlin, Teresa Mattei), fondamentali nel garantire l'uguaglianza giuridica e sociale tra i sessi all'interno della Carta."),
  ("Il nuovo ordinamento","entrata in vigore il 1° gennaio 1948, la Costituzione definisce l'Italia una repubblica democratica fondata sul lavoro."),
  ("Separazione dei poteri","si stabilisce un sistema parlamentare in cui il potere legislativo spetta al Parlamento, quello esecutivo al Governo e quello giudiziario alla Magistratura.")]),
 ("Gli anni del Centrismo (1948-1953)","De Gasperi al governo",[
  ("Le elezioni del 1948","segnano una profonda polarizzazione tra la DC (sostenuta dalla Chiesa cattolica e dagli USA) e il Fronte democratico popolare di sinistra (PCI e PSI, legati all'URSS). La DC ottiene una netta vittoria."),
  ("La linea economica e le riforme","sotto la guida di De Gasperi e del ministro Luigi Einaudi si segue una linea liberista. Vengono attuati grandi interventi pubblici come la riforma agraria (ridistribuzione delle terre) e la nascita della Cassa per il Mezzogiorno."),
  ("Politica estera","l'Italia sceglie l'integrazione nel blocco occidentale, aderendo al Piano Marshall e al Patto Atlantico (NATO), oltre a partecipare alla nascita della CECA.")]),
 ("Il miracolo economico e le sue criticità","Gli anni del boom",[
  ("Il boom economico","tra gli anni '50 e '60 l'Italia vive una crescita industriale eccezionale, trainata da settori come l'automobilistico (simboleggiato dalla Fiat 500), la siderurgia e la chimica."),
  ("Nuovi stili di vita","cambiano i consumi degli italiani con la diffusione di massa di elettrodomestici, automobili, televisione e con la nascita delle vacanze di massa."),
  ("Le criticità del boom","si accentua il divario economico tra il Nord industrializzato e il Sud agricolo, innescando una massiccia migrazione interna. Le grandi città industriali del Nord crescono in modo caotico, portando a problemi di integrazione, povertà suburbana e speculazione edilizia (\"cementificazione\").")]),
 ("La stagione del Centrosinistra (1953-1963)","L'apertura ai socialisti",[
  ("La svolta politica","per rispondere alle crescenti tensioni sociali e allargare la base democratica, la DC avvia un'apertura verso i socialisti (PSI), portando alla nascita dei governi di centrosinistra guidati da Amintore Fanfani e Aldo Moro."),
  ("Le grandi riforme","questo periodo è caratterizzato da importanti riforme sociali, tra cui la nazionalizzazione dell'energia elettrica (nascita dell'ENEL) e l'introduzione della scuola media unica e obbligatoria fino a 14 anni."),
  ("Le tensioni interne al PCI","sotto l'influenza dei fatti d'Ungheria (1956) e dopo la morte di Togliatti (1964), il PCI avvia un percorso di autonomia dall'Unione Sovietica, cercando una via democratica e costituzionale al comunismo.")]),
]
def sents(rest):
    return [x.strip() for x in re.split(r'(?<=[.!?])\s+(?=[A-ZÀ-Ù"«])',rest) if x.strip()]
