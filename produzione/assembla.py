#!/usr/bin/env python3
"""Inserisce gli AN nel video consegnato ai confini dei segmenti, con UNA sola codifica.
uso: assembla.py lezNN parte base.mp4 timeline.json vtt_in an_dir out_dir [--prova]
Scrive: <out>/video.mp4 timeline_new.json vtt_new; stampa i tempi nuovi."""
import sys, os, json, re, subprocess, importlib, argparse
QUI = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, QUI)
ap = argparse.ArgumentParser()
for k in ['lez', 'parte', 'base', 'timeline', 'vtt', 'an', 'out']: ap.add_argument(k)
ap.add_argument('--prova', action='store_true'); ap.add_argument('--card'); ap.add_argument('--solo-tempi', action='store_true'); o = ap.parse_args()
sys.path.insert(0, os.path.join(QUI, o.lez))
sp = importlib.import_module('spec_extra') if os.path.exists(os.path.join(QUI, o.lez, 'spec_extra.py')) else importlib.import_module('spec')
P = int(o.parte); os.makedirs(o.out, exist_ok=True)
FPS = 30; fr = lambda t: round(t * FPS) / FPS
def dur(p): return float(subprocess.run(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', p], capture_output=True, text=True).stdout)
TL = json.load(open(o.timeline)); st = {n: t for n, t, l in TL}
# ordine degli AN per punto di inserimento: nell'ordine della lista, mappe per ultime nello stesso argomento
ans = [a for a in sp.ANS if a['parte'] == P]
ins = {}
for a in ans: ins.setdefault(a['dopo'], []).append(a)
for k in ins: ins[k] = [a for a in ins[k] if a['tipo'] != 'mappa'] + [a for a in ins[k] if a['tipo'] == 'mappa']
cuts = []  # (tempo_taglio_originale, [(nome_an, file, durata)])
for k in sorted(ins):
    t = st['GL'] if k == 99 else st['S%d' % k]
    lst = []
    for a in ins[k]:
        n = f"P{P}_{a['id']}"; f = os.path.join(o.an, n + '.mp4'); lst.append((n, f, dur(f), a))
    cuts.append((fr(t), lst))
# nuova timeline
tot_ins = lambda t: sum(d for ct, l in cuts if ct <= t + 1e-6 for _, _, d, _ in l)
new = []
for n, t, l in TL: new.append([n, round(t + tot_ins(t), 3), l])
for ct, lst in cuts:
    pos = ct + sum(d for c2, l2 in cuts if c2 < ct for _, _, d, _ in l2)
    for n, f, d, a in lst:
        new.append([n.replace(f'P{P}_', 'AN_'), round(pos, 3), round(d, 3)]); pos += d
new.sort(key=lambda x: x[1])
# gli AN dopo il "quiz precedente": il Q/S ripasso restano dopo: nome AN_<id>
json.dump(new, open(f'{o.out}/timeline_new.json', 'w'))
tot = dur(o.base) + sum(d for _, l in cuts for _, _, d, _ in l)
# VTT
def ts(s): s = max(s, 0); return '%02d:%02d:%06.3f' % (s // 3600, (s % 3600) // 60, s % 60)
def pt(x): h, m, s = x.split(':'); return int(h) * 3600 + int(m) * 60 + float(s)
cues = re.findall(r'(\d+:\d+:\d+\.\d+) --> (\d+:\d+:\d+\.\d+)\n(.*?)(?:\n\n|\Z)', open(o.vtt).read(), re.S)
out = [(pt(a) + tot_ins(pt(a)), pt(b) + tot_ins(pt(b)), t.strip()) for a, b, t in cues]
for ct, lst in cuts:
    pos = ct + sum(d for c2, l2 in cuts if c2 < ct for _, _, d, _ in l2)
    for n, f, d, a in lst:
        txt = sp.voce_testo(a); fr_ = [x.strip() for x in re.split(r'(?<=[.!?:])\s+', txt) if x.strip()]
        # unisci frasi brevi, taglia le lunghe a ~80 caratteri
        blocchi = []
        for s in fr_:
            while len(s) > 84:
                i = s.rfind(' ', 0, 84); blocchi.append(s[:i]); s = s[i + 1:]
            blocchi.append(s)
        L = sum(len(b) for b in blocchi); t0 = pos + 0.3; spazio = d - 0.6
        for b in blocchi:
            t1 = t0 + spazio * len(b) / L
            ls = [b] if len(b) <= 42 else [b[:b.rfind(' ', 0, 42)], b[b.rfind(' ', 0, 42) + 1:]]
            out.append((t0, t1 - 0.05, '\n'.join(ls))); t0 = t1
        pos += d
out.sort(key=lambda x: x[0])
open(f'{o.out}/vtt_new.vtt', 'w').write('WEBVTT\n\n' + ''.join(f'{ts(a)} --> {ts(b)}\n{t}\n\n' for a, b, t in out))
print('durata nuova', round(tot, 2), 's =', '%d:%04.1f' % (tot // 60, tot % 60), '| inserito', round(tot - dur(o.base), 1), 's')
if o.solo_tempi: sys.exit()
# filtro
inp = ['-i', o.base]; fc = []; segs = []; prev = 0.0; k = 0; ai = 1
nb = len(cuts) + 1; 
fc.append(f'[0:v]split={nb}' + ''.join(f'[bv{i}]' for i in range(nb))); fc.append(f'[0:a]asplit={nb}' + ''.join(f'[ba{i}]' for i in range(nb)))
bounds = [0.0] + [c for c, _ in cuts] + [fr(st['COMPITI']) if o.card else dur(o.base)]
order = []
for i in range(nb):
    a, b = bounds[i], bounds[i + 1]
    fc.append(f'[bv{i}]trim=start={a:.5f}:end={b:.5f},setpts=PTS-STARTPTS,fps=30[v{i}b]'); fc.append(f'[ba{i}]atrim=start={a:.5f}:end={b:.5f},asetpts=PTS-STARTPTS,aformat=sample_rates=48000:channel_layouts=stereo[a{i}b]')
    order.append((f'[v{i}b]', f'[a{i}b]'))
    if i < len(cuts):
        for n, f, d, a_ in cuts[i][1]:
            inp += ['-i', f]; fc.append(f'[{ai}:v]fps=30,setsar=1[x{ai}v]'); fc.append(f'[{ai}:a]aformat=sample_rates=48000:channel_layouts=stereo[x{ai}a]')
            order.append((f'[x{ai}v]', f'[x{ai}a]')); ai += 1
if o.card:
    inp += ['-i', o.card]; fc.append(f'[{ai}:v]fps=30,setsar=1[x{ai}v]'); fc.append(f'[{ai}:a]aformat=sample_rates=48000:channel_layouts=stereo[x{ai}a]'); order.append((f'[x{ai}v]', f'[x{ai}a]')); ai += 1
fc.append(''.join(v + a for v, a in order) + f'concat=n={len(order)}:v=1:a=1[vo][ao]')
cmd = ['ffmpeg', '-y', '-v', 'error'] + inp + ['-filter_complex', ';'.join(fc), '-map', '[vo]', '-map', '[ao]', '-c:v', 'libx264', '-preset', 'veryfast', '-crf', os.environ.get('CRF', '19'), '-maxrate', '16M', '-bufsize', '32M', '-pix_fmt', 'yuv420p', '-r', '30', '-c:a', 'aac', '-b:a', '192k', '-ar', '48000', '-movflags', '+faststart']
if o.prova: cmd += ['-ss', os.environ.get('SS', '0'), '-t', os.environ.get('T', '60')]
cmd += [f'{o.out}/video.mp4']
open(f'{o.out}/cmd.txt', 'w').write(' '.join(map(str, cmd)))
subprocess.run(cmd, check=True); print('fatto')
