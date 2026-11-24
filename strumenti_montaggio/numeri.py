# Da numeri in lettere (testo per la voce) a cifre (schermo). Es. "duemilaventidue" -> 2022
import re
U={'zero':0,'due':2,'tre':3,'quattro':4,'cinque':5,'sei':6,'sette':7,'otto':8,'nove':9,'dieci':10,'undici':11,'dodici':12,'tredici':13,
   'quattordici':14,'quindici':15,'sedici':16,'diciassette':17,'diciotto':18,'diciannove':19}
T={'venti':20,'trenta':30,'quaranta':40,'cinquanta':50,'sessanta':60,'settanta':70,'ottanta':80,'novanta':90}
def parse(w):
    """ritorna int o None. Accetta parole composte (anche 'millenovecentoquarantacinque', 'duemilaventi')"""
    s=w.lower();pos=0;tot=0;cur=0;ok=False
    toks=sorted(list(U)+list(T)+['cento','mille','mila','uno','un','tré','ventuno','trentuno','ventotto','trentotto','quarantotto','cinquantotto','sessantotto','settantotto','ottantotto','novantotto'],key=lambda x:-len(x))
    # decomposizione greedy
    vals=[]
    while pos<len(s):
        for t in toks:
            if s.startswith(t,pos):
                vals.append(t);pos+=len(t);break
        else:return None
    if not vals:return None
    # elisioni: ventuno -> venti+uno gia gestito da lista; 'ventotto' ecc.
    n=0;cur=0
    for t in vals:
        if t in U:cur+=U[t]
        elif t in T:cur+=T[t]
        elif t in('uno','un'):cur+=1
        elif t=='tré':cur+=3
        elif t.endswith('uno') or t.endswith('otto') and t not in U:
            base=t[:-3] if t.endswith('uno') else t[:-4]
            b={'vent':20,'trent':30,'quarant':40,'cinquant':50,'sessant':60,'settant':70,'ottant':80,'novant':90}[base];cur+=b+(1 if t.endswith('uno') else 8)
        elif t=='cento':cur=(cur or 1)*100
        elif t=='mille':n+=(cur or 1)*1000;cur=0
        elif t=='mila':n+=(cur or 1)*1000;cur=0
    return n+cur
def digits(text):
    def rep(m):
        w=m.group(0)
        if w.lower() in('un','uno','sei','nove','otto','tre','due','dieci','cento','mille','sette','cinque','quattro'):
            return str(parse(w)) if w.lower() not in('sei','un','uno') else w   # 'sei' è anche verbo: lo lascio
        v=parse(w)
        return (f'{v:,}'.replace(',','.') if v>=10000 else str(v)) if v is not None and v>=11 else w
    out=re.sub(r"[A-Za-zàèéìòù]+",rep,text)
    return re.sub(r'\bsei (gennaio|febbraio|marzo|aprile|maggio|giugno|luglio|agosto|settembre|ottobre|novembre|dicembre)',r'6 \1',out)
if __name__=='__main__':
    for t in ['nel duemilauno','duemilaventidue','millenovecentoquarantacinque','il quarto governo','dodici anni','nel duemilaventuno','tre argomenti','duemilatrenta','centomila dollari','sei gennaio duemilaventuno']:
        print(t,'->',digits(t))

GLOSSE=[('USA',"Stati Uniti d'America"),('ONU','Organizzazione delle Nazioni Unite'),('ISIS','Stato Islamico'),('BRICS','Brasile, Russia, India, Cina, Sudafrica'),('NATO','alleanza militare occidentale'),('UE','Unione Europea')]
def gloss(t):
    """prima occorrenza di ogni sigla: SIGLA (spiegazione), se non c'è già una spiegazione vicina"""
    for s,sp in GLOSSE:
        m=re.search(r'\b'+s+r'\b',t)
        if m and not re.match(r'\s*(\(|=|,? ?cioè)',t[m.end():m.end()+12]) and sp.split()[0].lower() not in t.lower()[m.start()-40:m.end()+60]:
            t=t[:m.end()]+f' ({sp})'+t[m.end():]
    return t
