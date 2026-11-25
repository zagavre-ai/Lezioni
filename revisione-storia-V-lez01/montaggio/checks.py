import sys,json,subprocess,numpy as np
ORIG='/tmp/w/orig/video.mp4'
def rd(f,ss,d,sr=16000):
    c=['ffmpeg','-v','error','-ss',str(ss),'-t',str(d),'-i',f,'-vn','-ac','1','-ar',str(sr),'-f','s16le','-']
    return np.frombuffer(subprocess.run(c,capture_output=True).stdout,np.int16).astype(float)
def band(x,sr=16000):
    X=np.abs(np.fft.rfft(x*np.hanning(len(x))))**2;fr=np.fft.rfftfreq(len(x),1/sr)
    hi=X[fr>4000].sum();lo=X[(fr>100)].sum()
    return 10*np.log10(hi/lo+1e-12)
def delay(a,b,sr=16000):
    ea=np.abs(a);eb=np.abs(b)
    k=np.ones(160)/160;ea=np.convolve(ea,k,'same');eb=np.convolve(eb,k,'same')
    ea-=ea.mean();eb-=eb.mean()
    n=len(a);m=int(0.3*sr)
    best=None
    c=np.correlate(eb[m:n-m],ea,'valid') if False else None
    # brute: shifts -0.3..0.3 s step 1 ms
    res=[]
    for s in range(-m,m+1,16):
        if s>=0: u=ea[:n-s];v=eb[s:]
        else: u=ea[-s:];v=eb[:n+s]
        res.append((np.corrcoef(u,v)[0,1],s))
    return max(res)[1]/sr
def run(video,tl,pieces_src):
    """pieces_src: list of (name,start_in_final,a_orig,b_orig)"""
    out=[]
    for name,st,a,b in pieces_src:
        d=b-a
        for frac in (0.15,0.5,0.85):
            t0=a+d*frac;L=20
            xo=rd(ORIG,t0,L);xf=rd(video,st+d*frac,L)
            n=min(len(xo),len(xf));xo=xo[:n];xf=xf[:n]
            out.append((name,round(frac,2),round(band(xo),1),round(band(xf),1),round(delay(xo,xf),3)))
    return out
if __name__=='__main__':
    video=sys.argv[1];tl=json.load(open(sys.argv[2]));src=json.load(open(sys.argv[3]))
    for r in run(video,tl,src): print(r)
