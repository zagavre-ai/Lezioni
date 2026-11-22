import json,subprocess,re,sys,os
W='/home/user/w';OUT=W+'/final';os.makedirs(OUT,exist_ok=True)
V=OUT+'/Storia_Lez16_Parte1_1080p.mp4'
crf=sys.argv[1] if len(sys.argv)>1 else '19'
def sh(c):return subprocess.run(c,capture_output=True,text=True)
m=sh(['ffmpeg','-v','info','-f','concat','-safe','0','-i',W+'/out/concat.txt','-vn','-af','loudnorm=I=-16:TP=-1.5:LRA=11:print_format=json','-f','null','-']).stderr
j=json.loads(m[m.rfind('{'):m.rfind('}')+1]);print('misura',j['input_i'],j['input_tp'],j['input_lra'])
af=f"loudnorm=I=-16:TP=-1.5:LRA=11:measured_I={j['input_i']}:measured_TP={j['input_tp']}:measured_LRA={j['input_lra']}:measured_thresh={j['input_thresh']}:offset={j['target_offset']}:linear=true"
r=sh(['ffmpeg','-v','error','-y','-f','concat','-safe','0','-i',W+'/out/concat.txt','-c:v','libx264','-preset','veryfast','-crf',crf,'-pix_fmt','yuv420p','-r','30','-af',af,'-c:a','aac','-b:a','192k','-ar','48000','-movflags','+faststart',V])
print(r.stderr[-500:]);print(os.path.getsize(V)/1e6,'MB')
