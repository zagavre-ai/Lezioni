import subprocess,json,re,os
W='/tmp/w'
os.makedirs(W+'/vox48',exist_ok=True)
def lufs(path):
    r=subprocess.run(['ffmpeg','-hide_banner','-i',path,'-af','ebur128=peak=true','-f','null','-'],capture_output=True,text=True).stderr
    i=re.findall(r'I:\s+(-?[\d.]+) LUFS',r)[-1];p=re.findall(r'Peak:\s+(-?[\d.]+) dBFS',r)[-1]
    return float(i),float(p)
def prep_voice(name,src=None):
    """voce Kore -> stereo 48k, -16 LUFS (guadagno lineare, limitatore a -1.5 dB), dissolvenza 30 ms in/out"""
    out=f'{W}/vox48/{name}.wav'
    if os.path.exists(out):return out
    src=src or f'{W}/vox/{name}.wav'
    I,P=lufs(src);g=-16-I
    d=float(subprocess.run(['ffprobe','-v','error','-show_entries','format=duration','-of','csv=p=0',src],capture_output=True,text=True).stdout)
    subprocess.run(['ffmpeg','-v','error','-y','-i',src,'-af',f'volume={g:.2f}dB,alimiter=limit=0.84:level=disabled,afade=t=in:d=0.03,afade=t=out:st={d-0.035:.3f}:d=0.035,pan=stereo|c0=c0|c1=c0','-ar','48000',out],check=True)
    return out
def dur(path):
    return float(subprocess.run(['ffprobe','-v','error','-show_entries','format=duration','-of','csv=p=0',path],capture_output=True,text=True).stdout)
