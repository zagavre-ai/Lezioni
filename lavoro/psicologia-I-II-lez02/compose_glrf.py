# Compone glossario e ripasso finale con frasi GIA' generate (Kore): nessuna voce nuova
import json,numpy as np,soundfile as sf
D='/home/claude/lezioni/psicologia-I-II-lez02/voci/';W=D+'wav/';M=json.load(open(W+'meta_S1.json'));SR=24000
def seg(name,i):
    y,sr=sf.read(W+name+'.wav');assert sr==SR
    P=M[name]['phrases'];a=int(P[i]*SR);b=int(P[i+1]*SR) if i+1<len(P) else len(y)
    s=y[a:b].copy()
    # ritaglia il silenzio in coda e metti dissolvenze brevi
    e=np.abs(s)>0.01;n=len(s)-int(np.argmax(e[::-1]))+int(0.12*SR);s=s[:min(len(s),n)]
    f=int(0.015*SR);s[:f]*=np.linspace(0,1,f);s[-f:]*=np.linspace(1,0,f)
    return s,M[name]['text'][i]
def comp(out,items,gap=0.5):
    ys=[];ph=[];tx=[];t=0.0
    for name,i in items:
        s,x=seg(name,i);ph.append(round(t,2));tx.append(x);ys.append(s);ys.append(np.zeros(int(gap*SR)));t+=(len(s)/SR)+gap
    y=np.concatenate(ys[:-1]);y=y/np.abs(y).max()*0.9;sf.write(W+out+'.wav',y,SR)
    M[out]={'dur':round(len(y)/SR,2),'phrases':ph,'text':tx}
comp('GLX',[('GL1',0)]+[('GLL1',6),('GLL1',7),('GLL1',8)]+[('GL1',i) for i in range(1,11)]+[('GL1',11)])
comp('RFX',[('RF1',0),('RFL1',5),('RFL1',6)]+[('RF1',i) for i in range(1,9)])
json.dump(M,open(W+'meta_S1.json','w'),ensure_ascii=False,indent=1)
for k in ('GLX','RFX'):
    print(k,M[k]['dur'],len(M[k]['phrases']));[print('  ',p,t[:90]) for p,t in zip(M[k]['phrases'],M[k]['text'])]
