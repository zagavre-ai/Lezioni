# Montaggio v2 Tecnologie Lez1 · jingle e transizioni come Spagnolo, tagli nelle pause tra le frasi
import json,os,subprocess,sys
D='/home/claude/lezioni/psicologia-I-II-lez01/';W=D+'w2/';os.makedirs(W,exist_ok=True)
VID=D+os.environ.get('VIDF','docente_slide_1080.mp4');VOFF=float(os.environ.get('VOFF','0'));AUD=D+'audio/audio_B_sting.wav'
SND='/home/claude/v5/snd/%s.wav'
ENC=['-c:v','libx264','-preset','veryfast','-crf','18','-pix_fmt','yuv420p','-r','30','-g','60']
AP=['-c:a','pcm_s16le','-ar','48000','-ac','2']
LT=1.3
def run(c): subprocess.run(c,check=True)
def dur(f): return float(subprocess.run(['ffprobe','-v','error','-show_entries','format=duration','-of','csv=p=0',f],capture_output=True,text=True).stdout)
A=json.load(open(D+'align_s.json'))['align'];U=json.load(open(D+'units.json'))
T={o['i']:o['t'] for o in A}
def cut(t): return round(t-0.15,3)
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
            kind={('D','T'):'toT',('T','D'):'fromT',('D','R'):'toR',('R','S'):'toS',('S','Q'):'toQ',('Q','T'):'fromQ',('D','A'):'toAN',('A','D'):'fromAN',('Q','F'):'toFIN',('Q','A'):'fromQ',('A','F'):'toFIN',('S','F'):'toFIN',('A','T'):'toT',('C','A'):'toAN',('Q','G'):'toFIN'}.get((pt,ty),'def')
            kn,xd=XK[kind]
            tr=W+f'x_{pn}_{n}.mkv'
            if not os.path.exists(tr):
                run(['ffmpeg','-y','-v','error','-sseof','-%.3f'%LT,'-i',pf,'-t','%.3f'%LT,'-i',f,'-filter_complex',
                     f'[0:v]fps=30,trim=duration={LT},setpts=PTS-STARTPTS[a0];[1:v]fps=30,trim=duration={LT},setpts=PTS-STARTPTS[b0];[a0][b0]xfade=transition={kn}:duration={xd}:offset={LT-xd:.3f},format=yuv420p[v];[0:a]atrim=duration={LT},asetpts=PTS-STARTPTS[x];[1:a]atrim=duration={LT},asetpts=PTS-STARTPTS[y];[x][y]acrossfade=d={xd}[a]',
                     '-map','[v]','-map','[a]','-t','%.3f'%(2*LT-xd)]+ENC+AP+[tr])
            parts.append(tr);t+=dur(tr)
        body=W+f'b_{n}.mkv'
        if not os.path.exists(body):
            run(['ffmpeg','-y','-v','error','-ss','%.3f'%a,'-t','%.3f'%(b-a),'-i',f,'-c:v','libx264','-preset','veryfast','-crf','18','-pix_fmt','yuv420p','-r','30']+AP+[body])
        tl.append((n,round(t,3),round(dur(body),3)));parts.append(body);t+=dur(body)
    open(out+'.txt','w').write(''.join("file '%s'\n"%p for p in parts))
    run(['ffmpeg','-y','-v','error','-f','concat','-safe','0','-i',out+'.txt','-c:v','libx264','-preset','fast','-crf','19','-maxrate','12M','-bufsize','24M','-pix_fmt','yuv420p','-c:a','aac','-b:a','192k','-movflags','+faststart',out])
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
    part=int(sys.argv[1])
    B={'a1':cut(argstart(1)),'a2':cut(argstart(2)),'a3':cut(argstart(3)),'a4':cut(argstart(4)),'a5':cut(argstart(5)),'a6':cut(argstart(6)),
       'a7':cut(argstart(7)),'a8':cut(argstart(8)),'a9':cut(argstart(9)),'AN1':cut(T[77]),'AN2':cut(T[91]),'AN3':cut(T[131]),'AN4':cut(T[180]) if 180 in T else None,'AN5':cut(T[AN5_I]) if 'AN5_I' in globals() else None,'AN6':cut(T[AN6_I]) if 'AN6_I' in globals() else None,'end':4468.0}
    print(B)
    S0=('SIGLA',sigla('S0',D+'Sigla_Tecnologie_moda_15s.mp4'),'G')
    if part==1:
        seq=[S0,('INTRO1',still('INTRO1',D+'sv/s000_cover.png',V+'INTRO1.wav'),'C'),Dc('D0',0.0,B['a1']),Tc(1),Dc('D1',B['a1'],B['a2'])]+topic_tail(1)
        seq+=[Tc(2),Dc('D2',B['a2'],B['a3'])]+topic_tail(2)+[Tc(3),Dc('D3',B['a3'],B['a4'])]+topic_tail(3)
        seq+=[Tc(4),Dc('D4a',B['a4'],B['AN1']),an(1),Dc('D4b',B['AN1'],B['AN2']),an(2),Dc('D4c',B['AN2'],B['a5'])]+topic_tail(4)
        seq+=[Tc(5),Dc('D5a',B['a5'],B['AN3']),an(3),Dc('D5b',B['AN3'],B['a6'])]+topic_tail(5)
        if os.path.exists(D+'an/GL1.mp4'): seq+=[ex('GL1'),ex('RF1')]
        seq+=[('FIN1',mix_clip('FIN1',D+'dk/FIN1.mp4','finale',0.4,V+'FIN1.wav',1.0),'F'),('S9',finale('S9'),'G')]
    if part==2:
        seq=[S0,('IN2',still('IN2',D+'sv/s000_cover_P2.png',V+'IN2.wav'),'C'),('RIP',mix_clip('RIP',D+'an/RIP.mp4','trans',0.0,V+'RIP.wav',0.8,bed=True),'A')]
        seq+=[Tc(6),Dc('D6a',B['a6'],B['AN4']),an(4),Dc('D6b',B['AN4'],B['a7'])]+topic_tail(6)
        if os.environ.get('PREV15'):
            seq+=[('S9',finale('S9'),'G')]
        else:
            seq+=[Tc(7),Dc('D7a',B['a7'],B['AN5']),an(5),Dc('D7b',B['AN5'],B['a8'])]+topic_tail(7)
            seq+=[Tc(8),Dc('D8a',B['a8'],B['AN6']),an(6),Dc('D8b',B['AN6'],B['a9'])]+topic_tail(8)
            seq+=[Tc(9),Dc('D9',B['a9'],B['end'])]+topic_tail(9)
            if os.path.exists(D+'an/GL2.mp4'): seq+=[ex('GL2'),ex('RF2')]
            seq+=[('FIN2',mix_clip('FIN2',D+'dk/FIN2.mp4','finale',0.4,V+'FIN2.wav',1.0),'F'),('S9',finale('S9'),'G')]
    out=D+f'Tecnologie_Lez1_Parte{part}_VIDEO'+('_prime15min' if os.environ.get('PREV15') else '')+'.mp4'
    tl,t=join(seq,out)
    json.dump(tl,open(D+f'timeline_P{part}.json','w'),indent=0)
    print(out,round(t/60,2),'min')
