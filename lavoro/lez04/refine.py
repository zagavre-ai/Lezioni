import json,subprocess,base64,urllib.request,sys,concurrent.futures as cf,os
sys.path.insert(0,'.')
import tl;from content import ARG
al=json.load(open('align.json'))['items']
ks=list(al)
def item(k):
    a,s,i=k[1:].split('.');a=int(a);s=int(s[1:]);i=int(i[1:]);return ARG[a-1]['slides'][s]['items'][i]
def one(k):
    t=tl.tm(al[k]);ss=max(0,t-4);W=18
    f=f'/tmp/rf_{k}.mp3'
    subprocess.run(['ffmpeg','-y','-v','error','-ss',f'{ss:.2f}','-t',str(W),'-i','dt/docente_all.mkv','-vn','-ac','1','-ar','16000','-b:a','48k',f],check=True)
    b=base64.b64encode(open(f,'rb').read()).decode()
    pr=(f"In this clip ({W} s) a teacher speaks (Italian with English terms; she often reads the English text aloud). The slide item is: \"{item(k)}\". "
        "At what second within the clip (decimal) does she START to talk about the content of THIS item (first word of the sentence/phrase where she begins treating it)? "
        "If the item is not clearly covered in the clip, return start null. Reply ONLY JSON {\"start\":number|null,\"heard\":\"first words\"}.")
    body={"contents":[{"parts":[{"inline_data":{"mime_type":"audio/mp3","data":b}},{"text":pr}]}],"generationConfig":{"temperature":0,"responseMimeType":"application/json"}}
    for att in range(3):
        try:
            r=urllib.request.Request("https://generativelanguage.googleapis.com/v1beta/models/gemini-flash-latest:generateContent",json.dumps(body).encode(),{"Content-Type":"application/json"})
            j=json.load(urllib.request.urlopen(r,timeout=120));o=json.loads(j['candidates'][0]['content']['parts'][0]['text']);break
        except Exception as e: o={'start':None,'heard':'ERR'}
    return k,t,ss,o
with cf.ThreadPoolExecutor(6) as ex: R=list(ex.map(one,ks))
out={};ch=0
for k,t,ss,o in R:
    s=o.get('start') if isinstance(o,dict) else None
    new=t
    if isinstance(s,(int,float)) and 0<=s<=18: new=ss+s
    out[k]={'t_old':t,'t_new':new,'heard':str(o.get('heard'))[:60] if isinstance(o,dict) else ''}
    if abs(new-t)>0.3: ch+=1
json.dump(out,open('refine.json','w'),ensure_ascii=False,indent=1)
print('rifiniti',ch,'su',len(ks),'| scarto medio',sum(abs(v['t_new']-v['t_old']) for v in out.values())/len(out))
