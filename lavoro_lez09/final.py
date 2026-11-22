# Dissolvenze di 0,5 s tra i pezzi + codifica finale unica. uso: python3 final.py PARTE [crf]
import sys,os,json,subprocess,re
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
W='/home/user/Lezioni/w/lav/out';XF=0.5
parte=int(sys.argv[1]);crf=sys.argv[2] if len(sys.argv)>2 else '19'
P=json.load(open(W+f'/parte{parte}_pezzi.json'))
def dur(p):return float(subprocess.run(['ffprobe','-v','error','-show_entries','format=duration','-of','csv=p=0',p],capture_output=True,text=True).stdout)
D=[dur(p) for n,p in P];print('durata pezzi',sum(D)/60)
os.makedirs(W+f'/f{parte}',exist_ok=True)
seg=[];S=[];s0=0.0
for k,(n,p) in enumerate(P):
    S.append(s0);a=XF if k>0 else 0.0;b=D[k]-(XF if k<len(P)-1 else 0.0)
    seg.append((p,a,b))
    if k<len(P)-1:
        bl=W+f'/f{parte}/x{k:02d}.mkv'
        if not os.path.exists(bl) or os.path.getmtime(bl)<max(os.path.getmtime(p),os.path.getmtime(P[k+1][1])):
            subprocess.run(['ffmpeg','-v','error','-y','-ss',f'{D[k]-XF:.3f}','-t',str(XF),'-i',p,'-ss','0','-t',str(XF),'-i',P[k+1][1],'-filter_complex',f'[0:v][1:v]xfade=transition=fade:duration={XF}:offset=0,format=yuv420p[v];[0:a]aformat=channel_layouts=stereo[a0];[1:a]aformat=channel_layouts=stereo[a1];[a0][a1]amix=inputs=2:duration=longest:normalize=0[a]','-map','[v]','-map','[a]','-r','30','-c:v','libx264','-preset','veryfast','-crf','16','-c:a','pcm_s16le','-ar','48000',bl],check=True)
        seg.append((bl,0,XF))
    s0+=D[k]-XF
tot=s0+XF
L=[]
for p,a,b in seg:L.append(f"file '{p}'\ninpoint {a:.3f}\noutpoint {b:.3f}")
open(W+f'/f{parte}/c.txt','w').write('\n'.join(L))
# livello: misura
cat=W+f'/f{parte}/audio.wav'
subprocess.run(['ffmpeg','-v','error','-y','-f','concat','-safe','0','-i',W+f'/f{parte}/c.txt','-vn','-c:a','pcm_s16le',cat],check=True)
r=subprocess.run(['ffmpeg','-v','info','-i',cat,'-af','ebur128=framelog=quiet','-f','null','-'],capture_output=True,text=True).stderr
I=float(re.findall(r'I:\s+(-?[\d.]+) LUFS',r)[-1]);g=-16-I;print('LUFS misurato',I,'gain',g)
out=W+f'/Storia_Lez9_Parte{parte}_1080p.mp4'
subprocess.run(['ffmpeg','-v','error','-y','-f','concat','-safe','0','-i',W+f'/f{parte}/c.txt','-af',f'volume={g:.2f}dB,alimiter=limit=0.89:level=0','-c:v','libx264','-preset','veryfast','-crf',crf,'-pix_fmt','yuv420p','-r','30','-c:a','aac','-b:a','192k','-ar','48000','-movflags','+faststart',out],check=True)
json.dump([[('D'+n[1:] if re.fullmatch(r'A\d+',n) else n),round(S[i],3),round(D[i],3)] for i,(n,p) in enumerate(P)],open(W+f'/timeline_Parte{parte}.json','w'))
print('fatto',out,tot/60)
