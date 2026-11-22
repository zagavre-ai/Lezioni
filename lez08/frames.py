# generazione dei fotogrammi di sfondo (slide + opere con zoom lento) e montaggio con la webcam del prof
import numpy as np, cv2, subprocess, os, json
FPS=30
def load(p):
    im=cv2.imread(p,cv2.IMREAD_COLOR); return cv2.cvtColor(im,cv2.COLOR_BGR2RGB)
class Static:
    def __init__(s,png): s.img=load(png)
    def frame(s,t): return s.img
class Art:
    """sfondo con cornice; l'opera sta intera all'inizio e si avvicina piano (zoom lento verso un punto)"""
    def __init__(s,bg,art,box,dur,zmax=0.22,focus=(0.5,0.5),start=(0.5,0.5)):
        s.bg=load(bg); s.dur=max(dur,1.0); s.zmax=zmax; s.focus=focus; s.start=start
        a=load(art); s.a=a; h,w=a.shape[:2]; bx,by,bw,bh=box
        f=min(bw/w,bh/h); s.w=int(w*f)//2*2; s.h=int(h*f)//2*2
        s.x=bx+(bw-s.w)//2; s.y=by+(bh-s.h)//2
        # ombra morbida grigia dietro l'opera
        sh=np.zeros(s.bg.shape[:2],np.float32); cv2.rectangle(sh,(s.x+6,s.y+14),(s.x+s.w+6,s.y+s.h+14),1.0,-1); sh=cv2.GaussianBlur(sh,(0,0),16)
        s.bg=(s.bg*(1-0.22*sh[...,None])+np.array([120,128,145],np.float32)*0.22*sh[...,None]).astype(np.uint8)
        s.bg[s.y-2:s.y+s.h+2,s.x-2:s.x+s.w+2]=(227,232,240)
    def frame(s,t):
        p=min(max(t/s.dur,0),1); p=p*p*(3-2*p)
        z=1+s.zmax*p; h,w=s.a.shape[:2]
        cw,ch=w/z,h/z
        cx=(s.start[0]+(s.focus[0]-s.start[0])*p)*w; cy=(s.start[1]+(s.focus[1]-s.start[1])*p)*h
        x0=min(max(cx-cw/2,0),w-cw); y0=min(max(cy-ch/2,0),h-ch)
        M=np.float32([[s.w/cw,0,-x0*s.w/cw],[0,s.h/ch,-y0*s.h/ch]])
        v=cv2.warpAffine(s.a,M,(s.w,s.h),flags=cv2.INTER_AREA if z*s.w/w<1 else cv2.INTER_LINEAR)
        f=s.bg.copy(); f[s.y:s.y+s.h,s.x:s.x+s.w]=v; return f
def render_timeline(tl,total,pipe,fade_frames=8):
    """tl = [(t_start,stato)] ordinata; scrive total*FPS fotogrammi RGB sulla pipe; dissolvenza tra stati"""
    n=int(round(total*FPS)); cur=0; last_raw=None; blend_from=None; left=0
    for k in range(n):
        t=k/FPS
        while cur+1<len(tl) and t>=tl[cur+1][0]-1e-6:
            cur+=1; blend_from=last_raw; left=fade_frames if blend_from is not None else 0
        raw=tl[cur][1].frame(t-tl[cur][0])
        if left>0:
            a=(fade_frames-left+1)/(fade_frames+1); out=cv2.addWeighted(blend_from,1-a,raw,a,0); left-=1
        else: out=raw
        last_raw=raw
        pipe.write(np.ascontiguousarray(out).tobytes())
