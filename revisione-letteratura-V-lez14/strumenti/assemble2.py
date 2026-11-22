import json,sys,os,subprocess,numpy as np,wave
P=int(sys.argv[1]);W=f'/tmp/w14/aq{P}';os.makedirs(W,exist_ok=True)
TL=json.load(open(f'/tmp/w14/tl{P}.json'));OLD=f'/tmp/w14/P{P}.mp4'
PLN=json.load(open(f'/tmp/w14/dq{P}/plan.json'))['plan']
TOT={1:90226,2:87491}[P]
MAPS={1:{'AN03','AN06','AN09','AN11','AN12'},2:{'AN02','AN04','AN06','AN08','AN10','AN12','AN13'}}[P]
R1='/tmp/w14/voci/scambio/letteratura-V-lez14/vox/R1.wav'
USE_R1=(P==2 and os.path.exists('/tmp/w14/R1_48k.wav'))
def sh(c):
    r=subprocess.run(c,capture_output=True,text=True)
    if r.returncode: print(' '.join(c)[:200],r.stderr[-400:]);raise SystemExit(1)
ENC=['-c:v','libx264','-preset','veryfast','-crf','19','-pix_fmt','yuv420p','-r','30','-an','-x264-params','keyint=60:scenecut=0','-threads','2']
# vecchi intervalli in frame
old=[];
for i,(n,a,d) in enumerate(TL):
    f0=round(a*30);f1=round((a+d)*30);old.append([n,f0,f1])
old[-1][2]=TOT
w=wave.open(f'/tmp/w14/asm{P}/old.wav');A=np.frombuffer(w.readframes(w.getnframes()),np.int16).reshape(-1,2);w.close()
w=wave.open('/tmp/w14/orig_clean.wav');C=np.frombuffer(w.readframes(w.getnframes()),np.int16);w.close()
seq=[];aud=[];newtl=[];cur=0;prev=None;prevf=None
def edge(f,which):
    png=f+f'.{which}.png'
    if os.path.exists(png): return png
    if which=='first': sh(['ffmpeg','-v','error','-y','-i',f,'-frames:v','1',png])
    else: sh(['ffmpeg','-v','error','-y','-sseof','-0.2','-i',f,'-update','1','-q:v','2',png])
    return png
import wave as _w
def _rd(f):
    w=_w.open(f);a=np.frombuffer(w.readframes(w.getnframes()),np.int16);ch=w.getnchannels();w.close()
    return a.reshape(-1,ch)
def _w48(src,dst):
    subprocess.run(['ffmpeg','-v','error','-y','-i',src,'-ar','48000','-ac','2','-c:a','pcm_s16le',dst],check=True)
for nm in ('trans','repaso'):
    _w48(f'/tmp/w14/kitprod/v1/home/claude/v5/snd/{nm}.wav',f'/tmp/w14/snd_{nm}.wav')
TRANS=_rd('/tmp/w14/snd_trans.wav').astype(float);REP=_rd('/tmp/w14/snd_repaso.wav').astype(float)
def mixjingle(g,kind,gapf):
    n=gapf*1600;j=(REP if kind=='S' else TRANS)[:n].copy()*(0.4 if kind=='S' else 2.0)
    f=min(len(j),int(0.25*48000));j[-f:]*=np.linspace(1,0,f)[:,None]
    out=g.astype(float).copy();out[:len(j)]+=j
    return np.clip(out,-32768,32767).astype(np.int16)
def addpiece(name,vfile,nfr,audio,gapf,gapaud,oldname,oldstart):
    global cur,prevf
    audio=np.clip(audio.astype(float)*(1.084 if oldname in PLN else 0.75),-32768,32767).astype(np.int16)
    gapaud=np.clip(gapaud.astype(float)*0.75,-32768,32767).astype(np.int16)
    if prevf is not None and gapf>0:
        a=edge(prevf,'last');b=edge(vfile,'first');o=f'{W}/dis_{len(seq)}.mp4';D=gapf/30
        sh(['ffmpeg','-v','error','-y','-loop','1','-framerate','30','-t',f'{D+0.1:.3f}','-i',a,'-loop','1','-framerate','30','-t',f'{D+0.1:.3f}','-i',b,'-filter_complex',f'[0][1]xfade=transition=fade:duration={D:.4f}:offset=0,format=yuv420p','-frames:v',str(gapf),*ENC,o])
        seq.append(o);cur+=gapf
        g=gapaud[:gapf*1600]
        kind='S' if (oldname[0]=='S' and oldname[1:].isdigit()) else ('Q' if (oldname[0]=='Q' and oldname[1:].isdigit()) else 'T')
        if len(g)<gapf*1600: g=np.pad(g,((0,gapf*1600-len(g)),(0,0)))
        if kind!='Q': g=mixjingle(g,kind,gapf)
        aud.append(g)
    newtl.append([oldname,round(cur/30,3),round(nfr/30,3),oldstart])
    seq.append(vfile);aud.append(audio[:nfr*1600] if len(audio)>=nfr*1600 else np.pad(audio,((0,nfr*1600-len(audio)),(0,0))));cur+=nfr;prevf=vfile
for i,(n,f0,f1) in enumerate(old):
    if n in MAPS:
        if USE_R1 and n=='AN13': pass
        else: continue
    pf1=old[i-1][2] if i>0 else f0
    gapf=f0-pf1;gapaud=A[pf1*1600:f0*1600]
    if n in PLN:
        p=PLN[n];vf=f'/tmp/w14/dq{P}/{n}.mp4';nf=p['nf']
        c0=int(round(p['s0']*48000));seg=C[c0:c0+nf*1600]
        if len(seg)<nf*1600: seg=np.pad(seg,(0,nf*1600-len(seg)))
        audio=np.stack([seg,seg],1);addpiece(n,vf,nf,audio,gapf,gapaud,n,TL[i][1])
    elif USE_R1 and n=='AN13':
        import wave as wv
        w2=wv.open('/tmp/w14/R1_48k.wav');R=np.frombuffer(w2.readframes(w2.getnframes()),np.int16).reshape(-1,2);w2.close()
        nf=int(np.ceil((len(R)/48000+1.0)*30));R=np.pad(R,((int(0.4*48000),0),(0,0)))
        vf=f'{W}/R1.mp4'
        if not os.path.exists(vf): sh(['ffmpeg','-v','error','-y','-loop','1','-framerate','30','-t',f'{nf/30:.3f}','-i','/tmp/w14/build/png/mappa_prof.png','-frames:v',str(nf),*ENC,vf])
        addpiece('R1',vf,nf,R,gapf,gapaud,'R1',0)
    else:
        newf=f'/tmp/w14/new{P}/{n}.mp4'
        if n.startswith('INTRO'): newf=f'/tmp/w14/new{P}/INTRO1_np.mp4'
        if os.path.exists(newf): vf=newf
        else:
            vf=f'{W}/{n}.mp4'
            if not os.path.exists(vf): sh(['ffmpeg','-v','error','-y','-ss',f'{f0/30:.5f}','-i',OLD,'-frames:v',str(f1-f0),*ENC,vf])
        addpiece(n,vf,f1-f0,A[f0*1600:f1*1600],gapf,gapaud,n,TL[i][1])
open(f'{W}/list.txt','w').write(''.join(f"file '{s}'\n" for s in seq))
sh(['ffmpeg','-v','error','-y','-f','concat','-safe','0','-i',f'{W}/list.txt','-c','copy',f'{W}/video.mp4'])
Af=np.concatenate(aud);open(f'{W}/new.raw','wb').write(Af.astype(np.int16).tobytes())
sh(['ffmpeg','-v','error','-y','-f','s16le','-ar','48000','-ac','2','-i',f'{W}/new.raw','-c:a','aac','-b:a','192k',f'{W}/audio.m4a'])
sh(['ffmpeg','-v','error','-y','-i',f'{W}/video.mp4','-i',f'{W}/audio.m4a','-c','copy','-movflags','+faststart',f'{W}/finale.mp4'])
json.dump({'tl':newtl,'frames':cur},open(f'{W}/tl_new.json','w'))
print('finale',cur,'fotogrammi',len(Af)/1600)
