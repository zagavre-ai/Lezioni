# Controllo voci Kore: trascrive ogni wav (Whisper base, inglese) e confronta con il testo. uso: check_voci.py testi_voci.json cartella_wav
import sys,json,re,subprocess,numpy as np,sherpa_onnx,difflib
T=json.load(open(sys.argv[1]));W=sys.argv[2]
rec=sherpa_onnx.OfflineRecognizer.from_whisper(encoder="/tmp/whisper/whisper-base/base-encoder.int8.onnx",decoder="/tmp/whisper/whisper-base/base-decoder.int8.onnx",tokens="/tmp/whisper/whisper-base/base-tokens.txt",language="en",task="transcribe",num_threads=2)
norm=lambda s:re.findall(r"[a-z0-9']+",s.lower())
for v in T:
    f=f"{W}/{v['nome']}.wav"
    x=np.frombuffer(subprocess.run(['ffmpeg','-v','error','-i',f,'-ac','1','-ar','16000','-f','f32le','-'],capture_output=True).stdout,np.float32)
    d=len(x)/16000;out=[]
    for i in range(0,len(x),16000*28):
        st=rec.create_stream();st.accept_waveform(16000,x[i:i+16000*28]);rec.decode_stream(st);out.append(st.result.text)
    h=' '.join(out);r=difflib.SequenceMatcher(None,norm(v['testo']),norm(h)).ratio()
    flag='OK' if r>=0.8 else 'GUARDA'
    print(f"{flag} {r:.2f} {d:5.1f}s {v['nome']} | {h.strip()[:150]}" if flag!='OK' else f"OK {r:.2f} {d:5.1f}s {v['nome']}")
