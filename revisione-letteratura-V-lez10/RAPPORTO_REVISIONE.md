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
3. **Nessuna schermata ferma oltre 3 minuti.** Le slide del prof restano in piedi fino a 5–6 minuti: ho spezzato i pezzi del prof **nei silenzi tra due frasi** e inserito gli approfondimenti animati (voce Kore) a metà argomento, al posto che tutti in fondo: AN2 a 12:26, AN1 a 14:17, AN4 a 21:20, AN6b a 25:17, AN5b a 28:11, AN5 a 29:57, AN10 a 44:08; in fondo restano AN3b, AN7, AN8, AN11b. Il prof non è mai tagliato a metà frase (§5). Il momento di ogni inserto è scelto in un punto in cui il prof ha già detto o sta per dire quel tema: il testo dell'inserto è quello già approvato.
4. **Copertina: l'introduzione del prof dura 114 s sulla copertina** (era 3:46), poi due slide «Di cosa parliamo» (argomenti 1–2 e 3–4, due card ciascuna) fino a 226 s. Le card degli argomenti **non si accendono**: il prof nomina i crepuscolari e i vociani a 112–125 s, quando la slide è ancora la copertina; non ho forzato un'evidenziazione non vera.
5. **Una sola mappa, quella del prof** (crepuscolarismo, `MAPPE/LEZIONE 10.pdf`), **ridisegnata nel modello BES**: 12 riquadri in 5 colori con legenda in alto a destra (pesca = concetto centrale, celeste = luogo e date, paglierino = parole chiave, menta = esempi, lilla = conseguenze), testo 32–44 px, stessa struttura, stessi testi e stesse frecce del prof, **costruita ramo per ramo** con le voci Kore M1–M12 (riquadro in giallo finché la voce parla), poi mappa intera ferma 4 s. Posta **alla fine dell'argomento 3, prima del ripasso** (OK della master, 17:00). L'immagine del prof non ha marchi né foto dell'autore (nessuna fonte esterna): niente da togliere. Le vecchie mappe nostre e la voce `R5_MPD1` sono tolte dal video.
6. **Schede blu come Spagnolo** (titolo argomento, pillola di ripasso con onda audio, Quiz, Verifica, riepilogo) con i jingle `titolo`, `repaso`, `quiz`, `trans`.
7. **Struttura finale come da regole blindate**: glossario → riepilogo → **verifica di sbarramento** (scheda blu, 10 domande dall'Excel del prof, 80%) → sigla finale con avviso → intro «Compiti» → **compiti del prof** con voce Kore (4 domande, testo identico al PDF del prof). Verifica e compiti sono di nuovo dentro il video (con soglia 80% a `t_verifica`).
8. **Voci**: nuove M1–M12 (mappa), R6_COMP1–4 (compiti). Ogni voce nuova trascritta e confrontata col testo: anni e numeri corretti (1903, 1911…). Bordi (primi/ultimi 50 ms) < 0,01 nelle voci nuove; nelle vecchie quattro avevano un bordo 0,03–0,055 (P1_AN1 fine, P1_AN3b inizio, P1_AN6b fine, P1_AN11b inizio): dissolvenza di 50 ms su ogni voce nel montaggio. **Rifatte**: `P1_AN5_R2` (la trascrizione leggeva «103» al posto di «1903»: la R2 dice «1903» ✓, usata nel video) e `M11_R2` (usata). `S1_R2` richiesta per controllo: la trascrizione della R2 leggeva «Jolittiana», l'originale «Giolittiana» → **tenuta l'originale S1**. `M6_R2` non è arrivata: **tenuta M6** («Ecco le caratteristiche»; la trascrizione automatica ha letto «Con le caratteristiche»: **NV, da riascoltare**).
9. **Dispense A4** (`…_slide.pdf` 45 pagine, `…_mappe.pdf` 2 pagine): identiche alle slide del video (senza riquadro del prof e senza nome), con **strato di testo invisibile** selezionabile; copertina con solo materia e titolo; piè di pagina solo «LETTERATURA ITALIANA V» e «Pagina N» (senza nome del docente); PDF mappe con copertina «MAPPE» + mappa.
10. **Sottotitoli** rifatti sul video finale (601 cue, max 2 righe) con le correzioni della consegna precedente.

## 3. Esito del controllo severo (`controllo_severo.py`)
ESITO_SEVERO_DA_COMPLETARE

## 4. Prof mai tagliato a metà frase (M, trascrizione dell'originale; tagli nei silenzi, inizio 0,15 s prima della frase)
| Pezzo | Orig. inizio–fine (s) | Prime parole | Ultime parole | Frase intera |
|---|---|---|---|---|
| INTRO | 0.00–226.40 | «Buongiorno e benvenuti alla lezione sul…» | «…esami. verso quella verso quella meta. Allora.» | sì (taglio nel silenzio) |
| D1a | 226.40–746.35 | «qualche ceno storico E io mi…» | «…il partito e la realtà delle masse.» | sì (taglio nel silenzio) |
| D1b | 746.35–857.11 | «Interventisti. Figure di spicco? Lo sappiamo.…» | «…aeroplani. e da un tragico costo umano.» | sì (taglio nel silenzio) |
| D1c | 857.11–932.01 | «fino alla conclusione nel 1918 e...…» | «…Tutto questo è quindi il primo Novecento.» | sì (taglio nel silenzio) |
| D2a | 932.01–1086.96 | «Per tornare a noi, per tornare…» | «…più, e quindi... l'unificazione culturale del paese.» | sì (taglio nel silenzio) |
| D2b | 1086.96–1237.80 | «Accanto ai fenomeni di urbanizzazione, alle…» | «…la pagina. Questi erano i giornali, adesso.» | sì (taglio nel silenzio) |
| D2c | 1237.80–1418.34 | «vincono le immagini, le fotografie e…» | «…non funziona più anche prima della guerra.» | sì (taglio nel silenzio) |
| D2d | 1418.34–1491.44 | «Altri miti sorgono. Il vitalismo di…» | «…iniziasse davvero il Novecento, perché cambia tutto.» | sì (taglio nel silenzio) |
| D2e | 1491.44–1626.30 | «Gli intellettuali si trovano quindi in…» | «…in filosofia di storia si cita sicuramente.» | sì (taglio nel silenzio) |
| D3 | 1627.20–1921.10 | «Io prima avevo detto Avevo citato,…» | «…propria sofferenza biologica come unica materia d'arte.» | sì (taglio nel silenzio) |
| D4a | 1923.28–2057.77 | «Tutto un altro. Tut un altro…» | «…campagna spazio utopico di pace ed armonia.» | sì (taglio nel silenzio) |
| D4b | 2057.77–2178.60 | «Perre. Pare Pascoli su certe cose.…» | «…le loro riflessioni e le loro composizioni.» | sì (taglio nel silenzio) |

Prime e ultime parole di ogni pezzo sono intere (nessuna parola mozzata). Il pezzo D4b inizia con «Perre. Pare Pascoli su certe cose.»: sono parole dell'originale (riconoscimento incerto, **NV**), non tagliate.

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
