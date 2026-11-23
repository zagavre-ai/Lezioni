# Voci PROVVISORIE (non Kore) per montare e misurare i tempi. Uso: tts_prov.py testi_voci.json outdir
import sys,json,os,wave,numpy as np,sherpa_onnx
M='/tmp/tts/vits-piper-it_IT-paola-medium'
cfg=sherpa_onnx.OfflineTtsConfig(model=sherpa_onnx.OfflineTtsModelConfig(vits=sherpa_onnx.OfflineTtsVitsModelConfig(model=f'{M}/it_IT-paola-medium.onnx',tokens=f'{M}/tokens.txt',data_dir=f'{M}/espeak-ng-data'),num_threads=2))
tts=sherpa_onnx.OfflineTts(cfg)
V=json.load(open(sys.argv[1])); out=sys.argv[2]; os.makedirs(out,exist_ok=True)
for v in V:
    o=f"{out}/{v['nome']}.wav"
    if os.path.exists(o): continue
    a=tts.generate(v['testo'],sid=0,speed=1.0)
    x=np.array(a.samples,dtype=np.float32); x=np.clip(x,-1,1)
    with wave.open(o,'wb') as w: w.setnchannels(1);w.setsampwidth(2);w.setframerate(a.sample_rate);w.writeframes((x*32767).astype('<i2').tobytes())
    print(v['nome'],round(len(x)/a.sample_rate,1),flush=True)
