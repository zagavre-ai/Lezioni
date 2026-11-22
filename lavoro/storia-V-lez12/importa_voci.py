# -*- coding: utf-8 -*-
# Importa le voci Kore della master: normalizza a -16 LUFS, trascrive, confronta con il testo, allinea le frasi, controlla i bordi.
import os, sys, json, re, subprocess, difflib, shutil
sys.path.insert(0, '/home/user/Lezioni/lavoro/storia-V-lez12')
import voce, contenuti as C
W = '/home/user/w12'; RAW = f'{W}/vox_raw'; OK = f'{W}/vox'; os.makedirs(RAW, exist_ok=True); os.makedirs(OK, exist_ok=True)
sh = voce.sh
def norm(t): return re.sub(r"[^a-zàèéìòù0-9 ]", ' ', t.lower().replace("'", ' ')).split()
def trascrivi(wav, base):
    if not os.path.exists(base + '.json'): sh(['python3', '/home/user/Lezioni/tools/trascrivi.py', wav, base])
    S = json.load(open(base + '.json')); out = []
    for s in S:
        cur = None
        for t, w in s.get('parole') or []:
            if w.startswith(' ') or cur is None: cur = [t, w.strip()]; out.append(cur)
            else: cur[1] += w
    return [(t, w) for t, w in out if w]
def importa(nome, testo, raw):
    wav = f'{OK}/{nome}.wav'
    m = re.findall(r'"input_i" : "(-?[\d.]+)"', sh(['ffmpeg', '-v', 'info', '-i', raw, '-af', 'loudnorm=I=-16:TP=-1.5:print_format=json', '-f', 'null', '-']).stderr)
    g = -16.0 - float(m[-1]) if m else 0.0
    sh(['ffmpeg', '-v', 'error', '-y', '-i', raw, '-af', f'volume={g:.2f}dB,alimiter=limit=0.89:level=disabled', '-ar', '48000', '-ac', '2', wav])
    dur = voce.durata(wav)
    # bordi: ampiezza negli ultimi 50 ms e nei primi 50 ms
    import numpy as np
    x = np.frombuffer(subprocess.run(['ffmpeg', '-v', 'error', '-i', wav, '-ac', '1', '-ar', '48000', '-f', 'f32le', '-'], capture_output=True).stdout, np.float32)
    bordo_fine = float(np.abs(x[-2400:]).max()); bordo_ini = float(np.abs(x[:2400]).max())
    asr = trascrivi(wav, f'{RAW}/{nome}_asr')
    fs = voce.frasi(testo); tw = []; idx = []
    for i, f in enumerate(fs):
        for w in norm(f): tw.append(w); idx.append(i)
    aw = [norm(w) for _, w in asr]; A = []; AT = []
    for (t, _), ws in zip(asr, aw):
        for w in ws: A.append(w); AT.append(t)
    sm = difflib.SequenceMatcher(None, tw, A, autojunk=False); mappa = {}
    for a, b, n in sm.get_matching_blocks():
        for k in range(n): mappa[a + k] = b + k
    diff = [(tw[a1:a2], A[b1:b2]) for tag, a1, a2, b1, b2 in sm.get_opcodes() if tag != 'equal']
    tempi = []; prima = {}; ultima = {}
    for j, i in enumerate(idx):
        if j in mappa: prima.setdefault(i, AT[mappa[j]]); ultima[i] = AT[mappa[j]]
    prev_end = 0.0
    for i in range(len(fs)):
        a = prima.get(i, prev_end); b = ultima.get(i, a) + 0.35
        tempi.append((round(max(0, a - 0.05), 3), round(min(dur, b), 3))); prev_end = b
    # correggi sovrapposizioni
    for i in range(len(tempi) - 1):
        if tempi[i][1] > tempi[i + 1][0]: tempi[i] = (tempi[i][0], tempi[i + 1][0] - 0.02)
    sim = sm.ratio()
    r = dict(nome=nome, wav=wav, durata=dur, tempi=tempi, frasi=fs, reale=True, testo=testo, somiglianza=round(sim, 3), bordo_fine=bordo_fine, bordo_inizio=bordo_ini, differenze=[(' '.join(a), ' '.join(b)) for a, b in diff][:20])
    json.dump(r, open(f'{OK}/{nome}.json', 'w'), ensure_ascii=False, indent=1)
    return r
if __name__ == '__main__':
    rap = []
    for nome in C.VOCI:
        raw = f'{RAW}/{nome}.wav'
        if not os.path.exists(raw): continue
        r = importa(nome, C.VOCI[nome], raw)
        rap.append((nome, r['durata'], r['somiglianza'], r['bordo_fine'], r['differenze']))
        print(nome, round(r['durata'], 1), 'sim', r['somiglianza'], 'bordo fine', round(r['bordo_fine'], 3), 'diff', r['differenze'][:3], flush=True)
    json.dump(rap, open(f'{W}/rapporto_voci.json', 'w'), ensure_ascii=False, indent=1)
