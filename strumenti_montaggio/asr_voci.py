# trascrive ogni voce Kore (con tempi parola) -> voci_asr/NOME.json ; salta quelle gia' fatte
import os,sys,json,subprocess
sys.path.insert(0,'/home/user/Lezioni/kit/tools')
os.environ['TELESIO_ASR']='/tmp/asr'
import sherpa_onnx,wave,numpy as np
D='/tmp/asr/sherpa-onnx-nemo-parakeet-tdt-0.6b-v3-int8'
rec=sherpa_onnx.OfflineRecognizer.from_transducer(encoder=f'{D}/encoder.int8.onnx',decoder=f'{D}/decoder.int8.onnx',joiner=f'{D}/joiner.int8.onnx',tokens=f'{D}/tokens.txt',num_threads=2,model_type='nemo_transducer')
src=sys.argv[1];out=sys.argv[2];os.makedirs(out,exist_ok=True)
for f in sorted(os.listdir(src)):
    if not f.endswith('.wav'):continue
    o=f'{out}/{f[:-4]}.json'
    if os.path.exists(o):continue
    subprocess.run(['ffmpeg','-v','error','-y','-i',f'{src}/{f}','-ac','1','-ar','16000','/tmp/v16.wav'])
    w=wave.open('/tmp/v16.wav');a=np.frombuffer(w.readframes(w.getnframes()),dtype=np.int16).astype(np.float32)/32768
    s=rec.create_stream();s.accept_waveform(16000,a);rec.decode_stream(s);r=s.result
    json.dump({'text':r.text,'tokens':list(r.tokens),'ts':list(r.timestamps),'dur':len(a)/16000},open(o,'w'),ensure_ascii=False)
    print(f,r.text[:70],flush=True)
