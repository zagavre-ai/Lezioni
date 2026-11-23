# controllo delle voci Kore ricevute: durata, bordi (ampiezza negli ultimi/primi 50 ms < 0,03), trascrizione confrontata col testo
import sys,os,json,re,glob,difflib
sys.path.insert(0,'/tmp/claude-0/w/prod')
import numpy as np,asr
from eng import *
T={t['nome']:t['testo'] for t in json.load(open(W+'/testi_voci.json'))}
NUM=re.compile(r'^(uno|due|tre|quattro|cinque|sei|sette|otto|nove|dieci|undici|dodici|tredici|quattordici|quindici|sedici|diciassette|diciotto|diciannove|venti\w*|trenta\w*|quaranta\w*|cinquanta\w*|ottanta|cento|mille\w*|virgola)$')
out={}
for n,txt in T.items():
    p=f'{W}/vox/{n}.wav'
    if not os.path.exists(p):out[n]='MANCA';continue
    x=audio_load(p).mean(1);e=int(0.05*SR)
    edge=(float(np.abs(x[:e]).max()),float(np.abs(x[-e:]).max()))
    h=asr.words(p);json.dump(h,open(p[:-4]+'.words.json','w'),ensure_ascii=False)
    a=[asr.norm(w) for w in txt.split()];b=[asr.norm(w) for _,w in h]
    sm=difflib.SequenceMatcher(None,a,b,autojunk=False);diff=[]
    for op,i1,i2,j1,j2 in sm.get_opcodes():
        if op=='equal':continue
        A=a[i1:i2];Bw=b[j1:j2]
        if all(NUM.match(w) or w=='' for w in A) or any(re.search(r'\d',w) for w in Bw):continue
        diff.append((op,' '.join(A),' '.join(Bw)))
    out[n]=dict(durata=round(len(x)/SR,2),bordo_inizio=round(edge[0],4),bordo_fine=round(edge[1],4),bordi_ok=edge[0]<0.03 and edge[1]<0.03,differenze=diff[:8],n_diff=len(diff))
    print(n,out[n]['durata'],'bordi',edge,'diff',len(diff),diff[:3],flush=True)
json.dump(out,open(W+'/consegna/controllo_voci.json','w'),ensure_ascii=False,indent=1)
