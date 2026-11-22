import json, sys
sys.path.insert(0,'/home/user/work/build')
from eng import *
SRC='/home/user/work/lez01/Lezione 1 -Le fibre.mp4'
segs=json.load(open('/home/user/work/lez01/trascr.json'))
t0,t1=46.0,106.0
keep,cuts=piano_tagli(segs,t0,t1); print(keep,cuts)
cards=["Le fibre tessili sono sostanze che si presentano in natura o vengono prodotte dall'uomo con un aspetto <b>filamentoso</b> o <b>fusiforme</b>, caratterizzate da morfologia, resistenza, elasticità e flessibilità da permetterne la <b>filatura</b> e la <b>tessitura</b>.",
"Esistono materiali a <b>fibra corta</b> che, pur non essendo adatti alla filatura, possono essere compattati per formare il <b>feltro</b>.",
"La distinzione fondamentale tra questi materiali avviene in base alla loro <b>origine</b>."]
os.makedirs('p',exist_ok=True)
st=[]
with Rend() as r:
    for i,(t,on) in enumerate([(46.0,0),(73.4,1),(89.6,2)]):
        f=f'p/s{i}.png'; r.png(slide('01 · Classificazione delle fibre','Classificazione delle fibre',cards,on=on,kw=['Fibra tessile','Filatura','Feltro','Origine'],pag=3),f); st.append((t,f))
print(prof_clip(SRC,keep,st,'p/proto.mp4','x',gain_db=-2.3))
