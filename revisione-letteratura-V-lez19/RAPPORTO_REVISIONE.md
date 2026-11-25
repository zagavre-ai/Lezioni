# RAPPORTO DI REVISIONE · Letteratura italiana V · Lezione 19 · «Dal secondo dopoguerra a oggi» (Prof. Giorgio Mazzotti)
**Correzioni 22/11/2026** · ramo `revisione-letteratura-V-lez19` · stato: REVISIONATA (da ricontrollare dalla master).
Etichette: **M** = misurato, **S** = stima o lettura a vista, **NV** = non verificato.

## 1. Cosa ho cambiato rispetto alla revisione del 17/11
| Regola 22/11 | Com'era | Com'è ora |
|---|---|---|
| Testo delle card a 40 px, interlinea 1,5 | 26–31 px | **40 px, interlinea 1,5** nelle slide con il prof; 36–40 px negli schemi, glossario, riepilogo, approfondimenti (titoli, etichette, piè di pagina invariati) |
| Al massimo 3 card, frasi intere, mai «…» né iniziale minuscola | 3–4 card piccole per slide | **2 card per pagina** (a 40 px tre frasi del prof non entrano: la slide si divide, mai rimpicciolita). Ogni card è una frase intera del prof. La pagina cambia quando il prof passa alla frase dopo; il pallino/bordo giallo si accende alla **prima parola** con cui il prof incomincia la frase (tempi dalla trascrizione, ±1 s); l'altra card resta attenuata. Le pagine hanno numero progressivo (1–56) |
| Nessuna schermata ferma oltre 3 min, nessuna card sola oltre 60 s | prima parte dell'argomento 1: 211 s con la stessa slide; ultima slide 200 s | **nessuna pagina oltre 153 s** (la copertina con l'introduzione; tutte le altre ≤ 145 s; misurato). Nei tratti in cui il prof parla in generale ho aggiunto slide fatte **con le sue frasi**: «Il secondo Novecento in Italia» (4 frasi, 2:07–5:35 del suo pezzo) e «Una carrellata per concludere» (2 frasi, ultime 100 s) |
| Mappa: una sola, del prof, colori BES, ramo per ramo con la voce | mappa del prof in stile blu/giallo | **mappa del prof ridisegnata nel modello BES approvato** (concetto centrale pesca; parole chiave paglierino; esempi e opere menta; legenda in alto a destra), testo 34–50 px, maiuscolo/minuscolo, **stesse parole e stesse frecce** del prof. Costruita **ramo per ramo** con la voce Kore RV5 (riquadro acceso in giallo finché la voce parla), mappa intera ferma 4 s alla fine. Una volta sola, prima del glossario. **La mappa del prof non ha marchio di terzi né foto dell'autore** (è un disegno suo a riquadri): niente da togliere |
| Verifica e compiti dentro il video, sigla finale | tolti il 17/11 | **reinseriti** come da regole blindate §3.4: Verifica finale (jingle a +0,5 s), «Fine della lezione» con voce, sigla finale del kit con avviso diritti, intro «Compiti» con jingle, scheda compiti. Nella scheda: `t_verifica` e `t_compiti` |
| Sigle rispiegate | «DC, PCI, PSI» e «tv» nelle nostre schede | nelle schede nostre scritto per esteso («Democrazia Cristiana, Partito Comunista e Partito Socialista», «televisioni private»); nella card del prof «Rai (Radiotelevisione italiana)»; sulla voce le sigle erano già per esteso |
| Dispense A4 | slide con prof, 31 pagine | **56 pagine identiche alle slide del video** (senza riquadro, fascia e evidenziazione), testo grande, **strato di testo invisibile** (selezionabile), copertina con **solo materia e titolo**, piè di pagina solo materia + «Pagina N». PDF mappe: copertina «MAPPE · Letteratura italiana V» + mappa |
| Nome del prof | nel piè di pagina e nella voce di introduzione | **solo nella fascia gialla**: piè di pagina «LETTERATURA ITALIANA V · Pagina N» (video e PDF), frase «il professor Giorgio Mazzotti ci guida…» tolta dalla voce di benvenuto |
| Sottotitoli | solo il prof | **anche le voci narranti** (743 cue, ≤ 2 righe, tempi ±0,3 s su 6 punti) |
| Pause | titoli argomento con pausa 2,56–2,76 s | schede titolo 2,9 s: nessuna pausa ≥ 2,5 s |
| Audio | già ok | invariato: parlato del prof −16 LUFS, picco −1,4 dBFS, nessuna pausa > 2,5 s. Le voci Kore **già fatte** sono riusate (RV1 senza i primi 16,45 s di istruzioni di regia, RV2, RV3, RV4, RV5, AN1a–d, AN2a, AN2c, AN2d, AN3a, R1–R3, S1–S3, GL1, RF1, FIN1) |

## 2. Esito del controllo severo (`controllo_severo.py`, M)
**ESITO: OK** · errori: nessuno.
Durata 50.35 min · copertina trovata con titolo completo, durata 140 s (≤ 180) · slide con lo stesso titolo oltre 3 min: 0 · schermate identiche oltre 3 min: 0 · card con «…»: 0 · card sole oltre 60 s: 0 · loudness -16.2 LUFS · pause > 2,5 s: 0 · voce: tono [148, 156, 152, 156, 145, 152] Hz, chiarezza [1377, 1224, 1403, 1271, 1428, 1309] Hz (nessun campione alterato).
La voce «DA GUARDARE» (card con iniziale minuscola, 29 campioni) è un **falso allarme del riconoscimento di testo**: ho guardato i fotogrammi (4:05, 7:25, 9:05, 26:05): le card cominciano con «Il…», «La…» in maiuscolo; il programma perde la prima parola corta.

## 3. Misure sul video finale (M)
| | |
|---|---|
| Durata | **50:20.77 (3020.77 s)** · fotogrammi **90623 = durata × 30** · peso **293.0 MB** (< 400) · 4 pezzi + `.sha256` (ricomposto e controllato) |
| Formato | 1920×1080, 30 fps, x264 veryfast CRF 19, AAC 192k 48 kHz |
| Volume | **-16.2 LUFS** integrati · picco vero **-1.5 dBTP** |
| Pause > 2,5 s | **nessuna** (fine file 2,45 s) |
| Fermi immagine del prof (`freezedetect` ≥ 1 s) | **0** nei 4 pezzi |
| Jingle Quiz (`controllo_jingle.py`) | Q1 +0,005 · Q2 +0,005 · Q3 +0,005 s (limite 0,05) |
| Audio prof vs originale | **−0,02 s** (12 punti, 3 per pezzo; un secondo controllo indipendente su 16 punti: −0,02 s) · video prof vs originale **0 fotogrammi** (misurato sulla versione precedente, stessi pezzi e stessa codifica) (energia di movimento, correlazione 0,98–0,99 dove il prof si muove) → scarto ≤ **0,02 s** (limite 0,04) |

## 4. Pezzi del prof: inizio e fine (M, dalla trascrizione dell'originale)
| Pezzo | Inizio nel video | Prime parole | Ultime 8 parole | Frase intera? |
|---|---|---|---|---|
| D0 | 0:40.07 | «Buongiorno e benvenuti alla lezione Dal secondo dopoguerra…» | «…c'è anche la parte di teatro. Bene, allora.» | **sì** |
| D1 | 2:46.70 | «Vediamo di dare delle coordinate storiche, ancora una…» | «…ruolo, come dico sempre, della persona è fondamentale.» | **sì** |
| D2 | 20:33.50 | «Quale tipo di poeta? quale tipo di letterato?» | «…vedete, [la corporeità] più totale, e Patrizia Valduga.» | **sì** |
| D3 | 33:53.53 | «I maestri della narrativa. C'è anche la narrativa,…» | «…costituiscono magari materiale già più. Come dire. D'esame.» | **sì** (fine dell'originale) |
I pezzi sono continui dall'originale (nessun taglio interno); ogni pezzo parte e finisce in una pausa (≥ 0,5 s dalla parola più vicina).

## 5. Cartelle di cambi card (dalla trascrizione, secondi sull'originale)
quadro 335,2 / 346,4 / 359,1 / 393,6 · bipolarismo 418,5 / 441,3 / 464,2 · trasformazioni 513,2 / 551,2 / 609,2 · media 659,2 / 702,2 / 725,2 · dibattito 804,2 / 825,2 / 842,2 · poesia 896,2 / 948,2 / 1027,2 / 1099,2 · narrativa 1: 1257,5 / 1297,2 / 1347,2 · narrativa 2: 1421,2 / 1486,2 / 1533,2 · saggistica 1581,5 / 1628,5 · chiusa 1681,2 / 1751,5 · contesto 152,8 / 189,8 / 237,8 / 301,8. Negli approfondimenti, schemi, glossario e mappa lo stato cambia all'inizio della frase della voce corrispondente.

## 6. Secondi nuovi (scheda, timeline.json)
| Elemento | Secondi |
|---|---|
| Argomento 1 / Quiz 1 | 163.8 / 1226.6 |
| Argomento 2 / Quiz 2 | 1230.6 / 2026.6 |
| Argomento 3 / Quiz 3 | 2030.6 / 2874.5 |
| Mappa del prof | 2878.5 |
| Verifica finale / Compiti | 3001.1 / 3014.3 |
| Durata | 3020.77 |
(`inizio_s` = inizio della scheda titolo − 0,35 s, come nelle consegne precedenti.) La master rigenera la pagina.

## 7. Voci (M)
Tutte le voci Kore usate sono state **trascritte** e lette parola per parola (numeri compresi): anni e numeri sono detti per esteso (1946, 1948, 1958, 1962, 1992, 1994, 2022, gruppo 63…). Le uniche correzioni di contenuto riguardano RV1 (tagliati i primi 16,45 s di regia letta per errore), RV2 («incapace di svelare», come dice il prof), RV3 («accensioni liriche»), RV4 («Donna in guerra»). Bordi delle voci: dissolvenza di 15 ms in entrata e uscita. **Non ho potuto ascoltare** le voci a orecchio (pronuncia di Mazzotti, Lampedusa, Céspedes, Ucrìa): la trascrizione le riporta giuste.

## 8. Refusi e sigle (regola 2.7)
Nessun refuso trovato nel testo delle slide del prof (22 pagine controllate). Interventi sulle nostre schede: sigle e abbreviazioni scritte per esteso (DC/PCI/PSI, tv, Rai) come al §1. «Covid» (nome comune) lasciato. Nessun numero che non torni.

## 9. Controllo indipendente (agente che non ha montato la lezione)
Un agente separato, che non ha montato la lezione, ha spuntato la lista del §11 su due giri (misure e fotogrammi, sola lettura).
**Primo giro** (video delle 18:00): 5 difetti, **tutti corretti**: (1) la voce di introduzione diceva «il professor Giorgio Mazzotti» → frase tolta (RV1 senza quella frase e senza le istruzioni di regia); (2) il nome del prof nel piè di pagina di video e PDF → tolto: piè di pagina «LETTERATURA ITALIANA V» e «Pagina N», nome solo nella fascia gialla; (3) sottotitoli solo sul prof → aggiunti i sottotitoli di tutte le voci narranti (743 cue); (4) 6 card accese in anticipo di 1–2,2 s → spostate sull'inizio della frase; (5) pause di 2,56 e 2,76 s ai titoli degli argomenti → schede titolo da 3,6 a 2,9 s. Inoltre: «Rai» ora spiegata anche nella scheda Parole chiave.
**Secondo giro** (video finale): i 5 punti sono **OK** (cambi card ≤ 0,04 s dalla frase; nessuna pausa ≥ 2,5 s; piè di pagina senza nome in 12 fotogrammi; sottotitoli entro ±0,3 s su 6 punti). Corretto anche il cue «fa croll i partiti».
Voci della lista che l'agente **ha confermato OK** al primo giro: nessun taglio a metà frase, nessuna pagina oltre 3 min (massimo 153 s), mappa unica del prof con colori BES e legenda, timbro della voce identico all'originale (rapporto alti/bassi −15,4…−19,7 dB, come l'originale), −16,2 LUFS / −1,4 dBTP, fotogrammi = durata × 30, nessun fermo del prof, timeline e scheda coerenti.
**Restano (non difetti secondo le regole, ma da sapere):** (a) la scheda «Verifica finale» e le schede «Compiti» nel video sono **schede di pausa** (come i Quiz): le 10 domande e i 4 compiti sono nei file `verifica_finale.json` e `compiti.json` e li mostra la pagina della lezione, come nelle altre lezioni; (b) il fondo delle slide risulta #FDFDFD alla misura (compressione del video; il CSS è #FFFFFF); (c) un taglio di sottotitolo: «Sveu» corretto in «Svevo»; restano approssimazioni del riconoscimento sul parlato colloquiale del prof.


## 10. Cosa NON ho verificato
- **Ascolto a orecchio** (rumore, ronzio, «metallico», pronuncia delle voci): non possibile qui; ho solo le misure (volume, picco, tono e chiarezza della voce nel controllo severo).
- **Sincronia delle labbra a vista** (misurata solo sull'audio e sull'energia di movimento).
- Ogni cambio card: controllato a campione nel controllo indipendente, non uno per uno.
- La foto di Eco e Maraini sull'ultima slide originale del prof non è nei materiali disponibili (manca il `_videodispensa.pptx`) e non uso foto prese altrove: nel video c'è la slide di chiusura con le sue frasi.
- Riquadro del prof: la webcam originale è 247×139 px, ingrandita ×2,2 per il 4:3: più morbida del modello e la testa tocca il bordo alto già nell'originale.

## 11. File consegnati
`Letteratura_Lez19_Parte1_1080p.mp4.parte_00…03` + `.sha256`, `Letteratura_Lez19_Parte1.vtt` (455 cue), `Letteratura_Lez19_slide.pdf`, `Letteratura_Lez19_mappe.pdf`, `timeline.json`, `scheda_pubblicazione.json`, `quiz_argomenti.json`, `Quiz_Letteratura_Lez19.txt`, `Test_Letteratura_Lez19.xlsx` (= Excel del prof), `verifica_finale.json`, `compiti.json` (4 compiti del prof), `testo_youtube.txt`, `controllo_minuti.jpg`, questo rapporto. Voci nuove: nessuna.

## 12. Controllo del 25/11/2026 · riquadro del docente (segnalati 5:46, 13:16, 23:33, 36:53)
- **Video non modificato** (stesso sha256 della consegna del 22/11, durata 3020,77 s invariata). Non ho ricodificato perché **il difetto non è presente nel file consegnato**.
- **M** Riquadro (412×309 a x=1428, y=148) analizzato a 4 fotogrammi al secondo su tutti i pezzi D0–D3 del docente: mai vuoto (deviazione standard minima 8–23 solo sul primo fotogramma di ogni pezzo, dissolvenza). Ai minuti 5:46, 13:16, 23:33, 36:53 (±6 s, un fotogramma ogni 2 s) il docente è visibile e parla.
- **M** Movimento del riquadro confrontato con la webcam dell'originale (release `mazzotti-letteratura-V`, `Letteratura_Lez19.mp4`, 1775,13 s = somma dei 4 pezzi): correlazione 0,88 (D1), 0,72 (D2), 0,83 (D3); le finestre basse stanno ai bordi dei pezzi e dove il docente sta fermo. Nessun tratto senza docente.
- **M** `controllo_rapido.py`: ESITO OK (foglio e json in questa cartella).
- **NV** Non ho potuto vedere la copia vista da chi ha segnalato il difetto (Vimeo, altro lettore, altra versione del 17/11). Se il riquadro appare vuoto là, il file caricato non è questo: confrontare l'sha256.
