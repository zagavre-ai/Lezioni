#!/usr/bin/env python3
"""Schede della lezione (Storia V, «La guerra fredda (1945-1961)»): tutti i pezzi «scheda» in /tmp/w/pezzi.
Uso:  python3 schede.py            -> rifà tutto
      python3 schede.py T1 PS3 CW1 -> rifà solo questi pezzi   (nomi: SIG SFIN COVER CW1 CW2 T1..T7 PI1..PI7 PS1..PS7 Q1..Q7 GL1 GL2 FIN1 FIN2 VER CINTRO COMP)
      python3 schede.py --voci      -> rifà i pezzi che dipendono da voci arrivate dopo (CW1 CW2)
Le voci mancanti (W1_R2, W2_R2) sono sostituite da un silenzio provvisorio (parole/2,5 al secondo): rilanciando
quando il file arriva in vox/, il pezzo si rifà da solo (durata, tempi di accensione dalla trascrizione).
"""
import os, sys, json, re, subprocess, hashlib, shutil, math, html as H, difflib, unicodedata
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import numpy as np
import slide as S
import spec

W = '/tmp/w'
REPO = '/home/user/Lezioni'
OUT = W + '/pezzi'
WK = W + '/s'
VOX = W + '/vox/scambio/storia-V-lez14/vox'
SND = REPO + '/kit/suoni'
FPS = 30
for d in (OUT, WK, WK + '/fr', WK + '/aud', WK + '/asr', WK + '/html'):
    os.makedirs(d, exist_ok=True)
TESTI = {x['nome']: x['testo'] for x in json.load(open(W + '/old/testi_voci.json'))}
TESTI.update({x['nome']: x['testo'] for x in json.load(open(W + '/voci_nuove.json'))})
QUIZ = json.load(open(W + '/old/quiz_argomenti.json'))
COMPITI = json.load(open(W + '/old/compiti.json'))
TITOLO = 'La guerra fredda (1945-1961)'
ARGT = {n: spec.ARG[n][0] for n in spec.ARG}
PARTE = {1: [1, 2, 3], 2: [4, 5, 6, 7]}
AVVISO = ('© Centro Studi Telesio. Tutti i contenuti riprodotti in questa videolezione (testi, grafiche, animazioni, voci e registrazioni) sono di '
          'proprietà del Centro Studi Telesio. È vietata la riproduzione, anche parziale, senza autorizzazione scritta.')
NOTE = []  # note per il file note_schede.md


def sh(cmd, **k):
    r = subprocess.run(cmd, shell=isinstance(cmd, str), capture_output=True, text=True, **k)
    if r.returncode:
        raise RuntimeError((cmd if isinstance(cmd, str) else ' '.join(cmd)) + '\n' + r.stderr[-2000:])
    return r


def dur(f):
    return float(sh(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', f]).stdout)


def nfr(t):
    """numero di fotogrammi (arrotonda per eccesso) per una durata t"""
    return int(math.ceil(t * FPS - 1e-6))


# ------------------------------------------------------------------ numeri in lettere -> cifre (solo per lo schermo)
UN = {'due': 2, 'tre': 3, 'quattro': 4, 'cinque': 5, 'sei': 6, 'sette': 7, 'otto': 8, 'nove': 9, 'dieci': 10, 'undici': 11, 'dodici': 12,
      'tredici': 13, 'quattordici': 14, 'quindici': 15, 'sedici': 16, 'diciassette': 17, 'diciotto': 18, 'diciannove': 19}
TENS = {'vent': 20, 'trent': 30, 'quarant': 40, 'cinquant': 50, 'sessant': 60, 'settant': 70, 'ottant': 80, 'novant': 90}


def _p(w):
    if not w:
        return 0
    if w in UN:
        return UN[w]
    if w == 'uno':
        return 1
    if w.startswith('mille'):
        r = _p(w[5:])
        return None if r is None else 1000 + r
    m = re.match(r'^(due|tre|quattro|cinque|sei|sette|otto|nove)?cento(.*)$', w)
    if m:
        r = _p(m.group(2))
        return None if r is None else (UN.get(m.group(1), 1)) * 100 + r
    for st, v in TENS.items():
        if w.startswith(st):
            r = w[len(st):]
            if r in ('a', 'i', ''):
                return v
            r = r[1:] if r[0] in 'ai' else r
            u = 1 if r == 'uno' else UN.get(r)
            return v + u if u and u < 10 else None
    return None


def cifre(t):
    """«millenovecentoquarantacinque» -> «1945» per lo schermo; ordinali «trentottesimo» -> «38°»"""
    out = []
    parole = re.findall(r"[A-Za-zÀ-ÿ]+|[^A-Za-zÀ-ÿ]+", t)
    prev = ''
    for i, w in enumerate(parole):
        lw = w.lower()
        if re.match(r'^[A-Za-zÀ-ÿ]+$', w):
            if lw.endswith('esimo') and _p(lw[:-5]) and _p(lw[:-5]) > 10:
                out.append(f'{_p(lw[:-5])}°')
            elif lw in ('uno', 'una', 'un'):
                out.append(w)
            elif lw == 'sei' and prev != 'dei':
                out.append(w)
            elif w[0].isupper() and prev == 'anni':
                out.append(w)
            else:
                v = _p(lw)
                out.append(str(v) if v is not None and lw not in ('uno',) else w)
            prev = lw
        else:
            out.append(w)
    return ''.join(out)


def esc(s):
    return H.escape(s)


def sigle_in(t):
    return [(k, v) for k, v in S.SIGLE.items() if re.search(r'\b' + k + r'\b', t) and v.lower() not in t.lower()]


def chips(sg, cls='chip'):
    return ''.join(f'<span class="{cls}"><b>{esc(k)}</b> = {esc(v)}</span>' for k, v in sg)


# ------------------------------------------------------------------ voci e audio
def voce_path(nome):
    return f'{VOX}/{nome}.wav'


def voce_provvisoria(nome):
    return not os.path.exists(voce_path(nome))


def lufs(path):
    r = subprocess.run(['ffmpeg', '-nostats', '-i', path, '-af', 'ebur128', '-f', 'null', '-'], capture_output=True, text=True).stderr
    m = re.findall(r'I:\s+(-?[\d.]+) LUFS', r)
    return float(m[-1])


def audio_norm(path, target, tag, fade=0.04, pad=0.0, jingle=False):
    """porta a 48 kHz stereo e al livello `target` LUFS, dissolvenze di 40 ms, picco <= -1 dBTP; ritorna (file, durata)"""
    out = f'{WK}/aud/{tag}_{abs(int(target))}_v3.wav'
    key = out + '.key'
    k = f'{os.path.getmtime(path)}:{os.path.getsize(path)}'
    if os.path.exists(out) and os.path.exists(key) and open(key).read() == k:
        return out, dur(out)
    tmp = out + '.pre.wav'
    sh(['ffmpeg', '-y', '-v', 'error', '-i', path, '-af', 'aresample=48000,pan=stereo|c0=c0|c1=c0' if _mono(path) else 'aresample=48000', '-c:a', 'pcm_s16le', tmp])
    g = target - lufs(tmp)
    d = dur(tmp)
    if jingle:  # solo guadagno (nessun limiter con ritardo): l'attacco deve restare sull'istante esatto
        mv = float(re.findall(r'max_volume: (-?[\d.]+) dB', subprocess.run(['ffmpeg', '-nostats', '-i', tmp, '-af', 'volumedetect', '-f', 'null', '-'], capture_output=True, text=True).stderr)[0])
        g = min(g, -1.5 - mv)
        sh(['ffmpeg', '-y', '-v', 'error', '-i', tmp, '-af', f'volume={g}dB', '-c:a', 'pcm_s16le', out])
        os.remove(tmp)
        open(key, 'w').write(k)
        return out, dur(out)
    sh(['ffmpeg', '-y', '-v', 'error', '-i', tmp, '-af',
        f'volume={g}dB,alimiter=limit=0.891:level=disabled,afade=t=in:st=0:d={fade},afade=t=out:st={d - fade}:d={fade}' + (f',apad=pad_dur={pad}' if pad else ''),
        '-c:a', 'pcm_s16le', out])
    os.remove(tmp)
    open(key, 'w').write(k)
    return out, dur(out)


def _mono(path):
    return int(sh(['ffprobe', '-v', 'error', '-select_streams', 'a:0', '-show_entries', 'stream=channels', '-of', 'csv=p=0', path]).stdout) == 1


def voce(nome):
    """(file 48 kHz stereo -16 LUFS, durata, provvisoria?)"""
    if voce_provvisoria(nome):
        n = len(TESTI[nome].split())
        d = n / 2.5
        f = f'{WK}/aud/{nome}_provv.wav'
        sh(['ffmpeg', '-y', '-v', 'error', '-f', 'lavfi', '-i', 'anullsrc=r=48000:cl=stereo', '-t', f'{d:.3f}', '-c:a', 'pcm_s16le', f])
        return f, d, True
    f, d = audio_norm(voce_path(nome), -16, 'v_' + nome, pad=0.06)
    return f, d, False


def jingle(nome):
    return audio_norm(f'{SND}/{nome}.wav', -22, 'j_' + nome, jingle=True)[0]


def bordo_voce(f):
    """ampiezza massima negli ultimi 50 ms (deve stare sotto 0,03)"""
    x = np.frombuffer(sh(['ffmpeg', '-v', 'error', '-sseof', '-0.05', '-i', f, '-f', 's16le', '-ac', '1', '-'], ).stdout.encode('latin1') if False else
                      subprocess.run(['ffmpeg', '-v', 'error', '-sseof', '-0.05', '-i', f, '-f', 's16le', '-ac', '1', '-'], capture_output=True).stdout, np.int16)
    return float(np.abs(x).max() / 32768) if len(x) else 0.0


def mix_audio(out, total, voci, jingoli):
    """voci: [(nome, start)], jingoli: [(nome, start)] -> wav 48 kHz stereo lungo esattamente `total` secondi"""
    ins = []
    for nome, st in voci:
        f, d, pv = voce(nome)
        ins.append((f, st))
    for nome, st in jingoli:
        ins.append((jingle(nome), st))
    if not ins:
        sh(['ffmpeg', '-y', '-v', 'error', '-f', 'lavfi', '-i', 'anullsrc=r=48000:cl=stereo', '-t', f'{total:.6f}', '-c:a', 'pcm_s16le', out])
        return
    cmd = ['ffmpeg', '-y', '-v', 'error']
    fc = []
    for i, (f, st) in enumerate(ins):
        cmd += ['-i', f]
        ms = int(round(st * 1000))
        fc.append(f'[{i}:a]adelay={ms}|{ms}[a{i}]')
    fc.append(''.join(f'[a{i}]' for i in range(len(ins))) + f'amix=inputs={len(ins)}:normalize=0:duration=longest,apad,atrim=0:{total:.6f},asetpts=N/SR/TB[o]')
    cmd += ['-filter_complex', ';'.join(fc), '-map', '[o]', '-ar', '48000', '-ac', '2', '-c:a', 'pcm_s16le', out]
    sh(cmd)


# ------------------------------------------------------------------ trascrizione e allineamento
def trascrivi(nome):
    j = f'{WK}/asr/{nome}.json'
    if not os.path.exists(j):
        env = {**os.environ, 'TELESIO_ASR': '/tmp/asr'}
        subprocess.run(['python3', REPO + '/kit/tools/trascrivi.py', voce_path(nome), f'{WK}/asr/{nome}'], check=True, env=env, capture_output=True)
    return json.load(open(j))


def asr_parole(nome):
    s = trascrivi(nome)
    out = []
    cur = None
    for x in s:
        for t, w in x['parole']:
            if w.startswith(' ') or cur is None:
                if cur:
                    out.append(cur)
                cur = [float(t), w.strip()]
            else:
                cur[1] += w
    if cur:
        out.append(cur)
    res = []
    for t, w in out:
        for n in _norm(w):
            res.append((t, n))
    return res


def _norm(s):
    return re.sub(r'[^a-z0-9 ]', ' ', unicodedata.normalize('NFD', s.lower()).encode('ascii', 'ignore').decode()).split()


def tempi_unita(nome, unita):
    """tempo di inizio (s, relativo all'inizio della voce) di ogni unità di testo. Voce provvisoria: proporzione sui caratteri."""
    tot = sum(len(u) for u in unita)
    if voce_provvisoria(nome):
        d = voce(nome)[1]
        acc = 0
        res = []
        for u in unita:
            res.append(d * acc / tot)
            acc += len(u)
        return res
    A = asr_parole(nome)
    T = []
    for k, u in enumerate(unita):
        for w in _norm(cifre(u)):
            T.append((k, w))
    sm = difflib.SequenceMatcher(None, [w for t, w in A], [w for k, w in T], autojunk=False)
    mp = {}
    for a, b, n in sm.get_matching_blocks():
        for q in range(n):
            mp[b + q] = a + q
    first = {}
    last = {}
    for ti, (k, w) in enumerate(T):
        if ti in mp:
            first.setdefault(k, mp[ti])
            last[k] = mp[ti]
    res = []
    prev_last = -1
    for k in range(len(unita)):
        if k == 0:
            res.append(A[0][0] if A else 0.0)
            prev_last = last.get(0, 0)
            continue
        f = first.get(k)
        if f is None:  # unità senza corrispondenze: stima dopo la precedente
            f = min(len(A) - 1, prev_last + 1)
        lo = prev_last + 1
        cand = list(range(lo, f + 1))
        best = f
        if len(cand) > 1:
            gaps = [(A[i][0] - A[i - 1][0], i) for i in cand if i > 0]
            if gaps:
                g, i = max(gaps)
                if g > 0.25:
                    best = i
        res.append(A[min(best, len(A) - 1)][0])
        prev_last = max(prev_last, last.get(k, best))
    for i in range(1, len(res)):  # monotono
        res[i] = max(res[i], res[i - 1] + 0.05)
    return res


# ------------------------------------------------------------------ pagine delle slide (numeri della dispensa)
def pagina_ps(n):
    _, elenco = spec.numeri_pagina()
    for parte, p, k in elenco:
        if k == ('PS', n):
            return p
    raise KeyError(n)


# ------------------------------------------------------------------ sfondo blu animato (ciclo di 12 s, senza lampi)
BG = WK + '/bg_blu.mkv'
BGP = 12.0


def sfondo_blu():
    if os.path.exists(BG):
        return BG
    w, h = 960, 540
    yy, xx = np.mgrid[0:h, 0:w].astype(np.float32)
    xx *= 2
    yy *= 2  # coordinate a 1920x1080
    c0 = np.array([11, 21, 48], np.float32)   # #0B1530
    c1 = np.array([17, 36, 82], np.float32)
    g = ((xx / 1920 + yy / 1080) / 2)[..., None]
    base = c0 + (c1 - c0) * g
    blue = np.array([32, 96, 175], np.float32)  # #2060AF
    blobs = [  # cx, cy, ax, ay, kx, ky, fase, raggio, alpha
        (400, 300, 220, 140, 1, 2, 0.0, 520, 0.34), (1500, 250, 200, 160, 2, 1, 1.3, 460, 0.28),
        (1000, 900, 300, 120, 1, 1, 2.6, 600, 0.30), (1750, 880, 160, 170, 2, 2, 4.0, 420, 0.24),
        (200, 950, 180, 130, 1, 2, 5.1, 380, 0.22)]
    tmp = WK + '/bg_raw.mkv'
    p = subprocess.Popen(['ffmpeg', '-y', '-v', 'error', '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-s', f'{w}x{h}', '-r', '30', '-i', '-',
                          '-vf', 'scale=1920:1080:flags=bicubic,scale=out_color_matrix=bt709:out_range=tv,format=yuv420p', '-c:v', 'libx264', '-preset', 'veryfast', '-crf', '10',
                          '-colorspace', 'bt709', '-color_primaries', 'bt709', '-color_trc', 'bt709', '-color_range', 'tv', tmp], stdin=subprocess.PIPE)
    N = int(BGP * FPS)
    rng = np.random.default_rng(7)
    dither = (rng.random((h, w, 1)).astype(np.float32) - 0.5)
    for i in range(N):
        a = 2 * math.pi * i / N
        img = base.copy()
        for cx, cy, ax, ay, kx, ky, ph, r, al in blobs:
            x0 = cx + ax * math.cos(kx * a + ph)
            y0 = cy + ay * math.sin(ky * a + ph * 0.7)
            d2 = ((xx - x0) ** 2 + (yy - y0) ** 2) / (r * r)
            m = (al * np.exp(-d2 * 1.6))[..., None]
            img = img * (1 - m) + blue * m
        # anello sottile che si sposta
        rx = 1250 + 260 * math.cos(a + 0.5)
        ry = 600 + 160 * math.sin(a + 2.0)
        d = np.sqrt((xx - rx) ** 2 + (yy - ry) ** 2)
        ring = (0.09 * np.exp(-(((d - 380 - 40 * math.sin(2 * a)) / 2.6) ** 2)))[..., None]
        img = img * (1 - ring) + 255 * ring
        # griglia di punti che scorre piano (64 px ogni ciclo: si ripete senza stacco)
        sx = 64 * i / N
        dx = ((xx - sx) % 64) - 32
        dy = ((yy - sx) % 64) - 32
        dots = (0.11 * np.exp(-(dx * dx + dy * dy) / (2 * 2.2 ** 2)))[..., None]
        img = img * (1 - dots) + 255 * dots
        img = np.clip(img + dither, 0, 255).astype(np.uint8)
        p.stdin.write(img.tobytes())
    p.stdin.close()
    p.wait()
    os.replace(tmp, BG)
    return BG


# ------------------------------------------------------------------ framework delle scene (HTML con render(t))
CSS = S.CSS + """
html,body{background:#fff}
.blue,.blue body{background:transparent}
.bl{color:#fff}
#logo{z-index:5}
.k{font:800 30px/1 Fig;letter-spacing:.2em;color:#FFE600;text-transform:uppercase}
.kb{font:700 24px/1 Fig;letter-spacing:.14em;color:#2060AF;text-transform:uppercase}
.row{position:relative;display:flex;align-items:center;gap:22px;border-radius:20px;background:#fff;border:5px solid #E3E8F0;box-shadow:0 8px 22px rgba(60,70,90,.12);
 font:500 42px/52px Fig;padding:12px 30px;margin-bottom:16px;
 border-color:color-mix(in srgb,#FFE600 calc(var(--a,0)*100%),#E3E8F0);background:color-mix(in srgb,#FFFBD1 calc(var(--a,0)*100%),#fff)}
.row::before{content:"";position:absolute;left:-22px;top:50%;margin-top:-13px;width:26px;height:26px;border-radius:50%;background:#FFE600;opacity:var(--a,0);
 box-shadow:0 0 0 3px #fff,0 2px 8px rgba(60,70,90,.35)}
.row b{font-weight:800}
.num{flex:none;width:54px;height:54px;border-radius:50%;background:#0B1530;color:#fff;font:800 30px/54px Fig;text-align:center}
.txt{flex:1}
.chip{display:inline-block;font:700 28px/1.2 Fig;background:#EEF3FB;border-left:6px solid #2060AF;border-radius:10px;padding:5px 14px;color:#0B1530;margin:4px 0 0 0}
.chips{display:flex;flex-direction:column;align-items:flex-end;gap:4px}
.chipb{display:inline-block;font:700 30px/1.2 Fig;background:rgba(255,255,255,.12);border:2px solid rgba(255,255,255,.35);border-radius:14px;padding:8px 18px;color:#fff;margin-right:14px}
"""
JS = """
const EL=%s;
function ez(x){x=Math.max(0,Math.min(1,x));return 1-Math.pow(1-x,3)}
function eb(x){x=Math.max(0,Math.min(1,x));const c=1.7,k=c+1;return 1+k*Math.pow(x-1,3)+c*Math.pow(x-1,2)}
window.render=function(t){
 const fin=t<0;
 for(const e of EL){
  const d=document.getElementById(e.id);
  let p=ez((t-e.i)/e.d), q=e.o==null?0:ez((t-e.o)/(e.od||.3));
  let a=p*(1-q), lit=0;
  for(const [on,off] of e.l){lit=Math.max(lit,ez((t-on)/.25)*(1-ez((t-off)/.25)))}
  if(fin){a=1;lit=0;p=1}
  else if(e.dim!=null){a*=e.dim+(1-e.dim)*lit}
  let tr='';
  if(e.fx=='up')tr='translateY('+((1-p)*30)+'px)';
  else if(e.fx=='left')tr='translateX('+(-(1-p)*60)+'px)';
  else if(e.fx=='scale')tr='scale('+(0.85+0.15*p)+')';
  else if(e.fx=='bar')tr='scaleX('+p+')';
  else if(e.fx=='pop'){const s=eb((t-e.i)/e.d);tr='scale('+Math.max(0,s)+')';a=(t>=e.i)?1:0;if(fin)a=1}
  else if(e.fx=='play'){const s=eb((t-e.i)/e.d);const pu=(t>e.i+e.d)?1+0.035*Math.sin(2*Math.PI*(t-e.i-e.d)/2.4):1;tr='scale('+Math.max(0,s*pu)+')';a=(t>=e.i)?1:0}
  else if(e.fx=='ring'){const ph=((t-e.i)/2.4+e.ph)%%1;const z=(t>=e.i)?ph:0;tr='scale('+(1+0.9*z)+')';a=(t>=e.i)?0.5*(1-z)*(1-z):0}
  d.style.opacity=a;d.style.visibility=a<0.002?'hidden':'visible';
  d.style.transform=tr;d.style.setProperty('--a',lit);
 }
};
"""


class Scene:
    def __init__(s):
        s.els = []
        s.n = 0

    def add(s, inner, cls='', style='', i=0.0, d=0.5, fx='up', o=None, od=0.3, lit=None, dim=None, cont=None, ph=0.0, tag='div'):
        eid = f'e{s.n}'
        s.n += 1
        s.els.append(dict(id=eid, i=round(i, 4), d=d, fx=fx, o=None if o is None else round(o, 4), od=od,
                          l=[[round(a, 4), round(b, 4)] for a, b in (lit or [])], dim=dim, ph=ph, c=cont))
        return f'<{tag} id="{eid}" class="{cls}" style="opacity:0;visibility:hidden;{style}">{inner}</{tag}>'

    def ranges(s):
        R = []
        for e in s.els:
            R.append((e['i'], e['i'] + e['d']))
            if e['o'] is not None:
                R.append((e['o'], e['o'] + e['od']))
            for a, b in e['l']:
                R.append((a, a + .25))
                R.append((b, b + .25))
            if e['c']:
                R.append(tuple(e['c']))
            if e['fx'] == 'play':
                R.append((e['i'], e['i'] + 60))
            if e['fx'] == 'ring':
                R.append((e['i'], e['i'] + 60))
        return R

    def js(s):
        return JS % json.dumps(s.els)


def pagina(s, body, blue=False, extra_css=''):
    return (f'<!doctype html><html class="{"blue" if blue else ""}"><head><meta charset=utf-8><style>{CSS}{extra_css}</style></head>'
            f'<body class="{"blue" if blue else ""}">{body}<script>{s.js() if s else "window.render=function(){}"}</script></body></html>')


def head_bianco(kick, title, pag=None, foot=True, nl=1, tw=1760):
    top = 188 + nl * 65 + 20
    h = ('<img id=logo src="file:///tmp/w/logo.svg"><div id=hl></div>'
         f'<div id=kick>{esc(kick)}</div><div id=tit style="width:{tw}px">{esc(title)}</div><div id=bar style="top:{top - 6}px"></div>')
    if foot:
        h += '<div id=fl></div><div id=foot>STORIA V</div>' + (f'<div id=pag>Pagina {pag}</div>' if pag else '')
    return h, top


def head_blu():
    return '<img id=logo src="file:///tmp/w/s/logo_w.svg">'


# ------------------------------------------------------------------ rendering fotogrammi e codifica
def render_piece(name, html, sc, N, transparent, finale_png=None):
    """html: testo pagina; sc: Scene (o None). Produce fotogrammi solo dove qualcosa cambia; ritorna lista (frame, file)"""
    h = hashlib.md5((html + str(N)).encode()).hexdigest()[:10]
    d = f'{WK}/fr/{name}'
    hp = f'{WK}/html/{name}.html'
    if not (os.path.exists(d + '/.h') and open(d + '/.h').read() == h):
        shutil.rmtree(d, ignore_errors=True)
    os.makedirs(d, exist_ok=True)
    open(hp, 'w').write(html)
    F = {0, N - 1}
    if sc is not None:
        for a, b in sc.ranges():
            for i in range(max(0, int(math.floor(a * FPS)) - 0), min(N - 1, int(math.ceil((b + 0.02) * FPS))) + 1):
                F.add(i)
    F = sorted(F)
    jobs = [{'html': hp, 'transparent': transparent, 'frames': [{'t': i / FPS, 'out': f'{d}/{i:05d}.png'} for i in F]}]
    if finale_png:
        jobs.append({'html': hp, 'transparent': False, 'frames': [{'t': -1, 'out': finale_png}]})
    jp = f'{WK}/jobs_{name}.json'
    json.dump(jobs, open(jp, 'w'))
    sh(['node', HERE + '/shot2.js', jp], env={**os.environ, 'NODE_PATH': '/opt/node-tools/node_modules'}, cwd=HERE)
    open(d + '/.h', 'w').write(h)
    return [(i, f'{d}/{i:05d}.png') for i in F]


COL = ['-colorspace', 'bt709', '-color_primaries', 'bt709', '-color_trc', 'bt709', '-color_range', 'tv']
X264 = ['-c:v', 'libx264', '-preset', 'veryfast', '-crf', '16', '-pix_fmt', 'yuv420p'] + COL
TOYUV = 'scale=in_range=full:out_range=tv:out_color_matrix=bt709,format=yuv420p'


def codifica(name, frames, N, audio, blue):
    lst = f'{WK}/fr/{name}.txt'
    with open(lst, 'w') as f:
        for k, (i, p) in enumerate(frames):
            nxt = frames[k + 1][0] if k + 1 < len(frames) else N
            f.write(f"file '{p}'\nduration {(nxt - i) / FPS:.6f}\n")
        f.write(f"file '{frames[-1][1]}'\n")
    out = f'{OUT}/{name}.mkv'
    cmd = ['ffmpeg', '-y', '-v', 'error']
    if blue:
        cmd += ['-stream_loop', '-1', '-i', sfondo_blu(), '-f', 'concat', '-safe', '0', '-i', lst, '-i', audio,
                '-filter_complex', f'[0:v]scale=in_range=tv:in_color_matrix=bt709,format=gbrp[b];[1:v]fps={FPS},format=rgba[f];[b][f]overlay=0:0:format=gbrp,{TOYUV}[v]',
                '-map', '[v]', '-map', '2:a']
    else:
        cmd += ['-f', 'concat', '-safe', '0', '-i', lst, '-i', audio, '-vf', f'fps={FPS},{TOYUV}', '-map', '0:v', '-map', '1:a']
    cmd += ['-frames:v', str(N)] + X264 + ['-r', str(FPS), '-c:a', 'pcm_s16le', '-ar', '48000', '-ac', '2', out]
    sh(cmd)
    return out


def verifica_pezzo(name, N):
    out = f'{OUT}/{name}.mkv'
    r = sh(['ffprobe', '-v', 'error', '-count_packets', '-select_streams', 'v:0', '-show_entries', 'stream=nb_read_packets,width,height', '-of', 'csv=p=0', out]).stdout.strip()
    nf = int(r.split(',')[2]) if r.count(',') >= 2 else int(r.split(',')[-1])
    da = dur(out)
    return nf, da


def costruisci(name, T, html, sc, voci=(), jingoli=(), blue=False, note='', extra=None, finale_png=None):
    """T = durata (s) del pezzo, arrotondata ai 1/30 s"""
    N = nfr(T)
    T = N / FPS
    aud = f'{WK}/aud/mix_{name}.wav'
    mix_audio(aud, T, list(voci), list(jingoli))
    fr = render_piece(name, html, sc, N, blue, finale_png)
    codifica(name, fr, N, aud, blue)
    shutil.rmtree(f'{WK}/fr/{name}', ignore_errors=True)
    for x in (aud, f'{WK}/fr/{name}.txt'):
        if os.path.exists(x):
            os.remove(x)
    sid = {'durata_s': round(T, 6), 'frame': N, 'voci': [v for v, _ in voci], 'jingle': [j for j, _ in jingoli], 'note': note}
    prov = [v for v, _ in voci if voce_provvisoria(v)]
    if prov:
        sid['voci_provvisorie'] = prov
    if extra:
        sid.update(extra)
    json.dump(sid, open(f'{OUT}/{name}.json', 'w'), ensure_ascii=False, indent=1)
    for v, _ in voci:
        if not voce_provvisoria(v):
            b = bordo_voce(voce(v)[0])
            if b >= 0.03:
                NOTE.append(f'ATTENZIONE {name}: voce {v} bordo finale {b:.3f} >= 0,03')
    print(f'{name}: {T:.3f} s ({N} fotogrammi)' + (f' PROVVISORIO {prov}' if prov else ''), flush=True)
    return T


# ================================================================== PEZZI
def converti(src, name, secondi):
    out = f'{OUT}/{name}.mkv'
    N = int(round(secondi * FPS))
    sh(['ffmpeg', '-y', '-v', 'error', '-i', src, '-vf', f'fps={FPS},scale=1920:1080,{TOYUV.replace("in_range=full:", "")}',
        '-af', f'aresample=48000,apad=whole_dur={secondi},atrim=0:{secondi}',
        '-frames:v', str(N)] + X264 + ['-r', str(FPS), '-c:a', 'pcm_s16le', '-ar', '48000', '-ac', '2', out])
    json.dump({'durata_s': secondi, 'frame': N, 'voci': [], 'note': f'{os.path.basename(src)} convertita senza modifiche'}, open(f'{OUT}/{name}.json', 'w'), ensure_ascii=False, indent=1)
    print(f'{name}: {secondi} s')


def p_SIG():
    converti(REPO + '/kit/sigle/Sigla_Storia_15s.mp4', 'SIG', 15.0)


def p_SFIN():
    converti(REPO + '/kit/sigle/Sigla_finale_5s_con_avviso_diritti.mp4', 'SFIN', 5.0)


# ---------- copertine
COVER_CSS = """
#kick{top:150px}
#tit{top:196px;font:800 96px/1.04 Bri;width:1300px}
#bar2{position:absolute;left:80px;top:420px;width:85px;height:7px;border-radius:4px;background:#2060AF}
#arg{position:absolute;left:80px;top:470px;width:1300px;background:#F6F9FD;border-radius:22px;box-shadow:0 12px 30px rgba(60,70,90,.14);padding:26px 40px 18px 40px;border:3px solid #E3E8F0}
#arg h4{font:800 22px Fig;letter-spacing:.16em;color:#2060AF;margin-bottom:14px}
.ar{display:flex;gap:18px;align-items:flex-start;font:700 36px/46px Fig;color:#0B1530;padding:7px 14px;margin:0 -14px 6px -14px;border-radius:14px;border:4px solid transparent;
 border-color:color-mix(in srgb,#FFE600 calc(var(--a,0)*100%),transparent);background:color-mix(in srgb,#FFF7B8 calc(var(--a,0)*100%),transparent)}
.ar i{flex:none;font:800 28px/46px Fig;font-style:normal;color:#2060AF;width:40px}
#avv{position:absolute;left:0;right:0;top:1010px;text-align:center;font:500 24px/30px Fig;color:#3A4254;padding:0 230px}
"""


def cover_page(parte, prof, sc=None, items=None):
    """items: html delle righe argomenti (già avvolte da Scene.add) oppure None per statico"""
    args = PARTE[parte]
    base, top = head_bianco(f'STORIA V · VIDEOLEZIONE · PARTE {parte}', 'X', pag=1, foot=True, nl=2, tw=1300)
    base = re.sub(r'<div id=tit.*?</div>', '<div id=tit>La guerra fredda<br>(1945-1961)</div>', base)
    base = re.sub(r'<div id=bar [^>]*></div>', '<div id=bar2></div>', base)
    if items is None:
        lis = ''.join(f'<div class="ar"><i>{n}</i><span>{esc(ARGT[n])}</span></div>' for n in args)
    else:
        lis = items
    cam = '<div id=cam></div><div id=band><b>Giorgio Mazzotti</b><i>PROF. DI STORIA</i></div>' if prof else ''
    rows = ''
    body = (base + f'<div id=arg><h4>ARGOMENTI</h4>{lis}</div>' + cam + f'<div id=avv>{esc(AVVISO)}</div>')
    return body


def p_COVER():
    for parte in (1, 2):
        for prof in (False, True):
            body = cover_page(parte, prof)
            hp = f'{WK}/html/COVER{parte}{"_prof" if prof else ""}.html'
            open(hp, 'w').write(pagina(None, body, extra_css=COVER_CSS))
            out = f'{OUT}/COVER{parte}{"_prof" if prof else ""}.png'
            if os.path.exists(out):
                os.remove(out)
            jp = f'{WK}/jobs_cover{parte}{int(prof)}.json'
            json.dump([{'html': hp, 'transparent': False, 'frames': [{'t': 0, 'out': out}]}], open(jp, 'w'))
            sh(['node', HERE + '/shot2.js', jp], env={**os.environ, 'NODE_PATH': '/opt/node-tools/node_modules'}, cwd=HERE)
            print('COVER', parte, prof, 'ok')


def p_CW(parte):
    nome = f'W{parte}_R2'
    args = PARTE[parte]
    testo = TESTI[nome]
    f, d, pv = voce(nome)
    # unità di testo per l'accensione degli argomenti: prima dei due punti, poi un'unità per argomento
    pre, _, resto = testo.partition(': ')
    parti_r = re.split(r',\s+|\s+e\s+(?=la guerra fredda in Asia)', resto) if parte == 2 else None
    if parte == 1:
        m = re.match(r'^(il dopoguerra), (Bretton Woods e il bipolarismo), (la dottrina Truman e il blocco di Berlino\.)$', resto)
        parti_r = list(m.groups())
    else:
        parti_r = [x for x in re.split(r",\s+|\s+e\s+(?=la guerra fredda)", resto)]
        if len(parti_r) != 4:
            parti_r = re.split(r',\s+|\s+e\s+(?=la guerra)', resto)
    unita = [pre + ':'] + parti_r
    ts = tempi_unita(nome, unita)
    T0 = 0.3
    tt = [T0 + t for t in ts]
    fine = T0 + d
    sc = Scene()
    items = ''
    for k, n in enumerate(args):
        on = tt[k + 1] - 0.05
        off = (tt[k + 2] - 0.05) if k + 2 < len(tt) else fine + 0.4
        items += sc.add(f'<i>{n}</i><span>{esc(ARGT[n])}</span>', 'ar', '', i=0.9 + 0.25 * k, d=0.5, fx='left', lit=[(on, off)])
    body = cover_page(parte, False, items=items)
    T = fine + 0.6
    costruisci(f'CW{parte}', T, pagina(sc, body, extra_css=COVER_CSS), sc, voci=[(nome, T0)],
               note=f'copertina Parte {parte} senza riquadro del docente con la voce di benvenuto {nome}; poi il montaggio mette COVER{parte}_prof.png' + (' (VOCE PROVVISORIA: silenzio)' if pv else ''))


# ---------- schede titolo / quiz / pillola (blu)
def p_T(n):
    sc = Scene()
    parte = 1 if n <= 3 else 2
    ghost = sc.add(f'{n}', '', 'position:absolute;right:70px;top:40px;font:800 820px/1 Bri;color:rgba(255,255,255,.055)', i=0.0, d=1.2, fx='scale')
    k = sc.add(f'ARGOMENTO {n}', 'k', '', i=0.25, d=0.55, fx='up')
    t = sc.add(esc(ARGT[n]), '', 'font:800 100px/1.04 Bri;color:#fff;margin-top:30px', i=0.5, d=0.7, fx='up')
    b = sc.add('', '', 'width:170px;height:12px;border-radius:6px;background:#FFE600;margin-top:44px;transform-origin:left', i=1.0, d=0.6, fx='bar')
    seg = ''.join(f'<span style="display:inline-block;width:78px;height:14px;border-radius:7px;margin-right:12px;background:{"#FFE600" if i == n else ("rgba(255,255,255,.85)" if i < n else "rgba(255,255,255,.28)")}"></span>' for i in range(1, 8))
    pr = sc.add(seg + f'<span style="font:700 36px Fig;color:#fff;margin-left:14px;vertical-align:middle">{n} / 7</span>', '', 'margin-top:70px', i=1.3, d=0.6, fx='up')
    body = head_blu() + ghost + f'<div style="position:absolute;left:120px;top:300px;width:1480px">{k}{t}{b}{pr}</div>'
    costruisci(f'T{n}', 4.0, pagina(sc, body, blue=True), sc, jingoli=[('titolo', 0.0)], blue=True,
               note=f'scheda titolo argomento {n}/7 (solo jingle titolo.wav)')


def p_Q(n):
    sc = Scene()
    ring = ''.join(sc.add('', '', 'position:absolute;left:150px;top:380px;width:280px;height:280px;border-radius:50%;border:6px solid #FFE600', i=0.5, d=0.1, fx='ring', ph=ph / 3) for ph in range(3))
    play = sc.add('<svg width="280" height="280" viewBox="0 0 280 280"><circle cx="140" cy="140" r="140" fill="#FFE600"/><path d="M112 82 L202 140 L112 198 Z" fill="#0B1530"/></svg>',
                  '', 'position:absolute;left:150px;top:380px', i=0.5, d=0.55, fx='play')
    k = sc.add('QUIZ', 'k', 'position:absolute;left:560px;top:372px', i=0.65, d=0.5, fx='up')
    t = sc.add(f'Quiz {n} · {esc(ARGT[n])}', '', 'position:absolute;left:560px;top:420px;width:1240px;font:800 78px/1.06 Bri;color:#fff', i=0.8, d=0.6, fx='up')
    pill = sc.add('5 domande · serve almeno l’80% per continuare', '', 'position:absolute;left:560px;top:690px;font:700 38px/1.2 Fig;color:#fff;background:rgba(255,255,255,.13);border:2px solid rgba(255,255,255,.4);border-radius:60px;padding:14px 36px',
                  i=1.3, d=0.6, fx='up')
    body = head_blu() + ring + play + k + t + pill
    costruisci(f'Q{n}', 5.0, pagina(sc, body, blue=True), sc, jingoli=[('quiz', 0.5)], blue=True,
               note='scheda Quiz: 5 domande, 80%; le domande NON sono nel video (si fanno sulla piattaforma)', extra={'quiz_s': 0.5})


def p_PI(n):
    nome = f'PIA{n}'
    testo = TESTI[nome]
    f, d, pv = voce(nome)
    t = cifre(testo)
    m = re.match(r'^(.*?:)\s*(.+)$', t)
    if m:
        lead, big = m.group(1), m.group(2)
    elif t.startswith('Ripassiamo insieme '):
        lead, big = 'Ripassiamo insieme', t[len('Ripassiamo insieme '):]
    else:
        lead, big = '', t
    sc = Scene()
    k = sc.add(f'PILLOLA DI RIPASSO · ARGOMENTO {n}', 'k', '', i=0.2, d=0.5, fx='up')
    l1 = sc.add(esc(lead), '', 'font:700 52px/1.15 Fig;color:rgba(255,255,255,.88);margin-top:44px', i=0.4, d=0.6, fx='up') if lead else ''
    bg = sc.add(esc(big), '', 'font:800 86px/1.06 Bri;color:#fff;margin-top:22px', i=0.75, d=0.7, fx='up')
    b = sc.add('', '', 'width:170px;height:12px;border-radius:6px;background:#FFE600;margin-top:40px;transform-origin:left', i=1.3, d=0.6, fx='bar')
    sg = sigle_in(testo.replace('ONU', 'ONU'))
    ch = sc.add(chips(sg, 'chipb'), '', 'position:absolute;left:120px;top:860px', i=1.7, d=0.6, fx='up') if sg else ''
    body = head_blu() + f'<div style="position:absolute;left:120px;top:250px;width:1560px">{k}{l1}{bg}{b}</div>' + ch
    T = max(5.5, 0.3 + d + 1.6)
    costruisci(f'PI{n}', T, pagina(sc, body, blue=True), sc, voci=[(nome, 0.3)], jingoli=[('repaso', 0.0)], blue=True,
               note=f'pillola di introduzione al ripasso, argomento {n}, voce {nome}' + (' (provvisoria)' if pv else ''))


# ---------- schema di ripasso (bianco)
def righe_ps(n):
    out = []
    for j in range(1, 7):
        t = f'PR{n}{j}'
        if t in TESTI:
            out.append((t, cifre(TESTI[t])))
    return out


def p_PS(n):
    righe = righe_ps(n)
    pib, dpib, _ = voce('PIB')
    parte = 1 if n <= 3 else 2
    pag = pagina_ps(n)
    sc = Scene()
    T0 = 0.3
    t = T0 + dpib + 0.45
    starts = []
    for nome, _ in righe:
        starts.append(t)
        t += voce(nome)[1] + 0.35
    fine = starts[-1] + voce(righe[-1][0])[1]
    head, top = head_bianco(f'RIPASSO · ARGOMENTO {n}', ARGT[n], pag=pag)
    rows = ''
    for j, (nome, tx) in enumerate(righe):
        lead, body = S.split_card(tx)
        sg = sigle_in(tx)
        inner = (f'<div class="num">{j + 1}</div><div class="txt">' + (f'<b>{esc(lead)}:</b> ' if lead else '') + esc(body) + '</div>' +
                 (f'<div class="chips">{chips(sg)}</div>' if sg else ''))
        on = starts[j] - 0.05
        off = (starts[j + 1] - 0.05) if j + 1 < len(righe) else fine + 0.5
        rows += sc.add(inner, 'row', '', i=0.55 + 0.3 * j, d=0.5, fx='up', lit=[(on, off)], dim=0.78)
    body = head + f'<div style="position:absolute;left:80px;width:1760px;top:{top + 28}px">{rows}</div>'
    T = fine + 0.6
    costruisci(f'PS{n}', T, pagina(sc, body), sc, voci=[('PIB', T0)] + [(nome, s) for (nome, _), s in zip(righe, starts)],
               note=f'schema di ripasso argomento {n}: {len(righe)} righe accese a tempo con le voci PR{n}x', finale_png=f'{OUT}/PS{n}_finale.png')


# ---------- glossario
def p_GL(parte):
    nome = f'GL{parte}'
    testo = TESTI[nome]
    f, d, pv = voce(nome)
    frasi = re.split(r'(?<=\.)\s+', testo.strip())
    intro, voci_ = frasi[0], frasi[1:]
    ents = []
    for fr in voci_:
        term, _, ex = fr.partition(': ')
        ents.append((term, ex))
    ts = tempi_unita(nome, frasi)
    T0 = 0.3
    tt = [T0 + x for x in ts]
    npag = math.ceil(len(ents) / 4)
    base, extra = divmod(len(ents), npag)
    sizes = [base + (1 if i < extra else 0) for i in range(npag)]
    sc = Scene()
    pagine = []
    idx = 0
    for pg, sz in enumerate(sizes):
        cards = ''
        first = tt[1 + idx]
        last_next = tt[1 + idx + sz] if 1 + idx + sz < len(tt) else T0 + d + 0.2
        for q in range(sz):
            term, ex = ents[idx + q]
            on = tt[1 + idx + q] - 0.05
            off = (tt[2 + idx + q] - 0.05) if 2 + idx + q < len(tt) else T0 + d + 0.5
            if pg < npag - 1 and q == sz - 1:
                off = last_next - 0.45
            sg = sigle_in(term + ' ' + ex)
            exs = cifre(ex)
            inner = (f'<div style="font:800 52px/1.1 Bri;color:#2060AF">{esc(cifre(term))}</div>'
                     f'<div style="font:500 38px/48px Fig;color:#0B1530;margin-top:8px">{esc(exs[0].upper() + exs[1:])}</div>' +
                     (f'<div style="margin-top:6px">{chips(sg)}</div>' if sg else ''))
            cards += sc.add(inner, 'gc', '', i=on, d=0.5, fx='up', lit=[(on, off)], dim=0.72, o=(last_next - 0.4) if pg < npag - 1 else None, od=0.3)
        pagine.append(f'<div class="grid">{cards}</div>')
        idx += sz
    head, top = head_bianco(f'PAROLE CHIAVE · PARTE {parte}', 'Glossario', pag=None, foot=True)
    css = """.grid{position:absolute;left:80px;top:TOPPXpx;width:1760px;display:grid;grid-template-columns:860px 860px;gap:18px 40px;align-items:start}
.gc{border-radius:20px;background:#fff;box-shadow:0 8px 22px rgba(60,70,90,.12);padding:20px 30px 22px 30px;min-height:210px;
 border:5px solid color-mix(in srgb,#FFE600 calc(var(--a,0)*100%),#E3E8F0);background:color-mix(in srgb,#FFFBD1 calc(var(--a,0)*100%),#fff);position:relative}
.gc::before{content:"";position:absolute;left:-22px;top:30px;width:26px;height:26px;border-radius:50%;background:#FFE600;opacity:var(--a,0);box-shadow:0 0 0 3px #fff,0 2px 8px rgba(60,70,90,.35)}""".replace("TOPPX",str(top + 28))
    body = head + ''.join(pagine)
    T = T0 + d + 0.6
    costruisci(f'GL{parte}', T, pagina(sc, body, extra_css=css), sc, voci=[(nome, T0)],
               note=f'glossario animato Parte {parte}: {len(ents)} termini in {npag} schermate, accesi a tempo con la voce {nome}')


# ---------- ripasso finale
def p_FIN(parte):
    args = PARTE[parte]
    rf, fn = f'RF{parte}', f'FIN{parte}'
    frasi = re.split(r'(?<=\.)\s+', TESTI[rf].strip())
    intro, arg_f = frasi[0], frasi[1:]
    assert len(arg_f) == len(args), (parte, len(arg_f))
    d1 = voce(rf)[1]
    d2 = voce(fn)[1]
    ts1 = tempi_unita(rf, frasi)
    T0 = 0.3
    A = [T0 + x for x in ts1]
    T1 = T0 + d1 + 0.7
    sc = Scene()
    head, top = head_bianco(f'RIPASSO FINALE · PARTE {parte}', 'Ripasso finale', pag=None)
    rows = ''
    n = len(args)
    rh = 124
    for k, a in enumerate(args):
        sg = sigle_in(arg_f[k])
        tx = cifre(arg_f[k])
        inner = (f'<div class="num">{a}</div><div style="flex:none;width:470px;font:800 34px/1.1 Bri;color:#2060AF">{esc(ARGT[a])}</div>'
                 f'<div class="txt" style="font:500 32px/42px Fig">{esc(tx)}' + (f'<div style="margin-top:2px">{chips(sg)}</div>' if sg else '') + '</div>')
        on = A[k + 1] - 0.05
        off = (A[k + 2] - 0.05) if k + 2 < len(A) else T0 + d1 + 0.4
        rows += sc.add(inner, 'row', 'font-size:32px;margin-bottom:12px', i=0.5 + 0.3 * k, d=0.5, fx='up', lit=[(on, off)], dim=0.78)
    body = head
    if parte == 1:
        body += f'<div style="position:absolute;left:80px;width:1760px;top:{top + 26}px">{rows}</div>'
        txt = TESTI[fn]
        un = ['Per oggi è tutto.', 'Nella seconda parte vedremo', 'le due Europe,', 'gli Stati Uniti degli anni Cinquanta,', 'il blocco orientale dopo Stalin', 'e la guerra fredda in Asia.', 'Ti aspetto.']
        assert ' '.join(un) == txt, txt
        tt = [T1 + x for x in tempi_unita(fn, un)]
        lab = sc.add('NELLA SECONDA PARTE', 'kb', 'position:absolute;left:80px;top:760px', i=T1 - 0.2, d=0.5, fx='up')
        topics = ['Le due Europe', 'Gli Stati Uniti degli anni Cinquanta', 'Il blocco orientale dopo Stalin', 'La guerra fredda in Asia']
        chs = ''
        for q, tp in enumerate(topics):
            on = tt[2 + q] - 0.05
            off = (tt[3 + q] - 0.05) if q < 3 else T1 + d2 + 0.4
            x = 80 + (q % 2) * 890
            y = 806 + (q // 2) * 78
            chs += sc.add(f'<div class="num" style="width:44px;height:44px;font-size:26px;line-height:44px">{q + 4}</div><div class="txt" style="font:700 34px/44px Fig">{esc(tp)}</div>',
                          'row', f'position:absolute;left:{x}px;top:{y}px;width:860px;margin:0;padding:6px 24px', i=T1 - 0.1 + 0.15 * q, d=0.5, fx='up', lit=[(on, off)], dim=0.78)
        body += lab + chs
    else:
        tt = [T1 + x for x in tempi_unita(fn, [s for s in re.split(r'(?<=\.)\s+', TESTI[fn].strip())])]
        fr = re.split(r'(?<=\.)\s+', TESTI[fn].strip())
        blk = ''
        b1 = f'<div style="font:700 34px/42px Fig;color:#fff;padding:6px 0">{esc(cifre(fr[0]))}</div>'
        b2 = sc.add(esc(cifre(fr[1])), '', 'font:800 38px/46px Fig;color:#FFE600;padding:6px 0', i=tt[1] - 0.05, d=0.5, fx='up')
        blk = sc.add(b1 + b2, '', 'border-radius:22px;background:#0B1530;box-shadow:0 12px 30px rgba(60,70,90,.25);padding:14px 40px;margin-top:6px', i=T1 - 0.3, d=0.5, fx='up')
        body += f'<div style="position:absolute;left:80px;width:1760px;top:{top + 26}px">{rows}{blk}</div>'
    T = T1 + d2 + 0.6
    costruisci(f'FIN{parte}', T, pagina(sc, body), sc, voci=[(rf, T0), (fn, T1)],
               note=f'ripasso finale Parte {parte}: voci {rf} + {fn}; righe accese con la voce' + (' ; chiude con «nella seconda parte vedremo…»' if parte == 1 else ' ; chiude con la conclusione e l’invito alla verifica'))


# ---------- verifica, compiti
def p_VER():
    sc = Scene()
    k = sc.add('VERIFICA FINALE', 'k', '', i=0.5, d=0.5, fx='up')
    t = sc.add('Verifica di sbarramento', '', 'font:800 112px/1.05 Bri;color:#fff;margin-top:30px', i=0.7, d=0.7, fx='up')
    b = sc.add('', '', 'width:170px;height:12px;border-radius:6px;background:#FFE600;margin-top:40px;transform-origin:left', i=1.2, d=0.6, fx='bar')
    pills = ''
    for q, tx in enumerate(['10 domande a risposta multipla', 'Soglia di superamento: 80%', 'Almeno 8 risposte giuste su 10']):
        pills += sc.add(esc(tx), '', 'display:inline-block;font:700 38px/1.2 Fig;color:#fff;background:rgba(255,255,255,.13);border:2px solid rgba(255,255,255,.4);border-radius:60px;padding:14px 34px;margin:0 18px 0 0',
                        i=1.7 + 0.35 * q, d=0.6, fx='up')
    body = head_blu() + f'<div style="position:absolute;left:120px;top:300px;width:1620px">{k}{t}{b}<div style="margin-top:70px">{pills}</div></div>'
    costruisci('VER', 6.0, pagina(sc, body, blue=True), sc, jingoli=[('repaso', 0.3)], blue=True,
               note='scheda Verifica di sbarramento (soglia 80%, 10 domande, test del prof coincidente con verifica_finale.json)')


def p_CINTRO():
    sc = Scene()
    k = sc.add('ORA TOCCA A TE', 'k', '', i=0.3, d=0.5, fx='up')
    t = sc.add('Compiti', '', 'font:800 190px/1 Bri;color:#fff;margin-top:26px', i=0.5, d=0.7, fx='up')
    b = sc.add('', '', 'width:200px;height:14px;border-radius:7px;background:#FFE600;margin-top:46px;transform-origin:left', i=1.1, d=0.6, fx='bar')
    body = head_blu() + f'<div style="position:absolute;left:120px;top:310px;width:1620px">{k}{t}{b}</div>'
    costruisci('CINTRO', 3.5, pagina(sc, body, blue=True), sc, jingoli=[('titolo', 0.0)], blue=True, note='intro Compiti con jingle titolo.wav')


def p_COMP():
    es = COMPITI['esercizi']
    sc = Scene()
    head, top = head_bianco('ORA TOCCA A TE', 'Compiti', pag=None)
    per = 15.0
    gruppi = [es[i:i + 2] for i in range(0, len(es), 2)]
    pagine = ''
    t0 = 1.0
    for gi, g in enumerate(gruppi):
        rows = ''
        fine_g = t0 + len(g) * per + 0.5
        for q, e in enumerate(g):
            tx = re.sub(r'"([^"]*)"', r'«\1»', e['testo'])
            on = t0 + 0.6 + q * per
            off = on + per
            rows += sc.add(f'<div class="num">{e["n"]}</div><div class="txt" style="font:500 40px/54px Fig">{esc(tx)}</div>', 'row',
                           'font-size:40px;align-items:flex-start;margin-bottom:22px;padding:18px 34px', i=t0 + 0.1 + 0.4 * q, d=0.5, fx='up', lit=[(on, off)], dim=0.8,
                           o=(fine_g - 0.4) if gi < len(gruppi) - 1 else None, od=0.3)
        pagine += f'<div style="position:absolute;left:80px;width:1760px;top:{top + 24}px">{rows}</div>'
        t0 = fine_g
    body = head + pagine
    T = t0 + 0.2
    costruisci('COMP', T, pagina(sc, body), sc, jingoli=[('repaso', 0.0)], note='compiti del docente (compiti.json), 4 esercizi in 2 schermate, ognuno acceso 15 s')


def main():
    argv = sys.argv[1:]
    tutti = ['SIG', 'SFIN', 'COVER', 'CW1', 'CW2'] + [f'T{n}' for n in range(1, 8)] + [f'PI{n}' for n in range(1, 8)] + [f'PS{n}' for n in range(1, 8)] + \
            [f'Q{n}' for n in range(1, 8)] + ['GL1', 'GL2', 'FIN1', 'FIN2', 'VER', 'CINTRO', 'COMP']
    if '--voci' in argv:
        argv = ['CW1', 'CW2']
    req = argv or tutti
    for r in req:
        if r == 'SIG':
            p_SIG()
        elif r == 'SFIN':
            p_SFIN()
        elif r == 'COVER':
            p_COVER()
        elif r in ('CW1', 'CW2'):
            p_CW(int(r[2]))
        elif re.match(r'^T\d$', r):
            p_T(int(r[1:]))
        elif re.match(r'^PI\d$', r):
            p_PI(int(r[2:]))
        elif re.match(r'^PS\d$', r):
            p_PS(int(r[2:]))
        elif re.match(r'^Q\d$', r):
            p_Q(int(r[1:]))
        elif r in ('GL1', 'GL2'):
            p_GL(int(r[2]))
        elif r in ('FIN1', 'FIN2'):
            p_FIN(int(r[3]))
        elif r == 'VER':
            p_VER()
        elif r == 'CINTRO':
            p_CINTRO()
        elif r == 'COMP':
            p_COMP()
        else:
            print('pezzo sconosciuto', r)
    for n in NOTE:
        print(n)


if __name__ == '__main__':
    main()
