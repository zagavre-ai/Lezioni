import sys,subprocess,numpy as np
def timbro(f):
    r=subprocess.run(['ffmpeg','-v','error','-i',f,'-vn','-ac','1','-ar','48000','-f','f32le','-'],capture_output=True).stdout
    x=np.frombuffer(r,dtype=np.float32)
    # solo parlato: finestre sopra soglia
    n=48000; acc_hi=0;acc_all=0
    for i in range(0,len(x)-n,n):
        w=x[i:i+n]
        if np.sqrt((w**2).mean())<0.01: continue
        S=np.abs(np.fft.rfft(w*np.hanning(n)))**2
        fr=np.fft.rfftfreq(n,1/48000)
        acc_hi+=S[fr>4000].sum(); acc_all+=S[fr>100].sum()
    return 10*np.log10(acc_hi/acc_all)
if __name__=='__main__':
    for f in sys.argv[1:]:print(f,round(timbro(f),1),'dB')
