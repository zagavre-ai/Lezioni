# Costruisce la traccia audio nuova: V (vecchio) per i blocchi invariati, prof pulito per i D, R1-R6 per le mappe
import json,sys,subprocess,numpy as np,os
sys.path.insert(0,'.')
import plan
J=json.load(open('states.json'));NEWF=J['NEWF']
FPS=30;SR=48000
def rd(path,ss=None,t=None,af=None):
    c=['ffmpeg','-v','error']
    if ss is not None:c+=['-ss',f'{ss:.4f}']
    if t is not None:c+=['-t',f'{t:.4f}']
    c+=['-i',path]
    if af:c+=['-af',af]
    c+=['-ac','2','-ar',str(SR),'-f','f32le','-']
    return np.frombuffer(subprocess.run(c,capture_output=True).stdout,np.float32).reshape(-1,2)
V='/home/user/w/V.mp4';O='/home/user/w/Letteratura_Lez12.mp4'
CLEAN='aresample=48000,highpass=f=80,arnndn=m=/home/user/w/std.rnnn,loudnorm=I=-16:TP=-1.5:LRA=11,alimiter=limit=0.9'
# pulizia dell'intero originale in un colpo solo (loudnorm coerente fra i pezzi)
if not os.path.exists('/home/user/w/orig_clean.wav'):
    subprocess.run(['ffmpeg','-v','error','-y','-i',O,'-vn','-af',CLEAN,'-ac','2','-ar','48000','/home/user/w/orig_clean.wav'],check=True)
OC=rd('/home/user/w/orig_clean.wav')

SND='/home/user/w/snd/home/claude/v5/snd/'
JT=rd(SND+'titolo.wav');JR=rd(SND+'repaso.wav');JX=rd(SND+'trans.wav')
out=[]
old_start={n:a for n,a,b in plan.blocks};old_end={n:b for n,a,b in plan.blocks}
for n,a,b in plan.blocks:
    N=NEWF[n];ns=round(N/FPS*SR)  # campioni attesi
    if n in plan.DSEG:
        o0,o1=plan.DSEG[n];seg=OC[int((o0+0.015)*SR):int((o1+0.015)*SR)]
        core=round((o1-o0)*FPS)
        # 12 ms di dissolvenza ai bordi
        f=int(0.012*SR);seg=seg.copy();seg[:f]*=np.linspace(0,1,f)[:,None];seg[-f:]*=np.linspace(1,0,f)[:,None]
        # la voce parte con il video: posizione 0 del blocco
        blk=np.zeros((int(N*SR/FPS),2),np.float32);m=min(len(seg),len(blk));blk[:m]=seg[:m]
    elif n in ('AN4','AN9','AN14','AN20','AN26','ANF'):
        rv={'AN4':'R1','AN9':'R2','AN14':'R3','AN20':'R4','AN26':'R5','ANF':'R6'}[n]
        r=rd(f'/home/user/w/voci/scambio/letteratura-V-lez12/vox/{rv}.wav',af='loudnorm=I=-16:TP=-1.5:LRA=11,alimiter=limit=0.9')
        blk=np.zeros((int(N*SR/FPS),2),np.float32);s0=int(0.5*SR);m=min(len(r),len(blk)-s0);blk[s0:s0+m]=r[:m]
    elif n[0]=='S' and n[1:].isdigit():
        L=int(N*SR/FPS);blk=np.zeros((L,2),np.float32)
        v=rd(V,ss=old_start[n],t=(N-100)/FPS);o=int(100/FPS*SR);m=min(len(v),L-o);blk[o:o+m]=v[:m]
        j=JR[:L-int(0.2*SR)];blk[int(0.2*SR):int(0.2*SR)+len(j)]+=j
    else:
        blk=rd(V,ss=old_start[n],t=N/FPS)
        if n[0]=='T' and n[1:].isdigit(): blk=blk.copy();j=JT[:len(blk)-int(0.5*SR)];blk[int(0.5*SR):int(0.5*SR)+len(j)]+=j
        if n in ('VER','CI1'): blk=blk.copy();j=JT[:len(blk)-int(0.2*SR)];blk[int(0.2*SR):int(0.2*SR)+len(j)]+=j
        if n=='COMP': blk=blk.copy();j=JX[:len(blk)-int(0.2*SR)];blk[int(0.2*SR):int(0.2*SR)+len(j)]+=j
        if len(blk)<int(N*SR/FPS): blk=np.vstack([blk,np.zeros((int(N*SR/FPS)-len(blk),2),np.float32)])
    out.append(blk)
A=np.vstack(out)
# transizioni (trans.wav) tra pezzi
STARTS={};c=0
for (n,a,b),blk_ in zip(plan.blocks,out): STARTS[n]=c;c+=len(blk_)
for n in ('D0','AN1','AN5','AN10','AN15','AN21','GL1','RF1','FIN1'):
    p=STARTS[n]-int(0.4*SR);g=0.35 if n in ('D0','AN1','AN5','AN10','AN15','AN21') else 0.6
    A[p:p+len(JX)]+=JX*g
open('/home/user/w/b/audio_starts.json','w').write(json.dumps({k:v/SR for k,v in STARTS.items()}))
tot=round(sum(NEWF.values())/FPS*SR)
A=A[:tot]
import wave
w=wave.open('/home/user/w/audio_nuovo.wav','wb');w.setnchannels(2);w.setsampwidth(2);w.setframerate(SR)
w.writeframes((np.clip(A,-1,1)*32767).astype('<i2').tobytes());w.close()
print('audio',len(A)/SR,'s')
