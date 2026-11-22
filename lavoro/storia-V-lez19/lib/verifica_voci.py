# Controllo di ogni voce Kore: trascrizione, confronto parola per parola con il testo, bordi (ultimi 50 ms < 0,03)
import sys,json,re,difflib,subprocess,os,numpy as np
sys.path.insert(0,'/home/user/Lezioni/tools')
D=sys.argv[1] if len(sys.argv)>1 else '/home/claude/w19/vox'
TV={x['nome']:x['testo'] for x in json.load(open('/home/claude/voci/scambio/storia-V-lez19/testi_voci.json'))}
import sherpa_onnx
A='/tmp/asr/sherpa-onnx-nemo-parakeet-tdt-0.6b-v3-int8'
rec=sherpa_onnx.OfflineRecognizer.from_transducer(encoder=A+'/encoder.int8.onnx',decoder=A+'/decoder.int8.onnx',joiner=A+'/joiner.int8.onnx',tokens=A+'/tokens.txt',num_threads=2,model_type='nemo_transducer')
def norm(s): return re.findall(r"[a-zàèéìòù']+",s.lower())
out={}
names=sys.argv[2:] or sorted(TV)
for n in names:
    f=f'{D}/{n}.wav'
    if not os.path.exists(f): continue
    x=np.frombuffer(subprocess.run(['ffmpeg','-v','error','-i',f,'-ac','1','-ar','16000','-f','f32le','-'],capture_output=True).stdout,np.float32)
    s=rec.create_stream();s.accept_waveform(16000,x);rec.decode_stream(s);hyp=s.result.text
    a,b=norm(TV[n]),norm(hyp);sm=difflib.SequenceMatcher(None,a,b)
    diff=[(a[i1:i2],b[j1:j2]) for tag,i1,i2,j1,j2 in sm.get_opcodes() if tag!='equal']
    y=np.frombuffer(subprocess.run(['ffmpeg','-v','error','-i',f,'-ac','1','-ar','48000','-f','f32le','-'],capture_output=True).stdout,np.float32)
    end=float(np.abs(y[-2400:]).max());ini=float(np.abs(y[:2400]).max())
    out[n]=dict(rapporto=round(sm.ratio(),3),diff=diff,bordo_fine=round(end,4),bordo_inizio=round(ini,4),ok=(sm.ratio()>0.93 and end<0.03))
    print(n,out[n]['rapporto'],'fine',round(end,3),'OK' if out[n]['ok'] else 'DA GUARDARE',diff[:3],flush=True)
json.dump(out,open('/home/claude/w19/esito_voci.json','w'),ensure_ascii=False,indent=1)
