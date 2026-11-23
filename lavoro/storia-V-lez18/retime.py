import json,re,unicodedata,difflib,sys
W='/home/user/work18'
SEG=json.load(open(W+'/lavoro-storia-V-lez18/trasc18.json'))
def nrm(s):
    s=unicodedata.normalize('NFD',s.lower());s=''.join(c for c in s if unicodedata.category(c)!='Mn')
    return re.sub(r'[^a-z0-9]','',s)
# flusso di caratteri con tempi
CH=[];TM=[]
for s in SEG:
    for t,p in s['parole']:
        for c in nrm(p):CH.append(c);TM.append(t)
STR=''.join(CH)
tot=0;shift=[]
for n in range(1,7):
    d=json.load(open(f'{W}/cards_orig/arg{n}.json'))
    for w in d['finestre']:
        prev=w['t0']
        for k,c in enumerate(w['card']):
            t=c['t'];cs=nrm(c['testo'])
            i0=next((i for i,x in enumerate(TM) if x>=t-4),0);i1=next((i for i,x in enumerate(TM) if x>=t+35),len(TM))
            S=STR[i0:i1];sm=difflib.SequenceMatcher(None,S,cs,autojunk=False)
            # miglior blocco: il primo blocco lungo (>=10 lettere) della card
            blocks=[b for b in sm.get_matching_blocks() if b.size>=10]
            if blocks:
                b=blocks[0];tt=TM[i0+b.a]-min(b.b,60)*0.068
            else:tt=t
            new=max(t,round(tt-0.25,2))
            hi=w['t1']-1.5
            new=min(new,hi) if hi>t else t
            if new-t>1.0:shift.append((n,t,round(new-t,1),c['testo'][:50]))
            else:new=t
            c['t']=round(max(new,prev+0.0),2);prev=c['t']
    json.dump(d,open(f'{W}/cards/arg{n}.json','w'),ensure_ascii=False,indent=1)
print(len(shift));[print(x) for x in shift[:45]]
