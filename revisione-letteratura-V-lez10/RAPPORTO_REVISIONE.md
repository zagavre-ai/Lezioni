# RAPPORTO DI REVISIONE · Letteratura italiana V · Lezione 10 · «Il primo Novecento e la lirica italiana» (Prof. Giorgio Mazzotti)
17/11/2026 · chat di revisione 10 v2 · ramo `revisione-letteratura-V-lez10` · modello: lezione 11. Ogni dato è etichettato **M** (misurato), **S** (stima / lettura a vista), **NV** (non verificato).

## 1. Misure sul video nuovo (M)
| | Prima (consegna) | Dopo |
|---|---|---|
| Durata | 53:20,2 (3200,2 s) | **50:08,6 (3008,57 s)** |
| Fotogrammi | 96.005 | **90.257 = durata × 30** |
| Peso | 172,9 MB | **342,0 MB** (< 400), 4 parti da 90 MB + sha256 (ricomposto = uguale) |
| Formato | 1920×1080 | 1920×1080, 30 fps, x264 veryfast CRF 19, AAC 192k 48 kHz |
| Volume totale | – | **−16,0 LUFS**; picco **−2,0 dBTP** (limite −1) |
| Silenzi > 2,5 s | – | solo 4 punti da 2,79–2,81 s (schede titolo); **nessuno > 3 s** |
| Scatto quiz (controllo_jingle.py) | – | Q1–Q4 **+0,003 s** (limite 0,05) |
| Sincronia audio del prof con l'originale | – | 15 punti (3 per pezzo): **scarto max 0,016 s** (limite 0,04), correlazione 0,99–1,00 |

**Tabella secondo vecchio → nuovo** (la durata è cambiata; già aggiornati `scheda_pubblicazione.json`, `quiz_argomenti`, `timeline.json`):
| Elemento | vecchio | nuovo |
|---|---|---|
| Titolo arg. 1 | 257,9 | 240,7 |
| Quiz 1 | 1198,0 | 1131,0 |
| Titolo arg. 2 | 1203,0 | 1136,0 |
| Quiz 2 | 2142,9 | 2024,5 |
| Titolo arg. 3 | 2147,9 | 2029,5 |
| Quiz 3 | 2604,8 | 2507,0 |
| Titolo arg. 4 | 2609,8 | 2512,0 |
| Quiz 4 | 3025,3 | 2891,9 |
| Durata | 3200,2 | 3008,6 |
Verifica finale e compiti **non sono più nel video** (come lezione 11): restano in `verifica_finale.json` / `compiti.json`.

## 2. Confronto con il modello (punti 1–11)
| # | Esito |
|---|---|
| 1 sigla → dissolvenza → copertina | **corretto**: sigla Letteratura del kit, dissolvenza 0,7 s |
| 2 copertina | **corretto**: logo, riga Figtree Bold «LETTERATURA ITALIANA V · VIDEOLEZIONE», titolo Bricolage 800 con barretta, card ARGOMENTI (4). Il prof c'è in video vivo (parla davvero) |
| 3 slide fondo bianco, «01 · ARGOMENTO», card | **corretto**: tutte rifatte (prima fondo azzurro/blu scuro) |
| 4 piè di pagina | **corretto**: «LETTERATURA ITALIANA V · Prof. Giorgio Mazzotti» + «Pagina N» (N = ordine nel video, 34 pagine), Figtree Bold |
| 5 riquadro 4:3 | **corretto**: 412×310 a x=1428 y=148, angoli arrotondati, ombra grigia, niente bordo; ritaglio 4:3 dall'**originale** del prof con correzione del kit (contrasto 1,04, saturazione 1,03, hqdn3d, cas 0,35). Il tondo non c'è più |
| 6 fascia gialla | **corretto**: 2 righe, −3°, sempre visibile dove c'è il prof |
| 7 slide senza prof | **corretto**: approfondimenti, ripassi, mappa, glossario, riepilogo, titoli, quiz a pagina intera, testo 29–34 px, giallo solo sulla card in corso |
| 8 font | **corretto**: Bricolage 800 + Figtree; etichette e piè di pagina Figtree Bold (nessun DM Mono) |
| 9 finale | **corretto**: `Sigla_finale_5s_con_avviso_diritti.mp4` |
| 10 struttura | **OK**: sigla → presentazione (il prof) → per argomento: titolo, prof, approfondimenti, ripasso (R + schema), quiz → glossario → riepilogo → finale |
| 11 PDF A4 orizz. | **fatti**: `…_slide.pdf` 34 pagine, `…_mappe.pdf` 1 pagina. Confronto pagina/video: **S** (stesse immagini usate per il video, stato senza evidenziazione e senza prof; non ho fatto il confronto automatico fotogramma per fotogramma → **NV**). Il testo nel PDF è immagine, non selezionabile |

## 3. Problemi trovati e correzioni
| Minuto (vecchio) | Tipo | Com'era | Correzione |
|---|---|---|---|
| tutto | visivo | prof nel tondo, grafica non Spagnolo, fondo blu scuro in titoli/quiz/animazioni, DM Mono | tutto rifatto nel modello (§2) |
| 23:02–28:30 | visivo | evidenziazione ferma sul punto 1 mentre il prof va avanti | evidenziazioni rifatte dal parlato (tempi della trascrizione). Nessuna card resta evidenziata mentre il prof parla d'altro: dove le slide non coprono il discorso (Verga/Pascoli 8:08–9:39, stampa 19:01–21:39) tutte le card sono spente. Stati più lunghi: card «L'Italia divisa» 4:06 (neutralisti, interventisti, guerra), foto Gozzano 2:15 |
| ~15:34 (D1/D2) e ~27:12 | audio | i pezzi del prof finivano a metà frase («…Avevo citato, avevo anticipato un po' i crepuscolari») | pezzi rifatti dall'originale tagliando solo nei silenzi, a fine frase (tabella §6) |
| 4 pezzi, intro | visivo | riquadro non allineato con l'inquadratura reale: la webcam del prof **cambia posizione a 229,5 s** (spostamento) | ritaglio con cambio di posizione a 229,5 s (misurato sui fotogrammi) |
| 0:00–3:46 | visivo | titolo/argomenti: ok ma nel tondo | copertina con card ARGOMENTI e il prof che parla |
| mappe | contenuto | 5 mappe nostre (una per argomento + finale) | tolte con le loro voci. Il prof ne ha mandata **una sola** (crepuscolarismo): impaginata dopo il ripasso dell'argomento 3, con voce nuova **R5_MPD1** (generata dalla master in 10 min) |
| approfondimenti | voce/visivo | frasi «Ecco la mappa…» senza mappa | AN3, AN6, AN9, AN11, MF1 tolti; per le altre voci ogni frase ha una card sullo schermo evidenziata a tempo (allineamento voce ↔ trascrizione della voce) |
| quiz Q1 | dati | – | verificati i 4 quiz da 5 domande contro il materiale del prof: corretti, invariati |
| compiti.json | dati | formato `risposta_aperta` | formato `esercizi/aperta`; testo = PDF del prof (4 domande, M) |
| scheda_pubblicazione.json | dati | titolo con «Parte 1» | «Letteratura V · Lezione 10 · Il primo Novecento e la lirica italiana» |
| sottotitoli | testo | 677 blocchi con frasi senza senso e nomi storpiati | `.vtt` rifatto dall'originale (601 cue): ~100 correzioni a mano e per regola (D'Annunzio, Pascoli, Gozzano, Rebora, Lacerba, Laudi, Ungaretti, Deledda, Verlaine…), tolte 14 frasi inventate dal riconoscimento (es. «Olha só», «No estoy enquadrando…»). Max 2 righe |
| Verifica | dati | – | `Verifica_finale…xlsx` = Excel del prof (10 domande, M); `verifica_finale.json` |
| Audio prof | audio | – | rifatto dall'originale: aresample 48000, highpass 80, arnndn (modello `sh.rnnn` del kit), loudnorm −16 lineare, limitatore; stessi istanti dell'originale |

## 4. Pagine del libro in HD
Lezione 10: **non ha pagine del libro** (regole B-bis). Le slide del prof 8 e 10 contengono foto: la 8 (Gozzano, detto dal prof a 29:47 «Eccolo qua… Guido Gozzano») è usata a 29:46–32:01; la 10 (seconda foto) **il prof non la mostra mai** nell'originale e non è inserita.

## 5. Cosa NON ho verificato
- **Ascolto a orecchio**: fruscio, ronzio, «metallico», pronuncia delle voci Kore (nomi: Rebora, Lacerba, Brest-Litovsk, Corazzini; la trascrizione automatica ha letto «Rebola» e «l'accerba» in R4 e RF: **da riascoltare** e, se sbagliati, rigenerare come R6…).
- Sincronia labiale (dedotta dall'audio, non guardata).
- Freeze (`freezedetect`) sul riquadro del prof: non eseguito per mancanza di tempo; il prof è sempre video vivo (**S**).
- Sottotitoli: ~12 frasi sono **ricostruzioni plausibili** di parole storpiate dal riconoscimento (es. «Grazia Deledda», «Ungaretti», «magniloquenti», «dell'impero austro-ungarico»): **da riascoltare** a campione dalla master.
- Confronto automatico pagina PDF ↔ fotogramma (§2.11).
- Pronuncia di «Aracoeli»: non presente in questa lezione.
- Testa del prof a volte al limite alto del riquadro: già nell'originale (webcam 247×138 ingrandita ×2,2, più morbida del modello Spagnolo).

## 6. Prof mai tagliato a metà frase (M, trascrizione dell'originale)
segmenti 33 frame 90257 durata 50.14277777777777 min
| Pezzo | Fine (orig.) | Ultime parole dette | Frase finita |
|---|---|---|---|
| INTRO | 226.40 | «…esami. verso quella verso quella meta. Allora.» | sì |
| A1 | 932.01 | «…Tutto questo è quindi il primo Novecento.» | sì |
| A2 | 1626.30 | «…in filosofia di storia si cita sicuramente.» | sì |
| A3 | 1921.10 | «…propria sofferenza biologica come unica materia d'arte.» | sì |
| A4 | 2178.60 | «…le loro riflessioni e le loro composizioni.» | sì |

| Pezzo | Inizio (orig.) | Prime parole dette | Parola mozzata |
|---|---|---|---|
| INTRO | 0.00 | «Buongiorno e benvenuti alla lezione sul primo…» | no |
| A1 | 226.40 | «qualche ceno storico E io mi sposto…» | no |
| A2 | 932.01 | «Per tornare a noi, per tornare alla…» | no |
| A3 | 1627.20 | «Io prima avevo detto Avevo citato, avevo…» | no |
| A4 | 1923.28 | «Tutto un altro. Tut un altro discorso…» | no |

## 7. DA CONFERMARE COL PROF
- Giuseppe Antonio Borgese (nel parlato) / «Antonio Borgese» (mappa del prof) / articolo «La Stampa 1910» (Excel): nel video uso «Antonio Borgese» solo nella voce della mappa, come scritto nella mappa.
- Il prof dice che l'obbligo scolastico sale «da 9 a 12 anni»: la slide dice «fino a dodici anni» (coerente).

## 8. Come ho verificato
Trascrizione completa dell'originale (`trascrivi.py`, 405 segmenti) letta per intero; fotogrammi ogni 2 s del video vecchio (1/s estratti) e cambi slide dell'originale misurati a 2 fps; trascrizione di tutte le voci Kore per sincronizzare le card; misure sul video nuovo con ffprobe/ebur128/silencedetect/correlazione audio; contact sheet `controllo_minuti.jpg` (1 fotogramma ogni 30 s) guardato per intero.
