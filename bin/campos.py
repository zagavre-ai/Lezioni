# posizione del riquadro webcam nel video originale, secondo per secondo -> intervalli costanti
import sys,subprocess,numpy as np,json
src,out=sys.argv[1:3];W,H=1092,614
p=subprocess.run(['ffmpeg','-v','error','-i',src,'-vf','fps=1,format=gray','-f','rawvideo','-'],capture_output=True)
a=np.frombuffer(p.stdout,np.uint8).reshape(-1,H,W)
pos=[]
for f in a:
    best=None
    # il riquadro: zona scura-varia (non bianca) di circa 245x137 nella metà destra
    m=(f<225).astype(np.int32);ii=m.cumsum(0).cumsum(1)
    def s(x,y):return ii[y+133,x+243]-ii[y+133,x]-ii[y,x+243]+ii[y,x]
    for y in range(300,477,2):
        for x in range(560,849,2):
            v=s(x,y)
            if best is None or v>best[0]:best=(v,x,y)
    v,x,y=best
    # rifinitura a passo 1
    for yy in range(max(0,y-2),min(477,y+3)):
        for xx in range(max(0,x-2),min(849,x+3)):
            vv=s(xx,yy)
            if vv>v:v,x,y=vv,xx,yy
    pos.append((x+1,y+1,round(v/(243*133),2)))
I=[];
for t,(x,y,c) in enumerate(pos):
    if I and abs(I[-1][2]-x)<=3 and abs(I[-1][3]-y)<=3:I[-1][1]=t+1
    else:I.append([t,t+1,x,y])
json.dump(I,open(out,'w'));print(I)
