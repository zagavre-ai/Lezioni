import json,re,unicodedata
def norm(w):
    w=unicodedata.normalize('NFD',w.lower());w=''.join(c for c in w if not unicodedata.combining(c))
    return re.sub(r'[^a-z0-9]','',w)
STOP=set('della delle degli dello nella nelle nello sono viene vengono tutti tutte questo questa quello anche molto dopo prima ogni come quindi quale quali cosi cio dal dai dalle dagli sul sulla sulle degli negli nei tra fra gli una uno per con che non piu era essere stato state hanno aveva fatto'.split())
def keys(text):
    ws=[norm(x) for x in re.split(r'\s+',text)]
    return {w[:6] for w in ws if len(w)>=4 and w not in STOP}
def assign(segs,cards,t0,t1):
    """segs: [{inizio,fine,testo,parole}] ; ritorna lista [(t, card_idx)] cambi di evidenziazione, card_idx -1 = nessuna"""
    K=[keys(a+' '+b) for a,b in cards]
    ev=[];cur=-1;last_t=None
    win=[]
    for s in segs:
        if s['fine']<t0 or s['inizio']>t1: continue
        # per ogni parola del segmento
        for t,w in s['parole']:
            if t<t0 or t>t1: continue
            win.append((t,norm(w)[:6]))
    # finestra scorrevole di 14 s
    import bisect
    ts=[t for t,_ in win]
    t=t0
    res=[]
    while t<=t1:
        i0=bisect.bisect_left(ts,t-3);i1=bisect.bisect_right(ts,t+11)
        W=[w for _,w in win[i0:i1]]
        sc=[len(set(W)&k) for k in K]
        res.append((t,sc))
        t+=1.0
    return res
