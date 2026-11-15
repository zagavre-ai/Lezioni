# Ancore di sincronia della lezione 6 (tempi dal parlato del docente; unità = frase della slide)
import json,subprocess
T=json.load(open('/tmp/w06/t06.json'))
starts=[s['s'] for s in T]
sn=lambda t:min(starts,key=lambda x:abs(x-t))
V='/tmp/w06/LEZIONE 6 IL PRIMO DOPOGUERRA (1919-1925).mp4'
m=subprocess.run(['ffmpeg','-v','info','-i',V,'-vn','-af','ebur128','-f','null','-'],capture_output=True,text=True).stderr
I=float([l for l in m.split('\n') if 'I:' in l][-1].split('I:')[1].split('LUFS')[0])
END=T[-1]['e']
def arg(t0,t1,anc,imm=()):
    return dict(t0=sn(t0),t1=sn(t1) if t1<END-5 else END,ancore=[[sn(a),u] for a,u in anc],immagini=[[sn(a),sn(b),p,c] for a,b,p,c in imm])
B={'video':V,'pdf':'/tmp/w06/LEZIONE 6.pdf','trascrizione':'/tmp/w06/t06.json','gain_db':round(-16-I,2),
 'modello':'/tmp/m01/p1.mp4','sfin':[3219.666],'cintro':[3226.266],'d0':[0.0,sn(80)],
 'arg':{
  '1':arg(80,672,[(80,0),(154,1),(234,2),(355,4),(423,3),(433,3),(488,1)],[(434,672,4,'carta')]),
  '2':arg(672,1039,[(672,0),(792,1),(865,3),(900,2)],[(937,1039,4,'carta')]),
  '3':arg(1039,1416,[(1039,0),(1067,0),(1185,1),(1249,2),(1276,3)]),
  '4':arg(1416,1570,[(1416,0),(1417,2),(1438,1),(1524,3)]),
  '5':arg(1570,1747,[(1570,0),(1587,1),(1600,2),(1620,0),(1686,3)]),
  '6':arg(1747,2029,[(1747,0),(1773,1),(1854,2),(1918,3)],[(1936,2029,9,'carta')]),
  '7':arg(2029,2148,[(2029,0),(2071,1),(2131,2)]),
  '8':arg(2148,END,[(2148,0),(2257,1),(2271,2),(2287,3)]),
 }}
json.dump(B,open('/tmp/w06/ancore.json','w'),indent=1)
print('gain',B['gain_db'],'I',I)
for k,v in B['arg'].items():print(k,round(v['t0'],1),round(v['t1'],1),[(round(a),u) for a,u in v['ancore']],v['immagini'])
print(B['d0'])
