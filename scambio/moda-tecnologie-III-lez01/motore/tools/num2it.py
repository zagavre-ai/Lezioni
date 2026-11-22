import re
U=['zero','uno','due','tre','quattro','cinque','sei','sette','otto','nove','dieci','undici','dodici','tredici','quattordici','quindici','sedici','diciassette','diciotto','diciannove']
T=['','','venti','trenta','quaranta','cinquanta','sessanta','settanta','ottanta','novanta']
def _lt100(n):
    if n<20:return U[n]
    t,u=divmod(n,10);w=T[t]
    if u in(1,8):w=w[:-1]
    return w+('' if u==0 else ('tré' if u==3 else U[u]))
def _lt1000(n):
    c,r=divmod(n,100);s=''
    if c:s='cento' if c==1 else U[c]+'cento'
    if r:
        if c and r//10==8:s=s[:-1]
        s+=_lt100(r)
    return s
def it(n):
    if n<100:return _lt100(n)
    if n<1000:return _lt1000(n)
    if n<1000000:
        m,r=divmod(n,1000);s='mille' if m==1 else _lt1000(m)+'mila'
        if r:s+=(' e ' if r<100 else '')+_lt1000(r)
        return s
    m,r=divmod(n,1000000);s='un milione' if m==1 else _lt1000(m)+' milioni'
    if r:s+=' '+it(r)
    return s
def conv(t):
    """converte i numeri di un testo in lettere (decimali con virgola, percentuali, migliaia con punto)"""
    t=re.sub(r'(\d+)\s?%',lambda m:m.group(1)+' per cento',t)
    t=re.sub(r'(\d{1,3})\.(\d{3})\b',lambda m:str(int(m.group(1))*1000+int(m.group(2))),t)
    t=re.sub(r'(\d+),(\d+)',lambda m:it(int(m.group(1)))+' virgola '+(' '.join(U[int(c)] for c in m.group(2)) if m.group(2).startswith('0') else it(int(m.group(2)))),t)
    t=re.sub(r'\d+',lambda m:it(int(m.group(0))),t)
    for a,b in [(r'kg/mm²','chilogrammi al millimetro quadrato'),(r'°C','gradi centigradi'),(r'\bkg\b','chilogrammi'),(r'\bcm\b','centimetri'),(r'\bmm\b','millimetri'),(r'\bg\b','grammi'),(r'\bm\b','metri'),(r'\bUE\b','U E')]:
        t=re.sub(a,b,t)
    return t
if __name__=='__main__':
    for x in ['1007','2011','37%','8,7%','19,75','453 g','1.600 g','4000','6000 m','2 e 8 cm','80','100','180','21','28','101','1900','250','70 °C','120 g']:print(x,'->',conv(x))
