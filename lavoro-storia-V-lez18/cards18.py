import json,re,subprocess,os,sys
sys.path.insert(0,'/tmp/L18/lib')
from assemble import *
from align import sentence_times
TOPN=[("Un Paese da ricostruire",["Un Paese","da ricostruire"],"mercato nero · reduci · latifondi",128),
("La nascita della Repubblica",["La nascita","della Repubblica"],"De Gasperi · Togliatti · 2 giugno 1946",128),
("La Costituzione",["La Costituzione"],"Nilde Iotti · Lina Merlin · 1948",150),
("Il Centrismo (1948-1953)",["Il Centrismo","(1948-1953)"],"De Gasperi · Piano Marshall · NATO",128),
("Il miracolo economico",["Il miracolo","economico"],"Fiat 500 · boom · Nord e Sud",128),
("Il Centrosinistra (1953-1963)",["Il Centrosinistra","(1953-1963)"],"Fanfani · Moro · ENEL",128)]
def tfs(s):return 84 if len(s)<=24 else max(52,int(84*24/len(s)))
def sp(t):return re.split(r'(?<=[.!?:])\s+',t)
only=sys.argv[1] if len(sys.argv)>1 else 'all'
specs=json.load(open('/tmp/L18/cards_specs.json')) if os.path.exists('/tmp/L18/cards_specs.json') else {}
for i,(n,l,ex,fs) in enumerate(TOPN,1):
    specs[f'T{i}']={"type":"title","num":"%02d"%i,"total":6,"lines":l,"ex":ex,"fs":fs,"lineY":720 if len(l)>1 else 600,"dur":4}
    specs[f'Q{i}']={"type":"quiz","act":f"Quiz {i}","topic":n,"tfs":tfs(n),"pts":"5 domande · per continuare almeno l'80%","dur":5}
    if os.path.exists(f'/tmp/L18/voci/scambio/storia-V-lez18/vox/P{i}.wav'):
        s=sp(TXT[f'P{i}']);t,d=sentence_times(vn(f'P{i}'),s)
        specs[f'P{i}']={"type":"repaso","kicker":"Pillola di storia","big":"RIPASSO","topic":n,"tfs":tfs(n),"caps":[[round(0.9+a,2),round(0.9+b,2),x] for (a,b),x in zip(t,s)],"dur":round(max(7.5,0.9+d+1.3),2)}
s=sp(TXT['INTRO2']);t,d=sentence_times(vn('INTRO2'),s)
specs['RIP']={"type":"repaso","kicker":"Ripasso della prima parte","big":"RIPASSO","topic":"L'Italia repubblicana","tfs":84,"caps":[[round(0.9+a,2),round(0.9+b,2),x] for (a,b),x in zip(t,s)],"dur":round(0.9+d+0.8,2)}
for nm,items,v in (('F1',TOPN[:3],'RF1'),('F2',TOPN[3:],'RF2')):
    specs[nm]={"type":"final","kicker":"Storia V","l1":"RIEPILOGO","l2":"FINALE","items":[[x[0],""] for x in items],"sub":"Ripassiamo insieme ciò che abbiamo imparato.","dur":round(0.9+dur(vn(v))+0.8,2)}
json.dump(specs,open('/tmp/L18/cards_specs.json','w'),ensure_ascii=False,indent=1);print({k:v['dur'] for k,v in specs.items()})
