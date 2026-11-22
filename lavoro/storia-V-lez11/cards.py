import sys,os,json,subprocess
sys.path.insert(0,'/home/user/work/build')
from L import *
import schede
os.makedirs(B+'/cards',exist_ok=True)
specs=[]
for T in TOP:
    n=T['n']
    specs.append((f'T{n}',dict(type='title',num='%02d'%n,total=6,lines=T['lines'],ex=T['ex'],fs=T['fs'],lineY=720 if len(T['lines'])==2 else 720,dur=4.0)))
    R=f'R{n}';fr=tempi_frasi(R,TXT[R]);d=dur(vpath(R))
    D=round(max(14.0,1.0+d+1.7),2)
    specs.append((f'P{n}',dict(type='repaso',kicker='Pillola di storia',big='RIPASSO',topic=T['t'],tfs=tfs(T['t']),caps=[[round(1.0+a,2),round(1.0+b,2),cifre(f)] for a,b,f in fr],dur=D)))
    specs.append((f'Q{n}',dict(type='quiz',act=f'Quiz {n}',tfs=tfs(T['t']),topic=T['t'],pts="5 domande · per continuare almeno l'80%",dur=5.0)))
fr=tempi_frasi('RIEP1',TXT['RIEP1']);d=dur(vpath('RIEP1'))
ti=[round(1.0+fr[i+1][0]-0.2,2) for i in range(6)]
specs.append(('FINALE',dict(type='final',kicker='Storia V',l1='RIEPILOGO',l2='FINALE',items=[[T['t'],''] for T in TOP],sub='Ripassiamo insieme ciò che abbiamo imparato.',ti=ti,dur=round(1.0+d+1.7,2))))
specs.append(('VERIFICA',dict(type='quiz',act='Verifica finale',tfs=64,topic=TITOLO,pts="10 domande · per continuare almeno l'80%",dur=5.0)))
specs.append(('COMPITI',dict(type='simple',kicker='Storia V',big='Compiti',sub='Ora tocca a te',fs=210,dur=3.5)))
json.dump(dict(specs),open(B+'/cards/specs.json','w'),ensure_ascii=False,indent=1)
for nm,sp in specs:
    if os.path.exists(f'{B}/cards/{nm}.ok'): continue
    schede.render(sp,f'{B}/cards/{nm}',1.0)
    open(f'{B}/cards/{nm}.ok','w').write('1');print(nm,sp['dur'],flush=True)
