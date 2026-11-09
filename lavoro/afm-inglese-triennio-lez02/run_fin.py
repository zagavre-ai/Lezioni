import sys,json,os,subprocess
sys.path.insert(0,'/home/claude/v5')
import dark
dark.JS=dark.JS.replace("${[...'Lezione 1 · ¿De dónde eres?'].map","${[...(sp.kicker||'')].map").replace('style="font-size:150px">RESUMEN</div>','style="font-size:150px">${sp.t1||"RIEPILOGO"}</div>').replace('style="font-size:150px;color:#E3A95C">RIEPILOGO</div>','style="font-size:120px;color:#E3A95C">${sp.t2||""}</div>')
dark.JS=dark.JS.replace("${i+1}</div>","${sp.n0?sp.n0+i:i+1}</div>")
D='/home/claude/lezioni/afm-inglese-triennio-lez02/'
TV=json.load(open(D+'voci/testi_voci.json'))
v=float(subprocess.run(['ffprobe','-v','error','-show_entries','format=duration','-of','csv=p=0',D+'voci/wav/FIN1.wav'],capture_output=True,text=True).stdout)
TOP=['Economic systems','The public sector','Economic indicators','Focus: green economy','Focus: youth unemployment']
SP={'type':'final','kicker':'Inglese','t1':'THE END','t2':'','items':[[t,''] for t in TOP],'n0':1,'sub':' '.join(TV['FIN1']),'dur':round(max(8.0,v+2.0),2)}
dark.render(SP,D+'dk/FIN1',1.0);__import__('shutil').rmtree(D+'dk/FIN1',ignore_errors=True);print('FIN1')
