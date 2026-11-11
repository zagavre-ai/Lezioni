# Punto di taglio nella pausa più silenziosa prima dell'inizio di un argomento.
# snap(t): cerca in [t-2.0, t+0.1] il tratto di 120 ms con meno energia e restituisce il suo centro.
import subprocess,numpy as np
_X={}
def _audio(wav):
    if wav not in _X:
        _X[wav]=np.frombuffer(subprocess.run(['ffmpeg','-v','error','-i',wav,'-ac','1','-ar','16000','-f','f32le','-'],capture_output=True).stdout,np.float32)
    return _X[wav]
def snap(t,wav,before=2.0,after=0.1):
    x=_audio(wav);sr=16000;w=int(0.12*sr);h=int(0.02*sr)
    a=max(0,int((t-before)*sr));b=min(len(x)-w,int((t+after)*sr))
    best=None
    for i in range(a,b,h):
        e=float((x[i:i+w]**2).mean())
        if best is None or e<best[0]:best=(e,i)
    return round((best[1]+w/2)/sr,3)
def level(t,wav):
    x=_audio(wav);s=x[max(0,int((t-0.1)*16000)):int((t+0.1)*16000)]
    return round(20*np.log10(np.sqrt((s**2).mean())+1e-9),1)
