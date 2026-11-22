import sys;sys.path.insert(0,'/home/user/Lezioni/lez14')
from montaggio import *
import spec,shutil,json
b=[confine(spec.ARG[k][1])[0] for k in sorted(spec.ARG)]+[4310.0]
if __name__=='__main__':
    for n in [int(x) for x in sys.argv[1:]] or range(1,8):
        out=f'/tmp/w/pezzi/D{n}.mkv'
        if os.path.exists(out+'.ok'):continue
        info=costruisci_D(n,b[n-1],b[n]);componi_D(info,out)
        json.dump({'durata_s':info['tot'],'orig':[b[n-1],b[n]],'K':info['K']},open(f'/tmp/w/pezzi/D{n}.json','w'))
        open(out+'.ok','w').write('ok');print('D',n,'ok',info['tot'],flush=True)
