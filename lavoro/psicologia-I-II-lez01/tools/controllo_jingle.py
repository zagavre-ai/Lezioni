# Controllo obbligatorio dopo la codifica: lo scatto musicale di ogni scheda Quiz deve cadere a 0,0 s.
# uso: python3 controllo_jingle.py video_finale.mp4 timeline.json   (timeline: [[nome, inizio_s, durata_s], ...])
# atteso = inizio della scheda Q + 0,5 s (joff del montaggio). Scarto accettato: |scarto| <= 0,05 s.
import sys,json,subprocess,numpy as np
V,TL=sys.argv[1:3];SR=8000;JOFF=float(sys.argv[3]) if len(sys.argv)>3 else 0.5
def rd(f,ss=None,d=None):
    c=['ffmpeg','-v','error']+(['-ss',str(ss),'-t',str(d)] if ss is not None else [])+['-i',f,'-ac','1','-ar',str(SR),'-f','s16le','-']
    return np.frombuffer(subprocess.run(c,capture_output=True).stdout,np.int16).astype(float)
ref=rd('/home/claude/v5/snd/quiz.wav');ref=ref[:SR*2]
bad=0
for n,t,l in json.load(open(TL)):
    if not n.startswith('Q'):continue
    s=t-1.5;x=rd(V,s,5);c=np.correlate(x,ref,'valid');k=int(np.argmax(c));sc=s+k/SR-(t+JOFF)
    ok=abs(sc)<=0.05;bad+=not ok
    print(n,'atteso %.3f trovato %.3f scarto %+.3f'%(t+JOFF,s+k/SR,sc),'OK' if ok else 'DA CORREGGERE')
sys.exit(1 if bad else 0)
