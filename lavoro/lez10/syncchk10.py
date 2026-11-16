# Controllo di sincronia sul video finale: N righe a caso, cosa si sente nei 7 s dopo che la riga si accende.
# uso: syncchk7.py video.mp4 timeline.json N
import sys,json,random,subprocess,numpy as np,re
sys.path.insert(0,'/home/claude/w10')
import tl10 as TLM, content10 as C7, build10 as B7
v,tlf,N=sys.argv[1],sys.argv[2],int(sys.argv[3])
TL={n:t for n,t,d in json.load(open(tlf))};B=json.load(open('/home/claude/w10/bounds.json'))
B7.X=TLM.audio();TR=json.load(open('/home/claude/w10/tr10_auto.json'));CH=[x['s'] for x in TR]
def at(t):
    c=min(CH,key=lambda s:abs(s-t));g=c if abs(c-t)<1.0 else t
    return TLM.snap(B7.X,TLM.tm(g)-0.1,before=0.6,after=0.3)
import sherpa_onnx
rec=sherpa_onnx.OfflineRecognizer.from_whisper(encoder="/tmp/whisper/whisper-base/base-encoder.int8.onnx",decoder="/tmp/whisper/whisper-base/base-decoder.int8.onnx",tokens="/tmp/whisper/whisper-base/base-tokens.txt",language="",task="transcribe",num_threads=2)
items=[(a['n'],si,ii,x[0],x[1]) for a in C7.ARG for si,s in enumerate(a['slides']) for ii,x in enumerate(s['items'])]
random.seed(7);out=[]
for n,si,ii,txt,t in random.sample(items,N):
    tf=TL[f'D{n}']+(at(t)-B[n])
    x=np.frombuffer(subprocess.run(['ffmpeg','-v','error','-ss','%.2f'%(tf-1),'-t','8','-i',v,'-ac','1','-ar','16000','-f','f32le','-'],capture_output=True).stdout,np.float32)
    st=rec.create_stream();st.accept_waveform(16000,x);rec.decode_stream(st)
    m='%d:%05.2f'%(tf//60,tf%60)
    out.append(f'- {m} · argomento {n}, slide {si+1}, riga {ii+1}: «{txt.replace("**","")[:90]}» · si sente (da 1 s prima): «{st.result.text.strip()[:110]}»')
print('\n'.join(out))
