import json,sys,os,subprocess
sys.path.insert(0,'/tmp/w14');sys.path.insert(0,'/tmp/w14/build')
import buildd,encd,piano
P=int(sys.argv[1]);TL=json.load(open(f'/tmp/w14/tl{P}.json'));OFF=json.load(open('/tmp/w14/offsets.json'))[str(P)]
os.makedirs(f'/tmp/w14/d{P}',exist_ok=True)
D=[(n,a,d) for n,a,d in TL if n.startswith('D') and n[1:].isdigit()]
pages={'cover':1};plan={};prev_end=None
for n,a,d in D:
    off=OFF[str(min((float(k) for k in OFF),key=lambda k:abs(k-a)))]
    s0=a+off;s1=a+d+off
    trim=0.0
    if prev_end is not None and prev_end-s0>0.3: trim=round(prev_end-s0,3)
    prev_end=s1
    f0=round((a+trim)*30);f1=round((a+d)*30);s0a=s0+trim
    if n=='D0' and P==2:
        lst=[(buildd.ensure_png({'k':'cover'},P,pages),f1-f0)];pages.setdefault('cover',1)
    else:
        lst,used=buildd.compose(P,n,a,d,off,s0a,f0,f1,pages,trim,None)
    plan[n]={'f0':f0,'f1':f1,'s0':s0a,'trim':trim,'off':off,'lst':lst}
json.dump({'plan':plan,'pages':{str(k):v for k,v in pages.items()}},open(f'/tmp/w14/d{P}/plan.json','w'),indent=1)
subprocess.run(['node','/tmp/w14/build/render.js','/tmp/w14/build/html','/tmp/w14/build/png'],check=True)
for n,p in plan.items():
    out=f'/tmp/w14/d{P}/{n}.mp4'
    if os.path.exists(out+'.ok'): continue
    encd.encode(p['lst'],p['s0'],out);open(out+'.ok','w').close();print(n,'ok',flush=True)
open(f'/tmp/w14/d{P}/tutto.fatto','w').close()
