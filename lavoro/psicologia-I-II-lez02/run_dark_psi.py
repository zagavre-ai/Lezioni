# Schede grafiche (Psicologia): titoli T1..T10, quiz Q1..Q10, ripassi R1..R2, fine FIN1
import sys,json,os,re,subprocess
sys.path.insert(0,'/home/claude/v5')
import dark
dark.JS=dark.JS.replace("${[...'Lezione 1 · ¿De dónde eres?'].map","${[...(sp.kicker||'')].map").replace('style="font-size:150px">RESUMEN</div>','style="font-size:150px">${sp.t1||"RIEPILOGO"}</div>').replace('style="font-size:150px;color:#E3A95C">RIEPILOGO</div>','style="font-size:120px;color:#E3A95C">${sp.t2||""}</div>')
dark.JS=dark.JS.replace("${i+1}</div>","${sp.n0?sp.n0+i:i+1}</div>").replace('style="font-size:250px">REPASO</div>','style="font-size:230px">RIPASSO</div>')
D='/home/claude/lezioni/psicologia-I-II-lez02/';OUT=D+'dk'
os.makedirs(OUT,exist_ok=True)
TT=[(["Che cos'è",'la mente'],'psicologia · attività mentali · mente e corpo'),
(['Le origini:','i filosofi'],'Platone · Aristotele · Cartesio'),
(['Il cervello e','i processi mentali'],'substrato biologico · Phineas Gage'),
(['Dalla fisiologia','alla psicologia scientifica'],'Fechner · Donders · tempi di reazione'),
(['Wilhelm Wundt','e lo strutturalismo'],'laboratorio di Lipsia · Titchener'),
(['Funzionalismo','e Gestalt'],'James · corrente del pensiero · Wertheimer'),
(['Comportamentismo','e cognitivismo'],'Watson · stimolo e risposta · mente e computer'),
(['Jean Piaget e lo','sviluppo della mente'],'epistemologia genetica · quattro stadi'),
(['La psicologia','oggi'],'aree di ricerca · ambiti applicativi'),
(["La psicologia","dell'emergenza"],'situazioni straordinarie · prevenzione')]
QT=["Che cos'è la mente",'Le origini: i filosofi','Il cervello e i processi mentali','Dalla fisiologia alla psicologia scientifica','Wilhelm Wundt e lo strutturalismo','Funzionalismo e Gestalt','Comportamentismo e cognitivismo','Jean Piaget e lo sviluppo della mente','La psicologia oggi',"La psicologia dell'emergenza"]
TXT=json.load(open(D+'voci/testi_voci.json'))
def vdur(k):
    f=D+f'voci/wav/{k}.wav'
    if os.path.exists(f):return float(subprocess.run(['ffprobe','-v','error','-show_entries','format=duration','-of','csv=p=0',f],capture_output=True,text=True).stdout)
REP=[('Fìnias Ghèig','Phineas Gage'),('Fèkner','Fechner'),('Dònders','Donders'),('Vilhelm Vunt','Wilhelm Wundt'),('Vunt','Wundt'),('Ghestàlt','Gestalt'),('Piagè','Piaget'),('Gùstav','Gustav'),('Èdward Tìcena','Edward Titchener'),('Uìlliam Gèims','William James'),('Vertàimer','Wertheimer'),('Gion Uòtson','John Watson'),('Còvid diciannove','Covid-19'),('milleseicentoquarantuno','1641'),('milleottocentoquarantotto','1848')]
def cl(s):
    for a,b in REP:s=s.replace(a,b)
    return s
def caps(text,dur,a0=0.9):
    text=cl(text)
    ss=[s.strip() for s in re.split(r'(?<=[.!?])\s+',text) if s.strip()];tot=sum(len(s) for s in ss);t=a0;out=[];span=dur-a0-.4
    for s in ss: d=span*len(s)/tot;out.append([round(t,2),round(t+d,2),s]);t+=d
    return out
SP={}
for i,(l,e) in enumerate(TT):
    mx=max(len(x) for x in l)
    SP['T%d'%(i+1)]={'type':'title','num':str(i+1).zfill(2),'total':10,'lines':l,'ex':e,'fs':128 if mx<17 else (108 if mx<21 else 92),'dur':3.6,'lineY':720 if len(l)==2 else 600}
    SP['Q%d'%(i+1)]={'type':'quiz','topic':QT[i],'act':'Quiz %d'%(i+1),'pts':'5 domande · per continuare almeno l’80%','dur':4.0}
for k,top in [('R1',QT[0]),('R2',QT[1])]:
    v=vdur(k) or len(' '.join(TXT[k]).split())/2.4;txt=' '.join(TXT[k])
    SP[k]={'type':'repaso','kicker':'Schema di ripasso','topic':top,'caps':caps(txt,v+0.9),'dur':max(6.0,round(v+1.8,2))}
FINIT=[['La mente e le origini',''],['Cervello e fisiologia',''],['Wundt, funzionalismo e Gestalt',''],['Comportamentismo, cognitivismo e Piaget',''],["La psicologia oggi e dell'emergenza",'']]
v=vdur('FIN1') or 6
SP['FIN1']={'type':'final','kicker':'Psicologia','t1':'FINE','t2':'','items':FINIT,'n0':1,'sub':' '.join(TXT['FIN1']),'dur':round(max(8.0,v+2.0),2)}
json.dump(SP,open(D+'scripts_dark.json','w'),ensure_ascii=False,indent=1)
if __name__=='__main__':
    for k in (sys.argv[1:] or SP):
        if os.path.exists(f'{OUT}/{k}.mp4'):continue
        dark.render(SP[k],f'{OUT}/{k}',1.0);__import__('shutil').rmtree(f'{OUT}/{k}',ignore_errors=True);print(k,flush=True)
