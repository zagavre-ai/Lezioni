# -*- coding: utf-8 -*-
# Controlli sul video finale di una Parte. uso: python3 check.py P
import sys, os, re, json, subprocess, numpy as np
sys.path.insert(0,'/home/work/build')
import assemble as AS, plan as PL
P=int(sys.argv[1]);V=f'/home/work/build/out/Storia_Lez17_Parte{P}_1080p.mp4';TL=json.load(open(f'/home/work/build/out_timeline_P{P}.json'))
R=[]
def say(*a):
    s=' '.join(str(x) for x in a);print(s,flush=True);R.append(s)
def sh(c): return subprocess.run(c,capture_output=True,text=True)
j=json.loads(sh(['ffprobe','-v','error','-count_packets','-select_streams','v:0','-show_entries','stream=nb_read_packets,width,height,r_frame_rate:format=duration,size','-of','json',V]).stdout)
d=float(j['format']['duration']);fr=int(j['streams'][0]['nb_read_packets']);mb=int(j['format']['size'])/1e6
say(f"[misurato] durata {int(d//60)}:{d%60:04.1f} ({d:.1f} s) | fotogrammi {fr} (attesi {round(d*30)}) {'OK' if fr==round(d*30) else 'NO'} | peso {mb:.1f} MB {'OK' if mb<400 else 'NO'} | {j['streams'][0]['width']}x{j['streams'][0]['height']} {j['streams'][0]['r_frame_rate']}")
I,tp=AS.lufs(V);say(f"[misurato] LUFS integrato {I} (obiettivo -16 ±1) {'OK' if abs(I+16)<=1 else 'NO'} | picco vero {tp} dBTP {'OK' if tp is not None and tp<=-1 else 'NO'}")
# silenzi
r=sh(['ffmpeg','-nostats','-i',V,'-af','silencedetect=n=-50dB:d=2.5','-f','null','-']).stderr
sil=re.findall(r'silence_start: ([\d\.]+)',r);say(f"[misurato] silenzi > 2,5 s (-50 dB): {len(sil)} {[round(float(x)) for x in sil][:10]}")
# jingle quiz
SR=8000
def rd(f,ss=None,dd=None):
    c=['ffmpeg','-v','error']+(['-ss',str(ss),'-t',str(dd)] if ss is not None else [])+['-i',f,'-ac','1','-ar',str(SR),'-f','s16le','-']
    return np.frombuffer(sh(c).stdout if False else subprocess.run(c,capture_output=True).stdout,np.int16).astype(float)
ref=rd('/home/user/Lezioni/kit/suoni/quiz.wav')[:SR*2]
for n,t,f in TL:
    if n.startswith('quiz'):
        x=rd(V,t,3.5);cc=np.correlate(x,ref,'valid');k=int(np.argmax(cc));sc=k/SR-0.5
        say(f"[misurato] jingle {n}: atteso {t+0.5:.3f} trovato {t+k/SR:.3f} scarto {sc:+.3f} {'OK' if abs(sc)<=0.05 else 'NO'}")
# tagli del prof (tabella)
say("\n### Tabella: fine di ogni pezzo del prof (dall'originale, trascrizione)")
for n,t,f in TL:
    if n.startswith('prof'):
        pj=json.load(open([x for x in __import__('glob').glob('/home/work/build/pieces/P%d_T*.mp4.json'%P) if True][0])) if False else None
import glob
for fn in sorted(glob.glob(f'/home/work/build/pieces/P{P}_T*.mp4.json')):
    pj=json.load(open(fn));a,b=pj['cut'];segs=[s for s in PL.S if s['fine']<=b+0.01 and s['inizio']>=a-0.01]
    last=segs[-1];words=last['testo'].split()[-8:];ok=bool(re.search(r'[\.\?\!…]\s*$',last['testo'].strip()))
    first=segs[0]['testo'].split()[:6];gap=min([s['inizio'] for s in PL.S if s['inizio']>=b],default=0)-b
    tl=[x for x in TL if x[0].startswith('prof') and abs(x[2]-pj['N'])<5]
    minute=''
    say(f"- {os.path.basename(fn)[:-9]}: originale {a:.1f}–{b:.1f} s | inizio «{' '.join(first)}…» | fine «…{' '.join(words)}» | frase finita: {'sì' if ok else 'NO (da rivedere)'} | taglio {gap:.2f} s prima della frase che segue")
# schermata identica (area slide)
say("\n### Schermate identiche")
r=sh(['ffmpeg','-nostats','-i',V,'-vf','crop=1340:800:60:180,freezedetect=n=0.003:d=60','-an','-f','null','-']).stderr
fs=re.findall(r'freeze_start: ([\d\.]+)',r);fd=re.findall(r'freeze_duration: ([\d\.]+)',r);fe=re.findall(r'freeze_end: ([\d\.]+)',r)
long=[(float(a),float(b)) for a,b in zip(fs,fd)]
say(f"[misurato] schermate ferme > 60 s: {[(round(a),round(b)) for a,b in long]} (limite 180 s)  {'OK' if all(b<180 for a,b in long) else 'NO'}")
say(f"[misurato] schermata ferma più lunga: {max([b for a,b in long],default=0):.0f} s")
open(f'/home/work/build/controlli_P{P}.txt','w').write('\n'.join(R))
