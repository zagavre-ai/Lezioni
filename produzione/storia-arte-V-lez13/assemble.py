import sys,os,json,re
sys.path.insert(0,'/tmp/claude-0/w/prod')
import build_lez as B
from eng import *
import pyloudnorm as pyln
from concurrent.futures import ThreadPoolExecutor
B.build();IT=B.ITEMS
for it in IT:
    if it.kind=='clip':it.nf=int(open(f'{W}/mz/{it.name}.mp4.ok').read().split()[0])
N=len(IT);os.makedirs(W+'/fin',exist_ok=True)
start=[];c=0
for i,it in enumerate(IT):start.append(c);c+=it.nf-OV
total=c+OV
ENC=['-c:v','libx264','-preset','ultrafast','-crf','10','-pix_fmt','yuv420p','-r','30','-colorspace','bt709','-color_primaries','bt709','-color_trc','bt709','-an']
def body(i):
    o=f'{W}/fin2/b{i:03d}.mp4'
    sg=open(f'{W}/mz/{IT[i].name}.mp4.ok').read()+f'{i}{N}'
    if os.path.exists(o+'.ok') and open(o+'.ok').read()==sg:return o
    it=IT[i];a=OV if i>0 else 0;b=it.nf-OV if i<N-1 else it.nf
    sh(['ffmpeg','-v','error','-y','-i',f'{W}/mz/{it.name}.mp4','-vf',f'trim=start_frame={a}:end_frame={b},setpts=PTS-STARTPTS']+ENC+[o]);open(o+'.ok','w').write(sg);return o
def diss(i):
    o=f'{W}/fin2/d{i:03d}.mp4'
    sg=open(f'{W}/mz/{IT[i].name}.mp4.ok').read()+open(f'{W}/mz/{IT[i+1].name}.mp4.ok').read()+f'{i}'
    if os.path.exists(o+'.ok') and open(o+'.ok').read()==sg:return o
    A=IT[i];Bn=IT[i+1]
    fc=f"[0:v]trim=start_frame={A.nf-OV},setpts=PTS-STARTPTS[a];[1:v]trim=end_frame={OV},setpts=PTS-STARTPTS[b];[a][b]xfade=transition=fade:duration={OV/FPS}:offset=0,trim=end_frame={OV},setpts=PTS-STARTPTS"
    sh(['ffmpeg','-v','error','-y','-i',f'{W}/mz/{A.name}.mp4','-i',f'{W}/mz/{Bn.name}.mp4','-filter_complex',fc]+ENC+[o]);open(o+'.ok','w').write(sg);return o
jobs=[]
for i in range(N):
    jobs.append(('b',i))
    if i<N-1:jobs.append(('d',i))
def run(j):
    k,i=j;r=body(i) if k=='b' else diss(i);print('ok',k,i,flush=True);return r
if '--video' in sys.argv or '--all' in sys.argv:
    with ThreadPoolExecutor(2) as ex:list(ex.map(run,jobs))
    L=[]
    for i in range(N):
        L.append(f"file '{W}/fin2/b{i:03d}.mp4'")
        if i<N-1:L.append(f"file '{W}/fin2/d{i:03d}.mp4'")
    open(W+'/fin/list.txt','w').write('\n'.join(L))
    sh(['ffmpeg','-v','error','-y','-f','concat','-safe','0','-i',W+'/fin/list.txt','-c','copy',W+'/fin/video_only.mp4'])
    sh(['ffmpeg','-v','error','-y','-i',W+'/fin/video_only.mp4','-c:v','libx264','-preset','veryfast','-crf','19','-pix_fmt','yuv420p','-r','30','-x264-params','keyint=150:min-keyint=30','-colorspace','bt709','-color_primaries','bt709','-color_trc','bt709','-an',W+'/fin/video_final.mp4'])
    print('video',nframes(W+'/fin/video_final.mp4'),'attesi',total)
if '--audio' in sys.argv or '--all' in sys.argv:
    meter=pyln.Meter(SR);Y=np.zeros((total*SR//FPS+SR,2),np.float32);tr=audio_load(K+'suoni/trans.wav')*0.8
    for i,it in enumerate(IT):
        x=audio_load(f'{W}/mz/{it.name}.wav')
        if it.kind=='prof':
            # porta il parlato del prof a -16 LUFS (solo guadagno, timbro intatto)
            l=meter.integrated_loudness(x[int(0.4*SR):-int(0.4*SR)]);g=10**((-16-l)/20);x=x*g
        s=start[i]*SR//FPS;Y[s:s+len(x)]+=x[:len(Y)-s]
        if i>0:
            s2=s-int(0.2*SR);Y[s2:s2+len(tr)]+=tr
    Y=Y[:total*SR//FPS]
    l=meter.integrated_loudness(Y);Y=Y*10**((-16-l)/20);print('loudness prima',l)
    write_wav(W+'/fin/audio.wav',Y)
    sh(['ffmpeg','-v','error','-y','-i',W+'/fin/audio.wav','-af','alimiter=limit=0.75:level=false','-c:a','aac','-b:a','192k','-ar','48000',W+'/fin/audio.m4a'])
if '--mux' in sys.argv or '--all' in sys.argv:
    sh(['ffmpeg','-v','error','-y','-i',W+'/fin/video_final.mp4','-i',W+'/fin/audio.m4a','-c','copy','-movflags','+faststart','-shortest',W+'/fin/Storia_arte_Lez13_Parte1_1080p.mp4'])
    print('mux ok')
# timeline
TL=[];
for i,it in enumerate(IT):TL.append([it.name,round(start[i]/FPS,3),round(it.nf/FPS,3)])
json.dump(TL,open(W+'/fin/timeline_raw.json','w'),indent=0)
json.dump({'start':start,'total':total},open(W+'/fin/starts.json','w'))
