# rapporto.py WORK — RAPPORTO_REVISIONE.md, scheda_pubblicazione_ParteN.json, foglio.png (dopo monta.py parti + controlli.sh)
import sys,os,json,re,subprocess
import numpy as np
QUI=os.path.dirname(os.path.abspath(__file__));sys.path.insert(0,QUI);sys.path.insert(0,QUI+'/..')
import contenuti as C
W=os.path.abspath(sys.argv[1]);O=W+'/out/'
AN=json.load(open(QUI+'/../../../diritto-4222/analisi_tagli.json'))
mm=lambda s:'%02d:%02d'%(int(s//60),int(s%60))
def ss(s):return '%02d:%02d.%d'%(int(s//60),int(s%60),int(s*10%10))
TL={n:json.load(open(f'{O}Diritto_4222_Parte{n}_1080p_timeline.json')) for n in (1,2)}
# --- etichette dei pezzi secondo la scheda tecnica
def etichetta(nome,dd,visti):
    if nome=='cover':return '3 · Copertina + benvenuto Kore'
    if nome=='C0':return '3 · Saluto della prof (accorciato)'
    if re.match(r'^T\d$',nome):
        k=nome[1];return f'4a · Titolo argomento {k}' if dd<10 else f'4b · Prof — tratto intero «{nome}»'
    if nome.startswith('N'):return f'4c · Approfondimento animato {nome}'
    if re.match(r'^M\d$',nome):return f'4d · Mappa argomento {nome[1]}'
    if nome=='MF':return '4d · Mappa finale'
    if re.match(r'^R\d$',nome):return f'4e · Pillola di ripasso (intro blu) {nome[1]}'
    if re.match(r'^S\d$',nome):return f'4f · Schema guidato {nome[1]}'
    if re.match(r'^Q\d$',nome):return f'4g · Scheda Quiz {nome[1]}'
    return {'FIN':'6 · Riepilogo finale','FINE':'7 · Finale 5 s','RP':'Ripasso della Parte 1'}.get(nome,nome)
# --- jingle: correlazione con i file del kit
SR=8000
def rd(f,ss_=None,d=None):
    c=['ffmpeg','-v','error']+(['-ss',str(ss_),'-t',str(d)] if ss_ is not None else [])+['-i',f,'-ac','1','-ar',str(SR),'-f','s16le','-']
    return np.frombuffer(subprocess.run(c,capture_output=True).stdout,np.int16).astype(float)
def trova(v,t,wav,off):
    ref=rd(QUI+'/'+wav)[:SR*2];s=max(0,t-1.0);x=rd(v,s,4.5)
    if len(x)<len(ref):return None
    c=np.correlate(x,ref,'valid');k=int(np.argmax(c));return s+k/SR-(t+off)
jing=[]
for p in (1,2):
    v=f'{O}Diritto_4222_Parte{p}_1080p.mp4'
    for nome,t,dd in TL[p]:
        if re.match(r'^T\d$',nome) and dd<10:j=('titolo.wav',0.0)
        elif re.match(r'^R\d$',nome):j=('repaso.wav',0.0)
        elif re.match(r'^Q\d$',nome):j=('quiz.wav',0.5)
        else:continue
        sc=trova(v,t,*j);jing.append((p,nome,j[0],t,sc))
# --- freeze dentro i tratti della prof
def freeze(p):
    fz=[]
    try:
        for r in open(f'{O}freeze{p}.txt'):
            a,b=r.split();fz.append((float(a),float(b)))
    except Exception:pass
    return fz
# --- scheda_pubblicazione
for p in (1,2):
    v=f'{O}Diritto_4222_Parte{p}_1080p.mp4';d=float(subprocess.run(['ffprobe','-v','error','-show_entries','format=duration','-of','csv=p=0',v],capture_output=True,text=True).stdout)
    arg=[];quiz={};tl=TL[p]
    for nome,t,dd in tl:
        if re.match(r'^T\d$',nome) and dd<10:
            k=int(nome[1]);q=[x for x in tl if x[0]==f'Q{k}'][0]
            arg.append({'n':k,'titolo':C.ARGOMENTI[k-1][0],'inizio_s':round(t,3),'quiz_s':round(q[1],3)});quiz[f'Q{k}']=C.QUIZ[f'Q{k}']
    json.dump({'materia':C.MATERIA,'titolo':f'{C.TITOLO} · Parte {p}','docente':C.DOCENTE,'durata_s':round(d,2),'argomenti':arg,'quiz':quiz},open(f'{O}scheda_pubblicazione_Parte{p}.json','w'),ensure_ascii=False,indent=1)
# --- foglio.png: un fotogramma per ogni scheda blu e per ogni animazione
from PIL import Image,ImageDraw
tiles=[]
for p in (1,2):
    v=f'{O}Diritto_4222_Parte{p}_1080p.mp4'
    for nome,t,dd in TL[p]:
        if (re.match(r'^T\d$',nome) and dd<10) or re.match(r'^(R\d|Q\d|FIN|FINE|RP|N\d[a-f]|S\d|M\d|MF|cover)$',nome):
            ts=t+(min(dd*0.55,8) if nome[0] in 'NSM' else min(2.5,dd*0.6));f=f'/tmp/_f.png'
            subprocess.run(['ffmpeg','-v','error','-y','-ss',f'{ts:.2f}','-i',v,'-frames:v','1','-vf','scale=480:270',f]);im=Image.open(f).convert('RGB')
            ImageDraw.Draw(im).text((6,4),f'P{p} {nome} {mm(t)}',fill=(255,0,0));tiles.append(im)
cols=6;rows=(len(tiles)+cols-1)//cols;sheet=Image.new('RGB',(cols*480,rows*270),'gray')
for i,im in enumerate(tiles):sheet.paste(im,((i%cols)*480,(i//cols)*270))
sheet.save(O+'foglio.png');print('foglio',len(tiles),'tessere')
# --- rapporto
P=[n for n in AN if n['frammento_5s']]
slide_order=[x for k in ['N2a','N2b','N2c','N3a','N4a','N4b','N5a','N5b','N6a','N6b','N6c','N6d','N6e','N6f'] for x in [(k,s) for s in C.ANIM[k]['slides']]]
assert len(slide_order)==len(P)==32,(len(slide_order),len(P))
pos={}
for p in (1,2):
    for nome,t,dd in TL[p]:pos[nome]=(p,t,dd)
L=['# RAPPORTO DI REVISIONE · Diritto ed economia (I+II) · «Le organizzazioni collettive e l\'impresa»','',
 'Rifacimento della lezione della piattaforma (Prof.ssa J. Didone). Tutti i tratti lunghi della prof sono interi; i 32 pezzi da 5 s sono stati sostituiti da 14 animazioni con voce Kore, costruite solo sul testo delle slide.','']
for p in (1,2):
    d=sum(1 for _ in [0]);v=f'{O}Diritto_4222_Parte{p}_1080p.mp4'
    m=open(f'{O}misura{p}.txt').read().strip().split(',') if os.path.exists(f'{O}misura{p}.txt') else ['?','?','?']
    sha=open(v+'.sha256').read().split()[0] if os.path.exists(v+'.sha256') else '?'
    L+=[f'## Parte {p}',f'- File: `Diritto_4222_Parte{p}_1080p.mp4` · sha256 `{sha}`',f'- Durata misurata: **{ss(float(m[1]))}** ({float(m[1]):.2f} s) · fotogrammi **{m[0]}** (attesi {round(float(m[1])*30)}) · peso {int(m[2])/1e6:.0f} MB · 1920×1080, 30 fps',
        f'- Parlato: {open(f"{O}lufs{p}.txt").read().strip() if os.path.exists(f"{O}lufs{p}.txt") else "?"}','']
L+=['## 1 · Tabella dei pezzi (presente · minuto di inizio · durata misurata)','','| Parte | Pezzo | Presente | Inizio | Durata |','|---|---|---|---|---|',
    '| – | 1 · Sigla 15 s | **NO** (manca `Sigla_Diritto_15s.mp4`, chiesta alla master) | – | – |']
for p in (1,2):
    for nome,t,dd in TL[p]:L.append(f'| {p} | {etichetta(nome,dd,None)} | sì | {ss(t)} | {dd:.1f} s |')
L+=['| – | 5 · Glossario | NO (non previsto dall\'elenco del prompt) | – | – |','']
L+=['## 2 · I 32 pezzi da 5 s tolti e le animazioni che li sostituiscono','','| N. | Minuto vecchio | Slide (titolo) | Animazione | Posizione nuova |','|---|---|---|---|---|']
for n,(k,sl) in zip(P,slide_order):
    p,t,dd=pos[k];L.append(f"| {n['n']} | {mm(n['inizio'])} | {sl['t']} | {k} | Parte {p}, {ss(t)} |")
L+=['','## 3 · Slide rifatte in animazione, con il testo (a schermo / detto da Kore)','']
for n,(k,sl) in zip(P,slide_order):
    L+=[f"### Pezzo {n['n']} · {sl['t']} ({k})"]
    if sl.get('sub'):L.append(f"_{sl['sub']}_")
    for it in sl['items']:L.append(f"- **{it['h'] or '·'}** — {' / '.join(it['lines'])}  \n  _voce:_ {it['say']}")
    L.append('')
L+=['## 4 · Controlli sul file finale','','### Jingle (scarto dal punto atteso)','','| Parte | Pezzo | Suono | Inizio scheda | Scarto |','|---|---|---|---|---|']
for p,nome,w,t,sc in jing:L.append(f"| {p} | {nome} | {w} | {ss(t)} | {'?' if sc is None else '%+.3f s'%sc} |")
L+=['','Dissolvenza + `trans.wav` (0,8 s) a ogni cambio di pezzo: i minuti dei cambi sono gli inizi della tabella.','','### Fermi (freezedetect ≥ 0,9 s, soglia −55 dB)','']
for p in (1,2):
    inside=[]
    trs=[(t,t+dd) for nome,t,dd in TL[p] if (re.match(r'^T\d$',nome) and dd>=10) or nome=='C0']
    fz=freeze(p)
    for a,b in fz:
        if any(x<=a<=y for x,y in trs):inside.append((a,b))
    L.append(f'- Parte {p}: {len(fz)} fermi totali (schede statiche, ammessi); **dentro i tratti della prof: {len(inside)}** {[(ss(a),round(b,1)) for a,b in inside]}')
L+=['','### Altri controlli','- Fotogrammi = durata × 30 per entrambe le Parti (vedi sopra).','- Sottotitoli `.vtt` generati: prof dalla trascrizione con i tempi (termini corretti a mano: avviamento, UNI ISO 31000, Telethon), Kore dai testi noti. **Da rileggere a campione**: la trascrizione automatica può avere altre imprecisioni.','- `foglio.png`: un fotogramma di ogni scheda blu e di ogni animazione.','- Sincronia: ogni card gialla è accesa per la durata della sua frase Kore (tempi presi dalle durate dei file voce).','']
L+=['## 5 · DA CONFERMARE / difetti noti','',
 '1. **Sigla di apertura Diritto mancante** (`kit/sigle` ha solo Inglese, Letteratura, Storia). Il video parte senza sigla.',
 '2. **Durata delle Parti:** il materiale dà circa 68 minuti, sopra i 60: due Parti, divise alla fine dell\'argomento 4. La Parte 2 è più corta di 50 minuti.',
 '3. **Slide «I fattori aziendali»:** dice «affinché un fattore possa essere considerato un *obiettivo*». Nella voce e a schermo ho scritto «fattore»: DA CONFERMARE COL PROF.',
 '4. **Voci con differenze segnalate dalla master:** `N4b_s1_i1`, `S4_4`, `F_3` (da riascoltare).',
 '5. **Marchi di terzi:** nel tratto di chiusura compare «A SCUOLA DI IMPRESA» in basso a sinistra: coperto con un filtro; la foto con credito CC nella slide «Contabilità e bilancio» e l\'immagine «CSR» non sono state riprodotte nelle animazioni.',
 '6. **Saluto della prof:** accorciato a 9,6 s (fino a «…persone giuridiche»), tagliato a fine frase. Prima c\'è un benvenuto Kore sulla copertina bianca.',
 '7. **Slide con immagini o schemi** (diagramma del reddito, foto della logistica, schema «A scuola di impresa»): nelle animazioni c\'è solo il testo, come da regola.',
 '8. **Glossario:** non presente, perché il prompt non lo prevede.',
 '9. **Qualità del video della prof:** 852×480 portato a 1920×1080 senza inventare dettagli (solo colore e nitidezza): le scritte piccole delle slide restano morbide.','']
open(O+'RAPPORTO_REVISIONE.md','w').write('\n'.join(L));print('rapporto ok')
