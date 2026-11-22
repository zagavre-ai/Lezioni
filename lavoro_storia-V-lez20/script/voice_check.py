import sys,json,re,unicodedata,difflib,wave,numpy as np,os
sys.path.insert(0,'/tmp/w/b')
from voicelib import *
def norm(s):return re.sub(r'[^a-z0-9 ]',' ',unicodedata.normalize('NFD',s.lower()).encode('ascii','ignore').decode()).split()
names=sys.argv[1:] or sorted(VT)
rows=[];bad=0
for k in names:
    if k not in TV or k not in VT: continue
    a=norm(digits(TV[k]));b=norm(digits(VT[k]['testo']))
    r=difflib.SequenceMatcher(None,a,b).ratio()
    with wave.open(f'/tmp/w/vox/{k}.wav') as w:
        n=w.getnframes();sr=w.getframerate();x=np.frombuffer(w.readframes(n),np.int16).astype(float)/32768
        x=x.reshape(-1,w.getnchannels())[:,0]
    edge=float(np.abs(x[-int(0.05*sr):]).max());edge0=float(np.abs(x[:int(0.05*sr)]).max())
    ok=(r>=0.90) and edge<0.03
    if not ok: bad+=1
    diff=[ (t,w_) for t,w_ in [(x1,y1) for x1,y1 in []]]
    sm=difflib.SequenceMatcher(None,a,b);d=[(' '.join(a[i1:i2]),' '.join(b[j1:j2])) for tag,i1,i2,j1,j2 in sm.get_opcodes() if tag!='equal'][:4]
    rows.append((k,round(r,2),round(edge,3),round(edge0,3),'OK' if ok else 'VERIFICARE',d))
for r in rows: print(r)
print('da verificare:',bad,'su',len(rows))
