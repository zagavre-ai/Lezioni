import json,subprocess,os
t=json.load(open('/home/claude/w/testi_voci.json'))
V='/home/user/Lezioni/scambio/storia-V-lez21/vox'
n=0
for x in t:
    if os.path.exists(f'{V}/{x["nome"]}.wav'):continue
    out=f'/home/claude/w/vox_prov/{x["nome"]}.wav'
    if os.path.exists(out):continue
    subprocess.run(['espeak-ng','-v','it','-s','150','-w','/tmp/e.wav',x['testo']])
    subprocess.run(['ffmpeg','-v','error','-y','-i','/tmp/e.wav','-ar','48000','-ac','1',out]);n+=1
print('nuove provvisorie',n)
