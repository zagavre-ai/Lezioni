# Piano della lezione 12: segmenti, tempi vecchi (V) e nuovi (N). Si tengono le durate e i fotogrammi totali.
import json
TL=json.load(open('../consegna-letteratura-V-lez12/timeline.json'))
OLD={n:(a,d) for n,a,d in TL}
# orig: [inizio,fine) del prof nell'originale (continuo, senza sovrapposizioni, tagli a fine frase)
CUT=[0.15,96.15,250.17,395.95,633.70,915.60,1241.37]
DSEG={f'D{k}':(CUT[k],CUT[k+1]) for k in range(6)}
DSEG['D2']=(CUT[2],394.9)      # il prof tace fino a 401,2: si taglia il silenzio (sono fuori parole)
DSEG['D3']=(400.5,CUT[4])
OLD_D={k:OLD[k] for k in DSEG}
# blocchi in ordine con il tempo vecchio d'inizio; la durata di blocco = fino all'inizio del successivo (compresi i vuoti)
order=[]
real=[('SIGLA',0.0),('INTRO1',OLD['INTRO1'][0]),('D0',OLD['D0'][0]),('T1',OLD['T1'][0]),('D1',OLD['D1'][0]),
('AN1',300.033),('AN2',383.6),('AN3',445.433),('AN4',503.833),('S1',568.667),('Q1',613.133),
('T2',OLD['T2'][0]),('D2',OLD['D2'][0]),('AN5',775.167),('AN6',825.4),('AN7',889.3),('AN8',949.7),('AN9',1005.5),('S2',1075.1),('Q2',1118.266),
('T3',OLD['T3'][0]),('D3',OLD['D3'][0]),('AN10',1310.867),('AN11',1368.767),('AN12',1433.6),('AN13',1497.967),('AN14',1559.067),('S3',1623.97),('Q3',1654.867),
('T4',OLD['T4'][0]),('D4',OLD['D4'][0]),('AN15',2001.633),('AN16',2053.267),('AN17',2113.333),('AN18',2157.867),('AN19',2230.733),('AN20',2288.533),('S4',2353.43),('Q4',2395.399),
('T5',OLD['T5'][0]),('D5',OLD['D5'][0]),('AN21',2738.2),('AN22',2804.267),('AN23',2871.533),('AN24',2946.933),('AN25',3007.467),('AN26',3066.9),('S5',3133.4),('Q5',3175.099),
('ANF',3180.4),('GL1',3253.3),('RF1',3313.266),('FIN1',3369.033),('VER',3378.633),('SFIN',3385.233),('CI1',3391.833),('COMP',3396.933)]
TOT=3403.4667
blocks=[]
for i,(n,a) in enumerate(real):
    b=real[i+1][1] if i+1<len(real) else TOT
    blocks.append([n,a,b])
if __name__=='__main__':
    for n,a,b in blocks: print(n,round(a,3),round(b,3),round(b-a,2))
