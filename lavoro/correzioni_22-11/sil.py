import numpy as np, wave, json
def frames_rms(f,hop=0.02):
    w=wave.open(f);sr=w.getframerate();a=np.frombuffer(w.readframes(w.getnframes()),dtype=np.int16).astype(np.float32)/32768
    n=int(sr*hop);m=len(a)//n;x=a[:m*n].reshape(m,n);return 20*np.log10(np.sqrt((x**2).mean(1))+1e-9),hop
def silent_runs(f,mind=2.0,off=8.0):
    r,hop=frames_rms(f);fl=np.percentile(r,8);th=fl+off
    sil=r<th;runs=[];i=0
    while i<len(sil):
        if sil[i]:
            j=i
            while j<len(sil) and sil[j]:j+=1
            if (j-i)*hop>=mind:runs.append((i*hop,j*hop))
            i=j
        else:i+=1
    return runs,fl,th
if __name__=='__main__':
    runs,fl,th=silent_runs('/home/work/an/prof_clean.wav',2.0)
    print('floor',round(fl,1),'th',round(th,1),len(runs));print([(round(a,1),round(b-a,1)) for a,b in runs][:40])
