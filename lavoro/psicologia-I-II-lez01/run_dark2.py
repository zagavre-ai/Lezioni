import sys,json,os,re
sys.path.insert(0,'/home/claude/v5')
import dark
dark.JS=dark.JS.replace("${[...'Lezione 1 · ¿De dónde eres?'].map","${[...(sp.kicker||'')].map").replace('style="font-size:150px">RESUMEN</div>','style="font-size:150px">${sp.t1||"RIEPILOGO"}</div>').replace('style="font-size:150px;color:#E3A95C">RIEPILOGO</div>','style="font-size:120px;color:#E3A95C">${sp.t2||""}</div>')
dark.JS=dark.JS.replace("${i+1}</div>","${sp.n0?sp.n0+i:i+1}</div>").replace('style="font-size:250px">REPASO</div>','style="font-size:230px">RIPASSO</div>')
S=open('/home/claude/lezioni/psicologia-I-II-lez01/voci/Stringa_voci_Tecnologie_Lez1.txt').read()
F=[f.strip() for f in re.split(r'(?:Taglio\. ){4}Taglio\. ?',S)]
NAMES=['R1','R2','R3','R4','R5','FIN1','IN2','R6','R7','R8','R9','FIN2']
TXT=dict(zip(NAMES,F[:12]))
sys.path.insert(0,'/home/claude/lezioni/psicologia-I-II-lez01/voci')
import estese_P1 as _X
TXT['FIN1']=_X.F['FIN1'][0]
TOP=['Le fibre tessili','Le proprietà delle fibre','Il mercato delle fibre','Le fibre animali e la lana','La fibra di lana','Trattamenti e cura della lana','Le lane speciali','La seta: origine e produzione','La seta: trattamenti e cura']
def vdur(k):
    f=f'/home/claude/lezioni/psicologia-I-II-lez01/voci/wav/{k}.wav'
    if os.path.exists(f):
        import subprocess;return float(subprocess.run(['ffprobe','-v','error','-show_entries','format=duration','-of','csv=p=0',f],capture_output=True,text=True).stdout)
    return None
def caps(text,dur,a0=0.9):
    ss=[s.strip() for s in re.split(r'(?<=[.!?])\s+',text) if s.strip()];tot=sum(len(s) for s in ss);t=a0;out=[];span=dur-a0-.4
    for s in ss: d=span*len(s)/tot;out.append([round(t,2),round(t+d,2),s]);t+=d
    return out
SP={}
for i,k in enumerate(['R1','R2','R3','R4','R5','R6','R7','R8','R9']):
    v=vdur(k) or len(TXT[k].split())/2.4
    SP[k]={'type':'repaso','kicker':'Schema di ripasso','topic':TOP[i],'caps':caps(TXT[k],max(13.0,v+1.8)),'dur':max(13.0,round(v+1.8,2))}
    SP[k]['caps']=caps(TXT[k],v+0.9)
P1=[[TOP[i],''] for i in range(5)];P2=[[TOP[i],''] for i in range(5,9)]
for k,items,n0,t2 in [('FIN1',P1,1,'PARTE 1'),('FIN2',P2,6,'PARTE 2')]:
    v=vdur(k) or len(TXT[k].split())/2.4
    SP[k]={'type':'final','kicker':'Tecnologie dei materiali','t1':'FINE','t2':t2,'items':items,'n0':n0,'sub':TXT[k],'dur':round(max(8.0,v+2.0),2)}
json.dump(SP,open('/home/claude/lezioni/psicologia-I-II-lez01/scripts_dark2.json','w'),ensure_ascii=False,indent=1)
OUT='/home/claude/lezioni/psicologia-I-II-lez01/dk'
for k in (sys.argv[1:] or SP):
    dark.render(SP[k],f'{OUT}/{k}',1.0);__import__('shutil').rmtree(f'{OUT}/{k}',ignore_errors=True);print(k,flush=True)
