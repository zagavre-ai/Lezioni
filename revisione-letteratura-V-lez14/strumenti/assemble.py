import json,sys,os,subprocess,numpy as np,glob
P=int(sys.argv[1]);W=f'/tmp/w14/asm{P}';os.makedirs(W,exist_ok=True)
TL=json.load(open(f'/tmp/w14/tl{P}.json'));OLD=f'/tmp/w14/P{P}.mp4'
PL=json.load(open(f'/tmp/w14/d{P}/plan.json'))['plan']
TOT={1:90226,2:87491}[P]
def sh(c): 
    r=subprocess.run(c,capture_output=True,text=True)
    if r.returncode: print(' '.join(c)[:200],r.stderr[-400:]);raise SystemExit(1)
ENC=['-c:v','libx264','-preset','veryfast','-crf','19','-pix_fmt','yuv420p','-r','30','-an','-x264-params','keyint=60:scenecut=0','-threads','2']
pcs=[]
for i,(n,a,d) in enumerate(TL):
    f0=round(a*30);f1=round((a+d)*30)
    if n in PL: f0=PL[n]['f0'];f1=PL[n]['f1']
    pcs.append([n,f0,f1,round(a*30)])
pcs[-1][2]=TOT
# file video per pezzo
vf=[]
for n,f0,f1,f0old in pcs:
    out=f'{W}/{n}.mp4'
    new=f'/tmp/w14/new{P}/{n}.mp4'
    if os.path.exists(new): src=new
    elif n in PL: src=f'/tmp/w14/d{P}/{n}.mp4'
    else: src=None
    if src: 
        if not os.path.exists(out): os.symlink(src,out)
    elif not os.path.exists(out):
        sh(['ffmpeg','-v','error','-y','-ss',f'{f0/30:.5f}','-i',OLD,'-frames:v',str(f1-f0),*ENC,out])
    vf.append(out)
def edge(f,which):
    png=f+f'.{which}.png'
    if os.path.exists(png): return png
    if which=='first': sh(['ffmpeg','-v','error','-y','-i',f,'-frames:v','1',png])
    else:
        sh(['ffmpeg','-v','error','-y','-sseof','-0.2','-i',f,'-update','1','-q:v','2',png])
    return png
seq=[];cur=0;gaps=[]
for k,(n,f0,f1,f0old) in enumerate(pcs):
    if k>0:
        pf=pcs[k-1][2]
        g=f0-pf
        if g>0:
            hold=max(0,f0-f0old) if n in PL else 0   # frame tolti dalla ripetizione: tengo l'ultimo fotogramma
            hold=min(hold,g);dis=g-hold
            a=edge(vf[k-1],'last');b=edge(vf[k],'first')
            if hold:
                o=f'{W}/hold_{k}.mp4';sh(['ffmpeg','-v','error','-y','-loop','1','-framerate','30','-i',a,'-frames:v',str(hold),*ENC,o]);seq.append(o)
            if dis:
                o=f'{W}/dis_{k}.mp4';D=dis/30
                sh(['ffmpeg','-v','error','-y','-loop','1','-framerate','30','-t',f'{D+0.1:.3f}','-i',a,'-loop','1','-framerate','30','-t',f'{D+0.1:.3f}','-i',b,'-filter_complex',f'[0][1]xfade=transition=fade:duration={D:.4f}:offset=0,format=yuv420p','-frames:v',str(dis),*ENC,o]);seq.append(o)
            gaps.append((pf,f0,hold))
        elif g<0: raise Exception(f'sovrapposizione {n} {g}')
    seq.append(vf[k])
open(f'{W}/list.txt','w').write(''.join(f"file '{s}'\n" for s in seq))
sh(['ffmpeg','-v','error','-y','-f','concat','-safe','0','-i',f'{W}/list.txt','-c','copy',f'{W}/video.mp4'])
# audio
sh(['ffmpeg','-v','error','-y','-i',OLD,'-vn','-af','aresample=async=1:first_pts=0','-ac','2','-ar','48000','-c:a','pcm_s16le',f'{W}/old.wav'])
import wave
w=wave.open(f'{W}/old.wav');N=w.getnframes();A=np.frombuffer(w.readframes(N),np.int16).reshape(-1,2).copy();w.close()
w=wave.open('/tmp/w14/orig_clean.wav');C=np.frombuffer(w.readframes(w.getnframes()),np.int16);w.close()
OLDSTART={n:a for n,a,d in TL}
for n,p in PL.items():
    f0,f1,s0,tr=p['f0'],p['f1'],p['s0'],p['trim']
    a0=f0*1600;a1=f1*1600;c0=int(round(s0*48000))
    seg=C[c0:c0+(a1-a0)]
    if len(seg)<a1-a0: seg=np.pad(seg,(0,a1-a0-len(seg)))
    # silenzio nei frame tolti
    o0=round(OLDSTART[n]*30)*1600
    if o0<a0: A[o0:a0]=0
    A[a0:a1,0]=seg;A[a0:a1,1]=seg
A=A[:TOT*1600]
open(f'{W}/new.raw','wb').write(A.tobytes())
sh(['ffmpeg','-v','error','-y','-f','s16le','-ar','48000','-ac','2','-i',f'{W}/new.raw','-c:a','aac','-b:a','192k',f'{W}/audio.m4a'])
sh(['ffmpeg','-v','error','-y','-i',f'{W}/video.mp4','-i',f'{W}/audio.m4a','-c','copy','-movflags','+faststart',f'{W}/finale.mp4'])
print('finale',W+'/finale.mp4')
