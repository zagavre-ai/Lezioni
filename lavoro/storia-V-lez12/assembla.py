# -*- coding: utf-8 -*-
# Assemblaggio finale: dissolvenza 0,5 s + trans.wav a ogni cambio di pezzo, audio a -16 LUFS, una sola codifica video (copia dei pezzi).
import os, sys, json, subprocess, re
sys.path.insert(0, '/home/user/Lezioni/lavoro/storia-V-lez12')
import montaggio as M
from montaggio import sh, X264, FPS, OUT, KIT
W = '/home/user/w12'
TR = 0.5

def info(nome):
    d = f'{OUT}/{nome}'
    r = sh(['ffprobe', '-v', 'error', '-count_packets', '-select_streams', 'v:0', '-show_entries', 'stream=nb_read_packets', '-of', 'csv=p=0', f'{d}/v.mp4'])
    n = int(r.stdout.strip().strip(','))
    return dict(nome=nome, mp4=f'{d}/v.mp4', wav=f'{d}/a.wav', frames=n, durata=n / FPS, ultimo=f'{d}/ultimo.png')

def lufs(wav):
    m = re.findall(r'I:\s+(-?[\d.]+) LUFS', sh(['ffmpeg', '-v', 'info', '-i', wav, '-af', 'ebur128', '-f', 'null', '-']).stderr)
    return float(m[-1])

def assembla(seq, uscita, tmp):
    os.makedirs(tmp, exist_ok=True)
    P = [info(n) for n in seq]
    # 1) video: clip di transizione (dissolvenza dall'ultimo fotogramma del pezzo prima) + corpo del pezzo (copia)
    lista = []; t = 0.0; tempi = []
    nt = round(TR * FPS)
    for i, p in enumerate(P):
        tempi.append((p['nome'], round(t, 3), round(p['durata'], 3), p['frames']))
        if i == 0 or p['frames'] <= nt + 2:
            lista.append(p['mp4']); t += p['durata']; continue
        tr = f'{tmp}/tr_{i}_{p["nome"]}.mp4'; body = f'{tmp}/b_{i}_{p["nome"]}.mp4'
        if not os.path.exists(tr):
            sh(['ffmpeg', '-v', 'error', '-y', '-loop', '1', '-framerate', '30', '-t', f'{TR}', '-i', P[i - 1]['ultimo'], '-t', f'{TR}', '-i', p['mp4'],
                '-filter_complex', f'[0:v]scale=1920:1080,format=yuv420p,fps=30[a];[1:v]format=yuv420p,fps=30[b];[a][b]xfade=transition=fade:duration={TR}:offset=0,format=yuv420p[v]',
                '-map', '[v]', '-frames:v', str(nt)] + X264 + [tr])
        if not os.path.exists(body):
            sh(['ffmpeg', '-v', 'error', '-y', '-ss', f'{TR}', '-i', p['mp4'], '-c', 'copy', '-an', body])
        lista += [tr, body]; t += p['durata']
    with open(f'{tmp}/lista.txt', 'w') as fh:
        for f in lista: fh.write(f"file '{f}'\n")
    video = f'{tmp}/video.mp4'
    sh(['ffmpeg', '-v', 'error', '-y', '-f', 'concat', '-safe', '0', '-i', f'{tmp}/lista.txt', '-c', 'copy', video])
    # 2) audio: pezzi del prof al livello giusto, Kore normalizzate; trans.wav ai cambi
    prof = [p for p in P if p['nome'].startswith('prof')]
    with open(f'{tmp}/prof.txt', 'w') as fh:
        for p in prof: fh.write(f"file '{p['wav']}'\n")
    sh(['ffmpeg', '-v', 'error', '-y', '-f', 'concat', '-safe', '0', '-i', f'{tmp}/prof.txt', '-c', 'copy', f'{tmp}/prof_tutto.wav'])
    gp = -16.0 - lufs(f'{tmp}/prof_tutto.wav')
    fc = []; ins = []; ai = []
    for i, p in enumerate(P):
        ins += ['-i', p['wav']]
        fc.append(f"[{i}:a]volume={gp:.2f}dB[a{i}]" if p['nome'].startswith('prof') else f"[{i}:a]anull[a{i}]")
        ai.append(f'[a{i}]')
    fc.append(''.join(ai) + f'concat=n={len(P)}:v=0:a=1[cat]')
    # trans.wav ai cambi di pezzo (a partire dal secondo)
    k = len(P); mix = ['[cat]']
    for i, (nome, t0, d, fr) in enumerate(tempi):
        if i == 0: continue
        ins += ['-i', f'{KIT}/suoni/trans.wav']
        ms = int(round(t0 * 1000))
        fc.append(f"[{k}:a]aresample=48000,pan=stereo|c0=c0|c1=c0,volume=0.7,adelay={ms}|{ms}[x{k}]"); mix.append(f'[x{k}]'); k += 1
    fc.append(''.join(mix) + f'amix=inputs={len(mix)}:normalize=0:duration=first,alimiter=limit=0.89:level=disabled[mx]')
    sh(['ffmpeg', '-v', 'error', '-y'] + ins + ['-filter_complex', ';'.join(fc), '-map', '[mx]', '-ar', '48000', '-ac', '2', '-c:a', 'pcm_s16le', f'{tmp}/mix.wav'])
    # 3) livello finale a -16 LUFS con solo guadagno lineare
    L = lufs(f'{tmp}/mix.wav'); g = -16.0 - L
    sh(['ffmpeg', '-v', 'error', '-y', '-i', f'{tmp}/mix.wav', '-af', f'volume={g:.2f}dB,alimiter=limit=0.89:level=disabled', '-ar', '48000', '-c:a', 'pcm_s16le', f'{tmp}/finale.wav'])
    sh(['ffmpeg', '-v', 'error', '-y', '-i', video, '-i', f'{tmp}/finale.wav', '-map', '0:v', '-map', '1:a', '-c:v', 'copy', '-c:a', 'aac', '-b:a', '192k', '-ar', '48000',
        '-movflags', '+faststart', uscita])
    json.dump(dict(pezzi=tempi, guadagno_prof_db=round(gp, 2), lufs_mix=L, guadagno_finale_db=round(g, 2)), open(f'{tmp}/timeline.json', 'w'), indent=1)
    return tempi

SEQ = ['sigla', 'cover_ben', 'prof0', 'argomenti']
for k in range(1, 7):
    SEQ += [f'tit{k}', f'prof{k}', f'app{k}'] + ([f'mappa{k}'] if k in (2, 4, 6) else []) + [f'pil{k}', f'quiz{k}']
SEQ += ['glossario', 'ripasso', 'mappe_fin', 'verifica', 'sigla_fin', 'compiti_intro', 'compiti']

if __name__ == '__main__':
    seq = SEQ if len(sys.argv) < 2 else sys.argv[1].split(',')
    out = f'{W}/Storia_Lez12_prova.mp4' if len(sys.argv) < 3 else sys.argv[2]
    t = assembla(seq, out, f'{W}/asm')
    print('durata totale', sum(x[2] for x in t) / 60, 'min')
