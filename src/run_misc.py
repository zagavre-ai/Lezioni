import sys, os, time
sys.path.insert(0,'/tmp/w/build')
import pieces as P
K='/home/user/Lezioni/kit/sigle/'
jobs=[('SIGLA',lambda:P.build_sigla(K+'Sigla_Storia_arte_15s.mp4','SIGLA')),
 ('SIGLA_FINALE',lambda:P.build_sigla(K+'Sigla_finale_5s_con_avviso_diritti.mp4','SIGLA_FINALE')),
 ('COVER',P.build_cover)]
for i in range(1,6):
    jobs+= [(f'TIT{i}',lambda i=i:P.card_title(i)),(f'QZ{i}',lambda i=i:P.card_quiz(i)),(f'APP{i}',lambda i=i:P.build_approf(i)),(f'RIP{i}',lambda i=i:P.card_pillola(i))]
jobs+=[('GLOSS',P.build_glossario),('RIEPILOGO',P.build_ripasso_finale),('VERIFICA',P.build_verifica),('COMPITI_INTRO',P.build_compiti_intro),('COMPITI',P.build_compiti)]
only=sys.argv[1:] 
for nm,f in jobs:
    if only and nm not in only: continue
    t=time.time(); f(); print(nm,round(time.time()-t),'s',flush=True)
