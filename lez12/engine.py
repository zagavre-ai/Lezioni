# Motore ffmpeg: una "scena" = sfondo + livelli PNG (con dissolvenza) + webcam + audio, durata esatta in fotogrammi.
import subprocess, os, json, hashlib, numpy as np
FPS = 30
W = '/home/user/Lezioni/lavoro/'
B = W + 'build/'; os.makedirs(B, exist_ok=True)
K = '/home/user/Lezioni/kit/suoni/'
CAM = W + 'prep/cam.mp4'; PROF = W + 'prep/prof_clean.wav'
MASK = B + 'mask.png'
def snap(d): return round(d * FPS) / FPS
def run(c):
    r = subprocess.run(c, capture_output=True, text=True)
    if r.returncode: raise RuntimeError(' '.join(map(str, c))[:400] + '\n' + r.stderr[-1500:])
def dur(f): return float(subprocess.run(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', f], capture_output=True, text=True).stdout)
def mkmask():
    if os.path.exists(MASK): return
    from PIL import Image, ImageDraw
    m = Image.new('L', (412, 310), 0); d = ImageDraw.Draw(m); d.rounded_rectangle((0, 0, 411, 308), radius=18, fill=255); m.save(MASK)
def vox(name):
    for d in ('vox', 'vox_prov'):
        p = W + f'{d}/{name}.wav'
        if os.path.exists(p): return p
    raise FileNotFoundError(name)
def voice_span(wav):
    """inizio/fine del parlato (s) dentro il file."""
    x = np.frombuffer(subprocess.run(['ffmpeg', '-v', 'error', '-i', wav, '-ac', '1', '-ar', '8000', '-f', 's16le', '-'], capture_output=True).stdout, np.int16).astype(float)
    e = np.abs(x); th = max(300, e.max() * 0.04); i = np.where(e > th)[0]
    return (i[0] / 8000 - 0.03 if len(i) else 0.0), (i[-1] / 8000 + 0.05 if len(i) else len(x) / 8000)
def make(name, D, bg, states=(), cam=None, audio=(), dip=None, fin=0.35, fout=0.35, extra_vf=''):
    """states: [(png, t0, t1|None, opaque)]; cam: (ss, dur, at); audio: [(file, ss|None, d|None, at, gain_db)]"""
    mkmask(); D = snap(D); N = round(D * FPS)
    out = B + name + '.mov'
    spec = json.dumps([name, D, bg, [(s[0], s[1], s[2], s[3], os.path.getmtime(s[0])) for s in states], cam, [(a[0], a[1], a[2], a[3], a[4]) for a in audio]], default=str)
    h = hashlib.md5(spec.encode()).hexdigest()
    if os.path.exists(out + '.' + h): return out
    inp = []; fc = []; n = 0
    dipc = dip or ('white' if bg == 'white' else '0B1530')
    if bg == 'white': inp += ['-f', 'lavfi', '-i', f'color=c=white:s=1920x1080:r={FPS}:d={D}']
    else: inp += ['-f', 'lavfi', '-i', f'gradients=s=1920x1080:r={FPS}:c0=0B1530:c1=1D4A9A:c2=0B1530:x0=0:y0=0:x1=1920:y1=1080:speed=0.012:d={D}']
    cur = '[0:v]'; n = 1
    for k, (png, t0, t1, opq) in enumerate(states):
        e = D if t1 is None else min(D, t1)
        L = e - t0 + 0.3
        inp += ['-loop', '1', '-framerate', str(FPS), '-t', f'{L:.3f}', '-i', png]
        f = f'[{n}:v]format=rgba,fade=t=in:st=0:d=0.3:alpha=1'
        if t1 is not None and t1 < D: f += f',fade=t=out:st={e-t0:.3f}:d=0.3:alpha=1'
        fc.append(f + f',setpts=PTS+{t0:.3f}/TB[s{k}]')
        fc.append(f'{cur}[s{k}]overlay=0:0:eof_action=pass:format=auto[o{k}]'); cur = f'[o{k}]'; n += 1
    if cam:
        ss, cd, at = cam
        inp += ['-ss', f'{ss:.3f}', '-t', f'{cd:.3f}', '-i', CAM, '-i', MASK]
        pre = f'tpad=start_duration={at:.3f}:start_mode=clone,' if at > 0 else ''
        post = f'tpad=stop_duration={max(0, D-at-cd)+0.5:.3f}:stop_mode=clone,' if D - at - cd > 0 else ''
        fc.append(f'[{n}:v]{pre}{post}trim=0:{D:.3f},setpts=PTS-STARTPTS,format=yuva420p[c{n}]')
        fc.append(f'[{n+1}:v]format=gray[m]')
        fc.append(f'[c{n}][m]alphamerge[cm]'); fc.append(f'{cur}[cm]overlay=1428:148:eof_action=pass:format=auto[oc]'); cur = '[oc]'; n += 2
    fc.append(f'{cur}{extra_vf}fade=t=in:st=0:d={fin}:color={dipc},fade=t=out:st={D-fout:.3f}:d={fout}:color={dipc},format=yuv420p[v]')
    an = []
    for j, (f, ss, d, at, g) in enumerate(audio):
        inp += (['-ss', f'{ss:.3f}'] if ss is not None else []) + (['-t', f'{d:.3f}'] if d is not None else []) + ['-i', f]
        fo = (d if d is not None else dur(f)) - 0.03
        fc.append(f'[{n}:a]aresample=48000,aformat=channel_layouts=mono,afade=t=in:st=0:d=0.03,afade=t=out:st={max(0,fo):.3f}:d=0.03,volume={g}dB,adelay={int(at*1000)}:all=1[a{j}]'); an.append(f'[a{j}]'); n += 1
    if an: fc.append(''.join(an) + f'amix=inputs={len(an)}:normalize=0:duration=longest,pan=stereo|c0=0.7071*c0|c1=0.7071*c0,apad=whole_len={N*1600},atrim=end_sample={N*1600}[a]')
    else: fc.append(f'anullsrc=r=48000:cl=stereo,atrim=end_sample={N*1600}[a]')
    cmd = ['ffmpeg', '-y', '-v', 'error'] + inp + ['-filter_complex', ';'.join(fc), '-map', '[v]', '-map', '[a]', '-frames:v', str(N), '-r', str(FPS),
           '-c:v', 'libx264', '-preset', 'veryfast', '-crf', '14', '-pix_fmt', 'yuv420p', '-c:a', 'pcm_s16le', '-ar', '48000', out]
    run(cmd)
    for f in os.listdir(B):
        if f.startswith(name + '.mov.'): os.remove(B + f)
    open(out + '.' + h, 'w').write('1')
    return out
