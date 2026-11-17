# RAPPORTO REVISIONE · Letteratura italiana V · Lezione 17 · Giuseppe Ungaretti e l'Ermetismo
Revisione del 16-17/11/2026 (versione 2: regole delle 00:40, 01:20, 01:25, 01:30, 08:15 del 17/11). Video corretto: `Letteratura_Lez17_Parte1_1080p.mp4` (a pezzi `.parte_00…04`, sha256 nel file `.sha256`; la somma dei pezzi corrisponde allo sha256).
Etichette: **misurato** = misurato con uno strumento · **stima** = dedotto · **non verificato** = non ho potuto.
La lezione è stata **rifatta nel modello Spagnolo** (slide dal materiale del prof, riquadro 4:3, fascia gialla, schede di servizio). **La durata è cambiata** (regole del 17/11): mappa del prof nel video, tolti i silenzi > 3 s; tabella secondo vecchio → secondo nuovo al §10.

## 1. Misure sul video nuovo (misurato)
| Controllo | Risultato |
|---|---|
| Formato | 1920×1080, 30 fps, x264 veryfast CRF 19, AAC 192 k, 48 kHz |
| Durata / fotogrammi | **3198,5 s = 53:18 · 95 955 fotogrammi = durata × 30** (prima 3096,97 s: +119 s di mappa, −17 s di silenzi e code); ogni pezzo ha i fotogrammi del piano (46/46) |
| Peso | 394,0 MB (< 400 MB) |
| Volume | −16,8 LUFS integrato, LRA 6,8 LU |
| Picco | **−2,3 dBFS** (≤ −1 dBTP chiesto). Nella prima codifica un punto (4:14) superava 0 dBFS dopo l'AAC: aggiunto limitatore e −1 dB |
| Audio del prof | rifatto **dall'originale** con la catena del kit (`aresample 48000, highpass 80, arnndn sh.rnnn, loudnorm −16, alimiter`) |
| Sincronia labbra/voce | correlazione dell'audio del video finale con l'audio dell'originale (3–9 punti per pezzo): **scarto massimo 0,018 s** su D1…D6 (limite 0,04 s) |
| Immagine ferma del prof | `freezedetect` sul riquadro (412×309, soglia 0,0008, ≥ 1 s): **nessun fermo** nei pezzi del prof. Il riquadro del prof non compare mai nelle schede senza il prof che parla (benvenuto vocale: **senza riquadro**) |
| Jingle Quiz | `controllo_jingle.py` con `quiz.wav` del kit: **Q1–Q6 scarto +0,002 s, tutti OK** |
| PDF | slide: **70 pagine** A4 orizzontale; mappe: 1 pagina A4 orizzontale |

## 2. Confronto col modello Spagnolo (punto 000)
| # | Punto | Esito |
|---|---|---|
| 1 | Sigla 15 s → dissolvenza → copertina | **corretto**: sigla del kit, poi dissolvenza morbida (0,3 s) verso la copertina; stesso dissolvere tra tutti i pezzi (mai taglio secco) |
| 2 | Copertina (logo, «LETTERATURA ITALIANA V · VIDEOLEZIONE», titolo, card ARGOMENTI su 2 colonne) | **corretto** (prima: titolo + elenco senza card) |
| 3 | Slide: fondo bianco, «NN · ARGOMENTO» (numero dell'argomento), titolo + barretta, card | **corretto** (prima: fondo grigio-azzurro, nessun numero dell'argomento corretto) |
| 4 | Piè di pagina «LETTERATURA ITALIANA V · Prof. Giorgio Mazzotti» + «Pagina N» | **corretto** (prima: «Ripasso» al posto del numero in alcune schede) |
| 5 | Riquadro 4:3, ombra grigia, niente bordo | **corretto**: 412×309 px a x=1428, y=148, angoli r=18 (prima: tondo ≈ 290 px). Correzione immagine del kit (contrasto 1,04, saturazione 1,03, hqdn3d 1.5:1.5:3:3, cas 0,35 sul riquadro già rimpicciolito) |
| 6 | Fascia gialla −3°, due righe | **corretto**: «Giorgio Mazzotti» / «PROF. DI LETTERATURA ITALIANA», sempre visibile dove c'è il prof |
| 7 | Slide senza prof (ripassi, glossario, riepilogo, approfondimenti, mappa) | **corretto**: tutte bianche; card in corso con bordo giallo sottile e numero su pallino giallo, ombre grigie morbide (regola 01:30) |
| 8 | Font | Bricolage Grotesque 800, Figtree. Etichette e piè in Figtree Bold come nei fotogrammi del modello (DM Mono non usato) |
| 9 | Finale 5 s con avviso diritti | OK: `Sigla_finale_5s_con_avviso_diritti.mp4` del kit |
| 10 | Struttura | OK: sigla → benvenuto → 6 argomenti con titolo, prof, approfondimento, ripasso, schema, quiz → glossario → riepilogo → verifica → fine → finale → compiti |
| 11 | PDF slide + mappe | consegnati (§4) |

**Testa nel riquadro:** la webcam dell'originale è 247×139 px; il ritaglio 4:3 è 184×138 px ingrandito 2,24×, quindi l'immagine è **morbida** (limite dell'originale). In quasi tutto l'originale i capelli toccano il bordo alto della webcam: la testa è già tagliata in alto **nell'originale** (es. a 0:05, 5:00, 28:20). Non risolvibile.

## 3. Problemi trovati e correzioni
| Minuto | Tipo | Com'era | Correzione |
|---|---|---|---|
| 1:49–1:59 | visivo/audio | il **prof** dice «ecco la fotografia di Giuseppe Ungaretti in tarda età» (non è la voce narrante: non si taglia) ma sullo schermo c'era ancora la slide degli argomenti. La foto è nella sua slide 2 e nell'originale appare a 1:03–1:06 | slide con la foto (dalla sua slide 2) sullo schermo per 3 s, a 1:56–1:59, in sincronia col suo «fotografia» |
| 0:15–0:48 | visivo | nel benvenuto vocale il riquadro del prof era un'**immagine ferma** | tolto: copertina senza riquadro mentre parla la voce; il prof compare solo quando parla (da 0:54) |
| tutto | audio | nessuna transizione sonora, nessun jingle di ripasso | `repaso.wav` all'inizio dei 6 ripassi, `trans.wav` all'inizio di approfondimenti, schemi, mappa, glossario, riepilogo e verifica; jingle Quiz (+0,5 s) e titolo già presenti, verificati |
| tutto | visivo | taglio secco tra un pezzo e l'altro | dissolvenza da/verso il bianco di 0,3 s su ogni pezzo |
| 49:52 | struttura | la mappa del prof non era nel video | **mappa del prof** nel video (49:52–51:51) con voce nuova `MAP1` che la legge |
| D2–D5 | pezzi del prof | pause lunghe a inizio/fine pezzo e dentro il parlato (3–4,6 s) | tolti i silenzi > 3 s: tagli solo in silenzio (RMS < soglia), mai dentro le parole; tabella §11 |
| tutto | visivo | card in corso con fondo giallo pieno | bordo giallo sottile + numero su pallino giallo, fondo bianco |
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
| In memoria | 703 | Lez17_p703.png · fettina 1 | 12:29 | 1,06 |
| In memoria | 703 | Lez17_p703.png · fettina 2 | 13:30 | 0,89 |
| In memoria | 703 | Lez17_p703.png · fettina 3 | 13:44 | 0,90 |
| In memoria | 704 | Lez17_p704.png · fettina 4 | 13:59 | 0,93 |
| Veglia | 707 | Lez17_p707.png · fettina 1 | 21:43 | 1,22 |
| Veglia | 707 | Lez17_p707.png · fettina 2 | 22:40 | 1,33 |
| Veglia | 707 | Lez17_p707.png · fettina 3 | 22:50 | 1,45 |
| San Martino del Carso | 715 | Lez17_p715.png · fettine 1-3 | 24:31 / 24:44 / 24:49 | 1,45 |
| Mattina | 719 | Lez17_p719.png | 28:01 | 1,45 |
| Soldati | 720 | Lez17_p720.png | 30:43 | 1,45 |
| Fratelli | 729 | Lez17_p729.png · fettine 1-2 | 32:11 / 32:25 | 1,45 / 1,37 |
| Ed è subito sera | 735 | Lez17_p735.png | 46:17 e 46:49 | 1,45 |
Limite: **In memoria (p703) è a scala 0,89–1,06**: il testo del libro in quella pagina è piccolo; interlinea sullo schermo ≈ 50–58 px (stima), altezza dei caratteri ≈ 30 px, al limite del chiesto (≥ 26–30 px). **Controllare a vista.**

## 6. Sottotitoli, PDF, mappe, file
- **Sottotitoli** `Letteratura_Lez17_Parte1.vtt`: 808 cue, max 2 righe, max 49 caratteri a riga (**misurato**). Rifatti dalla trascrizione (Parakeet, parola per parola), con dizionario di correzioni (Ungaretti, Moammed Sceab, Apollinaire, Ermetismo, antifrastico, veggente, Quasimodo, Luzi, Ivry, Cima Quattro, scarnificazione…) e le poesie lette riscritte col **testo esatto del libro**. Le voci narranti usano il testo esatto delle voci. Eliminati gli intercalari («um», «mm»). Tempi dalla trascrizione, allineati ±0,3 s (**stima**, non misurata sull'audio); i tempi del parlato del prof non sono cambiati rispetto al video vecchio.
- **PDF slide** `Letteratura_Lez17_slide.pdf`: 69 pagine A4 orizzontale, senza riquadro e senza fascia; una pagina per slide (le slide con più fettine del libro hanno una pagina per fettina; i passaggi di evidenziazione sono la stessa pagina senza evidenziazione).
- **PDF mappe** `Letteratura_Lez17_mappe.pdf`: 1 pagina A4 orizzontale, **mappa del prof** (PDF «LEZIONE 17») impaginata nel modello `Modello_mappe_BES` (livelli 0–3), contenuto identico; tolti logo e QR di mappe-scuola.com, il ritratto, la copertina dei libri e il facsimile. **Nel video** (49:52, 119 s) con la voce `MAP1` (testo derivato dalla mappa, nessuna aggiunta; trascrizione della voce: somiglianza 0,94 col testo; **pronuncia non ascoltata**).
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
- **Stato:** inviato con `stato.py` (symlink `/home/claude/lezioni`); stato finale `REVISIONATA` alla consegna.
- **Pagina della lezione:** `quiz_argomenti.json` non contiene secondi; i secondi nuovi sono in `scheda_pubblicazione.json` e `timeline.json`.
- **Evidenziazioni e fettine:** calcolate dalla trascrizione, ±2 s (**stima**): da controllare in almeno 4 punti da chi guarda.
- **Pagina «Verifica finale» nel video:** è la scheda di pausa (5 s); la prova interattiva la genera la master dai file consegnati.

## 9. Come ho verificato
Trascrizione completa dell'audio (Parakeet TDT, 669 segmenti) del video montato e di `REV1`; 2357 fotogrammi a 1/s sull'originale del prof (classificazione delle slide per cluster) + confronto con le pagine del suo pptx; allineamento audio dell'originale (D1…D6 contigui, offset costanti); conteggio fotogrammi di **ogni pezzo** (45/45 uguali al piano vecchio); contact sheet `controllo_minuti.jpg` (1 fotogramma ogni 30 s); fotogrammi guardati a 740 s, 1400 s, 1760 s, 2700 s, 715 s e il benvenuto; misure ebur128 e picco sul file finale.

## 10. Secondi vecchio → nuovo (la durata è cambiata)
| Voce | Vecchio (s) | Nuovo (s) |
|---|---|---|
| Quiz 1 | 739,67 | 739,67 |
| Quiz 2 | 1297,83 | 1293,63 |
| Quiz 3 | 1677,93 | 1670,73 |
| Quiz 4 | 2121,50 | 2106,00 |
| Quiz 5 | 2662,37 | 2644,27 |
| Quiz 6 | 3005,00 | 2987,07 |
| Mappa (nuova) | — | 2990,07 (119,5 s) |
| Verifica finale | 3072,47 | 3174,00 |
| Compiti | 3091,97 | 3193,50 |
| Durata totale | 3096,97 | 3198,50 |
`scheda_pubblicazione.json` (inizio_s, quiz_s, durata_s), `timeline.json` e `testo_youtube.txt` (capitoli) sono già aggiornati. La master deve rigenerare la pagina e sostituire il video sullo stesso link.

## 11. Pezzi del prof: inizio e fine (mai a metà frase)
Tempi nel video nuovo; parole dalla trascrizione (Parakeet). **Tutti i pezzi iniziano e finiscono su una pausa**, nessuna parola mozzata (verificato sul livello audio: pause di 0,5–2 s ai bordi).
| Pezzo | Inizio | Prime parole | Fine | Ultime parole | Frase finita |
|---|---|---|---|---|---|
| D1 | 0:53 | «Buongiorno e benvenuti alla lezione su Giuseppe Ungaretti…» | 10:46 | «…il linguaggio mira all'essenzialità e alla concentrazione lirica.» | sì |
| D2 | 12:29 | «Qua ne possiamo già vedere un estratto…» | 19:38 | «…Per capire… Proseguiamo, vediamo.» | sì |
| D3 | 21:43 | «Molto importante questo spiegherà…» | 26:31 | «…riprese e antitesi a distanza.» | sì |
| D4 | 28:01 | «Santa Maria La Longa, il 26 gennaio 1917…» | 33:40 | «…e di ribellione profonda contro la consapevolezza della propria fragilità e precarietà esistenziale.» | sì |
| D5 | 35:16 | «Per finire, per andare alle conclusioni…» | 42:39 | «…il punto fondamentale che dovevamo aggiungere in chiusura ad Ungaretti.» | sì |
| D6 | 44:14 | «Per finire la lezione abbiamo già delineato bene o male l'Ermetismo…» | 48:22 | «…o profondamente umani, alla vita.» | sì |
Tagli dentro il parlato (solo in silenzio ≥ 3,1 s, ciascuno −1,5…2,0 s): a 18:01, 29:35, 32:11, 35:37 del video nuovo; più i silenzi a inizio/fine pezzo tolti.
