# File dei testi da generare con Vox Studio · uso: testi_txt.py testi_voci.json "Titolo" uscita.txt NOME1 NOME2 ...
import json,sys
T=json.load(open(sys.argv[1]));tit=sys.argv[2];out=sys.argv[3];names=sys.argv[4:]
tot=sum(len(' '.join(T[k])) for k in names)
L=[f'TESTI DA GENERARE — {tit}','',f'{len(names)} file, {tot} caratteri in tutto.',
'Un file audio per ogni blocco, sempre con la stessa voce (Kore, stile «Docente E-Learning BES/DSA»). Salva ogni file con il nome indicato',
'(es. S1.wav) e allegali alla chat: le frasi vengono separate e controllate in automatico.','']
for k in names:
    t=' '.join(T[k]);L+=['='*70,f'FILE: {k}   ·   {len(t)} caratteri','='*70,'',t,'']
open(out,'w').write('\n'.join(L));print(out,len(names),'file',tot,'caratteri')
