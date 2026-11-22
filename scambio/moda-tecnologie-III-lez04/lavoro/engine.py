# motore: pezzi della prof con pause accorciate, tondo ripulito, slide a card
import subprocess, json, os, numpy as np
SRC_CIRCLE=(809,436,30)   # cx,cy,r nel video sorgente 852x480
def audio16(src):
    return np.frombuffer(subprocess.run(['ffmpeg','-v','error','-i',src,'-ac','1','-ar','16000','-f','f32le','-'],capture_output=True).stdout,np.float32)
def silenzi(x,sr=16000,min_len=1.2):
    """tratti di vero silenzio (rumore di fondo) piu' lunghi di min_len secondi -> [(a,b)]"""
    h=int(0.01*sr); n=len(x)//h
    e=np.sqrt((x[:n*h].reshape(n,h)**2).mean(1))+1e-9
    db=20*np.log10(e); floor=np.percentile(db,8); thr=floor+7
    quiet=db<thr; out=[]; i=0
    while i<n:
        if quiet[i]:
            j=i
            while j<n and quiet[j]: j+=1
            if (j-i)*0.01>=min_len: out.append((i*0.01,j*0.01))
            i=j
        else: i+=1
    return out
def piano_tagli(sil, frasi_fine, t0, t1, tieni=0.3, tol=0.8):
    """pause > 1,2 s -> 0,6 s (0,3 + 0,3), SOLO se coincidono con un confine di frase.
    frasi_fine: lista tempi di fine frase (ASR). Restituisce intervalli da tenere [(a,b)] in [t0,t1]."""
    cut=[]
    for a,b in sil:
        if b<=t0 or a>=t1: continue
        if any(a-tol<=fe<=b+tol for fe in frasi_fine) and b-a>1.2:
            cut.append((a+tieni,b-tieni))
    keep=[];cur=t0
    for a,b in cut:
        if a>cur: keep.append((cur,a))
        cur=b
    keep.append((cur,t1))
    return keep
def mappa_t(keep,t):
    """tempo sorgente -> tempo di uscita"""
    o=0
    for a,b in keep:
        if t<a: return o
        if t<=b: return o+(t-a)
        o+=b-a
    return o
def clip_prof(src,keep,bg_list,out,dur_bg=None):
    """src: video prof; keep: intervalli; bg_list: file concat di PNG (sfondo slide) gia' sulla linea dei tempi di uscita"""
    cx,cy,r=SRC_CIRCLE
    D=300
    sel='+'.join(f'between(t,{a:.3f},{b:.3f})' for a,b in keep)
    tot=sum(b-a for a,b in keep)
    fc=(f"[1:v]select='{sel}',setpts=N/FRAME_RATE/TB,fps=30,crop={2*r}:{2*r}:{cx-r}:{cy-r},scale={D}:{D}:flags=lanczos,eq=contrast=1.06:saturation=1.1:brightness=0.01,"
        f"format=rgba[c0];[2:v]format=gray[m];[c0][m]alphamerge[c];"
        f"[0:v][c]overlay={1490}:{160}:format=auto,format=yuv420p[v];"
        f"[1:a]aselect='{sel}',asetpts=N/SR/TB,highpass=f=70,afftdn=nr=6:nf=-45[a]")
    subprocess.run(['ffmpeg','-v','error','-y','-i',bg_list,'-i',src,'-loop','1','-i','/home/claude/prod/mask300.png','-filter_complex',fc,'-map','[v]','-map','[a]','-t',f'{tot:.3f}',
        '-c:v','libx264','-preset','veryfast','-crf','19','-pix_fmt','yuv420p','-r','30','-c:a','aac','-b:a','192k','-ar','48000',out],check=True)
    return tot
