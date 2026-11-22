# clip.py: dal video della prof e dalla trascrizione ricava l'intervallo da tenere (pause oltre 1,2 s tra una frase e l'altra accorciate a 0,6 s),
# l'audio pulito e il tondo ritagliato, con i tagli sul passo di 1/30 s.
import json, re, subprocess, numpy as np, os, sys
SR=48000; FR=SR//30
def snap(t): return round(t*30)/30
def leggi_wav(p):
    a=subprocess.run(['ffmpeg','-v','error','-i',p,'-f','f32le','-ac','1','-ar',str(SR),'-'],capture_output=True,check=True).stdout
    return np.frombuffer(a,np.float32).copy()
def rms(x,a,b):
    s=x[int(a*SR):int(b*SR)]; return float(np.sqrt(np.mean(s**2))) if len(s) else 0.0
def intervalli(trasc, x, a, b, soglia_pausa=1.2, resta=0.6, rms_max=0.008):
    """ritorna lista di (inizio,fine) da tenere, tra a e b (secondi originali)"""
    S=[s for s in json.load(open(trasc)) if a-0.01<=s['inizio']<b]
    cut=[]  # (da,a) pezzi di pausa da togliere
    for p,q in zip(S,S[1:]):
        gap=q['inizio']-p['fine']
        if gap>soglia_pausa and re.search(r'[\.\?\!…]$',p['testo'].strip()):
            # tieni resta/2 dopo la fine e resta/2 prima dell'inizio; togli il centro se e' silenzio
            c0=p['fine']+resta/2; c1=q['inizio']-resta/2
            if c1-c0>0.2 and rms(x,c0,c1)<rms_max: cut.append((snap(c0),snap(c1)))
    keep=[];cur=snap(a)
    for c0,c1 in cut:
        keep.append((cur,c0)); cur=c1
    keep.append((cur,snap(b)))
    return [(s,e) for s,e in keep if e-s>1/30], cut
def mappa_tempi(keep):
    off=0;M=[]
    for s,e in keep: M.append((s,e,off)); off+=e-s
    return M, off
def orig2nuovo(M,t):
    for s,e,off in M:
        if s-1e-6<=t<=e+1e-6: return off+(t-s)
    # in un pezzo tagliato: porta al pezzo successivo
    for s,e,off in M:
        if t<s: return off
    return M[-1][2]+(M[-1][1]-M[-1][0])
def audio_taglio(x, keep, out_wav, fade=0.006):
    parts=[]
    for i,(s,e) in enumerate(keep):
        seg=x[int(round(s*SR)):int(round(e*SR))].copy()
        n=int(fade*SR)
        if i>0: seg[:n]*=np.linspace(0,1,n)
        if i<len(keep)-1: seg[-n:]*=np.linspace(1,0,n)
        parts.append(seg)
    y=np.concatenate(parts)
    import wave
    with wave.open(out_wav,'wb') as w:
        w.setnchannels(1);w.setsampwidth(2);w.setframerate(SR);w.writeframes((np.clip(y,-1,1)*32767).astype('<i2').tobytes())
    return len(y)/SR
def video_tondo(src, keep, out_mp4, cx=809.5, cy=437.5, r=31, lato=304):
    n=len(keep); half=int(r-1.5)  # un po' piu' piccolo del bordo per evitare l'alone
    x0=int(round(cx-half)); y0=int(round(cy-half)); w=2*half
    fl=f"[0:v]crop={w}:{w}:{x0}:{y0},scale={lato}:{lato}:flags=lanczos,unsharp=5:5:0.6,eq=contrast=1.06:saturation=1.08,format=yuv420p,split={n}"+''.join(f'[c{i}]' for i in range(n))+';'
    for i,(s,e) in enumerate(keep): fl+=f"[c{i}]trim=start={s:.4f}:end={e:.4f},setpts=PTS-STARTPTS[v{i}];"
    fl+=''.join(f'[v{i}]' for i in range(n))+f"concat=n={n}:v=1:a=0[out]"
    sc=out_mp4+'.filtro.txt'; open(sc,'w').write(fl)
    subprocess.run(['ffmpeg','-v','error','-y','-i',src,'-filter_complex_script',sc,'-map','[out]','-r','30','-c:v','libx264','-preset','veryfast','-crf','16','-pix_fmt','yuv420p',out_mp4],check=True)
