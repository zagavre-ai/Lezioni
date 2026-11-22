import sys,os,json,re,subprocess
sys.path.insert(0,'/home/claude/w/b')
from lib import *
from data import *
SEG=json.load(open(W+'/trasc.json'))
ORIG=W+'/mat/LEZIONE 7 GLI STATI UNITI DAL BOOM ECONOMICO AL NEW DEAL.mp4'
os.makedirs(B+'/pz4',exist_ok=True)
LEAD=0.30; TAIL=0.30; GAPMAX=2.5
def seg_range(t0,t1):
    return [i for i,s in enumerate(SEG) if s['inizio']>=t0-0.05 and s['fine']<=t1+0.05]
def noise(s):  # rumori trascritti da VAD che non sono parole del prof
    return s['testo'].strip().strip('.?!, ').lower() in ('um','yeah','you know','mm','mmm','sì','ah')
def intervals(t0,t1):
    ids=[i for i in seg_range(t0,t1) if not noise(SEG[i])]
    i0,i1=ids[0],ids[-1]
    prev_end=SEG[i0-1]['fine'] if i0>0 else -9; next_st=SEG[i1+1]['inizio'] if i1+1<len(SEG) else 9999
    a=SEG[i0]['inizio']-min(LEAD,max(0.05,(SEG[i0]['inizio']-prev_end)-0.1))
    b=SEG[i1]['fine']+min(TAIL,max(0.05,(next_st-SEG[i1]['fine'])-0.15))
    iv=[[a,b]]
    # accorcia pause > GAPMAX: tieni 0.5 s + 0.5 s
    out=[];cur=a
    seq=[SEG[i] for i in ids]
    for p,q in zip(seq,seq[1:]):
        g=q['inizio']-p['fine']
        if g>GAPMAX:
            out.append([cur,p['fine']+0.5]); cur=q['inizio']-0.5
    out.append([cur,b])
    return out,SEG[i1]
def piece_len(iv): return sum(y-x for x,y in iv)
def build_piece(name,t0,t1,states,cut_tail_report):
    """states: [(tempo_orig_inizio_stato, png)] ; il primo stato parte dall'inizio del pezzo"""
    iv,last=intervals(t0,t1); L=piece_len(iv)
    # mappa tempo originale -> tempo nel pezzo
    def tp(t):
        acc=0
        for x,y in iv:
            if t<=x: return acc
            if t<=y: return acc+(t-x)
            acc+=y-x
        return acc
    taus=[0.0]+[max(0.3,tp(t)) for t,_ in states[1:]]
    n=len(states)
    inp=[];fl=[]
    for k,(t,png) in enumerate(states):
        Lk=(taus[k+1]-taus[k]+0.25) if k<n-1 else (L-taus[k]+0.5)
        inp+=['-loop','1','-framerate','30','-t',f'{Lk:.3f}','-i',png]
    # webcam + audio
    vs=''.join(f"[0:v]trim={x:.3f}:{y:.3f},setpts=PTS-STARTPTS[v{j}];[0:a]atrim={x:.3f}:{y:.3f},asetpts=PTS-STARTPTS[a{j}];" for j,(x,y) in enumerate(iv))
    cc=''.join(f'[v{j}][a{j}]' for j in range(len(iv)))
    fg=vs+f"{cc}concat=n={len(iv)}:v=1:a=1[cv][ca];"
    fg+=f"[cv]crop=184:138:863:337,scale=412:309:flags=lanczos,unsharp=5:5:0.7:5:5:0,eq=contrast=1.03:saturation=1.05,format=yuva420p[cam0];[{n+1}:v]format=gray[msk];[cam0][msk]alphamerge[cam];"
    # catena xfade
    cur='[1:v]'
    for k in range(1,n):
        off=taus[k]-0.125
        fg+=f"{cur}[{k+1}:v]xfade=transition=fade:duration=0.25:offset={off:.3f}[x{k}];"; cur=f'[x{k}]'
    if n==1: cur='[1:v]'
    fg+=f"{cur}format=yuv420p[sl];[sl][cam]overlay=1428:148:format=auto,trim=duration={L:.3f},fade=t=in:st=0:d=0.3:color=white,fade=t=out:st={L-0.3:.3f}:d=0.3:color=white[vo];"
    fg+=f"[ca]highpass=f=70,afftdn=nr=5:nf=-50,volume=VOLGAIN,alimiter=limit=0.84:attack=3:release=40:level=0,atrim=duration={L:.3f},afade=t=in:st=0:d=0.03,afade=t=out:st={L-0.03:.3f}:d=0.03[ao]"
    # n+1 e' l'indice della maschera: la mettiamo come ultimo input
    return dict(name=name,iv=iv,L=L,inp=inp,fg=fg,last=last,n=n,taus=taus)

MASK=B+'/mask.png'
GAIN=os.environ.get('VOLGAIN','2.2')
def sub_events():
    ev=[]
    for n,(arg,ci,t0,anc) in enumerate(SUB):
        lit0=0 if abs(anc[0]-t0)<0.01 else None
        ev.append((t0,f'{B}/st/s{n:02d}_{"n" if lit0 is None else lit0}.png'))
        for k,a in enumerate(anc):
            if k==0 and lit0==0: continue
            ev.append((a,f'{B}/st/s{n:02d}_{k}.png'))
    ev.sort(); return ev
def states_for(t0,t1):
    ev=sub_events(); cur=None
    for t,p in ev:
        if t<=t0+0.01: cur=p
    st=[(t0,cur)]+[(t,p) for t,p in ev if t0+0.01<t<t1-0.5]
    return st
def run_piece(name,t0,t1,force=False,states=None):
    out=f'{B}/pz4/{name}.mkv'
    if os.path.exists(out+'.ok') and not force: return out
    P=build_piece(name,t0,t1,states or states_for(t0,t1),None)
    L=P['L']
    cmd=['ffmpeg','-y','-v','error','-i',ORIG]+P['inp']+['-loop','1','-framerate','30','-t',f'{L+1:.2f}','-i',MASK,
        '-filter_complex',P['fg'].replace('VOLGAIN',GAIN),'-map','[vo]','-map','[ao]','-c:v','libx264','-preset','veryfast','-crf','14','-pix_fmt','yuv420p','-r','30','-c:a','pcm_s16le','-ar','48000','-ac','2',out]
    r=subprocess.run(cmd,capture_output=True,text=True)
    if r.returncode: raise SystemExit(name+': '+r.stderr[-1500:])
    open(out+'.ok','w').write('1')
    json.dump(dict(name=name,t0=t0,t1=t1,L=L,iv=P['iv'],last=P['last']['testo'],lastend=P['last']['fine']),open(out+'.json','w'))
    return out
def piano():
    """elenco pezzi del prof: (nome, t0, t1) per argomento, spezzati dove entrano gli approfondimenti"""
    pz=[]
    for a in range(1,6):
        s,e=ARGT[a]; cuts=[t for _,t in AN[a]]
        bounds=[s]+cuts+[e]; k=0
        for i in range(len(bounds)-1):
            lo=bounds[i]+(0.001 if i>0 else 0); hi=bounds[i+1]
            pz.append((f'P{a}_{i}',lo,hi))
    return pz
if __name__=='__main__':
    import time
    sel=sys.argv[1:] 
    for n,t0,t1 in piano():
        if sel and n not in sel: continue
        t=time.time(); f=run_piece(n,t0,t1); print(n,round(dur(f),1),round(time.time()-t),'s',flush=True)

def run_intro():
    sys.path.insert(0,'/home/claude/w/b')
    from scenes import cover_html
    pg=page(); pngs=[]
    for k,hl in enumerate([None,0,1,2]):
        pg.set_content(cover_html(True,anim=False,hl=hl)); pg.wait_for_timeout(300); pg.evaluate('render(9)'); f=f'{B}/st/cover_prof{k}.png'; pg.screenshot(path=f); pngs.append(f)
    return run_piece('P0',0.9,170.9,states=[(0.9,pngs[0]),(55.0,pngs[1]),(100.0,pngs[2]),(140.0,pngs[3])])
