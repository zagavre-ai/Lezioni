# -*- coding: utf-8 -*-
# Montaggio di una lezione: python3 montaggio.py spec_modulo WORKDIR [--solo D|ALTRI|TUTTO]
# Ogni pezzo e' un mp4 1080p30 con audio; i pezzi gia' fatti (stessa firma) non si rifanno.
import sys,os,json,subprocess,importlib,hashlib,re,math,glob
sys.path.insert(0,'/home/user/work/build');sys.path.insert(0,'/home/user/Lezioni/kit/tools')
import grafica as G, anchors as AN, voci as VO
import numpy as np
S=importlib.import_module(sys.argv[1]);W=os.path.abspath(sys.argv[2])+'/'
MODO=sys.argv[3] if len(sys.argv)>3 else 'TUTTO'
for d in ['png','seg','vox','ph','mp']:os.makedirs(W+d,exist_ok=True)
SND='/home/user/work/kitzip/Telesio_kit_produzione_v1/home/claude/v5/snd/'
SIG='/home/user/work/kitzip/Telesio_sigle_v1/sigle/'
SIGLA_INIZ=SIG+'Sigla_Ideazione_progettazione_moda_15s.mp4';SIGLA_FIN=SIG+'Sigla_finale_chiusura.mp4'
SRC=W+S.SRC;M,D=S.MATERIA,S.DOCENTE
def sh(c,**k):
    r=subprocess.run(c,capture_output=True,text=True,**k)
    if r.returncode:raise RuntimeError(' '.join(map(str,c))[:300]+'\n'+r.stderr[-800:])
    return r.stdout
def dur(f):return float(sh(['ffprobe','-v','error','-show_entries','format=duration','-of','csv=p=0',f]).strip())
VT={v['nome']:v['testo'] for v in VO.costruisci(S)}
CUES={}
def reg(nome,nomi,V,ini,gap):
    t=ini;L=[]
    for n,(p,d,r) in zip(nomi,V):
        L.append([round(t,2),round(d,2),VT[n]]);t+=d+gap
    CUES[nome]=L
def voce(nome):
    """wav 48k stereo della voce Kore se c'e', altrimenti silenzio della durata stimata. Ritorna (percorso, durata, reale)"""
    for ext in ('wav','mp3','flac'):
        r=W+'vox/%s.%s'%(nome,ext)
        if os.path.exists(r) and os.path.getsize(r)>2000:
            o=W+'ph/%s_real.wav'%nome
            if not os.path.exists(o) or os.path.getmtime(o)<os.path.getmtime(r):
                sh(['ffmpeg','-v','error','-y','-i',r,'-ar','48000','-ac','2','-af','silenceremove=start_periods=1:start_threshold=-50dB,areverse,silenceremove=start_periods=1:start_threshold=-50dB,areverse',o])
            return o,dur(o),True
    o=W+'ph/%s_ph.wav'%nome;d=round(len(VT[nome])/14.5+0.3,2)
    if not os.path.exists(o):sh(['ffmpeg','-v','error','-y','-f','lavfi','-i','anullsrc=r=48000:cl=stereo','-t',str(d),o])
    return o,d,False
VENC=['-c:v','libx264','-preset','ultrafast','-crf','17','-pix_fmt','yuv420p','-r','30','-g','30']
AENC=['-c:a','aac','-b:a','192k','-ar','48000','-ac','2']
def fatto(nome,firma):
    f=W+'seg/%s.mp4'%nome;m=f+'.firma'
    return os.path.exists(f) and os.path.exists(m) and open(m).read()==firma
def segna(nome,firma):open(W+'seg/%s.mp4.firma'%nome,'w').write(firma)
def conc_audio(parti,gap,out,ini=0.0):
    """unisce wav con pause `gap` tra l'una e l'altra; ritorna tempi di inizio di ciascuna"""
    ins=[];fl=[];t=ini;T=[]
    if ini>0:ins+=['-f','lavfi','-t',str(ini),'-i','anullsrc=r=48000:cl=stereo']
    for p in parti:ins+=['-i',p]
    n0=1 if ini>0 else 0;lst=''.join('[%d:a]'%i for i in range(len(parti)+n0))
    # pause: usa apad su ciascuna parte
    f=''
    for k in range(len(parti)):
        f+='[%d:a]apad=pad_dur=%s[p%d];'%(k+n0,gap,k)
    seq=''.join('[p%d]'%k for k in range(len(parti)))
    if ini>0:seq='[0:a]'+seq
    f+=seq+'concat=n=%d:v=0:a=1[o]'%(len(parti)+n0)
    sh(['ffmpeg','-v','error','-y']+ins+['-filter_complex',f,'-map','[o]','-ar','48000','-ac','2',out])
    t=ini
    for p in parti:T.append(t);t+=dur(p)+gap
    return T
def card(png,d,audio,nome,firma,bande=False):
    """video fisso da png di durata d con audio (wav) opzionale; bande blu in entrata/uscita"""
    if fatto(nome,firma):return
    out=W+'seg/%s.mp4'%nome
    ins=['-loop','1','-framerate','30','-t','%.3f'%d,'-i',png]
    if audio:ins+=['-i',audio]
    else:ins+=['-f','lavfi','-t','%.3f'%d,'-i','anullsrc=r=48000:cl=stereo']
    fl='[0:v]format=yuv420p[v]'
    if bande:
        ins+=['-loop','1','-framerate','30','-t','%.3f'%d,'-i',W+'png/banda.png']
        r='min(100,min(250*t,250*(%.3f-t)))'%d
        fl='[2:v]split[b1][b2];[0:v][b1]overlay=0:\'-100+%s\'[a];[a][b2]overlay=0:\'H-%s\',format=yuv420p[v]'%(r,r)
    sh(['ffmpeg','-v','error','-y']+ins+['-filter_complex',fl,'-map','[v]','-map','1:a','-af','apad','-t','%.3f'%d]+VENC+AENC+[out])
    segna(nome,firma)
def mix_audio(d,voce_p,fx=None,voce_ini=0.0,out=None,fx_ini=0.0):
    ins=['-f','lavfi','-t','%.3f'%d,'-i','anullsrc=r=48000:cl=stereo'];fl=[];lab=['[0:a]']
    k=1
    if voce_p:
        ins+=['-i',voce_p];fl.append('[%d:a]adelay=%d|%d[v%d]'%(k,int(voce_ini*1000),int(voce_ini*1000),k));lab.append('[v%d]'%k);k+=1
    if fx:
        ins+=['-i',fx];fl.append('[%d:a]adelay=%d|%d[f%d]'%(k,int(fx_ini*1000),int(fx_ini*1000),k));lab.append('[f%d]'%k);k+=1
    sh(['ffmpeg','-v','error','-y']+ins+['-filter_complex',';'.join(fl)+(';' if fl else '')+''.join(lab)+'amix=inputs=%d:duration=first:normalize=0[o]'%len(lab),'-map','[o]','-t','%.3f'%d,'-ar','48000','-ac','2',out])
    return out
# ------------------------------------------------------------------ preparazione
def prepara_comuni():
    from PIL import Image,ImageDraw
    Image.new('RGB',(1920,100),(0x20,0x60,0xAF)).save(W+'png/banda.png')
    m=Image.new('L',(360*4,360*4),0);ImageDraw.Draw(m).ellipse((0,0,360*4-1,360*4-1),fill=255);m.resize((360,360),Image.LANCZOS).save(W+'png/maschera.png')
    r=Image.new('RGBA',(372*4,372*4),(0,0,0,0));ImageDraw.Draw(r).ellipse((0,0,372*4-1,372*4-1),fill=(255,230,0,255));ImageDraw.Draw(r).ellipse((6*4,6*4,366*4-1,366*4-1),fill=(0,0,0,0))
    r.resize((372,372),Image.LANCZOS).save(W+'png/anello.png')
def tagli():
    """inizio degli argomenti agganciato alla pausa piu' vicina (taglio.snap)"""
    from taglio import snap
    f=W+'tagli.json'
    if os.path.exists(f):return json.load(open(f))
    wav=W+'audio.wav';T=[]
    for a in S.ARGS:
        t=a['t0']
        if t>0:t=round(snap(t,wav,before=6.0,after=0.5),2)
        T.append(t)
    json.dump(T,open(f,'w'));return T
def anchor_arg(a,lo,hi,ch):
    f=W+'anch2_%d.json'%a['n']
    if os.path.exists(f):return json.load(open(f))
    cards=[c for s in a['slides'] for c in s['c']]
    ts,sc=AN.aggancia(ch,[AN.parole(c) for c in cards],lo,hi,[len(c) for c in cards])
    json.dump({'t':ts,'sc':sc},open(f,'w'));return {'t':ts,'sc':sc}
def seg_docente(a,lo,hi,ts):
    nome='D%d'%a['n'];L=hi-lo
    firma='v3|%.2f|%.2f|%s'%(lo,hi,hashlib.md5(json.dumps(ts).encode()).hexdigest())
    if fatto(nome,firma):return
    # stati: (png, inizio)
    kick='Argomento %d · %s'%(a['n'],a['titolo'])
    pn=[];tt=[];k=0;pag=[];us=[]
    for si,s in enumerate(a['slides']):
        for ci in range(len(s['c'])):
            u=W+'png/s%d_%d_%d.png'%(a['n'],si,ci)
            pag.append(G.slide(M,D,kick,s['t'],s['c'],ci));us.append(u)
            pn.append(u);tt.append(ts['t'][k]);k+=1
    u0=W+'png/s%d_t.png'%a['n'];pag.append(G.slide(M,D,kick,a['slides'][0]['t'],a['slides'][0]['c'],-1));us.append(u0)
    G.render(pag,us)
    # slide che cambia: il primo stato di una slide nuova parte 0,5 s prima del primo aggancio
    inizi=[lo]+[max(lo,t-0.0) for t in tt]
    seq=[(u0,lo)]+list(zip(pn,tt))
    fr=[];prev=None
    lst=''
    tl=[(p,max(lo,t)) for p,t in seq]
    # forza crescente
    out=[];last=lo-1
    for p,t in tl:
        if t<=last:t=last+0.04
        out.append((p,t));last=t
    out[0]=(out[0][0],lo)
    lines=[];F=0;N=int(round(L*30))
    for i,(p,t) in enumerate(out):
        e=out[i+1][1] if i+1<len(out) else hi
        f0=int(round((t-lo)*30));f1=int(round((e-lo)*30)) if i+1<len(out) else N
        n=max(1,f1-f0)
        while n>0:
            k=min(n,60);lines.append("file '%s'\nduration %.5f\n"%(p,k/30));n-=k
    lines.append("file '%s'\n"%out[-1][0])
    open(W+'seg/D%d.txt'%a['n'],'w').write(''.join(lines))
    cx,cy,r=S.CAM
    fl=("[1:v]crop=%d:%d:%d:%d,scale=360:360:flags=lanczos,unsharp=5:5:0.9,format=rgba,geq=r='r(X,Y)':g='g(X,Y)':b='b(X,Y)':a='if(lte(hypot(X-179.5,Y-179.5),180),255,0)'[cc];"
        "[0:v]fps=30[b];[b][cc]overlay=1525:290:shortest=1,format=yuv420p[v]")%(2*r,2*r,cx-r,cy-r)
    sh(['ffmpeg','-v','error','-y','-f','concat','-safe','0','-i',W+'seg/D%d.txt'%a['n'],'-ss','%.3f'%lo,'-t','%.3f'%L,'-i',SRC,
        '-filter_complex',fl,'-map','[v]','-map','1:a','-t','%.3f'%L]+VENC+AENC+[W+'seg/D%d.mp4'%a['n']])
    segna(nome,firma)
# ------------------------------------------------------------------ pezzi non-docente
def seg_titolo(a):
    nome='T%d'%a['n'];u=W+'png/t%d.png'%a['n'];G.render([G.titolo_arg(M,D,a['n'],a['titolo'])],[u])
    au=mix_audio(3.5,None,SND+'titolo.wav',out=W+'ph/t%d.wav'%a['n']);card(u,3.5,au,nome,'v1')
def seg_an(a):
    n=a['n'];an=a['an'];kick='Approfondimento · %s'%a['titolo']
    nomi=['AN%d_%d'%(n,k) for k in range(len(an['items'])+1)]
    V=[voce(x) for x in nomi];firma='v2|'+'|'.join('%.2f%s'%(d,'R' if r else 'p') for p,d,r in V)
    nome='AN%d'%n
    reg(nome,nomi,V,0.0,0.45)
    if fatto(nome,firma):return
    items=[(b,s) for b,s,f in an['items']]
    pag=[G.an(M,D,kick,an['t'],items,k) for k in range(len(items)+1)];us=[W+'png/an%d_%d.png'%(n,k) for k in range(len(items)+1)]
    G.render(pag,us)
    gap=0.45;du=[d+gap for p,d,r in V];au=W+'ph/an%d.wav'%n;conc_audio([p for p,d,r in V],gap,au)
    xfade_chain(us,du,0.35,au,W+'seg/%s.mp4'%nome);segna(nome,firma)
def xfade_chain(pngs,durs,f,audio,out):
    ins=[];n=len(pngs)
    for i,(p,d) in enumerate(zip(pngs,durs)):
        L=d+(f if i<n-1 else 0)
        ins+=['-loop','1','-framerate','30','-t','%.3f'%L,'-i',p]
    ins+=['-i',audio]
    fl='';cur='[0:v]';acc=durs[0]
    for i in range(1,n):
        fl+='%s[%d:v]xfade=transition=fade:duration=%.2f:offset=%.3f[x%d];'%(cur,i,f,acc,i);cur='[x%d]'%i;acc+=durs[i]
    fl+=cur+'format=yuv420p[v]'
    sh(['ffmpeg','-v','error','-y']+ins+['-filter_complex',fl,'-map','[v]','-map','%d:a'%n,'-t','%.3f'%sum(durs)]+VENC+AENC+[out])
def seg_mappa(nome,mp,pref,tit_kick):
    nomi=['%s_%d'%(pref,k) for k in range(len(mp['rami'])+1)]
    V=[voce(x) for x in nomi];firma='v3|'+'|'.join('%.2f%s'%(d,'R' if r else 'p') for p,d,r in V)
    reg(nome,nomi,V,0.8,0.5)
    if fatto(nome,firma):return
    wd=W+'mp/'+nome+'/';os.makedirs(wd,exist_ok=True)
    gap=0.5;T=conc_audio([p for p,d,r in V],gap,wd+'voce.wav',ini=0.8)
    mj=dict(materia=M,docente=D,titolo=mp['titolo'],rami=[dict(concetto=c,parola=p,esempio=e) for c,p,e in mp['rami']])
    json.dump(mj,open(wd+'mappa.json','w'),ensure_ascii=False)
    tempi=','.join('%.2f'%t for t in T[1:])
    sh([sys.executable,'/home/user/work/build/mappa_loc.py',wd+'mappa.json','--out',wd,'--voce',wd+'voce.wav','--tempi',tempi])
    sh(['ffmpeg','-v','error','-y','-i',wd+'mappa.mp4']+VENC+AENC+[W+'seg/%s.mp4'%nome]);segna(nome,firma)
def seg_ripasso(a):
    nome='R%d'%a['n'];pv,d,r=voce('R%d'%a['n']);firma='v2|%.2f%s'%(d,'R' if r else 'p');CUES[nome]=[[0.5,round(d,2),VT['R%d'%a['n']]]]
    u=W+'png/r%d.png'%a['n'];G.render([G.ripasso(M,D,'RIPASSO',a['titolo'],[x[0] for x in a['mappa']['rami']])],[u])
    dd=d+1.6;au=mix_audio(dd,pv,voce_ini=0.5,out=W+'ph/r%d.wav'%a['n']);card(u,dd,au,nome,firma)
def seg_quiz(a):
    nome='Q%d'%a['n'];u=W+'png/q%d.png'%a['n'];G.render([G.quiz(M,D,a['n'],a['titolo'])],[u])
    au=mix_audio(6.0,None,SND+'quiz.wav',out=W+'ph/q%d.wav'%a['n'],fx_ini=0.5);card(u,6.0,au,nome,'v3',bande=True)
def sfx(p):return '' if p==1 else str(p)
def seg_glossario(p,pt):
    nomi=['GL%d_%d'%(p,k) for k in range(len(pt['glossario'])+1)];V=[voce(x) for x in nomi]
    firma='v3|'+'|'.join('%.2f%s'%(d,'R' if r else 'p') for p,d,r in V);nome='GL%d'%p
    reg(nome,nomi,V,0.0,0.4)
    if fatto(nome,firma):return
    pag=[G.glossario(M,D,pt['glossario'],k) for k in range(len(pt['glossario'])+1)];us=[W+'png/gl%d_%d.png'%(p,k) for k in range(len(pag))]
    G.render(pag,us);gap=0.4;du=[d+gap for _,d,r in V];au=W+'ph/gl%d.wav'%p;conc_audio([x for x,d,r in V],gap,au)
    xfade_chain(us,du,0.3,au,W+'seg/%s.mp4'%nome);segna(nome,firma)
def seg_riepilogo(p,pt,nome,pref,titolo_kick):
    A={a['n']:a for a in S.ARGS}
    nomi=['%s_0'%pref]+['%s_%d'%(pref,n) for n in pt['args']];V=[voce(x) for x in nomi]
    firma='v3|'+'|'.join('%.2f%s'%(d,'R' if r else 'p') for _,d,r in V)
    reg(nome,nomi,V,0.0,0.4)
    if fatto(nome,firma):return
    ar=[A[n]['titolo'] for n in pt['args']];pag=[G.riepilogo(M,D,ar,k) for k in range(len(ar)+1)];us=[W+'png/%s_%d.png'%(nome,k) for k in range(len(pag))]
    G.render(pag,us);gap=0.4;du=[d+gap for _,d,r in V];au=W+'ph/%s.wav'%nome;conc_audio([x for x,d,r in V],gap,au)
    xfade_chain(us,du,0.3,au,W+'seg/%s.mp4'%nome);segna(nome,firma)
def seg_sigla(nome,src):
    if fatto(nome,'v1'):return
    sh(['ffmpeg','-v','error','-y','-i',src,'-vf','scale=1920:1080,fps=30,format=yuv420p']+VENC[:-4]+['-r','30','-g','30']+AENC+[W+'seg/%s.mp4'%nome]);segna(nome,'v1')
def seg_benvenuto(p):
    nome='BE'+sfx(p);vn='INTRO%d'%p
    pp,d,r=voce(vn);firma='v2|%.2f%s'%(d,'R' if r else 'p');u=W+'png/be%d.png'%p;CUES[nome]=[[0.4,round(d,2),VT[vn]]]
    G.render([G.scheda_unica(M,D,'BENVENUTI',S.TITOLO if p==1 else S.TITOLO+' · seconda parte',D)],[u]);dd=d+1.2
    au=mix_audio(dd,pp,voce_ini=0.4,out=W+'ph/%s.wav'%nome);card(u,dd,au,nome,firma)
def seg_chiusura(p,ultima):
    G.render([G.scheda_unica(M,D,'VERIFICA','Verifica finale','Rispondi alle domande del test'),G.scheda_unica(M,D,'COMPITI','Compiti','Svolgi le attività assegnate'),G.scheda_unica(M,D,'COMPITI','Compiti','')],
             [W+'png/fi.png',W+'png/co.png',W+'png/ci.png'])
    if ultima:
        au=mix_audio(5.0,None,SND+'quiz.wav',out=W+'ph/fi.wav',fx_ini=0.5);card(W+'png/fi.png',5.0,au,'FI%d'%p,'v3',bande=True)
    seg_sigla('SF'+sfx(p),SIGLA_FIN)
    if ultima:
        pp,d,r=voce('COMP1');dd=max(3.5,d+0.8);firma='v2|%.2f%s'%(dd,'R' if r else 'p');CUES['CI']=[[0.4,round(d,2),VT['COMP1']]]
        au=mix_audio(dd,pp,voce_ini=0.4,out=W+'ph/ci.wav');card(W+'png/ci.png',dd,au,'CI',firma)
        au=mix_audio(5.0,None,None,out=W+'ph/co.wav');card(W+'png/co.png',5.0,au,'CO','v2',bande=True)
# ------------------------------------------------------------------ main
def main():
    prepara_comuni();ch=json.load(open(W+'ali.json'));TG=tagli();tot=dur(SRC)
    PT=VO.parti(S);ORDINE={};idx={a['n']:i for i,a in enumerate(S.ARGS)};A={a['n']:a for a in S.ARGS}
    for p,pt in enumerate(PT,1):
        ordine=[]
        if MODO in('TUTTO','ALTRI'):
            seg_sigla('SI'+sfx(p),SIGLA_INIZ);seg_benvenuto(p);ordine+=['SI'+sfx(p),'BE'+sfx(p)]
            if p>1:
                seg_riepilogo(p,dict(args=PT[p-2]['args']),'RP%d'%p,'RPR%d'%p,'');ordine+=['RP%d'%p]
        for n in pt['args']:
            a=A[n];i=idx[n];lo=TG[i];hi=TG[i+1] if i+1<len(S.ARGS) else tot
            if MODO in('TUTTO','D'):
                ts=anchor_arg(a,lo,hi,ch);seg_docente(a,lo,hi,ts);print('D%d fatto'%a['n'],flush=True)
            if MODO in('TUTTO','ALTRI'):
                seg_titolo(a);seg_an(a);seg_mappa('MP%d'%a['n'],a['mappa'],'MP%d'%a['n'],'');seg_ripasso(a);seg_quiz(a);print('arg',a['n'],'altri fatti',flush=True)
            ordine+=['T%d'%a['n'],'D%d'%a['n'],'AN%d'%a['n'],'MP%d'%a['n'],'R%d'%a['n'],'Q%d'%a['n']]
        if MODO in('TUTTO','ALTRI'):
            seg_mappa('MF%d'%p,pt['mappa_finale'],'MPF' if len(PT)==1 else 'MPF%d'%p,'');seg_glossario(p,pt);seg_riepilogo(p,pt,'RF%d'%p,'RF%d'%p,'')
            seg_chiusura(p,p==len(PT))
            ordine+=['MF%d'%p,'GL%d'%p,'RF%d'%p]+(['FI%d'%p] if p==len(PT) else [])+['SF'+sfx(p)]+(['CI','CO'] if p==len(PT) else [])
        ORDINE[p]=ordine
    if MODO!='D':json.dump(ORDINE,open(W+'ordine.json','w'));json.dump(CUES,open(W+'cues_voci.json','w'),ensure_ascii=False)
main()
