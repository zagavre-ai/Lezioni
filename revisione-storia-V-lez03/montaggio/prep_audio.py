import subprocess, numpy as np, json, sys
sys.path.insert(0,'/home/user/w3/build')
SR=48000
def rd(af):
    c=['ffmpeg','-v','error','-i','/home/user/w3/orig/lez3.mp4','-vn','-ac','1','-ar','48000']+(['-af',af] if af else [])+['-f','f32le','-']
    return np.frombuffer(subprocess.run(c,capture_output=True).stdout,np.float32)
def metric(x, a=None, b=None):
    # parlato: finestre con energia sopra soglia; rapporto energia >4 kHz / >100 Hz in dB
    w=8192; hi=0; lo=0
    f=np.fft.rfftfreq(w,1/SR)
    for i in range(0,len(x)-w,w*2):
        s=x[i:i+w]*np.hanning(w)
        if np.sqrt(np.mean(s**2))<0.01: continue
        P=np.abs(np.fft.rfft(s))**2
        hi+=P[f>4000].sum(); lo+=P[f>100].sum()
    return 10*np.log10(hi/lo)
o=rd(None); print('orig',len(o)/SR, metric(o),flush=True)
for name,af in [('hp80','highpass=f=80'),('hp80_nr','highpass=f=80,afftdn=nr=6:nf=-50:tn=0'),('hp80_nr10','highpass=f=80,afftdn=nr=10:nf=-45')]:
    x=rd(af); print(name,metric(x),flush=True)
    if name=='hp80_nr': np.save('/home/user/w3/orig/clean_nr6.npy',x)
