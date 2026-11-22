import os,json,re,subprocess,sys
W='/home/claude/w'
REAL=W+'/scambio/storia-V-lez07/vox'; PROV=W+'/vox_prov'; ASRD=W+'/vox_asr'
os.makedirs(PROV,exist_ok=True); os.makedirs(ASRD,exist_ok=True)
T={x['nome']:x['testo'] for x in json.load(open(W+'/testi_voci.json'))}
def dur(f): return float(subprocess.run(['ffprobe','-v','error','-show_entries','format=duration','-of','csv=p=0',f],capture_output=True,text=True).stdout)
def sentences(text):
    parts=re.split(r'(?<=[.!?:])\s+',text.strip()); return [p for p in parts if p]
def path(name):
    r=f'{REAL}/{name}.wav'
    if os.path.exists(r): return r,False
    p=f'{PROV}/{name}.wav'
    if not os.path.exists(p):
        d=len(T[name])/13.4+0.5
        subprocess.run(['ffmpeg','-v','error','-y','-f','lavfi','-i',f'anullsrc=r=24000:cl=mono','-t',f'{d:.2f}','-c:a','pcm_s16le',p],check=True)
    return p,True
def info(name):
    p,prov=path(name); d=dur(p); S=sentences(T[name]); tot=sum(len(s) for s in S)
    f=f'{ASRD}/{name}.json'; times=None
    if not prov and os.path.exists(f):
        tok=json.load(open(f))   # [[t,token]]
        if tok:
            txt=''.join(t for _,t in tok); L=len(txt); cum=0; times=[]
            for s in S:
                i=min(len(tok)-1,int(cum/tot*L)); 
                # char index -> token index
                c=0;k=0
                for k,(tt,w) in enumerate(tok):
                    c+=len(w)
                    if c>=cum/tot*L: break
                times.append(tok[k][0]); cum+=len(s)
            times[0]=0.0
    if times is None:
        cum=0;times=[]
        for s in S: times.append(d*cum/tot); cum+=len(s)
    out=[]
    for i,s in enumerate(S): out.append((max(0,times[i]-0.05) if i else 0.0,(times[i+1]-0.05 if i+1<len(S) else d),s))
    return dict(name=name,path=p,dur=d,prov=prov,sent=out,text=T[name])
if __name__=='__main__':
    # trascrive tutte le voci vere non ancora trascritte
    todo=[n for n in T if os.path.exists(f'{REAL}/{n}.wav') and not os.path.exists(f'{ASRD}/{n}.json')]
    if todo:
        sys.path.insert(0,'/home/user/Lezioni/tools'); import trascrivi, numpy as np, sherpa_onnx
        trascrivi.prepara(); D=trascrivi.D; M=trascrivi.M; P=f'{D}/{M}/'
        rec=sherpa_onnx.OfflineRecognizer.from_transducer(encoder=P+'encoder.int8.onnx',decoder=P+'decoder.int8.onnx',joiner=P+'joiner.int8.onnx',tokens=P+'tokens.txt',model_type='nemo_transducer',num_threads=2)
        for n in todo:
            a=subprocess.run(['ffmpeg','-v','error','-i',f'{REAL}/{n}.wav','-ac','1','-ar','16000','-f','s16le','-'],capture_output=True).stdout
            x=np.frombuffer(a,np.int16).astype(np.float32)/32768
            st=rec.create_stream(); st.accept_waveform(16000,x); rec.decode_stream(st); r=st.result
            json.dump([[round(t,2),w] for t,w in zip(r.timestamps,r.tokens)],open(f'{ASRD}/{n}.json','w'),ensure_ascii=False)
            json.dump(r.text,open(f'{ASRD}/{n}.txt','w'),ensure_ascii=False)
            print(n,r.text[:60],flush=True)
