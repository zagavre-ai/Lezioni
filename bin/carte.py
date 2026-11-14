# Schede e inserti (chat D2): segnaposto voci, schede scure, schemi con voce, chiusura, unione.
# uso: python3 carte.py NN segnaposto|schede|inserti|lista
import sys,os,json,re,subprocess,shutil,html
sys.path.insert(0,'/home/claude/w/bin');sys.path.insert(0,'/home/claude/v5')
from conf import CONF
import monta as M
NN=sys.argv[1];C=CONF[NN];D=M.D;V=D+'voci/';W=D+'m/';LT=1.3
SND='/home/claude/v5/snd/%s.wav';SIG='/home/claude/kitx/sigle/'
ENC=['-c:v','libx264','-preset','veryfast','-crf','18','-pix_fmt','yuv420p','-r','30','-g','60'];AP=['-c:a','pcm_s16le','-ar','48000','-ac','2']
run=M.run;dur=M.dur;E=html.escape
TV=json.load(open(V+'testi_voci.json'));QZ=json.load(open(V+'quiz_argomenti.json'));NA=len(C['arg'])
# ------------------------------------------------ voci: segnaposto (silenzio della durata stimata) o voci Kore vere
def meta(k):
    f=V+f'wav/meta_{k}.json'
    return json.load(open(f)) if os.path.exists(f) else None
def f_segnaposto():
    os.makedirs(V+'wav',exist_ok=True)
    for k,fr in TV.items():
        if meta(k) and meta(k).get('vera'):continue
        t=0.0;P=[]
        for s in fr:P.append(round(t,2));t+=len(s.split())/2.4+0.45
        run(['ffmpeg','-y','-v','error','-f','lavfi','-i','anullsrc=r=48000:cl=stereo','-t','%.2f'%t,V+f'wav/{k}.wav'])
        json.dump({'phrases':P,'dur':round(t,2),'vera':False},open(V+f'wav/meta_{k}.json','w'))
    print('segnaposto',len(TV))
# ------------------------------------------------ schede scure del modello (titolo, quiz, fine)
import dark
dark.JS=dark.JS.replace("${[...'Lezione 1 · ¿De dónde eres?'].map","${[...(sp.kicker||'')].map").replace('style="font-size:150px">RESUMEN</div>','style="font-size:150px">${sp.t1||"RIEPILOGO"}</div>').replace('style="font-size:150px;color:#E3A95C">RIEPILOGO</div>','style="font-size:120px;color:#E3A95C">${sp.t2||""}</div>')
dark.JS=dark.JS.replace("${[...'Pausa del video · Quiz'].map","${[...(sp.kk||'Pausa del video · Quiz')].map").replace('Rispondi · premi <b class=cy>Check</b> · poi <b class=cy>Continua</b>','${sp.hint||"Rispondi · premi <b class=cy>Check</b> · poi <b class=cy>Continua</b>"}')
def f_schede():
    os.makedirs(D+'dk',exist_ok=True);SP={}
    for i,A in enumerate(C['arg']):
        l=A['l'];SP[f'T{i+1}']={'type':'title','num':str(i+1).zfill(2),'total':NA,'lines':l,'ex':A['ex'],'fs':128 if max(len(x) for x in l)<17 else 104,'dur':3.6,'lineY':720 if len(l)==2 else 600}
        SP[f'Q{i+1}']={'type':'quiz','topic':A['t'],'act':f'Quiz {i+1}','pts':'5 domande · per continuare almeno l’80%','dur':4.0}
    SP['FIN1']={'type':'final','kicker':'Letteratura italiana','t1':'FINE','t2':'','items':[[a['t'],''] for a in C['arg']],'n0':1,'sub':' '.join(TV['FIN1']),'dur':round(max(8.0,meta('FIN1')['dur']+2.0),2)}
    SP['CI1']={'type':'quiz','kk':'Dopo la lezione','topic':'Esercizi da svolgere','act':'Compiti','pts':'Li trovi qui sotto, sulla pagina','hint':'Svolgili con calma dopo il video','dur':3.5}
    for k,s in SP.items():
        if os.path.exists(f'{D}dk/{k}.mp4'):continue
        dark.render(s,f'{D}dk/{k}',1.0);shutil.rmtree(f'{D}dk/{k}',ignore_errors=True);print(k,flush=True)
# ------------------------------------------------ schemi con voce (S, GL, RF, INTRO), Verifica e Compiti
def vslide(kick,title,cards,act,intro=None):
    cs=''
    for i,c in enumerate(cards):
        on=i==act
        st='background:#13234a;border:4px solid #FFE600;box-shadow:0 0 30px rgba(255,230,0,.35);opacity:1' if on else 'background:#101c3d;border:4px solid #2a3a66;opacity:%s'%('.55' if act is not None and i<act else '.38')
        m=re.match(r'^([^:]{2,40}):\s*(.*)$',c)
        tx=(f'<b style="color:#FFE600">{E(m.group(1))}:</b> {E(m.group(2))}' if m else E(c))
        cs+=f'<div style="display:flex;gap:26px;align-items:flex-start;border-radius:22px;padding:28px 36px;{st}"><div style="flex:none;width:54px;height:54px;border-radius:50%;background:{"#FFE600" if on else "#2a3a66"};color:#0B1530;font-weight:800;font-size:28px;display:flex;align-items:center;justify-content:center">{i+1}</div><div style="font-size:38px;line-height:1.3;color:#fff">{tx}</div></div>'
    return f"""<div style="position:absolute;inset:0;background:radial-gradient(1200px 700px at 80% 10%,#1b3270,#0B1530)"></div>
<div style="position:absolute;left:0;top:0;width:1920px;height:14px;background:#2060AF"></div>
<div class=mono style="position:absolute;left:120px;top:80px;font-size:28px;letter-spacing:6px;color:#5BD6F0">{E(kick)}</div>
<div class=brico style="position:absolute;left:120px;top:126px;width:1680px;font-size:64px;line-height:1.08;color:#fff">{E(title)}</div>
<div style="position:absolute;left:120px;top:{214 if len(title)<48 else 290}px;width:260px;height:8px;background:#FFE600;border-radius:4px"></div>
<div style="position:absolute;left:120px;top:{270 if len(title)<48 else 340}px;width:1680px;display:flex;flex-direction:column;gap:28px">{cs}</div>
<div class=mono style="position:absolute;left:120px;top:1020px;font-size:22px;color:#8f9bbd;letter-spacing:2px">{M.MAT} · {M.DOC}</div>
<img src="{M.URI('/home/claude/v5/logo_white.png')}" style="position:absolute;left:1600px;top:990px;width:200px">"""
def band(t1,t2):
    return f"""<div style="position:absolute;inset:0;background:#0B1530"></div><div style="position:absolute;left:0;top:0;width:1920px;height:120px;background:#2060AF"></div><div style="position:absolute;left:0;top:960px;width:1920px;height:120px;background:#2060AF"></div>
<div class=mono style="position:absolute;left:160px;top:380px;font-size:30px;letter-spacing:6px;color:#5BD6F0">{M.MAT}</div>
<div class=brico style="position:absolute;left:160px;top:430px;font-size:150px;color:#fff">{E(t1)}</div>
<div style="position:absolute;left:160px;top:640px;width:300px;height:10px;background:#FFE600;border-radius:5px"></div>
<div style="position:absolute;left:160px;top:690px;font-size:44px;font-weight:600;color:#E3E8F4">{E(t2)}</div>"""
def blocchi():
    """nome -> (kicker, titolo, frasi da mostrare come card, indice della frase per ogni card)"""
    B={}
    for i,A in enumerate(C['arg']):
        k=f'S{i+1}';fr=TV[k];B[k]=('SCHEMA DI RIPASSO',A['t'],fr[1:])
    B['GL1']=('PAROLE CHIAVE','Il glossario della lezione',TV['GL1'][1:-1])
    B['RF1']=('RIPASSO FINALE','Ricapitoliamo la lezione',TV['RF1'][1:-1])
    B['INTRO1']=('LETTERATURA ITALIANA',C['titolo'],[f'Argomento {i+1}: {a["t"]}' for i,a in enumerate(C['arg'])])
    return B
def pron(s):  # nella grafica i nomi si scrivono giusti (le voci li hanno in grafia fonetica)
    for a,b in [('Uismàns','Huysmans'),('Uàild','Wilde'),('Dorian Grei','Dorian Gray'),('Dez Essànt','Des Esseintes'),('Zolà','Zola'),('Dèndi','Dandy'),('dèndi','dandy'),('Prust','Proust'),('Vulf','Woolf'),('Nìcce','Nietzsche'),('Bergsòn','Bergson'),('Fròid','Freud'),('Àinstain','Einstein'),('Giudit','Judith'),('Scespir','Shakespeare')]:s=s.replace(a,b)
    for a,b in [('milleottocentoquarantotto','1848'),('milleottocentoottantaquattro','1884'),('milleottocentocinquantaquattro','1854'),('milleottocentonovantacinque','1895'),('millenovecentoventisei','1926'),('milleottocentosettantuno','1871'),('millenovecento','1900')]:s=s.replace(a,b)
    return s
def f_inserti():
    B=blocchi();pages=[]
    for k,(kick,tit,cards) in B.items():
        cards=[pron(c) for c in cards]
        groups=[cards[i:i+3] for i in range(0,len(cards),3)]
        pages.append((f'{k}_h',vslide(kick,pron(tit),groups[0],None)))
        for g,gr in enumerate(groups):
            for j in range(len(gr)):pages.append((f'{k}_{g}_{j}',vslide(kick,pron(tit),gr,j)))
    pages+=[('VER',band('Verifica finale','Rispondi alle domande del test')),('COMP',band('Compiti','Gli esercizi da svolgere dopo la lezione'))]
    M.shot(pages,D+'ins')
    # video degli schemi a tempo di voce
    for k,(kick,tit,cards) in B.items():
        m=meta(k);P=m['phrases'];DL=1.0;L=m['dur']+DL+1.6
        st=[(0.0,f'{k}_h')]
        n=len(cards)
        for c in range(n):
            # card c = frase c+1 della voce (INTRO: le card degli argomenti entrano con la seconda frase)
            if k=='INTRO1':t=P[1]+DL+c*0.9 if len(P)>1 else DL
            else:t=P[c+1]+DL
            st.append((t,f'{k}_{c//3}_{c%3}'))
        if k=='INTRO1':st.append((P[-1]+DL if len(P)>2 else L-1,f'{k}_h'))
        lst=W+f'{k}.ins.ffc';s='';T=[x[0] for x in st]+[L]
        for i,(t,png) in enumerate(st):
            dd=T[i+1]-t
            if dd>0:s+=f"file '{D}ins/{png}.png'\nduration {dd:.3f}\n"
        s+=f"file '{D}ins/{st[-1][1]}.png'\n";open(lst,'w').write(s)
        o=D+f'ins/{k}.mp4'
        if m.get('vera') or not os.path.exists(o):
            run(['ffmpeg','-y','-v','error','-f','concat','-safe','0','-i',lst,'-vf','fps=30,format=yuv420p','-t','%.3f'%L]+ENC+[o])
    for k,d in [('VER',5.0),('COMP',5.0)]:
        o=D+f'ins/{k}.mp4'
        if not os.path.exists(o):run(['ffmpeg','-y','-v','error','-loop','1','-framerate','30','-i',D+f'ins/{k}.png','-t',str(d)]+ENC+[o])
    print('inserti pronti')
# ------------------------------------------------ pezzi con margini LT (come asm_moda2) e unione con transizioni
def mix_clip(name,vid,jingle=None,joff=0.4,voice=None,voff=0.9,bed=False,minlen=None):
    o=W+name+'.mkv'
    if os.path.exists(o):return o
    dv=dur(vid);L=dv
    if voice and os.path.exists(voice):L=max(L,voff+dur(voice)+0.8)
    if minlen:L=max(L,minlen)
    tot=L+2*LT
    ins=['-i',vid,'-f','lavfi','-t','%.3f'%tot,'-i','anullsrc=r=48000:cl=stereo'];fl=f'[0:v]fps=30,scale=1920:1080,setsar=1,tpad=start_mode=clone:start_duration={LT}:stop_mode=clone:stop_duration={LT+L-dv:.3f},format=yuv420p[v];[1:a]anull[b0]';lab=['b0'];k=2
    if jingle:
        ins+=['-i',SND%jingle];fl+=f';[{k}:a]aformat=channel_layouts=stereo,aresample=48000,adelay={int((LT+joff)*1000)}|{int((LT+joff)*1000)},volume={0.55 if voice else 0.9}[b{k}]';lab.append(f'b{k}');k+=1
    if voice and os.path.exists(voice):
        ins+=['-i',voice];fl+=f';[{k}:a]loudnorm=I=-16:TP=-1.5,aresample=48000,aformat=channel_layouts=stereo,aresample=48000,adelay={int((LT+voff)*1000)}|{int((LT+voff)*1000)}[b{k}]';lab.append(f'b{k}');k+=1
    if bed:
        ins+=['-i','/home/claude/kitx/home/claude/moda_tec/audio/bed.wav'];fl+=f';[{k}:a]atrim=0:{L:.3f},afade=t=in:d=1.2,afade=t=out:st={L-1.5:.3f}:d=1.5,aformat=channel_layouts=stereo,aresample=48000,volume=0.6,adelay={int(LT*1000)}|{int(LT*1000)}[b{k}]';lab.append(f'b{k}');k+=1
    fl+=';'+''.join(f'[{l}]' for l in lab)+f'amix=inputs={len(lab)}:normalize=0:duration=first[a]'
    run(['ffmpeg','-y','-v','error']+ins+['-filter_complex',fl,'-map','[v]','-map','[a]','-t','%.3f'%tot]+ENC+AP+[o]);return o
def sigla(name,src):
    o=W+name+'.mkv'
    if os.path.exists(o):return o
    run(['ffmpeg','-y','-v','error','-i',src,'-filter_complex',f'[0:v]fps=30,scale=1920:1080,setsar=1,format=yuv420p,tpad=start_mode=clone:start_duration={LT}:stop_mode=clone:stop_duration={LT}[v];[0:a]loudnorm=I=-18:TP=-1.5,aresample=48000,aformat=channel_layouts=stereo,adelay={int(LT*1000)}|{int(LT*1000)},apad=pad_dur={LT}[a]','-map','[v]','-map','[a]','-t','%.3f'%(dur(src)+2*LT)]+ENC+AP+[o]);return o
XK={'toT':('circleopen',1.3),'fromT':('circleclose',1.3),'toR':('wipeleft',1.2),'toS':('fade',1.0),'toQ':('zoomin',1.2),'fromQ':('circleclose',1.3),'toAN':('fade',1.0),'fromAN':('fade',1.0),'toFIN':('wipeleft',1.2),'def':('fade',1.0)}
KIND={('D','T'):'toT',('T','D'):'fromT',('D','S'):'toR',('S','Q'):'toQ',('Q','T'):'fromQ',('Q','A'):'fromQ',('A','A'):'toAN',('A','F'):'toFIN',('C','D'):'fromAN',('G','C'):'def'}
def join(seq):
    parts=[];tl=[];t=0.0
    for k,(n,f,ty) in enumerate(seq):
        d=dur(f);a=0.0 if k==0 else LT;b=d-LT if k<len(seq)-1 else d
        if k>0:
            pn,pf,pt=seq[k-1];kn,xd=XK[KIND.get((pt,ty),'def')]
            tr=W+f'x_{pn}_{n}.mkv'
            if not os.path.exists(tr):
                run(['ffmpeg','-y','-v','error','-sseof','-%.3f'%LT,'-i',pf,'-t','%.3f'%LT,'-i',f,'-filter_complex',
                     f'[0:v]fps=30,trim=duration={LT},setpts=PTS-STARTPTS[a0];[1:v]fps=30,trim=duration={LT},setpts=PTS-STARTPTS[b0];[a0][b0]xfade=transition={kn}:duration={xd}:offset={LT-xd:.3f},format=yuv420p[v];[0:a]atrim=duration={LT},asetpts=PTS-STARTPTS[x];[1:a]atrim=duration={LT},asetpts=PTS-STARTPTS[y];[x][y]acrossfade=d={xd}[a]',
                     '-map','[v]','-map','[a]','-max_muxing_queue_size','9999','-t','%.3f'%(2*LT-xd)]+ENC+AP+[tr])
            parts.append(tr);t+=dur(tr)
        body=W+f'b_{n}.mkv'
        if not os.path.exists(body):
            run(['ffmpeg','-y','-v','error','-ss','%.3f'%a,'-t','%.3f'%(b-a),'-i',f]+ENC+AP+[body])
        tl.append((n,round(t,3),round(dur(body),3)));parts.append(body);t+=dur(body)
    return parts,tl,t
def sequenza():
    VW=V+'wav/'
    S=[('SIGLA',sigla('SIG0',SIG+'Sigla_Letteratura_15s.mp4'),'G'),
       ('INTRO1',mix_clip('INTRO1',D+'ins/INTRO1.mp4',None,0,VW+'INTRO1.wav',1.0,bed=True),'C'),
       ('D0',W+'D0.mkv','D')]
    for i in range(1,NA+1):
        S+=[(f'T{i}',mix_clip(f'T{i}',D+f'dk/T{i}.mp4','titolo',0.45),'T'),(f'D{i}',W+f'D{i}.mkv','D'),
            (f'S{i}',mix_clip(f'S{i}',D+f'ins/S{i}.mp4','repaso',0.0,VW+f'S{i}.wav',1.0,bed=True),'S'),
            (f'Q{i}',mix_clip(f'Q{i}',D+f'dk/Q{i}.mp4','quiz',0.5),'Q')]
    S+=[('GL1',mix_clip('GL1',D+'ins/GL1.mp4','trans',0.0,VW+'GL1.wav',1.0,bed=True),'A'),
        ('RF1',mix_clip('RF1',D+'ins/RF1.mp4','trans',0.0,VW+'RF1.wav',1.0,bed=True),'A'),
        ('FIN1',mix_clip('FIN1',D+'dk/FIN1.mp4','finale',0.4,VW+'FIN1.wav',1.0),'F'),
        ('VER',mix_clip('VER',D+'ins/VER.mp4'),'V'),
        ('SFIN',sigla('SFIN',SIG+'Sigla_finale_chiusura.mp4'),'G'),
        ('CI1',mix_clip('CI1',D+'dk/CI1.mp4','quiz',0.5),'I'),
        ('COMP',mix_clip('COMP',D+'ins/COMP.mp4'),'V')]
    return S
def f_lista():
    parts,tl,t=join(sequenza())
    open(D+'lista.txt','w').write(''.join("file '%s'\n"%p for p in parts))
    json.dump(tl,open(D+'timeline.json','w'),indent=0)
    d={n:(a,l) for n,a,l in tl}
    print('durata totale %.1f s = %d:%04.1f'%(t,t//60,t%60),'| docente %.1f s'%sum(l for n,a,l in tl if n.startswith('D')),'| t_verifica %.2f t_compiti %.2f'%(d['VER'][0],d['COMP'][0]))
if __name__=='__main__':
    for f in sys.argv[2:]:globals()['f_'+f]()
