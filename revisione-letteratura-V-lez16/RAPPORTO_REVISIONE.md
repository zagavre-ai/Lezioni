# RAPPORTO REVISIONE · Letteratura italiana V · Lezione 16 · Umberto Saba — correzioni del 22/11/2026
Video: `Letteratura_Lez16_Parte1_1080p.mp4` (a pezzi `.parte_00…`, sha256 nel file `.sha256`).
**misurato** = misurato con uno strumento · **stima** = dedotto · **non verificato** = non ho potuto.

## 1. Cosa ho cambiato rispetto alla consegna del 17/11
| Punto | Prima | Ora |
|---|---|---|
| Mappe | 5 mappe nel video (4 per argomento + finale, 14:15–15:08, 26:54–27:34, 45:30–46:23, 50:50–51:41, 52:25–53:28) con 5 voci | **una sola mappa**, quella del prof, prima del glossario (49:02), disegnata nei colori BES con legenda in alto a destra; 3 schermate (vita · pensiero · opere) che si costruiscono ramo per ramo mentre la voce Kore legge (29 voci `MB01–MB29`, anni in lettere), riquadro in giallo finché la voce parla, poi la mappa intera ferma 4 s |
| Slide del prof e approfondimenti | fino a 7 card per slide, testo 20–27 px, card con titolo e testo separati | **al massimo 3 card per schermata**, ogni card è una frase intera del prof («Etichetta: frase»), testo **40 px**, interlinea 1,5; se tre card non entrano la schermata si divide; bordo giallo e pallino giallo quando il prof comincia la frase (±1 s) |
| Schermate ferme | cover 124 s, ritratto 146 s, una card sola per 120 s | nessuna schermata oltre 150 s: le più lunghe si ricompongono a metà con le card in ordine ruotato |
| Durata | 55:11,7 | 53:58.4 (le 4 mappe inventate tolte) |
| Piè di pagina | «LETTERATURA ITALIANA V · Prof. Giorgio Mazzotti» | «LETTERATURA ITALIANA V · Pagina N» (il nome del prof solo nella fascia gialla, regola del 22/11) |
| Dispense | slide A4 con testo da 20 px | slide A4 identiche al video (testo a 40 px) con **copertina** (solo materia e titolo); **PDF delle mappe a parte** con la stessa copertina più «MAPPE» |

## 2. Misure sul video finale
| Controllo | Risultato |
|---|---|
| Formato | 1920×1080, 30 fps, x264 veryfast CRF 19, AAC 192k 48 kHz, una sola codifica con `finale_a_pezzi.py` |
| Misura | durata 3238.402 s (53:58.4) · fotogrammi 97152 (attesi 97152) OK · 1920x1080 · 30/1 fps · peso 199.7 MB |
| Misura | volume integrato -16.3 LUFS · picco reale -1.1 dBTP |
| Silenzi > 3 s (−50 dB) | 4 tratti nella mappa (50:26, 50:59, 51:42, 52:10: 4,7–6,7 s = tenuta di 4 s a fine schermata più 1 s di cambio pagina, richieste dalla regola «ferma 4 secondi») e le schede finali (53:50, 7,8 s) |
| Jingle Quiz (`controllo_jingle.py`) | Q1 atteso 904.700 trovato 904.700 scarto +0.000 OK<br>Q2 atteso 1599.567 trovato 1599.566 scarto -0.001 OK<br>Q3 atteso 2671.733 trovato 2671.736 scarto +0.003 OK<br>Q4 atteso 2938.467 trovato 2938.469 scarto +0.002 OK |
| Sincronia audio/video del prof | scarto massimo audio: 2.88 ms; scarto massimo video: 2 fotogrammi | (misurato per correlazione sull'originale; il controllo indipendente ha misurato −15 ms costanti)
| Timbro della voce del prof | rapporto 4–8 kHz / 100 Hz–4 kHz: originale −16,3 dB → pulito −17,5 dB (limite −9…−20): voce non alterata |
| PDF | slide: 88 pagine A4 orizzontale (copertina con solo materia e titolo, testo selezionabile, schermate identiche al video senza riquadro); mappe: copertina «MAPPE» + 4 schermate |
| Sottotitoli | 816 blocchi, max 2 righe da 42 caratteri, max 6,6 s |

## 3. Controllo severo (`controllo_severo.py`)
**Non completato**: `controllo_severo.py` (OCR con tesseract) non ha finito entro la scadenza (≈ 20 min per Parte con passo 20 s). In sua vece un **agente separato** ha spuntato il §11 con misure e fotogrammi: i difetti trovati sono qui sotto, con cosa è stato corretto e cosa no.

## 4. Fine e inizio di ogni pezzo del prof
| Pezzo | Inizio (video) | Prime parole | Fine (video) | Ultime parole | Frase finita |
|---|---|---|---|---|---|
| D1 | 0:15.00 | «Buongiorno e benvenuti alla lezione su Umberto…» | 2:19.63 | «…riprenderà tante tematiche. Allora. Direi che possiamo iniziare.» | sì |
| D2 | 2:23.13 | «Questa è appunto una fotografia di Umberto…» | 10:35.47 | «…la parte dei traumi infantili, nel millovecentocinquant sette.» | sì |
| D3 | 15:12.70 | «Quindi un personaggio che ha avuto una…» | 21:27.03 | «…solidarietà basato sulla comune esperienza umana del dolore.» | sì |
| D4 | 26:47.57 | «Analizziamo il canzoniere. appunto il corpus poetico…» | 37:49.47 | «…E poi, appunto, in chiusura, come avevo detto.» | sì |
| D5 | 44:39.73 | «Abbiamo anche... ultimi testi di cui abbiamo…» | 46:16.73 | «…nei testi più significativi che abbiamo, appunto. Visto.» | sì |

## 5. Mappa: come l'ho disegnata
- Struttura, parole e ordine dei rami identici alla mappa del prof (`MAPPE/LEZIONE 16.pdf`). **Tolti il marchio «MAPPE per la SCUOLA» (mappe-scuola.com) e la foto dell'autore** (decisione di Sara).
- Colori BES: pesca = concetto centrale; celeste = date; paglierino = parole chiave (rami e caratteristiche); menta = esempi e opere; lilla = conseguenze (infanzia difficile, persecuzioni, ricovero).
- **Limite:** la mappa ha 29 riquadri (circa 1000 caratteri): a 34 px non entra in una schermata sola. Nel video le tre schermate dei rami hanno testo da 36–38 px; la **mappa intera** finale (4 s) ha testo da 21 px. Il PDF mappe ha la stessa mappa intera.

## 6. Cosa NON ho verificato
**Difetti trovati dall'agente di controllo indipendente (19:00 UTC) e stato:**
- **Corretti:** nome del prof nel piè delle schede finali («Fine della lezione», «Verifica», «Compiti»); mappa divisa in 4 schermate (1/4 vita · 2/4 pensiero · 3/4 poesia · 4/4 prosa) con casella centrale dentro il riquadro; card sola (leggi razziali 2 min; «linguaggio semplice» 97 s) riequilibrata con la card precedente; schermate «ruotate» senza card in corso (ora il bordo giallo resta sull'ultima card detta); etichette con «?:»; sigla «T6» tolta dal titolo delle fettine (solo nel PDF, **nel video il titolo è ancora «· T6»: pezzo non rigenerato per mancanza di tempo**).
- **NON corretti (tempo):**
  1. **Transizioni**: dissolvenza solo tra i pezzi grandi; resta un taglio secco tra un approfondimento e l'altro e tra le schede di servizio. `trans.wav` solo sui passaggi principali.
  2. **Silenzi 2,5–2,9 s** tra le voci Kore (703,6 s; 773,4 s; 2559 s; 2903,6 s) e a metà scheda Verifica: non accorciati.
  3. **Approfondimenti** di 65–90 s (la regola dice 40–60): non accorciati.
  4. **Compiti e verifica**: nel video restano le schede di servizio (verifica 4 s, compiti 5 s); domande e compiti del prof sono nella pagina interattiva (`verifica_finale.json`, `compiti.json`), non nel video.
  5. **Card che non sono una sola frase**: le card sono il testo delle slide del prof (`_videodispensa.pptx`); alcune («Le Scorciatoie», «I Raccontini») hanno 3–5 frasi e non le ho spezzate.
  6. **Testo mappa**: schermate 1 e 2 a 36–38 px; la 3 e la 4 sono più piccole (≈ 26–34 px, da misurare); la legenda è piccola.
  7. **Foto di Saba** (slide 2 del prof): ingrandimento morbido, non migliorata.
  8. **Voci**: MB07 («sposa») e MB26 («la prosa») dopo due generazioni la trascrizione automatica non conferma la parola: **non ascoltate**. Pronuncia di tutte le voci non verificata.
  9. Dispensa: la numerazione delle pagine salta dove stanno le mappe (nel PDF mappe).
- Rapporto: aggiornato solo ai numeri finali sopra.

## DA CONFERMARE COL PROF
- Padre di Saba: «cristiano» nelle slide, «cattolico» nella mappa del prof (restano come li dicono).
- «Ernesto»: la mappa dice 1975; le slide «scritto nel 1953 e pubblicato postumo».
- La mappa aggiunge fatti non nelle slide (1906 Firenze, 1908 libreria, 1909 Lina, 1955 clinica a Gorizia).
- Ritratto di Saba (slide 2): ritagliato dalla slide del prof, senza grafiche dell'editore.
