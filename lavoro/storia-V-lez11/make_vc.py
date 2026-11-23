import sys,os,json
sys.path.insert(0,'/home/user/work/build')
exec(open('/home/user/work/build/build2.py').read())
P=json.load(open(B+'/plan.json'))
pn={(k,tuple(w)):v for k,w,v in P['pn']}
VC={k:(v[0],v[1]) for k,v in P['VC'].items()}
CL=B+'/clips/'
def done(n): return os.path.exists(CL+n+'.mkv.ok')
def mark(n): open(CL+n+'.mkv.ok','w').write('1');print(n,flush=True)
# approfondimento: 3 voci AN di ogni argomento
for t in range(1,7):
    n=f'AN_T{t}'
    if done(n): continue
    o=0.5;seq=[];places=[]
    for k in range(3*t-2,3*t+1):
        key=f'AN{k}';d=dur(vpath(key));ev,wl=VC[key]
        end=o+d+0.7
        seq+=vc_seq(key,ev,wl,pn,o,end);places.append((o,key));o=end
    tot=nfr(o)/30
    enc_seq(seq,tot,CL+n+'.mkv')
    m=Mix(tot)
    for a,key in places: m.voice(a,key)
    m.save(CL+n+'.wav');mark(n)
# schema pillola
for t in range(1,7):
    n=f'SCH_T{t}'
    if done(n): continue
    key=f'SC{t}';evs,end=ev_SC(t);ev,wl=VC[key]
    tot=nfr(end)/30
    seq=vc_seq(key,ev,wl,pn,0,tot);enc_seq(seq,tot,CL+n+'.mkv')
    m=Mix(tot)
    for a,i,nm,d in evs: m.voice(a,nm)
    m.save(CL+n+'.wav');mark(n)
# glossario
n='GLOSS'
if not done(n):
    o=0.5;seq=[];places=[]
    for g in ('GL1','GL2'):
        d=dur(vpath(g));ev,wl=VC[g];end=o+d+0.8
        seq+=vc_seq(g,ev,wl,pn,o,end);places.append((o,g));o=end
    tot=nfr(o)/30;enc_seq(seq,tot,CL+n+'.mkv')
    m=Mix(tot)
    for a,g in places: m.voice(a,g)
    m.save(CL+n+'.wav');mark(n)
# compiti: voce COMP1, COMP2, COMP3 (chiusura); ogni esercizio si accende quando la voce lo legge
n='COMPITI_SL'
if not done(n):
    import subprocess as sp
    if vpath('COMP3') is None:
        sp.run(['ffmpeg','-y','-v','error','-f','lavfi','-i','anullsrc=r=24000:cl=mono','-t','7.0',B+'/vox_prov/COMP3.wav'],check=True)
    seq=[];o=0;pl=[]
    for c,v,first in (('CP1','COMP1',1),('CP2','COMP2',3),('CP3','COMP3',1)):
        d=dur(vpath(v))+1.2;w0=VC[c][1][0]
        if c=='CP3': ev=[(0,None),(0.6,1)]
        else:
            tf=tempi_frasi(v,TXT[v]);ev=[(0,None)]+[(0.6+a,first+i) for i,(a,b_,f) in enumerate(tf)]
        wl=[w0]*len(ev)
        # indice attivo relativo alla pagina: CP1 -> 1,2 ; CP2 -> 3,4 -> nella pagina 1,2
        seq+=vc_seq(c,[(t,(None if a is None else (a if c!='CP2' else a-2))) for t,a in ev],wl,pn,o,o+d);pl.append((o+0.6,v));o+=d
    tot=nfr(o)/30;enc_seq(seq,tot,CL+n+'.mkv');m_=Mix(tot)
    for a,v in pl: m_.voice(a,v)
    if 'vox_prov' in vpath('COMP3'): m_.jingle(o-8.2+0.5,'finale',-3.0)
    m_.save(CL+n+'.wav');mark(n)
