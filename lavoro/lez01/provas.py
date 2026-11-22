import sys,time;sys.path.insert(0,'/home/user/Lezioni/lavoro/lez01')
from pieces import *
pagine={(a,i):10+i for a in piano.SLIDE for i in range(len(piano.SLIDE[a]))}
t=time.time()
v,a,D=prof_piece('prova_A2',2,1041.06,1100.0,1.0,pagine,"L'architettura: Piranesi e i visionari francesi")
print(v,a,D,time.time()-t)
