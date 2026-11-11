# Compone GLc e RFc (parti già registrate in Kore + parti nuove, se arrivate; altrimenti silenzio segnaposto)
import json,os,numpy as np,soundfile as sf
D='/home/claude/lezioni/psicologia-I-II-lez01/voci/';W=D+'wav/';SR=24000
M=json.load(open(W+'meta_S1.json'));NU=json.load(open(D+'../testi_voci_NUOVI.json'))
def rd(n):
    y,sr=sf.read(W+n+'.wav');assert sr==SR;return y.astype(np.float32)
def new(n):
    """parte nuova: voce reale se importata, altrimenti silenzio della durata stimata"""
    if os.path.exists(W+n+'.wav') and n in M and not os.path.exists(W+n+'.PLACEHOLDER'):
        return rd(n),M[n]['phrases'],M[n]['text'],True
    tx=NU[n];ph=[];t=0.0
    for p in tx:ph.append(round(t,2));t+=len(p)/14.8+0.45
    return np.zeros(int(t*SR),np.float32),ph,tx,False
def build(name,base,keep,extra):
    y=rd(base);m=M[base];cut=m['phrases'][keep]
    y=y[:int(cut*SR)].copy();n=len(y)
    f=int(0.03*SR);y[-f:]*=np.linspace(1,0,f)
    gap=np.zeros(int(0.5*SR),np.float32)
    y2,ph2,tx2,real=new(extra)
    out=np.concatenate([y,gap,y2]);off=(len(y)+len(gap))/SR
    ph=m['phrases'][:keep]+[round(off+p,2) for p in ph2]
    tx=m['text'][:keep]+tx2
    sf.write(W+name+'.wav',out,SR)
    M[name]={'dur':round(len(out)/SR,2),'phrases':ph,'text':tx,'placeholder':not real}
    print(name,M[name]['dur'],len(ph),'frasi','reale' if real else 'SEGNAPOSTO per '+extra)
build('GLc','GL1',6,'GL2')
build('RFc','RF1',5,'RF2')
json.dump(M,open(W+'meta_S1.json','w'),ensure_ascii=False,indent=1)
