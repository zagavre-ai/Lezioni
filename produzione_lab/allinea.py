# chunk a pause + whisper tiny -> segmenti con tempo ~esatto. uso: allinea.py audio.wav out.json
import sys,json,subprocess,numpy as np,sherpa_onnx,time
wav,out=sys.argv[1:3]
x=np.frombuffer(subprocess.run(['ffmpeg','-v','error','-i',wav,'-ac','1','-ar','16000','-f','f32le','-'],capture_output=True).stdout,np.float32)
sr=16000;h=int(.05*sr);N=len(x)//h
en=np.array([float((x[i*h:(i+1)*h]**2).mean()) for i in range(N)])
db=10*np.log10(en+1e-10);thr=max(np.percentile(db,10)+8,-55)
sil=db<thr
# intervalli di parlato, separati da pause >=0.4s
iv=[];i=0
while i<N:
    if not sil[i]:
        j=i
        while j<N:
            k=j
            while k<N and sil[k]:k+=1
            if k-j>=8 or k>=N:break
            j=k+1 if k>j else j+1
        iv.append([i,min(j,N)]);i=j+1
    else:i+=1
# unisci fino a max 9s, spezza oltre 14s
ch=[];cur=None
for a,b in iv:
    if cur and (b-cur[0])*0.05<=9:cur[1]=b
    else:
        if cur:ch.append(cur)
        cur=[a,b]
if cur:ch.append(cur)
d='/home/user/work/asr/sherpa-onnx-whisper-tiny/'
r=sherpa_onnx.OfflineRecognizer.from_whisper(encoder=d+'tiny-encoder.int8.onnx',decoder=d+'tiny-decoder.int8.onnx',tokens=d+'tiny-tokens.txt',language='it',task='transcribe',num_threads=2)
res=[];t0=time.time()
for a,b in ch:
    s=x[max(0,a-3)*h:(b+3)*h]
    if len(s)<sr*0.5:continue
    st=r.create_stream();st.accept_waveform(sr,s);r.decode_stream(st)
    res.append({'s':round(a*.05,2),'e':round(b*.05,2),'t':st.result.text.strip()})
    if len(res)%20==0:json.dump(res,open(out,'w'),ensure_ascii=False);print(len(res),len(ch),round(time.time()-t0),flush=True)
json.dump(res,open(out,'w'),ensure_ascii=False);print('FINE',len(res))
