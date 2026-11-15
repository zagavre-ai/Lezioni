import sys,json,os
sys.path.insert(0,'/home/user/w5')
from build5 import *
shot_all()
B=bounds();print('limiti docente (tagliato):',[round(x,1) for x in B],flush=True)
ITT=json.load(open(D+'itemsT.json'))
def states_topic(n):
    a=ARG[n-1];st=[(D+f"sl/A{n}_0_x.png",B[n])]
    for si,s in enumerate(a['slides']):
        for ii in range(len(s['items'])):
            st.append((D+f"sl/A{n}_{si}_{ii}.png",ITT[f'A{n}.S{si}.I{ii}']))
    return st
def states_intro():
    g=[40.0,52.5,65.0,76.0,82.5,91.2,96.8];st=[(D+'sl/A0_0.png',B[0])]
    for i,x in enumerate(g): st.append((D+f'sl/A0_{i+1}.png',TLM.tm(x)))
    return st
def amap(k):
    n=len(VD.M[k][1]);names=[f'E5_AN{k}_{i}' for i in range(n+1)]
    od=D+f'map/{MODE}/o{k}';os.makedirs(od,exist_ok=True)
    vw=D+f'map/{MODE}/v{k}.wav';concat_voice(names,vw);of=offsets(names)
    tempi=','.join('%.2f'%(0.9+of[i+1]-0.1) for i in range(n))
    if not os.path.exists(od+'/mappa.mp4'):
        run(['python3','/home/user/Lezioni/kit/tools/mappa.py',D+f'map/mappa{k}.json','--out',od,'--durata','%.2f'%(0.9+dur(vw)+1.5),'--tempi',tempi,'--solo-video'])
    return od+'/mappa.mp4',vw
seq=[('SIGLA',sigla('S0',D+'as/Sigla_Inglese_15s.mp4'),'G')]
seq.append(('INTRO1',mix_clip('INTRO1',png_video('INTRO1',D+'sl/COVER.png',2.0),None,0,'E5_INTRO1',0.9),'C'))
seq.append(('D0',doc_clip('D0',B[0],B[1],states_intro()),'D'))
for k in range(1,7):
    seq.append((f'T{k}',mix_clip(f'T{k}',png_video(f'T{k}',D+f'sl/T{k}.png',2.6),'titolo',0.45),'T'))
    seq.append((f'D{k}',doc_clip(f'D{k}',B[k],B[k+1],states_topic(k)),'D'))
    mv,vw=amap(k);seq.append((f'AN{k}',mix_clip(f'AN{k}',mv,'trans',0.0,None,0.9,vfile=vw),'A'))
    seq.append((f'Q{k}',mix_clip(f'Q{k}',png_video(f'Q{k}',D+f'sl/Q{k}.png',4.0),'quiz',0.5),'Q'))
mv,vw=amap(7);seq.append(('AN7',mix_clip('AN7',mv,'trans',0.0,None,0.9,vfile=vw),'A'))
vwa=D+f'map/{MODE}/gla.wav';concat_voice(['E5_GL0','E5_GLa'],vwa);lead=dur(voice('E5_GL0'))+0.35
seq.append(('GL1',mix_clip('GL1',seq_video('GL1',[D+f'sl/GL0_{i}.png' for i in range(13)],vwa,lead),'trans',0.0,None,0.9,vfile=vwa),'A'))
seq.append(('GL2',mix_clip('GL2',seq_video('GL2',[D+f'sl/GL1_{i}.png' for i in range(13)],voice('E5_GLb')),None,0,'E5_GLb',0.9),'A'))
seq.append(('RF1',mix_clip('RF1',png_video('RF1',D+'sl/RF.png',3.0),'repaso',0.4,'E5_RF1',0.9),'R'))
seq.append(('FIN1',mix_clip('FIN1',png_video('FIN1',D+'sl/FIN.png',5.0),'finale',0.4,'E5_FIN1',1.0),'F'))
seq.append(('SFIN',sigla('SFIN',D+'as/Sigla_finale_chiusura.mp4'),'G'))
seq.append(('CMPI',mix_clip('CMPI',png_video('CMPI',D+'sl/CMPI.png',3.5),'trans',0.0,'E5_CMP1',0.9),'F'))
seq.append(('CMP1',mix_clip('CMP1',png_video('CMP1',D+'sl/CMP.png',3.7),'finale',0.4),'F'))
if os.environ.get('PIANO'):
    tot=sum(dur(f)-2*LT for n,f,ty in seq);print('durata stimata',round(tot/60,2),'min');sys.exit()
out=D+f'out_{MODE}/lista';os.makedirs(D+f'out_{MODE}',exist_ok=True)
tl,t=join(seq,out)
json.dump(tl,open(D+f'out_{MODE}/timeline.json','w'),indent=0)
print('lista pronta',round(t/60,2),'min',flush=True)
