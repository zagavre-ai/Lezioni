# BRIEF DI PRODUZIONE · Claude 2 · versione 11/11/2026 14:30 (vale per ogni macchina/sessione)

## 0. SETUP di una macchina nuova (15 minuti, una volta)
```bash
cd ~ && GIT_LFS_SKIP_SMUDGE=1 git clone -q --depth 1 https://github.com/zagavre-ai/Lezioni /home/user/lezioni 2>/dev/null || true
cd /home/user/lezioni && git fetch -q --depth 1 origin main scambio-claude2 && git checkout -q origin/main -- Telesio_kit_produzione_v1.zip Telesio_kit_produzione_v2_aggiunta.zip Telesio_kit_produzione_v3_aggiunta.zip Telesio_kit_produzione_v4_aggiunta.zip Telesio_kit_produzione_v5_aggiunta.zip Telesio_sigle_v1.zip kit
for z in Telesio_kit_produzione_v*.zip; do unzip -oq $z -d /; done; unzip -oq Telesio_sigle_v1.zip -d /home/claude/sigle_zip
mkdir -p /home/claude && ln -sfn /home/user/lezioni /home/claude/lezioni
mkdir -p /root/.fonts && cp /home/claude/kit_prod/fonts/*.ttf /root/.fonts/ && fc-cache -f
pip install -q --break-system-packages onnxruntime pdfplumber openpyxl pypdf reportlab soundfile scipy scikit-image opencv-python-headless python-pptx pymupdf
mkdir -p /tmp/asr && cd /tmp/asr && curl -sSL -o pk.tar.bz2 https://github.com/k2-fsa/sherpa-onnx/releases/download/asr-models/sherpa-onnx-nemo-parakeet-tdt-0.6b-v3-int8.tar.bz2 && tar xjf pk.tar.bz2 && rm pk.tar.bz2
mkdir -p /home/user/lezioni/tools && cp /home/user/lezioni/kit/tools/*.py /home/user/lezioni/tools/
mkdir -p /tmp/claude-0
```
Le cartelle delle lezioni stanno in /home/claude/lezioni/<tag>/ e NON vanno mai su GitHub (aggiungi `/<tag>/` a .git/info/exclude).

## 0-bis. REGOLE DI VELOCITÀ (11/11, obbligatorie: massimo 2 ore per lezione)
1. Codifica finale: in tools/finale_a_pezzi.py cambia '-preset','fast' → '-preset','veryfast'; CRF 21 (sopra i 60 min CRF 22); maxrate 16M.
2. Sottotitoli: NON ritrascrivere il video finale. Appena esiste OUT.mp4.gruppi/a.m4a (audio finale), lancia sub_finale/ASR su quel file IN PARALLELO alla codifica video.
3. Nessuna anteprima, nessun render ripetuto. Controlli su pezzi e audio finale durante la codifica; sul file finale solo fotogrammi e peso.
4. Sara ha APPROVATO tutti i quiz e tutti i testi delle voci (11/11). Le voci nuove sono già richieste alla master 1 sul ramo voci-<tag>: controlla ogni 20 minuti `git fetch origin voci-<tag>` e importa con voci_auto.py quando arrivano; intanto monta con segnaposto della stessa durata stimata e sostituisci solo l'audio alla fine (volume16.py rifà solo l'audio).

## Macchina (condivisa con altri 3 agenti: rispetta i limiti)
- 4 CPU, 15 GB RAM, circa 28 GB di disco liberi PER TUTTI. Tu puoi usare al massimo 6 GB: cancella subito i pezzi intermedi grandi.
- Cartella di lavoro: /home/claude/lezioni/<tag>/ (crea con il kit, vedi sotto). /home/claude/lezioni è un link al clone git /home/user/lezioni (ramo scambio-claude2: NON fare commit lì, NON cambiare ramo lì).
- Kit già scompattato in /home/claude (kit_prod, moda_tec, v5, asr_pk, sigle_zip...). Font installati. Trascrizione Parakeet pronta in /tmp/asr/sherpa-onnx-nemo-parakeet-tdt-0.6b-v3-int8/ (prova: cd /home/claude/asr_pk && python3 pk.py it.wav /tmp/t.jsonl 0). Chromium/Playwright preinstallato: non reinstallarlo.
- Strumenti aggiornati: /home/user/lezioni/kit/tools/ NON c'è sul ramo scambio-claude2; prendili così: `git -C /home/user/lezioni show origin/main:kit/tools/NOME.py > tools/NOME.py` (fai prima `git -C /home/user/lezioni fetch -q origin main`). Leggi anche origin/main:kit/REGOLE.md e /home/claude/kit_prod/METODO_v2_lezioni_dal_PDF.md + LEGGIMI_v5_8-11.md + WORKFLOW_videolezioni.md: è il metodo approvato (sincronia slide al secondo: non cambiarlo).
- Release (materiali): `gh api repos/zagavre-ai/lezioni/releases/tags/<tag>` per la lista; scarica con `curl -sSL -o FILE https://github.com/zagavre-ai/Lezioni/releases/download/<tag>/<NOME>`.
- Voci Kore già generate: ramo voci-<tag> (`git -C /home/user/lezioni fetch -q --depth 1 origin voci-<tag>` poi `git -C /home/user/lezioni archive FETCH_HEAD scambio/<tag> | tar x -C <cartella>`). NON rigenerarle, NON chiederne di nuove stanotte. Se ti serve una voce nuova (testo nuovo), scrivi il testo in <cartella>/testi_voci_NUOVI.json, monta con un segnaposto della durata stimata (silenzio o la tua stima) e mettilo nel rapporto: Sara lo approva domattina.
- CODIFICA FINALE 1440p: una sola alla volta su tutta la macchina. Lanciala SEMPRE così:
  `flock /tmp/claude-0/codifica.lock nice -n 5 python3 tools/finale_a_pezzi.py lista.txt USCITA.mp4 > cod.log 2>&1 && touch cod.fatto`
  in background (run_in_background) e attendi; riprende da sola se si interrompe (rilancia lo stesso comando). Lavori in background vengono fermati dopo 2 h: usa marcatori .ok/.fatto e rilancia.
- Tutto il resto pesante (render Playwright, ffmpeg dei pezzi): usa `nice -n 10` e al massimo 2 thread (`-threads 2`).
- Log con `> log && touch .fatto`, mai `| tail`.

## Regole di produzione (definitive)
- Parte 50–60 min (fino a ~65 resta una Parte). D = docente pulito senza pause; I = inserti. Mai tagliare parole del docente. Arricchire solo con materiale del docente (suo PDF), niente riempitivi.
- Struttura: sigla e presentazione; per ogni argomento: titolo → docente con slide sincronizzate (la frase si accende quando la dice) → approfondimenti animati → ripasso breve con voce → scheda Quiz «5 domande · per continuare almeno l'80%» (jingle a 0,0 s); glossario, ripasso finale.
- CHIUSURA NUOVA (lezioni montate da ora): dopo il ripasso finale → scheda statica «Verifica finale» 5 s con bande blu sopra e sotto → sigla finale → intro «Compiti» ~3,5 s con jingle (stesso stile sonoro delle schede Quiz) → scheda statica «Compiti» 5 s con bande blu. Scrivi nello stato (--nota) i secondi esatti t_verifica e t_compiti. Riferimento: https://zagavre-ai.github.io/Lezioni/prova-video-compiti/ (gh-pages: prova-video-compiti/index.html).
- Mai il numero della lezione in titoli, slide, sigle, video (solo nei nomi dei file).
- Grafica Telesio: 1920×1080 (poi 1440p), colori #0B1530 #2060AF #FFE600, grigi #EEF0F4 #C9D0DC; vietati viola, verde, crema, mattone. Bricolage Grotesque 800 titoli, Figtree ≥30 px testo, DM Mono etichette. Colonna destra x ≥ 1490 libera per il docente. Piè di pagina «MATERIA · Prof./Prof.ssa Nome Cognome · Pagina N». Max 3 card per slide, tabelle mai spezzate.
- Quiz di argomento: 5 domande (1 giusta, 3 sbagliate, spiegazione) dal materiale del docente. Se esistono già (stato vecchio / quiz approvati) riusa quelli; se li scrivi nuovi, mettili nel rapporto come «da approvare».
- File finale: Materia_LezN_ParteN_1440p.mp4, 2560×1440 30 fps, x264 fast CRF 20, maxrate 16M, AAC 192k 48 kHz, < 400 MiB (sopra i 60 min parti da CRF 22). Parlato −16 LUFS (volume16.py). Sottotitoli .vtt con sub_finale.py sul video FINALE.
- Controlli prima di PRONTA: controllo_finale.py e controllo_jingle.py (scatto Quiz 0,0 s, docente mai fermo, fotogrammi = durata×30, peso, volume, sincronia su 4 punti, .vtt a campione). Scarto A/V 0,07 s accettabile.
- Con voci segnaposto la lezione NON è PRONTA: lo stato resta IN_MONTAGGIO (o IN_CODIFICA) con la nota «voci segnaposto: <elenco>».
- Stato: `python3 tools/stato.py <tag> --parte N --stato ... --invia` a ogni cambio di fase (stato.py usa REPO=/home/claude/lezioni: va bene). Se dopo 20 minuti di tentativi sei bloccato: stato FERMA con il motivo, e chiudi con il rapporto.
- Consegna: carica video e .vtt come allegati della release: `gh api -X POST "https://uploads.github.com/repos/zagavre-ai/lezioni/releases/<release_id>/assets?name=<NOME>" -H "Content-Type: application/octet-stream" --input FILE`. Se non riesce, lascia i file in /home/claude/lezioni/<tag>/consegna/ e scrivilo nel rapporto. Testo YouTube con testo_youtube.py in consegna/.
- Privacy: niente dati personali di alunni/docenti su GitHub. Non toccare kit/gestionale/, registro-compiti/, gh-pages, main.
- Misura i tuoi tempi: scrivi in <cartella>/TEMPI.txt l'ora di inizio e di fine di ogni fase (servono domattina).

## Rapporto finale alla master (massimo 15 righe)
stato raggiunto, durata/peso/fotogrammi misurati, t_verifica, t_compiti, controlli passati, che cosa resta (voci nuove da approvare, quiz da approvare), dove sono i file, ore impiegate per fase.
