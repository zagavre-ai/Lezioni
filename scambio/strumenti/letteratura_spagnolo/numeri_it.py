import re
U={'zero':0,'uno':1,'un':1,'una':1,'due':2,'tre':3,'quattro':4,'cinque':5,'sei':6,'sette':7,'otto':8,'nove':9,'dieci':10,'undici':11,'dodici':12,'tredici':13,'quattordici':14,'quindici':15,'sedici':16,'diciassette':17,'diciotto':18,'diciannove':19}
T={'venti':20,'trenta':30,'quaranta':40,'cinquanta':50,'sessanta':60,'settanta':70,'ottanta':80,'novanta':90}
def sotto100(s):
    if s in U: return U[s]
    for k,v in T.items():
        for kk in (k,k[:-1]):
            if s.startswith(kk):
                r=s[len(kk):]
                if r=='' : return v
                if r=='tré': r='tre'
                if r in U and U[r]<10: return v+U[r]
    return None
def sotto1000(s):
    if s=='': return 0
    m=re.match(r'^(.*?)cento(.*)$',s)
    if m:
        a=1 if m.group(1)=='' else U.get(m.group(1))
        if a is None: return None
        r2=m.group(2); r2=('o'+r2) if r2.startswith('tt') else r2; b=sotto1000b(r2); 
        return None if b is None else a*100+b
    return sotto100(s)
def sotto1000b(s):
    if s=='': return 0
    return sotto100(s)
def parola(w):
    s=w.lower()
    if not s.startswith(('mille','duemila')): return None
    if s.startswith('mille'): base=1000; r=s[5:]
    else: base=2000; r=s[7:]
    v=sotto1000(r)
    return None if v is None else base+v
def converti(t):
    return re.sub(r"[A-Za-zàèéìòù]+",lambda m: str(parola(m.group(0))) if parola(m.group(0)) else m.group(0),t)
if __name__=='__main__':
    for x in ['millenovecentonove','millenovecentotredici','millenovecentoventiquattro','milleottocentottantuno','duemilauno','millenovecentosedici','mille','millenovecentoquarantacinque']: print(x,parola(x))

MESI='gennaio|febbraio|marzo|aprile|maggio|giugno|luglio|agosto|settembre|ottobre|novembre|dicembre'
_conv_anni=converti
def converti(t):
    t=_conv_anni(t)
    def g(m):
        n=sotto100(m.group(1).lower()) if m.group(1).lower()!='primo' else 1
        if m.group(1).lower()=='primo': return f'1° {m.group(2)}'
        return f'{n} {m.group(2)}' if n else m.group(0)
    return re.sub(r"\b([A-Za-z]+)\s+("+MESI+r")\b",g,t)
