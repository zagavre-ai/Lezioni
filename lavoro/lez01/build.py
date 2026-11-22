#!/usr/bin/env python3
# Montaggio di una Parte: python3 build.py 1|2  [--solo NOME ...]
import os,sys,json,shutil,time
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from asm import *
from asm import _lista
import pieces as P,blue_pieces as B,blu,piano,voci
KIT='/home/user/Lezioni/kit/'
PROF_CUT={ # nome: (arg, a, b, pre)
 'D0':(0,0.45,123.62,0.0),'D1':(1,123.76,1038.6,0.2),'D2':(2,1041.06,1466.95,1.0),'D3':(3,1467.18,2042.5,0.4),
 'D4':(4,2043.22,2842.5,1.0),'D5':(5,2845.6,3859.9,1.0)}
def piano_parte(parte):
    if parte==1:
        seq=['SIG','COVER','D0','ARG']
        for n in (1,2,3):seq+=[f'T{n}',f'D{n}',f'A{n}',f'R{n}',f'Q{n}']
    else:
        seq=['SIG','COVER2','SP']
        for n in (4,5):seq+=[f'T{n}',f'D{n}',f'A{n}',f'R{n}',f'Q{n}']
        seq+=['GL','RF','MF','VER','FIN','CI','COMP']
    return seq
def numera(seq):
    """numero di pagina per ogni pezzo e per ogni slide del docente (pagina = pagina di dispensa)"""
    import render
    pg={};n=0;pagine={}
    for s in seq:
        if s in('SIG','FIN','CI'):continue
        if s=='D0':continue
        if s[0]=='D':
            a=int(s[1])
            for i,sl in enumerate(piano.SLIDE[a]):
                pagine[(a,i)]=n+1;n+=len(render.chunks(sl))
            continue
        n+=1;pg[s]=n
    pg['D0']=1
    return pg,pagine
def titolo_arg(n):return piano.ARGOMENTI[n-1]['titolo']
def make(name,pagine,pg):
    blu.CUR=pg.get(name)
    if name=='SIG':return B.sigla('SIG',KIT+'sigle/Sigla_Storia_arte_15s.mp4')
    if name=='FIN':return B.sigla('FIN',KIT+'sigle/Sigla_finale_5s_con_avviso_diritti.mp4')
    if name=='COVER':return B.cover(1)
    if name=='COVER2':return B.cover(2)
    if name=='ARG':return B.elenco_argomenti()
    if name=='SP':return B.spiegone()
    if name=='GL':return B.glossario()
    if name=='RF':return B.ripasso_finale()
    if name=='MF':return B.mappa_finale()
    if name=='VER':return B.verifica_card()
    if name=='CI':return B.compiti_intro()
    if name=='COMP':return B.compiti()
    if name[0]=='T':return B.titolo_arg(int(name[1]),titolo_arg(int(name[1])))
    if name[0]=='A':return B.approfondimento(int(name[1]))
    if name[0]=='R':return B.pillola(int(name[1]),titolo_arg(int(name[1])))
    if name[0]=='Q':return B.quiz_card(int(name[1]),titolo_arg(int(name[1])))
    if name[0]=='D':
        arg,a,b,pre=PROF_CUT[name]
        return P.prof_piece(name,arg,a,b,pre,pagine,titolo_arg(arg) if arg else '',intro=(name=='D0'))
def main():
    parte=int(sys.argv[1]);solo=sys.argv[sys.argv.index('--solo')+1:] if '--solo' in sys.argv else None
    seq=piano_parte(parte);pg,pagine=numera(seq)
    info={}
    for nm in seq:
        v=CL+nm+'.mp4';a=CL+nm+'.wav'
        if os.path.exists(v) and os.path.exists(a) and not (solo and nm in solo):
            info[nm]=dur_wav(a);continue
        t=time.time();r=make(nm,pagine,pg);info[nm]=r[2];print(nm,round(r[2],2),'s',round(time.time()-t),'s lavoro',flush=True)
    # concatena
    tl=[];t=0
    for nm in seq:
        tl.append([nm,round(t,3),round(info[nm],3)]);t+=info[nm]
    json.dump(tl,open(WK+f'timeline_raw_P{parte}.json','w'),indent=0)
    out=WK+f'Storia_arte_Lez1_Parte{parte}_1080p.mp4'
    concat_final([CL+n+'.mp4' for n in seq],[CL+n+'.wav' for n in seq],out)
    print('FATTO',out,round(t/60,2),'min')
if __name__=='__main__':main()
