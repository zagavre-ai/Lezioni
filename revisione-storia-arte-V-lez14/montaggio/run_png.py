import sys,json,os;sys.path.insert(0,'/tmp/w/build')
import plan,subprocess
tl=plan.build()
jobs=[]
os.makedirs('/tmp/w/build/html',exist_ok=True)
for p,h in plan.HTML.items():
    if os.path.exists(p):continue
    hp=p.replace('/png/','/html/').replace('.png','.html');open(hp,'w').write(h)
    jobs.append(dict(html=hp,out=p))
print(len(jobs),'da rendere')
json.dump(jobs,open('/tmp/w/build/jobs.json','w'))
if jobs:
    r=subprocess.run(['node','/tmp/w/build/render.js','/tmp/w/build/jobs.json'],env=dict(os.environ,NODE_PATH='/opt/node22/lib/node_modules'),capture_output=True,text=True);print(r.stdout[-500:],r.stderr[-800:])
    print(open('/tmp/w/build/jobs.json.rep').read()[:3000])
