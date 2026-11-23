#!/usr/bin/env python3
# timbro: livello >4 kHz meno livello >100 Hz (dB). Deve stare tra -9 e -20. uso: timbro.py file [ss dur]
import sys,subprocess,re
def lv(f,flt,ss=None,d=None):
    c=['ffmpeg','-hide_banner','-nostats']+(['-ss',str(ss),'-t',str(d)] if ss is not None else [])+['-i',f,'-vn','-af',flt+',volumedetect','-f','null','-']
    r=subprocess.run(c,capture_output=True,text=True).stderr
    m=re.search(r'mean_volume: (-?[\d.]+) dB',r); return float(m.group(1))
def timbro(f,ss=None,d=None):
    a=lv(f,'highpass=f=100:p=2',ss,d); b=lv(f,'highpass=f=4000:p=2',ss,d); return round(b-a,1),a,b
if __name__=='__main__':
    a=sys.argv; print(timbro(a[1],*( (float(a[2]),float(a[3])) if len(a)>3 else (None,None))))
