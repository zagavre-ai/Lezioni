# Motore di montaggio: pezzi intermedi (qualità alta) -> concat -> codifica finale. Tutto a 30 fps, 48 kHz.
import subprocess, os, json, math
SRC='/tmp/w/lez10/LEZIONE.10.LA.GERMANIA.DA.WEIMAR.AL.NAZISMO.mp4'
B='/tmp/w/build'
FPS=30
def sh(c,check=True,**k):
    r=subprocess.run(c,capture_output=True,text=True,**k)
    if check and r.returncode: raise SystemExit('ERRORE: '+' '.join(map(str,c))[:300]+'\n'+r.stderr[-1500:])
    return r
def fr(t): return round(t*FPS)/FPS
def dur(f): return float(sh(['ffprobe','-v','error','-show_entries','format=duration','-of','csv=p=0',f]).stdout)
# maschera angoli arrotondati per il riquadro 4:3 del prof (412x309, raggio 14)
def maschera():
    p=f'{B}/mask.png'
    if not os.path.exists(p):
        from PIL import Image,ImageDraw
        m=Image.new('L',(412*4,309*4),0);ImageDraw.Draw(m).rounded_rectangle((0,0,412*4-1,309*4-1),radius=14*4,fill=255);m.resize((412,309),Image.LANCZOS).convert('RGB').save(p)
    return p
AF_PROF="highpass=f=70,afftdn=nr=5:nf=-45:tn=0"   # pulizia leggera, nessun filtro che cambi il timbro
def slide_list(stati,tot_frames,path):
    """stati: [(frame_inizio, png)] ordinati; scrive lista concat con durate esatte"""
    with open(path,'w') as f:
        for i,(a,png) in enumerate(stati):
            b=stati[i+1][0] if i+1<len(stati) else tot_frames
            if b<=a: continue
            f.write(f"file '{png}'\nduration {(b-a)/FPS:.6f}\n")
        f.write(f"file '{stati[-1][1]}'\n")
def misura_gain(ranges,target=-16.0):
    base=max(0.0,ranges[0][0]-2.0);fc=[];a=[]
    for i,(s0,s1) in enumerate(ranges):
        fc.append(f"[0:a]atrim=start={s0-base:.5f}:end={s1-base:.5f},asetpts=PTS-STARTPTS,aresample=48000[a{i}]");a.append(f'[a{i}]')
    fc.append(''.join(a)+f"concat=n={len(ranges)}:v=0:a=1,{AF_PROF},ebur128[o]")
    r=sh(['ffmpeg','-v','info','-ss',f'{base:.3f}','-to',f'{ranges[-1][1]+1.0:.3f}','-i',SRC,'-filter_complex',';'.join(fc),'-map','[o]','-f','null','-'],check=False).stderr
    import re
    m=re.findall(r'I:\s+(-?[\d.]+) LUFS',r)
    return (target-float(m[-1])) if m else 0.0
def pezzo_prof(nome,ranges,stati_src,out,gain_db=0.0,cam=True,chunk=1500):
    """Audio (catena completa) in un solo passaggio; video a blocchi di ~50 s (memoria bassa); poi unione."""
    off=0;mp=[]
    for s0,s1 in ranges:
        n=round((s1-s0)*FPS);mp.append((s0,s1,off,n));off+=n
    tot=off
    def to_out(t):
        for s0,s1,o,n in mp:
            if t<=s0: return o
            if t<s1: return o+round((t-s0)*FPS)
        return tot
    st=[]
    for t,png in sorted(stati_src):
        f=to_out(t)
        if st and st[-1][0]==f: st[-1]=(f,png)
        else: st.append((f,png))
    if st[0][0]!=0: st.insert(0,(0,st[0][1]))
    base=max(0.0,mp[0][0]-2.0);end=mp[-1][1]+1.0
    # --- audio ---
    fa=[];a=[]
    for i,(s0,s1,o,n) in enumerate(mp):
        fa.append(f"[0:a]atrim=start={s0-base:.5f}:end={s1-base:.5f},asetpts=PTS-STARTPTS,aresample=48000[a{i}]");a.append(f'[a{i}]')
    fa.append(''.join(a)+f"concat=n={len(mp)}:v=0:a=1,{AF_PROF},volume={gain_db}dB,alimiter=limit=0.89[aud]")
    wav=f'{B}/{nome}_aud.wav'
    sh(['ffmpeg','-v','error','-y','-ss',f'{base:.3f}','-to',f'{end:.3f}','-i',SRC,'-vn','-filter_complex',';'.join(fa),'-map','[aud]','-c:a','pcm_s16le','-ar','48000',wav])
    # --- video a blocchi ---
    parts=[]
    for ci,f0 in enumerate(range(0,tot,chunk)):
        f1=min(tot,f0+chunk);cp=f'{B}/{nome}_v{ci:02d}.mkv';parts.append(cp)
        # intervalli sorgente dentro [f0,f1)
        sub=[]
        for s0,s1,o,n in mp:
            a0=max(f0,o);a1=min(f1,o+n)
            if a1>a0: sub.append((s0+(a0-o)/FPS,s0+(a1-o)/FPS,a0-f0,a1-a0))
        # stati nel blocco
        stc=[(max(0,f-f0),png) for f,png in st if f<f1]
        pre=[x for x in st if x[0]<=f0]
        stc=[(0,pre[-1][1] if pre else st[0][1])]+[(f-f0,png) for f,png in st if f0<f<f1]
        # slide del blocco: un segmento video statico per ogni stato (memoria bassa), poi unione
        segs=[];sf=[]
        for k,(fa_,png) in enumerate(stc):
            fb_=stc[k+1][0] if k+1<len(stc) else f1-f0
            if fb_<=fa_: continue
            sp=f'{B}/{nome}_s{ci:02d}_{k:03d}.mkv';sf.append(sp)
            sh(['ffmpeg','-v','error','-y','-loop','1','-framerate','30','-i',png,'-frames:v',str(fb_-fa_),'-vf','format=yuv420p','-c:v','libx264','-preset','ultrafast','-crf','8','-r','30','-an',sp])
        ls=f'{B}/{nome}_sl{ci:02d}.txt';open(ls,'w').write(''.join(f"file '{p}'\n" for p in sf))
        slv=f'{B}/{nome}_slv{ci:02d}.mkv'
        sh(['ffmpeg','-v','error','-y','-f','concat','-safe','0','-i',ls,'-c','copy',slv])
        for p in sf: os.remove(p)
        b0=max(0.0,sub[0][0]-2.0);fc=[];v=[]
        for i,(s0,s1,o,n) in enumerate(sub):
            fc.append(f"[0:v]trim=start={s0-b0:.5f}:end={s1-b0:.5f},setpts=PTS-STARTPTS,crop=184:138:877:343,fps=30[v{i}]");v.append(f'[v{i}]')
        fc.append(''.join(v)+f"concat=n={len(sub)}:v=1:a=0,scale=412:309:flags=lanczos,unsharp=5:5:0.6:5:5:0,format=rgb24[cam]")
        fc.append("[1:v]format=yuv420p[bg]")
        fc.append("[2:v]format=gray[m];[cam][m]alphamerge[camm]")
        fc.append("[bg][camm]overlay=1428:148:format=auto:shortest=1,format=yuv420p[vo]" if cam else "[bg]format=yuv420p[vo]")
        sh(['ffmpeg','-v','error','-y','-ss',f'{b0:.3f}','-to',f'{sub[-1][1]+1.0:.3f}','-i',SRC,'-i',slv,'-loop','1','-framerate','30','-t',f'{(f1-f0)/FPS:.3f}','-i',maschera(),'-filter_complex',';'.join(fc),'-map','[vo]','-frames:v',str(f1-f0),
            '-c:v','libx264','-preset','veryfast','-crf','14','-pix_fmt','yuv420p','-r','30','-an',cp])
        os.remove(slv)
    lv=f'{B}/{nome}_vlist.txt';open(lv,'w').write(''.join(f"file '{p}'\n" for p in parts))
    sh(['ffmpeg','-v','error','-y','-f','concat','-safe','0','-i',lv,'-i',wav,'-map','0:v','-map','1:a','-c:v','copy','-c:a','copy','-shortest',out])
    for p in parts+[wav]:
        try: os.remove(p)
        except OSError: pass
    return tot/FPS
