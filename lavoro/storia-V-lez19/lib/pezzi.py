# Costruttori dei pezzi (tutti: 1920x1080, 30 fps, audio 48 kHz stereo) con ponte finale: ultimo fotogramma fermo 0,5 s + trans.wav; il pezzo dopo comincia con una dissolvenza di 0,4 s da quel fotogramma.
import os,subprocess,json,sys
sys.path.insert(0,'/home/claude/w19/lib')
from core import *
OUT=W+'/out';os.makedirs(OUT,exist_ok=True)
KIT='/home/user/Lezioni/kit'
BR=0.5   # ponte
def ff(args,log=None):
    r=subprocess.run(['ffmpeg','-v','error','-y']+args,capture_output=True,text=True)
    if r.returncode: raise SystemExit('ffmpeg rc=%s: '%r.returncode+r.stderr[-1500:])
def last_frame(mkv,png):
    ff(['-sseof','-0.1','-i',mkv,'-frames:v','1','-update','1',png])
def dur(f): return float(sh(['ffprobe','-v','error','-show_entries','format=duration','-of','csv=p=0',f]).stdout)
VENC=['-c:v','libx264','-preset','veryfast','-crf','14','-pix_fmt','yuv420p','-r','30']
AENC=['-c:a','pcm_s16le','-ar','48000','-ac','2']
def mask_png():
    p=W+'/lib/maschera.png'
    if not os.path.exists(p):
        from PIL import Image,ImageDraw
        w,h=412,309;im=Image.new('RGBA',(w,h),(255,255,255,255));d=ImageDraw.Draw(im)
        d.rounded_rectangle([0,0,w-1,h-1],radius=14,fill=(0,0,0,0));im.save(p)
    return p
def finish(inputs,fc,out,tot,prev,trans,vlabel='v',alabel='a',extra_audio=None):
    """aggiunge: ponte (fermo 0,5 s), dissolvenza dal pezzo precedente, trans.wav. Scrive un .mkv."""
    pass
def prof(pid,R,slides,prev=None,last=False):
    """R=intervalli dell'originale; slides=[(t_rel,png)] (png senza il riquadro del prof: ci sta il rettangolo grigio). Ritorna durata."""
    D=dur_r(R);tail=0 if last else BR
    out=f'{OUT}/{pid}.mkv'
    # slide: un clip denso per ogni stato (niente raffiche di fotogrammi), poi concatenati
    ss=sorted(slides);tot_fr=round((D+tail)*30);sv=f'{OUT}/{pid}.slides.txt';cl=[]
    for i,(t,p_) in enumerate(ss):
        f0=round(t*30);f1=round(ss[i+1][0]*30) if i+1<len(ss) else tot_fr+30
        n_=max(1,f1-f0);c=f'{OUT}/{pid}.s{i}.mkv'
        ff(['-loop','1','-framerate','30','-i',p_,'-frames:v',str(n_),'-vf','format=yuv420p','-c:v','libx264','-preset','ultrafast','-crf','8','-r','30','-an',c]);cl.append(c)
    with open(sv,'w') as f:
        for c in cl: f.write(f"file '{c}'\n")
    inp=['-f','concat','-safe','0','-i',sv]
    fc=[];n=len(R)
    for nm,src in (('v',W+'/orig.mp4'),('a',W+'/a/prof.wav')):
        with open(f'{OUT}/{pid}.{nm}list.txt','w') as f:
            f.write('ffconcat version 1.0\n')
            for x,y in R: f.write(f"file '{src}'\ninpoint {x:.3f}\noutpoint {y:.3f}\n")
        inp+=['-f','concat','-safe','0','-i',f'{OUT}/{pid}.{nm}list.txt']
    inp+=['-i',mask_png()]
    im=3  # indice maschera
    pv=None
    if prev: inp+=['-loop','1','-framerate','30','-t','0.6','-i',prev];pv=im+1
    inp+=['-i',KIT+'/suoni/trans.wav'];tr=(pv+1) if pv else im+1
    fc.append("[1:v]crop=185:139:876:343,scale=412:309:flags=lanczos,unsharp=5:5:0.7:5:5:0.0,eq=contrast=1.04:saturation=1.06:gamma=1.0,setsar=1,fps=30[cam0]")
    B_=[];acc=0
    for x,y in R[:-1]: acc+=y-x;B_.append(acc)
    if B_:
        ex="1"
        for t in B_: ex=f"min({ex},abs(t-{t:.3f})/0.02)"
        fc.append("[2:a]aformat=sample_rates=48000:channel_layouts=stereo,volume=eval=frame:volume='"+ex+"'[pa]")
    else: fc.append("[2:a]aformat=sample_rates=48000:channel_layouts=stereo[pa]")
    fc.append(f"[cam0]tpad=stop_mode=clone:stop_duration={tail+1:.2f}[cam]")
    fc.append("[0:v]setpts=PTS-STARTPTS,fps=30,format=yuv420p[bg]")
    fc.append("[bg][cam]overlay=1428:148:shortest=1[o1]")
    fc.append(f"[o1][{im}:v]overlay=1428:148[o2]")
    if pv:
        fc.append(f"[{pv}:v]format=rgba,fade=t=out:st=0:d=0.4:alpha=1[pf]")
        fc.append("[o2][pf]overlay=0:0:eof_action=pass[ov]")
    else: fc.append("[o2]null[ov]")
    fc.append(f"[pa]apad=pad_dur={tail+1}[pa2]")
    if not last: fc.append(f"[{tr}:a]atrim=0:1.2,adelay={int(D*1000)}|{int(D*1000)},volume=0.9[tt];[pa2][tt]amix=inputs=2:normalize=0:duration=first[ao]")
    else: fc.append("[pa2]anull[ao]")
    ff(inp+['-filter_complex',';'.join(fc),'-map','[ov]','-map','[ao]','-t',f'{D+tail:.3f}']+VENC+AENC+[out])
    for c in cl:
        try: os.remove(c)
        except: pass
    return D+tail
def scena(pid,video,eventi,prev=None,last=False,ad=None):
    """scena senza prof (video muto già reso): eventi audio = [(file wav, inizio s, dB)]. Durata = durata del video."""
    D=dur(video);tail=0 if last else BR
    inp=['-i',video];fc=[]
    k=1
    for f,t,g in eventi: inp+=['-i',f]
    pv=None
    if prev: inp+=['-loop','1','-framerate','30','-t','0.6','-i',prev];pv=1+len(eventi)
    inp+=['-i',KIT+'/suoni/trans.wav'];tr=(pv+1) if pv else 1+len(eventi)
    fc.append(f"[0:v]fps=30,format=yuv420p,tpad=stop_mode=clone:stop_duration={tail+1:.2f}[v0]")
    if pv:
        fc.append(f"[{pv}:v]format=rgba,fade=t=out:st=0:d=0.4:alpha=1[pf]");fc.append("[v0][pf]overlay=0:0:eof_action=pass[ov]")
    else: fc.append("[v0]null[ov]")
    ms=[]
    for i,(f,t,g) in enumerate(eventi):
        fc.append(f"[{1+i}:a]aformat=sample_rates=48000:channel_layouts=stereo,adelay={int(t*1000)}|{int(t*1000)},volume={g}dB[e{i}]");ms.append(f'[e{i}]')
    if not last:
        fc.append(f"[{tr}:a]atrim=0:1.2,adelay={int(D*1000)}|{int(D*1000)},volume=0.9[tt]");ms.append('[tt]')
    fc.append(''.join(ms)+f"amix=inputs={len(ms)}:normalize=0:duration=longest,apad=pad_dur=1[ao]")
    out=f'{OUT}/{pid}.mkv'
    ff(inp+['-filter_complex',';'.join(fc),'-map','[ov]','-map','[ao]','-t',f'{D+tail:.3f}']+VENC+AENC+[out])
    return D+tail
def clip(pid,mp4,prev=None,last=False):
    """clip esistente (sigla, sigla finale) con audio proprio"""
    D=dur(mp4);tail=0 if last else BR
    inp=['-i',mp4];fc=[]
    pv=None
    if prev: inp+=['-loop','1','-framerate','30','-t','0.6','-i',prev];pv=1
    inp+=['-i',KIT+'/suoni/trans.wav'];tr=(pv+1) if pv else 1
    fc.append(f"[0:v]fps=30,format=yuv420p,tpad=stop_mode=clone:stop_duration={tail+1:.2f}[v0]")
    if pv: fc.append(f"[{pv}:v]format=rgba,fade=t=out:st=0:d=0.4:alpha=1[pf]");fc.append("[v0][pf]overlay=0:0:eof_action=pass[ov]")
    else: fc.append("[v0]null[ov]")
    fc.append(f"[0:a]aformat=sample_rates=48000:channel_layouts=stereo,apad=pad_dur={tail+1}[a0]")
    if not last: fc.append(f"[{tr}:a]atrim=0:1.2,adelay={int(D*1000)}|{int(D*1000)},volume=0.9[tt];[a0][tt]amix=inputs=2:normalize=0:duration=first[ao]")
    else: fc.append("[a0]anull[ao]")
    out=f'{OUT}/{pid}.mkv'
    ff(inp+['-filter_complex',';'.join(fc),'-map','[ov]','-map','[ao]','-t',f'{D+tail:.3f}']+VENC+AENC+[out])
    return D+tail
