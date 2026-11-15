# Ancore di sincronia della lezione 15
import json,subprocess
T=json.load(open('/tmp/w15/t15.json'))
starts=[s['s'] for s in T]
sn=lambda t:min(starts,key=lambda x:abs(x-t))
V='/tmp/w15/LEZIONE 15 LA DECOLONIZZAZIONE (1945-1975).mp4'
m=subprocess.run(['ffmpeg','-v','info','-i',V,'-vn','-af','ebur128','-f','null','-'],capture_output=True,text=True).stderr
I=float([l for l in m.split('\n') if 'I:' in l][-1].split('I:')[1].split('LUFS')[0])
END=T[-1]['e']
def arg(t0,t1,anc,imm=()):
    return dict(t0=sn(t0),t1=sn(t1) if t1<END-5 else END,ancore=[[sn(a),u] for a,u in anc],immagini=[[sn(a),sn(b),p,c] for a,b,p,c in imm])
B={'video':V,'pdf':'/tmp/w15/LEZIONE 15.pdf','trascrizione':'/tmp/w15/t15.json','gain_db':round(-16-I,2),
 'modello':'/tmp/m01/p1.mp4','sfin':[3219.666],'cintro':[3226.266],'d0':[0.0,sn(107)],
 'arg':{
  '1':arg(107,421,[(107,0),(176,0),(212,2),(291,3),(369,1)]),
  '2':arg(421,622,[(421,3),(458,0),(558,2),(591,1)]),
  '3':arg(622,826,[(622,0),(704,1),(756,2),(800,3)]),
  '4':arg(826,1067,[(826,1),(880,0),(915,2),(1031,3)],[(1049,1067,6,'Asia')]),
  '5':arg(1067,1210,[(1067,0),(1131,1),(1144,2),(1197,3)]),
  '6':arg(1210,1549,[(1210,1),(1233,2),(1266,3),(1493,1),(1501,0)],[(1393,1481,8,'Maghreb')]),
  '7':arg(1549,1896,[(1549,0),(1634,1),(1710,2),(1861,3)],[(1722,1896,11,'Africa')]),
  '8':arg(1896,2160,[(1896,0),(1913,1),(2054,2),(2082,3)],[(2101,2160,13,'Palestina')]),
  '9':arg(2160,2393,[(2160,0),(2211,1),(2264,2),(2310,3)],[(2380,2393,15,'Sinai')]),
  '10':arg(2393,END,[(2393,0),(2444,1),(2470,2),(2514,3)]),
 }}
json.dump(B,open('/tmp/w15/ancore.json','w'),indent=1)
print('gain',B['gain_db'])
for k,v in B['arg'].items():print(k,round(v['t0'],1),round(v['t1'],1),len(v['ancore']),v['immagini'])
