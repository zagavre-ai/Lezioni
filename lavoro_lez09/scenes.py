# Scene con la voce Kore (approfondimenti, ripassi, mappe, glossario, titoli, quiz...). Voci mancanti = segnaposto di silenzio con durata stimata.
import os,re,json,subprocess,sys,numpy as np
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from prof import *
from PIL import Image
from cifre import cifre
REPO='/home/user/Lezioni'
VOXDIRS=[REPO+'/scambio/storia-V-lez09/vox','/home/user/Lezioni/w/vox_old']
TESTI={x['nome']:x['testo'] for x in json.load(open(REPO+'/scambio/storia-V-lez09/testi_voci.json'))}
PROV=W+'/vox_prov';os.makedirs(PROV,exist_ok=True)
def dur(p):return float(subprocess.run(['ffprobe','-v','error','-show_entries','format=duration','-of','csv=p=0',p],capture_output=True,text=True).stdout)
def voce(nome):
    """(percorso, e_reale)"""
    for d in VOXDIRS:
        p=f'{d}/{nome}.wav'
        if os.path.exists(p):return p,True
    t=TESTI[nome];d=max(1.5,len(t.split())*0.40);p=f'{PROV}/{nome}.wav'
    if not os.path.exists(p):subprocess.run(['ffmpeg','-v','error','-y','-f','lavfi','-i',f'anullsrc=r=24000:cl=mono','-t',f'{d:.2f}',p],check=True)
    return p,False
NAVY_CSS='''html,body{background:linear-gradient(135deg,#0B1530 0%,#14306A 60%,#1B4A9A 100%)!important;color:#fff!important}
#logo svg path{fill:#fff!important}#hl,#fl{background:rgba(255,255,255,.25)!important}#foot,#pag,#kick{color:#BFD3F2!important}#tit{color:#fff!important}'''
def hdoc(inner,kicker='',title='',bar=None,pag='',dark=False,foot='STORIA V',tit_size=None,cam=False,nome='Giorgio Mazzotti'):
    h=G.doc(inner,kicker,title,bar if bar is not None else 182+int(58*1.08*(1 if len(title)<40 else 2))+14,pag,cam,None,foot)
    if dark:h=h.replace('</style>',NAVY_CSS+'</style>')
    if pag=='' :h=h.replace('<div id="pag">Pagina </div>','')
    return h
def card1(t,on=False,dark=False,n=None):
    return f'<div class="card {"on" if on else ""}">{"<span class=n>%d</span>"%n if n else ""}{G.esc(t)}</div>'
def blend(a,b,n,dirp,tag):
    A=np.asarray(Image.open(a).convert('RGB'),np.float32);B=np.asarray(Image.open(b).convert('RGB'),np.float32);L=[]
    for i in range(1,n+1):
        al=i/(n+1);im=Image.fromarray((A*(1-al)+B*al).astype(np.uint8));p=f'{dirp}/{tag}_b{i}.png';im.save(p,compress_level=1);L.append(p)
    return L
SWEEP=W+'/sweep.png'
if not os.path.exists(SWEEP):
    g=np.zeros((1080,500,4),np.uint8);x=np.linspace(0,np.pi,500);a=(np.sin(x)**2*26).astype(np.uint8)
    g[...,:3]=255;g[...,3]=a[None,:];Image.fromarray(g,'RGBA').save(SWEEP)
def kore(name,states,out,prev=None,trans=True,jingle=None,anim=False,lead=1.1,tail=1.2,gap=0.45,pre=0.12):
    """states: lista di dict(html, voce=nome|None, hold=secondi se senza voce, jingle=(wav,offset))"""
    d=W+f'/k_{name}';os.makedirs(d,exist_ok=True);t=lead;ev=[];aud=[];pngs=[];vstart=lead
    with G.R() as r:
        for i,s in enumerate(states):
            p=f'{d}/s{i:02d}.png';r.shot(s['html'],p);pngs.append(p)
            st=t
            if 'rel' in s:
                st=vstart+s['rel']
            elif s.get('voce'):
                w,real=voce(s['voce']);dd=dur(w);aud.append((st,w));vstart=st;t=st+dd+gap
            else:t=st+s.get('hold',3.0)
            if s.get('jingle'):aud.append((st+s['jingle'][1],s['jingle'][0]))
            ev.append((max(st-pre,0 if i==0 else st-pre),i))
    tot=t-gap+tail
    L=[];prevp=None;tl=[]
    for k,(tt,i) in enumerate(ev):
        tl.append((0.0 if k==0 else tt,pngs[i]))
    seq=[]
    for k,(tt,p) in enumerate(tl):
        end=tl[k+1][0] if k+1<len(tl) else tot
        if k>0:
            bl=blend(tl[k-1][1],p,6,d,f'x{k}');seq+= [(q,1/30) for q in bl];start=tt+6/30
        else:start=tt
        seq.append((p,max(end-start,1/30)))
    lst=d+'/c.txt';open(lst,'w').write('\n'.join(f"file '{p}'\nduration {du:.4f}" for p,du in seq)+f"\nfile '{seq[-1][0]}'")
    base=d+'/base.mkv'
    vf='fps=30,format=yuv420p'
    if anim:
        subprocess.run(['ffmpeg','-v','error','-y','-f','concat','-safe','0','-i',lst,'-loop','1','-framerate','30','-t',f'{tot:.2f}','-i',SWEEP,'-filter_complex',"[0:v]fps=30,format=rgba[a];[1:v]format=rgba[s];[a][s]overlay=x='mod(t*230,2900)-600':y=0:shortest=1,format=yuv420p[o]",'-map','[o]','-t',f'{tot:.3f}','-c:v','libx264','-preset','ultrafast','-crf','12',base],check=True)
    else:
        subprocess.run(['ffmpeg','-v','error','-y','-f','concat','-safe','0','-i',lst,'-vf',vf,'-t',f'{tot:.3f}','-c:v','libx264','-preset','ultrafast','-crf','12',base],check=True)
    # audio
    ins=[];fl=[];lab=[]
    k=0
    if trans:aud.append((0.0,KIT+'/suoni/trans.wav'))
    for (st,w) in aud:
        ins+=['-i',w];ms=int(st*1000)
        g=',volume=0.5' if w.endswith('trans.wav') else ''
        fl.append(f"[{k+1 if prev else k+1}:a]aformat=channel_layouts=stereo,aresample=48000{g},adelay={ms}|{ms}[x{k}]");lab.append(f'[x{k}]');k+=1
    return d,base,aud,tot,ins,fl,lab
def finish(base,tot,aud,out,prev=None):
    ins=[];fl=[];lab=[]
    cmd=['ffmpeg','-v','error','-y','-i',base]
    n=1
    if prev:cmd+=['-loop','1','-framerate','30','-t','0.6','-i',prev];n=2
    for k,(st,w) in enumerate(aud):
        cmd+=['-i',w];ms=int(st*1000);g=',volume=0.5,atrim=0:1.05,afade=t=out:st=0.45:d=0.6' if w.endswith('trans.wav') else ''
        fl.append(f"[{n+k}:a]aformat=channel_layouts=stereo,aresample=48000{g},adelay={ms}|{ms}[x{k}]");lab.append(f'[x{k}]')
    fl.append(''.join(lab)+f"amix=inputs={len(lab)}:duration=longest:normalize=0,apad,atrim=0:{tot:.3f}[ao]")
    if prev:fl.append("[1:v]format=rgba[pv];[0:v]format=rgba,fade=t=in:st=0:d=0.5:alpha=1[vf];[pv][vf]overlay=shortest=1:format=auto,format=yuv420p[vo]")
    else:fl.append("[0:v]null[vo]")
    cmd+=['-filter_complex',';'.join(fl),'-map','[vo]','-map','[ao]','-t',f'{tot:.3f}','-c:v','libx264','-preset','veryfast','-crf','16','-pix_fmt','yuv420p','-r','30','-c:a','pcm_s16le','-ar','48000',out]
    subprocess.run(cmd,check=True)
def piece(name,states,out,prev=None,trans=True,jingle=None,anim=False,**kw):
    d,base,aud,tot,_,_,_=kore(name,states,out,prev,trans,jingle,anim,**kw)
    if jingle:aud.append((jingle[1],jingle[0]))
    finish(base,tot,aud,out,prev)
    json.dump([(round(st,3),os.path.basename(w)[:-4]) for st,w in aud if '/vox' in w or 'vox_prov' in w],open(out+'.ev.json','w'))
    return tot
