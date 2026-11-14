# Stima i tempi delle pagine del PDF (PG) in proporzione al testo, per align.py, e allarga le finestre di ricerca.
# uso: python3 stima_pagine.py cartella
import json,sys,re
D=sys.argv[1].rstrip('/')+'/'
U=json.load(open(D+'units.json'));W=[w for l in open(D+'pk.jsonl') for w in json.loads(l)['w']]
T0,T1=W[0][0],W[-1][0];np_=max(u['pg'] for u in U)+1
ch=[0]*(np_+1)
for u in U:ch[u['pg']]+=len(u['txt'])
tot=sum(ch);PG=[0];c=0
for p in range(1,np_+1):
    c+=ch[p];PG.append(round(T0+(T1-T0)*c/tot))
PG[0]=0;PG=PG[:np_+1]
s=open(D+'align.py').read()
s=re.sub(r'^PG=\[.*?\]$','PG='+json.dumps(PG),s,flags=re.M)
s=s.replace("lo=pstart(p)-40; hi=pend(p)+60","lo=pstart(p)-420; hi=pend(p)+420")
open(D+'align.py','w').write(s);print(len(PG),'pagine',PG[:6],'…',PG[-3:])

# align_s.py: finestre delle pagine dai tempi reali dell'allineamento (align.json)
if len(sys.argv)>2 and sys.argv[2]=='s':
    A=json.load(open(D+'align.json'));A=A['align'] if isinstance(A,dict) and 'align' in A else A
    st={};en={}
    for a in A:
        p=U[a['i']]['pg'];st[p]=min(st.get(p,1e9),a['first']);en[p]=max(en.get(p,0),a['last'])
    t=open(D+'align_s.py').read()
    t=re.sub(r'^PG=\[.*?\]$','PST='+json.dumps({str(k):v for k,v in st.items()})+'\nPEN='+json.dumps({str(k):v for k,v in en.items()}),t,flags=re.M)
    t=t.replace("def okwin(u,s): p=u['pg']; return PG[p-1]-60<=s['t']<=PG[p]+90","def okwin(u,s): p=str(u['pg']); return PST.get(p,0)-60<=s['t']<=PEN.get(p,1e9)+90")
    open(D+'align_s.py','w').write(t);print('align_s: finestre da align.json',len(st),'pagine')
