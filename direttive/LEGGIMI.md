# Direttive operative per i docenti

Sorgenti dei due documenti che la Coordinatrice Didattica trasmette ai docenti.

| File prodotto | Contenuto |
|---|---|
| `Direttive_operative_Docente.pdf` | Accesso, calendario, videolezioni, lezione in diretta, registrazione, registro, assenze, voti, compiti, studenti BES |
| `Direttive_operative_Responsabile.pdf` | Monitoraggio degli studenti: avanzamento delle videolezioni e scadenze dei programmi |

## Come si rigenerano

Servono `node` con Playwright e `python3` con PyMuPDF e Pillow.

```bash
node copertine_b.js   # le due copertine blu
python3 indice.py     # i documenti, con indice e segnalibri
```

```bash
python3 -c "
import indice
indice.innesta_copertina('Direttive_operative_Docente.pdf', 'copb_docente.pdf')
indice.innesta_copertina('Direttive_operative_Responsabile.pdf', 'copb_responsabile.pdf')"
```

L'ultimo passo sostituisce la prima pagina con la copertina a piena pagina, senza
toccare la numerazione delle altre.

## I file

| File | A cosa serve |
|---|---|
| `docente.html`, `responsabile.html` | Il testo dei due documenti |
| `stile.css` | Grafica comune: colori, caratteri, riquadri, tabelle, indice |
| `copertina_b.html` | Modello della copertina; i testi li mette `copertine_b.js` |
| `indice.py` | Genera il PDF, legge dove cade ogni sezione, riscrive l'indice con i numeri giusti e aggiunge i segnalibri. Ripete finché i numeri non cambiano più |
| `pdf.js`, `pdf_resp.js` | Impostazioni di stampa e piè di pagina |
| `img/` | Schermate della piattaforma e del Quaderno, logo, fondo della copertina |

I caratteri sono quelli del kit: `../kit/caratteri/` (Figtree e Bricolage Grotesque).

## Regole rispettate

- Le schermate degli studenti hanno nomi, telefoni e indirizzi oscurati.
- Nessuna credenziale compare nei documenti né nelle immagini.
- Ogni sezione comincia su una pagina nuova; elenchi e tabelle non si spezzano.
- L'indice è cliccabile e i segnalibri si aprono dal pannello laterale del lettore.

## Cosa manca

- Schermate `R1`–`R9` per il profilo Responsabile: al loro posto ci sono i riquadri
  tratteggiati con il codice.
- Schermate della condivisione schermo, da aggiungere alla sezione sulla lezione in
  diretta (servono per le mappe e per le slide).
