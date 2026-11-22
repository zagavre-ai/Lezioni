import sys,subprocess,numpy as np
def load(f,ss=None,t=None):
    c=['ffmpeg','-v','error']+(['-ss',str(ss),'-t',str(t)] if ss is not None else [])+['-i',f,'-vn','-ac','1','-ar','48000','-f','f32le','-']
    return np.frombuffer(subprocess.run(c,capture_output=True).stdout,np.float32)
def timbro(x,sr=48000):
    """dB(energia >4kHz) - dB(energia >100Hz), sui soli frame di parlato (rms alto)"""
    w=4096;hi=[];al=[]
    rms=[np.sqrt(np.mean(x[i:i+w]**2)) for i in range(0,len(x)-w,w)]
    thr=np.percentile(rms,50)
    f=np.fft.rfftfreq(w,1/sr)
    for k,i in enumerate(range(0,len(x)-w,w)):
        if rms[k]<thr: continue
        S=np.abs(np.fft.rfft(x[i:i+w]*np.hanning(w)))**2
        hi.append(S[f>4000].sum());al.append(S[f>100].sum())
    return 10*np.log10(sum(hi)/sum(al))
if __name__=='__main__':
    f=sys.argv[1]
    import os
    for ss in [300,1200,2400,3600,4800,5800]:
        x=load(f,ss,90);print(ss,round(timbro(x),1),'dB')
