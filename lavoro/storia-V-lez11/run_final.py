import sys,os,json,subprocess,re
sys.path.insert(0,'/home/user/work/build')
from assemble import *
crf=int(sys.argv[1]) if len(sys.argv)>1 else 19
L=order()
miss=[n for n,_ in L if not os.path.exists(CL+n+'.mkv.ok')]
if miss: print('MANCANO',miss);sys.exit(1)
names,total=assemble(L,None,B+'/audio_raw.wav',B+'/tl_raw.json')
# tl con etichette per i controlli
tl=json.load(open(B+'/tl_raw.json'))
MAP={'SIGLA':'S0','COVER_A':'C0'}
def lab(n):
    m=re.fullmatch(r'TIT(\d)',n)
    if m: return 'T'+m.group(1)
    m=re.fullmatch(r'QZ(\d)',n)
    if m: return 'Q'+m.group(1)
    m=re.fullmatch(r'PIL(\d)',n)
    if m: return 'P'+m.group(1)
    m=re.fullmatch(r'SCH_T(\d)',n)
    if m: return 'R'+m.group(1)
    return {'GLOSS':'GL','FINALE':'RF','FINE':'FI','VERIFICA':'VF','SIGLA_FIN':'SF','COMP_INTRO':'CI','COMPITI_SL':'CS','COMPITI_SL':'CS'}.get(n,n)
tl['tl']=[[lab(n),s,d] for n,s,d in tl['tl']]
json.dump(tl,open(B+'/timeline_Parte1_full.json','w'))
json.dump(tl['tl'],open(B+'/timeline_Parte1.json','w'))
# livello
e=subprocess.run(['ffmpeg','-hide_banner','-nostats','-i',B+'/audio_raw.wav','-af','ebur128=peak=true','-f','null','-'],capture_output=True,text=True).stderr
I=float(re.findall(r'\n\s+I:\s+(-?[\d.]+) LUFS',e)[-1]);g=-16-I;print('LUFS grezzo',I,'gain',g)
subprocess.run(['ffmpeg','-y','-v','error','-i',B+'/audio_raw.wav','-af',f'volume={g:.2f}dB,alimiter=limit=0.89:attack=3:release=60:level=false','-ar','48000',B+'/audio_fin.wav'],check=True)
encode(names,B+'/video_noaudio.mp4',crf)
out=B+'/Storia_Lez11_Parte1_1080p.mp4'
subprocess.run(['ffmpeg','-y','-v','error','-i',B+'/video_noaudio.mp4','-i',B+'/audio_fin.wav','-c:v','copy','-c:a','aac','-b:a','192k','-ar','48000','-ac','2','-movflags','+faststart','-shortest',out],check=True)
print('FATTO',os.path.getsize(out)/1e6,'MB',total)
