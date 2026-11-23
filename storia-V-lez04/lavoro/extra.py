# -*- coding: utf-8 -*-
# Pezzi che dipendono dalle voci Kore: cover con voce, mappe, pillole (blu + schema), glossario, riepilogo.
import sys, os, json, subprocess, re, wave
sys.path.insert(0, '/tmp/claude-0/w')
from dati import *
import slides as SL
from piece import seg_video, seg_files, W
VOX = os.environ.get('VOXDIR', W + '/vox')          # i wav delle voci (dal ramo voci-storia-V-lez04)
FPS = 30
VOX48 = os.environ.get('VOX48', W + '/vox48')

def vdur(name):
    f = f'{VOX}/{name}.wav'
    r = subprocess.run(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', f], capture_output=True, text=True)
    return float(r.stdout.strip())

def fr(sec): return int(round(sec * FPS))

def norm_encode(src, out, limit=None):
    """ricodifica standard (stessi parametri di tutti i pezzi) con keyframe a 0,4 s e a fine-0,4 s; limit = durata massima (taglio in coda)"""
    d = float(subprocess.run(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', src], capture_output=True, text=True).stdout)
    if limit: d = min(d, limit)
    n = int(round(d * FPS))
    subprocess.run(['ffmpeg', '-y', '-v', 'error', '-i', src, '-frames:v', str(n), '-c:v', 'libx264', '-preset', 'veryfast', '-crf', '21', '-r', '30', '-g', '60',
                    '-force_key_frames', f'0.4,{n / FPS - 0.4:.3f}', '-pix_fmt', 'yuv420p', '-an', out], check=True)
    return n

def static_piece(states, out):
    """states: [(png, frames)] -> mp4 standard"""
    lst = out + '.lst'
    with open(lst, 'w') as f:
        for p, n in states:
            for x in seg_files(p, n): f.write(f"file '{x}'\n")
    tmp = out + '.raw.mp4'
    subprocess.run(['ffmpeg', '-y', '-v', 'error', '-f', 'concat', '-safe', '0', '-i', lst, '-c', 'copy', tmp], check=True)
    n = norm_encode(tmp, out); os.remove(tmp)
    return n

def split_caps(text, d, lead=0.9):
    """didascalia in 1-2 frasi con tempi proporzionali alla lunghezza"""
    parts = re.split(r'(?<=[\.\!\?])\s+', text.strip())
    if len(parts) > 2: parts = [' '.join(parts[:-1]), parts[-1]]
    tot = sum(len(p) for p in parts); t = lead; out = []
    for p in parts:
        dd = d * len(p) / tot; out.append([round(t, 2), round(t + dd, 2) if p is not parts[-1] else round(t + dd + 0.8, 2), p]); t += dd
    return out

def voice_texts():
    return {v['nome']: v['testo'] for v in json.load(open(W + '/voci/testi_voci.json'))}

def page_nums(P):
    return json.load(open(f'{W}/pieces/pages_P{P}.json'))

def make_jobs(P):
    """job schede blu (pillole, riepilogo) per la Parte P; richiede le voci in vox/"""
    order = PARTI[P]; T = voice_texts(); os.makedirs(W + '/jobs', exist_ok=True)
    for pos, n in enumerate(order, 1):
        a = ARG[n - 1]; d = vdur(f'PI{n}')
        caps = split_caps(T[f'PI{n}'], d)
        topic = a['nome']; tfs = 84 if len(topic) <= 30 else max(52, int(84 * 30 / len(topic)))
        dur = round(caps[-1][1] + 1.2, 1)
        json.dump({"type": "repaso", "kicker": "Pillola di storia", "big": "RIPASSO", "topic": topic, "tfs": tfs, "caps": caps, "dur": dur}, open(f'{W}/jobs/P{P}R{pos}.json', 'w'), ensure_ascii=False)
    d = vdur(FIN[P])
    json.dump({"type": "final", "kicker": "Storia V", "l1": "RIEPILOGO", "l2": "FINALE", "items": [[ARG[n - 1]['nome'], ""] for n in order], "sub": "Ripassiamo insieme ciò che abbiamo imparato.", "dur": round(d + 1.7, 1)}, open(f'{W}/jobs/P{P}F.json', 'w'), ensure_ascii=False)

def schema_piece(P, n, pos, page):
    """schema guidato: righe una alla volta a tempo con la voce. ritorna (stati, N, eventi audio, durata)"""
    pass
    items = [(f'P{P}_sch{n}_{k}', SL.html_schema(n, k, page)) for k in range(5)]
    items.append((f'P{P}_sch{n}_x', SL.html_schema(n, 5, page)))     # tutte le righe, nessuna accesa
    items.append((f'P{P}_sch{n}_e', SL.html_schema(n, -1, page)))    # vuota
    SL.render(items, W + '/slpng')
    audio = []; t = 0.8; starts = []
    for k in range(5):
        d = vdur(f'SC{n}_{k + 1}'); audio.append((t, 'wav', f'{VOX48}/SC{n}_{k + 1}.wav')); starts.append(t); t += d + 1.0
    tot = t - 1.0 + 1.4   # fine ultima voce + 3 s di schema fermo (nessun silenzio oltre 3 s)
    N = fr(tot)
    st = [(f'{W}/slpng/P{P}_sch{n}_e.png', fr(starts[0] - 0.15))]
    for k in range(5):
        end = fr(starts[k + 1] - 0.15) if k < 4 else N - fr(1.4)
        st.append((f'{W}/slpng/P{P}_sch{n}_{k}.png', end - sum(f for _, f in st)))
    st.append((f'{W}/slpng/P{P}_sch{n}_x.png', N - sum(f for _, f in st)))
    return st, N, audio, N / 30.0
