import json,re,os
OUT='/tmp/w14/out'
def mm(x): return '%d:%04.1f'%(x//60,x%60)
def sil(P):
    L=open(f'{OUT}/silenzi{P}.txt').read();tl=json.load(open(f'/tmp/w14/tlnew{P}.json'))
    r=[]
    for e,d in re.findall(r'silence_end: ([\d.]+) \| silence_duration: ([\d.]+)',L):
        e=float(e);d=float(d);s=e-d;pc=[n for n,a,dd in tl if a-1.7<=s<=a+dd]
        r.append(f'{mm(s)}–{mm(e)} ({d:.1f} s) · pezzo {pc[0] if pc else "?"}')
    return r
def fermi(P):
    L=open(f'{OUT}/fermi{P}.txt').read();tl=json.load(open(f'/tmp/w14/tlnew{P}.json'))
    st=[float(x) for x in re.findall(r'freeze_start: ([\d.]+)',L)];du=[float(x) for x in re.findall(r'freeze_duration: ([\d.]+)',L)]
    r=[]
    for s,d in zip(st,du):
        pc=[n for n,a,dd in tl if a<=s<a+dd]
        if pc and pc[0].startswith('D'): r.append(f'{mm(s)} ({d:.1f} s) · {pc[0]}')
    return r
def loud(P): return ' · '.join(x.strip() for x in open(f'{OUT}/loud{P}.txt').read().strip().split('\n'))
old={1:json.load(open('/tmp/w14/tl1.json')),2:json.load(open('/tmp/w14/tl2.json'))}
new={1:json.load(open('/tmp/w14/tlnew1.json')),2:json.load(open('/tmp/w14/tlnew2.json'))}
dur={1:json.load(open('/tmp/w14/as1/tl_new.json'))['frames']/30,2:json.load(open('/tmp/w14/as2/tl_new.json'))['frames']/30}
def tabsec(P):
    on={n:a for n,a,d in old[P]};nn={n:a for n,a,d in new[P]};rows=[]
    for n in nn:
        if (n[0] in 'TQ' and n[1:].isdigit()) or n in('VER','CI1','COMP','GL1','RF1'):
            rows.append(f'| {n} | {on[n]:.1f} | {nn[n]:.1f} | {nn[n]-on[n]:+.1f} |')
    return '\n'.join(rows)
fine=open(f'{OUT}/tabella_fine_pezzi.md').read()
R=f"""# RAPPORTO REVISIONE · Letteratura italiana V · Lezione 14 · Pirandello (2 Parti)
Revisione del 16–17/11/2026. Video: `Letteratura_Lez14_Parte1_1080p.mp4` e `…Parte2…` (a pezzi `.parte_00…`, sha256 nei `.sha256`).
**misurato** = misurato con uno strumento · **stima** = dedotto · **non verificato** = non ho potuto.
**Stato: consegna con riserve** (sezione 5 e DA DECIDERE): non dico «tutto perfetto».

## 1. Misure sul video nuovo (misurato)
| Controllo | Parte 1 | Parte 2 |
|---|---|---|
| Formato | 1920×1080, 30 fps, x264 veryfast CRF 19, AAC 192k | uguale |
| Durata | {mm(dur[1])} ({dur[1]:.2f} s, {round(dur[1]*30)} fotogrammi) | {mm(dur[2])} ({dur[2]:.2f} s, {round(dur[2]*30)} fotogrammi) |
| Vecchia durata | 50:07,5 (90 226 fotogrammi) | 48:36,4 (87 491 fotogrammi) |
| Peso | {os.path.getsize('/tmp/w14/as1/finale.mp4')/1e6:.1f} MB | {os.path.getsize('/tmp/w14/as2/finale.mp4')/1e6:.1f} MB |
| Volume intero file (ebur128) | {loud(1)} | {loud(2)} |
| Audio del prof | pulito dall'originale con la catena del kit (`aresample 48000, highpass 80, arnndn sh.rnnn, loudnorm, alimiter`): −16,9 LUFS integrato, picco −2,0 dBTP (misurato sull'intero originale pulito) | uguale |
| Jingle Quiz a 0,0 s (`controllo_jingle.py`) | Q1–Q4: scarti −0,001…−0,004 s · OK | Q1–Q6: scarti −0,001…−0,006 s · OK |
| Altri jingle (correlazione col kit) | titolo 4/4 · ripasso 4/4 · transizione 5/5 | titolo 6/6 · ripasso 6/6 · transizione 7/7 |
| Silenzi > 3 s | {len(sil(1))}: {'; '.join(sil(1)) or 'nessuno'} | {len(sil(2))}: {'; '.join(sil(2)) or 'nessuno'} (solo schede di servizio Verifica e Compiti, vecchie) |
| Fermi immagine del prof (`freezedetect` sul solo riquadro, −55 dB, ≥ 0,7 s) | nessuno nei 5 pezzi D (misurato) | nessuno nei 7 pezzi D (misurato) |
| Sincronia audio del prof con l'originale | scarto massimo 0,5 ms su 36 punti (3 per pezzo D) | uguale |
| Sottotitoli | `.vtt` rigenerati dall'audio del video nuovo: {sum(1 for l in open(f'{OUT}/Letteratura_Lez14_Parte1.vtt',encoding='utf-8') if '-->' in l)} cue, max 2 righe da ≤43 caratteri | {sum(1 for l in open(f'{OUT}/Letteratura_Lez14_Parte2.vtt',encoding='utf-8') if '-->' in l)} cue |
| PDF | slide: 19 pagine A4 orizzontale | slide: 22 pagine; mappa del prof: 1 pagina (`…_mappe.pdf`) |
Le **durate sono cambiate** (decisione di Sara 17/11): la Parte 1 è **sotto i 50 minuti**, la Parte 2 anche. Vedi DA DECIDERE.

## 2. Confronto col modello Spagnolo (punto 000)
| # | Punto | Esito |
|---|---|---|
| 1 | Sigla → dissolvenza → copertina | sigla invariata; dissolvenze rifatte tra tutti i pezzi, con `trans.wav` |
| 2 | Copertina (logo, riga «LETTERATURA ITALIANA V · VIDEOLEZIONE», titolo, card ARGOMENTI) | **corretto**. Nella presentazione (voce di benvenuto) niente riquadro del prof: non parla |
| 3 | Slide: fondo bianco, «01 · ARGOMENTO», titolo+barretta, card | **corretto** per tutte le slide del prof |
| 4 | Piè di pagina + «Pagina N» | **corretto** (numerazione progressiva per Parte, copertina = 1) |
| 5 | Riquadro 4:3 con ombra grigia morbida, senza bordo | **corretto**: 412×309 px a x=1428 y=148, angoli r=18, correzione immagine del kit |
| 6 | Fascia gialla −3°, due righe | **corretto**, sempre visibile mentre parla il prof |
| 7 | Slide senza prof | **corretto** per approfondimenti, pillole di ripasso, glossario e riepilogo: rifatti nel modello (fondo bianco, card numerate, card in corso gialla, piè con «Pagina N»). **Non rifatte**: schede Quiz, Verifica, Compiti e finale (banda blu, come da prompt) |
| 8 | Font Figtree Bold / Bricolage 800 | corretto sulle slide rifatte (etichette in Figtree Bold) |
| 9 | Finale 5 s con avviso diritti | invariato (presente) |
| 10 | Struttura | mantenuta; **tolte le 12 mappe nostre**, inserita 1 mappa del prof con voce R1 (Parte 2) |
| 11 | PDF slide + mappe A4 orizzontale | slide: 19 + 22 pagine (prof, ripassi, glossario, riepilogo, approfondimenti; senza riquadro); mappe: sì. Non confrontate una per una col video |
Card in corso: bordo giallo sottile + numero su pallino giallo, fondo bianco, altre card con bordo grigio chiaro; ombre grigie morbide (richiesta di Sara 17/11 01:30).

## 3. Problemi trovati e correzioni
| Minuto (vecchio video) | Tipo | Com'era | Correzione |
|---|---|---|---|
| inserti (≈ 25 pezzi) | visivo | approfondimenti, pillole, glossario, riepilogo nella vecchia grafica scura | rifatti nel modello; testo dei ripassi/glossario/riepilogo = testo letto dalla voce; approfondimenti ricostruiti dalle schede vecchie (OCR + correzioni a mano) |
| tutta la lezione | visivo | banda blu a destra, riquadro rettangolare con bordo blu, nome bianco su blu, etichetta «ARGOMENTO 1 ·» | rifatte tutte le slide del prof nel modello (punti 000) |
| P1 ≈ 4:00–8:00 (contact sheet) | sincronia | evidenziazione ferma sulla card 1 per minuti | evidenziazioni ricalcolate dal parlato (stima: parole chiave di ogni card nella trascrizione, percorso monotono; ogni card si accende) |
| tutta la lezione | sincronia | slide scelte dal video vecchio | la sequenza delle slide ora segue lo schermo dell'originale (il prof torna più volte tra le slide 3 e 4: nell'originale ai minuti 8:50, 13:30, 14:33, 15:05) |
| 10 confini su 11 tra pezzi del prof | audio | il pezzo del prof finiva a **metà frase** (da +0,9 a +9,1 s prima della fine frase) e il pezzo seguente ripeteva parlato | tutti i confini spostati sulla fine frase (pausa ≥0,45 s, minimo di energia); tabella in fondo |
| 6 punti: P1 D3 (30:38) e D4 (40:22); P2 D3 (11:02), D4 (15:06), D5 (23:18), D6 (30:56) del video vecchio | audio | **ripetizione** di 0,8–1,9 s di parlato del prof dopo gli inserti (misurata con gli offset costanti) | tolta: i pezzi D sono contigui nell'originale |
| P2 1:00–1:10 | visivo | per 3 s la slide di «Uno, nessuno» con etichetta del teatro | ora copertina Parte 2 |
| P1 (5 pezzi AN03/06/09/11/12) · P2 (7 pezzi AN02/04/06/08/10/12/13) | grafica | 12 mappe fatte da noi con nodi non del prof | tolte (con la loro voce); inserita la mappa del prof nella Parte 2 ({mm([s for n,s,d in new[2] if n=='R1'][0])} del video nuovo, 120 s) |
| P2 Ciàula e Belluca (pezzi D4–D6) | pagina | pagina del libro piccola nel video | fettina dagli screen HD (vedi §4) |
| vtt | testo | 470 cue da un riconoscimento mediocre (es. «Piranvello», «lettratura», «pire andere»), tempi sfasati fino a 1 s | rigenerati dall'audio del video nuovo; nomi corretti: Ciàula, Meis, Moscarda, zi' Scarda, Casinò |
| scheda | testo | titolo «Pirandello · Parte 1»; argomento 2 «La visione del mondo e la trappola sociale» (≠ video), 3 «I primi grandi romanzi» | titolo standard «Letteratura V · Lezione 14 · Pirandello · Parte N», titoli argomento allineati al video, secondi aggiornati |
| audio | audio | la catena di pulizia del kit non era verificabile sul video vecchio | audio dei pezzi del prof rifatto dall'originale con la catena del kit |
| audio | jingle | transizioni e ripasso non rilevati dalla correlazione | `trans.wav` in ogni transizione, `repaso.wav` prima delle pillole |
Quiz: 5 domande per argomento già presenti; ho allineato i titoli. Verifica finale: le 10 domande coincidono con l'Excel del prof (similarità 1,0). Compiti: i 4 del PDF del prof, identici.

## 4. Pagine del libro in HD (B-bis)
Zip `Lez14_ingrandita.zip`: pagine 526–531 (Ciàula) e 533–538 (Belluca); **la pagina 532 manca nello zip**.
| Brano | Pagina | File HD | Minuto Parte 2 |
|---|---|---|---|
| Ciàula scopre la luna | 526 | Lez14_p526.png · prima fettina (titolo, temi principali, inizio) | dal pezzo D4 (≈ 20:45) a fine D5 |
| Il treno ha fischiato | 533 | Lez14_p533.png · prima fettina | D5 finale e tutto D6 |
Il prof **non legge** i brani: riassume mentre sullo schermo resta la prima pagina. Ho fatto scattare un'altra fettina solo se il testo citato coincide a lungo; non è scattata mai. Quindi **una sola fettina per novella**, ferma per minuti: lontano dalla lezione 11 di riferimento.

## 5. Cosa NON ho verificato / limiti noti / DA DECIDERE
- **Inserti rifatti**: i testi degli **approfondimenti** vengono dall'OCR delle schede vecchie, corretti a mano da me: non li ho riletti con la voce e potrebbero avere differenze di parola. I tempi di comparsa delle card sono **a intervalli regolari** (non a tempo con le parole). Ripassi, glossario e riepilogo hanno il testo della voce e i tempi dalle parole (stima).
- **Schede Quiz, Verifica, Compiti, finale**: restano come erano (banda blu).
- **PDF slide**: 19 + 22 pagine; non ho confrontato ogni pagina col fotogramma del video.
- **Fettine del libro**: una per novella (§4). Niente `controllo_fettine.jpg` con più fettine.
- **Durata**: Parte 1 {mm(dur[1])}, Parte 2 {mm(dur[2])}: entrambe **sotto i 50 minuti**. Decide Sara (unire, aggiungere, accettare).
- **Voce R1** (mappa del prof): la trascrizione dell'ascolto automatico rende «giorfatara», «Fumathia Pascal», «Uno Nessuno ai 100.000»: potrebbe essere errore del riconoscimento o pronuncia sbagliata della voce. **Non ascoltata da me.** Se è la voce, serve R2 con il testo riscritto.
- Il **riquadro del prof 4:3**: la webcam originale è 184×138 px ingrandita 2,2×: immagine morbida; la testa tocca il bordo alto già nell'originale (es. 0:20, 11:40, 23:20 dell'originale).
- **Sincronia labbra**: video e audio sono presi dallo stesso istante dell'originale (scarto audio misurato ≤0,5 ms); il movimento delle labbra **non l'ho verificato indipendentemente**.
- **Evidenziazioni** delle card: stima da parole chiave; non ascoltate a mano. Slide 47 (Serafino Gubbio) non è mai mostrata dal prof: non c'è nel video.
- **Mappa del prof**: una sola per tutta la lezione, messa nella Parte 2 (decisione mia, da confermare). Nel PDF mappe i nodi sono identici (letti dall'immagine). 
- Nella mappa del prof: «Così è **se** (se vi pare)» (probabile refuso) e «Il **gioco** delle parti» (nelle slide «giuoco»): DA CONFERMARE COL PROF.
- Le pillole e gli approfondimenti vecchi contengono ancora qualche contenuto che non coincide con le slide (es. quiz 2 titolo vecchio): ho allineato solo i titoli.

## Tabella: fine e inizio di ogni pezzo del prof (misurato su pause ≥ 0,45 s)
{fine}
(«Frase finita» e «Inizia a inizio frase» = punteggiatura della trascrizione automatica seguita da pausa; le «ultime parole» sono del riconoscimento, non riascoltate.)

## Tabella secondo vecchio → secondo nuovo
**Parte 1**
| Pezzo | Vecchio | Nuovo | Differenza |
|---|---|---|---|
{tabsec(1)}
**Parte 2**
| Pezzo | Vecchio | Nuovo | Differenza |
|---|---|---|---|
{tabsec(2)}
La master rigenera la pagina con i secondi di `scheda_pubblicazione_parte*.json`, `quiz_argomenti_parte*.json` e `timeline_parte*.json`.

## 6. Come ho verificato
Trascrizione dell'originale (64 min) e dei due video con `trascrivi.py`; allineamento per correlazione dell'audio (offset costanti per pezzo); scene dell'originale (differenza di fotogrammi + OCR dei titoli); fotogrammi ogni 30 s (`controllo_minuti_parte*.jpg`); `controllo_jingle.py`; `ebur128`, `silencedetect`, `freezedetect`; correlazione col kit per i jingle; confronto Excel/PDF del prof con le consegne.
"""
open(f'{OUT}/RAPPORTO_REVISIONE.md','w',encoding='utf-8').write(R);print(len(R))
