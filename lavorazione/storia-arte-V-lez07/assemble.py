# Montaggio finale: segmenti video (copiati) + ponti con dissolvenza e trans.wav + audio unico a -16 LUFS
import sys, os, json, subprocess, math, shutil
sys.path.insert(0, '/tmp/claude-0/w/build')
import numpy as np
from PIL import Image
import vid
from vid import *
import pyloudnorm as pyln

SEG = OUT + 'seg/'; TEA = OUT + 'teacher/'
BR = 27   # frame del ponte (0,9 s)

def order():
    o = ['SIGLA', 'COVER']
    for i in range(1, 8):
        o += ['T%d' % i, 'D%d' % i, 'S%d' % i]
        if i == 2: o.append('M2')
        if i == 5: o.append('M5')
        o += ['P%d' % i, 'Q%d' % i]
    o += ['GL', 'RF', 'MF', 'VE', 'SIGLAF', 'CI', 'COMP']
    return o

def paths(sid):
    if sid.startswith('D'): n = sid[1:]; return TEA + 'T%s.mp4' % n, TEA + 'T%s.wav' % n
    return SEG + sid + '.mp4', SEG + sid + '.wav'

def frame_png(mp4, out, last=False):
    cmd = ['ffmpeg', '-v', 'error', '-y'] + (['-sseof', '-0.2'] if last else []) + ['-i', mp4, '-frames:v', '1' if not last else '1', '-update', '1', out]
    if last:   # ultimo fotogramma: prende tutto e tiene l'ultimo
        cmd = ['ffmpeg', '-v', 'error', '-y', '-sseof', '-0.15', '-i', mp4, '-update', '1', '-q:v', '1', out]
    subprocess.run(cmd, check=True)

def bridge(k, a, b, force=False):
    sid = 'BR%02d' % k; mp = SEG + sid + '.mp4'
    if os.path.exists(mp) and not force: return sid
    pa, pb = SEG + 'br_a.png', SEG + 'br_b.png'
    frame_png(paths(a)[0], pa, True); frame_png(paths(b)[0], pb)
    A = Image.open(pa).convert('RGB'); B = Image.open(pb).convert('RGB'); e = Enc(mp)
    for i in range(BR):
        x = ease((i + 1) / (BR + 1)); e.put(Image.blend(A, B, x))
    n = e.close(); assert n == BR
    j = vid.jingle('trans')[:int(0.9 * SR)].copy(); j[-int(0.35 * SR):] *= np.linspace(1, 0, int(0.35 * SR))
    tr = np.zeros(BR * 1600, np.float32); tr[:len(j)] += j * 0.9
    vid.save_wav(SEG + sid + '.wav', tr)
    return sid

def build(force_bridges=False):
    o = order(); seq = []
    for k, sid in enumerate(o):
        if k: seq.append(bridge(k, o[k - 1], sid, force_bridges))
        seq.append(sid)
    # durata e audio
    tl = []; t = 0; parts = []
    for sid in seq:
        mp, wv = paths(sid) if not sid.startswith('BR') else (SEG + sid + '.mp4', SEG + sid + '.wav')
        n = int(subprocess.run(['ffprobe', '-v', 'error', '-count_packets', '-select_streams', 'v:0', '-show_entries', 'stream=nb_read_packets', '-of', 'csv=p=0', mp], capture_output=True, text=True).stdout.strip())
        a = vid.load_wav(wv)
        if 0 < len(a) - n * 1600 <= 3200: a = a[:n * 1600]   # un fotogramma in meno a fine pezzo: si toglie l'ultimo fotogramma di audio (silenzio di taglio)
        assert len(a) == n * 1600, (sid, len(a), n * 1600)
        parts.append((sid, n, a, mp)); tl.append([sid, round(t / FPS, 3), round(n / FPS, 3)]); t += n
    return parts, tl

def mix(parts):
    # docente: un solo guadagno per portare il parlato a -16 LUFS ; il resto e' gia' normalizzato per voce
    meter = pyln.Meter(SR)
    teach = np.concatenate([a for sid, n, a, mp in parts if sid.startswith('D')])
    lt = meter.integrated_loudness(teach.astype(np.float64)); gt = 10 ** ((-16.0 - lt) / 20)
    out = []
    for sid, n, a, mp in parts:
        out.append((a * gt) if sid.startswith('D') else a)
    full = np.concatenate(out)
    l = meter.integrated_loudness(full.astype(np.float64)); g = 10 ** ((-16.0 - l) / 20); full = full * g   # il limitatore e' sotto
    # limitatore morbido sui rari picchi, poi controllo -16 LUFS e picco reale <= -1 dBTP
    from scipy.signal import resample_poly
    def limited(x):
        vid.save_wav(OUT + '_pre.wav', np.clip(x, -4, 4) if False else x)
        subprocess.run(['ffmpeg', '-v', 'error', '-y', '-i', OUT + '_pre.wav', '-af', 'alimiter=limit=0.84:attack=4:release=60:level=0', '-c:a', 'pcm_s16le', OUT + '_post.wav'], check=True)
        return vid.load_wav(OUT + '_post.wav')
    full = limited(full)
    for _ in range(3):
        l2 = meter.integrated_loudness(full.astype(np.float64))
        if abs(l2 + 16) < 0.15: break
        full = limited(full * 10 ** ((-16 - l2) / 20))
    tpk = np.abs(resample_poly(full, 4, 1)).max()
    if tpk > 10 ** (-1.2 / 20): full = full * (10 ** (-1.2 / 20) / tpk)
    l2 = meter.integrated_loudness(full.astype(np.float64)); tpk = np.abs(resample_poly(full, 4, 1)).max()
    return full.astype(np.float32), dict(lufs_docente_prima=round(lt, 2), guadagno_docente_db=round(20 * math.log10(gt), 2), lufs_finale=round(l2, 2), picco_vero_dbtp=round(20 * math.log10(tpk), 2))

def run(final_name):
    parts, tl = build()
    full, st = mix(parts)
    lst = OUT + 'concat.txt'
    with open(lst, 'w') as f:
        for sid, n, a, mp in parts: f.write("file '%s'\n" % mp)
    vid.save_wav(OUT + 'audio_finale.wav', full)
    subprocess.run(['ffmpeg', '-v', 'error', '-y', '-i', OUT + 'audio_finale.wav', '-c:a', 'aac', '-b:a', '192k', '-ar', '48000', '-ac', '2', OUT + 'audio_finale.m4a'], check=True)
    vo = OUT + 'video_senza_audio.mp4'
    subprocess.run(['ffmpeg', '-v', 'error', '-y', '-f', 'concat', '-safe', '0', '-i', lst, '-c', 'copy', vo], check=True)
    subprocess.run(['ffmpeg', '-v', 'error', '-y', '-i', vo, '-i', OUT + 'audio_finale.m4a', '-c', 'copy', '-map', '0:v', '-map', '1:a', '-movflags', '+faststart', '-shortest', OUT + final_name], check=True)
    json.dump(tl, open(OUT + 'timeline_Parte1.json', 'w'))
    json.dump(st, open(OUT + 'audio_stats.json', 'w'))
    print(st, 'durata', tl[-1][1] + tl[-1][2])

if __name__ == '__main__':
    run(sys.argv[1] if len(sys.argv) > 1 else 'Storia_arte_Lez7_Parte1_1080p.mp4')
