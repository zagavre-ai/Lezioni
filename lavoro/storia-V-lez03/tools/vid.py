import subprocess,os,sys
X264=['-c:v','libx264','-preset','veryfast','-crf','19','-g','60','-keyint_min','30','-pix_fmt','yuv420p','-r','30','-an','-movflags','+faststart']
def run(cmd):
    r=subprocess.run(cmd,capture_output=True,text=True)
    if r.returncode: raise RuntimeError(' '.join(cmd)[:300]+'\n'+r.stderr[-600:])
def lst(path,seq):
    with open(path,'w') as f:
        for png,fr in seq: f.write(f"file '{png}'\nduration {fr/30:.6f}\n")
        f.write(f"file '{seq[-1][0]}'\n")
def enc_seq(seq,out,threads=1):
    total=sum(f for _,f in seq);l=out+'.txt';lst(l,seq)
    run(['ffmpeg','-v','error','-y','-f','concat','-safe','0','-i',l,'-vf','fps=30,format=yuv420p','-frames:v',str(total),'-threads',str(threads)]+X264+[out]);os.remove(l)
def enc_card(mp4,frames,out,threads=1):
    run(['ffmpeg','-v','error','-y','-i',mp4,'-vf',f'fps=30,tpad=stop_mode=clone:stop_duration=2,format=yuv420p','-frames:v',str(frames),'-threads',str(threads)]+X264+[out])
def enc_prof(seq,src,t0,out,threads=1):
    total=sum(f for _,f in seq);l=out+'.txt';lst(l,seq)
    fc=("[1:v]crop=184:138:847:344,scale=410:308:flags=lanczos,hqdn3d=1.5:1.5:3:3,eq=contrast=1.04:saturation=1.03,cas=0.35,format=rgba[c];"
        "[2:v]format=gray,scale=410:308[m];[c][m]alphamerge[cm];[0:v][cm]overlay=1428:146:format=auto,format=yuv420p")
    run(['ffmpeg','-v','error','-y','-f','concat','-safe','0','-i',l,'-ss',f'{t0:.6f}','-i',src,'-loop','1','-framerate','30','-i','/tmp/w/build/mask.png',
         '-filter_complex',fc,'-frames:v',str(total),'-threads',str(threads)]+X264+[out]);os.remove(l)
def enc_trans(a_png,b_png,frames,out):
    d=frames/30
    run(['ffmpeg','-v','error','-y','-loop','1','-framerate','30','-t',f'{d:.4f}','-i',a_png,'-loop','1','-framerate','30','-t',f'{d:.4f}','-i',b_png,
         '-filter_complex',f'[0:v][1:v]xfade=transition=fade:duration={d:.4f}:offset=0,format=yuv420p','-frames:v',str(frames)]+X264+[out])
def last_frame(mp4,png):
    run(['ffmpeg','-v','error','-y','-sseof','-0.1','-i',mp4,'-update','1','-frames:v','1',png])
def first_frame(mp4,png):
    run(['ffmpeg','-v','error','-y','-i',mp4,'-frames:v','1',png])
