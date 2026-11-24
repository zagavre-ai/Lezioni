#!/usr/bin/env python3
# Controllo di ogni voce Kore: trascrizione (ASR) confrontata col testo, numeri/date compresi; bordi (ultimi 50 ms < 0,03); nome del docente.
import sys, os, json, re, difflib, subprocess, unicodedata
import numpy as np
sys.path.insert(0,'/home/claude/w/code')
from numeri import digits
W='/home/claude/w';V='/home/user/Lezioni/scambio/storia-V-lez21/vox'
TESTI={x['nome']:x['testo'] for x in json.load(open(f'{W}/testi_voci.json'))}
def norm(s):
    s=digits(s.lower());s=unicodedata.normalize('NFD',s);s=''.join(c for c in s if not unicodedata.combining(c))
    s=re.sub(r"[^a-z0-9 ]",' ',s.replace("'",' '));return s.split()
def edge(p):
    x=np.frombuffer(subprocess.run(['ffmpeg','-v','error','-i',p,'-ac','1','-ar','24000','-f','f32le','-'],capture_output=True).stdout,np.float32)
    n=int(0.05*24000);return float(np.abs(x[-n:]).max()),float(np.abs(x[:n]).max())
def main(names=None):
    res={};bad=[]
    for nome,txt in TESTI.items():
        if names and nome not in names: continue
        p=f'{V}/{nome}.wav'
        if not os.path.exists(p): continue
        a=f'{W}/voci_asr/{nome}.json'
        if not os.path.exists(a): res[nome]='ASR_MANCANTE';continue
        got=norm(json.load(open(a))['text']);exp=norm(txt)
        sm=difflib.SequenceMatcher(None,exp,got);r=sm.ratio()
        diff=[(exp[i1:i2],got[j1:j2]) for t,i1,i2,j1,j2 in sm.get_opcodes() if t!='equal']
        nums_e=[w for w in exp if w.isdigit()];nums_g=[w for w in got if w.isdigit()]
        e_end,e_start=edge(p)
        nome_prof=bool(re.search(r'mazzotti|giorgio',' '.join(got)))
        res[nome]=dict(simile=round(r,3),diff=diff[:6],numeri_ok=(nums_e==nums_g),numeri_attesi=nums_e,numeri_trovati=nums_g,bordo_fine=round(e_end,4),bordo_ini=round(e_start,4),nome_docente=nome_prof)
        if r<0.9 or nums_e!=nums_g or e_end>=0.03 or nome_prof: bad.append(nome)
    json.dump(res,open(f'{W}/check_voci.json','w'),ensure_ascii=False,indent=1)
    print('voci controllate',len(res),'da rivedere',bad)
    for b in bad: print(b,res[b])
if __name__=='__main__': main(sys.argv[1:] or None)
