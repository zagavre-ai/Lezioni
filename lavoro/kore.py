# Pezzi con voce Kore (o provvisoria): scene a stati con dissolvenza, audio da file.
import os, re, subprocess, math, json, wave, struct
import numpy as np
import sys
sys.path.insert(0,'/home/user/Lezioni/lavoro')
import mont
from mont import sh, B, dur
VOX=['/tmp/w/vox_new','/tmp/w/voxrepo/scambio/storia-V-lez10/vox']   # prima le nuove, poi le vecchie
TESTI={x['nome']:x['testo'] for x in json.load(open('/tmp/w/old_testi.json'))}
for x in json.load(open('/tmp/w/voci/testi_voci.json')): TESTI[x['nome']]=x['testo']
PROV=[]   # voci provvisorie usate
def vox(nome):
    """percorso WAV (reale se c'è, altrimenti provvisorio silenzioso di durata stimata) e flag"""
    for d in VOX:
        p=f'{d}/{nome}.wav'
        if os.path.exists(p): return p,True
    p=f'{B}/prov/{nome}.wav';os.makedirs(os.path.dirname(p),exist_ok=True)
    if not os.path.exists(p):
        t=TESTI[nome];s=max(1.5,len(t.split())/2.45+0.6)
        sh(['ffmpeg','-v','error','-y','-f','lavfi','-i',f'anullsrc=r=24000:cl=mono','-t',f'{s:.2f}','-c:a','pcm_s16le',p])
    if nome not in PROV: PROV.append(nome)
    return p,False
def vdur(nome): return dur(vox(nome)[0])
# --- numeri in lettere -> cifre (solo per il testo a schermo) ---
U={'uno':1,'due':2,'tre':3,'quattro':4,'cinque':5,'sei':6,'sette':7,'otto':8,'nove':9,'dieci':10,'undici':11,'dodici':12,'tredici':13,'quattordici':14,'quindici':15,'sedici':16,'diciassette':17,'diciotto':18,'diciannove':19}
TN={'venti':20,'trenta':30,'quaranta':40,'cinquanta':50,'sessanta':60,'settanta':70,'ottanta':80,'novanta':90}
UNI={'uno':1,'due':2,'tre':3,'quattro':4,'cinque':5,'sei':6,'sette':7,'otto':8,'nove':9}
TEEN={'dieci':10,'undici':11,'dodici':12,'tredici':13,'quattordici':14,'quindici':15,'sedici':16,'diciassette':17,'diciotto':18,'diciannove':19}
TENS={'venti':20,'trenta':30,'quaranta':40,'cinquanta':50,'sessanta':60,'settanta':70,'ottanta':80,'novanta':90}
def _small(w):
    if w=='':return 0
    if w in UNI:return UNI[w]
    if w in TEEN:return TEEN[w]
    for t,v in TENS.items():
        if w==t:return v
        stem=t[:-1]
        if w.startswith(stem):
            r=w[len(stem):]
            for u,uv in UNI.items():
                if r in (('i' if t=='venti' else 'a')+u,) :return v+uv
                if u in('uno','otto') and r==u:return v+uv
    return None
def parse_it(w):
    w=w.lower().replace('é','e').replace('è','e')
    if not re.fullmatch(r'[a-z]+',w):return None
    tot=0
    m=re.match(r'^(mille|(\w+?)mila)(?=\w|$)',w)
    if m:
        if m.group(1)=='mille':tot+=1000
        else:
            p=_small(m.group(2))
            if not p:return None
            tot+=1000*p
        w=w[m.end():]
    m=re.match(r'^(due|tre|quattro|cinque|sei|sette|otto|nove)?cento',w)
    if m:
        tot+=100*(UNI[m.group(1)] if m.group(1) else 1);w=w[m.end():]
    s=_small(w)
    if s is None:return None
    tot+=s
    return tot if tot else None
MESI='gennaio|febbraio|marzo|aprile|maggio|giugno|luglio|agosto|settembre|ottobre|novembre|dicembre'
def digits(t):
    t=re.sub(r'\b(\w+)\s+per\s+cento\b',lambda m:(str(parse_it(m.group(1)))+'%') if parse_it(m.group(1)) else m.group(0),t)
    def rep(m):
        w=m.group(1);v=parse_it(w)
        if v and v>=100: s=str(v);return (f'{v:,}'.replace(',','.') if v>=10000 else s)+m.group(2)
        if v and v>=10 and re.match(r'\s+('+MESI+')',t[m.end(1):m.end(1)+12]): return str(v)+m.group(2)
        return m.group(0)
    t=re.sub(r"\b([A-Za-zàèéìòù]+)\b()",rep,t)
    t=re.sub(r'\bsei milioni\b','6 milioni',t);t=re.sub(r'\bottocentomila\b','800.000',t)
    return t
# --- sincronizzazione sulle pause della voce ---
def _read(wav):
    with wave.open(wav) as w:
        sr=w.getframerate();d=np.frombuffer(w.readframes(w.getnframes()),np.int16).astype(np.float32)/32768
    return d,sr
def pause_runs(wav,thr=0.012,minlen=0.18):
    x,sr=_read(wav);fr=int(sr*0.01);n=len(x)//fr
    r=np.sqrt((x[:n*fr].reshape(n,fr)**2).mean(1));out=[];cur=None
    for i,v in enumerate(r):
        if v<thr:
            if cur is None:cur=i
        else:
            if cur is not None and (i-cur)/100>=minlen:out.append((cur/100,i/100))
            cur=None
    return out,n/100
def tempi_unita(nome,unita):
    """inizio (s) di ciascuna unità di testo letta nella voce `nome`: proporzionale ai caratteri, agganciato alle pause"""
    wav,real=vox(nome);d=dur(wav);L=[len(u)+2 for u in unita];tot=sum(L);acc=0;stim=[]
    for l in L:stim.append(d*acc/tot);acc+=l
    if not real:return stim,d
    runs,_=pause_runs(wav);ts=[0.0];used=-1
    for k in range(1,len(unita)):
        cand=[(abs((a+b)/2-stim[k]),(a+b)/2,j) for j,(a,b) in enumerate(runs) if j>used and (a+b)/2>ts[-1]+0.4]
        if cand:
            e,t,j=min(cand)
            if e<0.18*d/len(unita)+1.2:ts.append(t);used=j;continue
        ts.append(stim[k])
    return ts,d
# --- scena a stati con dissolvenza ---
FADE=0.35
def scena(nome,stati,audio,tot,out,lead=0.6,tail=0.9,gain_db=0.0,extra_audio=None):
    """stati: [(t_inizio_s_relativo_alla_voce, png)] ; la voce parte a `lead`; durata totale = lead+tot+tail (30 fps esatti)"""
    D=round((lead+tot+tail)*30)/30
    st=sorted(stati,key=lambda x:x[0]);times=[0.0]+[max(0.0,t+lead-FADE/2) for t,_ in st[1:]]
    ins=[];fc=[]
    for i,(t,png) in enumerate(st):
        t_end=(times[i+1]+FADE if i+1<len(st) else D+FADE)
        ins+=['-loop','1','-framerate','30','-t',f'{t_end-times[i]:.3f}','-i',png]
    if len(st)==1: fc.append('[0:v]format=yuv420p[vo]')
    else:
        cur='[0:v]'
        for i in range(1,len(st)):
            fc.append(f'{cur}[{i}:v]xfade=transition=fade:duration={FADE}:offset={times[i]:.3f}[x{i}]');cur=f'[x{i}]'
        fc.append(f'{cur}format=yuv420p[vo]')
    ai=len(st)
    ins+=['-i',audio]
    fc.append(f'[{ai}:a]aresample=48000,adelay={int(lead*1000)}:all=1,volume={gain_db}dB,apad=whole_dur={D:.3f},atrim=0:{D:.3f}[ao]')
    sh(['ffmpeg','-v','error','-y']+ins+['-filter_complex',';'.join(fc),'-map','[vo]','-map','[ao]','-frames:v',str(round(D*30)),'-r','30','-c:v','libx264','-preset','veryfast','-crf','14','-pix_fmt','yuv420p','-c:a','pcm_s16le','-ar','48000',out])
    return D
