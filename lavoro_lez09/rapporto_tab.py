import sys,json,random,re
sys.path.insert(0,'.')
from prof import *
def mm(t):return '%d:%02d'%(t//60,t%60)
def fini(parte):
    rows=['| Pezzo | Fine (nel video originale) | Ultime parole (trascrizione) | Frase finita |','|---|---|---|---|']
    for n in ([0,1,2,3,4,5] if parte==1 else [6,7,8,9,10,11]):
        a0,a1=arg_range(n);a0,a1=snap(a0,a1)
        k=seg_at(a1-0.3) if False else max(i for i,s in enumerate(SEG) if s['fine']<=a1-0.0+0.01)
        txt=SEG[k]['testo'].strip();w=' '.join(txt.split()[-8:]);ok='sì' if re.search(r'[.!?…]$',txt) else 'NO (da guardare)'
        rows.append(f"| {'D0 (introduzione)' if n==0 else ('Riepilogo del prof' if n==11 else 'Argomento %d'%n)} | {mm(a1)} | …{w} | {ok} |")
    return '\n'.join(rows)
def punti(parte,n=10,seed=7):
    random.seed(seed);pool=[]
    for a,L in CARDS.items():
        if (a<=5)==(parte==1):
            for p,i,t in L:pool.append((a,p,i,t))
    pick=sorted(random.sample(pool,min(n,len(pool))))
    rows=['| Argomento | Card (inizio testo) | Minuto (originale) | Frase del prof che comincia lì (trascrizione) | Scarto |','|---|---|---|---|---|']
    for a,p,i,t in pick:
        k=seg_at(t);s=SEG[k]
        rows.append(f"| {a} | {' '.join(card(p,i).split()[:6])}… | {mm(s['inizio'])} | {s['testo'].strip()[:70]} | 0,0 s (per costruzione) |")
    return '\n'.join(rows)
if __name__=='__main__':
    print(fini(1));print(punti(1))
