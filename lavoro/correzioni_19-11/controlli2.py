# -*- coding: utf-8 -*-
# Controlli sul video finale di una Parte (correzioni 19/11). uso: python3 controlli2.py PARTE
import sys, os, json, subprocess, re, hashlib, random, zipfile, numpy as np
sys.path.insert(0, '/tmp/claude-0/l17')
from dati import PARTI, POFF
from PIL import Image, ImageDraw
P = int(sys.argv[1]); order = PARTI[P]; off = POFF[P]
WK = '/home/user/w/l17/work'; OUT = f'{WK}/out{P}'
B = '/home/user/w/b17'
V = f'{OUT}/Storia_Lez17_Parte{P}_1080p.mp4'
tl = json.load(open(f'{B}/timeline_Parte{P}.json')); NPC = {tl[i][0]: round((tl[i + 1][1] - tl[i][1]) * 30) + 12 for i in range(len(tl) - 1)}
ST = {}
for i, (nm, st) in enumerate(tl): ST[nm] = (st, (NPC[nm] if nm in NPC else None))
R = []
def say(*x):
    s = ' '.join(str(i) for i in x); print(s, flush=True); R.append(s)
def sh(c): return subprocess.run(c, capture_output=True, text=True)

j = json.loads(sh(['ffprobe', '-v', 'error', '-count_packets', '-select_streams', 'v:0', '-show_entries', 'stream=nb_read_packets,width,height,r_frame_rate:format=duration,size', '-of', 'json', V]).stdout)
dur = float(j['format']['duration']); fr = int(j['streams'][0]['nb_read_packets']); mb = int(j['format']['size']) / 1e6
say(f"[misurato] durata {int(dur // 60)}:{dur % 60:04.1f} ({dur:.1f} s) | fotogrammi {fr} (attesi {round(dur * 30)}) | peso {mb:.1f} MB | {j['streams'][0]['width']}x{j['streams'][0]['height']} {j['streams'][0]['r_frame_rate']}")
a = json.loads(sh(['ffprobe', '-v', 'error', '-select_streams', 'a:0', '-show_entries', 'stream=codec_name,sample_rate,duration', '-of', 'json', V]).stdout)['streams'][0]
say(f"[misurato] audio {a['codec_name']} {a['sample_rate']} Hz, durata audio {float(a['duration']):.2f} s (video {dur:.2f} s)")
h = hashlib.sha256(open(V, 'rb').read()).hexdigest(); say('[misurato] sha256', h)
r = sh(['ffmpeg', '-nostats', '-i', V, '-af', 'ebur128=peak=true', '-f', 'null', '-']).stderr
m = re.findall(r'\n\s+I:\s+(-?[\d\.]+) LUFS', r); p = re.findall(r'Peak:\s+(-?[\d\.]+) dBFS', r)
say(f"[misurato] LUFS integrato {m[-1] if m else '?'} | picco vero {p[-1] if p else '?'} dBTP")
def lufs_seg(a_, b_):
    r = sh(['ffmpeg', '-nostats', '-ss', str(a_), '-t', str(b_ - a_), '-i', V, '-af', 'ebur128', '-f', 'null', '-']).stderr
    m = re.findall(r'\n\s+I:\s+(-?[\d\.]+) LUFS', r); return float(m[-1]) if m else None
pr = [(nm, s) for nm, (s, n) in ST.items() if (nm.startswith('prof') or nm == 'intro') and n]
vals = [lufs_seg(s + 5, s + 125) for nm, s in pr[:4]]
say('[misurato] LUFS parlato del prof, campione su', len(vals), 'pezzi:', [round(x, 1) for x in vals if x is not None])
r = sh(['ffmpeg', '-nostats', '-i', V, '-af', 'silencedetect=n=-55dB:d=3', '-f', 'null', '-']).stderr
sil = re.findall(r'silence_start: ([\d\.]+)', r); sile = re.findall(r'silence_duration: ([\d\.]+)', r)
say('[misurato] silenzi > 3 s (-55 dB):', len(sil), [(round(float(a_)), round(float(b_), 1)) for a_, b_ in zip(sil, sile)])
fz = sh(['ffmpeg', '-nostats', '-i', V, '-vf', 'crop=412:310:1428:148,freezedetect=n=0.003:d=1.0', '-an', '-f', 'null', '-']).stderr
fs = [float(x) for x in re.findall(r'freeze_start: ([\d\.]+)', fz)]; fd = [float(x) for x in re.findall(r'freeze_duration: ([\d\.]+)', fz)]
profrange = [(s, s + n / 30) for nm, (s, n) in ST.items() if (nm.startswith('prof') or nm == 'intro') and n]
bad = [(round(a_, 1), round(b_, 1)) for a_, b_ in zip(fs, fd) if any(s <= a_ < e - 0.5 for s, e in profrange)]
say('[misurato] fermi del riquadro del prof >= 1 s dentro i pezzi del prof:', len(bad), bad[:10])
# scatto quiz
z = zipfile.ZipFile('/home/user/w/b04/Telesio_kit_produzione_v1.zip'); qn = [n for n in z.namelist() if n.endswith('snd/quiz.wav')][0]
open('/tmp/quiz_ref.wav', 'wb').write(z.read(qn))
SR = 8000
def rd(f, ss=None, d=None):
    c = ['ffmpeg', '-v', 'error'] + (['-ss', str(ss), '-t', str(d)] if ss is not None else []) + ['-i', f, '-ac', '1', '-ar', str(SR), '-f', 's16le', '-']
    return np.frombuffer(subprocess.run(c, capture_output=True).stdout, np.int16).astype(float)
ref = rd('/tmp/quiz_ref.wav')[:SR * 2]
for pos in range(1, len(order) + 1):
    g = pos + off; t = ST[f'quiz{g}'][0]; s = max(0, t - 1.5); x = rd(V, s, 5); c = np.correlate(x, ref, 'valid'); k = int(np.argmax(c)); sc = s + k / SR - (t + 0.5)
    say(f'[misurato] jingle quiz {g}: atteso {t + 0.5:.3f} trovato {s + k / SR:.3f} scarto {sc:+.3f} {"OK" if abs(sc) <= 0.05 else "DA CORREGGERE"}')
# slide: durata massima senza cambio, dai pezzi montati
say('\n## Slide ferme (misurato dal piano di montaggio dei pezzi, confermato dai fotogrammi ogni 30 s)')
mx_all = 0; rows = []
def runs_of(js):
    seq = json.load(open(js))['seq']; res = []; cur = None; acc = 0
    for sk, act, f in seq:
        key = tuple(sk)
        if key == cur: acc += f
        else:
            if cur is not None: res.append((cur, acc))
            cur = key; acc = f
    res.append((cur, acc)); return res
for nm in [x for x in ST if x == 'intro' or x.startswith('prof')]:
    if nm == 'intro': js = f'{WK}/pieces/P1_intro.mp4.json'
    else: g = int(nm[4:]); js = f'{WK}/pieces/P{P}_T{order[g - off - 1]}.mp4.json'
    if not os.path.exists(js): continue
    rr = runs_of(js); k, f = max(rr, key=lambda x: x[1]); mx_all = max(mx_all, f)
    rows.append((nm, len(rr), f / 30, k))
    say(f'| {nm} | slide diverse {len(rr)} | slide ferma piu\' lunga {f / 30:.0f} s ({f / 1800:.1f} min) | {k[0]} {k[1] if len(k) > 1 else ""} |')
say(f'[misurato] Parte {P}: slide ferma piu\' lunga {mx_all / 30:.0f} s = {mx_all / 1800:.2f} minuti (limite 3 minuti)')
say('\n| pezzo | minuto di inizio | durata (s) |\n|---|---|---|')
names = list(ST)
for i, nm in enumerate(names):
    s, n = ST[nm]; n = n if n else round(dur * 30 - s * 30)
    say(f'| {nm} | {int(s // 60)}:{s % 60:04.1f} | {n / 30:.1f} |')
open(f'{OUT}/controlli_P{P}.txt', 'w').write('\n'.join(R))
# un fotogramma ogni 30 s
n = int(dur // 30) + 1; cols = 6; w, hh = 320, 180; rows_ = (n + cols - 1) // cols
M = Image.new('RGB', (cols * w, rows_ * (hh + 16)), 'white'); dm = ImageDraw.Draw(M)
for i in range(n):
    t = min(i * 30 + 1, dur - 0.5); f = f'{OUT}/_m.png'
    subprocess.run(['ffmpeg', '-y', '-v', 'error', '-ss', f'{t:.1f}', '-i', V, '-frames:v', '1', '-vf', f'scale={w}:{hh}', f], check=True)
    x = (i % cols) * w; y = (i // cols) * (hh + 16); M.paste(Image.open(f).convert('RGB'), (x, y + 16)); dm.text((x + 4, y + 2), f'{int(t // 60)}:{int(t % 60):02d}', fill='black')
M.save(f'{OUT}/controllo_minuti_P{P}.jpg', quality=80)
print('fatto')
