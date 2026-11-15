# Whisper base (sherpa-onnx): pezzi di 6-14 s tagliati nelle pause; uso: wh.py audio lingua out.json
import sys,json,subprocess,numpy as np,sherpa_onnx
a,lang,out=sys.argv[1:4]
rec=sherpa_onnx.OfflineRecognizer.from_whisper(encoder="/tmp/whisper/whisper-base/base-encoder.int8.onnx",decoder="/tmp/whisper/whisper-base/base-decoder.int8.onnx",tokens="/tmp/whisper/whisper-base/base-tokens.txt",language=lang,task="transcribe",num_threads=3)
x=np.frombuffer(subprocess.run(['ffmpeg','-v','error','-i',a,'-ac','1','-ar','16000','-f','f32le','-'],capture_output=True).stdout,np.float32)
sr=16000;w=int(0.1*sr);h=int(0.05*sr)
en=np.array([float((x[i:i+w]**2).mean()) for i in range(0,len(x)-w,h)])
R=[];i=0;N=len(en)
while i<N:
    a0=i+int(6/0.05);b0=min(N,i+int(14/0.05))
    j=N if a0>=N else (a0+int(np.argmin(en[a0:b0])) if b0-a0>0 else N)
    if N-i<int(15/0.05): j=N
    s0=int(i*h);e0=min(len(x),int(j*h)+w)
    st=rec.create_stream();st.accept_waveform(sr,x[s0:e0]);rec.decode_stream(st)
    R.append({'s':s0/sr,'e':e0/sr,'t':st.result.text.strip()});i=j
json.dump(R,open(out,'w'),ensure_ascii=False);print(len(R))
