import json,sys,os,subprocess
sys.path.insert(0,'/tmp/w14');sys.path.insert(0,'/tmp/w14/build')
import gen,buildd
ENC=['-c:v','libx264','-preset','veryfast','-crf','19','-pix_fmt','yuv420p','-r','30','-an','-x264-params','keyint=60:scenecut=0','-threads','2']
for P in (1,2):
    TL=json.load(open(f'/tmp/w14/tl{P}.json'));os.makedirs(f'/tmp/w14/new{P}',exist_ok=True)
    ss=0.6 if P==1 else 2040.0
    cam=f'/tmp/w14/build/cam{P}.png'
    subprocess.run(['ffmpeg','-v','error','-y','-ss',str(ss),'-i','/tmp/w14/Letteratura_Lez14.mp4','-frames:v','1',cam],check=True)
    gen.scrivi(f'newcover{P}',gen.cover(f'Luigi Pirandello · Parte {P}',buildd.ARGS[P],pag=1))
    for n,a,d in TL:
        if n.startswith('T') and n[1:].isdigit():
            gen.scrivi(f'newT{P}_{n}',gen.sezione(int(n[1:]),buildd.ARGS[P][int(n[1:])-1]))
subprocess.run(['node','/tmp/w14/build/render.js','/tmp/w14/build/html','/tmp/w14/build/png'],check=True)
FCC="[1:v]crop=184:138:857:341,scale=412:309:flags=lanczos,hqdn3d=1.5:1.5:3:3,eq=contrast=1.04:saturation=1.03,cas=0.35,format=yuv420p[c];[2:v]format=gray,scale=412:309[m];[c]format=yuva420p[c2];[c2][m]alphamerge[ca];[0:v]format=yuv420p[bg];[bg][ca]overlay=1428:148:format=auto,format=yuv420p[v]"
for P in (1,2):
    TL=json.load(open(f'/tmp/w14/tl{P}.json'));TOT={1:90226,2:87491}[P]
    for n,a,d in TL:
        f0=round(a*30);f1=round((a+d)*30);k=f1-f0;out=f'/tmp/w14/new{P}/{n}.mp4'
        if os.path.exists(out): continue
        if n.startswith('INTRO') or n.startswith('BINTRO'):
            c=['ffmpeg','-v','error','-y','-loop','1','-framerate','30','-t',f'{k/30:.4f}','-i',f'/tmp/w14/build/png/newcover{P}.png','-loop','1','-framerate','30','-t',f'{k/30:.4f}','-i',f'/tmp/w14/build/cam{P}.png','-loop','1','-framerate','30','-t',f'{k/30:.4f}','-i','/tmp/w14/build/mask.png','-filter_complex',FCC,'-map','[v]','-frames:v',str(k),*ENC,out]
        elif n.startswith('T') and n[1:].isdigit():
            c=['ffmpeg','-v','error','-y','-loop','1','-framerate','30','-t',f'{k/30:.4f}','-i',f'/tmp/w14/build/png/newT{P}_{n}.png','-frames:v',str(k),*ENC,out]
        else: continue
        r=subprocess.run(c,capture_output=True,text=True)
        if r.returncode: print(n,r.stderr[-300:])
print('fatto')
