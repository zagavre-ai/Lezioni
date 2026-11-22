#!/usr/bin/env python3
"""Approfondimenti animati (AN*) e spiegone (RIP2) della lezione 14.
Uso:  python3 animazioni.py [NOME ...]      (senza argomenti: tutti i pezzi)
      python3 animazioni.py --solo-aud NOME  (solo audio/durata)   --frame NOME t  (un fotogramma di prova)
Ogni pezzo -> /tmp/w/pezzi/<NOME>.mkv + .json.  Le voci stanno in VOX; le trascrizioni in /tmp/w/an/asr (si rifanno da sole).
Se una voce cambia (nuovo wav) cancella /tmp/w/an/asr/<VOCE>.json e rilancia: tempi, durate e confronto col testo si rifanno da soli."""
import sys, os, re, json, math, wave, subprocess, difflib, unicodedata, html, shutil
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
REPO = '/home/user/Lezioni'
VOX = '/tmp/w/vox/scambio/storia-V-lez14/vox'
AN = '/tmp/w/an'; PZ = '/tmp/w/pezzi'; ASR = AN + '/asr'
for d in (AN, PZ, ASR, AN + '/fr'): os.makedirs(d, exist_ok=True)
FPS = 30
TESTI = {v['nome']: v['testo'] for v in json.load(open('/tmp/w/old/testi_voci.json'))}
if os.path.exists('/tmp/w/voci_nuove.json'):
    try:
        for v in json.load(open('/tmp/w/voci_nuove.json')): TESTI[v['nome']] = v['testo']
    except Exception: pass

def sh(cmd, **k):
    r = subprocess.run(cmd, shell=isinstance(cmd, str), capture_output=True, text=True, **k)
    if r.returncode: raise RuntimeError(str(cmd)[:300] + '\n' + r.stderr[-1500:])
    return r

# ------------------------------------------------------------------ numeri in lettere (per confrontare la trascrizione)
U = ['zero', 'uno', 'due', 'tre', 'quattro', 'cinque', 'sei', 'sette', 'otto', 'nove', 'dieci', 'undici', 'dodici', 'tredici', 'quattordici', 'quindici', 'sedici', 'diciassette', 'diciotto', 'diciannove']
T10 = ['', '', 'venti', 'trenta', 'quaranta', 'cinquanta', 'sessanta', 'settanta', 'ottanta', 'novanta']
def num_it(n):
    if n < 20: return U[n]
    if n < 100:
        t, u = divmod(n, 10); w = T10[t]
        if u in (1, 8): w = w[:-1]
        return w + (U[u] if u else '')
    if n < 1000:
        c, r = divmod(n, 100); w = 'cento' if c == 1 else U[c] + 'cento'
        if r and 80 <= r < 90: w = w[:-1]
        return w + (num_it(r) if r else '')
    m, r = divmod(n, 1000); w = 'mille' if m == 1 else num_it(m) + 'mila'
    return w + (num_it(r) if r else '')
def chiave(w):
    w = unicodedata.normalize('NFD', w.lower()); w = w.encode('ascii', 'ignore').decode()
    w = re.sub(r'(\d+)', lambda m: num_it(int(m.group(1))) if int(m.group(1)) < 1000000 else m.group(1), w)
    return re.sub(r'[^a-z0-9]', '', w)

# ------------------------------------------------------------------ voci: tempi parola per parola
def asr_words(nome):
    f = f'{ASR}/{nome}.json'
    if not os.path.exists(f):
        sh(['python3', REPO + '/kit/tools/trascrivi.py', f'{VOX}/{nome}.wav', f'{ASR}/{nome}'])
    out = []; cur = None
    for s in json.load(open(f)):
        for t, tok in s['parole']:
            if tok.startswith(' '):
                if cur and cur[1].strip(): out.append(cur)
                cur = [t, tok.strip()]
            else:
                if cur is None: cur = [t, tok]
                else:
                    if not cur[1].strip(): cur[0] = t
                    cur[1] += tok
    if cur and cur[1].strip(): out.append(cur)
    return [(t, w) for t, w in out if chiave(w)]

def wav_info(nome):
    w = wave.open(f'{VOX}/{nome}.wav'); sr = w.getframerate()
    x = np.frombuffer(w.readframes(w.getnframes()), np.int16).astype(np.float64) / 32768
    return x, sr

class Voce:
    """Tempi (in secondi dall'inizio del file ritagliato) di ogni parola del testo."""
    def __init__(self, nome):
        self.nome = nome
        x, sr = wav_info(nome); a = np.abs(x); idx = np.where(a > 0.012)[0]
        self.cut0 = max(0, idx[0] / sr - 0.04); self.cut1 = min(len(x) / sr, idx[-1] / sr + 0.06)
        self.dur = self.cut1 - self.cut0
        self.testo = TESTI.get(nome, '')
        tw = self.testo.split(); self.parole = tw
        tk = [chiave(w) for w in tw]
        aw = asr_words(nome); ak = [chiave(w) for t, w in aw]
        sm = difflib.SequenceMatcher(None, tk, ak, autojunk=False)
        tempo = [None] * len(tw)
        for i, j, n in sm.get_matching_blocks():
            for k in range(n): tempo[i + k] = aw[j + k][0]
        # parole non agganciate: se il blocco ha stessa lunghezza si accoppiano, altrimenti si interpola
        for tag, i1, i2, j1, j2 in sm.get_opcodes():
            if tag == 'replace' and (i2 - i1) == (j2 - j1):
                for k in range(i2 - i1): tempo[i1 + k] = aw[j1 + k][0]
        known = [(i, t) for i, t in enumerate(tempo) if t is not None]
        self.match = len(known) / max(1, len(tw))
        self.non_agganciate = [tw[i] for i, t in enumerate(tempo) if t is None]
        if not known: known = [(0, 0.1), (len(tw) - 1, self.dur - 0.3)]
        xs = [i for i, t in known]; ys = [t for i, t in known]
        self.t = [float(np.interp(i, xs, ys)) - self.cut0 for i in range(len(tw))]
        self.t = [max(0.0, v) for v in self.t]
        # confronto numeri: ogni parola-numero del testo deve avere una corrispondenza esatta
        self.numeri_ko = [tw[i] for i in range(len(tw)) if re.match(r'^(mille|millenove|cento|[a-z]*(cento|mila))', chiave(tw[i])) and tempo[i] is None]
        self.asr_testo = ' '.join(w for t, w in aw)
    def a(self, parola, nth=0, dopo=None):
        """tempo (nel pezzo) della parola (prefisso, senza maiuscole/accenti), nth-esima occorrenza dopo la parola 'dopo' (indice)"""
        k = chiave(parola); n = 0; start = 0
        if isinstance(dopo, str): start = self.idx(dopo) + 1
        elif isinstance(dopo, int): start = dopo
        for i in range(start, len(self.parole)):
            if self._m(i, k):
                if n == nth: return self.t[i]
                n += 1
        raise KeyError(f'{self.nome}: parola {parola!r} (#{nth}) non trovata')
    def _m(self, i, k):
        w = self.parole[i]
        return chiave(w).startswith(k) or ("'" in w and chiave(re.split(r"['’]", w, maxsplit=1)[1]).startswith(k))
    def idx(self, parola, nth=0):
        k = chiave(parola); n = 0
        for i, w in enumerate(self.parole):
            if self._m(i, k):
                if n == nth: return i
                n += 1
        raise KeyError(parola)
    def fine(self): return self.dur

class Pezzo:
    """Raccoglie le voci di un pezzo e traduce i tempi voce -> tempo del pezzo."""
    LEAD = 0.3; TAIL = 0.6
    def __init__(self, nome, voci, gap=1.0):
        self.nome = nome; self.voci = [Voce(v) for v in voci]; self.gap = gap
        self.off = []; t = self.LEAD
        for v in self.voci: self.off.append(t); t += v.dur + gap
        self.fine_voce = t - gap
        n = math.ceil((self.fine_voce + self.TAIL) * FPS - 1e-6); self.nfr = n; self.dur = n / FPS
    def v(self, i=0):
        P = self; V = P.voci[i]; o = P.off[i]
        class R:
            def __call__(s, parola, nth=0, dopo=None, pre=0.0): return o + V.a(parola, nth, dopo) - pre
            inizio = o; fine = o + V.dur
        return R()

# ------------------------------------------------------------------ audio
def audio_pezzo(P, out):
    """voci ritagliate ai bordi, dissolvenza 30 ms, 48 kHz stereo, -16 LUFS, trans.wav (circa -22 LUFS) nella pausa interna."""
    SR = 48000; tot = int(round(P.dur * SR)); buf = np.zeros(tot)
    for V, o in zip(P.voci, P.off):
        tmp = f'{AN}/_v_{V.nome}.f32'
        sh(['ffmpeg', '-y', '-v', 'error', '-ss', f'{V.cut0:.4f}', '-t', f'{V.dur:.4f}', '-i', f'{VOX}/{V.nome}.wav', '-ar', str(SR), '-ac', '1', '-f', 'f32le', tmp])
        y = np.fromfile(tmp, np.float32).astype(np.float64); os.remove(tmp)
        f = int(0.03 * SR); y[:f] *= np.linspace(0, 1, f); y[-f:] *= np.linspace(1, 0, f)
        i0 = int(round(o * SR)); n = min(len(y), tot - i0); buf[i0:i0 + n] += y[:n]
    raw = f'{AN}/_mix_{P.nome}.wav'
    np.stack([buf, buf], 1).astype(np.float32).tofile(raw + '.f32')
    sh(['ffmpeg', '-y', '-v', 'error', '-f', 'f32le', '-ar', str(SR), '-ac', '2', '-i', raw + '.f32', '-c:a', 'pcm_f32le', raw]); os.remove(raw + '.f32')
    # loudnorm a due passi sulla sola voce
    r = subprocess.run(['ffmpeg', '-hide_banner', '-i', raw, '-af', 'loudnorm=I=-16:TP=-1.5:LRA=11:print_format=json', '-f', 'null', '-'], capture_output=True, text=True).stderr
    m = json.loads(r[r.rindex('{'):r.rindex('}') + 1])
    af = (f"loudnorm=I=-16:TP=-1.5:LRA=11:measured_I={m['input_i']}:measured_TP={m['input_tp']}:measured_LRA={m['input_lra']}:"
          f"measured_thresh={m['input_thresh']}:offset={m['target_offset']}:linear=true")
    sh(['ffmpeg', '-y', '-v', 'error', '-i', raw, '-af', af, '-ar', str(SR), '-c:a', 'pcm_f32le', raw[:-4] + '_n.wav'])
    inputs = ['-i', raw[:-4] + '_n.wav']; fc = '[0:a]anull[v]'; mix = '[v]'; k = 1
    for j in range(len(P.voci) - 1):
        t = P.off[j] + P.voci[j].dur + 0.2
        inputs += ['-i', REPO + '/kit/suoni/trans.wav']
        fc += f';[{k}:a]volume=9.5dB,adelay={int(t * 1000)}|{int(t * 1000)}[tr{k}]'; mix += f'[tr{k}]'; k += 1
    fc += f';{mix}amix=inputs={k}:normalize=0,atrim=0:{P.dur:.5f},asetpts=PTS-STARTPTS[o]'
    sh(['ffmpeg', '-y', '-v', 'error'] + inputs + ['-filter_complex', fc, '-map', '[o]', '-ar', str(SR), '-ac', '2', '-c:a', 'pcm_s16le', out])
    for f in (raw, raw[:-4] + '_n.wav'): os.remove(f)
    # misure
    r = subprocess.run(['ffmpeg', '-hide_banner', '-i', out, '-af', 'ebur128=peak=true', '-f', 'null', '-'], capture_output=True, text=True).stderr
    I = re.findall(r'I:\s+(-?[\d.]+) LUFS', r)[-1]; pk = re.findall(r'Peak:\s+(-?[\d.]+) dBFS', r)[-1]
    return float(I), float(pk)

# ------------------------------------------------------------------ colori / grafica (modello Spagnolo)
BLU = '#0B1530'; TEL = '#2060AF'; GIA = '#FFE600'
PAL = {  # colori del disciplinare BES: (riempimento, bordo)
    'pesca': ('#FFD9C2', '#E8825A'), 'cel': ('#CFE8FB', '#4A9AD8'), 'pag': ('#FFF3C4', '#E0B800'),
    'men': ('#CDEFD9', '#3FA66B'), 'lil': ('#E2D6F5', '#8E6CC9'), 'bia': ('#FFFFFF', '#C9D3E3')}
SIGLE = {'USA': "Stati Uniti d'America", 'URSS': 'Unione delle Repubbliche Socialiste Sovietiche', 'ONU': 'Organizzazione delle Nazioni Unite',
         'FMI': 'Fondo Monetario Internazionale', 'NATO': "Organizzazione del Trattato dell'Atlantico del Nord",
         'CECA': "Comunità Europea del Carbone e dell'Acciaio", 'CEE': 'Comunità Economica Europea', 'RFT': 'Repubblica Federale Tedesca',
         'RDT': 'Repubblica Democratica Tedesca', 'Euratom': "Comunità Europea dell'Energia Atomica", 'Cominform': "Ufficio d'informazione dei partiti comunisti"}
def e(s): return html.escape(str(s))

def X(inner, t0, cls='', style='', a='pop', d=0.5, hl=None, fl=0, tag='div', t1=None, extra='', dx=0):
    at = f' data-t0="{t0:.3f}" data-a="{a}" data-d="{d}"'
    if t1 is not None: at += f' data-t1="{t1:.3f}"'
    if fl: at += f' data-fl="{fl}"'
    if dx: at += f' data-dx="{dx}"'
    if hl: at += ' data-hl="' + ';'.join(f'{x:.3f},{y:.3f}' for x, y in hl) + '"'
    return f'<{tag} class="{cls}" style="{style}"{at}{extra}>{inner}</{tag}>'

def scena(t0, t1, titolo, corpo, extra='', bstyle='', raw=False):
    t = X(e(titolo), t0 + 0.1, 'stit', a='up', d=0.55) + X('', t0 + 0.25, 'sbar', a='draw0', d=0.5) if titolo else ''
    body = corpo if raw else f'<div class="body" style="{bstyle}">{corpo}</div>'
    return f'<section data-t0="{t0:.3f}" data-t1="{t1:.3f}" data-sc="1">{t}{extra}{body}</section>'

def card(titolo, corpo, col, t0, w=None, hl=None, fl=3, cls='', style='', big=False, pos=None, **k):
    f, b = PAL[col]
    if pos: style += f'position:absolute;left:{pos[0]}px;top:{pos[1]}px;'
    st = f'background:{f};border-color:{b};' + (f'width:{w}px;' if w else 'flex:1;') + style
    return X((f'<h3>{titolo}</h3>' if titolo else '') + (f'<p>{corpo}</p>' if corpo else ''), t0, 'cd ' + cls, st, hl=hl, fl=fl, **k)

def chip(testo, t0, **k): return X(testo, t0, 'chip', **k)
def sig(chiave_, t0, **k):
    return X(f'<b>{e(chiave_)}</b>, cioè {e(SIGLE[chiave_])}', t0, 'chip', **k)
def num(da, a_, t0, d=1.6, pre='', suf='', cls='num', style='', sep=True, t1=None):
    return X(f'{pre}{da}{suf}', t0, cls, style, a='pop', d=0.45, t1=t1, extra=f' data-cnt="{da},{a_},{t0:.3f},{d},{pre},{suf},{1 if sep else 0}"')
def riga(items, style=''): return f'<div class="row" style="{style}">' + ''.join(items) + '</div>'
def colonna(items, style=''): return f'<div class="col" style="{style}">' + ''.join(items) + '</div>'
def freccia(t0, d=0.6, col=TEL, w=170, h=80, ver=False, cls=''):
    if ver:
        p = f'<svg width="{h}" height="{w}" viewBox="0 0 80 {w}"><path d="M40 6 L40 {w - 6} M14 {w - 34} L40 {w - 4} L66 {w - 34}" fill="none" stroke="{col}" stroke-width="9" stroke-linecap="round" stroke-linejoin="round"/></svg>'
    else:
        p = f'<svg width="{w}" height="{h}" viewBox="0 0 {w} 80"><path d="M6 40 L{w - 6} 40 M{w - 34} 14 L{w - 4} 40 L{w - 34} 66" fill="none" stroke="{col}" stroke-width="9" stroke-linecap="round" stroke-linejoin="round"/></svg>'
    return X(p, t0, 'arr ' + cls, a='draw', d=d)
def freccia_abs(x1, y1, x2, y2, t0, d=0.7, col=TEL, wd=9, hl=None):
    ang = math.atan2(y2 - y1, x2 - x1); L = 34
    ax, ay = x2 - L * math.cos(ang - 0.45), y2 - L * math.sin(ang - 0.45); bx, by = x2 - L * math.cos(ang + 0.45), y2 - L * math.sin(ang + 0.45)
    p = f'<svg width="1920" height="1080" viewBox="0 0 1920 1080" style="position:absolute;left:0;top:0"><path d="M{x1} {y1} L{x2} {y2} M{ax:.1f} {ay:.1f} L{x2} {y2} L{bx:.1f} {by:.1f}" fill="none" stroke="{col}" stroke-width="{wd}" stroke-linecap="round" stroke-linejoin="round"/></svg>'
    return X(p, t0, 'abs', 'left:0;top:0;width:1920px;height:1080px', a='draw', d=d, hl=hl)

ICONE = {
    'persona': '<circle cx="50" cy="28" r="18"/><path d="M14 92 C14 56 86 56 86 92 Z"/>',
    'aereo': '<path d="M52 4 L60 40 L96 62 L96 74 L60 62 L58 86 L72 96 L72 104 L50 98 L28 104 L28 96 L42 86 L40 62 L4 74 L4 62 L40 40 Z" transform="scale(.9) translate(6,0)"/>',
    'scudo': '<path d="M50 6 L90 20 L90 52 C90 76 70 90 50 98 C30 90 10 76 10 52 L10 20 Z"/>',
    'bilancia': '<rect x="46" y="14" width="8" height="74"/><rect x="26" y="86" width="48" height="10" rx="4"/><rect x="10" y="26" width="80" height="8" rx="4"/><path d="M14 34 L2 62 H26 Z M86 34 L74 62 H98 Z"/>',
    'dollaro': '<circle cx="50" cy="50" r="44" fill="none" stroke-width="8"/><text x="50" y="70" text-anchor="middle" font-size="62" font-weight="800" font-family="Figtree" stroke="none">$</text>',
    'globo': '<circle cx="50" cy="50" r="42" fill="none" stroke-width="8"/><ellipse cx="50" cy="50" rx="18" ry="42" fill="none" stroke-width="6"/><path d="M8 50 H92 M16 28 H84 M16 72 H84" fill="none" stroke-width="6"/>',
    'fabbrica': '<path d="M6 94 V44 L34 62 V44 L62 62 V44 L90 62 V94 Z"/><rect x="72" y="14" width="14" height="40"/>',
    'libro': '<path d="M8 18 H46 C50 18 50 22 50 22 V90 C46 84 40 84 36 84 H8 Z M92 18 H54 C50 18 50 22 50 22 V90 C54 84 60 84 64 84 H92 Z"/>',
    'stella': '<path d="M50 6 L62 38 L96 38 L68 58 L78 92 L50 72 L22 92 L32 58 L4 38 L38 38 Z"/>',
    'carro': '<rect x="14" y="48" width="72" height="28" rx="10"/><rect x="34" y="28" width="34" height="22" rx="6"/><rect x="60" y="34" width="38" height="8"/><circle cx="26" cy="82" r="10"/><circle cx="50" cy="82" r="10"/><circle cx="74" cy="82" r="10"/>',
    'muro': '<path d="M4 20 H96 V92 H4 Z M4 44 H96 M4 68 H96 M36 20 V44 M68 44 V68 M36 68 V92" fill="none" stroke-width="7"/>',
    'atomo': '<circle cx="50" cy="50" r="8"/><ellipse cx="50" cy="50" rx="44" ry="16" fill="none" stroke-width="6"/><ellipse cx="50" cy="50" rx="44" ry="16" fill="none" stroke-width="6" transform="rotate(60 50 50)"/><ellipse cx="50" cy="50" rx="44" ry="16" fill="none" stroke-width="6" transform="rotate(120 50 50)"/>',
    'carta': '<path d="M16 6 H62 L84 28 V94 H16 Z"/><path d="M62 6 V28 H84" fill="#fff"/>',
    'chiave': '<circle cx="30" cy="50" r="22" fill="none" stroke-width="9"/><path d="M52 50 H94 M80 50 V68 M66 50 V64" fill="none" stroke-width="9"/>',
    'sole': '<circle cx="50" cy="50" r="20"/><path d="M50 6 V22 M50 78 V94 M6 50 H22 M78 50 H94 M19 19 L30 30 M70 70 L81 81 M81 19 L70 30 M30 70 L19 81" stroke-width="8" stroke-linecap="round"/>',
    'sbarra': '<path d="M8 50 H92 M70 28 L94 50 L70 72" fill="none" stroke-width="9" stroke-linecap="round" stroke-linejoin="round"/>',
    'croce': '<path d="M20 20 L80 80 M80 20 L20 80" fill="none" stroke-width="12" stroke-linecap="round"/>',
    'fiamma': '<path d="M50 4 C56 30 84 40 80 68 C77 88 62 96 50 96 C36 96 20 86 20 66 C20 48 36 40 40 22 C46 30 48 20 50 4 Z"/>',
    'spiga': '<path d="M50 96 V30 M50 44 C34 44 28 34 28 20 C44 20 50 30 50 44 M50 44 C66 44 72 34 72 20 C56 20 50 30 50 44 M50 66 C34 66 28 56 28 42 C44 42 50 52 50 66 M50 66 C66 66 72 56 72 42 C56 42 50 52 50 66"/>',
}
def icona(nome, t0, col=TEL, s=110, **k):
    return X(f'<svg width="{s}" height="{s}" viewBox="0 0 100 100" fill="{col}" stroke="{col}">{ICONE[nome]}</svg>', t0, 'ico', **k)
def persone(n, t0, t1pace, col=TEL, s=70, cols=10):
    """griglia di piccole persone che compaiono una dopo l'altra tra t0 e t1pace"""
    out = ''
    for i in range(n):
        ti = t0 + (t1pace - t0) * i / max(1, n - 1)
        out += X(f'<svg width="{s}" height="{s}" viewBox="0 0 100 100" fill="{col}">{ICONE["persona"]}</svg>', ti, 'pp', a='pop', d=0.3)
    return f'<div class="grid" style="grid-template-columns:repeat({cols},{s + 14}px)">{out}</div>'

# ------------------------------------------------------------------ pagina HTML con il motore di animazione
CSS = """
@font-face{font-family:Fig;font-weight:500;src:url(file:///root/.fonts/Figtree-Medium.ttf)}
@font-face{font-family:Fig;font-weight:700;src:url(file:///root/.fonts/Figtree-Bold.ttf)}
@font-face{font-family:Fig;font-weight:800;src:url(file:///root/.fonts/Figtree-ExtraBold.ttf)}
@font-face{font-family:Bri;font-weight:800;src:url(file:///root/.fonts/BricolageGrotesque-ExtraBold.ttf)}
*{box-sizing:border-box;margin:0;padding:0}
html,body{width:1920px;height:1080px;background:#fff;overflow:hidden;font-family:Fig;color:#0B1530}
#logo{position:absolute;left:80px;top:48px;height:58px}
#hl{position:absolute;left:80px;right:80px;top:124px;height:2px;background:#E3E8F0}
#fl{position:absolute;left:80px;right:80px;top:981px;height:2px;background:#E3E8F0}
#prog{position:absolute;left:80px;top:981px;height:6px;width:0;background:#2060AF;border-radius:3px}
#kick{position:absolute;left:80px;top:146px;font:700 24px Fig;letter-spacing:.14em;color:#2060AF;text-transform:uppercase}
#foot{position:absolute;left:80px;top:1004px;font:700 22px Fig;letter-spacing:.12em;color:#2060AF}
#pill{position:absolute;right:80px;top:56px;font:800 26px Fig;letter-spacing:.12em;background:#FFE600;border-radius:12px;padding:10px 22px;box-shadow:0 6px 16px rgba(60,70,90,.2)}
.bg{position:absolute;border-radius:50%;z-index:0}
section{position:absolute;left:0;top:0;width:1920px;height:1080px}
.stit{position:absolute;left:80px;top:182px;width:1760px;font:800 58px/1.1 Bri;color:#0B1530}
.sbar{position:absolute;left:80px;top:258px;width:100px;height:7px;border-radius:4px;background:#2060AF}
.body{position:absolute;left:80px;top:300px;width:1760px;height:660px;display:flex;flex-direction:column;justify-content:center;gap:28px}
.row{display:flex;align-items:center;justify-content:center;gap:34px;width:100%}
.col{display:flex;flex-direction:column;align-items:center;justify-content:center;gap:24px}
.cd{border:5px solid;border-radius:28px;padding:26px 32px;box-shadow:0 10px 26px rgba(60,70,90,.16)}
.cd h3{font:800 50px/1.1 Bri;margin-bottom:12px}
.cd p{font:500 40px/1.28 Fig}
.cd b{font-weight:800}
.cd.hl{border-color:#FFE600;box-shadow:0 0 0 6px #FFE600,0 12px 28px rgba(60,70,90,.25)}
.chip{font:500 32px/1.25 Fig;background:#EEF3FB;border-radius:12px;padding:10px 20px;border-left:8px solid #2060AF;box-shadow:0 6px 16px rgba(60,70,90,.1)}
.chip b{font-weight:800}
.num{font:800 230px/1 Bri;color:#2060AF}
.lab{font:800 52px/1.15 Bri}
.sub{font:500 38px/1.3 Fig}
.big{font:800 96px/1.05 Bri;color:#2060AF}
.pp{display:block}
.grid{display:grid;gap:10px}
.arr svg,.ico svg{display:block}
.pillbox{display:inline-block;font:800 40px Bri;background:#FFE600;border-radius:14px;padding:6px 20px}
mark{background:linear-gradient(transparent 55%,#FFE600 55%);color:inherit;padding:0 4px}
.mapv{position:relative;overflow:hidden;border-radius:24px;border:5px solid #C9D3E3;box-shadow:0 10px 26px rgba(60,70,90,.18);background:#fff}
.mapin{position:absolute;left:0;top:0;transform-origin:0 0}
.mapin img{position:absolute;left:0;top:0;width:100%;height:100%;display:block}
.mk{position:absolute;border:8px solid #FFE600;border-radius:50%;box-shadow:0 0 0 4px #0B1530}
.mk.r{border-radius:14px}
.mkl{position:absolute;font:800 24px Fig;background:#FFE600;border-radius:10px;padding:4px 14px;white-space:nowrap}
.abs{position:absolute}
.pnode{font:800 44px/1.1 Bri;border:5px solid;border-radius:26px;padding:20px 30px;text-align:center;box-shadow:0 10px 26px rgba(60,70,90,.16)}
#dark{position:absolute;left:0;top:0;width:1920px;height:1080px;z-index:50;opacity:0;background:#0B1530;overflow:hidden}
.dk{position:absolute;z-index:60}
.dtit{font:800 92px/1.08 Bri;color:#fff}
.dsub{font:700 44px/1.2 Fig;color:#FFE600}
"""
JS = r"""
const clamp=(x,a=0,b=1)=>Math.min(b,Math.max(a,x));
const eo=p=>1-Math.pow(1-p,3), eio=p=>p<.5?4*p*p*p:1-Math.pow(-2*p+2,3)/2, bo=p=>{const c=1.7;return 1+(c+1)*Math.pow(p-1,3)+c*Math.pow(p-1,2)};
const ELS=[...document.querySelectorAll('[data-t0]')].map((el,i)=>{
  const sc=el.closest('section');const o={el,t0:Math.max(+el.dataset.t0,(sc&&sc!==el)?+sc.dataset.t0:0),a:el.dataset.a||'pop',d:+(el.dataset.d||.5),fl:+(el.dataset.fl||0),ph:i*1.3,dx:+(el.dataset.dx||0),
   t1:el.dataset.t1!==undefined?+el.dataset.t1:(sc&&sc!==el?+sc.dataset.t1:1e9),hl:[],cnt:null,len:0};
  if(el.dataset.hl)o.hl=el.dataset.hl.split(';').map(s=>s.split(',').map(Number));
  if(el.dataset.cnt){const q=el.dataset.cnt.split(',');o.cnt={from:+q[0],to:+q[1],t0:+q[2],d:+q[3],pre:q[4],suf:q[5],sep:q[6]=='1'}}
  if(o.a=='draw'||o.a=='draw0'){o.paths=[...el.querySelectorAll('path')];o.paths.forEach(p=>{p.__len=p.getTotalLength();p.style.strokeDasharray=p.__len})}
  return o});
const CAMS=[...document.querySelectorAll('[data-cam]')].map(el=>({el,kf:el.dataset.cam.split(';').map(s=>s.split(',').map(Number)),W:+el.dataset.w,H:+el.dataset.h,cw:+el.dataset.cw,ch:+el.dataset.ch}));
const DUR=+document.body.dataset.dur, DARK=(document.body.dataset.dark||'').split(';').filter(x=>x).map(s=>s.split(',').map(Number));
function fmt(v,sep){let s=String(Math.round(v));return sep?s.replace(/\B(?=(\d{3})+(?!\d))/g,'.'):s}
function render(t){
  for(const o of ELS){const el=o.el;let op=0,tx=0,ty=0,s=1;
    if(t>=o.t0&&t<o.t1+.4){const p=clamp((t-o.t0)/o.d),e=eo(p);
      switch(o.a){case 'pop':op=clamp(p*3);s=.65+.35*bo(p);break;case 'up':op=clamp(p*2.5);ty=(1-e)*50;break;case 'left':op=clamp(p*2.5);tx=-(1-e)*140;break;
        case 'right':op=clamp(p*2.5);tx=(1-e)*140;break;case 'fade':op=p;break;case 'zoom':op=clamp(p*2.5);s=1.2-.2*e;break;
        case 'none':op=clamp(p*8);break;case 'draw':op=p>0.015?1:0;o.paths.forEach(q=>q.style.strokeDashoffset=q.__len*(1-eio(p)));break;
        case 'draw0':op=1;el.style.width=(100+0*p)*eo(p)+'px';break;
        case 'ring':{const ph=((t-o.t0)/o.d)%1;op=(1-ph)*.9;s=.25+1.35*ph;break}
        case 'flow':{const ph=((t-o.t0)/o.d)%1;op=Math.sin(Math.PI*ph);tx=o.dx*ph;break}
        case 'wipe':op=1;el.style.clipPath=`inset(0 ${(1-e)*100}% 0 0)`;break;
        case 'grow':op=clamp(p*4);el.style.transformOrigin='50% 100%';s=1;el.style.transform=`scaleY(${e})`;break;
        default:op=1}
      if(t>o.t1){const q=clamp((t-o.t1)/.35);op*=1-q;ty-=q*24}
      if(o.fl&&p>=1)ty+=Math.sin(t*1.9+o.ph)*o.fl;
    }
    if(o.a!='grow'){el.style.transform=`translate(${tx}px,${ty}px) scale(${s})`}
    el.style.opacity=op;el.style.visibility=op>0.003?'visible':'hidden';
    if(o.hl.length){let on=false;for(const [a,b] of o.hl)if(t>=a&&t<b)on=true;el.classList.toggle('hl',on)}
    if(o.cnt&&t>=o.t0){const c=o.cnt,p=eo(clamp((t-c.t0)/c.d));el.textContent=c.pre+fmt(c.from+(c.to-c.from)*p,c.sep)+c.suf}
  }
  for(const c of CAMS){let k=c.kf,i=0;while(i<k.length-1&&t>=k[i+1][0])i++;let a=k[i],b=k[Math.min(i+1,k.length-1)];
    const p=a===b?0:eio(clamp((t-a[0])/(b[0]-a[0])));const s=a[3]+(b[3]-a[3])*p;const cx=clamp(a[1]+(b[1]-a[1])*p,.5/s,1-.5/s),cy=clamp(a[2]+(b[2]-a[2])*p,.5/s,1-.5/s);
    c.el.style.width=c.W+'px';c.el.style.height=c.H+'px';
    c.el.style.transform=`translate(${c.cw/2-cx*c.W*s}px,${c.ch/2-cy*c.H*s}px) scale(${s})`}
  document.getElementById('prog').style.width=(1760*clamp(t/DUR))+'px';
  // sfondo morbido in lento movimento
  document.querySelectorAll('.bg').forEach((b,i)=>{b.style.transform=`translate(${Math.sin(t*.35+i*2)*60}px,${Math.cos(t*.28+i*1.7)*40}px)`});
  // scheda scura
  let dk=0;for(const [a,b] of DARK){if(t>=a&&t<b)dk=Math.min(clamp((t-a)/.4),clamp((b-t)/.4))}
  document.querySelectorAll('.dklogo').forEach(x=>x.style.opacity=dk);const D=document.getElementById('dark');if(D){D.style.opacity=dk;D.style.visibility=dk>0?'visible':'hidden';
  if(dk>0){D.style.background=`radial-gradient(900px 700px at ${50+30*Math.sin(t*.5)}% ${45+25*Math.cos(t*.4)}%,#1d4a96 0%,rgba(11,21,48,0) 70%),radial-gradient(700px 600px at ${80+15*Math.cos(t*.45)}% ${85+10*Math.sin(t*.6)}%,#2060AF55 0%,rgba(11,21,48,0) 70%),#0B1530`}}
}
window.render=render;render(0);
"""
def pagina(P, kick, scene_html, scuro=None, pill='APPROFONDIMENTO'):
    bg = ''.join(f'<div class="bg" style="left:{x}px;top:{y}px;width:{s}px;height:{s}px;background:{c}"></div>' for x, y, s, c in
                 [(1380, 560, 520, 'rgba(32,96,175,.07)'), (1560, 120, 300, 'rgba(255,230,0,.16)'), (-120, 640, 420, 'rgba(32,96,175,.05)')])
    dark = ';'.join(f'{a:.3f},{b:.3f}' for a, b in (scuro or []))
    logo = '<img id="logo" src="file:///tmp/w/logo.svg">'
    darkdiv = '<div id="dark"></div><img class="dk dklogo" style="left:80px;top:48px;height:58px;filter:brightness(0) invert(1);opacity:0" src="file:///tmp/w/logo.svg">' if scuro else ''
    pl = f'<div id="pill">{e(pill)}</div>' if pill else ''
    return (f'<!doctype html><html><head><meta charset="utf-8"><style>{CSS}</style></head><body data-dur="{P.dur}" data-dark="{dark}">'
            f'{bg}{logo}<div id="hl"></div><div id="kick">{e(kick)}</div>{pl}{scene_html}<div id="fl"></div><div id="prog"></div><div id="foot">STORIA V</div>{darkdiv}<script>{JS}</script></body></html>')

NODE_FRAMES = r"""
const {chromium}=require('playwright');const fs=require('fs'),path=require('path');
(async()=>{const [html,a,b]=[process.argv[2],+process.argv[3],+process.argv[4]];
const br=await chromium.launch({args:['--allow-file-access-from-files']});const pg=await br.newPage({viewport:{width:1920,height:1080}});
await pg.goto('file://'+path.resolve(html));await pg.evaluate(()=>document.fonts.ready);await pg.waitForTimeout(300);
for(let i=a;i<b;i++){await pg.evaluate(t=>window.render(t),i/30);const buf=await pg.screenshot({type:'png'});
 if(!process.stdout.write(buf))await new Promise(r=>process.stdout.once('drain',r));}
await br.close()})();
"""
open(AN + '/frames.js', 'w').write(NODE_FRAMES)
NODEENV = {**os.environ, 'NODE_PATH': '/opt/node-tools/node_modules'}

def foto(html_path, t, out):
    jb = [{'html': html_path, 'out': out, 't': t, 'force': True}]
    json.dump(jb, open(AN + '/_job.json', 'w'))
    subprocess.run(['node', REPO + '/lez14/shot.js', AN + '/_job.json'], check=True, cwd=REPO + '/lez14', env=NODEENV)

def video(P, html_path, wav, out):
    """renderizza P.nfr fotogrammi (2 processi di Chromium) e codifica .mkv con l'audio"""
    n = P.nfr; mid = n // 2
    parts = []
    for k, (a, b) in enumerate([(0, mid), (mid, n)]):
        f = f'{AN}/_{P.nome}_{k}.mkv'
        cmd = (f'node {AN}/frames.js {html_path} {a} {b} | ffmpeg -y -v error -f image2pipe -framerate 30 -c:v png -i - '
               f'-c:v libx264 -preset veryfast -crf 14 -pix_fmt yuv420p -r 30 {f}')
        parts.append((subprocess.Popen(cmd, shell=True, env=NODEENV, cwd=REPO + '/lez14', stderr=subprocess.PIPE), f))
    for p, f in parts:
        p.wait()
        if p.returncode: raise RuntimeError(p.stderr.read().decode()[-800:])
    lst = AN + f'/_{P.nome}.txt'; open(lst, 'w').write(''.join(f"file '{f}'\n" for p, f in parts))
    sh(['ffmpeg', '-y', '-v', 'error', '-f', 'concat', '-safe', '0', '-i', lst, '-i', wav, '-map', '0:v', '-map', '1:a', '-c:v', 'libx264', '-preset', 'veryfast',
        '-crf', '16', '-pix_fmt', 'yuv420p', '-r', '30', '-c:a', 'pcm_s16le', '-ar', '48000', '-ac', '2', '-frames:v', str(n), out])
    for p, f in parts: os.remove(f)
    os.remove(lst)

def mappa_img(nome, ritaglio=None, cancella=None):
    """immagine del prof, ingrandita x3 con nitidezza (stessa routine di montaggio.migliora); ritaglio=(x0,y0,x1,y1) in px originali;
    cancella=[(x0,y0,x1,y1)] = riquadri (QR) riempiti col colore dei dintorni"""
    from PIL import Image, ImageFilter
    out = f'{AN}/{nome}_hq.png'
    if os.path.exists(out): return out, Image.open(out).size
    im = Image.open(f'/tmp/w/img/{nome}.jpg').convert('RGB')
    for r in cancella or []:
        x0, y0, x1, y1 = r[:4]; c = r[4] if len(r) > 4 else im.getpixel((max(0, x0 - 6), (y0 + y1) // 2)); im.paste(c, (x0, y0, x1, y1))
    if ritaglio: im = im.crop(ritaglio)
    im = im.filter(ImageFilter.GaussianBlur(0.5)).resize((im.width * 3, im.height * 3), Image.LANCZOS).filter(ImageFilter.UnsharpMask(3, 90, 2))
    im.save(out); return out, im.size

def mappa(src, size, w, h, cam, t0, marks='', cls='', style='', t1=None):
    """riquadro con immagine che si muove (cam=[(t,cx,cy,s),..] in frazioni dell'immagine; s=1 -> immagine intera nel riquadro)"""
    iw, ih = size; sc = min(w / iw, h / ih); W = iw * sc; H = ih * sc
    kf = ';'.join(f'{t:.3f},{cx},{cy},{s}' for t, cx, cy, s in cam)
    inner = f'<div class="mapin" data-cam="{kf}" data-w="{W:.1f}" data-h="{H:.1f}" data-cw="{w}" data-ch="{h}"><img src="file://{src}">{marks}</div>'
    return X(inner, t0, 'mapv ' + cls, f'width:{w}px;height:{h}px;{style}', a='fade', d=0.5, t1=t1)
def segno(x, y, w, h, t0, rect=False, etichetta='', lx=0, ly=-60, **k):
    """cerchio/rettangolo giallo sulla mappa, posizione in % dell'immagine"""
    inn = X('', t0, 'mk' + (' r' if rect else ''), f'left:{x}%;top:{y}%;width:{w}%;height:{h}%', a='pop', d=0.45, **k)
    if etichetta: inn += X(e(etichetta), t0 + 0.15, 'mkl', f'left:{x + lx}%;top:{y + h / 2 + ly / 10:.1f}%', a='pop', d=0.4, **k)
    return inn

PEZZI = {}
def pezzo(nome, voci, gap=1.0):
    def deco(fn): PEZZI[nome] = (voci, gap, fn); return fn
    return deco

def costruisci(nome):
    voci, gap, fn = PEZZI[nome]; P = Pezzo(nome, voci, gap)
    r = fn(P)
    kick, scene, scuro = r if len(r) == 3 else (*r, None)
    return P, pagina(P, kick, ''.join(scene), scuro, pill='APPROFONDIMENTO' if not nome.startswith('RIP') else 'RIPASSO')

def esegui(nome, solo_aud=False):
    P, h = costruisci(nome)
    hp = f'{AN}/{nome}.html'; open(hp, 'w').write(h)
    wav = f'{AN}/{nome}.wav'; I, pk = audio_pezzo(P, wav)
    info = dict(durata_s=round(P.dur, 4), fotogrammi=P.nfr, voci=[v.nome for v in P.voci], LUFS_voce=I, picco_dBFS=pk,
                tempi_voci=[round(o, 3) for o in P.off], fine_voce=round(P.fine_voce, 3),
                confronto=[dict(voce=v.nome, agganciate=round(v.match, 3), non_agganciate=v.non_agganciate, numeri_non_trovati=v.numeri_ko, ritagli=[round(v.cut0, 3), round(v.cut1, 3)]) for v in P.voci])
    print(nome, info['durata_s'], 'LUFS', I, 'picco', pk, 'match', [round(v.match, 2) for v in P.voci], flush=True)
    if solo_aud:
        os.remove(wav); return info
    out = f'{PZ}/{nome}.mkv'; video(P, hp, wav, out)
    info['note'] = 'animazione a 30 fps, voce Kore -16 LUFS, dissolvenze voce 30 ms; nessuna dissolvenza incorporata'
    json.dump(info, open(f'{PZ}/{nome}.json', 'w'), ensure_ascii=False, indent=1)
    os.remove(wav)
    return info

exec(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'animazioni_pezzi.py')).read())

def main():
    a = sys.argv[1:]
    if a and a[0] == '--frame':
        P, h = costruisci(a[1]); hp = f'{AN}/{a[1]}.html'; open(hp, 'w').write(h)
        for t in a[2:]: foto(hp, float(t), f'{AN}/fr/{a[1]}_{float(t):05.1f}.png')
        return
    solo = False
    if a and a[0] == '--solo-aud': solo = True; a = a[1:]
    for nome in (a or list(PEZZI)): esegui(nome, solo)
if __name__ == '__main__': main()
