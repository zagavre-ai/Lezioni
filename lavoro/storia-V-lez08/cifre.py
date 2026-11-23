# Sullo schermo i numeri e gli anni vanno in cifre (la voce li ha in lettere). Parser dei numeri italiani + sigle rispiegate.
import re
U={'zero':0,'uno':1,'un':1,'due':2,'tre':3,'tré':3,'quattro':4,'cinque':5,'sei':6,'sette':7,'otto':8,'nove':9,'dieci':10,'undici':11,'dodici':12,'tredici':13,'quattordici':14,'quindici':15,'sedici':16,'diciassette':17,'diciotto':18,'diciannove':19}
T={'venti':20,'trenta':30,'quaranta':40,'cinquanta':50,'sessanta':60,'settanta':70,'ottanta':80,'novanta':90}
def parse(w):
    """parola numerica composta ('millenovecentoventidue','ventitré','trecentomila') -> int o None"""
    s=w.lower().replace('é','e').replace('tré','tre')
    if not re.fullmatch(r'[a-z]+',s): return None
    tot=0; cur=0; i=0
    pezzi=[('mille',1000),('mila',1000),('cento',100),('milioni',10**6),('milione',10**6)]
    # scomposizione greedy
    rest=s; val=0; parti=[]
    def tok(r):
        for k in sorted(list(T)+list(U)+['mille','mila','cento','milioni','milione'],key=len,reverse=True):
            if r.startswith(k): return k,r[len(k):]
        # elisione: vent(i)uno, trent(a)otto...
        for k in T:
            st=k[:-1]
            if r.startswith(st): return k,r[len(st):]
        return None,r
    seq=[]
    while rest:
        k,r2=tok(rest)
        if k is None: return None
        seq.append(k); rest=r2
    if not seq: return None
    total=0; cur=0
    for k in seq:
        if k in U: cur+=U[k]
        elif k in T: cur+=T[k]
        elif k=='cento': cur=(cur or 1)*100
        elif k in('mille','mila'): total+=(cur or 1)*1000; cur=0
        elif k in('milioni','milione'): total+=(cur or 1)*10**6; cur=0
    return total+cur
def cifre(testo):
    out=[]
    for w in re.split(r'(\W+)',testo):
        if w and w.isalpha() and len(w)>=4 and w.lower() not in ('cento','mille','milioni','milione','mila','tredici_'):
            v=parse(w)
            if v is not None and v>=10: out.append(format(v,',').replace(',','.') if v>=10000 else str(v)); continue
        out.append(w)
    t=''.join(out)
    t=re.sub(r'\b(due|tre|quattro|cinque|sei|sette|otto|nove) milioni','\\1 milioni',t)
    for k,v in (('due',2),('tre',3),('quattro',4),('cinque',5)): t=re.sub(rf'\b{k} milioni',f'{v} milioni',t)
    t=re.sub(r'\b(\d+) per cento','\\1%',t)
    t=re.sub(r'Emanuele Terzo','Emanuele III',t)
    return t
SIGLE=[('PNF','Partito Nazionale Fascista'),('MVSN','Milizia volontaria per la sicurezza nazionale')]
def sigle(testo):
    for s,e in SIGLE:
        t2=re.sub(rf'\b{s}\b',f'{s} ({e})',testo,count=1)
        testo=t2
    return testo
if __name__=='__main__':
    for x in ["millenovecentoventidue e ventitré marzo","oltre due milioni di persone","venticinque per cento dei voti","trecentomila iscritti","due terzi dei seggi","ventun anni","il trenta maggio millenovecentoventiquattro","Vittorio Emanuele Terzo","Primo: la MVSN e il PNF","millenovecentodiciannove","sei mesi"]:
        print(cifre(x),'|',sigle(cifre(x)))
