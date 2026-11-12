# Testo pronto per YouTube (titolo, descrizione con capitoli, tag, playlist, visibilità) da scheda_pubblicazione.json.
# uso: python3 testo_youtube.py SCHEDA.json "Materia completa|Nome breve per il titolo" "Prof./Prof.ssa Nome" "Lezione N · Titolo" PARTE [TIMELINE.json] > testo.txt
# Capitoli: 0:00 Introduzione, poi l'inizio di ogni argomento (misurato), poi glossario/ripasso finale se c'è la timeline.
import sys,json
S=json.load(open(sys.argv[1]));MAT,DOC,LEZ,PAR=sys.argv[2:6];MB=MAT.split('|')[-1].strip();MAT=MAT.split('|')[0].strip();TL=json.load(open(sys.argv[6])) if len(sys.argv)>6 else []
def t(s):s=int(s);return '%d:%02d:%02d'%(s//3600,s%3600//60,s%60) if s>=3600 else '%d:%02d'%(s//60,s%60)
cap=[(0,'Introduzione')]+[(a['inizio_s'],'%s. %s'%(a['n'],a['titolo'])) for a in S['argomenti']]
for n,s,l in TL:
    if n.startswith('GL') and s>cap[-1][0]+10:cap.append((s,'Glossario e ripasso finale'));break
cap=[c for i,c in enumerate(cap) if i==0 or c[0]-cap[i-1][0]>=10]
tit=f"{MB} · {LEZ}"+(f" · Parte {PAR}" if PAR not in ('','0') else '')
if len(tit)>100:tit=tit[:97]+'…'
print('TITOLO:\n'+tit+'\n')
print('DESCRIZIONE:')
print(f"{MAT} · {LEZ}"+(f" · Parte {PAR}" if PAR not in ('','0') else '')+f"\nDocente: {DOC}\nCentro Studi Telesio\n")
print('Argomenti:');[print(f"{t(s)} {n}") for s,n in cap]
print('\nAl termine di ogni argomento il video si ferma per il quiz di verifica (5 domande).\nSottotitoli in italiano disponibili.\n© Centro Studi Telesio. Riproduzione vietata.\n')
print('TAG:\n'+', '.join([MAT,'Centro Studi Telesio','videolezione']+[a['titolo'] for a in S['argomenti']][:8])+'\n')
print('PLAYLIST: '+MAT+'\nVISIBILITÀ: Non in elenco\nPUBBLICO: No, non è per bambini\nSOTTOTITOLI: carica il file .vtt con lo stesso nome del video (lingua: Italiano)')
