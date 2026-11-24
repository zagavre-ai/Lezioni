import os, json, subprocess, hashlib
from whites import *
from screens import *
from profpieces import *
from maps import *
OUTD=f'{W}/clips';os.makedirs(OUTD,exist_ok=True)
class Ctx:
    def __init__(s,part,rend):
        s.part=part;s.rend=rend;s.clips=[];s.page=0;s.pagemap={};s.t=0.0;s.timeline=[];s.dispensa=[]  # dispensa: (png, testo)
    def newpage(s,key=None):
        if key is not None and key in s.pagemap: return s.pagemap[key]
        s.page+=1
        if key is not None: s.pagemap[key]=s.page
        return s.page
    def dpage(s,png,testo,key=None):
        if key is not None and key in s.pagemap: return s.pagemap[key]
        s.page+=1
        s.dispensa.append((png,testo,s.page))
        if key is not None: s.pagemap[key]=s.page
        return s.page
    def add(s,path,kind,label,arg=None,anim=True,png=None,testo=''):
        d=dur(path)
        s.clips.append(dict(path=path,kind=kind,label=label,arg=arg,anim=anim,dur=d))
        s.timeline.append([label,kind,round(s.t,2),round(d,2),arg]);s.t+=d
        if png and kind not in ('prof','approfondimento'): s.dpage(png,testo or label)
        return d
def frame_png(video,out,last=False):
    if last: sh(['ffmpeg','-v','error','-y','-sseof','-0.07','-i',video,'-frames:v','1','-update','1',out])
    else: sh(['ffmpeg','-v','error','-y','-i',video,'-frames:v','1',out])
def junction(ctx,idx):
    """clip di transizione tra clips[idx-1] e clips[idx] (trans.wav + dissolvenza 0,8 s)"""
    A=ctx.clips[idx-1];B=ctx.clips[idx]
    ja=f'{OUTD}/j{ctx.part}_{idx}_a.png';jb=f'{OUTD}/j{ctx.part}_{idx}_b.png'
    frame_png(A['path'],ja,True);frame_png(B['path'],jb,False)
    T=2.02;dis=0.8
    if A['anim'] and B['anim']: x=0.6;y=T-x-dis
    elif not A['anim']: x=0.0;y=T-dis
    else: x=T-dis;y=0.0
    x=fr(x);y=fr(y);tot=fr(x+dis+y)
    out=f'{OUTD}/j{ctx.part}_{idx}.mkv'
    fc=f'[0:v]format=yuv420p[a];[1:v]format=yuv420p[b];[a][b]xfade=transition=fade:duration={dis}:offset={x}[v]'
    r=sh(['ffmpeg','-v','error','-y','-loop','1','-framerate','30','-t',f'{x+dis:.3f}','-i',ja,'-loop','1','-framerate','30','-t',f'{dis+y:.3f}','-i',jb,
          '-i',JING['trans'],'-filter_complex',fc,'-map','[v]','-map','2:a','-t',f'{tot:.3f}','-r','30','-c:v','libx264','-preset','veryfast','-crf','14',
          '-c:a','pcm_s16le','-ar','48000','-ac','2','-af','volume=8dB,apad',out])
    if r.returncode: raise SystemExit(r.stderr[-600:])
    return out
def build_master(ctx,outname):
    """inserisce le transizioni e concatena tutti i clip in un mkv unico (copia)"""
    L=[];n=0
    for i,c in enumerate(ctx.clips):
        if i>0:
            j=junction(ctx,i);L.append(j);ctx.timeline.append(['trans','trans',0,dur(j),None])
        L.append(c['path'])
    lst=f'{OUTD}/{outname}.txt';open(lst,'w').write(''.join(f"file '{p}'\n" for p in L))
    m=f'{OUTD}/{outname}_master.mkv'
    r=sh(['ffmpeg','-v','error','-y','-f','concat','-safe','0','-i',lst,'-c','copy',m])
    if r.returncode: raise SystemExit(r.stderr[-600:])
    return m
def to_clip(src_mp4,out,fps=30,aud=True):
    """re-encode di un mp4 esterno (sigla) al formato dei clip"""
    sh(['ffmpeg','-v','error','-y','-i',src_mp4,'-vf','scale=1920:1080,fps=30,format=yuv420p','-c:v','libx264','-preset','veryfast','-crf','14','-c:a','pcm_s16le','-ar','48000','-ac','2',out])
    return out
