# Libreria di montaggio · Storia V lez. 3 (frame-per-frame in Python, una sola codifica x264)
import os, json, subprocess, re, wave, math, io
import numpy as np
from PIL import Image
W, H, FPS, SR = 1920, 1080, 30, 48000
SPF = SR // FPS  # 1600 campioni per fotogramma
FONTS = '/root/.fonts'
CHROME = '/opt/pw-browsers/chromium-1243/chrome-linux64/chrome'
KIT = '/home/user/Lezioni/kit'
CAM = dict(x=1428, y=148, w=412, h=309)  # riquadro 4:3 del prof

# ---------- rendering HTML -> array ----------
_pw = None; _br = None; _pg = None
def page():
    global _pw, _br, _pg
    if _pg is None:
        from playwright.sync_api import sync_playwright
        _pw = sync_playwright().start()
        _br = _pw.chromium.launch(executable_path=CHROME, args=['--no-sandbox'])
        _pg = _br.new_page(viewport={'width': W, 'height': H})
    return _pg
def shot(html):
    pg = page(); pg.set_content(html); pg.evaluate('document.fonts.ready')
    pg.wait_for_timeout(60)
    return np.asarray(Image.open(io.BytesIO(pg.screenshot(type='png'))).convert('RGB'))
def measure(html, js):
    pg = page(); pg.set_content(html); pg.evaluate('document.fonts.ready'); pg.wait_for_timeout(60)
    return pg.evaluate(js)

import base64 as _b64
def _ff(fam, wt, fn):
    return "@font-face{font-family:%s;font-weight:%d;src:url(data:font/ttf;base64,%s)}" % (fam, wt, _b64.b64encode(open(f'{FONTS}/{fn}', 'rb').read()).decode())
CSS = (_ff('Fig', 400, 'Figtree-Regular.ttf') + _ff('Fig', 500, 'Figtree-Medium.ttf') + _ff('Fig', 600, 'Figtree-SemiBold.ttf') +
       _ff('Fig', 700, 'Figtree-Bold.ttf') + _ff('Fig', 800, 'Figtree-ExtraBold.ttf') + _ff('Bri', 800, 'BricolageGrotesque-ExtraBold.ttf') +
       _ff('Bri', 700, 'BricolageGrotesque-Bold.ttf') +
       "*{box-sizing:border-box}html,body{margin:0;width:1920px;height:1080px;background:#fff;overflow:hidden;font-family:Fig;color:#0B1530}")

# ---------- audio ----------
def read_wav(p, mono=True):
    """legge un wav qualsiasi in float32 mono 48k (via ffmpeg)"""
    r = subprocess.run(['ffmpeg', '-v', 'error', '-i', p, '-f', 'f32le', '-ac', '1', '-ar', str(SR), '-'], capture_output=True)
    return np.frombuffer(r.stdout, dtype=np.float32).copy()
def dur(p):
    return float(subprocess.run(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', p], capture_output=True, text=True).stdout)
def lufs_gain(x, target=-16.0):
    """guadagno (dB) per portare il parlato a target LUFS (ebur128 via ffmpeg)"""
    p = subprocess.run(['ffmpeg', '-v', 'info', '-f', 'f32le', '-ar', str(SR), '-ac', '1', '-i', '-', '-af', 'ebur128=framelog=quiet', '-f', 'null', '-'],
                       input=x.tobytes(), capture_output=True)
    m = re.findall(r'I:\s+(-?[\d.]+) LUFS', p.stderr.decode())
    return target - float(m[-1]) if m else 0.0
def fade(x, a=0.03, b=0.03):
    x = x.copy(); na = int(a * SR); nb = int(b * SR)
    if na: x[:na] *= np.linspace(0, 1, na, dtype=np.float32)
    if nb: x[-nb:] *= np.linspace(1, 0, nb, dtype=np.float32)
    return x

# ---------- segmenti ----------
class Seg:
    """un pezzo del video: n fotogrammi, audio mono di n*SPF campioni, funzione frame(i)."""
    name = ''
    def __init__(self, n, audio, frame, name='', first_word=None, last_word=None, kind=''):
        self.n = n; self.frame = frame; self.name = name; self.kind = kind
        a = np.zeros(n * SPF, np.float32); k = min(len(audio), len(a)); a[:k] = audio[:k]
        self.audio = a
        self.first_word = first_word  # secondi dentro il pezzo in cui comincia la voce (per il suono di transizione)
        self.last_word = last_word

def blend(a, b, t):
    if t <= 0: return a
    if t >= 1: return b
    return (a.astype(np.uint16) * int(256 * (1 - t)) + b.astype(np.uint16) * int(256 * t) >> 8).astype(np.uint8)

def states_frame(states, fade_s=0.25):
    """states: lista [(t_inizio_s, array)] ordinata. Dissolvenza di fade_s all'inizio di ogni stato."""
    ts = [s[0] for s in states]
    def f(i):
        t = i / FPS; k = 0
        for j, x in enumerate(ts):
            if t >= x - 1e-9: k = j
        if k == 0: return states[0][1]
        u = (t - ts[k]) / fade_s
        return blend(states[k - 1][1], states[k][1], u) if u < 1 else states[k][1]
    return f

ROUND = None
def cam_mask():
    global ROUND
    if ROUND is None:
        from PIL import ImageDraw
        m = Image.new('L', (CAM['w'] * 4, CAM['h'] * 4), 0)
        ImageDraw.Draw(m).rounded_rectangle([0, 0, CAM['w'] * 4 - 1, CAM['h'] * 4 - 1], radius=40, fill=255)
        ROUND = (np.asarray(m.resize((CAM['w'], CAM['h']), Image.LANCZOS)).astype(np.float32) / 255)[:, :, None]
    return ROUND

class CamReader:
    """legge i fotogrammi del riquadro 4:3 dal video originale (ranges: [(a,b)] in secondi sorgente)"""
    def __init__(self, src, ranges, crop='179:134:853:345'):
        self.src = src; self.ranges = ranges; self.crop = crop
    def frames(self):
        fs = CAM['w'] * CAM['h'] * 3
        for a, b in self.ranges:
            n = int(round((b - a) * FPS))
            cmd = ['ffmpeg', '-v', 'error', '-ss', f'{a:.3f}', '-t', f'{b - a + 0.1:.3f}', '-i', self.src, '-vf',
                   f'crop={self.crop},scale={CAM["w"]}:{CAM["h"]}:flags=lanczos,unsharp=5:5:0.6,eq=contrast=1.04:saturation=1.05,fps={FPS}',
                   '-frames:v', str(n), '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-']
            p = subprocess.Popen(cmd, stdout=subprocess.PIPE)
            got = 0
            while got < n:
                buf = p.stdout.read(fs)
                if len(buf) < fs: break
                got += 1
                yield np.frombuffer(buf, np.uint8).reshape(CAM['h'], CAM['w'], 3)
            p.stdout.close(); p.wait()
            last = None
            while got < n:  # sicurezza: se mancano fotogrammi ripete l'ultimo (pochi)
                got += 1; yield last if last is not None else np.zeros((CAM['h'], CAM['w'], 3), np.uint8)

def paste_cam(bg, cam):
    out = bg.copy(); y, x, h, w = CAM['y'], CAM['x'], CAM['h'], CAM['w']
    m = cam_mask(); reg = out[y:y + h, x:x + w].astype(np.float32)
    out[y:y + h, x:x + w] = (reg * (1 - m) + cam.astype(np.float32) * m).astype(np.uint8)
    return out

# ---------- assemblaggio di una Parte ----------
def softlimit(x, th=0.8):
    y = x.copy(); m = np.abs(y) > th
    y[m] = np.sign(y[m]) * (th + (0.89 - th) * np.tanh((np.abs(y[m]) - th) / (0.89 - th)))
    return y

def assemble(segs, out_mp4, trans_wav, crf=19, log=None, preview=False, target_lufs=-16.0):
    """segs: lista di Seg. Dissolvenza incrociata (0,3-0,5 s, nel silenzio) fra pezzi consecutivi con trans.wav sopra."""
    Ls = []
    for i in range(len(segs) - 1):
        a, b = segs[i], segs[i + 1]
        l = max(0.3, min(0.5, getattr(a, 'pad_tail', 0.7), getattr(b, 'pad_head', 0.7)))
        Ls.append(int(round(l * FPS)))
    starts = []; t = 0
    for i, s in enumerate(segs):
        starts.append(t); t += s.n - (Ls[i] if i < len(segs) - 1 else 0)
    total = t
    audio = np.zeros(total * SPF + SR, np.float32)
    trans = read_wav(trans_wav)
    marks = []
    for i, s in enumerate(segs):
        a0 = starts[i] * SPF
        audio[a0:a0 + len(s.audio)] += s.audio
        if i > 0:
            p = segs[i - 1]
            end_prev = starts[i - 1] * SPF + int((p.last_word if p.last_word is not None else p.n / FPS - 0.3) * SR)
            beg_next = a0 + int((s.first_word if s.first_word is not None else 0.3) * SR)
            ini = end_prev + int(0.06 * SR); fin = beg_next - int(0.06 * SR)
            ln = max(0, min(fin - ini, len(trans), int(1.3 * SR)))
            if ln > int(0.2 * SR):
                tr = fade(trans[:ln] * 0.5, 0.04, min(0.3, ln / SR / 2))
                audio[ini:ini + ln] += tr
    audio = audio[:total * SPF]
    g = lufs_gain(audio, target_lufs); g = max(-4.0, min(4.0, g))
    audio = softlimit(audio * (10 ** (g / 20)))
    wavp = out_mp4 + '.audio.wav'
    pcm = (np.clip(audio, -1, 1) * 32767).astype(np.int16)
    with wave.open(wavp, 'wb') as w:
        w.setnchannels(1); w.setsampwidth(2); w.setframerate(SR); w.writeframes(pcm.tobytes())
    enc = ['ffmpeg', '-v', 'error', '-y', '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-s', f'{W}x{H}', '-r', str(FPS), '-i', '-', '-i', wavp,
           '-c:v', 'libx264', '-preset', 'ultrafast' if preview else 'veryfast', '-crf', '30' if preview else str(crf), '-pix_fmt', 'yuv420p',
           '-c:a', 'aac', '-b:a', '192k', '-ar', '48000', '-ac', '2', '-shortest', '-movflags', '+faststart', out_mp4]
    pr = subprocess.Popen(enc, stdin=subprocess.PIPE)
    tail = None; written = 0
    for i, s in enumerate(segs):
        Lp = Ls[i - 1] if i > 0 else 0; Ln = Ls[i] if i < len(segs) - 1 else 0
        for k in range(s.n):
            fr = s.frame(k)
            if Lp and k < Lp: fr = blend(tail[k], fr, (k + 1) / (Lp + 1))
            if Ln and k >= s.n - Ln:
                if k == s.n - Ln: tail = []
                tail.append(fr.copy()); continue
            pr.stdin.write(np.ascontiguousarray(fr).tobytes()); written += 1
        if log and i % 2 == 0: print(f'pezzo {i + 1}/{len(segs)} {s.name} fotogrammi {written}/{total}', file=log, flush=True)
    pr.stdin.close(); pr.wait()
    os.remove(wavp)
    return dict(frames=written, expected=total, dur=total / FPS, starts=[x / FPS for x in starts], Ls=[l / FPS for l in Ls], gain_db=g)

# ---------- assemblaggio v2: clip per pezzo (in parallelo) + clip di dissolvenza + concat senza ricodifica ----------
import multiprocessing as _mp, hashlib, shutil
_SEGS = None
ENC_V = ['-c:v', 'libx264', '-preset', 'veryfast', '-crf', '20', '-pix_fmt', 'yuv420p', '-threads', '1', '-g', '60', '-bf', '2', '-r', str(FPS),
         '-x264-params', 'scenecut=0:keyint=60:min-keyint=30', '-video_track_timescale', '30000']
def _enc(path, pre=False):
    return subprocess.Popen(['ffmpeg', '-v', 'error', '-y', '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-s', f'{W}x{H}', '-r', str(FPS), '-i', '-'] +
                            (['-c:v', 'libx264', '-preset', 'ultrafast', '-crf', '30', '-pix_fmt', 'yuv420p', '-threads', '1', '-r', str(FPS), '-video_track_timescale', '30000'] if pre else ENC_V) + ['-an', path],
                            stdin=subprocess.PIPE)
def _work(a):
    i, path, Lp, Ln, pre = a
    s = _SEGS[i]; p = None; head = []; tail = []
    body = s.n - Lp - Ln
    if body > 0: p = _enc(path, pre)
    for k in range(s.n):
        fr = s.frame(k)
        if k < Lp: head.append(fr.copy())
        if k >= s.n - Ln: tail.append(fr.copy())
        if Lp <= k < s.n - Ln: p.stdin.write(np.ascontiguousarray(fr).tobytes())
    if p: p.stdin.close(); p.wait()
    np.savez_compressed(path + '.head.npz', a=np.stack(head) if head else np.zeros(1)); np.savez_compressed(path + '.tail.npz', a=np.stack(tail) if tail else np.zeros(1))
    return i

def assemble2(segs, out_mp4, trans_wav, workdir, workers=4, target_lufs=-16.0, log=None, preview=False, keys=None):
    global _SEGS
    os.makedirs(workdir, exist_ok=True)
    Ls = []
    for i in range(len(segs) - 1):
        a, b = segs[i], segs[i + 1]
        l = max(0.3, min(0.5, getattr(a, 'pad_tail', 0.7), getattr(b, 'pad_head', 0.7)))
        Ls.append(int(round(l * FPS)))
    starts = []; t = 0
    for i, s in enumerate(segs):
        starts.append(t); t += s.n - (Ls[i] if i < len(segs) - 1 else 0)
    total = t
    # audio
    audio = np.zeros(total * SPF + SR, np.float32); trans = read_wav(trans_wav)
    for i, s in enumerate(segs):
        a0 = starts[i] * SPF; audio[a0:a0 + len(s.audio)] += s.audio
        if i > 0:
            p = segs[i - 1]
            end_prev = starts[i - 1] * SPF + int((p.last_word if p.last_word is not None else p.n / FPS - 0.3) * SR)
            beg_next = a0 + int((s.first_word if s.first_word is not None else 0.3) * SR)
            ini = end_prev + int(0.06 * SR); fin_ = beg_next - int(0.06 * SR)
            ln = max(0, min(fin_ - ini, len(trans), int(1.3 * SR)))
            if ln > int(0.2 * SR):
                audio[ini:ini + ln] += fade(trans[:ln] * 0.5, 0.04, min(0.3, ln / SR / 2))
    audio = audio[:total * SPF]
    g = lufs_gain(audio, target_lufs); g = max(-4.0, min(4.0, g)); audio = softlimit(audio * (10 ** (g / 20)))
    wavp = f'{workdir}/audio.wav'
    with wave.open(wavp, 'wb') as w:
        w.setnchannels(1); w.setsampwidth(2); w.setframerate(SR); w.writeframes((np.clip(audio, -1, 1) * 32767).astype(np.int16).tobytes())
    # clip per pezzo (con cache: nome+n+hash audio)
    _SEGS = segs; jobs = []; paths = []
    for i, s in enumerate(segs):
        Lp = Ls[i - 1] if i > 0 else 0; Ln = Ls[i] if i < len(segs) - 1 else 0
        key = hashlib.md5((s.name + str(s.n) + str(Lp) + str(Ln) + hashlib.md5(s.audio.tobytes()).hexdigest() + 'crf20' + (keys[i] if keys else '') + getattr(s, 'key', '')).encode()).hexdigest()[:12]
        path = f'{workdir}/c_{i:03d}_{key}.mp4'; paths.append((path, Lp, Ln))
        if not os.path.exists(path + '.tail.npz'): jobs.append((i, path, Lp, Ln, preview))
    if log: print(f'{len(jobs)} pezzi da codificare su {len(segs)}', file=log, flush=True)
    ctx = _mp.get_context('fork')
    with ctx.Pool(workers) as pool:
        for k, _ in enumerate(pool.imap_unordered(_work, jobs)):
            if log: print(f'codificati {k + 1}/{len(jobs)}', file=log, flush=True)
    # dissolvenze
    lst = []
    for i, (path, Lp, Ln) in enumerate(paths):
        if segs[i].n - Lp - Ln > 0: lst.append(path)
        if i < len(segs) - 1:
            tp = f'{workdir}/x_{i:03d}_{os.path.basename(path)[-16:-4]}_{os.path.basename(paths[i + 1][0])[-16:-4]}.mp4'
            if not os.path.exists(tp):
                T = np.load(path + '.tail.npz')['a']; Hd = np.load(paths[i + 1][0] + '.head.npz')['a']; L = Ls[i]
                pr = _enc(tp, preview)
                for k in range(L): pr.stdin.write(np.ascontiguousarray(blend(T[k], Hd[k], (k + 1) / (L + 1))).tobytes())
                pr.stdin.close(); pr.wait()
            lst.append(tp)
    with open(f'{workdir}/list.txt', 'w') as f:
        for p in lst: f.write(f"file '{p}'\n")
    r = subprocess.run(['ffmpeg', '-v', 'error', '-y', '-f', 'concat', '-safe', '0', '-i', f'{workdir}/list.txt', '-i', wavp, '-map', '0:v', '-map', '1:a', '-c:v', 'copy',
                        '-c:a', 'aac', '-b:a', '192k', '-ar', '48000', '-ac', '2', '-shortest', '-movflags', '+faststart', out_mp4], capture_output=True, text=True)
    if r.returncode: print(r.stderr[-800:], file=log or sys.stderr)
    return dict(frames=total, expected=total, dur=total / FPS, starts=[x / FPS for x in starts], Ls=[l / FPS for l in Ls], gain_db=g)
