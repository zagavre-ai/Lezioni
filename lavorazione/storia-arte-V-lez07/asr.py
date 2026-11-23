# Trascrizione con tempi parola per parola di una voce (sherpa-onnx Parakeet) + allineamento di frammenti di testo
import os, sys, json, hashlib, unicodedata, re, difflib, subprocess, wave
import numpy as np
D = '/tmp/asr'; M = 'sherpa-onnx-nemo-parakeet-tdt-0.6b-v3-int8'
CACHE = '/tmp/claude-0/w/out/asr_cache/'; os.makedirs(CACHE, exist_ok=True)
_rec = None; _vadcfg = None

def _init():
    global _rec, _vadcfg
    if _rec: return
    import sherpa_onnx
    P = f'{D}/{M}/'
    _rec = sherpa_onnx.OfflineRecognizer.from_transducer(encoder=P + 'encoder.int8.onnx', decoder=P + 'decoder.int8.onnx',
            joiner=P + 'joiner.int8.onnx', tokens=P + 'tokens.txt', model_type='nemo_transducer', num_threads=2)

def norm(w):
    w = unicodedata.normalize('NFD', w.lower()); w = ''.join(c for c in w if unicodedata.category(c) != 'Mn')
    return re.sub(r'[^a-z0-9]', '', w)

def words(wavpath):
    """[(tempo_s, parola)] ; cache su disco"""
    h = hashlib.md5(open(wavpath, 'rb').read()).hexdigest()[:12]; cp = CACHE + h + '.json'
    if os.path.exists(cp): return json.load(open(cp))
    _init(); import sherpa_onnx
    a = subprocess.run(['ffmpeg', '-v', 'error', '-i', wavpath, '-vn', '-ac', '1', '-ar', '16000', '-f', 's16le', '-'], capture_output=True, check=True).stdout
    x = np.frombuffer(a, np.int16).astype(np.float32) / 32768
    # pezzi da 25 s con 1 s di sovrapposizione evitata: la voce e' pulita, si taglia nei punti piu' silenziosi
    out = []; pos = 0; n = len(x); CH = 16000 * 25
    while pos < n:
        end = min(n, pos + CH)
        if end < n:   # cerca il minimo di energia negli ultimi 4 s
            lo = end - 16000 * 4; seg = np.abs(x[lo:end]); k = seg[:len(seg) // 800 * 800].reshape(-1, 800).mean(1).argmin(); end = lo + k * 800 + 400
        st = _rec.create_stream(); st.accept_waveform(16000, x[pos:end]); _rec.decode_stream(st); r = st.result
        t0 = pos / 16000
        cur = None
        for t, tok in zip(r.timestamps, r.tokens):
            if tok.startswith(' ') or cur is None:
                if cur: out.append(cur)
                cur = [round(t0 + t, 3), tok.strip()]
            else: cur[1] += tok
        if cur: out.append(cur)
        pos = end
    out = [o for o in out if o[1]]
    json.dump(out, open(cp, 'w'), ensure_ascii=False)
    return out

def speech_span(wavpath, thr=0.02):
    w = wave.open(wavpath); a = np.frombuffer(w.readframes(w.getnframes()), np.int16).astype(np.float32) / 32768
    if w.getnchannels() == 2: a = a.reshape(-1, 2).mean(1)
    sr = w.getframerate(); idx = np.where(np.abs(a) > thr)[0]
    return (idx[0] / sr, idx[-1] / sr) if len(idx) else (0, len(a) / sr)

def align(asr_words, fragments, total=None, span=None, want_words=False):
    """fragments: lista di testi consecutivi; ritorna [(inizio, fine)] in secondi per ciascuno"""
    ref = []; owner = []
    for i, fr in enumerate(fragments):
        for w in fr.split():
            nw = norm(w)
            if nw: ref.append(nw); owner.append(i)
    hyp = [norm(w) for _, w in asr_words]; ht = [t for t, _ in asr_words]
    sm = difflib.SequenceMatcher(None, ref, hyp, autojunk=False)
    rt = [None] * len(ref)
    for a, b, n in sm.get_matching_blocks():
        for k in range(n): rt[a + k] = ht[b + k]
    # interpolazione dei non agganciati
    s0, s1 = span if span else (ht[0] if ht else 0, (ht[-1] + .4) if ht else (total or 1))
    known = [(i, t) for i, t in enumerate(rt) if t is not None]
    if not known: known = [(0, s0), (len(ref) - 1, s1)]
    for i in range(len(ref)):
        if rt[i] is None:
            prev = [(j, t) for j, t in known if j < i]; nxt = [(j, t) for j, t in known if j > i]
            if prev and nxt:
                (j0, t0), (j1, t1) = prev[-1], nxt[0]; rt[i] = t0 + (t1 - t0) * (i - j0) / (j1 - j0)
            elif prev: rt[i] = prev[-1][1] + 0.35 * (i - prev[-1][0])
            else: rt[i] = max(s0, nxt[0][1] - 0.35 * (nxt[0][0] - i))
    starts = [None] * len(fragments)
    for k, o in enumerate(owner):
        if starts[o] is None: starts[o] = rt[k]
    for i in range(len(starts)):
        if starts[i] is None: starts[i] = starts[i - 1] if i else s0
    ends = starts[1:] + [s1]
    res = [(float(a), float(b)) for a, b in zip(starts, ends)]
    if not want_words: return res
    # tempi per ogni parola di ciascun frammento (nell'ordine di .split())
    wt = [[] for _ in fragments]; k = 0
    for i, fr in enumerate(fragments):
        for w in fr.split():
            if norm(w): wt[i].append(float(rt[k])); k += 1
            else: wt[i].append(wt[i][-1] if wt[i] else res[i][0])
    return res, wt

if __name__ == '__main__':
    print(words(sys.argv[1]))
