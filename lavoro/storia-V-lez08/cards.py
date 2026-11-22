#!/usr/bin/env python3
# Sezioni e card (frasi intere) dalle slide del prof -> cards.json ; titolo = prima riga di ogni pagina con titolo
import subprocess, json, re
P='/tmp/w/mat/sl/LEZIONE 8.pdf'
secs=[]
for pg in range(2,17):
    t=subprocess.run(['pdftotext','-f',str(pg),'-l',str(pg),P,'-'],capture_output=True,text=True).stdout
    L=[l.strip() for l in t.split('\n') if l.strip()]
    if not L: continue
    if ': ' not in L[0][:110] and not L[0].startswith('La convergenza'):
        cur={'titolo':L[0],'cards':[],'pagine':[pg]}; secs.append(cur); L=L[1:]
    else: cur=secs[-1]; cur['pagine'].append(pg)
    buf=''
    for ln in L:
        buf=(buf+' '+ln).strip()
        if buf.endswith('.') :
            cur['cards'].append(re.sub(r'\s+',' ',buf)); buf=''
    if buf: cur['cards'].append(re.sub(r'\s+',' ',buf))
json.dump(secs,open('cards.json','w'),ensure_ascii=False,indent=1)
for s in secs:print(len(s['cards']),s['pagine'],s['titolo'])
