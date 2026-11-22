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
# compiti (due pagine, voce COMP1/COMP2)
n='COMPITI_SL'
if not done(n):
    seq=[];o=0;pl=[]
    for c,v in (('CP1','COMP1'),('CP2','COMP2')):
        d=dur(vpath(v))+1.4;ev,wl=VC[c];seq+=vc_seq(c,ev,wl,pn,o,o+d);pl.append((o+0.6,v));o+=d
    tot=nfr(o)/30;enc_seq(seq,tot,CL+n+'.mkv');m=Mix(tot)
    for a,v in pl: m.voice(a,v)
    m.save(CL+n+'.wav');mark(n)
