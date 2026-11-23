# confronto voci Kore (vox/) con i testi: trascrizione, numeri, bordi. Scrive out/voci_controllo.md
import sys,json,re,os
sys.path.insert(0,'/home/user/work18')
import chk_voci as C
VOX='/home/user/work18/scambio/storia-V-lez18/vox'
T={x['nome']:x['testo'] for x in json.load(open('/home/user/work18/scambio/storia-V-lez18/testi_voci.json'))}
names=set()
for w in '12':
    for t,n in json.load(open(f'/home/user/work18/out/vl_parte{w}.json')):names.add(n)
rows=[];bad=[]
import difflib,numpy as np
for n in sorted(names):
    real=f'{VOX}/{n}_R2.wav' if os.path.exists(f'{VOX}/{n}_R2.wav') else f'{VOX}/{n}.wav'
    if not os.path.exists(real):rows.append((n,'MANCA','','','')); bad.append((n,'manca'));continue
    t,x=C.trans(real);ref=T[n]
    a=C.norm(C.converti(ref));b=C.norm(t);ratio=difflib.SequenceMatcher(None,''.join(a),''.join(b)).ratio()
    edge=float(np.abs(x[-800:]).max());start=float(np.abs(x[:800]).max())
    sm=difflib.SequenceMatcher(None,a,b);diff=[(' '.join(a[i1:i2]),' '.join(b[j1:j2])) for op,i1,i2,j1,j2 in sm.get_opcodes() if op!='equal']
    ok=ratio>=0.93 and edge<0.03
    rows.append((n,'OK' if ok else 'DA GUARDARE','%.3f'%ratio,'%.3f'%edge,str(diff[:4])))
    if not ok:bad.append((n,ratio,edge,diff[:4]))
open('/home/user/work18/out/voci_controllo.md','w').write('| voce | esito | rapporto | ampiezza ultimi 50 ms | differenze |\n|---|---|---|---|---|\n'+'\n'.join('| '+' | '.join(r)+' |' for r in rows))
print(len(rows),'voci;',len(bad),'da guardare');[print(b) for b in bad]
