# Prepara la cache di parole di tools/sub_finale.py dalla trascrizione già fatta (stesso audio della docente),
# riportata sui tempi del video finale (pezzi D* della timeline), con i termini corretti dal PDF.
# uso: python3 sub_cache.py timeline.json uscita.vtt   (poi: python3 tools/sub_finale.py video timeline uscita.vtt)
import json,sys,re
D='/home/claude/lezioni/afm-inglese-triennio-lez02/'
TL=json.load(open(sys.argv[1]));OUT=sys.argv[2]
B=json.load(open(D+'B.json'))
src={'D0':(0.0,B['a1'])}
for k in range(1,6): src[f'D{k}']=(B[f'a{k}'],B[f'a{k+1}'] if k<5 else B['end'])
FIX={'GMP':'GNP','NET':'NEET','mitta':'mista','siglet':'sigle','remunicipalization':'remunicipalisation','pre-market':'free-market','desides':'decides','bans':'banks'}
def fix(w):
    m=re.match(r"^(\W*)([\w'-]+?)(\W*)$",w)
    if m and m.group(2) in FIX: return m.group(1)+FIX[m.group(2)]+m.group(3)
    return w
W=[]
for l in open(D+'pk.jsonl'): W+=json.loads(l)['w']
C=[]
for n,t,l in TL:
    if n not in src or l<=1.0: continue
    a,b=src[n]
    for tt,w in W:
        if a<=tt<b:
            ft=t+(tt-a)
            if t<=ft<t+l: C.append([round(ft,3),fix(w),t,t+l])
json.dump(C,open(OUT+'.words.json','w'),ensure_ascii=False)
print('parole',len(C),'segmenti',len({c[2] for c in C}))
