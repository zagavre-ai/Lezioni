# Montaggio lezione 7 Inglese AFM: pezzi con margini LT, transizioni, lista per finale_a_pezzi
import json,os,subprocess,sys,re,html
sys.path.insert(0,'/home/claude/w7')
import tl7 as TLM
from content7 import ARG
import def7 as VD
from render import *
D='/home/claude/w7/';LT=1.3
MODE=os.environ.get('MODE','ph')           # ph = segnaposto, kore = voci Kore
W=D+('w_'+MODE)+'/';WD=D+'wd/';os.makedirs(W,exist_ok=True);os.makedirs(WD,exist_ok=True);os.makedirs(D+'ph',exist_ok=True)
ENC=['-c:v','libx264','-preset','veryfast','-crf','17','-pix_fmt','yuv420p','-r','30','-g','60']
AP=['-c:a','pcm_s16le','-ar','48000','-ac','2']
SND=D+'as/%s.wav'
GAIN=float(open(D+'gain.txt').read()) if os.path.exists(D+'gain.txt') else 0.0
def run(c):
    for k in range(3):
        r=subprocess.run(c)
        if r.returncode==0: return
    raise subprocess.CalledProcessError(r.returncode,c)
def dur(f): return float(subprocess.run(['ffprobe','-v','error','-show_entries','format=duration','-of','csv=p=0',f],capture_output=True,text=True).stdout)
def voice(name):
    real=D+'voci/wav/'+name+'.wav'
    if MODE=='kore':
        if not os.path.exists(real): raise SystemExit('manca voce Kore '+name)
        return real
    ph=D+'ph/'+name+'.wav'
    if not os.path.exists(ph):
        d=len(VD.V[name].split())/2.4+0.4
        run(['ffmpeg','-y','-v','error','-f','lavfi','-t','%.2f'%d,'-i','anullsrc=r=48000:cl=mono',ph])
    return ph
def concat_voice(names,out,gap=0.35):
    if os.path.exists(out): return
    ins=[];fl='';
    for i,n in enumerate(names):
        ins+=['-i',voice(n)];fl+=f'[{i}:a]aresample=48000,aformat=channel_layouts=mono,apad=pad_dur={gap if i<len(names)-1 else 0}[a{i}];'
    fl+=''.join(f'[a{i}]' for i in range(len(names)))+f'concat=n={len(names)}:v=0:a=1[o]'
    run(['ffmpeg','-y','-v','error']+ins+['-filter_complex',fl,'-map','[o]','-ar','48000',out])
def offsets(names,gap=0.35):
    o=[];t=0
    for n in names: o.append(t);t+=dur(voice(n))+gap
    return o
# ---------- tempi del docente ----------
import content7 as C7
X=None
def bounds():
    global X
    X=TLM.audio();b=[]
    for g in C7.TS+[C7.FINE_ARG]: b.append(TLM.snap(X,TLM.tm(g)-0.15))
    return [max(0.0,TLM.tm(C7.LS)-0.4)]+b+[round(TLM.TOT,3)]
def txt(x): return x[0] if isinstance(x,tuple) else x
# ---------- schede ----------
def shot_all():
    with sync_playwright() as p:
        b=p.chromium.launch();pg=b.new_page(viewport={'width':1920,'height':1080})
        def S(name,h):
            f=D+'sl/'+name+'.png'
            if not os.path.exists(f): shot(pg,h,f)
            return f
        intro=[t for t,_ in C7.INTRO]
        for i in range(len(intro)+1):
            S(f'A0_{i}',slide_html('Welcome','Trade and commerce',intro,i-1 if i>0 else -1,[("trade","scambio, commercio"),("commerce","commercio (di beni)"),("e-commerce","commercio elettronico")]))
        ch=[t for t,_ in C7.CHIUSURA]
        for i in range(len(ch)+1):
            S(f'A7_{i}',slide_html('Summary','What we have seen today',ch,i-1 if i>0 else -1,[("home trade","commercio interno"),("trade sanction","sanzione commerciale"),("ethical trade","commercio etico")]))
        for a in ARG:
            for si,s in enumerate(a['slides']):
                its=[txt(x) for x in s['items']]
                for ii in range(len(its)):
                    S(f"A{a['n']}_{si}_{ii}",slide_html(f"{a['n']:02d} · {a['titolo']}",s['t'],its,ii,s['kw']))
                S(f"A{a['n']}_{si}_x",slide_html(f"{a['n']:02d} · {a['titolo']}",s['t'],its,-1,s['kw']))
        for a in ARG:
            S(f"T{a['n']}",card_html(a['titolo'],f"Topic {a['n']} of 6",bands=False,dark=True))
            S(f"Q{a['n']}",card_html(f"Quiz · {a['titolo']}","5 questions · at least 80% to continue"))
        S('COVER',card_html('Trade and commerce','Inglese · Triennio Amministrazione, Finanza e Marketing',bands=False,dark=True,extra='<div class="x">Prof.ssa Maria Vittoria Fontanesi</div>'))
        S('FIN',card_html('Verifica finale','Final test',bands=True))
        S('CMPI',card_html('Compiti','Homework',bands=True,dark=True))
        S('CMP',card_html('Compiti','Scarica la scheda dei compiti dalla lezione',bands=True))
        rf=VD.V['E7_RF1'].split('. ')
        S('RF',review_html('Final review',[x.strip('.')+'.' for x in rf[1:-1]]))
        for g in (0,1):
            terms=VD.GL[g*12:(g+1)*12]
            for i in range(13): S(f'GL{g}_{i}',gloss_html(terms,i))
    return
def review_html(title,lines):
    li=''.join(f'<div class="it on" style="margin-bottom:22px;color:#0B1530"><span class="n">{i+1}</span>{md(l)}</div>' for i,l in enumerate(lines))
    return f'<html><head><style>{CSS}.items{{top:250px;width:1760px}}</style></head><body><img class="logo" src="{LOGO}"><div class="kick">Review</div><div class="hl">{html.escape(title)}</div><div class="bar"></div><div class="items">{li}</div><div class="foot">Inglese &nbsp;·&nbsp; Prof.ssa Maria Vittoria Fontanesi</div></body></html>'
def gloss_html(terms,cur):
    c=''
    for i,(e,it) in enumerate(terms):
        v=i<cur;on=i==cur-1
        c+=f'<div style="background:#fff;border-radius:14px;padding:16px 22px;border:3px solid {"#FFE600" if on else "transparent"};opacity:{1 if v else .0};box-shadow:0 2px 10px rgba(32,96,175,.08)"><div style="font:800 34px Bricolage">{html.escape(e)}</div><div style="font-size:25px;color:#2060AF;margin-top:4px">it. {html.escape(it)}</div></div>'
    return f'<html><head><style>{CSS}</style></head><body><img class="logo" src="{LOGO}"><div class="kick">Glossary · Glossario</div><div class="hl">Key words</div><div class="bar"></div><div style="position:absolute;left:80px;right:80px;top:310px;display:grid;grid-template-columns:1fr 1fr 1fr;gap:20px">{c}</div><div class="foot">Inglese &nbsp;·&nbsp; Prof.ssa Maria Vittoria Fontanesi</div></body></html>'
def mkmask():
    from PIL import Image,ImageDraw
    f=D+'sl/mask.png'
    if not os.path.exists(f):
        m=Image.new('L',(416,312),0);ImageDraw.Draw(m).rounded_rectangle((0,0,415,311),radius=22,fill=255);m.save(f)
    return f
# ---------- pezzi ----------
def mix_clip(name,vid,jingle=None,joff=0.4,vname=None,voff=0.9,bed=False,minlen=None,vfile=None,loop=None):
    o=W+name+'.mkv'
    if os.path.exists(o): return o
    dv=dur(vid);L=dv;vf=vfile or (voice(vname) if vname else None)
    if vf: L=max(L,voff+dur(vf)+0.8)
    if minlen: L=max(L,minlen)
    tot=L+2*LT
    ins=['-i',vid,'-f','lavfi','-t','%.3f'%tot,'-i','anullsrc=r=48000:cl=stereo'];fl=f'[0:v]fps=30,scale=1920:1080,setsar=1,tpad=start_mode=clone:start_duration={LT}:stop_mode=clone:stop_duration={LT+L-dv:.3f},format=yuv420p[v];[1:a]anull[b0]';lab=['b0'];k=2
    if jingle:
        ins+=['-i',SND%jingle];fl+=f';[{k}:a]aformat=channel_layouts=stereo,aresample=48000,adelay={int((LT+joff)*1000)}|{int((LT+joff)*1000)},volume={0.55 if vf else 0.9}[b{k}]';lab.append(f'b{k}');k+=1
    if vf:
        ins+=['-i',vf];fl+=f';[{k}:a]loudnorm=I=-16:TP=-1.5,aresample=48000,aformat=channel_layouts=stereo,adelay={int((LT+voff)*1000)}|{int((LT+voff)*1000)}[b{k}]';lab.append(f'b{k}');k+=1
    fl+=';'+''.join(f'[{l}]' for l in lab)+f'amix=inputs={len(lab)}:normalize=0:duration=first[a]'
    run(['ffmpeg','-y','-v','error']+ins+['-filter_complex',fl,'-map','[v]','-map','[a]','-t','%.3f'%tot]+ENC+AP+[o+'.tmp.mkv']);os.rename(o+'.tmp.mkv',o);return o
def png_video(name,png,secs):
    o=W+name+'_s.mp4'
    if not os.path.exists(o): run(['ffmpeg','-y','-v','error','-loop','1','-framerate','30','-i',png,'-t','%.3f'%secs,'-c:v','libx264','-preset','veryfast','-crf','14','-pix_fmt','yuv420p','-r','30',o])
    return o
def seq_video(name,states,vfile,lead=0.0,voff=0.9,tail=1.0):
    """immagini che cambiano a intervalli uguali sulla durata della voce (glossario)"""
    o=W+name+'_s.mp4'
    if os.path.exists(o): return o
    d=voff+dur(vfile)+tail;n=len(states)-1
    st=(d-voff-lead-tail)/n;ln=[(states[0],voff+lead)]
    for i in range(1,n+1): ln.append((states[i],st if i<n else st+tail))
    txt=''.join(f"file '{p}'\nduration {x:.3f}\n" for p,x in ln)+f"file '{ln[-1][0]}'\n"
    open(o+'.txt','w').write(txt)
    run(['ffmpeg','-y','-v','error','-f','concat','-safe','0','-i',o+'.txt','-vf','fps=30,format=yuv420p','-c:v','libx264','-preset','veryfast','-crf','14',o]);return o
def doc_clip(name,a,b,states):
    """docente tra a e b (tempo tagliato) su sfondo con slide sincronizzate, a pezzi corti (poca memoria) uniti senza ricodifica"""
    o=WD+name+'.mkv'
    if os.path.exists(o): return o
    gain=f',volume={GAIN}dB,alimiter=limit=0.89:level=disabled' if GAIN else ''
    FR=30;nA=round(a*FR);nB=round(b*FR)
    ln=[]
    for i,(p,t) in enumerate(states):
        n0=max(round(t*FR),nA);n1=min(round(states[i+1][1]*FR),nB) if i+1<len(states) else nB
        if n1-n0>=1: ln.append((p,n0,n1-n0))
    # spiana: primo pezzo parte da nA, nessun buco
    if ln and ln[0][1]>nA: ln[0]=(ln[0][0],nA,ln[0][2]+ln[0][1]-nA)
    pieces=[];mk=mkmask()
    def vf(pngidx):
        return ('[1:v]fps=30,scale=416:312,format=rgba[f];[2:v]format=gray[m];[f][m]alphamerge[fa];[0:v]format=yuv420p[bg];[bg][fa]overlay=1426:148:shortest=1,format=yuv420p[v]')
    for k,(p,n0,nf) in enumerate(ln):
        f=f'{WD}{name}_p{k:03d}.mkv'
        if not os.path.exists(f):
            t0=n0/FR;d=nf/FR
            run(['ffmpeg','-y','-v','error','-loop','1','-framerate','30','-t','%.4f'%d,'-i',p,'-ss','%.4f'%t0,'-t','%.4f'%d,'-i',D+'dt/docente_all.mkv','-loop','1','-framerate','30','-t','%.4f'%d,'-i',mk,'-filter_complex',
                vf(0)+f';[1:a]aformat=channel_layouts=stereo,aresample=48000,atrim=duration={d:.4f}{gain}[a]','-map','[v]','-map','[a]','-frames:v',str(nf),'-c:v','libx264','-preset','veryfast','-crf','17','-pix_fmt','yuv420p','-r','30','-g','60','-c:a','pcm_s16le','-ar','48000','-ac','2',f+'.tmp.mkv']);os.rename(f+'.tmp.mkv',f)
        pieces.append(f)
    # margini di LT secondi: primo e ultimo fotogramma fermi, audio muto
    def pad(tag,png,tf):
        f=f'{WD}{name}_{tag}.mkv'
        if not os.path.exists(f):
            run(['ffmpeg','-y','-v','error','-loop','1','-framerate','30','-t','%.3f'%LT,'-i',png,'-ss','%.4f'%tf,'-t','0.1','-i',D+'dt/docente_all.mkv','-loop','1','-framerate','30','-t','%.3f'%LT,'-i',mk,'-f','lavfi','-t','%.3f'%LT,'-i','anullsrc=r=48000:cl=stereo','-filter_complex',
                '[1:v]fps=30,scale=416:312,format=rgba,tpad=stop_mode=clone:stop_duration=%.3f[f];[2:v]format=gray[m];[f][m]alphamerge[fa];[0:v]format=yuv420p[bg];[bg][fa]overlay=1426:148:shortest=1,format=yuv420p[v]'%LT,'-map','[v]','-map','3:a','-t','%.3f'%LT,'-c:v','libx264','-preset','veryfast','-crf','17','-pix_fmt','yuv420p','-r','30','-g','60','-c:a','pcm_s16le','-ar','48000','-ac','2',f+'.tmp.mkv']);os.rename(f+'.tmp.mkv',f)
        return f
    h=pad('head',ln[0][0],nA/FR);t=pad('tail',ln[-1][0],max(0,(nB-1)/FR))
    open(WD+name+'.txt','w').write(''.join("file '%s'\n"%x for x in [h]+pieces+[t]))
    run(['ffmpeg','-y','-v','error','-f','concat','-safe','0','-i',WD+name+'.txt','-c','copy',o+'.tmp.mkv']);os.rename(o+'.tmp.mkv',o)
    return o
def sigla(name,src):
    o=W+name+'.mkv'
    if os.path.exists(o): return o
    run(['ffmpeg','-y','-v','error','-i',src,'-filter_complex',f'[0:v]fps=30,scale=1920:1080,format=yuv420p,tpad=start_mode=clone:start_duration={LT}:stop_mode=clone:stop_duration={LT}[v];[0:a]loudnorm=I=-18:TP=-1.5,aresample=48000,aformat=channel_layouts=stereo,adelay={int(LT*1000)}|{int(LT*1000)},apad=pad_dur={LT}[a]','-map','[v]','-map','[a]','-t','%.3f'%(dur(src)+2*LT)]+ENC+AP+[o+'.tmp.mkv']);os.rename(o+'.tmp.mkv',o);return o
XK={'toT':('circleopen',1.3),'fromT':('circleclose',1.3),'toR':('wipeleft',1.2),'toQ':('zoomin',1.2),'fromQ':('circleclose',1.3),'toAN':('fade',1.0),'fromAN':('fade',1.0),'toFIN':('wipeleft',1.2),'def':('fade',1.0)}
def join(seq,out):
    parts=[];tl=[];t=0.0
    for k,(n,f,ty) in enumerate(seq):
        d=dur(f);a=0.0 if k==0 else LT;b=d-LT if k<len(seq)-1 else d
        if k>0:
            pn,pf,pt=seq[k-1]
            kind={('D','T'):'toT',('T','D'):'fromT',('R','T'):'toT',('Q','T'):'fromQ',('A','R'):'toR',('D','A'):'toAN',('A','D'):'fromAN',('R','Q'):'toQ',('Q','A'):'fromQ',('A','F'):'toFIN',('R','F'):'toFIN',('Q','F'):'toFIN',('A','T'):'toT',('T','A'):'toAN'}.get((pt,ty),'def')
            kn,xd=XK[kind];tr=W+f'x_{pn}_{n}.mkv'
            if not os.path.exists(tr):
                run(['ffmpeg','-y','-v','error','-sseof','-%.3f'%LT,'-i',pf,'-t','%.3f'%LT,'-i',f,'-filter_complex',
                  f'[0:v]fps=30,trim=duration={LT},setpts=PTS-STARTPTS[a0];[1:v]fps=30,trim=duration={LT},setpts=PTS-STARTPTS[b0];[a0][b0]xfade=transition={kn}:duration={xd}:offset={LT-xd:.3f},format=yuv420p[v];[0:a]atrim=duration={LT},asetpts=PTS-STARTPTS[x];[1:a]atrim=duration={LT},asetpts=PTS-STARTPTS[y];[x][y]acrossfade=d={xd}[a]',
                  '-map','[v]','-map','[a]','-t','%.3f'%(2*LT-xd)]+ENC+AP+[tr+'.tmp.mkv']);os.rename(tr+'.tmp.mkv',tr)
            parts.append(tr);t+=dur(tr)
        body=W+f'b_{n}.mkv'
        if not os.path.exists(body):
            run(['ffmpeg','-y','-v','error','-ss','%.3f'%a,'-t','%.3f'%(b-a),'-i',f,'-c:v','libx264','-preset','veryfast','-crf','17','-pix_fmt','yuv420p','-r','30']+AP+[body+'.tmp.mkv']);os.rename(body+'.tmp.mkv',body)
        tl.append((n,round(t,3),round(dur(body),3)));parts.append(body);t+=dur(body)
    open(out+'.txt','w').write(''.join("file '%s'\n"%p for p in parts));return tl,t
