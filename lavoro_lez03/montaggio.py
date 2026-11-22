# Montaggio a pezzi con cache: ogni pezzo = video senza audio (h264, 1080p30, N fotogrammi esatti) + audio wav 48 kHz stereo della stessa durata
import os,subprocess,hashlib,json,shutil
from PIL import Image
OUT='/tmp/w/out';os.makedirs(OUT+'/pezzi',exist_ok=True);os.makedirs(OUT+'/png',exist_ok=True)
FPS=30
def sh(cmd,**k):
    r=subprocess.run(cmd,capture_output=True,text=True,**k)
    if r.returncode:raise RuntimeError(' '.join(map(str,cmd))[:300]+'\n'+r.stderr[-1500:])
    return r
def nfr(sec):return max(1,round(sec*FPS))
def save_png(img,key=None):
    """salva una Image e restituisce il percorso (nome dal contenuto)"""
    if isinstance(img,str):return img
    h=hashlib.md5(img.tobytes()).hexdigest()[:16];p=f'{OUT}/png/{h}.png'
    if not os.path.exists(p):img.save(p)
    return p
def _list(states,total_frames,path):
    """states=[(png,frames)] -> file per il concat demuxer; l'ultimo stato si allunga/accorcia per fare total_frames"""
    s=sum(f for _,f in states)
    if s!=total_frames:states=states[:-1]+[(states[-1][0],states[-1][1]+total_frames-s)]
    with open(path,'w') as f:
        for p,fr in states:f.write(f"file '{p}'\nduration {fr/FPS:.6f}\n")
        f.write(f"file '{states[-1][0]}'\n")
    return states
def key_of(*a):return hashlib.md5(json.dumps(a,default=str).encode()).hexdigest()[:14]
CAM='crop=180:135:856:345,scale=412:309:flags=lanczos,unsharp=5:5:0.5:3:3:0.0,eq=contrast=1.03:saturation=1.04,fps=30,setsar=1'
import numpy as np
CAMW,CAMH=412,309
CAMV='crop=180:135:856:345,scale=412:309:flags=lanczos,unsharp=5:5:0.5:3:3:0.0,eq=contrast=1.03:saturation=1.04,fps=30,setsar=1'
def _rd(p,n):
    b=bytearray()
    while len(b)<n:
        c=p.stdout.read(n-len(b))
        if not c:break
        b+=c
    return bytes(b)
def _enc(out_v,N):
    return subprocess.Popen(['ffmpeg','-v','error','-y','-f','rawvideo','-pix_fmt','rgb24','-s','1920x1080','-r','30','-i','-','-frames:v',str(N),
        '-c:v','libx264','-preset','veryfast','-crf','21','-pix_fmt','yuv420p','-r','30','-an',out_v],stdin=subprocess.PIPE)
_png_cache={}
def load_png(p):
    if p not in _png_cache:
        if len(_png_cache)>6:_png_cache.clear()
        _png_cache[p]=np.array(Image.open(p).convert('RGB'))
    return _png_cache[p]
def doc_piece(name,src,subs,states,tag=''):
    """pezzo con il prof: subs=[(x,y)] intervalli sorgente, states=[(png,frames)] in tempo d'uscita (il riquadro del prof si sovrappone)"""
    frames=[nfr(y-x) for x,y in subs];N=sum(frames)
    k=key_of('doc3',src,subs,[(p,f) for p,f in states],tag)
    v=f'{OUT}/pezzi/{name}_{k}.mp4';a=f'{OUT}/pezzi/{name}_{k}.wav'
    if os.path.exists(v) and os.path.exists(a):return dict(v=v,a=a,n=N,first=states[0][0],last=states[-1][0],name=name,src=src,subs=subs)
    s=sum(f for _,f in states)
    if s!=N:states=states[:-1]+[(states[-1][0],states[-1][1]+N-s)]
    # audio
    cmd=['ffmpeg','-v','error','-y'];fc=[];ai=[]
    for (x,y),f in zip(subs,frames):cmd+=['-ss',f'{x:.4f}','-t',f'{f/FPS:.4f}','-i',src]
    for i,f in enumerate(frames):
        fd=f/FPS
        fc.append(f'[{i}:a]aresample=48000,asetpts=PTS-STARTPTS,apad=whole_dur={fd:.4f},atrim=0:{fd:.4f},afade=t=in:st=0:d=0.03,afade=t=out:st={max(0,fd-0.03):.4f}:d=0.03[a{i}]');ai.append(f'[a{i}]')
    fc.append(''.join(ai)+f'concat=n={len(frames)}:v=0:a=1,highpass=f=70,afftdn=nr=6:nf=-48:tn=0,atrim=start=0.0250,asetpts=PTS-STARTPTS,apad,pan=stereo|c0=c0|c1=c0[au]')
    cmd+=['-filter_complex',';'.join(fc),'-map','[au]','-t',f'{N/FPS:.4f}','-c:a','pcm_s16le','-ar','48000',a]
    sh(cmd)
    # video
    enc=_enc(v,N);fi=0;si=0;left=states[0][1];buf=load_png(states[0][0]).copy();cur=states[0][0]
    for (x,y),f in zip(subs,frames):
        cp=subprocess.Popen(['ffmpeg','-v','error','-ss',f'{x:.4f}','-t',f'{f/FPS:.4f}','-i',src,'-vf',CAMV,'-an','-f','rawvideo','-pix_fmt','rgb24','-'],stdout=subprocess.PIPE)
        last=None
        for _ in range(f):
            raw=_rd(cp,CAMW*CAMH*3)
            if len(raw)==CAMW*CAMH*3:last=np.frombuffer(raw,np.uint8).reshape(CAMH,CAMW,3)
            while left==0:
                si+=1;left=states[si][1];buf=load_png(states[si][0]).copy()
            if last is not None:buf[148:148+CAMH,1428:1428+CAMW]=last
            enc.stdin.write(buf);left-=1
        cp.stdout.close();cp.wait()
    enc.stdin.close();enc.wait()
    return dict(v=v,a=a,n=N,first=states[0][0],last=states[-1][0],name=name,src=src,subs=subs)
def wav_events(events,total_frames,out):
    """mix audio: events=[(wav,offset_sec,gain[,ss,dur])] su durata fissa -> wav 48k stereo"""
    d=total_frames/FPS;cmd=['ffmpeg','-v','error','-y']
    for e in events:
        if len(e)>3:cmd+=['-ss',f'{e[3]:.4f}','-t',f'{e[4]:.4f}']
        cmd+=['-i',e[0]]
    if not events:cmd+=['-f','lavfi','-i','anullsrc=r=48000:cl=stereo']
    fc=[]
    for i,e in enumerate(events):
        o,g=e[1],e[2]
        fc.append(f'[{i}:a]aresample=48000,pan=stereo|c0=c0|c1=c0,adelay={int(o*1000)}|{int(o*1000)},volume={g}[e{i}]')
    if events:
        fc.append(''.join(f'[e{i}]' for i in range(len(events)))+f'amix=inputs={len(events)}:normalize=0:duration=longest,apad=whole_dur={d:.4f},atrim=0:{d:.4f}[au]')
        cmd+=['-filter_complex',';'.join(fc),'-map','[au]']
    cmd+=['-t',f'{d:.4f}','-c:a','pcm_s16le','-ar','48000','-ac','2',out]
    sh(cmd)
def still_piece(name,states,events=(),bg=None,tag='',layers=None):
    """pezzo senza prof: states=[(png,frames)] (RGBA sopra lo sfondo animato bg, oppure RGB opaco); layers=funzione(f,buf) facoltativa per animazioni"""
    N=sum(f for _,f in states)
    k=key_of('still2',name,[(p,f) for p,f in states],list(events),bg,tag)
    v=f'{OUT}/pezzi/{name}_{k}.mp4';a=f'{OUT}/pezzi/{name}_{k}.wav'
    if os.path.exists(v) and os.path.exists(a):return dict(v=v,a=a,n=N,first=states[0][0],last=states[-1][0],name=name)
    wav_events(list(events),N,a)
    enc=_enc(v,N);bgp=None
    if bg:bgp=subprocess.Popen(['ffmpeg','-v','error','-stream_loop','-1','-i',bg,'-vf','fps=30,scale=1920:1080:flags=bicubic','-an','-f','rawvideo','-pix_fmt','rgb24','-'],stdout=subprocess.PIPE)
    FB=1920*1080*3
    for p,fr in states:
        if bg:
            im=np.array(Image.open(p).convert('RGBA'));al=im[...,3:4].astype(np.uint16);fg=(im[...,:3].astype(np.uint16)*al//255);inv=(255-al)
        else:arr=load_png(p)
        for _ in range(fr):
            if bg:
                b=np.frombuffer(_rd(bgp,FB),np.uint8).reshape(1080,1920,3)
                out=(b.astype(np.uint16)*inv//255+fg).astype(np.uint8)
            else:out=arr
            enc.stdin.write(out)
    enc.stdin.close();enc.wait()
    if bgp:bgp.kill()
    return dict(v=v,a=a,n=N,first=states[0][0],last=states[-1][0],name=name)
def xfade_piece(prev_png,next_png,jingle,frames=15):
    """dissolvenza di 0,5 s tra due schermate (nel silenzio del prof) con trans.wav"""
    a=Image.open(prev_png).convert('RGB');b=Image.open(next_png).convert('RGB')
    sts=[]
    for i in range(frames):
        t=(i+1)/(frames+1);sts.append((save_png(Image.blend(a,b,t)),1))
    return still_piece('xf',sts,[(jingle,0.0,0.8)],tag=(prev_png,next_png))
def concat_all(pieces,out_v,out_a):
    """concatena video (copy) e audio (wav) di tutti i pezzi"""
    lv=f'{OUT}/lista_v.txt';la=f'{OUT}/lista_a.txt'
    open(lv,'w').write(''.join(f"file '{p['v']}'\n" for p in pieces))
    open(la,'w').write(''.join(f"file '{p['a']}'\n" for p in pieces))
    sh(['ffmpeg','-v','error','-y','-f','concat','-safe','0','-i',lv,'-c','copy',out_v])
    sh(['ffmpeg','-v','error','-y','-f','concat','-safe','0','-i',la,'-c','copy',out_a])
