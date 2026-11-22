import sys,os,json; sys.path.insert(0,'/home/user/lav/eng')
import prof_arg as P
P.BOLD=['vasi liberiani','corteccia','legno','cambio','floema','xilema','sostanze pectiche','macerazione','fusto']
src='lez05/Lezione 5 - Fibre vegetali.mp4'; wav='lez05/orig48.wav'; tr='lez05/trasc.json'
subs=[(34,'Le fibre dei vasi liberiani',['fibre vegetali','vasi liberiani','fusto']),(65,'La struttura del fusto',['corteccia','legno','cambio','floema','xilema']),(125.9,'Separare la fibra: la macerazione',['macerazione','sostanze pectiche'])]
anims=[(66,104.8,'fusto',dict(so=[67,89.9,75.6,71])),(126,150.8,'macerazione',dict(so=[126,139.3,148]))]
res=P.costruisci(dict(t0=34.0,t1=151.0),subs,anims,tr,wav,src,'lez05/out_a1',tag='a1')
print(res['D'],len(res['cards']),'card',len(res['dati']['slides']),'slide')
for s in res['dati']['slides']: print(round(s['t0'],1),round(s['t1'],1),s['title'],[round(c['t0'],1) for c in s['cards']])
print(P.rendi(res,src,wav,'lez05/out_a1',tag='a1'))
P.composita('lez05/out_a1','a1')
