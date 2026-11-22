# Piano dei pezzi del prof: tagli (sulle pause), pause accorciate, stati delle slide.
import sys, math, json
sys.path.insert(0,'/home/user/Lezioni/lavoro')
import struttura as S, tlib
from cuts import taglio, comprimi, g, onset, RMS
from trasc_util import mmss, find
ARGS={a['n']:a for a in S.ARG}
# confini tra pezzi del prof (tempo ASR dell'inizio della frase che segue)
B={'intro_fine':180.7,'a1':239.88,'a2':1039.13,'a3':1676.09,'a4':2462.37,'a5':3169.78,'a6':3784.93,'a7':4550.69,'a8':5355.72}
MID={}   # nessun approfondimento a metà argomento: le schermate lunghe si spezzano con le evidenze
END=5786.18
def taglio_pt(t):
    if t>=END-1: return END,END
    f,i,ok=taglio(t); return f,i
def refine_lit(t):
    o,p=onset(t,1.0); return o if p else t
def stati_arg(n,t0,t1):
    """[(t_src, spec)] per tutta la durata dell'argomento (t0,t1 = limiti sorgente dei suoi pezzi)"""
    a=ARGS[n];cards=a['cards'];ev=[]
    for i,c in enumerate(cards): ev.append((refine_lit(c['lit']),'c',i))
    for k,im in enumerate(a.get('immagini',[])):
        ev.append((refine_lit(im['lit']),'i',k));ev.append((refine_lit(im['fine']),'x',k))
    ev.sort()
    seq=[(t0-5.0,('c',None))]
    for t,kind,i in ev:
        if kind=='c': seq.append((t,('c',i)))
        elif kind=='i': seq.append((t,('i',i)))
        else: seq.append((t,('c',seq[-1][1][1] if False else None)))
    # dopo un'immagine torna al card lit precedente all'immagine
    out=[];last_card=None
    for t,(k,i) in seq:
        if k=='c':
            if i is None and out and out[-1][1][0]=='i': i=last_card
            if i is not None:last_card=i
            out.append((t,('c',i)))
        else: out.append((t,('i',i)))
    # tempi AP interni: sezioni di durata (per le evidenze) -> spezza dove >110 s
    res=[];
    for j,(t,s) in enumerate(out):
        tend=out[j+1][0] if j+1<len(out) else t1
        if s[0]=='c' and s[1] is not None:
            d=tend-t;ch=tlib.chunks(cards[s[1]]);nch=len(ch)
            # intervalli interni: AP a metà arg interrompe? lo trattiamo dopo (stesso stato prima e dopo)
            steps=min(max(1,math.ceil(d/80)),nch+1)
            if d>150 and nch>=2:
                for q in range(steps):
                    tq=t+q*d/steps; evq=None if q==0 else q-1
                    res.append((tq,('c',s[1],evq)))
                continue
        res.append((t,s+(None,) if s[0]=='c' else s))
    return res
def spec_key(n,s):
    if s[0]=='i': return f'i{n}_{s[1]}'
    cards=ARGS[n]['cards'];idx=tlib.finestra(cards,s[1] if s[1] is not None else 0,ARGS[n]['slide'])
    return f"c{n}_{'-'.join(map(str,idx))}_{s[1]}_{s[2] if len(s)>2 else None}"
def pezzi():
    """lista pezzi del prof con ranges/stati"""
    P=[]
    def add(pid,t_ini_asr,t_fine_asr,arg=None,tipo='prof'):
        fine=taglio_pt(t_fine_asr)[0] if t_fine_asr<END else END
        ini=0.69 if t_ini_asr==0 else taglio_pt(t_ini_asr)[1]
        P.append(dict(id=pid,s0=ini,s1=fine,arg=arg,tipo=tipo))
    add('D0',0,B['intro_fine'],None,'intro')
    add('DI',B['intro_fine'],B['a1'],None,'di')
    ordine=[1,2,3,4,5,6,7,8]
    for k,n in enumerate(ordine):
        ini=B[f'a{n}'];fine=B[f'a{ordine[k+1]}'] if k+1<len(ordine) else END
        if n in MID:
            add(f'A{n}a',ini,MID[n],n);add(f'A{n}b',MID[n],fine,n)
        else: add(f'A{n}',ini,fine,n)
    for p in P: p['ranges']=comprimi(p['s0'],p['s1'])
    return P
if __name__=='__main__':
    P=pezzi()
    for p in P:
        r=p['ranges'];tot=sum(b-a for a,b in r)
        print(p['id'],mmss(p['s0']),mmss(p['s1']),f"dur {p['s1']-p['s0']:.1f} -> {tot:.1f}",'pause tagliate:',len(r)-1)
    print('totale',sum(sum(b-a for a,b in p['ranges']) for p in P)/60)
