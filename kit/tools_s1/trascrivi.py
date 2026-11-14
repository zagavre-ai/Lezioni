#!/usr/bin/env python3
"""Trascrizione locale (Whisper base int8, sherpa-onnx) con tempi per segmento.
Uso: trascrivi.py video.mp4 out.json [lingua=it]
Modello: /tmp/whisper/whisper-base (vedi ramo modelli-whisper-base). Taglia l'audio alle pause (pezzi 4-14 s)."""
import sys,subprocess,json,numpy as np,sherpa_onnx,time
V,OUT=sys.argv[1],sys.argv[2];LANG=sys.argv[3] if len(sys.argv)>3 else 'it'
M='/tmp/whisper/whisper-base/'
a=np.frombuffer(subprocess.run(['ffmpeg','-v','error','-i',V,'-vn','-ac','1','-ar','16000','-f','s16le','-'],capture_output=True).stdout,dtype=np.int16).astype(np.float32)/32768
SR=16000;F=320;n=len(a)//F
e=np.sqrt((a[:n*F].reshape(n,F)**2).mean(1))+1e-9
db=20*np.log10(e);thr=max(np.percentile(db,15)+6,-52)
sil=db<thr
# pause: run di frame silenziosi >= 0.2 s -> punto di taglio al centro
cuts=[];i=0
while i<n:
    if sil[i]:
        j=i
        while j<n and sil[j]:j+=1
        if (j-i)*F/SR>=0.2:cuts.append(((i+j)//2*F/SR,(j-i)*F/SR))
        i=j
    else:i+=1
D=len(a)/SR;bounds=[0.0];MAXL,MINL=14.0,4.0
for c,l in cuts:
    pass
cur=0.0;k=0
while cur<D-0.01:
    cand=[(c,l) for c,l in cuts if cur+MINL<=c<=cur+MAXL]
    if cur+MAXL>=D:nxt=D
    elif cand:nxt=max(cand,key=lambda x:x[1])[0] if max(x[1] for x in cand)>0.35 else cand[-1][0]
    else:nxt=cur+MAXL
    bounds.append(nxt);cur=nxt
rec=sherpa_onnx.OfflineRecognizer.from_whisper(encoder=M+'base-encoder.int8.onnx',decoder=M+'base-decoder.int8.onnx',tokens=M+'base-tokens.txt',language=LANG,task='transcribe',num_threads=4)
out=[];t0=time.time();B=8
segs=list(zip(bounds[:-1],bounds[1:]))
for b in range(0,len(segs),B):
    grp=segs[b:b+B];st=[]
    for s,e_ in grp:
        s_=rec.create_stream();s_.accept_waveform(SR,a[int(s*SR):int(e_*SR)]);st.append(s_)
    rec.decode_streams(st)
    for (s,e_),x in zip(grp,st):
        t=x.result.text.strip()
        if t:out.append({'s':round(s,2),'e':round(e_,2),'t':t})
    print(f'{b}/{len(segs)} {time.time()-t0:.0f}s',flush=True)
json.dump(out,open(OUT,'w'),ensure_ascii=False,indent=0);print('OK',len(out),'segmenti')
