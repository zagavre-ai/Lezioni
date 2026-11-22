# Assemblaggio delle Parti: pezzi + dissolvenze (trans.wav) + timeline
import sys,json,os,subprocess;sys.path.insert(0,'/home/user/Lezioni/lavoro_lez03')
from piano import *
TR=M.OUT+'/trans08.wav'
if not os.path.exists(TR):M.sh(['ffmpeg','-v','error','-y','-i',SUON+'trans.wav','-t','0.8','-af','afade=t=out:st=0.5:d=0.3','-c:a','pcm_s16le','-ar','48000','-ac','2',TR])
def edge(p,which):
    """fotogramma (png) del primo/ultimo istante del pezzo, dal video"""
    f=p['v'][:-4]+('_first.png' if which=='first' else '_last.png')
    if not os.path.exists(f):
        t=0 if which=='first' else max(0,(p['n']-2)/30)
        M.sh(['ffmpeg','-v','error','-y','-ss',f'{t:.3f}','-i',p['v'],'-frames:v','1',f])
    return f
def xf(prev,nxt):
    a=edge(prev,'last');b=edge(nxt,'first')
    from PIL import Image
    A=Image.open(a).convert('RGB');B=Image.open(b).convert('RGB');n=24;sts=[]
    for i in range(n):sts.append((M.save_png(Image.blend(A,B,(i+1)/(n+1))),1))
    return M.still_piece('xf',sts,[(TR,0.0,0.9)],tag=(a,b))
def assemble(seq,out_prefix,tags):
    """seq: lista di (nome_timeline, pezzo); inserisce una dissolvenza davanti a ogni pezzo tranne il primo. Restituisce (lista pezzi con xf, timeline)"""
    allp=[];tl=[];t=0.0;prev=None
    for name,p in seq:
        if prev is not None:
            x=xf(prev,p);allp.append(x);t+=x['n']/30
        start=t
        allp.append(p);t+=p['n']/30
        tl.append([name,round(start,3),round(t-start,3)]);prev=p
    return allp,tl
