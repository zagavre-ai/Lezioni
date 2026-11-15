import subprocess,re,json
R={}
for p in range(1,5):
    o=subprocess.run(['ffmpeg','-v','info','-i',f'aud/p{p}.wav','-af','silencedetect=n=-36dB:d=0.9','-f','null','-'],capture_output=True,text=True).stderr
    s=[float(x) for x in re.findall(r'silence_start: ([\d.]+)',o)];e=[float(x) for x in re.findall(r'silence_end: ([\d.]+)',o)]
    R[p]=list(zip(s,e))
    d=float(subprocess.check_output(['ffprobe','-v','error','-show_entries','format=duration','-of','csv=p=0',f'aud/p{p}.wav']))
    tot=sum(b-a for a,b in R[p]);print(p,len(R[p]),'pause >0.9s, totale',round(tot,1),'s su',round(d,1),'; risparmio se →0.6:',round(sum(b-a-0.6 for a,b in R[p] if b-a>1.0),1))
json.dump(R,open('sil.json','w'))
