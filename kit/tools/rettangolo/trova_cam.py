import cv2,numpy as np,subprocess,sys
def frame(path,t):
    p=subprocess.run(['ffmpeg','-v','error','-ss',f'{t:.3f}','-i',path,'-frames:v','1','-f','image2pipe','-vcodec','png','-'],capture_output=True).stdout
    return cv2.imdecode(np.frombuffer(p,np.uint8),cv2.IMREAD_COLOR)
def trova(fin,src,tf,off,CX=1690,CY=230,R=118):
    F=frame(fin,tf);S=frame(src,tf+off)
    s=int(R*1.41/2);T=F[CY-s:CY+s,CX-s:CX+s]
    best=(-1,)
    for k in np.arange(1.2,3.21,0.05):
        t=cv2.resize(T,(int(T.shape[1]/k),int(T.shape[0]/k)),interpolation=cv2.INTER_AREA)
        if t.shape[0]>=S.shape[0]: continue
        m=cv2.matchTemplate(S,t,cv2.TM_CCOEFF_NORMED);_,v,_,l=cv2.minMaxLoc(m)
        if v>best[0]: best=(v,k,l[0]+t.shape[1]/2,l[1]+t.shape[0]/2)
    return best
if __name__=='__main__':
    print(trova(sys.argv[1],sys.argv[2],float(sys.argv[3]),float(sys.argv[4])))

def scatola(src,ts,cx,cy):
    """bordi esatti della webcam nell'originale, attorno al centro trovato"""
    S=frame(src,ts).astype(int);nw=(S.min(axis=2)<232);H,W=nw.shape;cx,cy=int(cx),int(cy)
    def ext(axis,sign):
        k=0
        while True:
            if axis=='x':
                x=cx+sign*k
                if not(0<=x<W) or nw[max(0,cy-50):cy+50,x].mean()<0.6: return x-sign
            else:
                y=cy+sign*k
                if not(0<=y<H) or nw[y,max(0,cx-90):cx+90].mean()<0.6: return y-sign
            k+=1
    return ext('x',-1),ext('x',1),ext('y',-1),ext('y',1)
