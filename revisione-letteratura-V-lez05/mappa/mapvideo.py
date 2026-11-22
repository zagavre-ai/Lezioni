import json,sys,os,subprocess,glob,numpy as np
from PIL import Image
sys.path.insert(0,'/tmp/w/map')
exec(open('/tmp/w/map/mapstates.py').read().split("if __name__")[0])
VOX=sys.argv[1] if len(sys.argv)>1 else '/tmp/w/vox'
STEPS=[('MP01',['c']),('MP02',['pad']),('MP03',['vL','v1']),('MP04',['v2']),('MP05',['v3']),('MP06',['v4']),('MP07',['v5']),('MP08',['v6']),
 ('MP09',['fL','f1','f2']),('MP10',['pL','p1']),('MP11',['p2']),('MP12',['p3']),('MP13',['p4']),('MP14',['oL','o0']),
 ('MP15',['w1']),('MP16',['w2']),('MP17',['w3']),('MP18',['w4']),('MP19',['w5']),('MP20',['w6']),('MP21',['w7'])]
PREF=sys.argv[2] if len(sys.argv)>2 else 'MP'
def dur(n):
    p=f'{VOX}/{n.replace("MP",PREF)}.wav'
    if not os.path.exists(p): return 3.0
    return float(subprocess.run(['ffprobe','-v','error','-show_entries','format=duration','-of','csv=p=0',p],capture_output=True,text=True).stdout)
t=0.5;plan=[];vis=set()
for n,ids in STEPS:
    d=dur(n);vis=vis|set(ids)
    plan.append(dict(name=n,t0=t,voice_at=t+0.15,dur=d,vis=sorted(vis),hl=ids))
    t=t+0.15+d+0.5
FINAL=4.0;TOT=t+FINAL
os.makedirs('/tmp/w/map/h2',exist_ok=True);os.makedirs('/tmp/w/map/p2',exist_ok=True)
files=[]  # (png,dur_s)
open('/tmp/w/map/h2/m_empty.html','w').write(state(set(),set()));files.append(('m_empty',0.5))
for i,s in enumerate(plan):
    nm=f'm_{i:02d}';open(f'/tmp/w/map/h2/{nm}.html','w').write(state(set(s['vis']),set(s['hl'])))
    nxt=plan[i+1]['t0'] if i+1<len(plan) else t
    files.append((nm,nxt-s['t0']))
open('/tmp/w/map/h2/m_final.html','w').write(state(set(n[0] for n in N),set()));files.append(('m_final',FINAL))
json.dump({'plan':plan,'tot':TOT,'files':files},open('/tmp/w/map/plan.json','w'),ensure_ascii=False,indent=1)
print('durata mappa s',round(TOT,2))
