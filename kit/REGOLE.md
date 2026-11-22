# Kit tecnico delle chat · Videolezioni Centro Studi Telesio (22/11/2026)

**Le regole sono tutte in `CLAUDE.md`** (radice del repository). Qui c'è solo il «come»: strumenti, file, comandi. Se qualcosa qui sembra contraddire il CLAUDE.md, vince il CLAUDE.md: scrivilo alla master.

## 1. Preparazione
```
git clone https://github.com/zagavre-ai/lezioni.git /home/claude/lezioni && cd /home/claude/lezioni
mkdir -p /root/.fonts && cp kit/caratteri/*.ttf /root/.fonts/ && fc-cache -f
mkdir -p tools && cp kit/tools/*.py tools/
```
- **Caratteri** (`kit/caratteri/`): Bricolage Grotesque (titoli, 800) e Figtree (testo; Bold per etichette e piè di pagina).
- **Jingle** (`kit/suoni/`): `titolo.wav` (titolo dell'argomento), `repaso.wav` (pillola/schema di ripasso), `quiz.wav` (scheda Quiz, scatto a +0,5 s), `trans.wav` (ogni cambio di pezzo), `finale.wav` (fine).
- **Sigle** (`kit/sigle/`): una per materia, più `Sigla_finale_5s_con_avviso_diritti.mp4`.
- **Modello grafico** (`kit/modello_spagnolo/`): fotogrammi di riferimento delle slide, del riquadro del docente e della dispensa.
- **Istruzioni e modelli per materia:** ramo `scambio-caputi` (Chimica, Tecnologie: modello «Gonna», acquerelli, scaricatore dalle release) e ramo `scambio-mazzotti` (Letteratura, Storia, Storia dell'arte: controllo severo, modello della mappa BES).

## 2. Strumenti (`kit/tools/`)
| Strumento | A cosa serve |
|---|---|
| `trascrivi.py` | Trascrizione italiana con i tempi delle parole |
| `taglio.py` | Sposta ogni taglio nella pausa più silenziosa, mai dentro una frase |
| `mappa.py` | Disegno vettoriale delle mappe (con i caratteri in `mappa_font/`) |
| `rettangolo/` | Trova e allinea il riquadro del docente nel video (vedi il suo LEGGIMI) |
| `scene_dal_word.py` | Slide divise per scene dal Word del docente (lezioni con segni F9) |
| `voci_auto.py` | Importa le voci Kore ricevute dalla master; non le cancella mai |
| `finale_a_pezzi.py` | Codifica finale a gruppi, riprende da dove si è fermata |
| `volume16.py` | Porta il parlato a −16 LUFS rifacendo solo l'audio |
| `sub_finale.py` | Sottotitoli `.vtt` sul video finale |
| `scheda_da_timeline.py` | `scheda_pubblicazione.json` con la durata misurata sul file finale |
| `controllo_finale.py` | Fotogrammi, peso, risoluzione, volume, fermi del docente |
| `controllo_jingle.py` | Scatto di ogni scheda Quiz a 0,0 s |
| `testo_youtube.py` | Testo con i capitoli dalla scheda (lo usa la master) |
| `stato.py` | Stato della lezione per la master |

## 3. Voci e illustrazioni (le fa la master)
- Le chat non hanno chiavi. Sul ramo **`voci-<tag>`** carichi `scambio/<tag>/testi_voci.json`:
  `[{"nome":"A1_APPROF","testo":"..."}]` (numeri e anni in lettere, nomi stranieri scritti nella loro lingua).
- Le voci tornano in `scambio/<tag>/vox/NOME.wav`, con `ESITI*.txt`. Ogni voce va trascritta e controllata prima di montarla. Per rifarne una, aggiungi lo stesso testo con nome `_R2`.
- Illustrazioni ad acquerello: `scambio/<tag>/immagini.json` `[{"nome":"IMG_...","descrizione":"...","riferimento":"(facoltativo)"}]`. Tornano in `scambio/<tag>/img/`.
- **Messaggi della master:** `scambio/<tag>/DALLA_MASTER.txt` nello stesso ramo. Leggilo a ogni cambio di fase.

## 4. Stato
```
python3 tools/stato.py <tag> --stato IN_REVISIONE --nota "presa da <tuo ramo>" --invia
python3 tools/stato.py <tag> --parte N --stato IN_MONTAGGIO|IN_CODIFICA|REVISIONATA|FERMA --nota "..." --invia
python3 tools/stato.py <tag> --serve_master "domanda o richiesta" --invia
```
- Stato ogni 30 minuti. Una lezione si prenota prima di cominciarla: se un'altra chat l'ha già presa, non si tocca.
- Durata, fotogrammi e peso li misura il programma.

## 5. File finali e consegna
- **Video:** `Materia_LezN_ParteN_1080p.mp4`, 1920×1080, 30 fps, x264 veryfast CRF 19 (`finale_a_pezzi.py`), AAC 192k 48 kHz, sotto i 400 MB (se li supera, CRF 20 o 21).
- **Consegna sul ramo `revisione-<tag>`:**
  - video a pezzi da 90 MB (`split -b 90M -d -a 2 <video> <video>.parte_`) con il suo `.sha256`;
  - `.vtt` (`sub_finale.py`) e `timeline_ParteN.json`, `scheda_pubblicazione_ParteN.json` (`scheda_da_timeline.py`), rifatti sul video finale;
  - quiz, verifica e compiti in JSON; dispensa e PDF delle mappe;
  - `RAPPORTO_REVISIONE.md` con l'esito di `controllo_finale.py`, `controllo_jingle.py` e del controllo dell'agente separato.
- Poi stato `REVISIONATA`. La master controlla e carica.
- **Mai video sul ramo `main`.** Commit senza firma. Mai dati di alunni, chiavi o password.

## 6. Macchina
- 2 processori: un lavoro pesante alla volta, ma la macchina non resta mai ferma (mentre una cosa codifica, prepari la successiva).
- Un lavoro in background viene fermato dopo 2 ore: lavori che ripartono da dove erano (marcatori `.ok`), log con `> log && touch .fatto`, mai `| tail`.
- Disco: cancella i pezzi intermedi appena una Parte è controllata.
- Video grandi delle release: si scaricano solo i file che servono (`estrai_da_release.py` nei rami di scambio).
