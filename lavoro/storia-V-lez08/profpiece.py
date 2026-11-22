#!/usr/bin/env python3
# Montaggio di un pezzo "docente + slide": audio e video dell'originale con gli stessi intervalli (griglia 1/30 s) -> sincronismo esatto.
import os, subprocess, json, wave, numpy as np
from PIL import Image, ImageDraw
ORIG='/tmp/w/mat/LEZIONE.8.IL.DOPOGUERRA.ITALIANO.E.IL.FASCISMO.1919-1925.mp4'
W='/tmp/w/work'; CACHE=W+'/cache'; os.makedirs(CACHE,exist_ok=True)
SW=48000
def orig_audio():
    p=CACHE+'/orig48.npy'
    if not os.path.exists(p):
        raw=subprocess.run(['ffmpeg','-v','error','-i',ORIG,'-vn','-ac','2','-ar','48000','-f','f32le','-'],capture_output=True).stdout
        np.save(p,np.frombuffer(raw,np.float32).reshape(-1,2))
    return np.load(p,mmap_mode='r')
def scrivi_wav(path,x):
    x=np.clip(x,-1,1); y=(x*32767).astype('<i2')
    with wave.open(path,'wb') as w: w.setnchannels(2); w.setsampwidth(2); w.setframerate(SW); w.writeframes(y.tobytes())
def maschera():
    """angoli: pixel della slide (bianco + ombra) fuori dal rettangolo arrotondato, opachi solo negli angoli"""
    p=CACHE+'/corner412.png'
    if not os.path.exists(p):
        import lib_slide as L
        base=L.cornice(pag=1,riquadro=True).convert('RGBA').crop((1428,148,1428+412,148+309))
        m=Image.new('L',(412*4,309*4),255); ImageDraw.Draw(m).rounded_rectangle((0,0,412*4-1,309*4-1),20*4,fill=0)
        a=m.resize((412,309),Image.LANCZOS); base.putalpha(a); base.save(p)
    return p
def audio_pezzo(iv,fade=0.012):
    A=orig_audio(); parts=[]
    nf=int(fade*SW)
    for a,b in iv:
        s=np.array(A[int(round(a*SW)):int(round(b*SW))]).copy()
        r=np.linspace(0,1,nf)[:,None]; s[:nf]*=r; s[-nf:]*=r[::-1]
        parts.append(s)
    return np.concatenate(parts)
def monta_prof(nome,iv,stati,out,fade_video=0.3):
    """iv: intervalli (s originali); stati: [(t_pezzo_inizio, png)], l'ultimo dura fino alla fine"""
    dur=sum(b-a for a,b in iv)
    wav=f'{CACHE}/{nome}.wav'; scrivi_wav(wav,audio_pezzo(iv))
    # elenco slide (concat demuxer)
    lst=f'{CACHE}/{nome}.txt'
    with open(lst,'w') as f:
        for k,(t,png) in enumerate(stati):
            t2=stati[k+1][0] if k+1<len(stati) else dur
            d=max(1/30,round((t2-t)*30)/30); f.write(f"file '{png}'\nduration {d:.4f}\n")
        f.write(f"file '{stati[-1][1]}'\n")
    S0=max(0.0,iv[0][0]-1.0); S0=round(S0*30)/30
    S0=max(0.0,iv[0][0]-1.0); S0=round(S0*30)/30
    sel='+'.join(f'between(t,{a-S0-0.004:.4f},{b-S0-0.004:.4f})' for a,b in iv)
    # passo 1: le slide diventano un vero flusso a 30 fps (a basso costo: immagini ferme), per non gonfiare la memoria
    sl=f'{CACHE}/{nome}_slide.mkv'
    r1=subprocess.run(['ffmpeg','-v','error','-y','-f','concat','-safe','0','-i',lst,'-vf','fps=30,format=yuv420p','-t',f'{dur:.4f}','-c:v','libx264','-preset','ultrafast','-crf','8','-g','30',sl],capture_output=True,text=True)
    if r1.returncode: raise SystemExit('slide: '+r1.stderr[-800:])
    flt=(f"[1:v]crop=185:139:'if(lt(t+{S0:.4f},1082.05),851,877)':'if(lt(t+{S0:.4f},1082.05),337,343)',select='{sel}',setpts=N/(30*TB),"
         f"scale=412:309:flags=lanczos,unsharp=5:5:0.7:5:5:0.0,eq=contrast=1.04:saturation=1.05,format=yuv420p[cam];"
         f"[0:v][cam]overlay=1428:148:format=yuv420[x1];[2:v]format=yuva420p[cn];[x1][cn]overlay=1428:148:format=yuv420,"
         f"fade=t=in:st=0:d={fade_video},fade=t=out:st={dur-fade_video:.3f}:d={fade_video}[v];"
         f"[3:a]highpass=f=70,afftdn=nr=6:nf=-55,afade=t=in:st=0:d=0.02[a]")
    cmd=['ffmpeg','-v','error','-y','-i',sl,'-ss',f'{S0:.4f}','-t',f'{iv[-1][1]-S0+1.0:.4f}','-i',ORIG,'-i',maschera(),'-i',wav,
         '-filter_complex',flt,'-map','[v]','-map','[a]','-t',f'{dur:.4f}','-r','30','-c:v','libx264','-preset','ultrafast','-crf','14','-pix_fmt','yuv420p','-c:a','pcm_s16le','-ar','48000',out]
    r=subprocess.run(cmd,capture_output=True,text=True)
    if r.returncode: raise SystemExit(r.stderr[-1500:])
    return dur
if __name__=='__main__':
    import sys
    sys.path.insert(0,os.path.dirname(__file__))
    from lib_slide import slide
    t=['Un Paese impoverito dal conflitto: al termine della Grande Guerra, l\'Italia si ritrova in una profonda crisi economica, caratterizzata da un altissimo deficit pubblico e da una violenta inflazione che dimezza il potere d\'acquisto dei salari.','Le pesanti conseguenze sociali: il drastico blocco delle commesse statali belliche costringe moltissime aziende alla chiusura improvvisa, provocando un\'ondata di disoccupazione che arriva a colpire oltre due milioni di persone.']
    slide('Il contesto del dopoguerra e la crisi del «Biennio rosso» (1919-1920)','01 · Il Biennio rosso',t,0,3).save(W+'/t_a.png')
    slide('Il contesto del dopoguerra e la crisi del «Biennio rosso» (1919-1920)','01 · Il Biennio rosso',t,1,3).save(W+'/t_b.png')
    iv=[[223.0,243.0]]
    d=monta_prof('prova',iv,[(0,W+'/t_a.png'),(10,W+'/t_b.png')],W+'/prova.mkv')
    print('ok',d)
