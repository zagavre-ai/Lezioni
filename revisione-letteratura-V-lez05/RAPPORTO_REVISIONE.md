# RAPPORTO REVISIONE · Letteratura V · Lezione 5 · Giovanni Verga — 17/11, ore 09:00 (IT)

**ESITO: LEZIONE NON CONSEGNABILE COME «REVISIONATA».** Il video non è stato rifatto nel modello Spagnolo: in 1 ora non era possibile ricostruire un montaggio di 57 minuti (piano di ~100 pezzi, 134 slide del prof, fettine HD, ritaglio 4:3 dall'originale, voci). Consegno i file di contorno corretti e l'elenco preciso di ciò che manca. Stato: **IN REVISIONE**. Legenda: **M** misurato · **S** stima · **NV** non verificato.

## 1. Cosa è stato consegnato (cartella `revisione-letteratura-V-lez05/`)
| File | Stato |
|---|---|
| `Letteratura_Lez5_Parte1_1080p.mp4.parte_00…02` + `.sha256` | video **vecchio** (grafica invariata) con la sola **audio abbassata di 0,8 dB** per rientrare nel picco: −16,8 LUFS, picco −1,7 dBTP (M). Fotogrammi 102 532 = identici al montaggio precedente (M): quiz/verifica/compiti restano agli stessi secondi |
| `Letteratura_Lez5_Parte1.vtt` | **rifatto** dalla trascrizione automatica del video finale (1083 cue, max 2 righe, tempi dalla voce). **NON riletto da una persona**: la trascrizione ha ancora errori (es. «Foyer», «eopea»); applicato un piccolo dizionario (Zola, Dumas, Mastro-don Gesualdo, Verismo, Malavoglia). Il vecchio `.vtt` aveva errori gravi («Comentici pato», «cicolo dei vinti», «l'usooreietà») (M) |
| `Letteratura_Lez5_mappe.pdf` | mappa del prof (cartella `MAPPE`), A4 orizzontale, **non ridisegnata**: immagine del prof in cornice Telesio (titolo, piè di pagina). **Tolto il logo «MAPPE per la SCUOLA»** (marchio di terzi). ⚠ La mappa porta il marchio/sito di un editore terzo: **decide Sara se i diritti ne permettono l'uso** |
| `Letteratura_Lez5_verifica_finale.xlsx`, `verifica_finale.json` | 10 domande dell'Excel del prof, testo identico (M) |
| `compiti.json` | 4 esercizi dal PDF «LEZIONE 5» del prof, testo identico (M) |
| `scheda_pubblicazione.json` | titolo «Letteratura V · Lezione 5 · Giovanni Verga» |
| `quiz_argomenti.json`, `Quiz_Letteratura_Lez5.txt` | 5×5 domande, lette: risposte coerenti con la lezione (letto, non verificato con il prof) |
| `controllo/` | contact sheet, trascrizioni `.srt` del video e dell'originale |

## 2. Confronto col modello Spagnolo (punti 000)
| # | Esito |
|---|---|
| 1 sigla→copertina | NV (sigla c'è; dissolvenza non misurata) |
| 2 copertina | **NON corretta**: manca logo in alto a sinistra, riga «QUINTO ANNO», elenco a una colonna, niente card ARGOMENTI (M, fotogramma 0:30) |
| 3 slide | **NON corretta**: fondo grigio-azzurro, non bianco |
| 4 piè di pagina | **NON corretto**: ripasso/glossario hanno «Ripasso», «Glossario» al posto del numero pagina |
| 5 riquadro 4:3 | **NON corretto**: il prof è ancora nel tondo |
| 6 fascia gialla | **NON corretta**: assente |
| 7 slide senza prof | **NON corrette**: ripassi/glossario con onda audio decorativa non presente nel modello |
| 8 font | NV (etichette sembrano DM Mono; vanno in Figtree Bold) |
| 9 finale 5 s | NV: a 57:00 c'è un fotogramma nero con una linea, non identificato |
| 10 struttura | sigla, presentazione, 5 argomenti, ripassi, glossario, riepilogo presenti (M, a campione). Verifica/compiti fuori dal video: ora preparati |
| 11 PDF slide + mappe | mappe: fatto. **PDF slide: NON fatto** (richiede il video rifatto) |

## 3. Problemi trovati
| Minuto | Tipo | Com'era | Correzione |
|---|---|---|---|
| audio | audio | picco −1,0 dBTP (al limite) | −0,8 dB → −1,7 dBTP (M) |
| vtt | testo | 649 cue con errori gravi | rifatto (vedi §1), non riletto |
| fine | consegna | mancavano verifica, compiti, mappe | prodotti |
| tutto | visivo | punti 2–7 sopra | **NON corretti** |
| 18–52 | pagina | pagine intere del libro, rigo piccolo, QR dell'editore visibili | **NON corrette** (`Lez05_ingrandita.zip` scaricato, non usato) |
| silenzi > 3 s | audio | 10:34–10:47, 28:45–28:56, 33:24–33:34, 44:07–44:17, 54:18–54:26 | NV: probabilmente schede quiz; da ascoltare |

## 4. Pagine del libro in HD
**NON fatto.** Brani nella lezione: T3 Rosso Malpelo, T4 «I vinti e la fiumana del progresso», T5, T7, T8 (Malavoglia), T9 La roba, T10 Libertà, T12 (morte di Mastro-don Gesualdo). Nessuna tabella minuto→pagina→file prodotta.

## 5. COSA NON HO VERIFICATO
Ascolto vero (voce Kore: pronunce, frasi che nominano immagini, «ecco/guarda» a 1:05, 14:41, 19:43, 20:30, 28:56, 30:35, 35:13, 50:44); sincronia labbra/voce (scarto ≤ 0,04 s); fermi immagine del prof (`freezedetect`); **fine e inizio di ogni pezzo del prof** (tabella richiesta il 17/11 01:25); jingle quiz con `controllo_jingle.py` e transizioni; ombre grigie e card gialla; evidenziazioni dal parlato; fettine HD; OCR di tutte le slide; PDF slide; rimontaggio con voci R1, R2.
**DA CONFERMARE COL PROF:** la mappa dà «La Roba 1882», «La Lupa 1880», «Cavalleria rusticana 1880»: confrontare con slide e voce (non fatto).

## 6. Come ho verificato
Ricomposizione pezzi + sha256 (M); fotogrammi 1 ogni 30 s a campione e a 1/s estratti (non tutti guardati); trascrizione completa con `trascrivi.py` (video montato 636 segmenti, originale 547); `ebur128` per volume e picco (M); confronto Excel/PDF del prof con i file consegnati (M).

## 7. Prossimo passo (S)
Rifacimento completo nel modello (metodo lezione 3): ~4–5 ore su macchina con 4 CPU, partendo da `controllo/` (trascrizioni). Non si può comprimere in 1 ora senza abbassare la qualità.
