# Pause della docente: quelle oltre 1,0 s diventano 0,6 s (0,3 s tenuti a ogni capo), dissolvenza breve sui tagli.
# uso: python3 condensa.py          (dalla cartella della lezione)
# entra: audio/audio_raw.wav (48 kHz mono, tutta la registrazione), cam_full.mp4 (riquadro docente), pk_orig.jsonl (parole)
# esce:  audio/audio_B_full.wav (pulito e condensato), orig/lez1.mp4 (riquadro condensato), pk.jsonl (tempi condensati),
#        keep.json (intervalli tenuti), condensa.txt (risparmio)
import json,subprocess,os,sys,numpy as np,soundfile as sf
D=os.path.dirname(os.path.abspath(__file__))+'/';FPS=30
SIL=float(os.environ.get('SIL','1.0'));KEEP=0.3;FADE=0.1
def sh(c):subprocess.run(c,check=True)
# 1. audio pulito sulla registrazione intera (versione B)
B0=D+'audio/audio_B_orig.wav'
if not os.path.exists(B0):
    sh(['ffmpeg','-v','error','-y','-i',D+'audio/audio_raw.wav','-af','highpass=f=80,arnndn=m=/home/claude/kit/02_Video/sh.rnnn,loudnorm=I=-16:TP=-1.5:LRA=11','-ar','48000','-ac','1',B0])
y,sr=sf.read(B0,dtype='float32');T=len(y)/sr
# 2. silenzi: energia in finestre da 20 ms, soglia sotto il parlato
hop=int(0.02*sr);n=len(y)//hop;e=np.sqrt(np.mean(y[:n*hop].reshape(n,hop)**2,axis=1)+1e-12);db=20*np.log10(e)
thr=max(np.percentile(db,10)+8,np.percentile(db,60)-22)
quiet=db<thr
W=[w for l in open(D+'pk_orig.jsonl') for w in json.loads(l)['w']];WT=np.array([t for t,_ in W])
cuts=[];i=0
while i<n:
    if quiet[i]:
        j=i
        while j<n and quiet[j]:j+=1
        a,b=i*0.02,j*0.02
        if b-a>SIL:
            ca,cb=a+KEEP,b-KEEP
            ca=round(ca*FPS)/FPS;cb=round(cb*FPS)/FPS
            if cb-ca>0.2 and not np.any((WT>ca-0.05)&(WT<cb+0.05)):cuts.append((ca,cb))
        i=j
    else:i+=1
keep=[];s=0.0
for a,b in cuts:keep.append((s,a));s=b
keep.append((s,round(T*FPS)/FPS));keep=[(a,b) for a,b in keep if b-a>1/FPS]
json.dump(keep,open(D+'keep.json','w'))
tot=sum(b-a for a,b in keep)
open(D+'condensa.txt','w').write(f'soglia {thr:.1f} dB · tagli {len(cuts)} · originale {T/60:.2f} min · condensato {tot/60:.2f} min · risparmio {(T-tot)/60:.2f} min\n')
print(open(D+'condensa.txt').read())
# 3. audio condensato con dissolvenza breve (0,1 s in uscita + 0,1 s in entrata) a ogni taglio
fl=int(FADE*sr);parts=[]
for k,(a,b) in enumerate(keep):
    seg=y[int(round(a*sr)):int(round(b*sr))].copy()
    if k>0 and len(seg)>fl:seg[:fl]*=np.linspace(0,1,fl,dtype=np.float32)
    if k<len(keep)-1 and len(seg)>fl:seg[-fl:]*=np.linspace(1,0,fl,dtype=np.float32)
    parts.append(seg)
sf.write(D+'audio/audio_B_full.wav',np.concatenate(parts),sr)
# 4. tempi delle parole nel montaggio condensato
def m(t):
    acc=0.0
    for a,b in keep:
        if t<a:return acc
        if t<=b:return acc+(t-a)
        acc+=b-a
    return acc
with open(D+'pk.jsonl','w') as f:
    for l in open(D+'pk_orig.jsonl'):
        d=json.loads(l);d['w']=[[round(m(t),3),w] for t,w in d['w']]
        for k_ in ('t','e'):
            if k_ in d:d[k_]=round(m(d[k_]),3)
        f.write(json.dumps(d,ensure_ascii=False)+'\n')
json.dump({'keep':keep},open(D+'mappa_tempi.json','w'))
# 5. riquadro della docente condensato (una codifica, piccola)
os.makedirs(D+'orig',exist_ok=True)
expr='+'.join(f'between(t,{a:.4f},{b-0.5/FPS:.4f})' for a,b in keep)
open(D+'sel.txt','w').write(f"[0:v]fps={FPS},select='{expr}',setpts=N/{FPS}/TB[v]")
if not os.path.exists(D+'orig/lez1.mp4'):
    sh(['ffmpeg','-v','error','-y','-i',D+'cam_full.mp4','-filter_complex_script',D+'sel.txt','-map','[v]','-an','-c:v','libx264','-preset','veryfast','-crf','18','-r',str(FPS),D+'orig/lez1.mp4'])
dv=float(subprocess.run(['ffprobe','-v','error','-show_entries','format=duration','-of','csv=p=0',D+'orig/lez1.mp4'],capture_output=True,text=True).stdout)
print('video',round(dv,2),'audio',round(tot,2),'scarto',round(dv-tot,3))
