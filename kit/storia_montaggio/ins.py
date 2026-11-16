# Costruisce i pezzi "inserto" (voce Kore + scene) di una lezione.  uso: python3 ins.py 18
import sys,os,json,re,subprocess
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from scene import *
SND='/home/claude/v5/snd/'
def norm_voice(w,out):
    if os.path.exists(out):return out
    run(['ffmpeg','-y','-v','error','-i',w,'-af','loudnorm=I=-16:TP=-1.5:LRA=11,aresample=48000','-ac','2',out]);return out
def mix(parts,out):
    """parts=[(wav,delay_s,vol)] -> wav stereo 48k"""
    cmd=['ffmpeg','-y','-v','error'];fc=[]
    for i,(w,d,v) in enumerate(parts):
        cmd+=['-i',w];fc.append(f'[{i}:a]aresample=48000,volume={v},adelay={int(d*1000)}|{int(d*1000)}[a{i}]')
    fc.append(''.join(f'[a{i}]' for i in range(len(parts)))+f'amix=inputs={len(parts)}:normalize=0:duration=longest[o]')
    run(cmd+['-filter_complex',';'.join(fc),'-map','[o]','-ac','2',out]);return out
def sentences(text):
    return [s.strip() for s in re.split(r'(?<=[.?!])\s+',text.strip()) if s.strip()]
class Ctx:
    def __init__(s,tag,work,voxdir,texts,imgs):
        s.tag=tag;s.w=work;s.vox=voxdir;s.T=texts;s.imgs=imgs;s.S=Shooter()
        for d in ('png','pc','au'):os.makedirs(f'{work}/{d}',exist_ok=True)
    def voice(s,n):
        return norm_voice(f'{s.vox}/{n}.wav',f'{s.w}/au/{n}_n.wav')
    def png(s,key,h):
        p=f'{s.w}/png/{key}.png'
        if not os.path.exists(p):s.S.shot(h,p)
        return p
    def piece(s,name,states,audio_parts,total):
        out=f'{s.w}/pc/{name}.mp4'
        a=mix(audio_parts,f'{s.w}/au/{name}_mix.wav')
        T=still_video(states,out,audio=a,total=total);return out,T
LEAD=1.0;TAIL=0.7
def build_an(c,n,spec):
    v=c.voice(n);d=dur(v);cues=[it['cue'] for it in spec['items']]
    t=[LEAD+x for x in cue_times(c.T[n],d,cues)]
    total=LEAD+d+TAIL;states=[];k0=0
    ts=[0]+t+[total]
    for k in range(-1,len(spec['items'])):
        key=f'{c.tag}_{n}_{k}'
        h=an_html(spec,k,c.imgs) if k>=0 else page('Approfondimento · '+spec['kick'],spec['title'],'')
        states.append((c.png(key,h),ts[k+1+1]-ts[k+1]))
    return c.piece(n,states,[(SND+'trans.wav',0,0.5),(v,LEAD,1.0)],total)
def build_cap(c,n,kind,sub,sting='repaso.wav'):
    v=c.voice(n);d=dur(v);S=sentences(c.T[n])
    t=[LEAD+x for x in cue_times(c.T[n],d,S)];total=LEAD+d+TAIL;ts=[0]+t+[total]
    states=[]
    for i in range(len(ts)-1):
        cap=S[max(0,i-1)] if i>0 else ''
        seg=ts[i+1]-ts[i];ph=0;tt=0
        # alterna le fasi dell'onda ogni 0,4 s
        while tt<seg-1e-6:
            dd=min(0.4,seg-tt);key=f'{c.tag}_{n}_{i}_{ph%4}'
            states.append((c.png(key,ripasso_html(kind,sub,cap,ph%4)),dd));tt+=dd;ph+=1
    return c.piece(n,states,[(SND+sting,0,0.5),(v,LEAD,1.0)],total)
def build_gl(c,n):
    v=c.voice(n);d=dur(v);S=sentences(c.T[n])[2:] if False else sentences(c.T[n])
    S=[x for x in S if ':' in x]
    items=[(x.split(':',1)[0],x.split(':',1)[1].strip()) for x in S]
    t=[LEAD+x for x in cue_times(c.T[n],d,[x for x in S])];total=LEAD+d+TAIL;ts=[0]+t+[total]
    states=[]
    for k in range(-1,len(items)):
        h=glossario_html(items,k) if k>=0 else page('Parole chiave','Glossario','')
        states.append((c.png(f'{c.tag}_{n}_{k}',h),ts[k+1+1]-ts[k+1]))
    return c.piece(n,states,[(SND+'trans.wav',0,0.5),(v,LEAD,1.0)],total)
def fine_html(text,cap):
    return doc(f'''{logo(True)}<div class="abs kick" style="left:150px;top:330px">Storia · Quinto anno</div>
<h1 class="abs" style="left:150px;top:390px;font-size:140px">Per oggi è tutto</h1>
<div class="abs" style="left:150px;top:600px;width:180px;height:8px;background:var(--giallo);border-radius:6px"></div>
<div class="cap">{esc(cap)}</div>''','bg-d')
def build_fin(c,n):
    v=c.voice(n);d=dur(v);S=sentences(c.T[n]);total=LEAD+d+TAIL
    t=[LEAD+x for x in cue_times(c.T[n],d,S)];ts=[0]+t+[total];states=[]
    for i in range(len(ts)-1):
        states.append((c.png(f'{c.tag}_{n}_{i}',fine_html(None,S[i-1] if i>0 else '')),ts[i+1]-ts[i]))
    return c.piece(n,states,[(SND+'finale.wav',0,0.5),(v,LEAD,1.0)],total)
def build_intro(c,n,titolo,parte,args):
    v=c.voice(n);d=dur(v);total=LEAD+d+TAIL
    p=c.png(f'{c.tag}_{n}',intro_html(titolo,parte,args))
    return c.piece(n,[(p,total)],[(SND+'titolo.wav',0,0.6),(v,LEAD,1.0)],total)
def build_title(c,num,total_args,title,ex):
    p=c.png(f'{c.tag}_T{num}',title_html(num,total_args,title,ex))
    return c.piece(f'T{num}',[(p,5.0)],[(SND+'titolo.wav',0,0.7)],5.0)
def build_quiz(c,num,sub):
    p=c.png(f'{c.tag}_Q{num}',pausa_html('Pausa del video · Quiz',f'Quiz {num}',sub,"5 domande · per continuare almeno l'80%"))
    return c.piece(f'Q{num}',[(p,4.2)],[(SND+'quiz.wav',0.5,1.0)],4.2)
def build_pausa(c,name,kicker,big,sub,pill,sting,dur_s=5.0,delay=0.0):
    p=c.png(f'{c.tag}_{name}',pausa_html(kicker,big,sub,pill))
    return c.piece(name,[(p,dur_s)],[(SND+sting,delay,0.8)],dur_s)
