# Montaggio v2 Tecnologie Lez1 · jingle e transizioni come Spagnolo, tagli nelle pause tra le frasi
import json,os,subprocess,sys
D='/home/claude/lezioni/afm-inglese-triennio-lez03/';W=D+'w2/';os.makedirs(W,exist_ok=True)
VID=D+os.environ.get('VIDF','docente_slide_1080.mp4');VOFF=float(os.environ.get('VOFF','0'));AUD=D+'audio/audio_B_sting.wav'
SND='/home/claude/v5/snd/%s.wav'
ENC=['-c:v','libx264','-preset','veryfast','-crf','18','-pix_fmt','yuv420p','-r','30','-g','60']
AP=['-c:a','pcm_s16le','-ar','48000','-ac','2']
LT=1.3
def run(c): subprocess.run(c,check=True)
def dur(f): return float(subprocess.run(['ffprobe','-v','error','-show_entries','format=duration','-of','csv=p=0',f],capture_output=True,text=True).stdout)
A=json.load(open(D+'align_s.json'))['align'];U=json.load(open(D+'units.json'))
T={o['i']:o['t'] for o in A}
sys.path.insert(0,'/home/claude/lezioni/tools');import taglio
def cut(t): return taglio.snap(t-0.15,'/home/claude/lezioni/afm-inglese-triennio-lez03/audio/audio_B_full.wav')
def argstart(k):
    return min(o['t'] for o in A if U[o['i']]['a']==k-1)
def doc(name,a,b):
    """parte della docente, con LT secondi fermi in testa e in coda (per le transizioni)"""
    o=W+name+'.mkv'
    if os.path.exists(o): return o
    d=b-a
    run(['ffmpeg','-y','-v','error','-ss','%.3f'%(a-VOFF),'-t','%.3f'%d,'-i',VID,'-ss','%.3f'%a,'-t','%.3f'%d,'-i',AUD,'-filter_complex',
         f'[0:v]fps=30,format=yuv420p,tpad=start_mode=clone:start_duration={LT}:stop_mode=clone:stop_duration={LT}[v];[1:a]aformat=channel_layouts=stereo,aresample=48000,adelay={int(LT*1000)}|{int(LT*1000)},apad=pad_dur={LT}[a]',
         '-map','[v]','-map','[a]','-t','%.3f'%(d+2*LT)]+ENC+AP+[o]);return o
def mix_clip(name,vid,jingle=None,joff=0.4,voice=None,voff=0.9,bed=False,minlen=None):
    """clip grafico con LT di testa/coda: jingle, voce, musica leggera sotto"""
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
def still(name,png,voice,delay=0.8):
    o=W+name+'.mkv'
    if os.path.exists(o): return o
    L=dur(voice)+delay+0.8+2*LT
    run(['ffmpeg','-y','-v','error','-loop','1','-framerate','30','-i',png,'-i',voice,'-filter_complex',
         f'[0:v]format=yuv420p[v];[1:a]loudnorm=I=-16:TP=-1.5,aresample=48000,aformat=channel_layouts=stereo,adelay={int((LT+delay)*1000)}|{int((LT+delay)*1000)},apad[a]','-map','[v]','-map','[a]','-t','%.3f'%L]+ENC+AP+[o]);return o
def sigla(name,src,tail=True):
    o=W+name+'.mkv'
    if os.path.exists(o): return o
    run(['ffmpeg','-y','-v','error','-i',src,'-filter_complex',f'[0:v]fps=30,format=yuv420p,tpad=start_mode=clone:start_duration={LT}:stop_mode=clone:stop_duration={LT}[v];[0:a]loudnorm=I=-18:TP=-1.5,aresample=48000,aformat=channel_layouts=stereo,adelay={int(LT*1000)}|{int(LT*1000)},apad=pad_dur={LT}[a]','-map','[v]','-map','[a]','-t','%.3f'%(dur(src)+2*LT)]+ENC+AP+[o]); return o
def finale(name):
    o=W+name+'.mkv'
    if os.path.exists(o): return o
    src='/home/claude/lez1/sigla_finale.mp4';png='/home/claude/v5/cp/pill_1080.png'
    tmp=W+name+'_r.mkv'
    run(['ffmpeg','-y','-v','error','-i',src,'-loop','1','-framerate','30','-i',png,'-filter_complex',
         '[0:v]fps=30,scale=1920:1080,setsar=1[b];[1:v]format=rgba,fade=t=in:st=0.3:d=0.4:alpha=1,fade=t=out:st=4.3:d=0.4:alpha=1[p];[b][p]overlay=0:0:shortest=1,format=yuv420p[v];[0:a]loudnorm=I=-18:TP=-1.5,aresample=48000,aformat=channel_layouts=stereo[a]',
         '-map','[v]','-map','[a]','-t','%.3f'%dur(src)]+ENC+AP+[tmp])
    return sigla(name,tmp)
# ---------- unione con transizioni: ogni pezzo ha LT di margine in testa e in coda ----------
XK={'toT':('circleopen',1.3),'fromT':('circleclose',1.3),'toR':('wipeleft',1.2),'toS':('fade',1.0),'toQ':('zoomin',1.2),'fromQ':('circleclose',1.3),'toAN':('fade',1.0),'fromAN':('fade',1.0),'toFIN':('wipeleft',1.2),'def':('fade',1.0)}
def join(seq,out):
    """seq: lista di (nome, file, tipo); transizione scelta dai tipi; restituisce la linea del tempo"""
    parts=[];tl=[];t=0.0
    for k,(n,f,ty) in enumerate(seq):
        d=dur(f)
        if k==0: a=0.0
        else: a=LT  # la testa viene coperta dalla transizione
        b=d-LT if k<len(seq)-1 else d
        if k>0:
            pn,pf,pt=seq[k-1]
            kind={('D','T'):'toT',('T','D'):'fromT',('D','R'):'toR',('R','S'):'toS',('S','Q'):'toQ',('Q','T'):'fromQ',('D','A'):'toAN',('A','D'):'fromAN',('Q','F'):'toFIN',('Q','A'):'fromQ',('A','F'):'toFIN',('S','F'):'toFIN',('A','T'):'toT',('A','R'):'toR',('C','A'):'toAN',('Q','G'):'toFIN'}.get((pt,ty),'def')
            kn,xd=XK[kind]
            tr=W+f'x_{pn}_{n}.mkv'
            if not os.path.exists(tr):
                run(['ffmpeg','-y','-v','error','-sseof','-%.3f'%LT,'-i',pf,'-t','%.3f'%LT,'-i',f,'-filter_complex',
                     f'[0:v]fps=30,trim=duration={LT},setpts=PTS-STARTPTS[a0];[1:v]fps=30,trim=duration={LT},setpts=PTS-STARTPTS[b0];[a0][b0]xfade=transition={kn}:duration={xd}:offset={LT-xd:.3f},format=yuv420p[v];[0:a]atrim=duration={LT},asetpts=PTS-STARTPTS[x];[1:a]atrim=duration={LT},asetpts=PTS-STARTPTS[y];[x][y]acrossfade=d={xd}[a]',
                     '-map','[v]','-map','[a]','-max_muxing_queue_size','9999','-t','%.3f'%(2*LT-xd)]+ENC+AP+[tr])
            parts.append(tr);t+=dur(tr)
        body=W+f'b_{n}.mkv'
        if not os.path.exists(body):
            run(['ffmpeg','-y','-v','error','-ss','%.3f'%a,'-t','%.3f'%(b-a),'-i',f,'-c:v','libx264','-preset','veryfast','-crf','18','-pix_fmt','yuv420p','-r','30']+AP+[body])
        tl.append((n,round(t,3),round(dur(body),3)));parts.append(body);t+=dur(body)
    open(out+'.txt','w').write(''.join("file '%s'\n"%p for p in parts))
    run(['ffmpeg','-y','-v','error','-f','concat','-safe','0','-i',out+'.txt','-vf','scale=2560:1440:flags=lanczos','-c:v','libx264','-preset','fast','-crf','16','-maxrate','24M','-bufsize','48M','-pix_fmt','yuv420p','-c:a','aac','-b:a','320k','-ar','48000','-movflags','+faststart',out])
    return tl,t
V=D+'voci/wav/'
def topic_tail(k):
    return [('R%d'%k,mix_clip('R%d'%k,D+'dk/R%d.mp4'%k,'repaso',0.4,V+'R%d.wav'%k,0.9),'R'),
            ('S%d'%k,mix_clip('S%d'%k,D+'po/S%d.mp4'%k,None,0,V+'S%d.wav'%k,1.0,bed=True),'S'),
            ('Q%d'%k,mix_clip('Q%d'%k,D+'dk/Q%d.mp4'%k,'quiz',0.5),'Q')]
def Tc(k): return ('T%d'%k,mix_clip('T%d'%k,D+'dk/T%d.mp4'%k,'titolo',0.45),'T')
def an(k): return ('AN%d'%k,mix_clip('AN%d'%k,D+'an/AN%d.mp4'%k,'trans',0.0,V+'AN%d.wav'%k,0.8),'A')
def ex(k): return (k,mix_clip(k,D+'an/%s.mp4'%k,'trans',0.0,V+'%s.wav'%k,0.8,bed=True),'A')
def Dc(n,a,b): return (n,doc(n,a,b),'D')
if __name__=='__main__':
    # Lez5 «Tessitura · parte II»: un solo video, 7 argomenti; animazioni a fine argomento, prima del ripasso
    import collections
    NQ=collections.Counter(q['quiz'] for q in json.load(open(D+'quiz_raw.json')))
    NA=7;ANK={1:[1],2:[2],6:[3,4],7:[5]}
    B={f'a{k}':cut(argstart(k)) for k in range(1,NA+1)};B['end']=round(dur(VID)+VOFF,3)
    print(B)
    def tail(k):
        t=topic_tail(k)
        return t  # ogni argomento ha il suo quiz
    seq=[('SIGLA',sigla('S0',D+'Sigla_Tecnologie_moda_15s.mp4'),'G'),('INTRO1',still('INTRO1',D+'sv/s000_cover.png',V+'INTRO1.wav'),'C'),Dc('D0',0.0,B['a1'])]
    for k in range(1,NA+1):
        seq+=[Tc(k),Dc(f'D{k}',B[f'a{k}'],B[f'a{k+1}'] if k<NA else B['end'])]+[an(j) for j in ANK.get(k,[])]+tail(k)
    seq+=[ex('GL1'),ex('RF1'),('FIN1',mix_clip('FIN1',D+'dk/FIN1.mp4','finale',0.4,V+'FIN1.wav',1.0),'F'),('SFIN',finale('SFIN'),'G')]
    out=D+'Tecnologie_Tessitura_parte_II_1440p.mp4'
    if os.environ.get('PIANO'):
        tot=0
        for n,f,ty in seq:tot+=dur(f)-2*LT+ (0 if n=='SIGLA' else 0)
        print('durata stimata',round(tot/60,2),'min');sys.exit()
    tl,t=join(seq,out)
    json.dump(tl,open(D+'timeline_L5.json','w'),indent=0)
    print(out,round(t/60,2),'min')
