# RAPPORTO DI REVISIONE · Letteratura italiana V · Lezione 12 · Prof. Giorgio Mazzotti

**Stato: REVISIONATA · video rifatto nel modello Spagnolo (punto 000) · 17/11/2026**

- Durata: **56:43 → 55:28** (3403.5 s → 3328.2 s). La durata è cambiata per decisione di Sara (17/11 00:40): mappe solo del prof (voci nuove R1–R6, più corte), tagli del silenzio, jingle del kit.
- Video 1920×1080, 30 fps, x264 veryfast CRF 19, AAC 192k; fotogrammi = durata × 30 (vedi misure).
- Cosa è **misurato** e cosa è **stima**: tutto ciò che è in «Misure» è misurato sul file finale; i sottotitoli sono **trascrizione automatica corretta** (stima di correttezza, vedi «Non verificato»).

## Misure sul file finale
```
== SCARTO AUDIO/VIDEO del prof (correlazione audio finale vs originale)
D0 scarti (s): [-0.005, -0.005, -0.005]
D1 scarti (s): [-0.005, -0.005, -0.005]
D2 scarti (s): [0.0, 0.002, -0.005]
D3 scarti (s): [0.002, 0.01, -0.005]
D4 scarti (s): [-0.012, -0.005, -0.005]
D5 scarti (s): [-0.012, 0.002, 0.0]
== FERMI IMMAGINE nel riquadro del prof
D0 fermi >=1 s: 0
D1 fermi >=1 s: 0
D2 fermi >=1 s: 0
D3 fermi >=1 s: 0
D4 fermi >=1 s: 0
D5 fermi >=1 s: 0
== MISURE GENERALI
durata 3328.167 s (55:28.2) fotogrammi 99845 (durata*30=99845) peso 317.8 MB 1920x1080
Summary: |  |   Integrated loudness: |     I:         -16.5 LUFS |     Threshold: -27.3 LUFS |  |   Loudness range: |     LRA:         7.0 LU |     Threshold: -37.4 LUFS |     LRA low:   -21.3 LUFS |     LRA high:  -14.3 LUFS |  |   True peak: |     Peak:       -1.4 dBFS | 
== SILENZI >=2,8 s
  144.4 s per 3.1 s  (blocco T1)
  619.3 s per 3.1 s  (blocco T2)
  1113.5 s per 3.0 s  (blocco T3)
  1694.2 s per 3.1 s  (blocco T4)
  2264.7 s per 2.8 s  (blocco AN19)
  2367.4 s per 3.0 s  (blocco T5)

== JINGLE QUIZ (kit/tools/controllo_jingle.py)
Q1 atteso 613.967 trovato 613.994 scarto +0.027 OK
Q2 atteso 1108.067 trovato 1108.094 scarto +0.027 OK
Q3 atteso 1688.833 trovato 1688.860 scarto +0.027 OK
Q4 atteso 2361.967 trovato 2361.995 scarto +0.028 OK
Q5 atteso 3121.600 trovato 3121.637 scarto +0.037 OK

Nota silenzi: restano le code dei jingle titolo (3,0–3,1 s a -45 dB) nei 5 titoli di argomento e 2,8 s in AN19; nessun silenzio > 3,5 s.
```

## Tabella di confronto con il modello Spagnolo (punto 000)
| # | Punto | Esito |
|---|---|---|
| 1 | Sigla della materia (15 s) → dissolvenza morbida → copertina | OK: sigla del kit `Sigla_Letteratura_15s.mp4`, poi dissolvenza di 1 s alla copertina |
| 2 | Copertina: logo, riga piccola, titolo grande con barretta, card «ARGOMENTI» | OK (corretto: prima c'era solo il titolo su fondo blu scuro, senza argomenti) |
| 3 | Slide su fondo bianco, riga «01 · ARGOMENTO», titolo + barretta, card/tabelle | OK (corretto: prima fondo blu scuro e banda blu) |
| 4 | Piè di pagina «LETTERATURA ITALIANA V · Prof. Giorgio Mazzotti» + «Pagina N» | OK, Pagina N progressiva nell'ordine del video (58 pagine) |
| 5 | Riquadro prof 4:3 ≈410×308, x1428 y148, angoli arrotondati, ombra grigia morbida, niente bordo blu | OK: 410×308, ritaglio 4:3 dal video originale (correzione immagine del kit: contrasto 1,04, saturazione 1,03, hqdn3d 1.5:1.5:3:3, cas 0.35). **Limite della sorgente:** la webcam nell'originale è un riquadro di soli 247×138 px, quindi il ritaglio è ingrandito ~2,2×; in alcuni minuti la sommità della testa è tagliata già nell'originale (la webcam inquadra stretto) |
| 6 | Fascia gialla inclinata (−3°), due righe, «PROF. DI LETTERATURA ITALIANA» | OK, sempre visibile dove c'è il prof |
| 7 | Slide senza prof | OK |
| 8 | Font Bricolage / Figtree; etichette in **Figtree Bold** maiuscolo spaziato (aggiornamento 15:10) | OK (DM Mono tolto) |
| 9 | Finale `Sigla_finale_5s_con_avviso_diritti.mp4` | OK |
| 10 | Struttura obbligatoria | OK: sigla → presentazione → 5 argomenti (titolo, prof, approfondimenti, ripasso, quiz) → glossario → riepilogo → finale |
| 11 | PDF A4 orizzontale | OK: `Letteratura_Lez12_slide.pdf` (58 pagine = le 58 slide del video, senza riquadro e nome) e `Letteratura_Lez12_mappe.pdf` (1 pagina) |

## Problemi trovati e come sono stati corretti
| Minuto (vecchio video) | Tipo | Com'era | Come l'ho corretto |
|---|---|---|---|
| tutto | visivo | Grafica non conforme al modello: fondo blu scuro, banda laterale blu, riquadro piccolo, nome senza fascia gialla | Rifatte tutte le 58 slide nel modello Spagnolo (HTML → PNG 1080p), riquadro 4:3 dall'originale |
| 0:17–2:23 | visivo | Presentazione: sulla slide solo il titolo, non gli argomenti; copertina ferma mentre il prof parla | Copertina con card «ARGOMENTI» (5 voci); il riquadro del prof compare solo mentre il prof parla davvero (video vivo) |
| 27:45–28:42 (inizio D4 vecchio) | audio/struttura | Dopo il quiz di Proust e il titolo «Kafka» il prof parlava ancora di Proust per 57 s (taglio D3/D4 sbagliato di 57 s) | Taglio spostato alla fine della frase «…Va bene?» (orig. 633,7 s): ora tutta la parte su Proust è prima di quiz e titolo di Kafka |
| D4/D5 | audio | Il pezzo di Kafka finiva a metà («…conflitti delle nazioni in Kafka» tagliato 4,6 s prima) e la frase finiva in D5 | Taglio spostato a fine frase (orig. 915,6 s) |
| D1→D2 (4:58/10:23) | audio | Pezzo D1 finito a metà frase («…però serve per») e 1 s di audio ripetuto all'inizio di D2; sovrapposizioni 1,0 / 0,5 / 0,74 / 0,8 s ai giunti D1–D5 (3,1 s ripetuti in totale) | Pezzi contigui dall'originale, tagli a fine frase, nessuna sovrapposizione |
| D2 fine / D3 inizio | audio | 5,6 s di silenzio del prof fermo (nessuna parola da 394,3 a 401,2 nell'originale) | Silenzio tolto dal montaggio (D2 finisce a 394,9; D3 inizia a 400,5, prima di «La recherche…») |
| 53:20 ca. | visivo/sync | Glossario: la voce legge Positivismo, Durata, Inconscio, **Inetto**, Flusso, Memoria involontaria, Straniamento, ma sullo schermo l'ordine era diverso (Flusso e Memoria prima di Inetto) | Ordine delle voci uguale alla voce; evidenziazione a tempo con la voce |
| 8:24, 25:59, 38:09, 54:04 e altre 2 | visivo/testo | Mappe concettuali inventate da noi (rami «es.» ecc.), non quelle del prof | Solo la mappa del prof (`MAPPE/LEZIONE 12.pdf`) con i suoi 7 riquadri e 3 frecce; voci nuove R1–R6 (le leggono); stessa mappa in 6 punti con evidenziato il riquadro di cui si parla (il prof ne ha una sola per tutta la lezione: «una per argomento» non è possibile con altro contenuto) |
| scheda / youtube | testo | `testo_youtube.txt` con capitoli sbagliati (es. «2. Il romanzo» a 5:49 invece di 10:18); titolo scheda non nel formato | Capitoli ricalcolati dalla timeline nuova; titolo «Letteratura V · Lezione 12 · …» |
| compiti | testo | `compiti.json` con chiavi diverse dal formato richiesto | Formato `{titolo, esercizi:[{n,tipo,testo}]}`, testo identico al PDF del prof |
| sottotitoli | testo | `.vtt` con molti errori (es. «sagistica», «falsarica», «cennati», «Mercel Pust») e cue sovrapposti | Rifatto sul video nuovo (trascrizione con tempi; voce Kore dal testo originale; termini corretti; rumori ASR inglesi tolti) |
| Q/T/S | audio | Titoli argomento e ripassi senza jingle; schede in silenzio per 3–4 s; transizioni senza suono | Jingle del kit: `titolo.wav`, `repaso.wav` (ripasso, con 3,3 s di jingle prima della voce), `quiz.wav` (già presente), `trans.wav` tra pezzi |
| tutto | audio/sync | Audio dei pezzi invariati con tempi irregolari fino a 0,18 s rispetto al video (nel file vecchio) | Audio rifatto per tempo-contenitore, scarto ora ≤ 0,01 s sul prof (misurato) |
| AN13, D5, ultime schede | audio | Silenzi > 3 s (fine di AN13 3,1 s; schede finali 9–10 s) | AN13 accorciato di 1 s; schede finali accorciate e con suono |
| PDF | testo | `dispensa_A4.pdf` non coincideva con le slide del video | Sostituito da `_slide.pdf` (58 pagine, stesse slide) e `_mappe.pdf` |

## Pezzi del prof: inizio e fine (frase finita sì/no)
| Pezzo | Minuto nel video nuovo | Prime parole | Ultime parole | Frase finita |
|---|---|---|---|---|
| D0 | 0:45–2:21 | sulla narrativa e la saggistica del primo novecento. | carrellata piuttosto breve da questo punto di vista. | sì |
| D1 | 2:27–5:01 | Allora. Abbiamo più volte detto il superamento, accennato | dire. Nuovo fare il punto su tante questioni. | sì |
| D2 | 10:22–12:47 | Ecco, capite che questo, questo terremoto culturale, definia | fanciullo il mare. E poi Marcel Proust, appunto. | sì |
| D3 | 18:36–22:29 | La recherche du temps perduto. La ricerca del | corrispondenze della coscienza e narrativa psicologica. Va bene? | sì |
| D4 | 28:17–32:59 | Parliamo anche di Franz Kafka, quindi oltre la | Ecco appunto i conflitti delle nazioni in Kafka. | sì |
| D5 | 39:30–44:56 | E adsiamo a Virginia Woolf, in coda, in | alle strutture economiche e culturali. del proprio tempo. | sì |

Nota: i tagli sono nelle pause fra due frasi della trascrizione con tempi parola per parola; l'inizio di D0 («Buongiorno e benvenuti…») non compare nella trascrizione automatica ma è nel sottotitolo (riletto dal vecchio `.vtt`).

## Mappe, quiz, test, compiti
- Mappa del prof: 1 pagina (`_mappe.pdf`); nel video: 6 passaggi (arg. 1–5 + finale) con le voci R1–R6.
- Quiz: 5 domande × 5 argomenti riviste, risposte corrette controllate sul testo del prof (nessuna modifica necessaria).
- Test: copia dell'Excel del prof (10 domande, 4 risposte), `Test_Letteratura_Lez12.xlsx`.
- Compiti: 4 esercizi dal PDF «LEZIONE 12.pdf», testo identico.

## Tempi vecchio → nuovo (secondi)
| Elemento | Vecchio | Nuovo |
|---|---|---|
| Argomento 1 · inizio | 143.233 | 142.433 |
| Argomento 1 · quiz | 613.133 | 613.467 |
| Argomento 2 · inizio | 618.433 | 617.467 |
| Argomento 2 · quiz | 1118.266 | 1107.567 |
| Argomento 3 · inizio | 1123.566 | 1111.567 |
| Argomento 3 · quiz | 1654.867 | 1688.333 |
| Argomento 4 · inizio | 1660.167 | 1692.333 |
| Argomento 4 · quiz | 2395.399 | 2361.467 |
| Argomento 5 · inizio | 2400.699 | 2365.467 |
| Argomento 5 · quiz | 3175.099 | 3121.1 |
| Durata totale | 3403.47 | 3328.17 |

## Non verificato / limiti (onesti)
- **Sottotitoli del prof:** sono la trascrizione automatica con correzioni dei nomi e dei termini noti. Non ho potuto riascoltare ogni frase: possono restare parole sbagliate nelle parti dette in fretta (nomi e frasi poco chiare sono state lasciate come riconosciute solo se sensate).
- **Voce del prof:** pulita con arnndn (modello rnnoise «somnolent-hogwash» da GitHub; il kit non contiene un modello arnndn) + loudnorm −16: l'assenza di «metallico» non è stata ascoltata ma misurata solo come livello.
- **Riquadro:** qualità limitata dalla sorgente (247×138 px); testa tagliata in alto già nell'originale in diversi minuti.
- **Pronuncia dei nomi nelle voci nuove R1–R6 (aggiornamento 08:45):** non ho potuto ascoltarle; ho fatto riconoscere le voci con la trascrizione automatica e tutti i nomi (Nietzsche, Bergson, Freud, Einstein, Proust, Kafka, Gregor, Woolf, Judith, Shakespeare) sono stati riconosciuti correttamente, quindi la pronuncia è con ogni probabilità giusta. Se Sara sente un nome storpiato: scrivere il nome come si pronuncia in `testi_voci.json` (nuova voce R7…) e rigenerare.
- **Pagine del libro:** la lezione 12 non ne ha (salto B-bis).
- **Titolo argomento 2:** la voce di benvenuto dice «il nuovo romanzo del Novecento», sullo schermo c'è «Il romanzo del primo Novecento» (stesso argomento).
