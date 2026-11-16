# RAPPORTO DI REVISIONE · Letteratura italiana V · Lezione 1 · PRIMA VERSIONE
Stato: **IN REVISIONE** · versione 1 del 16/11/2026 · prof. Giorgio Mazzotti

> **Non è ancora consegnata.** Questa è la prima versione (verifica + piano). La correzione non è fatta: c'è un blocco tecnico (punto 4) e la lezione va rifatta quasi tutta nella grafica.

## 1. Cosa ho verificato e come
| Cosa | Come | Misurato / stima |
|---|---|---|
| Video montato | 3 pezzi ricomposti, sha256 uguale a quello nel ramo `consegna-…` | misurato: OK, 63:53,8, 1920×1080, 30 fps, 264 MB |
| Visione | un fotogramma ogni 30 s per tutta la durata (128 fotogrammi, vedi `controllo_minuti_0…5.jpg`) e confronto con `kit/modello_spagnolo/` | misurato (a vista) |
| Originale del prof | `Letteratura_Lez1.mp4` dalla release | misurato: **42:09, 1092×614** (bassa risoluzione) |
| Sottotitoli | lettura del `.vtt` (2101 righe) | misurato |
| Materiali | HD pagine libro, mappa del prof, compiti, Excel | misurato |
| **Ascolto (trascrizione Whisper)** | **NON fatto**: vedi punto 4 | non verificato |
| OCR di tutte le slide, sincronia ±1,5 s, labbra, LUFS, rumore | **NON fatti** (dipendono dalla trascrizione e dal rifacimento) | non verificato |

## 2. Confronto con il modello Spagnolo (punto 000, 1–11)
| # | Punto | Esito | Com'è |
|---|---|---|---|
| 1 | Sigla → dissolvenza → copertina | **DA CORREGGERE** | Sigla 0:00–0:15 OK. Poi a 0:30 compare una slide scura con gli argomenti 4–6 (non della lezione 1), a 1:00 la copertina. A 2:00–2:15 un fondo blu vuoto con solo il logo |
| 2 | Copertina (logo, DM Mono, titolo+barretta, card «ARGOMENTI») | **DA CORREGGERE** | Copertina con solo titolo e «Prof. Giorgio Mazzotti»: **mancano gli argomenti**, e resta ferma da 0:56 a 2:15 mentre il prof presenta il corso |
| 3 | Slide fondo bianco, «01 · ARGOMENTO», barretta, card/tabelle | **DA CORREGGERE** | Fondo grigio-azzurro; le slide hanno in alto «ARGOMENTO …» non numerato come da modello; card con bordo giallo ovunque; schemi, ripassi, glossario e riepilogo su **fondo blu scuro** (stile non Spagnolo) |
| 4 | Piè di pagina «LETTERATURA ITALIANA V · Prof. Giorgio Mazzotti» + «Pagina N» | **DA CORREGGERE** | Manca la «V» e manca «Pagina N» a destra; c'è «Pagina 1…9» ma al centro-destra e la numerazione ricomincia |
| 5 | Riquadro 4:3 ≈410×308, ombra grigia, nessun bordo blu | **DA CORREGGERE** | Riquadro piccolo (~16:9) dentro una **banda blu notte** laterale: vietato dal brief («niente bande laterali blu») |
| 6 | Fascia gialla inclinata, due righe | **DA CORREGGERE** | Il nome è un testo piccolo bianco su blu, illeggibile (come segnala Sara). Manca la fascia gialla −3° |
| 7 | Slide senza prof | **DA CORREGGERE** | Fondo blu notte, parole in giallo ok ma stile diverso dal modello |
| 8 | Font Bricolage / Figtree / DM Mono | da controllare | A vista simili, non verificato con OCR |
| 9 | Finale `Sigla_finale_5s_con_avviso_diritti.mp4` | **DA CORREGGERE** | Il video chiude con una slide «I compiti della lezione» su blu a 63:30 e non c'è la sigla finale col testo dei diritti (da riverificare sul file) |
| 10 | Struttura | parziale | Ci sono: sigla, argomenti, approfondimenti, schemi di ripasso, mappe, glossario, riepilogo. Il quiz risulta fuori dai miei fotogrammi: da riverificare |
| 11 | PDF slide A4 + PDF mappe A4 | **DA RIFARE** | Esiste una dispensa A4 e `Mappe_…pdf`, ma le slide del video cambiano (vedi sopra) e la mappa non è quella del prof |

## 3. Problemi trovati (finora)
| Minuto | Tipo | Com'era | Come si corregge |
|---|---|---|---|
| 0:30–1:00 | visivo | slide con argomenti 4-6 dentro la sigla/copertina | togliere; copertina con tutti gli argomenti della lezione |
| 0:56–2:15 | visivo | il prof presenta il corso, a schermo la sola slide del titolo (come segnalato) | copertina con card «ARGOMENTI» e evidenziazione sincronizzata |
| 2:00–2:15 | visivo | fondo blu quasi vuoto con solo il logo | slide corretta |
| 2:15–7:00 e oltre | visivo | slide avanzano prima/dopo la voce del prof (come segnalato) | rifare la sincronia su trascrizione con i tempi |
| 1:00–63:00 | visivo | banda blu notte a destra, riquadro piccolo, nome illeggibile | riquadro 4:3 + fascia gialla come Spagnolo |
| 9:00, 17:30, 45:00, 45:30 | visivo | titolo «MAPPA CONCETTUALE» tagliato in alto; mappa dell'argomento 1 e 2 **inventate** (a 45:00 la mappa ha solo 2 rami, a 45:30 diventa piena) | usare **solo la mappa del prof** (vedi punto 5) |
| 36:00–62:30 | testo | «Charles **Bodlèr**» (nome sbagliato: Baudelaire), «**Splin**» (Spleen) in schemi e glossario, «Rinuncia/Bodlèr» nel ripasso e nei `.vtt` | correggere: Baudelaire, Spleen |
| 45:30–46:30 | visivo | a 46:30 fondo blu vuoto con sola un'ombra (probabile transizione troppo lunga) | transizione ≤ 1 s |
| 63:30 | visivo | ultima slide «Compiti» invece del finale standard | aggiungere finale da kit |
| tutto il `.vtt` | testo | errori tipo «lettatura», «ben umale il metesimo», «le tà del naturalismo», «Bodlèr», «losplin» (2101 righe da rileggere) | rifare con trascrizione + glossario dei termini |
| 0:00 – fine | audio | non ascoltato | da verificare dopo la trascrizione (-16 LUFS e rumore) |
| tutta la lezione | pagina | il prof legge **Corrispondenze** (Baudelaire): negli screen HD ci sono 5 pagine (p. 24, 26, 28, 30, 31). Nel video **non vedo nessuna fettina HD** nei miei fotogrammi | inserire le fettine a tempo con la voce (ho le pagine; serve la trascrizione per i minuti) |

## 4. Blocchi (per la master)
1. **BLOCCO TRASCRIZIONE:** non riesco a installare Whisper: il modello `small` si scarica da `huggingface.co` e il proxy della sessione lo rifiuta (403). `pip` funziona, i modelli no. Serve: **(a)** sbloccare `huggingface.co` per questa sessione, **oppure (b)** che la master carichi il modello (cartella `faster-whisper-small`) o la trascrizione `Letteratura_Lez1.mp4` con i tempi nella release/ramo voci. Senza trascrizione non posso rifare sincronia, sottotitoli, né inserire le fettine HD.
2. **Il montaggio non si rifà dal video attuale:** le slide sono già dentro il video, con il prof ritagliato (banda blu). Per avere il riquadro 4:3 e il fondo bianco devo rigenerare le slide e ricomporre dall'originale (**1092×614, bassa risoluzione**: nel riquadro 410×308 va bene). Non ho nel repository gli script di produzione delle slide della prima versione né le scene (`timeline.json` c'è, la guarderò). Chiedo conferma alla master: ripartire da `timeline.json` + `testi_voci.json` + voci Kore del ramo voci, e rifare le slide con la grafica Spagnolo.
3. Le voci Kore (ramo `voci-letteratura-V-lez01`) si riusano; frasi nuove solo se servono.

## 5. Materiali D (controllati)
- **Mappa del prof (lezione 1):** `MAPPE/LEZIONE 1.pdf`, **1 sola pagina**: «Charles Baudelaire (1821–1867)». Copre solo l'argomento 5-6 (Baudelaire). Per gli altri argomenti **non c'è mappa del prof** → lo scrivo a Sara (non si inventa). Il video attuale ha 3 mappe (una per argomento): quelle degli argomenti 1–4 sono inventate e vanno tolte o sostituite.
- **Compiti:** nello zip `LETTERATURA.ITALIANA.V.-…zip`, file «LEZIONE 1.pdf»: da trasformare in `compiti.json`.
- **Verifica finale:** `DOMANDE LEZIONE 1.xlsx` nello zip Excel: da trasformare in 10 domande.
- **HD pagine del libro (Lez01):** p. 24 «T1 Corrispondenze» (da *I fiori del male*), p. 26, 28, 30, 31 (screen 2370×3153).

## 6. Piano di correzione (stima, non misurata)
| Fase | Tempo stimato |
|---|---|
| Sbloccare/ottenere trascrizione e rifare sottotitoli | 40 min dopo il via |
| Rigenerare slide in grafica Spagnolo (copertina, 6 argomenti, ripassi, glossario, riepilogo) | 1 h 30 |
| Riquadro 4:3 + fascia gialla, correzione immagine, audio pulito | 1 h |
| Sincronia slide–prof su trascrizione + fettine HD | 1 h |
| Codifica, controlli, PDF A4, rapporto finale | 1 h 15 |
| **Totale** | **≈ 5 h 25 dal via**: **fuori dai 4 h** previsti; sta nei 5 h solo con il blocco 1 risolto subito |

## 7. Cosa NON ho potuto verificare
Ascolto/trascrizione, rumore, LUFS dei pezzi, sincronia labbra, testa tagliata nell'originale, OCR delle slide, esistenza del quiz nel video (non nei fotogrammi ogni 30 s), PDF slide ↔ video.
