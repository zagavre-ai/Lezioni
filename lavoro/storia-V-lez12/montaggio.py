# -*- coding: utf-8 -*-
# Montaggio dei pezzi del prof: webcam 4:3 dall'originale, slide a finestra, tagli nelle pause, audio pulito.
import os, json, subprocess, math, numpy as np
from PIL import Image, ImageDraw
import rend, slide, piano as P, contenuti as C
W = rend.WORK
SRC = f'{W}/in/LEZIONE 12 L_EUROPA E IL MONDO NEGLI ANNI TRENTA.mp4'
OUT = f'{W}/pezzi'; os.makedirs(OUT, exist_ok=True)
FPS = 30
ASR = json.load(open(f'{W}/trascr.json'))
KIT = '/home/user/Lezioni/kit'
X264 = ['-c:v', 'libx264', '-preset', 'veryfast', '-crf', '19', '-pix_fmt', 'yuv420p', '-r', '30', '-g', '60', '-keyint_min', '60', '-sc_threshold', '0', '-force_key_frames', '0,0.5', '-an']
TR = 0.5   # dissolvenza

def sh(cmd, **k):
    r = subprocess.run(cmd, capture_output=True, text=True, **k)
    if r.returncode: raise RuntimeError(' '.join(map(str, cmd))[:300] + '\n' + r.stderr[-1500:])
    return r

def fr(t): return round(t * FPS) / FPS

# ---------- audio dell'originale: inviluppo per trovare il silenzio ----------
_env = None
def env():
    global _env
    if _env is None:
        x = np.frombuffer(subprocess.run(['ffmpeg', '-v', 'error', '-i', SRC, '-vn', '-ac', '1', '-ar', '16000', '-f', 'f32le', '-'], capture_output=True).stdout, np.float32)
        n = len(x) // 160
        _env = np.sqrt((x[:n * 160].reshape(n, 160) ** 2).mean(1))   # 10 ms
    return _env

def piu_silenzioso(a, b):
    """istante in [a,b] con meno energia (finestra 120 ms)"""
    e = env(); i0 = max(0, int(a * 100)); i1 = min(len(e) - 12, max(i0 + 1, int(b * 100)))
    best = min(range(i0, i1 + 1), key=lambda i: e[i:i + 12].mean())
    return (best + 6) / 100

def segmenti_asr(t0, t1):
    return [s for s in ASR if s['inizio'] >= t0 - 0.05 and s['fine'] <= t1 + 0.6]

def taglio_inizio(t):
    """punto di attacco prima della frase che inizia a t: nel silenzio, almeno ~0,6 s prima se la pausa lo permette"""
    prev = max([s['fine'] for s in ASR if s['fine'] < t - 0.02] or [0])
    a = max(prev + 0.08, t - 0.95); b = max(a, t - 0.25)
    return fr(piu_silenzioso(a, b))

def taglio_fine(t):
    nxt = min([s['inizio'] for s in ASR if s['inizio'] > t + 0.02] or [t + 3])
    a = t + 0.15; b = min(t + 0.55, nxt - 0.2); b = max(a, b)
    return fr(piu_silenzioso(a, b))

def intervalli(ta, tb):
    """parti da tenere in [ta,tb]: pause oltre 2,5 s accorciate a circa 1 s"""
    segs = [s for s in ASR if s['fine'] > ta and s['inizio'] < tb]
    ranges = []; cur = ta
    for p, q in zip(segs, segs[1:]):
        g = q['inizio'] - p['fine']
        if g > 2.5:
            c1 = fr(piu_silenzioso(p['fine'] + 0.35, p['fine'] + 0.7)); c2 = fr(piu_silenzioso(q['inizio'] - 0.7, q['inizio'] - 0.35))
            if c2 - c1 > 0.5:
                ranges.append((cur, c1)); cur = c2
    ranges.append((cur, tb))
    return [(fr(a), fr(b)) for a, b in ranges if b - a >= 1 / FPS]

def maschera():
    f = f'{W}/maschera_cam.png'
    if not os.path.exists(f):
        m = Image.new('L', (412, 309), 0); ImageDraw.Draw(m).rounded_rectangle((0, 0, 411, 308), 14, fill=255); m.save(f)
    return f

def ultimo_fotogramma(mp4, out):
    sh(['ffmpeg', '-v', 'error', '-y', '-sseof', '-0.06', '-i', mp4, '-frames:v', '1', out])
    return out

def sfumature(img_a, img_b, out_dir, n=5):
    """fotogrammi intermedi tra due stati di slide (transizione morbida di 0,17 s)"""
    A = Image.open(img_a).convert('RGB'); B = Image.open(img_b).convert('RGB'); L = []
    for i in range(1, n + 1):
        f = f'{out_dir}/x_{os.path.basename(img_a)[:-4]}_{os.path.basename(img_b)[:-4]}_{i}.png'
        if not os.path.exists(f): Image.blend(A, B, i / (n + 1)).save(f)
        L.append(f)
    return L

# ---------- pezzo del prof ----------
def pezzo_prof(k, pagina0, gain_db=0.0, nome=None):
    """k = argomento. Ritorna dict(mp4, wav, durata, pagina_finale, tabella_fine, pagine=[(pagina,png)])"""
    T = P.TOP[k] if k else dict(t0=0.6, t1=168.4, titolo='')
    nome = nome or f'prof{k}'
    d = f'{OUT}/{nome}'; os.makedirs(d, exist_ok=True)
    ta = taglio_inizio(T['t0']) if k != 3 and k != 4 and k != 5 and k != 6 else taglio_inizio(T['t0'])
    tb = taglio_fine(T['t1'])
    rng = intervalli(ta, tb)
    # mappa tempo originale -> tempo del pezzo
    off = [0.0]
    for a, b in rng: off.append(off[-1] + (b - a))
    dur = off[-1]; nfr = round(dur * FPS); dur = nfr / FPS
    def f_(t):
        for (a, b), o in zip(rng, off):
            if a - 1e-6 <= t <= b + 1e-6: return o + (t - a)
        # tempo dentro una pausa tagliata: punto di taglio più vicino
        best = min(range(len(rng)), key=lambda i: min(abs(t - rng[i][0]), abs(t - rng[i][1])))
        return off[best] if t < rng[best][0] else off[best + 1]
    # slide
    pag = pagina0; stati = []; paginelist = []; mappa_pag = {}
    if k == 0:
        import inserti as _I
        cp = _I.cover_png(True); stati.append((0.0, dur, cp, 1)); paginelist.append((1, cp)); segs = []
    else: segs = slide.segmenti(k)
    for t0, t1, tp, w, a in segs:
        if t1 - t0 < 0.05: continue
        if w['id'] not in mappa_pag:
            mappa_pag[w['id']] = pag; pag += 1
        p = mappa_pag[w['id']]
        if tp == 'fin':
            png = f"{d}/s_{w['id']}_{'n' if a is None else a}_{p}.png"
            if not os.path.exists(png): slide.render_stato(k, a, w, p, png)
        else:
            png = f"{d}/i_{w['id']}_{p}.png"
            if not os.path.exists(png): slide.render_img(k, w['chiave'], w['cap'], p, png)
        stati.append((f_(max(t0, ta)), f_(min(t1, tb)), png, p))
        if not paginelist or paginelist[-1][0] != p: paginelist.append((p, png))
    # elenco immagini per concat (con sfumature)
    righe = []; tcur = 0.0; prev = None
    quadri = []   # (png, durata in fotogrammi)
    tot_fr = 0
    for i, (s0, s1, png, p) in enumerate(stati):
        n = round((s1) * FPS) - round(s0 * FPS) if i else round(s1 * FPS)
        if i == 0: n = round(s1 * FPS)
        quadri.append([png, n])
    # l'ultimo riempie fino alla durata
    quadri[-1][1] += nfr - sum(q[1] for q in quadri)
    # sfumature: sottrai 5 fotogrammi al quadro precedente e inseriscili come intermedi
    lista = []
    for i, (png, n) in enumerate(quadri):
        if i > 0 and quadri[i - 1][0] != png and n > 8 and lista and lista[-1][1] > 8:
            xs = sfumature(quadri[i - 1][0], png, d)
            lista[-1][1] -= 3; n -= 2
            for x in xs: lista.append([x, 1])
        lista.append([png, n])
    # correggi eventuale scarto
    diff = nfr - sum(n for _, n in lista); lista[-1][1] += diff
    with open(f'{d}/bg.txt', 'w') as fh:
        for png, n in lista: fh.write(f"file '{png}'\nduration {n / FPS:.6f}\n")
        fh.write(f"file '{lista[-1][0]}'\n")
    # filtri
    cam = []; aud = []; ins = ['-f', 'concat', '-safe', '0', '-i', f'{d}/bg.txt']
    for i, (a, b) in enumerate(rng):
        ins += ['-ss', f'{a:.4f}', '-t', f'{b - a:.4f}', '-i', SRC]
        cam.append(f"[{i+1}:v]setpts=PTS-STARTPTS[v{i}]")
        aud.append(f"[{i+1}:a]asetpts=PTS-STARTPTS,afade=t=in:d=0.015,afade=t=out:st={max(0, b - a - 0.015):.4f}:d=0.015[a{i}]")
    ins += ['-loop', '1', '-framerate', '30', '-i', maschera()]
    mk = len(rng) + 1
    n = len(rng)
    fc = ';'.join(cam + aud)
    fc += ';' + ''.join(f'[v{i}]' for i in range(n)) + f'concat=n={n}:v=1:a=0[vc]'
    fc += ';' + ''.join(f'[a{i}]' for i in range(n)) + f'concat=n={n}:v=0:a=1[ac]'
    fc += (";[vc]crop=185:138:876:343,scale=412:309:flags=lanczos,unsharp=5:5:0.7:5:5:0.0,eq=contrast=1.04:saturation=1.06:gamma=1.0,format=yuva420p[cam0];"
           f"[{mk}:v]format=gray,scale=412:309[mk];[cam0][mk]alphamerge[cam1];"
           "[0:v]fps=30,format=yuv420p[bg];[bg][cam1]overlay=1428:148:shortest=1,format=yuv420p[vout]")
    fc += (f";[ac]aresample=48000,highpass=f=70,afftdn=nr=5:nf=-48:tn=0,volume={gain_db:.2f}dB,pan=stereo|c0=c0|c1=c0[aout]")
    mp4 = f'{d}/v.mp4'; wav = f'{d}/a.wav'
    cmd = ['ffmpeg', '-v', 'error', '-y'] + ins + ['-filter_complex', fc,
           '-map', '[vout]', '-frames:v', str(nfr)] + X264 + [mp4,
           '-map', '[aout]', '-t', f'{dur:.4f}', '-ar', '48000', '-ac', '2', '-c:a', 'pcm_s16le', wav]
    sh(cmd)
    last = ultimo_fotogramma(mp4, f'{d}/ultimo.png')
    # tabella delle fine dei pezzi: ultime parole della frase finale
    fin_words = []
    for s in ASR:
        if s['fine'] <= tb and s['fine'] >= tb - 1.5:
            fin_words = [w[1] for w in s['parole']][-8:] if s.get('parole') else s['testo'].split()[-8:]
    ini_words = []
    for s in ASR:
        if s['inizio'] >= ta and s['inizio'] <= ta + 1.5:
            ini_words = s['testo'].split()[:8]; break
    return dict(nome=nome, mp4=mp4, wav=wav, durata=dur, frames=nfr, ultimo=last, pagina_finale=pag, pagine=paginelist,
                ta=ta, tb=tb, fine_parole=' '.join(fin_words), inizio_parole=' '.join(ini_words), intervalli=rng)
