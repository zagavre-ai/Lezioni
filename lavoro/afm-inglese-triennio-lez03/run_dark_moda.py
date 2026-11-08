import sys,json,os
sys.path.insert(0,'/home/claude/v5')
import dark
OUT='/home/claude/lezioni/afm-inglese-triennio-lez03/dk'
TT=[(['Production and','sectors of production'],'goods · services · sectors · supply chain'),
(['Economies','of scale'],'unit cost · internal · external · diseconomies'),
(['Quality control and','smart manufacturing'],'QC · Industry 4.0 · AI · digital twins'),
(['Relocation of','business operations'],'offshoring · outsourcing · reshoring'),
(['Focus: the','circular economy'],'reuse · repair · recycle')]
import collections
NQ=[5]*len(TT)  # quiz di fine argomento scritti da noi: 5 domande ciascuno
SP={}
for i,(l,e) in enumerate(TT):
    SP['T%d'%(i+1)]={'type':'title','num':str(i+1).zfill(2),'total':len(TT),'lines':l,'ex':e,'fs':128 if max(len(x) for x in l)<17 else (108 if max(len(x) for x in l)<21 else 96),'dur':3.6,'lineY':720 if len(l)==2 else 600}
    if NQ[i]:SP['Q%d'%(i+1)]={'type':'quiz','topic':(lambda tp:tp if len(tp)<=22 else '<span style="font-size:60px">'+tp+'</span>')(' '.join(l).replace(': ',' · ').replace(':','')),'act':'Quiz %d'%(sum(1 for x in NQ[:i+1] if x)),'pts':'%d domande · per continuare almeno l’80%%<div style="font-size:32px;font-weight:600;color:#5BD6F0;margin-top:12px">Answer the 5 questions: you need at least 4 right answers to go on.</div>'%NQ[i],'dur':4.0}
json.dump(SP,open('/home/claude/lezioni/afm-inglese-triennio-lez03/scripts_dark.json','w'),ensure_ascii=False,indent=1)
for k in (sys.argv[1:] or SP):
    if os.path.exists(f'{OUT}/{k}.mp4'):continue
    dark.render(SP[k],f'{OUT}/{k}',1.0);print(k,flush=True)
