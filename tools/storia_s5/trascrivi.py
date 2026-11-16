# uso: trascrivi.py audio16k.wav out.json   -> [{t0,t1,text}] a pezzi di 6-14 s tagliati sui silenzi
import sys,json,subprocess,re,numpy as np,sherpa_onnx
wav,out=sys.argv[1],sys.argv[2]
a=np.frombuffer(subprocess.run(['ffmpeg','-v','error','-i',wav,'-ac','1','-ar','16000','-f','s16le','-'],capture_output=True).stdout,np.int16).astype(np.float32)/32768
sr=16000;n=len(a)
# energia a finestre di 20 ms
w=sr//50;e=np.sqrt(np.convolve(a**2,np.ones(w)/w,'same'))[::w//2]  # una misura ogni 10 ms
thr=max(np.percentile(e,20)*1.5,0.004)
sil=e<thr
# candidate cut points: centri di silenzi >=0.25 s
cuts=[];i=0
while i<len(sil):
    if sil[i]:
        j=i
        while j<len(sil) and sil[j]:j+=1
        if (j-i)>=25:cuts.append((i+j)//2*0.01)
        i=j
    else:i+=1
dur=n/sr;chunks=[];s=0.0;last=0.0
for c in cuts+[dur]:
    if c-s>=14 or c==dur:
        # scegli il taglio più lontano da s entro 14 s
        pass
# greedy: da s, prendi l'ultimo taglio entro 14 s ma almeno 6 s
chunks=[];s=0.0
cs=np.array(cuts+[dur])
while s<dur-0.05:
    ok=cs[(cs>s+5)&(cs<=s+14)]
    t=ok[-1] if len(ok) else min(s+14,dur)
    chunks.append((s,float(t)));s=float(t)
rec=sherpa_onnx.OfflineRecognizer.from_whisper(encoder='/tmp/whisper/whisper-base/base-encoder.int8.onnx',decoder='/tmp/whisper/whisper-base/base-decoder.int8.onnx',tokens='/tmp/whisper/whisper-base/base-tokens.txt',language='it',task='transcribe',num_threads=4)
R=[]
for k,(t0,t1) in enumerate(chunks):
    seg=a[int(t0*sr):int(t1*sr)]
    st=rec.create_stream();st.accept_waveform(sr,seg);rec.decode_stream(st)
    R.append({'t0':round(t0,2),'t1':round(t1,2),'text':st.result.text.strip()})
    if k%20==0:print(k,len(chunks),flush=True)
json.dump(R,open(out,'w'),ensure_ascii=False,indent=0)
