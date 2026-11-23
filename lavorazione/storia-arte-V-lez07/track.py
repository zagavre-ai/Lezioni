import cv2,subprocess,numpy as np,json
W,H=1092,614
ref=cv2.imread('/tmp/claude-0/w/lez07/f_600.png')[343:482,825:1071]
p=subprocess.Popen(['ffmpeg','-v','error','-i','/tmp/claude-0/w/lez07/LEZIONE 7 LE AVANGUARDIE.mp4','-vf','fps=6','-f','rawvideo','-pix_fmt','bgr24','-'],stdout=subprocess.PIPE)
res=[];i=0
while True:
    b=p.stdout.read(W*H*3)
    if len(b)<W*H*3:break
    im=np.frombuffer(b,np.uint8).reshape(H,W,3)
    r=cv2.matchTemplate(im,ref,cv2.TM_CCOEFF_NORMED);_,mx,_,loc=cv2.minMaxLoc(r)
    res.append((round(i/6,3),round(float(mx),3),loc[0],loc[1]));i+=1
json.dump(res,open('/tmp/claude-0/w/lez07/camtrack6.json','w'))
open('/tmp/claude-0/w/lez07/camtrack6.fatto','w').write('ok')
