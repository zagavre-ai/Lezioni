#!/usr/bin/env python3
"""Rifacimento v2: taglia il video consegnato ai confini dei segmenti e inserisce gli AN. Ogni fotogramma è codificato UNA volta.
uso: assemble.py base.mp4 timeline_vecchia.json vtt_vecchio spec.py an_dir lavoro_dir uscita_dir [--prova]
pezzi: teacher [a,b) in fotogrammi; AN interi. Audio: wav PCM per pezzo -> concat -> AAC 192k una volta sola."""
import sys, os, json, re, subprocess, importlib.util
base, tlf, vttf, spec, andir, W, OUT = [os.path.abspath(x) for x in sys.argv[1:8]]
prova = '--prova' in sys.argv
os.makedirs(W, exist_ok=True); os.makedirs(OUT, exist_ok=True)
sp = importlib.util.spec_from_file_location('spec', spec); m = importlib.util.module_from_spec(sp); sp.loader.exec_module(m)
TL = json.load(open(tlf)); FPS = 30
def run(c): subprocess.run(c, check=True)
def dur(p): return float(subprocess.run(['ffprobe','-v','error','-show_entries','format=duration','-of','csv=p=0',p],capture_output=True,text=True).stdout)
fr = lambda t: round(t * FPS)
tinfo = {n: (t, l) for n, t, l in TL}
# punti di inserimento = fine del segmento indicato (D1..D4) oppure fine di Q4
def fine(n): return tinfo[n][0] + tinfo[n][1]
ins = {}
for a in m.AN: ins.setdefault(a['dopo'], []).append(a)
punti = sorted(((fr(fine(k)), k) for k in ins))
tot_fr = fr(dur(base))
pezzi = []  # (tipo, nome, frame_inizio, frame_fine, file)
prev = 0
for f, k in punti:
    pezzi.append(('T', f'T{len(pezzi)}', prev, f, None)); prev = f
    for a in ins[k]:
        pezzi.append(('A', a['id'], 0, fr(dur(f'{andir}/{a["id"]}.mp4')), f'{andir}/{a["id"]}.mp4'))
pezzi.append(('T', f'T{len(pezzi)}', prev, tot_fr, None))
if prova: pezzi = pezzi[:2] + [p for p in pezzi if p[0]=='A'][:1]
VENC = ['-c:v','libx264','-preset','veryfast','-crf','19','-maxrate','16M','-bufsize','32M','-pix_fmt','yuv420p','-r','30','-vf','scale=1920:1080:flags=lanczos,fps=30']
vl, wl, newpos = [], [], []
cur = 0
for i, (tp, nome, a, b, f) in enumerate(pezzi):
    n = b - a; vf = f'{W}/p{i:02d}.mp4'; wf = f'{W}/p{i:02d}.wav'
    okf = vf + ('.ok' if tp == 'T' else '.ok' + os.environ.get('ANV', '2') + '_' + str(n))
    if not os.path.exists(okf):
        if tp == 'T':
            run(['ffmpeg','-y','-v','error','-ss',f'{a/FPS:.6f}','-i',base,'-frames:v',str(n)] + VENC + ['-an', vf])
            run(['ffmpeg','-y','-v','error','-ss',f'{a/FPS:.6f}','-i',base,'-vn','-af',f'apad=whole_dur={n/FPS:.6f}','-t',f'{n/FPS:.6f}','-ac','2','-ar','48000','-c:a','pcm_s16le',wf])
        else:
            run(['ffmpeg','-y','-v','error','-i',f,'-frames:v',str(n)] + [x.replace('scale=1920','tpad=stop_mode=clone:stop_duration=3,scale=1920') for x in VENC] + ['-an', vf])
            run(['ffmpeg','-y','-v','error','-i',f,'-vn','-af',f'apad=whole_dur={n/FPS:.6f}','-t',f'{n/FPS:.6f}','-ac','2','-ar','48000','-c:a','pcm_s16le',wf])
        open(okf, 'w').write('1')
    vl.append(vf); wl.append(wf); newpos.append((nome, tp, a, b, cur, cur + n)); cur += n
    print('pezzo', i, nome, tp, n, 'fotogrammi', flush=True)
open(f'{W}/v.txt', 'w').write(''.join(f"file '{x}'\n" for x in vl)); open(f'{W}/w.txt', 'w').write(''.join(f"file '{x}'\n" for x in wl))
run(['ffmpeg','-y','-v','error','-f','concat','-safe','0','-i',f'{W}/w.txt','-c:a','aac','-b:a','192k','-ar','48000',f'{W}/a.m4a'])
final = f'{OUT}/Letteratura_Lez4_Parte1_1080p.mp4' if not prova else f'{W}/prova.mp4'
run(['ffmpeg','-y','-v','error','-f','concat','-safe','0','-i',f'{W}/v.txt','-itsoffset',os.environ.get('AOFF','0'),'-i',f'{W}/a.m4a','-map','0:v','-map','1:a','-c','copy','-movflags','+faststart',final])
json.dump(newpos, open(f'{W}/newpos.json', 'w'))
print('FINALE', final, round(dur(final), 2), 's', round(os.path.getsize(final)/1e6, 1), 'MB')
