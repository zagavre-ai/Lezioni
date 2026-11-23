import sys,pickle;sys.path.insert(0,'/tmp/claude-0/w/build')
import mapdefs,layout
name=sys.argv[1];seed=int(sys.argv[2]);iters=int(sys.argv[3])
m=getattr(mapdefs,name)()
init={i:(n.cx,n.cy) for i,n in m.nodes.items()}
e=layout.solve(m,seed=seed,iters=iters,init=init)
pickle.dump({i:(n.cx,n.cy,n.w) for i,n in m.nodes.items()},open('/tmp/claude-0/w/build/lay_%s_%d.pkl'%(name,seed),'wb'))
m.static().convert('RGB').save('/tmp/claude-0/w/build/lay_%s_%d.png'%(name,seed))
print(name,seed,e)
