import subprocess, numpy as np, sys
def pulisci(src, out_wav):
    # pulizia leggera: filtro dei bassi 70 Hz, riduzione leggera del rumore, 48 kHz mono. Il volume si regola dopo.
    subprocess.run(['ffmpeg','-v','error','-y','-i',src,'-vn','-ac','1','-ar','48000','-af','highpass=f=70,afftdn=nr=8:nf=-45:tn=0','-c:a','pcm_s16le',out_wav],check=True)
def leggi(wav):
    a=subprocess.run(['ffmpeg','-v','error','-i',wav,'-f','f32le','-ac','1','-ar','48000','-'],capture_output=True,check=True).stdout
    return np.frombuffer(a,np.float32)
def timbro(x, sr=48000):
    # acuti sopra i 4 kHz meno volume sopra i 100 Hz, in dB, sul parlato (finestre sopra la soglia)
    n=2048; w=np.hanning(n); hi=lo=0.0; k=0
    f=np.fft.rfftfreq(n,1/sr)
    E=[]
    for i in range(0,len(x)-n,n):
        fr=x[i:i+n]
        if np.sqrt(np.mean(fr**2))<0.01: continue
        s=np.abs(np.fft.rfft(fr*w))**2
        E.append(s)
    S=np.mean(E,axis=0)
    return 10*np.log10(S[f>4000].sum()/S[f>100].sum())
def lufs(wav):
    r=subprocess.run(['ffmpeg','-v','info','-i',wav,'-af','ebur128=peak=true','-f','null','-'],capture_output=True,text=True).stderr
    i=r.rfind('I:'); return r[i:i+40].split('\n')[0], r
if __name__=='__main__':
    x=leggi(sys.argv[1]); print('timbro dB',round(timbro(x),1), 'durata',len(x)/48000)
