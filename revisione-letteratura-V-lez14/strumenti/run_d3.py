import json,sys,os,subprocess
sys.path.insert(0,'/tmp/w14');sys.path.insert(0,'/tmp/w14/build')
import buildd,encd,piano
P=int(sys.argv[1]);C=json.load(open('/tmp/w14/cuts.json'))
B={1:[('D0',0.17,C['P1_D0|D1']),('D1',C['P1_D0|D1'],C['P1_D1|D2']),('D2',C['P1_D1|D2'],C['P1_D2|D3']),('D3',C['P1_D2|D3'],C['P1_D3|D4']),('D4',C['P1_D3|D4'],C['P1D4|P2D0'])],
   2:[('D0',C['P1D4|P2D0'],C['P2_D0|D1']),('D1',C['P2_D0|D1'],C['P2_D1|D2']),('D2',C['P2_D1|D2'],C['P2_D2|D3']),('D3',C['P2_D2|D3'],C['P2_D3|D4']),('D4',C['P2_D3|D4'],C['P2_D4|D5']),('D5',C['P2_D4|D5'],C['P2_D5|D6']),('D6',C['P2_D5|D6'],3860.0)]}[P]
os.makedirs(f'/tmp/w14/dq{P}',exist_ok=True)
pages={'cover':1};plan={}
for n,s0,s1 in B:
    nf=round((s1-s0)*30);lst=[];cum=0
    if n=='D0' and P==2: st=[[s0,s1,1,None]]
    elif n=='D0' and P==1: st=[[s0,s0+149.0,1,None],[s0+149.0,s0+165.5,'dcpA',None],[s0+165.5,s1,'dcpB',None]]
    else: st=piano.stati(s0,s1)
    for i,(a,b,s,c) in enumerate(st):
        end=nf if i==len(st)-1 else round((b-s0)*30);k=max(end-cum,0);cum+=k
        if k==0: continue
        if P==2 and s==48: s=1
        if s in('dcpA','dcpB'):
            pr=0 if s=='dcpA' else 1;lst.append((buildd.ensure_png({'k':'dcp','P':P,'part':pr,'pag':pages.setdefault(s,len(pages)+1)},P,pages),k));continue
        if s==1: key={'k':'cover','P':P}
        elif s==2: key={'k':'foto','lab':buildd.label(P,2,a),'pag':pages.setdefault(2,len(pages)+1)}
        elif s in('C','B'): key={'k':'libro','n':s,'i':c,'lab':buildd.label(P,s,a),'pag':pages.setdefault(s,len(pages)+1)}
        else:
            part=0 if c in (0,1) else 1
            key={'k':'cards','s':s,'c':c,'part':part,'lab':buildd.label(P,s,a),'pag':pages.setdefault(f'{s}_{part}',len(pages)+1)}
        lst.append((buildd.ensure_png(key,P,pages),k))
    plan[n]={'s0':s0,'s1':s1,'nf':nf,'lst':lst}
json.dump({'plan':plan,'pages':{str(k):v for k,v in pages.items()}},open(f'/tmp/w14/dq{P}/plan.json','w'),indent=1)
subprocess.run(['node','/tmp/w14/build/render.js','/tmp/w14/build/html','/tmp/w14/build/png'],check=True)
for n,p in plan.items():
    out=f'/tmp/w14/dq{P}/{n}.mp4'
    if os.path.exists(out+'.ok'): continue
    encd.encode(p['lst'],p['s0'],out);open(out+'.ok','w').close();print(n,'ok',flush=True)
open(f'/tmp/w14/dq{P}/tutto.fatto','w').close()
