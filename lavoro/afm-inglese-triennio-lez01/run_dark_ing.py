# Schede scure Inglese Lez1: titoli argomento (T), Quiz (Q), FINE (FIN1)
import sys,json,os,subprocess
sys.path.insert(0,'/home/claude/v5')
import dark
dark.JS=dark.JS.replace("${[...'Lezione 1 · ¿De dónde eres?'].map","${[...(sp.kicker||'')].map").replace('style="font-size:150px">RESUMEN</div>','style="font-size:150px">${sp.t1||"RIEPILOGO"}</div>').replace('style="font-size:150px;color:#E3A95C">RIEPILOGO</div>','style="font-size:120px;color:#E3A95C">${sp.t2||""}</div>')
dark.JS=dark.JS.replace("${i+1}</div>","${sp.n0?sp.n0+i:i+1}</div>")
dark.JS=dark.JS.replace('Rispondi · premi <b class=cy>Check</b> · poi <b class=cy>Continua</b>','Answer the questions · press <b class=cy>Check</b> · then <b class=cy>Continua</b><div style="font-size:26px;opacity:.75;margin-top:8px">Rispondi alle domande · premi Check · poi Continua</div>')
D='/home/claude/lezioni/afm-inglese-triennio-lez01/';OUT=D+'dk'
TT=[(['Globalisation'],'globalizzazione'),
(['Technological','advancement'],'progresso tecnologico'),
(['Diversity','and inclusion'],'diversità e inclusione'),
(['World instability'],'instabilità mondiale'),
(['Environmental','concerns'],'preoccupazioni ambientali')]
SP={}
for i,(l,e) in enumerate(TT):
    SP['T%d'%(i+1)]={'type':'title','num':str(i+1).zfill(2),'total':len(TT),'lines':l,'ex':e,'fs':128 if max(len(x) for x in l)<17 else 108,'dur':3.6,'lineY':720 if len(l)==2 else 600}
    SP['Q%d'%(i+1)]={'type':'quiz','topic':' '.join(l),'act':'Quiz %d'%(i+1),'pts':'5 questions · 5 domande · per continuare almeno l’80%','dur':4.0}
def vdur(k):
    f=D+f'voci/wav/{k}.wav'
    if os.path.exists(f):return float(subprocess.run(['ffprobe','-v','error','-show_entries','format=duration','-of','csv=p=0',f],capture_output=True,text=True).stdout)
TV=json.load(open(D+'voci/testi_voci.json'))
v=vdur('FIN1') or len(' '.join(TV['FIN1']).split())/2.4
SP['FIN1']={'type':'final','kicker':'Inglese · Global Factors','t1':'THE END','t2':'FINE','items':[[' '.join(l),e] for l,e in TT],'sub':' '.join(TV['FIN1']),'dur':round(max(8.0,v+2.0),2)}
json.dump(SP,open(D+'scripts_dark.json','w'),ensure_ascii=False,indent=1)
for k in (sys.argv[1:] or SP):
    if os.path.exists(f'{OUT}/{k}.mp4'):continue
    dark.render(SP[k],f'{OUT}/{k}',1.0);__import__('shutil').rmtree(f'{OUT}/{k}',ignore_errors=True);print(k,flush=True)
