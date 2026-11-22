import sys,os,json,subprocess,re
import numpy as np
sys.path.insert(0,'/home/user/work/build')
from kit2 import *
from subs import words_prof
V=sys.argv[1];TL=json.load(open(sys.argv[2]))['tl'];OUT=sys.argv[3]
R=[]
def say(*x):
    s=' '.join(str(i) for i in x);print(s,flush=True);R.append(s)
def sh(c,**k): return subprocess.run(c,capture_output=True,text=True,**k)
j=json.loads(sh(['ffprobe','-v','error','-count_packets','-select_streams','v:0','-show_entries','stream=nb_read_packets,width,height,r_frame_rate:format=duration,size','-of','json',V]).stdout)
dur=float(j['format']['duration']);fr=int(j['streams'][0]['nb_read_packets']);mb=int(j['format']['size'])/1e6
say(f"## Misure sul file finale\n- durata {int(dur//60)}:{dur%60:04.1f} ({dur:.1f} s) [misurato]\n- fotogrammi {fr}, attesi {round(dur*30)} (durata × 30) → {'OK' if abs(fr-dur*30)<=3 else 'NO'} [misurato]\n- peso {mb:.1f} MB → {'OK' if mb<400 else 'NO'} [misurato]\n- formato {j['streams'][0]['width']}x{j['streams'][0]['height']} {j['streams'][0]['r_frame_rate']}")
e=sh(['ffmpeg','-hide_banner','-nostats','-i',V,'-af','ebur128=peak=true','-vn','-f','null','-']).stderr
I=re.findall(r'\n\s+I:\s+(-?[\d.]+) LUFS',e);P=re.findall(r'Peak:\s+(-?[\d.]+) dBFS',e)
say(f"- volume integrato {I[-1]} LUFS (obiettivo −16 ±1); picco reale {P[-1]} dBTP (limite −1) [misurato]")
s=sh(['ffmpeg','-hide_banner','-nostats','-i',V,'-vn','-af','silencedetect=noise=-45dB:d=2.5','-f','null','-']).stderr
sil=re.findall(r'silence_start: ([\d.]+)',s)
say(f"- silenzi oltre 2,5 s (−45 dB): {len(sil)} {sil[:8]} [misurato]")
# timbre sui pezzi del docente
D=[(n,t,l) for n,t,l in TL if n.startswith('D')]
def timbre(a,b,f):
    r=sh(['ffmpeg','-hide_banner','-nostats','-ss',str(a),'-t',str(b-a),'-i',f,'-vn','-af',f'highpass=f=100,volumedetect','-f','null','-']).stderr
    x=float(re.findall(r'mean_volume: (-?[\d.]+)',r)[-1])
    r=sh(['ffmpeg','-hide_banner','-nostats','-ss',str(a),'-t',str(b-a),'-i',f,'-vn','-af',f'highpass=f=4000,volumedetect','-f','null','-']).stderr
    y=float(re.findall(r'mean_volume: (-?[\d.]+)',r)[-1]);return y-x
ORIG=W+'/orig/LEZIONE 11 L_URSS DI STALIN (1924-1939).mp4'
tf=[timbre(t+0.5,t+l-0.5,V) for n,t,l in D if l>3]
to=timbre(60,1500,ORIG)
say(f"- timbre (acuti >4 kHz meno volume >100 Hz): finale min {min(tf):.1f} max {max(tf):.1f} dB; originale {to:.1f} dB; ammesso −20…−9 → {'OK' if all(-20<=x<=-9 for x in tf) else 'NO'} [misurato]")
# sincronia: audio finale vs originale per ogni pezzo D (correlazione), video finale vs originale (cam)
PROF={'D0':0.0,'D1':57.6,'D2':357.35,'D3':471.7,'D4':871.3,'D5':1013.8,'D6a':1145.55,'D6b':1322.3,'D6c':1413.8}
def rd(f,ss,d,sr=8000):
    return np.frombuffer(sh(['ffmpeg','-v','error','-ss',str(ss),'-t',str(d),'-i',f,'-vn','-ac','1','-ar',str(sr),'-f','s16le','-'],) .stdout if False else subprocess.run(['ffmpeg','-v','error','-ss',str(ss),'-t',str(d),'-i',f,'-vn','-ac','1','-ar',str(sr),'-f','s16le','-'],capture_output=True).stdout,np.int16).astype(float)
say("\n## Sincronia labbra/voce (audio e video finale confrontati con l'originale)\n| pezzo | scarto audio (s) | scarto video (s) | labbra−voce (s) |\n|---|---|---|---|")
for n,t,l in D:
    if l<5: continue
    a0=PROF[n];x=rd(V,t+1,min(20,l-2));o=rd(ORIG,a0+1-0.5,min(20,l-2)+1.0)
    c=np.correlate(o,x,'valid');k=int(np.argmax(c));aoff=(k/8000)-0.5
    # video: cam
    def cam(f,ss,fps=10,n_=60):
        p=subprocess.run(['ffmpeg','-v','error','-ss',str(ss),'-t',str(n_/fps),'-i',f,'-vf',f'fps={fps},crop={412 if f==V else 180}:{309 if f==V else 135}:{1428 if f==V else 881}:{148 if f==V else 345},scale=64:48,format=gray','-f','rawvideo','-'],capture_output=True).stdout
        return np.frombuffer(p,np.uint8).reshape(-1,48,64).astype(float)
    vf=cam(V,t+3);vo=[];best=None
    cands=[];
    base=a0+3-0.5
    vo=cam(ORIG,base,10,70)
    m=min(len(vf),60)
    errs=[]
    for sft in range(0,11):
        e_=np.mean((vo[sft:sft+m]-vf[:m])**2) if sft+m<=len(vo) else 1e9;errs.append(e_)
    sb=int(np.argmin(errs));voff=sb/10-0.5
    say(f"| {n} | {aoff:+.3f} | {voff:+.2f} (passo 0,1 s) | {aoff-voff:+.2f} |")
say("(il video è tagliato dallo stesso file e agli stessi tempi dell'audio: lo scarto atteso è 0 entro 1 fotogramma = 0,033 s)")
# fermi del docente
say("\n## Fermi immagine nei pezzi del docente (freezedetect sul riquadro, ≥ 1 s)")
fz=[]
for n,t,l in D:
    r=sh(['ffmpeg','-v','info','-ss',str(t),'-t',str(l),'-i',V,'-vf','crop=412:309:1428:148,freezedetect=n=0.0005:d=1.0','-map','0:v','-f','null','-']).stderr
    st=re.findall(r'freeze_start: ([\d.]+)',r)
    if st: fz.append((n,st[:3]))
say('nessuno [misurato]' if not fz else f'DA GUARDARE {fz}')
# tabella fine di ogni pezzo
W_=words_prof();say("\n## Fine di ogni pezzo del docente\n| pezzo | minuto video (fine) | ultime parole (orig.) | frase finita |\n|---|---|---|---|")
BND={'D0':(0,57.6),'D1':(57.6,357.35),'D2':(357.35,471.7),'D3':(471.7,871.3),'D4':(871.3,1013.8),'D5':(1013.8,1145.55),'D6a':(1145.55,1322.3),'D6b':(1322.3,1413.8),'D6c':(1413.8,1506.13)}
for n,t,l in D:
    a,b=BND[n];ws=[(tt,w) for tt,w in W_ if w and tt<b][-8:];tail=' '.join(w for _,w in ws)
    last=[w for tt,w in ws][-1] if ws else ''
    say(f"| {n} | {int((t+l)//60)}:{(t+l)%60:04.1f} | …{tail} | {'sì' if last[-1:] in '.?!' else 'no'} |")
open(OUT,'w').write('\n'.join(R))
