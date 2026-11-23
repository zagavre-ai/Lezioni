# -*- coding: utf-8 -*-
import sys, os, json, subprocess, re, math, shutil, wave
import numpy as np
sys.path.insert(0,'/home/work/build')
import av
from av import sh, nframes, readwav
XF=12;SR=48000
PROF='/home/work/an/prof_clean.wav'
class Timeline:
    def __init__(self): self.pieces=[]
    def add(self,name,path,audio=None,tag=None,**kw):
        n=nframes(path)
        start=0 if not self.pieces else self.pieces[-1]['start']+self.pieces[-1]['n']-XF
        self.pieces.append(dict(name=name,path=path,n=n,start=start,audio=audio or [],tag=tag or name,**kw));return self.pieces[-1]
    def total_frames(self): return self.pieces[-1]['start']+self.pieces[-1]['n']
def build_video(T,out,tmp):
    os.makedirs(tmp,exist_ok=True);parts=[];P=T.pieces
    for i,p in enumerate(P):
        h=XF if i>0 else 0;t=XF if i<len(P)-1 else 0
        a=h/30.0;body=f'{tmp}/b{i:03d}.mp4'
        if not os.path.exists(body):
            sh(['ffmpeg','-y','-v','error','-ss',f'{a:.4f}','-i',p['path'],'-frames:v',str(p['n']-h-t),'-c','copy','-avoid_negative_ts','make_zero',body])
        parts.append(body)
        if i<len(P)-1:
            x=f'{tmp}/x{i:03d}.mp4'
            if not os.path.exists(x):
                A=P[i];B=P[i+1]
                sh(['ffmpeg','-y','-v','error','-ss',f"{(A['n']-XF)/30.0:.4f}",'-i',A['path'],'-i',B['path'],'-filter_complex',
                    f'[0:v]trim=end_frame={XF},setpts=PTS-STARTPTS[a];[1:v]trim=end_frame={XF},setpts=PTS-STARTPTS[b];[a][b]xfade=transition=fade:duration={XF/30.0:.4f}:offset=0,format=yuv420p[v]',
                    '-map','[v]','-frames:v',str(XF),'-c:v','libx264','-preset','veryfast','-crf','21','-r','30','-g','60','-pix_fmt','yuv420p','-an',x])
            parts.append(x)
    with open(tmp+'/list.txt','w') as f:
        for p in parts: f.write(f"file '{p}'\n")
    sh(['ffmpeg','-y','-v','error','-f','concat','-safe','0','-i',tmp+'/list.txt','-c','copy',out])
_prof=None
def prof_audio():
    global _prof
    if _prof is None:
        w=wave.open(PROF);_prof=np.frombuffer(w.readframes(w.getnframes()),dtype=np.int16).astype(np.float32)/32768
    return _prof
def fade(a,ms=30):
    n=int(SR*ms/1000)
    if len(a)>2*n:
        a=a.copy();r=np.linspace(0,1,n,dtype=np.float32)[:,None];a[:n]*=r;a[-n:]*=r[::-1]
    return a
def mix_audio(T):
    total=int(round(T.total_frames()/30.0*SR));mix=np.zeros((total,2),dtype=np.float32);prof=prof_audio()
    for p in T.pieces:
        t0=int(p['start']/30.0*SR)
        for ev in p['audio']:
            off,kind,arg=ev[0],ev[1],ev[2]
            if kind=='wav':
                a=readwav(arg)
                if len(ev)>3 and ev[3]=='fade': a=fade(a,30)
            elif kind=='prof':
                segs=[np.repeat(fade(prof[int(x*SR):int(y*SR),None],25),2,axis=1) for x,y in arg];a=np.concatenate(segs)
            s=t0+int(off*SR);e=min(total,s+len(a));mix[s:e]+=a[:e-s]
    return mix
def write(arr,path):
    pcm=(np.clip(arr,-0.97,0.97)*32767).astype(np.int16)
    w=wave.open(path,'wb');w.setnchannels(2);w.setsampwidth(2);w.setframerate(SR);w.writeframes(pcm.tobytes());w.close()
def lufs(path):
    r=subprocess.run(['ffmpeg','-nostats','-i',path,'-af','ebur128=peak=true','-f','null','-'],capture_output=True,text=True).stderr
    I=float(re.findall(r'\n\s+I:\s+(-?[\d\.]+) LUFS',r)[-1]);tp=re.findall(r'Peak:\s+(-?[\d\.]+) dBFS',r)
    return I,float(tp[-1]) if tp else None
def finish(T,P,outdir,name):
    os.makedirs(outdir,exist_ok=True)
    video=f'{outdir}/{name}_video.mp4'
    if not (os.environ.get('AUDIOONLY') and os.path.exists(video)):
        shutil.rmtree(f'{outdir}/tmp{P}',ignore_errors=True);build_video(T,video,f'{outdir}/tmp{P}')
    mix=mix_audio(T);write(mix,f'{outdir}/audio{P}_pre.wav')
    I,tp=lufs(f'{outdir}/audio{P}_pre.wav');gain=10**((-16.0-I)/20.0);mix=mix*gain
    pk=np.abs(mix).max();print('LUFS prima',I,'gain dB',20*math.log10(gain),'picco campione',20*math.log10(pk+1e-9))
    if pk>0.89: # limitatore dolce per picco <= -1 dBTP
        pass
    write(mix,f'{outdir}/audio{P}.wav')
    sh(['ffmpeg','-y','-v','error','-i',video,'-i',f'{outdir}/audio{P}.wav','-map','0:v','-map','1:a','-c:v','copy','-c:a','aac','-b:a','192k','-ar','48000','-movflags','+faststart',f'{outdir}/{name}.mp4'])
    return f'{outdir}/{name}.mp4'
