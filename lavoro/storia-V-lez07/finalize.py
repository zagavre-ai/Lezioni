# Sostituisce l'audio del video codificato con un audio rifatto UNA volta dai pezzi (PCM) con limitatore (picco <= -1 dBTP).
import sys,subprocess,os,glob
V=sys.argv[1]; LIST=sys.argv[2]; OUT=sys.argv[3]
G=V+'.gruppi/'
vl=G+'v.txt'
a=G+'a_lim.m4a'
r=subprocess.run(['ffmpeg','-y','-v','error','-f','concat','-safe','0','-i',LIST,'-map','0:a','-af','alimiter=limit=0.80:attack=5:release=60:level=0','-c:a','aac','-b:a','192k','-ar','48000',a],capture_output=True,text=True)
if r.returncode: raise SystemExit(r.stderr[-500:])
r=subprocess.run(['ffmpeg','-y','-v','error','-f','concat','-safe','0','-i',vl,'-i',a,'-map','0:v','-map','1:a','-c','copy','-movflags','+faststart',OUT],capture_output=True,text=True)
if r.returncode: raise SystemExit(r.stderr[-500:])
print('ok',OUT)
