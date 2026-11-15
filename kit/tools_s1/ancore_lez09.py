# Ancore di sincronia della lezione 9
import json,subprocess
T=json.load(open('/tmp/w09/t09.json'))
starts=[s['s'] for s in T]
sn=lambda t:min(starts,key=lambda x:abs(x-t))
V='/tmp/w09/LEZIONE 9 L_ITALIA DEL REGIME FASCISTA.mp4'
m=subprocess.run(['ffmpeg','-v','info','-i',V,'-vn','-af','ebur128','-f','null','-'],capture_output=True,text=True).stderr
I=float([l for l in m.split('\n') if 'I:' in l][-1].split('I:')[1].split('LUFS')[0])
END=T[-1]['e']
def arg(t0,t1,anc,imm=(),dopo=None):
    d=dict(t0=sn(t0),t1=sn(t1) if t1<END-5 else END,ancore=[[sn(a),u] for a,u in anc],immagini=[[sn(a),sn(b),p,c] for a,b,p,c in imm])
    if dopo:d['dopo']=dopo
    return d
B={'video':V,'pdf':'/tmp/w09/LEZIONE 9.pdf','trascrizione':'/tmp/w09/t09.json','gain_db':round(-16-I,2),
 'modello':'/tmp/m01/p1.mp4','sfin':[3219.666],'cintro':[3226.266],'d0':[0.0,sn(104)],
 'arg':{
  '1':arg(104,306,[(104,0),(123,0),(144,1),(160,2),(266,3)]),
  '2':arg(306,872,[(306,0),(346,0),(420,1),(467,2),(541,3),(683,4),(740,5)]),
  '3':arg(872,1375,[(872,0),(929,1),(1055,2),(1162,3)]),
  '4':arg(1375,1680,[(1375,0),(1427,0),(1466,1),(1560,3),(1619,4)]),
  '5':arg(1680,1923,[(1680,0),(1734,1),(1794,2)]),
  '6':arg(1923,2178,[(1923,0),(1933,1),(2040,2),(2114,2)]),
  '7':arg(2178,2496,[(2178,0),(2188,3),(2285,0),(2340,2),(2470,3)]),
  '8':arg(2496,2884,[(2496,0),(2569,2),(2822,3)]),
  '9':arg(2884,3071,[(2884,0),(2900,1),(2935,4),(2941,3),(3011,5)]),
  '10':arg(3071,3609,[(3071,0),(3171,1),(3260,2),(3314,4),(3464,5),(3542,6),(3560,7)],[],
           dopo=[dict(nome='D11',t0=sn(3609),t1=END,titolo='Il riepilogo del docente',sottotitolo='Il professore ripercorre i temi principali della lezione')]),
 }}
json.dump(B,open('/tmp/w09/ancore.json','w'),indent=1)
print('gain',B['gain_db'],'END',END)
for k,v in B['arg'].items():print(k,round(v['t0'],1),round(v['t1'],1),len(v['ancore']),'dopo' in v)
