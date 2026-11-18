# Sostituisce il prof nel tondo con il prof nel rettangolo 394x218, preso dal video originale e allineato sull'audio.
# Uso: python3 rettangolo.py <finale.mp4> <originale.mp4> <timeline.json> <uscita.mp4>
import json,subprocess,sys,os,numpy as np
sys.path.insert(0,os.path.dirname(__file__));from trova_cam import trova,scatola
from geometria import tondo
FIN,SRC,TLF,OUT=[os.path.abspath(x) for x in sys.argv[1:5]];MATERIA=sys.argv[5] if len(sys.argv)>5 else 'LETTERATURA ITALIANA';W=os.path.dirname(OUT)+'/'
def sh(*a):return subprocess.run(a,capture_output=True,text=True)
# 0. dove sta il tondo in questa lezione
G=tuple(float(x) for x in os.environ['GEO'].split(','))+(99,99) if os.environ.get('GEO') else tondo(FIN)  # 16/11: posizione del tondo a mano se Hough sbaglia
if not G or G[3]<4:print('TONDO NON TROVATO',G);sys.exit(3)
CX,CY,RAD=int(round(G[0])),int(round(G[1])),int(round(G[2]))
SIDE=2*(RAD+27);f=60/SIDE;BX,BY=CX-SIDE//2,CY-SIDE//2
RX=min(CX-197,1915-394);RY=CY-109
print('tondo',CX,CY,RAD,flush=True)
# 1. dove c'è il tondo (10 fotogrammi al secondo)
sh('ffmpeg','-v','error','-y','-i',FIN,'-vf',f'fps=10,crop={SIDE}:{SIDE}:{BX}:{BY},scale=60:60:flags=area,format=gray','-f','rawvideo',W+'ring.raw')
a=np.fromfile(W+'ring.raw',np.uint8).reshape(-1,60,60).astype(float)
yy,xx=np.mgrid[0:60,0:60];r=np.hypot(xx-29.5,yy-29.5)
ins=r<(RAD-23)*f;pres=(a[:,(r>(RAD+3)*f)&(r<(RAD+11)*f)].mean(1)>234)&(a[:,ins].std(1)>8)
try:
    _TL=[(n_,s_,s_+d_) for n_,s_,d_ in json.load(open(TLF)) if n_=='INTRO' or (n_.startswith('D') and n_[1:].isdigit())]
except Exception:_TL=[]
if _TL:
    _m=np.zeros(len(pres),bool)
    for _n,_s,_e in _TL:_m[int(_s*10):int(_e*10)+1]=True
    pres=pres&_m
# intervalli (buchi < 0,5 s chiusi, pezzi < 0,3 s scartati), allargati di 0,15 s per coprire le dissolvenze
iv=[];i=0;n=len(pres)
while i<n:
    if pres[i]:
        j=i
        while j<n and pres[j]:j+=1
        iv.append([i/10,j/10]);i=j
    else:i+=1
m=[]
for s,e in iv:
    if m and s-m[-1][1]<0.5:m[-1][1]=e
    else:m.append([s,e])
iv=[[max(0,s-0.15),e+0.15] for s,e in m if e-s>=0.3]
# timeline: se manca o non ha i pezzi del docente, si usano gli intervalli del tondo
tl_ok=os.path.exists(TLF)
if tl_ok:
    try:tl_ok=any(n=='INTRO' or (n.startswith('D') and n[1:].isdigit()) for n,_,_ in json.load(open(TLF)))
    except Exception:tl_ok=False
if not tl_ok:
    seg=[];
    for s_,e_ in iv:
        if seg and s_-seg[-1][1]<20:seg[-1][1]=e_
        else:seg.append([s_,e_])
    TLF=W+'tl_auto.json';json.dump([['D'+str(i+1),a_,b_-a_] for i,(a_,b_) in enumerate(seg)],open(TLF,'w'))
# colore dello sfondo vicino al tondo
from trova_cam import frame as _fr
_F=_fr(FIN,(iv[len(iv)//2][0]+iv[len(iv)//2][1])/2);_b,_g,_r=[int(v) for v in _F[CY,max(0,CX-RAD-26)]]
BG='0x%02X%02X%02X'%(_r,_g,_b);print('sfondo',BG,flush=True)
# 2. allineamento audio
sh('ffmpeg','-v','error','-y','-i',FIN,'-ac','1','-ar','8000','-f','s16le',W+'fin.raw');sh('ffmpeg','-v','error','-y','-i',SRC,'-ac','1','-ar','8000','-f','s16le',W+'src.raw')
sh('python3',os.path.dirname(__file__)+'/allinea.py',W+'fin.raw',W+'src.raw',TLF,W+'al.json')
R=[(t,o) for t,o,s in json.load(open(W+'al.json'))['res'] if o is not None]
TL=json.load(open(TLF));segs=[(nm,s,s+d) for nm,s,d in TL]
def off(t):
    near=sorted(R,key=lambda x:abs(x[0]+1-t))[:7];return float(np.median([o for _,o in near])) if near else None
# 3. pezzi: ogni intervallo spezzato dove cambia l'offset
pezzi=[]
for s,e in iv:
    t=s;cur=None;st=s
    ts=np.arange(s,e,0.5).tolist()+[e]
    for t in ts:
        o=off(t)
        if cur is None:cur=o
        elif o is not None and abs(o-cur)>0.04:
            pezzi.append([st,t,cur]);st=t;cur=o
    pezzi.append([st,e,cur])
pezzi=[p for p in pezzi if p[2] is not None and p[1]-p[0]>0.05]
# 4. posizione della webcam nell'originale (una ricerca per offset diverso)
cam={}
for p in pezzi:
    k=round(p[2],2)
    if k in cam:continue
    tm=(p[0]+p[1])/2;b=trova(FIN,SRC,tm,p[2],CX,CY,RAD-5)
    if b[0]<0.8:
        for tt in (p[0]+0.3*(p[1]-p[0]),p[0]+0.7*(p[1]-p[0])):
            b2=trova(FIN,SRC,tt,p[2],CX,CY,RAD-5);b=b2 if b2[0]>b[0] else b
    cam[k]=b
for p in pezzi:p.append(cam[round(p[2],2)])
box={}
for p in pezzi:
    k=round(p[2],2)
    if k not in box:
        tm=(p[0]+p[1])/2;x0,x1,y0,y1=scatola(SRC,tm+p[2],p[3][2],p[3][3])
        box[k]=(x0+2,y0+2,x1-x0-3,y1-y0-3)
    p.append(box[k])
bad=[p for p in pezzi if p[3][0]<0.8 or p[4][2]<150 or p[4][3]<80]
if bad and os.environ.get('TOLLERA'):  # 16/11: i pezzi senza webcam nell'originale restano col tondo (non si copre niente lì)
    def togli(iv0,a0,b0):
        out=[]
        for x,y in iv0:
            if y<=a0 or x>=b0: out.append((x,y));continue
            if x<a0: out.append((x,a0))
            if y>b0: out.append((b0,y))
        return out
    for q in bad: iv=togli(iv,q[0]-0.2,q[1]+0.2)
    pezzi=[q for q in pezzi if q not in bad]
    print('TOLLERATI (restano col tondo)',[(round(q[0],1),round(q[1],1)) for q in bad],flush=True);bad=[]
json.dump({'geo':[CX,CY,RAD,RX,RY],'iv':iv,'pezzi':[[a_,b_,o,list(map(float,c)),list(bx)] for a_,b_,o,c,bx in pezzi]},open(W+'pezzi.json','w'),indent=1)
if bad:print('ATTENZIONE webcam non trovata',bad);sys.exit(2)
from PIL import Image,ImageDraw,ImageFont,ImageFilter
_m=Image.new('L',(394,218),0);ImageDraw.Draw(_m).rounded_rectangle([0,0,393,217],radius=14,fill=255);_m.save(W+'maschera.png')
# 5. traccia del rettangolo allineata alla lezione (pezzi dall'originale + spazi vuoti), poi una sola sovrapposizione
FPS=30;NF=int(sh('ffprobe','-v','error','-count_packets','-select_streams','v:0','-show_entries','stream=nb_read_packets','-of','csv=p=0',FIN).stdout.strip())
lst=open(W+'traccia.txt','w');pos=0;k=0
def vuoto(nf):
    global k;o=W+f'p{k:03d}.mp4';k+=1
    sh('ffmpeg','-v','error','-y','-f','lavfi','-i','color=c=black:s=394x218:r=30','-frames:v',str(nf),'-c:v','libx264','-preset','veryfast','-crf','16','-pix_fmt','yuv420p',o);lst.write(f"file '{o}'\n")
for a_,b_,o,c,bx in pezzi:
    f0=int(round(a_*FPS));f1=int(round(b_*FPS))
    if f0>pos:vuoto(f0-pos)
    f0=max(f0,pos);nf=f1-f0
    if nf<=0:continue
    x,y,bw,bh=bx;out=W+f'p{k:03d}.mp4';k+=1
    sh('ffmpeg','-v','error','-y','-ss',f'{f0/FPS+o:.3f}','-i',SRC,'-frames:v',str(nf),'-vf',f'fps=30,crop={bw}:{bh}:{x}:{y},scale=394:218:flags=lanczos,unsharp=5:5:0.6,eq=contrast=1.04:saturation=1.08','-an','-c:v','libx264','-preset','veryfast','-crf','16','-pix_fmt','yuv420p',out)
    got=int(sh('ffprobe','-v','error','-count_packets','-select_streams','v:0','-show_entries','stream=nb_read_packets','-of','csv=p=0',out).stdout.strip() or 0)
    if got<nf:sh('ffmpeg','-v','error','-y','-i',out,'-vf',f'tpad=stop_mode=clone:stop={nf-got}','-c:v','libx264','-preset','veryfast','-crf','16',out+'.mp4');os.replace(out+'.mp4',out)
    lst.write(f"file '{out}'\n");pos=f1
if pos<NF:vuoto(NF-pos)
lst.close()
en='+'.join(f'between(t,{int(round(a_*FPS))/FPS:.4f},{(int(round(b_*FPS))-0.5)/FPS:.4f})' for a_,b_,o,c,bx in pezzi)
env='+'.join(f'between(t,{a_:.3f},{b_:.3f})' for a_,b_ in iv)
fc=(f"[0:v]drawbox=x={BX}:y={BY}:w={SIDE}:h={SIDE}:color={BG}@1:t=fill:enable='{env}'"+f"[b];[1:v]setpts=PTS-STARTPTS,format=yuva420p[cv];[2:v]format=gray[m];[cv][m]alphamerge[c];"
    f"[b][c]overlay={RX}:{RY}:eof_action=pass:enable='{en}'[v]")
r=subprocess.run(['ffmpeg','-v','error','-y','-i',FIN,'-f','concat','-safe','0','-i',W+'traccia.txt','-loop','1','-i',W+'maschera.png','-filter_complex',fc,'-map','[v]','-map','0:a','-c:v','libx264','-preset','superfast','-crf','18','-pix_fmt','yuv420p','-fps_mode','passthrough','-c:a','copy','-movflags','+faststart',OUT],capture_output=True,text=True)
if r.returncode:print(r.stderr[-1500:]);sys.exit(1)
def nf(p):return sh('ffprobe','-v','error','-count_packets','-select_streams','v:0','-show_entries','stream=nb_read_packets','-of','csv=p=0',p).stdout.strip()
def du(p):return sh('ffprobe','-v','error','-show_entries','format=duration','-of','csv=p=0',p).stdout.strip()
print('pezzi',len(pezzi),'fotogrammi',nf(FIN),nf(OUT),'durata',du(FIN),du(OUT),flush=True)
