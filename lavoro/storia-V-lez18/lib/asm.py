import os,sys,json,subprocess,hashlib,numpy as np
W='/home/user/work18';CL=W+'/clips';os.makedirs(CL,exist_ok=True)
SRC=W+'/src/LEZIONE 18 L_ITALIA REPUBBLICANA.mp4'
FPS=30;SR=48000
CRF=os.environ.get('CRF','19')
ENC=['-c:v','libx264','-preset','veryfast','-crf',CRF,'-pix_fmt','yuv420p','-r','30','-g','60','-bf','2','-an','-video_track_timescale','15360']
def run(cmd):
    r=subprocess.run(cmd,capture_output=True,text=True)
    if r.returncode:print(' '.join(map(str,cmd))[:600]);print(r.stderr[-1500:]);raise SystemExit(1)
    return r
def fr(s):return int(round(s*FPS))
def h8(*a):return hashlib.md5('|'.join(map(str,a)).encode()).hexdigest()[:12]
def fh(p):
    return hashlib.md5(open(p,'rb').read()).hexdigest()[:10]
CAMF=("crop=184:138:874:343,scale=412:309:flags=lanczos,eq=contrast=1.04:saturation=1.03,hqdn3d=1.5:1.5:3:3,cas=0.35,format=rgba")
def render_scene(states,cam=None,prev=None,xin=12,xs=8,name='s',camfade=True):
    """states=[(png,frames)], cam=t0 sorgente (s) o None, prev=png per la dissolvenza iniziale. Ritorna (mp4, ultimo_png, nframes)"""
    n=sum(f for _,f in states)
    ka=[name,[((os.path.dirname(p)+fh(p.split('@')[0]%1)) if '%' in p else fh(p),f) for p,f in states],cam,camfade,fh(prev) if prev else None,xin,xs]
    dark=any('%' in p for p,_ in states);crf=str(int(CRF)+3) if dark else CRF
    if crf!='19':ka.insert(1,crf)
    key=h8(*ka)
    out=f'{CL}/{key}.mp4';last=f'{CL}/{key}.png'
    if os.path.exists(out) and os.path.exists(last):return out,last,n
    seq=[]
    if prev:seq.append((prev,0,xin))
    for i,(p,f) in enumerate(states):
        x=xs if i<len(states)-1 else 0
        seq.append((p,f,min(x,max(1,f-1)) if x else 0))
    inp=[];flt=[]
    for i,(p,f,x) in enumerate(seq):
        c=f+x if not(prev and i==0) else x
        if i==len(seq)-1:c=f
        if '%' in p:
            pp,fps_=p.split('@');inp+=['-framerate',fps_,'-start_number','1','-t',f'{c/FPS:.5f}','-i',pp]
        else:inp+=['-loop','1','-framerate','30','-t',f'{c/FPS:.5f}','-i',p]
        flt.append(f'[{i}:v]fps=30,format=yuv420p,setsar=1,settb=AVTB[v{i}]')
    cur='v0';La=(seq[0][1]+seq[0][2]) if len(seq)>0 else 0
    if len(seq)==1:cur='v0'
    F=0
    for i in range(1,len(seq)):
        pf,px=seq[i-1][1],seq[i-1][2]
        off=F+pf if not(prev and i==1) else 0
        # offset = frame di inizio della transizione = F (somma f precedenti)
        F=F+pf
        flt.append(f'[{cur}][v{i}]xfade=transition=fade:duration={px/FPS:.5f}:offset={F/FPS:.5f}[x{i}]');cur=f'x{i}'
    if cam is not None:
        k=len(seq)
        inp+=['-ss',f'{cam:.5f}','-t',f'{n/FPS+0.2:.5f}','-i',SRC,'-loop','1','-framerate','30','-t',f'{n/FPS+0.2:.5f}','-i',W+'/st/mask.png']
        FADE='fade=t=in:st=0:d=0.3:alpha=1' if camfade else 'null'
        flt.append(f'[{k}:v]{CAMF},{FADE}[c];[{k+1}:v]format=gray[m];[c][m]alphamerge[cm];[{cur}]format=rgba[b];[b][cm]overlay=1428:148:shortest=1,format=yuv420p[o]')
        cur='o'
    run(['ffmpeg','-y','-loglevel','error']+inp+['-filter_complex',';'.join(flt),'-map',f'[{cur}]','-frames:v',str(n)]+[x if x!=CRF or ENC[ENC.index(x)-1]!='-crf' else crf for x in ENC]+[out+'.t.mp4']);os.rename(out+'.t.mp4',out)
    run(['ffmpeg','-y','-loglevel','error','-sseof','-0.1','-i',out,'-update','1','-frames:v','1',last])
    return out,last,n
