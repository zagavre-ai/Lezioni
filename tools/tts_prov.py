#!/usr/bin/env python3
# voce PROVVISORIA (non Kore) per il montaggio: python3 tts_prov.py testo.txt out.wav
import sys, wave, numpy as np, sherpa_onnx
D='/tmp/tts/vits-piper-it_IT-paola-medium'
cfg=sherpa_onnx.OfflineTtsConfig(model=sherpa_onnx.OfflineTtsModelConfig(vits=sherpa_onnx.OfflineTtsVitsModelConfig(model=f'{D}/it_IT-paola-medium.onnx',tokens=f'{D}/tokens.txt',data_dir=f'{D}/espeak-ng-data'),num_threads=2))
_t=None
def sintetizza(testo,out,speed=1.0):
    global _t
    if _t is None: _t=sherpa_onnx.OfflineTts(cfg)
    a=_t.generate(testo,sid=0,speed=speed)
    s=(np.clip(np.array(a.samples),-1,1)*32767).astype('<i2')
    w=wave.open(out,'wb');w.setnchannels(1);w.setsampwidth(2);w.setframerate(a.sample_rate);w.writeframes(s.tobytes());w.close()
    return len(s)/a.sample_rate
if __name__=='__main__':
    print(sintetizza(open(sys.argv[1]).read(),sys.argv[2]))
