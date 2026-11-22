import json, subprocess, os, numpy as np
W = '/tmp/w'
S = json.load(open(W + '/src/trasc.json'))
FPS = 30
CAMBOX = 'crop=184:138:863:343,scale=412:310:flags=lanczos,eq=contrast=1.04:saturation=1.06:brightness=0.01,format=yuv420p'

def seg_range(i0, i1):
    return S[i0]['inizio'], S[i1]['fine']

def intervals(i0, i1, maxgap=2.5, keep=0.5, head=0.15, tail=0.12):
    """intervalli [a,b] da tenere (tempo originale), accorciando le pause > maxgap a circa 2*keep (=1 s).
    Inizio 0,15 s prima della prima frase; fine 0,12 s dopo l'ultima."""
    a0 = max(0.0, S[i0]['inizio'] - head)
    out = []
    cur = a0
    for i in range(i0, i1):
        gap = S[i + 1]['inizio'] - S[i]['fine']
        if gap > maxgap:
            out.append([cur, S[i]['fine'] + keep]); cur = S[i + 1]['inizio'] - keep
    out.append([cur, S[i1]['fine'] + tail])
    # allinea alla griglia dei fotogrammi
    q = lambda t: round(t * FPS) / FPS
    out = [[q(a), q(b)] for a, b in out]
    return out

def mapper(iv):
    """tempo originale -> tempo nel pezzo (s)"""
    cum = 0.0; M = []
    for a, b in iv:
        M.append((a, b, cum)); cum += b - a
    def f(t):
        for a, b, c in M:
            if a - 1e-6 <= t <= b + 1e-6: return c + (t - a)
        # in un pezzo tagliato: porta al punto di taglio successivo
        for a, b, c in M:
            if t < a: return c
        return cum
    return f, cum

def build_chunk(name, i0, i1, outdir, **kw):
    """crea outdir/name.wav (stereo 48k pulito) e outdir/name_cam.mp4 (412x309, senza audio). Ritorna (durata, mapper, iv)"""
    os.makedirs(outdir, exist_ok=True)
    iv = intervals(i0, i1, **kw)
    f, dur = mapper(iv)
    # video
    fc = []; vin = ''
    for k, (a, b) in enumerate(iv):
        fc.append(f"[0:v]trim=start={a:.4f}:end={b:.4f},setpts=PTS-STARTPTS,{CAMBOX}[v{k}]"); vin += f'[v{k}]'
    fc.append(f"{vin}concat=n={len(iv)}:v=1:a=0[v]")
    open(f'{outdir}/{name}_fc.txt', 'w').write(';\n'.join(fc))
    subprocess.run(['ffmpeg', '-v', 'error', '-y', '-i', W + '/src/orig.mp4', '-filter_complex_script', f'{outdir}/{name}_fc.txt', '-map', '[v]',
                    '-r', '30', '-c:v', 'libx264', '-crf', '10', '-preset', 'veryfast', f'{outdir}/{name}_cam.mp4'], check=True)
    # audio: stesso taglio, dissolvenze 15 ms
    af = []; ain = ''
    for k, (a, b) in enumerate(iv):
        d = b - a
        af.append(f"[0:a]atrim=start={a:.4f}:end={b:.4f},asetpts=PTS-STARTPTS,afade=t=in:d=0.015,afade=t=out:st={d-0.015:.4f}:d=0.015[a{k}]"); ain += f'[a{k}]'
    af.append(f"{ain}concat=n={len(iv)}:v=0:a=1,pan=stereo|c0=c0|c1=c0[a]")
    open(f'{outdir}/{name}_af.txt', 'w').write(';\n'.join(af))
    subprocess.run(['ffmpeg', '-v', 'error', '-y', '-i', W + '/src/prof_clean.wav', '-filter_complex_script', f'{outdir}/{name}_af.txt', '-map', '[a]',
                    '-ar', '48000', f'{outdir}/{name}.wav'], check=True)
    return dur, f, iv
