# Montaggio dei pezzi del prof: slide di stato + riquadro 4:3 + audio pulito, tagli sulle pause
import sys, os, json, subprocess
sys.path.insert(0, '/home/user/w18')
from lib import *
from piano import *
from dati import ARGOMENTI, TITOLO
R = '/home/user/w18/'; OUT = R + 'b/'
SEG = json.load(open(R + 'trasc.json'))
PRE, POST, MAXPAUSA = 0.40, 0.45, 2.5

from pages import PG

def slide_img(sid, act, prof=True):
    p = OUT + f's_{sid}_{act}{"" if prof else "_np"}.png'
    if os.path.exists(p): return p
    if sid == 'COV':
        im = copertina(TITOLO, [t for _, t in ARGOMENTI], prof=prof, page=1)
    elif sid in TXT:
        a, tit, keys = TXT[sid]
        im = slide_testo(LAB[a], tit, [C[k] for k in keys], act if act is not None else -1, PG[sid])
    else:
        a, f, cr, kws = IMG[sid]
        src = Image.open(R + 'img/' + f).convert('RGB')
        if cr: src = src.crop((int(cr[0] * src.width), int(cr[1] * src.height), int(cr[2] * src.width), int(cr[3] * src.height)))
        im = slide_immagine(LAB[a], PG[sid], src, kws=kws)
    im.convert('RGB').save(p); return p

def intervalli(a, b):
    """parti da tenere (tempi originali): pause oltre 2,5 s accorciate a 1 s, taglio nelle pause"""
    segs = [s for s in SEG if s['fine'] > a and s['inizio'] < b]
    # primo e ultimo bordo
    prev_end = max([s['fine'] for s in SEG if s['fine'] <= segs[0]['inizio']] or [0])
    first = segs[0]['inizio']; last = segs[-1]['fine']
    nxt = min([s['inizio'] for s in SEG if s['inizio'] >= last] or [last + 5])
    gap0 = first - prev_end; gap1 = nxt - last
    s0 = first - min(PRE, max(0.12, gap0 * 0.45)); e0 = last + min(POST, max(0.12, gap1 * 0.45))
    out = []; cur = s0
    for i in range(len(segs) - 1):
        g = segs[i + 1]['inizio'] - segs[i]['fine']
        if g > MAXPAUSA:
            out.append((cur, segs[i]['fine'] + 0.5)); cur = segs[i + 1]['inizio'] - 0.5
    out.append((cur, e0))
    return out

def mappa_tempo(K):
    cum = [0]
    for s, e in K: cum.append(cum[-1] + (e - s))
    def f(t):
        for i, (s, e) in enumerate(K):
            if t < s: return cum[i]
            if t <= e: return cum[i] + (t - s)
        return cum[-1]
    return f, cum[-1]

def pezzo(pid, fade_in='white', fade_out='white', force=False):
    import shutil
    P = [p for p in PEZZI if p[0] == pid][0]; _, a, b, arg, st = P
    out = OUT + f'prof_{pid}.mp4'
    if os.path.exists(out) and not force: return out
    K = intervalli(a, b)
    snap = lambda x: round(x * 30) / 30
    CAMSW = 50.1; KK = []     # il riquadro della webcam nell'originale cambia posto a 50,1 s (copertina -> slide)
    for (s_, e_) in K:
        s_ = snap(s_); e_ = s_ + max(1, round((e_ - s_) * 30)) / 30
        if s_ < CAMSW < e_:
            m_ = snap(CAMSW); KK += [(s_, m_), (m_, e_)]
        else: KK.append((s_, e_))
    D = sum(e - s for s, e in KK)
    W_ = OUT + f'w_{pid}/'; shutil.rmtree(W_, ignore_errors=True); os.makedirs(W_)
    cl = []; al = []
    for i, (s, e) in enumerate(KK):
        cx, cy = (688, 451) if e <= CAMSW + 0.05 else (858, 338)
        c = W_ + f'c{i}.mp4'; w = W_ + f'a{i}.wav'
        subprocess.run(['ffmpeg', '-v', 'error', '-y', '-ss', f'{s:.4f}', '-i', R + 'orig.mp4', '-t', f'{e - s:.4f}', '-an',
                        '-vf', f'crop=184:138:{cx}:{cy},scale=412:309:flags=lanczos,eq=contrast=1.04:saturation=1.06:brightness=0.01,fps=30',
                        '-c:v', 'libx264', '-preset', 'ultrafast', '-crf', '12', '-pix_fmt', 'yuv444p', c], check=True)
        subprocess.run(['ffmpeg', '-v', 'error', '-y', '-ss', f'{s:.4f}', '-t', f'{e - s:.4f}', '-i', OUT + 'prof_16.wav', '-c:a', 'pcm_s16le', w], check=True)
        cl.append(c); al.append(w)
    open(W_ + 'c.txt', 'w').write(''.join(f"file '{x}'\n" for x in cl)); open(W_ + 'a.txt', 'w').write(''.join(f"file '{x}'\n" for x in al))
    subprocess.run(['ffmpeg', '-v', 'error', '-y', '-f', 'concat', '-safe', '0', '-i', W_ + 'c.txt', '-c', 'copy', W_ + 'cam.mp4'], check=True)
    subprocess.run(['ffmpeg', '-v', 'error', '-y', '-f', 'concat', '-safe', '0', '-i', W_ + 'a.txt', '-c', 'copy', W_ + 'aud.wav'], check=True)
    # tempo originale -> tempo del pezzo
    cum = [0]
    for s_, e_ in KK: cum.append(cum[-1] + (e_ - s_))
    def f(t):
        for i, (s_, e_) in enumerate(KK):
            if t < s_: return cum[i]
            if t <= e_: return cum[i] + (t - s_)
        return cum[-1]
    lst = []; nt = [f(t) for t, _, _ in st] + [D]; nt[0] = 0.0
    for i, (t, sid, act) in enumerate(st):
        d = nt[i + 1] - nt[i]
        if d <= 0.001: continue
        lst.append((slide_img(sid, act), d))
    nf = [max(1, round(d * 30)) for _, d in lst]; nf[-1] += round(D * 30) - sum(nf)
    sc = []
    for i, ((p_, d_), n_) in enumerate(zip(lst, nf)):
        c_ = W_ + f's{i}.mp4'
        subprocess.run(['ffmpeg', '-v', 'error', '-y', '-loop', '1', '-framerate', '30', '-i', p_, '-frames:v', str(n_), '-vf', 'format=yuv420p',
                        '-c:v', 'libx264', '-preset', 'ultrafast', '-crf', '14', '-r', '30', c_], check=True)
        sc.append(c_)
    lf = W_ + 's.txt'; open(lf, 'w').write(''.join(f"file '{x}'\n" for x in sc))
    fc = ["[0:v]format=yuv420p[bg]", "[1:v]format=yuv420p[cam]", "[bg][cam]overlay=1428:148:shortest=1[o1]",
          f"[o1][3:v]overlay=1428:148:shortest=1,fade=t=in:st=0:d=0.3:color={fade_in},fade=t=out:st={D-0.3:.3f}:d=0.3:color={fade_out},format=yuv420p[vo]",
          f"[2:a]afade=t=in:st=0:d=0.03,afade=t=out:st={D-0.03:.3f}:d=0.03[ao]"]
    subprocess.run(['ffmpeg', '-v', 'error', '-y', '-f', 'concat', '-safe', '0', '-i', lf, '-i', W_ + 'cam.mp4', '-i', W_ + 'aud.wav',
                    '-loop', '1', '-framerate', '30', '-t', f'{D:.3f}', '-i', cornice_cam(), '-filter_complex', ';'.join(fc), '-map', '[vo]', '-map', '[ao]',
                    '-r', '30', '-c:v', 'libx264', '-preset', 'ultrafast', '-crf', '14', '-pix_fmt', 'yuv420p', '-c:a', 'aac', '-b:a', '256k', '-ar', '48000', '-ac', '2',
                    '-t', f'{D:.3f}', out], check=True)
    shutil.rmtree(W_, ignore_errors=True)
    return out

if __name__ == '__main__':
    for pid in sys.argv[1:]:
        print(pid, pezzo(pid, force=True))
