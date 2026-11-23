# -*- coding: utf-8 -*-
# Eventi per i sottotitoli: voci Kore (testo noto, tempi dal montaggio) e finestre del prof, nei tempi del video finale.
import sys, json, os
sys.path.insert(0,'/home/work/build')
import anim
from pieces_x import V, OLD, SCV
from dati import GLP, PARTI
TXT={**OLD,**V}
def dur(n): return anim.vdur(n)
def events(P):
    TL=json.load(open(f'/home/work/build/out_timeline_P{P}.json'));ev=[];win=[]
    off={1:0,2:3,3:5}[P];topics=PARTI[P]
    def add(t0,n): ev.append((t0,t0+dur(n),TXT[n]))
    for name,s,f in TL:
        d=f/30
        if name in('prof1','prof2','prof3','prof4','prof5','prof6','prof7','prof8') or name=='intro' or name.startswith('prof'): win.append((s+0.4 if name!='sigla' else s,s+d-0.4)); continue
        if name=='cover': add(s+0.5,f'BEN{P}_R2')
        elif name=='dicosaparliamo': add(s+0.6,f'DCP{P}')
        elif name=='spiegone':
            t=0.7
            for j in range(len(PARTI[P-1])): n=f'SPG{P}_{j+1}';add(s+t,n);t+=dur(n)+0.9
        elif name.startswith('approfondimento'):
            g=int(name[len('approfondimento'):]);add(s+0.6,f'AP{topics[g-off-1]}')
        elif name.startswith('mappa'):
            k=int(name[5:]);add(s+0.8,f'MPR{k}_R2')
        elif name.startswith('pillola'):
            g=int(name[7:]);add(s+0.9,f'PI{topics[g-off-1]}')
        elif name.startswith('schema'):
            g=int(name[6:]);t=0.9
            for v in SCV[topics[g-off-1]]: add(s+t,v);t+=dur(v)+0.9
        elif name=='glossario':
            t=0.7;add(s+t,'LG0');t+=dur('LG0')+0.9
            for i in GLP[P]: n=f'LG{i+1}';add(s+t,n);t+=dur(n)+1.0
        elif name=='riepilogo': add(s+0.8,f'FZ{P}')
        elif name=='compiti': add(s+0.8,'COMPITI')
    return ev,win
if __name__=='__main__':
    for P in (1,2,3):
        e,w=events(P);print(P,len(e),[(round(a),round(b)) for a,b in w])
