import sys,json,time;sys.path.insert(0,'/home/user/Lezioni/lavoro_lez03')
from scene_doc import *
def intro_k():
    for k in range(60,10,-1):
        a,b=piece_range(0,k);subs=tagli_pause(a,b)
        if sum(y-x for x,y in subs)<=176 and SENT[k][0]-SENT[k-1][1]>0.35 and SENT[k][3]-SENT[k][2]>=3:return k
kI=intro_k()
json.dump({'kI':kI},open('/tmp/w/b/kI.json','w'))
P=piano_scene(kI);res={}
# i numeri di pagina si assegnano nell'ordine delle scene
for sc in P:
    t=time.time();pc=build_scene(sc);res[sc['nome']]=pc
    print(sc['nome'],pc['n'],'fr','%.0fs'%(time.time()-t),flush=True)
json.dump(res,open('/tmp/w/b/doc_pieces.json','w'),default=str)
open('/tmp/w/b/doc.fatto','w').write('ok')
