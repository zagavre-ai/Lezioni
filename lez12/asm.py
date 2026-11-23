# Assembla: lista concat, timeline_Parte1.json, durata totale. uso: python3 asm.py
import sys, os, json, subprocess
sys.path.insert(0, '/home/user/Lezioni/lez12')
import engine as E, piano as PI
def nfr(f):
    r = subprocess.run(['ffprobe', '-v', 'error', '-select_streams', 'v:0', '-count_packets', '-show_entries', 'stream=nb_read_packets', '-of', 'csv=p=0', f], capture_output=True, text=True).stdout.strip()
    return int(r)
tl = []; t = 0.0; lst = []; tot = 0
for n in PI.SEQ:
    f = E.B + n + '.mov'
    if not os.path.exists(f): print('MANCA', n); sys.exit(1)
    k = nfr(f); d = k / 30.0
    tl.append([n, round(t, 3), round(d, 3)]); t += d; tot += k; lst.append(f"file '{f}'\n")
open(E.W + 'lista.txt', 'w').write(''.join(lst))
json.dump(tl, open(E.W + 'consegna/timeline_Parte1.json', 'w'))
print('scene', len(tl), 'fotogrammi', tot, 'durata', round(t, 1), 's =', round(t / 60, 2), 'min')
