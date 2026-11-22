import subprocess,numpy as np,sys
def spett(path,ss=0,t=60):
    r=subprocess.run(['ffmpeg','-v','error','-ss',str(ss),'-t',str(t),'-i',path,'-vn','-f','f32le','-ac','1','-ar','16000','-'],capture_output=True).stdout
    x=np.frombuffer(r,dtype=np.float32)
    n=len(x)//2048
    X=np.abs(np.fft.rfft(x[:n*2048].reshape(n,2048)*np.hanning(2048),axis=1))**2
    f=np.fft.rfftfreq(2048,1/16000)
    # solo frame con parlato (energia sopra la mediana)
    e=X.sum(axis=1);X=X[e>np.median(e)]
    P=X.sum(axis=0)
    hi=P[f>4000].sum();lo=P[f>100].sum()
    return 10*np.log10(hi/lo)
if __name__=='__main__':
    print(round(spett(sys.argv[1],float(sys.argv[2]),float(sys.argv[3])),2))
