import os,sys,json,shutil
sys.path.insert(0,'/home/user/work18/scambio/strumenti');sys.path.insert(0,'/home/user/work18/lib')
import schede_spagnolo as d
from render import rr,W
def frames(spec,key,fps=30):
    """rende i fotogrammi della scheda blu; ritorna 'cartella/%05d.jpg@fps' e durata in fotogrammi a 30"""
    import hashlib
    h=hashlib.md5(json.dumps(spec,sort_keys=True,ensure_ascii=False).encode()).hexdigest()[:8]
    out=f'{W}/st/dark_{key}_{h}';N=int(round(spec['dur']*fps))
    if os.path.exists(out+'/ok'):return out+'/%05d.jpg@'+str(fps),int(round(spec['dur']*30))
    shutil.rmtree(out,ignore_errors=True);os.makedirs(out)
    pg=rr().pg
    open(out+'/p.html','w').write('<!doctype html><meta charset=utf-8><style>%s</style><body>%s'%(d.CSS,d.BODY))
    pg.goto('file://'+out+'/p.html');pg.evaluate("document.fonts.ready");pg.add_script_tag(content=d.JS);pg.evaluate("(s)=>init(s)",spec)
    for n in range(N):
        pg.evaluate("([t,f])=>draw(t,f)",[n/fps,n]);pg.screenshot(path='%s/%05d.jpg'%(out,n+1),type='jpeg',quality=93)
    open(out+'/ok','w').write('1')
    return out+'/%05d.jpg@'+str(fps),int(round(spec['dur']*30))
def lastpng(pat,out):
    from asm import run
    if not os.path.exists(out):
        d_=pat.split('@')[0];fs=sorted(f for f in os.listdir(os.path.dirname(d_)) if f.endswith('.jpg'))
        run(['ffmpeg','-y','-loglevel','error','-i',os.path.dirname(d_)+'/'+fs[-1],out])
    return out
