# Nucleo del montaggio: stati-immagine -> video, audio esatto, pezzi con fotogrammi forzati per le dissolvenze
import os, subprocess, json, hashlib, math, wave, shutil, sys
import numpy as np
from PIL import Image
sys.path.insert(0, '/tmp/w/build')
import lib
from lib import W, H

FPS = 30; TR = 12            # dissolvenza fra pezzi: 12 fotogrammi = 0,4 s
SR = 48000; SPF = SR // FPS  # campioni per fotogramma
WORK = '/tmp/w/build/work'; PIECES = '/tmp/w/build/pieces'
SRC = '/tmp/w/l6/LEZIONE 6 SIMBOLISMO E ART NOUVEAU.mp4'
KIT = '/home/user/Lezioni/kit'
for d in (WORK, PIECES): os.makedirs(d, exist_ok=True)

def sh(cmd, **kw):
    r = subprocess.run(cmd, capture_output=True, **kw)
    if r.returncode: raise RuntimeError(' '.join(map(str, cmd))[:300] + '\n' + r.stderr.decode()[-1500:])
    return r

def nfr(t): return int(round(t * FPS))

# ---------- audio ----------
def load_audio(path, ss=None, dur=None, af=None):
    cmd = ['ffmpeg', '-v', 'error']
    if ss is not None: cmd += ['-ss', '%.4f' % ss]
    if dur is not None: cmd += ['-t', '%.4f' % dur]
    cmd += ['-i', path, '-vn']
    if af: cmd += ['-af', af]
    cmd += ['-ac', '2', '-ar', str(SR), '-f', 'f32le', '-']
    x = np.frombuffer(sh(cmd).stdout, np.float32)
    return x.reshape(-1, 2).copy()

def fade(x, a_ms=30, b_ms=30):
    x = x.copy(); na = int(SR * a_ms / 1000); nb = int(SR * b_ms / 1000)
    if na and len(x) > na: x[:na] *= np.linspace(0, 1, na)[:, None]
    if nb and len(x) > nb: x[-nb:] *= np.linspace(1, 0, nb)[:, None]
    return x

def mix(n, parts):
    """parts: [(t_inizio_s, array(N,2), gain)] -> array (n*SPF,2)"""
    out = np.zeros((n * SPF, 2), np.float32)
    for t, a, g in parts:
        i = int(round(t * SR)); j = min(len(out), i + len(a))
        if i < 0: a = a[-i:]; i = 0
        if j > i: out[i:j] += a[:j - i] * g
    return out

def write_wav(path, x):
    x = np.clip(x, -1, 1); y = (x * 32767).astype('<i2')
    with wave.open(path, 'wb') as w:
        w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR); w.writeframes(y.tobytes())

def jingle(name):
    return load_audio(f'{KIT}/suoni/{name}.wav')

# ---------- stati -> sequenza di fotogrammi ----------
class Seq:
    """sequenza di stati (tempo s, immagine). Genera l'elenco concat con dissolvenze brevi fra stati."""
    def __init__(self, tag): self.tag = tag; self.states = []
    def add(self, t, im, fade_f=0): self.states.append((t, im, fade_f)); return self
    def build(self, n):
        d = f'{WORK}/{self.tag}'; shutil.rmtree(d, ignore_errors=True); os.makedirs(d)
        st = sorted(self.states, key=lambda s: s[0])
        idx = [min(n - 1, nfr(s[0])) for s in st]; idx[0] = 0
        seg = []                      # (png, nframes)
        cache = {}
        def png(im, key):
            p = f'{d}/{key}.png'
            if not os.path.exists(p): im.save(p, compress_level=1)
            return p
        for k, (t, im, ff) in enumerate(st):
            a = idx[k]; b = idx[k + 1] if k + 1 < len(st) else n
            if b <= a: continue
            ff = min(ff, b - a - 1)
            if k > 0 and ff > 0:
                prev = st[k - 1][1]
                for j in range(ff):
                    seg.append((png(blend(prev, im, (j + 1) / (ff + 1)), f'b{k}_{j}'), 1))
            seg.append((png(im, f's{k}'), b - a - max(ff if k > 0 else 0, 0)))
        lst = f'{d}/list.txt'
        with open(lst, 'w') as f:
            for p, c in seg: f.write(f"file '{p}'\nduration {c / FPS:.6f}\n")
            f.write(f"file '{seg[-1][0]}'\n")
        assert sum(c for p, c in seg) == n, (sum(c for p, c in seg), n)
        return lst

def blend(a, b, k):
    A = np.asarray(a.convert('RGBA'), np.float32); B = np.asarray(b.convert('RGBA'), np.float32)
    return Image.fromarray(np.clip(A * (1 - k) + B * k, 0, 255).astype(np.uint8), 'RGBA').convert('RGB') if a.mode == 'RGB' else Image.fromarray(np.clip(A * (1 - k) + B * k, 0, 255).astype(np.uint8), 'RGBA')

# ---------- sfondo blu animato (ciclo 6 s) ----------
def dark_loop():
    p = f'{WORK}/darkloop.mp4'
    if os.path.exists(p): return p
    d = f'{WORK}/dl'; os.makedirs(d, exist_ok=True)
    for i in range(180):
        lib.dark_frame(i / 30.0).convert('RGB').save(f'{d}/{i:03d}.png', compress_level=1)
    sh(['ffmpeg', '-y', '-v', 'error', '-framerate', '30', '-i', f'{d}/%03d.png', '-c:v', 'libx264', '-crf', '12', '-preset', 'veryfast', '-pix_fmt', 'yuv420p', p])
    shutil.rmtree(d); return p

ENC = ['-c:v', 'libx264', '-preset', 'veryfast', '-crf', '19', '-bf', '0', '-g', '60', '-sc_threshold', '0', '-pix_fmt', 'yuv420p', '-r', '30']
def kf(n): return ','.join('%.4f' % (f / FPS) for f in (TR, n - TR) if f > 0)

def encode(inputs, graph, n, out, maps=('[v]',), crf='24'):
    enc = [crf if a == '19' else a for a in ENC]
    cmd = ['ffmpeg', '-y', '-v', 'error', '-threads', '3'] + inputs + ['-filter_complex', graph, '-map', maps[0], '-frames:v', str(n)] + enc + ['-force_key_frames', kf(n), '-an', out]
    sh(cmd)

def video_white(seq, n, out):
    lst = seq.build(n)
    encode(['-f', 'concat', '-safe', '0', '-i', lst], '[0:v]fps=30,format=yuv420p[v]', n, out)

def video_dark(seq, n, out):
    lst = seq.build(n); bg = dark_loop()
    encode(['-stream_loop', '-1', '-i', bg, '-f', 'concat', '-safe', '0', '-i', lst],
           '[0:v]format=rgba[b];[1:v]fps=30,format=rgba[o];[b][o]overlay=0:0:format=auto,format=yuv420p[v]', n, out, crf='24')

# ---- riquadro del prof 4:3 (412x309 a x=1428,y=148) ----
CAM_CROP = (183, 137, 862, 344)      # w,h,x,y nel video 1092x614 (misurato)
def cam_mask():
    p = f'{WORK}/cammask.png'
    if not os.path.exists(p):
        from PIL import ImageDraw
        m = Image.new('L', (412, 309), 0); ImageDraw.Draw(m).rounded_rectangle((0, 0, 411, 308), 16, fill=255); m.save(p)
    return p

def video_teacher(seq, n, t0, out):
    lst = seq.build(n); w, h, x, y = CAM_CROP
    g = (f'[0:v]fps=30,format=yuv420p[bg];'
         f'[1:v]fps=30,hqdn3d=4:4:8:8,crop={w}:{h}:{x}:{y},scale=412:309:flags=lanczos,unsharp=5:5:0.4:3:3:0.0,eq=contrast=1.04:saturation=1.05,format=rgba[c];'
         f'[2:v]format=gray[m];[c][m]alphamerge[cr];[bg][cr]overlay=1428:148,format=yuv420p[v]')
    encode(['-f', 'concat', '-safe', '0', '-i', lst, '-ss', '%.4f' % t0, '-t', '%.4f' % (n / FPS + 0.5), '-i', SRC, '-loop', '1', '-i', cam_mask()], g, n, out, crf='24')

# ---------- audio del prof (voce con timbro intatto: solo filtro dei bassi leggero e riduzione leggera del rumore) ----------
TEACH_AF = 'highpass=f=70,afftdn=nr=5:nf=-50'
TEACH_GAIN_DB = 5.0   # da -21,3 LUFS verso -16 (verificato poi sul totale)
def teacher_audio(t0, n):
    x = load_audio(SRC, ss=t0, dur=n / FPS + 0.2, af=TEACH_AF)
    x = x[:n * SPF] * (10 ** (TEACH_GAIN_DB / 20))
    if len(x) < n * SPF: x = np.vstack([x, np.zeros((n * SPF - len(x), 2), np.float32)])
    return x

def finish(name, n, vpath, audio):
    """salva il pezzo: video intermedio già codificato + wav esatto"""
    assert audio.shape[0] == n * SPF, (name, audio.shape[0], n * SPF)
    wp = f'{PIECES}/{name}.wav'; write_wav(wp, audio)
    meta = {'name': name, 'n': n, 'video': vpath, 'wav': wp}
    json.dump(meta, open(f'{PIECES}/{name}.json', 'w'))
    return meta
