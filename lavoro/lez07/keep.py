# pause > 1,0 s ridotte a 0,6 s (regola delle lezioni 4-5). uso: keep.py audio.wav inizio fine out.json
import subprocess,re,json,sys
a,t0,t1,out=sys.argv[1],float(sys.argv[2]),float(sys.argv[3]),sys.argv[4]
o=subprocess.run(['ffmpeg','-v','info','-i',a,'-af','silencedetect=n=-36dB:d=0.9','-f','null','-'],capture_output=True,text=True).stderr
s=[float(x) for x in re.findall(r'silence_start: ([\d.]+)',o)];e=[float(x) for x in re.findall(r'silence_end: ([\d.]+)',o)]
K=[];cur=t0
for x,y in zip(s,e):
    if y<=t0 or x>=t1 or y-x<=1.0: continue
    c0=max(cur,x+0.3);c1=min(t1,y-0.3)
    if c0>cur+0.05: K.append([round(cur,4),round(c0,4)])
    cur=c1
if t1>cur: K.append([round(cur,4),round(t1,4)])
json.dump({'1':K},open(out,'w'));tot=sum(b-a for a,b in K)
print(len(K),'pezzi, docente tagliato',round(tot/60,2),'min su',round((t1-t0)/60,2))
