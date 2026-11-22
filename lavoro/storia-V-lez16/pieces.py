import json,subprocess,os,hashlib
from engine import *
from gfx import *
from lessondata import *
from plan import CH,IMG
OUT=W+'/pieces';os.makedirs(OUT,exist_ok=True)
SND='/home/user/Lezioni/kit/suoni/'
JOBS=[];_seen={}
PG={'n':0}
def newpage():PG['n']+=1;return PG['n']
def png(html_text,tag,transparent=False):
    h=hashlib.md5(html_text.encode()).hexdigest()[:12]
    o=f'{B}/png/{tag}_{h}.png'
    if o in _seen:return o
    hp=f'{B}/html/{tag}_{h}.html';open(hp,'w').write(html_text)
    JOBS.append(dict(html=hp,out=o,skip_if_exists=True,transparent=transparent));_seen[o]=1
    return o
def flush():
    global JOBS
    if not JOBS:return
    json.dump(JOBS,open(B+'/jobs.json','w'));r=subprocess.run(['node',B+'/render.js',B+'/jobs.json'],capture_output=True,text=True,cwd=B)
    print(r.stdout.strip(),r.stderr[-300:]);JOBS=[]
V_ENC=['-c:v','libx264','-preset','ultrafast','-crf','14','-pix_fmt','yuv420p','-r','30','-g','30']
A_ENC=['-c:a','pcm_s16le','-ar','48000','-ac','2']
def concat_png_list(states,nF,path):
    """states: [(frame_start,png)] -> file lista concat con durate in secondi esatte (frame/30)"""
    L=[]
    for i,(f0,p) in enumerate(states):
        f1=states[i+1][0] if i+1<len(states) else nF
        if f1>f0:L.append((p,(f1-f0)/FPS))
    with open(path,'w') as f:
        for p,d in L:f.write(f"file '{p}'\nduration {d:.6f}\n")
        f.write(f"file '{L[-1][0]}'\n")
def last_frame(piece,out):
    sh(['ffmpeg','-v','error','-y','-sseof','-0.1','-i',piece,'-frames:v','1',out]);return out
def trans_filter(prev_png,out_lbl='vout',in_lbl='vbase',d=0.3):
    return f"[{prev_png}:v]format=rgba,fade=t=out:st=0:d={d}:alpha=1[pv];[{in_lbl}][pv]overlay=0:0:eof_action=pass,format=yuv420p[{out_lbl}]"

def still_inputs(states,nF,fmt='yuv420p'):
    """ingressi -loop per ogni stato + filtro che li concatena in [bg]; ritorna (args, filtro, n_ingressi)"""
    a=[];f=[];lab=''
    for i,(f0,pn) in enumerate(states):
        f1=states[i+1][0] if i+1<len(states) else nF
        n=f1-f0
        if n<=0:continue
        k=len(lab)//0 if False else a.count('-i')
        a+=['-loop','1','-framerate','30','-t',f'{n/FPS:.6f}','-i',pn]
        f.append(f"[{k}:v]setsar=1,format={fmt}[st{k}]");lab+=f"[st{k}]"
    m=a.count('-i')
    f.append(lab+f"concat=n={m}:v=1:a=0,fps=30[bg]")
    return a,';'.join(f),m
