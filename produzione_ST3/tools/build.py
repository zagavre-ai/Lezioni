# Montaggio di una Parte. uso: build.py LEZ_DIR PARTE   (LEZ_DIR contiene doc.wav, doc48.wav, asr12.json, voci/, lav/dati.py)
import sys,os,json,re,glob,wave,subprocess,importlib.util
import numpy as np
sys.path.insert(0,'/home/user/lav/tools');sys.path.insert(0,'/home/user/Lezioni/kit/tools')
from lib import *
import sync,taglio
L=os.path.abspath(sys.argv[1]);PARTE=int(sys.argv[2])
spec=importlib.util.spec_from_file_location('dati',L+'/lav/dati.py');dati=importlib.util.module_from_spec(spec);spec.loader.exec_module(dati)
VOX=glob.glob(L+'/voci/scambio/*/vox')[0]
TJ=json.load(open(glob.glob(L+'/voci/scambio/*/testi_voci.json')[0]))
for k,v in dati.VOCI_CM.items():TJ.setdefault(k,v)
ASR=json.load(open(L+'/asr12.json'))
OUT=L+'/p%d/'%PARTE;PNG=OUT+'png/';PC=OUT+'pezzi/';AUD=OUT+'aud/'
for d in (OUT,PNG,PC,AUD):os.makedirs(d,exist_ok=True)
SR=48000
rend=None
def renderer():
    global rend
    if rend is None:rend=R()
    return rend
def png(name,html_):return renderer().png(html_,PNG+name+'.png')
# ---------- voci ----------
def stima(name):return max(8.0,sum(len(s.split()) for s in TJ[name])*0.48)
def voce(name):
    """audio stereo 48k normalizzato (-16 LUFS), oppure silenzio segnaposto"""
    f=VOX+'/%s.wav'%name;c=AUD+name+'.f32'
    if os.path.exists(f):
        if not os.path.exists(c):
            r=subprocess.run(['ffmpeg','-v','error','-i',f,'-af','loudnorm=I=-16:TP=-1.5:LRA=11','-ar',str(SR),'-ac','2','-f','f32le','-'],capture_output=True);open(c,'wb').write(r.stdout)
        return np.frombuffer(open(c,'rb').read(),np.float32).reshape(-1,2),True
    return np.zeros((int(stima(name)*SR),2),np.float32),False
def tempi_frasi(x,frasi):
    """inizio (s) di ogni frase nella voce x: proporzione dei caratteri + aggancio alla pausa piu' vicina"""
    m=np.abs(x.mean(1));h=int(0.02*SR);e=np.array([m[i:i+h].mean() for i in range(0,len(m)-h,h)])
    thr=max(e.max()*0.02,1e-4);voc=np.where(e>thr)[0]
    if len(voc)==0:return [0.0]*len(frasi)
    a,b=voc[0]*0.02,(voc[-1]+1)*0.02;ch=np.cumsum([0]+[len(f) for f in frasi]);tot=ch[-1]
    out=[]
    for i in range(len(frasi)):
        t=a+(b-a)*ch[i]/tot
        if i>0:
            lo,hi=int((t-0.9)/0.02),int((t+0.9)/0.02)
            seg=e[max(lo,0):hi];
            if len(seg)>3:
                # centro della pausa piu' lunga sotto soglia
                q=seg<thr*3;best=None;j=0
                while j<len(q):
                    if q[j]:
                        k=j
                        while k<len(q) and q[k]:k+=1
                        if best is None or k-j>best[1]-best[0]:best=(j,k)
                        j=k
                    else:j+=1
                if best:t=(max(lo,0)+(best[0]+best[1])/2)*0.02
        out.append(t)
    out[0]=0.0;return out
def scene_frames(starts,total_f):
    """starts in s -> lista frame per scena (somma = total_f)"""
    fr=[];pos=[nf(s) for s in starts]+[total_f]
    for i in range(len(starts)):fr.append(max(1,pos[i+1]-pos[i]))
    fr[-1]+=total_f-sum(fr);return fr
# ---------- pezzi ----------
TL=[];LISTA=[];DOCMAP={}
def verifica(f,n):
    c=int(sh(['ffprobe','-v','error','-count_packets','-select_streams','v:0','-show_entries','stream=nb_read_packets','-of','csv=p=0',f]).stdout)
    assert c==n,(f,c,n)
def audio_wav(path,x):
    x=np.clip(x,-1,1);d=(x*32767).astype('<i2')
    w=wave.open(path,'wb');w.setnchannels(2);w.setsampwidth(2);w.setframerate(SR);w.writeframes(d.tobytes());w.close()
def fit(x,frames):
    n=int(round(frames/FPS*SR))
    if len(x)>=n:return x[:n]
    return np.vstack([x,np.zeros((n-len(x),2),np.float32)])
def piece_still(name,scenes,x):
    """scenes [(png,frames)], x audio stereo (verra' adattato alla lunghezza)"""
    out=PC+name+'.mkv'
    total=sum(n for _,n in scenes)
    if not os.path.exists(out+'.ok'):
        concat_file(PC+name+'.txt',scenes);audio_wav(PC+name+'.wav',fit(x,total))
        sh(['ffmpeg','-y','-v','error','-f','concat','-safe','0','-i',PC+name+'.txt','-i',PC+name+'.wav','-map','0:v','-map','1:a','-vf','fps=30,format=yuv420p']+VENC+AENC+['-frames:v',str(total),out])
        verifica(out,total);open(out+'.ok','w').write('1')
    return out,total
def add(name,out,total,tag=None):
    t=sum(d for _,d in TL) if not TL else TL[-1][1]+TL[-1][2]
    TL.append([name,round(t,4),round(total/FPS,4)]);LISTA.append(out)
def add_still(name,scenes,x):
    o,n=piece_still(name,scenes,x);add(name,o,n)
def mix(base,events,total_f):
    """base zeros; events [(offset_s, audio)]"""
    y=np.zeros((int(round(total_f/FPS*SR)),2),np.float32)
    for off,a in events:
        i=int(off*SR);seg=a[:max(0,len(y)-i)];y[i:i+len(seg)]+=seg
    return y
def jingle(nm):
    p='/home/user/lav/kit/Telesio_kit_produzione_v1/home/claude/v5/snd/%s.wav'%nm
    r=subprocess.run(['ffmpeg','-v','error','-i',p,'-ar',str(SR),'-ac','2','-f','f32le','-'],capture_output=True)
    return np.frombuffer(r.stdout,np.float32).reshape(-1,2)
# ---------- schede ----------
def sig_iniziale():
    h=page_dark("STORIA · TERZO ANNO","Storia","Prof. Giorgio Mazzotti",bands=False,play=False)
    p=png('sigla',h);n=nf(15.0);add_still('SIGLA',[(p,n)],np.zeros((int(15*SR),2),np.float32))
def scheda_titolo(k,titolo):
    h=page_dark("ARGOMENTO %d"%k,titolo,"",bands=False,play=False,small="Storia · Prof. Giorgio Mazzotti")
    p=png('T%d'%k,h);n=nf(3.6);add_still('T%d'%k,[(p,n)],mix(None,[(0.0,jingle('titolo'))],n))
def scheda_quiz(k,titolo):
    h=page_dark("PAUSA DEL VIDEO · QUIZ",titolo,"5 domande · per continuare almeno l'80%")
    p=png('Q%d'%k,h);n=nf(4.0);add_still('Q%d'%k,[(p,n)],mix(None,[(0.5,jingle('quiz'))],n))
def vox_cards(name,kicker,title,start=None,wide=True,numbered=False,voce_name=None,prefix_drop=0,disp=None):
    """scene da una voce: ogni frase una carta; finestra di max 3"""
    x,ok=voce(voce_name or name);fr=TJ[voce_name or name]
    sents=[pulisci(s) for s in (disp or fr)]
    ts=tempi_frasi(x,fr);total=len(x)/SR
    total=max(total,1.0);n=nf(total)
    body=sents[prefix_drop:]
    scenes=[];idx=list(range(prefix_drop,len(fr)))
    starts=[ts[i] for i in idx]
    st=[0.0]+[s for s in starts[1:]]
    fr_l=scene_frames(st,n)
    for j,i in enumerate(idx):
        win=list(range(max(prefix_drop,i-2),i+1))
        cards=[sents[w] for w in win]
        html_=page_light(kicker,title,cards,len(win)-1,cam=False,wide=True)
        html_=html_
        scenes.append((png('%s_%d'%(name,j),html_),fr_l[j]))
    return scenes,x
def cardl(cards,active,kicker,title,**k):
    return page_light(kicker,title,cards,active,**k)
# ---------- docente ----------
def snap_t(t):
    t=taglio.snap(t,L+'/doc.wav') if 0<t<3600 else t
    return round(t*FPS)/FPS
def docente(name,k,t0,t1,intro_title=False):
    """pezzo del docente tra t0 e t1 (s sorgente) con slide sincronizzate"""
    out=PC+name+'.mkv';total=nf(t1-t0)
    if k==0:
        D=dati.D0;cards=D['cards'];kws=D['kws'];tit=D['tit'];img=D['img'];tt=D['t_title']
    else:
        tit,kws,cards=dati.ARG[k];img=dati.IMG.get(k);tt=0
    srcs=[c[1] for c in cards];t_ini=t0+tt
    act=sync.attiva(ASR,t_ini,t1,srcs)
    kick="STORIA · "+("INTRODUZIONE" if k==0 else "ARGOMENTO %d"%k)
    if not os.path.exists(out+'.ok'):
        items=[]
        if k==0:
            h=page_light("STORIA · TERZO ANNO",dati.TITOLO_LEZ.upper(),None,cam=True,kws=None)
            items.append((png('D0_titolo',h),nf(t_ini-t0)))
        bounds=[t_ini]+list(act[1:])+[t1]
        for i in range(len(cards)):
            win=list(range(max(0,i-2),i+1))
            h=page_light(kick,tit,[cards[w][0] for w in win],len(win)-1,cam=True,kws=kws,img=img)
            f=nf(bounds[i+1]-t0)-nf(bounds[i]-t0)
            items.append((png('D%d_%d'%(k,i),h),max(1,f)))
        tot=sum(n for _,n in items);items[-1]=(items[-1][0],items[-1][1]+total-tot)
        concat_file(PC+name+'.txt',items)
        fc="[0:v]fps=30,format=yuv420p[bg];[1:v]crop=245:139:826:321,scale=380:216:flags=lanczos,fps=30,format=yuv420p[c];[bg][c]overlay=1502:66:shortest=1[v]"
        src=glob.glob(L+'/LEZIONE*.mp4')[0]
        sh(['ffmpeg','-y','-v','error','-f','concat','-safe','0','-i',PC+name+'.txt','-ss',str(t0),'-t',str(total/FPS),'-i',src,'-ss',str(t0),'-t',str(total/FPS),'-i',L+'/doc48.wav',
            '-filter_complex',fc,'-map','[v]','-map','2:a']+VENC+AENC+['-frames:v',str(total),out])
        verifica(out,total);open(out+'.ok','w').write('1')
    DOCMAP[name]=[t0,t1];add(name,out,total)
# ---------- animazione (AN) ----------
def anim(n):
    name='AN%d'%n;tit=dati.AN_TIT[n]
    sc,x=vox_cards(name,"APPROFONDIMENTO · "+tit.upper(),tit)
    add_still(name,sc,x)
def ripasso(n):
    name='R%d'%n
    if name not in TJ:return
    x,ok=voce(name);fr=TJ[name];t=pulisci(fr[0]).replace('Ripassiamo: ','')
    h=page_light("RIPASSO BREVE","Ripassiamo",[t],0,wide=True)
    tot=nf(len(x)/SR+0.3);add_still(name,[(png(name,h),tot)],x)
def mappa_piece(k,stretta=False):
    name=k;x,ok=voce(k);fr=TJ[k];ts=tempi_frasi(x,fr)
    tit,rami=dati.MAPPE[k]
    js=dict(materia="Storia",docente="Prof. Giorgio Mazzotti",titolo=tit,rami=[dict(concetto=c,parola=p,esempio=e) for c,p,e,*_ in rami])
    od=PC+k+'_m/';os.makedirs(od,exist_ok=True)
    jf=od+'mappa.json';json.dump(js,open(jf,'w'),ensure_ascii=False)
    out=PC+k+'.mkv';hold=getattr(dati,'HOLD',(25,40))[1 if k.startswith('CMF') else 0]
    if not (os.path.exists(out+'.ok') and open(out+'.ok').read().split('|')[1]==str(int(ok))):
        wf=od+'voce.wav';audio_wav(wf,x)
        tm=','.join('%.2f'%t for t in ts[1:1+len(rami)])
        sh(['python3','/home/user/Lezioni/kit/tools/mappa.py',jf,'--out',od,'--voce',wf,'--tempi',tm])
        dd=dur(od+'mappa.mp4')+hold;tot=nf(dd)
        sh(['ffmpeg','-y','-v','error','-i',od+'mappa.mp4','-vf','fps=30,scale=1920:1080,format=yuv420p,tpad=stop_mode=clone:stop_duration=%d'%hold,'-af','aresample=48000,apad=pad_dur=%d'%hold]+VENC+AENC+['-frames:v',str(tot),'-t',str(tot/FPS),out]);verifica(out,tot)
        open(out+'.ok','w').write('%d|%d'%(tot,int(ok)))
    tot=int(open(out+'.ok').read().split('|')[0]);add(k,out,tot)
def glossario(name,kick='GLOSSARIO'):
    sc,x=vox_cards(name,kick,"Le parole chiave",prefix_drop=1)
    # la prima frase (introduzione) resta in audio: copri con la prima scena
    add_still(name,sc,x)
def card_text(name,kick,title,cards,x,nscene=None):
    h=page_light(kick,title,cards,0,wide=True)
    add_still(name,[(png(name,h),nf(len(x)/SR+0.3))],x)
def schede_finali(tit_part):
    h=page_dark("PAUSA DEL VIDEO","Verifica finale","Per proseguire rispondi al test della lezione")
    p=png('VER',h);n=nf(5.0);add_still('VER',[(p,n)],mix(None,[(0.5,jingle('quiz'))],n))
    sf=glob.glob('/home/user/lav/kit/sigle_zip/sigle/Sigla_finale_chiusura.mp4')[0]
    out=PC+'SFIN.mkv'
    if not os.path.exists(out+'.ok'):
        d=dur(sf);tot=nf(d)
        sh(['ffmpeg','-y','-v','error','-i',sf,'-vf','fps=30,scale=1920:1080,format=yuv420p','-af','aresample=48000,apad']+VENC+AENC+['-frames:v',str(tot),'-t',str(tot/FPS),out])
        open(out+'.ok','w').write(str(tot))
    add('SFIN',out,int(open(out+'.ok').read()))
    h=page_dark("COMPITI","Compiti per casa","",bands=True,play=False)
    p=png('CINTRO',h);n=nf(3.5);add_still('CINTRO',[(p,n)],np.zeros((int(3.5*SR),2),np.float32))
    h=page_dark("COMPITI","Compiti","Trovi la scheda dei compiti nella piattaforma",bands=True,play=False)
    p=png('COMP',h);n=nf(5.0);add_still('COMP',[(p,n)],np.zeros((int(5.0*SR),2),np.float32))
# ---------- regia delle Parti ----------
def regia():
    Q=json.load(open(L+'/quiz_argomenti.json'));arg=dati.PARTI[PARTE]
    cut=[0.0]+[snap_t(t) for t in dati.TAGLI[1:-1]]+[round(dati.TAGLI[-1]*FPS)/FPS]
    sig_iniziale()
    for it in dati.START[PARTE]:
        if it[0]=='intro':
            _,vn,kick,tt,cards=it;x,ok=voce(vn)
            h=page_light(kick,tt,cards,0,wide=True);add_still(vn,[(png(vn,h),nf(len(x)/SR+0.4))],x)
        elif it[0]=='rip':
            _,vn,kick,tt=it;sc,x2=vox_cards(vn,kick,tt,prefix_drop=1);add_still(vn,sc,x2)
        elif it[0]=='d0':
            docente('D0',0,cut[0],cut[1])
        elif it[0]=='an':
            for n in it[1]:anim(n)
    for k in arg:
        t=dati.ARG[k][0];scheda_titolo(k,t)
        docente('D%d'%k,k,cut[k],cut[k+1])
        for n in [n for n,a in dati.AN_ARG.items() if a==k]:anim(n)
        sc,xs=vox_cards('S%d'%k,"ARGOMENTO %d · SCHEMA DI RIPASSO"%k,t,prefix_drop=1);add_still('S%d'%k,sc,xs)
        mappa_piece('CM%d'%k);ripasso(k);scheda_quiz(k,Q['Q%d'%k]['title'])
    for it in dati.END[PARTE]:
        if it[0]=='tlf':
            sc,x=vox_cards(it[1],"LE DATE DELLA LEZIONE","Rimettiamo in fila le date",prefix_drop=1);add_still('TLF',sc,x)
        elif it[0]=='gl':glossario(it[1])
        elif it[0]=='cmf':mappa_piece(it[1])
        elif it[0]=='rf':
            sc,x=vox_cards(it[1],"RIPASSO FINALE",it[3],prefix_drop=1);add_still(it[2],sc,x)
        elif it[0]=='fin':
            x,ok=voce(it[1]);card_text('FIN1',it[2],it[3],[it[4]],x)
    schede_finali('')
    return
if __name__=='__main__':
    regia()
    # lista concat e timeline
    open(OUT+'lista.txt','w').write(''.join("file '%s'\n"%p for p in LISTA))
    json.dump(TL,open(OUT+'timeline.json','w'));json.dump(DOCMAP,open(OUT+'docmap.json','w'))
    tot=TL[-1][1]+TL[-1][2];print('DURATA %d:%04.1f'%(tot//60,tot%60),'pezzi',len(LISTA))
    if rend:rend.close()
