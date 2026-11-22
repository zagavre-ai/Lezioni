import sys,subprocess,numpy as np
def timbre(f,ss=None,t=None):
    cmd=['ffmpeg','-v','error']+(['-ss',str(ss)] if ss is not None else [])+(['-t',str(t)] if t else [])+['-i',f,'-vn','-ac','1','-ar','48000','-f','f32le','-']
    x=np.frombuffer(subprocess.run(cmd,capture_output=True).stdout,np.float32)
    w=4096;hp=[];lo=[]
    fr=np.fft.rfftfreq(w,1/48000)
    for i in range(0,len(x)-w,w):
        s=x[i:i+w]*np.hanning(w)
        if np.sqrt(np.mean(s**2))<0.01:continue
        P=np.abs(np.fft.rfft(s))**2;hp.append(P[fr>4000].sum());lo.append(P[fr>100].sum())
    return 10*np.log10(np.sum(hp)/np.sum(lo)) if hp else None
if __name__=='__main__':
    print(round(timbre(sys.argv[1]),2))
