# RAPPORTO REVISIONE · Letteratura italiana V · Lezione 17 · Giuseppe Ungaretti e l'Ermetismo
Revisione del 16/11/2026. Video corretto: `Letteratura_Lez17_Parte1_1080p.mp4` (a pezzi `.parte_00…04`, sha256 nel file `.sha256`; la somma dei pezzi corrisponde allo sha256).
Etichette: **misurato** = misurato con uno strumento · **stima** = dedotto · **non verificato** = non ho potuto.
La lezione è stata **rifatta nel modello Spagnolo** (slide dal materiale del prof, riquadro 4:3, fascia gialla, schede di servizio), con **durata e fotogrammi identici** al montaggio precedente: quiz, verifica e compiti restano agli stessi secondi su Vimeo.

## 1. Misure sul video nuovo
| Controllo | Risultato |
|---|---|
| Formato | 1920×1080, 30 fps, x264 veryfast CRF 19, AAC 192 k, 48 kHz (**misurato**) |
| Durata / fotogrammi | 3096,97 s = 51:37 · **92 909 fotogrammi = durata × 30, identici al video vecchio** (45 pezzi, ciascuno con i fotogrammi del piano vecchio; **misurato** pezzo per pezzo) |
| Peso | 385,6 MB (< 400 MB) (**misurato**) |
| Volume | −16,8 LUFS integrato, LRA 6,9 LU (**misurato**) |
| Picco | −2,5 dBFS sul file decodificato (**misurato**). Con la prima codifica un solo punto (4:14, parlato del prof molto forte) superava 0 dBFS dopo l'AAC: ho aggiunto un limitatore e abbassato di 1 dB |
| Audio del prof | rifatto **dall'originale** con la catena del kit (`aresample 48000, highpass 80, arnndn sh.rnnn, loudnorm −16, alimiter`), stessi offset del montaggio precedente (D1…D6 sono l'originale contiguo, nessun taglio interno) |
| Fermi immagine | il riquadro del prof è il video dell'originale (si muove sempre); fermo solo nelle schede statiche e nella copertina del benvenuto (voce narrante, 0:15–0:48), come prima |
| PDF | slide: **69 pagine** A4 orizzontale; mappe: **1 pagina** A4 orizzontale |

## 2. Confronto col modello Spagnolo (punto 000)
| # | Punto | Esito |
|---|---|---|
| 1 | Sigla 15 s → dissolvenza → copertina | OK: sigla del kit (`Sigla_Letteratura_15s`), poi copertina. Il passaggio è a stacco, non c'è dissolvenza (non l'ho rifatta: i frame del pezzo sono rigidi per mantenere i secondi) → **non possibile** |
| 2 | Copertina (logo, «LETTERATURA ITALIANA V · VIDEOLEZIONE», titolo, card ARGOMENTI su 2 colonne) | **corretto** (prima: titolo + elenco senza card) |
| 3 | Slide: fondo bianco, «NN · ARGOMENTO» (numero dell'argomento), titolo + barretta, card | **corretto** (prima: fondo grigio-azzurro, nessun numero dell'argomento corretto) |
| 4 | Piè di pagina «LETTERATURA ITALIANA V · Prof. Giorgio Mazzotti» + «Pagina N» | **corretto** (prima: «Ripasso» al posto del numero in alcune schede) |
| 5 | Riquadro 4:3, ombra grigia, niente bordo | **corretto**: 412×309 px a x=1428, y=148, angoli r=18 (prima: tondo ≈ 290 px). Correzione immagine del kit (contrasto 1,04, saturazione 1,03, hqdn3d 1.5:1.5:3:3, cas 0,35 sul riquadro già rimpicciolito) |
| 6 | Fascia gialla −3°, due righe | **corretto**: «Giorgio Mazzotti» / «PROF. DI LETTERATURA ITALIANA», sempre visibile dove c'è il prof |
| 7 | Slide senza prof (ripassi, glossario, riepilogo, approfondimenti) | **corretto**: tutte rifatte bianche (prima erano schede blu scuro) |
| 8 | Font | Bricolage Grotesque 800, Figtree. Etichette e piè in Figtree Bold come nei fotogrammi del modello (DM Mono non usato) |
| 9 | Finale 5 s con avviso diritti | OK: `Sigla_finale_5s_con_avviso_diritti.mp4` del kit |
| 10 | Struttura | OK: sigla → benvenuto → 6 argomenti con titolo, prof, approfondimento, ripasso, schema, quiz → glossario → riepilogo → verifica → fine → finale → compiti |
| 11 | PDF slide + mappe | consegnati (§4) |

**Testa nel riquadro:** la webcam dell'originale è 247×139 px; il ritaglio 4:3 è 184×138 px ingrandito 2,24×, quindi l'immagine è **morbida** (limite dell'originale). In quasi tutto l'originale i capelli toccano il bordo alto della webcam: la testa è già tagliata in alto **nell'originale** (es. a 0:05, 5:00, 28:20). Non risolvibile.

## 3. Problemi trovati e correzioni
| Minuto | Tipo | Com'era | Correzione |
|---|---|---|---|
| 1:49–1:59 | visivo/audio | il **prof** dice «ecco la fotografia di Giuseppe Ungaretti in tarda età» (non è la voce narrante: non si taglia) ma sullo schermo c'era ancora la slide degli argomenti. La foto è nella sua slide 2 e nell'originale appare a 1:03–1:06 | slide con la foto (dalla sua slide 2) sullo schermo per 3 s, a 1:56–1:59, in sincronia col suo «fotografia» |
| tutto | visivo | prof nel **tondo**; fondo grigio-azzurro; nome in testo semplice; schede blu | tutto rifatto nel modello (§2) |
| 20:28–21:38 (S2) | **audio** | la voce narrante **S2** durava 69 s ma conteneva ~35 s di frasi **non presenti nel testo né nel materiale del prof** («amico di Ungaretti morto suicida … nel 1916», «bellezza e giovinezza perdute», «per Ungaretti i poeti sono veggenti…»): errore di sintesi vocale | nuova voce `REV1` (testo dal materiale del prof: Moammed Sceab, esilio, Ermetismo), generata dal servizio, **accelerata del 4,5 %** per stare nei 69,4 s; schema ricostruito sul nuovo testo |
| 51:32 (compiti) | testo | il video mostrava **3 compiti inventati** («Perché il titolo L'allegria è antifrastico?», «Analizza Veglia», «Spiega Ed è subito sera») | **4 compiti del prof** (PDF «LEZIONE 17», testo identico) nella scheda e in `compiti.json` |
| 51:12 | consegna | verifica finale senza le domande | `verifica_finale.json` + xlsx con le **10 domande del prof** |
| D1–D6 | sincronia | evidenziazioni a occhio; slide ferme mentre il prof passava ad altro (es. nel vecchio montaggio la slide «La raccolta» restava a schermo mentre il prof parlava dello stile, che è nella slide «Soluzioni formali»; durante la teoria dell'Ermetismo restava la pagina del libro. Tempi esatti non rilevati) | evidenziazioni rifatte dalle parole del prof (tempi parola per parola, **stima ±1,5 s**); durante lo stile mostrata la sua slide «Le soluzioni formali»; durante la teoria dell'Ermetismo la sua slide «L'Ermetismo e le correnti» |
| ripassi/glossario/riepilogo | testo | numeri scritti per esteso come li legge la voce («milleottocentottantotto») nelle schede | scritti in cifre |
| 0:54–1:56 | struttura | mentre il prof presenta il corso sullo schermo c'era il solo titolo con elenco semplice | copertina con card **ARGOMENTI** (anche nel benvenuto vocale) |
| fine | visivo | schede «Quiz», «Verifica», «Compiti», «Fine» blu scuro | rifatte bianche nel modello |
| pagine del libro | pagina | miniature illeggibili | fettine dagli screen HD (§5) |
| vtt | testo | trascrizione con molti errori (es. «sa tra sua corrente poetica», «il sedetesame», «capirevo l'edettratura», «Mohamed Sheb», «Apolinea»), senza le voci narranti | rifatto da zero (§6) |
| scheda | testo | titolo «Giuseppe Ungaretti e l'Ermetismo» | «Letteratura V · Lezione 17 · Giuseppe Ungaretti e l'Ermetismo» |

## 4. Slide scelte dal parlato (cosa ho aggiunto)
Il prof mostra a schermo 8 slide e pagine del libro; per tutto il resto del suo parlato ho preparato schede **con testo ricavato da ciò che dice** (non inventato): «In memoria: l'analisi», «Veglia: l'analisi», «San Martino del Carso: l'analisi», «Mattina», «Soldati», «Fratelli» (analisi), «Gli anni del dolore», «I testi chiave dell'Allegria» (con i testi delle sue slide 4, 11, 18), «Ungaretti e il fascismo», «Ed è subito sera: l'analisi». Le slide del prof (introduzione, raccolta, soluzioni formali, Sentimento del tempo, Ermetismo, Luzi con ritratto) sono con il suo testo identico. **Decisione da validare**: nei punti in cui il prof teneva a schermo una slide diversa da ciò che diceva ho mostrato quella pertinente (indicati in §3).

## 5. Pagine del libro in alta risoluzione (B-bis)
Zip `Lez17_ingrandita.zip`: pagine 703, 704, 707, 715, 719, 720, 729, 735. Tagli solo sulle righe bianche, senza intestazioni, numeri di pagina, citazioni e QR; fettina in corso con bordo giallo. **Abbinamento fettina → parlato calcolato dalla trascrizione (stima ±2 s)**.
| Brano | Pagina | File HD | Minuto | Scala sullo schermo |
|---|---|---|---|---|
| In memoria | 703 | Lez17_p703.png · fettina 1 | 10:46 | 1,06 |
| In memoria | 703 | Lez17_p703.png · fettina 2 | 13:32 | 0,89 |
| In memoria | 703 | Lez17_p703.png · fettina 3 | 13:46 | 0,90 |
| In memoria | 704 | Lez17_p704.png · fettina 4 | 14:01 | 0,93 |
| Veglia | 707 | Lez17_p707.png · fettina 1 | 19:42 | 1,22 |
| Veglia | 707 | Lez17_p707.png · fettina 2 | 22:46 | 1,33 |
| Veglia | 707 | Lez17_p707.png · fettina 3 | 22:56 | 1,45 |
| San Martino del Carso | 715 | Lez17_p715.png · fettine 1-3 | 24:37 / 24:50 / 24:55 | 1,45 |
| Mattina | 719 | Lez17_p719.png | 26:38 | 1,45 |
| Soldati | 720 | Lez17_p720.png | 30:56 | 1,45 |
| Fratelli | 729 | Lez17_p729.png · fettine 1-2 | 32:26 / 32:40 | 1,45 / 1,37 |
| Ed è subito sera | 735 | Lez17_p735.png | 46:35 e 47:07 | 1,45 |
Limite: **In memoria (p703) è a scala 0,89–1,06**: il testo del libro in quella pagina è piccolo; interlinea sullo schermo ≈ 50–58 px (stima), altezza dei caratteri ≈ 30 px, al limite del chiesto (≥ 26–30 px). **Controllare a vista.**

## 6. Sottotitoli, PDF, mappe, file
- **Sottotitoli** `Letteratura_Lez17_Parte1.vtt`: 808 cue, max 2 righe, max 49 caratteri a riga (**misurato**). Rifatti dalla trascrizione (Parakeet, parola per parola), con dizionario di correzioni (Ungaretti, Moammed Sceab, Apollinaire, Ermetismo, antifrastico, veggente, Quasimodo, Luzi, Ivry, Cima Quattro, scarnificazione…) e le poesie lette riscritte col **testo esatto del libro**. Le voci narranti usano il testo esatto delle voci. Eliminati gli intercalari («um», «mm»). Tempi dalla trascrizione, allineati ±0,3 s (**stima**, non misurata sull'audio); i tempi del parlato del prof non sono cambiati rispetto al video vecchio.
- **PDF slide** `Letteratura_Lez17_slide.pdf`: 69 pagine A4 orizzontale, senza riquadro e senza fascia; una pagina per slide (le slide con più fettine del libro hanno una pagina per fettina; i passaggi di evidenziazione sono la stessa pagina senza evidenziazione).
- **PDF mappe** `Letteratura_Lez17_mappe.pdf`: 1 pagina A4 orizzontale, **mappa del prof** (PDF «LEZIONE 17») impaginata nel modello `Modello_mappe_BES` (livelli 0–3), contenuto identico; tolti logo e QR di mappe-scuola.com, il ritratto, la copertina dei libri e il facsimile. **Non inserita nel video**: cambierebbe i tempi e i quiz si sfaserebbero su Vimeo (decisione a Sara).
- **Quiz** `quiz_argomenti.json` / `Quiz_Letteratura_Lez17.txt`: 6 quiz × 5 domande, riletti contro le slide e il parlato del prof: coerenti e con una sola risposta giusta. Invariati.
- `verifica_finale.json` + `Letteratura_Lez17_verifica_finale.xlsx`: 10 domande dall'Excel del prof («DOMANDE LEZIONE 17»). `compiti.json`: 4 esercizi. `scheda_pubblicazione.json`, `testo_youtube.txt`, `timeline.json` (invariata: tempi e durate identici).

## 7. DA CONFERMARE COL PROF
- Mappa: «**1914 – torna in Italia schierandosi come interventista; 1915-18 in guerra come volontario**» · slide e voce: «nel 1914 si arruola come volontario».
- Mappa: «Allegria **1931**» · slide: «L'allegria (1916-1942)».
- Mappa: «Allegria **d naufragi**» (refuso) · scritto «Allegria di naufragi».
- Il prof dice che Moammed Sceab è «morto suicida a Parigi nel 1913»; la voce narrante vecchia (S2) diceva «1916»: ora 1913, come il prof.
Nella mappa ho lasciato i dati del prof.

## 8. Cosa NON ho verificato / limiti
- **Ascolto umano:** non ho ascoltato fruscio, ronzio, «metallico» dopo la pulizia, né la pronuncia delle voci Kore (nomi: Moammed Sceab, Apollinaire, Isonzo…). **Non verificato.**
- **Sincronia labbra:** audio e video dell'originale usano lo stesso offset, ritagliati con lo stesso `-ss` (stessa sorgente). Verifica indipendente sul movimento della bocca: **non fatta**.
- **Sottotitoli:** il testo è stato corretto con dizionario e per le poesie, **non riletto cue per cue** (808 cue). Restano probabili errori nel parlato a braccio; passaggi poco comprensibili nella trascrizione sono stati lasciati o ridotti (es. circa 3:25 «che cosa succedeva?», circa 4:10 «Nella less… quartiere italiano»). **Da rileggere.**
- **`controllo_jingle.py`:** non rieseguito: manca il file di riferimento (`/home/claude/v5/snd/quiz.wav`). L'audio dei pezzi Quiz è **copiato campione per campione** dal montaggio precedente alle stesse posizioni (stessi fotogrammi), quindi lo scatto è dove era (**stima**, non misurato).
- **Stato per la master:** `kit/tools/stato.py` non funziona in questa sessione (cerca `/home/claude/lezioni`): lo stato **REVISIONATA** non è stato inviato.
- **Evidenziazioni e fettine:** calcolate dalla trascrizione, ±2 s (**stima**): da controllare in almeno 4 punti da chi guarda.
- **Pagina «Verifica finale» nel video:** è la scheda di pausa (5 s); la prova interattiva la genera la master dai file consegnati.

## 9. Come ho verificato
Trascrizione completa dell'audio (Parakeet TDT, 669 segmenti) del video montato e di `REV1`; 2357 fotogrammi a 1/s sull'originale del prof (classificazione delle slide per cluster) + confronto con le pagine del suo pptx; allineamento audio dell'originale (D1…D6 contigui, offset costanti); conteggio fotogrammi di **ogni pezzo** (45/45 uguali al piano vecchio); contact sheet `controllo_minuti.jpg` (1 fotogramma ogni 30 s); fotogrammi guardati a 740 s, 1400 s, 1760 s, 2700 s, 715 s e il benvenuto; misure ebur128 e picco sul file finale.
