import sys,subprocess,json,re,numpy as np,os
V=sys.argv[1]
def sh(c): return subprocess.run(c,capture_output=True,text=True)
j=json.loads(sh(['ffprobe','-v','error','-count_packets','-select_streams','v:0','-show_entries','stream=width,height,r_frame_rate,nb_read_packets,codec_name:format=duration,size','-of','json',V]).stdout)
d=float(j['format']['duration']); n=int(j['streams'][0]['nb_read_packets'])
a=json.loads(sh(['ffprobe','-v','error','-select_streams','a:0','-show_entries','stream=codec_name,sample_rate,channels,bit_rate','-of','json',V]).stdout)['streams'][0]
e=sh(['ffmpeg','-hide_banner','-nostats','-i',V,'-af','ebur128=peak=true','-f','null','-']).stderr
I=re.findall(r'I:\s+(-?[\d.]+) LUFS',e)[-1]; P=re.findall(r'Peak:\s+(-?[\d.]+) dBFS',e)[-1]
print(f"durata {d:.2f} s ({int(d//60)}:{d%60:04.1f}) | fotogrammi {n} (durata x 30 = {d*30:.1f}) | {j['streams'][0]['width']}x{j['streams'][0]['height']} {j['streams'][0]['r_frame_rate']} {j['streams'][0]['codec_name']} | audio {a['codec_name']} {a['sample_rate']} Hz {a['channels']} ch {int(a['bit_rate'])//1000} kbps | peso {int(j['format']['size'])/1e6:.1f} MB | LUFS {I} | picco {P} dBFS")
