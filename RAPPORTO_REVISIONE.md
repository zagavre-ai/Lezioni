# RAPPORTO DI REVISIONE · Letteratura italiana V · Lezione 15 · La narrativa tra le due guerre
Prof. Giorgio Mazzotti · chat di revisione · 16/11/2026 · **VERSIONE FINALE (aggiornata 17/11 con le correzioni della master)** · stato **REVISIONATA**

**Video nuovo:** 51:41,8 (3101,8 s) · 93 055 fotogrammi (= durata × 30, OK) · 1920×1080 · 30 fps · x264 veryfast CRF 19 · AAC 192 k 48 kHz · 300,0 MB (4 parti da 90 MB, `sha256` uguale alla ricomposizione) · **−16,5 LUFS**, picco vero **−2,3 dBTP**. Il prof non è stato tagliato: i 4 pezzi coprono tutto l'originale (1876 s).

## 1. Che cosa ho verificato e come
| Cosa | Come | Esito |
|---|---|---|
| Video montato | pezzi ricomposti, sha256 uguale; fotogrammi/durata/peso con `ffprobe` | OK (misurato) |
| Audio (A) | trascrizione completa Whisper *small* (it) del video montato + `silencedetect` + `loudnorm`; trascrizione del prof con Whisper *medium* | misurato |
| «ecco / guarda / in questa foto…» | cercate in tutta la trascrizione: le uniche occorrenze sono del **prof** («ecco qua Federigo, come vedete, Federigo Tozzi» a 33:44 del montato: la slide con il ritratto c'è) o frasi generiche. **Nessuna frase della voce narrante** nomina immagini che mancano | OK |
| Visione (B) | 111 fotogrammi (uno ogni 30 s) + **164 stati di slide** con OCR; confronto con `kit/modello_spagnolo/` | misurato |
| Sincronia slide–prof | per ogni scheda evidenziata ho confrontato il tempo con la riga dei sottotitoli del prof (vedi problemi 7–13) | corretto |
| Testo (C) | OCR delle slide, dispensa, quiz, verifica (.xlsx), compiti, scheda, testo YouTube, tutti letti | misurato |
| Sottotitoli | trascrizione rifatta e **riletta riga per riga** (354 blocchi del prof, circa 300 corretti a mano; 8 tratti di voce narrante che mancavano) | fatto a mano |
| Pagine del libro (B-bis) | la lezione 15 **non ha pagine del libro** (lista del punto B-bis) | non applicabile |

**Non ho potuto verificare** (scritto perché sia chiaro): all'**ascolto** fruscio/ronzio/«metallico» (misuro solo livelli: nel montato il filtro a 80 Hz c'è, −13 dB sotto gli 80 Hz rispetto all'originale; `arnndn` non è dimostrabile da qui); la **sincronia delle labbra** (il controllo automatico sui pixel non dà un segnale: la webcam è troppo piccola; ho misurato invece l'allineamento sull'audio: offset costante per pezzo −41,43 / −303,03 / −561,40 / −865,93 s, correlazione 0,83–0,97 in tutte le finestre); lo **scatto dei Quiz a 0,0 s** (il kit non ha il suono di riferimento: `controllo_finale.py` risponde «non trovato»; le schede Quiz stanno agli stessi fotogrammi di prima rispetto all'audio); i dettagli dei testi di approfondimento scritti da noi (es. «Sauze d'Oulx → Salice d'Ulzio»).

## 2. Tabella dei problemi trovati (minuti = video montato vecchio)
| # | Minuto | Tipo | Com'era | Come l'ho corretto |
|---|---|---|---|---|
| 1 | tutta la lezione | visivo | Prof nel **tondo** (Ø ~250 px) con «Prof. Giorgio Mazzotti» piccolo sotto; niente fascia gialla | riquadro **4:3 412×310 (x 1428, y 148)**, angoli arrotondati, ombra grigia, nessun bordo; **fascia gialla −3°** «Giorgio Mazzotti» / «PROF. DI LETTERATURA ITALIANA», sempre visibile dove c'è il prof. Ritaglio dalla webcam del video **originale** (box 246×138, due posizioni: sotto fino a 19:29, sopra dopo) con contrasto 1,04, saturazione 1,03, `hqdn3d 1.5:1.5:3:3`, `cas 0.35` sul riquadro già rimpicciolito |
| 2 | tutta la lezione | visivo | Fondo grigio-azzurro, **tre stili diversi** (slide / approfondimenti / ripassi), testo piccolo, metà schermo vuoto, piè di pagina con «Introduzione/Ripasso/Approfondimento» invece di «Pagina N» | tutte le slide rifatte **identiche a Spagnolo** (vedi tabella 3) |
| 3 | 0:15 | visivo | dalla sigla nera alla copertina bianca c'era un **taglio netto** (lampo) | dissolvenza di 1 s |
| 4 | 19:13–19:24 | testo | sulla slide di ripasso: **«venticinque luglio 1940tré»** (anche nella dispensa, pag. 2) | «25 luglio 1943» |
| 5 | 13:10–13:18 | visivo/audio | ripasso arg. 1: la voce legge 4 punti, sullo schermo ne mancava uno (la marcia su Roma) | 4 punti a schermo, in sincronia |
| 6 | 0:15–0:37, 12:30–13:17, 18:31–19:23, 32:08–32:59, 51:31–52:20, 53:20–55:00 | testo | **~6 minuti di voce narrante senza sottotitoli** (benvenuto, 4 ripassi, glossario, riepilogo, congedo). Nel parlato del prof il .vtt era una trascrizione automatica con errori («ventegno», «shopperi», «ricotozi», «Fonda Mara», «il letteratura»…) | trascrizione rifatta e riletta: 880 blocchi, max 2 righe da 42, 1–6 s, 0 sovrapposti |
| 7 | 1:51–3:42 | visivo | card «Le condizioni dell'Italia» evidenziata per 111 s mentre il prof presenta la lezione (parla della crisi dal 3:44) | nessuna card evidenziata fino al 3:42, poi la card 1 |
| 8 | 4:47 | visivo | card «vittoria mutilata» 3 s in ritardo | a 4:44 (il prof la nomina a 4:44) |
| 9 | 14:26–14:56 | visivo | «Economia e società» in ritardo di ~4 s; poi «Il controllo delle masse» evidenziata mentre il prof parla di Patti Lateranensi, autarchia, IMI/IRI (cioè dell'altra card) | «Economia e società» dal momento in cui il prof dice «nel 1929… Patti Lateranensi» fino a fine pezzo; «controllo delle masse» non viene nominata dal prof in questo pezzo: non evidenziata |
| 10 | 15:08 | visivo | «alleanza con la Germania» 2 s in ritardo | anticipata di 2 s (15:06), quando il prof la nomina |
| 11 | 19:32–23:28 | visivo | **card «L'intellettuale di regime» evidenziata per 3 min 56 s** mentre il prof parla di altro (mobilitazione delle masse, Ministero della Cultura Popolare, radio e cinema, poi Gentile/manifesti) e pagina «politica linguistica» 6 s in ritardo | nessuna evidenziazione nel preambolo; «mezzi di comunicazione» quando cita stampa/radio/cinema; «intellettuale di regime» da Gentile; pagina linguistica da «unificazione linguistica» |
| 12 | 36:09 | visivo | card «Alvaro» 16 s prima che il prof ci arrivi («Proseguiamo allora… Alvaro» a 36:25) | a 36:25 |
| 13 | tutta la lezione | visivo | testi piccoli, «Pagina N» che salta | pagine numerate 1…63 nell'ordine del video, uguali al PDF |
| 14 | 11:35, 17:35, 31:16, 52:30 | contenuto | **Mappe concettuali inventate da noi** (arg. 1, 2, 3 e mappa finale) | **tolte** (regola «non inventarla»; tagliata solo la voce narrante, mai il prof) |
| 15 | 50:33–51:26 | contenuto | mappa arg. 4 con parole chiave («crisi, inettitudine, Meridione…») che nella mappa del prof **non ci sono** | **mappa del prof** (`MAPPE/LEZIONE 15.pdf`) con testo identico, nostra grafica, **voce nuova Kore** (6 frasi `PM1–PM6` generate dalla master) che legge i suoi riquadri |
| 16 | 55:00–55:24 | struttura | dopo «Fine della lezione» c'erano le schede «Verifica finale» e «Compiti» **dopo** il «GRAZIE»; finale non quello del kit | tolte dal video (stanno fuori, regola 10); finale = `Sigla_finale_5s_con_avviso_diritti.mp4` |
| 17 | audio | audio | picco vero **+0,63 dBTP** (limite −1) | limitatore: −2,5 dBTP; −16,4 LUFS |
| 18 | consegna | testo | `compiti.json` in formato sbagliato (lista di stringhe) | `{"titolo","esercizi":[{"n","tipo","testo"}]}`, testo identico al PDF del prof (4 esercizi) |
| 19 | consegna | testo | scheda: titolo «La narrativa tra le due guerre · Parte 1» | «Letteratura V · Lezione 15 · La narrativa tra le due guerre»; tempi di argomenti e quiz ricalcolati; `t_verifica` e `t_compiti` = fine video (sono fuori dal video) |
| 20 | consegna | testo | «Dispensa» e «Mappe» PDF non erano né le slide del video né le mappe del prof | `…_slide.pdf` (63 pagine = le slide del video) e `…_mappe.pdf` (1 pagina: la mappa del prof) |
| 21 | consegna | testo | testo YouTube con «Parte 1» e capitoli vecchi | rifatto con i nuovi tempi |
| 22 | 31:16 (nuovo) | visivo | **1,7 s di webcam ferma** nel pezzo del prof | è nell'**originale** (a 19:29 il prof dice «mi sposto un poco più sopra»: la finestra si muove). Non è un errore di montaggio; lo lascio, non si taglia il prof |
| 23 | vari | visivo | in alcuni punti la cima dei capelli del prof è tagliata | è già così nella webcam originale (il prof è molto vicino al bordo): più in alto non c'è immagine |
| 24 | es. 12:22 (nuovo) | audio | silenzi 2,4–3,8 s | solo alle **schede Quiz** (pausa prevista, 5 s). Il più lungo (3,8 s) è la scheda del quiz 4 + 0,8 s prima del glossario |

## 3. Confronto con il modello Spagnolo, punto per punto (regola 000)
| Punto | Esito |
|---|---|
| 1 Sigla 15 s → dissolvenza morbida → copertina | **corretto** (prima: taglio netto) |
| 2 Copertina (logo, riga DM Mono «LETTERATURA ITALIANA V · VIDEOLEZIONE», titolo Bricolage 800 + barretta, card ARGOMENTI su due colonne) | **corretto** |
| 3 Slide: fondo bianco, «01 · NOME ARGOMENTO» (numero dell'argomento), titolo + barretta, card e tabelle (glossario con intestazione blu notte), giallo solo per evidenziare | **corretto** |
| 4 Piè di pagina «LETTERATURA ITALIANA V · Prof. Giorgio Mazzotti» + «Pagina N» | **corretto** (mai il numero della lezione) |
| 5 Riquadro 4:3, ombra grigia, nessun bordo, tutta la testa e le spalle | **corretto** (412×310 a x 1428, y 148, misurato sul modello); testa: vedi problema 23 |
| 6 Fascia gialla −3°, due righe, sempre visibile | **corretto** |
| 7 Slide senza prof (approfondimenti, ripassi, glossario, riepilogo): testo grande, parole chiave in giallo | **corretto** |
| 8 Font: Bricolage Grotesque 800, Figtree, DM Mono | **corretto** (nessun altro font) |
| 9 Finale del kit 5 s con avviso diritti | **corretto** |
| 10 Struttura: sigla → presentazione → per argomento (titolo, prof, approfondimenti, pillola di ripasso, quiz da 5) → glossario → riepilogo → finale; verifica e compiti fuori; 50–60 min | **OK** (51:41,8). Gli «approfondimenti animati» restano a comparsa progressiva delle card (come nel montato) |
| 11 PDF A4 orizzontale: slide identiche al video + mappe del prof | **fatto**: `…_slide.pdf` **63 pagine** (ogni slide del video, senza riquadro e senza fascia; confronto fatto sul nuovo video: stesso testo, stesso ordine, stessa numerazione), `…_mappe.pdf` **1 pagina** (c'è solo la mappa del prof dell'arg. 4) |

## 4. Controlli sul video nuovo (A+B+C rifatti)
- `controllo_finale.py` del kit: durata 51:41,8 · fotogrammi 93 055 = attesi **OK** · 298,3 MB **OK** · 1920×1080 **OK** · parlato del prof **−16,2 LUFS OK** · sottotitoli: 880 blocchi, **0 sovrapposti, 0 oltre la fine**; «attacco sulla voce entro 0,3 s»: il controllo del kit dà 44 % su 16 campioni (pochi sono «verificabili»; i casi in difetto sono rumorini/«click» nei tratti di voce narrante). Nessuna cue cade su silenzio. Per le righe spezzate a metà frase il tempo è proporzionale e agganciato alla pausa più vicina: **stima ±0,5 s**, non misura.
- Trascrizione delle **giunzioni** (±2,5 s) di tutti i punti dove ho tolto le mappe: nessuna parola tagliata, nessun resto della voce delle mappe.
- 5 punti a caso + tutti i minuti cambiati guardati sul video nuovo (`controllo_minuti.jpg`, un fotogramma ogni 30 s).
- Freeze nel prof: 1 (problema 22). Nessun lampeggio (slide ferme, cambi senza flash; l'unica dissolvenza è sigla→copertina).

## 5. Domande per Sara (basta una riga di risposta)
1. **Mappe di arg. 1, 2, 3 e mappa finale**: del prof c'è solo quella dell'arg. 4. Le altre quattro le avevamo inventate e le ho **tolte** (regola «non inventarla»). Se le vuoi comunque, le rimetto.
2. Per la master: `t_verifica`/`t_compiti` nella scheda li ho messi a fine video perché le schede sono fuori dal video; se alla master servono altri valori me lo dice lei.

## 6. File consegnati
`Letteratura_Lez15_Parte1_1080p.mp4.parte_00…03` + `.sha256` · `Letteratura_Lez15_Parte1.vtt` · `Letteratura_Lez15_slide.pdf` · `Letteratura_Lez15_mappe.pdf` · `Quiz_Letteratura_Lez15.txt` + `quiz_argomenti.json` (controllati: 20 domande, risposte giuste) · `Verifica_finale_Letteratura_Lez15.xlsx` (10 domande, **identica** all'Excel del prof) · `compiti.json` · `scheda_pubblicazione.json` · `testo_youtube.txt` · `timeline.json` · `controllo_minuti.jpg` · questo rapporto.

## 7. Correzioni del 17/11 (aggiornamenti master 15:10, 01:20, 01:25, 01:30, 08:15)
Stessa durata (3101,8 s) e stessi fotogrammi (93 055) del giro precedente. Le slide sono state ridisegnate e il PDF slide (63 pagine) rifatto dalle stesse immagini.

| Richiesta | Esito |
|---|---|
| Font 15:10: «01 · ARGOMENTO», riga copertina, piè di pagina in **Figtree Bold maiuscolo spaziato** (non DM Mono) | **fatto** su tutte le slide e nel PDF; nessun carattere DM Mono rimasto (anche etichette di card, chip e numeri) |
| Ombre 01:30: sempre grigie e morbide, mai nere o «a blocco» | **fatto**: tolte tutte le ombre nette (card, schede, mappe, tabelle); riquadro prof e foto con ombra grigia sfocata |
| Card in corso: bordo giallo sottile, numero su pallino giallo, fondo bianco | **fatto** (lezione, ripassi, linee del tempo, schede opera, mappe); le altre card hanno bordo grigio chiaro |
| Jingle Quiz (01:20) | i suoni sono quelli del kit (`quiz.wav`, `titolo.wav`, `repaso.wav`, `trans.wav`). **Quiz: scatto a inizio scheda + 0,5 s, scarto misurato +0,004 / +0,003 / +0,005 / +0,004 s** (Q1–Q4, tolleranza 0,05): per Q3 e Q4 prima era −0,08/−0,12 e ho spostato l'inizio della scheda di 2 e 5 fotogrammi. `titolo.wav` già presente su tutti e 4 i titoli degli argomenti (corr. 0,96). **Aggiunti** `repaso.wav` sulle 4 schede «Ripasso» (mancava) e `trans.wav` (volume basso) sui passaggi alle schede Approfondimento, Glossario, Riepilogo, Fine |
| Transizioni (08:15) | dissolvenza da bianco di 0,33 s a ogni cambio di slide (non tra due pezzi del prof) + `trans.wav` come sopra. Niente taglio secco |
| Prof mai tagliato a metà frase (01:25) | **trovato e corretto**: il pezzo 2 finiva a 14:18 su «…il regime non sarebbe» (la parola «crollato.» stava nel pezzo 3). Ora il pezzo 2 finisce a «…il regime non sarebbe crollato.» (+1,3 s di prof, tolti dall'inizio del pezzo 3: durata invariata) |
| Mai immagine ferma del prof (08:15) | copertina/presentazione: il riquadro c'è solo con il prof che parla, in video vivo (copertina 0:15–0:41 senza riquadro). `freezedetect`: un solo fermo di 1,7 s a 31:16 (nell'**originale**: la finestra della webcam si sposta, il prof dice «mi sposto un poco più sopra») |
| Sincronia labbra/voce (08:15), max 0,04 s | misurata sull'audio originale in 3743 finestre da 2 s: scarto massimo dall'offset del pezzo **0,0004 / 0,0005 / 0,0004 / 0,0056 s** (pezzi 1–4), tutti < 0,04 s; i fotogrammi sono scelti con quegli offset (risoluzione 1/30 s = 0,033 s) |

**Fine e inizio di ogni pezzo del prof (01:25)** — minuti del video nuovo:
| Pezzo | Inizio | Prime parole | Fine | Ultime parole | Frase finita |
|---|---|---|---|---|---|
| D1 | 0:41,4 | «Buongiorno e benvenuti alla lezione che vedete dal titolo…» | 9:04,5 | «…E questo è il contesto storico. D'accordo, il contesto storico.» | **sì** |
| D2 | 12:30,4 | «Ora, giusto per ripassare, questo l'abbiamo comunque fatto anche in Storia…» | 14:19,5 | «…finché poi, con la guerra, il regime non sarebbe crollato.» | **sì** (prima: no) |
| D3 | 17:47,1 | «Ora, tutto questo giusto per farvi capire…» | 26:08,2 | «…non si può neanche, come dire, sospettare che tu lo pensi: devi stare attento.» | **sì** |
| D4 | 30:20,8 | «Il panorama letterario ne è travolto.» | 43:03,7 | «…per riflettere sulla società italiana dell'epoca, soprattutto durante la dittatura.» | **sì** |
Nessuna parola mozzata in partenza (inizi su pausa).

Il punto 2 e 3 del secondo messaggio della master («Cesare Pavese», picco −0,1 dB) riguardano un'altra lezione: qui il titolo è già «La narrativa tra le due guerre» e il picco è −2,3 dBTP.

## 8. Correzione del 17/11 (messaggio master 09:27, copertina)
Il fotogramma a 25 s (copertina) aveva ancora etichetta e piè di pagina in DM Mono: il pezzo sigla+copertina era rimasto in cache e non era stato ricodificato con le slide nuove. Ricodificato: ora «LETTERATURA ITALIANA V · VIDEOLEZIONE» e il piè di pagina sono in Figtree Bold, come nel resto della lezione (guardato il fotogramma a 25 s). Nient'altro cambiato.
Controlli sul video riconsegnato: 93 055 fotogrammi, 3101,8 s (invariati), **sha256 delle parti = sha256 del file** (`8a8cc8cf…`), −16,5 LUFS, picco −2,3 dBTP. Audio e sincronia non toccati: sono gli stessi dati del giro precedente (jingle Quiz +0,004 s, scarto sync prof ≤ 0,0056 s).
