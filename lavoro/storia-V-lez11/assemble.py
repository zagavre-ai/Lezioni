import sys,os,json,subprocess
sys.path.insert(0,'/home/user/work/build')
from kit2 import *
CL=B+'/clips/'
KIT='/home/user/Lezioni/kit/sigle/'
def kitclip(name,src):
    out=CL+name+'.mkv'
    if os.path.exists(out+'.ok'): return
    d=float(subprocess.run(['ffprobe','-v','error','-show_entries','format=duration','-of','csv=p=0',src],capture_output=True,text=True).stdout)
    n=nfr(d)
    subprocess.run(['ffmpeg','-y','-v','error','-i',src,'-vf','scale=1920:1080,fps=30,format=yuv420p','-frames:v',str(n),'-an','-c:v','libx264','-preset','veryfast','-crf','16',out],check=True)
    subprocess.run(['ffmpeg','-y','-v','error','-i',src,'-t',f'{n/30:.4f}','-ac','2','-ar','48000',CL+name+'.wav'],check=True)
    open(out+'.ok','w').write('1')
def cardclip(name,card,jing=None,voice=None,vt=1.0,jt=0.0,jg=0.0,extra=None,maxd=None):
    out=CL+name+'.mkv'
    if os.path.exists(out+'.ok'): return
    src=f'{B}/cards/{card}.mp4'
    if not os.path.exists(f'{B}/cards/{card}.ok'): return
    d=float(subprocess.run(['ffprobe','-v','error','-show_entries','format=duration','-of','csv=p=0',src],capture_output=True,text=True).stdout)
    n=nfr(min(d,maxd) if maxd else d)
    subprocess.run(['ffmpeg','-y','-v','error','-i',src,'-vf','fps=30,format=yuv420p','-frames:v',str(n),'-c:v','libx264','-preset','veryfast','-crf','16',out],check=True)
    m=Mix(n/30)
    if jing: m.jingle(jt,jing,jg)
    if voice: m.voice(vt,voice)
    m.save(CL+name+'.wav');open(out+'.ok','w').write('1')
def staticclip(name,png,d,voice=None,vt=0.4):
    out=CL+name+'.mkv'
    if os.path.exists(out+'.ok'): return
    n=nfr(d)
    subprocess.run(['ffmpeg','-y','-v','error','-loop','1','-framerate','30','-i',png,'-frames:v',str(n),'-vf','format=yuv420p','-c:v','libx264','-preset','veryfast','-crf','16',out],check=True)
    m=Mix(n/30)
    if voice: m.voice(vt,voice)
    m.save(CL+name+'.wav');open(out+'.ok','w').write('1')
def mapclip(name,mp,voice):
    out=CL+name+'.mkv'
    if os.path.exists(out+'.ok'): return
    src=f'{B}/mp/{mp}.mp4';d=float(subprocess.run(['ffprobe','-v','error','-show_entries','format=duration','-of','csv=p=0',src],capture_output=True,text=True).stdout);n=nfr(d)
    subprocess.run(['ffmpeg','-y','-v','error','-i',src,'-vf','fps=30,format=yuv420p','-frames:v',str(n),'-c:v','libx264','-preset','veryfast','-crf','16',out],check=True)
    m=Mix(n/30);m.voice(1.0,voice)
    import json as _j
    ev=_j.load(open(f'{B}/mp/{mp}.json'))['end_voice'];m.jingle(ev+0.5,'titolo',-4.0)
    m.save(CL+name+'.wav');open(out+'.ok','w').write('1')
def clen(name): return float(subprocess.run(['ffprobe','-v','error','-show_entries','format=duration','-of','csv=p=0',CL+name+'.mkv'],capture_output=True,text=True).stdout)
def order():
    L=[]
    L.append(('SIGLA','S'))
    L.append(('COVER_A','C'));L.append(('D0','D'))
    sub={1:['D1'],2:['D2'],3:['D3'],4:['D4'],5:['D5'],6:['D6a','D6b','AN_T6','D6c']}
    for t in range(1,7):
        L.append((f'TIT{t}','T%d'%t))
        for s in sub[t]: L.append((s,'D' if s.startswith('D') else 'A%d'%t))
        if t!=6: L.append((f'AN_T{t}','A%d'%t))
        if t==1: L.append(('MAP1','M1'))
        if t==3: L.append(('MAP23','M3'))
        if t==4: L.append(('MAP4','M4'))
        L.append((f'PIL{t}','P%d'%t));L.append((f'SCH_T{t}','R%d'%t));L.append((f'QZ{t}','Q%d'%t))
    L+=[('GLOSS','GL'),('FINALE','RF'),('FINE','FI'),('VERIFICA','VF'),('SIGLA_FIN','SF'),('COMP_INTRO','CI'),('COMPITI_SL','CS')]
    return L
def assemble(L,out_v,out_a,tl_out,trans_gain=0.0):
    names=[n for n,_ in L];dur=[clen(n) for n in names]
    D=[];
    for i in range(1,len(names)):
        D.append(0.8 if names[i]=='COVER_A' else 0.4)
    starts=[0.0]
    for i in range(1,len(names)): starts.append(starts[-1]+dur[i-1]-D[i-1])
    total=starts[-1]+dur[-1]
    # video
    inp=[];fc=[];prev='[0:v]'
    for i,n in enumerate(names): inp+=['-i',CL+n+'.mkv']
    for i in range(len(names)): fc.append(f'[{i}:v]fps=30,settb=1/30,setpts=PTS-STARTPTS,format=yuv420p[s{i}]')
    prev='[s0]'
    for i in range(1,len(names)):
        off=starts[i]
        lab=f'[v{i}]' if i<len(names)-1 else '[vout]'
        fc.append(f'{prev}[s{i}]xfade=transition=fade:duration={D[i-1]}:offset={off:.4f}{lab}');prev=lab
    open(B+'/fc.txt','w').write(';\n'.join(fc))
    # audio
    M=Mix(total+1.0)
    tr=rdwav(JING('trans'),2)
    for i,n in enumerate(names):
        a=rdwav(CL+n+'.wav',2).astype(np.float32).copy()
        if i>0:
            f=int(D[i-1]*SR);a[:f]*=np.linspace(0,1,f,dtype=np.float32)[:,None]
        if i<len(names)-1:
            f=int(D[i]*SR);a[-f:]*=np.linspace(1,0,f,dtype=np.float32)[:,None]
        M.add(starts[i],a,0,0.0)
        if i>0: M.add(starts[i],tr,trans_gain,0.0)
    M.a=M.a[:int(total*SR)]
    M.save(out_a)
    tl=[[n,round(starts[i],3),round(dur[i],3)] for i,(n,_) in enumerate(L)]
    # i nomi del timeline: D*, T*, Q*, ecc. per i controlli
    json.dump({'tl':tl,'total':total,'D':D},open(tl_out,'w'))
    return names,total
def encode(names,out_v,crf=19):
    inp=[]
    for n in names: inp+=['-i',CL+n+'.mkv']
    cmd=['ffmpeg','-y','-v','error']+inp+['-filter_complex_script',B+'/fc.txt','-map','[vout]','-c:v','libx264','-preset','veryfast','-crf',str(crf),'-pix_fmt','yuv420p','-r','30',out_v]
    subprocess.run(cmd,check=True)
