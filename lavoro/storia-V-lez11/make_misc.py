import sys,os
sys.path.insert(0,'/home/user/work/build')
from assemble import *
os.makedirs(CL,exist_ok=True)
kitclip('SIGLA',KIT+'Sigla_Storia_15s.mp4')
kitclip('SIGLA_FIN',KIT+'Sigla_finale_5s_con_avviso_diritti.mp4')
d=dur(vpath('BENV1_R2'))
staticclip('COVER_A',B+'/cover_a.png',0.5+d+1.0,'BENV1_R2',0.5)
for t in range(1,7):
    cardclip(f'TIT{t}',f'T{t}','titolo',None,jg=0.0)
    cardclip(f'PIL{t}',f'P{t}','repaso',f'R{t}',vt=1.0,jg=-3.0)
    cardclip(f'QZ{t}',f'Q{t}','quiz',None,jt=0.5,maxd=4.7)
cardclip('FINALE','FINALE',None,'RIEP1',vt=1.0)
mapclip('MAP1','M1','MP1');mapclip('MAP23','M23','MP23');mapclip('MAP4','M4','MP4')
cardclip('FINE','FINE','finale','FIN1',vt=1.0,jg=-3.0)
cardclip('VERIFICA','VERIFICA','quiz',None,jt=0.5,maxd=4.7)
cardclip('COMP_INTRO','COMPITI','titolo','COMPI',vt=0.9,jg=-3.0)
