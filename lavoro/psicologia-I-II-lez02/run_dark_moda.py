import sys,json,os
sys.path.insert(0,'/home/claude/v5')
import dark
OUT='/home/claude/lezioni/psicologia-I-II-lez02/dk'
TT=[(['Le fibre tessili'],'naturali · chimiche · in mischia'),
(['Le proprietà','delle fibre'],'morfologiche · chimiche · fisiche'),
(['Il mercato','delle fibre'],'sporcabilità · pulibilità'),
(['Le fibre animali','e la lana'],'razze · tosatura · lavaggio'),
(['La fibra','di lana'],'cheratina · finezza · micron'),
(['Trattamenti e cura','della lana'],'finissaggi · proprietà · cura'),
(['Le lane','speciali'],'vigogna · cashmere · mohair'),
(['La seta:','origine e produzione'],'baco · bozzolo · sgommatura'),
(['La seta:','trattamenti e cura'],'proprietà · cura · seta di ragno')]
NQ=[2,2,5,2,3,2,1,2,1]
SP={}
for i,(l,e) in enumerate(TT):
    SP['T%d'%(i+1)]={'type':'title','num':str(i+1).zfill(2),'total':9,'lines':l,'ex':e,'fs':128 if max(len(x) for x in l)<17 else 108,'dur':3.6,'lineY':720 if len(l)==2 else 600}
    SP['Q%d'%(i+1)]={'type':'quiz','topic':' '.join(l).replace(': ',' · ').replace(':',''),'act':'Quiz %d'%(i+1),'pts':'%d domand%s · per continuare almeno l’80%%'%(NQ[i],'a' if NQ[i]==1 else 'e'),'dur':4.0}
json.dump(SP,open('/home/claude/lezioni/psicologia-I-II-lez02/scripts_dark.json','w'),ensure_ascii=False,indent=1)
for k in (sys.argv[1:] or SP):
    if os.path.exists(f'{OUT}/{k}.mp4'):continue
    dark.render(SP[k],f'{OUT}/{k}',1.0);print(k,flush=True)
