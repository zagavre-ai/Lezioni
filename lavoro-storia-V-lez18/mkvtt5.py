import json,re,sys,os,textwrap
sys.path.insert(0,'/tmp/L18/lib')
W='/tmp/L18'
part=int(sys.argv[1])
SEG=json.load(open(f'{W}/seg_P{part}.json'))
exec(open(W+'/make5.py').read().split("SEG=[];T0=[0.0]")[0].split("DEF={")[0].split("from PIL import Image")[0].replace("from assemble import *","") ) if False else None
TXT={x['nome']:x['testo'] for x in json.load(open(W+'/voci/scambio/storia-V-lez18/testi_voci.json'))}
mk=open(W+'/make5.py').read();i=mk.index("DEF={");j=mk.index("SEG=[];T0=[0.0]")
ST=W+'/st';S=lambda n,x,s:'';IMGp=lambda k:''
ns={'ST':ST,'S':S,'IMGp':IMGp};exec(mk[i:j],ns);DEF=ns['DEF']
start={s['name']:s['start'] for s in SEG}
def tm(pt):
    for k,(a,b,_) in DEF.items():
        if k in start and a<=pt<b:return start[k]+(pt-a),k
    return None,None
COR=[("Grigori Rash Putin","Grigorij Rasputin"),("Rash Putin","Rasputin"),("Bash Putin","Rasputin"),("Putin, consigliere","Rasputin, consigliere"),("Putov","Putilov"),
("Troz\\w+","Trockij"),("Trotski","Trockij"),("Kerensky","Kerenskij"),("Cornilov|Corniloff|Kornilof|Korgov","Kornilov"),("l'ov\\b|Il Vov|il Vov|Boff|VOV|il Vof|L'ov","L'vov"),("Ramanov","Romanov"),("Cronstad","Kronstadt"),("Gresnitovsk","Brest-Litovsk"),("Katterinburg","Ekaterinburg"),
("\\bURS\\b","URSS"),("\\bUrs\\b","URSS"),("lo Zara\\b","lo zar"),("bolsceviche|bolsceviti|bolscevi\\b","bolscevichi"),("\\bCeca\\b","Čeka"),("Pietroburgo, San","San Pietroburgo, San"),("caporetto","Caporetto"),("La scesa di","L'ascesa di"),("sempre quelli","sempre quelli")]
def fix(s):
    s=re.sub(r'\s+',' ',s.strip())
    for a,b in COR:s=re.sub(a,b,s)
    return s
def ts(t):return '%02d:%02d:%06.3f'%(int(t//3600),int(t%3600//60),t%60)
cues=[]
for x in json.load(open('/tmp/w5/trasc5.json')):
    a,b=x['inizio'],x['fine'];na,k=tm(a)
    if na is None:continue
    nb=min(na+(b-a),start[k]+(DEF[k][1]-DEF[k][0]))
    cues.append([na,max(nb,na+0.4),fix(x['testo'])])
def sp(t):return re.split(r'(?<=[.!?])\s+',t)
from align import sentence_times
for s in SEG:
    for tr,p,g in s['aud']:
        n=os.path.basename(p)[:-4]
        if p.startswith(W+'/vn/') and n in TXT:
            c=f'{W}/al_{n}_v.json';ss=sp(TXT[n])
            if os.path.exists(c):t,d=json.load(open(c))
            else:t,d=sentence_times(p,ss);json.dump([t,d],open(c,'w'))
            for (a,b),x in zip(t,ss):cues.append([s['start']+tr+a,s['start']+tr+b,x])
cues=[c for c in cues if len(c[2])>5 and not re.fullmatch(r'(All right|Uh|Um|Mm|Eh|Ehm|Ah|Ok|Okay|Simply|Allora|Bene|Ecco|Quindi|Insomma|Comunque)[.!?,]*',c[2].strip(),re.I)]
cues.sort()
out=['WEBVTT','']
k=0
for a,b,tx in cues:
    ln=textwrap.wrap(tx,44);parts=[ln[i:i+2] for i in range(0,len(ln),2)];d=(b-a)/len(parts)
    for i,pp in enumerate(parts):
        k+=1;out.append(f'{k}\n{ts(a+i*d)} --> {ts(a+(i+1)*d-0.02)}\n'+'\n'.join(pp)+'\n')
open(f'{W}/out/Storia_Lez5_Parte{part}.vtt','w').write('\n'.join(out));print(part,k,'cue')
