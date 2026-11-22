import sys;sys.path.insert(0,'/home/user/Lezioni/lez14')
from montaggio import *
import time
A,_=confine(60);B,_=confine(982)
t=time.time()
# prova ridotta: primi 150 s
info=costruisci_D(1,A,A+150)
print('layer',time.time()-t,info['nf'],len(info['K']))
componi_D(info,WK+'/prova_D1.mkv')
print('ok',time.time()-t)
