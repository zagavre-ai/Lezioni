# Controllo delle voci Kore ricevute: durata, bordi (ultimi/primi 50 ms sotto 0,03), trascrizione confrontata parola per parola
import sys, json, difflib, os
sys.path.insert(0,'/tmp/w/build')
import numpy as np, timing, core
V=json.load(open('/tmp/w/voci/testi_voci.json')); rows=[]
for v in V:
    n=v['nome']; p=f'/tmp/w/vox/{n}.wav'
    if not os.path.exists(p): rows.append((n,'MANCA')); continue
    x=core.load_audio(p); d=len(x)/48000
    e_end=float(np.abs(x[-int(0.05*48000):]).max()); e_ini=float(np.abs(x[:int(0.05*48000)]).max())
    W=timing.wav_words(n,v['testo']); got=[timing.norm(w) for t,w in W]; exp=[timing.norm(w) for w in timing.words_of(v['testo'])]
    sm=difflib.SequenceMatcher(None,exp,got,autojunk=False); r=sm.ratio()
    diff=[(' '.join(exp[i1:i2]),' '.join(got[j1:j2])) for op,i1,i2,j1,j2 in sm.get_opcodes() if op!='equal']
    rows.append((n,round(d,1),'bordo fine %.3f ini %.3f'%(e_end,e_ini),'OK bordi' if e_end<0.03 and e_ini<0.03 else 'BORDO>0,03','corrispondenza %.3f'%r,diff[:8]))
for r in rows: print(r)
