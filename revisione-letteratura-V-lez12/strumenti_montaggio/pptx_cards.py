import json
P=json.load(open('../pptx.json'))
def cards(slides):
    out=[]
    for n in slides:
        d=P[n-1];title=[l for nm,ls in d['raw'] if nm.startswith('Text 5') for l in ls][1]
        for nm,ls in d['raw']:
            if nm.startswith('Text 6'):
                for p in ls:
                    lead,_,rest=p.partition(': ');out.append({'lead':lead,'text':rest,'title':title})
    return out
CARDS={'D1':cards([2,3]),'D2':cards([4,5]),'D3':cards([6]),'D4':cards([8,10]),'D5':cards([11,13,14])}
