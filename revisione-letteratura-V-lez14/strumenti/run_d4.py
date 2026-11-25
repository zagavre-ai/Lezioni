import json,sys,os,subprocess
sys.path.insert(0,'/tmp/w14');sys.path.insert(0,'/tmp/w14/build')
import buildd,encd,piano
P=int(sys.argv[1]);REDO=sys.argv[2].split(',')
PL=json.load(open(f'/tmp/w14/dq{P}/plan.json'));pages=PL['pages'];plan=PL['plan']
pages={k:v for k,v in pages.items()}
def pg(k): return pages.setdefault(k,len(pages)+1)
for n in REDO:
    s0,s1,nf=plan[n]['s0'],plan[n]['s1'],plan[n]['nf'] if 's1' in plan[n] else None
    s1=plan[n]['s1'];nf=plan[n]['nf']
    st=piano.stati(s0,s1)
    if P==1 and n=='D2': st=[[a,b,s,(2 if (s==3 and a>=941.9) else c)] for a,b,s,c in st]
    lst=[];cum=0
    for i,(a,b,s,c) in enumerate(st):
        end=nf if i==len(st)-1 else round((b-s0)*30);k=max(end-cum,0);cum+=k
        if k==0: continue
        if P==2 and s==48: s=1
        if s==1: key={'k':'cover','P':P}
        elif s==2: key={'k':'foto','lab':buildd.label(P,2,a),'pag':pg('2')}
        elif s in('C','B'): key={'k':'libro','v':3,'n':s,'i':c,'lab':buildd.label(P,s,a),'pag':pg(s)}
        else:
            part=0 if c in (None,0,1) else 1
            key={'k':'cards','s':s,'c':c,'part':part,'lab':buildd.label(P,s,a),'pag':pg(f'{s}_{part}')}
        lst.append((buildd.ensure_png(key,P,pages),k))
    plan[n]['lst']=lst
json.dump({'plan':plan,'pages':pages},open(f'/tmp/w14/dq{P}/plan.json','w'),indent=1)
subprocess.run(['node','/tmp/w14/build/render.js','/tmp/w14/build/html','/tmp/w14/build/png'],check=True)
for n in REDO:
    out=f'/tmp/w14/dq{P}/{n}.mp4'
    encd.encode(plan[n]['lst'],plan[n]['s0'],out);print(n,'ok',flush=True)
