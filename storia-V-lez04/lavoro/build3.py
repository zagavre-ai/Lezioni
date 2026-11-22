# -*- coding: utf-8 -*-
# Correzione 19/11: pezzi del prof con slide che cambiano al massimo ogni 150 s (card intere del PDF, max 3 per slide).
# Uso: python3 build2.py PARTE [solo_topic_n ...]
import sys, os, json, subprocess, hashlib, re
sys.path.insert(0, '/tmp/claude-0/w')
os.environ['PLAYWRIGHT_BROWSERS_PATH'] = '/opt/pw-browsers'
from plan_prof import *
import slides as SL
from build_prof import topic_states, frames_from_runs
from dati import *
W = '/tmp/claude-0/w'
NEWP = '/tmp/claude-0/w/pieces'; os.makedirs(NEWP, exist_ok=True)
SLP = '/tmp/claude-0/w/slpng3'; os.makedirs(SLP, exist_ok=True)
MAXF = 150 * 30          # una slide non resta uguale oltre 150 s (limite del prof: 3 minuti)
PIECE_N = {}
IMGFILE = {p: f'{W}/img/p{p:02d}.png' for p in IMGPAGES}

CPG = None
def hcard(n, i):
    """altezza stimata (px) di una card a 40 px, interlinea 1,5, ~54 caratteri per riga"""
    import math
    return max(1, math.ceil(len(CPG[n][i]) / 54)) * 60 + 24 + 12 + 6
FITH = 700
def family(c, nc, n=None):
    """insiemi di card (max 3, che ENTRANO a 40 px) che contengono la card attiva c: prima i contigui"""
    import itertools
    fit = lambda s: sum(hcard(n, i) for i in s) <= FITH
    if c < 0:
        for r in (3, 2, 1):
            for s in itertools.combinations(range(nc), r):
                if s[0] == 0 and fit(s) and s[-1] - s[0] == len(s) - 1: return [s]
    allsets = [s for r in (3, 2, 1) for s in itertools.combinations(range(nc), r) if c in s and fit(s)]
    base = max([s for s in allsets if s[-1] - s[0] == len(s) - 1 and s[0] == (0 if c <= 1 else c - (len(s) - 1))], key=len, default=allsets[0])
    contig = lambda s: s[-1] - s[0] == len(s) - 1
    allsets.sort(key=lambda s: (s != base, not contig(s), -len(s), sum(abs(x - c) for x in s)))
    return allsets

def retime(fr, nc, curn=None):
    """fr: [(key, frames)] a livello di fotogramma -> [(slidekey, active, frames)] con slide che cambia entro MAXF"""
    out = []; cur = None; since = 0; hist = []; last_c = 0
    def push(sk, act, f):
        if out and out[-1][0] == sk and out[-1][1] == act: out[-1][2] += f
        else: out.append([sk, act, f])
    total_after = [0] * (len(fr) + 1)
    for i in range(len(fr) - 1, -1, -1): total_after[i] = total_after[i + 1] + fr[i][1]
    # ultimo istante in cui la slide corrente puo' restare: se resta poco, la estendo (mai oltre 165 s)
    for i, (k, f) in enumerate(fr):
        rem = f
        while rem > 0:
            if k[0] == 'txt':
                c = k[2]
                if c >= 0: last_c = c
                if cur is not None and cur[0] == 'cards' and (c in cur[2] or c < 0) and since < MAXF:
                    ident = cur
                else:
                    fam = family(c, nc, curn)
                    cands = [s for s in fam if ('cards', k[1], s) != cur]
                    # la meno usata di recente (a parita', la prima in ordine di preferenza)
                    def lru(s):
                        return max([j for j, h in enumerate(hist) if h == ('cards', k[1], s)] or [-1])
                    pick = min(cands, key=lambda s: (lru(s), cands.index(s)))
                    ident = ('cards', k[1], pick); since = 0; hist.append(ident)
                allowed = MAXF - since
                take = min(rem, allowed) if allowed > 0 else rem
                if rem - take < 450 and rem <= MAXF + 450 - since: take = rem   # resto breve: non spezzare
                cur = ident; push(('cards', k[1], ident[2]), c, take); since += take; rem -= take
            else:   # immagine del prof
                pg = k[1]
                ident = ('img', pg, k[2])
                if cur is None or cur[0] != 'img' or cur[1] != pg:
                    cur = ident; since = 0
                # alterna immagine intera / immagine + card ogni MAXF
                allowed = MAXF - (since % MAXF)
                take = min(rem, allowed)
                if rem - take < 450 and rem <= MAXF + 450: take = rem
                variant = (since // MAXF) % 2
                sk = ('img', pg, k[2]) if variant == 0 else ('imgc', pg, k[2], last_c)
                push(sk, -1, take); since += take; rem -= take
    res = []
    for x in out:   # niente lampi: un pezzo sotto 1,5 s si unisce al precedente
        if res and x[2] < 45: res[-1][2] += x[2]
        else: res.append(list(x))
    return [tuple(x) for x in res]

def skey(sk, act):
    return '_'.join(str(x).replace(' ', '') for x in (sk if isinstance(sk, tuple) else (sk,))) + f'_a{act}'

def html_cards(n, cset, active, cp, page):
    a = ARG[n - 1]
    cards = ''
    for i in cset:
        c = cp[n][i]; h, b = SL.head_body(c)
        cards += f"<div class='card {'on' if i == active else ''}'><div class=num>{i + 1}</div><div><b>{SL.esc(h)}:</b> {SL.esc(b)}</div></div>"
    return SL.frame(f"{SL.P2(n):02d} · {a['nome']}", SL.esc(a['titolo']).replace("casus belli", "<i>casus belli</i>"), page,
                    f"<div class=cards>{cards}</div>", keys=[k for k, _ in a['schema']], active=active, titlesize=50)

def html_imgc(n, imgfile, c, cp, page):
    a = ARG[n - 1]; cc = cp[n][max(c, 0)]; h, b = SL.head_body(cc)
    body = (f"<div class=imgbox style='height:470px'><img style='width:1290px;height:440px;object-fit:contain' src='file://{imgfile}'></div>"
            f"<div class=cards style='top:780px'><div class='card on'><div class=num>{max(c,0)+1}</div><div><b>{SL.esc(h)}:</b> {SL.esc(b)}</div></div></div>")
    return SL.frame(f"{SL.P2(n):02d} · {a['nome']}", SL.esc(a['titolo']).replace("casus belli", "<i>casus belli</i>"), page, body,
                    keys=[k for k, _ in a['schema']], active=max(c, 0), titlesize=50)

def html_percorso(order, page):
    cards = ''
    for i, n in enumerate(order):
        a = ARG[n - 1]
        cards += f"<div class=card><div class=num>{i + 1}</div><div><b>{SL.esc(a['nome'])}:</b> {SL.esc(a['chip'].replace(' · ', ' · '))}</div></div>"
    return SL.frame('IL PERCORSO DELLA LEZIONE', 'Il percorso della lezione', page, f"<div class=cards>{cards}</div>", titlesize=56)

def piece_png(P, sk, act, cp, page, order):
    nm = f'P{P}_' + skey(sk, act)
    f = f'{SLP}/{nm}.png'
    if os.path.exists(f): return f, None
    if sk[0] == 'cards': h = html_cards(sk[1], sk[2], act, cp, page)
    elif sk[0] == 'img': h = SL.html_img(sk[2], IMGFILE[sk[1]], page)
    elif sk[0] == 'imgc': h = html_imgc(sk[2], IMGFILE[sk[1]], sk[3], cp, page)
    elif sk[0] == 'cover': h = SL.html_cover(1, True, order, None)
    elif sk[0] == 'percorso': h = html_percorso(order, page)
    return f, (nm, h)

def encode(a, dur, states, out):
    import piece as PC
    N = round(dur * 30); lst = out + '.txt'
    with open(lst, 'w') as f:
        for p, fr in states:
            for x in PC.seg_files(p, fr): f.write(f"file '{x}'\n")
    fc = ("[0:v]format=yuv420p[bg];[1:v]crop=181:136:856:344,scale=412:310:flags=lanczos,hqdn3d=1.5:1.5:3:3,eq=contrast=1.04:saturation=1.03,cas=0.35,format=yuva420p[p];"
          "[2:v]format=gray[m];[p][m]alphamerge[pa];[bg][pa]overlay=1428:148:format=auto,format=yuv420p[v]")
    cmd = ['ffmpeg', '-y', '-v', 'error', '-f', 'concat', '-safe', '0', '-i', lst, '-ss', f'{a:.3f}', '-t', f'{dur + 0.5:.3f}', '-i', W + '/dl/v.mp4', '-loop', '1', '-framerate', '30', '-t', f'{dur + 0.5:.3f}', '-i', W + '/mask.png',
           '-filter_complex', fc, '-map', '[v]', '-frames:v', str(N), '-c:v', 'libx264', '-preset', 'veryfast', '-crf', '17', '-r', '30', '-g', '60', '-force_key_frames', f'0.4,{dur - 0.4:.3f}', '-pix_fmt', 'yuv420p', '-an', out]
    subprocess.run(cmd, check=True)

def build_piece(P, name, subs, runs_fr, nc, cp, order, pageno, forced=None, curn=None):
    """subs: intervalli sorgente (con tagli dei silenzi); runs_fr: stati a livello fotogramma"""
    dur_total = sum(y - x for x, y in subs); N = int(round(dur_total * 30))
    seq = forced if forced is not None else retime(runs_fr, nc, curn)
    assert sum(f for _, _, f in seq) == N, (sum(f for _, _, f in seq), N)
    items = []; states = []
    for sk, act, f in seq:
        if sk not in pageno: pageno[sk] = max(pageno.values()) + 1
        png, it = piece_png(P, sk, act, cp, pageno[sk], order)
        if it: items.append(it)
        states.append((png, f))
    if items: SL.render(items, SLP)
    # sotto-intervalli
    out = f'{NEWP}/P{P}_{name}.mp4'
    if len(subs) == 1:
        encode(subs[0][0], dur_total, states, out)
    else:
        parts = []; sts = [list(s) for s in states]
        for si, (x, y) in enumerate(subs):
            nf = int(round((y - x) * 30)) if si < len(subs) - 1 else N - sum(int(round((yy - xx) * 30)) for xx, yy in subs[:-1])
            take = []; need_f = nf
            while need_f > 0:
                s = sts[0]; t = min(s[1], need_f); take.append((s[0], t)); s[1] -= t; need_f -= t
                if s[1] == 0: sts.pop(0)
            p = out.replace('.mp4', f'_{si}.mp4'); parts.append(p)
            encode(x, nf / 30, take, p)
        with open(out + '.lst', 'w') as f:
            for p in parts: f.write(f"file '{p}'\n")
        subprocess.run(['ffmpeg', '-y', '-v', 'error', '-f', 'concat', '-safe', '0', '-i', out + '.lst', '-c', 'copy', out], check=True)
        for p in parts: os.remove(p)
    json.dump(dict(subs=subs, N=N, seq=[(list(map(str, sk)), a, f) for sk, a, f in seq]), open(out + '.json', 'w'))
    return seq

def main():
    P = int(sys.argv[1]); only = [int(x) for x in sys.argv[2:]]
    segs, topics, intro, pageidx, dmin, isimg, cp = plan()
    global CPG; CPG = cp
    order = PARTI[P]; TT = {T['n']: T for T in topics}; pageno = {('cover',): 1}
    pn = json.load(open(f'{NEWP}/pages_P{P}.json')) if os.path.exists(f'{NEWP}/pages_P{P}.json') else {}
    if P == 1 and (not only or 0 in only):
        a, b = intro['src_a'], intro['src_b']; N = int(round((b - a) * 30))
        pass
        f1 = 100 * 30   # copertina 100 s, poi «Il percorso della lezione»
        seq = [(('cover',), -1, f1), (('percorso',), -1, N - f1)]
        build_piece(P, 'intro', [(a, b)], None, 5, cp, order, pageno, forced=seq)
        print('intro fatto', flush=True)
    for pos, n in enumerate(order, 1):
        if only and n not in only: continue
        T = TT[n]; g = pos + POFF[P]
        subs = sub_intervals(segs, T['src_a'], T['src_b']); runs = topic_states(T, pageidx, isimg, subs)
        fr = frames_from_runs(runs, int(round(sum(y - x for x, y in subs) * 30)))
        pass
        N = sum(f for _, f in fr)
        pass
        seq = build_piece(P, f'T{n}', subs, fr, len(cp[n]), cp, order, pageno, curn=n)
        mx = {}
        for sk, act, f in seq: mx[sk] = mx.get(sk, 0) + f
        print('fatto T', n, 'slide', len(set(s for s, _, _ in seq)), 'run max slide', max(f for _, _, f in seq) / 30, flush=True)
    json.dump({'|'.join(map(str, k)): v for k, v in pageno.items()}, open(f'{NEWP}/pages_P{P}_{"_".join(map(str, only)) or "all"}.json', 'w'))

if __name__ == '__main__':
    main()
