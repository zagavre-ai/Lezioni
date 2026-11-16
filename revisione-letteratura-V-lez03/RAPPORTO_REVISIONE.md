# RAPPORTO REVISIONE · Letteratura italiana V · Lezione 3 (Carducci) · PRIMA VERSIONE
Stato: **FERMA — il rifacimento non è partito** (motivi in fondo). Questa è la verifica fatta finora.

## Misurato
- Pezzi ricomposti, sha256 identico a quello del ramo consegna. Video: **2560×1440** (le regole chiedono 1080p), 30 fps, 62:12.
- Parlato: **-16,1 LUFS** (OK), true peak -0,8 dBFS (sopra il limite -1: da ritoccare).
- Originale del prof (release): 1092×614, 56:37.
- 124 fotogrammi (uno ogni 30 s) guardati; OCR eseguito su tutti; `.vtt` letto con ricerca dei termini.

## Problemi trovati
| Minuto | Tipo | Com'è | Correzione prevista |
|---|---|---|---|
| tutto | visivo | prof nel **tondo**, fondo azzurrino, riga «LETTERATURA ITALIANA» sotto un nome non su fascia gialla | riquadro 4:3 con ombra, fascia gialla inclinata a due righe, fondo bianco (punto 000) |
| tutto | visivo | piè di pagina «LETTERATURA ITALIANA · Prof. Giorgio Mazzotti» ok nel testo ma carattere/colori diversi dal modello; etichetta in alto da riconfrontare | rifare le slide con la matrice di Spagnolo |
| 10:30–15:00, 36:00–46:00 | pagina | pagine del libro (San Petronio, Alla stazione…) **piccole e illeggibili**, prese dal video, non dallo screen HD | usare `Lez03_ingrandita.zip` (p050,051,053,054,056,057,058), fettine con rigo ≥ 26 px |
| 0:00 | visivo | titolo e argomenti ok, ma copertina non nel modello (manca card «ARGOMENTI» come Spagnolo, riga DM Mono «… · VIDEOLEZIONE») | rifare |
| vtt | testo | «Giosuèè» (×3), «Giambie ed epoti», «Giambi e ipodi», «le ho di barbare», «Leodi Barbare», «da. Dei fiori» | correggere tutte le righe |
| vtt | testo | vuoti > 3 s: 1:51–1:58, 11:07–11:50, 28:58–29:46, 45:50–46:44 (probabili slide senza voce: da verificare) | controllare |
| 0:00–0:46 | audio | 46 s prima della prima frase (sigla 15 s + copertina) | verificare |
| tutto | formato | 1440p invece di 1080p; picco audio -0,8 dBTP | ricodifica con `finale_a_pezzi.py` |
| — | consegna | mancano dispensa/PDF slide A4, PDF mappe, test finale, compiti, `compiti.json` | produrli (compiti e Excel dalle zip della release) |

## NON verificato (non posso)
- **Ascolto completo (Whisper):** il modello non è scaricabile qui (Hugging Face bloccato, 403). Per ora ho solo il testo del `.vtt` esistente: **non** conferma che audio e immagini coincidano. Non ho potuto controllare frase per frase «ecco / guarda / in questa pagina» (30 occorrenze da controllare).
- Rumore dell'audio del prof (fruscio/ronzio/metallico): non ascoltato.
- Sincronia labbra e card gialle: visto solo a campione sui fotogrammi.

## Perché mi fermo
1. Per rifare grafica 4:3 e slide servono i **sorgenti di montaggio** (slide HTML/timeline) che non sono sul ramo consegna: ci sono solo il video finito e `.vtt`/quiz. Rifarle dal video = ricostruire tutto da zero (>5 h).
2. Mi serve il modello Whisper `small` (o un file da mettere nel repo/release) per l'ascolto.
3. Mappe del prof, compiti, Excel: gli zip non sono nella lista che ho consultato per questa lezione (compiti/Excel sono negli zip generici da aprire).

**Richiesta alla master:** sorgenti di montaggio della lezione 3 (o ok a ricostruire) + modello Whisper. Mi bastano 1 riga.
