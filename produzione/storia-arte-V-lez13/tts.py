# voci PROVVISORIE (Piper, italiano): servono solo per le durate; le voci vere (Kore) le fa la master
import sys,json,os,wave
from piper import PiperVoice
D='/tmp/claude-0/w/tts/vits-piper-it_IT-paola-medium/'
V=PiperVoice.load(D+'it_IT-paola-medium.onnx',config_path=D+'it_IT-paola-medium.onnx.json')
def say(txt,out):
    with wave.open(out,'wb') as w: V.synthesize_wav(txt,w)
if __name__=='__main__':
    T=json.load(open(sys.argv[1]));os.makedirs(sys.argv[2],exist_ok=True)
    for t in T:
        o=f"{sys.argv[2]}/{t['nome']}.wav"
        if not os.path.exists(o):say(t['testo'],o)
