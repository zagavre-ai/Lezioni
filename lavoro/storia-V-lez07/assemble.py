import sys,os,json,subprocess
sys.path.insert(0,'/home/claude/w/b')
from lib import *
from data import *
import prof
TR=KIT+'/suoni/trans.wav'
def order():
    L=[('sigla',B+'/sc/sigla.mkv',False),('cover1',B+'/sc/cover.mkv',True),('Dintro',B+'/pz4/P0.mkv',True),('dic',B+'/sc/dic.mkv',True)]
    pz={n for n,_,_ in prof.piano()}
    for a in range(1,6):
        L.append((f'T{a}',B+f'/sc/tit{a}.mkv',True))
        for i in range(3):
            L.append((f'Dprof{a}_{i}',B+f'/pz4/P{a}_{i}.mkv',True))
            if i<2: L.append((f'an{a}_{i}',B+f'/sc/an{a}_{i}.mkv',True))
        if a>=3: L.append((f'M{a-2}',B+f'/sc/map{a-2}.mkv',True))
        L.append((f'r{a}',B+f'/sc/pil{a}.mkv',True)); L.append((f'sch{a}',B+f'/sc/sch{a}.mkv',True)); L.append((f'Q{a}',B+f'/sc/quiz{a}.mkv',True))
    L.append(('GL1',B+'/sc/glos.mkv',True))
    for a in range(1,6): L.append((f'RF{a}',B+f'/sc/rip{a}.mkv',True))
    L+= [('VF1',B+'/sc/verif.mkv',True),('FIN1',B+'/sc/fin.mkv',True),('sigla_fin',B+'/sc/sigla_fin.mkv',True),
         ('compiti_intro',B+'/sc/compi.mkv',True),('compiti1',B+'/sc/compi1.mkv',True),('compiti2',B+'/sc/compi2.mkv',True)]
    return L
def frames(f):
    return int(subprocess.run(['ffprobe','-v','error','-count_packets','-select_streams','v:0','-show_entries','stream=nb_read_packets','-of','csv=p=0',f],capture_output=True,text=True).stdout.strip())
def normalizza(name,src,trans):
    out=f'{B}/fin/{name}.mkv'
    n=frames(src); d=n/30
    if os.path.exists(out+'.ok') and open(out+'.ok').read()==f'{n}:{os.path.getmtime(src)}': return out,n
    ins=['-i',src]+(['-i',TR] if trans else [])
    fg="[0:a]aformat=sample_rates=48000:channel_layouts=stereo[a0]"
    if trans: fg+=";[1:a]aformat=sample_rates=48000:channel_layouts=stereo[t];[a0][t]amix=inputs=2:normalize=0:duration=first[a1]"
    else: fg+=";[a0]anull[a1]"
    fg+=f";[a1]apad,atrim=duration={d:.6f}[ao]"
    ff(*ins,'-filter_complex',fg,'-map','0:v','-map','[ao]','-c:v','copy','-c:a','pcm_s16le',out)
    open(out+'.ok','w').write(f'{n}:{os.path.getmtime(src)}'); return out,n
if __name__=='__main__':
    only_ready='--ready' in sys.argv
    L=order(); tl=[];lst=[];t=0.0;missing=[]
    for name,src,trans in L:
        if not os.path.exists(src+'.ok') and name not in ('sigla','sigla_fin') or not os.path.exists(src):
            missing.append(name); continue
        out,n=normalizza(name,src,trans); lst.append(out); tl.append([name,round(t,3),round(n/30,3)]); t+=n/30
    open(B+'/lista.txt','w').write(''.join(f"file '{f}'\n" for f in lst))
    json.dump(tl,open(B+'/timeline_Parte1.json','w'))
    print('pezzi',len(lst),'durata',round(t,1),'mancano',missing)
