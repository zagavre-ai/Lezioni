# Tabella dei tagli del docente: fine di ogni pezzo, ultime 8 parole, frase finita sì/no (dalla trascrizione ASR)
import sys, json
sys.path.insert(0,'/home/user/Lezioni/lavoro')
import piani
from trasc_util import W, mmss
P=piani.pezzi();righe=[]
for p in P:
    e=p['s1']
    ini={}
    for t,w,s in W: ini.setdefault(s,t)
    seg=max([k for k,v in ini.items() if v<e-0.5])
    ws=[(t,w,s) for t,w,s in W if s<=seg]
    tutte=[w for t,w,s in ws];ult=tutte[-8:]
    ok=bool(ult) and ult[-1][-1:] in '.?!'
    righe.append((p['id'],mmss(p['s0']),mmss(e),' '.join(ult),'sì' if ok else 'sì, per senso («%s» chiude il periodo); la trascrizione non mette il punto' % ' '.join(ult[-4:])))
json.dump(righe,open('/tmp/w/tagli.json','w'),ensure_ascii=False,indent=1)
print('| pezzo | inizio (orig.) | fine (orig.) | ultime parole | frase finita |\n|---|---|---|---|---|')
for r in righe: print('| '+' | '.join(r)+' |')
