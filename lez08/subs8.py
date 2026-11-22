# sottotitoli .vtt sul video finale: prof (trascrizione, tempi mappati) + voci Kore (testo noto); termini corretti
import sys, os, json, re
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from plan import *
FIX=[(r'\b(book|bunk|munk|monk|moon|munc)\b','Munch'),(r'\bke?rcn?ner|kirchener|kirken|kirkner|chirchner\b','Kirchner'),(r'\bka?ndinsky|candinski|kandinski\b','Kandinskij'),
 (r'\bcoshka|kokoshka|kokoska|cocoska\b','Kokoschka'),(r'\bconcile|goncile|chile|scile\b','Schiele'),(r'\bmark\b','Marc'),(r'\bdie ?bruck|diebrik|diebruc|bruck\b','Die Brücke'),
 (r'\bdel? ?blau ?rider|der blau rider|ver blau rider|blau rider\b','Der Blaue Reiter'),(r'\bensor|enso\b','Ensor'),(r'\bgimmel|simon\b','Simmel'),(r'\bgeorge\b','Georg'),(r'\bvergmund|werkbund|vergbund\b','Werkbund'),
 (r'\bmu ?tesius|mathesius\b','Muthesius'),(r'\bnauman\b','Naumann'),(r'\bclee\b','Klee'),(r'\bgogin\b','Gauguin'),(r'\bpotsdammer ?pl\w+|post dummer plus\b','Potsdamer Platz'),(r'\bsofie\b','Sofie')]
def fixw(s):
    for p,r in FIX: s=re.sub(p,r,s,flags=re.I)
    return s
def parole_asr():
    W=[]; cur='';t0=None
    for s in TRASC:
        for t,tok in s['parole']:
            if tok.startswith(' ') or t0 is None:
                if cur.strip(): W.append((t0,cur.strip()))
                cur=tok; t0=t
            else: cur+=tok
    if cur.strip(): W.append((t0,cur.strip()))
    return W
def blocchi(W,maxc=42):
    """W=[(t,parola)] -> cue (a,b,testo) da 1-6 s, max 2 righe da 42 caratteri"""
    out=[]; cur=[]; 
    def chiudi(endt):
        if not cur: return
        txt=' '.join(w for _,w in cur); a=cur[0][0]; b=max(endt,a+1.0)
        # a capo a meta' se supera maxc
        if len(txt)>maxc:
            ws=txt.split(); l1='';
            for i,w in enumerate(ws):
                if len(l1+' '+w)>maxc: break
                l1=(l1+' '+w).strip()
            r=' '.join(ws[len(l1.split()):]); txt=l1+'\n'+r
        out.append((a,b,txt)); cur.clear()
    for i,(t,w) in enumerate(W):
        if cur and (len(' '.join(x for _,x in cur)+' '+w)>maxc*2-4 or t-cur[0][0]>5.5):
            chiudi(t-0.05)
        cur.append((t,w))
        if re.search(r'[.?!]$',w) and len(cur)>3: chiudi(W[i+1][0]-0.05 if i+1<len(W) and W[i+1][0]-t<1.2 else t+0.9)
    if cur: chiudi(cur[-1][0]+1.0)
    return out
def ts(s): h,r=divmod(s,3600); m,r=divmod(r,60); return '%02d:%02d:%06.3f'%(h,m,r)
def vtt(parte,outp):
    tl=json.load(open(f'/tmp/w/out/timeline_pezzi_P{parte}.json')); W=parole_asr(); cues=[]
    for p in PROF:
        pe=[x for x in tl if x['pezzo']==p['id'] or x['pezzo']==('P0_intro' if p['id']=='P0_intro' else p['id'])]
        if not pe: continue
        a,b,_,_=taglio(p); off=pe[0]['inizio']
        ws=[(off+(t-a),fixw(w)) for t,w in W if a<=t<b]
        cues+=[(x,y,z) for x,y,z in blocchi(ws)]
    # voci Kore: testo noto, tempi proporzionali (o reali se ci sono i json)
    meta={}
    for x in tl:
        mp=f'/tmp/w/b/meta_{x["pezzo"]}.json'
        if os.path.exists(mp): meta[x['pezzo']]=(x['inizio'],json.load(open(mp)))
    TESTI={v['nome']:v['testo'] for v in json.load(open('/tmp/w/voci/testi_voci.json'))}
    for pz,(st,m) in meta.items():
        for wavn,s0 in m['parts']:
            nm=re.sub(r'^(prov_|cc_)','',wavn)[:-4]
            if wavn.endswith('.wav') and wavn.startswith('prov_'): nm=wavn[5:-4]
            if nm not in TESTI: continue
            ws=TESTI[nm].split(); 
            jf=f'/tmp/w/vox/{nm}.json'
            if os.path.exists(jf) and wavn==nm+'.wav': tw=[(t,w) for t,w in json.load(open(jf))]; 
            else: tw=None
            d=m['total']-s0-1.2
            T=[(st+s0+i/len(ws)*d,w) for i,w in enumerate(ws)] if not tw else [(st+s0+t,w) for (t,_),w in zip(tw,ws)]
            cues+=blocchi(T)
    cues.sort()
    with open(outp,'w') as f:
        f.write('WEBVTT\n\n')
        for i,(a,b,t) in enumerate(cues,1): f.write(f'{i}\n{ts(a)} --> {ts(b)}\n{t}\n\n')
    return len(cues)
if __name__=='__main__': print(vtt(int(sys.argv[1]),sys.argv[2]))
