import cv2, sys, subprocess, numpy as np
# misura il tondino della webcam su alcuni fotogrammi: cerca il cerchio nell'angolo in basso a destra
def misura(mp4, tempi=(120,900,1800,2700,3500)):
    ris=[]
    for t in tempi:
        subprocess.run(['ffmpeg','-v','error','-y','-ss',str(t),'-i',mp4,'-frames:v','1','/tmp/_c.png'])
        im=cv2.imread('/tmp/_c.png'); g=cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
        H,W=g.shape; x0,y0=int(W*0.82),int(H*0.78)
        sub=cv2.GaussianBlur(g[y0:,x0:],(5,5),0)
        c=cv2.HoughCircles(sub,cv2.HOUGH_GRADIENT,dp=1,minDist=30,param1=80,param2=18,minRadius=26,maxRadius=36)
        if c is not None:
            x,y,r=c[0][0]; ris.append((x+x0,y+y0,r))
    return ris
if __name__=='__main__':
    r=misura(sys.argv[1]); print(r)
    if r: a=np.array(r); print('mediana',np.median(a,axis=0))
