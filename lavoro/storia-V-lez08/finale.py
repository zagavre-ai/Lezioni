#!/usr/bin/env python3
# Codifica finale UNICA: x264 veryfast CRF 19, AAC 192k 48 kHz, parlato a -16 LUFS (loudnorm a due passate, lineare).
import sys, json, subprocess, re, os
V, OUT = sys.argv[1], sys.argv[2]; CRF = os.environ.get('CRF', '19')
m = subprocess.run(['ffmpeg', '-v', 'info', '-i', V, '-vn', '-af', 'loudnorm=I=-16:TP=-1.5:LRA=11:print_format=json', '-f', 'null', '-'], capture_output=True, text=True).stderr
j = json.loads(m[m.rfind('{'):m.rfind('}') + 1]); print('prima', j['input_i'], 'LUFS', j['input_tp'], 'dBTP', flush=True)
af = f"loudnorm=I=-16:TP=-1.5:LRA=11:measured_I={j['input_i']}:measured_TP={j['input_tp']}:measured_LRA={j['input_lra']}:measured_thresh={j['input_thresh']}:offset={j['target_offset']}:linear=true"
r = subprocess.run(['ffmpeg', '-v', 'error', '-y', '-i', V, '-map', '0:v', '-map', '0:a', '-c:v', 'libx264', '-preset', 'veryfast', '-crf', CRF, '-maxrate', '14M', '-bufsize', '28M', '-pix_fmt', 'yuv420p', '-r', '30',
                    '-af', af, '-c:a', 'aac', '-b:a', '192k', '-ar', '48000', '-ac', '2', '-movflags', '+faststart', OUT], capture_output=True, text=True)
if r.returncode: print(r.stderr[-800:]); sys.exit(1)
m2 = re.findall(r'I:\s+(-?[\d.]+) LUFS', subprocess.run(['ffmpeg', '-v', 'info', '-i', OUT, '-af', 'ebur128=peak=true', '-f', 'null', '-'], capture_output=True, text=True).stderr)
print('dopo', m2[-1], 'LUFS;', os.path.getsize(OUT) / 1e6, 'MB')
