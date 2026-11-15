import json,numpy as np,subprocess
OFF=[0,921.0,1804.6,2654.03]
SEG=json.load(open('/home/user/w4/segdur.json'))   # (parte, i, a, b, durata reale)
# inizio reale di ogni pezzo nel docente tagliato
ST=[];acc=0.0
for p,i,a,b,x in SEG: ST.append((p,a,b,acc));acc+=x
TOT=acc
def tm(g):
    """tempo originale globale -> tempo nel docente tagliato (con le durate reali dei pezzi)"""
    p=max(i for i in range(4) if g>=OFF[i])+1;t=g-OFF[p-1];last=0.0
    for pp,a,b,s in ST:
        if pp<p: continue
        if pp>p: return last
        if t<a: return s
        if t<=b: return s+(t-a)
        last=s+(b-a)
    return last
def audio():
    return np.frombuffer(subprocess.run(['ffmpeg','-v','error','-i','/home/user/w4/dt/docente_all.mkv','-vn','-ac','1','-ar','16000','-f','f32le','-'],capture_output=True).stdout,np.float32)
def snap(x,t,before=2.0,after=0.5):
    sr=16000;w=int(0.15*sr);h=int(0.02*sr)
    a=max(0,int((t-before)*sr));b=min(len(x)-w,int((t+after)*sr));best=None
    for i in range(a,b,h):
        e=float((x[i:i+w]**2).mean())
        if best is None or e<best[0]:best=(e,i)
    return round((best[1]+w/2)/sr,3)
