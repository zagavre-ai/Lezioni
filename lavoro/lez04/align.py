import json,urllib.request,sys
sys.path.insert(0,'.');from content import ARG
OFF=[0,921.0,1804.6,2654.03]
T=[]
for p in range(1,5):
    for x in json.load(open(f'tr/p{p}.json')): T.append((round(x['s']+OFF[p-1],1),round(x['e']+OFF[p-1],1),x['t']))
tr='\n'.join(f'[{s}-{e}] {t}' for s,e,t in T)
items=[];
for a in ARG:
    for si,s in enumerate(a['slides']):
        for ii,it in enumerate(s['items']): items.append(f"A{a['n']}.S{si}.I{ii}: {it}")
prompt=("Below is a timestamped transcript (seconds, global timeline) of an Italian teacher explaining, in Italian with English terms, a lesson on Types of Business; "
"then the list of slide items (English text) the teacher presents in order. For EACH item give the time in seconds when the teacher STARTS talking about that item "
"(the moment the item should be highlighted). Times must be non-decreasing in the item order, inside the transcript. If the teacher skips an item, give the time of the next covered content. "
"Also give for each of the 5 topics (A1..A5) the time the teacher starts introducing it (A1 is the first, after the intro of the whole lesson), and the lesson_start time (first speech).\n"
"Return ONLY JSON: {\"lesson_start\":s,\"topic_start\":{\"A1\":s,...},\"items\":{\"A1.S0.I0\":s,...}}\n\nTRANSCRIPT:\n"+tr+"\n\nITEMS:\n"+'\n'.join(items))
body={"contents":[{"parts":[{"text":prompt}]}],"generationConfig":{"temperature":0,"responseMimeType":"application/json"}}
r=urllib.request.Request("https://generativelanguage.googleapis.com/v1beta/models/gemini-flash-latest:generateContent",json.dumps(body).encode(),{"Content-Type":"application/json"})
import time
for att in range(4):
    try:
        j=json.load(urllib.request.urlopen(r,timeout=600));break
    except Exception as e:
        print('retry',att,e, getattr(e,'read',lambda:b'')()[:300]);time.sleep(5)
a=json.loads(j['candidates'][0]['content']['parts'][0]['text'])
json.dump(a,open('align.json','w'),indent=1);json.dump(T,open('transcript_global.json','w'),ensure_ascii=False)
print(a['lesson_start'],a['topic_start'],len(a['items']),len(items))
