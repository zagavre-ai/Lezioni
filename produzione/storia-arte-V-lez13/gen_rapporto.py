import sys,os,json,glob,subprocess
sys.path.insert(0,'/tmp/claude-0/w/prod')
W='/tmp/claude-0/w/prod';R=W+'/rev'
cr=json.load(open(glob.glob(W+'/fin/cr/controllo_rapido_*.json')[0]))
tag=json.load(open(W+'/fin/tabella_tagli.json'));tb=json.load(open(W+'/fin/timbre.json'))
cv=json.load(open(W+'/consegna/controllo_voci.json')) if os.path.exists(W+'/consegna/controllo_voci.json') else {}
import numpy as np
fr=subprocess.run(['ffprobe','-v','error','-count_packets','-select_streams','v:0','-show_entries','stream=nb_read_packets','-of','csv=p=0',W+'/fin/Storia_arte_Lez13_Parte1_1080p.mp4'],capture_output=True,text=True).stdout.strip().strip(',')
voci_ok=cv and all(isinstance(v,dict) and v['bordi_ok'] for v in cv.values())
L=[]
L.append("# RAPPORTO · Storia dell'arte V · Razionalismo e Metafisica (1 Parte)\n")
L.append("Montaggio nel modello Storia V sul video originale del prof (2354,4 s). Ogni misura è marcata [misurato] o [per costruzione]; in fondo c'è l'elenco di cosa NON è stato verificato.\n")
L.append("## 1 · Misure sul file finale\n| | |\n|---|---|")
for k,v in [('Durata',f"{cr['durata_min']} min"),('Formato',cr['formato']),('Peso',f"{cr['peso_MB']} MB"),('Fotogrammi',fr),('LUFS',cr['LUFS']),('Picco',f"{cr['picco_dBTP']} dBTP"),('Pause mute oltre 2,5 s',cr['pause_mute'] or 'nessuna'),('ESITO controllo_rapido.py',cr['ESITO'])]:L.append(f"| {k} | {v} [misurato] |")
L.append(f"\nTimbro del prof (acuti >4 kHz rispetto a >100 Hz, 20 s per pezzo): originale {np.mean(tb['orig']):.1f} dB, finale {np.mean(tb['fin']):.1f} dB, differenza {np.mean(tb['fin'])-np.mean(tb['orig']):+.1f} dB; limite −9…−20 [misurato]. Audio del prof: filtro dei bassi 80 Hz, riduzione leggera del rumore, nessun altro filtro; ogni pezzo portato a −16 LUFS solo con guadagno.\n")
L.append("Sincronia labbra/voce: audio e video del prof escono dagli stessi istanti dell'originale (stessi intervalli, taglio per fotogrammi interi) [per costruzione]; non misurata con uno strumento. Fermi immagine del prof: nessuno oltre 0,4 s (tenuta di 0,4 s sotto la dissolvenza all'inizio e alla fine di ogni pezzo) [per costruzione]. Scatto del quiz: vedi controllo_jingle (4 quiz a +0,005 s) [misurato].\n")
L.append("## 2 · Tabella dei pezzi del docente (fine di ogni pezzo)\n| Pezzo | Inizio | Fine | Prime parole | Ultime parole | Frase finita |\n|---|---|---|---|---|---|")
for r in tag:L.append('| '+' | '.join(r)+' |')
L.append("\nI tagli cadono nelle pause (margine 0,15 s prima della frase che segue). Pause oltre 2,5 s accorciate a circa 0,9 s; tolti solo i riempitivi isolati («Uh», «Um», «Mm-hmm», «Yeah», «The», «Okay»).\n")
L.append("## 3 · Voci Kore\n")
if cv:
    L.append("| Voce | Durata | Bordi (inizio/fine) | Differenze con il testo |\n|---|---|---|---|")
    for n,v in cv.items():L.append(f"| {n} | {v['durata']} s | {v['bordo_inizio']}/{v['bordo_fine']} | {v['n_diff']} |" if isinstance(v,dict) else f"| {n} | MANCA | | |")
    L.append(f"\nBordi sotto 0,03: {'sì, tutte' if voci_ok else 'NO, vedi tabella'} [misurato]. Differenze: numeri e date in lettere ignorati; le altre elencate in controllo_voci.json. **Pronuncia dei nomi stranieri e latini non ascoltata da questa chat.**\n")
else:L.append("Voci provvisorie.\n")
L.append("""## 4 · Immagini, fonti, risoluzioni
- Le opere vengono dal PDF del prof (`SLIDE/LEZIONE 13.pdf`), estratte con pdfimages e ritagliate dai margini e dalle didascalie. Risoluzioni d'origine: Piazza della Vittoria 794×511, piazza San Pietro 464×319 e 464×343, Canto d'amore 448×548, Le muse inquietanti 450×654, Morandi 505×620, Carrà 456×618, Casa del Fascio e i particolari del PDF circa 100–110 dpi.
- Ingrandimento Lanczos con nitidezza leggera (non rete neurale). Le opere restano piccole in origine: **se la master ha messo versioni alte su `opere-storia-arte-V`, non sono state usate in questa consegna** (vedi stato).
- Wikimedia non raggiungibile dalla rete della chat (403).
- Webcam del prof: 246×138 px nel video d'origine, ritaglio 4:3 di 184×138 px portato a 412×309 (ingrandimento 2,2×, Lanczos, nitidezza leggera, colore appena corretto).
## 5 · Mappe
- Le due mappe del prof (La metafisica, Architettura Italia fascista) ridisegnate nel modello BES, un riquadro alla volta con la voce, la mappa intera ferma 4 s. Parole del prof; testo in maiuscole/minuscole.
- Il prof non ha la domanda come titolo: l'ho scritta io con le sue parole («Che cos'è la metafisica?», «Come risponde l'architettura dell'Italia fascista al regime?»). La master la ricontrolli.
- Argomenti 1 e 4: il prof non ha mappa; chiusi con la pillola di ripasso.
## 6 · Refusi e anomalie del materiale del prof
- Slide: «delle Arti» → «delle arti», «del Regime» → «del regime», «di Regime» → «di regime», «Primo Dopoguerra» → «primo dopoguerra».
- Mappa «Metafisica»: «PIAZZA DESERTE» → «piazze deserte».
- Casa del Fascio di Como: il prof dice «altezza 6,6 metri, esattamente la metà del lato di base» con lato 33,2 m: non torna (la metà è 16,6). Nelle voci scritto solo «la metà del lato di base».
- Natura morta metafisica con la squadra (Morandi): didascalia del PDF 1919, il prof dice 1918. Voce come dice il prof (1918); anno omesso nella didascalia.
- Il prof dice «Palazzo della Civiltà del Lavoro», la slide «Palazzo della Civiltà Italiana». Nei nostri testi: nome della slide.
- Test Excel: spazi iniziali in due risposte (« Giorgio Morandi», « La Casa del Fascio»), tolti.
- Il prof dice «de Chirico fondatore a Firenze nel 1910»: riportato come lo dice.
- Sottotitoli: la trascrizione automatica sbaglia alcuni nomi; corretti con un elenco di sostituzioni (de Chirico, Carrà, Terragni, Casa del Fascio, Colosseo quadrato, Matteotti, Patti Lateranensi, ecc.). Non riletti tutti a mano.
## 7 · Cosa NON è stato verificato
- Il confronto parola per parola di ogni voce Kore con il testo è fatto con trascrizione automatica; non ho ascoltato le voci.
- Sincronia labbra/voce non misurata con strumento; le 10 accensioni delle card sono state fissate sulla trascrizione automatica (±1 s) ma non riascoltate.
- I sottotitoli .vtt non sono stati riletti riga per riga.
- Il controllo dell'agente separato del §11 non è ancora stato fatto in questa consegna.
- Il controllo severo della master (`controllo_severo.py`) non è stato lanciato.
""")
open(R+'/RAPPORTO_REVISIONE.md','w').write('\n'.join(L));print('ok')
