#!/usr/bin/env python3
# Controlla ogni voce Kore: trascrizione (sherpa) confrontata con il testo, numeri, bordi (ultimi 50 ms < 0,03), durata.
import sys, os, re, json, subprocess, difflib, numpy as np
sys.path.insert(0, '/home/user/Lezioni/lez12'); sys.path.insert(0, '/home/user/Lezioni/tools')
from voci import VOCI
W = '/home/user/Lezioni/lavoro/'
NUM = {'millenovecentosedici': '1916', 'millenovecentotredici': '1913', 'millenovecentoventiquattro': '1924', 'millenovecentotrentasette': '1937'}
def norm(t):
    t = t.lower()
    for k, v in NUM.items(): t = t.replace(k, v)
    t = re.sub(r"[«»“”\"'’.,;:!?()\-]", ' ', t); return t.split()
sel = sys.argv[1:] or list(VOCI)
os.makedirs(W + 'vox_chk', exist_ok=True); res = {}
for n in sel:
    f = W + f'vox/{n}.wav'
    if not os.path.exists(f): res[n] = 'MANCA'; continue
    x = np.frombuffer(subprocess.run(['ffmpeg', '-v', 'error', '-i', f, '-ac', '1', '-ar', '48000', '-f', 's16le', '-'], capture_output=True).stdout, np.int16).astype(float) / 32768
    bordo = float(np.abs(x[-2400:]).max()); inizio = float(np.abs(x[:2400]).max()); dur = len(x) / 48000
    out = W + f'vox_chk/{n}'
    if not os.path.exists(out + '.json'): subprocess.run([sys.executable, '/home/user/Lezioni/tools/trascrivi.py', f, out], capture_output=True)
    asr = ' '.join(s['testo'] for s in json.load(open(out + '.json')))
    a, b = norm(VOCI[n]), norm(asr); sm = difflib.SequenceMatcher(None, a, b); r = sm.ratio()
    diff = [(' '.join(a[i1:i2]), ' '.join(b[j1:j2])) for tag, i1, i2, j1, j2 in sm.get_opcodes() if tag != 'equal']
    res[n] = dict(durata=round(dur, 1), bordo_fine=round(bordo, 3), bordo_inizio=round(inizio, 3), similitudine=round(r, 3), differenze=diff[:12], troncata=bordo >= 0.03)
    print(n, res[n]['durata'], 'fine', res[n]['bordo_fine'], 'sim', res[n]['similitudine'], 'TRONCATA' if bordo >= 0.03 else '', diff[:4], flush=True)
json.dump(res, open(W + 'vox_chk/esito.json', 'w'), ensure_ascii=False, indent=1)
