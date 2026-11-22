# Rapporto di controllo indipendente - Verga (final4.mp4, 59:20)

Controllore: agente separato, sola lettura. Metodo: fotogrammi estratti con ffmpeg e letti uno a uno (fogli in /tmp/w/ctrl_agent/*.png), misure in pixel sui fotogrammi a 1920x1080, correlazione audio delle voci MQ con l'audio del video (picco 0,98-1,00 su 21/21), differenze di fotogramma per gli stati fermi, trascrizione /tmp/w/asr/orig.json per il bordo giallo. Tempi sempre del video reale (m:ss).

## Esito sintetico
| # | Punto | Esito |
|---|-------|-------|
| 1 | Card: max 3, frase intera, testo >=36 px | OK (con osservazioni sulle pagine del libro) |
| 2 | Bordo giallo = ciò che dice il prof (10 punti) | NON OK: 8 punti su 15 non corrispondono, solo 1 entro ±1 s |
| 3 | Nessuno schermo uguale >3 min | NON OK: Pagina 6 per 4:22, Pagina 11 per 3:38 |
| 4 | Riquadro prof, fascia gialla | Riquadro OK; fascia gialla assente per 27 min di slide |
| 5 | Mappa | In parte: un riquadro alla volta NON rispettato (gruppi), nome del docente nel piè di pagina |
| 6 | Copertina | OK |
| 7 | Numeri lezione, fondo, font, nome docente | Nome docente scritto in tutte le animazioni (piè di pagina): NON OK. Resto OK |
| 8 | Difetti grafici | Elenco sotto (QR, marchi editore, testi tagliati, ecc.) |

## 1) Card
- Campionati 42 fotogrammi di slide/ripasso (sl0-sl3, h1-h3, rp1-rp3, r3c): 24 slide col prof, 18 slide/pagine di ripasso, glossario e ripasso finale.
- Max card per slide: 3 (solo le pagine di ripasso R1 pag.8-9, R3 pag.53, R4 pag.68-69, R5 pag.92-93 hanno 3 card; le slide col prof ne hanno 2). Nessuna slide con 4 o più. OK.
- Nessuna card con "…" o iniziale minuscola; tutte le card dei ripassi sono frasi intere con la maiuscola (verificato su tutte le pagine dei ripassi: 10:07, 10:20, 10:31, 28:21, 28:36, 33:10, 43:40, 44:04, 53:48, 54:08). OK.
- Misura testo: riga card a 1:48,5 alta 37 px dall'ascendente al discendente, interlinea 60 px: corpo circa 40 px. >=36 OK. Ripassi: stessa grandezza (interlinea 60 px).
- Non misurato riga per riga su tutti i fotogrammi: stima visiva coerente su tutti i campioni.
- Osservazione: nelle slide con pagina del libro (T3, T5, T7, T8, T9, T10, T12: da 16:41 a 52:40 e altri tratti) il "testo" è l'immagine della pagina con corpo 10-14 px, illeggibile per un utente BES (non sono card, ma non rispettano "testo >=28-30 px").

## 2) Bordo giallo vs parole del prof (trascrizione, tempo originale = montaggio + scarto del pezzo)
Fotogramma guardato a ogni passaggio; "anticipo" = bordo acceso prima dell'inizio della frase della card.
| Minuto | Card accesa | Cosa dice il prof (orig.) | Esito |
|---|---|---|---|
| 2:31 | "Abbandono degli studi legali" (pag.3) | 106,6-113,6: "...maestro Antonino Abate... patriottismo" (contenuto della card 1). Studi legali/Giurisprudenza: mai trovati nella trascrizione | NON OK |
| 2:39 | "Prime opere: Amore e patria" (pag.4) | 114,6 "...opere giovanili... Amore e patria" (frase a 117,2) | OK entro 2,6 s |
| 2:59 | "Le letture giovanili" (pag.5) | 135,1 "La sua formazione si distacca... tradizione umanistica" | OK (0,5 s) |
| 4:52 | "Il periodo a Firenze" (pag.6) | acceso a 247,6; "Firenze 1869" detto a 303,8; testo affine ("liberarsi dei limiti...") da 253 | ANTICIPO 5,5 s (56 s sulla parola Firenze) |
| 6:52 | "La svolta milanese" (pag.6) | acceso a 367,6, ma il prof parla ancora di Firenze; Milano a 372,4 | NON OK (4,8 s) |
| 9:14 | "Il ritorno definitivo 1893" (pag.7) | acceso a 509,6; "nel novantatré rientra a Catania" a 514,3 | NON OK (4,7 s) |
| 12:22 | "Il principio dell'impersonalità" (pag.11) | acceso a 636; "poetica... principio cardine dell'impersonalità" 641-649, spiegazione fino a 748 | tema OK, anticipo 5-13 s |
| 14:22 | "La tecnica dello straniamento" (pag.12) | acceso a 756,0; frase a 757,5 | OK entro 1,5 s |
| 15:02 | "L'artificio della regressione" (pag.13) | acceso a 796; "L'artificio della regressione" detto a 871,1 | NON OK (75 s di anticipo; nel frattempo parla d'altro) |
| 28:56 | "Il pessimismo verghiano" (pag.47) | acceso a 1569; il prof dice "ciclo interrotto, 5 romanzi" (1574-1602); "pessimismo" mai detto | NON OK |
| 30:12 | "La fiumana del progresso" (pag.47) | acceso 1645; frase sulla fiumana a 1620,9 | tema OK, ritardo 24 s |
| 31:26 | "Il progetto del ciclo: 5 romanzi" (pag.48) | acceso a 1719,4; detto a 1576-1602 (2 min prima); a 1719 parla dell'osservatore verista | NON OK |
| 31:58 | "L'interruzione dell'opera" (pag.49) | acceso 1751; detto a 1574; a 1751 parla di benessere materiale/più deboli | NON OK |
| 33:34 | "I Malavoglia (1881)" (pag.55) | acceso 1797; frase "I Malavoglia pubblicato nel 1881" a 1824,5 | anticipo 27 s |
| 40:22 / 40:30 | "Mastro-don Gesualdo (1889)" e "Il dramma del vincitore" (pag.58-59) | a 2205-2213 il prof descrive gli estratti dei Malavoglia (capitoli I, VII, XV) | NON OK |

Esito: solo 1 punto su 15 rispetta ±1 s (2:59); 3 sono tolleranti (2:39, 14:22, tema giusto); 8 sono NON OK. Cause: schede sulle Vinti in ordine diverso da quello del parlato; card di Mastro-don Gesualdo accese mentre il prof parla dei Malavoglia; bordo acceso alla fine della frase precedente invece che all'inizio della propria.
Inoltre la card 1 "I Malavoglia (1881)" resta accesa da 33:34 a 40:14 (400 s) cambiando solo le "Parole chiave".

## 3) Stesso schermo oltre 3 minuti (differenze di fotogramma confermate)
- "Pagina 6" (I grandi spostamenti): da 4:52 a 9:14 = 262 s; cambia solo il bordo giallo a 6:52. NON OK.
- "Pagina 11": da 10:44 a 14:22 = 218 s; cambia solo il bordo a 12:22. NON OK.
- Pagine 55-57 (stessa slide, cambiano solo le "Parole chiave" ogni 133 s): 33:34-40:13 = 400 s con la stessa card accesa. A rischio.
- Altre: Pagina 47 150 s, Pagina 5 113 s, Pagina 13 106 s: sotto i 3 min.
- Ripassi, glossario, mappa, schede: tutti sotto i 3 min.

## 4) Riquadro del prof e fascia gialla
- Riquadro 412x309 circa a x=1428,y=148, angoli arrotondati, ombra: OK, misurato a 1:48,5.
- Assente in sigla, copertina (0:15-0:41), titoli argomento, titoli ripasso, ripassi, quiz, glossario, ripasso finale, mappa, schede finali: 265 fotogrammi campionati ogni 3 s fuori dalle slide, nessun riquadro (i valori alti rilevati sono sigla nera e riquadri della mappa). OK.
- Compare a 0:44,9 (prima parola del prof a 0:45,4). OK.
- DIFETTO: la fascia gialla col nome compare in tutte le slide "slide" (103/103 fotogrammi) ma in nessuna slide con le card (0/60 fotogrammi; in totale circa 27 min 34 s di video: 1:05-9:14 e 9:14-9:42, 10:44-14:22 e 17:08-17:38, 28:56-30:00, 33:34-40:30). Il riquadro del prof resta senza nome per metà lezione.
- Non verificato: se in ogni istante la voce del prof è presente mentre il riquadro è visibile (controllo sui confini: primo e ultimo parlato dei 5 pezzi).

## 5) Mappa (54:25 - 56:47)
- Voci MQ01-MQ21 individuate nell'audio del video (correlazione 0,98-1,00): MQ01 54:25,7 ... MQ21 56:34,3-56:42,6. Intere, non troncate.
- Costruzione: 21 voci, 21 passi, MA in 4 passi si accendono più riquadri insieme: MQ03 (Vita + 1840), MQ09 (Formazione + Irregolare + Scrittori francesi, già visibili a 54:24,9 prima della voce), MQ10 (Poetica + Attenzione ai problemi sociali), MQ14 (Opere + Scene umili). Regola "un riquadro alla volta con la sua freccia": NON pienamente rispettata. Le frecce sono trattini neri di 4-6 px quasi invisibili, non frecce blu notte leggibili.
- Riquadro acceso in giallo = riquadro letto: controllati tutti i 21 a metà voce, corrispondenza OK (MQ01 Verga, MQ04 1865 Firenze, MQ07 1893, MQ11 Impersonalità, MQ15 Storia di una Capinera, MQ17 La Lupa, MQ19 I Malavoglia, MQ21 La roba, ecc.). Sincronia di partenza entro 0,1 s nei 3 controlli a inizio voce.
- Fermo finale: ultimo cambiamento a 56:43,0; schermata immobile fino a 56:47,3 = 4,2 s. OK.
- Colori e legenda: pesca, celeste, paglierino, menta (lilla in legenda, non usato), legenda in alto a destra. OK. Nessun marchio di terzi, nessuna foto dell'autore, nessun logo. OK.
- Testo dei riquadri: righe con ascendente-discendente 32 px, interlinea 41 px: corpo circa 34 px. Al limite (34 OK).
- Testi vs voci (anni in lettere tolti): identici per MQ06, 07, 08, 11, 12, 15-21. Diversi: MQ02 (voce "È considerato...", riquadro senza "È"), MQ03-05 (riquadro "1865 · a Firenze" vs "Nel 1865 va a Firenze"), MQ09, MQ10, MQ14 (riquadri abbreviati in tre parole chiave), MQ13 (voce "Una lingua vicina al parlato", riquadro "Lingua vicina al parlato"). Esito: non identici.
- DIFETTO: in basso a sinistra, per tutta la mappa, "LETTERATURA ITALIANA V · Prof. Giorgio Mazzotti": nome del docente nell'animazione. L'ultima fila di riquadri (1922 · muore a Catania) arriva a 10-15 px dal piè di pagina.
- Non verificato: confronto con la mappa originale del docente (struttura, frecce, parole); pronuncia delle voci (nessun ascolto umano; MQ11 trascritta "scride" dal riconoscimento: da ascoltare).

## 6) Copertina
- 0:15-0:41: titolo "Giovanni Verga" intero, in una riga, 0:20 con evidenziazione degli argomenti uno per uno; nessun riquadro; sopra la copertina col prof (0:45-1:05) il riquadro è in alto a destra e sotto non c'è nessun titolo (solo la fascia gialla). OK.
- Osservazione: l'elenco "Argomenti" ha corpo circa 29 px (righe da 28 px), l'etichetta "ARGOMENTI" 10 px; occupa solo metà schermo.

## 7) Numeri di lezione, fondo, font, nome del docente
- Numeri di lezione: nessuno trovato. Presenti "Argomento 01 di 05", "Quiz 1" e "Pagina N" (numerazione delle pagine, non di lezione).
- Fondo bianco puro nelle schede (misurato 252-255, appena sotto il bianco puro: da verificare se è #FFFFFF); sigla e saluto finale neri (previsti).
- Font: titoli Bricolage Grotesque, testo Figtree, etichette Figtree Bold: visibili e coerenti. Nella sigla (0:15, fissa) compare "[ANALISI TESTUALE]" in carattere a spaziatura fissa tipo DM Mono, e la sigla non è di "Letteratura italiana - Verga": da verificare con la master.
- Nome del docente: la voce non lo dice (testi.json: nessuna occorrenza). Ma il piè di pagina "LETTERATURA ITALIANA V · Prof. Giorgio Mazzotti" è scritto in OGNI scheda animata: copertina e argomenti (0:15-0:41), titoli argomento, titoli ripasso, ripassi, quiz, glossario, ripasso finale, "Fine della lezione", verifica, compiti, e la mappa. NON OK (regola: nome solo nella fascia gialla).

## 8) Difetti grafici con minuto
1. QR "AUDIOLETTURA" dell'editore visibile nella pagina del libro: 40:37-40:48 (Pagina 60), 42:37-42:50 (Pagina 65), 44:18-44:28 (Pagina 70), 52:40-53:06 (Pagina 89). Altri non rilevati con il modello, ma controllati a vista solo i campioni.
2. Marchi/pulsanti dell'editore nelle pagine: "ANALISI INTERATTIVA NEL LIBRO DIGITALE" con cursore, "TESTO CHIAVE", "ENTRA NEL TESTO", icona "I DIRITTI/UBITI" in 16:41-16:55 (Pagina 14), 32:06-32:18 (Pagina 50, anche testo guasto "da . . .ʻ…"), 41:03-42:03 (Pagina 62), 48:40-49:00 (Pagina 80).
3. Testo tagliato in cima/fondo dentro la card-pagina (pagine del libro ritagliate a metà riga o a metà nota): 16:41 (Pagina 14, nota in basso a sinistra), 21:49 (Pagina 19, inizio "un arcolaio" a metà frase), 22:43 (Pagina 23, nota "ciò che è" tagliata in fondo), 24:33 (Pagina 31), 40:42 (Pagina 60), e su quasi tutte le pagine del libro (pagine ritagliate a metà riga).
4. Testo pagina del libro troppo piccolo (circa 10-14 px) in tutte le slide col libro (16:41-52:40, ~35% del video).
5. Piè di pagina col nome del docente su tutte le animazioni (v. punto 7).
6. Glossario spezzato su due pagine (Pagina 94 e 95, 56:47-57:46): tabella spezzata in due (regola: mai spezzate). Il ripasso finale (57:46-58:55) è su tre pagine.
7. Quiz: le schede "Pausa del video, 5 domande" durano 5 s e non contengono le domande; verifica finale (58:57-59:06) e compiti (59:15-59:20) sono solo schede di 5 s: il test Excel della verifica e i compiti del docente non sono dentro il video (fuori dal perimetro dei miei 8 punti, segnalato).
8. Schede di titolo, quiz e ripasso con fondo bianco: la regola 4 chiedeva "blu scuro animato"; seguito il fondo bianco richiesto dal brief: da confermare.

## Altri controlli fatti (fuori dai punti)
- Taglio del pezzo P1 a 9:42,9 (fotogramma 17486): il livello audio è 69-70 dB fino a 40 ms dalla fine, poi dissolvenza: la parola finale ("...millenovecentoventidue") è tagliata sulla sillaba finale (ultimo token a 537,99 in originale, taglio a 538,0). Probabile taglio a metà parola. Fine P3 (32:43,7, orig 1797,05 "d'accordo?") è al limite: taglio 0,05 s dopo l'inizio dell'ultima sillaba. Fine P2, P4, P5: OK (energia decrescente).
- Voci MQ trascritte in /tmp/w/voxq/MQ*_t.json: corrispondono al testo (cifre al posto delle lettere).

## Non verificato
Sincronia labbra/voce (0,04 s), timbro/LUFS, bordi voci <0,03, quiz scatto 0,0 s, fotogrammi=durata*30 (106796/30 = 3559,87 s torna), peso (391 MB torna), glossario/ripassi con voce (solo visivo), pronuncia dei nomi, qualità/nitidezza di tutte le immagini (solo campioni: la webcam del prof è morbida ma originale).
