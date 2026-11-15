import json,subprocess,os,concurrent.futures as cf
KEEP=json.load(open('keep.json'))
names={1:'Aparte1',2:'A.perte.2',3:'BPARTE.1',4:'B.PARTE2'}
os.makedirs('dt/seg',exist_ok=True)
def seg(a):
    p,i,x,y=a
    o=f'dt/seg/p{p}_{i:03d}.mkv'
    if os.path.exists(o): return
    d=y-x
    subprocess.run(['ffmpeg','-y','-v','error','-ss',f'{x:.3f}','-t',f'{d:.3f}','-i',f'ENG_Amm_Lez04_video_{names[p]}.mp4','-vf','fps=30,crop=1440:1080:240:0,scale=640:480','-af',f'aresample=48000,aformat=channel_layouts=stereo,afade=t=in:d=0.02,afade=t=out:st={max(0,d-0.02):.3f}:d=0.02','-c:v','libx264','-preset','veryfast','-crf','20','-pix_fmt','yuv420p','-g','30','-c:a','pcm_s16le',o+'.tmp.mkv'],check=True)
    os.rename(o+'.tmp.mkv',o)
J=[(int(p),i,a,b) for p,K in KEEP.items() for i,(a,b) in enumerate(K)]
with cf.ThreadPoolExecutor(4) as ex: list(ex.map(seg,J))
with open('dt/list.txt','w') as f:
    for p,i,a,b in J: f.write(f"file 'seg/p{p}_{i:03d}.mkv'\n")
subprocess.run(['ffmpeg','-y','-v','error','-f','concat','-safe','0','-i','dt/list.txt','-c','copy','dt/docente_all.mkv'],check=True)
open('dt/fatto','w').write('1')
