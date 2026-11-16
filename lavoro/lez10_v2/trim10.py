import json,subprocess,os,concurrent.futures as cf
KEEP=json.load(open('keep.json'))['1']
os.makedirs('dt/seg',exist_ok=True)
def seg(a):
    i,x,y=a;o=f'dt/seg/p1_{i:03d}.mkv'
    if os.path.exists(o): return
    d=y-x
    subprocess.run(['ffmpeg','-y','-v','error','-ss',f'{x:.3f}','-t',f'{d:.3f}','-i','ENG_Amm_Lez10_Videolezione.mp4','-vf','fps=30,crop=1440:1080:240:0,scale=640:480','-af',f'aresample=48000,highpass=f=80,arnndn=m=/home/claude/tools/sh.rnnn,loudnorm=I=-16:TP=-1.5:LRA=11,alimiter=limit=0.89:level=disabled,aresample=48000,aformat=channel_layouts=stereo,afade=t=in:d=0.02,afade=t=out:st={max(0,d-0.02):.3f}:d=0.02','-c:v','libx264','-preset','veryfast','-crf','20','-pix_fmt','yuv420p','-g','30','-c:a','pcm_s16le',o+'.tmp.mkv'],check=True)
    os.rename(o+'.tmp.mkv',o)
J=[(i,a,b) for i,(a,b) in enumerate(KEEP)]
with cf.ThreadPoolExecutor(1) as ex: list(ex.map(seg,J))
with open('dt/list.txt','w') as f:
    for i,a,b in J: f.write(f"file 'seg/p1_{i:03d}.mkv'\n")
subprocess.run(['ffmpeg','-y','-v','error','-f','concat','-safe','0','-i','dt/list.txt','-c','copy','dt/docente_all.mkv'],check=True)
d=[(1,i,a,b,float(subprocess.check_output(['ffprobe','-v','error','-show_entries','format=duration','-of','csv=p=0',f'dt/seg/p1_{i:03d}.mkv']))) for i,a,b in J]
json.dump(d,open('segdur.json','w'));open('dt/fatto','w').write('1')
