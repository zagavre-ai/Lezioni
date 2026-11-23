import sys,json,subprocess,re
sys.path.insert(0,'/home/user/work18/lib')
from timbre import *
out={}
for w in ('1','2'):
    V=f'/home/user/work18/out/Storia_Lez18_Parte{w}_1080p.mp4'
    pr=json.loads(subprocess.run(['ffprobe','-v','error','-count_packets','-select_streams','v:0','-show_entries','stream=nb_read_packets,width,height,r_frame_rate,codec_name:format=duration,size','-of','json',V],capture_output=True,text=True).stdout)
    d=float(pr['format']['duration']);fr=int(pr['streams'][0]['nb_read_packets'])
    a=subprocess.run(['ffmpeg','-v','info','-i',V,'-af','ebur128=peak=true,silencedetect=n=-45dB:d=2.5','-f','null','-'],capture_output=True,text=True).stderr
    I=re.findall(r'I:\s+(-?[\d.]+) LUFS',a)[-1];TP=re.findall(r'Peak:\s+(-?[\d.]+) dBFS',a)[-1]
    sil=re.findall(r'silence_duration: ([\d.]+)',a)
    tl=json.load(open(f'/home/user/work18/out/timeline_Storia_Lez18_Parte{w}.json'))
    pieces=[(n,t,dd) for n,t,dd in tl if re.match(r'^(P\d[abc]_0|IN1)$',n)]
    tb=[round(timbro(rd(V,t+20,40)),1) for n,t,dd in pieces[::max(1,len(pieces)//6)][:6]]
    out[w]=dict(durata_s=round(d,2),durata_min=round(d/60,2),fotogrammi=fr,attesi=round(d*30,1),peso_MB=round(int(pr['format']['size'])/1e6,1),res=f"{pr['streams'][0]['width']}x{pr['streams'][0]['height']}",LUFS=I,picco_dBFS=TP,silenzi_oltre_2_5s=sil,timbro_dB=tb)
json.dump(out,open('/home/user/work18/out/misure.json','w'),indent=1);print(json.dumps(out,indent=1))
