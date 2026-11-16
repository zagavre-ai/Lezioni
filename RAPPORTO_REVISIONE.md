# RAPPORTO DI REVISIONE · Inglese AFM triennio · Lezione 10 · Work today · v2

Tag `afm-inglese-triennio-lez10` · chat della master E1 · 16/11/2026 · prof.ssa Maria Vittoria Fontanesi.
La v1 (consegnata la mattina del 16/11) non rispettava lo STOP QUALITÀ e il modello grafico Spagnolo Lez. 1 (decisioni di Sara del 16/11): questa v2 la **sostituisce sullo stesso ramo**. Stesse voci Kore, stessi testi, stessi quiz.

**Misurato:** durata 67:32.1 (4052.1 s); prof 60:53.6 **intero, senza nessun taglio** (nella v1 le pause oltre 1 s erano accorciate a 0,6 s).

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
| 10 | Struttura: sigla → presentazione con voce → per argomento: titolo, prof con slide sincronizzate, pillola di ripasso (mappa animata con voce Kore), quiz di 5 domande → glossario → riepilogo finale → finale | OK · in più: mappa finale e saluto della prof prima del glossario; schede «Verifica finale» e «Compiti» (servono alla pagina interattiva) prima del finale. Durata 67:32.1: sopra i 60 minuti perché la registrazione della prof è una sola e il prof non si taglia (precedente: lez05 69 min, una Parte) |
| 11 | PDF A4 orizzontale: slide identiche al video senza riquadro e senza fascia; mappe | `afm-inglese-triennio-lez10_slide.pdf`: 27 pagine, una per slide, stesso ordine e stessa «Pagina N» del video (fatte dagli stessi file HTML, solo senza riquadro e fascia) · mappe: `Mappe_afm-inglese-triennio-lez10.pdf`. Per Inglese AFM nella release **non ci sono mappe della prof**: le mappe sono quelle della lezione (contenuto preso solo dal materiale della prof) |

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
| consegna | pagina | mancava il PDF delle slide | `afm-inglese-triennio-lez10_slide.pdf` |

## Controlli fatti (misurati)
- durata 67:32.1 (4052.1 s) | fotogrammi 121562 (attesi 121562) OK | peso 255.6 MB (243.8 MiB) OK | 1920x1080 OK
- quiz 5 scatto 0,0 s: OK
- fermi immagine nei pezzi del docente: nessuno OK
- volume del parlato (mediana dei pezzi del docente): -16.9 LUFS OK
- sottotitoli: 788 blocchi, sovrapposti 0, oltre la fine 0, attacco sulla voce entro 0,3 s: 60% di 5 verificabili DA GUARDARE
- foglio di miniature: Inglese_Lez10_Parte1_1080p.mp4.miniature.jpg
- ESITO: DA SISTEMARE: sottotitoli

Scatto dei quiz (correlazione con il jingle):
- Q1 atteso 1303.299 trovato 1303.299 scarto +0.000 OK
- Q2 atteso 2125.365 trovato 2125.365 scarto +0.000 OK
- Q3 atteso 2911.665 trovato 2911.665 scarto +0.000 OK
- Q4 atteso 3478.631 trovato 3478.631 scarto +0.000 OK
- Q5 atteso 3872.898 trovato 3872.898 scarto +0.000 OK

Sincronia slide–prof, 6 righe a caso (che cosa si sente quando la riga si accende):
- 50:08.82 · argomento 4, slide 1, riga 3: «Information is transmitted instantaneously: it saves time and money and improves productiv» · si sente (da 1 s prima): «The main characteristic of digital communication is that information is»
- 31:52.05 · argomento 2, slide 2, riga 4: «Taxes and expenses to pay, and stress due to the constant search for new gigs.» · si sente (da 1 s prima): «work. Another issue is to do with taxes and expenses because they since they are»
- 57:10.32 · argomento 4, slide 3, riga 5: «Its name entered the English language: "I'll zoom you later", "Let's have a Zoom".» · si sente (da 1 s prima): «forms. And its name has even entered the English language as a verb as well as a noun.»
- 63:11.93 · argomento 5, slide 3, riga 5: «Numeracy and IT skills: using data to support your work, IT skills like coding.» · si sente (da 1 s prima): «developing possible solutions and finally numeracy and IT skills. This is to say using date.»
- 7:49.01 · argomento 1, slide 1, riga 4: «During recessions unemployment rises and wages are low; when unemployment drops, businesse» · si sente (da 1 s prima): «The job market clearly plays a very important role in the economy, and it is also»
- 12:35.34 · argomento 1, slide 2, riga 1: «New in-demand professions: digitalisation and technology lead to a higher demand for IT jo» · si sente (da 1 s prima): «economy. So starting with the first point, we can say that the trend of digitalization»

## Cosa NON ho potuto verificare
- Ascolto a orecchio: la verifica dell'audio è con le misure (volume, scatto dei quiz) e con la trascrizione automatica, non con l'ascolto umano.
- OCR delle slide: i testi delle slide sono generati da file di testo controllati (stesso testo dei PDF), non riletti con l'OCR.
- **Verifica finale:** nella release manca l'Excel della prof (`ENG_Amministrazione_Lez10_Verifica.xlsx`): nel ramo c'è un test `PROPOSTA_DA_VALIDARE`.
- **COMPITI_MANCANTI:** nella release manca il PDF dei compiti della prof.

## Nota sui sottotitoli (lez10)
`controllo_finale.py` segna «DA GUARDARE» (3 su 5 blocchi verificabili entro 0,3 s). I 2 blocchi fuori (8:46 e 54:18 circa) sono frasi che seguono subito un'altra frase: il controllo prende come «attacco» la coda della frase precedente (energia alta 0,8 s prima del blocco, poi pausa, poi la frase nuova che parte sul blocco). Misurato sull'energia del parlato: l'inizio del sottotitolo è giusto. Tutti i blocchi sono stati spostati sull'attacco della voce con `vttsnap.py` (135 su 788).
