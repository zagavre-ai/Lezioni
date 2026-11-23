import sys,os,json,subprocess,numpy as np;sys.path.insert(0,'/tmp/w/build')
import cv2
from multiprocessing import Pool
import plan
from engine import *
tl=plan.build()
segs=tl.segs;N=len(segs);XF=9
os.makedirs(f'{B}/clips',exist_ok=True)
def nv(i):
    s=segs[i];return s['n']-(XF if (s['xf'] and i<N-1) else 0)
import hashlib
def ck(i):return hashlib.md5((json.dumps(segs[i]['spec'],sort_keys=True)+str(nv(i))).encode()).hexdigest()[:20]
def cp(i):return f'{B}/clips/{ck(i)}.mp4'
def migrate():
    for i in range(N):
        o=f'{B}/clips/{i:04d}.mp4'
        if os.path.exists(o) and not os.path.exists(cp(i)):os.rename(o,cp(i))
def job(i):
    render_clip(segs[i]['spec'],nv(i),cp(i));return i
def frame(path,idx):
    cap=cv2.VideoCapture(path);cap.set(cv2.CAP_PROP_POS_FRAMES,idx);ok,f=cap.read();cap.release();assert ok,(path,idx);return f
def tclip(i):
    out=f'{B}/clips/T{ck(i)}_{ck(i+1)}.mp4'
    if os.path.exists(out) and os.path.getsize(out)>500:return
    a=frame(cp(i),nv(i)-1).astype(np.float32);b=frame(cp(i+1),0).astype(np.float32)
    ff=subprocess.Popen(['ffmpeg','-v','error','-y','-f','rawvideo','-pix_fmt','bgr24','-s','1920x1080','-r','30','-i','-','-c:v','libx264','-preset','veryfast','-crf','14','-pix_fmt','yuv420p','-r','30','-g','30',out],stdin=subprocess.PIPE)
    for k in range(1,XF+1):
        x=k/(XF+1);x=x*x*(3-2*x)
        ff.stdin.write(((1-x)*a+x*b).astype(np.uint8).tobytes())
    ff.stdin.close();ff.wait()
if __name__=='__main__':
    migrate()
    with Pool(3) as p:
        for i in p.imap_unordered(job,range(N)):pass
    print('clip fatti',N,flush=True)
    for i in range(N-1):
        if segs[i]['xf']:tclip(i)
    L=[]
    for i in range(N):
        L.append(f"file '{cp(i)}'")
        if segs[i]['xf'] and i<N-1:L.append(f"file '{B}/clips/T{ck(i)}_{ck(i+1)}.mp4'")
    open(f'{B}/lista.txt','w').write('\n'.join(L))
    # audio
    tot=sum(s['n'] for s in segs);canvas=np.zeros((tot*SPF,2),'float32');off=0;TLJ=[]
    for i,s in enumerate(segs):
        canvas[off*SPF:(off+s['n'])*SPF]+=s['a']
        if s['xf'] and i<N-1:place(canvas,JING['trans'],(off+s['n'])/FPS-0.45,0.55)
        TLJ.append([s['name'],round(off/FPS,2),round(s['n']/FPS,2)]);off+=s['n']
    # volume: -16 LUFS sul parlato (misura di insieme)
    import pyloudnorm as pyln
    m=pyln.Meter(SR);l=m.integrated_loudness(canvas);g=10**((-16.0-l)/20);canvas*=g
    print('LUFS prima',round(l,2),'gain',round(g,3),'picco',float(np.abs(canvas).max()))
    sf.write(f'{B}/audio.wav',canvas,SR,subtype='FLOAT')
    json.dump(TLJ,open(f'{B}/timeline_Parte1.json','w'),ensure_ascii=False)
    print('totale',tot/FPS/60,'min',flush=True)
