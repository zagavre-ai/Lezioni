import json,subprocess,os
OFF=[0,921.0,1804.6,2654.03]
S=json.load(open('sil.json'));al=json.load(open('align.json'))
DUR={1:921.0,2:883.6,3:849.4333,4:748.6}
KEEP={}  # per parte: lista (a,b) originali
for p in range(1,5):
    K=[];cur=0.0
    for s,e in S[str(p)]:
        d=e-s
        if d<=1.0: continue
        if s<0.1: cur=max(0,e-0.3);continue   # silenzio iniziale
        if e>DUR[p]-0.1: K.append((cur,s+0.3));cur=None;break   # silenzio finale
        K.append((cur,s+0.3));cur=e-0.3
    if cur is not None: K.append((cur,DUR[p]))
    KEEP[p]=K
    print(p,len(K),'tenuto',round(sum(b-a for a,b in K),1),'di',DUR[p])
json.dump(KEEP,open('keep.json','w'))
if not os.path.exists('dt'): os.makedirs('dt')
names={1:'Aparte1',2:'A.perte.2',3:'BPARTE.1',4:'B.PARTE2'}
for p in range(1,5):
    out=f'dt/part{p}.mkv'
    if os.path.exists(out): continue
    K=KEEP[p];fc=[];lab=''
    for i,(a,b) in enumerate(K):
        fc.append(f'[0:v]trim={a:.3f}:{b:.3f},setpts=PTS-STARTPTS,fps=30,crop=1440:1080:240:0,scale=640:480[v{i}]')
        fc.append(f'[0:a]atrim={a:.3f}:{b:.3f},asetpts=PTS-STARTPTS,aresample=48000,aformat=channel_layouts=stereo,afade=t=in:d=0.02,afade=t=out:st={max(0,b-a-0.02):.3f}:d=0.02[a{i}]')
        lab+=f'[v{i}][a{i}]'
    fc.append(f'{lab}concat=n={len(K)}:v=1:a=1[v][a]')
    open(f'dt/fc{p}.txt','w').write(';\n'.join(fc))
    subprocess.run(['ffmpeg','-y','-v','error','-i',f'ENG_Amm_Lez04_video_{names[p]}.mp4','-filter_complex_script',f'dt/fc{p}.txt','-map','[v]','-map','[a]','-c:v','libx264','-preset','veryfast','-crf','20','-pix_fmt','yuv420p','-c:a','pcm_s16le',out],check=True)
    print('ok',p,flush=True)
