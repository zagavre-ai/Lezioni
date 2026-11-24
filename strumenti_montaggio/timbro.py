import sys,subprocess,numpy as np
def rd(f,ss=None,d=None):
    c=['ffmpeg','-v','error']+(['-ss',str(ss),'-t',str(d)] if ss is not None else [])+['-i',f,'-vn','-ac','1','-ar','48000','-f','f32le','-']
    return np.frombuffer(subprocess.run(c,capture_output=True).stdout,np.float32)
def rapporto(x,sr=48000):
    # solo parlato: finestre con energia sopra soglia
    w=8192;P=None;n=0
    hi=0;lo=0
    for i in range(0,len(x)-w,w):
        s=x[i:i+w]*np.hanning(w)
        if np.sqrt(np.mean(s**2))<0.01: continue
        S=np.abs(np.fft.rfft(s))**2;f=np.fft.rfftfreq(w,1/sr)
        hi+=S[f>4000].sum();lo+=S[f>100].sum()
    return 10*np.log10(hi/lo) if lo>0 else None
if __name__=='__main__':
    for f in sys.argv[1:]:
        x=rd(f);print(f,'acuti>4kHz / >100Hz = %.1f dB'%rapporto(x))
