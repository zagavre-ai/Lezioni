import sys,subprocess,os,re
part=int(sys.argv[1]);out=sys.argv[2]
L=open(f'/tmp/w/b/list_P{part}.txt').read()
files=re.findall(r"file '(.+)'",L)
open(f'/tmp/w/b/vlist{part}.txt','w').write(''.join(f"file '{f}'\n" for f in files))
open(f'/tmp/w/b/alist{part}.txt','w').write(''.join(f"file '{f}.wav'\n" for f in files))
subprocess.run(['ffmpeg','-v','error','-y','-f','concat','-safe','0','-i',f'/tmp/w/b/vlist{part}.txt','-an','-c:v','copy',f'/tmp/w/b/v{part}.mp4'],check=True)
subprocess.run(['ffmpeg','-v','error','-y','-f','concat','-safe','0','-i',f'/tmp/w/b/alist{part}.txt','-af','volume=-2.7dB','-c:a','aac','-b:a','192k','-ar','48000','-ac','2',f'/tmp/w/b/a{part}.m4a'],check=True)
subprocess.run(['ffmpeg','-v','error','-y','-i',f'/tmp/w/b/v{part}.mp4','-i',f'/tmp/w/b/a{part}.m4a','-map','0:v','-map','1:a','-c','copy','-movflags','+faststart',out],check=True)
print(subprocess.run(['ffprobe','-v','error','-count_packets','-select_streams','v:0','-show_entries','stream=nb_read_packets:format=duration,size','-of','compact',out],capture_output=True,text=True).stdout)
