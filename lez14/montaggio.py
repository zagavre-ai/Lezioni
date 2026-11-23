import sys,os,json,subprocess,re,hashlib,shutil
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from lib import *;import slide as S
from PIL import Image
ORIG=W+'/orig.mp4';WK=W+'/wk';os.makedirs(WK,exist_ok=True)
SEG=json.load(open(W+'/asr/orig.json'));P=parole()
SL=json.load(open(W+'/slides.json'))
FPS=30
def sh(cmd,**k):
    r=subprocess.run(cmd,shell=isinstance(cmd,str),capture_output=True,text=True,**k)
    if r.returncode:raise RuntimeError(cmd if isinstance(cmd,str) else ' '.join(cmd)+'\n'+r.stderr[-1500:])
    return r
def fr(t):return round(t*FPS)/FPS
# ---------- silenzi dell'originale
def silenzi():
    f=W+'/silenzi.json'
    if not os.path.exists(f):
        r=subprocess.run(['ffmpeg','-i',ORIG,'-af','silencedetect=n=-38dB:d=1.0','-f','null','-'],capture_output=True,text=True).stderr
        a=[float(x) for x in re.findall(r'silence_start: ([\d.]+)',r)];b=[float(x) for x in re.findall(r'silence_end: ([\d.]+)',r)]
        json.dump(list(zip(a,b)),open(f,'w'))
    return json.load(open(f))
# ---------- confini di frase
def confine(T,cerca=25):
    """tempo (in silenzio, 0,15 s prima della frase che segue) del confine di frase piu' vicino a T"""
    best=None
    for i in range(1,len(SEG)):
        prev=SEG[i-1];cur=SEG[i]
        pt=prev['testo'].strip()
        if not re.search(r'[.?!…]["»]?\s*$',pt) or re.search(r'(\.\.\.|…)["»]?\s*$',pt):continue   # «qualcosa...» = frase lasciata a meta
        gap=cur['inizio']-prev['fine']
        if gap<0.25:continue
        c=cur['inizio']-0.15
        d=abs(c-T)
        if d<=cerca and (best is None or d<best[0]):best=(d,c,i,prev['fine'])
    if not best:raise RuntimeError('nessun confine vicino a %s'%T)
    return fr(best[1]),best[2]
def fine_pezzo(c):
    """c = inizio frase seguente - 0,15: fine pezzo = ultima parola + 0,4 s al massimo, dentro il silenzio"""
    return c
def keep(a,b,tag=''):
    """intervalli da tenere in [a,b]: pause > 2,5 s accorciate a ~1 s (taglio dentro il silenzio)"""
    out=[];cur=a
    for s,e in silenzi():
        if e<=a or s>=b:continue
        s=max(s,a);e=min(e,b)
        if e-s>2.5:
            k1=fr(s+0.5);k2=fr(e-0.5)
            if k2>k1:out.append((cur,k1));cur=k2
    out.append((cur,b));return [(fr(x),fr(y)) for x,y in out if y>x]
def tmap(K):
    """mappa tempo originale -> tempo montato"""
    acc=0;m=[]
    for a,b in K:m.append((a,b,acc));acc+=b-a
    def f(t):
        for a,b,o in m:
            if t<=b:return o+max(0,t-a)
        return acc
    return f,acc

# ---------- immagini del prof (dal suo PDF), migliorate
def migliora(nome):
    out=f'{WK}/{nome}_hq.png'
    if os.path.exists(out):return out
    im=Image.open(f'{W}/img/{nome}').convert('RGB')
    from PIL import ImageFilter
    im=im.filter(ImageFilter.GaussianBlur(0.5)).resize((im.width*3,im.height*3),Image.LANCZOS).filter(ImageFilter.UnsharpMask(3,90,2))
    im.save(out);return out
def base_img(kick,caption,pag):
    h=f'{WK}/base2_{hashlib.md5((kick+caption+str(pag)).encode()).hexdigest()[:8]}.html'
    open(h,'w').write(S.page(kick,caption,[],[],None,None,pag,[]).replace('<div id=cards','<div id=cards style=display:none') )
    return h
def png_di(h,force=False):
    o=h[:-5]+'.png';shots([{'html':h,'out':o}],'job_'+os.path.basename(h));return o

def stati_argomento(n,A,B,K):
    """eventi di stato sulla linea del tempo montato: [(t_montato, chiave)]
    chiave = ('c',pagina,finestra,attiva,clausola,zoom) o ('i',nome,durata)"""
    import spec
    t_ed,_=tmap(K);ev=[]
    for sc in spec.ARG[n][3]:
        t0=max(sc[3] if sc[0]=='c' else sc[2],A);t1=min(sc[4] if sc[0]=='c' else sc[3],B)
        if t1<=t0:continue
        if sc[0]=='i':ev.append((t_ed(t0),('i',sc[1],t_ed(t1)-t_ed(t0))));continue
        _,pg,idx,_,_,sched=sc;pars=SL[pg]['par'];wins=S.finestre([pars[i] for i in idx],SL[pg]['titolo'])
        win_of={}
        for w in wins:
            for c in w:win_of[idx[c]]=tuple(idx[x] for x in w)
        sched=[(max(t,t0) if i==0 else t,c) for i,(t,c) in enumerate(sched)]
        sched[0]=(t0,sched[0][1])
        for i,(t,c) in enumerate(sched):
            te=sched[i+1][0] if i+1<len(sched) else t1
            if c is None:
                ev.append((t_ed(t),('c',pg,win_of[idx[0]] if i==0 else prev_win,None,None,0)));continue
            lead,cl=S.clausole(pars[c])
            if len(cl)>1:
                tt,_=allinea(cl,P,t,te);tt=[t]+[max(t,x) for x in tt[1:]]
                # clausole troppo vicine: nessuna sotto-evidenziazione
                tt=[x for k2,x in enumerate(tt)]
            else:tt=[t]
            prev_win=win_of[c]
            for j,tj in enumerate(tt):ev.append((t_ed(tj),('c',pg,win_of[c],c,j,0)))
    ev.sort(key=lambda x:x[0])
    # variante zoom: stati card lunghi > 80 s alternano normale/zoom ogni 40 s
    out=[];N=len(ev);tot=t_ed(1e9)
    for i,(t,k) in enumerate(ev):
        te=ev[i+1][0] if i+1<N else tot
        out.append((t,k))
        if k[0]=='c' and k[3] is not None and te-t>80:
            u=t+40;z=1
            while te-u>20:
                out.append((u,k[:5]+(z,)));z=1-z;u+=40
    return out

# ---------- costruzione del livello slide e composizione del pezzo docente
FAD=6  # fotogrammi di dissolvenza tra stati
def pagina_card(kick,titolo,pg,win,att,cla,zoom=0,pag=None):
    pars=SL[pg]['par']
    h=f'{WK}/c2_{pg}_{"".join(map(str,win))}_{att}_{cla}_{zoom}.html'
    open(h,'w').write(S.page(kick,titolo,pars,list(win),att,cla,pag,KEYS_[pg],zoom=zoom))
    return h
def costruisci_D(n,A,B,nome=None,pezzi_extra=None):
    """A,B: tempi originali (gia' sui confini di frase). Produce WK/D{n}.mkv e ritorna info."""
    import spec;global KEYS_,PAGINA_;KEYS_=spec.KEYS;PAGINA_=spec.PAGINA
    titolo_arg=spec.ARG[n][0]
    K=keep(A,B);t_ed,tot=tmap(K);nf=round(tot*FPS)
    ev=stati_argomento(n,A,B,K)
    kick=f'Argomento {n} · {titolo_arg}'
    num,_=spec.numeri_pagina();parte=1 if n<=3 else 2
    # frame di inizio di ogni stato
    stati=[(round(t*FPS),k) for t,k in ev];stati[0]=(0,stati[0][1])
    # rimuovi duplicati consecutivi
    ded=[];
    for f,k in stati:
        if ded and ded[-1][1]==k:continue
        if ded and f<=ded[-1][0]:ded[-1]=(ded[-1][0],k);continue
        ded.append((f,k))
    stati=ded
    # render pagine card
    jobs=[];pagine={}
    for f,k in stati:
        if k[0]=='c':
            h=pagina_card(kick,SL[k[1]]['titolo'],k[1],k[2],k[3],k[4],k[5],num[(parte,('c',k[1],tuple(k[2])))]);o=h[:-5]+'.png';pagine[k]=o;jobs.append({'html':h,'out':o})
        else:
            cap=spec.IMG[k[1]][1];h=base_img(kick,cap,num[(parte,('i',k[1]))]);o=h[:-5]+'.png';pagine[k]=o;jobs.append({'html':h,'out':o})
    shots(jobs,f'jobsD{n}')
    # clip per run: card consecutive -> un clip; immagine -> un clip
    clips=[];i=0;N=len(stati)
    ends=[stati[j+1][0] for j in range(N-1)]+[nf]
    runs=[]
    for j,(f,k) in enumerate(stati):
        if runs and runs[-1]['tipo']==k[0]=='c':runs[-1]['st'].append((f,ends[j],k))
        else:runs.append({'tipo':k[0],'st':[(f,ends[j],k)]})
    for ri,r in enumerate(runs):
        f0=r['st'][0][0];f1=r['st'][-1][1];out=f'{WK}/D{n}_r{ri}.mp4'
        fin=ri>0;fout=ri<len(runs)-1
        vf=['fps=30','format=yuv420p']
        if r['tipo']=='c':
            # elenco frame
            frames=[]
            prev=None
            for (a,b,k) in r['st']:
                cur=pagine[k]
                for q in range(a,b):
                    if prev and q-a<FAD and b-a>2*FAD:
                        frames.append(blend(prev,cur,(q-a+1)/(FAD+1)))
                    else:frames.append(cur)
                prev=cur
            lst=f'{WK}/D{n}_r{ri}.txt';agg=[]
            for p in frames:
                if agg and agg[-1][0]==p:agg[-1][1]+=1
                else:agg.append([p,1])
            with open(lst,'w') as L:
                for p,c in agg:L.write(f"file '{p}'\nduration {c/FPS:.6f}\n")
                L.write(f"file '{agg[-1][0]}'\n")
            nfr=f1-f0
            if fin:vf.append(f'fade=t=in:st=0:d={FAD/FPS}:color=white')
            if fout:vf.append(f'fade=t=out:st={(nfr-FAD)/FPS}:d={FAD/FPS}:color=white')
            sh(['ffmpeg','-v','error','-y','-f','concat','-safe','0','-i',lst,'-vf',','.join(vf),'-frames:v',str(nfr),'-r','30','-c:v','libx264','-preset','ultrafast','-crf','12','-an',out])
        else:
            k=r['st'][0][2];nfr=f1-f0;img=migliora(spec.IMG[k[1]][0])
            im=Image.open(img);fw,fh=1305,640
            sc=min(fw/im.width,fh/im.height);w2,h2=int(im.width*sc*1.0),int(im.height*sc*1.0)
            vf2=f"[1:v]scale={int(w2*2)}:{int(h2*2)}:flags=lanczos,zoompan=z='1+0.00008*on':x='(iw-iw/zoom)/2':y='(ih-ih/zoom)/2':d=1:s={w2}x{h2}:fps=30[z];[0:v][z]overlay={80+(fw-w2)//2}:{300+(fh-h2)//2},fps=30,format=yuv420p"
            if fin:vf2+=f',fade=t=in:st=0:d={FAD/FPS}:color=white'
            if fout:vf2+=f',fade=t=out:st={(nfr-FAD)/FPS}:d={FAD/FPS}:color=white'
            sh(['ffmpeg','-v','error','-y','-loop','1','-framerate','30','-i',pagine[k],'-loop','1','-framerate','30','-i',img,'-filter_complex',vf2,'-frames:v',str(nfr),'-c:v','libx264','-preset','ultrafast','-crf','12','-an',out])
        clips.append(out)
    lst=f'{WK}/D{n}_layer.txt';open(lst,'w').write(''.join(f"file '{c}'\n" for c in clips))
    layer=f'{WK}/D{n}_layer.mp4';sh(['ffmpeg','-v','error','-y','-f','concat','-safe','0','-i',lst,'-c','copy',layer])
    return dict(K=K,layer=layer,nf=nf,stati=stati,tot=tot)
def blend(a,b,x):
    o=f'{WK}/bl_{hashlib.md5((a+b+str(round(x,2))).encode()).hexdigest()[:10]}.png'
    if not os.path.exists(o):Image.blend(Image.open(a).convert('RGB'),Image.open(b).convert('RGB'),x).save(o)
    return o

def maschera():
    o=f'{WK}/mask_cam.png'
    if not os.path.exists(o):
        from PIL import ImageDraw
        m=Image.new('L',(412,309),0);ImageDraw.Draw(m).rounded_rectangle((0,0,411,308),radius=18,fill=255);m.save(o)
    return o
CAM=(862,343,184,138)
AFILT='highpass=f=70,afftdn=nr=6:nf=-50:tn=0'
def componi_D(info,out,cam=True,audio_filter=AFILT):
    K=info['K'];A=K[0][0];off=A-1.0
    fc=[];vi=[];ai=[]
    for i,(a,b) in enumerate(K):
        fc.append(f'[1:v]trim=start={a-off:.4f}:end={b-off:.4f},setpts=PTS-STARTPTS,crop={CAM[2]}:{CAM[3]}:{CAM[0]}:{CAM[1]}[v{i}]')
        d=b-a;fc.append(f'[1:a]atrim=start={a-off:.4f}:end={b-off:.4f},asetpts=PTS-STARTPTS,afade=t=in:d=0.02,afade=t=out:st={max(0,d-0.02):.4f}:d=0.02[a{i}]')
        vi.append(f'[v{i}]');ai.append(f'[a{i}]')
    fc.append(''.join(vi)+f'concat=n={len(K)}:v=1:a=0,scale=412:309:flags=lanczos,eq=contrast=1.04:saturation=1.06,format=gray,format=rgb24[cm0]' if False else ''.join(vi)+f'concat=n={len(K)}:v=1:a=0,scale=412:309:flags=lanczos,eq=contrast=1.04:saturation=1.06,format=rgba[cm0]')
    fc.append('[cm0][2:v]alphamerge[cm]')
    fc.append(''.join(ai)+f'concat=n={len(K)}:v=0:a=1,aresample=48000,{audio_filter},pan=stereo|c0=c0|c1=c0[aud]')
    fc.append('[0:v][cm]overlay=1428:148:shortest=1,format=yuv420p[vid]')
    sh(['ffmpeg','-v','error','-y','-i',info['layer'],'-ss',f'{max(0,off):.3f}','-i',ORIG,'-loop','1','-framerate','30','-i',maschera(),'-filter_complex',';'.join(fc),'-map','[vid]','-map','[aud]','-frames:v',str(info['nf']),'-c:v','libx264','-preset','veryfast','-crf','16','-c:a','pcm_s16le','-ar','48000',out])
    return out
