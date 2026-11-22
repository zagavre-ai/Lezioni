import re
U={'zero':0,'uno':1,'un':1,'una':1,'due':2,'tre':3,'tré':3,'quattro':4,'cinque':5,'sei':6,'sette':7,'otto':8,'nove':9,'dieci':10,'undici':11,'dodici':12,'tredici':13,'quattordici':14,'quindici':15,'sedici':16,'diciassette':17,'diciotto':18,'diciannove':19}
D={'venti':20,'trenta':30,'quaranta':40,'cinquanta':50,'sessanta':60,'settanta':70,'ottanta':80,'novanta':90}
def _parse(w):
    """parola italiana composta -> intero o None"""
    s=w;tot=0;thou=0
    if s.startswith('millenovecento') or s.startswith('mille') or s.startswith('duemila') or s.startswith('duecentomila') or re.match(r'^[a-z]+mila',s):
        m=re.match(r'^(mille|(\w+?)mila)',s)
        if m:
            pre=m.group(2);thou=1000 if m.group(1)=='mille' else (_parse(pre) or 0)*1000;s=s[m.end():]
            if m.group(1)=='mille' and not s:return 1000
            tot=thou
    m=re.match(r'^(?:(due|tre|quattro|cinque|sei|sette|otto|nove)?cento)',s)
    if m:tot+=(U.get(m.group(1),1))*100;s=s[m.end():]
    for d,v in sorted(D.items(),key=lambda x:-len(x[0])):
        stem=d[:-1]
        if s.startswith(d) or (s.startswith(stem) and s[len(stem):len(stem)+1] in 'uo' and s[len(stem):] and s[len(stem):] in ('uno','otto')):
            if s.startswith(d):tot+=v;s=s[len(d):]
            else:tot+=v;s=s[len(stem):]
            break
    if s:
        if s in U:tot+=U[s];s=''
        else:return None
    return tot if tot>0 or w=='zero' else None
MESI='gennaio febbraio marzo aprile maggio giugno luglio agosto settembre ottobre novembre dicembre'.split()
def num_words(text):
    toks=list(re.finditer(r"[A-Za-zàèéìòù]+",text));out=[];last=0
    for i,m in enumerate(toks):
        w=m.group(0);n=_parse(w.lower())
        prev=toks[i-1].group(0).lower() if i else '';nxt=toks[i+1].group(0).lower() if i+1<len(toks) else ''
        nn2=toks[i+2].group(0).lower() if i+2<len(toks) else ''
        ok=n is not None and w.lower()!='cento' and not w[0].isupper() and prev!='anni' and (n>=100 or nxt in MESI or (nxt=='per' and nn2=='cento') or prev in('apollo','compito'))
        if ok:
            r=f'{n:,}'.replace(',','.') if n>=10000 else str(n)
            out.append(text[last:m.start()]+r);last=m.end()
            if nxt=='per' and nn2=='cento':pass
    out.append(text[last:])
    t=''.join(out)
    return re.sub(r'(\d+) per cento',r'\1%',t)
if __name__=='__main__':
    for t in ["nel millenovecentosessantuno","duecentomila persone","il venti luglio millenovecentosessantanove","ventidue novembre millenovecentosessantatré","l'ottanta per cento","Apollo undici","Il Sessantotto","gli anni sessanta","tre astronauti"]:print(t,'->',num_words(t))
