# Ritaglio 4:3 della webcam del prof dall'originale, per ogni fotogramma, ingrandito con qualita' (Lanczos + nitidezza leggera)
import cv2,numpy as np,json,subprocess,sys
SRC='/tmp/w/mat/LEZIONE 14 I NUOVI REALISMI.mp4'
tl=json.load(open('/tmp/w/lav/cam.json'))
# posizione per secondo, regolarizzata (mediana su 5 s) e arrotondata sulle posizioni note
pos=[(a[2],a[3]) for a in tl]
from collections import Counter
def snap(p):
    cands=[(821,330),(818,332),(825,338),(350,476),(666,476)]
    return min(cands,key=lambda c:abs(c[0]-p[0])+abs(c[1]-p[1]))
P=[snap(p) for p in pos]
# mediana mobile
S=[]
for i in range(len(P)):
    w=P[max(0,i-2):i+3];S.append(Counter(w).most_common(1)[0][0])
json.dump(S,open('/tmp/w/lav/campos.json','w'))
W,H=245,137   # dimensione della webcam nell'originale (misurata)
OW,OH=412,310
cw=int(round(H*4/3))  # 183 px di larghezza per il 4:3
cap=cv2.VideoCapture(SRC)
ff=subprocess.Popen(['ffmpeg','-v','error','-y','-f','rawvideo','-pix_fmt','bgr24','-s',f'{OW}x{OH}','-r','30','-i','-',
  '-c:v','libx264','-preset','veryfast','-crf','10','-pix_fmt','yuv420p','/tmp/w/build/cam.mp4'],stdin=subprocess.PIPE)
n=0
kern=np.array([[0,-1,0],[-1,5,-1],[0,-1,0]],np.float32)
while True:
    ok,f=cap.read()
    if not ok:break
    sec=min(n//30,len(S)-1);x,y=S[sec]
    cam=f[y:y+H,x:x+W]
    x0=(W-cw)//2+4   # leggermente a destra del centro (il viso e' al centro)
    c=cam[:,x0:x0+cw]
    c=cv2.resize(c,(OW,OH),interpolation=cv2.INTER_LANCZOS4)
    c=cv2.fastNlMeansDenoisingColored(c,None,2,2,5,15) if n%1==0 and False else c
    bl=cv2.GaussianBlur(c,(0,0),1.2);c=cv2.addWeighted(c,1.35,bl,-0.35,0)   # unsharp leggero
    ff.stdin.write(c.tobytes());n+=1
ff.stdin.close();ff.wait();print('fotogrammi',n)
