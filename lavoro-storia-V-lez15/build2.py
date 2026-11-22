# -*- coding: utf-8 -*-
# Pezzi del prof (correzioni 22/11): intro sulla copertina e tratti di ogni argomento con slide a finestra a 40 px.
import sys, os, json, subprocess, numpy as np
sys.path.insert(0, '/tmp/claude-0/l15')
from plan2 import *
import sl2
from piece import prof_piece
W = '/tmp/claude-0/l15'
os.makedirs(W + '/pieces', exist_ok=True); os.makedirs(W + '/slpng', exist_ok=True)
IMGFILES = {6: ['up_p06_x29.png'], 8: ['up_p08_x34.png', 'up_p08_x35.png'], 11: ['up_p11_x42.png'], 13: ['up_p13_x47.png'], 15: ['up_p15_x52.png']}

def smooth_states(keys, step=0.1, min_img=3.0, min_card=1.6):
    runs = []
    for k in keys:
        if runs and runs[-1][0] == k: runs[-1][1] += 1
        else: runs.append([k, 1])
    ch = True
    while ch:
        ch = False
        for i in range(1, len(runs)):
            k, n = runs[i]; lim = min_img if k[0] == 'img' else min_card
            if n * step < lim and len(runs) > 1: runs[i - 1][1] += n; del runs[i]; ch = True; break
        j = 1
        while j < len(runs):
            if runs[j][0] == runs[j - 1][0]: runs[j - 1][1] += runs[j][1]; del runs[j]; ch = True
            else: j += 1
    return runs

def tract_runs(T, subs, pageidx, isimg):
    keys = []
    for a, b in subs:
        t = a
        while t < b - 1e-6: keys.append(state_at(t + 0.2, T, pageidx, isimg)); t += 0.1
    return smooth_states(keys)

def frames_from_runs(runs, total):
    out = []; acc = 0.0; used = 0
    for k, n in runs:
        acc += n * 3.0; f = int(round(acc)) - used
        if f > 0: out.append([k, f]); used += f
    if out: out[-1][1] += total - used
    return out

def kname(k): return '_'.join(str(x) for x in k)

def main():
    segs, topics, intro, pageidx, dmin, isimg = plan()
    TT = {T['n']: T for T in topics}
    cp = sl2.cards_from_pdf()
    # elenco dei tratti: (nome, a, b, T)
    jobs = [('intro', intro['src_a'], intro['src_b'], None)]
    for n in GLOBAL_ORDER:
        tr, info = tracts(segs, TT[n])
        for i, (a, b) in enumerate(tr): jobs.append((f'T{n}_{i}', a, b, TT[n]))
    data = []
    for name, a, b, T in jobs:
        if T is None: subs = [(a, b)]; runs = [[('cover',), int(round((b - a) / 0.1))]]
        else: subs = subs_of(segs, a, b, T['n']); runs = tract_runs(T, subs, pageidx, isimg)
        data.append((name, a, b, T, subs, runs))
    # pagine: cover=1, agenda=2, poi per ordine di comparsa nel video (anche gli approfondimenti)
    page = {('cover',): 1, ('agenda',): 2}; cur = 3
    for n in GLOBAL_ORDER:
        ks = [d for d in data if d[3] is not None and d[3]['n'] == n]
        for idx, (name, a, b, T, subs, runs) in enumerate(ks):
            for k, _ in runs:
                kk = ('txt', k[1], k[2]) if k[0] == 'txt' else ('img', k[1])
                if kk not in page: page[kk] = cur; cur += 1
            if idx < len(AN_OF[n]): page[('an', AN_OF[n][idx])] = cur; cur += 1
        page[('schema', n)] = cur; cur += 1
    page[('gloss',)] = cur; cur += 1
    for i in range(1, 5): page[('cmp', i)] = cur; cur += 1
    json.dump({str(k): v for k, v in page.items()}, open(W + '/pieces/pages.json', 'w'), indent=1)
    # PNG
    need = {}
    for name, a, b, T, subs, runs in data:
        for k, _ in runs: need[k] = 1
    items = []
    for k in need:
        nm = f'{kname(k)}'
        if os.path.exists(f'{W}/slpng/{nm}.png') and not os.environ.get('RIFAI'): continue
        if k[0] == 'cover': items.append((nm, sl2.cover(True)))
        elif k[0] == 'txt': items.append((nm, sl2.txt_slide(k[1], k[2], k[3], cp, page[('txt', k[1], k[2])])))
        elif k[0] == 'img': items.append((nm, sl2.img_slide(k[2], [f'{W}/img/up_{f[3:]}' if False else f'{W}/img/{f}' for f in IMGFILES[k[1]]], page[('img', k[1])])))
    sl2.render(items, W + '/slpng')
    for name, a, b, T, subs, runs in data:
        out = f'{W}/pieces/{name}.mp4'
        if os.path.exists(out): continue
        dur_total = sum(y - x for x, y in subs); N = int(round(dur_total * 30)); fr = frames_from_runs(runs, N)
        states = [(f"{W}/slpng/{kname(k)}.png", f) for k, f in fr]
        if len(subs) == 1: prof_piece(subs[0][0], dur_total, states, out)
        else:
            parts = []; sts = [list(s) for s in states]
            for si, (x, y) in enumerate(subs):
                nf = int(round((y - x) * 30)) if si < len(subs) - 1 else N - sum(int(round((yy - xx) * 30)) for xx, yy in subs[:-1])
                take = []; need_f = nf
                while need_f > 0:
                    s = sts[0]; t = min(s[1], need_f); take.append((s[0], t)); s[1] -= t; need_f -= t
                    if s[1] == 0: sts.pop(0)
                p = out.replace('.mp4', f'_{si}.mp4'); parts.append(p); prof_piece(x, nf / 30, take, p)
            with open(out + '.lst', 'w') as f:
                for p in parts: f.write(f"file '{p}'\n")
            subprocess.run(['ffmpeg', '-y', '-v', 'error', '-f', 'concat', '-safe', '0', '-i', out + '.lst', '-c', 'copy', out], check=True)
        json.dump(dict(subs=subs, dur=dur_total, N=N, runs=[(list(map(str, k)), n) for k, n in runs]), open(out + '.json', 'w'))
        print('fatto', name, round(dur_total, 1), flush=True)

if __name__ == '__main__':
    main()
