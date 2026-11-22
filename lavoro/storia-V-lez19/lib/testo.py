# numeri in lettere -> cifre per lo schermo (la voce li legge in lettere)
import re
U={'zero':0,'due':2,'tre':3,'quattro':4,'cinque':5,'sei':6,'sette':7,'otto':8,'nove':9}
TE={'dieci':10,'undici':11,'dodici':12,'tredici':13,'quattordici':14,'quindici':15,'sedici':16,'diciassette':17,'diciotto':18,'diciannove':19}
TS={'venti':20,'trenta':30,'quaranta':40,'cinquanta':50,'sessanta':60,'settanta':70,'ottanta':80,'novanta':90}
def p(w):
    w=w.replace('é','e')
    if w in ('uno','una','un'): return None
    tot=0;s=w
    if s.startswith('mille'): tot+=1000;s=s[5:]
    else:
        for k,v in U.items():
            if k!='zero' and s.startswith(k+'mila'): tot+=v*1000;s=s[len(k)+4:];break
    for k,v in list(U.items())+[('',1)]:
        if k=='zero':continue
        if s.startswith(k+'cent') :
            rest=s[len(k)+4:]
            if rest.startswith('o'):  # cento / centottanta
                if rest=='o' or rest[1:]=='' : tot+=v*100;s='';break
                # elisione: "centottanta" -> cent+ottanta ; "centoventi"
                if rest.startswith('ottan') or rest.startswith('otto'): tot+=v*100;s=rest;break
                tot+=v*100;s=rest[1:];break
            elif rest.startswith('ottan') or rest.startswith('otto'): tot+=v*100;s=rest;break
    if s:
        done=False
        for k,v in TS.items():
            for pre in (k,k[:-1]):
                if s.startswith(pre):
                    rest=s[len(pre):]
                    if pre==k and (rest=='' or rest in U or rest=='uno'): tot+=v+(U.get(rest,1 if rest=='uno' else 0));s='';done=True;break
                    if pre==k[:-1] and (rest=='uno' or rest.startswith('otto')): tot+=v+(1 if rest=='uno' else 8);s='';done=True;break
            if done:break
        if not done:
            if s in TE: tot+=TE[s];s=''
            elif s in U: tot+=U[s];s=''
            elif s=='tre': tot+=3;s=''
    return tot if s=='' and tot>0 else None
def cifre(t):
    def rep(m):
        w=m.group(0);v=p(w.lower())
        return str(v) if v is not None else w
    t=t.replace(' per cento',' PERCENTO')
    t=re.sub(r"\b[a-zA-Zàèéìòù]{3,}\b",rep,t)
    t=re.sub(r' PERCENTO','%',t)
    return t
if __name__=='__main__':
    for s in ['millenovecentosessantanove','millenovecentottanta','cinquantacinque giorni','ventitré','settantacinque per cento','novecentonovantadue','duemilauno','sedici marzo','centoventi','tre quarti','trentuno','ventotto']:
        print(s,'->',cifre(s))
