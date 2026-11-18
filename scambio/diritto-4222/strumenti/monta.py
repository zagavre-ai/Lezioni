# monta.py — monta la lezione 4222 a pezzi (ripartibile: ogni pezzo ha il suo .ok).
# uso: python3 monta.py WORK VOX VIDEO_ORIG [fase]     fasi: pezzi | parti
#  WORK = cartella di lavoro (con tratti/ e schede/ già pronti)   VOX = cartella dei .wav Kore della master
import sys,os,json,subprocess,shutil,re,math
QUI=os.path.dirname(os.path.abspath(__file__));sys.path.insert(0,QUI);sys.path.insert(0,os.path.join(QUI,'..'))
import contenuti as C
import scene
W,VOX=os.path.abspath(sys.argv[1]),os.path.abspath(sys.argv[2]);FASE=sys.argv[4] if len(sys.argv)>4 else 'pezzi'
SND=QUI;KIT=os.path.join(QUI,'..','..','..','kit')
for d in ['seg','vp','tmp']:os.makedirs(f'{W}/{d}',exist_ok=True)
ENV=dict(os.environ,PYTHONPATH=QUI+'/pwshim')
def sh(c,**k):
    r=subprocess.run(c,capture_output=True,text=True,**k)
    if r.returncode:raise SystemExit('ERRORE: '+' '.join(map(str,c))[:300]+'\n'+r.stderr[-800:])
    return r
def dur(f):return float(sh(['ffprobe','-v','error','-show_entries','format=duration','-of','csv=p=0',f]).stdout)
# ---------------- voci: tolgo il silenzio ai bordi
_cache={}
def vox(k):
    if k in _cache:return _cache[k]
    src=f'{VOX}/{k}.wav';o=f'{W}/vp/{k}.wav'
    if not os.path.exists(o):
        sf='silenceremove=start_periods=1:start_threshold=-48dB:start_silence=0.05'
        sh(['ffmpeg','-y','-v','error','-i',src,'-af',f'aresample=48000,{sf},areverse,{sf},areverse','-ac','2','-c:a','pcm_s16le',o])
    _cache[k]=(o,dur(o));return _cache[k]
def mix(events,total,out,voice_norm=True):
    """events: [(t,wav,tipo)] tipo 'v' voce (normalizzata -16 LUFS insieme) o 'j' jingle (volume come nel kit)"""
    def track(ev,o,norm):
        if not ev:
            sh(['ffmpeg','-y','-v','error','-f','lavfi','-i','anullsrc=r=48000:cl=stereo','-t',f'{total}','-c:a','pcm_s16le',o]);return
        ins=[];fl=[]
        for i,(t,w,_) in enumerate(ev):
            ins+=['-i',w];fl.append(f'[{i}:a]aresample=48000,aformat=channel_layouts=stereo,adelay={int(t*1000)}:all=1[a{i}]')
        fl.append(''.join(f'[a{i}]' for i in range(len(ev)))+f'amix=inputs={len(ev)}:normalize=0:duration=longest,apad,atrim=0:{total}'+(',loudnorm=I=-16:TP=-1.5:LRA=11' if norm else '')+',aresample=48000[o]')
        sh(['ffmpeg','-y','-v','error',*ins,'-filter_complex',';'.join(fl),'-map','[o]','-c:a','pcm_s16le',o])
    tv=out+'.v.wav';tj=out+'.j.wav'
    track([e for e in events if e[2]=='v'],tv,True);track([e for e in events if e[2]=='j'],tj,False)
    sh(['ffmpeg','-y','-v','error','-i',tv,'-i',tj,'-filter_complex','[0:a][1:a]amix=inputs=2:normalize=0,alimiter=limit=0.89,atrim=0:%s[o]'%total,'-map','[o]','-c:a','pcm_s16le',out])
    os.remove(tv);os.remove(tj)
def mux(video,audio,out,total=None):
    sh(['ffmpeg','-y','-v','error','-i',video,'-i',audio,'-map','0:v','-map','1:a','-c:v','copy','-c:a','pcm_s16le','-t',f'{total or dur(video)}',out])
def ok(f):return os.path.exists(f+'.ok')
def done(f):open(f+'.ok','w').write('1')
ARG=lambda k:f'{k:02d} · {C.ARGOMENTI[k-1][0]}'
# ---------------- pezzi
def p_cover():
    o=f'{W}/seg/cover.mkv'
    if ok(o):return o
    a,d=vox('W01');tot=a and d+2.2
    scene.render({'type':'cover','materia':C.MATERIA,'titolo':C.TITOLO,'docente':C.DOCENTE,'argomenti':[x[0] for x in C.ARGOMENTI],'dur':tot},f'{W}/tmp/cover.mp4',30,4)
    mix([(0.9,a,'v')],tot,f'{W}/tmp/cover.wav');mux(f'{W}/tmp/cover.mp4',f'{W}/tmp/cover.wav',o);done(o);return o
def p_titolo(k):
    o=f'{W}/seg/T{k}.mkv'
    if ok(o):return o
    mix([(0,SND+'/titolo.wav','j')],4,f'{W}/tmp/t{k}.wav');mux(f'{W}/schede/T{k}.mp4',f'{W}/tmp/t{k}.wav',o,4);done(o);return o
def p_quiz(k):
    o=f'{W}/seg/Q{k}.mkv'
    if ok(o):return o
    mix([(0.5,SND+'/quiz.wav','j')],5,f'{W}/tmp/q{k}.wav');mux(f'{W}/schede/Q{k}.mp4',f'{W}/tmp/q{k}.wav',o,5);done(o);return o
def p_anim(nid):
    o=f'{W}/seg/{nid}.mkv'
    if ok(o):return o
    a=json.loads(json.dumps(C.ANIM[nid]));t=0.9;ev=[]
    for si,s in enumerate(a['slides'],1):
        s['t0']=t
        for ii,i in enumerate(s['items'],1):
            w,d=vox(f'{nid}_s{si}_i{ii}');i['t0']=t;i['t1']=t+d;ev.append((t,w,'v'));t+=d+0.4
        s['t1']=t+0.1;t+=0.8
    tot=t+0.4
    for s in a['slides']:
        for i in s['items']:i.pop('say',None)
    scene.render({'type':'anim','arg':ARG(a['arg']),'materia':C.MATERIA,'slides':a['slides'],'dur':tot},f'{W}/tmp/{nid}.mp4',30,4)
    mix(ev,tot,f'{W}/tmp/{nid}.wav');mux(f'{W}/tmp/{nid}.mp4',f'{W}/tmp/{nid}.wav',o);done(o);return o
def p_schema(k):
    o=f'{W}/seg/S{k}.mkv'
    if ok(o):return o
    t=1.0;ev=[];rows=[]
    for i,(kw,df) in enumerate(C.SCHEMI[k],1):
        w,d=vox(f'S{k}_{i}');rows.append([kw,df,t,t+d+2.5]);ev.append((t,w,'v'));t+=d+2.5
    tot=t+3.0
    scene.render({'type':'schema','arg':ARG(k),'materia':C.MATERIA,'titolo':C.ARGOMENTI[k-1][0],'rows':rows,'dur':tot},f'{W}/tmp/S{k}.mp4',30,4)
    mix(ev,tot,f'{W}/tmp/S{k}.wav');mux(f'{W}/tmp/S{k}.mp4',f'{W}/tmp/S{k}.wav',o);done(o);return o
def schede_render(spec,out):
    json.dump([[json.dumps(spec),out,30]],open(out+'.job.json','w'))
    sh([sys.executable,f'{QUI}/../../strumenti/letteratura_spagnolo/render_fast.py',out+'.job.json'],env=ENV)
def p_repaso(k):
    o=f'{W}/seg/R{k}.mkv'
    if ok(o):return o
    a,d=vox(f'R{k}');tot=max(14.0,0.9+d+1.6)
    fr=re.split(r'(?<=[.!?])\s+',C.PILLOLA_ANNUNCIO[k]);L=[len(x) for x in fr];T=sum(L);caps=[];t=0.9
    for x,l in zip(fr,L):
        dd=d*l/T;caps.append([round(t,2),round(t+dd,2),x]);t+=dd
    caps[-1][1]=tot-0.3
    top=C.ARGOMENTI[k-1][0];tfs=84 if len(top)<=30 else max(52,int(84*30/len(top)))
    schede_render({'type':'repaso','kicker':'Pillola di diritto','big':'RIPASSO','topic':top,'tfs':tfs,'caps':caps,'dur':tot},f'{W}/tmp/R{k}.mp4')
    mix([(0,SND+'/repaso.wav','j'),(0.9,a,'v')],tot,f'{W}/tmp/R{k}.wav');mux(f'{W}/tmp/R{k}.mp4',f'{W}/tmp/R{k}.wav',o);done(o);return o
def mappa_json(m):
    return {'materia':C.MATERIA,'docente':C.DOCENTE,'titolo':m['titolo'],'rami':[{'concetto':r[0],'parola':r[1],'esempio':r[2]} for r in m['rami']]}
def p_mappa(k):
    nome='MF' if k==0 else f'M{k}';o=f'{W}/seg/{nome}.mkv'
    if ok(o):return o
    m=C.MAPPA_FINALE if k==0 else C.MAPPE[k]
    t=0.9;ev=[];tempi=[]
    w,d=vox(f'{nome}_0');ev.append((t,w,'v'));t+=d+0.5
    for i in range(1,len(m['rami'])+1):
        w,d=vox(f'{nome}_{i}');tempi.append(t);ev.append((t,w,'v'));t+=d+0.5
    tot=t+1.2;va=f'{W}/tmp/{nome}.wav';mix(ev,tot,va)
    json.dump(mappa_json(m),open(f'{W}/tmp/{nome}.json','w'),ensure_ascii=False)
    shutil.rmtree(f'{W}/tmp/{nome}_out',ignore_errors=True)
    sh([sys.executable,f'{KIT}/tools/mappa.py',f'{W}/tmp/{nome}.json','--out',f'{W}/tmp/{nome}_out','--voce',va,'--tempi',','.join(f'{x:.2f}' for x in tempi),'--solo-video'],env=ENV)
    sh(['ffmpeg','-y','-v','error','-i',f'{W}/tmp/{nome}_out/mappa.mp4','-map','0:v','-map','0:a','-vf','fps=30,format=yuv420p','-c:v','libx264','-preset','veryfast','-crf','17','-c:a','pcm_s16le','-ar','48000','-ac','2',o])
    done(o);return o
def p_final():
    o=f'{W}/seg/FIN.mkv'
    if ok(o):return o
    ev=[];t=0.9;items=[]
    for i,x in enumerate(C.RIEPILOGO_VOCE):
        w,d=vox(f'F_{i}');ev.append((t,w,'v'));t+=d+0.35
    tot=t+1.7-0.35
    items=[[a[0],''] for a in C.ARGOMENTI]
    schede_render({'type':'final','kicker':C.MATERIA,'l1':'RIEPILOGO','l2':'FINALE','items':items,'sub':'Ripassiamo insieme ciò che abbiamo imparato.','dur':tot},f'{W}/tmp/FIN.mp4')
    mix(ev,tot,f'{W}/tmp/FIN.wav');mux(f'{W}/tmp/FIN.mp4',f'{W}/tmp/FIN.wav',o);done(o);return o
def p_ripasso_p1():
    o=f'{W}/seg/RP.mkv'
    if ok(o):return o
    ev=[];t=0.9
    for i in range(len(C.RIPASSO_P1)):
        w,d=vox(f'RP_{i}');ev.append((t,w,'v'));t+=d+0.35
    tot=t+1.7-0.35
    schede_render({'type':'final','kicker':C.MATERIA+' · Parte 1','l1':'RIPASSO','l2':'PARTE 1','items':[[a[0],''] for a in C.ARGOMENTI[:4]],'sub':'Ripassiamo insieme la prima parte.','dur':tot},f'{W}/tmp/RP.mp4')
    mix(ev,tot,f'{W}/tmp/RP.wav');mux(f'{W}/tmp/RP.mp4',f'{W}/tmp/RP.wav',o);done(o);return o
def p_finale5():
    o=f'{W}/seg/FINE.mkv'
    if ok(o):return o
    sh(['ffmpeg','-y','-v','error','-i',f'{KIT}/sigle/Sigla_finale_5s_con_avviso_diritti.mp4','-i',SND+'/finale.wav','-map','0:v','-map','1:a','-vf','fps=30,format=yuv420p','-c:v','libx264','-preset','veryfast','-crf','17','-c:a','pcm_s16le','-ar','48000','-ac','2','-t','5',o]);done(o);return o
def p_sigla():
    f=f'{KIT}/sigle/Sigla_Diritto_15s.mp4'
    return None if not os.path.exists(f) else f
def tratto(n):return f'{W}/tratti/{n}.mkv'
# ---------------- ordine della lezione (le animazioni stanno al posto dei pezzi da 5 s)
def sequenza():
    S=[('cover',p_cover),('C0',lambda:tratto('C0'))]
    def T(k):return ('T%d'%k,lambda:p_titolo(k))
    A=lambda n:(n,lambda:p_anim(n));TR=lambda n:(n,lambda:tratto(n))
    ch=lambda k:[('M%d'%k,lambda:p_mappa(k)),('R%d'%k,lambda:p_repaso(k)),('S%d'%k,lambda:p_schema(k)),('Q%d'%k,lambda:p_quiz(k))]
    S+=[T(1),TR('T1')]+ch(1)
    S+=[T(2),A('N2a'),A('N2b'),A('N2c'),TR('T2')]+ch(2)
    S+=[T(3),A('N3a'),TR('T3')]+ch(3)
    S+=[T(4),A('N4a'),TR('T4'),A('N4b'),TR('T5')]+ch(4)
    S+=[T(5),A('N5a'),A('N5b'),TR('T6')]+ch(5)
    S+=[T(6)]+[A(n) for n in ['N6a','N6b','N6c','N6d','N6e','N6f']]+ch(6)+[TR('T7'),('MF',lambda:p_mappa(0)),('FIN',p_final),('FINE',p_finale5)]
    return S
if __name__=='__main__':
    S=sequenza();R={}
    for n,f in S:
        if n=='cover' and not os.path.exists(f'{VOX}/W01.wav'):print('manca W01');continue
        try:R[n]=f();print('ok',n,flush=True)
        except SystemExit as e:print('SALTATO',n,str(e)[:200],flush=True)
    json.dump({n:p for n,p in R.items()},open(W+'/pezzi.json','w'),indent=1)
