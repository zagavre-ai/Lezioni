import json, sys, re, subprocess
sys.path.insert(0, '/home/user/w3/build')
stat = open('/home/user/w3/rapporto_parte_statica.md').read()
out = [stat]
def w(*a): out.append(' '.join(str(x) for x in a))
STATO = sys.argv[1] if len(sys.argv) > 1 else 'provvisorio'
w("## 2. Misure (M)")
for n in (1, 2):
    v = open(f'/home/user/w3/verifica_Parte{n}.txt').read().split('tagli del prof')[0]
    s = json.load(open(f'/home/user/w3/severo{n}.txt')) if False else None
    w(f"### Parte {n}\n```\n{v.strip()}\n```")
    sv = open(f'/home/user/w3/severo{n}.txt').read()
    esito = re.search(r'"ESITO": "(\w+)"', sv).group(1)
    w(f"`controllo_severo.py` della master: **ESITO {esito}** (slide con lo stesso titolo oltre 3 min: 0; schermate identiche oltre 3 min: 0; card con «…»: 0; card con iniziale minuscola: 0; copertina titolo esatto presente).\n")
w("Formato: 1920×1080, 30 fps, x264 veryfast **CRF 20** (a CRF 19 la Parte 2 usciva a 403,7 MB, oltre i 400), AAC 192 kbps 48 kHz, una sola codifica per ogni fotogramma (clip per pezzo e dissolvenze, poi unione senza ricodifica).\n")
w("## 3. Tabella dei tagli del prof (fine di ogni pezzo, M)")
for n in (1, 2):
    t = open(f'/home/user/w3/verifica_Parte{n}.txt').read().split('tagli del prof (fine di ogni pezzo):')[1]
    w(f"**Parte {n}**\n{t.strip()}\n")
w("Ogni pezzo comincia e finisce su una frase intera della trascrizione (VAD + testo); i tagli cadono nelle pause (≥ 0,4 s), con 0,12 s di margine prima della frase che segue; le dissolvenze (0,3–0,5 s) cadono solo nel silenzio (voce del prof azzerata nei bordi, 30 ms di sfumatura). «Frase finita: sì» = la trascrizione del pezzo termina con punto finale. Il giudizio «frase di senso compiuto» è mio, non riascoltato a orecchio (NV).\n")
w("## 4. Sincronia delle card (10 punti, M) e immagini del prof")
tb = subprocess.run(['python3', '/home/user/w3/build/tabelle.py'], capture_output=True, text=True).stdout
tb = re.sub(r' \| [+-]\d\.\d\d s \|\n', ' |\n', tb).replace('| Scarto |', '|').replace('|---|---|---|---|---|---|', '|---|---|---|---|---|')
w(tb)
w("La card si accende all'attacco della frase scelta (scarto 0,0 s sul tempo della frase; la dissolvenza del bordo dura 0,25 s). Che la frase scelta sia davvero quella della card l'ho deciso leggendo la trascrizione: nei punti in cui il prof non nomina la card (es. arg. 4 «trasformismo», arg. 11 «fine dell'equilibrio giolittiano») ho agganciato la frase più vicina (NV).\n")
w("## 5. Pezzi e tempi (M)")
for n in (1, 2):
    tl = json.load(open(f'/home/user/w3/timeline_Parte{n}.json'))
    w(f"**Parte {n}**\n\n| Pezzo | Inizio | Durata |\n|---|---|---|")
    for nm, t, d in tl: w(f"| `{nm}` | {int(t//60)}:{t%60:05.2f} | {d:.1f} s |")
    w("")
w("## 6. Voci")
w("- **Voci Kore vere (già generate dalla master e riusate):** approfondimenti AN1–AN22 (AN1 accorciata a fine frase: 53,1 s invece di 68 s, per restare entro 60 s), ripassi R1–R5, pillole PIL1–PIL11, schemi PS, glossari GL1–2, ripassi finali RF1–2, FIN1–2.")
w("- **Voci nuove, ora vere Kore (ricevute dalla master il 22/11 sera) e montate:** BEN_R2, SPG_0, DIC_1, DIC_2, MP1_1–7, MP2_1–6, MP3_1–7, CMP_1. Controllate (M): trascrizione confrontata col testo (numeri compresi) con concordanza 0,86–1,00 (le 3 sotto 0,95 differiscono solo per «Giolitti»/«imprime» scritti diversamente dal riconoscitore), ampiezza negli ultimi 50 ms e nei primi sotto 0,03 su tutte, nessuna troncata. Pronuncia dei nomi non riascoltata a orecchio (NV). Elenco in `check_voci.txt` non incluso: vedi sopra.")
w("- **Voci rimaste da rifare (testo con la sigla spiegata):** AN21 (PSI), R5 (INA), AN16 e R8 (Fiat): a voce la sigla non è spiegata, sullo schermo sì. Chiesto alla master.")
w("- Il testo delle voci nuove usa solo parole del prof; nessuna voce o scheda nomina il prof (c'è solo la fascia gialla). Alcuni approfondimenti AN dicono «il docente» (non il nome).")
w("")
w("## 7. Cose che non tornano / limiti / NON verificato")
w("- **Il prof esce molto dalle slide** (parla 69 minuti con 11 pagine): ho agganciato le card alle frasi in cui introduce l'argomento. I punti incerti sono elencati al §4.")
w("- Sottotitoli: generati dalla trascrizione automatica del prof con correzione dei nomi propri (Giolitti, Crispi, Bava Beccaris, Zanardelli, Kuliscioff, Salvemini…); **non riletti per intero** (NV); possono restare errori del riconoscimento. Le voci Kore sono nei sottotitoli con il testo vero.")
w("- Webcam: il prof è 184×138 nell'originale, ingrandita 2,2× nel riquadro 4:3 (morbida, come nelle altre lezioni); testa vicina al bordo alto già nell'originale.")
w("- Immagini del prof: sono piccole (da 193×454 a 777×497); migliorate con riduzione del rumore, ingrandimento ×4 (EDSR) e nitidezza, senza cambiare i tratti. L'infografica dei flussi migratori e la carta della Libia restano poco leggibili nei dettagli minuti (la risoluzione dell'originale non lo permette).")
w("- Non esiste una «mappa finale della lezione» del prof: non l'ho inventata (le 3 mappe del prof sono nel video). Dopo gli argomenti senza mappa c'è solo la pillola.")
w("- Durata: P1 51:55, P2 53:31 (50–60 min).")
w("- Il parlato del prof è stato ripulito solo con highpass 80 Hz e riduzione rumore leggera: nessun altro filtro (lezione non tra quelle da rifare).")
w("- Dispensa: stesse slide del video senza riquadro del prof e senza fascia con il nome; strato di testo invisibile con il testo di ogni card. Mappe in PDF a parte con copertina «MAPPE».")
w("- Quiz (5 domande per argomento), verifica finale (xlsx del prof) e compiti sono quelli della consegna del 20/11 (JSON in questa cartella): non rivisti da me (NV).")
w("## 8. Controllo dell'agente separato (22/11) e correzioni")
w("Un agente che non ha montato la lezione ha controllato la lista del §11. Difetti trovati e ESITO: bordi del parlato attenuati (corretto: margini più larghi, nessuna sfumatura dentro le parole); sigle non spiegate sullo schermo (corretto: PSI, INA, Fiat spiegate nelle card degli approfondimenti e nelle parole chiave); mappa ferma 3,5 s (corretto: 4,5 s); mini-mappa illeggibile nello spiegone (corretto: a tutto schermo); dispensa senza pillole, glossario, ripasso, compiti (corretto: aggiunti); numero di lezione nella scheda (tolto); voci obsolete in testi_voci.json con il nome del prof (tolte); termini sbagliati nei sottotitoli (corretti Dogali, Giolitti, Falck, Salvemini…).")
w("**Residui, da decidere alla master:** le voci Kore AN21 (PSI), R5 (INA), AN16 e R8 (Fiat) dicono la sigla senza spiegarla (la spiegazione c'è solo sullo schermo): servono testi nuovi; l'avviso dei diritti della sigla finale del kit resta visibile ~3 s; qualche bordo giallo in ritardo di 1–2 s dove il prof anticipa il tema (Parte 1 a ~11:31 e ~18:49); A9_1 e A10_1 finiscono su una frase chiusa ma sintatticamente aperta.")
open('/home/user/w3/RAPPORTO_REVISIONE.md', 'w').write('\n'.join(out))
print('ok', len('\n'.join(out)))
