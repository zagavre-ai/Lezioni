import sys,os,json,subprocess,numpy as np,random
sys.path.insert(0,'/home/claude/w/b')
from lib import *
ORIG=W+'/mat/LEZIONE 7 GLI STATI UNITI DAL BOOM ECONOMICO AL NEW DEAL.mp4'
def vframe(f,t,crop,size=(40,30)):
    cmd=['ffmpeg','-v','error','-ss',f'{t:.3f}','-i',f,'-frames:v','1','-vf',f'crop={crop},scale={size[0]}:{size[1]},format=gray','-f','rawvideo','-']
    r=subprocess.run(cmd,capture_output=True).stdout
    return np.frombuffer(r,np.uint8).astype(float) if len(r)==size[0]*size[1] else None
def tp_inv(iv,x):
    acc=0
    for a,b in iv:
        if x<=acc+(b-a): return a+(x-acc)
        acc+=b-a
    return iv[-1][1]
def check(video,tl,n_per=4,seed=1):
    random.seed(seed); res=[]
    pos={n:(t,l) for n,t,l in tl}
    for name,(T0,L) in pos.items():
        if not (name.startswith('Dprof') or name=='Dintro'): continue
        pn={'Dintro':'P0'}.get(name,'P'+name[5:])
        J=json.load(open(f'{B}/pz4/{pn}.mkv.json')); iv=J['iv']
        for k in range(n_per):
            x=random.uniform(1.0,L-1.0); tf=T0+x; to=tp_inv(iv,x)
            fin=vframe(video,tf,'412:309:1428:148')
            if fin is None: continue
            best=None
            for d in range(-9,10):
                o=vframe(ORIG,to+d/30,'184:138:863:337')
                if o is None: continue
                e=np.abs(o-fin).mean()
                if best is None or e<best[0]: best=(e,d)
            res.append((name,round(x,1),best[1],round(best[0],1)))
    return res
if __name__=='__main__':
    video=sys.argv[1]; tl=json.load(open(sys.argv[2]))
    r=check(video,tl)
    offs=[d for _,_,d,_ in r]
    print('campioni',len(r),'scarto fotogrammi (min,max,mediana):',min(offs),max(offs),np.median(offs))
    bad=[x for x in r if abs(x[2])>1]
    print('fuori ±1 fotogramma (0,033 s):',bad)
