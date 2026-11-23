# Compone RAPPORTO_REVISIONE.md: parti misurate (rapporto.py) + parti scritte. VOCI=vere|provvisorie
import os, subprocess, sys, json, re
W = '/tmp/claude-0/l15'; OUT = W + '/out'; V = os.environ.get('VOCI', 'provvisorie')
subprocess.run(['python3', W + '/rapporto.py'], capture_output=True, cwd=W)
parti = open(OUT + '/_rapporto_parti.md').read()
cs = ''
if os.path.exists(OUT + '/cs_final.txt'):
    t = open(OUT + '/cs_final.txt').read(); j = json.loads(t[t.index('{'):])
    cs = '\n**Controllo severo della master (`controllo_severo.py`), esito: %s** [misurato]. Copertina %s; schermate identiche oltre 3 min: %s; slide con lo stesso titolo oltre 3 min: %s; card sole oltre 60 s: %s; pause oltre 2,5 s: %s; loudness %s LUFS; tono della voce (6 campioni, Hz): %s.\n' % (j['ESITO'], 'con titolo intero' if j['copertina_titolo_presente'] else 'NON OK', len(j['schermata_identica_oltre_3min']), len(j['slide_stesso_titolo_oltre_3min']), len(j['una_card_sola_oltre_60s']), j['silenzi_oltre_3s'], j['lufs'], j['voce_tono_hz'])
voci = ('Voci Kore definitive controllate (trascritte e confrontate, bordi misurati). **Unica provvisoria: CHIUSURA_COMPITI** («Svolgi i compiti qui sotto e premi Consegna: arrivano al docente nel tuo quaderno dei compiti»), richiesta alla master il 23/11 dopo la nuova regola: nel video c\'è un tono al suo posto, la frase è già sullo schermo.' if V == 'vere' else
        '**ATTENZIONE: nel video ci sono ancora voci PROVVISORIE** (un tono al posto di BEN_R2 «benvenuto», DP «Di cosa parliamo» e CPT1-4 «compiti»), e per le 11 voci da rifare e le 5 con le sigle rispiegate sono usate quelle vecchie. La lezione NON è definitiva finché la master non manda le voci: le richieste sono nel ramo `voci-storia-V-lez15` (testi_voci.json: BEN_R2, DP, CPT1-CPT4, PI3_R2, SC6_1_R2, SC10_1_R2, GL1_R2, GL3_R2, GL4_R2, GL7_R2, AN5_R2, AN7_R2, AN8_R2, AN9_R2, SC7_2_R3, SC8_2_R3, SC10_4_R3, AN15_R3, AN20_R3). Appena arrivano si rifà il montaggio (un solo comando).')
man = f'''
{cs}
## 4 · Voci Kore
{voci}
- Controllo fatto sulle 115 voci esistenti (trascrizione e confronto parola per parola [misurato]): differenze solo di numeri scritti in cifre dall'ASR; voci da rifare perché sbagliate o con bordo finale ≥ 0,03: **GL1** (il file era il glossario intero di 33 s), **SC6_1, AN7, AN8, AN9** (troncate, ampiezza finale 0,10-0,23), PI3, SC10_1, GL3, GL4, GL7, AN5 (0,03-0,07). AN8 anche «DA CONTROLLARE» dalla master.
- Ogni voce nel montaggio: silenzio di testa/coda tolto, dissolvenza 30 ms, −16 LUFS.
- Pronuncia dei nomi stranieri (Dien Bien Phu, Vietminh, Nkrumah, Mau Mau, Ceylon…): non ascoltata [non verificato]; l'ASR legge «Dien Bien Phu» come «bian fu» in AN8.

## 4b · Correzioni della master del 23/11 01:15 (RESPINTA, rifatto)
1. **Pillole di ripasso**: ora a tutto schermo in blu scuro (come la scheda RIPASSO), 4 righe sempre visibili che si accendono in giallo con la voce (prima: tabella su fondo bianco con una riga sola nei campioni a 42:22 e 57:47) [misurato: controllo_rapido OK, foglio guardato].
2. **Cartine del prof grandi**: «La decolonizzazione dell'Africa» (pagina 11 del PDF) e «L'inizio della questione palestinese» (pagina 13) ora a tutta altezza nell'area slide (area 1316×716 px invece di 1290×630), dal file del prof (non c'è sorgente migliore nel PDF); per l'Africa lo zoom si sposta in 6 zone seguendo ciò che dice il prof (Liberia, Africa francese, britannica, italiana, portoghese, intera). Tolti il QR «Atlante interattivo» (non funzionante) e il cerchietto sul bordo sinistro. Sorgenti piccole (777×610 e 1037×637): ingrandite, leggibili ma morbide.
3. «Check» → «Rispondi · premi Controlla · poi Continua» sulle schede quiz e verifica.
4. Compiti: compaiono uno alla volta con bordo giallo mentre la voce li legge; in fondo la frase «Svolgi i compiti qui sotto e premi Consegna…» (voce provvisoria).
5. `controllo_rapido.py`: ESITO OK; foglio e json sul ramo (`foglio_fotogrammi_…jpg`, `controllo_rapido_….json`); foglio guardato.

## 5 · Cosa è stato rifatto (correzioni 22/11)
1. **Slide del prof**: card a 40 px, interlinea 1,5, finestre da 3 card (4 card del prof → due sotto-slide «a finestra» che si sovrappongono; argomento 10: finestre da 2 card perché le sigle espanse non entrano); card intere dal PDF del prof; bordo giallo + pallino all'inizio della frase (cue ricavati a mano dalla trascrizione). Fondo bianco, riquadro 4:3 (412×309 a x=1428, y=148), fascia gialla col nome solo lì; piè di pagina senza il nome del docente.
2. **Copertina** animata senza riquadro del prof (titolo esatto «La decolonizzazione (1945-1975)» + voce di benvenuto), poi introduzione del prof sulla copertina (106,7 s) col riquadro che compare quando parla, poi slide animata «Di cosa parliamo» senza riquadro.
3. **Nome del docente** mai detto né scritto nelle animazioni (BEN rifatta come BEN_R2).
4. **Mappe: nessuna.** Per la lezione 15 il PDF «MAPPE LEZIONE 15» non esiste (indice master); come da risposta della master non ne ho inventate: ogni argomento chiude con pillola di ripasso e schema; niente PDF delle mappe.
5. **Verifica di sbarramento** (scheda con jingle a +0,5 s, 10 domande dal test Excel del prof) e **Compiti** (intro 3,5 s + 4 compiti del prof letti e mostrati, 2 per schermata) ora sono dentro il video, dopo la sigla finale per i compiti. I compiti vengono dal file «LEZIONE 15.pdf» dello zip dei compiti (testo identico) [misurato].
6. **Audio del prof** rifatto dall'originale: passa-alto 70 Hz, riduzione del rumore leggera, normalizzazione dinamica a −17,1 LUFS, poi mix a −16,0 LUFS; timbro (media >4 kHz meno media >100 Hz) −17,0 dB nel video contro −17,5 dB dell'originale [misurato] (limite −9…−20). Pause del prof oltre 2,5 s accorciate a circa 1 s; tolte le ripetizioni e i riempitivi: «Per il loro. Per le loro.», «L'Indonesia appunto», «Um» ×4, «Perché ehm», «Come dire ehm», «Mm» ×2. Tagli del parlato a fotogramma intero con dissolvenze di 10 ms.
7. **Riordino delle digressioni** (niente «già visto»): nel video originale il prof, parlando dell'Africa subsahariana, salta alle colonie portoghesi e poi al Maghreb/Gheddafi (pagine 10 e 8 del suo PDF). Le parole sono intere e nello stesso ordine, ma i due blocchi sono stati spostati: il Maghreb con la foto di Gheddafi in fondo all'argomento 5, le colonie portoghesi in fondo all'argomento 7. Così ogni slide e immagine del prof compare in un solo argomento.
8. **Sigle rispiegate sullo schermo** (BES): ONU, USA, URSS, FLN, ANC, FMI, NATO, UNESCO espanse tra parentesi in card, schemi, glossario, approfondimenti, chip dei titoli e quiz. A voce le ho spiegate nelle nostre voci (SC7_2, SC8_2, SC10_4, AN15, AN20 → versioni _R3). **Il prof a voce non le spiega e non si tocca**: nei tratti del docente la spiegazione è solo sullo schermo.
9. **Approfondimenti**: 2 per argomento (voci Kore, solo materiale del prof); per argomento 40-48 s con le pause di lettura. Sono slide di testo che si accendono con la voce, senza immagini: dichiarato.
10. **Quiz**: 10 schede da 5 domande, scatto a +0,5 s misurato +0,003 s su tutte; titolo dell'argomento ridotto per non toccare il pulsante; tolto «Check» dalle istruzioni.
11. **Sottotitoli** sul video finale: 862 blocchi, inizio agganciato all'attacco reale della voce; corretti a regole: Siria, URSS, ONU, Vietminh, Indonesia, guerra civile, Re Idris I, Gandhi, Nehru, Bandung, Dien Bien Phu, Gheddafi, Mandela, apartheid, Ceylon, Ghana, ecc. Non riscritto il parlato: restano forme del parlato e qualche errore dell'ASR in frasi dubbie (es. «un'esplosione belli», «messo nel suo Mandela si»), non corretti per non inventare.
12. **Dispensa** A4 orizzontale, 62 pagine: stesse slide del video, stessa numerazione, a tutta larghezza, con strato di testo invisibile (modo di rendering 3) in ogni pagina; copertina con sola materia e titolo; piè di pagina «STORIA V» e numero; nessun nome del docente. Senza riquadro del docente né parole chiave. Non c'è il PDF delle mappe (nessuna mappa).

## 6 · Controllo dell'agente separato (primo giro, sul video precedente) e correzioni
| Difetto trovato | Stato |
|---|---|
| Slide/immagini del prof in due argomenti (pagine 32 e 33 dentro l'argomento 6) | corretto: riordino digressioni (punto 7) |
| Taglio a metà frase argomento 3 («…con gli hindu» / «o gli induisti…») | corretto: taglio dopo «…violenti scontri» |
| Glossario che esce dalla slide | corretto: righe più basse, tutte dentro |
| Sigle non rispiegate | corretto sullo schermo; voci _R3 richieste; **resta aperto a voce nei tratti del prof** |
| Approfondimenti sotto i 40 s per argomento | corretto con pause di lettura (non con nuovo contenuto) |
| Titolo quiz sul pulsante; titolo «Verifica» doppio; parola «Check» | corretti |
| Errori nei sottotitoli, «Um», ripetizioni | corretti (vedi punti 6 e 11) |
| Card accesa 1,75 s prima a 346 s | corretto (cue spostato a 283,4 s sorgente) |
| GL4 con anno in cifre nel testo per la voce | corretto (GL4_R2 in lettere) |
| «Scheda nera GRAZIE PER L'ATTENZIONE» dopo i compiti | è la sigla finale ufficiale del kit con l'avviso dei diritti: **da confermare dalla master** |
| QR «Atlante interattivo» e cerchietto bianco nelle mappe del prof | **non corretto**: sono nell'immagine sorgente del prof (non si modifica) |

## 7 · Immagini e refusi
- Tutte le immagini sono quelle del PDF del prof (pagine 6, 8, 11, 13, 15), **nessuna scaricata dal web**. Le sorgenti sono piccole (246×377, 330×387, 396×446, 777×610, 882×766, 1037×637): ingrandite 2× con Lanczos e nitidezza (la foto di Gheddafi, 330×387, ugualmente): leggibili ma morbide [giudizio visivo]. Non si può fare di più senza altre sorgenti.
- Refusi: confrontando le card con il PDF del prof non ci sono differenze di testo [misurato dall'agente separato: 0 differenze]; non ho trovato refusi da correggere nelle slide. Anomalie di numeri o contenuti: non analizzati oltre il confronto card/PDF [non verificato]; le slide sono riportate come le scrive il prof.

## 8 · Tempi dei pezzi e struttura
Durata 61:38 (una sola Parte, sotto i 65 min: nessuno spiegone). Struttura: sigla, copertina, intro del prof, «Di cosa parliamo», per ogni argomento: titolo con jingle, prof + slide (2 o 3 tratti), 2 approfondimenti Kore, pillola, schema a 4 righe, quiz; poi glossario, riepilogo, verifica, sigla finale, Compiti.

## 9 · Non verificato
- Sincronismo labbra/voce a 0,04 s: audio e video del prof escono dallo stesso istante sorgente, a fotogramma intero [per costruzione]; non misurato col viso (la correlazione movimento/voce non dà picchi).
- Pronuncia dei nomi stranieri nelle voci; ascolto delle voci narranti.
- Funzionamento dell'80% dei quiz sulla piattaforma.
- File originali del prof non modificati [per costruzione: lavoro solo su copie].
- Che trans.wav sia presente a ogni cambio: per costruzione sì (mix); la correlazione automatica dell'agente non l'ha trovato.
'''
open(OUT + '/_rapporto.md', 'w').write(parti + '\n' + man)
print(len(parti + man), 'caratteri')
