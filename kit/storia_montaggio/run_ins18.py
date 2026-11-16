import sys,os,json
sys.path.insert(0,'/home/user/Lezioni/storia_s7')
os.environ['PLAYWRIGHT_BROWSERS_PATH']='/opt/pw-browsers'
from ins import *
from spec18 import *
W='/tmp/w18/w';VOX='/tmp/w18/scambio/storia-V-lez18/vox'
T={o['nome']:o['testo'] for o in json.load(open('/tmp/w18/scambio/storia-V-lez18/testi_voci.json'))}
imgs={'p4':'/tmp/w18/img/crop4.png','p5':'/tmp/w18/img/crop5.png','p8':'/tmp/w18/img/crop8.png','p11':'/tmp/w18/img/crop11.png'}
c=Ctx('l18',W,VOX,T,imgs)
D={}
def reg(n,r):D[n]=round(r[1],3);print(n,D[n],flush=True)
def build_map(n):
    out=f'{W}/pc/{n}.mp4'
    if os.path.exists(out):D[n]=round(dur(out),3);return
    v=c.voice(n);d=dur(v)
    rami=MAPS[n]['rami'];t=[LEAD+x for x in cue_times(T[n],d,[r['cue'] for r in rami])]
    a=mix([(SND+'trans.wav',0,0.5),(v,LEAD,1.0)],f'{W}/au/{n}_mix.wav')
    m={'materia':'Storia','docente':'Prof. Giorgio Mazzotti','titolo':MAPS[n]['titolo'],'rami':[{k:x for k,x in r.items() if k!='cue'} for r in rami]}
    md=f'{W}/map/{n}';os.makedirs(md,exist_ok=True);json.dump(m,open(md+'/mappa.json','w'),ensure_ascii=False)
    run(['python3','/home/user/Lezioni/kit/tools/mappa.py',md+'/mappa.json','--out',md,'--voce',a,'--tempi',','.join(map(str,t))])
    tot=dur(md+'/mappa.mp4')+0.5
    run(['ffmpeg','-y','-v','error','-i',md+'/mappa.mp4','-vf','fps=30,tpad=stop_mode=clone:stop_duration=0.7,format=yuv420p','-af','apad','-c:v','libx264','-preset','veryfast','-crf','14','-c:a','aac','-b:a','192k','-ar','48000','-ac','2','-t',f'{tot:.3f}',out])
    D[n]=round(dur(out),3);print(n,D[n],flush=True)
for n,s in AN.items():reg(n,build_an(c,n,s))
for n in ('MAP1','MAP2','MAP3','MAP4','MAP5','MAP6','MAPF1','MAPF2'):build_map(n)
for i in range(1,7):reg(f'R{i}',build_cap(c,f'R{i}','R',ARGS[i-1][0]))
for n in ('RF1','RF2'):reg(n,build_cap(c,n,'RF',TITOLO,'repaso.wav'))
for n in ('GL1','GL2'):reg(n,build_gl(c,n))
for n in ('FIN1','FIN2'):reg(n,build_fin(c,n))
reg('INTRO1',build_intro(c,'INTRO1',TITOLO,'Prima parte',[a[0] for a in ARGS[:3]]))
reg('INTRO2',build_intro(c,'INTRO2',TITOLO,'Seconda parte',[a[0] for a in ARGS[3:]]))
for i,a in enumerate(ARGS):reg(f'T{i+1}',build_title(c,i+1,6,a[0],a[1]));reg(f'Q{i+1}',build_quiz(c,i+1,a[0]))
json.dump(D,open('/tmp/w18/ins_dur.json','w'),indent=1)
c.S.close();print('FATTO')
