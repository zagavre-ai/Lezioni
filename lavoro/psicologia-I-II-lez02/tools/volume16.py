# Porta il parlato a circa -16 LUFS rifacendo SOLO l'audio (video copiato, nessuna ricodifica dell'immagine).
# uso: python3 volume16.py VIDEO.mp4   -> sostituisce il file (il vecchio resta come VIDEO.mp4.prima_volume finché non lo cancelli)
import sys,re,json,subprocess,os,shutil
V=sys.argv[1]
def sh(c):return subprocess.run(c,capture_output=True,text=True)
m=sh(['ffmpeg','-v','info','-i',V,'-af','loudnorm=I=-16:TP=-1.5:LRA=11:print_format=json','-f','null','-']).stderr
j=json.loads(m[m.rfind('{'):m.rfind('}')+1]);print('prima',j['input_i'],'LUFS, picco',j['input_tp'])
if -17.0<=float(j['input_i'])<=-15.0:print('già nella norma');sys.exit()
af=f"loudnorm=I=-16:TP=-1.5:LRA=11:measured_I={j['input_i']}:measured_TP={j['input_tp']}:measured_LRA={j['input_lra']}:measured_thresh={j['input_thresh']}:offset={j['target_offset']}:linear=true"
T=V+'.tmp.mp4'
r=sh(['ffmpeg','-v','error','-y','-i',V,'-map','0','-c:v','copy','-af',af,'-c:a','aac','-b:a','192k','-ar','48000','-movflags','+faststart',T])
if r.returncode:print(r.stderr[-500:]);sys.exit(1)
m2=re.findall(r'I:\s+(-?[\d.]+) LUFS',sh(['ffmpeg','-v','info','-i',T,'-af','ebur128','-f','null','-']).stderr)
print('dopo',m2[-1],'LUFS')
os.replace(V,V+'.prima_volume');os.replace(T,V);print('FATTO',V)
