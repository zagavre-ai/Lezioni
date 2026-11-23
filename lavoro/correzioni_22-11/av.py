# -*- coding: utf-8 -*-
import subprocess, os, hashlib, json, wave
import numpy as np
W='/home/work/build'
SRC='/home/work/l17/orig/LEZIONE.17.LE.FASI.CONCLUSIVE.DELLA.GUERRA.FREDDA.1969-1991.mp4'
FPS=30
def sh(c,**k): return subprocess.run(c,check=True,**k)
def probe_dur(f):
    return float(subprocess.run(['ffprobe','-v','error','-show_entries','format=duration','-of','csv=p=0',f],capture_output=True,text=True).stdout)
def nframes(f):
    r=subprocess.run(['ffprobe','-v','error','-count_packets','-select_streams','v:0','-show_entries','stream=nb_read_packets','-of','csv=p=0',f],capture_output=True,text=True)
    return int(r.stdout.strip().split(',')[0])
def fr(s): return int(round(s*FPS))
# maschera arrotondata 412x310
def make_mask():
    from PIL import Image, ImageDraw
    m=Image.new('L',(412,310),0);ImageDraw.Draw(m).rounded_rectangle((0,0,411,309),radius=14,fill=255);m.save(W+'/mask.png')
if not os.path.exists(W+'/mask.png'): make_mask()
ENC=['-c:v','libx264','-preset','veryfast','-crf','21','-r','30','-g','60','-pix_fmt','yuv420p','-an']
def states_video(states,out,xf=0.3):
    """states [(png, frames)] -> mp4 con dissolvenze brevi tra stati; durata totale = somma dei frame. keyframe a 0,4 s e a fine-0,4 s."""
    n=len(states); tot=sum(f for _,f in states)
    if n==1:
        cmd=['ffmpeg','-y','-v','error','-loop','1','-framerate','30','-i',states[0][0],'-frames:v',str(tot)]+ENC+['-force_key_frames',f'0.4,{tot/30-0.4:.3f}',out]
        sh(cmd);return tot
    xfr=max(2,int(round(xf*30)))
    cmd=['ffmpeg','-y','-v','error'];fc=[];
    for i,(p,f) in enumerate(states):
        L=f+(xfr if i<n-1 else 0)
        cmd+=['-loop','1','-framerate','30','-t',f'{L/30:.4f}','-i',p]
    cum=0;prev='[0:v]'
    for i in range(n-1):
        cum+=states[i][1]
        lab=f'[x{i}]' if i<n-2 else '[vout]'
        fc.append(f'{prev}[{i+1}:v]xfade=transition=fade:duration={xfr/30:.4f}:offset={cum/30:.4f}{lab}');prev=lab
    cmd+=['-filter_complex',';'.join(fc),'-map','[vout]','-frames:v',str(tot)]+ENC+['-force_key_frames',f'0.4,{tot/30-0.4:.3f}',out]
    sh(cmd);return tot
def still_seq(states,out):
    """stati senza dissolvenza (concat di still) con overlay opzionale gestito altrove"""
    pass
def norm_encode(src,out,limit=None,start=0):
    d=probe_dur(src)-start
    if limit:d=min(d,limit)
    n=int(round(d*FPS))
    sh(['ffmpeg','-y','-v','error','-ss',f'{start:.3f}','-i',src,'-frames:v',str(n)]+ENC+['-force_key_frames',f'0.4,{n/FPS-0.4:.3f}',out])
    return n
def prof_piece(subs,states,out,w=W,crop=(181,136,856,344),box=(1428,148)):
    """subs [(a,b)] intervalli del sorgente (s); states [(png,frames)] sulla somma; webcam 4:3 412x310 sopra la slide."""
    N=sum(int(round((b-a)*30)) for a,b in subs) if len(subs)>1 else int(round((subs[0][1]-subs[0][0])*30))
    assert sum(f for _,f in states)==N,(sum(f for _,f in states),N)
    lst=out+'.lst'
    with open(lst,'w') as f:
        for p,fra in states:
            h=hashlib.md5(f'{p}{os.path.getmtime(p)}'.encode()).hexdigest()[:10]
            clip=f'{w}/segs/{h}_{fra}.mp4'
            if not os.path.exists(clip):
                os.makedirs(w+'/segs',exist_ok=True)
                sh(['ffmpeg','-y','-v','error','-loop','1','-framerate','30','-i',p,'-frames:v',str(fra),'-c:v','libx264','-preset','ultrafast','-crf','12','-pix_fmt','yuv420p','-g','30','-r','30',clip+'.tmp.mp4']);os.rename(clip+'.tmp.mp4',clip)
            f.write(f"file '{clip}'\n")
    cw,ch,cx,cy=crop
    cmd=['ffmpeg','-y','-v','error','-f','concat','-safe','0','-i',lst]
    for a,b in subs: cmd+=['-ss',f'{a:.3f}','-t',f'{b-a+0.3:.3f}','-i',SRC]
    k=len(subs); cmd+=['-loop','1','-framerate','30','-i',w+'/mask.png']
    fc='';parts=''
    for i,(a,b) in enumerate(subs):
        nf=int(round((b-a)*30)) if k>1 else N
        fc+=f"[{i+1}:v]fps=30,trim=end_frame={nf},setpts=PTS-STARTPTS,crop={cw}:{ch}:{cx}:{cy},scale=412:310:flags=lanczos,hqdn3d=1.5:1.5:3:3,eq=contrast=1.04:saturation=1.03,cas=0.35[c{i}];"
        parts+=f'[c{i}]'
    fc+=parts+f"concat=n={k}:v=1:a=0,format=yuva420p[p];[{k+1}:v]format=gray[m];[p][m]alphamerge[pa];[0:v]format=yuv420p[bg];[bg][pa]overlay={box[0]}:{box[1]}:format=auto,format=yuv420p[v]"
    cmd+=['-filter_complex',fc,'-map','[v]','-frames:v',str(N),'-c:v','libx264','-preset','veryfast','-crf','21','-r','30','-g','60','-force_key_frames',f'0.4,{N/30-0.4:.3f}','-pix_fmt','yuv420p','-an',out]
    sh(cmd)
    return N
def readwav(f):
    w=wave.open(f);n=w.getnframes();ch=w.getnchannels();a=np.frombuffer(w.readframes(n),dtype=np.int16).astype(np.float32)/32768;a=a.reshape(-1,ch)
    if ch==1:a=np.repeat(a,2,axis=1)
    return a
def wav48(src,out,loud=None):
    if os.path.exists(out):return out
    af=(f'loudnorm=I={loud}:TP=-1.5:LRA=7,' if loud else '')+'aresample=48000'
    sh(['ffmpeg','-y','-v','error','-i',src,'-af',af,'-ac','2','-c:a','pcm_s16le',out]);return out
