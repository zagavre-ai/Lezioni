# RAPPORTO REVISIONE · Letteratura italiana V · Lezione 25 · Pier Paolo Pasolini
Revisione del 17/11/2026. Video: `Letteratura_Lez25_Parte1_1080p.mp4` (a pezzi `.parte_00/01`, sha256 nel file `.sha256`, verificato sul file ricomposto).
**misurato** = misurato con uno strumento; **stima** = dedotto; **non verificato** = non ho potuto.

## 1. Misure sul video nuovo (misurato)
| Controllo | Risultato |
|---|---|
| Formato | 1920×1080, 30 fps, x264 veryfast CRF 19, AAC 192k |
| Durata / fotogrammi | **38:38,2 (2318,2 s)** · 69 547 fotogrammi = durata × 30. **La durata è cambiata** (prima 45:19): via le 7 mappe nostre (−6:30) e i silenzi, aggiunta la mappa del prof con voce nuova (+1:47). Resta sotto i 50 minuti: il materiale del prof dura 20 min, non si allunga con riempitivi |
| Peso | 146.6 MB |
| Volume | -16.9 LUFS integrato; picco -1.0 dBFS (≤ −1) |
| Silenzi ≥ 3 s | **nessuno** (prima 27, di 3–11 s) |
| Fermi del riquadro del prof ≥ 1 s (`freezedetect`) | **nessuno** |
| Sincronia audio/video del prof | audio del video finale confrontato con l'originale, per ogni pezzo D0–D6: scarto **−0,013 s** (limite 0,04). Audio e immagine del prof vengono dallo stesso file con lo stesso offset |
| Jingle Quiz (`controllo_jingle.py`) | Q1–Q6: scarto **0,000 s** |
| PDF slide | 47 pagine A4 orizzontale; ognuna confrontata con il fotogramma del video (esclusi riquadro e nome): **47 su 47 coincidono** |
| Rumore del prof | fondo −58 dB (prima −54 dB), catena arnndn del kit |

## 2. Confronto col modello Spagnolo (punto 000)
| # | Punto | Esito |
|---|---|---|
| 1 | Sigla → dissolvenza → copertina | OK (dissolvenza di 0,5 s dalla sigla) |
| 2 | Copertina (logo, riga «LETTERATURA ITALIANA V · VIDEOLEZIONE», titolo, card ARGOMENTI su 2 colonne) | **corretto** (prima fondo scuro) |
| 3 | Slide: fondo bianco, «01 · ARGOMENTO», titolo + barretta | **corretto** |
| 4 | Piè «LETTERATURA ITALIANA V · Prof. Giorgio Mazzotti» + «Pagina N» | **corretto** (prima senza «V» e a sinistra) |
| 5 | Riquadro 4:3 | **corretto**: 412×309 px a x=1428 y=148, angoli r=18, ombra grigia morbida, nessun bordo (prima riquadro piccolo con bordo blu e banda blu) |
| 6 | Fascia gialla −3°, due righe | **corretto** (prima testo bianco piccolo, senza fascia) |
| 7 | Slide senza prof | **corretto**: approfondimenti, ripassi, glossario, riepilogo, mappa, schede titolo/Quiz/Verifica/Compiti/Fine su fondo bianco (prima blu notte, e carattere con le grazie su titoli e «FINE») |
| 8 | Font | Bricolage Grotesque 800 e Figtree (etichette in Figtree Bold, aggiornamento 15:10) |
| 9 | Finale | sigla finale 5 s del kit conservata |
| 10 | Struttura | OK: sigla, presentazione, 6 argomenti (titolo, prof, approfondimenti, ripasso, quiz), mappa del prof, glossario, riepilogo, fine |
| 11 | PDF slide + mappe | consegnati |

Card «in corso»: bordo giallo, pallino giallo, fondo bianco; le altre con bordo grigio chiaro; ombre sempre grigie e morbide (aggiornamento 01:30).

## 3. Problemi trovati e correzioni
| Minuto (nuovo) | Tipo | Com'era | Correzione |
|---|---|---|---|
| tutto | visivo | grafica diversa dal modello (vedi §2) | tutte le slide rifatte; riquadro 4:3 dall'originale con correzione immagine del kit |
| copertina | visivo | riquadro del prof presente anche dove parla solo la voce | riquadro solo dove il prof parla (video vivo, nessun fermo); in presentazione con voce Kore niente riquadro |
| 34:31 | contenuto | 7 mappe fatte da noi (non del prof), con voce | tolte; una sola mappa, **quella del prof** (`MAPPE/LEZIONE 25.pdf`), nella nostra grafica, voce nuova **R2** (Kore) con evidenziazione del ramo; senza le foto di Pasolini e senza il logo del sito della mappa |
| raccordi del prof | prof | pezzi tagliati a metà frase e frasi ripetute (v. §4) | tagli rifatti a fine frase, su pause misurate; nessuna ripetizione |
| 16:13 | voce | la voce Kore di AN06 era **troncata**: si fermava a «…morale del Paese» e mancavano 4 frasi (denunce, 2 novembre 1975) mentre le card erano a schermo | nuova narrazione **R1** completa (25,6 s), card a tempo con la voce |
| silenzi | audio | 27 silenzi di 3–11 s (schede titolo, Quiz, Verifica, Compiti, code dei pezzi) | tolti |
| jingle / transizioni | audio | ripasso, Verifica, Compiti, Fine senza jingle; passaggi a taglio secco | `repaso.wav` sui ripassi, `quiz.wav` su Verifica e Compiti, `finale.wav` su Fine, `trans.wav` + dissolvenza 0,2 s sui passaggi; Quiz e titoli come prima |
| audio prof | audio | non pulito con la catena del kit | rifatto dall'originale: `aresample 48000, highpass 80, arnndn (sh.rnnn)`, guadagno per pezzo a −16,5 LUFS, limitatore −1,5 dB. Nota: `loudnorm` dinamico **cancellava il parlato per 5–9 s** in 3 punti; sostituito da guadagno fisso (verificato: nessun secondo di parlato perso) |
| scheda titolo 4 | testo | «Poesia e conflitti interiori» ≠ elenco «Le prime fasi poetiche e i conflitti interiori» | uniformato all'elenco della dispensa |
| quiz | testo | «Quale è il primo film» | «Qual è» |
| verifica | pagina | mancava la verifica finale | `verifica_finale.json` + xlsx del prof (10 domande) |
| compiti | pagina | ok | 4 domande del prof, testo identico al PDF |
| scheda | testo | titolo «Pier Paolo Pasolini · Parte 1» | «Letteratura V · Lezione 25 · Pier Paolo Pasolini»; secondi aggiornati |
| vtt | testo | trascrizione automatica con errori («con giorno bevenute», «più di ottubra»…) | rifatto: voce Kore dai testi esatti, prof dalla nuova trascrizione con i nomi corretti (Pasolini, Officina, Accattone, Canterbury, Scritti corsari…), 599 cue di max 2 righe, tempi sul nuovo montaggio |

## 4. Fine e inizio di ogni pezzo del prof (aggiornamento 01:25)
| Pezzo | Minuto (nuovo) | Prime parole | Ultime parole | Frase finita |
|---|---|---|---|---|
| D0 | 0:51–1:10 | Buongiorno e benvenuti alla lezione su | dissacranti appunto della letteratura italiana. del Novecento. Analizziamo. | sì |
| D1 | 1:13–5:04 | Ecco appunto una sua fotografia. Analizziamo | costruirsi un'altra vita, una nuova vita, se vogliamo. | sì |
| D2 | 6:57–8:56 | Nella capitale l'impatto con i duri | potrebbe potremmo rubricarlo il suo... il suo impegno. | sì |
| D3 | 10:44–15:10 | Andiamo avanti. Intorno al millovecentosanta, periodo | But Come dire. diversa e un po' fastidiosa. | sì |
| D4 | 17:18–21:18 | Allora ripercorriamo, dopo aver visto velocemente | Officina. Quella di vista di cui abbiamo parlato. | sì |
| D5 | 24:24–27:49 | Poi c'è anche la narrativa, certamente. | o scritti corsali del 1975, 5, d'accordo. d'accordo, | sì (taglio dopo «d'accordo.», prima di «possiamo andare») |
| D6 | 30:37–32:42 | possiamo andare pure su questi. Nelle | intellettuali più lucidi, tormentati e provocatori. del novecento. | sì |

Prima i raccordi D1/D2 («…tentò di | costruirsi…»), D2/D3 («…il suo | impegno») e D3/D4 («…un po’ | fastidiosa») erano tagliati a metà frase e D5/D6 ripeteva «d'accordo» (1,95 s). I tagli sono ora su pause misurate (−50…−66 dB).

## 5. Secondi vecchio → nuovo (la durata è cambiata)
| Scheda | vecchio (s) | nuovo (s) |
|---|---|---|
| Q1 | 481.7 | 411.2 |
| Q2 | 779.0 | 638.1 |
| Q3 | 1239.4 | 1032.2 |
| Q4 | 1746.2 | 1457.8 |
| Q5 | 2190.6 | 1830.9 |
| Q6 | 2490.4 | 2067.4 |
| VER | 2693.8 | 2304.4 |
| CI1 | 2707.0 | 2312.2 |

`scheda_pubblicazione.json` (`inizio_s`, `quiz_s`, `durata_s` = 2318,23) e `quiz_argomenti.json` sono aggiornati; la master rigenera la pagina.

## 6. DA CONFERMARE COL PROF
- Mappa: «dopo l'**8 settembre 1943** si rifugia a Casarsa»; slide e lezione dicono «dal **1942** vive a Casarsa». Nel video restano mappa (voce R2) e slide come sono.
- Mappa: «muore assassinato **a Roma**»; slide: «presso **Ostia**».
- Parlato 1:18: «Ecco appunto una **sua fotografia**» ma nelle sue slide non c'è nessuna foto (non è nei materiali; non si scaricano foto): non risolvibile, parla il prof.
- Nomi dubbi nella trascrizione del parlato: «Silone» (tra Verga e Pavese) e «a Marx» (prima «a Marshall»): **da riascoltare**.
- La mappa del prof è una sola (non una per argomento): nel video una sola mappa, a fine lezione.

## 7. Cosa NON ho verificato (non verificato)
- **Pronuncia della voce Kore** (Accattone, Officina, Decameron…): nessun ascolto umano. La trascrizione automatica sulla voce RF1 ha letto «E a Cattone» al minuto 44:27 del vecchio video: **da riascoltare**.
- **Sottotitoli del prof parola per parola**: trascrizione automatica buona ma non perfetta; alcuni tratti poco intelligibili sono stati tolti o corretti a senso. Vanno riletti all'ascolto.
- **Testa nel riquadro**: nell'originale il prof è una webcam di 245×138 px con i capelli a contatto del bordo alto; il ritaglio 4:3 (184×138 px ingrandito 2,2×) è morbido e la testa tocca il bordo. Non risolvibile.
- Sincronia card/parlato: misurata con i tempi parola per parola (stima ±1 s), non con riascolto.
- Pagine del libro: la lezione non ne ha (B-bis non applicabile).

## 8. Come ho verificato
Trascrizione parola per parola (`trascrivi.py`), OCR dei fotogrammi del video vecchio, correlazione audio per allineare il prof all'originale, `freezedetect`, `silencedetect`, `ebur128`, `controllo_jingle.py`, confronto pixel di ogni pagina PDF col fotogramma, contact sheet `controllo_minuti.jpg` (1 fotogramma ogni 30 s).
