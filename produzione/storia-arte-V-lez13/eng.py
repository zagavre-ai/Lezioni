# motore di montaggio: voci, tagli del docente, elementi, rendering a pezzi, giunzioni con dissolvenza
import os,re,json,subprocess,math,glob,hashlib,wave
import numpy as np
W='/tmp/claude-0/w/prod';FPS=30;SR=48000
SRC='/tmp/claude-0/w/mat/LEZIONE 13 RAZIONALISMO E METAFISICA.mp4'
SEG=json.load(open('/tmp/claude-0/w/trasc.json'))
K='/home/user/Lezioni/kit/'
OV=12   # fotogrammi di dissolvenza (0,4 s)
def sh(cmd,**k):
    r=subprocess.run(cmd,shell=isinstance(cmd,str),capture_output=True,text=True,**k)
    if r.returncode:raise RuntimeError(cmd if isinstance(cmd,str) else ' '.join(cmd))+'\n'+r.stderr[-1500:] if False else RuntimeError((cmd if isinstance(cmd,str) else ' '.join(cmd))[:300]+'\n'+r.stderr[-1800:])
    return r
# ---- voci ----
def vox(n):
    for d in ('vox','vox_prov'):
        p=f'{W}/{d}/{n}.wav'
        if os.path.exists(p):return p
    raise FileNotFoundError(n)
def vox_final(n):return os.path.exists(f'{W}/vox/{n}.wav')
def dur(p):return float(sh(['ffprobe','-v','error','-show_entries','format=duration','-of','csv=p=0',p]).stdout)
def voxwords(n):
    p=vox(n);j=p[:-4]+'.words.json'
    if not os.path.exists(j):
        import asr;json.dump(asr.words(p),open(j,'w'),ensure_ascii=False)
    return json.load(open(j))
TESTI={t['nome']:t['testo'] for t in json.load(open(W+'/testi_voci.json'))}
def sentences(text):
    return [s for s in re.split(r'(?<=[.?!])\s+',text.strip()) if s]
def sent_times(n,text=None):
    """[(frase, t_inizio, t_fine)] dalla trascrizione della voce"""
    import asr
    text=text or TESTI[n];ss=sentences(text);ref=text.split();T=asr.align(ref,voxwords(n))
    out=[];i=0;d=dur(vox(n))
    for k,s in enumerate(ss):
        c=len(s.split());out.append([s,T[i],None]);i+=c
    for k in range(len(out)):out[k][2]=out[k+1][1] if k+1<len(out) else d
    return out
# ---- numeri in cifre per lo schermo ----
U={'uno':1,'due':2,'tre':3,'quattro':4,'cinque':5,'sei':6,'sette':7,'otto':8,'nove':9}
TN={'venti':20,'trenta':30,'quaranta':40,'cinquanta':50}
SP={'dieci':10,'undici':11,'dodici':12,'tredici':13,'quattordici':14,'quindici':15,'sedici':16,'diciassette':17,'diciotto':18,'diciannove':19}
def parse_it(w):
    for t,v in sorted(TN.items(),key=lambda x:-len(x[0])):
        if w.startswith(t):
            r=w[len(t):].replace('tré','tre')
            if r=='':return v
            if r in U:return v+U[r]
            if r in ('uno','otto') :return v+U[r]
    if w in SP:return SP[w]
    if w in U:return U[w]
    return None
def digits(s):
    s=re.sub(r'millenovecento(\w*)',lambda m:str(1900+(parse_it(m.group(1)) or 0)) if m.group(1)=='' or parse_it(m.group(1)) else m.group(0),s)
    s=re.sub(r'\bventotto\b','28',s);s=re.sub(r'\bsedici\b','16',s);s=re.sub(r'\bottanta per cento\b','80%',s)
    return s
# ---- tagli del docente ----
FILL=re.compile(r'^(uh|um|mm|mm-hmm|yeah|the|fori|qui|okay|b dece)[\.\?!,]*$',re.I)
def keep(a,b):
    """intervalli sorgente [(s,e)] del docente tra a e b: toglie riempitivi e accorcia le pause oltre 2,5 s a 1 s"""
    segs=[s for s in SEG if s['inizio']>=a-0.06 and s['fine']<=b+0.06]
    good=[];lastbad=False;gaps=[]
    prev=None;fill_between=False
    for s in segs:
        if FILL.match(s['testo'].strip()) :
            fill_between=True;continue
        good.append((s,fill_between));fill_between=False
    iv=[]
    for i,(s,fb) in enumerate(good):
        lead=0.15;tail=0.25
        st=s['inizio']-lead;en=s['fine']+tail
        if i>0:
            pe=good[i-1][0]['fine'];g=s['inizio']-pe
            if g>2.5 or (fb and g>1.4):
                # pausa lunga o riempitivo tolto: pausa di circa 0,9 s
                iv[-1][1]=pe+0.45;st=s['inizio']-0.45
            else:
                iv[-1][1]=s['inizio'];st=s['inizio']
        iv.append([st,en])
    return [tuple(x) for x in iv],good
def frames_ranges(iv):
    """porta ogni intervallo a un numero intero di fotogrammi; ritorna [(a,n)]"""
    out=[]
    for a,b in iv:
        n=max(1,round((b-a)*FPS));out.append((round(a*1000)/1000,n))
    return out
# ---- elementi ----
class Item:
    def __init__(s,name,kind='static',**k):
        s.name=name;s.kind=kind;s.__dict__.update(k);s.audio=[];s.states=[];s.nf=0;s.meta={}
def audio_load(p):
    a=sh(['ffmpeg','-v','error','-i',p,'-f','f32le','-ac','2','-ar',str(SR),'-'],).stdout if False else subprocess.run(['ffmpeg','-v','error','-i',p,'-f','f32le','-ac','2','-ar',str(SR),'-'],capture_output=True).stdout
    return np.frombuffer(a,np.float32).reshape(-1,2)
def write_wav(p,x):
    x=np.clip(x,-1,1);b=(x*32767).astype('<i2').tobytes()
    with wave.open(p,'wb') as w:w.setnchannels(2);w.setsampwidth(2);w.setframerate(SR);w.writeframes(b)
def enc_args(crf=19):
    return ['-c:v','libx264','-preset','veryfast','-crf',str(crf),'-pix_fmt','yuv420p','-r','30','-x264-params','keyint=60:min-keyint=30:scenecut=0','-vf','scale=out_color_matrix=bt709:out_range=tv,format=yuv420p','-colorspace','bt709','-color_primaries','bt709','-color_trc','bt709','-an']
def render_static(it,out):
    """it.states=[(t0_s,png)] ; it.nf fotogrammi"""
    lst=out+'.txt';st=sorted(it.states,key=lambda x:x[0]);L=[]
    f0=[round(t*FPS) for t,_ in st]+[it.nf]
    for i,(t,p) in enumerate(st):
        n=f0[i+1]-f0[i]
        if n<=0:continue
        L.append(f"file '{p}'\nduration {n/FPS:.6f}")
    L.append(f"file '{st[-1][1]}'")
    open(lst,'w').write('\n'.join(L))
    sh(['ffmpeg','-v','error','-y','-f','concat','-safe','0','-i',lst,'-frames:v',str(it.nf)]+['-c:v','libx264','-preset','ultrafast','-crf','12','-pix_fmt','yuv420p','-r','30','-vf','fps=30,scale=out_color_matrix=bt709:out_range=tv,format=yuv420p','-colorspace','bt709','-an',out])
def render_prof(it,out,aout):
    """it.fr=[(a,n)] intervalli sorgente; it.states=[(t_out_s,png)] ; ritardo/coda 0,4 s di tenuta"""
    fr=it.fr;K_=len(fr);ins=[];fc=[];vs=[];As=[]
    for i,(a,n) in enumerate(fr):
        ins+=['-ss',f'{a:.3f}','-t',f'{n/FPS:.6f}','-i',SRC]
    base=K_
    ins+=['-f','concat','-safe','0','-i',it.name_lst,'-loop','1','-framerate','30','-i',W+'/mask_cam.png']
    for i,(a,n) in enumerate(fr):
        fc.append(f"[{i}:v]fps=30,trim=end_frame={n},setpts=PTS-STARTPTS,crop=184:138:853:336,scale=412:309:flags=lanczos,unsharp=5:5:0.7:5:5:0.0,eq=contrast=1.06:saturation=1.06:brightness=0.01[v{i}]")
        fc.append(f"[{i}:a]aresample=48000,aformat=channel_layouts=stereo,highpass=f=80,afftdn=nr=6:nf=-45,atrim=end={n/FPS:.6f},asetpts=PTS-STARTPTS,afade=t=in:d=0.02,afade=t=out:st={max(0,n/FPS-0.02):.4f}:d=0.02[a{i}]")
    fc.append(''.join(f'[v{i}]' for i in range(K_))+f'concat=n={K_}:v=1:a=0,tpad=start_duration=0.4:start_mode=clone:stop_duration=0.4:stop_mode=clone[cam]')
    fc.append(''.join(f'[a{i}]' for i in range(K_))+f'concat=n={K_}:v=0:a=1,adelay=400|400,apad=pad_dur=0.4[aud]')
    fc.append(f'[{base+1}:v]format=gray,trim=end_frame={it.nf},setpts=PTS-STARTPTS[mk]')
    fc.append('[cam][mk]alphamerge[camm]')
    fc.append(f'[{base}:v]fps=30,format=rgba[bg]')
    fc.append('[bg][camm]overlay=1428:148:shortest=1,format=yuv420p,trim=end_frame=%d,setpts=PTS-STARTPTS[vo]'%it.nf)
    cmd=['ffmpeg','-v','error','-y']+ins+['-filter_complex',';'.join(fc)]
    cmd+=['-map','[vo]','-c:v','libx264','-preset','ultrafast','-crf','12','-pix_fmt','yuv420p','-r','30','-colorspace','bt709','-an',out,'-map','[aud]','-t',f'{it.nf/FPS:.6f}','-c:a','pcm_s16le','-ar','48000','-ac','2',aout]
    sh(cmd)
def render_clip(it,out,aout):
    sh(['ffmpeg','-v','error','-y','-i',it.src,'-vf','fps=30,scale=1920:1080,scale=out_color_matrix=bt709:out_range=tv,format=yuv420p','-c:v','libx264','-preset','ultrafast','-crf','12','-pix_fmt','yuv420p','-an',out])
    sh(['ffmpeg','-v','error','-y','-i',it.src,'-vn','-ac','2','-ar','48000','-c:a','pcm_s16le',aout])
def nframes(p):
    r=sh(['ffprobe','-v','error','-count_packets','-select_streams','v:0','-show_entries','stream=nb_read_packets','-of','csv=p=0',p]);return int(r.stdout.strip().split(',')[-1])
