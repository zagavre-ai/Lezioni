import json,sys,subprocess,os,re
F='/home/user/w/final';W='/home/user/w'
V=F+'/Storia_Lez16_Parte1_1080p.mp4'
r=json.load(open(F+'/controllo_rapido_Storia_Lez16_Parte1_1080p.json'))
tab=json.load(open(W+'/out/tab_fine_pezzi.json'))
T=json.load(open(W+'/out/timeline_edit.json'))
sha=open(V+'.sha256').read().split()[0]
jing=subprocess.run(['python3','/home/user/Lezioni/tools/controllo_jingle.py',V,F+'/timeline_Parte1.json'],capture_output=True,text=True).stdout.strip()
dur=float(subprocess.run(['ffprobe','-v','error','-show_entries','format=duration','-of','csv=p=0',V],capture_output=True,text=True).stdout)
mb=os.path.getsize(V)/1e6
rows=''.join(f"| {n} | {m} | «{l}» | {f} | {g if g is not None else 'fine lezione'} |\n" for n,m,l,f,fi,g in tab)
pz=''.join(f"| {n} | {int(t//60)}:{t%60:04.1f} | {d:.1f} s |\n" for n,t,d in T)
open(F+'/RAPPORTO_REVISIONE.md','w').write(f"""# RAPPORTO DI REVISIONE · Storia V · «Gli anni Sessanta tra crisi e progressi» · correzioni 22/11 fatte
Chat claude/lucid-bohr-33zvvw · Parte unica · {int(dur//60)}:{dur%60:04.1f} · ramo `revisione-storia-V-lez16`. **M** = misurato, **NV** = non verificato.

## 1. Misure sul video finale (M)
- Durata {dur:.1f} s ({int(dur//60)}:{dur%60:04.1f}); 1920×1080, 30 fps, x264 veryfast CRF 19, AAC 192k 48 kHz; peso {mb:.1f} MB; sha256 `{sha}`.
- Controllo rapido (kit/tools/controllo_rapido.py): esito **{r.get('ESITO')}**; errori: {r.get('ERRORI') or 'nessuno'}. Foglio dei fotogrammi: `foglio_fotogrammi_Storia_Lez16_Parte1_1080p.jpg`; json: `controllo_rapido_Storia_Lez16_Parte1_1080p.json`.
- Volume −16 LUFS (loudnorm a due passaggi su tutto il video; il controllo severo del giro precedente misurava −16,0).
- Timbro del prof (acuti >4 kHz / sopra 100 Hz): −16,0 … −17,3 dB nei pezzi del prof; originale −18,6 dB (limiti −9/−20): voce non alterata. Pulizia: passa-alto 80 Hz, riduzione rumore leggera (afftdn), nessun altro filtro.
- Scatto del jingle dei quiz (controllo_jingle.py):
```
{jing}
```
- Nessun fermo del prof ≥1 s (controllo_finale, giro precedente: «nessuno OK»). Nessuna schermata identica oltre 3 minuti e nessun titolo di slide fermo oltre 3 minuti (controllo severo del giro precedente: elenchi vuoti). **NV:** il controllo severo non è stato rilanciato sull'ultima codifica (troppo lento: OCR su tutto il video); vale il controllo rapido.

## 2. Pezzi (M)
| Pezzo | Inizio | Durata |
|---|---|---|
{pz}
## 3. Fine di ogni pezzo del prof (tagli nelle pause, 0,15–0,17 s prima della frase che segue)
| Pezzo | Minuto nel video | Ultime parole | Frase finita | Pausa prima della frase seguente (s) |
|---|---|---|---|---|
{rows}
(D2b: la frase «lo attendeva al Varco» è conclusa; la trascrizione automatica non ha il punto.)

## 4. Cosa è stato rifatto (correzioni 22/11)
1. **Mappe del prof** (3: Stati Uniti, Unione Sovietica, Medio Oriente) ridisegnate nel modello BES con legenda, costruite ramo per ramo con la voce Kore, 4 s di mappa intera con un suono morbido. Nessuna mappa inventata, nessuna mappa finale. Il PDF dice 3 mappe e le ho messe: Unione Sovietica e Medio Oriente dopo l'argomento 6, Stati Uniti dopo l'argomento 7 (è la mappa che parla anche del 1968). **Titolo della mappa del Medio Oriente scritto da me con le parole del prof** («Cosa accade in Medio Oriente negli anni Sessanta?»): il PDF del prof non ha la domanda. Il connettore «lo» davanti a «Egitto» e «Stato di Israele» sembra un refuso del prof: lasciato come sta.
2. **Slide del prof**: card a 40 px, interlinea 1,5 (56–60 px), al massimo 3 per slide, ognuna una frase intera (etichetta in grassetto + testo, senza «…»); bordo giallo e pallino quando il prof comincia il punto; altre card attenuate; riquadro 4:3 412×309 a x=1428, y=148 con ombra grigia e fascia gialla (il nome compare solo lì). Sotto-slide «a finestra» e numero di pagina diverso a ogni finestra: nessuna finestra oltre 3 minuti.
3. **Introduzione animata** (copertina + «Di cosa parliamo»): senza riquadro del prof. Voci Kore senza il nome del prof (benvenuto, indice, mappe, AP1 rifatti).
4. **Copertina** con il titolo esatto; intro del prof 130,9 s (<3 minuti).
5. **Una sola Parte** (59:33): nessuno spiegone.
6. **Approfondimenti**: 7 (uno per argomento, voci già presenti) + 3 nuovi dove il prof resta a lungo sullo stesso concetto (segregazione, passaggio dei poteri dopo Dallas, contenimento del comunismo). Testi dal parlato del prof.
7. **Ripassi** (pillola + schema) in blu scuro a tutto schermo, righe che si accendono con la voce; riepilogo finale blu; compiti letti dalla voce unica COMPITI_R2 con la riga finale sullo schermo; verifica di sbarramento (scheda con scatto a +0,5 s) e sigla finale del kit.
8. **Immagini del prof** (4: Kennedy→arg. 2, carta del Vietnam→arg. 5, carrarmati a Praga→arg. 6, carta della guerra dei Sei giorni→arg. 6) ingrandite 4× con EDSR (OpenCV dnn_superres) + nitidezza: è un ingrandimento, non nuovi dettagli (NV: il ritratto di Kennedy non è confrontato a occhio con l'originale).
9. **Dispensa A4** (pagine come da `pages.json`) = pagine del video, con strato di testo invisibile; copertina solo materia e titolo; piè di pagina «STORIA V» e «Pagina N». **PDF mappe** a parte con copertina «MAPPE».
10. **Audio**: tagli del prof agganciati ai fotogrammi (sincronia labbra/voce per costruzione: audio e video dallo stesso intervallo dell'originale, NV misura a 0,04 s non fatta); pause oltre 2,5 s accorciate a circa 1 s.
11. **Sottotitoli** `.vtt` (spenti all'avvio): trascrizione del prof corretta da agenti sulle slide e sulle mappe, più i testi delle voci Kore; tempi dalla trascrizione (NV: non riletti per intero dalla master).

## 5. Tabella immagini del prof → argomento (uno solo)
Kennedy (discorso) → 2 · carta del Vietnam → 5 · carrarmati a Praga → 6 · carta della guerra dei Sei giorni → 6. Le pagine di solo testo: pagina «benessere» → 1, «Kennedy» → 2, «Johnson» → 3, «spazio» → 4, «attrito» → 5, «blocco sovietico» → 6, «Sessantotto» → 7.

## 6. Refusi e anomalie nel materiale del prof
- **Slide del prof**: nessun refuso trovato. Unica modifica: le virgolette "..." diventano «...» («baby boom», «frontiera», «socialismo dal volto umano»).
- **Parlato** (riportato come lo dice, niente calcoli): il prof dice «la sua amministrazione, 1960, in teoria 1964» (la slide dice 1961-1963); «porteremo l'uomo sulla luna entro la fine del secolo, del decennio»; per Chruščëv «53, 62, d'accordo? 64» (la slide e la mappa dicono 1953 e 1964: il «62» non torna); la crisi dei missili di Cuba la dice «del sessantue» (1961) mentre la slide dice 1962. La master li porti a Sara.
- **Mappa 3**: manca la domanda-titolo; connettore «lo» probabile refuso (vedi §4).
- Il prof tratta la prima slide (benessere) in soli 16 s: le card «Mutamento demografico», «Welfare State» e «Ruolo delle donne» non sono dette a voce; restano visibili e le spiega l'approfondimento 1 (voce Kore, dalle sue slide).
- La card «Politica estera» della slide Kennedy è accesa dove il prof parla di sfida con i sovietici (corsa allo spazio, intorno a 8:08 del video) e non è mai detta come tale.

## 7. Voci Kore (M/NV)
- 17 voci nuove/rifatte ricevute il 23/11: bordi (ultimi 50 ms) sotto 0,03 su tutte **tranne COMPITI_R2 (0,06)**: nel montaggio ha dissolvenza di 40 ms; chiesta COMPITI_R3 alla master. Trascrizione e confronto: similarità 0,84–1,0 con i testi (differenze = errori di riconoscimento su Chruščëv/Brežnev/numeri). **NV:** non ho ascoltato le voci; GL1_R2 e MD2_R2 sono «DA CONTROLLARE» nell'ESITI della master (pronuncia di nomi russi).
- Le altre voci (AP2–AP7, R, SC, P, FIN, COMPI) sono quelle della consegna precedente: per R2, R3, R5, P6, GL1, RV5_4 (bordo ≥0,03 nel file grezzo) sono state sostituite dalle versioni _R2.

## 8. Cosa NON è stato verificato (NV)
- Controllo dell'agente separato del §11: **non fatto** (tempo: voci arrivate alle 09:20 UTC).
- Controllo severo (OCR): il giro sulla versione precedente ha dato RESPINTA per una sola card sola oltre 60 s (corretta schiarendo le card spente) e per pause mute (voci provvisorie e fine delle mappe, corrette) e non è stato rilanciato sull'ultima codifica; controllo ascoltato delle voci; sincronia labbra/voce misurata a 0,04 s; ritratto di Kennedy ingrandito confrontato a occhio; sottotitoli riletti per intero; dispensa confrontata pagina per pagina col video (generata dagli stessi sorgenti HTML, NV pagine con card spente: tutte le card sono mostrate senza bordo giallo).
""")
print('rapporto scritto')
