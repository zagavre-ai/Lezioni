# PDF a slide (una pagina = un argomento) → blocks.json: titolo di pagina + paragrafi/elenchi con grassetti
import json,re
P=json.load(open('pdf_lines.json'))
blocks=[];titles={}
def txt(runs):return ''.join(t for b,t in runs)
for pi,lines in enumerate(P):
    if pi==0: continue
    tl=[l for l in lines if l['size']>=30]
    titles[pi+1]=re.sub(r'\s+',' ',' '.join(txt(l['runs']) for l in tl)).strip()
    prev_top=None;cur=None
    for l in lines:
        if l['size']>=30 or not txt(l['runs']).strip(): continue
        t=txt(l['runs']).lstrip()
        runs=[list(r) for r in l['runs']]
        for r in runs:
            if r[1].strip(): r[1]=r[1].lstrip();break
        bul=bool(re.match(r'^•',t));num=bool(re.match(r'^\d\.',t))
        gap=(l['top']-prev_top) if prev_top is not None else 99
        new=cur is None or bul or num or gap>45
        if bul or num:
            for r in runs:
                if r[1].strip(): r[1]=re.sub(r'^(•|\d\.)\s*','',r[1],count=1);break
        if new:
            cur={'t':'li' if (bul or num) else 'p','runs':runs,'pg':pi+1};blocks.append(cur)
        else:
            cur['runs'].append([False,' ']);cur['runs']+=runs
        prev_top=l['top']
for b in blocks:
    m=[]
    for bo,t in b['runs']:
        if m and m[-1][0]==bo: m[-1][1]+=t
        else: m.append([bo,t])
    b['runs']=[[bo,re.sub(r'\s+',' ',t)] for bo,t in m]
    b['runs'][0][1]=b['runs'][0][1].lstrip();b['runs'][-1][1]=b['runs'][-1][1].rstrip()
json.dump(blocks,open('blocks.json','w'),ensure_ascii=False,indent=0)
json.dump(titles,open('page_titles.json','w'),ensure_ascii=False,indent=0)
for i,b in enumerate(blocks): print(i,b['pg'],b['t'],''.join(('**'+t+'**' if bo else t) for bo,t in b['runs']))
print(titles)
