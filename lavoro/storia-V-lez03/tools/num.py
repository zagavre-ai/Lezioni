import re
U={'zero':0,'uno':1,'un':1,'due':2,'tre':3,'quattro':4,'cinque':5,'sei':6,'sette':7,'otto':8,'nove':9,'dieci':10,'undici':11,'dodici':12,'tredici':13,'quattordici':14,'quindici':15,'sedici':16,'diciassette':17,'diciotto':18,'diciannove':19}
T={'venti':20,'trenta':30,'quaranta':40,'cinquanta':50,'sessanta':60,'settanta':70,'ottanta':80,'novanta':90}
def parse_tail(s):
    """s: stringa tipo 'novantasei' -> int o None"""
    if s=='': return 0
    if s in U: return U[s]
    for t,v in T.items():
        if s.startswith(t[:-1]):
            r=s[len(t):] if s.startswith(t) else s[len(t)-1:]
            if r=='': return v
            if r in U and U[r]<10: return v+U[r]
    return None
def conv_year(w):
    w=w.replace('é','e').replace('è','e')
    w=re.sub(r'^milleottocentott','milleottocentoott',w)
    m=re.fullmatch(r'mille(otto|nove)cento(.*)',w)
    if not m: return None
    base=1800 if m.group(1)=='otto' else 1900
    t=parse_tail(m.group(2))
    return None if t is None else str(base+t)
def to_digits(text):
    def rep(m):
        r=conv_year(m.group(0).lower());return r if r else m.group(0)
    text=re.sub(r"\bmille(?:otto|nove)cento[a-zé]*",rep,text,flags=re.I)
    text=re.sub(r"\bdodici\b(?= anni)","12",text)
    return text
if __name__=='__main__':
    for w in ['milleottocentonovantasei','millenovecento','millenovecentoundici','milleottocentottantasette','millenovecentoquattordici','millenovecentotre','millenovecentododici','milleottocentocinquantatré']:
        print(w,conv_year(w))
