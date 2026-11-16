# RAPPORTO REVISIONE · Letteratura italiana V · Lezione 20 · Carlo Emilio Gadda
Revisione del 16/11/2026. Video corretto: `Letteratura_Lez20_Parte1_1080p.mp4` (a pezzi `.parte_00…02`, sha256 nel file `.sha256`).
Regola: **misurato** = misurato con uno strumento; **stima** = dedotto; **non verificato** = non ho potuto.
Lezione **rifatta per intero nel modello Spagnolo** (non rattoppata), a parità di durata e di fotogrammi.

## 1. Misure sul video nuovo (misurato)
| Controllo | Risultato |
|---|---|
| Formato | 1920×1080, 30 fps, x264 veryfast CRF 19, AAC 192k 48 kHz |
| Durata / fotogrammi | 54:50,4 (3290,37 s) · 98 711 fotogrammi = durata × 30 · **identici al montaggio precedente**: quiz, verifica e compiti restano agli stessi secondi (somma di 101 pezzi = 98 711 fotogrammi) |
| Peso | 191,0 MB (182,2 MiB) |
| Scatto dei quiz | `controllo_jingle.py`: Q1–Q6 a **0,000 s** (scarto massimo 0,001 s) |
| Volume | −17,1 LUFS integrato; parlato del prof (mediana dei pezzi D) −17,3 LUFS; picco **−1,2 dBTP** (≤ −1) |
| Fermi immagine del prof | `controllo_finale.py`: nessuno (soglia 1 s). Una scansione più sensibile (freezedetect −60 dB, ≥ 2 s) segna 16 punti di 2–3,9 s in cui il prof sta fermo: non sono fotogrammi ripetuti ma pose ferme (filtro temporale hqdn3d) |
| Sottotitoli | 812 blocchi, max 2 righe da 42 caratteri, nessuna sovrapposizione, nessuno oltre la fine. **Sincronia: `controllo_finale.py` dà «DA GUARDARE»** (attacco entro 0,3 s: 56 % di 18 blocchi verificabili, soglia 80 %). Mia misura su 332 blocchi: scarto mediano −0,01 s (prof) e −0,05 s (voce), ma con dispersione di ±0,5 s per i blocchi del prof (i blocchi spezzati dentro la frase hanno il tempo ripartito sui caratteri: **stima**). Da controllare a occhio |
| PDF | slide: 64 pagine A4 orizzontale · mappe: 1 pagina A4 orizzontale |

## 2. Confronto col modello Spagnolo (punto 000)
| # | Punto | Esito |
|---|---|---|
| 1 | Sigla → dissolvenza morbida → copertina | sigla 16 s invariata (nera, «ANALISI TESTUALE»); dissolvenza **rifatta** fra tutti i pezzi |
| 2 | Copertina (logo, riga «LETTERATURA ITALIANA V · VIDEOLEZIONE», titolo, card ARGOMENTI) | **corretto**: card con **tutti e 6** gli argomenti (prima 3 su 6, mentre la voce ne elencava 6) |
| 3 | Slide fondo bianco, «01 · ARGOMENTO», titolo + barretta blu, card | **corretto** (prima: fondo grigio, «ARGOMENTO 1 · …», barretta gialla, fondo blu scuro su approfondimenti/ripassi/glossario/riepilogo/compiti) |
| 4 | Piè «LETTERATURA ITALIANA V · Prof. Giorgio Mazzotti» + «Pagina N» a destra | **corretto** (prima senza «V» e col numero attaccato) |
| 5 | Riquadro 4:3 ≈410×308, ombra morbida, niente bordo blu | **corretto**: 412×309 px a x=1428, y=148, angoli r=18 (prima 396×221 16:9 con bordo blu e banda blu a destra) |
| 6 | Fascia gialla −3°, due righe, sempre visibile | **corretto**: «Giorgio Mazzotti» / «PROF. DI LETTERATURA ITALIANA» su tutte le slide col prof |
| 7 | Slide senza prof: testo grande, giallo solo sulla parola in corso | **corretto** (approfondimenti, ripassi, glossario, riepilogo, mappe, titoli argomento, schede Quiz/Verifica/Compiti) |
| 8 | Font | Bricolage Grotesque 800, Figtree. Etichette e piè in Figtree Bold come nel modello. **Corretto**: le schede titolo d'argomento usavano un carattere con le grazie (serif), ora no |
| 9 | Finale 5 s con avviso diritti | **corretto**: ora è `Sigla_finale_5s_con_avviso_diritti.mp4` del kit (prima cartello nero senza avviso) |
| 10 | Struttura | OK: sigla → presentazione → 6 argomenti (slide del prof, approfondimenti, ripasso, quiz) → glossario → riepilogo → finale; poi verifica e compiti |
| 11 | PDF A4 orizzontale | consegnati (§ 4) |

**Testa nel riquadro:** il prof è ripreso in una webcam di soli ≈ 246×137 px nel video originale (1092×614): il taglio 4:3 (183×137) è ingrandito ≈ 2,25× e quindi **più morbido** del modello Spagnolo. Nell'originale i capelli toccano il bordo alto del riquadro webcam (es. 0:05, 6:40, 15:00, 23:20 dell'originale): non risolvibile. Correzione immagine del kit applicata (contrasto 1,04, saturazione 1,03, hqdn3d 1.5:1.5:3:3, cas 0.35).

## 3. Problemi trovati e correzioni
| Minuto | Tipo | Com'era | Correzione |
|---|---|---|---|
| tutto | visivo | grafica vecchia: banda blu, riquadro 16:9 col bordo, nome senza fascia, fondo scuro nei pezzi senza prof | tutta rifatta nel modello (64 pagine) |
| 0:18–0:54 | visivo/testo | presentazione con 3 argomenti su 6 (la voce dice «sei argomenti» e li elenca) | cover con 6 argomenti, evidenziati in sincronia con la voce (misurato dalla trascrizione) |
| 1:52 e sui 6 titoli d'argomento | visivo | schede titolo d'argomento in carattere con le grazie; il titolo dell'argomento 6 era **troncato** («Il giallo filosofico / Quer pasticciaccio…») | schede nel modello; titolo «Il giallo filosofico» |
| 0:50–0:58 (orig.) | visivo | il prof dice «questo è un ritratto fotografico… di Carlo Emilio Gadda»: sullo schermo non c'era la foto | inserita la foto dalle sue slide (ritaglio dal video originale, bassa risoluzione) per l'intero passaggio |
| 6:56 · 18:00 · 25:16 · 32:36 · 38:07 · 45:37 (fine dei pezzi del prof) | audio | a ogni cucitura il prof **ripeteva 0,56 · 0,54 · 1,53 · 1,02 · 1,33 s** di parlato (misurato per correlazione, ±0,15 s); alcune cuciture cadevano dentro una frase (es. orig. 355,7 s «segnata da profondi | avvenimenti»; 891,7 s «il primo grande | lavoro») | tagli spostati su pause fra una frase e l'altra (misurato sul segnale: minimo di energia); nessuna ripetizione. Per tenere la durata ogni pezzo è accelerato/rallentato di 0,6–1,8 % (voce senza cambio di tono) |
| pezzi del prof | audio | non puliti con la catena del kit | rifatti dall'originale: `aresample 48000, highpass 80, arnndn (sh.rnnn), loudnorm −16, alimiter` (−17,3 LUFS dopo i pezzi; picco −1,2 dBTP). **Non ho ascoltato** fruscio/ronzio/metallico |
| tutte le slide del prof | sincronia | evidenziazioni scelte a occhio; D1 card 1 accesa dall'inizio mentre il prof parlava dei dati di vita | rifatte dal parlato del prof (tempi parola per parola, stima ±1,5 s): es. 2:02 card 2 «Le origini» (1893/Milano), 3:02 card 1, 3:39 card 2, 4:33 card 3, 6:17 pagina «La professione e la svolta»; «visione del mondo» al 13:42 quando il prof passa al caos; l'evidenziazione si spegne dopo «concludendo» (orig. 1427 s, ≈ 43:21) |
| 8:28 · 9:42 · 19:20 · 20:46 · 26:36 · 27:50 · 34:08 · 39:20 · 47:03 · 48:07 · 49:07 · 50:51 (misurato) | audio | **silenzi di 3,0–3,9 s** fra una voce narrante e l'altra (fine approfondimento/mappa); erano già nel video vecchio | **NON corretti**: servirebbero tagli o voci nuove e si sfalserebbero quiz e compiti. Da decidere con Sara |
| 1:31 · 5:04 · 11:54 · 13:58 · 16:19 · 24:56 · 30:47 (misurato; 3,2–6,4 s) | audio | pause del **prof stesso** di 3,2–6,4 s, ora vere (la pulizia toglie il rumore di fondo) | lasciate: si taglia solo fra le frasi e la durata deve restare la stessa. Segnalate |
| 9:44 · 20:48 · 26:39 · 34:10 · 39:23 · 49:10 · 50:54 (mont.) | visivo/testo | mappe concettuali **non del prof** (7 mappe da 6 nodi costruite da noi con la voce Kore) | tenute nel video perché ognuna ha la sua voce narrante (cambiarle = nuove voci e durata diversa). Impaginate di nuovo nel modello. La **mappa del prof** (`MAPPE/LEZIONE 20.pdf`) è consegnata nel PDF mappe, identica nei contenuti. **Decide Sara** se sostituirle |
| quiz, test | testo | il test aveva il foglio «Istruzioni» del modello (15 domande) | `verifica_finale.json` + xlsx del prof: 10 domande, testo identico all'Excel |
| scheda | testo | titolo «Carlo Emilio Gadda · Parte 1» | «Letteratura V · Lezione 20 · Carlo Emilio Gadda» |
| sottotitoli | testo | parlato del prof pieno di errori («gabbiana», «Carlo Milogato», «ultratutto fotografico», «1893,973», «Ungaretti»→«garetti»…) | rifatti da trascrizione nuova: 812 blocchi, nomi e titoli corretti, fillers non intelligibili tolti. **Dubbi nel § 5** |
| audio generale | audio | (errore mio, corretto) l'estrazione dell'audio vecchio perdeva 0,7 s per buchi nei timestamp: i jingle dei quiz risultavano sfasati 0,2–0,5 s | audio ricostruito per intervalli e riallineato: scatto a 0,000 s |

## 4. Consegne
`Letteratura_Lez20_Parte1_1080p.mp4` (a pezzi + sha256) · `Letteratura_Lez20_Parte1.vtt` · `Letteratura_Lez20_slide.pdf` (64 pagine, le slide **senza riquadro e senza fascia**, nello stesso ordine del video; la pagina «ritratto» è numerata 1 come la copertina) · `Letteratura_Lez20_mappe.pdf` (la mappa del prof, 1 pagina; il prof non ne ha mandata una per argomento) · `quiz_argomenti.json` · `Quiz_Letteratura_Lez20.txt` · `verifica_finale.json` + `Letteratura_Lez20_verifica_finale.xlsx` (10 domande del prof) · `compiti.json` (4 esercizi, identici al PDF «LEZIONE 20») · `scheda_pubblicazione.json` · `testo_youtube.txt` · `timeline.json` · `controllo_minuti.jpg`.
Pagine del libro: la lezione 20 non ne ha (B-bis non applicabile). Quiz: riletti contro le slide del prof, domande e risposte giuste coerenti, invariati.

## 5. Cosa NON ho verificato / limiti
- **Ascolto umano:** non ho ascoltato nulla. Fruscio/ronzio/«metallico» dopo la pulizia: **non verificato**. Sincronia delle labbra: i pezzi del prof usano lo stesso orologio per audio e video (stima); verifica indipendente sulle labbra non fatta (webcam troppo piccola).
- **Voce narrante Kore:** la trascrizione automatica ha restituito forme sospette, da riascoltare: «Il termine che usa **il docente**» (≈ 18:07, frase poco naturale), «**gattiano**» per gaddiano (≈ 20:53), «**Mar Adal**» per Maradagàl (≈ 32:51), «**brutto di via Merulana**» al posto di «de via» (≈ 45:43, 50:18), «L'**A Dal Gisa**» (≈ 40:22), «**gialosofico**» (≈ 0:41, 51:53). Possono essere errori della trascrizione: **non corretto**, non ho aggiunto voci `R1…` perché non ho potuto ascoltare. Se confermate serve la master.
- **Sottotitoli — da riascoltare (dubbi):** 2:01 «1893, 1973: Milano, Roma», 4:10 «di un buon tenore di vita», 4:50 attacco dopo «vederla», 5:29 «alla Pirandello», 13:19 «espressioni gergali», 17:19 («forse anche materna… la critica alla madre»), 29:06 («non anche gli anni di quello»), 29:36 («tratti forse anche a oggi»), 37:09 («strumenti scientifici»), 42:21 («è fatta apposta, forse anche il primo»). Il resto è stato riletto cue per cue contro la trascrizione, ma le frasi lasciate com'erano nel parlato sono disfluenti.
- **Evidenziazioni e foto:** calcolate dalla trascrizione (Parakeet), stima ±1,5 s, da controllare in almeno 4 punti a occhio. La foto di Gadda è un ritaglio dal video del prof (≈ 334×365 px ingrandito ×3): meno nitida; **le slide originali del prof (`Letteratura_Lez20_videodispensa.pptx`) non sono nella release** (ci sono solo 1–17 e 26).
- **PDF slide vs video:** nate dagli stessi modelli HTML (stima di identità); **non** confrontate pixel per pixel pagina per pagina.
- **Frasi tagliate della voce narrante / «ecco, guarda…»:** letti tutti i punti («ecco la mappa», «apriamo la scheda», «mettiamo a confronto») sulla trascrizione: l'immagine nominata è sullo schermo entro 1 s. Nessuna frase tagliata.
- **Durata dei pezzi del prof:** ritmo variato di 0,6–1,8 % (voce senza cambio di tono, stima di inudibilità, non ascoltato).

## DA CONFERMARE COL PROF
- La meccanica: il prof dice «1924-28», le schede e la voce Kore dicono «1924».
- Nessun'altra discordanza di date fra mappa del prof (Milano 1893, morte 1973), parlato e slide.

## 6. Come ho verificato
Trascrizione completa del video originale (Parakeet TDT, 307 segmenti) e dell'audio della voce narrante (312 segmenti) con `trascrivi.py`; confronto audio originale/montato per correlazione (pezzi D: offset e fattori di velocità); 195 fotogrammi di stato del video vecchio; 110 fotogrammi a 1/30 s sul nuovo (`controllo_minuti.jpg`) + 4 a pieno formato; `controllo_finale.py`, `controllo_jingle.py`; scansioni ffmpeg (loudnorm, silencedetect −45 dB/3 s, freezedetect). OCR automatico non disponibile: testi riletti a vista e dalla dispensa del montaggio precedente.
