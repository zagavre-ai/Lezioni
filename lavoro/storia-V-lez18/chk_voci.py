# controlla le voci: trascrive (Parakeet) e confronta parola per parola col testo; bordi: ultimi 50 ms < 0,03
import sys,os,re,json,subprocess,numpy as np,difflib
sys.path.insert(0,'/home/user/work18/lib')
import sherpa_onnx
sys.path.insert(0,'/home/user/work18/scambio/strumenti/letteratura_spagnolo')
from numeri_it import converti
P='/tmp/asr/sherpa-onnx-nemo-parakeet-tdt-0.6b-v3-int8/'
rec=sherpa_onnx.OfflineRecognizer.from_transducer(encoder=P+'encoder.int8.onnx',decoder=P+'decoder.int8.onnx',joiner=P+'joiner.int8.onnx',tokens=P+'tokens.txt',model_type='nemo_transducer',num_threads=2)
def norm(s):return re.sub(r"[^a-zà-ÿ0-9' ]",' ',s.lower().replace("’","'")).split()
def trans(wav):
    a=subprocess.run(['ffmpeg','-v','error','-i',wav,'-ac','1','-ar','16000','-f','s16le','-'],capture_output=True,check=True).stdout
    x=np.frombuffer(a,np.int16).astype(np.float32)/32768
    st=rec.create_stream();st.accept_waveform(16000,x);rec.decode_stream(st);return st.result.text,x
if __name__=='__main__':
    VOX=sys.argv[1];names=sys.argv[2:]
    T={x['nome']:x['testo'] for x in json.load(open('/home/user/work18/scambio/storia-V-lez18/testi_voci.json'))}
    for n in names:
        t,x=trans(f'{VOX}/{n}.wav');a=norm(converti(T[n]));b=norm(t)
        ja=''.join(a);jb=''.join(b);ratio=difflib.SequenceMatcher(None,ja,jb).ratio()
        sm=difflib.SequenceMatcher(None,a,b);diff=[(op,' '.join(a[i1:i2]),' '.join(b[j1:j2])) for op,i1,i2,j1,j2 in sm.get_opcodes() if op!='equal']
        edge=float(np.abs(x[-800:]).max()) if len(x)>800 else 1
        print(n,'rapporto %.3f'%ratio,'parole',len(a),'diverse',len(diff),'bordo_fine %.3f'%edge,diff[:6])
