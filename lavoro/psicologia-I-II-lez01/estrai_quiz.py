# Excel della docente (domanda | risposta giusta | 5 sbagliate) → quiz_raw.json, con l'argomento a cui appartiene ogni domanda
# uso: python3 estrai_quiz.py lezione.xlsx   (serve units.json già creato da struttura.py)
import openpyxl,json,re,sys,math,collections
src=sys.argv[1] if len(sys.argv)>1 else 'lez1.xlsx'
U=json.load(open('units.json'))
def toks(s): return [w for w in re.findall(r"[a-zàèéìòù0-9]+",s.lower()) if len(w)>3]
df=collections.Counter(w for u in U for w in set(toks(u['txt'])))
idf=lambda w:math.log((len(U)+1)/(df.get(w,0)+1))
def sim(a,b):
    A,B=set(toks(a)),set(toks(b));return sum(idf(w) for w in A&B)/(1+sum(idf(w) for w in A))
ws=openpyxl.load_workbook(src).active;Q=[]
for r in ws.iter_rows(values_only=True):
    r=[(str(x).strip() if x is not None else '') for x in r]
    if not r[0] or r[1].lower().startswith('risposta'): continue
    p,a,w=r[0],r[1],[x for x in r[2:7] if x]
    best=max(range(len(U)),key=lambda i:sim(p+' '+a,U[i]['txt']))
    Q.append({'p':p,'a':a,'w':w,'quiz':U[best]['a']+1,'ref':U[best]['txt'],'ref_a':U[best]['a']+1})
json.dump(Q,open('quiz_raw.json','w'),ensure_ascii=False,indent=1)
print(len(Q),'domande',collections.Counter(q['quiz'] for q in Q))
