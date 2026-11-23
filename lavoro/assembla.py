# Assemblaggio di una Parte: pezzi + transizioni (trans.wav + dissolvenza 0,6 s) -> lista concat -> timeline
import sys, os, json, subprocess
sys.path.insert(0,'/home/user/Lezioni/lavoro')
import mont
from mont import sh, B, dur
K=f'{B}/k';TR=f'{B}/tr';os.makedirs(TR,exist_ok=True)
TRANS='/home/user/Lezioni/kit/suoni/trans.wav'
def path(n):
    if n in ('D0','DI') or (n.startswith('A') and n[1:].isdigit()): return f'{B}/{n}.mkv'
    return f'{K}/{n}.mkv'
def tname(n):   # nome nella timeline
    if n=='DI': return 'D0B'
    if n.startswith('A') and n[1:].isdigit(): return 'D'+n[1:]
    return n
SEQ={1:['SIGLA','COVERV1','D0','DI']+sum([[f'T{n}',f'A{n}',f'AP{n}']+(['MAP1'] if n==4 else [])+[f'PI{n}',f'PS{n}',f'Q{n}'] for n in (1,2,3,4)],[])+['GL1','RIEP1','FIN1','FINALE'],
     2:['SIGLA','COVERV2','SPG2']+sum([[f'T{n}',f'A{n}',f'AP{n}']+(['MAP2'] if n==5 else ['MAP3'] if n==7 else [])+[f'PI{n}',f'PS{n}',f'Q{n}'] for n in (5,6,7,8)],[])+['GL2','RIEP2','FIN2','VER','FINALE','CINTRO','COMPITI']}
def frame(src,out,last):
    if os.path.exists(out) and os.path.getmtime(out)>os.path.getmtime(src): return out
    if last: sh(['ffmpeg','-v','error','-y','-sseof','-0.12','-i',src,'-frames:v','1','-update','1',out])
    else: sh(['ffmpeg','-v','error','-y','-i',src,'-frames:v','1',out])
    return out
def transizione(a,b):
    out=f'{TR}/{a}__{b}.mkv'
    pa,pb=path(a),path(b)
    if os.path.exists(out) and os.path.getmtime(out)>max(os.path.getmtime(pa),os.path.getmtime(pb)): return out
    fa=frame(pa,f'{TR}/{a}_last.png',True);fb=frame(pb,f'{TR}/{b}_first.png',False)
    sh(['ffmpeg','-v','error','-y','-loop','1','-framerate','30','-t','0.9','-i',fa,'-loop','1','-framerate','30','-t','0.9','-i',fb,'-i',TRANS,
        '-filter_complex',"[0:v][1:v]xfade=transition=fade:duration=0.6:offset=0,format=yuv420p,trim=0:0.6,setpts=PTS-STARTPTS[v];[2:a]aresample=48000,aformat=channel_layouts=mono,atrim=0:0.6,afade=t=out:st=0.4:d=0.2[a]",
        '-map','[v]','-map','[a]','-frames:v','18','-r','30','-c:v','libx264','-preset','veryfast','-crf','14','-pix_fmt','yuv420p','-c:a','pcm_s16le','-ar','48000',out]);return out
FIX=f'{B}/fix';os.makedirs(FIX,exist_ok=True)
def nframes(f):
    return int(sh(['ffprobe','-v','error','-count_packets','-select_streams','v:0','-show_entries','stream=nb_read_packets','-of','csv=p=0',f]).stdout.strip())
def esatto(p):
    """copia del pezzo con l'audio lungo esattamente quanto il video (frame/30)"""
    out=f'{FIX}/'+p.replace('/','_').lstrip('_')
    if os.path.exists(out) and os.path.getmtime(out)>os.path.getmtime(p): return out,nframes(out)/30
    n=nframes(p);D=n/30
    sh(['ffmpeg','-v','error','-y','-i',p,'-c:v','copy','-af',f'apad=whole_dur={D:.6f},atrim=0:{D:.6f}','-c:a','pcm_s16le','-ar','48000',out]);return out,D
def assembla(parte):
    seq=SEQ[parte];lista=[];tl=[];t=0.0
    for i,n in enumerate(seq):
        if i>0:
            tr,dtr=esatto(transizione(seq[i-1],n));lista.append(tr);t+=dtr
        p,d=esatto(path(n));lista.append(p);tl.append([tname(n),round(t,3),round(d,3)]);t+=d
    open(f'{B}/lista_P{parte}.txt','w').write(''.join(f"file '{p}'\n" for p in lista))
    json.dump(tl,open(f'{B}/timeline_Parte{parte}.json','w'))
    return t,tl
if __name__=='__main__':
    for p in (int(x) for x in sys.argv[1:] or (1,2)):
        t,tl=assembla(p);print('Parte',p,f'{t/60:.1f} min',len(tl),'pezzi')
