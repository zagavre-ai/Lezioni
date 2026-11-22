import json,sys
W='/home/claude/w19'
for n in (1,2):
    tl=json.load(open(f'{W}/timeline_P{n}_tmp.json'));json.dump(tl,open(f'{W}/timeline_P{n}.json','w'),ensure_ascii=False,indent=0)
    tool=[]
    for it in tl:
        i=it['id'];t=it['tipo']
        if t in('prof','intro'): nm='D_'+i
        elif t=='titolo': nm='T'+i[1:]
        elif t=='quiz': nm='Q'+i[1:]
        elif t=='glossario': nm=f'GL{n}'
        elif t=='ripasso_finale': nm=f'RF{n}'
        elif t=='finale': nm='FI'
        else: nm=i
        tool.append([nm,it['inizio'],it['durata']])
    json.dump(tool,open(f'{W}/timeline_tool_P{n}.json','w'))
    print(n,len(tool),tl[-1]['inizio']+tl[-1]['durata'])
