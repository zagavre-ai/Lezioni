import subprocess,os
FC=("[1:v]crop=184:138:857:341,scale=412:309:flags=lanczos,hqdn3d=1.5:1.5:3:3,eq=contrast=1.04:saturation=1.03,cas=0.35,format=yuv420p[c];"
    "[2:v]format=gray,scale=412:309[m];[c]format=yuva420p[c2];[c2][m]alphamerge[ca];"
    "[0:v]format=yuv420p[bg];[bg][ca]overlay=1428:148:format=auto,format=yuv420p[v]")
def encode(lst,s0,out,orig='/tmp/w14/Letteratura_Lez14.mp4',crf=19):
    parts=[];t=s0;base=out[:-4]
    for i,(nm,k) in enumerate(lst):
        d=k/30;po=f'{base}_s{i:03d}.mp4'
        cmd=['ffmpeg','-v','error','-y','-loop','1','-framerate','30','-t',f'{d:.4f}','-i',f'/tmp/w14/build/png/{nm}.png',
             '-ss',f'{t:.4f}','-t',f'{d+0.2:.4f}','-i',orig,'-loop','1','-framerate','30','-t',f'{d:.4f}','-i','/tmp/w14/build/mask.png',
             '-filter_complex',FC,'-map','[v]','-frames:v',str(k),'-r','30','-an','-threads','2','-filter_threads','1',
             '-c:v','libx264','-preset','veryfast','-crf',str(crf),'-pix_fmt','yuv420p','-x264-params','keyint=60:scenecut=0',po]
        r=subprocess.run(cmd,capture_output=True,text=True)
        if r.returncode: print(r.stderr[-800:]);raise SystemExit(1)
        parts.append(po);t+=d
    L=base+'_list.txt'
    open(L,'w').write(''.join(f"file '{p}'\n" for p in parts))
    r=subprocess.run(['ffmpeg','-v','error','-y','-f','concat','-safe','0','-i',L,'-c','copy',out],capture_output=True,text=True)
    if r.returncode: print(r.stderr[-500:]);raise SystemExit(1)
    for p in parts: os.remove(p)
