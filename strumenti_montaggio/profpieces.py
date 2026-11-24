import os, subprocess, json
from edl import *
from kore import sh, dur, W
P=f'{W}/prof'
os.makedirs(f'{P}/a',exist_ok=True)
MASK=f'{P}/mask.png'
if not os.path.exists(MASK):
    from PIL import Image, ImageDraw
    m=Image.new('L',(412*4,309*4),0);ImageDraw.Draw(m).rounded_rectangle((0,0,412*4-1,309*4-1),radius=16*4,fill=255)
    m.resize((412,309),Image.LANCZOS).convert('RGB').save(MASK)
def snap(B):
    """intervalli agganciati alla griglia dei fotogrammi"""
    iv=[[fr(x),fr(y)] for x,y in B['iv']]
    acc=0;maps=[]
    for x,y in iv:
        maps.append((x,y,acc));acc+=y-x
    B['iv']=iv;B['maps']=maps;B['dur']=acc
    return B
def extract_arg(name,B):
    """cam_<name>.mkv e aud_<name>.wav: concatenazione degli intervalli tenuti (taglio nelle pause, audio e video insieme)"""
    cam=f'{P}/a/{name}_cam.mkv';aud=f'{P}/a/{name}_aud.wav'
    if os.path.exists(cam) and os.path.exists(aud) and os.path.exists(f'{P}/a/{name}.ok'): return cam,aud
    vs=[];as_=[]
    for k,(x,y) in enumerate(B['iv']):
        v=f'{P}/a/{name}_{k}.mkv';a=f'{P}/a/{name}_{k}.wav'
        sh(['ffmpeg','-v','error','-y','-ss',f'{x:.3f}','-i',f'{P}/cam.mp4','-t',f'{y-x:.3f}','-c:v','libx264','-preset','veryfast','-crf','12','-pix_fmt','yuv444p','-r','30',v])
        d=y-x
        sh(['ffmpeg','-v','error','-y','-ss',f'{x+0.025:.3f}','-i',f'{P}/aud.wav','-t',f'{d:.3f}','-af',f'afade=t=in:d=0.02,afade=t=out:st={d-0.02:.3f}:d=0.02,apad=whole_dur={d:.3f}','-ac','2','-ar','48000',a])
        vs.append(v);as_.append(a)
    open(f'{P}/a/{name}_v.txt','w').write(''.join(f"file '{v}'\n" for v in vs))
    open(f'{P}/a/{name}_a.txt','w').write(''.join(f"file '{a}'\n" for a in as_))
    sh(['ffmpeg','-v','error','-y','-f','concat','-safe','0','-i',f'{P}/a/{name}_v.txt','-c','copy',cam])
    sh(['ffmpeg','-v','error','-y','-f','concat','-safe','0','-i',f'{P}/a/{name}_a.txt','-c','copy',aud])
    open(f'{P}/a/{name}.ok','w').write('1')
    return cam,aud
def make_piece(name,cam,aud,c0,c1,states,out):
    """c0,c1 tempo compresso; states [(t0,t1,png)] in tempo compresso, copre c0..c1"""
    c0=fr(c0);c1=fr(c1);d=c1-c0
    lst=out+'.txt';L=[]
    for (a,b,png) in states:
        L.append(f"file '{png}'\nduration {fr(b)-fr(a):.5f}\n")
    L.append(f"file '{states[-1][2]}'\n")
    open(lst,'w').write(''.join(L))
    bg=out+'.bg.mkv';parts=[]
    for k,(a,b,png) in enumerate(states):
        dd=fr(b)-fr(a);pf=f'{out}.s{k}.mkv'
        r0=sh(['ffmpeg','-v','error','-y','-loop','1','-framerate','30','-i',png,'-t',f'{dd:.3f}','-vf','format=yuv420p','-c:v','libx264','-preset','ultrafast','-crf','16','-r','30',pf])
        if r0.returncode: raise SystemExit(r0.stderr[-800:])
        parts.append(pf)
    open(lst,'w').write(''.join(f"file '{x}'\n" for x in parts))
    r0=sh(['ffmpeg','-v','error','-y','-f','concat','-safe','0','-i',lst,'-c','copy',bg])
    if r0.returncode: raise SystemExit(r0.stderr[-800:])
    for x in parts: os.remove(x)
    fc='[1:v]format=rgba[c];[3:v]format=gray[m];[c][m]alphamerge[cm];[0:v][cm]overlay=1428:148:shortest=1,format=yuv420p[v]'
    r=sh(['ffmpeg','-v','error','-y','-i',bg,'-ss',f'{c0:.3f}','-t',f'{d:.3f}','-i',cam,
          '-ss',f'{c0:.3f}','-t',f'{d:.3f}','-i',aud,'-loop','1','-framerate','30','-t',f'{d:.3f}','-i',MASK,'-filter_complex',fc,'-map','[v]','-map','2:a',
          '-af',f'volume=3.3dB,apad=whole_dur={d:.3f}','-t',f'{d:.3f}','-r','30','-c:v','libx264','-preset','veryfast','-crf','14','-c:a','pcm_s16le','-ar','48000',out])
    os.remove(bg)
    if r.returncode: raise SystemExit(r.stderr[-800:])
    return d
