import sys,json,re,glob,os
sys.path.insert(0,'/home/user/lav/tools')
from num2it import conv
C='/home/user/lav/lez01/cont/'
LET='ABCD'
def carica(n):
    ns={};exec(open(f'{C}a{n:02d}.py').read(),ns);return ns['A']
def ordina_opz(n,qi,q):
    """porta la risposta giusta in una posizione diversa a rotazione (n+qi)%4"""
    pos=(n+qi)%4;o=list(q['o']);ok=o[q['ok']];altre=[x for i,x in enumerate(o) if i!=q['ok']]
    out=altre[:pos]+[ok]+altre[pos:];return out,pos
def vopz(t):
    t=t.replace('1 libbra','una libbra').replace('UE','U E').replace('1007/2011','mille e sette del duemilaundici')
    return conv(t)
def nodi_mappa(m):
    out=[m['titolo']]
    for r in m['rami']:
        out.append(r['v'])
        for f in r['f']:out.append(f['v'])
    return out
RINOMINA={'A09_APPROF':'A09_APPROF_V2','A09_MAPPA':'A09_MAPPA_V2'}
def voci_argomento(n):
    A=carica(n);V=[]
    V.append((f'A{n:02d}_APPROF',A['approf']['voce']))
    V.append((f'A{n:02d}_MAPPA',' '.join(nodi_mappa(A['mappa']))))
    V.append((f'A{n:02d}_RIPASSO','Ripasso. '+' '.join(v for _,v in A['ripasso'])))
    for qi,q in enumerate(A['quiz'],1):
        o,pos=ordina_opz(n,qi,q)
        dom=f"Domanda {['uno','due','tre','quattro','cinque'][qi-1]}. {q['dv']} "+' '.join(f"Risposta {LET[i]}: {vopz(x)}." for i,x in enumerate(o))
        ris=f"La risposta giusta è la {LET[pos]}: {vopz(o[pos])}. {q['sv']}"
        V.append((f'A{n:02d}_Q{qi}_D',dom));V.append((f'A{n:02d}_Q{qi}_R',ris))
    return [(RINOMINA.get(k,k),t) for k,t in V]
if __name__=='__main__':
    ns=[int(x) for x in sys.argv[1:]]
    V=[]
    for n in ns:V+=voci_argomento(n)
    bad=[(k,re.findall(r'\d+',t)) for k,t in V if re.search(r'\d',t)]
    print('voci',len(V),'con cifre:',bad)
    json.dump([{'nome':k,'testo':t} for k,t in V],open('/home/user/lav/lez01/voci_tmp.json','w'),ensure_ascii=False,indent=1)
    for k,t in V[:6]:print(k,'|',t[:200])
