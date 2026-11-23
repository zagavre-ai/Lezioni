# Estrae la webcam del prof (posizione seguita fotogramma per fotogramma) in un video intra-frame 412x309
import cv2,subprocess,numpy as np,json,sys
W,H=1092,614
tr=json.load(open('/tmp/claude-0/w/lez07/camtrack6.json'))
# posizioni: ultimo valore buono (score>=0.6) ; spostamenti piccoli (<=2 px) ignorati
pos=[];last=(825,343)
for t,s,x,y in tr:
    if s>=0.6 and (abs(x-last[0])>2 or abs(y-last[1])>2):last=(x,y)
    pos.append(last)
def posat(n):
    i=min(len(pos)-1,int(round(n/30*6)));return pos[i]
src='/tmp/claude-0/w/lez07/LEZIONE 7 LE AVANGUARDIE.mp4'
dec=subprocess.Popen(['ffmpeg','-v','error','-i',src,'-f','rawvideo','-pix_fmt','bgr24','-'],stdout=subprocess.PIPE)
enc=subprocess.Popen(['ffmpeg','-v','error','-y','-f','rawvideo','-pix_fmt','bgr24','-s','412x309','-r','30','-i','-','-c:v','libx264','-preset','veryfast','-crf','8','-g','1','-pix_fmt','yuv444p','/tmp/claude-0/w/lez07/cam_all.mp4'],stdin=subprocess.PIPE)
n=0
k=np.array([[0,-1,0],[-1,5,-1],[0,-1,0]],np.float32)
while True:
    b=dec.stdout.read(W*H*3)
    if len(b)<W*H*3:break
    im=np.frombuffer(b,np.uint8).reshape(H,W,3)
    x,y=posat(n)
    c=im[y+2:y+137,x+33:x+213]            # 180x135 (4:3), centrato sulla webcam 246x139
    c=cv2.resize(c,(412,309),interpolation=cv2.INTER_LANCZOS4)
    bl=cv2.GaussianBlur(c,(0,0),1.2);c=cv2.addWeighted(c,1.35,bl,-0.35,0)   # nitidezza leggera
    c=np.clip((c.astype(np.float32)-128)*1.05+128+2,0,255).astype(np.uint8)  # correzione colore leggera
    enc.stdin.write(c.tobytes());n+=1
enc.stdin.close();enc.wait();print('frames',n)
open('/tmp/claude-0/w/lez07/cam_all.fatto','w').write(str(n))
