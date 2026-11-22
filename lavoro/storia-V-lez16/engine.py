import json,subprocess,os,re,math,hashlib
W='/home/user/w';B=W+'/build';FPS=30
S=json.load(open(W+'/out/trasc.json'))
CAM=(900,344,181,136)   # x,y,w,h della webcam 4:3 nel video originale (1092x614)
def sh(c,**k):
    r=subprocess.run(c,capture_output=True,text=True,**k)
    if r.returncode:raise RuntimeError('rc=%s '%r.returncode+' '.join(map(str,c))[:200]+'\n'+r.stderr[-1500:])
    return r
def dur(f):return float(sh(['ffprobe','-v','error','-show_entries','format=duration','-of','csv=p=0',f]).stdout)
def nframes(f):return int(sh(['ffprobe','-v','error','-count_packets','-select_streams','v:0','-show_entries','stream=nb_read_packets','-of','csv=p=0',f]).stdout)
def fr(t):return round(t*FPS)
# ---- parole con tempi
def _words():
    out=[]
    for s in S:
        cur=None
        for t,tok in s['parole']:
            if tok.startswith(' ') or cur is None:
                if cur:out.append(cur)
                cur=[t,tok.strip()]
            else:cur[1]+=tok
        if cur:out.append(cur)
    return out
WORDS=_words()
def norm(w):
    import unicodedata
    return re.sub(r'[^a-z0-9]','',unicodedata.normalize('NFD',w.lower()).encode('ascii','ignore').decode())
def tw(frase,dopo=0.0):
    """tempo d'inizio della prima occorrenza (dopo 'dopo') della sequenza di parole"""
    k=[norm(x) for x in frase.split()]
    ws=[(t,norm(w)) for t,w in WORDS]
    for i in range(len(ws)):
        if ws[i][0]<dopo:continue
        if all(i+j<len(ws) and ws[i+j][1]==k[j] for j in range(len(k))):return ws[i][0]
    raise KeyError(frase)
# ---- tagli: intervalli originali [a,b] di un pezzo del docente (seg s0..s1), pause >2,5 s accorciate a ~1 s
def chunk_ranges(s0,s1,lead=0.55,tail=0.40,maxpause=2.5,keep=1.0):
    a=max(S[s0]['inizio']-lead,(S[s0-1]['fine']+0.10) if s0>0 else 0.0)
    nxt=S[s1+1]['inizio'] if s1+1<len(S) else S[s1]['fine']+1
    b=min(S[s1]['fine']+tail,nxt-0.17)
    rr=[];cur=a
    for i in range(s0,s1):
        g0=S[i]['fine'];g1=S[i+1]['inizio']
        if g1-g0>maxpause:
            rr.append((cur,g0+keep/2));cur=g1-keep/2
    rr.append((cur,b))
    sn=lambda x:round(x*30)/30
    return [(sn(x),sn(y)) for x,y in rr]
def build_map(rr):
    m=[];o=0.0
    for a,b in rr:m.append((a,b,o));o+=b-a
    return m,o
def to_edit(m,t):
    for a,b,o in m:
        if a<=t<=b:return o+t-a
    if t<m[0][0]:return 0.0
    return m[-1][2]+(m[-1][1]-m[-1][0])
