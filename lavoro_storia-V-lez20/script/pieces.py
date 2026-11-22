import os, subprocess, math, json
from PIL import Image
W = '/tmp/w'; B = '/tmp/w/b'
FPS = 30
KIT = '/home/user/Lezioni/kit'
PD = B + '/pieces'; os.makedirs(PD, exist_ok=True)
os.makedirs(B + '/blend', exist_ok=True)

def fr(t): return int(round(t * FPS))

class Piece:
    def __init__(self, name, states, audio=None, D=0.0, cam=None, lead=0.8, tail=0.5, trans=True, jingle=None, mixes=None, part=1, fixed_total=None, video_clip=None, fade_in=None, overlay=None):
        """states: [(t_piece, png)] in tempo del pezzo (che include lead). audio: wav del contenuto, messo a t=lead. D: durata contenuto.
        mixes: [(wav, t_piece, gain_db)] suoni extra (jingle). trans: mette trans.wav a t=0. video_clip: pezzo gia' video (sigle)."""
        self.name = name; self.states = sorted(states); self.audio = audio; self.D = D; self.cam = cam
        self.lead = lead; self.tail = tail; self.trans = trans; self.mixes = mixes or []; self.part = part
        self.video_clip = video_clip; self.fade_in = fade_in; self.overlay = overlay
        self.total = fixed_total or (fr(lead + D + tail) / FPS)
        self.nfr = fr(self.total)

def blend_frames(a_png, b_png, key, n=12):
    out = []
    A = Image.open(a_png).convert('RGB'); Bm = Image.open(b_png).convert('RGB')
    for k in range(n):
        f = f'{B}/blend/{key}_{k:02d}.png'
        if not os.path.exists(f):
            Image.blend(A, Bm, (k + 1) / (n + 1)).save(f)
        out.append(f)
    return out

def mask_png():
    f = B + '/assets/mask2.png'
    if not os.path.exists(f):
        from PIL import ImageDraw
        m = Image.new('L', (412, 310), 0); ImageDraw.Draw(m).rounded_rectangle((0, 0, 411, 308), 18, fill=255); m.save(f)
    return f

def mux(p, nxt, outfile, crf=19):
    """codifica il pezzo (video+audio). nxt: il pezzo seguente (per la dissolvenza in coda) o None"""
    if os.path.exists(outfile): return outfile
    T = p.total
    if p.video_clip:
        cmd = ['ffmpeg', '-v', 'error', '-y', '-i', p.video_clip]
        vf = '[0:v]fps=30,scale=1920:1080,format=yuv420p'
        if p.overlay:
            cmd += ['-i', p.overlay]; vf += '[b];[b][1:v]overlay=0:0,format=yuv420p'
        cmd += ['-filter_complex', vf + '[v];[0:a]aresample=48000,pan=stereo|c0=c0|c1=c1,apad,atrim=0:%.4f,asplit=2[a][a2]' % T,
                '-map', '[v]', '-map', '[a]', '-t', f'{T:.4f}', '-r', '30', '-c:v', 'libx264', '-preset', 'veryfast', '-crf', str(crf), '-pix_fmt', 'yuv420p', '-g', '60',
                '-c:a', 'aac', '-b:a', '192k', '-ar', '48000', '-ac', '2', outfile,
                '-map', '[a2]', '-t', f'{T:.4f}', '-c:a', 'pcm_s16le', outfile + '.wav']
        subprocess.run(cmd, check=True); return outfile
    states = list(p.states)
    # dissolvenza in coda verso il primo fotogramma del successivo
    tail_n = 12
    t_dis = T - tail_n / FPS
    if nxt is not None and nxt.states:
        bl = blend_frames(states[-1][1], nxt.states[0][1], p.name, tail_n)
        states = [s for s in states if s[0] < t_dis - 1e-6]
        for k, f in enumerate(bl): states.append((t_dis + k / FPS, f))
    # lista concat
    lst = f'{PD}/{p.name}.txt'
    with open(lst, 'w') as fh:
        for i, (t, png) in enumerate(states):
            t_next = states[i + 1][0] if i + 1 < len(states) else T
            n = max(1, fr(t_next) - fr(t))
            fh.write(f"file '{png}'\nduration {n / FPS:.5f}\n")
        fh.write(f"file '{states[-1][1]}'\n")
    cmd = ['ffmpeg', '-v', 'error', '-y', '-f', 'concat', '-safe', '0', '-i', lst]
    idx = 1
    fc = ["[0:v]fps=30,scale=1920:1080,format=yuv420p[bg]"]
    last = 'bg'
    if p.cam:
        cmd += ['-i', p.cam, '-loop', '1', '-i', mask_png()]
        fc.append(f"[{idx}:v]tpad=start_duration={p.lead}:start_mode=clone:stop_duration={p.tail + 1}:stop_mode=clone,format=yuva420p,"
                  f"fade=t=in:st=0:d=0.3:alpha=1[cv0]")
        fc.append(f"[{idx + 1}:v]format=gray[mk]")
        fc.append("[cv0][mk]alphamerge[cv1]")
        # dissolvenza in uscita della webcam
        fc.append(f"[cv1]fade=t=out:st={t_dis:.4f}:d={tail_n / FPS:.4f}:alpha=1[cv]")
        fc.append("[bg][cv]overlay=1428:148:shortest=0[vv]"); last = 'vv'
        idx += 2
    # audio
    ains = []
    afc = []
    if p.audio:
        cmd += ['-i', p.audio]; afc.append(f"[{idx}:a]adelay={int(p.lead * 1000)}|{int(p.lead * 1000)},apad[a{idx}]"); ains.append(f'[a{idx}]'); idx += 1
    ex = list(p.mixes)
    if p.trans: ex.append((KIT + '/suoni/trans.wav', 0.0, -3.0, 'duck'))
    for m in ex:
        wav, t0, g = m[0], m[1], m[2]
        cmd += ['-i', wav]
        extra = ''
        if len(m) > 3 and m[3] == 'duck': extra = ',afade=t=out:st=%.2f:d=0.6' % max(0.0, p.lead - 0.1)
        afc.append(f"[{idx}:a]aformat=sample_rates=48000:channel_layouts=stereo,volume={g}dB{extra},adelay={int(t0 * 1000)}|{int(t0 * 1000)},apad[a{idx}]"); ains.append(f'[a{idx}]'); idx += 1
    if not ains:
        afc.append(f"anullsrc=r=48000:cl=stereo[a0]"); ains = ['[a0]']
    afc.append(f"{''.join(ains)}amix=inputs={len(ains)}:normalize=0:duration=longest,atrim=0:{T:.4f},"
               f"afade=t=out:st={T - 0.06:.4f}:d=0.06,aresample=48000[aopre];[aopre]asplit=2[aout][aout2]")
    fc.append(f"[{last}]" + (f"fade=t=in:st=0:d=0.4:color={p.fade_in}" if p.fade_in else "fade=t=in:st=0:d=0.001") + "[vfin]")
    FCG = ';'.join(fc + afc)
    cmd += ['-filter_complex', FCG, '-map', '[vfin]', '-map', '[aout]', '-t', f'{T:.4f}', '-r', '30',
            '-c:v', 'libx264', '-preset', 'veryfast', '-crf', str(crf), '-pix_fmt', 'yuv420p', '-g', '60',
            '-c:a', 'aac', '-b:a', '192k', '-ar', '48000', '-ac', '2', outfile]
    cmd += ['-map', '[aout2]', '-t', f'{T:.4f}', '-c:a', 'pcm_s16le', '-ar', '48000', '-ac', '2', outfile + '.wav']
    subprocess.run(cmd, check=True)
    return outfile
