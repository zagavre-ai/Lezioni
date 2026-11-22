import ast,json,sys,os
sys.path.insert(0,'/home/user/w/build')
import gfx
gfx.NOCAM=True
from kore import *
from buildall import PSN,COMPITI,numbering  # noqa
from gfx import *
W='/home/user/w'
OUTD=W+'/dispensa';os.makedirs(OUTD,exist_ok=True)
EXTRA=".foot{top:1257px}.fl,.fr{top:1276px}html,body{height:1357px}"
def fix(h):return h.replace('</style>',EXTRA+'</style>',1)
keys=json.load(open(W+'/out/pagine.json'));keys=sorted(((v,ast.literal_eval(k) if k.startswith('(') else k) for k,v in keys.items()))
css_rows=".card{padding-top:6px;padding-bottom:6px;line-height:56px}.card .n{top:6px}"
def page_html(num,key,mappe=False):
    if key=='cover':return cover(["Gli anni Sessanta","tra crisi e progressi"],[x['nome'] for x in ARGS],False,num)
    if key=='indice':return wslide('Videolezione','Di cosa parliamo',[dict(t=a['nome']) for a in ARGS],None,num,extra_css=css_rows)
    t=key[0]
    if t=='p':
        nome,win=key[1],key[2];c=[c for c in CH if c['nome']==nome][0];a=ARGS[c['arg']-1]
        tl=2 if len(a['tit'])>48 else 1
        return slide(f"{a['n']:02d} · {a['nome']}",a['tit'],[a['cards'][i] for i in win],None,num,a['kw'],tl=tl)
    if t=='img':
        im=IMG[key[1]];ch=[c for c in CH if any(v[0]=='i' and v[2]==key[1] for v in c['views'])][0];a=ARGS[ch['arg']-1]
        return image_slide(f"{a['n']:02d} · {a['nome']}",im['tit'],f"{B}/img/{im['f']}",num,a['kw'],tl=2 if len(im['tit'])>48 else 1)
    if t=='ap':
        name,w=key[1],key[2];vn=vname(name);S_=sentences(TEXTS[vn]);q=S_[0];cards=[dict(t=screen(s)) for s in S_[1:]][w*3:w*3+3]
        lab=name[2:];n=int(lab[0]);a=ARGS[n-1]
        return wslide(f"APPROFONDIMENTO · {a['n']:02d} {a['nome']}",q,cards,None,num,tl=2 if len(q)>62 else 1)
    if t=='ps':
        n=key[1];a=ARGS[n-1];lines=[dict(t=screen(TEXTS[vname(x)])) for x in PSN[n]]
        return wslide(f"RIPASSO · {n:02d} {a['nome']}",'Schema di ripasso',lines,None,num,extra_css=css_rows)
    if t=='map':
        m=MAPS[key[1]-1];sh={'centro'}|{(c,r) for c,col in enumerate(m['cols']) for r in range(len(col))}
        return map_html(m,sh,None,num)
    if t=='gl':
        S_=sentences(TEXTS[vname('GL1')]);terms=[]
        for s in S_[1:]:
            l,_,r=s.partition(':');terms.append(dict(l=l.strip(),t=screen(r.strip())))
        return wslide('Glossario','Le parole chiave della lezione',terms[key[1]*3:key[1]*3+3],None,num)
    if t=='co':
        C=[dict(t=c) for c in COMPITI];return wslide('Compiti del prof','Compiti',C[key[1]*2:key[1]*2+2],None,num,extra_css=".card{line-height:56px}")
    raise KeyError(key)
if __name__=='__main__':
    jobs=[];pages=[]
    for num,key in keys:
        h=fix(page_html(num,key));hp=f'{B}/html/disp_{num:03d}.html';open(hp,'w').write(h)
        jobs.append(dict(html=hp,out=f'{OUTD}/p{num:03d}.png',h=1357,textout=f'{OUTD}/p{num:03d}.json'));pages.append(num)
    # copertina MAPPE
    cm=cover(["Gli anni Sessanta","tra crisi e progressi"],[x['nome'] for x in ARGS],False,1,mappe=True)
    open(B+'/html/disp_mappe_cover.html','w').write(fix(cm))
    jobs.append(dict(html=B+'/html/disp_mappe_cover.html',out=f'{OUTD}/mappe_cover.png',h=1357,textout=f'{OUTD}/mappe_cover.json'))
    for k in (1,2,3):
        m=MAPS[k-1];sh={'centro'}|{(c,r) for c,col in enumerate(m['cols']) for r in range(len(col))}
        hp=f'{B}/html/disp_mappa{k}.html';open(hp,'w').write(fix(map_html(m,sh,None,k+1)))
        jobs.append(dict(html=hp,out=f'{OUTD}/mappa{k}.png',h=1357,textout=f'{OUTD}/mappa{k}.json'))
    json.dump(jobs,open(B+'/jobs_disp.json','w'))
    r=subprocess.run(['node',B+'/render.js',B+'/jobs_disp.json'],capture_output=True,text=True,cwd=B);print(r.stdout[-300:],r.stderr[-300:])
    json.dump(pages,open(OUTD+'/pages.json','w'))
