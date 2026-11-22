import sys,os,json
sys.path.insert(0,'/home/user/work/build')
from L import *
import schede
d=dur(vpath('FIN1'))
sp=dict(type='simple',kicker='Storia V',big='Per oggi è tutto',fs=130,sub='Ora tocca a te: verifica finale e compiti',dur=round(1.0+d+1.5,2))
if not os.path.exists(B+'/cards/FINE.ok'):
    schede.render(sp,B+'/cards/FINE',1.0);open(B+'/cards/FINE.ok','w').write('1');print('FINE',sp['dur'])
