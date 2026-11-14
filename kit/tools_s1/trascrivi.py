#!/usr/bin/env python3
"""Trascrizione con timestamp (modello transcribe via proxy). Uso: trascrivi.py video.mp4 out.json [chunk_s=150]"""
import sys,os,json,subprocess,base64,time,concurrent.futures as cf,urllib.request,re
V,OUT=sys.argv[1],sys.argv[2];CH=int(sys.argv[3]) if len(sys.argv)>3 else 150
MODEL=os.environ.get('TRMODEL','gemini-3.5-transcribe')
d=float(subprocess.check_output(['ffprobe','-v','error','-show_entries','format=duration','-of','csv=p=0',V]))
tmp=OUT+'_chunks';os.makedirs(tmp,exist_ok=True)
PROMPT=("Trascrivi in italiano, parola per parola, questo audio di una lezione di storia. Restituisci SOLO JSON: lista di segmenti "
 "[{\"s\":inizio_in_secondi,\"e\":fine_in_secondi,\"t\":\"frase\"}] con tempi relativi all'inizio dell'audio (decimali), frasi di 3-12 secondi. "
 "Non omettere nulla del parlato, non aggiungere nulla. Nomi propri e date scritti correttamente.")
def one(i):
    f=f'{tmp}/c{i:03d}.json'
    if os.path.exists(f):return json.load(open(f))
    st=i*CH;mp=f'{tmp}/c{i:03d}.mp3'
    subprocess.run(['ffmpeg','-v','error','-y','-ss',str(st),'-t',str(CH),'-i',V,'-vn','-ac','1','-ar','16000','-b:a','32k',mp],check=True)
    b=base64.b64encode(open(mp,'rb').read()).decode()
    body={'contents':[{'parts':[{'text':PROMPT},{'inline_data':{'mime_type':'audio/mp3','data':b}}]}],'generationConfig':{'temperature':0,'responseMimeType':'application/json'}}
    for k in range(4):
        try:
            r=urllib.request.Request(f'https://generativelanguage.googleapis.com/v1beta/models/{MODEL}:generateContent',data=json.dumps(body).encode(),headers={'Content-Type':'application/json','x-goog-api-key':'dummy'})
            j=json.load(urllib.request.urlopen(r,timeout=300))
            t=j['candidates'][0]['content']['parts'][0]['text']
            seg=json.loads(t);seg=[{'s':round(x['s']+st,2),'e':round(x['e']+st,2),'t':x['t']} for x in seg]
            json.dump(seg,open(f,'w'),ensure_ascii=False);return seg
        except Exception as ex:
            print('retry',i,str(ex)[:150],file=sys.stderr);time.sleep(5*(k+1))
    return []
n=int(d//CH)+1
with cf.ThreadPoolExecutor(4) as ex:res=list(ex.map(one,range(n)))
allseg=[s for r in res for s in r]
json.dump(allseg,open(OUT,'w'),ensure_ascii=False,indent=0);print(len(allseg),'segmenti',d)
