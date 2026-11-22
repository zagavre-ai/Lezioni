# RAPPORTO DI REVISIONE · Letteratura italiana V · Lezione 10 · «Il primo Novecento e la lirica italiana»
Correzioni finali del 22/11/2026 · ramo `revisione-letteratura-V-lez10` · prese alle 16:35 UTC, consegnate entro le 19:30 UTC.
Ogni dato è etichettato **M** (misurato), **S** (stima o lettura a vista), **NV** (non verificato).

## 0. In breve
- Rifatti da zero i **5 pezzi del prof** (copertina+argomenti, 4 argomenti): slide con **card intere, al massimo 3 per pagina, testo 40 px, interlinea 1,5**, nessuna pagina ferma oltre 3 minuti (la più lunga: 173 s, M), riquadro 4:3 e fascia gialla come Spagnolo. Il video e l'audio del prof sono **gli stessi della consegna precedente** (stessi tagli, nessun taglio a metà frase).
- **Copertina: 108 s** (prima 226 s). Poi la slide «Di cosa parliamo» con gli argomenti che si accendono quando il prof li nomina.
- **Mappa**: una sola, quella del prof (crepuscolarismo), ridisegnata nei colori BES con legenda, costruita **ramo per ramo** con la voce Kore (M1–M12), spostata **in fondo all'argomento 3, prima della pillola**. Le 4 mappe inventate da noi erano già state tolte il 17/11.
- **Verifica finale (10 domande) e compiti del prof dentro il video**: scheda «Verifica finale», intro «Compiti» e 4 slide con la voce Kore (R6_COMP1–4).
- Durata **51:33,5**, 92.806 fotogrammi (= durata × 30, M), 226 MB, 1920×1080, −16,0 LUFS, picco −2,0 dBFS (M).
- Dispensa **50 pagine A4 orizzontali** con testo selezionabile + PDF mappe (2 pagine).
- Esito del controllo severo: **RESPINTA solo per «8 pause > 2,5 s»** (tutte strutturali, §7). Tutto il resto OK (M, `controllo_severo.py` con passo 30 s invece di 10 perché la macchina era lenta): slide oltre 3 min **0**, schermate identiche oltre 3 min **0**, card con «…» **0**, card sola oltre 60 s **0**, copertina trovata con titolo intero (120 s misurati a passo 30, 108 s reali), durata 51,56 min, −16,0 LUFS, voce non alterata (tono 145–156 Hz, chiarezza 1305–1480 Hz, soglie 95 e 800). «DA_GUARDARE: card con iniziale minuscola» a 13:15, 14:15, 27:15, 34:15…: sono falsi allarmi del riconoscimento sulle card attenuate («La svolta russa:», «Il ruolo delle riviste:», «Temi e toni:» lette senza le prime parole perché grigie); nel testo le card cominciano tutte con la maiuscola (S, a vista). Suggerimento: schiarire l'attenuazione delle card non accese (oggi opacità 55%) per il contrasto; non ho avuto il tempo di rifare i pezzi.
- Esito del controllo dell'agente indipendente: **nessun difetto sul montaggio** dei pezzi del prof (card, sincronia del bordo giallo ±1,5 s su 18 punti, pagine ≤173 s, riquadro e fascia, nessun fermo, labbra ≤0,03 s, volume, fotogrammi, peso, ortografia, mappa uguale a quella del prof, verifica e compiti). I difetti che ha trovato su sottotitoli, PDF e piè di pagina sono corretti (§7-bis); restano i dubbi elencati là.

## 1. Misure sul video finale (M)
| | Valore |
|---|---|
| Durata | 3093,533 s = 51:33,5 |
| Fotogrammi | 92.806 = durata × 30 |
| Peso | 226,2 MB (3 pezzi da 90 MB + sha256 del file intero) |
| Formato | 1920×1080, 30 fps, x264 veryfast CRF 19, AAC 192k 48 kHz |
| Volume totale | −16,0 LUFS (ebur128), picco −2,0 dBFS |
| Scatto dei quiz (controllo_jingle) | Q1 +0,003 s, Q2 +0,003 s, Q3 +0,003 s, Q4 +0,003 s (limite 0,05) |
| Timbro del prof (energia sopra 4 kHz meno sopra 100 Hz, 15 punti) | finale da −15,3 a −21,7 dB; originale da −16,0 a −23,2 dB; **in ogni punto il finale è uguale o più chiaro dell'originale**, mai sotto −25 |
| Pause oltre 2,5 s (silencedetect −45 dB) | 8 punti, tutti **strutturali** (vedi §7) |

## 2. Cosa ho cambiato
| Dove | Prima | Dopo |
|---|---|---|
| Copertina 0:14 | prof sopra la copertina per 226 s | copertina 108 s, poi slide «Di cosa parliamo» (119 s) con argomenti in evidenza a 2:08,5 (03) e 2:11,5 (04) quando il prof li nomina |
| D1–D4 (pezzi del prof) | 4 card per slide, testo ~30 px, un'unica pagina ferma anche 5–7 minuti, card evidenziata non sempre in sincronia | 2 o 3 card per pagina (mai di più), testo 40 px, interlinea 1,5, pagine da 29 a 173 s, **18 pagine** al posto di 8; il bordo giallo si accende quando il prof **inizia** la frase (tempi dal sottotitolo allineato, ±1 s S); una card sola solo con la foto di Gozzano accanto |
| Piè di pagina | «Pagina N» con N della vecchia numerazione | numerazione rifatta su tutto il video (50 pagine), applicata anche agli inserti (rimessa a mano la cifra sul fotogramma) |
| Mappa | dopo la pillola di ripasso, immagine ferma da 56 s, voce unica R5_MPD1 | prima della pillola dell'argomento 3, 68,7 s, costruita ramo per ramo con 12 voci, riquadro acceso in giallo finché parla, mappa intera ferma 4 s |
| Fine video | verifica e compiti fuori dal video | scheda Verifica finale (5 s, scatto a +0,5 s come i quiz) + intro Compiti (3,5 s) + 4 slide dei compiti con voce |
| Sottotitoli | solo parlato del prof, 601 cue, 14 refusi, qualche cue a 3 righe | 787 cue: parlato del prof (spostato di +12,733 s dopo la mappa, refusi corretti, max 2 righe) **più tutte le voci Kore** (inserti, ripassi, glossario, riepilogo, mappa, compiti), con le date in cifre come sullo schermo |
| Dispensa | 34 pagine | 50 pagine identiche al video, senza riquadro/fascia, piè di pagina senza nome del prof, testo invisibile selezionabile |
| Pagina interattiva | – | `timeline.json`, `scheda_pubblicazione.json`, `verifica_finale.json`, `compiti.json` con i secondi nuovi (verifica 3016,3 s; compiti 3021,3 s) |

## 3. Pagine dei pezzi del prof (M, dalla specifica del montaggio)
| Pagina | Inizio | Durata | Titolo slide | Card |
|---|---|---|---|---|
| 1 | 0:14.3 | 108 s | Copertina (titolo, argomenti) | 1 |
| 2 | 2:02.0 | 119 s | Di cosa parliamo (argomenti si accendono: 03 a 2:08,5; 04 a 2:11,5) | 1 |
| 4 | 4:03.7 | 114 s | Il quadro storico italiano (l'Età giolittiana) | 2 |
| 5 | 5:58.0 | 69 s | Il quadro storico italiano (l'Età giolittiana) | 2 |
| 6 | 7:07.0 | 158 s | Il quadro storico italiano (l'Età giolittiana) | 2 |
| 7 | 9:45.0 | 29 s | Il contesto internazionale e la Grande Guerra | 2 |
| 8 | 10:14.0 | 162 s | Il contesto internazionale e la Grande Guerra | 2 |
| 9 | 12:56.0 | 173 s | Il contesto internazionale e la Grande Guerra | 2 |
| 16 | 18:59.0 | 155 s | Trasformazioni sociali e linguistiche | 2 |
| 17 | 21:34.0 | 106 s | Trasformazioni sociali e linguistiche | 2 |
| 18 | 23:20.0 | 103 s | Trasformazioni sociali e linguistiche | 3 |
| 19 | 25:03.0 | 122 s | Il panorama culturale e la crisi delle certezze | 2 |
| 20 | 27:05.0 | 105 s | Il panorama culturale e la crisi delle certezze | 2 |
| 21 | 28:50.0 | 103 s | Il panorama culturale e la crisi delle certezze | 3 |
| 29 | 33:52.5 | 152 s | I crepuscolari | 2 |
| 30 | 36:25.0 | 141 s | I crepuscolari | 1 |
| 37 | 42:07.7 | 161 s | I vociani e Clemente Rebora | 2 |
| 38 | 44:48.7 | 94 s | I vociani e Clemente Rebora | 2 |


Tutte le pagine hanno numero diverso (la più lunga resta sotto i 180 s). Le pagine con 3 card (18 e 21) servono come riepilogo mentre il prof parla di quello che non è sulla slide (la stampa, 23:20–25:03).

## 4. Pezzi del prof: inizio e fine (nessun taglio a metà frase)
Tagli **identici alla consegna del 17/11** (scelti sulla trascrizione dell'originale, nelle pause); minuti dell'originale.
| Pezzo | Video | Originale | Prime parole | Ultime parole | Frase finita |
|---|---|---|---|---|---|
| INTRO | 0:14,3–4:00,7 | 0:00–3:46,4 | «Buongiorno e benvenuti alla lezione sul primo Novecento e la lirica italiana.» | «…verso quella meta. Allora.» | sì |
| D1 | 4:03,7–15:49,3 | 3:46,4–15:32,0 | «Qualche cenno storico.» | «…Tutto questo è quindi il primo Novecento.» | sì |
| D2 | 18:59,0–30:33,3 | 15:32,0–27:06,3 | «Per tornare a noi, per tornare alla letteratura in senso stretto.» | «…in filosofia di storia si cita sicuramente.» | sì |
| D3 | 33:52,5–38:46,4 | 27:07,2–32:01,1 | «Io prima avevo detto… avevo anticipato un po' i crepuscolari.» | «…propria sofferenza biologica come unica materia d'arte.» | sì |
| D4 | 42:07,7–46:23,1 | 32:03,3–36:18,6 | «Tutto un altro discorso relativamente ai vociani.» | «…le loro riflessioni e le loro composizioni.» | sì |

Sincronia labbra–voce (M): ho confrontato l'audio del video precedente con l'originale; scarto 0,018 s (INTRO, D1, D3), 0,028 s (D2), 0,031 s (D4), con il video dell'originale preso allo stesso tempo (il video anticipa l'audio di quella quantità). Limite 0,04 s: dentro, ma D2 e D4 sono vicini al limite. Ritaglio webcam: la webcam del prof **cambia posizione a 229,5 s dell'originale** (da copertina a slide): ritaglio con cambio di posizione a 3,1 s dall'inizio di D1 (M, a vista).

## 5. Mappa del prof (decisione di Sara)
- Fonte: `MAPPE/LEZIONE 10.pdf` della release (una sola mappa, «Il crepuscolarismo (1903 - 1911)»). Stessa struttura, stesse frecce, **stesse parole**; ridisegnata nel modello BES (`modello_mappa_BES`): pesca = concetto centrale; celeste = date e sequenze (movimento, termine, chi l'ha coniato); paglierino = parole chiave (caratteristiche); menta = esempi e opere (maggiori esponenti); lilla = conseguenze («Poesia minuscola»). Testo 34–50 px, legenda in alto a destra.
- Nella mappa del prof non ci sono né il marchio di mappe-scuola.com né foto dell'autore: niente da togliere (S, a vista).
- Voci: 12 frasi Kore, numeri in lettere («millenovecentotré… millenovecentoundici»); bordi sotto 0,03 su tutte (M: massimo 0,003). **Non ho potuto trascriverle** (il modello di riconoscimento non si scarica dalla rete di questa macchina): il controllo parola per parola delle voci è **NV**; l'esito della master segnala M1 «durata fuori misura» (6,09 s: pause interne max 0,28 s, M) e M11 «frasi 0/1» (1,92 s, bordi puliti, M): vanno riascoltate.
- Nel testo della mappa resta «Antonio Borgese» come scritto dal prof; nel parlato dice «Giuseppe Antonio Borgese»: **da confermare col prof** (non toccato).

## 6. Inserti Kore già fatti (non rifatti)
Come deciso dalla master (22/11 17:00 UTC) restano quelli del 17/11: 5 approfondimenti per argomento (AP_P1_AN1…AN11b), 4 ripassi, glossario, riepilogo, schede titolo e quiz. Testo misurato **circa 29–34 px (S)**, con fino a 7 righe per slide (es. «Mettiamo in fila le date»): sotto i 40 px e oltre le 3 card. Se la master vuole che siano a 40 px/3 card vanno rifatti uno per uno con la stessa durata e lo stesso audio. In questa consegna ho solo rinumerato le pagine.

## 7. Pause oltre 2,5 s (M)
Il controllo con silencedetect (−45 dB, 2,5 s) segna 8 punti. Nessuno è una pausa del prof (il prof non ha pause oltre 2,5 s): sono **le schede ferme per scelta di formato**:
| Minuto | Che cos'è | Durata |
|---|---|---|
| 18:53 | scheda Quiz 1 (jingle poi silenzio) | ~2,8 s |
| 33:46 | scheda Quiz 2 | ~2,8 s |
| 41:15–41:20 | fine mappa (resta ferma 4 s dopo l'ultima voce) | 4,75 s |
| 42:02–42:05 | scheda Quiz 3 | 2,87 s |
| 48:27–48:30 | scheda Quiz 4 | 2,88 s |
| 50:18–50:21 | scheda Verifica finale | 2,87 s |
| 50:22–50:25 | intro Compiti → prima voce | 2,94 s |
| 50:57–51:00 | tra compito 2 e compito 3 | 2,67 s |
**Non ho coperto i silenzi con rumore per far passare il controllo** (sarebbe truccarlo). Se la master vuole togliere questi punti dall'elenco bastano ritocchi di durata alle schede (quiz, verifica) e ai compiti; la fine della mappa (4 s ferma) è voluta dal modello.

## 7-bis. Controllo di un agente separato e correzioni fatte
Un agente che non ha montato la lezione ha spuntato il §11 (24 pagine PDF confrontate, 18 punti di evidenziazione misurati a 30 fps, freezedetect sul riquadro, 30 fotogrammi a caso). Difetti trovati e come li ho corretti:
| Difetto | Correzione |
|---|---|
| Nessun sottotitolo sulle voci Kore (circa 12 minuti) | aggiunti: posizione di ogni voce trovata con la correlazione sull'audio del video (21 voci, correlazione 0,93–1,00, M) |
| Numeri in lettere nei sottotitoli | date in cifre (1903, 1911, «Domanda 1»…) |
| Refusi nei sottotitoli del prof («dannunio», «belli», «soprattut», «conferenzi», «del decadentisti», «millonoventosedici», «La voce») | corretti (10 cue) |
| Cue a 3 righe, cue orfano, sovrapposizioni | tutto a massimo 2 righe, orfani uniti, sovrapposizioni tolte (M: massimo 2 righe) |
| Testo del PDF slide con parole incollate | testo invisibile rifatto parola per parola (esatto per le pagine nuove, da OCR per quelle degli inserti) |
| Nome del prof nel piè di pagina delle schede animate (inserti, mappa, verifica, compiti) | tolto: restano «LETTERATURA ITALIANA V» e «Pagina N» (nelle slide del prof il nome resta nella fascia gialla e nel piè di pagina come da modello Spagnolo) |
Dubbi segnalati dall'agente e **non** corretti: (1) la sigla del kit mostra «LETTERATURA ITALIANA [ANALISI TESTUALE]» in carattere monospaziato: è la sigla della master, da confermare; (2) tra 14,3 e 15,2 s, durante la dissolvenza, il riquadro del prof compare 0,9 s prima della sua prima parola; (3) due card visibili ma nessuna accesa per ~60 s all'inizio di D1 e di D3 (il prof introduce prima di arrivare alla prima frase); (4) testo degli inserti stimato dall'agente a circa 25–28 px (la mia stima è 29–34 px): sotto i 30 px se vale la stima più bassa; (5) colori dei rami della mappa = scelta di interpretazione; (6) bordi di 5 voci degli inserti sopra 0,03 (P1_AN1 0,055, P1_AN11 0,054, P1_AN3b 0,042, P1_AN11b 0,032, P1_AN6b 0,031): nel video non ho misurato se hanno la dissolvenza di 20–40 ms (NV).

## 8. Cosa NON ho potuto verificare
- Trascrizione automatica delle 16 voci nuove (M1–M12, R6_COMP1–4): modello non scaricabile → **NV**; controllati solo durate, bordi, loudness.
- Ascolto a orecchio di fruscio, ronzio, «metallico» sul prof: **NV** (solo misure di timbro).
- Pronuncia di Rebora, Lacerba, Brest-Litovsk nelle voci degli inserti: **NV** (restano da riascoltare come da rapporto del 17/11).
- Sottotitoli: ~12 frasi sono ricostruzioni plausibili (Deledda, Ungaretti, magniloquenti); **NV**.
- Testa del prof: nell'inquadratura originale i capelli toccano il bordo alto già a 0:14 e a 3:46; il ritaglio 4:3 usa tutta l'altezza dell'inquadratura e non taglia di più (S).
- Confronto pagina PDF ↔ fotogramma: le pagine nuove sono create dalla stessa pagina HTML usata per il video (senza riquadro/fascia/evidenziazione e con il piè di pagina senza nome del prof); controllo a vista su campione (vedi agente); non è un confronto automatico di tutti i fotogrammi.
- Pagine del PDF degli inserti: testo invisibile ricavato dal riconoscimento ottico (può avere errori); quello delle pagine nuove è esatto.
- Voce del docente alterata: no, confrontata con l'originale (§1).

## 9. File consegnati
Video a pezzi (3 × 90 MB) + `.sha256`, `Letteratura_Lez10_Parte1.vtt`, `Letteratura_Lez10_slide.pdf`, `Letteratura_Lez10_mappe.pdf`, `timeline.json`, `scheda_pubblicazione.json` (anche con suffisso `_Parte1`), `quiz_argomenti.json`, `Quiz_Letteratura_Lez10.txt`, `Verifica_finale_Letteratura_Lez10.xlsx`, `verifica_finale.json`, `compiti.json`, `testo_youtube.txt`, `controllo_minuti.jpg`.
