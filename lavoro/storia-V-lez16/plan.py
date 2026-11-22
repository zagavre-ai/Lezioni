from engine import *
from lessondata import *
def T(i):return S[i]['inizio']
# viste: ('c',t,finestra,acceso)  oppure ('i',t,chiave_immagine)
CH=[
 dict(nome='D0',arg=0,s0=0,s1=23,views=[]),
 dict(nome='D1',arg=1,s0=24,s1=26,views=[('c',0,[0,1,2],None),('c',T(24),[0,1,2],0),('c',T(25),[0,1,2],1),('c',T(26),[2,3,4],None)]),
 dict(nome='D2a',arg=2,s0=27,s1=83,views=[('c',0,[0,1,2],None),('c',T(40),[0,1,2],0),('c',T(43),[0,1,2],1),
    ('c',T(53),[1,2],1),('c',T(59),[1,2],2),('c',T(67),[1,2,3],1)]),
 dict(nome='D2b',arg=2,s0=84,s1=115,views=[('c',0,[2,3],3),('i',T(107),'kennedy')]),
 dict(nome='D3a',arg=3,s0=116,s1=147,views=[('c',0,[0,1],None),('c',T(133),[0,1],0),('c',T(143),[1,2],1)]),
 dict(nome='D3b',arg=3,s0=148,s1=177,views=[('c',0,[0,1,2],0),('c',tw("L'estensione dei diritti politici"),[1,2],1),('c',tw("innesca al contempo"),[1,2],2)] ),
 dict(nome='D4',arg=4,s0=178,s1=241,views=[('c',0,[0,1],None),('c',T(185),[0,1],0),('c',T(198),[1,2],1),('c',T(203),[1,2],2),('c',T(213),[0,1,2],2)]),
 dict(nome='D5a',arg=5,s0=242,s1=277,views=[('c',0,[0,1],None),('c',T(244),[0,1],0),('c',T(257),[1,2],None)]),
 dict(nome='D5b',arg=5,s0=278,s1=312,views=[('c',0,[0,1,2],None),('c',T(278),[0,1,2],0),('c',T(282),[0,1,2],1),('i',T(290),'vietnam'),('c',T(302),[1,2],2)]),
 dict(nome='D6',arg=6,s0=313,s1=329,views=[('c',0,[0,1,2],None),('c',T(314),[0,1,2],0),('c',T(316),[0,1,2],1),('c',T(318),[0,1,2],2),('i',T(324),'praga'),('i',T(325),'seigiorni')]),
 dict(nome='D7',arg=7,s0=330,s1=360,views=[('c',0,[0,1,2],None),('c',T(331),[0,1,2],0),('c',T(334),[0,1,2],2),('c',T(337),[0,1,2],1),('c',T(341),[0,1,2],0),('c',T(344),[1,2,3],None),('c',T(347),[1,2,3],3)]),
]
IMG={'kennedy':dict(f='p4_1_x4.png',tit="Il presidente Kennedy tiene un discorso all'American University, il 10 giugno 1963"),
     'vietnam':dict(f='p8_1_x4.png',tit="La guerra nel Vietnam (1966-1975)"),
     'praga':dict(f='p10_0_x4.png',tit="I carrarmati sovietici a Praga nel 1968"),
     'seigiorni':dict(f='p11_1_x4.png',tit="La guerra dei Sei giorni (1967)")}
