# allinea.py: collega le frasi del PDF della prof (testo corretto) ai tempi della trascrizione.
import json, re, sys, difflib, subprocess, unicodedata
def norm(w):
    w=unicodedata.normalize('NFD',w.lower());w=''.join(c for c in w if unicodedata.category(c)!='Mn')
    return re.sub(r'[^a-z0-9]','',w)
def parole_trasc(js):
    P=[]
    for s in json.load(open(js)):
        cur=None
        for t,tok in s['parole']:
            if tok.startswith('▁') or cur is None:
                if cur: P.append(cur)
                cur=[t,tok.lstrip('▁')]
            else: cur[1]+=tok
        if cur: P.append(cur)
    return [(t,w,norm(w)) for t,w in P if norm(w)]
def frasi_pdf(pdf):
    txt=subprocess.run(['pdftotext','-layout',pdf,'-'],capture_output=True,text=True).stdout
    lines=[l.strip() for l in txt.split('\n')]
    out=[];buf=''
    for l in lines:
        if not l: 
            if buf: out.append(buf);buf=''
            continue
        if re.match(r'^[-●•]\s',l): 
            if buf: out.append(buf)
            buf=l[1:].strip().replace('​','')
        else: buf=(buf+' '+l).strip()
    if buf: out.append(buf)
    fr=[]
    for p in out:
        p=p.replace('​','')
        for s in re.split(r'(?<=[\.\!\?:;])\s+(?=[A-ZÀÈÉÌÒÙ])',p):
            if len(s)>3: fr.append(s)
    return fr
def allinea(frasi,TP):
    # per ogni frase del PDF cerca la finestra migliore nella trascrizione a partire dalla posizione corrente (avanti soltanto)
    W=[x[2] for x in TP];pos=0;ris=[]
    for f in frasi:
        fw=[norm(w) for w in f.split() if norm(w)]
        if len(fw)<2: ris.append(None);continue
        best=(0,None,None)
        lo=pos;hi=min(len(W),pos+len(fw)*3+400)
        n=len(fw)
        # finestre di lunghezza ~n, passo 2; punteggio = rapporto di allineamento
        for i in range(lo,hi-2,2):
            seg=W[i:i+int(n*1.25)+2]
            sm=difflib.SequenceMatcher(None,fw,seg,autojunk=False)
            m=sum(b.size for b in sm.get_matching_blocks())
            sc=m/n
            if sc>best[0]: best=(sc,i,i+len(seg))
        sc,i,j=best
        if sc>=0.5 and i is not None:
            # affina: primo e ultimo elemento che combaciano
            seg=W[i:j];sm=difflib.SequenceMatcher(None,fw,seg,autojunk=False)
            bl=[b for b in sm.get_matching_blocks() if b.size]
            a0=i+bl[0].b;a1=i+bl[-1].b+bl[-1].size-1
            ris.append(dict(t0=TP[a0][0],t1=TP[min(a1+1,len(TP)-1)][0],q=round(sc,2),i0=a0,i1=a1));pos=a1+1
        else: ris.append(dict(q=round(sc,2),t0=None))
    return ris
if __name__=='__main__':
    TP=parole_trasc(sys.argv[1]);F=frasi_pdf(sys.argv[2]);R=allinea(F,TP)
    json.dump([dict(f=f,**(r or {})) for f,r in zip(F,R)],open(sys.argv[3],'w'),ensure_ascii=False,indent=0)
    ok=sum(1 for r in R if r and r.get('t0') is not None);print(len(F),'frasi',ok,'allineate')
