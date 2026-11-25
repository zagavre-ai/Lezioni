import os,sys,json,shutil,subprocess,math
sys.path.insert(0,'/tmp/w/b')
from lib import *
PC='/tmp/w/pc';os.makedirs(PC,exist_ok=True)
KIT='/home/user/Lezioni/kit/'
VOX='/tmp/w/voci/scambio/storia-V-lez02/vox/'
FPS=30
TXT={x['nome']:x['testo'] for x in json.load(open('/tmp/w/voci/scambio/storia-V-lez02/testi_voci.json'))}
TXT.update({x['nome']:x['testo'] for x in json.load(open('/tmp/w/wv/scambio/storia-V-lez02/testi_voci.json'))})
_lu={}
def vgain(path):
    if path not in _lu: _lu[path]=lufs(path)
    return -16.0-_lu[path]
def sh(cmd,**k):
    r=subprocess.run(cmd,shell=isinstance(cmd,str),capture_output=True,text=True,**k)
    if r.returncode: raise RuntimeError((cmd if isinstance(cmd,str) else ' '.join(cmd))+'\n'+r.stderr[-1500:])
    return r
def nfr(sec): return int(round(sec*FPS))
def save(im,path):
    im.save(path,compress_level=1)
def video_from_frames(name,frames,total,fade=True,extra_overlay=None):
    """frames: list of (PIL image or path, dur). Writes PC/name.v.mp4 with exactly nfr(total) frames"""
    d=f'{PC}/{name}';shutil.rmtree(d,ignore_errors=True);os.makedirs(d)
    lines=[];acc=0.0;n=0;paths=[]
    for k,(im,du) in enumerate(frames):
        p=f'{d}/f{k:04d}.png'
        if isinstance(im,str): shutil.copy(im,p)
        else: save(im,p)
        paths.append((p,du))
    # quantize durations to frame counts
    tot=nfr(total);cnt=[];acc=0.0;done=0
    for p,du in paths:
        acc+=du;t=min(tot,nfr(acc));c=max(0,t-done);cnt.append(c);done+=c
    if done<tot: cnt[-1]+=tot-done
    with open(f'{d}/list.txt','w') as f:
        for (p,du),c in zip(paths,cnt):
            if c>0: f.write(f"file '{p}'\nduration {c/FPS:.6f}\n")
        f.write(f"file '{paths[-1][0]}'\n")
    return d,tot
def enc_video(name,d,tot,vf_extra='',inputs_extra=None,fc=None,fade=True):
    out=f'{PC}/{name}.v.mp4'
    fd=''
    if fade:
        fd=f",fade=t=in:st=0:d=0.4,fade=t=out:st={tot/FPS-0.4:.3f}:d=0.4"
    if fc is None:
        cmd=['ffmpeg','-v','error','-y','-f','concat','-safe','0','-i',f'{d}/list.txt','-vf',f'fps={FPS},format=yuv420p{fd}','-frames:v',str(tot),
             '-c:v','libx264','-preset','veryfast','-crf','19','-pix_fmt','yuv420p','-r',str(FPS),'-an',out]
    else:
        cmd=fc(d,tot,fd,out)
    sh(cmd);return out
def make_audio(name,tot,items,voice_fade=0.03):
    """items: (path,start_s,gain_db,kind) kind in voice|fx"""
    out=f'{PC}/{name}.wav';dur=tot/FPS
    if not items:
        sh(['ffmpeg','-v','error','-y','-f','lavfi','-i',f'anullsrc=r=48000:cl=stereo','-t',f'{dur:.4f}',out]);return out
    cmd=['ffmpeg','-v','error','-y'];fl=[];labs=[]
    for i,(p,st,g,kind) in enumerate(items):
        cmd+=['-i',p]
        f=f"[{i}:a]aformat=sample_rates=48000:channel_layouts=stereo,volume={g:.2f}dB"
        if kind=='voice':
            vd=float(sh(['ffprobe','-v','error','-show_entries','format=duration','-of','csv=p=0',p]).stdout)
            f+=f",afade=t=in:d={voice_fade},afade=t=out:st={max(0,vd-voice_fade):.3f}:d={voice_fade}"
        f+=f",adelay={int(st*1000)}|{int(st*1000)}[a{i}]"
        fl.append(f);labs.append(f'[a{i}]')
    fl.append(''.join(labs)+f"amix=inputs={len(items)}:normalize=0:duration=longest,apad=whole_dur={dur:.4f},atrim=0:{dur:.4f}[o]")
    cmd+=['-filter_complex',';'.join(fl),'-map','[o]','-ar','48000','-ac','2',out]
    sh(cmd);return out
def piece(name,frames,total,audio,fade=True):
    d,tot=video_from_frames(name,frames,total)
    v=enc_video(name,d,tot,fade=fade)
    a=make_audio(name,tot,audio)
    shutil.rmtree(d,ignore_errors=True)
    return dict(name=name,v=v,a=a,dur=tot/FPS)
TRANS=KIT+'suoni/trans.wav';JT=KIT+'suoni/titolo.wav';JR=KIT+'suoni/repaso.wav';JQ=KIT+'suoni/quiz.wav';JF=KIT+'suoni/finale.wav'
