# fix_quiz.py VIDEO OUT finestre.json — sovrappone schede (png o clip) in finestre [a,b] con dissolvenze;
# ricodifica SOLO i GOP che le contengono (finestre vicine nello stesso pezzo), tempi dei fotogrammi identici all'originale.
import json,subprocess,sys,os,shutil
V,OUT,J=sys.argv[1:4]; W=sorted(json.load(open(J)),key=lambda w:w['a']); T='seg_tmp'; shutil.rmtree(T,ignore_errors=True); os.makedirs(T)
def sh(c):
    r=subprocess.run(c,capture_output=True,text=True)
    if r.returncode: print(r.stderr[-2000:]); sys.exit(1)
    return r.stdout
pk=sh(['ffprobe','-v','error','-select_streams','v','-show_entries','packet=pts_time,flags','-of','csv=p=0',V]).split()
kf=sorted(float(x.split(',')[0]) for x in pk if ',K' in x)
dur=float(sh(['ffprobe','-v','error','-show_entries','format=duration','-of','csv=p=0',V]))
# gruppi di finestre che si toccano
G=[]
for w in W:
    k0=max([k for k in kf if k<=w['a']-0.45]); k1=min([k for k in kf if k>=w['b']+0.45]+[dur])
    if G and k0<G[-1]['k1']+0.01: G[-1]['k1']=max(G[-1]['k1'],k1); G[-1]['w'].append(w)
    else: G.append({'k0':k0,'k1':k1,'w':[w]})
cuts=sorted(set(c for g in G for c in (g['k0'],g['k1']) if 0<c<dur))
sh(['ffmpeg','-v','error','-y','-i',V,'-map','0:v','-c','copy','-f','segment','-segment_times',','.join(f'{c-0.005:.6f}' for c in cuts),'-reset_timestamps','1',f'{T}/s%03d.mp4'])
segs=sorted(x for x in os.listdir(T) if x.endswith('.mp4')); st=[0.0]
for x in segs: st.append(st[-1]+float(sh(['ffprobe','-v','error','-show_entries','format=duration','-of','csv=p=0',f'{T}/'+x])))
cnt=lambda x: sh(['ffprobe','-v','error','-count_packets','-select_streams','v','-show_entries','stream=nb_read_packets','-of','csv=p=0',x]).strip()
for g in G:
    i=max(j for j in range(len(segs)) if st[j]<=g['w'][0]['a']-0.3+1e-3); f=f'{T}/s{i:03d}.mp4'
    assert st[i+1]>=g['w'][-1]['b']+0.3-1e-3, ('pezzo troppo corto',g['w'][-1]['pezzo'] if 'pezzo' in g['w'][-1] else '',st[i],st[i+1])
    ins=['-i',f]; flt=[]; cur='0:v'; n=1
    for j,w in enumerate(g['w']):
        a=w['a']-st[i]; b=w['b']-st[i]; fo=w.get('fout',0.4); fi=w.get('fin',0.3)
        pv=f'{f}.{j}.prev.png'; nx=f'{f}.{j}.next.png'
        sh(['ffmpeg','-v','error','-y','-ss',f"{max(0,w['a']-0.4):.3f}",'-i',V,'-frames:v','1',pv])
        sh(['ffmpeg','-v','error','-y','-ss',f"{w['b']+0.4:.3f}",'-i',V,'-frames:v','1',nx])
        if 'png' in w: ins+=['-loop','1','-framerate','30','-i',w['png']]; src=f'[{n}:v]format=rgba,'
        else: ins+=['-i',w['clip']]; src=f'[{n}:v]format=rgba,setpts=PTS-STARTPTS+{a:.3f}/TB,'
        ins+=['-loop','1','-framerate','30','-i',pv,'-loop','1','-framerate','30','-i',nx]
        last=(j==len(g['w'])-1)
        flt.append(f"{src}fade=in:st={a:.3f}:d={fi}:alpha=1,fade=out:st={b-fo:.3f}:d={fo}:alpha=1[o{j}]")
        flt.append(f"[{cur}][{n+1}:v]overlay=0:0:enable='between(t,{a-0.3:.3f},{a+fi:.3f})':shortest=1[p{j}]")
        flt.append(f"[p{j}][{n+2}:v]overlay=0:0:enable='between(t,{b-fo:.3f},{b+0.3:.3f})':shortest=1[q{j}]")
        endopt=':shortest=1' if 'png' in w else ':eof_action=pass'
        flt.append(f"[q{j}][o{j}]overlay=0:0:enable='between(t,{a:.3f},{b:.3f})'{endopt}[r{j}]")
        cur=f'r{j}'; n+=3
    flt.append(f'[{cur}]format=yuv420p[v]')
    sh(['ffmpeg','-v','error','-y',*ins,'-filter_complex',';'.join(flt),'-map','[v]',
        '-c:v','libx264','-preset','veryfast','-crf','19','-g','60','-keyint_min','6','-sc_threshold','40','-bf','3','-profile:v','high','-level','4.0',
        '-pix_fmt','yuv420p','-fps_mode','passthrough','-video_track_timescale','15360',f+'.new.mp4'])
    c0,c1=cnt(f),cnt(f+'.new.mp4')
    if c0!=c1: print('FOTOGRAMMI DIVERSI',f,c0,c1); sys.exit(1)
    os.replace(f+'.new.mp4',f); print('ricodificato',f,f"{st[i]:.2f}-{st[i+1]:.2f}",c0,[w.get('pezzo','') for w in g['w']],flush=True)
open(f'{T}/lista.txt','w').write(''.join(f"file '{s}'\n" for s in segs))
sh(['ffmpeg','-v','error','-y','-f','concat','-safe','0','-i',f'{T}/lista.txt','-i',V,'-map','0:v','-map','1:a','-c','copy','-movflags','+faststart',OUT])
print('fotogrammi prima',cnt(V),'dopo',cnt(OUT),'durata',sh(['ffprobe','-v','error','-show_entries','format=duration','-of','csv=p=0',OUT]).strip())
