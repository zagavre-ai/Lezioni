import sys,os,json,subprocess,re,shutil
sys.path.insert(0,'/tmp/L18/lib')
FPS=30;W='/tmp/L18';ST=W+'/st';SG=W+'/seg'
def run(cmd,**k):
    r=subprocess.run(cmd,capture_output=True,text=True,**k)
    if r.returncode:print(' '.join(cmd)[:400]);print(r.stderr[-1500:]);raise SystemExit(1)
    return r
def fr(x):return int(round(x*FPS))
ENC=['-c:v','libx264','-preset','veryfast','-crf','14','-pix_fmt','yuv420p','-r','30','-g','60','-an']
def stills(seq,out,cam=None,limit_prof=None):
    """seq=[(png,frames)]; cam=(ss,) -> sovrappone la webcam del prof dal tempo ss del video originale"""
    if os.path.exists(out):return
    lst=out+'.txt';n=0;os.makedirs(SG+'/clips',exist_ok=True)
    with open(lst,'w') as f:
        for png,k in seq:
            c=f"{SG}/clips/{os.path.basename(png)[:-4]}_{k}.mp4"
            if not os.path.exists(c):
                run(['ffmpeg','-y','-loglevel','error','-loop','1','-framerate','30','-i',png,'-frames:v',str(k),'-vf','format=yuv420p']+ENC+[c+'.t.mp4']);os.rename(c+'.t.mp4',c)
            f.write(f"file '{c}'\n");n+=k
    base=out+'.base.mp4' if cam is not None else out+'.tmp.mp4'
    run(['ffmpeg','-y','-loglevel','error','-f','concat','-safe','0','-i',lst,'-c','copy',base])
    if cam is not None:
        fc=("[1:v]crop=184:138:874:343,scale=412:309:flags=lanczos,eq=contrast=1.04:saturation=1.03,hqdn3d=1.5:1.5:3:3,cas=0.35,format=rgba[c];"
            "[2:v]format=gray[m];[c][m]alphamerge[cm];[0:v]format=rgba[b];[b][cm]overlay=1428:146:shortest=1,format=yuv420p[o]")
        cmd=['ffmpeg','-y','-loglevel','error','-i',base,'-ss',f'{cam:.3f}','-t',f'{n/FPS+0.5:.3f}','-i',W+'/prof.mp4','-loop','1','-framerate','30','-t',f'{n/FPS+0.5:.3f}','-i',ST+'/mask.png',
             '-filter_complex',fc,'-map','[o]','-frames:v',str(n)]+ENC+[out+'.tmp.mp4']
        run(cmd);os.remove(base)
    os.rename(out+'.tmp.mp4',out)
def nframes(p):
    r=run(['ffprobe','-v','error','-count_packets','-select_streams','v:0','-show_entries','stream=nb_read_packets','-of','csv=p=0',p]);return int(r.stdout.strip())
