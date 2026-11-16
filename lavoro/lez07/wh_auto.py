# Whisper base, lingua riconosciuta pezzo per pezzo, sugli stessi pezzi di un'altra trascrizione. uso: wh_auto.py audio.wav pezzi.json out.json
import sys,json,subprocess,numpy as np,sherpa_onnx
a,pz,out=sys.argv[1:4]
rec=sherpa_onnx.OfflineRecognizer.from_whisper(encoder="/tmp/whisper/whisper-base/base-encoder.int8.onnx",decoder="/tmp/whisper/whisper-base/base-decoder.int8.onnx",tokens="/tmp/whisper/whisper-base/base-tokens.txt",language="",task="transcribe",num_threads=1)
x=np.frombuffer(subprocess.run(['ffmpeg','-v','error','-i',a,'-ac','1','-ar','16000','-f','f32le','-'],capture_output=True).stdout,np.float32)
R=[]
for c in json.load(open(pz)):
    s0=int(c['s']*16000);e0=int(c['e']*16000)
    st=rec.create_stream();st.accept_waveform(16000,x[s0:e0]);rec.decode_stream(st)
    R.append({'s':c['s'],'e':c['e'],'lang':getattr(st.result,'lang',''),'t':st.result.text.strip()})
json.dump(R,open(out,'w'),ensure_ascii=False);print(len(R))
