import numpy as np
from PIL import Image
def runs(v,th,minlen):
    r=[];s=None
    for i,x in enumerate(v):
        if x>th and s is None:s=i
        if x<=th and s is not None:
            if i-s>=minlen:r.append((s,i))
            s=None
    if s is not None and len(v)-s>=minlen:r.append((s,len(v)))
    return r
def photo_blocks(path,th=0.5,minlen=40):
    im=Image.open(path).convert('RGB');a=np.array(im);m=(a.min(axis=2)<238)
    cols=runs(m.mean(axis=0),th,minlen); out=[]
    for c0,c1 in cols:
        rows=runs(m[:,c0:c1].mean(axis=1),th,minlen)
        for r0,r1 in rows: out.append((c0,r0,c1,r1))
    return out
if __name__=='__main__':
    import sys
    for n in ['001','008','009','012','015','017','018','021','025','026','027','030','033']:
        p=f'/tmp/w/l6s/img/i-{n}.jpg'; print(n,Image.open(p).size,photo_blocks(p))
