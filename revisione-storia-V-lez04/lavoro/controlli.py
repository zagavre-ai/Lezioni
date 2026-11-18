# -*- coding: utf-8 -*-
# Controlli sul video finale di una Parte. uso: python3 controlli.py <parte>   (scrive out/controlli_P<parte>.txt e out/foglio_P<parte>.png, controllo_minuti_P<parte>.jpg)
import sys, os, json, subprocess, re, hashlib, numpy as np
sys.path.insert(0, '/tmp/claude-0/w')
from dati import *
from PIL import Image, ImageDraw, ImageFont
W = '/tmp/claude-0/w'; OUT = W + '/out'
P = int(sys.argv[1]); off = POFF[P]; order = PARTI[P]
V = f'{OUT}/Storia_Lez4_Parte{P}_1080p.mp4'
TL = json.load(open(f'{OUT}/tl_P{P}.json'))['timeline']; ST = {n: (s, f / 30) for n, s, f in TL}
R = []
def say(*x):
    s = ' '.join(str(i) for i in x); print(s, flush=True); R.append(s)
def sh(c): return subprocess.run(c, capture_output=True, text=True)

# 1. misure base
j = json.loads(sh(['ffprobe', '-v', 'error', '-count_packets', '-select_streams', 'v:0', '-show_entries', 'stream=nb_read_packets,width,height,r_frame_rate:format=duration,size', '-of', 'json', V]).stdout)
dur = float(j['format']['duration']); fr = int(j['streams'][0]['nb_read_packets']); mb = int(j['format']['size']) / 1e6
say(f"[misurato] durata {int(dur // 60)}:{dur % 60:04.1f} ({dur:.1f} s) | fotogrammi {fr} (attesi {round(dur * 30)}) | peso {mb:.1f} MB | {j['streams'][0]['width']}x{j['streams'][0]['height']} {j['streams'][0]['r_frame_rate']}")
a = json.loads(sh(['ffprobe', '-v', 'error', '-select_streams', 'a:0', '-show_entries', 'stream=codec_name,sample_rate,duration', '-of', 'json', V]).stdout)['streams'][0]
say(f"[misurato] audio {a['codec_name']} {a['sample_rate']} Hz, durata audio {float(a['duration']):.2f} s (video {dur:.2f} s)")
h = hashlib.sha256(open(V, 'rb').read()).hexdigest(); say('[misurato] sha256', h)
# 2. loudness complessivo e picco
r = sh(['ffmpeg', '-nostats', '-i', V, '-af', 'ebur128=peak=true', '-f', 'null', '-']).stderr
m = re.findall(r'\n\s+I:\s+(-?[\d\.]+) LUFS', r); p = re.findall(r'Peak:\s+(-?[\d\.]+) dBFS', r)
say(f"[misurato] LUFS integrato {m[-1] if m else '?'} | picco vero {p[-1] if p else '?'} dBTP")
# 2b. LUFS del solo parlato del prof (pezzi prof)
def lufs_seg(a_, b_):
    r = sh(['ffmpeg', '-nostats', '-ss', str(a_), '-t', str(b_ - a_), '-i', V, '-af', 'ebur128', '-f', 'null', '-']).stderr
    m = re.findall(r'\n\s+I:\s+(-?[\d\.]+) LUFS', r); return float(m[-1]) if m else None
pr = [(n, s, d) for n, (s, d) in ST.items() if n.startswith('prof') or n == 'intro']
if pr:
    vals = [lufs_seg(s + 3, s + min(d, 120) - 3) for n, s, d in pr[:4]]
    say('[misurato] LUFS parlato del prof, campione su', len(vals), 'pezzi:', [round(x, 1) for x in vals if x is not None])
# 3. silenzi > 3 s
r = sh(['ffmpeg', '-nostats', '-i', V, '-af', 'silencedetect=n=-55dB:d=3', '-f', 'null', '-']).stderr
sil = re.findall(r'silence_start: ([\d\.]+)', r); sile = re.findall(r'silence_duration: ([\d\.]+)', r)
say('[misurato] silenzi > 3 s (-55 dB):', len(sil), [(round(float(a_)), round(float(b_), 1)) for a_, b_ in zip(sil, sile)])
# 4. fermi del prof: freezedetect sulla zona del riquadro, solo pezzi prof
fz = sh(['ffmpeg', '-nostats', '-i', V, '-vf', 'crop=412:310:1428:148,freezedetect=n=0.003:d=1.0', '-an', '-f', 'null', '-']).stderr
fs = [float(x) for x in re.findall(r'freeze_start: ([\d\.]+)', fz)]; fd = [float(x) for x in re.findall(r'freeze_duration: ([\d\.]+)', fz)]
profrange = [(s, s + d) for n, (s, d) in ST.items() if n.startswith('prof') or n == 'intro']
bad = [(round(a_, 1), round(b_, 1)) for a_, b_ in zip(fs, fd) if any(s <= a_ < e for s, e in profrange)]
say('[misurato] fermi del riquadro del prof >= 1 s dentro i pezzi del prof:', len(bad), bad[:10])
# 5. scatto dei quiz
SR = 8000
def rd(f, ss=None, d=None):
    c = ['ffmpeg', '-v', 'error'] + (['-ss', str(ss), '-t', str(d)] if ss is not None else []) + ['-i', f, '-ac', '1', '-ar', str(SR), '-f', 's16le', '-']
    return np.frombuffer(subprocess.run(c, capture_output=True).stdout, np.int16).astype(float)
ref = rd('/tmp/claude-0/w/kit/Telesio_kit_produzione_v1/home/claude/v5/snd/quiz.wav')[:SR * 2]; badq = 0
for pos in range(1, len(order) + 1):
    g = pos + off; t = ST[f'quiz{g}'][0]; s = max(0, t - 1.5); x = rd(V, s, 5); c = np.correlate(x, ref, 'valid'); k = int(np.argmax(c)); sc = s + k / SR - (t + 0.5)
    ok = abs(sc) <= 0.05; badq += (not ok); say(f'[misurato] jingle quiz {g}: atteso {t + 0.5:.3f} trovato {s + k / SR:.3f} scarto {sc:+.3f} {"OK" if ok else "DA CORREGGERE"}')
# 6. tabella pezzi (sezione C della scheda tecnica)
say('\n| pezzo | presente | minuto di inizio | durata misurata (s) |\n|---|---|---|---|')
for n, (s, d) in ST.items(): say(f'| {n} | sì | {int(s // 60)}:{s % 60:04.1f} | {d:.1f} |')
open(f'{OUT}/controlli_P{P}.txt', 'w').write('\n'.join(R))
# 7. foglio di controllo: un fotogramma di ogni scheda blu + didascalia delle pillole
fotos = []
def frame_at(t):
    f = f'{OUT}/_f.png'; subprocess.run(['ffmpeg', '-y', '-v', 'error', '-ss', f'{t:.2f}', '-i', V, '-frames:v', '1', '-vf', 'scale=640:-2', f], check=True); return Image.open(f).convert('RGB').copy()
for pos in range(1, len(order) + 1):
    g = pos + off; s = ST[f'titolo{g}'][0]; fotos.append((f'titolo {g}', frame_at(s + 3.3)))
    s, d = ST[f'pillola{g}']; fotos.append((f'pillola {g} (onda)', frame_at(s + 2.5))); fotos.append((f'pillola {g} (didascalia)', frame_at(s + d - 2.3)))
    s = ST[f'quiz{g}'][0]; fotos.append((f'quiz {g}', frame_at(s + 4.0)))
s, d = ST['riepilogo']; fotos.append(('riepilogo (inizio)', frame_at(s + 2.0))); fotos.append(('riepilogo (ultimo)', frame_at(s + d - 1.0)))
cols = 4; w, hh = 640, 360; rows = (len(fotos) + cols - 1) // cols
S = Image.new('RGB', (cols * w, rows * (hh + 24)), 'white'); dr = ImageDraw.Draw(S)
for i, (nm, im) in enumerate(fotos):
    x = (i % cols) * w; y = (i // cols) * (hh + 24); S.paste(im, (x, y + 24)); dr.text((x + 6, y + 6), nm, fill='black')
S.save(f'{OUT}/foglio_P{P}.png'); say('foglio', len(fotos), 'fotogrammi')
# 8. un fotogramma ogni 30 s
n = int(dur // 30) + 1; cols = 6; w, hh = 320, 180; rows = (n + cols - 1) // cols
M = Image.new('RGB', (cols * w, rows * (hh + 16)), 'white'); dm = ImageDraw.Draw(M)
for i in range(n):
    t = min(i * 30 + 1, dur - 0.5); f = f'{OUT}/_m.png'
    subprocess.run(['ffmpeg', '-y', '-v', 'error', '-ss', f'{t:.1f}', '-i', V, '-frames:v', '1', '-vf', f'scale={w}:{hh}', f], check=True)
    x = (i % cols) * w; y = (i // cols) * (hh + 16); M.paste(Image.open(f).convert('RGB'), (x, y + 16)); dm.text((x + 4, y + 2), f'{int(t // 60)}:{int(t % 60):02d}', fill='black')
M.save(f'{OUT}/controllo_minuti_P{P}.jpg', quality=80)
print('fatto')
