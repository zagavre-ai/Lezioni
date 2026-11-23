import sys,os,json,glob
sys.path.insert(0,'/tmp/claude-0/w/prod')
import asr
d=sys.argv[1]
for f in sorted(glob.glob(d+'/*.wav')):
    o=f[:-4]+'.words.json'
    if not os.path.exists(o):json.dump(asr.words(f),open(o,'w'),ensure_ascii=False)
print('ok')
