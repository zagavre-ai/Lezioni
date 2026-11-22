# Motore di montaggio: voci, audio, clip, dissolvenze. Tutto in fotogrammi interi (30 fps) e campioni (48 kHz).
import os,re,json,hashlib,subprocess,numpy as np,soundfile as sf
from scipy.signal import resample_poly
B='/tmp/w/build';FPS=30;SR=48000;SPF=SR//FPS   # 1600 campioni per fotogramma
KIT='/home/user/Lezioni/kit'
def fr(t):return int(round(t*FPS))
def sh(c,**k):return subprocess.run(c,capture_output=True,text=True,**k)

# ---------- suoni ----------
def load_stereo(path):
    if path.endswith('.mp4'):
        tmp=f'{B}/tmp_'+os.path.basename(path)+'.wav'
        if not os.path.exists(tmp):subprocess.run(['ffmpeg','-v','error','-y','-i',path,'-vn','-ar','48000','-ac','2',tmp])
        path=tmp
    x,sr=sf.read(path,dtype='float32',always_2d=True)
    if sr!=SR:x=np.stack([resample_poly(x[:,i],SR,sr) for i in range(x.shape[1])],1).astype('float32')
    if x.shape[1]==1:x=np.repeat(x,2,1)
    return x[:,:2]
def mono(x):return x.mean(1) if x.ndim==2 else x
JING={k:load_stereo(f'{KIT}/suoni/{k}.wav') for k in ['trans','titolo','repaso','quiz','finale']}

# ---------- voci ----------
def split_sent(t):
    return [s.strip() for s in re.split(r'(?<=[.?!:])\s+(?=[A-ZÀ-ÝÈÉ«])',t) if s.strip()]
def tts_it(text,out):
    sh(['espeak-ng','-v','it','-s','158','-p','52','-w',out,text])
def lufs_gain(x,target=-16.0):
    import pyloudnorm as pyln
    m=pyln.Meter(SR);l=m.integrated_loudness(x if x.ndim==1 else x)
    return 10**((target-l)/20)
_VC={}
def voice(name,testi):
    """ritorna (audio mono 48k float32 a -16 LUFS, [inizio di ogni frase in s], frasi). Usa la voce vera in vox/ se c'e', altrimenti la provvisoria (espeak)."""
    if name in _VC:return _VC[name]
    sents=split_sent(testi[name])
    real=f'{B}/vox/{name}.wav'
    if os.path.exists(real):
        x=load_stereo(real);x=mono(x);starts=align(x,sents,name)
        prov=False
    else:
        os.makedirs(f'{B}/tts',exist_ok=True);parts=[];starts=[];t=0.0
        for i,s in enumerate(sents):
            p=f'{B}/tts/{name}_{i}.wav'
            if not os.path.exists(p):tts_it(s,p)
            y,sr=sf.read(p,dtype='float32');y=y if y.ndim==1 else y[:,0]
            y=resample_poly(y,SR,sr).astype('float32')
            # taglia il silenzio in coda
            nz=np.where(np.abs(y)>0.01)[0];y=y[:nz[-1]+int(0.04*SR)] if len(nz) else y
            starts.append(t);parts.append(y);gap=0.45 if s.endswith(('.','?')) else 0.3
            parts.append(np.zeros(int(gap*SR),'float32'));t+=len(y)/SR+gap
        x=np.concatenate(parts[:-1]);prov=True
    g=lufs_gain(x,-16.0) if len(x)>SR else 1.0
    x=(x*g).astype('float32')
    # bordi: dissolvenza di 30 ms
    k=int(0.03*SR);x[:k]*=np.linspace(0,1,k);x[-k:]*=np.linspace(1,0,k)
    _VC[name]=(x,starts,sents,prov);return _VC[name]
def _norm(w):
    import unicodedata
    w=unicodedata.normalize('NFD',w.lower());w=''.join(c for c in w if c.isalnum())
    return w
def asr_words(name):
    """trascrizione della voce vera con i tempi (Parakeet); in cache"""
    j=f'{B}/vox_asr/{name}.json'
    if not os.path.exists(j):
        os.makedirs(f'{B}/vox_asr',exist_ok=True)
        subprocess.run(['python3','-I',f'{KIT}/tools/trascrivi.py',f'{B}/vox/{name}.wav',f'{B}/vox_asr/{name}'],capture_output=True)
    d=json.load(open(j));S=d['segmenti'] if isinstance(d,dict) else d
    words=[];cur=None
    for g in S:
        for t,tok in g['parole']:
            if tok.startswith(' ') or cur is None:
                if cur:words.append(cur)
                cur=[t,tok.strip()]
            else:cur[1]+=tok
    if cur:words.append(cur)
    return words
def align(x,sents,name=None):
    tot=sum(len(s) for s in sents);d=len(x)/SR;t=0;prop=[]
    for s in sents:prop.append(t);t+=d*len(s)/tot
    if not name:return prop
    try:
        import difflib
        hyp=asr_words(name);H=[_norm(w) for _,w in hyp]
        ref=[];first=[]
        for s in sents:
            first.append(len(ref));ref+=[_norm(w) for w in s.split() if _norm(w)]
        sm=difflib.SequenceMatcher(None,ref,H,autojunk=False);mp={}
        for tag,i1,i2,j1,j2 in sm.get_opcodes():
            if tag=='equal':
                for k in range(i2-i1):mp[i1+k]=j1+k
        out=[]
        for k,f in enumerate(first):
            for d_ in range(0,4):
                if f+d_ in mp:out.append(max(0.0,hyp[mp[f+d_]][0]-0.05));break
            else:out.append(prop[k])
        for k in range(1,len(out)):
            if out[k]<=out[k-1]:out[k]=prop[k] if prop[k]>out[k-1] else out[k-1]+0.5
        out[0]=0.0
        return out
    except Exception as e:
        print('allineamento ASR fallito',name,e);return prop
# ---------- sequenza ----------
class TL:
    def __init__(s):s.segs=[]
    def add(s,kind,n,audio,spec,name,xf=True,page=None):
        n=int(n);a=np.zeros((n*SPF,2),'float32')
        if audio is not None:
            m=min(len(audio),len(a));a[:m]=audio[:m]
        s.segs.append(dict(kind=kind,n=n,a=a,spec=spec,name=name,xf=xf,page=page))
        return s.segs[-1]
def place(canvas,x,t,gain=1.0):
    """mescola x (stereo o mono) nel canvas a t secondi"""
    if x.ndim==1:x=np.repeat(x[:,None],2,1)
    i=int(round(t*SR));j=i+len(x)
    if i<0:x=x[-i:];i=0;j=i+len(x)
    j=min(j,len(canvas));canvas[i:j]+=x[:j-i]*gain

# ---------- render clip ----------
ENC=['-c:v','libx264','-preset','veryfast','-crf','14','-pix_fmt','yuv420p','-r','30','-g','30','-an']
MASK=f'{B}/mask.png'
def make_mask():
    if os.path.exists(MASK):return
    from PIL import Image,ImageDraw
    m=Image.new('L',(412,309),0);ImageDraw.Draw(m).rounded_rectangle((0,0,411,308),radius=18,fill=255);m.save(MASK)
make_mask()
def render_clip(spec,n,out):
    if os.path.exists(out) and os.path.getsize(out)>1000:return
    k=spec['k']
    if k=='still':
        c=['ffmpeg','-v','error','-y','-loop','1','-framerate','30','-i',spec['png'],'-frames:v',str(n)]+ENC+[out]
    elif k=='seq':
        lst=out+'.txt';L=[]
        for p,nf in spec['frames']:L.append(f"file '{p}'\nduration {nf/FPS:.6f}")
        L.append(f"file '{spec['frames'][-1][0]}'")
        open(lst,'w').write('\n'.join(L))
        c=['ffmpeg','-v','error','-y','-f','concat','-safe','0','-i',lst,'-vf','fps=30,format=yuv420p','-frames:v',str(n)]+ENC+[out]
    elif k=='prof':
        f0=spec['f0']
        c=['ffmpeg','-v','error','-y','-loop','1','-framerate','30','-i',spec['png'],'-ss',f'{f0/FPS:.6f}','-i',f'{B}/cam.mp4','-loop','1','-framerate','30','-i',MASK,
           '-filter_complex','[1:v]crop=412:309:0:0,format=rgba[c];[2:v]format=gray[m];[c][m]alphamerge[cm];[0:v][cm]overlay=1428:148:shortest=1,format=yuv420p',
           '-frames:v',str(n)]+ENC+[out]
    elif k=='video':
        c=['ffmpeg','-v','error','-y','-i',spec['path'],'-vf','fps=30,scale=1920:1080,format=yuv420p','-frames:v',str(n)]+ENC+[out]
    r=subprocess.run(c,capture_output=True,text=True)
    if r.returncode or not os.path.exists(out):raise SystemExit('ffmpeg: '+r.stderr[-400:]+' '+str(spec)[:200])
