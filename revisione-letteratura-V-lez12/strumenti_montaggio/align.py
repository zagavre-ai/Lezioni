import json,re,unicodedata,difflib
V=json.load(open('/home/user/w/trasc_V.json'))
def nrm(w):
    w=unicodedata.normalize('NFD',w.lower());w=''.join(c for c in w if c.isalpha())
    return w[:5]
def asr_words(a,b):
    out=[];cur=None
    for s in V:
        if s['fine']<a or s['inizio']>b: continue
        for t,p in s['parole']:
            if not(a<=t<b): continue
            if p.startswith(' ') or cur is None:
                if cur: out.append(cur)
                cur=[t,p.strip()]
            else: cur[1]+=p
    if cur: out.append(cur)
    return [(t,w) for t,w in out if nrm(w)]
def starts(sentences,a,b):
    """tempo (relativo ad a) in cui comincia ogni frase, dall'allineamento con il parlato riconosciuto"""
    aw=asr_words(a,b);sw=[];first=[]
    for s in sentences:
        first.append(len(sw));sw+= [w for w in re.findall(r"[\wàèéìòùÀÈÉÌÒÙ']+",s) if nrm(w)]
    A=[nrm(w) for w in sw];B=[nrm(w) for t,w in aw]
    m=difflib.SequenceMatcher(None,A,B,autojunk=False)
    mp={}
    for i,j,n in m.get_matching_blocks():
        for k in range(n): mp[i+k]=j+k
    res=[]
    for f in first:
        k=f
        while k<len(A) and k not in mp and k<f+4: k+=1
        if k in mp: res.append(aw[mp[k]][0]-a-0.15)
        else: res.append(None)
    # interpolazione dei mancanti
    for i,x in enumerate(res):
        if x is None: res[i]=(res[i-1]+0.5) if i>0 and res[i-1] is not None else 0.5
    return [max(0,x) for x in res]
if __name__=='__main__':
    import sys
    T=json.load(open('/home/user/w/testi_altri.json'))
    print([round(x,1) for x in starts(T['S1'],568.667,613.133)])
    print([round(x,1) for x in starts(T['GL1'],3253.3,3313.266)])

def spoken_time(a,b,words,after,window=30):
    """primo istante (relativo ad a) in cui una delle parole è pronunciata dopo 'after'"""
    keys=[nrm(w) for w in words if len(re.sub(r'\W','',w))>3]
    for t,w in asr_words(a,b):
        if t-a>=after and t-a<=after+window and nrm(w) in keys[:3]: 
            if nrm(w)==keys[0] or True: return t-a
    return None
def word_times(text,a,b):
    sw=[w for w in text.split(' ')]
    aw=asr_words(a,b)
    A=[nrm(w) for w in sw];B=[nrm(w) for t,w in aw]
    m=difflib.SequenceMatcher(None,A,B,autojunk=False);mp={}
    for i,j,n in m.get_matching_blocks():
        for k in range(n): mp[i+k]=aw[j+k][0]-a
    return mp
