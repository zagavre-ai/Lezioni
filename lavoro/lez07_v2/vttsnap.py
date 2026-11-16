# Sposta l'inizio di ogni blocco del .vtt sull'attacco della voce nel video finale (stesso criterio di controllo_finale.py).
# uso: vttsnap.py VIDEO.mp4 file.vtt
import sys,re,subprocess,numpy as np
V,F=sys.argv[1:3];SR=8000   # come controllo_finale.py
x=np.frombuffer(subprocess.run(['ffmpeg','-v','error','-i',V,'-ac','1','-ar',str(SR),'-f','s16le','-'],capture_output=True).stdout,np.int16).astype(float)
e=np.convolve(x**2,np.ones(400)/400,'same');thr=np.percentile(e,60)
def ts(s):h,m,y=s.split(':');return int(h)*3600+int(m)*60+float(y)
def fm(t):return '%02d:%02d:%06.3f'%(t//3600,t%3600//60,t%60)
txt=open(F).read();pat=re.compile(r'(\d+:\d\d:[\d.]+) --> (\d+:\d\d:[\d.]+)')
C=[[ts(a),ts(b)] for a,b in pat.findall(txt)];n=0
for k,(c0,c1) in enumerate(C):
    i0=int(max(0,c0-0.8)*SR);seg=e[i0:int((c0+0.8)*SR)]
    if not len(seg) or seg[:int(0.5*SR)].mean()>=thr*0.5: continue   # blocco che non parte dopo una pausa
    if not (seg>thr).any(): continue
    on=i0/SR+np.argmax(seg>thr)/SR-0.05
    if k and on<C[k-1][1]+0.02:   # il blocco prima finisce dopo l'attacco: si accorcia (se resta almeno 0,3 s)
        if on-0.02-C[k-1][0]>=0.3: C[k-1][1]=on-0.02
        else: on=C[k-1][1]+0.02
    if abs(on-c0)>0.05 and on<c1-0.4: C[k][0]=on;n+=1
it=iter(C)
txt=pat.sub(lambda m:(lambda c:f'{fm(c[0])} --> {fm(c[1])}')(next(it)),txt)
open(F,'w').write(txt);print('blocchi spostati sull\'attacco della voce:',n,'su',len(C))
