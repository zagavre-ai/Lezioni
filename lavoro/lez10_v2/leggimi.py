# LEGGIMI della consegna. uso: leggimi.py CARTELLA TAG "Titolo" N_lezione VIDEO.mp4 timeline.json sincronia.txt > LEGGIMI.md
import sys,json,os,subprocess
W,TAG,TIT,N,V,TLF,SY=sys.argv[1:8]
os.chdir(W)
d=float(subprocess.run(['ffprobe','-v','error','-show_entries','format=duration','-of','csv=p=0',V],capture_output=True,text=True).stdout)
TL={n:(t,du) for n,t,du in json.load(open(TLF))}
S=json.load(open('scheda_pubblicazione.json')) if os.path.exists('scheda_pubblicazione.json') else {}
mm=lambda x:'%d:%02d'%(x//60,x%60)
doc=sum(du for n,(t,du) in TL.items() if n.startswith('D'))
L=[f'# Inglese AFM triennio · Lezione {N} · {TIT}','',f'Tag: `{TAG}` · una sola Parte · durata misurata **{mm(d)}** ({d:.1f} s) · prof {mm(doc)}, intera, senza tagli. Versione v2 (modello grafico Spagnolo Lez. 1): sostituisce la v1.',
 f'Video 1080p, x264 veryfast CRF 19, AAC 192k; {os.path.getsize(V)/2**20:.1f} MiB; a pezzi da 90 MiB (`.parte_NN`) + `.sha256`.','',
 '## Come ricomporre il video','```','cat '+V+'.parte_* > '+V,'sha256sum -c '+V+'.sha256','```','',
 '## Struttura','- sigla, benvenuto (voce Kore, inglese B1), docente con slide sincronizzate e parole chiave tradotte in italiano;',
 '- per ogni argomento: titolo, docente, mappa concettuale animata (voce Kore), scheda Quiz (5 domande, almeno 80%);',
 '- mappa finale, saluto della docente, glossario (24 parole inglese/italiano), ripasso finale, verifica finale, compiti, finale 5 s con avviso dei diritti.',
 f'- `t_verifica` = {TL["FIN1"][0]:.3f} s · `t_compiti` = {TL["CMPI"][0]:.3f} s (bande blu su quiz, verifica e compiti).','',
 '## Argomenti (inizio nel video)']
for a in S.get('argomenti',[]): L.append(f"- {mm(a['inizio_s'])} · {a['n']}. {a['titolo']}")
L+=['','## Controllo di sincronia (righe a caso, cosa si sente quando la riga si accende)','']+open(SY).read().strip().splitlines()+['',
 '## File','- `Mappe_'+TAG+'.pdf`: mappe A4 orizzontale, una per pagina (una per argomento + mappa finale), stessa grafica del video.',
 '- `quiz_argomenti.json`, `Quiz_Inglese_Lez'+N+'.txt`: quiz di fine argomento (da approvare).',
 '- `'+TAG+'_slide.pdf`: slide A4 orizzontale identiche al video (senza riquadro e fascia). `RAPPORTO_REVISIONE.md`, `controllo_minuti.jpg`, `timeline.json`.',
 '- `scheda_pubblicazione.json`, `testo_youtube.txt`, sottotitoli `.vtt` della docente (italiano e inglese, come parla lei; corretti a mano dove la trascrizione automatica sbagliava).']
print('\n'.join(L))
