import sys,json,os,re
sys.path.insert(0,'/home/claude/v5')
import dark
dark.JS=dark.JS.replace("${[...'Lezione 1 · ¿De dónde eres?'].map","${[...(sp.kicker||'')].map").replace('style="font-size:150px">RESUMEN</div>','style="font-size:150px">${sp.t1||"RIEPILOGO"}</div>').replace('style="font-size:150px;color:#E3A95C">RIEPILOGO</div>','style="font-size:120px;color:#E3A95C">${sp.t2||""}</div>')
dark.JS=dark.JS.replace("${i+1}</div>","${sp.n0?sp.n0+i:i+1}</div>").replace('style="font-size:250px">REPASO</div>','style="font-size:230px">RIPASSO</div>')
TV=json.load(open('/home/claude/lezioni/afm-inglese-triennio-lez03/voci/testi_voci.json'))
TXT={k:' '.join(v) for k,v in TV.items()}
TOP=['Tessuti a treccia e a rete','I non tessuti','I tessuti accoppiati','Il controllo qualità','Peso, stabilità e pilling','La sicurezza nei reparti tessili','Navetta, maglia e laboratorio']
def vdur(k):
    f=f'/home/claude/lezioni/afm-inglese-triennio-lez03/voci/wav/{k}.wav'
    if os.path.exists(f):
        import subprocess;return float(subprocess.run(['ffprobe','-v','error','-show_entries','format=duration','-of','csv=p=0',f],capture_output=True,text=True).stdout)
    return None
def caps(text,dur,a0=0.9):
    ss=[s.strip() for s in re.split(r'(?<=[.!?])\s+',text) if s.strip()];tot=sum(len(s) for s in ss);t=a0;out=[];span=dur-a0-.4
    for s in ss: d=span*len(s)/tot;out.append([round(t,2),round(t+d,2),s]);t+=d
    return out
SP={}
for i in range(len(TOP)):
    k='R%d'%(i+1);v=vdur(k) or len(TXT[k].split())/2.4
    SP[k]={'type':'repaso','kicker':'Schema di ripasso','topic':TOP[i],'caps':caps(TXT[k],v+0.9),'dur':max(13.0,round(v+1.8,2))}
v=vdur('FIN1') or len(TXT['FIN1'].split())/2.4
SP['FIN1']={'type':'final','kicker':'Tecnologie dei materiali','t1':'FINE','t2':'','items':[[t,''] for t in TOP],'n0':1,'sub':TXT['FIN1'],'dur':round(max(8.0,v+2.0),2)}
json.dump(SP,open('/home/claude/lezioni/afm-inglese-triennio-lez03/scripts_dark2.json','w'),ensure_ascii=False,indent=1)
OUT='/home/claude/lezioni/afm-inglese-triennio-lez03/dk'
for k in (sys.argv[1:] or SP):
    dark.render(SP[k],f'{OUT}/{k}',1.0);__import__('shutil').rmtree(f'{OUT}/{k}',ignore_errors=True);print(k,flush=True)
