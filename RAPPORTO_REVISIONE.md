# RAPPORTO DI REVISIONE · Letteratura italiana V · Lezione 15 · La narrativa tra le due guerre
Prof. Giorgio Mazzotti · chat di revisione (16/11/2026) · **VERSIONE 1 (prima ora): verifica fatta, correzione in corso**

## 1. Che cosa ho verificato e come
- **Video montato** (consegna-letteratura-V-lez15): pezzi ricomposti, **sha256 uguale** (OK). 1920×1080, 30 fps, **55:24,6**, 99 737 fotogrammi.
- **Audio:** trascrizione completa del parlato (Whisper small, italiano) + `silencedetect` + `loudnorm` (misurati).
- **Visione:** 111 fotogrammi (uno ogni 30 s) + **164 stati di slide** trovati col rilevamento dei cambi, ognuno letto con OCR. Confrontato con il modello `kit/modello_spagnolo/`.
- **Testo:** .vtt, dispensa PDF, quiz, verifica (.xlsx), compiti, scheda, testo YouTube letti e confrontati con il materiale del prof (release `mazzotti-letteratura-V`: Excel, PDF compiti, mappa).
- **Non posso verificare all'ascolto** (non ho orecchie): fruscio/ronzio/«metallico». Misuro solo livelli (LUFS, picco). Scritto qui perché sia chiaro.

## 2. Problemi trovati (tabella)
| Minuto | Tipo | Com'era | Come lo correggo |
|---|---|---|---|
| tutta la lezione | visivo | Prof nel **tondo** (diametro ~250 px) con scritta «Prof. Giorgio Mazzotti» piccola sotto; **niente fascia gialla** | riquadro **4:3 (410×308, x1428 y146), ombra grigia morbida**, fascia gialla −3° su due righe, dal video originale con correzione immagine del kit |
| tutta la lezione | visivo | Fondo grigio-azzurro, **tre stili diversi** nella stessa lezione (slide, approfondimenti, ripassi), testo piccolo e metà schermo vuoto, piè di pagina con «Introduzione/Ripasso/Approfondimento» invece di «Pagina N» | tutte le slide rifatte **identiche a Spagnolo** (fondo bianco, label DM Mono, titolo Bricolage 800 + barretta, card/tabelle, piè «LETTERATURA ITALIANA V · Prof. Giorgio Mazzotti» + «Pagina N») |
| 0:15 | visivo | Dalla sigla (nero) alla copertina (bianco) c'è un **taglio netto**: lampo | dissolvenza di 1 s |
| 0:15–0:38 | visivo | Copertina senza il prof | resta senza prof (parla la voce di benvenuto); il prof entra a 0:41 come da audio |
| 17:07–19:20 (circa) | testo | **«venticinque luglio 1940tré»** sulla slide di ripasso (anche nella dispensa, p. 2) | «25 luglio 1943» |
| 13:10–13:18 | visivo/audio | Ripasso arg. 1: la voce legge la 4ª frase («marcia su Roma») ma sullo schermo non c'è | frase 4 sulla slide |
| 0:15–0:37, 12:30–13:17, 18:31–19:24, 32:11–33:00, 51:40–55:00 (ripassi, benvenuto, glossario, riepilogo, congedo) | testo | **Sottotitoli mancanti** per ~6 minuti di voce narrante (il .vtt ha 741 righe ma niente in questi tratti) | .vtt rifatto su tutta la voce |
| 55:00–55:24 | struttura | Dopo «Fine della lezione» ci sono le schede «Verifica finale» e «Compiti» **dopo** il «GRAZIE» (ordine sbagliato) e il finale non è quello del kit (manca l'avviso dei diritti) | tolte dal video (verifica e compiti stanno fuori, regola 10); finale = `Sigla_finale_5s_con_avviso_diritti.mp4` |
| mappe 11:35, 17:35, 31:16, 51:00, 52:30 | contenuto | **Mappe concettuali inventate da noi** (arg. 1, 2, 3 e mappa finale) e anche quella dell'arg. 4 con parole chiave («crisi, inettitudine, Meridione…») che nella mappa del prof **non ci sono**. La mappa del prof (`LEZIONE 15.pdf`, release `MAPPE`) è **una sola** e riguarda solo l'argomento 4 | arg. 4: **mappa del prof**, testo identico, nella nostra grafica (voce nuova). Arg. 1–3 e finale: *non inventate* → tolte (regola «non inventarla») — **decisione per Sara qui sotto** |
| audio | audio | volume −16,29 LUFS (OK) ma **picco vero +0,63 dBTP** (limite −1) | limitatore a −1,5 dBTP |
| consegna | testo | `compiti.json` nel formato sbagliato (lista di stringhe) | `{"titolo":…,"esercizi":[{"n":1,"tipo":"aperta","testo":…}]}`, testo identico al PDF del prof |
| consegna | testo | scheda_pubblicazione: titolo «La narrativa tra le due guerre · Parte 1» | «Letteratura V · Lezione 15 · La narrativa tra le due guerre» |
| consegna | testo | «Dispensa» PDF e «Mappe» PDF non sono le slide del video né le mappe del prof | `…_slide.pdf` (pagine = slide del video, A4 orizzontale) e `…_mappe.pdf` (mappa del prof) |
| consegna | testo | testo_youtube: titolo con «Parte 1», capitoli da rifare con i nuovi tempi | rifatto |

## 3. Domande per Sara (rispondi con una riga)
1. **Mappe di arg. 1, 2, 3 e mappa finale**: non esistono mappe del prof (c'è solo quella dell'arg. 4). Per regola non si inventano: le ho **tolte** (tagliando la voce narrante, mai il prof). Se invece vuoi tenere le nostre, dimmelo e le rimetto.
2. Le «schede» di approfondimento (Tozzi, Alvaro, Silone, Buzzati) e le «parole chiave» sono scritte da noi sul materiale del prof; non ho trovato niente di non detto dal prof nei punti che ho controllato, ma non ho potuto controllare ogni dettaglio (es. «Sauze d'Oulx → Salice d'Ulzio»).

## 4. Piano di correzione e tempi (stima)
1. Slide nuove (riquadro 4:3 + grafica Spagnolo): 40 min (in corso).
2. Montaggio dal video originale del prof, allineato sull'audio (misurato: i 4 pezzi del prof coprono tutto l'originale, 1876 s): 40 min.
3. Voce nuova per la mappa dell'arg. 4 (testi inviati alla master su `voci-letteratura-V-lez15`): 30 min di attesa, intanto lavoro sul resto.
4. Sottotitoli, PDF, compiti, scheda, controlli: 60 min.
Consegna prevista entro le 4 ore.
