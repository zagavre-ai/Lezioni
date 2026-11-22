# controlla le voci Kore arrivate: trascrizione, confronto col testo, bordi (<0,03 negli ultimi 50 ms) -> /tmp/w/vox/NOME.json e rapporto
import sys, os, json, glob, subprocess, re, difflib, numpy as np
sys.path.insert(0,'/home/user/Lezioni/tools'); import trascrivi as T
T.prepara(); import sherpa_onnx
P=f'{T.D}/{T.M}/'
rec=sherpa_onnx.OfflineRecognizer.from_transducer(encoder=P+'encoder.int8.onnx',decoder=P+'decoder.int8.onnx',joiner=P+'joiner.int8.onnx',tokens=P+'tokens.txt',model_type='nemo_transducer',num_threads=4)
VOX='/home/user/Lezioni/scambio/storia-arte-V-lez08/vox'; OUT='/tmp/w/vox'; os.makedirs(OUT,exist_ok=True)
TESTI={v['nome']:v['testo'] for v in json.load(open('/tmp/w/voci/testi_voci.json'))}
def norm(s): return re.sub(r'[^a-zàèéìòùü0-9 ]',' ',s.lower()).split()
rep=[]
for f in sorted(glob.glob(VOX+'/*.wav')):
    n=os.path.basename(f)[:-4]; base=n.split('_R')[0] if re.search(r'_R\d+$',n) else n
    a=subprocess.run(['ffmpeg','-v','error','-i',f,'-vn','-ac','1','-ar','16000','-f','s16le','-'],capture_output=True).stdout
    x=np.frombuffer(a,np.int16).astype(np.float32)/32768
    words=[]; texts=[]
    for i in range(0,len(x),16000*25):
        st=rec.create_stream(); st.accept_waveform(16000,x[i:i+16000*25]); rec.decode_stream(st); r=st.result
        texts.append(r.text.strip())
        # token -> parole con tempo
        cur=''; t0=None
        for t,tok in zip(r.timestamps,r.tokens):
            if tok.startswith(' ') or t0 is None:
                if cur.strip(): words.append((round(i/16000+t0,2),cur.strip()))
                cur=tok; t0=t
            else: cur+=tok
        if cur.strip(): words.append((round(i/16000+t0,2),cur.strip()))
    json.dump(words,open(f'{OUT}/{base}.json','w'))
    asr=' '.join(texts); ref=TESTI.get(base,'')
    sm=difflib.SequenceMatcher(None,norm(ref),norm(asr)); ratio=sm.ratio()
    ini=float(np.abs(x[:800]).max()); fin=float(np.abs(x[-800:]).max())
    diff=[(' '.join(norm(ref)[a:b]),' '.join(norm(asr)[c:d])) for tag,a,b,c,d in sm.get_opcodes() if tag!='equal']
    rep.append((n,round(len(x)/16000,2),round(ratio,3),round(ini,3),round(fin,3),diff[:8]))
    print(n,round(len(x)/16000,1),'s  somiglianza',round(ratio,3),'bordo ini/fin',round(ini,3),round(fin,3),'OK' if fin<0.03 and ini<0.03 else 'BORDO!',flush=True)
json.dump(rep,open(f'{OUT}/rapporto_voci.json','w'),ensure_ascii=False,indent=1)
