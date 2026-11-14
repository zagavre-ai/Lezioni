import sys,os,json,base64,subprocess,urllib.request,re
src,out=sys.argv[1:3]; CH=300
d=float(subprocess.run(['ffprobe','-v','error','-show_entries','format=duration','-of','csv=p=0',src],capture_output=True,text=True).stdout)
res=[]
for i in range(int(d//CH)+1):
    s=i*CH
    if s>=d: break
    f=f'{out}_c{i}.mp3'
    subprocess.run(['ffmpeg','-y','-v','error','-ss',str(s),'-t',str(CH),'-i',src,'-vn','-ac','1','-ar','16000','-b:a','32k',f],check=True)
    b=base64.b64encode(open(f,'rb').read()).decode()
    body={"contents":[{"parts":[{"inline_data":{"mime_type":"audio/mp3","data":b}},{"text":"Trascrivi fedelmente in italiano questo parlato di un docente di letteratura. Una riga per frase nel formato [mm:ss] testo, con il tempo di inizio della frase relativo all'inizio di questo audio. Nomi propri e titoli scritti correttamente. Solo la trascrizione."}]}],"generationConfig":{"temperature":0}}
    for k in range(4):
        try:
            r=urllib.request.Request('https://generativelanguage.googleapis.com/v1beta/models/gemini-3.8-flash:generateContent',json.dumps(body).encode(),{'Content-Type':'application/json','x-goog-api-key':'dummy'})
            t=json.load(urllib.request.urlopen(r,timeout=300))['candidates'][0]['content']['parts'][0]['text'];break
        except Exception as e: t='';print('retry',i,e,flush=True)
    for m in re.finditer(r'\[(\d+):(\d+)\]\s*(.+)',t):
        res.append([s+int(m[1])*60+int(m[2]),m[3].strip()])
    os.remove(f);print('chunk',i,len(res),flush=True)
json.dump(res,open(out+'.json','w'),ensure_ascii=False)
open(out+'.fatto','w').write('1')
