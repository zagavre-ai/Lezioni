import json,subprocess,os,sys
sys.path.insert(0,'.')
import plan
order=[n for n,a,b in plan.blocks]
open('final_list.txt','w').write(''.join(f"file '{os.path.abspath('seg/'+n+'.mp4')}'\n" for n in order))
OUT='/home/user/w/out/Letteratura_Lez12_Parte1_1080p.mp4'
subprocess.run(['ffmpeg','-v','error','-y','-f','concat','-safe','0','-i','final_list.txt','-i','/home/user/w/audio_nuovo.wav','-map','0:v','-map','1:a','-c:v','copy','-af','alimiter=limit=0.89:level=disabled','-c:a','aac','-b:a','192k','-ar','48000','-movflags','+faststart','-shortest',OUT],check=True)
print('fatto',OUT,os.path.getsize(OUT)/1e6,'MB')
