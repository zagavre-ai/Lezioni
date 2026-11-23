# porta l'audio di ogni scena a N*1600 campioni esatti (N = fotogrammi), senza ricodificare il video
import sys, os, subprocess
sys.path.insert(0, '/home/user/Lezioni/lez12')
import engine as E, piano as PI
for n in PI.SEQ:
    f = E.B + n + '.mov'
    if os.path.exists(f + '.aok'): continue
    N = int(subprocess.run(['ffprobe', '-v', 'error', '-select_streams', 'v:0', '-count_packets', '-show_entries', 'stream=nb_read_packets', '-of', 'csv=p=0', f], capture_output=True, text=True).stdout)
    tmp = E.B + 'fx_' + n + '.mov'
    E.run(['ffmpeg', '-y', '-v', 'error', '-i', f, '-map', '0:v', '-map', '0:a', '-c:v', 'copy', '-af', f'asetpts=N/SR/TB,apad=whole_len={N*1600},atrim=end_sample={N*1600}', '-c:a', 'pcm_s16le', tmp])
    os.replace(tmp, f); open(f + '.aok', 'w').write('1'); print(n, N, flush=True)
