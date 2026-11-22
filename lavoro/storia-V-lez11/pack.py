import sys,os,json,re,shutil,subprocess
sys.path.insert(0,'/home/user/work/build')
from L import *
from subs import make_vtt
OUT=B+'/consegna';os.makedirs(OUT,exist_ok=True)
REV=W+'/rev/revisione-storia-V-lez11/'
# quiz
q=json.load(open(REV+'quiz_argomenti.json'))
def fix(s):
    s=s.replace("dell'URSS","dell'Unione Sovietica").replace("nell'URSS","nell'Unione Sovietica").replace("l'URSS","l'Unione Sovietica").replace("L'URSS","L'Unione Sovietica").replace("URSS","Unione Sovietica")
    return s
def walk(o):
    if isinstance(o,str): return fix(o)
    if isinstance(o,list): return [walk(x) for x in o]
    if isinstance(o,dict): return {k:walk(v) for k,v in o.items()}
    return o
q=walk(q)
for t in range(1,7): q[f'Q{t}']['title']=f"Quiz {t} · {TOP[t-1]['t']}"
json.dump(q,open(OUT+'/quiz_argomenti.json','w'),ensure_ascii=False,indent=1)
v=json.load(open(REV+'verifica_finale.json'));v['titolo']="Verifica finale · Storia V · L'URSS di Stalin (1924-1939)"
json.dump(v,open(OUT+'/verifica_finale.json','w'),ensure_ascii=False,indent=1)
shutil.copy(W+'/domande/DOMANDE LEZIONE 11.xlsx',OUT+'/verifica_finale_prof.xlsx')
shutil.copy(REV+'compiti.json',OUT+'/compiti.json')
tl=json.load(open(B+'/tl_raw.json'))
n=make_vtt(tl['tl'],OUT+'/Storia_Lez11_Parte1.vtt');print('cues',n)
shutil.copy(B+'/timeline_Parte1.json',OUT+'/timeline_Parte1.json')
shutil.copy(B+'/Storia_Lez11_dispensa.pdf',OUT+'/Storia_Lez11_dispensa.pdf')
shutil.copy(B+'/Storia_Lez11_mappe.pdf',OUT+'/Storia_Lez11_mappe.pdf')
V=B+'/Storia_Lez11_Parte1_1080p.mp4'
subprocess.run([sys.executable,'/home/user/Lezioni/kit/tools/scheda_da_timeline.py',V,OUT+'/timeline_Parte1.json',OUT+'/quiz_argomenti.json',"Storia V · L'URSS di Stalin (1924-1939)",OUT+'/scheda_pubblicazione_Parte1.json','Storia V'],check=True)
