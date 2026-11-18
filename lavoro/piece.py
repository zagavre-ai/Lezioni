import subprocess,os,hashlib
W='/tmp/claude-0/l15'
def _clip(png,frames):
    h=hashlib.md5(f'{png}{frames}{os.path.getmtime(png)}'.encode()).hexdigest()[:12]
    out=f'{W}/segs/{h}.mp4'
    if not os.path.exists(out):
        os.makedirs(f'{W}/segs',exist_ok=True)
        subprocess.run(['ffmpeg','-y','-v','error','-loop','1','-framerate','30','-i',png,'-frames:v',str(frames),'-c:v','libx264','-preset','ultrafast','-crf','9','-pix_fmt','yuv420p','-g','30','-r','30',out+'.tmp.mp4'],check=True)
        os.rename(out+'.tmp.mp4',out)
    return out
def seg_files(png,frames):
    q,r=divmod(frames,30);L=[]
    if q: L+= [_clip(png,30)]*q
    if r: L.append(_clip(png,r))
    return L
def seg_video(png,frames):
    return _clip(png,frames)
def prof_piece(a,dur,states,out,src=W+'/dl/v.mp4',w=W):
    """a: secondo di inizio nel video del prof; dur: secondi; states: [(png,frames)] la cui somma = round(dur*30)"""
    N=round(dur*30);assert sum(f for _,f in states)==N,(sum(f for _,f in states),N)
    lst=out+'.txt'
    with open(lst,'w') as f:
        for p,fr in states:
            for x in seg_files(p,fr):f.write(f"file '{x}'\n")
    fc=("[0:v]format=yuv420p[bg];[1:v]crop=181:136:856:344,scale=412:310:flags=lanczos,hqdn3d=1.5:1.5:3:3,eq=contrast=1.04:saturation=1.03,cas=0.35,format=yuva420p[p];"
        "[2:v]format=gray[m];[p][m]alphamerge[pa];[bg][pa]overlay=1428:148:format=auto,format=yuv420p[v]")
    cmd=['ffmpeg','-y','-v','error','-f','concat','-safe','0','-i',lst,'-ss',f'{a:.3f}','-t',f'{dur+0.5:.3f}','-i',src,'-loop','1','-framerate','30','-t',f'{dur+0.5:.3f}','-i',w+'/mask.png',
         '-filter_complex',fc,'-map','[v]','-frames:v',str(N),'-c:v','libx264','-preset','veryfast','-crf','23','-r','30','-g','60','-force_key_frames',f'0.4,{dur-0.4:.3f}','-pix_fmt','yuv420p','-an',out]
    subprocess.run(cmd,check=True)
