import sys,json,difflib,glob,os,subprocess,numpy as np
sys.path.insert(0,'/tmp/w/b')
from lib import norm
TXT={x['nome']:x['testo'] for x in json.load(open('/tmp/w/voci/scambio/storia-V-lez02/testi_voci.json'))}
TXT.update({x['nome']:x['testo'] for x in json.load(open('/tmp/w/wv/scambio/storia-V-lez02/testi_voci.json'))})
V='/tmp/w/voci/scambio/storia-V-lez02/vox/'
out={}
for n in sorted(TXT):
    p=f'/tmp/w/trvox/{n}.json'
    if not os.path.exists(p) or not os.path.exists(V+n+'.wav'): continue
    a=norm(json.load(open(p))['testo']);b=norm(TXT[n])
    sm=difflib.SequenceMatcher(None,b,a,autojunk=False)
    diff=[(' '.join(b[i1:i2]),' '.join(a[j1:j2])) for t,i1,i2,j1,j2 in sm.get_opcodes() if t!='equal']
    x=np.frombuffer(subprocess.run(['ffmpeg','-v','error','-i',V+n+'.wav','-ac','1','-ar','48000','-f','s16le','-'],capture_output=True).stdout,np.int16)/32768
    edge=float(np.abs(x[-2400:]).max()) if len(x) else 1
    out[n]=dict(ratio=round(sm.ratio(),3),diff=diff,edge=round(edge,4),dur=round(len(x)/48000,1))
json.dump(out,open('/tmp/w/verifica_voci.json','w'),ensure_ascii=False,indent=1)
for n,v in out.items():
    bad=[d for d in v['diff'] if not (len(d[0])<4 and len(d[1])<4)]
    print(n,v['ratio'],v['edge'],v['dur'],bad[:4])
