# Rende lo «spiegone» (ripasso della Parte 1 all'inizio della Parte 2) a tempo di voce
import json,sys
sys.path.insert(0,'/home/claude/lezioni/psicologia-I-II-lez02/an');import render_an as R
sp=json.load(open('/home/claude/lezioni/psicologia-I-II-lez02/an/RIP.json'))
m=json.load(open('/home/claude/lezioni/psicologia-I-II-lez02/voci/wav/meta_INTRO1.json'))['RIP']
sp['P']=[p+0.8 for p in m['phrases']][:len(sp['caps'])];sp['dur']=round(m['dur']+0.8+2.5,2)
json.dump(sp,open('/home/claude/lezioni/psicologia-I-II-lez02/an/RIP.json','w'),ensure_ascii=False)
R.render(sp,'/home/claude/lezioni/psicologia-I-II-lez02/an/RIP');print('RIP',sp['dur'])
