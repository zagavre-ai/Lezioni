# Codifica finale del montaggio a gruppi di pezzi (riprende da dove si è fermata).
# uso: python3 finale_a_pezzi.py lista.txt uscita.mp4
# lista.txt = la lista concat scritta da asm_moda2.py (SOLOLISTA=1).
# - video: gruppi di pezzi consecutivi (circa 8 minuti), scalati a 1080p (RIS=1440 per il vecchio formato), x264 veryfast CRF 19 (CRF=…): esce direttamente il video da caricare, sotto i 400 MB
# - audio: tutto in una volta dalla lista completa (AAC 192k), così non ci sono scarti tra i gruppi
# - unione senza ricomprimere; controllo: fotogrammi uguali alla somma dei pezzi
import sys,os,subprocess,re
L,OUT=os.path.abspath(sys.argv[1]),os.path.abspath(sys.argv[2]);W=OUT+'.gruppi/';os.makedirs(W,exist_ok=True)
P=re.findall(r"file '(.+)'",open(L).read())
fr=lambda f:int(subprocess.run(['ffprobe','-v','error','-select_streams','v:0','-count_packets','-show_entries','stream=nb_read_packets','-of','csv=p=0',f],capture_output=True,text=True).stdout.strip())
du=lambda f:float(subprocess.run(['ffprobe','-v','error','-show_entries','format=duration','-of','csv=p=0',f],capture_output=True,text=True).stdout)
G=[];cur=[];s=0
for p in P:
    cur.append(p);s+=du(p)
    if s>=480:G.append(cur);cur=[];s=0
if cur:G.append(cur)
for k,g in enumerate(G):
    f=W+'g%03d.mp4'%k
    if os.path.exists(f+'.ok'):continue
    open(W+'g%03d.txt'%k,'w').write(''.join("file '%s'\n"%p for p in g))
    subprocess.run(['nice','-n','5','ffmpeg','-y','-v','error','-f','concat','-safe','0','-i',W+'g%03d.txt'%k,'-map','0:v','-vf','scale='+('2560:1440' if os.environ.get('RIS')=='1440' else '1920:1080')+':flags=lanczos',
        '-c:v','libx264','-preset',os.environ.get('PRESET','veryfast'),'-crf',os.environ.get('CRF','19'),'-maxrate','16M','-bufsize','32M','-pix_fmt','yuv420p','-r','30','-an',f],check=True)
    open(f+'.ok','w').write('1');print('gruppo',k+1,'di',len(G),flush=True)
if not os.path.exists(W+'a.m4a.ok'):
    subprocess.run(['ffmpeg','-y','-v','error','-f','concat','-safe','0','-i',L,'-map','0:a','-c:a','aac','-b:a','192k','-ar','48000',W+'a.m4a'],check=True);open(W+'a.m4a.ok','w').write('1')
open(W+'v.txt','w').write(''.join("file '%sg%03d.mp4'\n"%(W,k) for k in range(len(G))))
subprocess.run(['ffmpeg','-y','-v','error','-f','concat','-safe','0','-i',W+'v.txt','-i',W+'a.m4a','-map','0:v','-map','1:a','-c','copy','-movflags','+faststart',OUT],check=True)
nv=fr(OUT);ns=sum(fr(W+'g%03d.mp4'%k) for k in range(len(G)))
print(OUT,'fotogrammi',nv,'gruppi',ns,'| durata video',du(OUT),'| MB',round(os.path.getsize(OUT)/2**20,1))
assert nv==ns
