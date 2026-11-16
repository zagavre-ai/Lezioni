# BRIEF APPROVATO · Videolezioni Centro Studi Telesio (31/10/2026) — VINCOLANTE

> **16/11 · Sara: la grafica deve essere IDENTICA alla Lezione 1 di Spagnolo consegnata con il brief** (modello in `kit/modello_spagnolo/` su main): riquadro 4:3 con ombra grigia morbida, fascia gialla col nome su due righe sempre visibile. Dove questo file dice altro (rettangolo, ombra blu), vale il modello Spagnolo.
>
> Copia del brief presentato e **approvato**. Tutte le chat di produzione e di revisione lo rispettano. Dove le regole successive (REGOLE.md, regole di revisione 16/11) sono più precise, valgono quelle; per tutto il resto vale questo brief.

## 1. Produzione
- Videolezione ~60 minuti, con **sigla di apertura e sigla di chiusura**.
- Dispensa **PDF A4 orizzontale**, identica alla slide 16:9 ma senza riquadro docente.
- Stessa matrice grafica per tutte le lezioni. Stile «GeoPop Premium Edutainment»: riquadro docente alternato a infografiche, schemi, animazioni didattiche.
- Grafiche scalabili (HTML/CSS/PDF; PNG solo come uscita).

## 2. Matrice grafica v3
- Fondo bianco #FFFFFF (o grigio chiarissimo); testo e bordi Blu notte #0B1530; Blu Telesio #2060AF; giallo #FFE600 solo per evidenziare; grigi #EEF0F4 / #C9D0DC solo riempimenti.
- **Vietati** viola, verde, crema/avorio, mattone; niente post-it storti, niente corsivo decorativo.
- Titoli **Bricolage Grotesque 800**; testo **Figtree**; etichette **DM Mono** tra [ ].
- Card Focus squadrata, bordo 2 px, ombra netta, nessuna rotazione. Tabelle in grassetto.

## 3. Regole vincolanti
1. **BES/DSA: le tabelle non si spezzano mai** su due slide o pagine.
2. **Nessun marchio o logo di terzi** visibile.
3. Grafiche scalabili.
4. **Nessun lampeggio** (≤ 3 lampi/s; nessuna variazione di luminanza > 20% in meno di 330 ms).
5. Contrasto testo/sfondo alto; testo fermo almeno 1,5 s.

## 4. Sigle
- Sigle approvate su fondo nero, **15 s**, −16 LUFS, true peak ≤ −1 dBTP (Letteratura: `kit/sigle/Sigla_Letteratura_15s.mp4`; Storia: `kit/sigle/Sigla_Storia_15s.mp4`).
- **Finale breve 5 s** uguale per tutte: fondo nero, «GRAZIE PER L'ATTENZIONE», barra gialla, logo Telesio bianco, senza nome del docente.

## 5. Montaggio
1. Sigla iniziale (15 s) → **transizione morbida** (dissolvenza ~1 s, la musica sfuma; nessun lampo).
2. Lezione: slide a schermo intero con il **riquadro docente** (4:3 in alto a destra, come Spagnolo Lez. 1).
3. Inserti di animazione didattica dove serve; il video del docente **non si taglia mai** (unica eccezione approvata: le Actividad di Spagnolo).
4. Sigla finale con la stessa transizione morbida.
- **Correzione immagine del docente (kit):** guadagno per canale, gamma, contrasto 1,04, saturazione 1,03, `hqdn3d 1,5:1,5:3:3`, `cas 0,35`, sul riquadro già rimpicciolito.
- **Audio (kit):** `aresample 48 kHz, highpass 80, arnndn, loudnorm −16, alimiter`. Firma: `CentroStudiTelesio-videocorretto-v2-audiopulito`.

## 5-bis. Transizione e sottopancia
- **Sottopancia del docente:** striscia **gialla #FFE600** sotto il riquadro docente, **leggermente inclinata (−3°)** o a due blocchi bianco+giallo; **nome del docente** in #0B1530, Bricolage Grotesque 800, contrasto altissimo; eventuale qualifica in DM Mono tra [ ]. Entra con la copertina e ricompare a inizio di ogni argomento principale; nessun movimento rapido.
- **Riquadro docente:** niente cornice storta; **ombra netta Blu Telesio + bordo blu notte sottile**, come le card Focus (stile delle lezioni di Spagnolo).
- Nella dispensa A4 il sottopancia non compare.

## 5-quater. Esercizi interattivi
- La Direzione vuole assolutamente gli esercizi interattivi: il video si ferma, esercizio sopra il video, esito, punteggio; non si salta un esercizio non fatto; layout adattivo per telefono; accessibile da tastiera.

## Docenti
- Letteratura italiana V e Storia V: **Prof. Giorgio Mazzotti**.
