# conversione pezzi in .mov con audio PCM esatto, liste, timeline, codifica finale a pezzi
import sys,os,json,subprocess
sys.path.insert(0,'/home/user/Lezioni/storia_s7')
from lib import *
W='/tmp/w18/w';PC=W+'/pc'
def frames(f):return int(run(['ffprobe','-v','error','-count_packets','-select_streams','v:0','-show_entries','stream=nb_read_packets','-of','csv=p=0',f]).strip())
def mov(n):
    src=f'{PC}/{n}.mp4';dst=f'{PC}/{n}.mov'
    if os.path.exists(dst+'.ok'):return frames(dst)
    N=frames(src);T=N/FPS
    run(['ffmpeg','-y','-v','error','-i',src,'-map','0:v','-map','0:a','-c:v','copy','-af',f'apad,atrim=0:{T:.6f}','-c:a','pcm_s16le','-ar','48000','-ac','2',dst])
    open(dst+'.ok','w').write('1');return N
ORD1=['SIGLA','INTRO1','D0']
for k in (1,2,3):ORD1+=[f'T{k}',f'D{k}']+[f'AN{k}{x}' for x in 'abc']+[f'MAP{k}',f'R{k}',f'Q{k}']
ORD1+=['MAPF1','GL1','RF1','FIN1','VER','SFIN','CINTRO','COMP']
ORD2=['SIGLA','INTRO2']
for k in (4,5,6):ORD2+=[f'T{k}',f'D{k}']+[f'AN{k}{x}' for x in 'abc']+[f'MAP{k}',f'R{k}',f'Q{k}']
ORD2+=['MAPF2','GL2','RF2','FIN2','VER','SFIN','CINTRO','COMP']
if __name__=='__main__':
    sel=int(sys.argv[1])
    for parte,ORD in (((1,ORD1),(2,ORD2))[sel-1],):
        t=0.0;TL=[];lst=''
        for n in ORD:
            N=mov(n);d=N/FPS;TL.append([n,round(t,3),round(d,3)]);t+=d;lst+=f"file '{PC}/{n}.mov'\n"
        os.makedirs('/tmp/w18/out',exist_ok=True)
        open(f'/tmp/w18/lista_p{parte}.txt','w').write(lst)
        json.dump(TL,open(f'/tmp/w18/out/timeline_Parte{parte}.json','w'))
        print('parte',parte,'durata',round(t,2),'=',int(t//60),'min',round(t%60,1),'s');
