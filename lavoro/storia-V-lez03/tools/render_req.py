import sys,os;sys.path.insert(0,'/tmp/w/tools')
import plan
def render_all(workers=1):
    todo=[(p,f) for p,f in plan.REQ.items() if not os.path.exists(p)]
    print(len(todo),'png da rendere',flush=True)
    if not todo: return
    with plan.SL.R() as r:
        for p,f in todo: r.shot(f(),p)
