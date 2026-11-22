import json, sys, re, os, subprocess, hashlib, statistics
sys.path.insert(0, '/tmp/w/b')
O = '/tmp/w/b/out'
def sh(c): return subprocess.run(c, capture_output=True, text=True)
def mm(t): return '%d:%02d' % (t // 60, t % 60)
PROV = {}
for p in (1, 2):
    PROV.update(json.load(open(f'/tmp/w/b/meta_P{p}.json'))['PROV'])
tim = json.load(open('/tmp/w/b/timbro_pezzi.json'))
def sev(p):
    t = open(f'{O}/severo_P{p}.txt').read()
    try: return json.loads(t[t.index('{'):])
    except Exception: return {}
def cf(p): return open(f'{O}/cf_P{p}.txt').read()
def stats(p):
    v = f'{O}/Storia_Lez20_Parte{p}_1080p.mp4'
    j = json.loads(sh(['ffprobe', '-v', 'error', '-count_packets', '-select_streams', 'v:0', '-show_entries', 'stream=nb_read_packets:format=duration,size', '-of', 'json', v]).stdout)
    r = sh(['ffmpeg', '-hide_banner', '-i', v, '-af', 'ebur128=peak=true', '-f', 'null', '-']).stderr
    I = re.findall(r'I:\s+(-?[\d.]+) LUFS', r)[-1]; P = re.findall(r'Peak:\s+(-?[\d.]+) dBFS', r)[-1]
    sha = hashlib.sha256(open(v, 'rb').read()).hexdigest()
    return dict(dur=float(j['format']['duration']), fr=int(j['streams'][0]['nb_read_packets']), mb=int(j['format']['size']) / 1e6, I=I, P=P, sha=sha)
ST = {p: stats(p) for p in (1, 2)}
SV = {p: sev(p) for p in (1, 2)}
voice = subprocess.run(['python3', '/tmp/w/b/voice_check.py'], capture_output=True, text=True).stdout
vtab = [l for l in voice.splitlines() if l.startswith('(')]
prov_txt = '\n'.join(f"- `{k}`: {v.get('testo', v.get('provvisoria_con', ''))[:140]}" for k, v in PROV.items()) or '- nessuna: tutte le voci sono quelle definitive.'
tl = {p: json.load(open(f'/tmp/w/b/timeline_P{p}.json')) for p in (1, 2)}
tpezzi = ''
for p in (1, 2):
    tpezzi += f'\n**Parte {p}**\n\n| Pezzo | Inizio | Durata (s) |\n|---|---|---|\n' + '\n'.join(f'| {n} | {mm(a)} | {d:.1f} |' for n, a, d in tl[p]) + '\n'
tabelle = open(f'{O}/tabelle.md').read()
from prof import mapper
from content import CHUNKS
META = json.load(open('/tmp/w/b/ch/meta.json'))
IM = {}
for p in (1, 2):
    for n, st, d in tl[p]:
        k = n[1:] if n[0] == 'D' and n[1:] in META else None
        if not k: continue
        f, _ = mapper([tuple(x) for x in META[k]['iv']])
        for t, kind, v in CHUNKS[k].get('ev', []):
            if kind == 'img' and v not in IM: IM[v] = f'{mm(st + 0.8 + f(t))} (Parte {p})'
def sm(p):
    d = SV[p]
    return f"copertina {d.get('copertina_durata_s', '-')} s; slide stesso titolo >3 min: {len(d.get('slide_stesso_titolo_oltre_3min', []))}; schermate identiche >3 min: {len(d.get('schermata_identica_oltre_3min', []))}; card con puntini: {len(d.get('card_con_puntini', []))}; card che iniziano minuscole: {len(d.get('card_iniziale_minuscola', []))}; una card sola >60 s: {len(d.get('una_card_sola_oltre_60s', []))}; pause >2,5 s: {d.get('silenzi_oltre_3s', '-')}; esito: **{d.get('ESITO', '-')}** — errori: {d.get('ERRORI', [])}"
agente = open(f'{O}/agente_separato.md').read() if os.path.exists(f'{O}/agente_separato.md') else '_Controllo dell\'agente separato non ancora eseguito._'
note_extra = open(f'{O}/note_extra.md').read() if os.path.exists(f'{O}/note_extra.md') else ''
R = f"""# RAPPORTO DI REVISIONE · Storia · «Gli anni Novanta: il mondo post-bipolare» · CORREZIONI 22/11
Chat `claude/keen-hypatia-d76anw` · ramo di consegna `revisione-storia-V-lez20` · {subprocess.run(['date','-u','+%d/%m/%Y %H:%M UTC'],capture_output=True,text=True).stdout.strip()}.
Ogni dato è etichettato **M** (misurato), **S** (a vista / stima) o **NV** (non verificato).

## 0. Cosa è stato fatto e cosa no (in breve)
- Lezione **rimontata da zero** dall'originale del prof (release `mazzotti-storia-V`, zip 004): il montaggio precedente non era ricostruibile. Slide, mappe, quiz, pillole, quiz, glossario, ripasso finale, verifica, sigle e compiti sono nuovi.
- **Due Parti**, tagliate a fine argomento 4 (decisione approvata dalla master): Parte 1 = {mm(ST[1]['dur'])}, Parte 2 = {mm(ST[2]['dur'])}. La Parte 2 è sotto i 50 minuti perché il materiale del prof è breve (CLAUDE.md §3.6: «va bene, non si allunga»).
- **Voci provvisorie ancora presenti:** vedi §3. Finché non arrivano e non sono sostituite **questa consegna non è definitiva**.

## 1. Misure sui video finali (M)
| | Parte 1 | Parte 2 |
|---|---|---|
| File | `Storia_Lez20_Parte1_1080p.mp4` | `Storia_Lez20_Parte2_1080p.mp4` |
| Durata | {mm(ST[1]['dur'])} ({ST[1]['dur']:.2f} s) | {mm(ST[2]['dur'])} ({ST[2]['dur']:.2f} s) |
| Fotogrammi / durata×30 | {ST[1]['fr']} / {round(ST[1]['dur']*30)} | {ST[2]['fr']} / {round(ST[2]['dur']*30)} |
| Peso | {ST[1]['mb']:.1f} MB | {ST[2]['mb']:.1f} MB |
| Formato | 1920×1080, 30 fps, x264 veryfast (CRF 19 le schede, CRF 22 i pezzi del prof, per stare sotto 400 MB), AAC 192k 48 kHz | idem |
| Volume | {ST[1]['I']} LUFS, picco {ST[1]['P']} dBFS | {ST[2]['I']} LUFS, picco {ST[2]['P']} dBFS |
| sha256 | `{ST[1]['sha']}` | `{ST[2]['sha']}` |

Audio: una sola codifica AAC sull'intero programma (audio rifatto in un passaggio dai pezzi non compressi, così non ci sono scarti di durata). Video: ogni pezzo codificato una volta, uniti senza ricodifica.

### Controlli automatici
- `controllo_finale.py` Parte 1:\n```\n{cf(1)}\n```
- `controllo_finale.py` Parte 2:\n```\n{cf(2)}\n```
- `controllo_severo.py` Parte 1 (M): {sm(1)}
- `controllo_severo.py` Parte 2 (M): {sm(2)} — «copertina non trovata» e «durata < 50 min» sono attesi: la Parte 2 non ha copertina (si apre con sigla e spiegone) ed è breve per scelta approvata.
- Pause >2,5 s: sono le code silenziose di 4 s con la mappa intera ferma (richieste dal §6), le code dei jingle delle schede titolo/quiz e, finché sono provvisorie, i silenzi delle voci non ancora arrivate. Nel parlato del prof non ci sono pause >2,5 s (M, rilevamento sulla trascrizione: nessun intervallo da accorciare).
- Quiz: scatto del jingle a 0,0 s su tutte e 8 le schede (M).
- Fermi immagine ≥1 s nei pezzi del prof: nessuno (M, `freezedetect`). Resta una fermata di 0,8 s all'inizio di ogni pezzo (fotogramma fisso con dissolvenza, 24 fotogrammi) e di 0,5 s in coda (S).
- **Timbro del prof (M):** acuti >4 kHz meno volume >100 Hz, originale −17,7 dB; nei pezzi finali: {', '.join(f'{n} {v}' for p in ('1','2') for n, v in tim[p])} dB → tutti tra −9 e −20 (nessun filtro che cambi il timbro: solo passa-alto 70 Hz, riduzione rumore leggera, guadagno e limitatore).
- Sottotitoli: `Storia_Lez20_Parte1.vtt` e `..._Parte2.vtt`, ricavati dalla trascrizione del prof con i tempi parola per parola rimappati sul video finale, termini corretti (Iugoslavia, Eltsin, Milošević, Gorbaciov, Tienanmen, URSS, NATO, Al-Qaeda…) e le frasi delle voci Kore. Il controllo «attacco sulla voce» di `controllo_finale.py` dà 71 % (P1) e 53 % (P2) di blocchi entro 0,3 s su pochi blocchi verificabili (21 e 17): la mediana dello scarto è 0,02 s (M), ma la metrica automatica è severa sui blocchi che seguono un jingle. **NV: ascolto completo non fatto.** Residui di trascrizione automatica possibili nei sottotitoli del prof (parole non riconosciute): da controllare a campione.

## 2. Cosa è cambiato rispetto alla consegna precedente (punti del prompt 22/11)
| # | Punto | Esito |
|---|---|---|
| 1 | Mappe del prof, ridisegnate nel modello BES, costruite ramo per ramo con la voce | **Fatto per le 4 mappe del PDF del prof** (Iugoslavia, Europa, Italia, globalizzazione), identiche per struttura, frecce e parole, titolo = domanda del prof; legenda a 5 colori in alto a destra; testo 38–40 px; un riquadro alla volta, giallo mentre la voce lo legge, mappa intera ferma 4 s. Togliere tutte le mappe inventate: **fatto** (nessuna mappa per gli argomenti 1, 2, 6, 7 e nessuna mappa finale, come da messaggio della master 19:25). I colori sono una mia scelta per categoria (pesca centro; celeste date; paglierino parole chiave; menta esempi; lilla conseguenze): la master li ricontrolli. Il titolo della mappa Iugoslavia ha «URSS (Unione Sovietica)» perché ogni sigla va spiegata. |
| 2 | Slide del prof: card a 40 px, max 3 card intere, bordo giallo all'inizio della frase, nessuna schermata identica oltre 3 minuti | **Fatto.** Card intere (mai «…»), testo 40 px (interlinea 1,5; le viste «focus» 48 px), massimo 2–3 card per pagina in finestra scorrevole, bordo giallo e pallino all'inizio della frase (tabella §6). Sotto-slide a finestra: ogni pagina che dura >150 s alterna la vista d'insieme e una vista «focus» sulla card con titolo e numero di pagina propri (ogni vista ha il suo «Pagina N»). Riquadro 4:3 (412×309 a x=1428, y=148) con ombra grigia. |
| 3 | Introduzione animata senza riquadro; nome del prof mai detto/scritto | Copertina animata con voce di benvenuto **senza riquadro**; il riquadro compare con la prima parola del prof. Il nome del prof è solo nella fascia gialla. **Attenzione:** la voce di benvenuto provvisoria (`INTRO1`) dice il nome: va sostituita con `INTRO1_N` (richiesta alla master). Nelle schede animate non compare. |
| 4 | Copertina con titolo esatto; intro ≤3 min; poi «Di cosa parliamo» | Titolo «GLI ANNI NOVANTA: IL MONDO POST-BIPOLARE». Copertina+introduzione = {SV[1].get('copertina_durata_s','-')} s (M, controllo severo). Poi slide «Gli argomenti di oggi». |
| 5 | Spiegone all'inizio della Parte 2 | **Fatto:** SP0 + ripasso degli argomenti 1–5 con le voci `R1`–`R5` già fatte, ciascuno con l'immagine del prof e, per gli argomenti 3–5, la sua mappa. La master aveva scritto «ciascuna mappa una volta sola»: nello spiegone le mappe tornano perché il §3.6 le prevede; se non va, si tolgono. |
| 6 | Refusi del prof | vedi §5 |
| 7 | Audio −16 LUFS, pause lunghe, timbro | −16 LUFS (M); timbro intatto (M); nessuna pausa >2,5 s nel prof (M). |
| 8 | Dispensa identica al video + PDF mappe | **Fatto:** `Storia_Lez20_Parte1_dispensa.pdf` e `..._Parte2_dispensa.pdf` (A4 orizzontale; copertina con solo materia e titolo; piè di pagina «STORIA» + «Pagina N», nessun nome del prof) e `Storia_Lez20_mappe.pdf` (copertina identica + «MAPPE»). Le pagine sono HTML stampato in PDF: il testo è vero e selezionabile (equivale allo strato invisibile). Le pagine «focus» e le immagini del prof sono incluse come nel video. |
| 9 | Lezione 18 | non è la mia lezione. |

## 3. Voci
- **Voci provvisorie presenti in questa consegna:**
{prov_txt}
- Voci Kore già esistenti riusate (85 file dal ramo `voci-storia-V-lez20`): ognuna **trascritta** (Parakeet) e **confrontata parola per parola** con il suo testo (numeri in lettere convertiti), **bordi** misurati (ampiezza negli ultimi 50 ms < 0,03) e ogni voce portata a −16 LUFS con dissolvenze di 30–35 ms (M). Esito: tutte entro il 90 % di corrispondenza e bordi < 0,03 tranne voci **non usate** (GL1, INTRO1 in sostituzione, MAP*, MAPF1, che nel montaggio non compaiono) e differenze di sola grafia del riconoscitore (centrodestra / centro destra, Jugoslavia / Iugoslavia, Qaida / Qaeda). Da riascoltare a mano: `PS5_3` (il riconoscitore non ha trovato l'ultima parola «inedito»: possibile taglio, **NV**).
- **Pronuncia dei nomi stranieri e latini: NV** (non posso ascoltare). Da far controllare: Fukuyama, Eltsin, Tienanmen, Srebrenica, Maastricht, Al-Qaeda, Milošević, Dayton, Seattle.
- Testi: solo dal materiale del prof. Controllati contro la trascrizione: i fatti degli approfondimenti (Dayton 1995, Montenegro 2006, Kosovo 2008, Tangentopoli, Putin) sono tutti nel parlato del prof (S).
- Numeri e anni: in lettere nelle voci, in cifre sullo schermo (conversione automatica, M su tutti i testi).
- Righe di pillola: per gli argomenti 2 e 3 le voci esistenti erano 3, le regole chiedono 4–6: ho aggiunto una riga a testo del prof (`PS2_4`, `PS3_4`), da far generare.

## 4. Struttura montata (tempi misurati)
{tpezzi}

## 5. Refusi e anomalie nel materiale del prof
Corretti nelle nostre slide/dispensa (i file originali non sono toccati):
- «Boris **Elcin**» → «Boris **Eltsin**» (slide arg. 1; test finale e compiti: stesso refuso, corretto nei nostri JSON).
- «dell'ex **rft**» → «dell'ex **RFT** (Repubblica Federale Tedesca)» (slide arg. 4), sigla da spiegare.
- Sigle spiegate sullo schermo alla prima comparsa in ogni card: USA, URSS, UE, NATO, PSI, RFT. A voce non posso spiegarle: la voce del prof non si tocca (le voci Kore le spiegano dove il testo lo permette, es. «Unione Sovietica»).
- Nel test finale: «Elcin» → «Eltsin».
- Nelle mappe del prof non ho trovato refusi (S).
**Anomalie (riportate come le dice il prof, nessun calcolo):**
- Mappa Iugoslavia: «Kosovo (1998)»; la slide dice «nel 1999 … intervento NATO» e il prof dice «98-99»: i due anni sono coerenti con eventi diversi, ma da far vedere a Sara.
- A voce il prof dice che Gorbaciov «all'epoca» era presidente della Russia (era presidente dell'URSS): lasciato com'è.
- A voce il prof pronuncia «Yelsin/Yeltsin/Nielsen»: nei sottotitoli «Eltsin».
- Il prof chiama «Jugoslavia» la ex Iugoslavia a voce; sullo schermo «Iugoslavia» (grafia italiana della slide).
{note_extra}

## 6. Tagli, card e immagini
{tabelle}

**Tabella immagine del prof → argomento (uno solo)**
| Immagine (PDF slide) | Argomento in cui compare | Minuto video | Qualità |
|---|---|---|---|
| Carta «Dove si trova la Cecenia» (542×675) | 1 | {IM['cecenia']} | originale, nitida (S) |
| Carta «Dove si trova il Kuwait» (253×333) | 2 | {IM['kuwait']} | **piccola**: ingrandita 2,2× con Lanczos e nitidezza leggera (S) |
| Carta «L'ex Iugoslavia 1991-2008» (1231×748) | 3 | {IM['iugoslavia']} | originale, nitida (S) |
| Carta «Le tappe dell'integrazione europea» (783×655) | 4 | {IM['ue']} | originale (S) |
| Ritratti Berlusconi (298×367) e Prodi (216×487) | 5 | {IM['ritratti']} | **piccoli**: ingranditi 1,4–1,8× con Lanczos e nitidezza leggera, tratti invariati (S) |
Le immagini sono quelle del PDF del prof alla massima risoluzione disponibile; non scaricato nulla dal web. Il prof fa vedere la carta del Kuwait solo per 3,5 s: l'ho tenuta mentre parla del Kuwait (la mostro dove lo cita).

## 7. Controllo dell'agente separato
{agente}

## 8. Cosa NON ho verificato (NV)
- Ascolto delle voci Kore (pronuncia, interpretazione): nessun ascolto possibile qui.
- Sincronia labbra/voce: i pezzi del prof sono tagliati con gli stessi istanti sull'audio e sul video dello stesso file (scarto 0 per costruzione); misura indipendente con tracciamento delle labbra non fatta.
- Il riquadro del prof ha la testa tagliata in alto **nell'originale** (la webcam è già così nel video del prof): non recuperabile.
- La risoluzione della webcam è bassa (246×138 nell'originale a 1092×614): ritaglio 4:3 centrato sul volto e ingrandito a 412×309, un po' morbido.
- Immagini piccole del prof: vedi §6.
- «Ripetizioni e incespicamenti» del prof: tolte solo le pause; non ho tagliato interiezioni ed esitazioni dentro le frasi (per non rischiare tagli a metà frase).
- Quiz, test e compiti: testi dei JSON precedenti (quiz 8×5, verifica da 10 domande dal file Excel del prof, compiti 4 esercizi), con i refusi corretti; la verifica nel video è una scheda con jingle (come i quiz) e le domande sono in `verifica_finale.json`: se la master vuole le domande lette nel video, va deciso.
- Compiti nel video: schede con il testo del prof e voce (provvisoria finché non arrivano `COMP1–4`).
"""
open(f'{O}/RAPPORTO_REVISIONE.md', 'w').write(R)
print(len(R))
