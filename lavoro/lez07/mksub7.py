# Sottotitoli della docente (lezione 7) nei tempi del video finale. uso: mksub7.py timeline.json out.vtt
# testo: Whisper base con lingua riconosciuta pezzo per pezzo (italiano o inglese, come parla la docente)
import sys,json,re,subprocess,os
sys.path.insert(0,'/home/claude/w7')
import tl7 as TLM, content7 as C7
tlf,out=sys.argv[1:3]
A=json.load(open('tr7_auto.json'));I=json.load(open('tr7_fine.json'))
def clean(t):
    t=re.sub(r'\[[^\]]*\]|\([^)]*\)','',t)
    w=t.split();o=[]
    for x in w:   # ripetizioni a catena (allucinazioni): massimo 2 volte la stessa parola o coppia
        if len(o)>=2 and x.lower()==o[-1].lower()==o[-2].lower(): continue
        o.append(x)
    t=' '.join(o)
    t=re.sub(r'(\b(?:\w+\s+){1,3}?\w+\b)(?:\s+\1){2,}',r'\1',t)
    return t.strip()
F=json.load(open('subfix.json'))   # correzioni a mano dei pezzi sbagliati (confronto delle tre trascrizioni)
raw=[]
for k,(a,i) in enumerate(zip(A,I)):
    t=a['t'] if a['lang'] in ('it','en') else i['t']
    if str(k) in F: t=F[str(k)]
    t=clean(t)
    if len(t)<3: continue
    raw.append({'s':TLM.tm(a['s']),'e':TLM.tm(a['e']),'t':t})
json.dump(raw,open('sub7_raw.json','w'),ensure_ascii=False)
txt=' '.join(x[0] for a in C7.ARG for s in a['slides'] for x in s['items'])+' '+' '.join(t for t,_ in C7.INTRO+C7.CHIUSURA)
open('d.txt','w').write('')   # niente correzione automatica: i pezzi sono già corretti a mano
r=subprocess.run(['python3','/home/claude/tools/mkvtt.py','sub7_raw.json',tlf,'bounds.json','d.txt',out]);sys.exit(r.returncode)
