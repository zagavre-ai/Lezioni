import sys,os,json,subprocess,re
sys.path.insert(0,'/home/user/work/build')
from assemble import *
L=order();names,total=assemble(L,None,B+'/audio_raw.wav',B+'/tl_raw.json')
e=subprocess.run(['ffmpeg','-hide_banner','-nostats','-i',B+'/audio_raw.wav','-af','ebur128=peak=true','-f','null','-'],capture_output=True,text=True).stderr
I=float(re.findall(r'\n\s+I:\s+(-?[\d.]+) LUFS',e)[-1]);g=-16-I
subprocess.run(['ffmpeg','-y','-v','error','-i',B+'/audio_raw.wav','-af',f'volume={g:.2f}dB,alimiter=limit=0.89:attack=3:release=60:level=false','-ar','48000',B+'/audio_fin.wav'],check=True)
n=int(subprocess.run(['ffprobe','-v','error','-count_packets','-select_streams','v:0','-show_entries','stream=nb_read_packets','-of','csv=p=0',B+'/video_noaudio.mp4'],capture_output=True,text=True).stdout.strip())
subprocess.run(['ffmpeg','-y','-v','error','-i',B+'/video_noaudio.mp4','-i',B+'/audio_fin.wav','-c:v','copy','-t',str(n/30),'-c:a','aac','-b:a','192k','-ar','48000','-ac','2','-movflags','+faststart',B+'/Storia_Lez11_Parte1_1080p.mp4'],check=True)
print('REMUX',total,g)
