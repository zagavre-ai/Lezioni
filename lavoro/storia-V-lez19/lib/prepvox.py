import os,subprocess,json,glob,sys
D='/home/claude/w19/vox';N='/home/claude/w19/voxn';os.makedirs(N,exist_ok=True)
dur={}
for f in sorted(glob.glob(D+'/*.wav')):
    n=os.path.basename(f)[:-4];o=f'{N}/{n}.wav'
    if not os.path.exists(o):
        subprocess.run(['ffmpeg','-v','error','-y','-i',f,'-af','loudnorm=I=-16:TP=-1.5:LRA=7,aresample=48000','-ac','2','-ar','48000',o],check=True)
    dur[n]=float(subprocess.run(['ffprobe','-v','error','-show_entries','format=duration','-of','csv=p=0',o],capture_output=True,text=True).stdout)
json.dump(dur,open('/home/claude/w19/vox_dur.json','w'),indent=0)
print(len(dur))
