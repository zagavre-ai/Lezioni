# -*- coding: utf-8 -*-
# Rimonta il VIDEO di una Parte sostituendo solo intro / pezzi del prof / mappe; l'audio resta quello consegnato (stessi tempi, stessi fotogrammi).
# uso: python3 assemble2.py PARTE fase     (fasi: blocchi | finale)
import sys, os, json, subprocess, re, shutil
sys.path.insert(0, '/tmp/claude-0/w')
from dati import PARTI, POFF
P = int(sys.argv[1]); FASE = sys.argv[2]
B = '/home/user/w/b04/revisione-storia-V-lez04'
WK = '/home/user/w/l04/work'; OLD = f'/home/user/w/l04/old/Parte{P}.mp4'; XF = 12
OUT = f'{WK}/out{P}'; os.makedirs(OUT, exist_ok=True)
tl = json.load(open(f'{B}/timeline_Parte{P}.json'))
names = [n for n, _ in tl]
# lunghezze in fotogrammi di ogni pezzo, calcolate DALLA timeline di QUESTA Parte (n = distanza tra gli inizi + sovrapposizione)
NPC = {}
for i in range(len(tl) - 1): NPC[tl[i][0]] = round((tl[i + 1][1] - tl[i][1]) * 30) + XF

def nfr(f):
    return int(subprocess.run(['ffprobe', '-v', 'error', '-count_packets', '-select_streams', 'v:0', '-show_entries', 'stream=nb_read_packets', '-of', 'csv=p=0', f], capture_output=True, text=True).stdout.strip().split(',')[0])

if not os.path.exists(OLD):
    os.makedirs(os.path.dirname(OLD), exist_ok=True)
    parts = sorted(f for f in os.listdir(B) if f.startswith(f'Storia_Lez4_Parte{P}_1080p.mp4.parte_'))
    with open(OLD, 'wb') as o:
        for p in parts: o.write(open(f'{B}/{p}', 'rb').read())
TOTAL = nfr(OLD)
# fotogramma di inizio e lunghezza di ogni pezzo (il pezzo i occupa [s_i, s_i + n_i); i pezzi si sovrappongono di XF)
start = {}; n = {}; s = 0
for i, nm in enumerate(names):
    start[nm] = s
    n[nm] = NPC[nm] if nm in NPC else TOTAL - s
    s = s + n[nm] - XF
assert start[names[-1]] + n[names[-1]] == TOTAL, (start[names[-1]] + n[names[-1]], TOTAL)
# controllo: ogni pezzo nuovo ha esattamente i fotogrammi del pezzo che sostituisce; la posizione calcolata coincide con la timeline
for nm in names:
    assert abs(start[nm] / 30 - dict(tl)[nm]) < 0.05, (nm, start[nm] / 30, dict(tl)[nm])

def newclip(nm):
    if nm == 'intro': return f'{WK}/pieces/P1_intro.mp4'
    if nm.startswith('prof'):
        g = int(nm[4:]); return f'{WK}/pieces/P{P}_T{PARTI[P][g - POFF[P] - 1]}.mp4'
    if nm.startswith('mappa'): return f'{WK}/clips/mappa{nm[5:]}.mp4'
    return None
changed = [nm for nm in names if newclip(nm)]
for nm in changed: assert nfr(newclip(nm)) == n[nm], (nm, nfr(newclip(nm)), n[nm])
# blocchi: pezzi cambiati consecutivi
blocks = []
for nm in names:
    if nm in changed:
        if blocks and names.index(blocks[-1][-1]) == names.index(nm) - 1: blocks[-1].append(nm)
        else: blocks.append([nm])

def interval(b):
    a = start[b[0]]; e = start[b[-1]] + n[b[-1]]
    return a, e

def blocco(k, b):
    out = f'{OUT}/blk{k}.mp4'
    if os.path.exists(out + '.ok'): return out
    a, e = interval(b)
    fa = f'{OUT}/blk{k}_A.png'; fb = f'{OUT}/blk{k}_B.png'
    # ultimo fotogramma pulito del pezzo precedente / primo pulito del successivo
    subprocess.run(['ffmpeg', '-y', '-v', 'error', '-ss', f'{(a - 1) / 30:.4f}', '-i', OLD, '-frames:v', '1', fa], check=True)
    subprocess.run(['ffmpeg', '-y', '-v', 'error', '-ss', f'{(e + XF if False else e) / 30:.4f}', '-i', OLD, '-frames:v', '1', fb], check=True)
    ins = ['-loop', '1', '-framerate', '30', '-t', f'{XF / 30:.4f}', '-i', fa]
    for nm in b: ins += ['-i', newclip(nm)]
    ins += ['-loop', '1', '-framerate', '30', '-t', f'{XF / 30:.4f}', '-i', fb]
    m = len(b); d = XF / 30
    fl = ''; cur = '0:v'; curf = XF
    labels = [f'{i}:v' for i in range(m + 2)]
    fl += ''.join(f'[{i}:v]settb=AVTB,fps=30,format=yuv420p,setsar=1[v{i}];' for i in range(m + 2))
    cur = 'v0'; curf = XF
    for i in range(1, m + 2):
        nf = XF if i == m + 1 else n[b[i - 1]]
        off = (curf - XF) / 30
        fl += f'[{cur}][v{i}]xfade=transition=fade:duration={d:.5f}:offset={off:.5f}[x{i}];'
        cur = f'x{i}'; curf = curf + nf - XF
    fl = fl.rstrip(';')
    assert curf == e - a, (curf, e - a)
    subprocess.run(['ffmpeg', '-y', '-v', 'error'] + ins + ['-filter_complex', fl, '-map', f'[{cur}]', '-frames:v', str(e - a), '-c:v', 'libx264', '-preset', 'veryfast', '-crf', '16', '-r', '30', '-g', '60', '-pix_fmt', 'yuv420p', '-an', out], check=True)
    assert nfr(out) == e - a, (nfr(out), e - a)
    open(out + '.ok', 'w').write('1')
    return out

def lista():
    L = []; pos = 0
    for k, b in enumerate(blocks):
        a, e = interval(b)
        if a > pos: L.append(('old', pos, a))
        L.append(('blk', k, None)); pos = e
    if pos < TOTAL: L.append(('old', pos, TOTAL))
    return L

def oldclip(a, e):
    f = f'{OUT}/old_{a}_{e}.mp4'
    if not os.path.exists(f + '.ok'):
        subprocess.run(['ffmpeg', '-y', '-v', 'error', '-ss', f'{a / 30:.5f}', '-i', OLD, '-frames:v', str(e - a), '-c:v', 'libx264', '-preset', 'veryfast', '-crf', '12', '-r', '30', '-g', '60', '-pix_fmt', 'yuv420p', '-an', f], check=True)
        assert nfr(f) == e - a, (a, e, nfr(f))
        open(f + '.ok', 'w').write('1')
    return f

if FASE == 'blocchi':
    for k, b in enumerate(blocks):
        print('blocco', k, b, interval(b), flush=True); blocco(k, b)
    print('blocchi pronti')
elif FASE == 'finale':
    L = lista(); GD = f'{OUT}/g'; os.makedirs(GD, exist_ok=True)
    # gruppi di ~8 minuti: ogni voce della lista, spezzata a 14400 fotogrammi
    segm = []
    for t, x, y in L:
        if t == 'blk': segm.append(('blk', x, None, None, nfr(f'{OUT}/blk{x}.mp4')))
        else: segm.append(('old', None, x, y, y - x))
    groups = []; cur = []; cnt = 0
    for sg in segm:
        cur.append(sg); cnt += sg[4]
        if cnt >= 14400: groups.append(cur); cur = []; cnt = 0
    if cur: groups.append(cur)
    tot = 0
    for gi, g in enumerate(groups):
        f = f'{GD}/g{gi:03d}.mp4'
        if os.path.exists(f + '.ok'): tot += int(open(f + '.ok').read()); continue
        with open(f'{GD}/g{gi:03d}.txt', 'w') as lf:
            for t, k, a, e, nn in g:
                if t == 'blk': lf.write(f"file '{OUT}/blk{k}.mp4'\n")
                else: lf.write(f"file '{oldclip(a, e)}'\n")
        want = sum(x[4] for x in g)
        subprocess.run(['ffmpeg', '-y', '-v', 'error', '-f', 'concat', '-safe', '0', '-i', f'{GD}/g{gi:03d}.txt', '-map', '0:v', '-c:v', 'libx264', '-preset', 'veryfast', '-crf', '19',
                        '-maxrate', '16M', '-bufsize', '32M', '-pix_fmt', 'yuv420p', '-r', '30', '-g', '60', '-an', f], check=True)
        got = nfr(f); print('gruppo', gi + 1, 'di', len(groups), 'fotogrammi', got, 'attesi', want, flush=True)
        assert got == want, (got, want)
        open(f + '.ok', 'w').write(str(got)); tot += got
    assert tot == TOTAL, (tot, TOTAL)
    open(f'{GD}/v.txt', 'w').write(''.join(f"file '{GD}/g{gi:03d}.mp4'\n" for gi in range(len(groups))))
    subprocess.run(['ffmpeg', '-y', '-v', 'error', '-i', OLD, '-vn', '-c:a', 'copy', f'{OUT}/a.m4a'], check=True)
    final = f'{OUT}/Storia_Lez4_Parte{P}_1080p.mp4'
    subprocess.run(['ffmpeg', '-y', '-v', 'error', '-f', 'concat', '-safe', '0', '-i', f'{GD}/v.txt', '-i', f'{OUT}/a.m4a', '-map', '0:v', '-map', '1:a', '-c', 'copy', '-movflags', '+faststart', final], check=True)
    print('finale', final, 'fotogrammi', nfr(final), 'MB', round(os.path.getsize(final) / 1e6, 1))
