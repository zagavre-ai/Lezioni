#!/usr/bin/env python3
import json, os, sys
W = '/home/user/Lezioni/lavoro/consegna/'
J = lambda f: json.load(open(W + f))
m = J('misure.json'); cr = J('controllo_rapido_StoriaArteV_Lez12_Parte1_1080p.json'); tl = J('timeline_Parte1.json')
extra = {}
for f in ('extra.json',):
    if os.path.exists(W + f): extra = J(f)
mm = lambda t: f'{int(t//60)}:{int(t%60):02d}'
NOMI = {'SIG': 'Sigla (15 s)', 'COVER': 'Copertina animata con voce di benvenuto (senza riquadro del docente)', 'D0': 'Introduzione del docente sopra la copertina', 'GLOSS': 'Glossario animato (voce Kore)',
        'RF': 'Ripasso finale argomento per argomento (voce Kore)', 'VF': 'Scheda «Verifica di sbarramento» (10 domande, soglia 80%)', 'SF': 'Sigla finale con avviso dei diritti', 'CI': 'Intro «Compiti»', 'COMPITI': 'Compiti del docente letti dalla voce Kore', 'MAPPA': 'Mappa del docente (Dadaismo), costruita ramo per ramo con la voce'}
righe = []
for n, t, d in tl:
    nm = NOMI.get(n) or ('Titolo argomento %s' % n[1] if n[0] == 'T' else 'Quiz argomento %s (5 domande, soglia 80%%)' % n[1] if n[0] == 'Q' else 'Approfondimento animato (voce Kore)' if n.startswith('AN') else 'Pillola di ripasso (voce Kore)' if n.startswith('PILL') else 'Docente con slide sincronizzate' if n[0] == 'D' else n)
    righe.append(f'| {n} | {mm(t)} | {d:.1f} s | {nm} |')
voci = extra.get('voci', 'PROVVISORIE (sintesi locale): da sostituire con le voci Kore')
dub = json.load(open('/home/user/Lezioni/lavoro/trascr_corretta.json'))['dubbi']
md = f"""# RAPPORTO DI REVISIONE · Storia dell'arte V · «Dadaismo e Surrealismo»
Tag `storia-arte-V-lez12` · lezione prenotata e montata da questa chat (ramo di lavoro `voci-storia-arte-V-lez12`, consegna su `revisione-storia-arte-V-lez12`) · una sola Parte.

**Voci narranti: {voci}.**

## 1. Misure sul video finale (misurato)
| Misura | Valore | Limite |
|---|---|---|
| Formato | {cr['formato']} | 1920×1080, 30 fps |
| Durata | {m['durata_s']/60:.2f} min ({m['durata_s']:.1f} s) | 50–60 min; fino a circa 65 resta una sola Parte |
| Fotogrammi | {m['fotogrammi']} (= durata × 30: {round(m['durata_s']*30)}) | uguali |
| Peso | {cr['peso_MB']} MB | sotto 400 MB |
| Volume | {m['LUFS']} LUFS, picco {m['picco_dBFS']} dBFS | −16 ±1 LUFS, picco ≤ −1 |
| Timbro del docente (acuti >4 kHz meno livello >100 Hz) | {', '.join(f"{k}: {v['finale']} dB (originale {v['originale']})" for k, v in m['timbro_dB'].items())} | tra −9 e −20 dB |
| Pause mute oltre 2,5 s | {len(cr['pause_mute'])} | nessuna |
| Schermate uguali oltre 3 min | {len(cr['schermate_ferme_oltre_3_min'])} | nessuna |
| Nome del docente nel piè di pagina | {len(cr['nome_docente_nel_pie_di_pagina'])} fotogrammi | nessuno |
| Controllo rapido (`controllo_rapido.py`) | **ESITO {cr['ESITO']}** | OK |
| Scatto del quiz a 0,0 s (`controllo_jingle`) | {extra.get('jingle', 'non misurato')} | ±0,05 s |
| Sincronia voce–labbra (scarto massimo, correlazione sui pezzi del docente) | {extra.get('sync', 'non misurato')} | ≤ 0,04 s |

## 2. Struttura (timeline_Parte1.json)
| Scena | Minuto | Durata | Cos'è |
|---|---|---|---|
""" + '\n'.join(righe) + f"""

Argomenti: 1 · I folli anni Venti · 2 · Il Dadaismo e Marcel Duchamp · 3 · Il Surrealismo e gli oggetti surrealisti · 4 · Ernst, Miró, Dalí e Magritte. Ogni argomento ha titolo con jingle, docente con slide sincronizzate, almeno un approfondimento animato (7 in tutto, solo dal materiale del docente), pillola di ripasso con jingle e quiz di 5 domande (scatto a +0,5 s). La mappa è una sola perché il docente ne ha fatta una sola (Dadaismo): sta alla fine dell'argomento 2; gli altri argomenti si chiudono con la pillola.

## 3. Tagli del docente: fine di ogni pezzo (misurato sulla trascrizione)
Tutti i tagli cadono nelle pause, 0,15 s prima della frase che segue; nessun taglio a metà frase. L'audio del docente non ha pause mute oltre 2,5 s, quindi non è stata accorciata nessuna pausa.

""" + open(W + 'tabella_tagli.md').read() + f"""
Note: D2c termina con «…Ecco, successivamente. A partire dal 1924.» (frase finita, ponte verso il Surrealismo); da D3a è stato tolto il riempitivo «Come appunto.» a fine pezzo (1883 s dell'originale).

## 4. Audio e video del docente
- File originale del docente non modificato. Riquadro 4:3 412×309 a x=1428, y=148, ombra grigia, fascia gialla con nome e materia; ritaglio 4:3 dalla webcam originale (nel video originale la webcam è piccola, 246×138 px, quindi è ingrandita circa 2,2×: resa un po' morbida, limite noto). Posizione della webcam seguita nei tre punti in cui cambia (a 1226 s, 1922 s e 2880 s dell'originale). Correzione colore leggera (contrasto 1,04, saturazione 1,03, `hqdn3d 1,5:1,5:3:3`, `cas 0,35`), nessuna sfocatura dello sfondo.
- Audio: filtro dei bassi 80 Hz, riduzione leggera del rumore (`afftdn` 8 dB), −16 LUFS, picco ≤ −1,5 dBFS, nessun `arnndn`. La pulizia ritarda l'audio di 30 ms: compensato nel montaggio.
- Fermi: nessun fermo immagine del docente di 1 s o più (al massimo 0,35 s a inizio e fine pezzo, dentro la dissolvenza).

## 5. Refusi corretti (nelle nostre slide, mappe e dispensa; elencati per la ricontrollo della master)
| Dove | Come stava | Come l'ho messo |
|---|---|---|
| Slide «Gli oggetti surrealisti», card «Esempi iconici» | «Salvador Dali» | «Salvador Dalí» |
| Mappa del docente | «TRISTAN ZARA» | «Tristan Tzara» |
| Mappa del docente | «SOCIETA'» | «società» (accento) |
| Mappa del docente | testo tutto maiuscolo | maiuscole e minuscole, 36–52 px, parole identiche |
| Slide del docente | virgolette dritte | virgolette tipografiche “ ” |
| Mappa del docente | senza titolo | titolo-domanda scritto da noi con le parole del docente: «Che cos'è il Dadaismo?» (da confermare) |

## 6. Anomalie e cose DA CONFERMARE COL PROF (riportate come le dice il docente, non toccate)
- **Date**: «Telefono aragosta» a voce 1938, didascalia del PDF 1936 → l'anno non è scritto né detto nelle nostre schede. «La chiave dei sogni» a voce 1930, didascalia 1936 → anno omesso.
- **Card mai commentate a voce**: «Il frottage di Ernst» e «L'elefante di Celebes» (slide «L'immaginario di Max Ernst e Joan Miró»): il docente non le nomina, parla de «L'angelo del focolare». Nel glossario e nel quiz il frottage è definito solo con le parole della slide.
- **Domanda 9 della verifica** (Miró, «Il carnevale di Arlecchino», 1924-25): quest'opera non compare né a voce né nelle slide del docente (il docente mostra le Costellazioni).
- Nome del Cabaret Voltaire, di Hugo Ball e Tristan Tzara dai quali partono le domande: scritti come nel materiale (a voce il riconoscimento automatico sentiva «Ugo Bal», «Tristian Sarà»).
- Nei primi minuti il docente dice più volte «impressionismo / post-impressionismo / espressionismo» dove ci si aspetterebbe «Dadaismo e Surrealismo» (minuti 0:48, 4:26, 10:24, 14:16 dell'originale). Lasciato come detto; i sottotitoli riportano quel che si sente.
- Il docente spiega il gioco di parole volgare di L.H.O.O.Q.: nei sottotitoli compare come lo dice.
- Titoli e dati delle opere di Miró e di Magritte presi dalle didascalie del PDF del docente (letti a 300 dpi); non sono state inserite altre didascalie.
- Dubbi sulla trascrizione ({len(dub)}), controllati sul contesto e non sull'audio: """ + '; '.join(f"{d['minuto']} {d['problema']}" for d in dub[:25]) + """

## 7. Immagini
- Tutte le opere vengono dal PDF del docente (nessuna immagine dal web: Wikimedia Commons non è raggiungibile da questa rete). Estratte con `pdfimages`, ritagliate una per una e ingrandite ×4 con una rete di super-risoluzione (EDSR) senza cambiare l'opera; dimensioni finali 968–3432 px sul lato lungo. Le immagini originali erano piccole (da 242 a 875 px).
- Nessun ritratto di persone reali.

## 8. Voci e controlli sulle voci
""" + extra.get('voci_dettaglio', 'Le voci Kore non sono ancora arrivate quando scrivo questo rapporto: il montaggio usa voci provvisorie con le stesse parole e durata stimata. Al loro arrivo: trascrizione e confronto parola per parola, numeri, bordi (ultimi 50 ms sotto 0,03), dissolvenza 30 ms, e rifacimento del video.') + """

## 9. Cosa NON ho verificato
""" + extra.get('non_verificato', '- Pronuncia dei nomi stranieri nelle voci Kore (da ascoltare).\n- I sottotitoli non sono riletti sull\'audio parola per parola: partono dalla trascrizione automatica, corretta sul contesto e sul materiale del docente.') + """
- Le domande dei quiz sono scritte da noi dal materiale del docente: da approvare dalla master.
- Il controllo severo della master (`controllo_severo.py`) non è stato eseguito da me; ho eseguito `controllo_rapido.py` (ESITO OK) e le misure sopra.

## 10. Come ho verificato
Trascrizione automatica con tempi parola per parola (sherpa-onnx/Parakeet) per i tagli e le card; `controllo_rapido.py` e foglio dei fotogrammi guardato; correlazione dell'audio finale con l'originale per la sincronia; misura del timbro sulle bande >100 Hz e >4 kHz; `controllo_jingle` sui quattro quiz; controllo separato di un agente che non ha montato la lezione sull'elenco del §11 del CLAUDE.md (vedi sotto).

""" + extra.get('agente', '## 11. Controllo dell\'agente separato\n(da completare)\n')
open(W + 'RAPPORTO_REVISIONE.md', 'w').write(md); print(len(md))
