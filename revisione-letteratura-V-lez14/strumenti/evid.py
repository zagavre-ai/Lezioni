import json,re,collections
W=json.load(open('tr/orig.json'))
def ricostruisci(W):
    out=[];cur=None
    for sg in W:
        for t,w in sg['parole']:
            if w.startswith(' ') or cur is None:
                if cur: out.append(cur)
                cur=[t,w.strip()]
            else: cur[1]+=w
    out.append(cur);return out
words=[(t,x) for t,w in ricostruisci(W) for x in re.split(r"['’]",w)]
norm=lambda w:re.sub(r'[^a-zàèéìòù]','',w.lower())
STOP=set('della delle degli dello dalla dalle quello quella questo questa sono anche perch quindi allora cosa cose molto ancora senza dopo prima sempre fatto tutti tutto essere stato stata'.split())
words=[(t,norm(w)[:5]) for t,w in words if len(norm(w))>=5 and norm(w)[:5] not in STOP]
T=json.load(open('pptx_text.json'))
def cardsof(i): return T[str(i)][2:-1] if i in(3,4) or i>=46 else []
def stems(c):
    lead=c.split(':')[0] if ':' in c[:90] else ''
    return {norm(x)[:5]:(4.0 if w in lead.split() else 1.0) for w in c.split() for x in re.split(r"['’]",w) if len(norm(x))>=5 and norm(x)[:5] not in STOP}
def evidenzia(slide,a,b,win=4.5,thr=3.0):
    """evento: la card i si accende al primo istante (dopo la precedente) in cui il prof pronuncia le sue parole distintive"""
    C=cardsof(slide);K=[stems(c) for c in C];cnt=collections.Counter(s for k in K for s in k)
    n=len(K);ts=[a+x*0.5 for x in range(int((b-a)*2)+1)]
    t_on=[None]*n;prev=a-1
    for i in range(n):
        for t in ts:
            if t<=prev+(3.0 if i>0 else 0): continue
            sc=sum(K[i][s]/cnt[s] for tt,s in words if t-0.5<=tt<=t+win and s in K[i])
            if sc>=thr: t_on[i]=t;prev=t;break
    iv=[];cur=None;last=a
    ev=sorted((t,i) for i,t in enumerate(t_on) if t is not None)
    pos=a
    for t,i in ev:
        iv.append([pos,t,cur]);pos=t;cur=i
    iv.append([pos,b,cur])
    iv=[x for x in iv if x[1]-x[0]>0.05]
    return iv
if __name__=='__main__':
    TR=json.load(open('slidetrack_raw.json'))
    for slide,a,b in [(3,193.5,530.5),(4,530.5,810),(3,905.5,1324.5),(46,1324.5,1764),(48,1764,2029)]:
        print(slide,a,b,[(round(x,0),round(y,0),v) for x,y,v in evidenzia(slide,a,b)])
