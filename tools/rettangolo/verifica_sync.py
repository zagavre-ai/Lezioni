import cv2,numpy as np,subprocess,sys,json,random
from trova_cam import frame
ORIG,NEW,PJ=sys.argv[1:4];J=json.load(open(PJ));P=J['pezzi'];CX,CY,R,RX,RY=J['geo'];random.seed(1)
ris=[]
for a,b,o,c,*_ in P:
    for _ in range(4):
        t=random.uniform(a+1,b-1);F=frame(ORIG,t);N=frame(NEW,t)
        h=int(R*0.65);circ=F[CY-h:CY+h,CX-h:CX+h]  # centro del tondo
        rect=N[RY:RY+218,RX:RX+394]
        best=-1
        for k in np.arange(0.8,1.61,0.05):
            tm=cv2.resize(circ,(int(2*h/k/ (R/123)),int(2*h/k/(R/123))))
            m=cv2.matchTemplate(rect,tm,cv2.TM_CCOEFF_NORMED);best=max(best,m.max())
        ris.append(round(float(best),3))
print('somiglianza tondo/rettangolo:',ris,'minimo',min(ris))
