import sys,os,json,re,subprocess,shutil,glob
sys.path.insert(0,'/tmp/L18/lib')
from build import *
import numpy as np
from PIL import Image
VN=W+'/vn';VOX=W+'/voci/scambio/storia-V-lez18/vox'
SND=W+'/kit/home/claude/v5/snd'
TXT={x['nome']:x['testo'] for x in json.load(open(W+'/voci/scambio/storia-V-lez18/testi_voci.json'))}
def dur(p):
    return float(run(['ffprobe','-v','error','-show_entries','format=duration','-of','csv=p=0',p]).stdout)
def vn(name):
    p=f'{VN}/{name}.wav'
    if not os.path.exists(p):
        src=f'{VOX}/{name}.wav'
        if not os.path.exists(src):raise SystemExit('manca la voce '+name)
        run(['ffmpeg','-y','-loglevel','error','-i',src,'-af','loudnorm=I=-16:TP=-1.5:LRA=7,aresample=48000','-ac','2','-ar','48000',p])
    return p
def sents(name):
    return re.split(r'(?<=[.!?:])\s+',TXT[name])
_al={}
def align_(name):
    from align import sentence_times
    if name not in _al:
        c=f'{W}/al_{name}.json'
        if os.path.exists(c):_al[name]=json.load(open(c))
        else:
            t,d=sentence_times(vn(name),sents(name));_al[name]=[t,d];json.dump(_al[name],open(c,'w'))
    return _al[name]
def blend_frames(prev,first,k,tag):
    """k fotogrammi che sfumano da prev a first (png) -> cartella; ritorna clip mp4"""
    out=f'{SG}/clips/bl_{tag}_{k}.mp4'
    if os.path.exists(out):return out
    d=f'{SG}/clips/_b_{tag}';os.makedirs(d,exist_ok=True)
    a=Image.open(prev).convert('RGB');b=Image.open(first).convert('RGB')
    for i in range(k):
        Image.blend(a,b,(i+1)/(k+1)).save(f'{d}/{i:03d}.png')
    run(['ffmpeg','-y','-loglevel','error','-framerate','30','-i',d+'/%03d.png','-frames:v',str(k),'-vf','format=yuv420p']+ENC+[out+'.t.mp4']);os.rename(out+'.t.mp4',out);shutil.rmtree(d)
    return out
def stills2(seq,out,prev=None,blend=9,cam=None,tag=''):
    """come stills ma con testa sfumata da prev (png). seq [(png,frames)]"""
    if os.path.exists(out):return
    os.makedirs(SG+'/clips',exist_ok=True)
    lst=out+'.txt';n=0;parts=[]
    first=True
    for png,k in seq:
        if first and prev is not None and blend>0:
            b=min(blend,k-1) if k>blend else k
            parts.append(blend_frames(prev,png,b,os.path.basename(out)[:-4]))
            n+=b
            rest=k-b
            if rest>0:
                c=clip(png,rest);parts.append(c);n+=rest
        else:
            c=clip(png,k);parts.append(c);n+=k
        first=False
    with open(lst,'w') as f:
        for c in parts:f.write(f"file '{c}'\n")
    base=out+'.base.mp4' if cam is not None else out+'.tmp.mp4'
    run(['ffmpeg','-y','-loglevel','error','-f','concat','-safe','0','-i',lst,'-c','copy',base])
    if cam is not None:
        fc=("[1:v]crop=184:138:874:343,scale=412:309:flags=lanczos,eq=contrast=1.04:saturation=1.03,hqdn3d=1.5:1.5:3:3,cas=0.35,format=rgba,fade=t=in:st=0:d=0.3:alpha=1[c];"
            "[2:v]format=gray[m];[c][m]alphamerge[cm];[0:v]format=rgba[b];[b][cm]overlay=1428:146:shortest=1,format=yuv420p[o]")
        run(['ffmpeg','-y','-loglevel','error','-i',base,'-ss',f'{cam:.3f}','-t',f'{n/FPS+0.5:.3f}','-i',W+'/prof.mp4','-loop','1','-framerate','30','-t',f'{n/FPS+0.5:.3f}','-i',ST+'/mask.png',
             '-filter_complex',fc,'-map','[o]','-frames:v',str(n)]+ENC+[out+'.tmp.mp4']);os.remove(base)
    os.rename(out+'.tmp.mp4',out);return n
def clip(png,k):
    c=f"{SG}/clips/{os.path.basename(png)[:-4]}_{k}.mp4"
    if not os.path.exists(c):
        run(['ffmpeg','-y','-loglevel','error','-loop','1','-framerate','30','-i',png,'-frames:v',str(k),'-vf','format=yuv420p']+ENC+[c+'.t.mp4']);os.rename(c+'.t.mp4',c)
    return c
def last_png(mp4,out):
    if not os.path.exists(out):
        run(['ffmpeg','-y','-loglevel','error','-sseof','-0.1','-i',mp4,'-update','1','-frames:v','1',out])
    return out
def mp4_enter(raw,prev,out,d=0.3,extra=None):
    """scheda/sigla: dissolve dai primi d secondi dall'ultimo fotogramma prev (png)"""
    if os.path.exists(out):return
    n=nframes(raw)
    fc=f"[1:v]format=rgba,fade=t=out:st=0:d={d}:alpha=1[o];[0:v][o]overlay=eof_action=pass:shortest=0,format=yuv420p[v]"
    run(['ffmpeg','-y','-loglevel','error','-i',raw,'-loop','1','-framerate','30','-t',str(d+0.1),'-i',prev,'-filter_complex',fc,'-map','[v]','-frames:v',str(n)]+ENC+[out+'.t.mp4']);os.rename(out+'.t.mp4',out)
