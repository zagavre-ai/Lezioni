# Assemblaggio finale: corpi dei pezzi copiati senza ricodificare + dissolvenze di 12 fotogrammi codificate a parte; audio sommato a campione esatto
import os, sys, json, subprocess, shutil
import numpy as np
sys.path.insert(0, '/tmp/w/build')
from core import *

ORDER = ['SIGLA', 'COVER', 'INTRO_A', 'INTRO_B']
for i in range(1, 6): ORDER += [f'TIT{i}', f'T{i}', f'APP{i}', f'RIP{i}', f'QZ{i}']
ORDER += ['GLOSS', 'RIEPILOGO', 'MAPPA_M1', 'MAPPA_M2', 'VERIFICA', 'SIGLA_FINALE', 'COMPITI_INTRO', 'COMPITI']
TLNAME = {'SIGLA': 'SIGLA', 'COVER': 'COVER', 'INTRO_A': 'INTRO1', 'INTRO_B': 'INTRO2', 'GLOSS': 'GL', 'RIEPILOGO': 'RF', 'MAPPA_M1': 'M1', 'MAPPA_M2': 'M2', 'VERIFICA': 'VER', 'SIGLA_FINALE': 'SIGF', 'COMPITI_INTRO': 'CI', 'COMPITI': 'CO'}
for i in range(1, 6): TLNAME.update({f'TIT{i}': f'T{i}', f'T{i}': f'D{i}', f'APP{i}': f'A{i}', f'RIP{i}': f'P{i}', f'QZ{i}': f'Q{i}'})

def meta(name):
    p = f'{PIECES}/{name}.json'
    if os.path.exists(p): return json.load(open(p))
    # pezzi delle mappe (dal fork): ricodificati con fotogrammi chiave nei punti di dissolvenza
    v = f'{PIECES}/{name}.mp4'; w = f'{WORK}/{name}.wav'; k = f'{WORK}/{name}_k.mp4'
    if not os.path.exists(k) or os.path.getmtime(k) < os.path.getmtime(v):
        n = int(sh(['ffprobe', '-v', 'error', '-count_packets', '-select_streams', 'v:0', '-show_entries', 'stream=nb_read_packets', '-of', 'csv=p=0', v]).stdout.strip())
        enc = ['24' if a == '19' else a for a in ENC]
        sh(['ffmpeg', '-y', '-v', 'error', '-i', v, '-vf', 'fps=30,format=yuv420p', '-frames:v', str(n)] + enc + ['-force_key_frames', kf(n), '-an', k])
        real = os.path.exists('/tmp/w/vox/' + name.replace('MAPPA_', '') + '_MAPPA.wav')
        x = load_audio(v, af='loudnorm=I=-16:TP=-1.5:LRA=7' if real else None)
        if len(x) < n * SPF: x = np.vstack([x, np.zeros((n * SPF - len(x), 2), np.float32)])
        write_wav(w, x[:n * SPF])
    n = int(sh(['ffprobe', '-v', 'error', '-count_packets', '-select_streams', 'v:0', '-show_entries', 'stream=nb_read_packets', '-of', 'csv=p=0', k]).stdout.strip())
    return {'name': name, 'n': n, 'video': k, 'wav': w}

def run(out, order=ORDER, only_video=False, gain_db=None):
    M = [meta(n) for n in order]; N = len(M)
    for m in M: assert m['n'] > 2 * TR + 2, m
    starts = [0]
    for i in range(1, N): starts.append(starts[-1] + M[i - 1]['n'] - TR)
    total = starts[-1] + M[-1]['n']
    W = out + '.parti'; os.makedirs(W, exist_ok=True)
    segs = []
    for i, m in enumerate(M):
        a = 0 if i == 0 else TR; b = m['n'] if i == N - 1 else m['n'] - TR
        body = f'{W}/b{i:02d}.mp4'
        if not os.path.exists(body + '.ok'):
            sh(['ffmpeg', '-y', '-v', 'error', '-ss', '%.5f' % (a / FPS), '-i', m['video'], '-frames:v', str(b - a), '-c', 'copy', '-an', body]); open(body + '.ok', 'w').write('1')
        segs.append(body)
        if i < N - 1:
            tr = f'{W}/x{i:02d}.mp4'
            if not os.path.exists(tr + '.ok'):
                nx = M[i + 1]
                sh(['ffmpeg', '-y', '-v', 'error', '-ss', '%.5f' % ((m['n'] - TR) / FPS), '-i', m['video'], '-i', nx['video'],
                    '-filter_complex', f'[0:v]trim=end_frame={TR},setpts=PTS-STARTPTS[a];[1:v]trim=end_frame={TR},setpts=PTS-STARTPTS[b];[a][b]xfade=transition=fade:duration={TR / FPS:.4f}:offset=0,format=yuv420p[v]',
                    '-map', '[v]', '-frames:v', str(TR)] + ENC + ['-force_key_frames', '0', '-an', tr]); open(tr + '.ok', 'w').write('1')
            segs.append(tr)
    lst = f'{W}/lista.txt'; open(lst, 'w').write(''.join(f"file '{s}'\n" for s in segs))
    vid = f'{W}/video.mp4'
    sh(['ffmpeg', '-y', '-v', 'error', '-f', 'concat', '-safe', '0', '-i', lst, '-c', 'copy', vid])
    # audio
    A = np.zeros((total * SPF, 2), np.float32)
    trans = load_audio(f'{KIT}/suoni/trans.wav')[:int(0.8 * SR)]; trans = fade(trans, 5, 250)
    for i, m in enumerate(M):
        x = load_audio(m['wav'])
        if i < N - 1:
            k = TR * SPF; x[-k:] *= np.linspace(1, 0, k)[:, None]
        s = starts[i] * SPF; A[s:s + len(x)] += x
        if i < N - 1:
            t0 = (starts[i] + m['n'] - TR) * SPF; A[t0:t0 + len(trans)] += trans * 0.55
    wp = f'{W}/audio_grezzo.wav'; write_wav(wp, A)
    # livello: -16 LUFS integrati con guadagno lineare (la voce non cambia timbro)
    mm = sh(['ffmpeg', '-v', 'info', '-i', wp, '-af', 'loudnorm=I=-16:TP=-1.5:print_format=json', '-f', 'null', '-']).stderr.decode()
    j = json.loads(mm[mm.rfind('{'):mm.rfind('}') + 1]); g = -16.0 - float(j['input_i']) if gain_db is None else gain_db
    af = f'volume={g:.2f}dB,alimiter=limit=0.79:level=disabled'
    final_a = f'{W}/audio.m4a'
    sh(['ffmpeg', '-y', '-v', 'error', '-i', wp, '-af', af, '-c:a', 'aac', '-b:a', '192k', '-ar', '48000', final_a])
    sh(['ffmpeg', '-y', '-v', 'error', '-i', vid, '-i', final_a, '-map', '0:v', '-map', '1:a', '-c', 'copy', '-movflags', '+faststart', out])
    TL = []
    for i, m in enumerate(M):
        d = (m['n'] - (TR if i < N - 1 else 0)) / FPS
        TL.append([TLNAME.get(m['name'], m['name']), round(starts[i] / FPS, 3), round(d, 3)])
    json.dump(TL, open(out.replace('.mp4', '_timeline.json'), 'w'), indent=0)
    print('totale', total, 'fotogrammi', round(total / FPS, 1), 's; guadagno', round(g, 2), 'dB; input_i', j['input_i'])
    return TL

if __name__ == '__main__':
    out = sys.argv[1]; order = sys.argv[2].split(',') if len(sys.argv) > 2 else ORDER
    run(out, order)
