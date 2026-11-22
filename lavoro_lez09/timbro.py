import sys,subprocess,numpy as np
def timbro(path,ss=None,t=None,ar=48000):
    cmd=['ffmpeg','-v','error']+(['-ss',str(ss)] if ss is not None else [])+(['-t',str(t)] if t else [])+['-i',path,'-vn','-ac','1','-ar',str(ar),'-f','f32le','-']
    x=np.frombuffer(subprocess.run(cmd,capture_output=True).stdout,np.float32)
    w=8192;acc=np.zeros(w//2+1);n=0
    for i in range(0,len(x)-w,w):
        s=x[i:i+w]*np.hanning(w)
        if np.sqrt(np.mean(s**2))<0.01: continue
        acc+=np.abs(np.fft.rfft(s))**2;n+=1
    f=np.fft.rfftfreq(w,1/ar)
    hi=acc[f>4000].sum();lo=acc[f>100].sum()
    return 10*np.log10(hi/lo),n
if __name__=='__main__':
    print(timbro(sys.argv[1],*(float(a) for a in sys.argv[2:4])))
