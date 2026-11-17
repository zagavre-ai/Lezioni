# RAPPORTO REVISIONE · Letteratura italiana V · Lezione 12 · Narrativa e saggistica del primo Novecento
Revisione del 17/11/2026. Video: `Letteratura_Lez12_Parte1_1080p.mp4` (a pezzi `.parte_00…`, sha256 nel file `.sha256`).
Sotto: **misurato** = misurato con uno strumento; **stima** = dedotto; **non verificato** = non ho potuto.

## 1. Misure sul video nuovo
| Controllo | Risultato |
|---|---|
| Formato | 1920x1080, 30 fps, x264 veryfast CRF 19, AAC 192k, 48 kHz (misurato) |
| Durata / fotogrammi | **56:14 (3374.7 s) · 101241 fotogrammi** = durata × 30 (misurato). **La durata è cambiata** (prima 56:43,5 = 102 104 fotogrammi): decisione di Sara 17/11 (silenzi, tagli a fine frase, mappe del prof). Tabella dei secondi vecchio → nuovo sotto |
| Peso | 193.4 MB (sotto i 400 MB) (misurato) |
| Volume | -17.0 LUFS integrato, LRA 6.5; **picco (true peak) -1.0 dBTP** (misurato con `ebur128=peak=true`; prima: 0,0 / +1,5 dBTP sull'originale del prof) |
| Scatto del jingle Quiz | `controllo_jingle.py`: **scarto +0,000 s su tutte e 5 le schede Quiz** (misurato). Prima: +0,41, +0,52, +0,66 s su 3 schede misurate (stima: ±0,1 s) |
| Silenzi > 3 s | nessuno (misurato, soglia −48 dB). Prima: 12 silenzi di 3,0–3,6 s e uno di 9,2 s (misurato) |
| Fermi immagine del prof | misurati con `freezedetect` **solo sul riquadro del prof** (412×310, n=−50 dB, d=1 s): **0 fermi ≥ 1 s durante i pezzi del prof** (misurato). I fermi rilevati altrove (102) sono schede senza prof (slide statiche) |
| Sincronia audio/video del prof | correlazione dell'audio del video finale con l'originale del prof (misurato): D0 scarto -0.015 s (corr 0.83; avvio fotogramma +0.000 s); D1 scarto -0.015 s (corr 0.84; avvio fotogramma +0.000 s); D2 scarto -0.015 s (corr 0.86; avvio fotogramma -0.013 s); D3 scarto -0.015 s (corr 0.82; avvio fotogramma -0.010 s); D4 scarto -0.015 s (corr 0.85; avvio fotogramma -0.010 s); D5 scarto -0.015 s (corr 0.84; avvio fotogramma +0.010 s). Limite regola: 0,04 s |
| PDF | slide: 59 pagine A4 orizzontale, identiche alle slide del video (senza riquadro e senza fascia); mappe: 6 pagine A4 orizzontale (una per argomento + mappa finale) |

### Secondi vecchio → nuovo (per la pagina Vimeo: la master rigenera)
| Punto | Prima (s) | Ora (s) |
|---|---|---|
| Quiz 1 | 613.1 (10:13) | 615.7 (10:15) |
| Quiz 2 | 1118.3 (18:38) | 1111.7 (18:31) |
| Quiz 3 | 1654.9 (27:34) | 1635.8 (27:15) |
| Quiz 4 | 2395.4 (39:55) | 2376.5 (39:36) |
| Quiz 5 | 3175.1 (52:55) | 3150.3 (52:30) |
| Verifica finale | 3378.6 (56:18) | 3357.0 (55:57) |
| Compiti | 3396.9 (56:36) | 3370.5 (56:10) |
| Durata totale | 3403.5 (56:43) | 3374.7 (56:14) |

`scheda_pubblicazione.json` (inizio_s, quiz_s, durata_s, t_verifica, t_compiti) e `timeline.json` sono già aggiornati ai secondi nuovi.

## 2. Confronto col modello Spagnolo (punto 000)
| # | Punto | Esito |
|---|---|---|
| 1 | Sigla 15 s → dissolvenza → copertina | OK: sigla del kit invariata («[ANALISI TESTUALE]» è nella sigla ufficiale `Sigla_Letteratura_15s.mp4`, non l'ho toccata); dissolvenza di 12 fotogrammi dalla sigla alla copertina |
| 2 | Copertina | **corretto**: logo, «LETTERATURA ITALIANA V · VIDEOLEZIONE», titolo Bricolage 800, barretta, card ARGOMENTI su due colonne |
| 3 | Slide: fondo bianco, «01 · ARGOMENTO», card | **corretto** (era fondo scuro con banda blu). Numero = numero dell'argomento |
| 4 | Piè di pagina + «Pagina N» | **corretto**, Figtree Bold (non DM Mono) |
| 5 | Riquadro 4:3 | **corretto**: 412×310 px a x=1428, y=148, angoli r=18, ombra grigia morbida, nessun bordo; il riquadro c'è solo mentre il prof parla davvero (video vivo); copertina durante la voce di benvenuto senza riquadro |
| 6 | Fascia gialla due righe −3° | **corretto**, sempre visibile con il prof |
| 7 | Slide senza prof | **corretto**: approfondimenti, mappe, ripassi, glossario, riepilogo, schede di servizio |
| 8 | Font | Bricolage Grotesque 800, Figtree (nessun altro) |
| 9 | Finale 5 s con avviso diritti | OK: sigla finale del kit riusata, con `finale.wav` |
| 10 | Struttura | OK: sigla, presentazione, 5 argomenti (titolo, prof con slide, approfondimenti, ripasso, quiz), mappa, glossario, riepilogo, finale |
| 11 | PDF slide + mappe A4 | consegnati |

**Card in corso** (aggiornamento 01:30): bordo giallo sottile, numero su pallino giallo, fondo bianco; le altre card con bordo grigio chiaro e ombra grigia morbida. **Jingle** (01:20): `quiz.wav` sulle schede Quiz, Verifica e Compiti; `titolo.wav` sul titolo dell'argomento; `repaso.wav` (−8 dB) sulla pillola di ripasso; `finale.wav` sulla sigla finale; `trans.wav` ai raccordi col prof. **Transizioni:** dissolvenza di 8 fotogrammi tra un pezzo e l'altro, mai taglio secco.

**Testa nel riquadro:** il taglio 4:3 prende la webcam dell'originale (247×139 px, ritaglio 185×139 ingrandito 2,2×: immagine morbida perché l'originale è piccola). **In quasi tutta la lezione i capelli toccano il bordo alto già nell'originale** (es. 0:20, 2:30, 5:30, 8:00, 10:40, 13:00 dell'originale): non risolvibile.

## 3. Problemi trovati e correzioni
| Minuto (vecchio) | Tipo | Com'era | Correzione |
|---|---|---|---|
| tutto | visivo | grafica vecchia: fondo scuro/azzurrino, banda blu laterale, riquadro piccolo nella banda, nessuna fascia gialla | tutto rifatto nel modello Spagnolo (59 pagine) |
| 4:05, 10:15, 18:50, 31:20 circa | audio | **ripetizioni** ai raccordi del prof: ogni ripresa riparte 0,5–1,0 s prima di dove era finito il pezzo precedente (misurato per correlazione con l'originale: 1,00 / 0,52 / 0,74 / 0,81 s) | i pezzi sono rifatti dall'originale senza sovrapposizioni |
| 4:58 (D1), 21:49 (D3) | audio | **pezzi del prof tagliati a metà frase**: D1 finiva su «…però serve per…», D3 su «…nella ricerca del tempo perduto» mozzando la parola «Ricerca»; D2 finiva a metà parola in «Marcel Proust è il re–» | ogni pezzo finisce ora a fine frase (tabella sotto) |
| 1665–1810 s (arg. 4) | visivo | card 1 («La realtà come assurdo») evidenziata 145 s prima che il prof la nominasse (la nomina a 722 s dell'originale) | evidenziazioni rifatte dal parlato del prof (tempi parola per parola) |
| tutto | visivo | evidenziazioni scelte a occhio | rifatte dalla trascrizione; la card «La realtà esteriore» (Woolf) non viene mai nominata dal prof: resta non accesa |
| 8:24–9:28, 18:10–19:00, 26:30–27:25, 38:10–39:10, 52:00 circa | mappe | **mappe inventate da noi** (6 rami, es. «Nietzsche/Bergson/Freud…»), non quelle del prof | sostituite con la **mappa del prof** (8 riquadri) in grafica v3, letta da voci nuove R9, R10, R17–R20; contenuto identico, tranne «RECERCHE» → «RECHERCHE» (refuso) |
| silenzi | audio | 12 silenzi di 3,0–3,6 s e uno di 9,2 s | tolti: blocchi accorciati alla durata della voce + 1,3 s; nessun silenzio > 3 s |
| schede Quiz | audio | scatto del jingle a +0,41/+0,52/+0,66 s dall'inizio atteso | jingle `quiz.wav` rimesso a +0,5 s esatto: scarto 0,000 s |
| schede Verifica / Compiti / «ora tocca a te» | audio | senza jingle, grafica diversa dal modello | rifatte nel modello, con jingle |
| vtt | testo | errori sistematici di trascrizione: «sagistica», «falsarica», «Buongiorno, è benvenuti la lezione», «Mercel Pust», «Berkson», «Ciachia», «Compre» (Combray), «Cafe», «Sebo/Slevo» (Svevo), «Blasbury», «Jodith»… | rilette e corrette tutte le frasi del prof (219 segmenti); aggiunte le voci narranti (testo esatto). 804 cue, max 2 righe × 42 caratteri |
| testo_youtube | testo | capitoli sbagliati (5:49, 9:15, 12:58, 19:27, 25:51 invece dei minuti reali) | capitoli ricalcolati dai secondi veri |
| scheda | testo | titolo «Narrativa e saggistica del primo Novecento · Parte 1» | «Letteratura V · Lezione 12 · Narrativa e saggistica del primo Novecento» |
| audio prof | audio | non pulito con la catena del kit; l'originale ha picchi a +1,5 dBTP | rifatto dall'originale: `aresample 48000, highpass 80, arnndn (sh.rnnn), loudnorm −16 (2 passate), alimiter`; picco ≤ −1 dBTP |
| quiz | testo | titolo Q2 «Il romanzo del primo Novecento» | «Il nuovo romanzo del Novecento» (come voce e titolo argomento) |

### Fine e inizio di ogni pezzo del prof (aggiornamento 01:25)
| Pezzo | Inizio (s) | Fine (s) | Prime parole | Ultime parole dette | Frase finita |
|---|---|---|---|---|---|
| D0 | 45.9 | 141.9 | Buongiorno e benvenuti alla lezione sulla… | …carrellata piuttosto breve da questo punto di vista. | sì (fine frase; niente parole mozzate in partenza) |
| D1 | 146.4 | 300.4 | Allora, abbiamo più volte detto, accennato,… | …di nuovo, fare il punto su tante questioni. | sì (fine frase; niente parole mozzate in partenza) |
| D2 | 624.2 | 768.5 | Ecco, capite che questo terremoto culturale,… | …morte a Venezia. E poi Marcel Proust, appunto. | sì (fine frase; niente parole mozzate in partenza) |
| D3 | 1120.2 | 1294.4 | Marcel Proust è il recupero memoriale,… | …di me, dall'azione distruttiva degli anni e dell'oblio. | sì (fine frase; niente parole mozzate in partenza) |
| D4 | 1644.3 | 1986.0 | Insomma, il protagonista di Marcel Proust… | …comprendere per analizzare la società, capite? Franz Kafka. | sì (fine frase; niente parole mozzate in partenza) |
| D5 | 2385.0 | 2713.9 | Ecco, appunto, i conflitti, le alienazioni… | …alle strutture economiche e culturali del proprio tempo. | sì (fine frase; niente parole mozzate in partenza) |

## 4. Pagine del libro in alta risoluzione
Lezione 12: **nessuna pagina del libro** (elenco delle regole: la 12 non ne ha). Punto saltato.

## 5. Cosa NON ho verificato / limiti
- **Ascolto umano:** non ho ascoltato fruscio, ronzio, «metallico» dopo la pulizia, né la pronuncia delle voci Kore. Le voci nuove sono state ritrascritte con `trascrivi.py` e confrontate col testo: nomi e opere risultano resi correttamente («Recherche», «Woolf» come «Wolf», «Dalloway»); i dubbi dell'ASR sono solo parole brevi. **Non verificato all'ascolto.**
- **Sincronia labbra/voce:** misurata solo come scarto audio/video dell'allineamento (tabella §1): lo stesso offset vale per audio e video; la bocca non è misurabile (webcam piccola). 
- **Evidenziazioni:** calcolate dal parlato (Parakeet), precisione ±0,3 s (voci) e ±1 s (prof); da riguardare in 4 punti a campione.
- **Webcam morbida (2,2×) e capelli sul bordo alto:** limite dell'originale, non risolvibile.
- **Testi che il prof dice in modo poco chiaro, trascritti con la forma più probabile — DA CONFERMARE COL PROF:** «autore di capolavori come *La morte a Venezia*» (Thomas Mann, ~6:25 dell'originale: la trascrizione automatica dava «il bel fanciullo il mare»); «Nel sedicesimo secolo, *pieno Medioevo*» (17:50 dell'originale); frase «dice la… / sostiene la…» a 20:00 dell'originale (parola non comprensibile, **omessa** nei sottotitoli); «Siamo a *Praga*» (10:50).
- **Domanda 7 della verifica del prof** («lotta per il voto alle donne»): la risposta giusta non compare nella lezione; l'ho lasciata come l'ha scritta il prof. Domande 6 («debito contratto dai genitori»): idem, più dettagliata del video. **DA CONFERMARE COL PROF.**
- **Mappa del prof:** la freccia da «L'inetto» a «Spazio, tempo…» e il gruppo «Autori principali» (senza riquadro nella mappa del prof) sono resi come rami dello stesso albero; nessun testo aggiunto o tolto.
- **Date/dati che non coincidono:** nessuno trovato tra mappa, slide e voce.
- **Voci Kore dei ripassi (S1–S5), glossario, riepilogo, introduzione:** riusate dalla consegna precedente (testo ricavato dall'ascolto automatico: non c'era nel json). Non rigenerate.
- Quiz riletti contro le slide del prof: coerenti; invariati salvo il titolo Q2.
- La master deve rigenerare la pagina Vimeo (nuovi secondi).

## 6. Come ho verificato
Trascrizione completa del video vecchio e dell'originale (Parakeet TDT via `trascrivi.py`, 770 + 219 segmenti), 3405 fotogrammi a 1/s sul video vecchio, correlazione audio per trovare i pezzi del prof nell'originale, trascrizione di tutte le voci narranti e confronto col testo (difflib), 113 fotogrammi sul video nuovo (`controllo_minuti.jpg`, uno ogni 30 s), `controllo_jingle.py`, `ebur128`, `silencedetect`, `freezedetect` sul riquadro, correlazione audio finale/originale per la sincronia, controllo che la somma dei pezzi sia uguale ai fotogrammi del video (101241).