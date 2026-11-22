import sys,json,re,os,wave,numpy as np,subprocess
sys.path.insert(0,'/tmp/w/b')
from audio import *
VT=json.load(open('/tmp/w/src/vox_tr.json'))
TV={x['nome']:x['testo'] for x in json.load(open('/tmp/w/old/testi_voci.json'))}
def read(path):
    with wave.open(path) as w:
        n=w.getnframes();a=np.frombuffer(w.readframes(n),dtype=np.int16).reshape(-1,w.getnchannels());return a
def concat_voices(outname,names,gap=0.45,gaps=None,srcs=None):
    """concatena voci gia' a 48k stereo; ritorna (wav,starts,durata)"""
    out=f'/tmp/w/b/aud/{outname}.wav';os.makedirs('/tmp/w/b/aud',exist_ok=True)
    parts=[];starts=[];t=0.0
    for i,n in enumerate(names):
        g=(gaps[i] if gaps else (0 if i==0 else gap))
        if g: parts.append(np.zeros((int(g*48000),2),np.int16));t+=g
        p=(srcs or {}).get(n) or prep_voice(n)
        a=read(p);starts.append(t);parts.append(a);t+=len(a)/48000
    a=np.concatenate(parts)
    with wave.open(out,'wb') as w:
        w.setnchannels(2);w.setsampwidth(2);w.setframerate(48000);w.writeframes(a.tobytes())
    return out,starts,t
def sentences(txt):
    s=re.split(r'(?<=[.?!])\s+',txt.strip())
    return [x for x in s if x]
def sentence_times(name,txt,srcs=None):
    """inizio (s) di ogni frase del testo nella voce `name`, allineando per proporzione di lettere sui token ASR"""
    E=VT[name];tok=E['parole']
    letters=[len(re.sub(r'[^a-zA-Z0-9]','',w)) for _,w in tok];tot=sum(letters)
    cum=np.cumsum([0]+letters)
    S=sentences(txt);ls=[len(re.sub(r'[^a-zA-Z0-9]','',x)) for x in S];lt=sum(ls)
    out=[];acc=0
    for l in ls:
        target=acc/lt*tot
        j=int(np.searchsorted(cum,target,side='left'));j=min(j,len(tok)-1)
        out.append(0.0 if acc==0 else max(0.0,tok[j][0]-0.15));acc+=l
    return S,out
def word_time(name,phrase,after=0.0):
    """tempo del primo token della frase (cerca nella stringa dei token)"""
    E=VT[name];tok=E['parole'];s='';pos=[]
    for t,w in tok:
        pos.append((len(s),t));s+=w.lower()
    key=phrase.lower()
    i=s.find(key.replace(' ',''))
    if i<0:
        s2=''.join(w.lower() for _,w in tok);i=s2.replace(' ','').find(key.replace(' ',''))
    # indice su stringa senza spazi
    s3='';pos3=[]
    for t,w in tok:
        for ch in w.lower():
            if ch!=' ': pos3.append(t);s3+=ch
    k=s3.find(re.sub(r'[^a-z0-9àèéìòù]','',key))
    # cerca la prima occorrenza dopo `after`
    while k>=0 and pos3[k]<after: k=s3.find(re.sub(r'[^a-z0-9àèéìòù]','',key),k+1)
    return pos3[k] if k>=0 else None

import re as _re
_U={'uno':1,'un':1,'due':2,'tre':3,'tré':3,'quattro':4,'cinque':5,'sei':6,'sette':7,'otto':8,'nove':9}
_T={'dieci':10,'undici':11,'dodici':12,'tredici':13,'quattordici':14,'quindici':15,'sedici':16,'diciassette':17,'diciotto':18,'diciannove':19}
_D={'venti':20,'trenta':30,'quaranta':40,'cinquanta':50,'sessanta':60,'settanta':70,'ottanta':80,'novanta':90}
def _lt100(w):
    if w=='' : return 0
    if w in _U: return _U[w]
    if w in _T: return _T[w]
    for d,v in _D.items():
        if w==d: return v
        if w.startswith(d) or w.startswith(d[:-1]):
            rest=w[len(d):] if w.startswith(d) else w[len(d)-1:]
            if rest in _U and rest!='un': return v+_U[rest]
            if w.startswith(d[:-1]) and rest in ('uno','otto'): return v+_U[rest]
    return None
def _lt1000(w):
    if w=='': return 0
    m=_re.match(r'^(?:(due|tre|quattro|cinque|sei|sette|otto|nove))?(?:cent(?=ottant)|cento)(.*)$',w)
    if m:
        h=_U.get(m.group(1),1)*100;r=_lt100(m.group(2));return None if r is None else h+r
    return _lt100(w)
def num(w):
    w=w.lower()
    m=_re.match(r'^(?:(due|tre|quattro|cinque|sei|sette|otto|nove)mila|mille)(.*)$',w)
    if m:
        th=(_U[m.group(1)] if m.group(1) else 1)*1000;r=_lt1000(m.group(2));return None if r is None else th+r
    return _lt1000(w)
def digits(txt):
    def f(m):
        w=m.group(0);v=num(w)
        if v is not None and (v>=20 or 'cento' in w or 'mil' in w): return str(v)
        return w
    return _re.sub(r"[A-Za-zàèéìòù]+",f,txt)
