import numpy as np,subprocess,sys
def rd(f,ss=0,d=None):
    c=['ffmpeg','-v','error','-ss',str(ss)]+(['-t',str(d)] if d else [])+['-i',f,'-ac','1','-ar','48000','-f','f32le','-']
    return np.frombuffer(subprocess.run(c,capture_output=True).stdout,np.float32)
def timbro(x,sr=48000):
    # dB di (energia sopra 4 kHz) meno (energia sopra 100 Hz), sui soli tratti di parlato
    w=8192;a=[];b=[]
    for i in range(0,len(x)-w,w):
        s=x[i:i+w]*np.hanning(w)
        if np.sqrt(np.mean(s**2))<0.01:continue
        S=np.abs(np.fft.rfft(s))**2;f=np.fft.rfftfreq(w,1/sr)
        a.append(S[f>4000].sum());b.append(S[f>100].sum())
    return 10*np.log10(sum(a)/sum(b))
if __name__=='__main__':
    f=sys.argv[1]
    for ss in (300,1200,2400,3600):print(ss,round(timbro(rd(f,ss,60)),1))
