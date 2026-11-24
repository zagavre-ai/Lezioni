#!/usr/bin/env python3
# Verifica sincronismo: (1) per ogni clip, durata video (fotogrammi/30) = durata audio; (2) per 6 campioni del docente, scarto fra l'audio finale e l'originale (correlazione degli inviluppi).
import sys,os,json,subprocess,re,pickle,numpy as np
sys.path.insert(0,'/home/claude/w/code')
W='/home/claude/w'
def sh(c): return subprocess.run(c,capture_output=True,text=True)
def adur(f):
    r=sh(['ffmpeg','-v','info','-i',f,'-map','0:a','-f','null','-']).stderr
    t=re.findall(r'time=(\d+):(\d+):([\d.]+)',r)[-1];return int(t[0])*3600+int(t[1])*60+float(t[2])
def vfr(f):
    return int(sh(['ffprobe','-v','error','-count_frames','-select_streams','v:0','-show_entries','stream=nb_read_frames','-of','csv=p=0',f]).stdout.strip())
def clips(part):
    d=pickle.load(open(f'{W}/ctx{part}.pkl','rb'));res=[];worst=0
    for c in d['clips']:
        v=vfr(c['path'])/30;a=adur(c['path']);res.append((os.path.basename(c['path']),round(v,3),round(a,3),round(a-v,3)));worst=max(worst,abs(a-v))
    return res,worst
def env(x,sr,hop=0.01):
    n=int(sr*hop);m=len(x)//n;return np.sqrt((x[:m*n].reshape(m,n)**2).mean(1))
def rd(f,ss,d,sr=8000):
    return np.frombuffer(sh_b(['ffmpeg','-v','error','-ss',str(ss),'-t',str(d),'-i',f,'-vn','-ac','1','-ar',str(sr),'-f','s16le','-']),np.int16).astype(float)
def sh_b(c): return subprocess.run(c,capture_output=True).stdout
def lag(final,t_final,orig,t_orig,d=20):
    a=env(rd(final,t_final,d),8000);b=env(rd(orig,t_orig,d),8000)
    n=min(len(a),len(b));a=a[:n]-a[:n].mean();b=b[:n]-b[:n].mean()
    c=np.correlate(a,b,'full');k=int(np.argmax(c))-(n-1);return k*0.01
if __name__=='__main__':
    for part in (1,2):
        r,w=clips(part);print('Parte',part,'scarto massimo audio-video per clip: %.3f s'%w)
        for x in r:
            if abs(x[3])>0.02:print('  ',x)
