# Ancore di sincronia della lezione 18 (tempi dal parlato del docente; unità = frase della slide in ordine)
import json,subprocess
T=json.load(open('/tmp/w18/t18.json'))
starts=[s['s'] for s in T]
sn=lambda t:min(starts,key=lambda x:abs(x-t))
V='/tmp/w18/LEZIONE 18 L_ITALIA REPUBBLICANA.mp4'
m=subprocess.run(['ffmpeg','-v','info','-i',V,'-vn','-af','ebur128','-f','null','-'],capture_output=True,text=True).stderr
I=float([l for l in m.split('\n') if 'I:' in l][-1].split('I:')[1].split('LUFS')[0])
def arg(t0,t1,anc,imm=()):
    return dict(t0=sn(t0),t1=sn(t1) if t1<4270 else 4274.4,ancore=[[sn(a),u] for a,u in anc],immagini=[[sn(a),sn(b),p,c] for a,b,p,c in imm])
B={
 'video':V,'pdf':'/tmp/w18/LEZIONE 18.pdf','trascrizione':'/tmp/w18/t18.json','gain_db':round(-16-I,2),
 'modello':'/tmp/m01/p1.mp4','sfin':[3219.666],'cintro':[3226.266],'d0':[0.0,sn(187)],
 'arg':{
  '1':arg(187,663,[(187,0),(222,0),(270,1),(390,2),(462,3),(484,4)]),
  '2':arg(663,1870,[(663,1),(846,0),(1630,2),(1680,3),(1820,4)],[(848,880,4,'De Gasperi'),(1840,1870,4,'De Gasperi')]),
  '3':arg(1870,2098,[(1870,0),(2011,1),(2046,2)]),
  '4':arg(2098,3163,[(2098,0),(2504,1),(2745,2),(2789,3),(2842,4)],[(2204,2477,5,'confine'),(2928,2954,8,'INA-Casa')]),
  '5':arg(3163,3500,[(3163,0),(3265,1),(3376,2),(3478,3)]),
  '6':arg(3500,4274.4,[(3500,0),(3583,1),(3730,0),(3784,2),(4059,1),(4099,2)],[(3816,3825,11,'Fanfani e Moro')]),
 }}
json.dump(B,open('/tmp/w18/ancore.json','w'),indent=1)
print('gain',B['gain_db'],'I',I)
for k,v in B['arg'].items():print(k,round(v['t0'],1),round(v['t1'],1),[(round(a),u) for a,u in v['ancore']],v['immagini'])
print(B['d0'])
