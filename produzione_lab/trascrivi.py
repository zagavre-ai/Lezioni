import sys,json,subprocess,numpy as np,sherpa_onnx
wav,out=sys.argv[1:3]
x=np.frombuffer(subprocess.run(['ffmpeg','-v','error','-i',wav,'-ac','1','-ar','16000','-f','f32le','-'],capture_output=True).stdout,np.float32)
sr=16000;h=int(.1*sr);N=len(x)//h
en=np.array([float((x[i*h:(i+1)*h]**2).mean()) for i in range(N)])
thr=np.percentile(en,25)*1.5
# chunk: <=27 s, taglio nella pausa migliore tra 12 e 27 s
cuts=[0];i=0
while (cuts[-1]+27*10)<N:
    a=cuts[-1]+120;b=cuts[-1]+270
    seg=en[a:b];j=a+int(np.argmin(np.convolve(seg,np.ones(3)/3,'same')));cuts.append(j)
cuts.append(N)
d='/home/user/work/asr/sherpa-onnx-whisper-base/'
r=sherpa_onnx.OfflineRecognizer.from_whisper(encoder=d+'base-encoder.int8.onnx',decoder=d+'base-decoder.int8.onnx',tokens=d+'base-tokens.txt',language='it',task='transcribe',num_threads=4)
res=[]
for k in range(len(cuts)-1):
    s=x[cuts[k]*h:cuts[k+1]*h]
    if len(s)<sr: continue
    st=r.create_stream();st.accept_waveform(sr,s);r.decode_stream(st)
    res.append({'s':round(cuts[k]/10,1),'e':round(cuts[k+1]/10,1),'t':st.result.text.strip()})
    json.dump(res,open(out,'w'),ensure_ascii=False)
