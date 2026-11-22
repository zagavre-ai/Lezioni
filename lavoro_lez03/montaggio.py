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
def doc_piece(name,src,subs,states,tag=''):
    """pezzo con il prof: subs=[(x,y)] intervalli sorgente (secondi, multipli di 1/30), states=[(png,frames)] in tempo d'uscita"""
    frames=[nfr(y-x) for x,y in subs];N=sum(frames)
    k=key_of('doc',src,subs,[(p,f) for p,f in states],tag)
    v=f'{OUT}/pezzi/{name}_{k}.mp4';a=f'{OUT}/pezzi/{name}_{k}.wav'
    if os.path.exists(v) and os.path.exists(a):return dict(v=v,a=a,n=N,first=states[0][0],last=states[-1][0],name=name)
    lst=f'{OUT}/pezzi/{name}_{k}.txt';states=_list(states,N,lst)
    cmd=['ffmpeg','-v','error','-y','-f','concat','-safe','0','-i',lst]
    for (x,y),f in zip(subs,frames):cmd+=['-ss',f'{x:.4f}','-t',f'{f/FPS:.4f}','-i',src]
    fc=[];vi=[];ai=[]
    for i,f in enumerate(frames,1):
        fc.append(f'[{i}:v]{CAM},setpts=PTS-STARTPTS[c{i}]');vi.append(f'[c{i}]')
        fd=f/FPS
        fc.append(f'[{i}:a]aresample=48000,asetpts=PTS-STARTPTS,apad=whole_dur={fd:.4f},atrim=0:{fd:.4f},afade=t=in:st=0:d=0.03,afade=t=out:st={max(0,fd-0.03):.4f}:d=0.03[a{i}]');ai.append(f'[a{i}]')
    fc.append(''.join(vi)+f'concat=n={len(frames)}:v=1:a=0[cam]')
    fc.append(''.join(ai)+f'concat=n={len(frames)}:v=0:a=1,highpass=f=70,afftdn=nr=6:nf=-48:tn=0,pan=stereo|c0=c0|c1=c0[au]')
    fc.append(f'[0:v]fps=30,format=yuv420p[bg];[bg][cam]overlay=1428:148:format=auto:shortest=0,format=yuv420p[v]')
    cmd+=['-filter_complex',';'.join(fc),'-map','[v]','-frames:v',str(N),'-c:v','libx264','-preset','veryfast','-crf','19','-pix_fmt','yuv420p','-r','30','-an',v,
          '-map','[au]','-t',f'{N/FPS:.4f}','-c:a','pcm_s16le','-ar','48000',a]
    sh(cmd)
    return dict(v=v,a=a,n=N,first=states[0][0],last=states[-1][0],name=name)
def wav_events(events,total_frames,out):
    """mix audio: events=[(wav,offset_sec,gain)] su durata fissa -> wav 48k stereo"""
    d=total_frames/FPS;cmd=['ffmpeg','-v','error','-y']
    for w,o,g in events:cmd+=['-i',w]
    if not events:cmd+=['-f','lavfi','-i','anullsrc=r=48000:cl=stereo']
    fc=[]
    for i,(w,o,g) in enumerate(events):
        fc.append(f'[{i}:a]aresample=48000,pan=stereo|c0=c0|c1=c0,adelay={int(o*1000)}|{int(o*1000)},volume={g}[e{i}]')
    if events:
        fc.append(''.join(f'[e{i}]' for i in range(len(events)))+f'amix=inputs={len(events)}:normalize=0:duration=longest,apad=whole_dur={d:.4f},atrim=0:{d:.4f}[au]')
        cmd+=['-filter_complex',';'.join(fc),'-map','[au]']
    cmd+=['-t',f'{d:.4f}','-c:a','pcm_s16le','-ar','48000','-ac','2',out]
    sh(cmd)
def still_piece(name,states,events=(),bg=None,tag=''):
    """pezzo senza prof: states=[(png,frames)] (anche RGBA sopra lo sfondo animato bg), events=[(wav,offset,gain)]"""
    N=sum(f for _,f in states)
    k=key_of('still',name,[(p,f) for p,f in states],list(events),bg,tag)
    v=f'{OUT}/pezzi/{name}_{k}.mp4';a=f'{OUT}/pezzi/{name}_{k}.wav'
    if os.path.exists(v) and os.path.exists(a):return dict(v=v,a=a,n=N,first=states[0][0],last=states[-1][0],name=name)
    lst=f'{OUT}/pezzi/{name}_{k}.txt';states=_list(states,N,lst)
    if bg:
        cmd=['ffmpeg','-v','error','-y','-stream_loop','-1','-i',bg,'-f','concat','-safe','0','-i',lst,
             '-filter_complex','[0:v]fps=30,scale=1920:1080,format=yuv420p[b];[1:v]fps=30,format=rgba[f];[b][f]overlay=0:0:shortest=1,format=yuv420p[v]','-map','[v]']
    else:
        cmd=['ffmpeg','-v','error','-y','-f','concat','-safe','0','-i',lst,'-vf','fps=30,format=yuv420p','-map','0:v']
    cmd+=['-frames:v',str(N),'-c:v','libx264','-preset','veryfast','-crf','19','-pix_fmt','yuv420p','-r','30','-an',v]
    sh(cmd);wav_events(list(events),N,a)
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
