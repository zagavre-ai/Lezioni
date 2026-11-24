import sys,time;sys.path.insert(0,'.')
from dark import *
r=R()
t0=time.time()
pillola_scene(r,1,"Gli USA dopo l'11 settembre",'PI1',['SC1_1','SC1_2','SC1_3','SC1_4'],f'{W}/t/pill1.mkv',png=f'{W}/fr/d_pill.png');print('pill',time.time()-t0,flush=True)
Q=json.load(open('/home/user/Lezioni/scambio/storia-V-lez21/quiz.json'))
t0=time.time()
quiz_scene(r,'Quiz 1 · Gli USA dopo l\'11 settembre',Q['Q1']['title'],Q['Q1']['items'][:2],f'{W}/t/quiz1.mkv','Per continuare servono almeno 4 risposte giuste su 5.',png=f'{W}/fr/d_quiz.png');print('quiz',time.time()-t0,flush=True)
r.close()
