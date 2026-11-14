#!/bin/bash
# uso: norm_doc.sh video.mp4 out48.wav  (normalizza il parlato a -16 LUFS, 2 passaggi, 48k stereo)
V="$1"; O="$2"
M=$(ffmpeg -v info -i "$V" -vn -af loudnorm=I=-16:TP=-1.5:LRA=11:print_format=json -f null - 2>&1)
python3 - "$V" "$O" "$M" <<'P'
import sys,json,subprocess
V,O,M=sys.argv[1:4];j=json.loads(M[M.rfind('{'):M.rfind('}')+1])
af=f"loudnorm=I=-16:TP=-1.5:LRA=11:measured_I={j['input_i']}:measured_TP={j['input_tp']}:measured_LRA={j['input_lra']}:measured_thresh={j['input_thresh']}:offset={j['target_offset']}:linear=true"
subprocess.run(['ffmpeg','-v','error','-y','-i',V,'-vn','-af',af,'-ar','48000','-ac','2','-c:a','pcm_s16le',O],check=True);print('prima',j['input_i'])
P
