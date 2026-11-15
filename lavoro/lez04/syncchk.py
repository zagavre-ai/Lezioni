import json,subprocess,base64,urllib.request,sys,random
sys.path.insert(0,'.')
import tl;from content import ARG
al=json.load(open('align.json'))['items']
keys=[f'A1.S0.I1',f'A1.S2.I1',f'A1.S5.I2',f'A2.S0.I2',f'A2.S3.I1',f'A3.S1.I1',f'A3.S4.I2',f'A4.S2.I1',f'A5.S2.I2',f'A5.S3.I2']
def item(k):
    a,s,i=k[1:].split('.');a=int(a);s=int(s[1:]);i=int(i[1:]);return ARG[a-1]['slides'][s]['items'][i]
res=[]
for k in keys:
    t=tl.tm(al[k]);
    subprocess.run(['ffmpeg','-y','-v','error','-ss',f'{max(0,t-3):.2f}','-t','14','-i','dt/docente_all.mkv','-vn','-ac','1','-ar','16000','-b:a','48k','/tmp/c.mp3'],check=True)
    b=base64.b64encode(open('/tmp/c.mp3','rb').read()).decode()
    pr=f"In this clip (14 s) a teacher speaks (Italian with English terms). The slide item is: \"{item(k)}\". At what second within the clip (decimal) does she START talking about the content of this item? Reply ONLY a JSON {{\"start\":number,\"heard\":\"first words\"}}."
    body={"contents":[{"parts":[{"inline_data":{"mime_type":"audio/mp3","data":b}},{"text":pr}]}],"generationConfig":{"temperature":0,"responseMimeType":"application/json"}}
    for att in range(3):
        try:
            r=urllib.request.Request("https://generativelanguage.googleapis.com/v1beta/models/gemini-flash-latest:generateContent",json.dumps(body).encode(),{"Content-Type":"application/json"})
            j=json.load(urllib.request.urlopen(r,timeout=120));o=json.loads(j['candidates'][0]['content']['parts'][0]['text']);break
        except Exception as e: o={'start':None,'heard':str(e)[:50]}
    print(k,'atteso 3.0 trovato',o.get('start'),'|',str(o.get('heard'))[:70],flush=True)
