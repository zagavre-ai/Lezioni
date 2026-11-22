import re
U={'uno':1,'una':1,'un':1,'due':2,'tre':3,'quattro':4,'cinque':5,'sei':6,'sette':7,'otto':8,'nove':9,'dieci':10,'undici':11,'dodici':12,'tredici':13,'quattordici':14,'quindici':15,'sedici':16,'diciassette':17,'diciotto':18,'diciannove':19}
T={'venti':20,'trenta':30,'quaranta':40,'cinquanta':50,'sessanta':60,'settanta':70,'ottanta':80,'novanta':90}
D={'due':2,'tre':3,'quattro':4,'cinque':5,'sei':6,'sette':7,'otto':8,'nove':9}
def p(w):
    if w=='':return 0
    if w.startswith('mille'):
        r=p(w[5:]);return None if r is None else 1000+r
    m=re.match(r'(.+?)mila(.*)',w)
    if m:
        a=p(m.group(1));r=p(m.group(2))
        if a is not None and r is not None and a<1000:return a*1000+r
    m=re.match(r'(due|tre|quattro|cinque|sei|sette|otto|nove)?cento(.*)',w)
    if m:
        r=p(m.group(2));return None if r is None else D.get(m.group(1),1)*100+r
    for t,v in T.items():
        for stem in (t,t[:-1]):
            if w.startswith(stem):
                rest=w[len(stem):]
                if rest=='' :return v
                if rest in U and U[rest]<10 and (stem==t or rest[0] in 'uo'):return v+U[rest]
    if w in U:return U[w]
    return None
NUMW=r'(?:mille|(?:due|tre|quattro|cinque|sei|sette|otto|nove)?(?:mila|cento)|(?:venti|trenta|quaranta|cinquanta|sessanta|settanta|ottanta|novanta)mila|venti|vent|trenta|trent|quaranta|quarant|cinquanta|cinquant|sessanta|sessant|settanta|settant|ottanta|ottant|novanta|novant|uno|una|due|tre|quattro|cinque|sei|sette|otto|nove|dieci|undici|dodici|tredici|quattordici|quindici|sedici|diciassette|diciotto|diciannove|tré)+'
def cifre(t):
    t=re.sub(r'\bsei ai\b','6 ai',t)
    def rep(m):
        w=m.group(0);v=p(w.lower().replace('é','e'))
        if v is None or (w.lower() in ('una','un','uno','sei','tre','due') ):return w
        return str(v)
    return re.sub(r'\b'+NUMW+r'\b',rep,t,flags=re.I)
if __name__=='__main__':
    for s in ['millenovecentoventicinque','millenovecentotrentotto','ventotto','quattrocento','novanta','sei ai diciotto anni','quattordici anni','quota novanta','cinquantamila persone','millenovecentoventitré','venti','otto ore']:
        print(s,'->',cifre(s))
