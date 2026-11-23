import sys;sys.path.insert(0,'/tmp/claude-0/w/build')
import asr,json
for n in range(1,8):
    w=asr.words('/tmp/claude-0/w/out/teacher/T%d.wav'%n);print(n,len(w),flush=True)
