import sys,json,os
sys.path.insert(0,'/home/claude/v5')
import dark
OUT='/home/claude/lezioni/afm-inglese-triennio-lez02/dk';os.makedirs(OUT,exist_ok=True)
# istruzioni del quiz scritte a schermo, in inglese con l'italiano sotto
dark.JS=dark.JS.replace("Rispondi · premi <b class=cy>Check</b> · poi <b class=cy>Continua</b>","Answer, press <b class=cy>Check</b>, then <b class=cy>Continue</b><div style=\"font-size:26px;margin-top:8px;color:rgba(243,245,250,.62)\">Rispondi, premi Check, poi Continua</div>")
dark.JS=dark.JS.replace("${[...('Argomento '+sp.num+' / '+sp.total)]","${[...('Topic '+sp.num+' / '+sp.total)]")
TT=[(['Economic','systems'],'free market · command · mixed'),
(['The public','sector'],'privatisation · pros and cons'),
(['Economic','indicators'],'GDP · inflation · unemployment'),
(['Focus:','green economy'],'natural capital · sustainability'),
(['Focus: youth','unemployment'],'NEET rate · gender gap')]
SP={}
for i,(l,e) in enumerate(TT):
    SP['T%d'%(i+1)]={'type':'title','num':str(i+1).zfill(2),'total':len(TT),'lines':l,'ex':e,'fs':128 if max(len(x) for x in l)<17 else 108,'dur':3.6,'lineY':720 if len(l)==2 else 600}
    SP['Q%d'%(i+1)]={'type':'quiz','topic':' '.join(l).replace(':',' ·').replace('  ',' '),'act':'Quiz %d'%(i+1),'pts':'5 questions · 5 domande · per continuare almeno l’80%','dur':4.0}
json.dump(SP,open('/home/claude/lezioni/afm-inglese-triennio-lez02/scripts_dark.json','w'),ensure_ascii=False,indent=1)
for k in (sys.argv[1:] or SP):
    if os.path.exists(f'{OUT}/{k}.mp4'):continue
    dark.render(SP[k],f'{OUT}/{k}',1.0);print(k,flush=True)
