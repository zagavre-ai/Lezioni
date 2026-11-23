# Utilità video/audio per i segmenti non-docente
import os, subprocess, json, wave, math
import numpy as np
from PIL import Image
OUT = '/tmp/claude-0/w/out/'
os.makedirs(OUT + 'seg', exist_ok=True)
FPS = 30; SR = 48000

class Enc:
    def __init__(self, path):
        self.p = subprocess.Popen(['ffmpeg', '-v', 'error', '-y', '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-s', '1920x1080', '-r', '30', '-i', '-',
                                   '-c:v', 'libx264', '-preset', 'veryfast', '-crf', '19', '-pix_fmt', 'yuv420p', '-an', path], stdin=subprocess.PIPE)
        self.n = 0; self._last = None; self._b = None
    def put(self, img, n=1):
        if img is not self._last:
            self._b = img.convert('RGB').tobytes(); self._last = img
        for _ in range(n): self.p.stdin.write(self._b)
        self.n += n
    def close(self):
        self.p.stdin.close(); self.p.wait(); return self.n

def load_wav(p):
    w = wave.open(p); a = np.frombuffer(w.readframes(w.getnframes()), np.int16).astype(np.float32) / 32768
    if w.getnchannels() == 2: a = a.reshape(-1, 2).mean(1)
    if w.getframerate() != SR:
        raise ValueError('sr %d %s' % (w.getframerate(), p))
    return a

def save_wav(p, a):
    w = wave.open(p, 'wb'); w.setnchannels(1); w.setsampwidth(2); w.setframerate(SR)
    w.writeframes((np.clip(a, -1, 1) * 32767).astype(np.int16).tobytes()); w.close()

def to48(src, dst):
    subprocess.run(['ffmpeg', '-v', 'error', '-y', '-i', src, '-vn', '-ac', '1', '-ar', '48000', '-c:a', 'pcm_s16le', dst], check=True)

def place(track, a, t, gain=1.0, fade_in=0.02, fade_out=0.03):
    """mette l'audio a (mono) nel buffer track a t secondi"""
    s = int(round(t * SR)); a = a.copy() * gain
    fi, fo = int(fade_in * SR), int(fade_out * SR)
    if fi and len(a) > fi: a[:fi] *= np.linspace(0, 1, fi)
    if fo and len(a) > fo: a[-fo:] *= np.linspace(1, 0, fo)
    e = min(len(track), s + len(a)); track[s:e] += a[:e - s]
    return track

JING = '/home/user/Lezioni/kit/suoni/'
_j = {}
def jingle(name):
    if name not in _j:
        d = OUT + 'jingle_' + name + '.wav'
        if not os.path.exists(d): to48(JING + name + '.wav', d)
        a = load_wav(d); pk = np.abs(a).max(); _j[name] = (a * (0.56 / pk)).astype(np.float32) if pk > 0 else a   # picco a -5 dBFS: i guadagni nelle schede sono relativi
    return _j[name]

def ease(x): x = min(1, max(0, x)); return x * x * (3 - 2 * x)

def finish(sid, frames_written, audio, meta):
    """salva wav (durata esatta = fotogrammi/30) e json del segmento"""
    n = frames_written * 1600
    if len(audio) < n: audio = np.concatenate([audio, np.zeros(n - len(audio), np.float32)])
    audio = audio[:n]
    save_wav(OUT + 'seg/%s.wav' % sid, audio)
    meta = dict(meta); meta.update(id=sid, frames=frames_written)
    json.dump(meta, open(OUT + 'seg/%s.json' % sid, 'w'), ensure_ascii=False, default=float)
    return meta
