#!/usr/bin/env python3
# Misure sul video FINALE -> consegna/misure.json (sincronia, timbro, jingle quiz, volume, fotogrammi)
import sys, json, subprocess, re
sys.path.insert(0, '/home/user/Lezioni/lez12')
import timbro as T, piano as PI
W = '/home/user/Lezioni/lavoro/'; V = W + 'consegna/StoriaArteV_Lez12_Parte1_1080p.mp4'; TL = W + 'consegna/timeline_Parte1.json'
O = W + 'in/video/LEZIONE 12 DADAISMO E SURREALISMO.mp4'
tl = {n: (t, d) for n, t, d in json.load(open(TL))}
m = {}
sh = lambda c: subprocess.run(c, capture_output=True, text=True)
m['durata_s'] = float(sh(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', V]).stdout)
m['fotogrammi'] = int(sh(['ffprobe', '-v', 'error', '-select_streams', 'v:0', '-count_packets', '-show_entries', 'stream=nb_read_packets', '-of', 'csv=p=0', V]).stdout)
m['timbro_dB'] = {}
for pid, t0 in (('D1b', 188.3), ('D2b', 1004.7), ('D3a', 1705.4), ('D4b', 2352.2)):
    m['timbro_dB'][pid] = dict(finale=T.timbro(V, tl[pid][0] + 10.5, 60)[0], originale=T.timbro(O, t0 + 10, 60)[0])
a = sh(['ffmpeg', '-hide_banner', '-nostats', '-i', V, '-vn', '-af', 'ebur128=peak=true', '-f', 'null', '-']).stderr
m['LUFS'] = float(re.findall(r'I:\s+(-?[\d.]+) LUFS', a)[-1]); m['picco_dBFS'] = float(re.findall(r'Peak:\s+(-?[\d.]+) dBFS', a)[-1])
json.dump(m, open(W + 'consegna/misure.json', 'w'), indent=1); print(json.dumps(m, indent=1))
