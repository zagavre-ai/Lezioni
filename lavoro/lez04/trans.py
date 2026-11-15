import sys,json,base64,subprocess,os,re,urllib.request,concurrent.futures as cf
CH=240
def one(args):
    p,k=args
    out=f'tr/p{p}_{k:02d}.json'
    if os.path.exists(out): return
    mp3=f'tr/p{p}_{k:02d}.mp3'
    subprocess.run(['ffmpeg','-y','-v','error','-ss',str(k*CH),'-t',str(CH),'-i',f'aud/p{p}.wav','-ac','1','-ar','16000','-b:a','48k',mp3],check=True)
    b=base64.b64encode(open(mp3,'rb').read()).decode()
    prompt=("Transcribe this English lesson audio (teacher speaking, Italian-accented English) verbatim, sentence by sentence. "
     "Return ONLY a JSON array of objects {\"s\":start_seconds,\"e\":end_seconds,\"t\":text} with times in seconds (decimal) from the start of THIS clip, as precise as possible. Do not skip any speech.")
    body={"contents":[{"parts":[{"inline_data":{"mime_type":"audio/mp3","data":b}},{"text":prompt}]}],"generationConfig":{"temperature":0,"responseMimeType":"application/json"}}
    for att in range(3):
        try:
            r=urllib.request.Request("https://generativelanguage.googleapis.com/v1beta/models/gemini-flash-latest:generateContent",json.dumps(body).encode(),{"Content-Type":"application/json"})
            j=json.load(urllib.request.urlopen(r,timeout=300))
            t=j['candidates'][0]['content']['parts'][0]['text']
            a=json.loads(t)
            for x in a: x['s']+=k*CH; x['e']+=k*CH
            json.dump(a,open(out,'w'),ensure_ascii=False);return
        except Exception as e: err=e
    print('ERR',p,k,err)
jobs=[]
for p in range(1,5):
    d=float(subprocess.check_output(['ffprobe','-v','error','-show_entries','format=duration','-of','csv=p=0',f'aud/p{p}.wav']))
    jobs+=[(p,k) for k in range(int(d//CH)+1)]
with cf.ThreadPoolExecutor(4) as ex: list(ex.map(one,jobs))
open('tr/fatto','w').write('1')
