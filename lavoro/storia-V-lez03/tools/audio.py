import numpy as np,subprocess,os
SR=48000
def rd(path,sr=SR):
    raw=subprocess.run(['ffmpeg','-v','error','-i',path,'-f','s16le','-ac','2','-ar',str(sr),'-'],capture_output=True,check=True).stdout
    return np.frombuffer(raw,np.int16).reshape(-1,2).astype(np.float32)
class Mem:
    """audio del prof processato: memmap s16 stereo"""
    def __init__(s,path): s.m=np.memmap(path,dtype=np.int16,mode='r').reshape(-1,2)
    def cut(s,t0,t1): return s.m[int(round(t0*SR)):int(round(t1*SR))].astype(np.float32)
def mix(frames,parts):
    """parts: list of (array float32 (n,2), offset_s, gain)"""
    n=int(round(frames/30*SR));out=np.zeros((n,2),np.float32)
    for a,off,g in parts:
        o=int(round(off*SR))
        if o>=n: continue
        seg=a[:max(0,n-o)] if o>=0 else a[-o:]
        o=max(o,0)
        out[o:o+len(seg)]+=seg*g
    return np.clip(out,-32768,32767).astype(np.int16)
