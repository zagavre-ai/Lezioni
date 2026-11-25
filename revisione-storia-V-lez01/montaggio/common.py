import json,re,bisect
W='/tmp/w'
SEG=json.load(open(W+'/tr/orig.json'))
SIL=json.load(open(W+'/sil.json'))
WORDS=[]  # (t, text, segidx)
for i,s in enumerate(SEG):
    for t,w in s['parole']: WORDS.append((t,w,i))
def sent_end_before(a):
    # a = silence start; find last word before a, check its segment ends w/ terminal punct and that word is last of segment
    k=bisect.bisect_left([w[0] for w in WORDS],a)-1
    if k<0: return False
    t,w,i=WORDS[k]
    s=SEG[i]
    last=s['parole'][-1][0]
    if abs(last-t)>1e-6: return False
    tx=s['testo'].strip()
    return bool(re.search(r'[.?!]["»]?$',tx)) and not tx.endswith('...')
def cut(target,win=25):
    best=None
    for a,b in SIL:
        if b-a<0.45: continue
        if abs(a-target)>win: continue
        if not sent_end_before(a): continue
        d=abs(a-target)
        if best is None or d<best[0]: best=(d,a,b)
    return best
if __name__=='__main__':
    for tg in [120,1132,1636,2184,2370,2795,3284,3636,4071,4525,4647]:
        c=cut(tg)
        if c:
            a,b=c[1],c[2]
            k=bisect.bisect_left([w[0] for w in WORDS],a)-1
            nxt=''.join(w[1] for w in WORDS[k+1:k+8])
            prv=''.join(w[1] for w in WORDS[max(0,k-7):k+1])
            print(tg,round(a,2),round(b,2),'|',prv,'||',nxt)
        else: print(tg,None)

def cands2(tg,win=20,mingap=0.3):
    out=[]
    for i in range(len(SEG)-1):
        s,n=SEG[i],SEG[i+1]
        tx=s['testo'].strip()
        if not re.search(r'[.?!]["»]?$',tx) or tx.endswith('...'): continue
        gap=n['inizio']-s['fine']
        if gap<mingap or abs(s['fine']-tg)>win: continue
        out.append((round(n['inizio']-0.15,2),round(gap,2),tx[-40:],n['testo'][:50]))
    return out
