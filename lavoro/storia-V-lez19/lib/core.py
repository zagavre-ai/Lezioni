import json,re,os,subprocess,sys,math
sys.path.insert(0,'/home/claude/w19/lib')
W='/home/claude/w19'
SEG=json.load(open(W+'/trasc.json'))
VD=json.load(open(W+'/vox_dur.json'))
FILL={'um','uh','mm','eh','ehm','ah'}
def sh(c,**k): return subprocess.run(c,capture_output=True,text=True,**k)
def norm(s): return re.sub(r'[^a-zàèéìòù ]','',s.lower()).strip()
# ---- confini: solo fine di frase vera (punto/?/! e segmento seguente che comincia con maiuscola o pausa >= 0,3 s)
def fine_frase(k):
    t=SEG[k]['testo'].strip()
    if not re.search(r'[.?!]["»”]?$',t) or t.endswith('...') or t.endswith('…'): return False
    if k+1<len(SEG):
        n=SEG[k+1]['testo'].strip()
        if n and n[0].islower() and SEG[k+1]['inizio']-SEG[k]['fine']<0.3: return False
    return True
def snap_fine(t):
    """indice del segmento che chiude una frase, la cui fine è più vicina a t"""
    c=[k for k in range(len(SEG)) if fine_frase(k)]
    return min(c,key=lambda k:abs(SEG[k]['fine']-t))
def snap_inizio(t):
    """indice del primo segmento di una frase (il precedente chiude una frase) con inizio più vicino a t"""
    c=[k+1 for k in range(len(SEG)-1) if fine_frase(k)]+[0]
    return min(c,key=lambda k:abs(SEG[k]['inizio']-t))
def ranges(a,b):
    """a,b = indici del primo e ultimo segmento (frase intera all'inizio e alla fine). Ritorna lista di (t0,t1) dell'originale,
    senza segmenti-riempitivo isolati (Um, Uh, Mm) e con pause > 2,5 s accorciate a circa 1 s; i tagli stanno nelle pause."""
    gp=SEG[a]['inizio']-(SEG[a-1]['fine'] if a>0 else 0)
    t0=SEG[a]['inizio']-max(0.15,min(0.30,gp-0.08))
    gn=(SEG[b+1]['inizio'] if b+1<len(SEG) else SEG[b]['fine']+1)-SEG[b]['fine']
    t1=SEG[b]['fine']+max(0.12,min(0.35,gn-0.10))
    R=[];cur=t0
    for k in range(a,b):
        s,n=SEG[k],SEG[k+1]
        gap=n['inizio']-s['fine']
        # riempitivo isolato in mezzo
        if norm(n['testo']) in FILL and k+2<=b:
            R.append((cur,s['fine']+0.15));cur=n['fine']+ (0.15 if k+2<len(SEG) else 0)
            continue
        if norm(s['testo']) in FILL and k==a: continue
        if gap>2.5:
            R.append((cur,s['fine']+0.6));cur=n['inizio']-0.4
    R.append((cur,t1))
    # elimina intervalli piccoli o invertiti
    return [(round(x,3),round(y,3)) for x,y in R if y-x>0.3]
def dur_r(R): return sum(y-x for x,y in R)
def rel(R,t):
    """tempo originale -> tempo nel pezzo montato"""
    acc=0
    for x,y in R:
        if t<x: return acc
        if t<=y: return acc+(t-x)
        acc+=y-x
    return acc
def tabella_fine(a,b):
    w=SEG[b]['testo'].split()
    return dict(minuto=f"{int(SEG[b]['fine']//60)}:{int(SEG[b]['fine']%60):02d}",ultime=' '.join(w[-8:]),frase_finita=fine_frase(b))
