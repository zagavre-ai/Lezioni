# Compone un pezzo della prof: sfondo (card) + tondo ripulito (circa 2x, maschera tonda, colore leggero) + voce pulita. Pause tra frasi >1,2 s -> 0,6 s.
import sys,json,subprocess,os
sys.path.insert(0,'/home/user/lav/tools')
from frasi import parole_asr
from piani import *
from PIL import Image,ImageDraw
L='/home/user/lav/lez01/'
SRC=L+'Lezione.1.-.Preparazione.pt.1.mp4';AUD=L+'orig_clean.wav'
CX,CY,R=810,438,30          # tondino misurato (px sul video 852x480)
def maschera(path,d=128):
    s=4;im=Image.new('L',(d*s,d*s),0);ImageDraw.Draw(im).ellipse([(d/2-R*2)*s,(d/2-R*2)*s,(d/2+R*2)*s,(d/2+R*2)*s],fill=255)
    im.resize((d,d),Image.LANCZOS).save(path)
def comp(k,bg,out,a,b,W):
    iv=intervalli(a,b,W);n=len(iv)
    mk=L+'bg/maschera.png';maschera(mk)
    fv=[];fa=[]
    for i,(x,y) in enumerate(iv):
        fv.append(f"[1:v]trim=start={x-a:.3f}:end={y-a:.3f},setpts=PTS-STARTPTS[v{i}]")
        fa.append(f"[2:a]atrim=start={x-a:.3f}:end={y-a:.3f},asetpts=PTS-STARTPTS,afade=t=in:d=0.02,afade=t=out:st={max(0,y-x-0.03):.3f}:d=0.03[a{i}]")
    cv=''.join(f'[v{i}]' for i in range(n));ca=''.join(f'[a{i}]' for i in range(n))
    fc=';'.join(fv+fa)+f";{cv}concat=n={n}:v=1:a=0[vc];{ca}concat=n={n}:v=0:a=1[ac]"
    fc+=f";[vc]crop=64:64:{CX-32-a*0:.0f}:{CY-32}:exact=1,scale=128:128:flags=lanczos,eq=contrast=1.06:saturation=1.08:brightness=0.015,format=yuva420p[cv]"
    fc+=";[3:v]format=gray[m];[cv][m]alphamerge[ci];[0:v][ci]overlay=1576:144:format=auto:shortest=1,format=yuv420p[v]"
    cmd=['ffmpeg','-v','error','-y','-i',bg,'-ss',f'{a:.3f}','-t',f'{b-a:.3f}','-i',SRC,'-ss',f'{a:.3f}','-t',f'{b-a:.3f}','-i',AUD,'-framerate','30','-loop','1','-t',f'{b-a:.3f}','-i',mk,
         '-filter_complex',fc,'-map','[v]','-map','[ac]','-c:v','libx264','-preset','veryfast','-crf','17','-pix_fmt','yuv420p','-r','30','-c:a','pcm_s16le','-ar','48000','-shortest',out]
    subprocess.run(cmd,check=True)
if __name__=='__main__':
    k=int(sys.argv[1]);tr=json.load(open(L+'trasc.json'));W=parole_asr(tr)
    a,b=PEZZI[k];comp(k,L+f'bg/A{k:02d}/bg.mp4',L+f'bg/A{k:02d}/prof.mp4',a,b,W)
    print('ok')
