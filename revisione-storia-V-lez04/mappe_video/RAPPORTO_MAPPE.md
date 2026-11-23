# Rapporto mappe · Storia V · La prima guerra mondiale

Cartella: `/home/user/Lezioni/storia-V-lez04/mappe/`. Sorgenti: `render.py` (generico, legge `mappe.json`), `mappa_lib.js`, `mappa.css`, `costruisci_mappe_json.py` (genera `mappe.json`), `mappa{k}.html`.
Consegne: `mappa{k}.mp4`, `mappa{k}_finale.png`, `mappa{k}_tempi.json` (k = 1..6), `Mappe_dispensa.pdf`.

## 1. Confronto con le mappe del prof (parola per parola, struttura, frecce)
Ho guardato le 6 immagini del prof (`m-1..m-6.png`). L'elenco della richiesta coincide con le immagini: nessuna differenza di parole. Il prof ha i riquadri teal (grassetto) e arancio; io li ho ricolorati con i colori BES. Unica scelta di scrittura mia: i segni «'» sono resi con l'apostrofo tipografico «’»; «patto di Londra» è scritto «Patto di Londra» (nome proprio, come lo dice la voce); le a capo dei riquadri sono quelle del prof, tranne dove indicato sotto.

| Mappa | Riquadri (testo) | Frecce con etichetta |
|---|---|---|
| 1 | L'EUROPA DELL'INIZIO DEL NOVECENTO; alleanze contrapposte; Triplice alleanza; Triplice intesa; Guglielmo II di Germania; una politica estera e coloniale aggressiva; la crisi dell'Impero ottomano; la concorrenza tra Austria-Ungheria e Russia | è divisa in; è destabilizzata da (tronco comune ai due figli); che adotta; che causa. Triplice alleanza/intesa: frecce a gomito dal lato del riquadro «alleanze contrapposte», senza etichetta (come il prof) |
| 2 | L'ATTENTATO DI SARAJEVO; le alleanze contrapposte; l'attacco tedesco alla Francia; le battaglie di Tannenberg, dei laghi Masuri e di Leopoli; la guerra di posizione nelle trincee | fa scattare; con (diramazione a due); cui segue (i due riquadri confluiscono in uno) |
| 3 | L'ITALIA; interventisti; neutralisti; liberali conservatori; nazionalisti; il patto di Londra; manifestazioni per l'intervento; liberali progressisti; socialisti | è divisa tra; che sono; che firmano; che organizzano. Neutralisti → due frecce a gomito senza etichetta (come il prof) |
| 4 | LA PRIMA GUERRA MONDIALE; guerra globale; guerra totale; 1916; 1917; gigantesche e inutili battaglie; il ritiro della Russia; l'intervento degli Stati Uniti; la sconfitta italiana a Caporetto | è una; nel; vede (1916); vede (1917) |
| 5 | L'ANNO 1918; una grande offensiva tedesca; l'Intesa con la battaglia di Amiens; la sconfitta austriaca sul fronte italiano; l'armistizio (4 novembre 1918); la rivoluzione in Germania; l'armistizio (11 novembre 1918) | inizia con; alla quale risponde; vede; cui segue; che porta a |
| 6 | LA CONFERENZA DI PACE DI PARIGI; i Quattordici punti di Wilson; l'autodeterminazione dei popoli; la nascita di una Società delle Nazioni; Francia e Regno Unito; una pace punitiva per la Germania | è ispirata da; che sostengono; è condizionata da; che vogliono |

Differenze di impaginazione rispetto al prof (le parole non cambiano): in mappa 2 «la guerra di posizione nelle trincee» sta su una riga (il prof la spezza in 2); in mappa 4 «guerra globale/totale», «1916», «1917» hanno l'ordine e la disposizione del prof, ma i figli di 1917 sono su una riga; in mappa 5 le parentesi delle date vanno a capo come nel prof.
Differenze tra voce e mappa (da segnalare alla master): la voce MAP2 non dice «e di Leopoli» (c'è nel riquadro del prof); le voci dicono «Seguono», «Poi», «Gli interventisti sono», «I neutralisti sono» al posto delle etichette «con», «cui segue», «che sono» (non si può cambiare: la voce segue la mappa in modo naturale); la voce MAP2 dice «la Triplice Alleanza» con la A maiuscola, il riquadro del prof ha «Triplice alleanza»: ho tenuto il prof.

## 2. Colori BES
- **Pesca (concetto centrale)**: il riquadro centrale di ogni mappa.
- **Paglierino (parole chiave)**: riquadri teal/grassetto del prof e i gruppi: alleanze contrapposte, Guglielmo II, la crisi dell'Impero ottomano (M1); le alleanze contrapposte (M2); interventisti, neutralisti, liberali conservatori, nazionalisti, liberali progressisti, socialisti (M3); guerra globale, guerra totale (M4); la sconfitta austriaca, la rivoluzione in Germania (M5); i Quattordici punti, Francia e Regno Unito (M6).
- **Celeste (date e sequenze)**: 1916 e 1917 (M4); i due armistizi con la data (M5). Il prof li aveva arancio: scelta mia.
- **Menta (esempi e opere)**: Triplice alleanza, Triplice intesa (M1); attacco tedesco, battaglie di Tannenberg… (M2); Patto di Londra, manifestazioni (M3); battaglie del 1916, ritiro della Russia, intervento USA, Caporetto (M4); offensiva tedesca, battaglia di Amiens (M5).
- **Lilla (conseguenze)**: politica aggressiva, concorrenza tra Austria-Ungheria e Russia (M1); guerra di posizione (M2); autodeterminazione, Società delle Nazioni, pace punitiva (M6).
Legenda sempre in alto a destra. Assegnazione di giudizio mia: la master può cambiarla modificando il campo `c` in `costruisci_mappe_json.py`.

## 3. Misure del testo (a 1920×1080)
Riquadri 38 px (Figtree SemiBold); riquadro centrale 46 px (Bricolage Grotesque 800, maiuscolo); etichette delle frecce 34 px (Figtree Medium); titolo 56 px (Bricolage 800, blu Telesio); legenda 20 px e «MAPPA CONCETTUALE»/«STORIA V» 20–22 px (non sono testo della mappa). Fondo bianco, riempimenti pastello, bordi pieni, frecce #0B1530 spessore 5 px, ombre grigie. Ogni mappa entra in UNA sola schermata. Il renderer verifica da solo: riquadri fuori area o a meno di 30 px l'uno dall'altro, frecce che attraversano riquadri estranei, etichette che toccano riquadri o altre etichette: esito «nessun problema» su tutte e 6 le mappe (dopo 3 correzioni che il controllo stesso ha segnalato).

## 4. Come ho ottenuto i tempi
Nessun modello di trascrizione era installabile direttamente (HuggingFace bloccato). Ho scaricato dai release GitHub di sherpa-onnx il modello Whisper «base» multilingue (solo come strumento di misura, non entra nella consegna) e ho fatto così:
1. rilevamento delle pause con l'inviluppo del segnale (soglia −28 dB dal picco, ≥ 60 ms) e taglio della voce nei punti di pausa;
2. trascrizione di ogni segmento e confronto con il testo di `testi_voci.json`: le frasi rilevate corrispondono alle frasi del testo;
3. i confini tra etichetta e riquadro dentro lo stesso respiro sono stimati a sillabe tra due pause certe (≈ 0,15 s a sillaba);
4. controllo finale: per ognuno dei 69 passi ho ritrascritto la finestra [inizio−0,1; fine+0,1] e confrontato col testo (somiglianza ≥ 0,8 per la grande maggioranza; i casi bassi erano numeri scritti in lettere che Whisper trascrive in cifre, o parole spezzate al bordo); ho corretto di 0,1–0,4 s i confini dove la trascrizione mostrava una parola dalla parte sbagliata (es. «vede» in M4/M5, «una» in M1, «all'armistizio» in M5).
**Precisione stimata: ±0,2–0,3 s sull'inizio di ogni passo.** Non c'è allineamento parola per parola: dove non c'è pausa il confine è una stima. Tutti i tempi sono in `mappa{k}_tempi.json` (`passi_voce`: t0/t1 in secondi di voce; `nodi`: entrata e intervalli di accensione in secondi di video, con t_video = 0,5 + t_voce).
Regole di montaggio: riquadro che entra 0,1 s prima della sua frase (dissolvenza + salita di 12 px in 0,3 s); freccia con etichetta che entra all'inizio dell'etichetta detta dalla voce; riquadro in corso giallo #FFE600 (riempimento + alone) da inizio a fine frase (+0,1 s), con rampa di 0,15 s (nessun lampo); il centro entra a +1,0 s e si accende quando la voce lo dice. Dove la voce ripete il genitore («Gli interventisti sono…», «I neutralisti sono…») si riaccende il riquadro genitore.

## 5. Video
1920×1080, 30 fps, x264 veryfast CRF 18, yuv420p, senza audio. Durata = 0,5 + voce + 1,5 + 4,0 arrotondata al fotogramma (la mappa completa resta visibile ≥ 5,5 s dopo l'ultima parola, 4 s a riposo senza accensioni). Fotogrammi contati con ffprobe (`-count_frames`) = durata × 30 per tutte e 6:
M1 991 (33,03 s) · M2 680 (22,67 s) · M3 833 (27,77 s) · M4 852 (28,40 s) · M5 838 (27,93 s) · M6 718 (23,93 s). Pesi 0,4–0,7 MB.

## 6. PDF
`Mappe_dispensa.pdf`: 7 pagine A4 orizzontale generate da Chromium partendo dallo stesso HTML/SVG vettoriale (testo selezionabile, verificato con pdfplumber; nessuno strato invisibile necessario). Pagina 1 copertina (logo Telesio, «STORIA V · VIDEOLEZIONE», «MAPPE», «Storia V», «La prima guerra mondiale»); pagine 2–7 una mappa ciascuna a tutta larghezza (stessa grafica delle `_finale.png`) con piè di pagina «STORIA V» e «Pagina N». Niente nome del docente né numero di lezione. Nel PDF il piè di pagina «STORIA V» della mappa è sostituito da quello della pagina.

## 7. Cosa ho guardato davvero
Letto con Read: le 6 mappe del prof; `mappa1..6_finale.png`; fotogrammi estratti dai video: M1 a 1,7 s (solo centro) e a 15,6 s (costruzione a metà, riquadro giallo), M4 a 13,2 s (riquadro giallo, ramo 1916 costruito); pagine 1, 3, 5 del PDF. Difetti corretti: font misurati prima del caricamento (riquadri fuori centro), riquadri troppo vicini (M1, M4), etichetta che toccava un riquadro (M4), PDF rimpicciolito del 25% (ora a tutta larghezza), apostrofi dritti.

## 8. Cosa NON ho verificato
- Non ho riguardato ogni singolo fotogramma né fatto una visione completa dei 6 video a velocità reale (controllate solo le pagine/frames citati e il conteggio dei fotogrammi).
- I tempi non sono ricavati da un allineamento parola per parola (vedi sopra): serve un ascolto a campione sul montaggio finale.
- L'audio non è stato montato: i video sono muti; l'allineamento reale con la voce a +0,5 s va controllato dopo il montaggio.
- La copertina del PDF imita lo stile della copertina delle slide Spagnolo (logo, kicker blu, titolo grande, sottolineatura) ma non ho avuto le slide di questa lezione: confrontarla con la copertina vera.
- Le pagine 2, 4, 6, 7 del PDF e i video M2, M3, M5, M6 a metà costruzione non sono stati aperti uno a uno (la struttura è uguale alle altre e il controllo automatico del layout è passato).
- Pronuncia dei nomi (Tannenberg, Masuri, Amiens, Wilson) non controllata ascoltando.
- Colori BES: assegnazione di giudizio, da approvare.
