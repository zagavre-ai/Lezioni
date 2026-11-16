# Come kit/tools/finale_a_pezzi.py (stessi parametri: 1080p lanczos, x264 veryfast CRF 19, maxrate 16M, AAC 192k dalla lista intera),
# ma ogni pezzo del docente (b_D*) è un gruppo a sé, salvato in una cartella comune: quando cambiano solo le voci
# (segnaposto -> Kore) i pezzi del docente già codificati si riusano e si codificano solo i pezzi nuovi.
# uso: python3 finale_cache.py lista.txt uscita.mp4 cartella_cache [--solo-video]   (--solo-video: codifica solo i pezzi del docente, per prepararli prima delle voci)
import sys,os,subprocess,re,hashlib
L,OUT,C=os.path.abspath(sys.argv[1]),os.path.abspath(sys.argv[2]),os.path.abspath(sys.argv[3]);SOLO='--solo-video' in sys.argv
os.makedirs(C,exist_ok=True);W=OUT+'.gruppi/';os.makedirs(W,exist_ok=True)
P=re.findall(r"file '(.+)'",open(L).read())
fr=lambda f:int(subprocess.run(['ffprobe','-v','error','-select_streams','v:0','-count_packets','-show_entries','stream=nb_read_packets','-of','csv=p=0',f],capture_output=True,text=True).stdout.strip())
du=lambda f:float(subprocess.run(['ffprobe','-v','error','-show_entries','format=duration','-of','csv=p=0',f],capture_output=True,text=True).stdout)
G=[];cur=[]
for p in P:
    if os.path.basename(p).startswith('b_D'):
        if cur:G.append(cur);cur=[]
        G.append([p])
    else: cur.append(p)
if cur:G.append(cur)
CRF=os.environ.get('CRF','19');PRE=os.environ.get('PRESET','veryfast')
def key(g):
    h=hashlib.sha1(f'{CRF}{PRE}'.encode())
    for p in g: st=os.stat(p);h.update(f'{st.st_ino}:{st.st_size}:{int(st.st_mtime)};'.encode())
    return h.hexdigest()[:16]
files=[]
for k,g in enumerate(G):
    f=C+'/'+key(g)+'.mp4';files.append(f)
    if os.path.exists(f+'.ok'):continue
    if SOLO and not os.path.basename(g[0]).startswith('b_D'):continue
    open(f+'.txt','w').write(''.join("file '%s'\n"%p for p in g))
    subprocess.run(['nice','-n','5','ffmpeg','-y','-v','error','-f','concat','-safe','0','-i',f+'.txt','-map','0:v','-vf','scale=1920:1080:flags=lanczos',
        '-c:v','libx264','-preset',PRE,'-crf',CRF,'-maxrate','16M','-bufsize','32M','-pix_fmt','yuv420p','-r','30','-an',f],check=True)
    open(f+'.ok','w').write('1');print('gruppo',k+1,'di',len(G),os.path.basename(g[0]),flush=True)
if SOLO: print('solo video: fatto');sys.exit()
if not os.path.exists(W+'a.m4a.ok'):
    subprocess.run(['ffmpeg','-y','-v','error','-f','concat','-safe','0','-i',L,'-map','0:a','-c:a','aac','-b:a','192k','-ar','48000',W+'a.m4a'],check=True);open(W+'a.m4a.ok','w').write('1')
open(W+'v.txt','w').write(''.join("file '%s'\n"%f for f in files))
subprocess.run(['ffmpeg','-y','-v','error','-f','concat','-safe','0','-i',W+'v.txt','-i',W+'a.m4a','-map','0:v','-map','1:a','-c','copy','-movflags','+faststart',OUT],check=True)
nv=fr(OUT);ns=sum(fr(f) for f in files)
print(OUT,'fotogrammi',nv,'gruppi',ns,'| durata video',du(OUT),'| MB',round(os.path.getsize(OUT)/2**20,1))
assert nv==ns
