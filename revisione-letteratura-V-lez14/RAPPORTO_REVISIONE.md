# RAPPORTO REVISIONE · Letteratura V · Lezione 14 (Pirandello) · PRIMA VERSIONE PARZIALE · 16/11/2026
**Stato: NON REVISIONATA.** Questa è una verifica iniziale, non la correzione. Niente è stato ricodificato.

## Misurato
- Video montati ricomposti: Parte 1 = 50:07,5 (sha256 OK), Parte 2 = 48:36,4 (sha256 OK), 1920×1080 h264+aac.
- Originale del prof `Letteratura_Lez14.mp4` = 64:20 (3860 s). Scaricati anche: slide del prof, `Lez14_ingrandita.zip` (HD pagine libro), `MAPPE-…zip`, zip compiti, zip Excel.
- Contact sheet Parte 1 (1 fotogramma/minuto): `controllo_minuti_parte1_parziale.jpg`.

## Problemi trovati finora (Parte 1, a vista, contact sheet + 1 fotogramma a 10:00)
| Minuto | Tipo | Com'è | Correzione necessaria |
|---|---|---|---|
| tutta la lezione | visivo | Punto 000: fondo grigio chiaro + **banda blu scura a destra**, riquadro **rettangolare con bordo blu**, nome bianco su blu in 2 righe (non fascia gialla inclinata) | Rifare tutte le slide con il modello Spagnolo: fondo bianco, riquadro 4:3 con ombra, fascia gialla |
| tutta la lezione | visivo | Etichetta «ARGOMENTO 1 · …» invece di «01 · NOME» | Rifare etichetta |
| tutta la lezione | visivo | Piè di pagina «LETTERATURA ITALIANA · Prof. Giorgio Mazzotti · Pagina N» ok nel testo, ma stile da confrontare col modello | Confronto fine |
| ~3–13 (argomento 1–2) | visivo | Più minuti consecutivi sulla stessa slide con evidenziazione ferma (es. slide «trappola sociale», p. 3, dal min ~6 al ~10) | Verificare sincronia con la voce (±1,5 s); possibile errore tipo lezione 10 |
| approfondimenti, glossario, ripasso | visivo | Fondo blu scuro pieno | Punto 000.7: slide senza prof con fondo bianco |
| mappe | contenuto | Mappe nel video con nodi brevi («I primi grandi romanzi», ecc.) | Da confrontare con le **mappe del prof** (MAPPE zip): non confrontate |
| quiz | visivo | Banda blu su Quiz (nota del brief: «si tiene») | Vedi domanda sotto |

## NON verificato (bloccato)
- **Trascrizione Whisper:** il modello non si scarica (proxy 403 verso il sito dei modelli). Non ho aggirato il blocco. Quindi **non ho controllato** voce↔immagine («ecco/guarda…»), tagli, silenzi, ripetizioni, sincronia labbra, rumore, LUFS.
- OCR: non c'è tesseract nell'ambiente; refusi delle slide e dei .vtt non controllati.
- Parte 2, pagine del libro HD (tabella brano·pagina·file·minuto), PDF slide/mappe A4, quiz/test/compiti/scheda: non verificati. `compiti.json` esistente: 4 domande aperte, da confrontare col PDF del prof.
- Strumenti `kit/tools/rettangolo` non usati: servono per il vecchio rettangolo; la forma 4:3 va rifatta dall'originale.

## Piano di correzione (stima, non misura)
Rifare in grafica Spagnolo tutte le slide (circa 100 minuti di video in due Parti), ritagliare il prof 4:3 dall'originale con la correzione del kit, ripulire l'audio, reinserire pagine HD, rigenerare PDF. Serve la pipeline di produzione originale e un modello Whisper: **più delle 5 ore** nell'ambiente attuale.
