# Costruzione dei pezzi del prof: slide a finestra sincronizzate + riquadro 4:3 + audio ripulito.
import os,re,json,subprocess,sys
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from spec import *
import grafica as G
SRC='/home/user/Lezioni/w/orig/lez9.mp4'
W='/home/user/Lezioni/w/lav/out';os.makedirs(W,exist_ok=True)
MAXGAP=150.0
def silenzi():
    f=W+'/silenzi.json'
    if os.path.exists(f):return json.load(open(f))
    r=subprocess.run(['ffmpeg','-v','info','-i',SRC,'-vn','-af','silencedetect=n=-38dB:d=0.3','-f','null','-'],capture_output=True,text=True).stderr
    st=[float(x) for x in re.findall(r'silence_start: ([\d.]+)',r)];en=[float(x) for x in re.findall(r'silence_end: ([\d.]+)',r)]
    L=list(zip(st,en));json.dump(L,open(f,'w'));return L
_X=None
def _x():
    global _X
    if _X is None:
        import numpy as np
        _X=np.frombuffer(subprocess.run(['ffmpeg','-v','error','-i',SRC,'-vn','-ac','1','-ar','16000','-f','f32le','-'],capture_output=True).stdout,np.float32)
    return _X
def _rms(a,b):
    import numpy as np
    s=_x()[int(a*16000):int(b*16000)];return float(np.sqrt(np.mean(s**2))) if len(s) else 0.0
def snap(t0,t1,L=None,soglia=0.012):
    """tagli nelle pause: inizio fino a 0,15 s prima della frase, fine fino a 0,25 s dopo, solo se lì c'è silenzio"""
    a0=t0
    for k in range(1,4):
        if _rms(t0-0.05*k,t0-0.05*(k-1))<soglia:a0=t0-0.05*k
        else:break
    a1=t1
    for k in range(1,6):
        if _rms(t1+0.05*(k-1),t1+0.05*k)<soglia:a1=t1+0.05*k
        else:break
    return a0,a1
def segmenti(t0,t1,L,maxp=2.5,keep=1.0):
    """intervalli sorgente da tenere: le pause > maxp si accorciano a ~keep"""
    cuts=[(a,b) for a,b in L if a>t0 and b<t1 and b-a>maxp]
    out=[];cur=t0
    for a,b in cuts:
        out.append((cur,a+keep/2));cur=b-keep/2
    out.append((cur,t1));return out
def mappa(segs):
    """sorgente -> uscita"""
    acc=0;tab=[]
    for a,b in segs:tab.append((a,b,acc));acc+=b-a
    def f(t):
        for a,b,o in tab:
            if a<=t<=b:return o+t-a
        for a,b,o in tab:
            if t<a:return o
        return acc
    return f,acc
def finestre(eventi,tot,cards,title):
    """eventi: [(t_out, key)] in ordine ; cards: key->testo. Ritorna stati [(t_out_inizio, cards_visibili(keys), acceso(key) , focus)]"""
    stati=[];win=None;wstart=0
    keys_seq=[k for t,k in eventi]
    with G.R() as r:
        def fits(ks,on):
            inner,bar=G.pagina(title,[cards[k] for k in ks],None)
            return r.heights(G.doc(inner,'','',bar))<=955
        for i,(t,k) in enumerate(eventi):
            if win is None or k not in win or t-wstart>MAXGAP:
                # nuova finestra: k + successive carte uniche
                ks=[k]
                for j in range(i+1,len(eventi)):
                    kk=eventi[j][1]
                    if kk in ks:continue
                    if len(ks)<3 and fits(ks+[kk],None):ks.append(kk)
                    else:break
                if len(ks)==1 and i>0:   # almeno 2 carte se possibile: aggiungi la precedente
                    pk=eventi[i-1][1]
                    if pk!=k and fits([pk,k],None):ks=[pk,k]
                win=sorted(ks,key=lambda x:list(cards).index(x));wstart=t
            stati.append([t,list(win),k,False])
    # inserisce varianti 'focus' se un tratto resta uguale oltre MAXGAP
    out=[];
    for i,s in enumerate(stati):
        out.append(s)
        fine=stati[i+1][0] if i+1<len(stati) else tot
        t=s[0];n=0
        while fine-t>MAXGAP+30:
            t+=MAXGAP-10;n+=1
            out.append([t,s[1],s[2],n%2==1])
    return out

CAM=(846+30,343,185,139)   # x,y,w,h ritaglio 4:3 della webcam originale
KW={1:['Leggi Fascistissime','Alfredo Rocco','Capo del Governo'],2:['Podestà','Tribunale speciale','OVRA','confino'],3:['Gran Consiglio','elezioni plebiscitarie','Stato etico'],
    4:['Dopolavoro','Balilla','sabato fascista','GUF'],5:['Riforma Gentile','libro di testo unico'],6:['Patti Lateranensi','questione romana','Concordato'],
    7:['corporativismo','INPS','dazi'],8:['Quota 90','IMI e IRI','bonifica integrale','autarchia'],9:['battaglia demografica','ONMI'],10:['Etiopia','Asse Roma-Berlino','Manifesto della Razza']}
SIGLE={'PNF':'Partito Nazionale Fascista','OVRA':'Opera volontaria repressione antifascismo (polizia segreta)','OND':'Opera Nazionale Dopolavoro','ONB':'Opera Nazionale Balilla',
 'GUF':'Gruppi Universitari Fascisti','EIAR':'Ente Italiano per le Audizioni Radiofoniche','LUCE':'L’Unione Cinematografica Educativa','MinCulPop':'Ministero della Cultura Popolare',
 'INFPS':'Istituto Nazionale Fascista della Previdenza Sociale','INPS':'Istituto Nazionale della Previdenza Sociale','IMI':'Istituto Mobiliare Italiano','IRI':'Istituto per la Ricostruzione Industriale',
 'ONMI':'Opera Nazionale Maternità e Infanzia','AOI':'Africa Orientale Italiana'}
def sigle_in(ks,cards):
    t=' '.join(cards[k] for k in ks);o=[]
    for s,e in SIGLE.items():
        if re.search(r'\b'+re.escape(s)+r'\b',t) and e.lower().split(' (')[0] not in t.lower():o.append((s,e))
    return o
def build(n,pagnum0,out_mp4,t0=None,t1=None,prefix=None,anchors=None):
    """pezzo del prof per l'argomento n"""
    L=silenzi();a0,a1=arg_range(n)
    t0=a0 if t0 is None else t0;t1=a1 if t1 is None else t1
    t0,t1=snap(t0,t1,L);segs=segmenti(t0,t1,L);f,tot=mappa(segs)
    cards={};ev=[]
    for p,i,a in CARDS[n]:
        k=f'{p}.{i}';cards[k]=card(p,i);ev.append((f(SEG[seg_at(a)]['inizio']),k))
    # ordine di visualizzazione = ordine di pagina/indice
    cards=dict(sorted(cards.items(),key=lambda kv:tuple(int(x) for x in kv[0].split('.'))))
    title=ARGS[n][1]
    stati=finestre(ev,tot,cards,title)
    imm=[(f(mmss(a)),f(mmss(b)),fn) for fn,a,b in IMMAGINI.get(n,[])]
    return dict(n=n,segs=segs,tot=tot,stati=stati,cards=cards,imm=imm,title=title)

import shutil
KIT='/home/user/Lezioni/w/kit_wt/kit'
CHAIN='highpass=f=80,afftdn=nr=4:nf=-45:tn=0'
def guadagno():
    f=W+'/gain.json'
    if os.path.exists(f):return json.load(open(f))['g']
    r=subprocess.run(['ffmpeg','-v','info','-i',SRC,'-vn','-af',CHAIN+',ebur128=framelog=quiet','-f','null','-'],capture_output=True,text=True).stderr
    I=float(re.findall(r'I:\s+(-?[\d.]+) LUFS',r)[-1]);g=-16-I;json.dump({'I':I,'g':g},open(f,'w'));return g
def seq_pagine(d,pag0):
    """sequenza cronologica di pagine: [(t,'win'|'focus'|'img',ks,on,fn,tb,pag)] e ultima pagina"""
    st=list(d['stati'])
    if st[0][0]>0.5:st=[[0.0,st[0][1],None,False]]+st
    ev=[(s[0],0,s) for s in st]+[(a,1,(a,fn,b)) for a,b,fn in d['imm']]
    ev.sort(key=lambda e:(e[0],e[1]));out=[];pag=pag0;last=None;cur_ks=None
    for t,k,x in ev:
        if k==1:
            pag+=1;out.append((t,'img',None,None,x[1],x[2],pag))
        else:
            _,win,on,focus=x;ks=tuple(win)
            if focus:out.append((t,'focus',ks,on,None,None,pag if last==ks else pag));continue
            if ks!=last:pag+=1;last=ks
            out.append((t,'win',ks,on,None,None,pag))
    return out,pag
def render_stati(d,pag0,dirp):
    os.makedirs(dirp,exist_ok=True);cards=d['cards'];title=d['title'];n=d['n']
    seq,pag=seq_pagine(d,pag0);ev=[];winpag={}
    with G.R() as r:
        for t,kind,ks,on,fn,tb,pg in seq:
            if kind=='img':
                cap=IMMCAP.get(fn,'')
                h=G.doc(f'<img class="img" src="file:///home/user/Lezioni/w/imgs/{fn}" style="left:80px;top:290px;height:650px;max-width:1290px">',f'ARGOMENTO {n}',cap,259,pg,True,KW.get(n))
                p=f'{dirp}/i{len(ev):03d}.png';r.shot(h,p);ev.append((t,p,tb));continue
            if kind=='focus':
                inner,bar=G.pagina(title,[cards[on]],0)
                inner=inner.replace('class="card on"','class="card on" style="font-size:46px;line-height:1.45"')
            else:
                sg=sigle_in(ks,cards);inner,bar=G.pagina(title,[cards[k] for k in ks],(list(ks).index(on) if on in ks else None),sg or None)
            h=G.doc(inner,('RIEPILOGO' if n==11 else f'ARGOMENTO {n}'),title,bar,pg,True,KW.get(n))
            p=f'{dirp}/s{len(ev):03d}.png';r.shot(h,p);ev.append((t,p))
    return ev,pag
IMMCAP={'i-005.jpg':'Mussolini dal balcone di Palazzo Venezia','i-006.jpg':'La propaganda: il fascismo non accetta un «no»','i-010.jpg':'I Balilla e l’addestramento militare',
        'i-014.jpg':'La firma dei Patti Lateranensi','i-018.jpg':'La battaglia del grano','i-021.jpg':'Un simbolo del fascismo: il Palazzo della Civiltà italiana','i-024.jpg':'La guerra d’Etiopia (1935-1936)'}

def timeline(ev):
    base=[(e[0],e[1]) for e in ev if len(e)==2];base.sort()
    tl=list(base)
    for e in ev:
        if len(e)==3:
            ta,p,tb=e;tl.append((ta,p))
            # stato attivo a tb
            act=[b for b in base if b[0]<=tb];tl.append((tb,(act[-1] if act else base[0])[1]))
    tl.sort(key=lambda x:x[0]);return tl
def prep(d,tag):
    """taglia sorgente: cam ritagliata (mp4 piccolo) e audio ripulito (wav) con pause accorciate"""
    cam=W+f'/{tag}_cam.mkv';aud=W+f'/{tag}_aud.wav';g=guadagno()
    x,y,w,h=CAM;parts_v=[];parts_a=[]
    for i,(a,b) in enumerate(d['segs']):
        pv=W+f'/{tag}_v{i}.mkv';pa=W+f'/{tag}_a{i}.wav'
        subprocess.run(['ffmpeg','-v','error','-y','-ss',f'{a:.3f}','-t',f'{b-a:.3f}','-i',SRC,'-an','-vf',f'crop={w}:{h}:{x}:{y},fps=30','-c:v','libx264','-preset','ultrafast','-crf','10',pv],check=True)
        subprocess.run(['ffmpeg','-v','error','-y','-ss',f'{a:.3f}','-t',f'{b-a:.3f}','-i',SRC,'-vn','-ac','2','-ar','48000',pa],check=True)
        parts_v.append(pv);parts_a.append(pa)
    for nm,ps,ext in (('v',parts_v,cam),('a',parts_a,aud+'.raw.wav')):
        lf=W+f'/{tag}_{nm}.txt';open(lf,'w').write('\n'.join(f"file '{p}'" for p in ps))
        subprocess.run(['ffmpeg','-v','error','-y','-f','concat','-safe','0','-i',lf,'-c','copy' if nm=='v' else 'pcm_s16le',ext] if nm=='v' else ['ffmpeg','-v','error','-y','-f','concat','-safe','0','-i',lf,'-c:a','pcm_s16le',ext],check=True)
    subprocess.run(['ffmpeg','-v','error','-y','-i',aud+'.raw.wav','-af',f'{CHAIN},volume={g:.2f}dB,alimiter=limit=0.89:level=0','-ar','48000',aud],check=True)
    for p in parts_v+parts_a:os.remove(p)
    return cam,aud
def ffcmd(d,tl,out,prev_png=None,trans=True,tag='x'):
    tot=d['tot'];cam,aud=prep(d,tag)
    lst=W+f'/c_{tag}.txt';L=[]
    for i,(t,p) in enumerate(tl):
        fine=tl[i+1][0] if i+1<len(tl) else tot
        L.append(f"file '{p}'\nduration {max(fine-t,1/30):.4f}")
    L.append(f"file '{tl[-1][1]}'");open(lst,'w').write('\n'.join(L))
    base=W+f'/{tag}_base.mkv';clips=[];bounds=[round(t*30) for t,_ in tl]+[round(tot*30)]
    for i,(t,png) in enumerate(tl):
        nfr=max(bounds[i+1]-bounds[i],1);cp=W+f'/{tag}_clip{i:02d}.mkv'
        subprocess.run(['ffmpeg','-v','error','-y','-loop','1','-framerate','30','-i',png,'-frames:v',str(nfr),'-vf','format=yuv420p','-c:v','libx264','-preset','ultrafast','-crf','12','-g','60','-r','30',cp],check=True);clips.append(cp)
    open(W+f'/{tag}_clips.txt','w').write('\n'.join(f"file '{c}'" for c in clips))
    subprocess.run(['ffmpeg','-v','error','-y','-f','concat','-safe','0','-i',W+f'/{tag}_clips.txt','-c','copy',base],check=True)
    for c in clips:os.remove(c)
    fc=[];cmd=['ffmpeg','-v','error','-y','-i',base,'-i',cam,'-i',aud]
    fc.append("[1:v]scale=412:309:flags=lanczos,unsharp=5:5:0.7,eq=contrast=1.04:saturation=1.05,format=rgba,geq=r='r(X,Y)':g='g(X,Y)':b='b(X,Y)':a='if(gt(hypot(max(0,abs(X-205.5)-189.5),max(0,abs(Y-154)-138)),16),0,255)'[cam]")
    fc.append("[0:v]format=rgba[bg];[bg][cam]overlay=1428:148:format=auto:shortest=1[vb]")
    ai=3
    if prev_png:
        cmd+=['-loop','1','-framerate','30','-t','0.6','-i',prev_png];ai+=1
        fc.append(f"[{ai-1}:v]format=rgba[pv];[vb]fade=t=in:st=0:d=0.5:alpha=1[vf];[pv][vf]overlay=shortest=1:format=auto,format=yuv420p[vo]")
    else:fc.append("[vb]format=yuv420p[vo]")
    if trans:
        cmd+=['-i',KIT+'/suoni/trans.wav']
        fc.append(f"[{ai}:a]atrim=0:1.3,volume=0.45,afade=t=out:st=0.6:d=0.7,aformat=channel_layouts=stereo,aresample=48000[tr];[2:a]aformat=channel_layouts=stereo[ap];[ap][tr]amix=inputs=2:duration=first:normalize=0[ao]")
    else:fc.append("[2:a]anull[ao]")
    cmd+=['-filter_complex',';'.join(fc),'-map','[vo]','-map','[ao]','-t',f'{tot:.3f}','-c:v','libx264','-preset','veryfast','-crf','16','-pix_fmt','yuv420p','-r','30','-c:a','pcm_s16le','-ar','48000',out]
    return cmd
HERE=os.path.dirname(os.path.abspath(__file__))

RIEP_TITLES={2:'La fascistizzazione dello Stato',4:'La gioventù fascista',5:'La scuola fascista',6:'I media e i Patti Lateranensi',9:'Il ruolo della donna e la demografia',7:'Il corporativismo e l’agricoltura',8:'Quota 90, Stato imprenditore e autarchia',10:'Politica estera, impero e Leggi Razziali'}
RIEP_EV=[('60:26',2),('60:37',4),('61:17',5),('62:00',6),('63:14',9),('63:51',7),('64:46',8),('65:37',10)]
def build_riep():
    L=silenzi();t0,t1=arg_range(11);t0,t1=snap(t0,t1,L);segs=segmenti(t0,t1,L);f,tot=mappa(segs)
    cards={f'r{k}':RIEP_TITLES[k] for _,k in RIEP_EV};ev=[(f(SEG[seg_at(a)]['inizio']),f'r{k}') for a,k in RIEP_EV]
    cards=dict(sorted(cards.items(),key=lambda kv:[k for _,k in RIEP_EV].index(int(kv[0][1:]))))
    stati=finestre(ev,tot,cards,'Riepilogo della lezione')
    return dict(n=11,segs=segs,tot=tot,stati=stati,cards=cards,imm=[],title='Riepilogo della lezione')
