import sys,json
sys.path.insert(0,'/home/user/work18/lib')
from cuts import SEG,WORDS,level,WAV
out=[]
for w in ('1','2'):
    pm=json.load(open(f'out/pm_parte{w}.json'));tl={n:(t,d) for n,t,d in json.load(open(f'out/timeline_Storia_Lez18_Parte{w}.json'))}
    out.append(f'\n**Parte {w}**\n\n| pezzo | inizio nel video | prime parole | fine nel video | fine (sorgente) | ultime 8 parole | frase finita | livello nel taglio |\n|---|---|---|---|---|---|---|---|')
    for name,T0,T1 in pm:
        # inizio pezzo nel video
        t0=tl[name][0]
        # fine nel video = fine dell'ultima finestra del pezzo: inizio + (T1-T0)
        t1=t0+(T1-T0)
        def txt(ws):
            o=''
            for x in ws:o+=x[1]
            return o.split()
        ws=[x for x in WORDS if x[0]<T1];last=' '.join(txt(ws[-40:])[-8:])
        ws2=[x for x in WORDS if x[0]>=T0][:40];first=' '.join(txt(ws2)[:8])
        seg=[s for s in SEG if s['inizio']<T1];ls=seg[-1] if seg else None
        done='sì' if ls and ls['testo'].strip()[-1:] in '.?!' else 'sì (pausa)' if ls and T1-ls['fine']>=0.2 else 'DA CONTROLLARE'
        mm=lambda t:'%d:%05.2f'%(t//60,t%60)
        out.append(f'| {name} | {mm(t0)} | {first}… | {mm(t1)} | {T1:.2f} s | …{last} | {done} | {float(level(T1,WAV)):.0f} dB |')
open('out/tabella_tagli.md','w').write('\n'.join(out));print('\n'.join(out)[:3000])
