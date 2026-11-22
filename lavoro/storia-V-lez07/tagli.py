import sys,json,re
sys.path.insert(0,'/home/claude/w/b')
from sottotitoli import correggi,SEG
def mmss(t): return f'{int(t//60)}:{t%60:04.1f}'
def tabella(tl):
    pos={n:(t,l) for n,t,l in tl}
    rows=['| Pezzo | Fine (minuto del video) | Ultime parole | Frase finita | Inizio (prime parole) | Inizia a frase intera | Margine dal taglio alla frase che segue (s) |','|---|---|---|---|---|---|---|']
    bad=0
    for name,(T0,L) in pos.items():
        if not (name.startswith('Dprof') or name=='Dintro'): continue
        pn='P0' if name=='Dintro' else 'P'+name[5:]
        J=json.load(open(f'/home/claude/w/b/pz4/{pn}.mkv.json')); iv=J['iv']
        # segmento finale e iniziale
        ids=[i for i,s in enumerate(SEG) if s['inizio']>=iv[0][0]-0.4 and s['fine']<=iv[-1][1]+0.4]
        first=SEG[ids[0]];last=SEG[ids[-1]]
        fin=last['testo'].strip(); ok=bool(re.search(r'[.?!]$',fin)) and not fin.endswith('...')
        prev=SEG[ids[0]-1]['testo'].strip() if ids[0]>0 else '.'
        sok=bool(re.search(r'[.?!]$',prev)) or ids[0]==0 or True
        words=' '.join(correggi(fin).split()[-8:])
        fw=' '.join(correggi(first['testo']).split()[:6])
        nxt=SEG[ids[-1]+1]['inizio'] if ids[-1]+1<len(SEG) else None
        marg=round(nxt-iv[-1][1],2) if nxt else '–'
        if not ok: bad+=1
        rows.append(f'| {name} | {mmss(T0+L)} | …{words} | {"sì" if ok else "NO"} | {fw}… | {"sì" if re.search(r"[.?!]$",prev) or ids[0]==0 else "NO (segue «"+prev[-25:]+"»)"} | {marg} |')
    return '\n'.join(rows),bad
if __name__=='__main__':
    t,b=tabella(json.load(open(sys.argv[1]))); print(t); print('fine senza punto:',b)
