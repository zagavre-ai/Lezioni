# Correzioni ai blocchi del PDF: divide un blocco all'inizio di una frase, o unisce un blocco al precedente.
# uso: python3 fix_blocks.py cartella 'split:15:I fili componenti' 'join:58'   (indici dei blocchi ORIGINALI)
import json,sys
D=sys.argv[1];import os
src=D+'/blocks_orig.json'
if not os.path.exists(src):os.rename(D+'/blocks.json',src)
B=json.load(open(src));ops={}
for o in sys.argv[2:]:
    k,i,*r=o.split(':');ops[int(i)]=(k,':'.join(r))
def txt(b):return ''.join(r[1] for r in b['runs'])
def split_at(b,s):
    T=txt(b);k=T.index(s);A=[];C=[];pos=0
    for bo,t in b['runs']:
        a,e=pos,pos+len(t);pos=e
        if e<=k:A.append([bo,t])
        elif a>=k:C.append([bo,t])
        else:A.append([bo,t[:k-a]]);C.append([bo,t[k-a:]])
    A[-1][1]=A[-1][1].rstrip();return dict(b,runs=A),dict(b,runs=C)
out=[]
for i,b in enumerate(B):
    if i in ops and ops[i][0]=='split':x,y=split_at(b,ops[i][1]);out+=[x,y];print('split',i,'→',len(out)-2,len(out)-1)
    elif i in ops and ops[i][0]=='join':out[-1]=dict(out[-1],runs=out[-1]['runs']+[[False,' ']]+b['runs']);print('join',i)
    else:out.append(b)
json.dump(out,open(D+'/blocks.json','w'),ensure_ascii=False);print(len(out),'blocchi')
