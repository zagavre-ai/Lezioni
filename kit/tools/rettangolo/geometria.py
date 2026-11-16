import cv2,numpy as np,subprocess,sys,collections
from trova_cam import frame
def durata(p):return float(subprocess.run(['ffprobe','-v','error','-show_entries','format=duration','-of','csv=p=0',p],capture_output=True,text=True).stdout)
def tondo(fin,n=24):
    d=durata(fin);C=[]
    for t in np.linspace(60,d-60,n):
        F=frame(fin,t);g=cv2.medianBlur(cv2.cvtColor(F,cv2.COLOR_BGR2GRAY),5)
        cs=cv2.HoughCircles(g[:,1100:],cv2.HOUGH_GRADIENT,dp=1.2,minDist=200,param1=120,param2=60,minRadius=70,maxRadius=190)
        if cs is not None:
            for x,y,r in cs[0][:2]:C.append((int(round((x+1100)/4))*4,int(round(y/4))*4,int(round(r/3))*3))
    if not C:return None
    (cx,cy,r),k=collections.Counter(C).most_common(1)[0]
    sel=[c for c in C if abs(c[0]-cx)<=8 and abs(c[1]-cy)<=8]
    return (float(np.median([c[0] for c in sel])),float(np.median([c[1] for c in sel])),float(np.median([c[2] for c in sel])),len(sel),len(C))
if __name__=='__main__':print(tondo(sys.argv[1]))
