# RAPPORTO REVISIONE · Letteratura italiana V · Lezione 18 · Eugenio Montale
Revisione del 17/11/2026. Video corretto: `Letteratura_Lez18_Parte1_1080p.mp4` (a pezzi `.parte_NN`, sha256 nel file `.sha256`).
Etichette: **misurato** = misurato con uno strumento; **stima** = dedotto; **non verificato** = non potuto verificare.

## 1. Misure sul video nuovo
| Controllo | Risultato |
|---|---|
| Formato | 1920×1080, 30 fps, x264 veryfast (CRF 19; tratti col prof CRF 22), AAC 192k 48 kHz (**misurato**) |
| Durata / fotogrammi | 53:39,5 · **96 585** fotogrammi = durata × 30 = **identici al video vecchio** (**misurato**) |
| Peso | 163,4 MB, 2 parti da ≤ 90 MB, sha256 verificato sulla ricomposizione (**misurato**) |
| Volume | −16,4 LUFS integrato, LRA 6,5 LU; picco campioni −2,2 dBFS (**misurato**). Il true peak non l'ho letto separatamente (**non verificato**; con il picco a −2,2 dBFS è molto probabilmente ≤ −1 dBTP). Prima della correzione era −15,0 LUFS e −0,9 dBFS: abbassato di 1,4 dB |
| Jingle dei quiz (`controllo_jingle.py`) | Q1…Q6: scarto **0,000 s** (OK, **misurato**); prima della correzione −0,16…−0,21 s (spostato) |
| Sincronia labbra/voce | audio del video contro originale, 5 punti per pezzo del prof, D0…D6: scarto **−0,015 s** in tutti (≤ 0,04, **misurato**; video e audio vengono dallo stesso file originale) |
| Fermi immagine del prof | misura `freezedetect` sul riquadro: vedi sotto (**in corso al momento della consegna del rapporto: non verificato**); il riquadro è sempre video vivo (mai fermo immagine, copertina compresa) per costruzione |
| PDF | slide: **74 pagine** A4 orizzontale (una per slide del video; numerazione = «Pagina N» del video); mappe: 1 pagina |
| Confronto PDF/video | pagine = slide del video senza riquadro e fascia (stessi file HTML): confronto fatto su 12 pagine a vista; non su tutte (**non verificato**) |

## 2. Confronto col modello Spagnolo (punto 000)
| # | Punto | Esito |
|---|---|---|
| 1 | Sigla 15 s → dissolvenza morbida → copertina | **OK**: sigla del kit, dissolvenza di 1 s sulla copertina (misurato a vista su 3 fotogrammi) |
| 2 | Copertina (logo, «LETTERATURA ITALIANA V · VIDEOLEZIONE», titolo, card ARGOMENTI su 2 colonne) | **corretto** (era sfondo blu scuro) |
| 3 | Slide: fondo bianco, «01 · ARGOMENTO», titolo + barretta, card | **corretto** (era pannello laterale blu e «ARGOMENTO 1 · LA VITA») |
| 4 | Piè di pagina «LETTERATURA ITALIANA V · Prof. Giorgio Mazzotti» + «Pagina N» | **corretto**; 74 pagine, numerazione uguale al PDF slide |
| 5 | Riquadro 4:3 (412×310 a x=1428, y=148, r=18), ombra grigia morbida, niente bordo | **corretto** |
| 6 | Fascia gialla −3°, due righe, sempre visibile col prof | **corretto**; assente quando il prof non parla (copertina con la voce, schede) |
| 7 | Slide senza prof | **corretto**: approfondimenti, mappe, ripassi, glossario, riepilogo, quiz, verifica, compiti, finale |
| 8 | Font Bricolage 800 / Figtree (etichette e piè in Figtree Bold) | **OK** (controllo a vista; nessun DM Mono) |
| 9 | Finale 5 s con avviso diritti | **OK** (`Sigla_finale_5s_con_avviso_diritti.mp4`, a 53:21,5) |
| 10 | Struttura | **OK**: sigla, presentazione, 6 argomenti (titolo, prof, approfondimenti, mappa, ripasso, quiz), mappa finale, glossario, riepilogo, fine, verifica, compiti |
| 11 | PDF slide + mappe | consegnati: slide **74 pagine** A4 orizzontale; mappe **1 pagina** |
Aggiornamenti 17/11 (01:20–08:15): card in corso con bordo giallo sottile e pallino giallo numerato, ombre grigie morbide; jingle (`quiz.wav` ai quiz, `titolo.wav` ai titoli, `repaso.wav` ai ripassi, `trans.wav` ai passaggi); dissolvenze brevi tra i pezzi; riquadro del prof solo con video vivo.

## 3. Problemi trovati e correzioni (minuti sul video VECCHIO → NUOVO)
| Minuto | Tipo | Com'era | Correzione |
|---|---|---|---|
| 28:27–31:44, 34:30–41:24 | **sincronia (grave)** | I pezzi del prof erano sfasati rispetto agli argomenti: la spiegazione di *Spesso il male di vivere* (orig. 16:52–20:09, argomento 3) stava dopo il quiz 3 e sotto la slide «Le occasioni»; *Le occasioni* e *La bufera* stavano sotto «La bufera e altro e Satura» | piano rifatto sulle pause del prof: arg. 3 = orig. 8:07–20:10, arg. 4 = 20:10–22:41, arg. 5 = 22:41–25:12, arg. 6 = 25:12–29:25. **I quiz 3, 4, 5 cambiano secondo (tabella §6).** Durata totale invariata (3219,5 s, 96 585 fotogrammi) |
| tutto | **pagina** | nessuna pagina del libro nel video, ma il prof legge 4 testi | 17 fettine dagli screen HD (§4) |
| 6:24, 16:21, 21:00, 33:06, 41:01, 48:59, 50:22 | **visivo** | 7 «mappe» inventate da noi (non del prof) | mappa del prof (1 sola) nella nostra grafica, stesso testo (tolti logo mappe-scuola.com e 2 foto); 7 inserti con voce nuova `R1…R6, RF`, che leggono la mappa del prof + ricordano le slide |
| 38:49–38:51 / 42:35 | audio | frase ripetuta «…con tanto di testo/testi» (sovrapposizione di 1,8 s) | taglio su una pausa |
| 12:02 / 15:22 | audio | pezzo finito a metà parola «vog|liamo» | tagli solo su pause ≥ 0,2 s (misurate) |
| orig. 1:12 | audio | pezzo del prof finito a metà frase («Direi che» | «Questa è appunto una sua fotografia…») | taglio spostato prima di «Direi che»: ora la frase è intera (D1 inizia a 1:12) |
| tutto | visivo | grafica fuori dal modello (fondo scuro, riquadro con bordo blu, niente fascia gialla) | tutto rifatto (punto 000) |
| tutto | sincronia | evidenziazioni scelte a occhio | rifatte dalle parole del prof e dalla voce (trascrizione) |
| copertina | visivo | riquadro del prof fermo durante la voce di benvenuto | copertina senza riquadro durante la voce; riquadro in dissolvenza quando il prof parla |
| audio | audio | parlato del prof non pulito col kit | rifatto dall'originale: `aresample 48000, highpass 80, arnndn (sh.rnnn), loudnorm −16, alimiter` |
| ripassi | audio | senza jingle | `repaso.wav` a ogni ripasso; `trans.wav` ai passaggi |
| vtt | testo | ~50 errori («solo è disclusivamente», «alletterrature», «poesino», «delignato», poesie lette male…) | riscritto dalla trascrizione, nomi e poesie dal libro |
| Q4 domanda 2 | testo | «clima del dopoguerra e degli anni Trenta» (errore anche nella slide del prof) | «Gli anni Trenta, con la minaccia del fascismo e dei totalitarismi» (dalla voce del prof) |
| scheda | testo | titolo «Eugenio Montale · Parte 1» | «Letteratura V · Lezione 18 · Eugenio Montale» |
| consegna | file | mancavano `verifica_finale`, `…_slide.pdf`; il «Test» era il modello vuoto; PDF mappe con 7 mappe inventate | prodotti |

## 4. Pagine del libro in alta risoluzione (B-bis)
Zip `Lez18_ingrandita.zip`: p. 756, 757, 758, 762, 763, 765, 789. Solo la colonna del brano, tagli su righe bianche, senza intestazioni/numeri di pagina/QR; fettina in corso con bordo giallo. Foglio `controllo_fettine.jpg` (un fotogramma per fettina, guardato).
| Brano | Pagina | File HD | Minuto (nuovo) |
|---|---|---|---|
| I limoni | 756 | Lez18_p756.png · strofa 1 | 15:50 |
| I limoni | 756 | Lez18_p756.png · strofa 2 | 16:15 |
| I limoni | 757 | Lez18_p757.png · strofa 3 | 16:32 |
| I limoni | 757 | Lez18_p757.png · strofa 4 | 16:53 |
| I limoni | 757 | Lez18_p757.png · strofa 5 | 17:16 |
| I limoni | 757 | Lez18_p757.png · strofa 6 | 17:35 |
| I limoni | 758 | Lez18_p758.png · strofa 7 | 17:59 |
| Meriggiare pallido e assorto | 762 | Lez18_p762.png · strofa 1 | 20:19 |
| Meriggiare… | 762 | Lez18_p762.png · strofa 2 | 20:35 |
| Meriggiare… | 763 | Lez18_p763.png · strofa 3 | 20:48 |
| Meriggiare… | 763 | Lez18_p763.png · strofa 4 | 21:03 |
| Spesso il male di vivere | 765 | Lez18_p765.png · quartina 1 | 24:20 |
| Spesso il male di vivere | 765 | Lez18_p765.png · quartina 2 | 24:37 |
| Ho sceso, dandoti il braccio | 789 | Lez18_p789.png · strofa 1 | 44:08 |
| Ho sceso… | 789 | Lez18_p789.png · strofa 2 | 44:28 |

Non inserite (decisione): il paragrafo «METRO» di p. 762 (rigo troppo piccolo, < 26 px) e i commenti di analisi del manuale (p. 758, 763, 765, 789): il prof li riprende a voce, il video mostra le sue slide.

## 5. Fine e inizio di ogni pezzo del prof (aggiornamento 01:25)
| Pezzo | Minuto nuovo | Prime parole dette | Ultime parole dette | Frase finita? |
|---|---|---|---|---|
| D0 | 0:45.0 (orig. 0:00.1–1:13.7) | «Buongiorno e benvenuti alla lezione su» | «In ogni caso. Eugenio Montale, beh... Direi che» | sì («…Eugenio Montale, beh… Direi che» è ora in D1: il pezzo finisce prima, su una pausa di 0,4 s, a «In ogni caso.») |
| D1 | 2:03.5 (orig. 1:13.7–4:07.3) | «Questa è appunto una sua fotografia.» | «e muore nel 1981, attraverso veramente. in novecento.» | sì |
| D2 | 8:03.2 (orig. 4:07.3–8:06.9) | «Vediamo la prima raccolta, la più» | «ciò che non siamo, ciò che non vogliamo.» | sì |
| D3 | 15:24.0 (orig. 8:06.9–20:10.0) | «Bene, e allora come propone giustamente» | «nostra condizione, se no addirittura ci potrebbe attaccare.» | sì |
| D4 | 31:45.2 (orig. 20:10.0–22:40.7) | «Seconda raccolta, le occasioni. Allora. Mm.» | «immobile e privo di un varco di salvezza.» | sì |
| D5 | 37:02.7 (orig. 22:40.7–25:12.7) | «Poi viene ve ne un'altra di» | «i linguaggi alienanti. della moderna società di consumo.» | sì |
| D6 | 43:19.3 (orig. 25:12.7–29:25.7) | «All'interno di quest'opera la sezione Xenia,» | «diciamolo, in sede scolastica. Di solito. sono richieste.» | sì (fine registrazione) |

**Misurato** sull'originale: ogni taglio cade in una pausa di almeno 0,2–1,5 s (audio < soglia) e tra due frasi; nessuna parola mozzata in partenza né in chiusura. D0 termina a «…In ogni caso. Eugenio Montale, beh…» e D1 inizia con «Direi che questa è appunto una sua fotografia, si debba iniziare dalla vita» (frase intera).

## 6. Quiz, verifica e compiti: secondi vecchio → nuovo (misurato)
| Elemento | Vecchio | Nuovo |
|---|---|---|
| Quiz 1 | 7:53.1 (473.1 s) | 7:53.1 (473.1 s) |
| Quiz 2 | 15:12.6 (912.6 s) | 15:12.6 (912.6 s) |
| Quiz 3 | 28:17.5 (1697.5 s) | 31:33.8 (1893.8 s) |
| Quiz 4 | 34:20.2 (2060.2 s) | 36:51.3 (2211.3 s) |
| Quiz 5 | 42:24.8 (2544.8 s) | 43:07.9 (2587.9 s) |
| Quiz 6 | 50:17.8 (3017.8 s) | 50:17.8 (3017.8 s) |
| Verifica finale | 53:14,9 (3194.9 s) | invariato |
| Compiti | 53:33,2 (3213.2 s) | invariato |

Inizio argomenti nuovo: T1 1:56,8 (era 1:59,3), T2 7:58,4, T3 15:17,9, T4 31:39,1 (era 28:22,8), T5 36:56,6 (era 34:25,5), T6 43:13,2 (era 42:30,1). Quiz 1 e 2 sono rimasti agli stessi secondi di prima (la differenza è assorbita dal cartello del titolo).
Aggiornati `scheda_pubblicazione.json`, `timeline.json`, `testo_youtube.txt`. **La pagina Vimeo/quiz va riallineata ai secondi nuovi.**

## 7. Cosa NON ho verificato / limiti
- **Ascolto umano** (fruscio/ronzio/metallico dopo la pulizia): non ascoltato. **Non verificato.**
- **Pronuncia della voce Kore** nelle voci nuove (R1…R6, RF): controllata solo con la trascrizione automatica, che segna «Contarla» (R3, prima versione), «Rusilla» (R6b, per «Drusilla»), «Primerla» (R3b) e «VAR» (R4): sono molto probabilmente errori del riconoscimento, ma **da riascoltare**: R3b a 30:07, R6b a 48:22, R4b a 35:57. Nelle vecchie voci S1/S6 «Viessò» (Vieusseux) da riascoltare.
- **Sottotitoli:** riscritti dalla trascrizione (prof) e dai testi veri (voce Kore), poesie dal libro; tempi proporzionali alle strofe (**stima**, ±1–2 s nelle poesie). Parole non decifrabili lasciate come sono: «anche Insha» (≈ 38:03), «Allora i» (≈ 38:14), «Il poeta si rivendica» (≈ 38:23), passaggio sulle rime di *Meriggiare* (≈ 17:30). **Non riletti cue per cue.**
- **Fermi immagine** del riquadro: vedi §1 (non verificato in questa versione).
- **Testa tagliata:** nell'originale la webcam è 243×139 px e i capelli toccano il bordo alto in molti punti (es. 1:30, 3:20, 14:10 dell'originale): non risolvibile. Webcam ingrandita 2,2× (immagine morbida).
- **Foto di Montale** (1:14 orig.): vedi §8.
- **Didascalia «DAL LIBRO…»** nelle fettine alte (strofa 4 di *I limoni*, 16:53) tocca il bordo basso del riquadro giallo: difetto minore **non corretto**.
- **Jingle `titolo.wav`/`quiz.wav`** già presenti nell'audio del montaggio precedente (misurati); `repaso.wav` e `trans.wav` aggiunti ai ripassi e ai passaggi: livello scelto a orecchio dalla misura, non ascoltato.
- **PDF slide:** testo vero (selezionabile) ma le slide sono 16:9 centrate su A4 (margini bianchi sopra e sotto): non identico al modello Spagnolo che usa tutta la pagina.

## 8. DA CONFERMARE COL PROF
- Slide 9 (*Le occasioni*): «nel clima storico del **dopoguerra** e degli anni trenta» (la raccolta è del 1939): lasciato com'è nella slide; nel quiz uso «anni Trenta».
- La mappa del prof non ha rami per *I testi degli Ossi* e per *La figura della moglie*: negli inserti MP3 e MP6 evidenzio i nodi *Ossi di seppia* e *Satura* e ricordo le slide.
- A 1:14 (orig.) il prof dice «Questa è appunto una sua fotografia»: nella sua slide c'è un ritratto di Montale; **non l'ho messo** (regola: mai foto di personaggi pubblici scaricate). Decide Sara.
- Il prof dice «Meriggiare pallido e assorto: tre quartine e una strofa di cinque versi»; il libro (p. 762) conferma.

## 9. Come ho verificato
Trascrizione completa di originale e video vecchio (Parakeet via `trascrivi.py`), 3 220 fotogrammi a 1/s sul video vecchio, allineamento audio con `allinea.py`, misure sul video nuovo con ffmpeg (ebur128, freezedetect, ffprobe), `controllo_finale.py`, `controllo_jingle.py`, correlazione audio/originale per la sincronia, `controllo_minuti.jpg` (1 fotogramma ogni 30 s) e `controllo_fettine.jpg`.
