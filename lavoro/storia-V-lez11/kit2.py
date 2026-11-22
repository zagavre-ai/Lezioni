import sys,os,json,subprocess,numpy as np,re,hashlib
sys.path.insert(0,'/home/user/work/build')
from L import *
SR=48000
JING=lambda n:'/home/user/Lezioni/kit/suoni/%s.wav'%n
_g=json.load(open(B+'/gain.json')) if os.path.exists(B+'/gain.json') else {}
def rdwav(p,ch=1):
    a=np.frombuffer(subprocess.run(['ffmpeg','-v','error','-i',p,'-ac',str(ch),'-ar',str(SR),'-f','f32le','-'],capture_output=True).stdout,np.float32)
    return a.reshape(-1,ch) if ch>1 else a
def lufs(p):
    r=subprocess.run(['ffmpeg','-hide_banner','-nostats','-i',p,'-af','ebur128=peak=true','-f','null','-'],capture_output=True,text=True).stderr
    m=re.findall(r'\n\s+I:\s+(-?[\d.]+) LUFS',r);return float(m[-1]) if m else None
def vgain(p):
    k=os.path.basename(p)+str(os.path.getsize(p))
    if k not in _g:
        l=lufs(p);_g[k]=(-16-l) if l is not None and l>-60 else 0.0
        json.dump(_g,open(B+'/gain.json','w'))
    return _g[k]
class Mix:
    def __init__(s,dur): s.n=int(round(dur*SR));s.a=np.zeros((s.n,2),np.float32)
    def add(s,t,x,gain_db=0.0,fade=0.03):
        if x.ndim==1: x=np.stack([x,x],1)
        x=x*np.float32(10**(gain_db/20))
        if fade:
            f=int(fade*SR);f=min(f,len(x)//2)
            if f>0:
                w=np.linspace(0,1,f,dtype=np.float32)[:,None];x=x.copy();x[:f]*=w;x[-f:]*=w[::-1]
        i=int(round(t*SR));j=min(s.n,i+len(x))
        if j>i: s.a[i:j]+=x[:j-i]
    def voice(s,t,name):
        p=vpath(name);x=rdwav(p,1);s.add(t,x,vgain(p),0.03)
    def jingle(s,t,name,gain=0.0): s.add(t,rdwav(JING(name),2),gain,0.0)
    def save(s,fn):
        a=np.clip(s.a,-1,1);subprocess.run(['ffmpeg','-y','-v','error','-f','f32le','-ar',str(SR),'-ac','2','-i','-',fn],input=a.tobytes(),check=True)
def nfr(d): return int(round(d*30))
