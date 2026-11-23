# Controllo separato · Storia V · La rivoluzione russa (Parte 1 e Parte 2)

Controllore: sessione separata, che non ha montato la lezione. Nessun file modificato. Voci Kore nuove (18 provvisorie, sintesi robotica): non segnalate come difetto. Non lanciato `controllo_severo.py`.

## 1. Fine e inizio di ogni pezzo D del prof
Metodo: tempi sorgente ricostruiti da `piano.py` (`cut_in`/`cut_out`/`intervals`); ultime parole trascritte con ASR (Parakeet) direttamente sull'audio del video finale, ultimi 9 s di ogni pezzo; ampiezza (rms 10 ms) degli ultimi 300 ms.

| Pezzo | Fine nel finale | Ultime parole (ASR sul finale) | Frase finita |
|---|---|---|---|
| D0 | P1 2:02.8 | «...Quindi capite che la situazione è molto complicata. Perciò facciamo un passo indietro.» | sì |
| D0b | P1 3:35.9 | «...dal punto di vista storico, comprendere gli eventi.» | sì |
| D1 | P1 9:20.8 | «...avvertita come insufficiente la struttura politica, e quindi esplode, esplode la rivoluzione.» | sì |
| D2 | P1 20:17.0 | «...i socialisti rivoluzionari, che adesso, di cui adesso parleremo.» | sì (frase sintatticamente spezzata dal prof stesso, ma finisce nella sua pausa) |
| D3 | P1 30:39.6 | «...il colpo finale ad ottobre sarà esattamente quello che accadrà.» | sì |
| D4 | P1 35:53.4 | «...Kornilov viene fermato e anche arrestato.» | sì |
| D4b | P1 42:13.1 | «...presieduto da Lenin.» | sì |
| D5 | P2 5:53.4 | «...Dal trattato di Brest-Litovsk in avanti.» (ultimi 9 fotogrammi silenziati: la «E» che segue non entra) | sì |
| D6 | P2 13:56.4 | «...uno dei pochi territori che riescono a riconquistare.» | sì |
| D7 | P2 17:45.8 | «...a tratti a torto, a tratti a ragione, se ci pensate.» (taglio sorgente 2876.35, voce riprende 2876.44: margine 0,09 s invece di 0,15) | sì |
| D8 | P2 23:48.5 | «...perché venne salvato da elementi, appunto, di proto o para capitalismo.» | sì |
| D9 | P2 30:29.4 | «...dopo Lenin se sarà Stalin o Trockij a succedere, appunto, al grande rivoluzionario.» | sì |

Inizi: tutti su inizio di frase (D0 «Buongiorno e benvenuti», D1 «Andiamo quindi», D2 «La crisi precipitò», D3 «Ora, la Russia», D4 «Vediamo gli ulteriori passaggi», D4b «Quindi siamo nell'estate», D5 «Il nuovo governo», D6 «Vediamo che cosa accade», D7 «Per far fronte», D8 «La combinazione tra i dissesti», D9 «Sul piano istituzionale»). D7/D8 si sovrappongono di 0,31 s nel sorgente, ma dentro il silenzio 2875,95-2876,40: nessuna parola ripetuta. Esito: OK.

## 2. Timbro (energia >4 kHz meno energia >100 Hz, finestre da 4096 campioni, soglia rms 0,01)
Finale vs originale sugli stessi intervalli sorgente.

| | finale | originale |
|---|---|---|
| Parte 1 | -16,9 dB | -17,1 dB |
| Parte 2 | -16,9 dB | -17,0 dB |
| per pezzo | da -15,7 (D0) a -17,9 (D2) | da -15,8 a -18,1 |

Tutti entro -9 / -20 dB; scarto dall'originale ≤0,2 dB. OK.

## 3. Sincronismo (cross-correlazione audio finale vs originale, 24 finestre da 8 s su 12 pezzi D; 6 finestre video)
- Audio: scarto costante -25 ms (da -24,3 a -25,6 ms) in tutte le 24 finestre, correlazione 0,92-0,95. Origine: `prof_clean.wav` è 25 ms in ritardo sull'originale (verificato su 4 punti).
- Video (movimento del riquadro vs `cam4x3.mp4`): 0 fotogrammi in D0, D5, D7, D9; -1 fotogramma (33 ms, video in ritardo) in D1 e D3.
- Scarto netto audio-labbra: 8-25 ms, entro 0,04 s. OK, ma margine ridotto (25 ms su 40) dove il video è a 0 ritardo.

## 4. Fermo immagine del prof
`freezedetect n=-60dB d=0.5` sul riquadro 412x308 a x=1428,y=148 su tutto il video: nessun fermo ≥0,5 s dentro i pezzi D (i fermi trovati sono solo nelle schede senza riquadro). OK. (Il crop a 309 px di altezza non è accettato dal codec, ho usato 308.)

## 5. Card accese e frase in corso
Tutti gli eventi di accensione confrontati con la trascrizione (card = testo della slide del prof). Dieci verificati anche sul fotogramma (accensione a ±0,6 s):

| Minuto finale | Card accesa | Frase del prof in quel punto | Esito |
|---|---|---|---|
| P1 6:39.6 | autoritarismo di Nicola II | «La debolezza del regime zarista...» (376,1) | OK |
| P1 13:55.7 | crollo del regime zarista | «Però come si comportano le forze armate inviate?» (664,0) | OK |
| P1 25:13.3 | contrasto sulla guerra | «Il principale elemento di divergenza... la prima guerra mondiale» (1232,4) | OK |
| P1 33:38.2 | golpe di Kornilov | «...tentativo di un colpo di Stato» (1663,5) | OK |
| P1 41:39.0 | Consiglio dei commissari | «I menscevichi e i socialisti rivoluzionari abbandonarono...» (2084,5) | OK |
| P2 2:48.8 | emancipazione femminile | «E poi le riforme sociali e di genere. La nuova costituzione...» (2198,0) | OK |
| P2 10:51.8 | uccisione della famiglia reale | «Ora, nel corso della guerra civile... la famiglia imperiale» (2578,3) | OK |
| P2 16:59.7 | resistenza contadina | «Quindi il comunismo di guerra provocò l'immediata opposizione del mondo contadino» (2830,0) | OK |
| P2 22:38.8 | pilastri della NEP | «i punti principali della NEP compresero l'abolizione delle requisizioni» (3081,6) | OK |
| P2 26:22.0 | struttura federale apparente | «Perché repubbliche socialiste... sovietiche» (3175,0) | OK |

Nota minore: P2 19:13 (D8, card 1 «Bilancio demografico») si accende all'inizio del pezzo, quando il prof parla di carestia e crollo della produzione; le cifre sui morti le dice 22 s dopo (2898,7). Accettabile, ma non esattamente «inizio frase».
Schermata identica più lunga nei pezzi D (tra due cambi di stato): 138 s (D4b, P1 39:20) < 180 s. OK. Al massimo 3 card per slide, card intere (il testo è la slide del prof, titolo in grassetto + frase), testo ≈36 px a 1080p. OK.

## 6. Riquadro, nomi, numeri, fondo
- BENV1, BENV2, RIP2 e tutte le schede animate (AN, MAP, P, Q, T, GL, RIEP, FIN, VERIFICA, COMPITI, CO1): campionati 2 fotogrammi ciascuno (contact sheet): nessun riquadro del prof. Il riquadro compare solo nei pezzi D, compreso D0 (copertina con il prof che parla) e D0b. OK.
- Nome del docente: nel codice compare solo nella fascia gialla (`prof_box`, usata solo nelle slide D e nella carta di Brest-Litovsk). Testi delle voci nuove senza nome; i vecchi testi con «professor Mazzotti» (B0, B2, MD*) sono sostituiti da B0_R2, B2_R2, MP*. OK (la sostituzione dell'audio effettivo non è stata ascoltata: NON VERIFICABILE sulle voci provvisorie).
- Numero di lezione: assente in video, PDF, .vtt, schede. «STORIA V» in piè di pagina è la materia indicata dal master (annotato: la «V» potrebbe essere letta come numero, ma è il nome della materia).
- Fondo: sorgente (255,255,255); nel video decodificato 253 per la conversione a range limitato. Non è un difetto. Il fondo dei riquadri card è (247,249,253), azzurrino leggero.

## 7. Misure tecniche
| | Parte 1 | Parte 2 |
|---|---|---|
| Durata | 2749,867 s (45:50) | 2111,933 s (35:12) |
| Fotogrammi | 82496 = 2749,867×30 OK | 63358 = 2111,933×30 OK |
| Video | h264 High, 1920×1080, 30 fps, x264 crf 19, veryfast | idem |
| Audio | AAC LC 48 kHz, 2 canali, 189 kb/s | 186 kb/s |
| Peso | 263.086.187 B (251 MB) | 203.629.265 B (194 MB) |
| Loudness integrata | -16,0 LUFS | -16,1 LUFS |
| Picco campione | -2,0 dBFS | -2,6 dBFS |
| LRA | 5,9 LU | 5,9 LU |

Tutto OK (picco true-peak non misurato separatamente, il picco campione è ≤ -2 dBFS). Scatto jingle `quiz.wav` (cross-correlazione): scarto 0,000 s in Q1-Q9 e nella scheda VERIFICA. Mappe: ferma a mappa completa per 3,9 s + 0,3 s di dissolvenza (MAP2, MAP6, MAP8); MAP4 ferma 5,4 s (freezedetect).
Durata delle Parti: 45,8 e 35,2 min, entrambe sotto i 50 minuti (vedi difetti).

## 8. PDF
| Controllo | Esito |
|---|---|
| `Storia_Lez5_slide.pdf`: 35 pagine A4 orizzontale, copertina «STORIA · VIDEOLEZIONE / La rivoluzione russa» + piè di pagina «STORIA V / Pagina 1» | OK: solo materia e titolo, niente nome del docente né numero lezione |
| Nome del docente / «Mazzotti» / «Giorgio» nel testo dei due PDF | assente OK |
| Strato di testo invisibile (render mode `3 Tr`, pdftotext 2830 parole) | presente OK |
| Numerazione pagine uguale al video (es. pag. 6, 18, 20, 24, 29, 31 coincidono) | OK |
| Pagina 35 (carta «La nascita dell'Unione Sovietica (1922)») | DIFETTO minore: nessun testo leggibile da sintesi vocale (immagine, né didascalia né parole chiave); pag. 34 analoga |
| Dispensa identica al video | DIFETTO minore: nel PDF non c'è né il riquadro del prof né la fascia gialla, e la composizione cambia (card a tutta larghezza, tutte non accese, parole chiave a destra); copertina del PDF senza elenco argomenti (voluto da §9) |
| `Storia_Lez5_mappe.pdf`: 5 pagine, copertina con «MAPPE» + materia + titolo; piè «STORIA V / MAPPE» | OK |
| Mappe vettoriali | OK: testo con font incorporati (Figtree, Bricolage), unica immagine per pagina = logo 330×104 |
| Mappe = quelle del prof (struttura, frecce, parole): confrontate con mappa-1..4.png | OK; il prof scrive i titoli dei riquadri in maiuscolo, qui maiuscolo/minuscolo come da regola; legenda a 5 colori in alto a destra |

## 9. Sottotitoli
- `.vtt` valido (WEBVTT, UTF-8 senza BOM): Parte 1 = 1092 cue, Parte 2 = 733 cue. Massimo 2 righe (nessun cue a 3 righe), massimo 42 caratteri per riga, nessuna sovrapposizione (inizio successivo ≥ fine precedente), tempi crescenti, ultima fine entro la durata. OK.
- DIFETTO: cue del prof con errori di trascrizione (termini non corretti sul materiale del docente):

| # | Minuto | Cue | Dovrebbe essere |
|---|---|---|---|
| 1 | P1 7:55.6 | «Grigorij Rash Putin» | Grigorij Rasputin |
| 2 | P1 7:57.8 | «Putin,» | Rasputin |
| 3 | P1 8:37.9 | «Bash Putin fu infine assassinato nel / dicembre millenoventosedici» | Rasputin; «millenovecentosedici» (o 1916) |
| 4 | P1 14:01.5 | «dallo Zar a» | zar (minuscolo, come nel resto) |
| 5 | P1 14:14.5 | «Un matatoio.» | un mattatoio |
| 6 | P1 18:26.2 | «alla Duma e al principe il Boff.» | principe L'vov |
| 7 | P1 26:58.1 | «Vladimir / Iliciulianov,» | Vladimir Il'ič Ul'janov (come nella slide del prof) |
| 8 | P1 34:13.7 | «quell'Einin» | Lenin |
| 9 | P2 2:55.7 e 3:06.1 | «San C.» / «San C l'uguaglianza» | sancisce / sancì (verificare sul docente) |
| 10 | P2 8:22.0 | «vasi territori» | vasti territori |
| 11 | P2 12:37.2 | «recruvescenza» | recrudescenza |
| 12 | P2 17:26.0 | «spreio dello sforzo» | spregio |

  Altri da ricontrollare: «Ceka» (P2 5:08) contro «Čeka» in `verifica_finale.json`; «Brest Litovsk» senza trattino (P2 1:39.8) contro «Brest-Litovsk» altrove; «Lvov» (P1 20:56, P2 0:54) contro «L'vov» (P1 18:05, slide); «Kronstadt» (P2 20:24; slide e mappa «Kronstadt», quiz e verifica ugualmente, ma il prof/slide in russo sarebbe «Kronštadt»: coerente, lasciare alla master); «Putin» a P1 3:29 «nella Russia di Putin» è invece detto davvero dal prof.

## 10. Altri difetti trovati
- `quiz_argomenti.json` Q8: titolo «La Nuova Politica Economica (Nuova politica economica)», e testi «con la Nuova politica economica»; `verifica_finale.json` domanda 8, risposta sbagliata «Nuova politica economica (Nuova politica economica)» (nell'Excel del prof: «Nuova politica economica (NEP)»); `compiti.json` esercizio 4 «(Nuova politica economica)» ripetuta. La sostituzione automatica della sigla ha prodotto un doppione. Nel video le schede Q8 e Compiti mostrano «(NEP)» e sono corrette: il difetto è nei JSON.
- Quiz e verifica nel video sono solo schede titolo (Q = 4,7 s, VERIFICA = 11 s, «10 domande · serve almeno l'80%»): le domande stanno solo nei JSON. Se l'interazione con soglia 80% non è aggiunta altrove, la regola «verifica dentro il video» non è soddisfatta: NON VERIFICABILE da qui. `scheda_pubblicazione_Parte2.json` non contiene i tempi di verifica e compiti (solo argomenti e quiz).
- Spiegone RIP2 (P2 0:24-1:26, 61 s): inizia con una card sola «Bentornato.» su schermo quasi vuoto; le mappe e l'immagine sono miniature illeggibili (circa 190×100 px a 1080p); compare un riquadro blu «febbraio 1917» che sembra un segnaposto al posto di un'immagine. Il testo copre i 4 argomenti, ma «Ripassiamo insieme la prima parte» ha solo 1 mappa su 4 ben visibile. DIFETTO minore rispetto a «con le immagini e le mappe di quella Parte».
- Parti più corte di 50 minuti: 45:50 e 35:12 (totale 81 min). Chiudere la Parte 1 dopo l'argomento 5 darebbe circa 51+29 min. Decisione della master.
- Gli approfondimenti AN sono tutti solo testo (nessuna immagine ad alta risoluzione né opere): coerente con «solo materiale del docente» ma poco intrattenimento; segnalato come osservazione.
- D2 termina con la frase spezzata dal prof stesso («adesso di cui adesso parleremo»): taglio corretto, solo da tenere presente.

## 11. Lista di controllo §11
| Punto | Esito |
|---|---|
| Nessun taglio a metà frase del docente | OK (tabella §1) |
| Voce del docente non alterata: timbro -9/-20 dB | OK: -16,9 dB in entrambe le Parti |
| Labbra e voce entro 0,04 s; nessun fermo del prof | OK (25 ms di ritardo audio, nessun fermo ≥0,5 s) |
| Nessuna schermata identica oltre 3 minuti | OK (massimo 138 s nei D) |
| Card intere, max 3, bordo giallo all'inizio frase (10 punti) | OK |
| Mappe del docente, colori BES con legenda, ramo per ramo | OK; ferme 3,9-5,4 s alla fine |
| Ogni sigla rispiegata; niente «già visto» | PARZIALE: sigle rispiegate nelle slide (NEP, URSS, Ceka, Politburo); doppione «Nuova politica economica (Nuova politica economica)» nei JSON; «già visto» non verificato a tappeto, a campione nessun ripetuto |
| Glossario; quiz da 5 domande con scatto a 0,0 s; verifica e compiti dentro il video | Glossario OK; quiz 5 domande nei JSON, scatto 0,000 s OK; verifica e compiti: schede presenti (compiti con le 4 domande in video, 61 s), domande della verifica NON VERIFICABILE nel video |
| Voci intere: trascritte, numeri giusti, bordi <0,03 | NON VERIFICABILE (voci nuove provvisorie) |
| Copertina con titolo esatto; intro del docente ≤3 min; nessun titolo sotto il riquadro | OK: copertina «La rivoluzione russa», D0 = 97,7 s sulla copertina, poi D0b sugli argomenti; titoli lunghi su 2 righe |
| Parti dopo la prima aperte dallo spiegone | OK, con i difetti di forma in §10 |
| -16 LUFS ±1; fotogrammi = durata×30; peso <400 MB | OK |
| Nessun numero di lezione, nome di programma, fondo bianco | OK |
| Nessun riquadro del prof (nemmeno vuoto) in intro animata; nome mai detto o scritto nelle animazioni | OK (campioni 2 per pezzo; voci nuove non ascoltate) |
| Immagini alta risoluzione; nomi stranieri nella loro lingua e pronunciati bene | NON VERIFICABILE per la pronuncia; ortografia incoerente (§9: Lvov/L'vov, Ceka/Čeka, «Brest Litovsk») |
| PDF dispensa e mappe: copertina con solo materia e titolo (+MAPPE) | OK |
| Dispensa identica al video con testo invisibile; sottotitoli sul video finale | Testo invisibile OK; dispensa non identica (manca riquadro/fascia); sottotitoli: formato OK, 12+ errori di termini (§9) |
| Il rapporto dice cosa è stato verificato e cosa no | Questo documento; NON verificato: pronuncia e ortografia a voce delle voci Kore, ascolto di tutto il parlato, true-peak, lettura a schermo di tutte le schede (campione di 2 fotogrammi per scheda), sincronismo oltre le 24 finestre |
