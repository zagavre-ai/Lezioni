# timbro = livello (dB) dell'energia sopra 4 kHz meno quello sopra 100 Hz, sul parlato (frame sopra soglia)
import sys,wave,numpy as np
def timbro(path,t0=None,t1=None):
    w=wave.open(path);sr=w.getframerate();ch=w.getnchannels();n=w.getnframes()
    a=np.frombuffer(w.readframes(n),dtype=np.int16).astype(np.float32)/32768
    if ch>1:a=a.reshape(-1,ch).mean(1)
    if t0 is not None:a=a[int(t0*sr):int((t1 or len(a)/sr)*sr)]
    N=4096;hop=2048;win=np.hanning(N);f=np.fft.rfftfreq(N,1/sr)
    hi=[];lo=[];rms=[]
    for i in range(0,len(a)-N,hop):
        x=a[i:i+N]*win;S=np.abs(np.fft.rfft(x))**2
        rms.append(S.sum())
        hi.append(S[f>=4000].sum());lo.append(S[f>=100].sum())
    rms=np.array(rms);hi=np.array(hi);lo=np.array(lo)
    thr=np.percentile(rms,50)           # solo la metà più forte: parlato
    m=rms>=thr
    return 10*np.log10(hi[m].sum()/lo[m].sum())
if __name__=='__main__':
    print(round(timbro(sys.argv[1],*(float(x) for x in sys.argv[2:4])),2),'dB')
