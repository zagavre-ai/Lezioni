# RAPPORTO · Storia dell'arte V · Lezione 14 · «I nuovi realismi» · Parte 1 (unica)

**STATO: consegna con VOCI KORE PROVVISORIE.** Le voci Kore non erano ancora arrivate alle 12:00 (ramo `voci-storia-arte-V-lez14` ha solo `testi_voci.json`, 22 voci incl. COMPITI). Tutte le voci narranti di questo video sono segnaposto sintetici con le stesse parole. **Non è consegna finale.** Appena arrivano le voci: controllo (trascrizione, numeri, bordi < 0,03), rimontaggio (~1 ora: i clip del docente sono in cache), nuovi controlli e riconsegna.

## 1. Misure sul video (misurato)
| Voce | Valore |
|---|---|
| File | `StoriaArte_Lez14_Parte1_1080p.mp4`, 1920×1080, 30 fps, 45:42,5, 82275 fotogrammi (= durata × 30), 342 MB |
| Codifica | x264 veryfast CRF 19, AAC 192k 48 kHz (una sola codifica del video; l'audio finale è stato rinormalizzato e unito senza ricodificare il video) |
| Volume | −16,0 LUFS, picco −1,2 dBTP |
| `controllo_rapido.py` | **ESITO OK** (nessuna pausa muta > 2,5 s, nessun nome nel piè di pagina, nessuna schermata > 3 min, titolo in copertina 2/2 parole). Foglio e json in questa cartella; il foglio è stato guardato. |
| Scatto jingle quiz (`controllo_jingle.py`) | Q1–Q7: scarto massimo +0,008 s (accettato ≤ 0,05) |
| Timbro docente (>4 kHz rispetto a >100 Hz) | originale −17,4 dB; nel video −15,8 dB (dentro −9/−20). Filtro bassi 80 Hz, riduzione rumore FFT leggera, compressore dolce 2,5:1 |
| Labbra/voce | scarto 0 per costruzione: webcam ritagliata dall'originale fotogramma per fotogramma (57350 fotogrammi, stessi dell'originale) e audio dalla stessa traccia. Non misurato con strumento separato. |
| Quiz / verifica | 6 quiz da 5 domande (30) + verifica di sbarramento con le 10 domande del docente, dentro il video; soglia 80% |

## 2. Struttura (come CLAUDE.md §3)
Sigla *Storia dell'arte* (15 s) → copertina con voce di benvenuto (senza riquadro) → introduzione del docente sulla copertina (1:35) → slide degli argomenti (voce, senza riquadro) → 6 argomenti, ognuno: titolo con jingle, docente con card, approfondimento animato (voce), [mappa del docente], pillola con jingle, quiz → glossario (10 termini) → ripasso finale → mappa finale → verifica → sigla finale con avviso diritti → intro «Compiti» con jingle → compiti letti dalla voce (4 compiti, il quarto con bordo giallo, frase finale a schermo e a voce).
Una sola Parte (45:42 < 50 min: va bene, non si allunga). Piè di pagina solo «STORIA DELL'ARTE V» e «Pagina N».

## 3. Tagli del docente (tabella inizio/fine, tutte frasi finite)
Vedi `tabella_tagli.md` (minuti sul video finale). Tagli solo nelle pause; tolte solo 3 pause > 2,2 s (599,6–602,8 s; 1117,1–1120,5 s; 1614,0–1616,5 s dell'originale, ridotte a ~1 s). Nessuna parola del docente tolta o riassunta.

## 4. Anomalie nel materiale del docente (da portare a Sara)
- Parlato: la Nuova Oggettività «nata nel 1905» (al minuto 2:20 dell'originale): data che non torna (è degli anni Venti). **Non ripetuta** nelle voci e nelle card; nei sottotitoli il parlato resta com'è.
- Il docente dice «Georg Gross» (Grosz), «Backman» (Beckmann), «Schiller» (Sheeler), «Grand Hood» (Grant Wood), «Hooper» (Hopper), «Walt Evans» (Walker Evans), «Foreign Security Administration» (Farm Security Administration), «Albert Spur» (Speer): nei nostri testi e sottotitoli sono scritti giusti (la trascrizione automatica può aver sbagliato alcuni nomi: la master li ricontrolli).
- Slide del docente: «Nighthawks» ha anno 1942 (coerente col parlato); «American Gothic» e «American Landscape» 1930 come nelle domande.
- Mappe del docente senza titolo-domanda: scritte da noi con le sue parole (M1 «Che cosa sono i nuovi realismi?», M2 «Che cosa succede all'arte moderna sotto il nazismo?», M3 «Come raccontano la realtà Picasso, Frida Kahlo ed Edward Hopper?»). La mappa 3 è unica per tre argomenti: è nella mappa finale; gli argomenti 3–6 chiudono con la pillola.
- Compiti: dal foglio `LEZIONE 14.pdf` (4 compiti, testo esatto).

## 5. Immagini e fonti
Solo le opere delle slide del docente (`pdfimages`), ritagliate e ingrandite con Lanczos + nitidezza leggera, senza cambiare l'opera: Metropolis (Dix), Guernica (Picasso), Autoritratto con la colonna spezzata e Autoritratto con collana di spine (Kahlo), American Landscape (Sheeler), American Gothic (Wood), Nighthawks (Hopper). **Risoluzione d'origine bassa** (Kahlo 302×388 px, Sheeler/Wood ~415×319 e 267×319 px): ingrandite 2–2,6×, non perfette. Richieste alla master (alta risoluzione): le 7 opere + *Office at Night* (Hopper 1940), *Migrant Mother* (Lange 1936), *Sharecropper's Family* (Evans 1936), *Autoritratto in smoking* (Beckmann 1927). **Non arrivate**: in questo video *Office at Night*, *Migrant Mother* e *Sharecropper's Family* sono citate dal docente ma non hanno l'immagine (solo card di testo); da inserire quando la master le manda.
Webcam del docente: **origine 245×137 px** (16:9), ritaglio 4:3 di 183×137 px ingrandito a 412×309 (2,25×), nitidezza leggera; la testa è già tagliata in alto nell'originale.

## 6. Cosa NON ho verificato
- Le voci Kore (non esistono ancora): trascrizione, numeri, pronuncia dei nomi stranieri, bordi < 0,03.
- Controllo di un agente separato sulla lista del §11: non ancora fatto (si fa sul video con le voci vere).
- Sottotitoli `.vtt`: costruiti dalla trascrizione automatica con correzioni automatiche dei nomi; **non riletti uno per uno**; i tempi delle frasi sono per segmento (±0,5 s). Le voci provvisorie sono sottotitolate con il loro testo.
- Evidenziazione delle card: i tempi sono quelli della trascrizione (inizio della frase); non ho controllato a mano 10 punti.
- «Dispensa identica al video»: PDF A4 con lo strato di testo invisibile, ma senza confronto pagina per pagina con i fotogrammi.
- Fondo blu delle schede scure fisso (non animato); le immagini degli approfondimenti non hanno movimento.
- Cambi di schermata dentro un pezzo del docente: stacco netto (dissolvenza + `trans.wav` solo ai cambi di pezzo).
- Controllo del timbro oltre la banda >4 kHz e ascolto del docente: non fatti all'orecchio.

## 7. File
Video a pezzi da 90 MB + sha256, `.vtt`, `timeline_Parte1.json`, `scheda_pubblicazione_Parte1.json` (titolo «Storia dell'arte V · Lezione 14 · I nuovi realismi»), `quiz_argomenti.json`, `verifica_finale.json` + xlsx del docente, `compiti.json`, dispensa A4 (79 pagine) e PDF delle mappe (4 pagine), foglio dei fotogrammi e json del controllo rapido, `montaggio/` (strumenti).
