# RAPPORTO REVISIONE · Letteratura italiana V · Lezione 19 · Dal secondo dopoguerra a oggi
Revisione del 16/11/2026 (prova del metodo «2 ore»). Video corretto: `Letteratura_Lez19_Parte1_1080p.mp4` (a pezzi `.parte_00…01`, sha256 nel file `.sha256`).
Ogni dato è etichettato **misurato** (con uno strumento), **stima** (dedotto) o **non verificato**. Mai «fatto» senza una misura.

## 1. Misure sul video nuovo (misurato)
| Controllo | Risultato |
|---|---|
| Formato | 1920×1080, 30 fps, x264 veryfast (CRF 19; tratti col prof CRF 21), AAC 192k 48 kHz |
| Durata / fotogrammi | **50:25,23 · 90 757 fotogrammi** = durata × 30. **La durata è cambiata** (prima 53:44,17 · 96 725) per la decisione di Sara delle 00:40: via le 3 mappe nostre e la loro voce, mappa finale accorciata alla sola voce nuova, pezzi del prof allungati/accorciati a fine frase. Tabella dei secondi sotto |
| Peso | 170.1 MB (sotto i 400 MB) |
| Volume | −16,5 LUFS integrato (LRA 6,4) · picco (true peak) **−1,3 dBTP** (≤ −1 dBTP chiesto) |
| Silenzi ≥ 3 s | 3 silenzi sulle schede di servizio, **non nella voce**: 49:57–50:01 (Verifica finale, dopo il jingle), 50:16–50:20 e 50:21–50:25 (Compiti): sono schede statiche in cui il video si ferma per la pagina; lasciati così. Nessun silenzio ≥ 3 s nel parlato del prof, nelle voci o nelle schede degli argomenti (a −45 dB) |
| Fermi immagine del riquadro (`freezedetect`, ≥ 1 s) | **nessuno** nei 4 pezzi del prof (D0–D3), misurato sul riquadro; copertina e presentazione (0:18–0:48) **senza riquadro**: il prof compare solo dal 0:48, quando parla |
| Scarto audio/video del prof | **max 0,005 s** (17 punti, ≥1 per ogni pezzo del prof, correlazione del suo audio nel video nuovo con l'audio dell'originale, da cui provengono anche i fotogrammi); limite 0,04 s. Il ritardo di 15 ms del filtro audio è compensato |
| Jingle Quiz a 0,0 s (`controllo_jingle.py`) | Q1 +0,021 s · Q2 +0,024 s · Q3 +0,023 s (tolleranza 0,05 s): **OK**. Il jingle (`quiz.wav`) è nello zip `Telesio_kit_produzione_v1.zip` (cartella `home/claude/v5/snd/`), non in `kit/` |
| Jingle e transizioni | scheda **Quiz**: `quiz.wav` (già presente, misurato); **titolo argomento**: `titolo.wav` (già presente nelle tre schede T); **Verifica finale** e **Compiti**: `titolo.wav` aggiunto (prima in silenzio); **transizioni**: `trans.wav` a −10 dB e dissolvenza di 0,2 s su 29 passaggi (prima nessun suono, taglio con sola dissolvenza); sulle schede a scatto (Quiz, Verifica, Fine, Compiti) nessuna dissolvenza, come nel vecchio |
| PDF | slide: **31 pagine** A4 orizzontale (identiche alle slide del video, senza riquadro e fascia); mappe: **1 pagina** A4 orizzontale (la mappa del prof) |
| Sottotitoli | 728 cue, max 2 righe, max 49 caratteri per riga |
| Confronto pagine PDF ↔ video | fatto su tutte le 31 pagine: titolo, intestazione e piè di pagina coincidono con il fotogramma del video (scarto medio ≤ 0,7 su 255); sul resto della slide lo scarto è ≤ 1,2 dove lo stato è lo stesso e fino a 3,4 dove nel video c'è una card evidenziata (atteso) |

### Secondi vecchio → nuovo (da aggiornare nella pagina; già nel `scheda_pubblicazione.json`)
| Punto | Vecchio (s) | Nuovo (s) |
|---|---|---|
| Inizio argomento 1 | 171,898 | 171,270 |
| Quiz 1 | 1287,865 | 1219,700 |
| Inizio argomento 2 | 1292,865 | 1224,670 |
| Quiz 2 | 2143,633 | 2021,833 |
| Inizio argomento 3 | 2148,633 | 2026,837 |
| Quiz 3 | 3050,468 | 2866,400 |
| Verifica finale | 3193,486 | 2994,600 |
| Compiti | 3213,006 | 3014,133 |
| Durata | 3224,167 | 3025,233 |

### Fine e inizio di ogni pezzo del prof (misurato sulla trascrizione)
Ogni pezzo finisce a fine frase e inizia a inizio frase (i tagli interni di 0,6–1,3 s sono nei silenzi tra due parole). Il pezzo 2 del vecchio montaggio finiva a metà frase («…Patrizia Cavalli, vedete… e Patrizia Valduga»): corretto.
| Pezzo | Dal minuto | Al minuto | Prime parole | Ultime parole | Frase finita |
|---|---|---|---|---|---|
| Prof 1 (presentazione) | 0:48,1 | 2:51,6 | «Buongiorno e benvenuti alla lezione…» | «…c'è anche la parte di teatro. Bene, allora.» | sì |
| Prof 2 (argomento 1) | 2:56,5 | 13:32,8 | «Vediamo di dare delle coordinate storiche…» | «…voi capite… la pluralità, la ricchezza.» | sì |
| Prof 3 (argomento 2) | 20:29,2 | 28:12,9 | «L'incredibile vastità di argomenti e di situazioni…» | «…Patrizia Cavalli… e Patrizia Valduga.» | sì |
| Prof 4 (argomento 3) | 33:51,4 | 42:45,8 | «I maestri della narrativa. C'è anche la…» | «…materiale già più. Come dire. D'esame.» | sì |

## 2. Confronto col modello Spagnolo (punto 000)
| # | Punto | Esito |
|---|---|---|
| 1 | Sigla 15 s → dissolvenza morbida → copertina | **corretto**: sigla invariata (kit), dissolvenza di 1,3 s sulla nuova copertina (misurato 0:16,7–0:18,0). **Segnalo**: la sigla di Letteratura (kit, già approvata) porta la scritta «[ANALISI TESTUALE]»: non l'ho toccata, decide la master |
| 2 | Copertina (logo, riga «LETTERATURA ITALIANA V · VIDEOLEZIONE», titolo Bricolage 800, barretta, card ARGOMENTI) | **corretto** (prima: titolo + elenco, prof senza riquadro) |
| 3 | Slide fondo bianco, «01 · ARGOMENTO», titolo + barretta, card | **corretto** (prima fondo azzurrino, card diverse) |
| 4 | Piè «LETTERATURA ITALIANA V · Prof. Giorgio Mazzotti» + «Pagina N» | **corretto** su tutte le slide (N = pagina del PDF; mai il numero della lezione) |
| 5 | Riquadro 4:3 | **corretto**: 412×309 px a x=1428, y=148, angoli arrotondati r=18, ombra grigia, nessun bordo (prima: tondo). Ritaglio 4:3 dalla webcam dell'originale (185×139 px → ×2,2: morbido) con correzione del kit (contrasto 1,04, saturazione 1,03, hqdn3d 1.5:1.5:3:3, cas 0.35) |
| 6 | Fascia gialla −3°, due righe | **corretto**: «Giorgio Mazzotti» / «PROF. DI LETTERATURA ITALIANA», su tutte le slide col prof |
| 7 | Slide senza prof | **corretto**: approfondimenti, ripassi, glossario, riepilogo, mappa, schede nel modello. Card «in corso» come da aggiornamento 01:30: **bordo giallo sottile, numero su pallino giallo, fondo bianco**; le altre card con bordo grigio chiaro; ombre **grigie e morbide** (nessuna ombra nera o a blocco); controllato su tutte le 31 pagine del PDF e sui fotogrammi |
| 8 | Font | Bricolage Grotesque 800 (titoli), Figtree (testo ed etichette). DM Mono non usato (nel modello le etichette sono in Figtree, come nella lez. 3) |
| 9 | Finale 5 s con avviso diritti | OK, invariato (50:07–50:14, kit). Prima: «Fine della lezione» rifatta nel modello (50:00–50:07) |
| 10 | Struttura | OK: sigla, presentazione, 3 argomenti (titolo, prof, approfondimenti, ripasso con voce, schema, quiz 5 domande), mappe, glossario, riepilogo, finale; verifica e compiti a fine video |
| 11 | PDF slide + mappe | consegnati |

## 3. Problemi trovati e correzioni
| Minuto (nuovo = vecchio) | Tipo | Com'era | Correzione |
|---|---|---|---|
| tutto | visivo | prof nel tondo, fondo azzurrino/grigio, card e animazioni in grafica diversa, schede finali scure | tutto rifatto: 34 slide e 204 stati, riquadro 4:3, fascia, schede nel modello |
| 0:18–0:48 | visivo | riquadro del prof con una **foto ferma** durante la voce di benvenuto (e durante la dissolvenza dalla sigla) | riquadro e fascia tolti: la copertina non ha il prof (regola 08:15: riquadro solo se il prof parla). Il prof compare dal 0:48, quando parla davvero |
| 0:19–0:45 | audio | voce di benvenuto: «La storia e la società?» al posto del titolo dell'argomento 1 (dalla trascrizione) | nuova voce **RV1** con i tre titoli esatti (i primi 16 s della traccia generata erano la «regia» letta ad alta voce: tagliati, misurato) |
| 2:56–6:27 | sincronia | slide «Il quadro storico-politico» ferma con la card 1 evidenziata per ~3,8 min (misurato sui fotogrammi 1/s del vecchio) mentre il prof parla dello sfondo storico, non della Repubblica del 1946 (il prof dice «2 giugno 1946» a 335,7 s dell'originale = 6:27 nel nuovo) | slide aggiunta «Il secondo Novecento: lo sfondo» con 4 card prese **parola per parola dal prof** (153 s, 190 s, 256 s, 302 s nell'originale), accese dal parlato; la card 1 della slide 3 si accende quando il prof dice «2 giugno 1946» |
| tutte le slide del prof | sincronia | evidenziazioni scelte a occhio | rifatte dalla trascrizione del prof (tempi parola per parola, **stima ±1 s**, vedi §5); ogni card è accesa quando il prof ne parla, nessuna slide ferma > 60 s con un tema diverso salvo i due casi sotto |
| 11:24–11:50 (slide «Globalizzazione e debito pubblico») | sincronia | slide del prof mai commentata dal prof | mostrata per 26 s nel punto in cui il prof chiude la parte sulle tensioni (633,8–660 s originale) con la card accesa; **da confermare col prof** |
| 25:57–28:12 | sincronia | slide «La linea lombarda e le ultime tendenze» ferma 130 s (Sereni, Giudici, Cavalli, Valduga) | invariato: unica card del prof, tema coerente con il parlato (non fermo su un altro argomento) |
| 41:12–42:45 | sincronia | alla fine il prof riassume (93 s) con la slide Eco/Maraini ferma | al posto della slide ferma compare **la mappa del prof** (dalle 1681 s originale), nella stessa durata |
| tutto il parlato del prof | audio | non dimostrabile che fosse pulito | rifatto dall'**originale** con la catena del kit: `aresample 48000, highpass 80, arnndn (sh.rnnn), loudnorm −16, alimiter`, −1 dB di margine; 18 tagli delle pause (0,6–1,3 s) rifatti **nei silenzi** dell'originale (energia del tratto tolto: 15–323 su picchi del parlato > 1500), tempi nuovi (vedi tabella secondi) |
| 29:21–30:24 (AN2b, Caproni) | audio/contenuto | la voce diceva «un artificio ingannevole, **capace** di svelare il senso ultimo dell'esistenza»: il prof dice «**in**capace» | frase rigenerata (**RV2**) e inserita al posto di quella (misurato: +1,9 s, assorbiti nei silenzi della coda; 0,26 s con un'accelerazione dell'1,4% della sola frase) |
| 44:05–45:28 (AN3b, Ginzburg) | audio/contenuto | «priva di **ascensioni** liriche»: il prof dice «accensioni liriche» | frase rigenerata (**RV3**) e inserita (−0,3 s) |
| 45:28–46:42 (AN3c, Maraini) | audio/contenuto | «**Donne** in guerra»: il titolo è **Donna** in guerra (anche il prof) | frase rigenerata (**RV4**) e inserita (−1,0 s) |
| 47:51–48:44 (mappa finale) | contenuto | quattro mappe nostre (una per argomento + finale) con rami e parole chiave inventati da noi, non del prof | **tolte tutte e quattro** (e le loro voci): resta **la mappa del prof** (albero con i suoi due rami e gli esponenti), animata a tempo con una nuova voce **RV5** (50 s; l'attesa muta di 17 s dopo la voce è stata tolta). Durata −3:19 rispetto a prima |
| tutto, sottotitoli | testo | 706 cue con errori da riconoscimento automatico, ad es. «dopo guerra», «statisolati», «confrontatico», «sudannuzio», «Piumbo», «bohettaggi», «aredità», «ghiatto pardo» | `.vtt` **rifatto** da zero: prof dalla trascrizione dell'originale + correzioni a mano di nomi, titoli e frasi (141 regole di correzione + 20 tratti di borbottio tolti, vedi §5 per i dubbi); voci Kore dal copione esatto, agganciato alla voce parola per parola; 728 cue, tempi misurati su 3 spezzoni da 60 s (scarto cue–parlato da −0,32 a +0,02 s, esclusi i cue che iniziano a metà frase) |
| 49:54–50:25 | testo/grafica/audio | schede «Quiz», «Verifica finale», «Compiti», «Fine» scure, stile diverso; Verifica e Compiti in silenzio | rifatte nel modello (bianche, logo, piè di pagina); jingle `titolo.wav` su Verifica e Compiti |
| fine | consegna | `compiti.json` in formato diverso; verifica da 10 domande dell'Excel non presente come file; nessun PDF slide/mappe | prodotti: `verifica_finale.json` + xlsx (10 domande del prof; le 4 risposte della domanda 1 erano date Excel: scritte «2 giugno 1946», «1 gennaio 1948», «25 aprile 1945», «2 giugno 1954»), `compiti.json` (4 esercizi, testo identico al PDF del prof), `…_slide.pdf`, `…_mappe.pdf` |
| scheda | testo | titolo «Dal secondo dopoguerra a oggi» | «Letteratura V · Lezione 19 · Dal secondo dopoguerra a oggi» |
| quiz 3, d. 5 | testo | «Che cosa unisce Dacia Maraini?» | «…nelle sue opere?» (risposte invariate). Quiz riletti contro le slide del prof: domande e risposte giuste coerenti |
| audio (messa a punto) | audio | — | l'audio estratto dal video vecchio era **in anticipo di 83 ms** sul video (misurato per correlazione con `controllo_jingle`): ricorretto, i quiz tornano a 0,0 s |

## 4. Pagine del libro in HD
La lezione 19 **non ha pagine del libro**: punto non applicabile.

## 5. Cosa NON ho verificato / limiti
- **Ascolto umano: non fatto.** Non ho ascoltato né il prof pulito (fruscio, ronzio, «metallico») né le voci Kore. Dopo la pulizia ho misurato solo volume e picco. **Non verificato.**
- **Pronuncia della voce Kore:** non posso ascoltarla. Ho confrontato il parlato con il copione con il riconoscimento automatico, che sbaglia sui nomi rari quanto una voce sbagliata: non so distinguere. Nella nuova voce RV5 il riconoscimento ha capito «Aldamerini» e «Pefenolio» (Alda Merini, Beppe Fenoglio); nelle vecchie S3 «Pe Fenoglio», «Da Camaraini», «Ucria». **Da ascoltare** (nomi: Alda Merini, Fenoglio, Maraini, Ucrìa, Céspedes, Menabò). Non ho potuto fare di più senza ascoltare.
- **Jingle e transizioni nuovi** (`titolo.wav` su Verifica e Compiti, `trans.wav` a −10 dB su 29 passaggi): inseriti e misurati nei tempi, **non ascoltati**; il livello è una stima. Se sovrastano la voce, abbassare di 3 dB.
- **Voci nuove:** nomi `RV1…RV5` (non `R1…`: `R1–R3` esistono già, sono i ripassi). RV2–RV4 sono inserite come **frasi singole** (non l'intero approfondimento) per non cambiare la durata; il resto è la voce di prima.
- **Evidenziazioni:** calcolate con la trascrizione automatica (Parakeet): **stima ±1 s**. Da controllare in almeno 4 punti da chi guarda.
- **Sottotitoli del prof:** il testo viene dalla trascrizione automatica corretta a mano; **non l'ho riascoltato cue per cue**. Punti dubbi (minuti del video nuovo): 23:47 «Il passaggio d'Enea e Cronistoria» (il riconoscimento ha scritto «finzioni e cronistoria»); 23:54 «con il dramma della propria vicenda privata» (parola illeggibile); 40:06 «ironia dissacrante» (illeggibile). Il passo «la corporeità più totale» non è più nel video (tolto con lo spostamento del taglio a fine frase). Frasi senza senso del prof (borbottii) tolte.
- **Sincronia labbra:** misurato lo scarto audio/video del prof (max 5 ms, §1: l'audio e i fotogrammi vengono dallo stesso originale; il ritardo di 15 ms del filtro è compensato). Verifica indipendente dei movimenti della bocca: non fatta. **Non verificato** all'ascolto.
- **Webcam piccola:** il ritaglio 4:3 prende 185×139 px dell'originale, ingrandito 2,2×: immagine morbida. I capelli toccano il bordo alto già nell'originale (es. 0:05, 5:00, 19:00): non risolvibile. Testa mai tagliata ai lati.
- **Mappe:** il prof ha mandato **una sola mappa** (tutta la lezione). Quella è nel video (due volte: alla fine del prof, 41:12, e nello slot finale 47:51) e nel PDF. Nel video **non c'è nessuna mappa nostra** (regola delle 00:40): solo quella del prof, nello slot finale e a pagina 25 del PDF slide.
- **Slide non del prof:** «Il secondo Novecento: lo sfondo» (4 card dalle parole del prof) e le schede degli approfondimenti non sono slide del prof. Il `.pptx` del prof per la lezione 19 **non è nella release** (solo 17 e 26 per le ultime lezioni): i testi delle slide vengono dalla dispensa del montaggio precedente e dall'originale del prof (il fotogramma 5:00 dell'originale mostra la slide del prof: confrontata, il testo coincide). Non ho fatto il confronto su tutte le slide dell'originale.
- **Quiz:** riletti contro il testo delle slide, non aggiunti né tolti.
- **Pagina interattiva:** non ho aperto il player (la genera la master).
- **Alcune slide sono lunghe** (s9: 130 s; mappa finale del prof: 95 s) perché hanno una sola card o il prof riassume; vedi tabella.

### DA CONFERMARE COL PROF
1. **Titoli delle raccolte di Caproni** citati a 23:47 («Il passaggio d'Enea e Cronistoria»?): la trascrizione automatica dice «finzioni e cronistoria».
2. **Alda Merini:** il prof dice a 25:03 «è arrivata fino all'inizio del 2000» (sottotitolo: «all'inizio del Duemila»); la slide non riporta date. Verificare l'affermazione.
3. **Mappa:** il prof scrive «ALBA DE CESPEDES» (senza accento) e le slide «Alba de Céspedes»: nella mappa ho scritto **Céspedes** (ortografia corretta). Nessuna data della mappa è in contrasto con slide o voce (la mappa non ne ha).
4. **Slide «Globalizzazione e debito pubblico»** (seconda slide «Trasformazioni economiche e sociali»): il prof non ne parla; l'ho lasciata nell'ordine del prof.
5. **Titolo della scheda finale** «Letteratura V · Lezione 19 · Dal secondo dopoguerra a oggi»: il titolo viene dalla scheda precedente, non dal prof.

## 6. Come ho verificato
Rifatto il 17/11 con le regole delle 00:40, 01:20, 01:25, 01:30 e 08:15. Trascrizione completa dell'originale (29:35, 321 segmenti) e del video vecchio (675 segmenti) con `trascrivi.py` (Parakeet TDT); allineamento audio vecchio↔originale (3 464 finestre agganciate su 3 502), 3 224 fotogrammi a 1/s del video vecchio e scarti per fotogramma per i punti di taglio; 101 fotogrammi a 1/30 s sul video nuovo (`controllo_minuti.jpg`); controllo del riquadro a 10 fotogrammi/s; ebur128 (volume e picco); `controllo_jingle.py` sul video nuovo e sul vecchio; trascrizione di tre spezzoni del video nuovo (3×60 s) per i sottotitoli; confronto pagina per pagina del PDF con il video; piano di montaggio: 38 segmenti = 90 757 fotogrammi; `freezedetect`, `silencedetect` e correlazione audio per ogni pezzo del prof.
