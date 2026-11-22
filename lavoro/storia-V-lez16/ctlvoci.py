import sys,json,re,difflib
sys.path.insert(0,'/home/user/w/build')
from kore import *
from voice import words_of,real,prepare
from numconv import num_words
import numpy as np
def toks(t):
    t=num_words(t);t=re.sub(r'(\d+)\.(\d{3})',r'\1\2',t)
    return [norm(w) for w in re.split(r'\s+',t.replace('-',' ')) if norm(w)]
def check(name,text):
    p=real(name)
    if not p:return None
    o,d,prov=prepare(name,text)
    x=np.frombuffer(subprocess.run(['ffmpeg','-v','error','-i',o,'-ac','1','-ar','48000','-f','f32le','-'],capture_output=True).stdout,np.float32)
    tail=float(np.abs(x[-int(0.05*48000):]).max());head=float(np.abs(x[:int(0.05*48000)]).max())
    ws=[w for t,w in words_of(o)];a=toks(text);b=[norm(w) for w in ws if norm(w)];b=toks(' '.join(ws))
    sm=difflib.SequenceMatcher(None,a,b,autojunk=False);r=sm.ratio()
    diff=[(op,' '.join(a[i1:i2]),' '.join(b[j1:j2])) for op,i1,i2,j1,j2 in sm.get_opcodes() if op!='equal']
    return dict(nome=name,durata=round(d,1),coda=round(tail,4),testa=round(head,4),simile=round(r,3),diff=diff[:8])
if __name__=='__main__':
    names=sys.argv[1:] or sorted(TEXTS)
    res=[]
    for n in names:
        t=TEXTS.get(n)
        if not t:continue
        r=check(n,t)
        if r:res.append(r);print(r['nome'],r['durata'],'coda',r['coda'],'sim',r['simile'],r['diff'][:4],flush=True)
    json.dump(res,open(W+'/out/ctlvoci.json','w'),ensure_ascii=False,indent=1)
