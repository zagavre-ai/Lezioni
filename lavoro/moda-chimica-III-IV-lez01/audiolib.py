import subprocess, numpy as np
def pcm(path, ss=None, t=None, af=None, sr=48000):
    c=['ffmpeg','-v','error']
    if ss is not None: c+=['-ss',str(ss)]
    if t is not None: c+=['-t',str(t)]
    c+=['-i',path,'-vn','-ac','1']
    if af: c+=['-af',af]
    c+=['-ar',str(sr),'-f','f32le','-']
    return np.frombuffer(subprocess.run(c,capture_output=True,check=True).stdout,np.float32)
def timbro(x, sr=48000):
    """acuti >4 kHz meno volume >100 Hz, in dB (regola 2.4: tra -9 e -20)"""
    n=1<<int(np.floor(np.log2(len(x))))
    X=np.abs(np.fft.rfft(x[:n]*np.hanning(n)))**2; f=np.fft.rfftfreq(n,1/sr)
    hi=X[f>4000].sum(); al=X[f>100].sum()
    return 10*np.log10(hi/al)
def lufs(path, af=None):
    c=['ffmpeg','-hide_banner','-nostats','-i',path,'-vn']+(['-af',af+',ebur128=peak=true'] if af else ['-af','ebur128=peak=true'])+['-f','null','-']
    r=subprocess.run(c,capture_output=True,text=True).stderr
    i=r.rfind('Integrated loudness'); 
    I=float(r[i:].split('I:')[1].split('LUFS')[0]); p=r.rfind('Peak:'); P=float(r[p:].split('Peak:')[1].split('dBFS')[0])
    return I,P
