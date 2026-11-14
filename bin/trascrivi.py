import sys,json
from faster_whisper import WhisperModel
src,out=sys.argv[1],sys.argv[2]
import wave,numpy as np
wf=wave.open(src);aud=np.frombuffer(wf.readframes(wf.getnframes()),np.int16).astype(np.float32)/32768
m=WhisperModel('base',device='cpu',compute_type='int8',cpu_threads=2)
segs,info=m.transcribe(aud,language='it',word_timestamps=True,vad_filter=True,initial_prompt="Lezione di letteratura italiana del prof. Giorgio Mazzotti: Decadentismo, Huysmans, Controcorrente, Des Esseintes, Oscar Wilde, Dorian Gray, Grazia Deledda, Proust, Kafka, Virginia Woolf, Bergson, Freud.")
R=[]
for s in segs:
    R.append({'s':round(s.start,2),'e':round(s.end,2),'t':s.text.strip(),'w':[[round(w.start,2),round(w.end,2),w.word] for w in (s.words or [])]})
json.dump({'durata':info.duration,'seg':R},open(out,'w'),ensure_ascii=False)
