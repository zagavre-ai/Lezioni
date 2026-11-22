import sys,numpy as np,subprocess
def timbro(f,ss=None,d=None):
    c=['ffmpeg','-v','error']+(['-ss',str(ss),'-t',str(d)] if ss is not None else [])+['-i',f,'-vn','-ac','1','-ar','16000','-f','f32le','-']
    x=np.frombuffer(subprocess.run(c,capture_output=True).stdout,np.float32)
    w=2048;P=np.zeros(w//2+1);n=0
    for i in range(0,len(x)-w,w):
        s=x[i:i+w]*np.hanning(w)
        if np.sqrt(np.mean(s**2))<0.01:continue   # solo parlato
        P+=np.abs(np.fft.rfft(s))**2;n+=1
    f_=np.fft.rfftfreq(w,1/16000)
    hf=P[(f_>=4000)].sum();lf=P[(f_>=100)].sum()
    return 10*np.log10(hf/lf+1e-12),n
if __name__=='__main__':
    for f in sys.argv[1:]:print(f,'acuti>4k / sopra100Hz: %.1f dB (frame parlato %d)'%timbro(f))
