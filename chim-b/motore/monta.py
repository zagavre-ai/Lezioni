# monta.py: produce i pezzi (video muto + audio wav) con fotogrammi = durata x 30 esatti.
import json, os, subprocess, wave, numpy as np, sys, shutil
sys.path.insert(0, os.path.dirname(__file__))
from render import render_scena
SR = 48000
SND = '/home/user/lav/kit_zip/home/claude/v5/snd'
def dur_wav(p):
    return float(subprocess.run(['ffprobe','-v','error','-show_entries','format=duration','-of','csv=p=0',p],capture_output=True,text=True).stdout)
def carica(p):
    a = subprocess.run(['ffmpeg','-v','error','-i',p,'-f','f32le','-ac','2','-ar',str(SR),'-'],capture_output=True,check=True).stdout
    return np.frombuffer(a, np.float32).reshape(-1,2).copy()
def salva(p, y):
    with wave.open(p,'wb') as w:
        w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR); w.writeframes((np.clip(y,-1,1)*32767).astype('<i2').tobytes())
def norm_voce(src, dst):
    # voce Kore: -16 LUFS, bordi con dissolvenza 20-40 ms (la dissolvenza vera la mette il mixer)
    if os.path.exists(dst): return dst
    subprocess.run(['ffmpeg','-v','error','-y','-i',src,'-ac','1','-ar','48000','-af','loudnorm=I=-16:TP=-1.5:LRA=11','-c:a','pcm_s16le',dst],check=True)
    return dst
def piano(durate, lead=1.0, gap=0.7):
    t = lead; st = []
    for d in durate:
        if d is None: st.append([round(t,3), 0.0]); continue
        st.append([round(t,3), d]); t += d + gap
    return st, t
def mix(durata, voci, jingles=(), gain_j=1.0):
    """voci=[(t, wav)], jingles=[(t, nome.wav, gain)] -> array stereo lungo durata s"""
    n = int(round(durata * SR)); y = np.zeros((n,2), np.float32)
    for t, p in voci:
        v = carica(p); k = int(0.03*SR)
        v[:k] *= np.linspace(0,1,k)[:,None]; v[-k:] *= np.linspace(1,0,k)[:,None]
        i = int(round(t*SR)); m = min(len(v), n-i)
        if m > 0: y[i:i+m] += v[:m]
    for t, nome, g in jingles:
        v = carica(f'{SND}/{nome}') * g; i = int(round(t*SR)); m = min(len(v), n-i)
        if m > 0: y[i:i+m] += v[:m]
    return y
def pezzo(out, html, dati, durata, voci=(), jingles=(), fps=30):
    """render della scena + audio; out = prefisso (scrive out.mp4 muto, out.wav)."""
    nfr = int(round(durata*fps)); durata = nfr/fps
    render_scena(html, dati, durata, out+'.mp4', fps)
    salva(out+'.wav', mix(durata, voci, jingles))
    return durata
