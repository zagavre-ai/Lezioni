import sys,json,subprocess,re,glob,hashlib,os,numpy as np
sys.path.insert(0,'/tmp/w/b')
def timbro_wav(f):
    import wave
    with wave.open(f) as w:
        x=np.frombuffer(w.readframes(w.getnframes()),np.int16).reshape(-1,2).astype(float)[:,0]/32768
    n=48000;hi=al=0
    for i in range(0,len(x)-n,n):
        w_=x[i:i+n]
        if np.sqrt((w_**2).mean())<0.01: continue
        S=np.abs(np.fft.rfft(w_*np.hanning(n)))**2;fr=np.fft.rfftfreq(n,1/48000)
        hi+=S[fr>4000].sum();al+=S[fr>100].sum()
    return 10*np.log10(hi/al)
out={}
for part in (1,2):
    fs=[f for f in sorted(glob.glob(f'/tmp/w/b/pp{part}/*.wav')) if re.search(r'_(D\d|A\d)',f)]
    out[part]=[(os.path.basename(f)[4:-8],round(timbro_wav(f),1)) for f in fs]
print(json.dumps(out))
json.dump(out,open('/tmp/w/b/timbro_pezzi.json','w'))
