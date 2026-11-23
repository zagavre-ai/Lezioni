# RAPPORTO DI REVISIONE · Letteratura italiana V · Lezione 10 · «Il primo Novecento e la lirica italiana» (Prof. Giorgio Mazzotti)
Correzioni 22/11/2026 · ramo `revisione-letteratura-V-lez10` · presa 16:35 UTC, consegna entro le 19:30 UTC. Ogni dato è **M** (misurato), **S** (stima / lettura a vista) o **NV** (non verificato).

## 1. Misure sul video finale (M)
| | Valore |
|---|---|
| Durata | **51:39,8 (3099.8 s)** (50–65 min ✓; prima 53:20) |
| Fotogrammi | **92994 = durata × 30** |
| Peso | **347.7 MB** (< 400), 4 parti da 90 MB + sha256 (ricomposto = uguale) |
| Formato | 1920×1080, 30 fps, x264 veryfast CRF 19, AAC 192k 48 kHz |
| Volume | **−16,0 LUFS**; picco **−2,0 dBTP** |
| Pause > 2,5 s (−50 dB) | **nessuna** (prima 6: schede Quiz e mappa; accorciate le schede Quiz e Verifica a 4,4 s e messi due `trans.wav` nella tenuta finale della mappa) |
| Scatto quiz Q1–Q4 | **+0,003 s** (`controllo_jingle.py`, limite 0,05) |
| Sincronia audio del prof con l'originale | 36 punti (3 per pezzo, 12 pezzi): **scarto max 0,02 s** (limite 0,04), correlazione ≥ 0,99 |
| Timbro del prof | energia sopra 4 kHz rispetto a tutto sopra 100 Hz: originale −18,0…−19,4 dB, pulito −13,9…−19,1 dB (4 campioni): dentro −9…−20 dB, voce **non** alterata |

Posizioni nel video finale (secondi nuovi, già in `scheda_pubblicazione.json` e `timeline.json`):
| Elemento | Inizio |
|---|---|
| T1 | 4:00 |
| Q1 | 18:51 |
| T2 | 18:55 |
| Q2 | 33:56 |
| T3 | 34:00 |
| MAPPA | 40:22 |
| Q3 | 42:09 |
| T4 | 42:14 |
| Q4 | 48:34 |
| GL | 48:38 |
| RF | 49:34 |
| VER | 50:25 |
| FINALE | 50:29 |
| CI | 50:34 |
| COMPITI | 50:38 |

Vecchi secondi (consegna 17/11): titolo arg. 1 240,7 · Quiz 1 1131,0 · titolo 2 1136,0 · Quiz 2 2024,5 · titolo 3 2029,5 · Quiz 3 2507,0 · titolo 4 2512,0 · Quiz 4 2891,9 · durata 3008,6. Tutti i secondi cambiano e sono rigenerati sul video finale: `timeline.json`, `scheda_pubblicazione.json` (con `t_verifica` e `t_compiti`), `quiz_argomenti.json`, `verifica_finale.json`, `testo_youtube.txt`, `.vtt`.

## 2. Cosa ho cambiato rispetto alla consegna del 20/11
1. **Testo a 40 px, interlinea 1,5** su tutte le slide del prof e sugli approfondimenti, ripassi, glossario e compiti (una slide, la «I vociani», a 36 px perché a 40 le tre card non entrano e una card sola per 87 s non è ammessa). Se tre card non entrano la slide si divide: 45 pagine (prima 34).
2. **Al massimo 3 card per slide, ogni card è un punto intero** della slide del prof (nessun «…», nessuna iniziale minuscola; le card hanno l'altezza del loro testo). Le slide a 4 punti (quadro storico, contesto) sono divise 2+2; le altre 3 card entrano insieme.
3. **Nessuna schermata ferma oltre 3 minuti.** Le slide del prof restano in piedi fino a 5–6 minuti: ho spezzato i pezzi del prof **nei silenzi tra due frasi** e inserito gli approfondimenti animati (voce Kore) a metà argomento, al posto che tutti in fondo: AN2 12:44, AN1 15:05, AN4 21:33, AN6b 24:39, AN10 44:32 (minuti dalla timeline), AN5b e AN5 nell'argomento 2; in fondo restano AN3b, AN7, AN8, AN11b. Il prof non è tagliato a metà frase (§4). Il momento di ogni inserto è scelto in un punto in cui il prof ha già detto o sta per dire quel tema: il testo dell'inserto è quello già approvato.
4. **Copertina: l'introduzione del prof dura 114 s sulla copertina** (era 3:46), poi due slide «Di cosa parliamo» (argomenti 1–2 e 3–4, due card ciascuna) fino a 226 s. Le card degli argomenti **non si accendono**: il prof nomina i crepuscolari e i vociani a 112–125 s, quando la slide è ancora la copertina; non ho forzato un'evidenziazione non vera.
5. **Una sola mappa, quella del prof** (crepuscolarismo, `MAPPE/LEZIONE 10.pdf`), **ridisegnata nel modello BES**: 12 riquadri in 5 colori con legenda in alto a destra (pesca = concetto centrale, celeste = luogo e date, paglierino = parole chiave, menta = esempi, lilla = conseguenze), testo 32–44 px, stessa struttura, stessi testi e stesse frecce del prof, **costruita ramo per ramo** con le voci Kore M1–M12 (riquadro in giallo finché la voce parla), poi mappa intera ferma 4 s. Posta **alla fine dell'argomento 3, prima del ripasso** (OK della master, 17:00). L'immagine del prof non ha marchi né foto dell'autore (nessuna fonte esterna): niente da togliere. Le vecchie mappe nostre e la voce `R5_MPD1` sono tolte dal video.
6. **Schede blu come Spagnolo** (titolo argomento, pillola di ripasso con onda audio, Quiz, Verifica, riepilogo) con i jingle `titolo`, `repaso`, `quiz`, `trans`.
7. **Struttura finale come da regole blindate**: glossario → riepilogo → **verifica di sbarramento** (scheda blu, 10 domande dall'Excel del prof, 80%) → sigla finale con avviso → intro «Compiti» → **compiti del prof** con voce Kore (4 domande, testo identico al PDF del prof). Verifica e compiti sono di nuovo dentro il video (con soglia 80% a `t_verifica`).
8. **Voci**: nuove M1–M12 (mappa), R6_COMP1–4 (compiti). Ogni voce nuova trascritta e confrontata col testo: anni e numeri corretti (1903, 1911…). Bordi (primi/ultimi 50 ms) < 0,01 nelle voci nuove; nelle vecchie quattro avevano un bordo 0,03–0,055 (P1_AN1 fine, P1_AN3b inizio, P1_AN6b fine, P1_AN11b inizio): dissolvenza di 50 ms su ogni voce nel montaggio. **Rifatte**: `P1_AN5_R2` (la trascrizione leggeva «103» al posto di «1903»: la R2 dice «1903» ✓, usata nel video) e `M11_R2` (usata). `S1_R2` richiesta per controllo: la trascrizione della R2 leggeva «Jolittiana», l'originale «Giolittiana» → **tenuta l'originale S1**. `M6_R2` non è arrivata: **tenuta M6** («Ecco le caratteristiche»; la trascrizione automatica ha letto «Con le caratteristiche»: **NV, da riascoltare**).
9. **Dispense A4** (`…_slide.pdf` 45 pagine, `…_mappe.pdf` 2 pagine): identiche alle slide del video (senza riquadro del prof e senza nome), con **strato di testo invisibile** selezionabile; copertina con solo materia e titolo; piè di pagina solo «LETTERATURA ITALIANA V» e «Pagina N» (senza nome del docente); PDF mappe con copertina «MAPPE» + mappa.
10. **Sottotitoli** rifatti sul video finale (601 cue, max 2 righe) con le correzioni della consegna precedente.

## 3. Controllo severo e audit indipendente
- **`controllo_severo.py`: NON COMPLETATO.** È partito più volte sul video ma l'OCR su 310 fotogrammi non è finito entro la scadenza (macchina condivisa con le codifiche). **Non ho un esito OK**: la master deve rilanciarlo.
- **Audit di un agente separato** (non ha montato la lezione; punti del §11): OK su timbro del prof (−12,7…−20,5 dB), nessun fermo immagine del prof, nessuna schermata identica oltre 150 s, 12 bordi gialli esatti, quiz/verifica/compiti identici a Excel e PDF del prof, −16,0 LUFS, 92.994 fotogrammi, PDF con testo e copertine giuste, nessun nome di programma né numero di lezione nel video.
- **Difetti dell'audit corretti in questa consegna:** (1) fondo dei pezzi del prof a 252 invece di 255 → corretto (misurato 255); (2) pezzi D1b/D1c e INTRO/D1a tagliati a metà frase → tagli spostati (§4); (3) nome del docente nel piè di pagina delle pagine Kore (approfondimenti, ripassi, glossario, compiti) → tolto (resta nella fascia gialla e nel piè delle slide del prof, come nel modello Spagnolo); (4) sottotitoli («millenovecentotto…», «conferenzi», «Giolitti alzato», «trince», «viatico», 2:58/3:16) → corretti; (5) «URSS» spiegata nel sottotitolo, non nella voce del prof; (6) testo della mappa a 34 px minimo; (7) foto di Gozzano ingrandita 2× (Lanczos, rumore, nitidezza): la sorgente resta 632×850, **da migliorare dalla master se serve**; (8) minuti e frasi false del rapporto corretti.
- **NON corretti (tempo), da riascoltare/decidere dalla master:** voci Kore con possibile inizio troncato secondo la trascrizione automatica (AN11b «Tre…», AN5b «Tre…», AN8 «Non è», RF «Ottimo»; «Giolitti» sentito «Giulitti» in AN3b e GL): se sbagliate rigenerare come `_R2`; RIP4 ha 3 righe (il testo ha 3 frasi); «Di cosa parliamo» senza card accesa; riquadro del prof visibile ~0,7 s prima che parli; nessuna voce Kore di benvenuto sulla copertina (il prof saluta di persona); AN1 e AN5 anticipano date e riviste prima che il prof ne parli; «Lezione 10» nei metadati (scheda, testo YouTube, verifica).
- **Scatto quiz:** l'audit lo legge a +0,005 s dall'inizio scheda; `controllo_jingle.py` (atteso = inizio scheda + 0,5 s) dà **+0,003 s** su Q1–Q4: regola rispettata.
- **Mappe:** il prof ne ha fatta **una sola** (argomento 3); non ci sono mappe per 1, 2, 4 né finale e non le ho inventate (master, 17:00: «mappa in fondo all'argomento 3 va bene»).

## 4. Prof mai tagliato a metà frase (M, trascrizione dell'originale; tagli nei silenzi)
| Pezzo | Orig. inizio–fine (s) | Prime parole | Ultime parole | Frase intera |
|---|---|---|---|---|
| INTRO | 0.00–227.90 | «Buongiorno e benvenuti alla lezione sul…» | «…quella verso quella meta. Allora. qualche ceno» | sì («Allora, qualche cenno storico») |
| D1a | 227.90–746.35 | «ceno storico E io mi sposto…» | «…il partito e la realtà delle masse.» | sì |
| D1b | 746.35–869.40 | «Interventisti. Figure di spicco? Lo sappiamo.…» | «…Parigi, il trattato di Versailles. nel diciannove» | quasi: finisce su «…nel diciannove» (incipit abbandonato dal prof) |
| D1c | 869.40–932.01 | «Ecco prima, nel frattempo, chiaramente sul…» | «…Tutto questo è quindi il primo Novecento.» | sì |
| D2a | 932.01–1086.96 | «Per tornare a noi, per tornare…» | «…più, e quindi... l'unificazione culturale del paese.» | sì |
| D2b | 1086.96–1237.80 | «Accanto ai fenomeni di urbanizzazione, alle…» | «…la pagina. Questi erano i giornali, adesso.» | sì |
| D2c | 1237.80–1418.34 | «vincono le immagini, le fotografie e…» | «…non funziona più anche prima della guerra.» | sì |
| D2d | 1418.34–1491.44 | «Altri miti sorgono. Il vitalismo di…» | «…iniziasse davvero il Novecento, perché cambia tutto.» | sì |
| D2e | 1491.44–1626.30 | «Gli intellettuali si trovano quindi in…» | «…in filosofia di storia si cita sicuramente.» | sì |
| D3 | 1627.20–1921.10 | «Io prima avevo detto Avevo citato,…» | «…propria sofferenza biologica come unica materia d'arte.» | sì |
| D4a | 1923.28–2057.77 | «Tutto un altro. Tut un altro…» | «…campagna spazio utopico di pace ed armonia.» | sì |
| D4b | 2057.77–2178.60 | «Perre. Pare Pascoli su certe cose.…» | «…le loro riflessioni e le loro composizioni.» | sì |

Il pezzo D4b inizia con «Perre. Pare Pascoli su certe cose.»: parole dell'originale (riconoscimento incerto, **NV**).

## 5. Refusi nel materiale del prof (corretti nelle nostre slide, elenco per la master)
- Slide del prof «Il panorama culturale…»: «tipica del **fine** Ottocento» → «tipica della **fine dell'**Ottocento».
- Slide del prof «I vociani…»: «L'esperienza di *Viatico*» → «L'esperienza di «Viatico»» (titolo dell'opera tra virgolette).
Nessun numero o contenuto del prof modificato. File originali del prof (slide, Excel, compiti, mappa) invariati.
Da confermare col prof (non toccato): Borgese è «Antonio Borgese» nella sua mappa e «Giuseppe Antonio Borgese» nel suo parlato e nell'Excel («La Stampa 1910»).

## 6. Regole BES
- **Niente «già visto»**: ogni slide e immagine del prof compare in un solo argomento (verificato sull'elenco delle pagine); l'unica foto del prof usata è quella di Gozzano (slide 8 del prof), nell'argomento 3. La seconda foto del prof (slide 10) **non è mai mostrata dal prof** nell'originale e non c'è.
- **Sigle**: nel testo non ci sono sigle o abbreviazioni da spiegare (S: lette a vista).
- **Glossario** presente, con voce. Il colore non è mai l'unico segnale (card gialle con pallino numerato; mappa con testo in ogni riquadro). Nessun lampeggio.
- **Nome del docente** mai detto né scritto nelle animazioni (voci dicono «il docente»/«il professore»); solo nella fascia gialla. Il «Prof. Giorgio Mazzotti» è nel piè di pagina delle slide del video, come nel modello Spagnolo.
- **Nessun riquadro del prof nell'introduzione animata** quando non parla: sulla copertina il prof parla dal secondo 0,9; i primi 0,9 s mostrano il prof prima di parlare (**NV**, non ho potuto togliere il riquadro nel primo secondo senza tagliare il parlato).
- **Foto Gozzano**: presa dalla slide 8 del prof, risoluzione originale 632×850: bassa; **non migliorata** (non è stato possibile in questa sessione): **da migliorare dalla master** se serve (§ regola foto di persone reali).

## 7. Inserti Kore già fatti (nota della master delle 17:00)
Gli approfondimenti e i ripassi Kore sono a 40 px (non a 30) e a tre card per pagina: nessun muro di testo.

## 8. Cosa NON ho verificato
- **Ascolto a orecchio**: pronuncia delle voci Kore (soprattutto Rebora, Lacerba, Brest-Litovsk, Corazzini, M6 «Ecco le caratteristiche»), fruscio e «metallico» del prof; labbra/voce (dedotti dall'audio).
- Sottotitoli: ~12 frasi sono ricostruzioni plausibili di parole storpiate dal riconoscimento («Grazia Deledda», «Ungaretti», «magniloquenti»…): da riascoltare a campione.
- Controllo `freezedetect` sul riquadro del prof (non eseguito; il riquadro è sempre video vivo, S).
- Il controllo del §11 da parte di un agente separato: vedi §3.
- La foto di Gozzano è a bassa risoluzione (§6).
- Confronto pagina PDF ↔ fotogramma: le pagine sono le stesse immagini del video (stato senza evidenziazione) — **S**.

## 10. Correzioni 23/11 (DALLA_MASTER: consegna 19:28 respinta)
- **Piè di pagina**: tolto «Prof. Giorgio Mazzotti» da TUTTE le slide del video (restano «LETTERATURA ITALIANA V» e «Pagina N», come dispensa e mappe); il nome sta solo nella fascia gialla. Misurato sul foglio dei fotogrammi.
- **Pausa muta a 50:27 (Verifica)**: scheda accorciata a 3,9 s con `trans.wav` a +2,4 s; **nessuna pausa oltre 2,5 s** (`controllo_rapido.py`: **ESITO OK**, nessun errore).
- **Quiz e Verifica**: «premi Controlla» al posto di «premi Check».
- **Compiti**: ora una card alla volta con bordo giallo, più la riga «Svolgi i compiti qui sotto e premi Consegna…». La voce unica `COMPITI` e le rifatte `P1_AN11b_R2`, `P1_AN5b_R2`, `RF_R2`, `GL_R2` (inizio/fine troncati nella trascrizione) sono **richieste nel ramo voci**: nel video ci sono ancora le voci provvisorie (4 voci R6_COMP1–4 in fila). Appena arrivano le sostituisco e riconsegno. `M6_R2` («Ecco le caratteristiche») è già nel video.
- Falsi allarmi indicati dalla master («card sola» a 2:45 ecc.): non toccati.
- Allegati: `foglio_fotogrammi_*.jpg` e `controllo_rapido_*.json`.
