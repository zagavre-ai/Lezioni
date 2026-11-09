# Montaggio Inglese Lez1 «Global Factors» · una Parte · tagli solo nelle pause della docente (>1,0 s → 0,6 s, dissolvenza 0,2 s)
# Struttura: sigla · INTRO1 · D0 · per ogni argomento: T · D · S (ripasso con voce) · Q · GL1 · RF1 · FIN1 · sigla finale
# SOLOLISTA=1 → scrive solo la lista dei pezzi (per tools/finale_a_pezzi.py), PIANO=1 → stima la durata
import json,os,subprocess,sys
D='/home/claude/lezioni/afm-inglese-triennio-lez01/';W=D+'w2/';os.makedirs(W,exist_ok=True)
VID=D+'docente_slide_1080.mp4';AUD=D+'audio/audio_B_full.wav'
SND='/home/claude/v5/snd/%s.wav'
ENC=['-c:v','libx264','-preset','veryfast','-crf','16','-pix_fmt','yuv420p','-r','30','-g','60']
AP=['-c:a','pcm_s16le','-ar','48000','-ac','2']
LT=1.3;XF=0.2;FPS=30
def run(c): subprocess.run(c,check=True)
def dur(f): return float(subprocess.run(['ffprobe','-v','error','-show_entries','format=duration','-of','csv=p=0',f],capture_output=True,text=True).stdout)
sys.path.insert(0,'/home/claude/lezioni/tools');import taglio
def fr(t): return round(t*FPS)/FPS
def cut(t): return fr(taglio.snap(t-0.15,AUD))
K=json.load(open(D+'tenuti.json'))  # tratti tenuti (pause lunghe accorciate), tempi della lezione originale
def pieces(a,b):
    P=[[fr(max(a,x)),fr(min(b,y))] for x,y in K if y>a+0.05 and x<b-0.05]
    return [p for p in P if p[1]-p[0]>=0.1]
def chunk(name,P,first,last):
    """P = tratti consecutivi; dissolvenza XF tra un tratto e l'altro (video e audio); LT fermi in testa/coda solo a inizio/fine"""
    o=W+name+'.mkv'
    if os.path.exists(o): return o
    c0,c1=P[0][0],P[-1][1];n=len(P)
    fl=f'[0:v]fps={FPS},format=yuv420p,split={n}'+''.join(f'[v{i}]' for i in range(n))+f';[1:a]aformat=channel_layouts=stereo,aresample=48000,asplit={n}'+''.join(f'[a{i}]' for i in range(n))
    for i,(x,y) in enumerate(P):
        fl+=f';[v{i}]trim=start={x-c0:.4f}:end={y-c0:.4f},setpts=PTS-STARTPTS[V{i}];[a{i}]atrim=start={x-c0:.4f}:end={y-c0:.4f},asetpts=PTS-STARTPTS[A{i}]'
    lv,la,L='V0','A0',P[0][1]-P[0][0]
    for i in range(1,n):
        d=P[i][1]-P[i][0];x=max(1/FPS,fr(min(XF,d/2,L/2)))
        fl+=f';[{lv}][V{i}]xfade=transition=fade:duration={x:.3f}:offset={L-x:.4f}[XV{i}];[{la}][A{i}]acrossfade=d={x:.3f}[XA{i}]'
        lv,la=f'XV{i}',f'XA{i}';L=L+d-x
    pv=f'tpad=start_mode=clone:start_duration={LT if first else 0}:stop_mode=clone:stop_duration={LT if last else 0}'
    pa=(f'adelay={int(LT*1000)}|{int(LT*1000)},' if first else '')+(f'apad=pad_dur={LT},' if last else '')+'anull'
    fl+=f';[{lv}]{pv},format=yuv420p[v];[{la}]{pa}[a]'
    T=L+(LT if first else 0)+(LT if last else 0)
    run(['ffmpeg','-y','-v','error','-ss','%.3f'%c0,'-t','%.3f'%(c1-c0+0.1),'-i',VID,'-ss','%.3f'%c0,'-t','%.3f'%(c1-c0+0.1),'-i',AUD,'-filter_complex',fl,
         '-map','[v]','-map','[a]','-t','%.4f'%T]+ENC+AP+[o]);return o
def pad(name,src,last):
    """LT secondi fermi (primo o ultimo fotogramma) + silenzio, per le transizioni"""
    o=W+name+'.mkv'
    if os.path.exists(o): return o
    png=W+name+'.png'
    run(['ffmpeg','-y','-v','error']+(['-sseof','-0.2'] if last else [])+['-i',src]+(['-update','1'] if last else ['-frames:v','1'])+[png])
    run(['ffmpeg','-y','-v','error','-loop','1','-framerate','30','-i',png,'-f','lavfi','-i','anullsrc=r=48000:cl=stereo','-t','%.4f'%LT,'-map','0:v','-map','1:a']+ENC+AP+[o]);return o
def doc(name,a,b,maxp=24):
    """parte della docente [a,b] della lezione originale, pause lunghe accorciate.
    Scrive anche b_<name>.mkv (corpo senza i fermi) unendo i pezzi senza ricomprimere."""
    o=W+name+'.mkv'
    if os.path.exists(o): return o
    P=pieces(a,b);G=[];cur=[]
    for p in P:
        cur.append(list(p))
        if len(cur)>=maxp:
            x,y=cur[-1];m=fr((x+y)/2)
            if y-x>0.6: cur[-1][1]=m;G.append(cur);cur=[[m,y]]
    if cur: G.append(cur)
    fs=[chunk(f'{name}_c{k:02d}',g,False,False) for k,g in enumerate(G)]
    h=pad(name+'_h',fs[0],False);t=pad(name+'_t',fs[-1],True)
    open(W+'b_'+name+'.txt','w').write(''.join("file '%s'\n"%f for f in fs))
    run(['ffmpeg','-y','-v','error','-f','concat','-safe','0','-i',W+'b_'+name+'.txt','-c','copy',W+'b_'+name+'.mkv'])
    open(o+'.txt','w').write(''.join("file '%s'\n"%f for f in [h]+fs+[t]))
    run(['ffmpeg','-y','-v','error','-f','concat','-safe','0','-i',o+'.txt','-c','copy',o]);return o
def mix_clip(name,vid,jingle=None,joff=0.4,voice=None,voff=0.9,bed=False,minlen=None):
    o=W+name+'.mkv'
    if os.path.exists(o): return o
    dv=dur(vid);L=dv
    if voice and os.path.exists(voice): L=max(L,voff+dur(voice)+0.8)
    if minlen: L=max(L,minlen)
    tot=L+2*LT
    ins=['-i',vid,'-f','lavfi','-t','%.3f'%tot,'-i','anullsrc=r=48000:cl=stereo'];fl=f'[0:v]fps=30,scale=1920:1080,setsar=1,tpad=start_mode=clone:start_duration={LT}:stop_mode=clone:stop_duration={LT+L-dv:.3f},format=yuv420p[v];[1:a]anull[b0]';lab=['b0'];k=2
    if jingle:
        ins+=['-i',SND%jingle];fl+=f';[{k}:a]aformat=channel_layouts=stereo,aresample=48000,adelay={int((LT+joff)*1000)}|{int((LT+joff)*1000)},volume={0.55 if voice else 0.9}[b{k}]';lab.append(f'b{k}');k+=1
    if voice and os.path.exists(voice):
        ins+=['-i',voice];fl+=f';[{k}:a]loudnorm=I=-16:TP=-1.5,aresample=48000,aformat=channel_layouts=stereo,adelay={int((LT+voff)*1000)}|{int((LT+voff)*1000)}[b{k}]';lab.append(f'b{k}');k+=1
    if bed:
        ins+=['-i',D+'audio/bed.wav'];fl+=f';[{k}:a]atrim=0:{L:.3f},afade=t=in:d=1.2,afade=t=out:st={L-1.5:.3f}:d=1.5,aformat=channel_layouts=stereo,aresample=48000,adelay={int(LT*1000)}|{int(LT*1000)}[b{k}]';lab.append(f'b{k}');k+=1
    fl+=';'+''.join(f'[{l}]' for l in lab)+f'amix=inputs={len(lab)}:normalize=0:duration=first[a]'
    run(['ffmpeg','-y','-v','error']+ins+['-filter_complex',fl,'-map','[v]','-map','[a]','-t','%.3f'%tot]+ENC+AP+[o]);return o
def still(name,png,voice,delay=0.8,jingle=None):
    o=W+name+'.mkv'
    if os.path.exists(o): return o
    L=dur(voice)+delay+0.8+2*LT
    ins=['-loop','1','-framerate','30','-i',png,'-i',voice];fl=f'[0:v]format=yuv420p,zoompan=z=\'1+0.00012*on\':d=1:x=\'iw/2-(iw/zoom/2)\':y=\'ih/2-(ih/zoom/2)\':s=1920x1080:fps=30[v];[1:a]loudnorm=I=-16:TP=-1.5,aresample=48000,aformat=channel_layouts=stereo,adelay={int((LT+delay)*1000)}|{int((LT+delay)*1000)},apad[a]'
    run(['ffmpeg','-y','-v','error']+ins+['-filter_complex',fl,'-map','[v]','-map','[a]','-t','%.3f'%L]+ENC+AP+[o]);return o
def sigla(name,src):
    o=W+name+'.mkv'
    if os.path.exists(o): return o
    run(['ffmpeg','-y','-v','error','-i',src,'-filter_complex',f'[0:v]fps=30,scale=1920:1080,setsar=1,format=yuv420p,tpad=start_mode=clone:start_duration={LT}:stop_mode=clone:stop_duration={LT}[v];[0:a]loudnorm=I=-18:TP=-1.5,aresample=48000,aformat=channel_layouts=stereo,adelay={int(LT*1000)}|{int(LT*1000)},apad=pad_dur={LT}[a]','-map','[v]','-map','[a]','-t','%.3f'%(dur(src)+2*LT)]+ENC+AP+[o]); return o
XK={'toT':('circleopen',1.3),'fromT':('circleclose',1.3),'toR':('wipeleft',1.2),'toS':('wipeleft',1.2),'toQ':('zoomin',1.2),'fromQ':('circleclose',1.3),'toAN':('fade',1.0),'fromAN':('fade',1.0),'toFIN':('wipeleft',1.2),'def':('fade',1.0)}
def join(seq,out):
    parts=[];tl=[];t=0.0
    for k,(n,f,ty) in enumerate(seq):
        d=dur(f);a=0.0 if k==0 else LT;b=d-LT if k<len(seq)-1 else d
        if k>0:
            pn,pf,pt=seq[k-1]
            kind={('D','T'):'toT',('T','D'):'fromT',('D','S'):'toS',('S','Q'):'toQ',('Q','T'):'fromQ',('D','A'):'toAN',('A','D'):'fromAN',('Q','A'):'fromQ',('A','F'):'toFIN',('C','D'):'def',('G','C'):'def'}.get((pt,ty),'def')
            kn,xd=XK[kind];tr=W+f'x_{pn}_{n}.mkv'
            if not os.path.exists(tr):
                run(['ffmpeg','-y','-v','error','-sseof','-%.3f'%LT,'-i',pf,'-t','%.3f'%LT,'-i',f,'-filter_complex',
                     f'[0:v]fps=30,trim=duration={LT},setpts=PTS-STARTPTS[a0];[1:v]fps=30,trim=duration={LT},setpts=PTS-STARTPTS[b0];[a0][b0]xfade=transition={kn}:duration={xd}:offset={LT-xd:.3f},format=yuv420p[v];[0:a]atrim=duration={LT},asetpts=PTS-STARTPTS[x];[1:a]atrim=duration={LT},asetpts=PTS-STARTPTS[y];[x][y]acrossfade=d={min(xd,LT-0.05)}[a]',
                     '-map','[v]','-map','[a]','-max_muxing_queue_size','9999','-t','%.3f'%(2*LT-xd)]+ENC+AP+[tr])
            parts.append(tr);t+=dur(tr)
        body=W+f'b_{n}.mkv'
        if not os.path.exists(body):
            run(['ffmpeg','-y','-v','error','-ss','%.3f'%a,'-t','%.3f'%(b-a),'-i',f]+ENC+AP+[body])
        tl.append((n,round(t,3),round(dur(body),3)));parts.append(body);t+=dur(body)
    open(out,'w').write(''.join("file '%s'\n"%p for p in parts))
    return tl,t
V=D+'voci/wav/'
def Tc(k): return ('T%d'%k,mix_clip('T%d'%k,D+'dk/T%d.mp4'%k,'titolo',0.45),'T')
def Sc(k): return ('S%d'%k,mix_clip('S%d'%k,D+'po/S%d.mp4'%k,'repaso',0.3,V+'S%d.wav'%k,1.0,bed=True),'S')
def Qc(k): return ('Q%d'%k,mix_clip('Q%d'%k,D+'dk/Q%d.mp4'%k,'quiz',0.5),'Q')
def ex(k): return (k,mix_clip(k,D+'an/%s.mp4'%k,'trans',0.0,V+'%s.wav'%k,0.8,bed=True),'A')
def Dc(n,a,b): return (n,doc(n,a,b),'D')
END=3731.5
B=[cut(414.4),cut(1649.6),cut(2425.7),cut(2884.75),cut(3400.5),END]
if __name__=='__main__':
    print('argomenti',B,flush=True)
    seq=[('SIGLA',sigla('S0',D+'sigla_15s.mp4'),'G'),('INTRO1',still('INTRO1',D+'sv/s000_intro.png',V+'INTRO1.wav'),'C'),Dc('D0',0.0,B[0])]
    for k in range(1,6):
        seq+=[Tc(k),Dc(f'D{k}',B[k-1],B[k]),Sc(k),Qc(k)]
    seq+=[ex('GL1'),ex('RF1'),('FIN1',mix_clip('FIN1',D+'dk/FIN1.mp4','finale',0.4,V+'FIN1.wav',1.0),'F'),('SFIN',sigla('SFIN','/home/claude/sigle/Sigla_finale_chiusura.mp4'),'G')]
    tl,t=join(seq,D+'lista_finale.txt')
    json.dump(tl,open(D+'timeline.json','w'),indent=0)
    print('lista pronta',round(t/60,2),'min',flush=True)
