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
def pezzo_prof(nome,ranges,stati_src,out,gain_db=0.0,cam=True):
    """ranges: [(s0,s1)] secondi sorgente (multipli di 1/30), nell'ordine; stati_src: [(t_sorgente, png)] cambi di slide in tempo sorgente"""
    # mappa tempo sorgente -> frame di uscita
    off=0;mp=[]
    for s0,s1 in ranges:
        n=round((s1-s0)*FPS);mp.append((s0,s1,off,n));off+=n
    tot=off
    def to_out(t):
        for s0,s1,o,n in mp:
            if t<=s0: return o
            if t<s1: return o+round((t-s0)*FPS)
        return tot
    st=[];
    for t,png in sorted(stati_src):
        f=to_out(t)
        if st and st[-1][0]==f: st[-1]=(f,png)
        else: st.append((f,png))
    if st[0][0]!=0: st.insert(0,(0,st[0][1]))
    lst=f'{B}/{nome}_slide.txt';slide_list(st,tot,lst)
    base=max(0.0,mp[0][0]-2.0)
    fc=[];v=[];a=[]
    for i,(s0,s1,o,n) in enumerate(mp):
        s0,s1=s0-base,s1-base
        fc.append(f"[0:v]trim=start={s0:.5f}:end={s1:.5f},setpts=PTS-STARTPTS,crop=184:138:877:343,fps=30[v{i}]")
        fc.append(f"[0:a]atrim=start={s0:.5f}:end={s1:.5f},asetpts=PTS-STARTPTS,aresample=48000[a{i}]")
        v.append(f'[v{i}]');a.append(f'[a{i}]')
    fc.append(''.join(v)+f"concat=n={len(mp)}:v=1:a=0,scale=412:309:flags=lanczos,unsharp=5:5:0.6:5:5:0,format=rgb24[cam]")
    fc.append(''.join(a)+f"concat=n={len(mp)}:v=0:a=1,{AF_PROF},volume={gain_db}dB,alimiter=limit=0.89[aud]")
    fc.append("[1:v]fps=30,format=rgb24[bg]")
    fc.append("[2:v]format=gray[m];[cam][m]alphamerge[camm]")
    fc.append("[bg][camm]overlay=1428:148:format=auto:shortest=1,format=yuv420p[vo]" if cam else "[bg]format=yuv420p[vo]")
    c=['ffmpeg','-v','error','-y','-ss',f'{base:.3f}','-to',f'{mp[-1][1]+1.0:.3f}','-i',SRC,'-f','concat','-safe','0','-i',lst,'-loop','1','-i',maschera(),'-filter_complex',';'.join(fc),'-map','[vo]','-map','[aud]','-frames:v',str(tot),
       '-c:v','libx264','-preset','veryfast','-crf','14','-pix_fmt','yuv420p','-r','30','-c:a','pcm_s16le','-ar','48000',out]
    sh(c);return tot/FPS
