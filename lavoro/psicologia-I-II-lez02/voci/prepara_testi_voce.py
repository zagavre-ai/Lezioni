# Prepara il file di testo da dare alla coordinatrice per generare le voci con Vox Studio / ElevenLabs:
# un blocco per file audio, con il nome da dare al file e il numero di caratteri.
# uso: python3 prepara_testi_voce.py "Titolo materia" NOME1 NOME2 ...  → voci/Testi_voci_da_generare.txt
# testi: voci/testi_voci.json {NOME:[frasi]} se c'è, altrimenti estese_P1.F
import sys,os,json;sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
D=os.path.dirname(os.path.abspath(__file__))+'/';TJ=D+'testi_voci.json'
T=json.load(open(TJ)) if os.path.exists(TJ) else {}
try:
    import estese_P1 as X;[T.setdefault(k,v) for k,v in X.F.items()]
except Exception:pass
tit=sys.argv[1];names=sys.argv[2:];tot=sum(len(' '.join(T[k])) for k in names)
out=[f'TESTI DA GENERARE — {tit}','',f'{len(names)} file, {tot} caratteri in tutto.',
'Un file audio per ogni blocco, sempre con la stessa voce femminile (quella approvata). Salva ogni file con il nome indicato',
'(es. S1.mp3) e allegali alla chat: le frasi vengono separate e controllate in automatico.','']
for k in names:
    t=' '.join(T[k]);out+=['='*70,f'FILE: {k}.mp3   ·   {len(t)} caratteri','='*70,'',t,'']
open(D+'Testi_voci_da_generare.txt','w').write('\n'.join(out));print(D+'Testi_voci_da_generare.txt',tot,'caratteri')
