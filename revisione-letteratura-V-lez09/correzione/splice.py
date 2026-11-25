import subprocess,sys,json,os
V,OUTV,AUD,WD=sys.argv[1:5]; spec=json.load(open(sys.argv[5]))   # spec: lista finestre
FPS=30
def sh(c): subprocess.run(c,check=True)
# keyframe
pk=subprocess.run(['ffprobe','-v','error','-select_streams','v','-skip_frame','nokey','-show_entries','frame=pts_time','-of','csv=p=0',V],capture_output=True,text=True).stdout.split()
K=sorted(float(x.strip(',')) for x in pk)
tot=float(subprocess.run(['ffprobe','-v','error','-show_entries','format=duration','-of','csv=p=0',V],capture_output=True,text=True).stdout)
import bisect
wins=[]
for w in spec:
    a,b=w['a'],w['b']
    ka=K[bisect.bisect_right(K,a-1e-3)-1]
    j=bisect.bisect_left(K,b-1e-3);kb=K[j] if j<len(K) else tot
    wins.append([ka,kb,[w]])
# unisci sovrapposti
wins.sort();m=[]
for x in wins:
    if m and x[0]<m[-1][1]+1e-3: m[-1][1]=max(m[-1][1],x[1]);m[-1][2]+=x[2]
    else: m.append(x)
os.makedirs(WD,exist_ok=True)
lst=[];cur=0.0
for i,(ka,kb,ws) in enumerate(m):
    if ka>cur+1e-6: lst.append(('copy',cur,ka))
    ins=['-ss','%.4f'%ka,'-t','%.4f'%(kb-ka),'-i',V];fc=[];n=1;last='[0:v]'
    for w in ws:
        s=w['a']-ka;e=w['b']-ka
        if w['tipo']=='video':
            ins+=['-i',w['src']];fc.append('[%d:v]setpts=PTS-STARTPTS+%.4f/TB[o%d]'%(n,s,n))
            fc.append('%s[o%d]overlay=0:0:eof_action=pass:enable=\'between(t,%.4f,%.4f)\'[v%d]'%(last,n,s,e-1e-4,n))
        else:
            ins+=['-loop','1','-framerate','30','-i',w['src']]
            fc.append('%s[%d:v]overlay=%d:%d:enable=\'between(t,%.4f,%.4f)\'[v%d]'%(last,n,w['x'],w['y'],s,e-1e-4,n))
        last='[v%d]'%n;n+=1
    p='%s/new%d.mp4'%(WD,i)
    if not os.path.exists(p): sh(['ffmpeg','-v','error','-y']+ins+['-filter_complex',';'.join(fc),'-map',last,'-t','%.4f'%(kb-ka),'-r','30','-c:v','libx264','-preset','veryfast','-crf','19','-profile:v','high','-level','4.0','-pix_fmt','yuv420p','-an',p])
    lst.append(('new',p,kb-ka));cur=kb
if cur<tot-1e-3: lst.append(('copy',cur,None))
parts=[]
for i,x in enumerate(lst):
    if x[0]=='copy':
        p='%s/cp%d.mp4'%(WD,i);a_=x[1];b_=x[2] if x[2] else tot
        n=int(round((b_-a_)*FPS))
        sh(['ffmpeg','-v','error','-y','-ss','%.5f'%a_,'-i',V,'-map','0:v','-frames:v',str(n),'-c','copy','-an',p]);parts.append(p)
    else:
        p=x[1];q=p.replace('new','nx');n=int(round(x[2]*FPS))
        sh(['ffmpeg','-v','error','-y','-i',p,'-frames:v',str(n),'-c','copy',q]);parts.append(q)
open(WD+'/c.txt','w').write(''.join("file '%s'\n"%os.path.abspath(p) for p in parts))
sh(['ffmpeg','-v','error','-y','-f','concat','-safe','0','-i',WD+'/c.txt','-i',AUD,'-map','0:v','-map','1:a','-c','copy','-movflags','+faststart',OUTV])
print('fatto',OUTV)
