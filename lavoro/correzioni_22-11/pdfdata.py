# -*- coding: utf-8 -*-
import re, subprocess, json
PDF='/home/work/l17/slide/LEZIONE 17.pdf'
PAG={1:2,2:4,3:5,4:7,5:9,6:10,7:13,8:16}
def page_text(p): return subprocess.run(['pdftotext','-f',str(p),'-l',str(p),'-layout',PDF,'-'],capture_output=True,text=True).stdout
def paras(p):
    t=page_text(p).split('\n');t=[l.strip() for l in t]
    title=t[0] if t and t[0] else ''
    # primo blocco non vuoto = titolo (puo' essere su 1 riga)
    i=0
    while i<len(t) and not t[i]:i+=1
    title=t[i];i+=1
    out=[];cur=[]
    for l in t[i:]:
        if l: cur.append(l)
        elif cur: out.append(' '.join(cur));cur=[]
    if cur: out.append(' '.join(cur))
    return title,out
def sentences(par):
    """paragrafo -> frasi intere. La parte in grassetto (fino ai due punti) resta con la prima frase."""
    m=re.match(r'^([^:]{3,70}):\s+(.*)$',par)
    lead,body=(m.group(1),m.group(2)) if m else ('',par)
    parts=re.split(r'(?<=[a-zàèéìòù0-9\)\"”])\.\s+(?=[A-ZÀÈÉÌÒÙ])',body)
    parts=[x.strip() for x in parts if x.strip()]
    parts=[x if x.endswith(('.','!','?','”','"')) else x+'.' for x in parts]
    cards=[]
    for k,s in enumerate(parts): cards.append(dict(lead=lead if k==0 else '',text=s,par=0))
    return cards
def topic_cards(n):
    title,ps=paras(PAG[n]);out=[]
    for pi,p in enumerate(ps):
        for c in sentences(p): c['par']=pi;out.append(c)
    return title,out
if __name__=='__main__':
    D={}
    for n in PAG:
        t,c=topic_cards(n);D[n]=dict(title=t,cards=c)
        print(n,t,len(c),[len(x['text'])+len(x['lead']) for x in c])
    json.dump(D,open('/home/work/build/cards.json','w'),ensure_ascii=False,indent=1)
