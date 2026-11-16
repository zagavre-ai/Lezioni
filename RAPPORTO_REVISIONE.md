# RAPPORTO DI REVISIONE · Inglese AFM triennio · Lezione 7 · Trade and commerce · v2

Tag `afm-inglese-triennio-lez07` · chat della master E1 · 16/11/2026 · prof.ssa Maria Vittoria Fontanesi.
La v1 (consegnata la mattina del 16/11) non rispettava lo STOP QUALITÀ e il modello grafico Spagnolo Lez. 1 (decisioni di Sara del 16/11): questa v2 la **sostituisce sullo stesso ramo**. Stesse voci Kore, stessi testi, stessi quiz.

**Misurato:** durata 71:08.8 (4268.8 s); prof 62:47.8 **intero, senza nessun taglio** (nella v1 le pause oltre 1 s erano accorciate a 0,6 s).

## Confronto con il modello Spagnolo (punto 000, 1–11)
| # | Punto | Esito |
|---|---|---|
| 1 | Sigla della materia 15 s → dissolvenza → copertina | OK · `Sigla_Inglese_15s`; **tutte** le transizioni del video sono dissolvenze morbide di 1 s (nella v1 c'erano cerchi, tendine e zoom) |
| 2 | Copertina: logo, «INGLESE · VIDEOLEZIONE», titolo + barretta, card ARGOMENTI su due colonne | corretto (nella v1 era una scheda blu notte). Sulla copertina c'è la voce Kore di benvenuto, il prof non parla: copertina senza riquadro, come le «slide senza prof» |
| 3 | Slide: fondo bianco, riga «0N · ARGOMENTO», titolo Bricolage 800 + barretta, card, giallo solo sulla riga in corso | corretto (nella v1 fondo grigio chiaro #F4F7FB) |
| 4 | Piè di pagina «INGLESE · Prof.ssa Maria Vittoria Fontanesi» + «Pagina N», mai il numero della lezione | corretto (nella v1 mancava «Pagina N») |
| 5 | Riquadro prof 4:3 410×308 in x 1428 y 146, angoli arrotondati, ombra grigia morbida, testa intera, correzione immagine del kit | corretto (v1: 416×312) · correzione `eq contrast 1,04 saturation 1,03, hqdn3d 1.5:1.5:3:3, cas 0,35` sul riquadro rimpicciolito · testa e spalle intere: controllato sul foglio `controllo_minuti.jpg` |
| 6 | Fascia gialla inclinata, due righe «Maria Vittoria Fontanesi» / «PROF.SSA DI INGLESE», sempre visibile col prof | corretto (nella v1 tre righe con il corso) |
| 7 | Slide senza prof (titoli degli argomenti, glossario, ripasso finale): testo grande, logo, piè di pagina | corretto |
| 8 | Font solo Bricolage Grotesque / Figtree / DM Mono | OK per Bricolage e Figtree; DM Mono non è nel kit (`kit/tools/mappa_font`): le etichette sono in Figtree bold spaziato, come nella v1. Nessun altro font |
| 9 | Finale `Sigla_finale_5s_con_avviso_diritti.mp4` | corretto (nella v1 la vecchia sigla di chiusura, prima dei compiti); ora è l'ultimo pezzo |
| 10 | Struttura: sigla → presentazione con voce → per argomento: titolo, prof con slide sincronizzate, pillola di ripasso (mappa animata con voce Kore), quiz di 5 domande → glossario → riepilogo finale → finale | OK · in più: mappa finale e saluto della prof prima del glossario; schede «Verifica finale» e «Compiti» (servono alla pagina interattiva) prima del finale. Durata 71:08.8: sopra i 60 minuti perché la registrazione della prof è una sola e il prof non si taglia (precedente: lez05 69 min, una Parte) |
| 11 | PDF A4 orizzontale: slide identiche al video senza riquadro e senza fascia; mappe | `afm-inglese-triennio-lez07_slide.pdf`: 36 pagine, una per slide, stesso ordine e stessa «Pagina N» del video (fatte dagli stessi file HTML, solo senza riquadro e fascia) · mappe: `Mappe_afm-inglese-triennio-lez07.pdf`. Per Inglese AFM nella release **non ci sono mappe della prof**: le mappe sono quelle della lezione (contenuto preso solo dal materiale della prof) |

## Problemi trovati nella v1 e correzioni
| Minuto (v1) | Tipo | Com'era | Come è ora |
|---|---|---|---|
| tutta la lezione | audio | pause del prof oltre 1 s accorciate (prof tagliato) | prof intero, nessun taglio |
| tutta la lezione | audio | solo guadagno + limitatore | catena del kit: `aresample 48k, highpass 80, arnndn (sh.rnnn del kit), loudnorm −16, alimiter` |
| tutta la lezione | visivo | fondo grigio chiaro, riquadro 416×312, fascia su tre righe, niente «Pagina N» | modello Spagnolo (punti 3–6) |
| inizio | visivo | copertina blu notte | copertina bianca con card ARGOMENTI |
| titoli degli argomenti | visivo | schede blu notte | slide bianche con «0N · Topic N» |
| transizioni | visivo | cerchi, tendine, zoom | dissolvenze di 1 s |
| fine | visivo | vecchia sigla di chiusura prima dei compiti | finale 5 s con avviso dei diritti, in fondo |
| consegna | pagina | mancava il PDF delle slide | `afm-inglese-triennio-lez07_slide.pdf` |

## Controlli fatti (misurati)
- durata 71:08.8 (4268.8 s) | fotogrammi 128065 (attesi 128065) OK | peso 262.1 MB (250.0 MiB) OK | 1920x1080 OK
- quiz 6 scatto 0,0 s: OK
- fermi immagine nei pezzi del docente: nessuno OK
- volume del parlato (mediana dei pezzi del docente): -16.6 LUFS OK
- sottotitoli: 820 blocchi, sovrapposti 0, oltre la fine 0, attacco sulla voce entro 0,3 s: 100% di 4 verificabili OK
- foglio di miniature: Inglese_Lez7_Parte1_1080p.mp4.miniature.jpg
- ESITO: TUTTO OK

Scatto dei quiz (correlazione con il jingle):
- Q1 atteso 495.198 trovato 495.198 scarto +0.000 OK
- Q2 atteso 1029.498 trovato 1029.498 scarto +0.000 OK
- Q3 atteso 1715.464 trovato 1715.464 scarto +0.000 OK
- Q4 atteso 2766.464 trovato 2766.464 scarto +0.000 OK
- Q5 atteso 3479.030 trovato 3479.030 scarto -0.000 OK
- Q6 atteso 4076.863 trovato 4076.863 scarto +0.000 OK

Sincronia slide–prof, 6 righe a caso (che cosa si sente quando la riga si accende):
- 30:02.78 · argomento 4, slide 1, riga 3: «Consumer habits are changing: people are gradually shifting from physical shops to online » · si sente (da 1 s prima): «We need to consider e-commerce in this lesson because nowadays consumer»
- 13:27.35 · argomento 2, slide 4, riga 1: «Product retailing: businesses selling physical goods, like food, groceries and electronics» · si sente (da 1 s prima): «In general, we can identify three different categories of retailing.»
- 36:50.30 · argomento 4, slide 3, riga 3: «Social commerce: users discover and buy products directly on social media shops.» · si sente (da 1 s prima): «Then we have the S-commerce or social commerce which is tied to the tools.»
- 63:23.32 · argomento 6, slide 3, riga 1: «Employment is freely chosen. Freedom of association and collective bargaining.» · si sente (da 1 s prima): «There are 9 basic principles. Employment is freely chosen.»
- 4:11.38 · argomento 1, slide 2, riga 3: «Countries are linked by very strong connections, stronger than before.» · si sente (da 1 s prima): «Thirdly, another factor that improves commerce and trade in»
- 8:57.60 · argomento 2, slide 1, riga 1: «Home trade is the sale and distribution of products within one country, from production to» · si sente (da 1 s prima): «trade. Contrary includes the sale and distribution of products within one country.»

## Cosa NON ho potuto verificare
- Ascolto a orecchio: la verifica dell'audio è con le misure (volume, scatto dei quiz) e con la trascrizione automatica, non con l'ascolto umano.
- OCR delle slide: i testi delle slide sono generati da file di testo controllati (stesso testo dei PDF), non riletti con l'OCR.
- **Verifica finale:** nella release manca l'Excel della prof (`ENG_Amministrazione_Lez07_Verifica.xlsx`): nel ramo c'è un test `PROPOSTA_DA_VALIDARE`.
- **COMPITI_MANCANTI:** nella release manca il PDF dei compiti della prof.
