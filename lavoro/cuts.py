import numpy as np, sys
sys.path.insert(0,'/home/user/Lezioni/lavoro')
from trasc_util import W, mmss
X=np.fromfile('/tmp/w/src16.f32',dtype=np.float32);SR=16000
fr=SR//100;n=len(X)//fr
RMS=np.sqrt((X[:n*fr].reshape(n,fr)**2).mean(1))   # 10 ms
THR=float(np.percentile(RMS,12))*2.2+1e-5
FPS=30
def g(t): return round(t*FPS)/FPS
def sil_run(t0,t1):
    """(inizio,fine) del tratto più lungo sotto soglia in [t0,t1], in secondi"""
    a=int(max(0,t0)*100);b=int(t1*100);best=None;cur=None
    for i in range(a,min(b,n)):
        if RMS[i]<THR:
            if cur is None:cur=i
        else:
            if cur is not None and (best is None or i-cur>best[1]-best[0]):best=(cur,i)
            cur=None
    if cur is not None and (best is None or min(b,n)-cur>best[1]-best[0]):best=(cur,min(b,n))
    return (best[0]/100,best[1]/100) if best else None
def word_before(t):
    """ultima parola con inizio < t"""
    k=None
    for w in W:
        if w[0]<t:k=w
        else:break
    return k
def sentence_start(rx_time):
    """tempo d'inizio della prima parola con inizio >= rx_time-0.05"""
    for w in W:
        if w[0]>=rx_time-0.05:return w[0]
def runs(t0,t1,minlen=0.12):
    a=int(t0*100);b=int(t1*100);out=[];cur=None
    for i in range(max(0,a),min(b,n)):
        if RMS[i]<THR:
            if cur is None:cur=i
        else:
            if cur is not None and i-cur>=minlen*100: out.append((cur/100,i/100))
            cur=None
    return out
def onset(t,raggio=1.2):
    """inizio reale del parlato (fine della pausa) più vicino al tempo t della trascrizione"""
    r=runs(t-raggio,t+raggio)
    if not r:return t,None
    p=min(r,key=lambda x:abs(x[1]-t));return p[1],p
def taglio(tB):
    """tB = inizio (approssimato) della frase che segue. Ritorna (fine_pezzo_precedente, inizio_pezzo_successivo, ok)"""
    o,p=onset(tB)
    if p is None or p[1]-p[0]<0.12:
        return g(tB-0.2),g(tB-0.2),False
    s0,s1=p
    fine=g(min(s0+0.3,(s0+s1)/2));ini=g(max(fine,s1-0.15))
    return fine,ini,True
def comprimi(t0,t1,max_pausa=2.5,tieni=1.0):
    """ranges sorgente (s0,s1) del pezzo con le pause > max_pausa accorciate a ~tieni"""
    out=[];cur=t0;a=int(t0*100);b=int(t1*100);i=a
    while i<b:
        if RMS[i]<THR:
            j=i
            while j<b and RMS[j]<THR:j+=1
            L=(j-i)/100
            if L>max_pausa:
                s=g(i/100+tieni/2);e=g(j/100-tieni/2)
                if e>s and s>cur:
                    out.append((cur,s));cur=e
            i=j
        else:i+=1
    out.append((cur,t1));return [(g(x),g(y)) for x,y in out if y-x>1/FPS]
if __name__=='__main__':
    print('THR',THR)
    for t in (239.88,1039.13,1676.09,2462.37,3169.78,3784.93,4550.69,5355.72):
        print(mmss(t),taglio(t))
