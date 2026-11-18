import sys;sys.path.insert(0,'/tmp/w/tools')
from plan2 import *
def part1():
    plan.PAGE[0]=0
    segs=[seg_sigla()]
    segs[0]['tr']=36
    pc=seg_cover(False);plan.PAGE[0]=1
    ben=dict(id='cover_ben',k='seq',seq=[[pc,fr(round(vdur('BEN')+2.2,1))]],frames=fr(round(vdur('BEN')+2.2,1)),aud=[voice('BEN',0.9)])
    segs.append(ben)
    pp=seg_cover(True)
    # introduzione del prof (0 -> CUT[1]) sulla copertina
    F=fr(CUT[1]);segs.append(dict(id='intro_prof',k='prof',t0=0.0,frames=F,bg=[[0.0,pp,'cut']]))
    for n in range(1,6): segs+=arg_segs(n)
    segs.append(seg_gloss(1,'GL1'));segs.append(seg_final(1,'RF1','FIN1','f1'));segs.append(seg_fine())
    return segs
def arg_segs(n):
    L=[seg_title(n),seg_prof(n)]
    for i in (2*n-1,2*n): L.append(seg_an(n,i))
    if n in MAPS: L.append(seg_map(n))
    L+= [seg_pill(n),seg_schema(n),seg_quiz(n)]
    return L
def part2():
    segs=[seg_sigla()];segs[0]['tr']=36
    segs.append(seg_rip2())
    for n in range(6,12): segs+=arg_segs(n)
    segs.append(seg_gloss(2,'GL2'));segs.append(seg_final(2,'RF2','FIN2','f2'));segs.append(seg_fine())
    return segs
