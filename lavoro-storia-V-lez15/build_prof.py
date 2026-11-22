# -*- coding: utf-8 -*-
# Costruisce i pezzi del prof (slide + riquadro) per le due Parti. Uso: python3 build_prof.py [parte]
import sys, os, json, subprocess, numpy as np
sys.path.insert(0, '/tmp/claude-0/l15')
from plan_prof import *
import slides as SL
from piece import prof_piece
W = '/tmp/claude-0/l15'
os.makedirs(W + '/pieces', exist_ok=True); os.makedirs(W + '/slpng', exist_ok=True)
IMGFILE = {p: f'{W}/img/p{p:02d}c.png' for p in IMGPAGES}

def smooth_states(keys, step=0.1, min_img=3.0, min_card=1.6):
    """lista di chiavi a passo fisso -> sistema le sequenze troppo brevi"""
    runs = []
    for k in keys:
        if runs and runs[-1][0] == k: runs[-1][1] += 1
        else: runs.append([k, 1])
    # card/immagini troppo brevi: assorbi nel precedente
    ch = True
    while ch:
        ch = False
        for i in range(1, len(runs)):
            k, n = runs[i]
            lim = min_img if k[0] == 'img' else min_card
            if n * step < lim and i < len(runs) - 0 and len(runs) > 1:
                runs[i - 1][1] += n; del runs[i]; ch = True; break
        # unisci uguali adiacenti
        j = 1
        while j < len(runs):
            if runs[j][0] == runs[j - 1][0]: runs[j - 1][1] += runs[j][1]; del runs[j]; ch = True
            else: j += 1
    return runs

def topic_states(T, pageidx, isimg, subs):
    keys = []
    for a, b in subs:
        t = a
        while t < b - 1e-6:
            keys.append(state_at(t, T, pageidx, isimg)); t += 0.1
    # il primo stato non puo' essere una card accesa/immagine breve: forza
    return smooth_states(keys)

def frames_from_runs(runs, total_frames):
    """runs a passo 0.1 s -> frame (30 fps), somma = total_frames"""
    out = []; acc = 0.0; used = 0
    for k, n in runs:
        acc += n * 3.0  # 3 frame per passo
        f = int(round(acc)) - used
        if f > 0: out.append([k, f]); used += f
    d = total_frames - used
    if out: out[-1][1] += d
    return out

def key_name(k):
    return '_'.join(str(x) for x in k)

def main():
    which = sys.argv[1:] or ['1', '2']
    segs, topics, intro, pageidx, dmin, isimg, cp = plan()
    for P in which:
        P = int(P); order = PARTI[P]
        pass
        TT = {T['n']: T for T in topics}
        # numerazione pagine slide (come PDF): cover=1, poi per argomento testo, immagini, schema; glossario in fondo
        page = {('cover',): 1}; cur = 2; plan_p = []
        pieces = []
        # intro del prof (solo Parte 1)
        if P == 1:
            plan_p.append(('intro', intro['src_a'], intro['src_b'], None))
        for n in order:
            plan_p.append(('topic', TT[n]['src_a'], TT[n]['src_b'], TT[n]))
        # stati
        data = []
        for kind, a, b, T in plan_p:
            if kind == 'intro':
                subs = [(a, b)]; runs = [[('cover', 1), int(round((b - a) / 0.1))]]
            else:
                subs = sub_intervals(segs, a, b); runs = topic_states(T, pageidx, isimg, subs)
            data.append((kind, a, b, T, subs, runs))
            if kind == 'topic':
                n = T['n']; page.setdefault(('txt', n), cur); cur += 1 if ('txt', n) not in page or page[('txt', n)] == cur else 0
        # assegna pagine per ordine di apparizione (testo, poi immagini)
        page = {('cover',): 1}; cur = 2
        for kind, a, b, T, subs, runs in data:
            if kind != 'topic': continue
            n = T['n']; page[('txt', n)] = cur; cur += 1
            for k, _ in runs:
                if k[0] == 'img' and ('img', k[1]) not in page: page[('img', k[1])] = cur; cur += 1
            page[('schema', n)] = cur; cur += 1
        for kind, a, b_, T, subs, runs in data:
            if kind != 'topic': continue
            for k, _ in runs:
                if k[0] == 'txt' and ('txt', k[1]) not in page: page[('txt', k[1])] = cur; cur += 1
        page[('gloss',)] = cur
        json.dump({str(k): v for k, v in page.items()}, open(f'{W}/pieces/pages_P{P}.json', 'w'), indent=1)
        # render slide PNG necessari
        need = {}
        for kind, a, b, T, subs, runs in data:
            for k, _ in runs: need[k] = 1
        items = []
        for k in need:
            nm = f'P{P}_{key_name(k)}'
            if os.path.exists(f'{W}/slpng/{nm}.png'): continue
            if k[0] == 'cover': items.append((nm, SL.html_cover(1, True, order if P == 1 else order, None if P == 1 else None)))
            elif k[0] == 'txt': items.append((nm, SL.html_txt(k[1], k[2], cp, page[('txt', k[1])])))
            elif k[0] == 'img':
                items.append((nm, SL.html_img(k[2], IMGFILE[k[1]], page[('img', k[1])])))
        SL.render(items, W + '/slpng')
        # encode
        for kind, a, b, T, subs, runs in data:
            name = 'intro' if kind == 'intro' else f"T{T['n']}"
            out = f'{W}/pieces/P{P}_{name}.mp4'
            if os.path.exists(out): continue
            dur_total = sum(y - x for x, y in subs)
            N = int(round(dur_total * 30)); fr = frames_from_runs(runs, N)
            states = [(f"{W}/slpng/P{P}_{key_name(k)}.png", f) for k, f in fr]
            # un pezzo per sotto-intervallo (tagli dei silenzi > 3 s)
            if len(subs) == 1:
                prof_piece(subs[0][0], dur_total, states, out)
            else:
                # ripartisci gli stati sui sotto-intervalli
                parts = []; idx = 0; rem = states[0][1]; cur_state = 0
                sts = [list(s) for s in states]
                for si, (x, y) in enumerate(subs):
                    nf = int(round((y - x) * 30)) if si < len(subs) - 1 else N - sum(int(round((yy - xx) * 30)) for xx, yy in subs[:-1])
                    take = []; need_f = nf
                    while need_f > 0:
                        s = sts[0]; t = min(s[1], need_f); take.append((s[0], t)); s[1] -= t; need_f -= t
                        if s[1] == 0: sts.pop(0)
                    p = out.replace('.mp4', f'_{si}.mp4'); parts.append(p)
                    prof_piece(x, nf / 30, take, p)
                with open(out + '.lst', 'w') as f:
                    for p in parts: f.write(f"file '{p}'\n")
                subprocess.run(['ffmpeg', '-y', '-v', 'error', '-f', 'concat', '-safe', '0', '-i', out + '.lst', '-c', 'copy', out], check=True)
            json.dump(dict(subs=subs, dur=dur_total, N=N, runs=[(list(map(str, k)), n) for k, n in runs]), open(out + '.json', 'w'))
            print('fatto', out, round(dur_total, 1), flush=True)

if __name__ == '__main__':
    main()
