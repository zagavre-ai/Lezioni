# -*- coding: utf-8 -*-
# Voci narranti: le Kore (della master) in vox/NOME.wav; in mancanza, voce provvisoria (espeak-ng) con tempi per frase.
import os, re, json, subprocess, wave
import contenuti as C
W = '/home/user/w12'
VOX = f'{W}/vox'; PROV = f'{W}/vox_prov'; os.makedirs(PROV, exist_ok=True); os.makedirs(VOX, exist_ok=True)
def sh(c): 
    r = subprocess.run(c, capture_output=True, text=True)
    if r.returncode: raise RuntimeError(r.stderr[-500:])
    return r
def frasi(testo):
    if ' | ' in testo: return [x.strip() for x in testo.split(' | ')]
    return [x for x in re.split(r'(?<=[.?!])\s+', testo.strip()) if x]
def durata(wav): return float(sh(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', wav]).stdout)
def provvisoria(nome):
    f = f'{PROV}/{nome}.json'
    testo = C.VOCI[nome]
    if os.path.exists(f):
        j = json.load(open(f))
        if j.get('testo') == testo: return j
    fs = frasi(testo); parti = []; tempi = []; t = 0.0
    lst = f'{PROV}/{nome}.txt'; open(lst, 'w').close()
    segs = []
    for i, fr in enumerate(fs):
        w = f'{PROV}/{nome}_{i}.wav'
        sh(['espeak-ng', '-v', 'it', '-s', '150', '-p', '45', '-w', w + '.raw.wav', fr.replace('Piłsudski', 'Pilsudski').replace('Léon', 'Leon')])
        sh(['ffmpeg', '-v', 'error', '-y', '-i', w + '.raw.wav', '-ar', '48000', '-ac', '2', '-af', 'apad=pad_dur=0.30', w])
        d = durata(w); tempi.append((round(t, 3), round(t + d - 0.30, 3))); t += d; segs.append(w)
    with open(lst, 'w') as fh:
        for w in segs: fh.write(f"file '{w}'\n")
    out = f'{PROV}/{nome}.wav'
    sh(['ffmpeg', '-v', 'error', '-y', '-f', 'concat', '-safe', '0', '-i', lst, '-af', 'loudnorm=I=-16:TP=-1.5', '-ar', '48000', '-ac', '2', out])
    r = dict(nome=nome, wav=out, durata=durata(out), tempi=tempi, frasi=fs, reale=False, testo=testo)
    json.dump(r, open(f, 'w'), ensure_ascii=False); return r
def get(nome):
    f = f'{VOX}/{nome}.json'
    if os.path.exists(f): return json.load(open(f))   # voce reale già allineata
    return provvisoria(nome)
