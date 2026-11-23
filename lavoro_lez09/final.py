# Dissolvenze di 0,5 s tra i pezzi + codifica finale unica. uso: python3 final.py PARTE [crf]
import sys,os,json,subprocess,re
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
W='/home/user/Lezioni/w/lav/out';XF=0.5
parte=int(sys.argv[1]);crf=sys.argv[2] if len(sys.argv)>2 else '19'
P=json.load(open(W+f'/parte{parte}_pezzi.json'))
def dur(p):return float(subprocess.run(['ffprobe','-v','error','-show_entries','format=duration','-of','csv=p=0',p],capture_output=True,text=True).stdout)
def nfr(p):return int(subprocess.run(['ffprobe','-v','error','-select_streams','v:0','-count_packets','-show_entries','stream=nb_read_packets','-of','csv=p=0',p],capture_output=True,text=True).stdout)
FR=[nfr(p) for n,p in P];D=[f/30 for f in FR];print('durata pezzi',sum(D)/60)
EPS=1/60
os.makedirs(W+f'/f{parte}',exist_ok=True)
seg=[];S=[];s0=0.0
for k,(n,p) in enumerate(P):
    S.append(s0);a=XF if k>0 else 0.0;b=D[k]-(XF if k<len(P)-1 else 0.0)
    seg.append((p,a,b,k))
    if k<len(P)-1:
        bl=W+f'/f{parte}/x{k:02d}.mkv'
        if not os.path.exists(bl) or os.path.getmtime(bl)<max(os.path.getmtime(p),os.path.getmtime(P[k+1][1])):
            subprocess.run(['ffmpeg','-v','error','-y','-ss',f'{D[k]-XF:.5f}','-t',str(XF),'-i',p,'-ss','0','-t',str(XF),'-i',P[k+1][1],'-filter_complex',f'[0:v][1:v]xfade=transition=fade:duration={XF}:offset=0,format=yuv420p[v]','-map','[v]','-an','-r','30','-frames:v','15','-c:v','libx264','-preset','veryfast','-crf','16',bl],check=True)
        seg.append((bl,0,XF,-1))
    s0+=D[k]-XF
tot=s0+XF
L=[]
for p,a,b,k in seg:
    if k<0:L.append(f"file '{p}'")
    else:
        ln=f"file '{p}'"
        if a>0:ln+=f"\ninpoint {a-EPS:.5f}"
        if b<D[k]:ln+=f"\noutpoint {b-EPS:.5f}"
        L.append(ln)
open(W+f'/f{parte}/c.txt','w').write('\n'.join(L))
# audio campione per campione: ogni pezzo sommato alla sua posizione esatta (le dissolvenze di 0,5 s sommano coda e attacco)
import numpy as np
SR=48000;cum=0;tot_fr=sum(FR)-15*(len(FR)-1);out_a=np.zeros((tot_fr*1600,2),np.float32)
for k,(n,p) in enumerate(P):
    x=np.frombuffer(subprocess.run(['ffmpeg','-v','error','-i',p,'-vn','-ac','2','-ar',str(SR),'-f','f32le','-'],capture_output=True).stdout,np.float32).reshape(-1,2)
    L=FR[k]*1600;x=x[:L];s0_=cum*1600;out_a[s0_:s0_+len(x)]+=x;cum+=FR[k]-15
import wave
cat=W+f'/f{parte}/audio.wav';
with wave.open(cat,'wb') as wf:
    wf.setnchannels(2);wf.setsampwidth(2);wf.setframerate(SR);wf.writeframes((np.clip(out_a,-1,1)*32767).astype(np.int16).tobytes())
r=subprocess.run(['ffmpeg','-v','info','-i',cat,'-af','ebur128=framelog=quiet','-f','null','-'],capture_output=True,text=True).stderr
I=float(re.findall(r'I:\s+(-?[\d.]+) LUFS',r)[-1]);g=-16-I;print('LUFS misurato',I,'gain',g)
out=W+f'/Storia_Lez9_Parte{parte}_1080p.mp4'
subprocess.run(['ffmpeg','-v','error','-y','-f','concat','-safe','0','-i',W+f'/f{parte}/c.txt','-i',cat,'-map','0:v','-map','1:a','-af',f'volume={g:.2f}dB,alimiter=limit=0.89:level=0','-c:v','libx264','-preset','veryfast','-crf',crf,'-pix_fmt','yuv420p','-r','30','-c:a','aac','-b:a','192k','-ar','48000','-movflags','+faststart',out],check=True)
json.dump([[('D'+n[1:] if re.fullmatch(r'A\d+',n) else n),round(S[i],3),round(D[i],3)] for i,(n,p) in enumerate(P)],open(W+f'/timeline_Parte{parte}.json','w'))
print('fatto',out,tot/60)
