import sys,os,json
sys.path.insert(0,'/tmp/claude-0/w/prod')
import build_lez as B
from eng import *
import pyloudnorm as pyln
os.makedirs(W+'/mz',exist_ok=True)
B.build()
meter=pyln.Meter(SR)
def voice_gain(p):
    x=audio_load(p);l=meter.integrated_loudness(x)
    return 10**((-16-l)/20) if np.isfinite(l) else 1.0
def mix(it):
    n=int(it.nf/FPS*SR);y=np.zeros((n,2),np.float32)
    for (t,p,g) in it.audio:
        x=audio_load(p)
        if '/vox' in p:
            x=x*voice_gain(p)
            f=int(0.03*SR);x[:f]*=np.linspace(0,1,f)[:,None];x[-f:]*=np.linspace(1,0,f)[:,None]
        else:x=x*g
        s=int(t*SR);e=min(n,s+len(x));y[s:e]+=x[:e-s]
    return y
only=sys.argv[1:]
for it in B.ITEMS:
    if only and it.name not in only:continue
    mz=f'{W}/mz/{it.name}.mp4';au=f'{W}/mz/{it.name}.wav'
    import hashlib
    sig=hashlib.md5(json.dumps([[s[1] for s in it.states],getattr(it,'fr',None),[(a[1],os.path.getmtime(a[1])) for a in it.audio],it.nf],default=str).encode()).hexdigest()
    if os.path.exists(mz+'.ok') and open(mz+'.ok').read().split()[-1]==sig:continue
    if it.kind=='static':
        render_static(it,mz);write_wav(au,mix(it))
    elif it.kind=='prof':render_prof(it,mz,au)
    else:render_clip(it,mz,au)
    n=nframes(mz)
    if it.kind!='clip' and n!=it.nf:print('ATTENZIONE',it.name,n,it.nf,flush=True)
    if it.kind=='clip':it.nf=n
    open(mz+'.ok','w').write(f'{n} {sig}');print('ok',it.name,n,flush=True)
