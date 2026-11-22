import sys,json,os,subprocess,shutil
sys.path.insert(0,'/home/claude/prod')
from engine import *
from slides import *
_AUD={}
def get_sil(src):
    if src not in _AUD:
        x=audio16(src); _AUD[src]=(x,silenzi(x))
    return _AUD[src]
def build_piece(src,frasi,slides,T0,T1,outdir,tag,label,chips_default=()):
    """slides: [{'title':..,'chips':[..],'cards':[(t_src,html),..]}] in ordine; ciascuna slide dura dal t del suo 1o card fino al 1o card della successiva (T1 per l'ultima).
    T0/T1: estremi del pezzo (devono cadere in silenzio tra due frasi)."""
    os.makedirs(outdir,exist_ok=True)
    x,sil=get_sil(src)
    fine=[f['t1'] for f in frasi if T0<=f['t1']<=T1]
    keep=piano_tagli(sil,fine,T0,T1)
    # stati: (t_src_inizio, png)
    stati=[]
    with R() as r:
        for si,s in enumerate(slides):
            cards=[c[1] for c in s['cards']]
            for ci,(t,h) in enumerate(s['cards']):
                png=f"{outdir}/{tag}_s{si:02d}_{ci}.png"
                r.png(pagina(label,s['title'],cards,ci,s.get('chips',chips_default)),png)
                stati.append((max(t,T0) if (si==0 and ci==0) else t,png))
    stati[0]=(T0,stati[0][1])
    tot=sum(b-a for a,b in keep); NF=round(tot*30)
    fb=[round(mappa_t(keep,t)*30) for t,_ in stati]+[NF]
    parts=[]
    for i,(t,png) in enumerate(stati):
        n=fb[i+1]-fb[i]
        if n<=0: continue
        pf=f"{outdir}/{tag}_bg{i:03d}.mp4"
        subprocess.run(['ffmpeg','-v','error','-y','-loop','1','-framerate','30','-i',png,'-frames:v',str(n),'-c:v','libx264','-preset','ultrafast','-crf','16','-pix_fmt','yuv420p','-r','30',pf],check=True)
        parts.append(pf)
    lst=f"{outdir}/{tag}_bg.txt"
    open(lst,'w').write(''.join(f"file '{p}'\n" for p in parts))
    bgv=f"{outdir}/{tag}_bg.mp4"
    subprocess.run(['ffmpeg','-v','error','-y','-f','concat','-safe','0','-i',lst,'-c','copy',bgv],check=True)
    out=f"{outdir}/{tag}.mp4"
    dur=clip_prof(src,keep,bgv,out)
    json.dump({'keep':keep,'stati':[(t,mappa_t(keep,t)) for t,_ in stati],'durata':dur},open(f"{outdir}/{tag}.json",'w'))
    return dur,keep
