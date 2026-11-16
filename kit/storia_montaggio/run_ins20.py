import sys,os,json
sys.path.insert(0,'/home/user/Lezioni/storia_s7')
os.environ['PLAYWRIGHT_BROWSERS_PATH']='/opt/pw-browsers'
from ins import *
from spec20 import *
W='/tmp/w20/w';VOX='/tmp/w20/scambio/storia-V-lez20/vox'
T={o['nome']:o['testo'] for o in json.load(open('/tmp/w20/scambio/storia-V-lez20/testi_voci.json'))}
imgs={'p7':'/tmp/w20/img/crop7.png'}
c=Ctx('l20',W,VOX,T,imgs)
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
for i in range(1,9):build_map(f'MAP{i}')
build_map('MAPF1')
for i in range(1,9):reg(f'R{i}',build_cap(c,f'R{i}','R',ARGS[i-1][0]))
reg('RF1',build_cap(c,'RF1','RF',TITOLO,'repaso.wav'))
reg('GL1',build_gl(c,'GL1'));reg('FIN1',build_fin(c,'FIN1'))
reg('INTRO1',build_intro(c,'INTRO1',TITOLO,'',[a[0] for a in ARGS]))
for i,a in enumerate(ARGS):reg(f'T{i+1}',build_title(c,i+1,8,a[0],a[1]));reg(f'Q{i+1}',build_quiz(c,i+1,a[0]))
# schede fisse
sig='/home/user/Lezioni/kit/sigle/Sigla_Storia_15s.mp4'
def enc(src,dst,ss=None,t=None):
    cmd=['ffmpeg','-y','-v','error']+(['-ss',str(ss)] if ss is not None else [])+['-i',src]+(['-t',str(t)] if t else [])+['-vf','fps=30,scale=1920:1080,format=yuv420p','-af','aresample=48000,apad','-c:v','libx264','-preset','veryfast','-crf','14','-c:a','aac','-b:a','192k','-ar','48000','-ac','2','-shortest',dst]
    run(cmd)
enc(sig,W+'/pc/SIGLA.mp4');enc(sig,W+'/pc/SFIN.mp4',ss=10,t=5)
reg('VER',build_pausa(c,'VER','Pausa del video · Verifica','Verifica finale',TITOLO,'Test finale della lezione','trans.wav'))
reg('COMP',build_pausa(c,'COMP','Pausa del video · Compiti','Compiti','Ora tocca a te','','trans.wav'))
p=c.png('l20_CINTRO',doc(f'''{logo(True)}<div class="abs kick" style="left:150px;top:380px">Storia · Quinto anno</div><h1 class="abs" style="left:150px;top:440px;font-size:140px">I compiti</h1><div class="abs" style="left:150px;top:640px;font-family:BG;font-weight:800;font-size:54px;color:#5DA3F0">Ora tocca a te</div>''','bg-d'))
reg('CINTRO',c.piece('CINTRO',[(p,3.7)],[(SND+'trans.wav',0,0.7)],3.7))
json.dump(D,open('/tmp/w20/ins_dur.json','w'),indent=1)
c.S.close();print('FATTO')
