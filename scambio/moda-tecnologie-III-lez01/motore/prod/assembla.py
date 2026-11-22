# Assembla una Parte: dissolvenze tra le scene, audio mixato, una sola codifica (x264 veryfast CRF 19, AAC 192k 48 kHz)
import sys,subprocess,json,os,wave
import numpy as np
W,H,FPS=1920,1080,30;FS=W*H*3//2
SND='/home/user/lav/kit/home/claude/v5/snd/'
def info(p):
    r=subprocess.run(['ffprobe','-v','error','-select_streams','v:0','-show_entries','stream=nb_frames,duration','-show_entries','format=duration','-of','json',p],capture_output=True,text=True)
    j=json.loads(r.stdout);return float(j['format']['duration'])
def frames(p):
    c=['ffmpeg','-v','error','-i',p,'-vf',f'scale={W}:{H}:force_original_aspect_ratio=decrease,pad={W}:{H}:(ow-iw)/2:(oh-ih)/2:white,fps={FPS},format=yuv420p','-f','rawvideo','-']
    pr=subprocess.Popen(c,stdout=subprocess.PIPE,bufsize=FS*4)
    while True:
        b=pr.stdout.read(FS)
        if len(b)<FS:break
        yield np.frombuffer(b,dtype=np.uint8)
    pr.wait()
def n_frames(p):
    r=subprocess.run(['ffprobe','-v','error','-count_packets','-select_streams','v:0','-show_entries','stream=nb_read_packets','-of','csv=p=0',p],capture_output=True,text=True)
    return int(r.stdout.strip().split(',')[0])
def audio_di(p,sr=48000):
    b=subprocess.run(['ffmpeg','-v','error','-i',p,'-vn','-ac','2','-ar',str(sr),'-f','s16le','-'],capture_output=True).stdout
    return np.frombuffer(b,dtype=np.int16).reshape(-1,2).astype(np.float32)/32768
def assembla(clips,out_mp4,ov=0.4,crf=19,tmp='/tmp/parte_audio.wav',log=print):
    """clips=[dict(v=mp4, a=wav|None, trans=bool, nome=str)]; ritorna la timeline [(nome,inizio_s,durata_s)]"""
    ovf=int(round(ov*FPS));lens=[];N=[]
    for c in clips:
        n=n_frames(c['v']);N.append(n)
    starts=[];t=0
    for i,n in enumerate(N):
        starts.append(t);t+=n-(ovf if i<len(N)-1 else 0)
    tot_frames=t;dur=tot_frames/FPS
    # audio
    sr=48000;A=np.zeros((int((dur+2)*sr),2),dtype=np.float32)
    tr=audio_di(SND+'trans.wav')
    for i,c in enumerate(clips):
        a=audio_di(c['a'] if c.get('a') else c['v'])
        s0=int(starts[i]/FPS*sr)
        # dissolvenza audio ai bordi della scena (durata dell'overlap) solo dove si sovrappone
        n=len(a);f=int(ov*sr)
        if i>0:a[:f]*=np.linspace(0,1,f)[:,None]
        if i<len(clips)-1:a[-f:]*=np.linspace(1,0,f)[:,None]
        e=min(len(A),s0+n);A[s0:e]+=a[:e-s0]
        if c.get('trans',True) and i>0:
            s1=max(0,s0-int(0.3*sr));e1=min(len(A),s1+len(tr));A[s1:e1]+=tr[:e1-s1]
    A=np.clip(A[:int(dur*sr)],-1,1);w=wave.open(tmp,'wb');w.setnchannels(2);w.setsampwidth(2);w.setframerate(sr);w.writeframes((A*32767).astype(np.int16).tobytes());w.close()
    enc=subprocess.Popen(['ffmpeg','-v','error','-y','-f','rawvideo','-pix_fmt','yuv420p','-s',f'{W}x{H}','-r',str(FPS),'-i','-','-i',tmp,'-c:v','libx264','-preset','veryfast','-crf',str(crf),'-pix_fmt','yuv420p','-r',str(FPS),'-c:a','aac','-b:a','192k','-ar','48000','-movflags','+faststart','-frames:v',str(tot_frames),out_mp4],stdin=subprocess.PIPE)
    tail=[]  # ultimi ovf frame del clip precedente
    emesse=0
    for i,c in enumerate(clips):
        it=frames(c['v']);head=[];buf=[]
        k=0
        for fr in it:
            if i>0 and k<ovf:
                a=tail[k].astype(np.uint16);b=fr.astype(np.uint16);al=(k+1)/(ovf+1)
                enc.stdin.write(((a*(1-al)+b*al).astype(np.uint8)).tobytes());emesse+=1
            elif i<len(clips)-1 and k>=N[i]-ovf:
                buf.append(fr.copy())
            else:
                enc.stdin.write(fr.tobytes());emesse+=1
            k+=1
        tail=buf
        log(f'{i+1}/{len(clips)} {c.get("nome","")} frames {k}')
    # eventuali frame mancanti
    while emesse<tot_frames:
        enc.stdin.write(np.zeros(FS,dtype=np.uint8).tobytes() if False else (tail[-1] if tail else np.full(FS,255,dtype=np.uint8)).tobytes());emesse+=1
    enc.stdin.close();enc.wait()
    return [(c.get('nome',''),starts[i]/FPS,N[i]/FPS) for i,c in enumerate(clips)],dur
