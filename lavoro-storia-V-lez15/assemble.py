# -*- coding: utf-8 -*-
# Montaggio finale di una Parte: pezzi video + transizioni xfade 0,4 s + audio mixato; poi sottotitoli, schede, rapporto.
import sys, os, json, subprocess, re, math, shutil
import numpy as np
sys.path.insert(0, '/tmp/claude-0/l15')
from dati import *
from plan2 import ANCORE
W = '/tmp/claude-0/l15'
KIT = '/home/user/Lezioni/kit'
SND = W + '/kit/Telesio_kit_produzione_v1/home/claude/v5/snd'
XF = 12          # frame di dissolvenza (0,4 s)
SR = 48000

def sh(cmd, **k): return subprocess.run(cmd, check=True, **k)

def nframes(f):
    r = subprocess.run(['ffprobe', '-v', 'error', '-count_packets', '-select_streams', 'v:0', '-show_entries', 'stream=nb_read_packets', '-of', 'csv=p=0', f], capture_output=True, text=True)
    return int(r.stdout.strip().split(',')[0])

def wav48(src, out, loud=None):
    if os.path.exists(out): return out
    af = f'pan=stereo|c0=c0|c1=c0,loudnorm=I={loud}:TP=-1.5:LRA=7,' if loud else ''
    sh(['ffmpeg', '-y', '-v', 'error', '-i', src, '-af', af + 'aresample=48000', '-ac', '2', '-c:a', 'pcm_s16le', out])
    return out

def readwav(f):
    import wave
    w = wave.open(f); n = w.getnframes(); ch = w.getnchannels(); a = np.frombuffer(w.readframes(n), dtype=np.int16).astype(np.float32) / 32768
    a = a.reshape(-1, ch)
    if ch == 1: a = np.repeat(a, 2, axis=1)
    return a

class Timeline:
    def __init__(self): self.pieces = []; self.audio = []
    def add(self, name, path, audio=None, tag=None):
        n = nframes(path)
        start = 0 if not self.pieces else self.pieces[-1]['start'] + self.pieces[-1]['n'] - XF
        self.pieces.append(dict(name=name, path=path, n=n, start=start, audio=audio or [], tag=tag))
        return self.pieces[-1]
    def t0(self, p): return p['start'] / 30.0
    def total_frames(self): return self.pieces[-1]['start'] + self.pieces[-1]['n']

def build_video(T, out, tmp):
    os.makedirs(tmp, exist_ok=True)
    parts = []; P = T.pieces
    for i, p in enumerate(P):
        h = XF if i > 0 else 0; t = XF if i < len(P) - 1 else 0
        a = h / 30.0; d = (p['n'] - h - t) / 30.0
        body = f'{tmp}/b{i:03d}.mp4'
        if not os.path.exists(body):
            sh(['ffmpeg', '-y', '-v', 'error', '-ss', f'{a:.4f}', '-i', p['path'], '-frames:v', str(p['n'] - h - t), '-c', 'copy', '-avoid_negative_ts', 'make_zero', body])
        parts.append(body)
        if i < len(P) - 1:
            x = f'{tmp}/x{i:03d}.mp4'
            if not os.path.exists(x):
                A = P[i]; B = P[i + 1]
                sh(['ffmpeg', '-y', '-v', 'error', '-ss', f"{(A['n'] - XF) / 30.0:.4f}", '-i', A['path'], '-i', B['path'],
                    '-filter_complex', f'[0:v]trim=end_frame={XF},setpts=PTS-STARTPTS[a];[1:v]trim=end_frame={XF},setpts=PTS-STARTPTS[b];[a][b]xfade=transition=fade:duration={XF / 30.0:.4f}:offset=0,format=yuv420p[v]',
                    '-map', '[v]', '-frames:v', str(XF), '-c:v', 'libx264', '-preset', 'veryfast', '-crf', '21', '-r', '30', '-g', '60', '-pix_fmt', 'yuv420p', '-an', x])
            parts.append(x)
    with open(tmp + '/list.txt', 'w') as f:
        for p in parts: f.write(f"file '{p}'\n")
    sh(['ffmpeg', '-y', '-v', 'error', '-f', 'concat', '-safe', '0', '-i', tmp + '/list.txt', '-c', 'copy', out])

def mix_audio(T, out_wav, prof):
    total = int(round(T.total_frames() / 30.0 * SR))
    mix = np.zeros((total, 2), dtype=np.float32)
    for p in T.pieces:
        t0 = int(p['start'] / 30.0 * SR)
        for ev in p['audio']:
            off, kind, arg = ev[0], ev[1], ev[2]
            if kind == 'wav': a = readwav(arg)
            elif kind == 'prof':
                a = np.concatenate([np.repeat(prof[int(x * SR):int(y * SR), None], 2, axis=1) for x, y in arg])
            s = t0 + int(off * SR); e = min(total, s + len(a))
            mix[s:e] += a[:e - s]
    return mix
