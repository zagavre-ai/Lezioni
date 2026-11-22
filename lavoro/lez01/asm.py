# Infrastruttura di montaggio: ogni pezzo = video muto (mp4 1920x1080 30 fps) + audio wav stereo 48 kHz, di durata esatta (N/30 s).
import os,sys,subprocess,json,math,wave,shutil
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from PIL import Image,ImageDraw
W,H,FPS=1920,1080,30
WK='/tmp/w/'
CL=WK+'clips/';ST=WK+'stati/';os.makedirs(CL,exist_ok=True);os.makedirs(ST,exist_ok=True)
SND='/home/user/Lezioni/kit/suoni/'
def sh(cmd,**k):
    r=subprocess.run(cmd,capture_output=True,text=True,**k)
    if r.returncode:raise RuntimeError(' '.join(map(str,cmd))[:300]+'\n'+r.stderr[-1500:])
    return r
def fr(d):return max(1,int(round(d*FPS)))
def snap(d):return fr(d)/FPS
def dur_wav(p):return float(sh(['ffprobe','-v','error','-show_entries','format=duration','-of','csv=p=0',p]).stdout)
ENC=['-c:v','libx264','-preset','veryfast','-crf','19','-g','60','-pix_fmt','yuv420p','-r','30','-an']
def _lista(states,name):
    """states: [(png_path,durata_s)] -> file lista concat con durate multiple di 1/30"""
    p=ST+name+'.txt';tot=0;n=0
    with open(p,'w') as f:
        for png,d in states:
            k=fr(d);n+=k;f.write(f"file '{png}'\nduration {k/FPS:.6f}\n")
        f.write(f"file '{states[-1][0]}'\n")
    return p,n
MASK=ST+'mask412.png'
def mask():
    if not os.path.exists(MASK):
        m=Image.new('L',(412,309),0);ImageDraw.Draw(m).rounded_rectangle((0,0,411,308),16,fill=255);m.save(MASK)
    return MASK
def fade_f(D,fi=0.35,fo=0.35):
    return f"fade=t=in:st=0:d={fi}:color=black,fade=t=out:st={D-fo:.4f}:d={fo}:color=black"
def video_stati(name,states,cam=None,bg=False,fade=(0.35,0.35)):
    """Rende il video muto del pezzo. cam=(t_orig_inizio) per sovrapporre il docente (cam.mp4); bg=True: stati RGBA sopra lo sfondo blu animato."""
    out=CL+name+'.mp4'
    lst,n=_lista(states,name);D=n/FPS
    ff=['ffmpeg','-v','error','-y']
    if bg:ff+=['-stream_loop','-1','-i',WK+'bg_blu.mp4']
    ff+=['-f','concat','-safe','0','-i',lst]
    if cam is not None:ff+=['-ss',f'{cam:.4f}','-t',f'{D:.4f}','-i',WK+'cam.mp4','-loop','1','-framerate','30','-i',mask()]
    fl=[]
    if bg:
        fl.append(f"[1:v]fps=30,format=rgba[s];[0:v]fps=30,format=yuv420p[b];[b][s]overlay=0:0:format=auto[v0]")
    else:
        fl.append(f"[0:v]fps=30,format=yuv420p[v0]")
    if cam is not None:
        ci=2 if bg else 1
        mi=ci+1
        fl[-1]=fl[-1].replace('[0:v]',f'[{0 if not bg else 1}:v]') if False else fl[-1]
        fl.append(f"[{ci}:v]fps=30,setpts=PTS-STARTPTS,format=yuv444p[c];[{mi}:v]format=gray[m];[c][m]alphamerge[cr];[v0][cr]overlay=1428:148:format=auto[v1]")
        last='v1'
    else:last='v0'
    ffx=f"[{last}]{fade_f(D,*fade) if fade else 'null'},format=yuv420p[v]"
    fl.append(ffx)
    ff+=['-filter_complex',';'.join(fl),'-map','[v]','-t',f'{D:.4f}']+ENC+[out]
    sh(ff)
    return out,D
def audio_pezzo(name,D,parts,fade_ms=30):
    """parts: [(wav_path, t_inizio_nel_pezzo, gain_db, taglio_inizio_s, taglio_durata_s|None, fade_in_ms)] -> wav stereo 48k di durata esatta D"""
    out=CL+name+'.wav';ins=[];fl=[]
    for i,pt in enumerate(parts):
        p,t0,g,ss,dd,fi=(list(pt)+[0,None,fade_ms])[:6] if len(pt)<6 else pt
        ins+=['-i',p]
        chain=f"[{i}:a]aformat=sample_rates=48000:channel_layouts=stereo"
        if ss or dd:chain+=f",atrim=start={ss}"+(f":duration={dd}" if dd else "")+",asetpts=PTS-STARTPTS"
        if g:chain+=f",volume={g}dB"
        if fi:chain+=f",afade=t=in:st=0:d={fi/1000}"
        chain+=f",adelay={int(t0*1000)}|{int(t0*1000)}[a{i}]"
        fl.append(chain)
    n=len(parts)
    if n==0:
        sh(['ffmpeg','-v','error','-y','-f','lavfi','-i','anullsrc=r=48000:cl=stereo','-t',f'{D:.4f}','-c:a','pcm_s16le',out]);return out
    mix=''.join(f'[a{i}]' for i in range(n))+f"amix=inputs={n}:normalize=0:duration=longest,apad,atrim=0:{D:.4f}[a]"
    fl.append(mix)
    sh(['ffmpeg','-v','error','-y']+ins+['-filter_complex',';'.join(fl),'-map','[a]','-ar','48000','-ac','2','-c:a','pcm_s16le',out])
    return out
def voce(nome,testo=None):
    """percorso della voce Kore se c'e', altrimenti voce provvisoria (silenzio, durata stimata dal testo). Ritorna (path, durata, provvisoria)."""
    real=f'/home/user/Lezioni/scambio_voci/vox/NC_{nome}.wav'
    if os.path.exists(real):return real,dur_wav(real),False
    p=WK+f'prov/NC_{nome}.wav'
    if not os.path.exists(p):
        os.makedirs(WK+'prov',exist_ok=True)
        n=len(testo.split());d=n*0.40+testo.count('.')*0.3+0.5
        sh(['ffmpeg','-v','error','-y','-f','lavfi','-i','anullsrc=r=48000:cl=stereo','-t',f'{d:.2f}','-c:a','pcm_s16le',p])
    return p,dur_wav(p),True
def concat_final(parts_v,parts_a,out_mp4,out_wav=None):
    """concatena i video (copia) e gli audio (wav), codifica AAC 192k a 48 kHz una volta sola e mux"""
    lv=WK+'concat_v.txt';la=WK+'concat_a.txt'
    open(lv,'w').write(''.join(f"file '{p}'\n" for p in parts_v))
    open(la,'w').write(''.join(f"file '{p}'\n" for p in parts_a))
    sh(['ffmpeg','-v','error','-y','-f','concat','-safe','0','-i',lv,'-f','concat','-safe','0','-i',la,'-c:v','copy','-c:a','aac','-b:a','192k','-ar','48000','-ac','2','-movflags','+faststart','-shortest',out_mp4])
