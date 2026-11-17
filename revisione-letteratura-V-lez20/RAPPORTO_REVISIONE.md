# RAPPORTO REVISIONE · Letteratura italiana V · Lezione 20 · Carlo Emilio Gadda · VERSIONE 2 (17/11/2026)
Sostituisce la versione del 16/11 (che aveva **un errore grave nell'audio del prof**, vedi § 3). **Misurato** = misurato con uno strumento; **stima** = dedotto; **non verificato** = non ho potuto.

## 1. Misure sul video nuovo (misurato)
| Controllo | Risultato |
|---|---|
| Formato | 1920×1080, 30 fps, x264 veryfast CRF 19, AAC 192k 48 kHz |
| Durata | **47:43,6 (2863,6 s) = 85 909 fotogrammi** (prima 54:50). La durata è cambiata come deciso da Sara (mappe nostre tolte, silenzi tolti, tagli del prof a fine frase). **È sotto i 50 minuti della regola del 7/11**: da decidere |
| Peso | 175,5 MB (167,4 MiB) |
| Scatto dei quiz | `controllo_jingle.py`: Q1–Q6 a **0,000 s** |
| Volume | −16,8 LUFS integrato; parlato del prof (mediana pezzi D) −16,6 LUFS; picco **−1,2 dBTP** (`ebur128=peak=true`) |
| Fermi immagine del prof | nessuno (`controllo_finale.py`, soglia 1 s) |
| Silenzi ≥ 2,5 s (silencedetect −45 dB) | **uno solo**: 47:20,6–47:23,6 (3,0 s) fra la scheda «Verifica finale» e la sigla finale |
| Sincronia labbra/voce (pezzi del prof) | scarto audio-finale vs audio dell'originale, 3 punti per pezzo (inizio/metà/fine): **−10 … −15 ms** su tutti e 7 i pezzi (correlazione dell'inviluppo, punteggio 0,77–0,95). Limite 0,04 s: OK. Video e audio vengono dallo stesso file e dallo stesso intervallo |
| Sottotitoli | 686 blocchi, max 2 righe da 42 caratteri, nessuna sovrapposizione. `controllo_finale.py`: attacco entro 0,3 s **70 % di 23 blocchi → «DA GUARDARE» (soglia 80 %)** |
| PDF | slide: 58 pagine A4 orizzontale (senza riquadro e fascia) · mappe: 1 pagina (la mappa del prof) |

## 2. Aggiornamenti di oggi applicati
- **Mappe solo del prof:** tolte le 7 mappe nostre e le loro voci; nel video c'è la mappa del prof (`MAPPE/LEZIONE 20.pdf`) a 44:57, impaginata nella nostra grafica, con la voce nuova **R1** (44,7 s, generata dalla master) e le caselle che compaiono in sincronia con la voce (stima dai tempi della trascrizione di R1). Contenuto identico alla mappa del prof.
- **Silenzi > 3 s e code vuote** tolti: ogni scheda finisce 1 s dopo l'ultima parola della voce.
- **Jingle come Spagnolo** (`kit/.../snd`): `titolo.wav` sulle 6 schede titolo d'argomento, `repaso.wav` sui 6 ripassi, `quiz.wav` sulle 6 schede Quiz (e sulla Verifica finale), `titolo.wav` sulla scheda Compiti, `finale.wav` sulla scheda finale dei compiti, `trans.wav` su ogni transizione.
- **Transizioni:** dissolvenza di 1,3–1,6 s fra tutti i pezzi (45 transizioni) col suono `trans.wav`, mai taglio secco. Verso/da i pezzi del prof la dissolvenza usa la slide **senza riquadro**: il prof compare solo quando parla (nessuna immagine ferma del prof).
- **Card «in corso»:** bordo giallo sottile + numero su pallino giallo, fondo bianco; altre card bordo grigio chiaro. Ombre sempre grigie e morbide (anche riquadro del prof e foto). Controllato su slide, ripassi, schede opera, mappa, PDF.
- **Font:** Figtree Bold (etichette, «01 · ARGOMENTO», piè di pagina, copertina); titoli lunghi a capo su due righe e mai sotto il riquadro del prof (misurato: titolo max 1290 px, riquadro da 1428 px).
- **Prof mai tagliato a metà frase:** tabella § 5.

## 3. Problemi trovati e correzioni (oltre a quelli della versione del 16/11)
| Minuto | Tipo | Com'era | Correzione |
|---|---|---|---|
| tutto il prof | **audio** | **errore mio nella v1:** l'audio del prof era scritto a 192 kHz e letto come 48 kHz → parlato sbagliato nei pezzi del prof (non me ne ero accorto: misuravo solo volume e jingle) | rifatto a 48 kHz; sincronia misurata (§ 1) |
| 6:56 (v1) | audio | taglio dentro la frase «segnata da profondi \| avvenimenti luttuosi» | il pezzo 1 finisce a fine frase (orig. 360,3 s) |
| 25:16 (v1) | audio | taglio dentro la frase «il primo grande \| lavoro … è sicuramente La cognizione del dolore» | il pezzo 3 finisce a fine frase (orig. 904,7 s) |
| 5 cuciture | audio | frasi ripetute di 0,5–1,5 s | nessuna: pezzi contigui, **velocità 1,0 (niente più variazioni di ritmo)** |
| 7 mappe | testo | mappe nostre | mappa del prof + R1 |
| 12 punti | audio | silenzi 3,0–3,9 s fra voci narranti | tolti |
| sottotitoli | testo | (v1) | rifatti sui nuovi tempi; mappe nostre tolte; aggiunta la voce R1 |
| scheda | testo | durate | `scheda_pubblicazione.json` aggiornata (inizio_s, quiz_s, durata_s, t_verifica, t_compiti) |

Tabella **secondo vecchio → secondo nuovo** (durata 3290.37 → 2863.63 s):
| Pezzo | vecchio (s) | nuovo (s) |
|---|---|---|
| T1 | 112.4 | 113.1 |
| Q1 | 688.6 | 624.4 |
| T2 | 693.9 | 629.7 |
| Q2 | 1350.3 | 1218.8 |
| T3 | 1355.6 | 1224.1 |
| Q3 | 1708.1 | 1513.6 |
| T4 | 1713.4 | 1518.9 |
| Q4 | 2143.2 | 1873.7 |
| T5 | 2148.5 | 1879.0 |
| Q5 | 2450.4 | 2124.8 |
| T6 | 2455.7 | 2130.1 |
| Q6 | 3048.4 | 2652.7 |
| GL1 | 3132.6 | 2705.9 |
| RF1 | 3190.5 | 2763.7 |
| VER | 3265.3 | 2838.5 |
| COMP | 3284.1 | 2857.3 |

## 4. Consegne
Video a pezzi + sha256 · `.vtt` · `…_slide.pdf` · `…_mappe.pdf` · `quiz_argomenti.json` · `Quiz_Letteratura_Lez20.txt` · `verifica_finale.json` + xlsx (10 domande del prof) · `compiti.json` (4, identici al PDF del prof) · `scheda_pubblicazione.json` · `testo_youtube.txt` · `timeline.json` · `controllo_minuti.jpg` · `sync_labbra.json`. Pagine del libro: nessuna in questa lezione.

## 5. Pezzi del prof: inizio e fine (misurato dalla trascrizione dell'originale)
| Pezzo | inizio (min) | fine (min) | prime parole | ultime parole | frase finita |
|---|---|---|---|---|---|
| D0 | 0:54 | 1:52 | «Buongiorno a tutti e benvenuti alla lezione su Carlo Emilio Gadda» | «…una fotografia di Carlo Emilio Gadda.» | sì |
| D1 | 1:58 | 7:00 | «Vediamo nella vita.» | «…segnata da profondi avvenimenti luttuosi.» | sì |
| D2 | 10:35 | 16:51 | «Ecco, vediamo però la poetica gaddiana…» | «…primo dopoguerra. Allora, il Giornale di guerra e di prigionia.» | sì (enunciato completo che annuncia il tema) |
| D3 | 20:29 | 23:17 | «Andiamo pure su quest'altra slide, il Giornale appunto di guerra e di prigionia…» | «…è sicuramente La cognizione del dolore.» | sì |
| D4 | 25:24 | 29:07 | «Pubblicato inizialmente a puntate, i famosi romanzi a puntate.» | «…della mediocrità del mondo.» | sì |
| D5 | 31:24 | 33:41 | «Altre opere: L'Adalgisa, Eros e Priapo…» | «…ma anche di incredibilmente polemico.» | sì |
| D6 | 35:35 | 40:07 | «Bene, il giallo filosofico, Quer pasticciaccio brutto de via Merulana.» | «…il contenuto e le modalità che abbiamo delineato.» | sì (fine della registrazione) |
Nessuna parola mozzata in partenza: ogni attacco cade in una pausa (minimo di energia, ≥ 0,4 s).

## 6. Cosa NON ho verificato / limiti
- **Ascolto umano: nessuno.** Fruscio/ronzio/«metallico»: non verificato. Voce **R1**: nella trascrizione risulta «la Dal Gisa» e «brutto **di** via Merulana» (R1 e altre voci Kore): se all'ascolto è sbagliato, serve rigenerarla. Altre voci sospette già elencate nella v1: «il docente» (≈ 18:07), «gattiano», «Mar Adal», «de via».
- **Sottotitoli:** sincronia sotto soglia (70 %); dubbi sul testo del prof (v1, § 5): vedi elenco. Da controllare a occhio.
- **Evidenziazioni** dei pezzi del prof: dalla trascrizione, stima ±1,5 s. Caselle della mappa del prof: stima dai tempi di R1.
- **Foto di Gadda** (ritaglio dal video del prof, bassa risoluzione) e webcam 246×137 px ingrandita 2,25×: morbida; capelli al bordo già nell'originale. Slide originali (.pptx) della lezione 20 non nella release.
- **Durata 47:44** sotto i 50 minuti: dopo le decisioni di Sara sulle mappe e sui silenzi.
- Controllo di identità PDF slide/video: stessi modelli HTML, **non** confronto pixel per pixel.
- **Date:** La meccanica: il prof dice «1924-28», schede e voce «1924». Nessun'altra discordanza.
