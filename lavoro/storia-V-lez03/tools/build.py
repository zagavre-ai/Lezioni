import sys,json,os,subprocess,shutil
sys.path.insert(0,'/tmp/w/tools')
import numpy as np
from multiprocessing import Pool
import vid,audio
from audio import SR
SEG='/tmp/w/build/seg/';os.makedirs(SEG,exist_ok=True)
SRC='/tmp/w/dl/LEZIONE3.mp4'
PROFA=audio.Mem('/tmp/w/profaudio.raw')
TRANS='/tmp/w/kit/home/claude/v5/snd/trans.wav'
CHUNK=7200
def pieces(part,i,seg):
    k=seg['k'];base=f"{part}_{i:03d}_{seg['id']}"
    if k=='prof':
        # timeline bg -> lista (png,frames) con crossfade
        st=seg['bg'];F=seg['frames'];ev=[]
        for j,(t,png,mode) in enumerate(st):
            f0=round(t*30);f1=round(st[j+1][0]*30) if j+1<len(st) else F
            ev.append((png,f0,f1,mode))
        # espandi in per-fotogramma-run
        runs=[]
        from PIL import Image
        for j,(png,f0,f1,mode) in enumerate(ev):
            if mode=='x' and j>0 and f1-f0>8:
                prev=ev[j-1][0];xf=f"{SEG}x_{os.path.basename(prev)[:-4]}_{os.path.basename(png)[:-4]}"
                for s_ in range(1,7):
                    p=f"{xf}_{s_}.png"
                    if not os.path.exists(p):
                        a=Image.open(prev).convert('RGB');b=Image.open(png).convert('RGB');Image.blend(a,b,s_/7).save(p)
                    runs.append((p,1))
                runs.append((png,f1-f0-6))
            else: runs.append((png,f1-f0))
        # spezza in chunk
        out=[];pos=0;cur=[];curf=0;n=0
        for png,f in runs:
            while f>0:
                take=min(f,CHUNK-curf);cur.append((png,take));curf+=take;f-=take
                if curf==CHUNK: out.append((cur,curf));cur=[];curf=0
        if cur: out.append((cur,curf))
        res=[];pos=0
        for n,(seq,cf) in enumerate(out):
            res.append(dict(out=f"{SEG}{base}_c{n}.mp4",kind='prof',seq=seq,t0=seg['t0']+pos/30,frames=cf));pos+=cf
        return res
    if k=='seq': return [dict(out=f"{SEG}{base}.mp4",kind='seq',seq=seg['seq'],frames=seg['frames'])]
    return [dict(out=f"{SEG}{base}.mp4",kind='card',mp4=seg['mp4'],frames=seg['frames'])]
def do(p):
    if os.path.exists(p['out']) and os.path.getsize(p['out'])>1000: return p['out']
    tmp=p['out']+'.part.mp4'
    if p['kind']=='seq': vid.enc_seq(p['seq'],tmp)
    elif p['kind']=='prof': vid.enc_prof(p['seq'],SRC,p['t0'],tmp)
    else: vid.enc_card(p['mp4'],p['frames'],tmp)
    os.rename(tmp,p['out']);return p['out']
def seg_audio(seg):
    F=seg['frames'];parts=[]
    if seg['k']=='prof':
        parts.append((PROFA.cut(seg['t0'],seg['t0']+F/30),0,1.0))
    for a in seg.get('aud',[]):
        x=audio.rd(a['f'])
        if a.get('a') is not None or a.get('b') is not None:
            x=x[int((a.get('a') or 0)*SR):int(a['b']*SR) if a.get('b') else None]
        parts.append((x,a['off'],a['g']))
    return audio.mix(F,parts)
def trans_audio(frames,g=0.8):
    x=audio.rd(TRANS);n=int(frames/30*SR);x=x[:n].copy()
    fo=int(0.4*SR);x[-fo:]*=np.linspace(1,0,fo)[:,None]
    return audio.mix(frames,[(x,0,g)])
def build_part(part,segs,tdur=None,workers=4,nocopy=False):
    jobs=[];plist=[]
    for i,s in enumerate(segs):
        ps=pieces(part,i,s);plist.append(ps);jobs+=ps
    with Pool(workers) as pool: list(pool.imap_unordered(do,jobs))
    concat=[];audf=open(f'/tmp/w/build/{part}.raw','wb');tl=[];tpos=0;frames_total=0
    for i,s in enumerate(segs):
        tl.append(dict(id=s['id'],start=round(frames_total/30,2),dur=round(s['frames']/30,2)))
        for p in plist[i]: concat.append(p['out'])
        audf.write(seg_audio(s).tobytes());frames_total+=s['frames']
        if i+1<len(segs):
            n=s.get('tr',24) if True else 24
            n=segs[i+1].get('tr_in',n)
            a=f"{SEG}{part}_{i:03d}_la.png";b=f"{SEG}{part}_{i:03d}_fb.png";t=f"{SEG}{part}_{i:03d}_tr.mp4"
            if not os.path.exists(t):
                vid.last_frame(plist[i][-1]['out'],a);vid.first_frame(plist[i+1][0]['out'],b);vid.enc_trans(a,b,n,t)
            concat.append(t);audf.write(trans_audio(n).tobytes());frames_total+=n
    audf.close()
    with open(f'/tmp/w/build/{part}_concat.txt','w') as f:
        for c in concat: f.write(f"file '{c}'\n")
    json.dump(dict(total_frames=frames_total,items=tl),open(f'/tmp/w/build/{part}_timeline.json','w'),indent=1)
    return frames_total
def mux(part,out):
    subprocess.run(['ffmpeg','-v','error','-y','-f','concat','-safe','0','-i',f'/tmp/w/build/{part}_concat.txt','-f','s16le','-ar','48000','-ac','2','-i',f'/tmp/w/build/{part}.raw',
        '-c:v','copy','-c:a','aac','-b:a','192k','-ar','48000','-movflags','+faststart',out],check=True)
