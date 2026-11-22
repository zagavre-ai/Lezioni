# Misure sul video finale: sincronia con l'originale (per ogni pezzo del prof), timbro, silenzi lunghi
import sys,json,subprocess,numpy as np;sys.path.insert(0,'/home/user/Lezioni/lavoro_lez03')
from scipy.signal import welch
SR=8000
def pcm(path,ss=None,d=None):
    c=['ffmpeg','-v','error']+(['-ss',f'{ss:.3f}','-t',f'{d:.3f}'] if ss is not None else [])+['-i',path,'-vn','-ac','1','-ar',str(SR),'-f','s16le','-']
    return np.frombuffer(subprocess.run(c,capture_output=True).stdout,np.int16).astype(np.float64)
def env(x,w=80):
    k=np.ones(w)/w;return np.convolve(np.abs(x),k,'same')[::w//8]   # 100 Hz
def sync(final,orig,info):
    """info: {nome:[inizio_finale_s, inizio_sorgente_s]} -> scarto (s) per pezzo, misurato sull'originale"""
    out={}
    for n,(tf,ts) in info.items():
        d=14.0
        a=env(pcm(final,tf+0.2,d));b=env(pcm(orig,ts-1.0+0.2,d+2.0))
        a=a-a.mean();b=b-b.mean();c=np.correlate(b,a,'valid');k=int(np.argmax(c))
        lag=(k/100.0)-1.0       # >0: il finale è in ritardo rispetto alla sorgente
        out[n]=round(lag,3)
    return out
def timbro(path,ss=None,d=None):
    x=pcm(path,ss,d);f,p=welch(x,SR,nperseg=2048)
    hi=p[f>3500].sum();lo=p[f>100].sum()
    return round(10*np.log10(hi/lo),1)
if __name__=='__main__':
    final,orig,infof=sys.argv[1:4];info=json.load(open(infof))
    s=sync(final,orig,info);print('sincronia (s):',s);print('max',max(abs(v) for v in s.values()))
