import sys,os,json
sys.path.insert(0,'/tmp/w/b')
from plan import *
from multiprocessing import Pool
def seq_with_pages(p):
    seq=part_seq(p);pg=3 if p==1 else 1;out=[]
    for sp in seq:
        if sp[0]=='teach':
            n=sp[1];pk=pick(B[n-1],B[n]);npg=len(group_pages([(t,digits(x)) for t,x in pk]))
            sp=('teach',n,pg);pg+=npg
        out.append(sp)
    return out
def job(sp):
    name=spec_name(sp)
    if os.path.exists(f'{PC}/{name}.done'): return name,'cached'
    try:
        r=build_any(sp)
        json.dump({k:v for k,v in r.items() if k in('name','v','a','dur','src','cues')},open(f'{PC}/{name}.done','w'))
        if sp[0]=='teach': json.dump({'picks':r['picks'],'info':r['info']},open(f'{PC}/{name}.picks.json','w'))
        return name,'ok %.1f'%r['dur']
    except Exception as e:
        return name,'ERR '+str(e)[:400]
if __name__=='__main__':
    parts=[int(x) for x in sys.argv[1:]] or [1,2]
    todo=[]
    for p in parts:
        for sp in seq_with_pages(p):
            if all(have(v) for v in spec_voices(sp)): todo.append(sp)
    seen=set();t2=[]
    for sp in todo:
        n=spec_name(sp)
        if n not in seen: seen.add(n);t2.append(sp)
    with Pool(1) as pool:
        for n,r in pool.imap_unordered(job,t2): print(n,r,flush=True)
