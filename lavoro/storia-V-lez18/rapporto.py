# -*- coding: utf-8 -*-
import json,os,re,sys
W='/home/user/work18';O=W+'/out'
M=json.load(open(O+'/misure.json'))
tag=open(O+'/tabella_tagli.md').read()
prov=sorted(set(json.load(open(O+'/voci_provvisorie_Storia_Lez18_Parte1.json')))|set(json.load(open(O+'/voci_provvisorie_Storia_Lez18_Parte2.json'))))
def sev(w):
    try:
        d=json.load(open(f'{O}/severo_p{w}.json'));return d
    except Exception:return None
R=[]
A=R.append
A("# RAPPORTO DI REVISIONE · Storia · «L'Italia repubblicana» · Parte 1 e Parte 2\n")
A("Rifatta da zero il 22–23/11/2026 dai materiali del prof (release `mazzotti-storia-V`: video 4274 s, slide, MAPPE LEZIONE 18, test Excel, compiti) con le regole del CLAUDE.md. La vecchia consegna del 16/11 (ramo `consegna-storia-V-lez18`) non è stata usata.\n")
if prov:
    A(f"> **STATO DELLE VOCI: {len(prov)} voci Kore sono ancora PROVVISORIE** (sintesi espeak), in attesa delle voci della master: {', '.join(prov)}.\n> Appena arrivano si controllano (trascrizione, numeri, bordi) e si rimontano le due Parti; il prof, le slide e le mappe non cambiano.\n")
else:
    A("> Tutte le voci Kore sono quelle della master, controllate (trascrizione, numeri, bordi < 0,03).\n")
A("## 1. Misure sul file finale\n\n| | Parte 1 | Parte 2 |\n|---|---|---|")
for k,l in [('durata_min','durata (min)'),('fotogrammi','fotogrammi (letti)'),('attesi','fotogrammi attesi (durata×30)'),('peso_MB','peso (MB)'),('res','risoluzione'),('LUFS','volume integrato (LUFS)'),('picco_dBFS','picco (dBFS, campione)'),('silenzi_oltre_2_5s','pause > 2,5 s'),('timbro_dB','timbro del prof: energia >4 kHz meno >100 Hz (dB), 6 campioni (atteso −9…−20; originale ≈ −19…−22)')]:
    A(f"| {l} | {M['1'][k]} | {M['2'][k]} |")
A("\nCodifica: x264 veryfast, CRF 19 (Parte 1) e CRF 21 (Parte 2, per stare sotto i 400 MB), 30 fps, AAC 192k 48 kHz, una sola codifica per Parte.\n")
for w in ('1','2'):
    d=sev(w)
    if d:A(f"**controllo_severo.py Parte {w}:** esito **{d.get('ESITO')}** · errori: {d.get('ERRORI')} · tono voce {d.get('voce_tono_hz')} · chiarezza {d.get('voce_chiarezza_hz')} · copertina {d.get('copertina_durata_s')} s\n")
A("## 2. Tagli del prof (fine di ogni pezzo)\nOgni pezzo comincia 0,15–0,35 s prima della prima parola e finisce in una pausa (livello nel taglio sotto −45 dB). Tabella con minuto nel video, sorgente, ultime parole, frase finita:\n"+tag+"\n\nNote: IN1 finisce su «…non faremo altro che ripercorrerlo.»; la false partenza «Ma dal lato italiano, diciamo» è stata tolta (incespicamento). P2c finisce con «…il 1° gennaio 1948» (frase conclusa, senza punto nella trascrizione automatica).\n")
A("## 3. Struttura e regole (CLAUDE.md §3, §4, §6, §9)\n- Sigla 15 s → copertina animata con voce di benvenuto (senza riquadro del prof) → intro del prof sulla copertina (112 s, poi slide «Di cosa parliamo») → per ogni argomento: titolo (`titolo.wav`), prof con slide a card (max 3, frase intera, bordo giallo all'inizio della frase), 1–2 approfondimenti animati con voce Kore, mappa del prof (solo argomenti 2, 5, 6), pillola di ripasso (`repaso.wav`) + schema, quiz di 5 domande (`quiz.wav` a +0,5 s).\n- Parte 2: dopo la sigla, copertina animata e **spiegone** della Parte 1 (3 argomenti, con la mappa dell'arg. 2).\n- Fine: glossario, ripasso finale, **verifica di sbarramento (10 domande dell'Excel del prof, 80%)** e sigla finale con avviso diritti, poi intro «Compiti» di 3,5 s con jingle e i 4 compiti del prof (tutto nel video della Parte 2).\n- Transizioni: `trans.wav` + dissolvenza su ogni cambio di pezzo.\n- Dispense A4 orizzontali per Parte (`Storia_Lez18_ParteN_slide.pdf`): stesse slide del video senza riquadro del prof, con strato di testo invisibile; copertina solo «Storia» + titolo; piè «STORIA» e «Pagina N». PDF mappe per Parte (`…_ParteN_mappe.pdf`), copertina con «MAPPE».\n- Sottotitoli `.vtt` fatti sul video finale (parlato del prof da riconoscimento automatico con correzioni dei nomi: **da rileggere a campione**; voci Kore dai testi).\n")
A("## 4. Mappe (come da risposta della master delle 18:45 UTC)\n- Mappe del prof (PDF «MAPPE LEZIONE 18»), ridisegnate in vettoriale nel modello BES (5 colori, legenda in alto a destra, testo 36 px), costruite ramo per ramo con la voce, mappa intera ferma ≥ 4 s: **arg. 2** «Come nasce la Repubblica italiana?» (Parte 1), **arg. 5** «Quali sono i principali avvenimenti dell'età detta del centrismo?» e **arg. 6** (Parte 2).\n- **Titolo scritto da noi (dichiarato):** la mappa dell'arg. 6 nel PDF del prof non ha la domanda; ho scritto «Come nascono i governi di centrosinistra?» con parole del prof.\n- Nella mappa dell'arg. 5 la sigla «Cee» è rispiegata con una nota a piè mappa («Cee: Comunità economica europea»); le parole dei riquadri restano quelle del prof.\n- Argomenti 1, 3, 4: il prof non ha mappa → nessuna mappa inventata, l'argomento si chiude con pillola e quiz; nessuna mappa finale della lezione.\n- Differenza tra mappa del prof («Fronte popolare democratico») e quiz/Excel («Fronte democratico popolare»): lasciati come sono.\n")
A("## 5. Immagini e fonti\nTutte dal PDF del prof: carta «Il confine orientale italiano (1920-1954)» e foto Piano INA-Casa (ingrandite 3× con nitidezza, erano 792×470 e 255×392: restano di qualità limitata, da guardare). Nessuna immagine presa dal web; nessuna foto di persone scaricata. Le foto di De Gasperi e di Fanfani–Moro del PDF non sono state usate (non corrispondono a ciò che il prof dice in quel momento).\n")
A("## 6. Anomalie del materiale del prof (riportate come le dice lui, da portare a Sara)\n"+open(W+'/anomalie.md').read()+"\n")
A("## 7. Voci\n- Voci Kore già presenti usate dopo controllo con trascrizione (Parakeet): AN*, R*, P*, SC*, GL*, RF*, FIN*. Troncate in fondo e da rifare: AN2a, AN2b, AN6a, R6. Sigle non spiegate nelle voci vecchie (rifatte in `_R2`): R4, AN4c, SC4_4, R6, AN6b, RF2, SC6_2.\n- Voci nuove richieste: INTRO1_R2, INTRO2_R2, SP2_1-3, M2_01-08, M5_01-10, M6_01-07 (`voci_da_generare.json` nel ramo di lavoro).\n- Numeri e anni in lettere nel testo per la voce, in cifre sullo schermo.\n")
A("## 8. Cosa è stato verificato e cosa NO\n"+open(W+'/verificato.md').read())
open(O+'/RAPPORTO_REVISIONE.md','w').write('\n'.join(R));print('ok',len('\n'.join(R)))
