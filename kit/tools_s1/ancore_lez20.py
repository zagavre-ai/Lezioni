# Ancore di sincronia della lezione 20
import json,subprocess,sys
sys.path.insert(0,'/home/user/Lezioni/kit/tools_s1')
T=json.load(open('/tmp/w20/t20.json'))
starts=[s['s'] for s in T]
sn=lambda t:min(starts,key=lambda x:abs(x-t))
V='/tmp/w20/LEZIONE 20 GLI ANNI NOVANTA IL MONDO POST-BIPOLARE.mp4'
m=subprocess.run(['ffmpeg','-v','info','-i',V,'-vn','-af','ebur128','-f','null','-'],capture_output=True,text=True).stderr
I=float([l for l in m.split('\n') if 'I:' in l][-1].split('I:')[1].split('LUFS')[0])
END=T[-1]['e']
def arg(t0,t1,anc,imm=()):
    return dict(t0=sn(t0),t1=sn(t1) if t1<END-5 else END,ancore=[[sn(a),u] for a,u in anc],immagini=[[sn(a),sn(b),p,c] for a,b,p,c in imm])
B={'video':V,'pdf':'/tmp/w20/LEZIONE 20.pdf','trascrizione':'/tmp/w20/t20.json','gain_db':round(-16-I,2),
 'modello':'/tmp/m01/p1.mp4','sfin':[3219.666],'cintro':[3226.266],'d0':[0.0,sn(234)],
 'arg':{
  '1':arg(234,1332,[(234,0),(292,1),(497,2),(836,3),(1007,3)],[(1085,1101,3,'Cecenia')]),
  '2':arg(1332,1608,[(1332,0),(1407,1),(1560,2)]),
  '3':arg(1608,2125,[(1608,0),(1770,1),(1946,2)],[(1998,2112,7,'Iugoslavia')]),
  '4':arg(2125,2636,[(2125,0),(2181,3),(2258,1),(2472,4)],[(2467,2634,9,'UE')]),
  '5':arg(2636,2921,[(2636,0),(2652,1),(2719,2),(2809,3)],[(2860,2921,11,'Berlusconi')]),
  '6':arg(2921,3104,[(2921,0),(2956,1),(2977,2),(2990,3),(3005,4),(3030,1)]),
  '7':arg(3104,3229,[(3104,0),(3146,1),(3164,3),(3197,2)]),
  '8':arg(3229,END,[(3229,0),(3241,1),(3267,2),(3308,3)]),
 }}
json.dump(B,open('/tmp/w20/ancore.json','w'),indent=1)
print('gain',B['gain_db'])
for k,v in B['arg'].items():print(k,round(v['t0'],1),round(v['t1'],1),[(round(a),u) for a,u in v['ancore']],v['immagini'])
